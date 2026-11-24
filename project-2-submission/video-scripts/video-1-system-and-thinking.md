# Video 1 — System and Thinking

- **Maximum duration:** 3:00
- **Recording date:** ____________________
- **Duration:** ____________________
- **Video filename / YouTube URL:** ____________________
- **Transcript filename:** ____________________
- **Captions confirmed:** ____________________

## 0:00–0:30 — Decision context

**Say this:** “Codex helped organize code and documentation, but I selected
the inputs and scenarios, made the decision, and remain responsible for this
analysis. This is educational analysis, not investment advice. This is a
Project 2 portfolio-analysis system for the Meridian investment committee. My
current recommendation is: do not allocate or rebalance yet. The process uses
a 6.50% objective, a 3.00% reserve minimum, and a long-only grid, but the 10%
calendar-year loss rule is unresolved. I designed the committee adoption-gate
view so a mechanically qualifying base-case mix cannot be confused with an
approved trade.”

**Recording instruction:** Keep your webcam visibly on screen throughout.

**Show this:** The mandate, decision-status, and committee adoption-gate areas
in `portfolio/app.py`.

## 0:30–1:05 — Original result and locked prediction

**Say this:** “The original 60-month CSV result was 65% SGOV and 35% VTI, with
6.62% expected return, 5.64% estimated volatility, and 65% reserve-eligible
weight. Before the test, I locked one changed input: use the most recent 36
monthly observations instead of all 60. My human-first prediction was that the
result would become more conservative, with higher SGOV and lower VTI.”

**Show this:** `docs/locked-changed-input-record.md`, then the baseline
column in `docs/changed-input-execution-result.md`.

## 1:05–1:35 — Lookback sensitivity

**Say this:** “The prediction was supported. The 36-month result was 85% SGOV
and 15% VTI, with 7.06% expected return and 1.99% estimated volatility. The
largest allocation change was 20 percentage points. That shows the allocation
is materially sensitive to the historical lookback.”

**Show this:** The before-and-after results table in
`docs/changed-input-execution-result.md`.

## 1:35–2:05 — Lab 20 objective sensitivity

**Say this:** “Lab 20 held the same 60-month data, grid, reserve minimum, and
reserve eligibility fixed, and changed only the objective from 6.50% to 7.00%.
The qualifying allocation moved from 65% SGOV and 35% VTI to 60% SGOV and 40%
VTI. Expected return rose from 6.62% to 7.03%, estimated volatility rose from
5.64% to 6.42%, and reserve-eligible weight fell from 65% to 60%. The largest
allocation change was 5 percentage points.”

**Show this:** `docs/lab-20-objective-test-result.md`.

## 2:05–2:30 — Downside challenge

**Say this:** “I then used the locked downside scenario: VTI annual expected
return was set to negative 25%, and 0.25 percentage points of annual
implementation cost was subtracted from every candidate’s gross expected
return. No candidate qualified. The required stop condition was: ‘No
qualifying portfolio—do not allocate; escalate for CIO guidance.’”

**Show this:** `docs/stress-test-plan.md` and the stop-condition output in
`docs/stress-test-execution-result.md`.

## 2:30–3:00 — Validation, AI check, and conclusion

**Say this:** “One AI-produced item I personally checked was the
Codex-formatted locked changed-input record. I verified that it stated the
exact 60-to-36-month change, my prediction, and the later execution record’s
matching before-and-after SHA-256 integrity check. Codex helped organize and
format work, but I chose the prediction, stress scenario, stop condition, and
recommendation. A partner README-only cold run and a partner explanation of the
Lab 20 ticker-order check were also completed and documented. The system does
not support allocation yet.”

**Show this:** The AI-use disclosure in
`docs/validation-and-ai-use.md`, the integrity section in
`docs/changed-input-execution-result.md`, `docs/partner-cold-run.md`, and
`docs/lab-20-partner-explanation.md`.
