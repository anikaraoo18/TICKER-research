Hi, my name is Anika Rao. This video demonstrates the Apple model commands, the recorded validation checks, and why I keep the valuation methods separate.

The README requires Python 3 and lists these four commands from the repository root: `python3 dcf.py`, the Lab 08 P/E model, the Lab 10 pro-forma model, and the Lab 11 sensitivity model. I will run them live now using the commands shown in the README.

The DCF prints a value per diluted share of $80.1646 and a WACC and terminal-growth sensitivity grid from $65.6625 to $103.9522. Its reverse DCF reports no solution in the stated uniform-growth-shift bracket. The P/E model prints a two-peer implied range of $153.38 to $236.38 and a median-implied price of $194.88.

The five-year pro-forma prints a value per fixed diluted share of $118.12. For FY2026 through FY2030, it displays a zero balance-sheet gap and confirms cash is at or above the floor. The Lab 11 sensitivity model shows Mac cases from $116.21 to $120.40 and gross-margin cases from $115.29 to $120.94. Its restored-base comparison shows zero differences from the initial base for FY2030 EBIT, FCFE, and value per share.

The first technical temporary-checkout attempt failed before model output because the timing wrapper reported, “time: python: No such file or directory.” The README was then corrected from `python` to `python3`. A later clean temporary checkout of the new commit passed on October 19, 2026 using Python 3.9.6. The recorded elapsed time was 0.246 seconds, and the first failure was none.

I do not average the methods. The FCFF DCF and pro-forma use different architectures. The P/E and EV/EBITDA work uses peers with business-model and fiscal-period differences. The market-price comparisons also use different stated dates. The recorded conclusion is Watch/Defer, not one precise target price.

The live outputs and recorded checks support reproducibility in the documented environment, while the remaining model and comparison limits support Watch/Defer.

This was recorded October 19th. Thank you.