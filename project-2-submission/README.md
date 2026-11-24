# Project 2 — Portfolio Analysis

**AI use and ownership:** Codex helped organize code and documentation. I
selected the inputs and scenarios, made the decisions, and remain responsible
for this analysis.

**Educational analysis, not investment advice.** This project does not
authorize or execute any trade.

This is a portfolio-analysis system for the Meridian investment committee. The
current decision is **do not allocate or rebalance yet**.

## Decision context

- **Intended user and committee ask:** Meridian's investment committee must
  decide whether to adopt, allocate to, rebalance, pilot, or reject this
  classroom process. The present ask is to keep it in analysis and defer any
  allocation.
- **Horizon and cadence:** Seven-year policy horizon, reviewed quarterly;
  annual rebalancing would be considered only after the unresolved controls are
  defined and tested.
- **Mandate:** CPI plus 4% net over rolling five-year periods, compared with a
  60/40 policy benchmark, with a $3 million cash/daily-liquid-government
  reserve concept and a 10% calendar-year-loss rule whose enforcement remains
  unresolved.
- **Scope boundary:** Project 2 is a separate investment-management exercise.
  It does not revise Project 1's preserved Edition A or later Project 1 work.

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

Run the reproducible known-answer and integrity checks:

~~~sh
python3 -m unittest discover -s project-2-submission/tests -v
~~~

A separate-person README-only cold run was completed by Lili Alderink in a
newly downloaded Windows copy using Python 3.11.9. The app was visible; the
record, commands, timing, and evidence limits are in
[docs/partner-cold-run.md](docs/partner-cold-run.md).

## Repository map

- `portfolio/app.py` — interactive educational portfolio explorer and
  Project 2 decision summary, including a committee adoption-gate dashboard
  and a chart of the already documented allocation changes.
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

The model transforms oldest-first monthly adjusted prices into simple monthly
returns (later price / earlier price - 1), annualizes the arithmetic mean by
multiplying by 12, and annualizes sample volatility by multiplying monthly
standard deviation by the square root of 12. No personal, credentialed, or
private data is used. Digrin data is retained only as a cited classroom
snapshot; this project does not claim redistribution rights or a vendor
revision guarantee.

## Key limitations

- Historical estimates are not forecasts.
- The app uses a 6.50% annual return hurdle, a 3.00% reserve minimum, and a
  long-only grid search. Its normal-case historical-return output is not
  separately cost-adjusted; the 0.25-percentage-point cost deduction appears
  only in the documented downside stress test. The app does not certify the
  $3 million distribution reserve because
  portfolio value is unknown; issuer cap; turnover; five-business-day
  liquidity; no-derivatives/no-borrowing implementation controls; or the
  unresolved 10% calendar-year loss-rule definition.
- The Lab 14 four-sleeve Benchmark and Equal-weight results are comparative
  classroom baselines, not allocations in the active SGOV/VGIT/VCIT/VTI ETF
  universe.
- The allocation changes materially when the historical lookback changes, and
  the locked downside stress test produced no qualifying portfolio.
- The committee adoption-gate dashboard is intentionally a decision aid, not
  a score, forecast, or additional optimizer. It visualizes existing evidence
  so the committee can distinguish a base-case mechanical pass from adoption
  readiness.
