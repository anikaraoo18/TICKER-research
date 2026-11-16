# Lab 20 - Objective-Change Test Result

**Timestamp:** 2026-11-16 15:05 EST
**Prediction-lock commit:** `604a50e8cf69f3de19dd8a4db4d20c3f1911ab9f`

## Execution

Exact command:

```sh
python3 project-2-submission/portfolio/run_lab20_objective_test.py
```

The script was run once. It reused `portfolio.py` functions and the all-60-month
`prices.csv` data for SGOV, VGIT, VCIT, and VTI. The long-only 5-percentage-point
grid, 3.00% reserve minimum, and SGOV/VGIT reserve eligibility were unchanged.
The only changed input was the objective: 6.50% for baseline and 7.00% for the
changed run.

## Results

| Measure | Baseline objective: 6.50% | Changed objective: 7.00% |
|---|---:|---:|
| SGOV weight | 65.00% | 60.00% |
| VGIT weight | 0.00% | 0.00% |
| VCIT weight | 0.00% | 0.00% |
| VTI weight | 35.00% | 40.00% |
| Expected return | 6.62% | 7.03% |
| Volatility | 5.64% | 6.42% |
| Reserve-eligible weight | 65.00% | 60.00% |
| Largest allocation change from baseline | 0.00 percentage points | 5.00 percentage points |

## Prediction assessment

| Prediction component | Assessment | Evidence |
|---|---|---|
| More aggressive allocation | Supported | VTI increased by 5.00 percentage points and SGOV decreased by 5.00 percentage points. |
| Less SGOV and more VTI | Supported | SGOV changed from 65.00% to 60.00%; VTI changed from 35.00% to 40.00%. |
| Higher volatility | Supported | Estimated volatility rose from 5.64% to 6.42%. |
| Lower reserve-eligible weight | Supported | Reserve-eligible weight fell from 65.00% to 60.00%. |
| Committee decision remains “Do not allocate or rebalance yet.” | Supported | The decision remains unchanged. |

## Committee decision

**Do not allocate or rebalance yet.** The higher objective produced a mechanically
qualifying portfolio, but it did not resolve the undefined 10% calendar-year
loss rule. The existing downside stress test also produced no qualifying
portfolio, so the decision does not change.

## Plan-integrity check

SHA-256 of `project-2-submission/docs/lab-20-prediction.md` before execution:

```text
514a82573959c85bd872383372838bc140312d9e20949f5343924c7df8dc7539
```

SHA-256 after execution:

```text
514a82573959c85bd872383372838bc140312d9e20949f5343924c7df8dc7539
```

**Passed:** the prediction lock was unchanged before and after execution.

## Limit

The existing model's objective field was held to its established convention, so
this test does not separately model implementation costs.
