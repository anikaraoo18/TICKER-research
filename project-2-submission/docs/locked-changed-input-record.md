# Project 2 — Locked Changed-Input Record

**Record timestamp:** November 10, 2026, 4:04:45 PM EST
**Decision/analysis date:** October 22, 2026
**Execution status:** Locked before execution. No results are recorded here, and
this is not a completed stress test. No Git commit hash is claimed.

## Decision

I would not execute a real trade yet because the 10% loss-limit rule is
unresolved.

## Baseline

The baseline is a 60-month historical CSV optimization using SGOV, VGIT, VCIT,
and VTI. The qualifying result was 65% SGOV / 35% VTI, with 6.62% expected
return, 5.64% estimated volatility, and 65% reserve-eligible weight.

## Locked changed input

The lookback window changes from all 60 monthly observations to the most recent
36 monthly observations. No other assumptions or inputs may change.

## Human-first prediction

The optimization will become more conservative, with a higher SGOV allocation
and reduced VTI allocation.

## Rationale

The recent 36-month window may reflect different return, correlation, and
volatility conditions than the full five-year history. This is a structural
sensitivity to the lookback choice, not evidence of a permanent regime shift.

## Conditions that would change my view

- An explicit CIO definition of the 10% calendar-year loss rule.
- A completed downside stress test.

## AI-use disclosure

Codex helped format this record. The decision, prediction, rationale, and
conditions above were provided by me.
