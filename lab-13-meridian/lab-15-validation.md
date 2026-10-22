# Lab 15 Active-Universe Validation

`prices.csv` was evaluated with the reusable CSV-estimation and 5-percentage-point long-only grid-search functions in `portfolio.py`. Both cases used a 6.5% objective, a 3.0% reserve minimum, and SGOV and VGIT as the only reserve-eligible assets.

## All 60 monthly observations

| ETF | Estimated annual expected return |
| --- | ---: |
| SGOV | 3.72% |
| VGIT | -0.15% |
| VCIT | 0.73% |
| VTI | 12.00% |

The lowest-risk qualifying mix was:

| ETF | Weight |
| --- | ---: |
| SGOV | 65.00% |
| VGIT | 0.00% |
| VCIT | 0.00% |
| VTI | 35.00% |

- Expected portfolio return: 6.62%
- Volatility: 5.64%
- Reserve-eligible weight: 65.00%

## Last 36 monthly observations

| ETF | Estimated annual expected return |
| --- | ---: |
| SGOV | 4.31% |
| VGIT | 3.92% |
| VCIT | 6.51% |
| VTI | 22.63% |

The lowest-risk qualifying mix was:

| ETF | Weight |
| --- | ---: |
| SGOV | 85.00% |
| VGIT | 0.00% |
| VCIT | 0.00% |
| VTI | 15.00% |

- Expected portfolio return: 7.06%
- Volatility: 1.99%
- Reserve-eligible weight: 85.00%

## Largest weight change

The largest weight change was **20.00 percentage points**: SGOV increased from 65.00% to 85.00%, while VTI decreased from 35.00% to 15.00%. VGIT and VCIT remained at 0.00% in both cases.

Historical estimates are not forecasts and are not investment advice.

## Partner challenge and response

My partner chose VTI as the expected-return estimate she distrusted most and changed VTI to 10.00% in the Streamlit app. The original loaded CSV-estimate answer used 65% SGOV and 35% VTI, with 6.62% expected return, 5.64% volatility, and 65% reserve-eligible weight. The edited lowest-risk qualifying mix became 40% SGOV, 0% VGIT, 35% VCIT, and 25% VTI, with 6.50% expected return, 4.81% volatility, and 40% reserve-eligible weight. The largest allocation change shown was 35 percentage points.

My partner’s challenge showed that the lowest-risk qualifying mix changes materially when the VTI return estimate changes. I will treat the historical return estimate as uncertain rather than as a forecast, and I would revisit the allocation if updated data changes that estimate.
