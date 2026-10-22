# Lab 15 Evolution

## Practice baseline preserved

BIL, IEF, LQD, and VT were used for the course's Meridian known-answer practice. Their data and validation record were preserved as `prices-meridian-example.csv` and `lab-15-validation-meridian-example.md`; they were not deleted or presented as my final selected universe.

## Active universe changed

After recognizing that the course examples were for practice rather than recommendations, I replaced them with SGOV, VGIT, VCIT, and VTI for this class analysis. SGOV is the cash/reserve sleeve, VGIT is the government-bond sleeve, VCIT is the investment-grade fixed-income sleeve, and VTI is the broad-equity sleeve.

## What stayed the same

- The long-only 5-point grid search.
- The 6.5% objective and 3% reserve minimum.
- SGOV and VGIT as reserve-eligible assets.
- The reusable math in `portfolio.py`.

## What the new evidence changed

Using all 60 months, the lowest-risk qualifying estimate was 65% SGOV and 35% VTI, with a 6.62% expected return and 5.64% volatility. Using only the last 36 months, it was 85% SGOV and 15% VTI, with a 7.06% expected return and 1.99% volatility.

For the partner challenge, VTI was changed to 10.00%, producing 40% SGOV, 35% VCIT, and 25% VTI, with a 6.50% expected return and 4.81% volatility. These are historical estimates, not forecasts.

## What remains uncertain

Historical returns and correlations can change. The 10% annual-loss rule still needs CIO clarification before adopting a real allocation. This is a class learning analysis, not investment advice.
