"""Streamlit display for three SEC EDGAR 10-K investor checklists."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st


SCRIPT = Path(__file__).parent / "buffett-investor" / "scripts" / "buffett_facts.py"
MEMO = Path(__file__).parent / "cost_buffett_memo.md"
MEMOS = {
    "Buffett": MEMO,
    "Cathie Wood": Path(__file__).parent / "cost_cathie_wood_memo.md",
    "Michael Burry": Path(__file__).parent / "cost_michael_burry_memo.md",
}
NUMBER_PATTERN = re.compile(r"(?<![A-Za-z0-9])\$?[0-9][0-9,]*(?:\.\d+)?%?(?!-[A-Za-z])")


def load_script():
    spec = importlib.util.spec_from_file_location("buffett_facts", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


@st.cache_data(show_spinner=False)
def report_for(ticker: str) -> dict:
    return load_script().analyze(ticker)


def normalized_numbers(report: dict) -> set[str]:
    values: set[str] = set()
    for row in report["rows"]:
        for value in row.values():
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                values.add(str(value))
                values.add(f"{value:,.0f}")
                values.add(f"${value:,.0f}")
                values.add(f"{value:.1%}")
    return values


def memo_unprinted_numbers(memo: str, report: dict) -> list[str]:
    known = normalized_numbers(report)
    for checks in report.get("investor_checks", {}).values():
        for label in checks:
            known.update(match.group(0) for match in NUMBER_PATTERN.finditer(label))
    candidates = [match.group(0) for match in NUMBER_PATTERN.finditer(memo)]
    return sorted({value for value in candidates if value not in known})


def result(value: bool | None) -> str:
    return "not known" if value is None else ("pass" if value else "fail")


def verdict(checks: dict[str, bool | None]) -> str:
    if any(value is False for value in checks.values()):
        return "fail"
    if any(value is None for value in checks.values()):
        return "not known"
    return "pass"


def currency(value: int | float | None) -> str:
    return "not found" if value is None else f"${value:,.0f}"


def percentage(value: int | float | None) -> str:
    return "not known" if value is None else f"{value:.1%}"


def reported_values(rows: list[dict], label: str, formatter) -> str:
    return "; ".join(formatter(row.get(label)) for row in rows)


def checks_text(checks: dict[str, bool | None]) -> str:
    return "\n".join(f"- {label}: {result(value)}" for label, value in checks.items())


def generated_memos(report: dict) -> dict[str, str]:
    """Build non-COST memos solely from the report values shown in the app."""
    rows = report["rows"]
    checks = report["investor_checks"]
    return {
        "Buffett": (
            f"## {verdict(checks['Buffett']).title()}\n\n"
            f"Reported owner earnings, first through latest: {reported_values(rows, 'Owner earnings', currency)}.\n\n"
            f"Reported ROE, first through latest: {reported_values(rows, 'ROE', percentage)}.\n\n"
            f"Buffett checks:\n{checks_text(checks['Buffett'])}"
        ),
        "Cathie Wood": (
            f"## {verdict(checks['Cathie Wood']).title()}\n\n"
            f"Reported revenue, first through latest: {reported_values(rows, 'Revenue', currency)}.\n\n"
            f"Reported operating cash flow, first through latest: {reported_values(rows, 'Operating cash flow', currency)}.\n\n"
            f"Cathie Wood checks:\n{checks_text(checks['Cathie Wood'])}"
        ),
        "Michael Burry": (
            f"## {verdict(checks['Michael Burry']).title()}\n\n"
            f"Reported operating cash flow, first through latest: {reported_values(rows, 'Operating cash flow', currency)}.\n\n"
            f"Reported net income, first through latest: {reported_values(rows, 'Net income', currency)}.\n\n"
            f"Reported liabilities, first through latest: {reported_values(rows, 'Liabilities', currency)}.\n\n"
            f"Reported equity, first through latest: {reported_values(rows, 'Equity', currency)}.\n\n"
            f"Michael Burry checks:\n{checks_text(checks['Michael Burry'])}"
        ),
    }


def show_memos(memos: dict[str, str], report: dict) -> None:
    unsupported_by_memo = {}
    columns = st.columns(3)
    for column, (investor, memo) in zip(columns, memos.items()):
        with column:
            st.markdown(f"### {investor}")
            st.markdown(memo)
            unsupported_by_memo[investor] = memo_unprinted_numbers(memo, report)
    unsupported = {name: values for name, values in unsupported_by_memo.items() if values}
    if unsupported:
        details = "; ".join(f"{name}: {', '.join(values)}" for name, values in unsupported.items())
        st.warning("Unsupported memo numbers (not printed by the script): " + details)
    else:
        st.success("Every number across all three memos was printed by the script.")


def main() -> None:
    st.set_page_config(page_title="Investor panel 10-K checks", layout="wide")
    st.title("Investor panel: SEC EDGAR 10-K checks")
    st.caption("Data from SEC EDGAR; built with AI help, a learning demonstration, not investment advice.")
    ticker = st.text_input("Ticker", value="COST").strip().upper()
    if not ticker:
        return
    try:
        with st.spinner("Downloading SEC EDGAR 10-K facts..."):
            report = report_for(ticker)
    except ValueError as exc:
        st.error(str(exc))
        return

    st.subheader(f"{report['company']} ({report['ticker']})")
    frame = pd.DataFrame(report["rows"])
    chart_data = frame.melt(
        id_vars="fiscal_year_end", value_vars=["Owner earnings", "Net income"],
        var_name="Measure", value_name="USD",
    ).dropna()
    chart = alt.Chart(chart_data).mark_line(point=True).encode(
        x=alt.X("fiscal_year_end:N", title="Fiscal year end"),
        y=alt.Y("USD:Q", title="U.S. dollars", axis=alt.Axis(format="$.2s")),
        color="Measure:N", tooltip=["fiscal_year_end:N", "Measure:N", alt.Tooltip("USD:Q", format=",.0f")],
    ).properties(height=360)
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Reported facts and calculated measures")
    st.dataframe(frame, use_container_width=True, hide_index=True)
    st.subheader("Investor panel checks")
    panel_rows = [
        {"Investor": investor, "Check": label, "Result": result(value)}
        for investor, checks in report["investor_checks"].items()
        for label, value in checks.items()
    ]
    st.dataframe(pd.DataFrame(panel_rows), use_container_width=True, hide_index=True)
    st.subheader("Verdicts")
    st.dataframe(
        pd.DataFrame(
            [{"Investor": investor, "Verdict": verdict(checks)} for investor, checks in report["investor_checks"].items()]
        ),
        use_container_width=True,
        hide_index=True,
    )

    if ticker == "COST":
        st.subheader("Costco investor memos")
        static_memos = {investor: path.read_text(encoding="utf-8") for investor, path in MEMOS.items() if path.exists()}
        show_memos(static_memos, report)
    else:
        st.subheader(f"{report['company']} investor memos")
        show_memos(generated_memos(report), report)


if __name__ == "__main__":
    main()
