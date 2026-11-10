# Point-in-Time Data Card

## Data/signal name

October 22, 2026 portfolio-price snapshot and lookback-sensitivity signal.

## Decision date

October 22, 2026.

## Source and saved snapshot

The saved source file is `project-2-submission/portfolio/prices.csv`. Its
universe documentation identifies Digrin's displayed monthly **Adjusted** price
field, rather than Real price, as the price-data source for each ETF. The
documented retrieval date is October 22, 2026. No retrieval timestamp or
vendor revision guarantee is recorded.

## Universe and observation window

The universe is SGOV, VGIT, VCIT, and VTI. The saved CSV contains 60 nonblank
monthly adjusted-price observations, from October 2021 through September 2026,
with aligned ETF dates.

## What was known from the saved snapshot

The 60-month historical CSV optimization produced 65.00% SGOV, 0.00% VGIT,
0.00% VCIT, and 35.00% VTI, with 6.62% expected return, 5.64% estimated
volatility, and 65.00% reserve-eligible weight.

With the same process and only the lookback changed to the most recent 36
monthly observations, the result was 85.00% SGOV, 0.00% VGIT, 0.00% VCIT, and
15.00% VTI, with 7.06% expected return, 1.99% estimated volatility, and
85.00% reserve-eligible weight. The largest allocation change was 20.00
percentage points.

## Signal interpretation

The allocation recommendation is materially sensitive to the chosen historical
lookback. This supports a defer/escalate decision rather than a trade.

## Availability and provenance limits

The repository preserves the saved CSV and its documented retrieval
information, but it does not prove that the vendor's historical values were
unrevised on every prior date.

BAA10YM remains quarantined from Project 2 decision inputs because its
point-in-time availability and revision status were not established
sufficiently. The Lab 17 record states that the September 2026 value was not
available by a September 30, 2026 decision date and calls for an as-of-vintage
process before admission.

This data card does not authorize a trade and is not a return forecast.

## AI-use disclosure

Codex organized this card from existing repository evidence. I retained
responsibility for whether to use the signal.
