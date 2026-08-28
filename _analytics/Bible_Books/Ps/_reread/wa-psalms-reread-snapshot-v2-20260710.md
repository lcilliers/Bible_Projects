# Psalms — re-read gate SNAPSHOT v2 (Book II close), 2026-07-10

> Book-wide gate re-measure at **72 / 150 psalms re-read** (48%) under the corrected method — taken at the close of **Book II (Ps 42–72)**, the whole first contiguous stretch of corrected reads. Deltas shown against the 2026-07-09 baseline and the 2026-07-10 (51/150) snapshot.
> **Runner:** `python scripts/_check_reread_measures_v3_20260709.py --book Psalms` (read-only). Unit model = passage (poetic). Prior docs: [`wa-psalms-reread-baseline-20260709.md`](wa-psalms-reread-baseline-20260709.md), [`wa-psalms-reread-snapshot-20260710.md`](wa-psalms-reread-snapshot-20260710.md).

## Trajectory — three measurement points
| metric | baseline 07-09 (0 corrected) | snapshot 07-10 (51/150) | **Book II close (72/150)** | Δ vs baseline |
|---|--:|--:|--:|--:|
| characteristics | 3,810 | 3,700 | **3,566** | −244 † |
| active lexical rows | 76,321 | 83,892 | **85,303** | **+8,982** |
| per-span `ve_nr` | no 103/116 | +103, +116 | 103 + 116 live | 2 dims added |
| **G2** chars with no operation | 1,847 | 1,160 | **915** | **−932** |
| **G4** recurring terms read identically | 4 | 2 | **2** | −2 |
| **G6** candidate verses no discovery | 976 | 654 | **521** | **−455** |
| **G9b** malformed pairs | 0 | 0 | **0** | held ✅ |
| **G10** chars missing ≥1 mandatory dim | 3,810 (all) | 2,451 | **1,948** | **−1,862** |
| **G10** mandatory dims with ZERO rows | none | none | none | ✅ |
| G1 / G3 / G7 | pass | pass | **pass** | held ✅ |

† Characteristics keep falling because Screen 0 re-roles God-content spans the old `role-reassess` pass had mis-called characteristics down to qualifier/standalone. Fewer, **truer** characteristics — not lost coverage.

## Reading of the Book-II-close point
- **Every completeness/integrity gate has moved the right way at every step.** At 72/150 the corrected-read portion carries **full genre-aware ledgers**: G10-incomplete chars now **1,948** (from 3,810 — roughly **half the whole book is now complete**, and all of it is the re-read half), no-operation down to 915, no-discovery down to 521, flattened-term reuse steady at 2.
- **G9b stays 0** — the pair_kind fix (baked into the apply script mid-session) has held clean across every psalm since, including the two largest reads in the project (Ps 68 = 123 spans, Ps 69 = 157 spans).
- **source (103) and locus (116) are populated** wherever re-read; G1/G3/G7 remain clean.
- Residual debt (1,948 incomplete ledgers, 915 no-operation, 521 no-discovery) is now **entirely the 78 not-yet-re-read psalms** (Books III–V) under the old pass.
- **G0 unchanged** (159 over the 12-span budget) — the poetic genre caveat: a "passage" is a whole psalm, so whole-chapter reading exceeds the budget by design, not a true failure.

## Book II (Ps 42–72) — what the corrected read captured
31 psalms, span-depth, all gate-clean. Highlights of the inner-being harvest: the deer-thirst and downcast-soul dialogue (42–43); the Miserere's 41-char penitential anatomy (51); the two-portrait contrasts of tyrant vs righteous (52, 62); the fear→trust refrain (56); "my soul clings to you" (63); the drowning-lament's 29 chars (69, the project's richest single psalm); the old-age prayer's proclaim-to-another-generation theme (71); and the ideal king's justice-as-mercy (72). Screen 0 held every God-hymn / creation-hymn / war-hymn correctly God-centred (46, 65, 66, 68), and reclaimed ~200+ spans a prior pass had mis-tagged.

*Filed 2026-07-10, Psalms folder. Read-only validation snapshot at the Book II close. Next: Book III (Ps 73 onward).*
