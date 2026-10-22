# Lab 15 Uploaded-Universe Validation

This is the preserved BIL/IEF/LQD/VT practice and known-answer run; it is retained as a baseline rather than the current class-analysis universe.

`prices.csv` was evaluated with the reusable CSV-estimation and 5-percentage-point long-only grid-search functions in `portfolio.py`. Inputs for both cases were a 6.5% objective, a 3.0% reserve minimum, and BIL and IEF as the only reserve-eligible assets.

## All available monthly observations

The CSV supplied 60 monthly price observations.

| ETF | Estimated annual expected return |
| --- | ---: |
| BIL | 3.66% |
| IEF | -1.73% |
| LQD | -0.93% |
| VT | 11.00% |

The lowest-risk qualifying mix was:

| ETF | Weight |
| --- | ---: |
| BIL | 60.00% |
| IEF | 0.00% |
| LQD | 0.00% |
| VT | 40.00% |

- Expected portfolio return: 6.60%
- Volatility: 6.06%
- Reserve-eligible weight: 60.00%

## Last 36 monthly observations

The estimator used only the final 36 monthly price observations.

| ETF | Estimated annual expected return |
| --- | ---: |
| BIL | 4.35% |
| IEF | 3.82% |
| LQD | 5.81% |
| VT | 21.74% |

The lowest-risk qualifying mix was:

| ETF | Weight |
| --- | ---: |
| BIL | 85.00% |
| IEF | 0.00% |
| LQD | 0.00% |
| VT | 15.00% |

- Expected portfolio return: 6.96%
- Volatility: 1.79%
- Reserve-eligible weight: 85.00%

## Largest weight change

The largest change was **25.00 percentage points**: BIL increased from 60.00% to 85.00%, while VT decreased from 40.00% to 15.00%. IEF and LQD remained at 0.00% in both cases.

These historical estimates are for this classroom exercise only; they are not forecasts and are not investment advice.
