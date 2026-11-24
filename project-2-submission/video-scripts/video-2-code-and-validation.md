# Video 2 — Code and Validation

- **Maximum duration:** 5:00
- **Recording date:** ____________________
- **Duration:** ____________________
- **Video filename / YouTube URL:** https://youtu.be/NLVmMIjTx7k
- **Transcript filename:** YouTube automatic captions/transcript available at the video URL; not separately exported.
- **Captions confirmed:** Available through YouTube automatic captions; not independently corrected.

## 0:00–0:40 — Reproducibility entry point

**Say this:** “Codex helped organize code and documentation, but I selected
the inputs and scenarios, made the decision, and remain responsible for this
analysis. This is educational analysis, not investment advice. The README is
the reproducibility entry point. It identifies the Meridian investment
committee as the decision user, gives fresh-environment setup steps, and runs
the Streamlit app with one command. The independent README-only cold run by my
partner was completed and documented; it confirmed the README commands worked
in the reported environment, without validating investment results or
authorizing a trade.”

**Recording instruction:** Keep your webcam visibly on screen throughout.

**Show this:** `README.md`, including setup, run command, and the explicit
cold-run limitation, then `docs/partner-cold-run.md`.

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

## 2:40–3:25 — Lab 20 objective validation

**Say this:** “The Lab 20 script reuses the copied estimator and grid-search
function. With the same all-60-month SGOV, VGIT, VCIT, and VTI data, 5-point
long-only grid, 3% reserve minimum, and SGOV/VGIT reserve eligibility, it
changes only the objective from 6.50% to 7.00%. The result moves from 65% SGOV
and 35% VTI to 60% SGOV and 40% VTI. Expected return rises from 6.62% to
7.03%, volatility from 5.64% to 6.42%, and reserve-eligible weight from 65%
to 60%; the largest allocation change is 5 percentage points.”

**Show this:** `portfolio/run_lab20_objective_test.py` and
`docs/lab-20-objective-test-result.md`.

**Add while showing the app:** “The adoption-gate dashboard and allocation
chart display these already documented results. They do not silently rerun the
model or create a new forecast.”

## 3:25–4:05 — Downside validation and failure mode

**Say this:** “The downside script preserves the 60-month estimates except for
VTI’s annual expected return, which is overridden to negative 25%. It
subtracts 0.25 percentage points of annual implementation cost from every
candidate’s gross expected return. The qualification rule requires at least
6.50% net return and 3.00% reserve eligibility. No candidate qualified, so the
stop condition triggered.”

**Show this:** `portfolio/run_downside_stress_test.py`,
`docs/stress-test-plan.md`, and
`docs/stress-test-execution-result.md`.

## 4:05–5:00 — Integrity and validation evidence

**Say this:** “The changed-input record and stress plan each have matching
before-and-after SHA-256 checks in their execution records. The Lab 20
prediction lock also has matching before-and-after SHA-256 checks. The
validation evidence includes the completed partner cold run and the partner
code explanation: the script requires the CSV header order to match SGOV,
VGIT, VCIT, and VTI exactly, so it raises an error rather than silently
misaligning calculations if the same tickers appear in another order.”

**Show this:** `docs/validation-and-ai-use.md`, including completed checks
and `docs/lab-20-partner-explanation.md`.
