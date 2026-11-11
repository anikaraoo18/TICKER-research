# Video 2 — Code and Validation

- **Maximum duration:** 5:00
- **Recording date:** ____________________
- **Duration:** ____________________
- **Video filename / YouTube URL:** ____________________
- **Transcript filename:** ____________________
- **Captions confirmed:** ____________________

## 0:00–0:40 — Reproducibility entry point

**Say this:** “The README is the reproducibility entry point. It identifies the
Meridian investment committee as the decision user, gives fresh-environment
setup steps, and runs the Streamlit app with one command. The independent
README-only cold run by another person is still pending.”

**Show this:** `README.md`, including setup, run command, and the explicit
cold-run limitation.

## 0:40–1:40 — Data flow and portfolio logic

**Say this:** “The app imports the copied portfolio logic. The CSV estimator
validates an oldest-first monthly price file, estimates annual expected
returns, volatilities, and correlations, and the grid search evaluates
long-only mixes in 5-percentage-point steps. For the active uploaded ETF CSV,
SGOV and VGIT are the default reserve-eligible assets.”

**Show this:** Imports and upload/reserve-eligibility sections in
`portfolio/app.py`; then `estimate_annual_inputs_from_csv` and
`find_lowest_volatility_mix` in `portfolio/portfolio.py`.

## 1:40–2:40 — Locked changed-input validation

**Say this:** “The lookback test reuses the copied CSV estimator and grid-search
function. It holds the 6.5% objective, 3% reserve minimum, and SGOV/VGIT
reserve eligibility fixed while changing only all 60 monthly observations to
the most recent 36. The prediction of higher SGOV and lower VTI was supported,
with a 20-percentage-point largest allocation change.”

**Show this:** `portfolio/run_lookback_test.py`,
`docs/locked-changed-input-record.md`, and
`docs/changed-input-execution-result.md`.

## 2:40–3:45 — Downside validation and failure mode

**Say this:** “The downside script preserves the 60-month estimates except for
VTI’s annual expected return, which is overridden to negative 25%. It
subtracts 0.25 percentage points of annual implementation cost from every
candidate’s gross expected return. The qualification rule requires at least
6.50% net return and 3.00% reserve eligibility. No candidate qualified, so the
stop condition triggered.”

**Show this:** `portfolio/run_downside_stress_test.py`,
`docs/stress-test-plan.md`, and
`docs/stress-test-execution-result.md`.

## 3:45–5:00 — Integrity and remaining work

**Say this:** “The changed-input record and stress plan each have matching
before-and-after SHA-256 checks in their execution records. The validation
record also notes that the locked changed-input record has no pre-execution Git
commit hash; none is added later. Remaining work is the independent cold run
and final consistency review across submission artifacts.”

**Show this:** `docs/validation-and-ai-use.md`, including completed checks
and remaining validation work.
