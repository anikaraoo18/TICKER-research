# Video 2 - Code and Validation Script

**Maximum speaking time:** 5 minutes

## Opening - 0:00 to 0:20

Hello. This video demonstrates the Apple model commands, the recorded validation checks, and why I keep the valuation methods separate.

## What to show on screen

1. Open `README.md` and show “Setup and run.”
2. Open a terminal in the repository root and run `python3 --version`.
3. Run `python3 dcf.py` and show the value per diluted share, sensitivity grid, and reverse-DCF message.
4. Run `python3 AAPL-research/lab-08/aapl_pe.py` and show the implied range.
5. Run `python3 AAPL-research/lab-10/aapl_proforma.py` and show the accounting checks and value per share.
6. Run `python3 AAPL-research/lab-11/aapl_proforma_sensitivity.py` and show the output spans and restored-base comparison.
7. Open `docs/project1-visible-output.md` at “Technical fresh-environment cold run.”
8. Open `docs/validation-and-ai-use-final.md` at “Execution and reproducibility.”

## Script

### README commands - 0:20 to 1:10

The README requires Python 3 and lists these four commands from the repository root: `python3 dcf.py`, the Lab 08 P/E model, the Lab 10 pro-forma model, and the Lab 11 sensitivity model. I will run them live now using the commands shown in the README.

### DCF and P/E - 1:10 to 2:00

The DCF prints a value per diluted share of $80.1646 and a WACC and terminal-growth sensitivity grid from $65.6625 to $103.9522. Its reverse DCF reports no solution in the stated uniform-growth-shift bracket. The P/E model prints a two-peer implied range of $153.38 to $236.38 and a median-implied price of $194.88.

### Pro-forma and sensitivity validation - 2:00 to 3:10

The five-year pro-forma prints a value per fixed diluted share of $118.12. For FY2026 through FY2030, it displays a zero balance-sheet gap and confirms cash is at or above the floor. The Lab 11 sensitivity model shows Mac cases from $116.21 to $120.40 and gross-margin cases from $115.29 to $120.94. Its restored-base comparison shows zero differences from the initial base for FY2030 EBIT, FCFE, and value per share.

### Cold-run history - 3:10 to 4:05

The first technical temporary-checkout attempt failed before model output because the timing wrapper reported, “time: python: No such file or directory.” The README was then corrected from `python` to `python3`. A later clean temporary checkout of the new commit passed on October 19, 2026 using Python 3.9.6. The recorded elapsed time was 0.246 seconds, and the first failure was none.

### Why methods are not averaged - 4:05 to 4:40

I do not average the methods. The FCFF DCF and pro-forma use different architectures. The P/E and EV/EBITDA work uses peers with business-model and fiscal-period differences. The market-price comparisons also use different stated dates. The recorded conclusion is Watch/Defer, not one precise target price.

## Closing - 4:40 to 5:00

The live outputs and recorded checks support reproducibility in the documented environment, while the remaining model and comparison limits support Watch/Defer.

## Recording checklist

- Recording date: ____________________
- Recording file or link: ____________________
- Transcript file or link: ____________________
- Upload or submission location: ____________________
