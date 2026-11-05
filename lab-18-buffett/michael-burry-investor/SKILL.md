---
name: michael-burry-investor
description: Apply two reproducible earnings-quality and balance-sheet checks using SEC EDGAR 10-K Company Facts, without forecasts or market data.
---

# Michael Burry investor

Use this skill for the Lab 18 Michael Burry perspective. It is based on the
provided forensic-accounting brief, narrowed to the reported facts available in
this coursework app.

Run `buffett-investor/scripts/buffett_facts.py TICKER` after setting
`SEC_USER_AGENT` locally. Use only values printed by that script in a memo.

Use exactly these mechanical checks:

- Operating cash flow is at least net income every reported fiscal year.
- Liabilities are no more than twice equity in the latest reported fiscal year.

Do not add a price target, forecast, unreported liability claim, or accounting
inference. If a required reported fact is unavailable, report `not known`, not
an estimate.
