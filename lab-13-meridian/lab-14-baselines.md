# Lab 14 Portfolio Baselines

## Classroom inputs

The four course-authored classroom sleeves are Treasury bills, Treasury 10-year
notes, an investment-grade bond fund, and a global equity index fund. The
objective return is 6.5%.

## Known-answer results

| Portfolio | Expected return | Volatility | Reserve-eligible weight | Meets 6.5% objective? |
|---|---:|---:|---:|---|
| Benchmark | 6.80% | 10.46% | 0.0% | Yes |
| Equal weight | 5.20% | 5.21% | 50.0% | No |
| Inverse volatility | 3.77% | 1.05% | 90.3% | No |

## Validation evidence

- For the symmetric investment-grade-bond/global-equity correlation test, both
  0.25 entries were temporarily changed to 0.50. Benchmark volatility became
  11.00%. Both entries were restored to 0.25, and benchmark volatility returned
  to 10.46%.
- For the invalid-correlation check, a correlation of 1.3 produced a clear
  refusal before any portfolio calculations. The input was restored afterward.

## Candidate E

Candidate E holds 40% in the investment-grade bond fund and 60% in the global
equity index fund. It has 0.0% reserve-eligible weight and fails Meridian's
reserve rule. It is not adoptable: other Lab 13 ambiguity remains unresolved.

## Variance and volatility

My partner asked why the square root is used. I explained that the formula
first produces variance, and the square root converts it to volatility, the
normal percentage-risk measure.

## Files and AI-use disclosure

- [Meridian mandate check](mandate.py)
- [Portfolio baseline calculations](portfolio.py)
- Codex assisted with implementation after I supplied the course prompt and
  classroom inputs; I ran the program and checked the required known answers
  and validation cases.
