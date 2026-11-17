# Lab 20 - Partner Explanation

## Partner question and explanation

My partner, Lili Alderink, asked: “Why does the code require
`assets == expected_tickers`, and what would happen if the CSV contained the
same four tickers in a different order?”

I explained that the script reads the CSV header order into `assets` and
requires it to match `("SGOV", "VGIT", "VCIT", "VTI")` exactly. The
exact-order check prevents a silent data-to-calculation mismatch. If the same
tickers appeared in a different column order, the script would raise an error
before the optimization runs; it does not automatically reorder them.

Lili confirmed she understood the explanation.

## Personal reflection

I learned that validating both ticker names and their column order is important
because a program can otherwise produce plausible-looking but misaligned
portfolio results.
