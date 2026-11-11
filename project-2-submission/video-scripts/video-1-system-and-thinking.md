# Video 1 — System and Thinking

- **Maximum duration:** 3:00
- **Recording date:** ____________________
- **Duration:** ____________________
- **Video filename / YouTube URL:** ____________________
- **Transcript filename:** ____________________
- **Captions confirmed:** ____________________

## 0:00–0:30 — Decision context

**Say this:** “This is an educational Project 2 portfolio-analysis system for
the Meridian investment committee. My current recommendation is: do not
allocate or rebalance yet. The process uses a 6.50% objective, a 3.00% reserve
minimum, and a long-only grid, but the 10% calendar-year loss rule is
unresolved.”

**Show this:** The mandate and panel-status area in
`portfolio/app.py` or the opening of `docs/decision-memo.md`.

## 0:30–1:15 — Original result and locked prediction

**Say this:** “The original 60-month CSV result was 65% SGOV and 35% VTI, with
6.62% expected return, 5.64% estimated volatility, and 65% reserve-eligible
weight. Before the test, I locked one changed input: use the most recent 36
monthly observations instead of all 60. My human-first prediction was that the
result would become more conservative, with higher SGOV and lower VTI.”

**Show this:** `docs/locked-changed-input-record.md`, then the baseline
column in `docs/changed-input-execution-result.md`.

## 1:15–1:50 — What changed and why it matters

**Say this:** “The prediction was supported. The 36-month result was 85% SGOV
and 15% VTI, with 7.06% expected return and 1.99% estimated volatility. The
largest allocation change was 20 percentage points. That shows the allocation
is materially sensitive to the historical lookback.”

**Show this:** The before-and-after results table in
`docs/changed-input-execution-result.md`.

## 1:50–2:25 — Downside challenge

**Say this:** “I then used the locked downside scenario: VTI annual expected
return was set to negative 25%, and 0.25 percentage points of annual
implementation cost was subtracted from every candidate’s gross expected
return. No candidate qualified. The required stop condition was: ‘No
qualifying portfolio—do not allocate; escalate for CIO guidance.’”

**Show this:** `docs/stress-test-plan.md` and the stop-condition output in
`docs/stress-test-execution-result.md`.

## 2:25–3:00 — AI check and conclusion

**Say this:** “One AI-produced item I personally checked was the
Codex-formatted locked changed-input record. I verified that it stated the
exact 60-to-36-month change, my prediction, and the later execution record’s
matching before-and-after SHA-256 integrity check. Codex helped organize and
format work, but I chose the prediction, stress scenario, stop condition, and
recommendation. The system does not support allocation yet.”

**Show this:** The AI-use disclosure in
`docs/validation-and-ai-use.md` and the integrity section in
`docs/changed-input-execution-result.md`.
