# Lab 13 — Meridian Foundation Human-First Mandate

## Statement classification

| CIO statement | My classification | Why |
|---|---|---|
| CPI + 4% net of estimated costs over rolling five-year periods | Objective | This is the stated return goal, but not a guarantee. |
| Seven-year policy horizon; quarterly review; annual rebalancing | Hard constraint | These are stated time and review rules. |
| $750,000 distribution every quarter | Hard constraint | The reserve must support these scheduled payments. |
| At least 12 months of distributions in cash or daily-liquid government securities | Hard constraint | This is a specific liquidity requirement. |
| 60% global equities / 40% U.S. investment-grade bonds | Benchmark | This is the stated policy benchmark. |
| Long-only; no borrowing, short sales, or derivatives | Hard constraint | These investment actions are directly prohibited. |
| One issuer may not exceed 8% | Hard constraint | This is a stated concentration limit. |
| Annual turnover should not exceed 25% without approval | Constraint with exception process | Turnover above 25% needs documented committee approval. |
| At least 90% redeemable within five business days | Hard constraint | This is a stated liquidity limit. |
| Calendar-year loss cannot exceed 10% | Requires clarification | The CIO did not define enforcement, probability, or what happens if the limit is breached. |
| No sector, climate, tax, active-management, or home-bias preference | Missing preference | These choices should not be invented. |
| “Build the best portfolio” | Unverifiable promise | “Best” is not defined; the committee must choose the tradeoff to optimize. |

## Mandate

- Decision user: Meridian Foundation investment committee.
- Decision: Decide whether to authorize further analysis and a small pilot; not to execute trades today.
- Objective: Seek CPI + 4% net of estimated costs over rolling five-year periods.
- Investable universe: Requires clarification. The case supports long-only, liquid investments, but does not define eligible funds, securities, countries, sectors, or active versus passive management.
- As-of date: October 15, 2026.
- Horizon: Seven years.
- Rebalancing: Quarterly review and annual rebalancing.
- Benchmark: 60% broad global equities / 40% U.S. investment-grade bonds.
- Naïve baseline: Hold the required 12 months of distributions ($3 million) in cash or daily-liquid government securities, then apply the stated 60/40 benchmark to the remaining reserve. This is a test baseline, not a CIO-approved allocation.
- Risk measure: Requires clarification. Calendar-year loss is mentioned, but no complete risk measure or enforcement rule is supplied.
- Loss tolerance: The CIO stated no calendar-year loss greater than 10%, but the practical enforcement rule is unresolved.
- Liquidity rule: At least 90% must be redeemable within five business days under ordinary market conditions; at least 12 months of scheduled distributions must remain in cash or daily-liquid government securities.

## Constraints

1. Long-only; no borrowing, short sales, or derivatives.
2. No issuer may exceed 8% of the portfolio.
3. Annual turnover should not exceed 25% without documented committee approval.
4. At least 90% must be redeemable within five business days under ordinary market conditions.
5. Keep at least $3 million—four quarterly distributions—in cash or daily-liquid government securities.
6. Rebalance annually and review quarterly.

## Precommitted validation plan

- Benchmark test: Compare proposed-policy results with the stated 60/40 benchmark.
- Naïve-baseline test: Compare with the cash-reserve-plus-60/40 baseline.
- Perturbation test: Test weaker returns, higher inflation, and distribution needs.
- Holdout test: Use a separate historical period from the one used to design assumptions.
- Cost test: Measure whether estimated trading and implementation costs prevent meeting the net objective.
- Failure condition: Stop or escalate if the approach violates any hard constraint, fails liquidity/distribution requirements, or relies on an undefined interpretation of the 10% loss statement.

## Required escalation

- Question for the CIO: When the return objective, liquidity needs, and “no calendar-year loss greater than 10%” statement conflict, which tradeoff should control—and is the 10% limit an absolute rule, a probability target, or a monitoring threshold?
- Why analysis cannot proceed without it: Different answers would lead to materially different risk measures, portfolio choices, and validation tests.