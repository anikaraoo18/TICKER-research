# Lab 17 Notes

## BAA10YM data card

- **Source:** FRED, Federal Reserve Bank of St. Louis
- **Link:** <https://fred.stlouisfed.org/series/BAA10YM>
- **What it measures:** The monthly spread between Moody's Baa corporate-bond
  yield and the 10-year Treasury yield.
- **Units:** Percent, not seasonally adjusted.
- **Frequency:** Monthly.
- **Publication timing observed in the app:** As of September 30, 2026, the
  newest available observation was August 2026; September 2026 became
  available by October 29, 2026.
- **Revision evidence observed in the app:** Zero revised values on shared
  dates in this comparison.
- **Download date:** October 29, 2026.
- **Three FRED values checked against the app:** July 2026: 1.59%; August
  2026: 1.64%; September 2026: 1.48%.
- **Limitation:** This is a historical data check, not a forecast or investment
  recommendation.

## Initial Project 2 call

- **Decision:** Quarantine BAA10YM for now.
- **Reason:** It is relevant to VCIT, but the September value was not available
  by a September 30 decision date. It may only be used with an as-of date that
  reflects what was actually published at each decision point.
- **What would change the decision:** An implemented Project 2 process that
  consistently uses as-of vintages and documents the timing of each portfolio
  decision.

## Code explanation with partner

I opened the function containing `alfredgraph.csv` in `asof_app.py` and
explained it line by line to my partner: it builds an ALFRED URL with the
selected vintage date, downloads the CSV, treats `.` as missing data, and
returns the values available as of that date.

My partner asked what happens if a FRED series ID is unknown. I answered that
the app catches the error and shows an error for that one series while allowing
the other selected series to continue working.

## Partner attack: revisions

My partner trusted revisions least. I responded: the app showed zero revised
values on shared dates for BAA10YM when comparing September 30, 2026 with
today, but FRED states that all data are subject to revision. Therefore,
Project 2 should continue to use ALFRED as-of vintages instead of assuming
today's historical values always equal the values known on a decision date.

## Final Project 2 call and reflection

BAA10YM remains Quarantined for Project 2. It is relevant to VCIT, but on
September 30, 2026 the newest available observation was August 2026 at 1.64%;
September's 1.48% was available only later. The series could be admitted only
in a process that consistently uses the ALFRED as-of value available at every
decision date.

A backtest using today's values would overstate what was known at the time by
using September's value before it was published.
