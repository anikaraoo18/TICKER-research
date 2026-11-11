# Video 3 — Committee Decision

- **Maximum duration:** 5:00
- **Recording date:** ____________________
- **Duration:** ____________________
- **Video filename / YouTube URL:** ____________________
- **Transcript filename:** ____________________
- **Captions confirmed:** ____________________

## 0:00–0:45 — Open the live app and lead with the decision

**Say this:** “I am presenting to the Meridian investment committee. My
recommendation is: do not allocate or rebalance yet. The proposed-strategy
allocation range is 0% to 0%. This is a hold/defer decision, not an instruction
to sell existing assets or a claim about real portfolio holdings.”

**Show this:** Open `portfolio/app.py` through the README command, then show
the top decision-status panel.

## 0:45–1:35 — Baseline comparisons

**Say this:** “The Benchmark has 40% investment-grade bonds and 60% global
equities. It reports 6.80% expected return and 10.46% volatility, but 0%
reserve-eligible weight, so it fails the 3% reserve minimum. Equal weight has
25% in each Lab 14 sleeve, 5.20% expected return, 5.21% volatility, and 50%
reserve-eligible weight, but it misses the 6.5% objective.”

**Show this:** The Lab 14 baselines table in the app.

## 1:35–2:20 — Constrained result and sensitivity

**Say this:** “The 60-month constrained ETF result was 65% SGOV and 35% VTI,
with 6.62% expected return, 5.64% volatility, and 65% reserve-eligible
weight. It is conditionally qualifying mechanically, not approved for
allocation. The locked 36-month comparison shifted to 85% SGOV and 15% VTI.
The largest allocation change was 20 percentage points.”

**Show this:** The documented Project 2 results section in the app.

## 2:20–3:05 — Downside stop condition

**Say this:** “In the locked downside test, VTI’s annual expected return was
negative 25%, and a 0.25-point annual implementation cost was deducted from
every candidate. No candidate met the net-return and reserve requirements. The
result was: ‘No qualifying portfolio—do not allocate; escalate for CIO
guidance.’”

**Show this:** The downside-stress line in the app and
`docs/stress-test-execution-result.md`.

## 3:05–4:05 — Constraints and provenance

**Say this:** “This classroom app models the objective, reserve minimum, and
long-only search. It does not certify the $3 million distribution reserve
because portfolio value is unknown, issuer cap, turnover, five-business-day
liquidity, no-derivatives/no-borrowing controls, or the unresolved 10% loss
rule. The saved price snapshot ends September 2026 and was retrieved October
22, 2026. Historical estimates are not forecasts, and BAA10YM is quarantined
from decision inputs.”

**Show this:** The mandate-constraint and provenance notices in the app.

## 4:05–5:00 — Committee ask

**Say this:** “The committee should not allocate or rebalance yet. Reconsider
only after a written CIO definition of the 10% loss rule, a repeatable downside
stress result that qualifies without loosening constraints, confirmation of
data provenance, or a material change in the objective, reserve requirement,
or investable universe. This is educational analysis, not investment advice.”

**Show this:** The monitoring and reversal triggers in
`docs/decision-memo.md`.
