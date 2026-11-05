#!/usr/bin/env python3
"""Retrieve five fiscal years of 10-K facts for Buffett-style checks."""

from __future__ import annotations

import argparse
import gzip
import json
import os
import sys
import zlib
from datetime import date
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SEC_HEADERS = {"Accept-Encoding": "gzip, deflate"}
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
FLOW_TAGS = {
    "Revenue": ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"],
    "Net income": ["NetIncomeLoss"],
    "Operating cash flow": ["NetCashProvidedByUsedInOperatingActivities"],
    "Capital spending": [
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "PaymentsToAcquireProductiveAssets",
    ],
}
EQUITY_TAG = "StockholdersEquity"
BALANCE_TAGS = {
    "Liabilities": ["Liabilities"],
    "Current assets": ["AssetsCurrent"],
    "Current liabilities": ["LiabilitiesCurrent"],
}


def user_agent() -> str:
    value = os.environ.get("SEC_USER_AGENT", "").strip()
    if not value:
        raise ValueError("SEC_USER_AGENT is required; set it in your local environment.")
    return value


def get_json(url: str) -> dict:
    headers = {**SEC_HEADERS, "User-Agent": user_agent()}
    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=30) as response:
            payload = response.read()
            encoding = response.headers.get("Content-Encoding", "").lower()
            if "gzip" in encoding:
                payload = gzip.decompress(payload)
            elif "deflate" in encoding:
                payload = zlib.decompress(payload)
            return json.loads(payload.decode("utf-8"))
    except HTTPError as exc:
        raise ValueError(f"SEC EDGAR returned HTTP {exc.code}.") from exc
    except URLError as exc:
        raise ValueError(f"Could not reach SEC EDGAR: {exc.reason}") from exc


def cik_for_ticker(ticker: str) -> int:
    companies = get_json(TICKERS_URL)
    for row in companies.values():
        if row["ticker"].upper() == ticker.upper():
            return int(row["cik_str"])
    raise ValueError(f"Ticker {ticker.upper()} was not found by SEC EDGAR.")


def units_for(facts: dict, tag: str) -> list[dict]:
    return facts.get("facts", {}).get("us-gaap", {}).get(tag, {}).get("units", {}).get("USD", [])


def is_annual_flow(item: dict) -> bool:
    if item.get("form") != "10-K" or item.get("fp") != "FY":
        return False
    if not item.get("start") or not item.get("end") or not item.get("filed"):
        return False
    try:
        days = (date.fromisoformat(item["end"]) - date.fromisoformat(item["start"])).days
    except ValueError:
        return False
    return 300 <= days <= 380


def latest_by_end(items: list[dict]) -> dict[str, dict]:
    latest: dict[str, dict] = {}
    for item in items:
        end = item["end"]
        if end not in latest or (item["filed"], item.get("accn", "")) > (
            latest[end]["filed"], latest[end].get("accn", "")
        ):
            latest[end] = item
    return latest


def select_tagged_flows(facts: dict, tags: list[str]) -> tuple[dict[str, dict], str | None]:
    # A preferred tag is used whenever it has a reported annual value for a period.
    by_end: dict[str, dict] = {}
    for tag in reversed(tags):
        for end, item in latest_by_end([x for x in units_for(facts, tag) if is_annual_flow(x)]).items():
            by_end[end] = {"value": item["val"], "tag": tag, "filed": item["filed"]}
    return by_end, (tags[0] if by_end else None)


def select_equity(facts: dict, ends: list[str]) -> dict[str, dict]:
    return select_tagged_balance(facts, [EQUITY_TAG], ends)


def select_tagged_balance(facts: dict, tags: list[str], ends: list[str]) -> dict[str, dict]:
    """Return the latest reported 10-K instant fact for each requested year."""
    items = []
    for tag in tags:
        items.extend(
            {**item, "tag": tag}
            for item in units_for(facts, tag)
            if item.get("form") == "10-K" and item.get("end") in ends and item.get("filed")
        )
    chosen = latest_by_end(items)
    return {
        end: {"value": item["val"], "tag": item.get("tag", tags[0]), "filed": item["filed"]}
        for end, item in chosen.items()
    }


def display(value: int | float | None) -> str:
    return "not found" if value is None else f"${value:,.0f}"


def check_text(value: bool | None) -> str:
    return "not known" if value is None else ("pass" if value else "fail")


