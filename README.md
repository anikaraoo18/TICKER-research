# Project 1 — Apple Equity Research

## Decision

This project analyzes Apple Inc. (`AAPL`) for an equity-research analyst. The
intended user is an investment committee deciding whether to **initiate**,
**watch/defer**, or **not initiate** a position. The current working conclusion
is **Watch/Defer**. It is a coursework draft, not investment advice.

## Setup and run

Python 3 is required. From the repository root, run the existing models:

```sh
python3 dcf.py
python3 AAPL-research/lab-08/aapl_pe.py
python3 AAPL-research/lab-10/aapl_proforma.py
python3 AAPL-research/lab-11/aapl_proforma_sensitivity.py
```

The relevant Apple scripts use only the Python standard library. No third-party
Python packages are required; see `requirements.txt`.

## Repository map

- `AAPL_Lab_06_input_table.md` — Apple DCF inputs, checks, and reported Lab 06 results.
- `dcf.py` — five-year FCFF DCF, sensitivity grid, and reverse-DCF check.
- `AAPL-research/lab-07/AAPL_Lab_07_comps_calculations.md` — comparable-company calculations.
- `AAPL-research/lab-08/aapl_pe.py` — two-peer P/E calculation.
- `AAPL-research/lab-08/lab08_aapl_sources.md` — P/E inputs, sources, and interpretation.
- `AAPL-research/lab-10/aapl_proforma.py` — FY2026–FY2030 three-statement pro forma and FCFE valuation.
- `AAPL-research/lab-10/aapl_lab10_assumptions.md` — pro-forma sources and assumptions.
- `AAPL-research/lab-10/aapl_lab10_results.md` — reported Lab 10 output.
- `AAPL-research/lab-11/aapl_proforma_sensitivity.py` — one-at-a-time sensitivity analysis.
- `AAPL-research/lab-11/aapl_lab11_notes.md` — Locked Changed-Input Record and sensitivity results.
- `AAPL-research/lab-12/aapl_lab12_review.md` — presentation/review evidence and next research priorities.
- `docs/` — Project 1 draft documentation and completion records.

## Data sources

Existing Apple work cites Apple’s FY2025 Form 10-K and other SEC filings,
historical-price records from Yahoo Finance or other identified price sources,
and peer-company filings. Use the source locators in the Lab 06, Lab 07, Lab
08, and Lab 10 files rather than treating this README as a replacement for
source documentation.

## Known limitations

- The Lab 06 starting FCFF is a CFO-less-capex proxy, not a fully reconciled FCFF measure.
- Lab 06 treats reported cash as a preliminary non-operating-cash proxy; the operating-cash policy needs support.
- P/E analyses use different peer sets and have business-model and fiscal-year timing differences; Lab 07 does not force EV/EBITDA.
- Lab 10 holds several inputs constant or uses simplifying judgments, including debt, marketable securities, diluted shares, cost of equity, and terminal growth.
- Lab 11 sensitivity rankings apply only to the stated input ranges; its review identifies an unmodeled Services downside case.
- Existing valuation outputs use different stated market-observation dates, so they should not be combined into a final valuation range without further reconciliation.
