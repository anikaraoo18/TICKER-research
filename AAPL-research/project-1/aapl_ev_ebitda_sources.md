# Project 1 — AAPL/GRMN Single-Peer EV/EBITDA Cross-Check

## Scope and convention

This is a **single-peer cross-check**, not a peer median and not a valuation to
average with DCF or P/E. It uses the existing Lab 08 September 9, 2026 closing
prices: AAPL $315.34 and GRMN $272.18. The prices are the existing Lab 08
historical-price inputs, not filing facts. All other inputs below are from the
latest primary annual filings publicly available by that date.

Formulae: market capitalization = price × point-in-time common shares;
enterprise value = market capitalization + interest-bearing debt − cash and
cash equivalents; EBITDA = reported EBIT (operating income) + reported
depreciation and amortization. All amounts are USD millions except price and
the stated shares; the script converts price × million shares to USD millions.

## Filed inputs and calculations

| Company | Fiscal period / filing date | Filed input, unit, exact locator, and calculation |
|---|---|---|
| AAPL | FY2025 ended Sept. 27, 2025; Form 10-K filed Oct. 31, 2025 | [Apple 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm): cover page, line 96, 14,776.353M common shares outstanding as of Oct. 17, 2025; Consolidated Balance Sheets, p. 31, cash and cash equivalents $35,934M; p. 31, interest-bearing debt = commercial paper $7,979M + current term debt $12,350M + non-current term debt $78,328M = $98,657M; Consolidated Statements of Operations, p. 29, operating income $133,050M; Cash Flows, p. 33, depreciation and amortization $11,698M. EBITDA = $133,050M + $11,698M = $144,748M. Note 3, p. 36, diluted weighted-average shares 15,004.697M. |
| GRMN | FY2025 ended Dec. 27, 2025; Form 10-K filed Feb. 18, 2026 | [Garmin 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1121788/000119312526056028/grmn-20251227.htm): cover page, 192.480830M registered shares outstanding (excluding treasury) as of Feb. 13, 2026; Consolidated Balance Sheets, p. 49, cash and cash equivalents $2,278.646M; Item 7A, p. 43, “no outstanding long-term debt” and “no meaningful debt-related interest rate risk,” supporting $0 interest-bearing debt; Consolidated Statements of Income, p. 47, operating income $1,876.076M; Cash Flows, p. 50, depreciation $152.611M, plus Note 7—Intangible Assets, amortization of intangible assets $32.368M. D&A = $152.611M + $32.368M = $184.979M; EBITDA = $1,876.076M + $184.979M = $2,061.055M. |

## Calculation output

| Measure | Calculation | Result |
|---|---|---:|
| Garmin market capitalization | $272.18 × 192.480830M | $52,389.432M |
| Garmin enterprise value | $52,389.432M + $0.000M − $2,278.646M | $50,110.786M |
| Garmin EV/EBITDA | $50,110.786M ÷ $2,061.055M | 24.3132x |
| AAPL implied enterprise value | 24.3132x × $144,748M AAPL EBITDA | $3,519,283.133M |
| AAPL implied equity value | $3,519,283.133M − $98,657M + $35,934M | $3,456,560.133M |
| AAPL implied value per diluted share | $3,456,560.133M ÷ 15,004.697M | $230.37 |

## Limitations

- Fiscal periods differ: AAPL FY2025 ended September 27, 2025; Garmin FY2025
  ended December 27, 2025. Both precede the common September 9, 2026 price.
- Common shares are point-in-time market-cap inputs; AAPL diluted weighted-
  average shares are a separate income-statement denominator used only for the
  implied per-share calculation.
- The specified bridge subtracts cash and cash equivalents only. It excludes
  marketable securities; this is a required formula convention, not a claim
  that the securities are operating assets.
- Garmin's fitness, aviation, marine, outdoor, and auto-OEM businesses differ
  materially from Apple's integrated hardware-and-services business. This is a
  cross-check, not a stand-alone target price.
