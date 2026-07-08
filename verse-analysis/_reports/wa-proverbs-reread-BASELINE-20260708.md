# Proverbs re-read — BASELINE (the starting point to beat), 2026-07-08

> The nine success gates (from `wa-proverbs-reread-success-criteria-20260708.md`) run against Proverbs **as it stands now** — the compromised prior read (provenances `lexical-model-2026` / `role-reassess-2026` / `locus-derivation-v1-20260704`). This is the "before". Tomorrow's re-read, re-measured with the same script, must move each gate to its pass value; the delta is the demonstrated improvement.
>
> **Reproduce:** `python scripts/_check_proverbs_reread_measures_v1_20260708.py --label baseline` (read-only).
> **Honest reading of these numbers:** several gates fail because the *old model did not record the fields the new bar requires* (resolution states, the discovery-lookout, cross-verse links), not only because individual readings were wrong. That is precisely the gap the re-read closes — the baseline measures how far the current data sits below the new standard.

## Structure (context)
- Proverbs: **915 verses**, **2,124 candidate char-spans** across **800 candidate verses**, **251 active segment units**.
- Current characteristic-role spans: **1,708** (1,456 `lexical-model-2026` + 252 `role-reassess-2026`).
- Active `ve_lexical` rows: 22,342 `lexical-model` + 1,193 `role-reassess` + 725 `locus`.

## Gate results — BASELINE vs target
| gate | study aim | baseline | target | status |
|---|---|--:|--:|:--:|
| **G0** | focus (units digestible) | **36 units** > 12 char-spans (worst: PRO-14-F=129, 15-F=109, 10-F=96) | 0 | ❌ |
| **G1** | nothing passed over | 40 candidate spans undecided; 0 verses unprocessed | 0 / 0 | ❌ (a) |
| **G2** | worked, not named | 0 chars without lexical; **1,139** chars with **no operation read** | 0 / 0 | ❌ (b) |
| **G3** | read from the verse | **21,823** values ungrounded (no resolution state); 0 over-calls | 0 / 0 | ❌ (a) |
| **G4** | distinctions preserved | 0 recurring terms flattened | 0 | ✅ |
| **G5** | belonging honoured | **103** cohesive multi-verse units with no cross-verse link | 0 | ❌ |
| **G6** | unexpected surfaced | **438** candidate verses with no discovery entry | 0 | ❌ |
| **G7** | honest uncertainty | 0 silent blanks | 0 | ✅ |
| **G8** | better than before | (baseline scale = 1,708 char-role spans; per-chapter recorded) | delta > 0 | — |

**Baseline score: 2 of 9 gates pass (G4, G7). Seven to close.**

## What each failing gate says about the prior read
- **G0 (36 over budget)** — the digestion problem is real and broad: 6 F-frames (Prov 10–15) at 72–129 char-spans, plus ~30 long discourse/thread units. This is the structural cause of selective analysis.
- **G2 (1,139 chars with no operation)** — two-thirds of "characteristics" carry no read of *what they do* — named, not worked. The single biggest fidelity-to-objective gap.
- **G3 (21,823 ungrounded)** — the old model stored values without a warrant/resolution state, so grounding is not auditable. The new model records `span/inferred/unknown/none` on every value.
- **G5 (103 units in isolation)** — cohesive lectures were read verse-by-verse with no recorded inter-verse movement — exactly the "belonging" the objective wants surfaced.
- **G6 (438 no discovery)** — the discovery-lookout was not run on most verses, so the read could only confirm, not learn.
- **G1 (40 undecided)** — a small tail of candidate spans never resolved.

## Per-chapter characteristic scale (G8 before)
ch1:62 · 2:45 · 3:59 · 4:27 · 5:23 · 6:36 · 7:21 · 8:64 · 9:29 · **10:87 · 11:85 · 12:83 · 13:73 · 14:98 · 15:98** · 16:72 · 17:65 · 18:43 · 19:61 · 20:49 · 21:81 · 22:51 · 23:43 · 24:56 · 25:40 · 26:27 · 27:41 · 28:64 · 29:62 · 30:29 · 31:34
*(Chapters 10–15 — the F-frames — carry the densest load, as expected.)*

## Definition of success against this baseline
The re-read succeeds when the same script reports **G0–G3, G5–G8 all at their pass values, G4/G7 still 0**, the **read-back audit clears ≥90% sound with zero fidelity failures**, and the **G8 delta is positive** (net new/corrected characteristics; the six F-frame chapters fully treated in digestible units).

*Filed 2026-07-08. Read-only baseline. The number to beat is on the table.*
