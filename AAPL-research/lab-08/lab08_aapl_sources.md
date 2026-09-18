# Lab 08 — AAPL P/E Sources and Peer Screen

## Frozen Apple peer policy

For Apple, I will investigate public, profitable technology companies with meaningful consumer-device, software, digital-service, or ecosystem revenue and exposure to developed global consumer markets.

I will use or qualify a company only if it has positive annual reported GAAP diluted earnings per share, a verifiable share price on Apple’s September 9, 2026 comparison date, and primary-source evidence explaining its business model.

I will qualify or exclude companies that are mainly enterprise software/cloud, advertising platforms, semiconductor manufacturers, retailers, or pure component suppliers because their revenue drivers, margins, capital intensity, and growth expectations can differ materially from Apple’s hardware-and-services mix.

## Target and peer source fields

| Company | Ticker | September 9, 2026 price | Annual GAAP diluted EPS | Fiscal year-end | Publication date | Price source | Annual EPS / business-model source | Disposition and business reason |
|---|---|---:|---:|---|---|---|---|---|
| Apple | AAPL | $315.34 | $7.46 | September 27, 2025 | October 31, 2025 | Yahoo Finance, AAPL regular-session close, September 9, 2026, 4:00:01 PM EDT (UTC−4) | [Apple FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm), Consolidated Statements of Operations, diluted earnings per share row | target |
| Garmin | GRMN | $272.18 | $8.59 | December 27, 2025 | February 18, 2026 | [Yahoo Finance historical prices](https://finance.yahoo.co.jp/quote/GRMN/history) | [Garmin 2025 Form 10-K, Item 1—Business](https://www.sec.gov/Archives/edgar/data/1121788/000119312526056028/grmn-20251227.htm); [FY2025 results release](https://www.garmin.com/en-US/newsroom/press-release/corporate/garmin-announces-fourth-quarter-and-fiscal-year-2025-results/) | qualify — GPS-enabled consumer products, services, and applications in fitness and outdoor markets; aviation, marine, and auto-OEM exposure remains an important difference from Apple. |
| Logitech | LOGI | $98.69 | $4.80 | March 31, 2026 | May 21, 2026 | [StockAnalysis LOGI historical data](https://stockanalysis.com/stocks/logi/history/) | [Logitech FY2026 Form 10-K, Item 1—Business](https://www.sec.gov/Archives/edgar/data/1032975/000103297526000021/logi-20260331.htm), and Consolidated Statements of Income, diluted EPS row | qualify — software-enabled consumer hardware for gaming, creating, and work; peripheral and video-collaboration exposure remains an important difference from Apple. |

## AI paths and dispositions

- Codex suggested Garmin and Logitech.
- Gemini suggested Dell and Sony.
- Dell: `exclude` — enterprise/commercial focus and missing exact price evidence in the Gemini result.
- Sony: `exclude` — total annual diluted EPS was negative.

## My hand calculation

I checked Logitech by hand: $98.69 ÷ $4.80 = 20.560417x P/E. This matches the calculator’s Logitech peer multiple.

## My removal prediction

I predicted that removing Garmin would lower Apple’s implied value because Garmin has the higher P/E multiple. The calculator confirmed this: removing Garmin leaves Logitech’s 20.560417x P/E, reducing Apple’s implied value from $194.88 to $153.38, a decrease of $41.50.

## AI criticism

**Status: Accept.** The critique correctly identifies that my DCF starting FCFF is a CFO-less-capex proxy, not a fully reconciled FCFF measure with an after-tax-interest adjustment. I also accept the annual-earnings timing limitation: Apple, Garmin, and Logitech have different fiscal year-ends even though their prices use the same September 9, 2026 date.

**Question that could change my decision:** If a fully reconciled Apple FCFF calculation produces a materially higher DCF range, I would reconsider my comparison.

**My response:** Unresolved. Apple’s filing did not separately provide the after-tax interest amount needed to fully reconcile the FCFF definition, so I cannot yet test whether that adjustment would move the DCF range materially.

## My conditional call

**Watch/defer.** Apple’s market price of $315.34 is above both my DCF range of $65.66–$103.95 and my two-peer P/E range of $153.38–$236.38. I will not average the methods because they measure different things and both have material limitations. I would reconsider if a fully reconciled FCFF model materially raises the DCF range, or if later annual earnings and a better-supported peer set justify higher comparable P/E multiples.
