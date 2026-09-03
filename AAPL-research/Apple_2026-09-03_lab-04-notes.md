# Lab 04 — Apple Evidence Ledger and Checkout Notes

## Deliverable status

The nine required ledger rows are in [Apple_2026-09-03_evidence-ledger.csv](Apple_2026-09-03_evidence-ledger.csv). Each row includes the required item, classification, value/unit, period, source locator, rationale, independent check, and failure mode.

## Reconciled discrepancy

**Different share-count definitions, not competing values.** Apple reports **15,004.697 million weighted-average diluted shares** for FY2025 EPS and **14,773.260 million shares outstanding** at September 27, 2025. The first is a period-average diluted EPS denominator; the second is a point-in-time basic outstanding-share count. The ledger uses the diluted weighted-average count provisionally for per-share value and identifies the timing/convention mismatch as a failure mode. **Source: Apple FY2025 Form 10-K, Item 8, Note 3, p. 36; Consolidated Balance Sheets, p. 31.**

## Contamination found and corrected

**Mechanical contamination: mixing a point-in-time share count with a diluted EPS-based valuation.** This would understate the share denominator if the model uses FY2025 diluted EPS conventions but divides by 14.773 billion period-end shares. The correction is to retain 15.005 billion weighted-average diluted shares in the current ledger row and explicitly revisit the as-of share convention at the valuation date. **Source: Apple FY2025 Form 10-K, Item 8, Note 3, p. 36; Consolidated Balance Sheets, p. 31.**

## Unresolved item

**Cash and marketable securities classification.** The ledger identifies $132.420 billion of cash, cash equivalents, and current/non-current marketable securities, but it does not yet establish how much cash is required to operate the business or whether every marketable security is non-operating. Do not add the full amount to equity value until that policy is supported. **Source: Apple FY2025 Form 10-K, Item 8, Consolidated Balance Sheets, p. 31.**

## AI architecture comparison

Complete this only after your Edition A receipt. Record the actual interfaces used and independently validate any accepted suggestion. Do not claim that a Gemini response exists unless you obtained one.

| Material suggestion | Codex proposal | Gemini response | Accept / modify / reject | Finance reason / evidence |
|---|---|---|---|---|
| Valuation object | Value Apple’s operating business with FCFF to enterprise value, then bridge to common equity. | [Paste actual response] | [Your decision] | FCFF values assets available to all capital providers; bridge separately classifies cash, debt, and other claims. |
| FCFF construction | EBIT x (1 - normalized tax rate) + D&A - capex - change in operating NWC. | [Paste actual response] | [Your decision] | The ledger supplies each base-year component, subject to normalization and scope review. |
| Normalization | Do not automatically forecast the 15.6% FY2025 effective tax rate. | [Paste actual response] | [Your decision] | Item 7 identifies State Aid Decision effects in the FY2025 tax provision. |
| Enterprise-equity bridge | Add only excess cash/non-operating assets after policy review; deduct interest-bearing debt and separately decide treatment of leases and other claims. | [Paste actual response] | [Your decision] | The cash/securities and debt rows have distinct dates, definitions, and failure modes. |
| Validation tests | Recompute sales, EBIT, tax rate, D&A, capex, NWC, debt, liquidity, and diluted EPS from their component rows. | [Paste actual response] | [Your decision] | The independent-check column documents these arithmetic reconciliations. |

## Readiness statement

**Ready:** The FY2025 revenue, EBIT, D&A, capex, debt, cash/securities, and diluted-share inputs reconcile to Apple’s primary filing and have labeled units and dates.

**Unsafe:** Treating all $132.420 billion of cash and marketable securities as excess cash, or mixing period-end shares with diluted weighted-average shares, could materially contaminate the bridge.

**Next test:** Establish Apple’s operating-cash requirement and choose a share-count convention aligned with the September 1, 2026 valuation date before calculating a per-share value.

## Checkout fields you must enter yourself

- Lab date
- Teammates / learning partners
- Session token displayed in class
- Actual AI access paths used
- In-person attendance declaration
- Truth attestation
- Brightspace receipt / attempt identifier
- Growth note: what you can now bridge that you could not bridge last week
