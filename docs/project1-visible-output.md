# Project 1 — Visible Apple Script Output

## Current run

**Run date and time:** October 19, 2026, 2:26:52 PM EDT  
**Working directory:** `TICKER-research`  
**Environment scope:** Current repository environment; not a documented fresh-environment cold run.

Commands executed once:

```sh
python dcf.py
python AAPL-research/lab-08/aapl_pe.py
python AAPL-research/lab-10/aapl_proforma.py
python AAPL-research/lab-11/aapl_proforma_sensitivity.py
```

## Output produced in the current run

| Script | Key visible output | Result |
|---|---|---|
| `dcf.py` | Value per diluted share: $80.1646; WACC/terminal-growth grid: $65.6625–$103.9522; reverse DCF reported no solution within its stated -5 to +10 percentage-point uniform-growth-shift bracket. | Pass: script completed. |
| `AAPL-research/lab-08/aapl_pe.py` | Garmin P/E 31.685681x; Logitech P/E 20.560417x; implied AAPL range $153.38–$236.38; median-implied price $194.88. | Pass: script completed. |
| `AAPL-research/lab-10/aapl_proforma.py` | Equity value $1,772,295.25M; terminal-value share 70.53%; value per fixed diluted share $118.12. FY2026–FY2030 accounting checks each showed a 0.0 balance-sheet gap and `cash >= floor: True`. | Pass: script completed and all displayed checks passed. |
| `AAPL-research/lab-11/aapl_proforma_sensitivity.py` | Mac cases: $116.21–$120.40; gross-margin cases: $115.29–$120.94. Restored base matched initial base: FY2030 EBIT $183,240.4M, FCFE $147,305.4M, and $118.12 per fixed diluted share, all with zero differences. | Pass: script completed; displayed accounting and restored-base checks passed. |

## EV/EBITDA cross-check run

Command executed once:

```sh
python3 AAPL-research/project-1/aapl_ev_ebitda.py
```

Visible output passed its formula/unit checks: market capitalization uses price
times million shares, enterprise value adds interest-bearing debt and subtracts
cash and cash equivalents, and EBITDA is reported EBIT plus reported D&A. It
reported Garmin market capitalization of $52,389.432M, EBITDA of $2,061.055M,
enterprise value of $50,110.786M, and EV/EBITDA of 24.3132x. It then reported
an implied AAPL enterprise value of $3,519,283.133M, implied equity value of
$3,456,560.133M, and implied value per diluted share of $230.37. The run states
the September 9, 2026 valuation-date convention and labels the result a
single-peer cross-check only; it must not be averaged with DCF or P/E.

## Historical records quoted elsewhere, not newly produced today

- The September 9, 2026 AAPL regular-session close of $315.34 is historical comparison data recorded in Lab 06 and Lab 08, not a price retrieved in this run.
- The September 23, 2026 completed regular-session close of $337.02 is historical comparison data recorded in Lab 10 results, not a price retrieved in this run.
- The September 29, 2026 Lab 11 Locked Changed-Input Record predates this run; it remains the changed-input evidence and is not recreated by this log.
- The October 8, 2026 README-only partner run is historical evidence in the project-readiness record, not an output produced in this run.

## Technical fresh-environment cold run

**Start/end:** October 19, 2026, 2:39:11 PM EDT / October 19, 2026, 2:39:11 PM EDT  
**Elapsed:** 0.246 seconds  
**Checkout:** clean temporary local checkout at committed revision
`909cb199fb3046ba1cf7b57a3729ac7b0de1672c`; no network access or package
installation was used.  
**Python:** Python 3.9.6  
**Commands:** `python3 dcf.py`, `python3 AAPL-research/lab-08/aapl_pe.py`,
`python3 AAPL-research/lab-10/aapl_proforma.py`, and
`python3 AAPL-research/lab-11/aapl_proforma_sensitivity.py`  
**First failure:** none

All four commands completed. The DCF printed $80.1646 per diluted share and a
$65.6625–$103.9522 sensitivity grid. The P/E model printed a $153.38–$236.38
implied range. The pro-forma printed $118.12 per fixed diluted share with
FY2026–FY2030 accounting gaps of 0.0 and cash-floor checks true. Lab 11 printed
the restored-base match with zero differences, plus per-share spans of $4.19
for Mac growth and $5.66 for gross margin.

The original failure, `time: python: No such file or directory`, was repaired
by commit `909cb19` changing the README's runnable commands from `python` to
`python3`. This subsequent clean-checkout rerun passed without packages.

This technical temporary-checkout result is separate from Lili Alderink's
October 8 README-only run on the project author's computer.

## Pass/fail summary

All four Apple valuation scripts executed to completion in the current environment. No script reported an exception or failed displayed validation check. This result confirms current-environment reproducibility only; it does not establish a final fresh-environment cold run.

The separate October 19 technical fresh-environment cold run passed after the
README command correction, independently confirming the current-environment
result above.