def analyze(ticker: str) -> dict:
    ticker = ticker.upper()
    cik = cik_for_ticker(ticker)
    facts = get_json(FACTS_URL.format(cik=cik))
    selected = {label: select_tagged_flows(facts, tags)[0] for label, tags in FLOW_TAGS.items()}
    all_ends = sorted({end for metric in selected.values() for end in metric})[-5:]
    if len(all_ends) < 5:
        raise ValueError("SEC EDGAR did not provide five fiscal-year 10-K periods for these checks.")
    equity = select_equity(facts, all_ends)
    balance = {
        label: select_tagged_balance(facts, tags, all_ends)
        for label, tags in BALANCE_TAGS.items()
    }
    rows = []
    for end in all_ends:
        row = {"fiscal_year_end": end}
        for label, metric in selected.items():
            entry = metric.get(end)
            row[label] = None if entry is None else entry["value"]
            row[f"{label} tag"] = None if entry is None else entry["tag"]
        entry = equity.get(end)
        row["Equity"] = None if entry is None else entry["value"]
        row["Equity tag"] = None if entry is None else entry["tag"]
        for label, metric in balance.items():
            entry = metric.get(end)
            row[label] = None if entry is None else entry["value"]
            row[f"{label} tag"] = None if entry is None else entry["tag"]
        cfo, capex, income, eq = (row["Operating cash flow"], row["Capital spending"], row["Net income"], row["Equity"])
        row["Owner earnings"] = None if cfo is None or capex is None else cfo - capex
        row["Owner earnings tag"] = None if row["Owner earnings"] is None else "OCF minus capital spending"
        row["ROE"] = None if income is None or eq is None or eq <= 0 else income / eq
        rows.append(row)
    roe_values = [row["ROE"] for row in rows]
    owner_values = [row["Owner earnings"] for row in rows]
    checks = {
        "ROE is at least 15% every year": None if any(x is None for x in roe_values) else all(x >= .15 for x in roe_values),
        "Owner earnings are positive every year": None if any(x is None for x in owner_values) else all(x > 0 for x in owner_values),
        "Owner earnings grew from the first year to the last year": None if any(x is None for x in owner_values) else owner_values[-1] > owner_values[0],
    }
    revenue_values = [row["Revenue"] for row in rows]
    cfo_values = [row["Operating cash flow"] for row in rows]
    liability, latest_equity = rows[-1]["Liabilities"], rows[-1]["Equity"]
    revenue_increases = [
        later > earlier for earlier, later in zip(revenue_values, revenue_values[1:])
    ]
    cathie_checks = {
        "Revenue grew from the first year to the last year": None if any(x is None for x in revenue_values) else revenue_values[-1] > revenue_values[0],
        "Revenue increased in at least 3 of 4 year-over-year comparisons": None if any(x is None for x in revenue_values) else sum(revenue_increases) >= 3,
        "Operating cash flow is positive every year": None if any(x is None for x in cfo_values) else all(x > 0 for x in cfo_values),
    }
    burry_checks = {
        "Operating cash flow is at least net income every year": None if any(row["Operating cash flow"] is None or row["Net income"] is None for row in rows) else all(row["Operating cash flow"] >= row["Net income"] for row in rows),
        "Liabilities are no more than twice equity in the latest year": None if liability is None or latest_equity is None or latest_equity <= 0 else liability <= 2 * latest_equity,
    }
    return {
        "ticker": ticker,
        "company": facts.get("entityName", ticker),
        "rows": rows,
        "checks": checks,
        "investor_checks": {"Buffett": checks, "Cathie Wood": cathie_checks, "Michael Burry": burry_checks},
    }


def print_report(report: dict) -> None:
    print(f"{report['company']} ({report['ticker']}) — SEC EDGAR 10-K facts")
    for row in report["rows"]:
        print(f"\nFiscal year end: {row['fiscal_year_end']}")
        for label in ["Revenue", "Net income", "Operating cash flow", "Capital spending", "Equity", "Liabilities", "Current assets", "Current liabilities", "Owner earnings"]:
            tag = row.get(f"{label} tag") or "not found"
            print(f"  {label}: {display(row[label])} [{tag}]")
        roe = "not known" if row["ROE"] is None else f"{row['ROE']:.1%}"
        print(f"  ROE: {roe}")
    print("\nBuffett checks:")
    for label, value in report["checks"].items():
        print(f"  {label}: {check_text(value)}")
    for investor in ["Cathie Wood", "Michael Burry"]:
        print(f"\n{investor} checks:")
        for label, value in report["investor_checks"][investor].items():
            print(f"  {label}: {check_text(value)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ticker")
    parser.add_argument("--json", action="store_true", help="print machine-readable report")
    args = parser.parse_args()
    try:
        report = analyze(args.ticker)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)


if __name__ == "__main__":
    main()
