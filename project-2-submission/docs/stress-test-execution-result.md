# Project 2 — Downside Stress-Test Execution Result

**Execution timestamp:** November 10, 2026, 4:29:42 PM EST

**Exact command:**

```sh
python3 project-2-submission/portfolio/run_downside_stress_test.py
```

## Input conditions

- Data window: all 60 monthly observations in
  `project-2-submission/portfolio/prices.csv`.
- Universe: SGOV, VGIT, VCIT, and VTI.
- Grid and reserve conditions: long-only 5-percentage-point grid search, 3.00%
  reserve minimum, and SGOV and VGIT as reserve-eligible.
- Stressed input: VTI annual expected return overridden to -25.00%.
- Preserved inputs: all other CSV-derived expected returns, all volatilities,
  all correlations, and all other constraints.
- Cost treatment: 0.25 percentage points of annual implementation cost
  subtracted from each candidate's gross expected return.
- Qualification rule: net expected return of at least 6.50% and
  reserve-eligible weight of at least 3.00%.

## Output

```text
DOWNSIDE_STRESS_TEST
Months used: 60
Effective stressed VTI return: -25.00%
Cost treatment: subtract 0.25 percentage points of annual implementation cost from each candidate's gross expected return.
Candidate qualification rule: net expected return >= 6.50% and reserve-eligible weight >= 3.00%.
No qualifying portfolio—do not allocate; escalate for CIO guidance.
```

## Stop condition

**Triggered.** No candidate qualified under the locked scenario, so the
specified escalation message was produced. No objective, constraint, or
scenario input was changed to force a qualifying answer.

## Plan-integrity verification

The stress-test plan was unchanged before and after execution. Its SHA-256
digest was
`bce879eddb1d7edccdcdd40a09878a26b5cf9e3fe7c1656adca3b1e078d2bd28`
at both checks.

## Interpretation and limits

Under this severe hypothetical VTI-return and cost scenario, the existing
constrained process did not produce a qualifying allocation. This is a
hypothetical sensitivity, not a forecast, loss guarantee, or actual trade. It
does not resolve the CIO's undefined 10% calendar-year loss-limit rule.
