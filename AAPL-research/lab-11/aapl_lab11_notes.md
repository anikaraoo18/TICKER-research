# AAPL Lab 11 — Locked Changed-Input Record

Saved before sensitivity analysis: September 29, 2026

This record was revised before any sensitivity run to follow the instructor’s request for a deeper Apple product analysis.

## Driver 1 — Mac revenue-growth path

Apple reports the broader Mac category, not MacBook-only revenue. Mac was $33,708 million, or 8.10% of total Apple revenue, in FY2025.

| Case   | FY2026 | FY2027 | FY2028 | FY2029 | FY2030 |
| ------ | -----: | -----: | -----: | -----: | -----: |
| Lower  |  -0.5% |  -1.0% |  -1.5% |  -2.0% |  -2.5% |
| Base   |   4.5% |   4.0% |   3.5% |   3.0% |   2.5% |
| Higher |   9.5% |   9.0% |   8.5% |   8.0% |   7.5% |

**Units:** percentage points of annual Mac-category revenue growth.

**Range reason:** Apple’s reported Mac-category growth was -26.93% in FY2023, 2.14% in FY2024, and 12.42% in FY2025. The lower and higher cases move every base-year Mac growth rate by five percentage points, remaining within the recent historical range.

**Model design:** Non-Mac revenue remains on the original base total-revenue-growth path. In the base case, Mac growth matches that original path, preserving the existing Apple base output.

**Prediction:** Because Mac represented 8.10% of FY2025 Apple revenue, changing Mac growth should move total revenue, operating profit, FCFE, and value per share, but likely less than changing the growth rate of Apple’s entire revenue base. Higher Mac growth should increase the outputs; lower Mac growth should decrease them.

## Driver 2 — Gross margin

| Case   | FY2026–FY2030 |
| ------ | ------------: |
| Lower  |         45.5% |
| Base   |         46.5% |
| Higher |         47.5% |

**Units:** percentage points of revenue.

**Range reason:** Apple’s FY2023–FY2025 gross margin ranged from 44.13% to 46.91%; these are labelled sensitivity judgments around the 46.5% base.

**Prediction:** A one-percentage-point lower margin should reduce operating profit, FCFE, and value per share because Apple keeps less gross profit from each sales dollar. The higher case should have the opposite effect.

## Partner exchange 1

**Partner’s question:** What about costs?

**My response:** Costs matter too, so I will test gross margin as my second driver. Higher product costs lower gross margin, which reduces operating profit, FCFE, and value per share even if revenue does not change.

Partner range check: My partner confirmed that Mac-growth and gross-margin inputs use percentage points and that each sensitivity run changes only one independent driver while the other assumptions remain at base.

## My check on my partner’s UiPath analysis

**My challenge:** Why is revenue growth more important than SG&A? If UiPath’s costs rise, wouldn’t FCFE and value fall even if revenue increases?

**Partner check of my model:** My partner confirmed that $120.40 − $118.12 = +$2.28 per share and that gross margin remained at the 46.5% base assumption in the Mac-high run. No correction was needed.

**My check of my partner’s UiPath analysis:** I reviewed my partner’s displayed UiPath base and sensitivity results and confirmed that the selected driver was changed separately from the other assumptions. I asked how the input affects UiPath’s cash flow and value. No correction was raised during the review.

## Partner
**Question:** Could gross margin rank as the larger driver only because of the sensitivity ranges I selected?

**Response:** The ranking applies only over my stated ranges and is not a forecast probability. However, Mac growth was tested over a wider ±5-percentage-point range while gross margin moved only ±1 percentage point, yet gross margin still produced the larger value-per-share span because it affects all Apple revenue rather than only the Mac category.

## Sensitivity results

| Driver / case         | FY2030 EBIT | FY2030 FCFE | Value per share |
| --------------------- | ----------: | ----------: | --------------: |
| Mac growth — Lower    | $179,847.5M | $144,613.9M |         $116.21 |
| Mac growth — Base     | $183,240.4M | $147,305.4M |         $118.12 |
| Mac growth — Higher   | $187,366.1M | $150,577.1M |         $120.40 |
| Gross margin — Lower  | $179,010.0M | $143,790.5M |         $115.29 |
| Gross margin — Base   | $183,240.4M | $147,305.4M |         $118.12 |
| Gross margin — Higher | $187,470.9M | $150,820.3M |         $120.94 |

## Output spans over the stated ranges

| Driver       | EBIT span | FCFE span | Value-per-share span |
| ------------ | --------: | --------: | -------------------: |
| Mac growth   | $7,518.6M | $5,963.1M |                $4.19 |
| Gross margin | $8,460.9M | $7,029.8M |                $5.66 |

## Restored-base check

The initial and restored base cases matched exactly: FY2030 EBIT was $183,240.4M, FY2030 FCFE was $147,305.4M, and value per fixed diluted share was $118.12.

## My interpretation

1. Which driver had the larger value-per-share span over my stated ranges?
Gross margin, because its value-per-share span is $5.66, larger than Mac growth’s $4.19

2. Why did that driver move Apple’s results more than the Mac-growth driver?
Gross margin applies to Apple’s entire revenue base. Mac represented only 8.10% of Apple revenue, so even a large Mac-growth change affects only part of the company.

3. Did my original prediction match the result? If not, what model link explains the difference?
My prediction that Mac growth would have a smaller effect than whole-company revenue growth is supported by the results. Mac-growth changes moved results in the expected direction, but I did not directly quantify a whole-company revenue-growth comparison

4. Which assumption would I research next, based on both impact and uncertainty?
I would research gross margin, because it had the bigger impact and can change with product mix and costs.

5. Does this sensitivity result change my valuation conclusion or research priority? Why?
The result should make gross margin a higher research priority; it does not make the sensitivity result a forecast or a buy/sell conclusion.
