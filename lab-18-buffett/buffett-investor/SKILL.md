---
name: buffett-investor
description: Evaluate a public company with Buffett-style business-quality checks from SEC EDGAR 10-K facts, not price data. Use for reproducible five-year ROE and owner-earnings analysis.
---

# Buffett investor

Use this skill to evaluate reported business quality from SEC EDGAR Company Facts data.
It deliberately excludes market price, valuation multiples, and forecasts.

Run `scripts/buffett_facts.py TICKER` after setting `SEC_USER_AGENT` in the
local environment. The SEC requires an identifying User-Agent; never put that
value, a name, or an email address in repository files.

The script uses only 10-K facts, labels years by fiscal year-end, prefers the
latest filing for duplicate periods, and does not estimate missing facts. Use
only its printed numbers in any memo. Treat a `not known` check as unresolved,
not as a pass or fail.

For a Streamlit presentation, call the script with `--json` and display the
facts, XBRL tags, checks, and any memo. Validate that numeric claims in a memo
are among the script's printed values before showing it as supported.
