# Project 2 — Portfolio Analysis

An in-progress educational portfolio-analysis project for the Meridian
investment committee. The current decision is **do not allocate or rebalance
yet**. This is educational analysis, not investment advice; it does not
authorize or execute any trade.

## Fresh-environment setup and run

From the repository root, use Python 3 to create and activate a virtual
environment, then install the documented dependency:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r project-2-submission/requirements.txt
```

Run the app:

```sh
streamlit run project-2-submission/portfolio/app.py
```

No independent README-only cold run by another person is recorded yet.

## Repository map

- `portfolio/app.py` — interactive educational portfolio explorer and
  Project 2 decision summary.
- `portfolio/portfolio.py` — copied CSV-estimation and long-only grid-search
  logic.
- `portfolio/prices.csv` and `portfolio/universe.md` — saved active
  SGOV/VGIT/VCIT/VTI price snapshot and source documentation.
- `portfolio/run_lookback_test.py` and
  `docs/changed-input-execution-result.md` — locked lookback sensitivity
  test and result.
- `portfolio/run_downside_stress_test.py`,
  `docs/stress-test-plan.md`, and
  `docs/stress-test-execution-result.md` — locked downside stress test and
  result.
- `docs/decision-memo.md`, `docs/point-in-time-data-card.md`, and
  `docs/validation-and-ai-use.md` — current decision, provenance, and
  validation records.

## Data source and provenance limits

The active universe is SGOV, VGIT, VCIT, and VTI. The saved CSV contains
monthly Digrin displayed **Adjusted** prices, not Real prices, for October 2021
through September 2026; the documented retrieval date is October 22, 2026.
The repository preserves the saved snapshot but does not prove that the
vendor's historical values were unrevised on every prior date. BAA10YM is
quarantined and is not a decision input.

## Key limitations

- Historical estimates are not forecasts.
- The app models a 6.50% net objective, 3.00% reserve minimum, and long-only
  grid search, but does not certify the $3 million distribution reserve because
  portfolio value is unknown; issuer cap; turnover; five-business-day
  liquidity; no-derivatives/no-borrowing implementation controls; or the
  unresolved 10% calendar-year loss-rule definition.
- The allocation changes materially when the historical lookback changes, and
  the locked downside stress test produced no qualifying portfolio.
