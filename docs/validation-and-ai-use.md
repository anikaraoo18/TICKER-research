# Project 1 — Validation and AI-Use Record

## Status

This record carries forward existing Lab 10 and Lab 11 evidence. It does not
replace those lab records or claim a newly documented pre-run prediction.

## Existing Locked Changed-Input Record

See [AAPL Lab 11 — Locked Changed-Input Record](../AAPL-research/lab-11/aapl_lab11_notes.md).

Verified details carried forward from that file only:

- It was saved before sensitivity analysis on September 29, 2026.
- It states that it was revised before any sensitivity run for a deeper Apple
  product analysis.
- The two documented drivers were the Mac revenue-growth path and gross margin.
- The recorded sensitivity output spans were $4.19 per fixed diluted share for
  the Mac-growth cases and $5.66 for the gross-margin cases.
- The recorded restored-base check matched the initial base case: FY2030 EBIT
  of $183,240.4M, FY2030 FCFE of $147,305.4M, and value per fixed diluted share
  of $118.12.

## Project 1 changed-input evidence

| Required field | Record |
|---|---|
| Date and time locked | September 29, 2026; the Lab 11 record says it was saved before sensitivity analysis. No time is documented. |
| Model/version or commit reference | Lab 11 sensitivity analysis using the Lab 10 base model; no commit reference is documented. |
| Base inputs locked | Lab 10 base path: FY2026–FY2030 revenue growth of 4.5%, 4.0%, 3.5%, 3.0%, and 2.5%, with 46.5% gross margin. |
| Inputs changed | Mac-category revenue-growth path, one driver at a time; gross margin, one driver at a time. |
| Inputs held constant | For Mac cases, non-Mac revenue growth and 46.5% gross margin remained at base. For margin cases, Mac and non-Mac growth remained at base. |
| Reason for each change | The documented record tests Mac's contribution to total revenue and tests gross margin because it affects costs and all revenue. |
| Output comparison and validation result | Mac cases: $116.21–$120.40; margin cases: $115.29–$120.94; restored base exactly reproduced $118.12, FY2030 EBIT of $183,240.4M, and FY2030 FCFE of $147,305.4M. |
| Student confirmation | [STUDENT TO COMPLETE] |

The Lab 11 Locked Changed-Input Record is the Project 1 changed-input evidence.
No separate Project 1 pre-run prediction is claimed or created here.

## AI-tool disclosure

Existing records identify Codex and Gemini as tools used after Edition A for
research organization, source checking, model development, and documentation.
The Lab 08 peer-screen record further attributes the Garmin and Logitech peer
suggestions to Codex and Dell and Sony suggestions to Gemini; Dell and Sony were
excluded for the recorded reasons. No prompt text or exact AI-use date is
documented.

| Required field | Record |
|---|---|
| AI tool(s) and access path(s) actually used | Codex and Gemini are identified; access paths are not documented. |
| Date(s) used | Not documented. |
| Material suggestion or output | Lab 08 records Codex suggestions of Garmin and Logitech and Gemini suggestions of Dell and Sony. |
| Independent validation performed | The existing record says material Apple 10-K inputs and model outputs were independently checked; the Lab 08 record documents a Logitech hand calculation. Specific AI-by-AI verification actions are not fully documented. |
| Accept / modify / reject decision and reason | Garmin and Logitech were qualified; Dell and Sony were excluded for the reasons recorded in Lab 08. Other tool-output dispositions are not documented. |
| Student attestation | [STUDENT TO COMPLETE] |

## Limitations and follow-up

- The AAPL/GRMN EV/EBITDA script was run with `python3` and completed. It
  printed the formula and unit checks, Garmin EV/EBITDA of 24.3132x, and an
  implied AAPL diluted-share value of $230.37. This is a separate single-peer
  cross-check, not a median or a replacement for the Lab 11 changed-input record.
- The existing record does not document an exact AI-use date, prompts, or a
  complete AI-by-AI validation log.
- A technical fresh-checkout cold run passed on October 19, 2026 using Python
  3.9.6 and the README's four `python3` commands. It took 0.246 seconds, had no
  first failure, and displayed passing Lab 10 accounting and Lab 11
  restored-base checks. The original `python` failure was repaired by the
  README-only commit `909cb19`, which changed the runnable commands to `python3`.
- The October 8 README-only run occurred on the project author's computer, so
  it is distinct from the later successful temporary-checkout run.
- [STUDENT TO COMPLETE: identify any changes made after the Lab 11 locked record.]
