# Project 2 — Changed-Input Execution Result

**Execution timestamp:** November 10, 2026, 4:18:50 PM EST

**Exact command:**

```sh
python3 project-2-submission/portfolio/run_lookback_test.py
```

## Locked-record integrity

The locked changed-input record was unchanged before and after execution. Its
SHA-256 digest was
`c60f63862fb84c8c65adacaeabf1325171be3ba387c301fbeb78c858dfce8953`
at both checks.

## Results

The test reused the copied `portfolio.py` functions and `prices.csv`. The
objective remained 6.5%, the reserve minimum remained 3%, and SGOV and VGIT
remained the reserve-eligible ETFs. The only changed model input was the
lookback window.

| Measure | Baseline: all 60 monthly observations | Changed input: most recent 36 monthly observations |
|---|---:|---:|
| SGOV weight | 65.00% | 85.00% |
| VGIT weight | 0.00% | 0.00% |
| VCIT weight | 0.00% | 0.00% |
| VTI weight | 35.00% | 15.00% |
| Expected return | 6.62% | 7.06% |
| Estimated volatility | 5.64% | 1.99% |
| Reserve-eligible weight | 65.00% | 85.00% |

The largest allocation change was 20.00 percentage points.

## Human-first prediction assessment

**Supported.** The changed-input run increased SGOV from 65.00% to 85.00% and
reduced VTI from 35.00% to 15.00%, matching the locked prediction of a more
conservative result.

## Plain-language interpretation

Using only the most recent 36 months of the same historical price series led
the grid search to hold more of its allocation in SGOV and less in VTI. This
shows that the selected output is sensitive to the historical lookback window.

## Limits and unresolved mandate item

Historical estimates are not forecasts, and this result does not authorize a
trade. The 10% calendar-year loss-limit rule remains unresolved.
