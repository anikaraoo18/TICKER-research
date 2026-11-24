# Project 2 — Validation and AI-Use Record

## Reproducibility

From the repository root, the README run command is:

```sh
streamlit run project-2-submission/portfolio/app.py
```

The app accepts an uploaded monthly adjusted-price CSV. The included CSV is the
documented SGOV/VGIT/VCIT/VTI classroom universe.

Separate-person README-only cold-run evidence is recorded in
[`partner-cold-run.md`](partner-cold-run.md).

## Completed checks

- Syntax checks passed for the copied portfolio app and logic.
- Import checks passed for Streamlit and the local copied `portfolio` module.
- The app launched successfully after the decision-summary update and was then
  stopped after the launch check.
- Lili Alderink completed a README-only cold run in a newly downloaded
  repository copy on Windows with Python 3.11.9. The app was visible; see
  [`partner-cold-run.md`](partner-cold-run.md) for the reported commands,
  timing, and evidence limits.
- After review, the Project 2 interface default reserve eligibility for an
  uploaded SGOV/VGIT/VCIT/VTI CSV was corrected from the prior BIL/IEF default
  to SGOV and VGIT. This interface correction did not change portfolio math,
  prices, test scripts, locked records, or preserved execution inputs/results.
- The locked changed-input record remained unchanged before and after its
  execution: both checks reported SHA-256
  `c60f63862fb84c8c65adacaeabf1325171be3ba387c301fbeb78c858dfce8953`.
- The locked stress-test plan remained unchanged before and after its
  execution: both checks reported SHA-256
  `bce879eddb1d7edccdcdd40a09878a26b5cf9e3fe7c1656adca3b1e078d2bd28`.
- The locked changed-input record does not contain a pre-execution Git commit
  hash. No hash is added or claimed here.
- Lab 20 supplies the completed commit-before-execution changed-input record:
  lab-20-prediction.md was committed in 604a50e before the objective test, and
  lab-20-objective-test-result.md was committed in 8ff296c. Its prediction,
  old/new values, expected and actual direction, and unchanged decision effect
  are recorded there.
- Whitespace checks passed for the Project 2 files created so far.
- The committee adoption-gate dashboard and allocation-stability chart display
  documented Project 2 evidence only; they do not create a new optimization,
  modify a locked record, or add a forecast.

## Test results

### Locked changed-input test

The all-60-month result was 65.00% SGOV, 0.00% VGIT, 0.00% VCIT, and 35.00%
VTI, with 6.62% expected return, 5.64% estimated volatility, and 65.00%
reserve-eligible weight. With only the lookback changed to the most recent 36
months, the result was 85.00% SGOV, 0.00% VGIT, 0.00% VCIT, and 15.00% VTI,
with 7.06% expected return, 1.99% estimated volatility, and 85.00%
reserve-eligible weight.

The largest allocation change was 20 percentage points. The human-first
prediction of higher SGOV and lower VTI was supported.

### Downside stress test

Under the locked scenario of a -25.00% annual VTI expected return and a 0.25
percentage-point annual implementation-cost deduction, no candidate met the
6.50% net-return and 3.00% reserve requirements. The stop condition triggered:

```text
No qualifying portfolio—do not allocate; escalate for CIO guidance.
```

The 0.25-percentage-point cost deduction belongs only to this downside stress
test. Normal-case expected-return results are historical annualized estimates
compared directly with the stated hurdle; they are not separately
cost-adjusted.

### Lab 20 objective changed-input test

The human-authored, AI-off Lab 20 prediction raised only the annual return
hurdle from 6.50% to 7.00%. It predicted less SGOV, more VTI, higher
estimated volatility, lower reserve-eligible weight, and an unchanged defer
decision. The result matched: the 60-month mix moved from SGOV 65% / VTI 35%
to SGOV 60% / VTI 40%; expected return changed from 6.62% to 7.03%; volatility
from 5.64% to 6.42%; reserve-eligible weight from 65% to 60%; and the largest
allocation shift was 5 percentage points. The committee decision remained
**Do not allocate or rebalance yet.**

### Known-answer and integrity tests

tests/test_portfolio.py checks the published Lab 14 benchmark and equal-weight
return/volatility/reserve answers, the saved CSV ticker order and 60-observation
structure, the known 60-month qualifying mix, and the correlation-table
rejection path. The README gives the command to run it.

## Remaining validation work

- A final consistency review across the README, app, memo, video scripts,
  videos, transcripts, and manifest.

## AI-use disclosure

Codex helped with code organization, documentation formatting, and validation
structure. I chose and approved the no-trade decision, human-first prediction,
stress scenario, stop condition, and final recommendation. No Gemini or other
AI tool is claimed here unless documented elsewhere.

## Limits

This work is educational analysis, not investment advice. No real trade was
executed.
