# Lab 15 Reflection

## My decision

**Pilot further analysis; do not adopt a real allocation yet.** The SGOV/VGIT/VCIT/VTI search produced qualifying historical-estimate mixes, but Meridian's 10% calendar-year-loss rule still lacks a defined CIO risk convention and cannot be guaranteed by this simple model.

## What the model does

The app tests every long-only mix in 5-percentage-point steps. It removes mixes that miss the 6.5% objective or 3% reserve minimum, then selects the qualifying mix with the lowest estimated volatility.

## What I learned from validation

Using all 60 months produced 65% SGOV and 35% VTI, while using the last 36 months produced 85% SGOV and 15% VTI. The largest allocation difference was 20 percentage points, and my partner's VTI challenge changed the qualifying mix materially. This shows that historical estimates can be sensitive to the selected period and to an expected-return assumption, so I should treat them as uncertain inputs rather than fixed conclusions.

## What would change my mind

- The CIO defines the 10% annual-loss rule and the action required after a breach.
- Newer market data materially changes estimated returns, volatilities, or correlations.
- Liquidity or reserve assumptions change.
- A stress test shows the proposed mix cannot support distributions.

## Limits

Historical estimates are not forecasts, and the grid uses only 5-percentage-point increments. This is a classroom learning analysis—not investment advice.
