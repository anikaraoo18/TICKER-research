# Project 2 — Pre-Execution Stress-Test Plan

**Record timestamp:** November 10, 2026, 4:26:53 PM EST

**Analysis/decision date:** October 22, 2026

## Purpose

Test whether the existing constrained portfolio process still produces a
qualifying allocation under a severe hypothetical equity scenario.

## Locked inputs

- **Data window:** The existing 60 monthly observations in
  `project-2-submission/portfolio/prices.csv`.
- **Universe:** SGOV, VGIT, VCIT, and VTI.
- **Baseline constraints:** Long-only 5-percentage-point grid search; objective
  of 6.50% net annual expected return; reserve minimum of 3.00%; SGOV and VGIT
  are reserve-eligible.
- **Stress input:** Override only VTI's annual expected return to negative
  25.00%.
- **Cost input:** Subtract 0.25 percentage points of annual implementation cost
  from every candidate portfolio's gross expected return to determine its net
  expected return.
- **Other estimate inputs:** Preserve all other expected returns, volatilities,
  correlations, and constraints from the 60-month CSV calculation.

## Qualifying rule

Net expected return must be at least 6.50%, and reserve-eligible weight must
be at least 3.00%.

## Stop condition

If no candidate qualifies, report: “No qualifying portfolio—do not allocate;
escalate for CIO guidance.” Do not lower the objective, loosen constraints, or
change the scenario to force an answer.

## Limit

This is a hypothetical sensitivity, not a forecast, a loss guarantee, or
authority to trade. It does not resolve the CIO's undefined 10% calendar-year
loss rule.

## AI-use disclosure

Codex formatted this document, but I selected and approved the scenario and
stop condition.
