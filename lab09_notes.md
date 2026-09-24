# Lab 09 — ABG Pro-Forma Build

## The lab question

What are five years of company statements worth when they are built from defensible assumptions, and how do we know the statements are right?

## Value-carrying judgments

- Organic revenue grows 1.8% per year.
- Profitability uses a 17.05% gross margin and declining SG&A-to-gross-profit ratios.
- Equity is valued using a 10% cost of equity and 2.5% terminal growth.

## Why cash is calculated last

Cash is the result of operations, inventory investment, capital spending, debt activity, financing, and buybacks. It is not an independent assumption.

## Model verification

| Check | FY2026 | FY2030 |
|---|---:|---:|
| Revenue | 18,323.0 | 19,678.3 |
| Operating income | 844.2 | 971.4 |
| Net income | 413.6 | 527.5 |
| FCFE | 211.4 | 342.3 |
| Year-end cash | 101.8 | 719.8 |
| Balance-sheet gap | 0.0 | 0.0 |

| Valuation check | Result |
|---|---:|
| Equity value per share | $291.75 |
| Share of value after 2030 | 79.76% |

## Floor-plan financing

Floor-plan financing is inventory lending used by auto dealers. It rises with inventory, carries interest based on the opening balance, and affects FCFE. Removing it would cause cash to fall to about negative $1.1 billion.

## Checks in the model

`proforma.py` includes balance-sheet and minimum-cash checks. It raises an error before valuation if the statements do not balance.
