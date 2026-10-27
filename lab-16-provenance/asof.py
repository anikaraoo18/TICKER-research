"""Show the information that was knowable on a decision date.

Edit DECISION_DATE and ROWS to use another training table.  This script uses
only the Python standard library.
"""

from collections import defaultdict
from datetime import date


# Editable inputs
DECISION_DATE = date.fromisoformat("2026-03-31")
ROWS = [
    {"row": 1, "ticker": "AAA", "month": "2026-01", "published_on": "2026-02-10", "index": 101.0},
    {"row": 2, "ticker": "AAA", "month": "2026-02", "published_on": "2026-03-10", "index": 104.0},
    {"row": 3, "ticker": "AAA", "month": "2026-03", "published_on": "2026-04-10", "index": 109.0},
    {"row": 4, "ticker": "AAA", "month": "2026-02", "published_on": "2026-03-25", "index": 103.0},
    {"row": 5, "ticker": "BBB", "month": "2026-01", "published_on": "2026-02-10", "index": 98.0},
    {"row": 6, "ticker": "BBB", "month": "2026-02", "published_on": "2026-03-10", "index": 97.0},
    {"row": 7, "ticker": "BBB", "month": "2026-02", "published_on": "2026-03-10", "index": 97.0},
    {"row": 8, "ticker": "BBB", "month": "2026-03", "published_on": "2026-04-10", "index": 92.0},
    {"row": 9, "ticker": "CCC", "month": "2026-01", "published_on": "2026-02-10", "index": 110.0},
    {"row": 10, "ticker": "CCC", "month": "2026-02", "published_on": "2026-04-05", "index": 112.0},
    {"row": 11, "ticker": "", "month": "2026-02", "published_on": "2026-03-10", "index": 99.0},
    {"row": 12, "ticker": "CCC", "month": "2026-02", "published_on": "2026-03-10", "index": 111.0},
]


def show_funnel(rule: str, removed: list[dict]) -> None:
    """Print one ordered filtering step and its source-row numbers."""
    row_numbers = [row["row"] for row in removed]
    print(f"{rule}: removed {len(removed)} row(s): {row_numbers}")


def remove_missing_tickers(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    removed = [row for row in rows if not row["ticker"].strip()]
    return [row for row in rows if row not in removed], removed


def remove_exact_duplicates(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """Keep the first row with identical data, excluding its source row number."""
    seen = set()
    kept, removed = [], []
    for row in rows:
        key = (row["ticker"], row["month"], row["published_on"], row["index"])
        if key in seen:
            removed.append(row)
        else:
            seen.add(key)
            kept.append(row)
    return kept, removed


def remove_late_publications(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    removed = [row for row in rows if date.fromisoformat(row["published_on"]) > DECISION_DATE]
    return [row for row in rows if row not in removed], removed


def keep_latest_revision(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """For each ticker-month, retain the latest publication available in rows."""
    latest = {}
    for row in rows:
        key = (row["ticker"], row["month"])
        if key not in latest or row["published_on"] > latest[key]["published_on"]:
            latest[key] = row
    kept = [row for row in rows if latest[(row["ticker"], row["month"])] is row]
    return kept, [row for row in rows if row not in kept]


def print_panel(title: str, rows: list[dict]) -> None:
    print(f"\n{title}")
    print("Row  Ticker  Month measured  Published on  Index")
    for row in sorted(rows, key=lambda item: item["row"]):
        print(
            f'{row["row"]:>3}  {row["ticker"]:<6}  {row["month"]:<14}  '
            f'{row["published_on"]:<12}  {row["index"]:.1f}'
        )


def print_signals(title: str, rows: list[dict]) -> None:
    """Print each ticker's latest month-over-month index change."""
    print(f"\n{title}")
    by_ticker = defaultdict(list)
    for row in rows:
        by_ticker[row["ticker"]].append(row)

    for ticker in sorted(by_ticker):
        history = sorted(by_ticker[ticker], key=lambda row: row["month"])
        if len(history) < 2:
            print(f"{ticker}: insufficient monthly history")
            continue
        previous, latest = history[-2:]
        change = (latest["index"] / previous["index"] - 1) * 100
        print(
            f'{ticker}: {change:+.2f}% through {latest["month"]} '
            f'(from {previous["index"]:.1f} to {latest["index"]:.1f})'
        )


def main() -> None:
    print(f"Decision date: {DECISION_DATE.isoformat()}")
    print(f"Starting rows: {len(ROWS)}")

    panel, removed = remove_missing_tickers(ROWS)
    show_funnel("1. No ticker", removed)

    panel, removed = remove_exact_duplicates(panel)
    show_funnel("2. Exact duplicate", removed)

    eligible_before_cutoff = panel
    panel, removed = remove_late_publications(panel)
    show_funnel("3. Published after decision date", removed)

    panel, removed = keep_latest_revision(panel)
    show_funnel("4. Superseded revision", removed)
    print_panel("As-of panel", panel)
    print_signals("As-of signals", panel)

    # The comparison keeps all valid, nonduplicate rows but deliberately does
    # not apply the publication-date cutoff before choosing each latest revision.
    naive_panel, _ = keep_latest_revision(eligible_before_cutoff)
    print_signals("Naive signals (ignoring publication date)", naive_panel)


if __name__ == "__main__":
    main()
