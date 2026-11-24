# Video 3 — Committee Decision

- **Maximum duration:** 5:00
- **Recording date:** November 24, 2026
- **Duration:** Approximately 5 minutes
- **Video filename / YouTube URL:** https://youtu.be/6XToy2aDI2g
- **Transcript filename:** YouTube automatic captions/transcript available at the video URL; not separately exported.
- **Captions confirmed:** Available through YouTube automatic captions; not independently corrected.

## 0:00–0:45 — Open the live app, demonstrate one bounded control, and lead with the decision

**Say this:** “Codex helped organize code and documentation, but I selected
the inputs and scenarios, made the decision, and remain responsible for this
analysis. This is educational analysis, not investment advice. I am presenting
to the Meridian investment committee. My recommendation is: do not allocate or
rebalance yet. The proposed-strategy allocation range is 0% to 0%. This is a
hold/defer decision, not an instruction to sell existing assets or a claim
about real portfolio holdings. I will now change the bounded objective control
from 6.50% to 7.00%, show the resulting mix, then reset the app to the loaded
base case.”

**Recording instruction:** Keep your webcam visibly on screen. Start the app
with the README command, change Objective from 6.50% to 7.00%, show the changed
mix, click **Reset to loaded base case**, then show the top decision-status
panel, adoption-gate dashboard, and allocation-stability chart.

**Show this:** Open `portfolio/app.py` through the README command. Show the
top decision-status panel, then explain why a green base mechanical-fit gate
does not outweigh the unresolved stability, downside, governance, and
provenance gates.

## 0:45–1:35 — Baseline comparisons

**Say this:** “The Benchmark has 40% investment-grade bonds and 60% global
equities. It reports 6.80% expected return and 10.46% volatility, but 0%
reserve-eligible weight, so it fails the 3% reserve minimum. Equal weight has
25% in each Lab 14 sleeve, 5.20% expected return, 5.21% volatility, and 50%
reserve-eligible weight, but it misses the 6.5% objective.”

**Show this:** The Lab 14 baselines table in the app.

## 1:35–2:30 — Constrained result and sensitivity

**Say this:** “The 60-month constrained ETF result was 65% SGOV and 35% VTI,
with 6.62% expected return, 5.64% volatility, and 65% reserve-eligible
weight. It is conditionally qualifying mechanically, not approved for
allocation. The locked 36-month comparison shifted to 85% SGOV and 15% VTI.
The largest allocation change was 20 percentage points. In Lab 20, changing
only the objective from 6.50% to 7.00% shifted the 60-month result to 60% SGOV
and 40% VTI. Expected return changed to 7.03%, volatility to 6.42%, and
reserve-eligible weight to 60%. The largest allocation change in that test was
5 percentage points.”

**Show this:** The documented Project 2 results section in the app, then
`docs/lab-20-objective-test-result.md`.

## 2:30–3:15 — Downside stop condition

**Say this:** “In the locked downside test, VTI’s annual expected return was
negative 25%, and a 0.25-point annual implementation cost was deducted from
every candidate. No candidate met the net-return and reserve requirements. The
result was: ‘No qualifying portfolio—do not allocate; escalate for CIO
guidance.’”

**Show this:** The downside-stress line in the app and
`docs/stress-test-execution-result.md`.

## 3:15–4:05 — Constraints, provenance, and validation

**Say this:** “This classroom app models the objective, reserve minimum, and
long-only search. It does not certify the $3 million distribution reserve
because portfolio value is unknown, issuer cap, turnover, five-business-day
liquidity, no-derivatives/no-borrowing controls, or the unresolved 10% loss
rule. The saved price snapshot ends September 2026 and was retrieved October
22, 2026. Historical estimates are not forecasts, and BAA10YM is quarantined
from decision inputs. A partner cold run and a partner code explanation have
been completed and documented; neither authorizes a trade.”

**Show this:** The mandate-constraint and provenance notices in the app.
Then show `docs/partner-cold-run.md` and
`docs/lab-20-partner-explanation.md`.

## 4:05–5:00 — Committee ask

**Say this:** “The committee should not allocate or rebalance yet. Reconsider
only after a written CIO definition of the 10% loss rule, a repeatable downside
stress result that qualifies without loosening constraints, confirmation of
data provenance, or a material change in the objective, reserve requirement,
or investable universe. This is educational analysis, not investment advice.”

**Show this:** The monitoring and reversal triggers in
`docs/decision-memo.md`.
