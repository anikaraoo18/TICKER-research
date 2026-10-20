# Project Readiness Feedback — Evidence Record

## Current decision

**Watch/Defer.** This is the current working conclusion in the Apple research
record, not investment advice.

## Highest-risk claim

Apple’s valuation conclusion is highly sensitive to gross margin and
terminal-value assumptions, and the methods use different dates/inputs.

Existing evidence supports this concern: Lab 11 reports a $5.66 gross-margin
value-per-share span over its stated range, larger than the $4.19 Mac-growth
span, and Lab 10 reports that terminal value is 70.53% of total value. The
existing valuation exercises use different market-observation dates and
different inputs; they are not a single final valuation range.

## Risks to resolve

- **Finance risk:** Gross-margin changes affect Apple’s full revenue base, and
  the Lab 12 review identifies an unmodeled Services downside case.
- **Data risk:** The preserved Edition A names September 1, 2026 as its
  valuation date, while existing exercises use September 9 or September 23,
  2026 market observations and different peer sets/inputs.
- **Technical/reproducibility risk:** The copied audit script imports `pandas`;
  although it is available in this environment, it is not declared in the
  Apple-model `requirements.txt`. A different Python environment may not run
  the audit without an independently supplied pandas installation.

## Audit result

Command run:

```sh
python project_audit.py project-submission-manifest-template.csv
```

`pandas` was available. After correcting CSV quoting in the copied working
manifest, the audit completed and reported these mechanical gaps:

- Research-Evolution.pdf
- Repository
- Visible executed output
- Decision memo or deck
- Validation-and-AI-Use.pdf
- Video 1
- Transcript Video 1
- Video 2
- Transcript Video 2
- Video 3
- Transcript Video 3

The manifest intentionally leaves unsupported access checks, frozen artifacts,
and all video/transcript evidence incomplete. The initial audit invocation
found a CSV parser error from unquoted commas in the copied working manifest;
that formatting error was corrected before the successful run above. No
packages were installed.

## Technical fresh-environment cold run

- Start/end: October 19, 2026, 2:39:11 PM EDT / October 19, 2026, 2:39:11 PM EDT.
- Elapsed time: 0.246 seconds.
- Checkout: a clean temporary local clone at `/private/tmp/ticker-project1-cold-run-python3.4X1dvh`, created from committed revision `909cb199fb3046ba1cf7b57a3729ac7b0de1672c`; no network access or package installation was used.
- Clean-checkout status before the attempted scripts: clean.
- Python version in the clean checkout: Python 3.9.6.
- README commands run: `python3 dcf.py`;
  `python3 AAPL-research/lab-08/aapl_pe.py`;
  `python3 AAPL-research/lab-10/aapl_proforma.py`; and
  `python3 AAPL-research/lab-11/aapl_proforma_sensitivity.py`.
- First failure: none.
- Key visible results: the FCFF DCF printed $80.1646 per diluted share and a $65.6625–$103.9522 sensitivity grid; the P/E model printed a $153.38–$236.38 implied range; the Lab 10 pro-forma printed $118.12 per fixed diluted share with FY2026–FY2030 balance-sheet gaps of 0.0 and cash-floor checks true; Lab 11 printed a restored-base match with zero differences and value-per-share spans of $4.19 for Mac growth and $5.66 for gross margin.
- Result: passed. The original `python` failure was repaired by commit `909cb19`, which changed the README's runnable commands to `python3`; the new fresh-checkout run passed without package installation.

This is a technical temporary-checkout run and is distinct from Lili Alderink's
earlier README-only run on the project author's computer.

## README-only partner run on the author's computer

- Reviewer: Lili Alderink
- Date: October 8, 2026
- Start time: 3:44 PM ET
- End time: 3:46 PM ET
- First failure: None.
- Elapsed time to visible output: 2 minutes.
- What the reviewer did: Lili used my README to run the Apple DCF, Lab 08 P/E model, Lab 10 pro-forma model, and Lab 11 sensitivity model on my computer.
- Visible result: The scripts executed successfully. The DCF printed $80.1646 per diluted share; the Lab 08 P/E analysis printed a $153.38–$236.38 implied range; the Lab 10 model printed $118.12 per fixed diluted share with all balance-sheet checks passing; and the Lab 11 sensitivity model printed passing restored-base and accounting checks.
- Limitation: This was completed on the project author’s computer, so the run confirms the README and commands worked in the current environment but does not test a fresh machine or fresh environment.
