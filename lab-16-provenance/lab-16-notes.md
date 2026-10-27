# Lab 16 Provenance Notes

## Partner explanation

I opened the Rule 4 revision-selection block in `asof.py` and explained it line
by line to my partner. I explained that the code first works only with rows
available by the decision date, groups records with the same ticker and
measured month, and keeps the row with the latest allowed publication date.

My partner asked why AAA’s February value was revised in the code. I explained
that the code does not know or infer the economic reason for a revision. It only
compares publication dates and keeps the latest eligible version. The training
table itself does not state why the source revised AAA’s value.

This rule prevents the model from using a value that was not available on the
decision date.

## Known-answer run

For the March 31, 2026 decision date, the row funnel removed:

- Row 11: no ticker.
- Row 7: duplicate.
- Rows 3, 8, and 10: published after the decision date.
- Row 2: superseded revision.

The final as-of rows were 1, 4, 5, 6, 9, and 12.

The as-of signals were:

- AAA: +1.98% through February.
- BBB: -1.02% through February.
- CCC: +0.91% through February.

The naïve signals, which ignore publication date, were:

- AAA: +5.83% through March.
- BBB: -5.15% through March.
- CCC: +1.82% through February.

This demonstrates why publication date matters and avoids look-ahead bias.

## Partner April 15 validation

My partner temporarily changed the decision date from March 31, 2026 to April
15, 2026 in their own copy of `asof.py`, ran the script, and confirmed the
as-of signals matched the naïve signals for AAA, BBB, and CCC. They restored
the original March 31, 2026 decision date afterward.

## My reflection

The as-of result is different from the naïve result because the naïve result
uses information that was published after March 31, 2026. The as-of filter only
uses information available at the decision date. This matters because using
later revisions or later monthly data would make a historical strategy appear
to know the future. I would use an as-of process before relying on any data
signal for a portfolio decision.
