---
name: cathie-wood-investor
description: Evaluate a company's reported growth trajectory and cash-generation capacity from five years of SEC EDGAR 10-K facts, without forecasts or market data.
---

# Cathie Wood investor

Use this skill for the Lab 18 Cathie Wood perspective. It is inspired by the
provided innovation-focused brief, but this coursework implementation is
strictly limited to reported SEC EDGAR 10-K Company Facts.

Run `buffett-investor/scripts/buffett_facts.py TICKER` after setting
`SEC_USER_AGENT` locally. Use only values printed by that script in a memo.

Use these reproducible reported-fact checks:

- Revenue grew from the first reported fiscal year to the last.
- Revenue increased in at least three of four year-over-year comparisons.
- Operating cash flow was positive in every reported fiscal year.

Do not create TAM estimates, price targets, future revenue, technology claims,
or innovation claims. If a required reported fact is unavailable, report the
check as `not known`, never as an estimate.
