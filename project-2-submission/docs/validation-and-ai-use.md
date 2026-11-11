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
- Whitespace checks passed for the Project 2 files created so far.

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
