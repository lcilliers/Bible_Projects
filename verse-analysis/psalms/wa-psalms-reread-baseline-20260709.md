# Psalms — re-read BASELINE (the starting point to beat), 2026-07-09

> Psalms measured against the nine success gates **as it stands now** — the completed Psalter (a deliberate span-level `role-reassess-2026` read, the best-covered book). This is the "before"; the intervention's re-run shows the delta. Read the numbers through `verse-analysis/_reports/wa-reread-measures-interpretation-guidance-and-crossbook-baseline-20260709.md` (quality-vs-completeness; failing-now vs pass-at).
> **Runner:** `python scripts/_check_reread_measures_v3_20260709.py --book Psalms --label baseline` (read-only). **Unit model = passage** (0 segments, 314 passages — Psalms is poetic/chapter-driven, §14, not segmentation).

## Structure
2,461 verses · 4,768 candidate char-spans · **3,810 characteristics** · **76,321 active lexical rows** · 314 passages.
Per-span `ve_nr` present: 101,102,104,105,106,107,108,109,110,112,113,114,115 — **no 103 (source), no 111 (effect), no 116 (locus; locus was run only on the 5 wisdom books).**

## Gate results — Psalms baseline
*failing now = items to correct · pass at = 0 · status ❌ if failing-now>0, ✅ if 0, ⏸ if not measurable.*

| gate | measure | failing now | pass at | status |
|---|---|--:|--:|:--:|
| **G0** | passages > 12 char-spans | 150† | 0 | ❌† |
| **G1** | undecided spans / verses unprocessed | **0 / 0** | 0 | ✅ |
| **G2** | chars: no lexical / no operation(106) | 0 / **1,847** | 0 | ❌ |
| **G3** | ungrounded pairs / over-calls | 0 / 0 | 0 | ✅ |
| **G4** | recurring terms read identically | **4** | 0 | ❌ |
| **G5** | cohesive units read in isolation | N/A‡ | 0 | ⏸ |
| **G6** | candidate verses with no discovery | **976** | 0 | ❌ |
| **G7** | content items with null value | 0 | 0 | ✅ |
| **G9** | (a) orphan qual / (b) malformed / (c) dangling | N/A‡ / **0** / N/A‡ | 0 | ⏸/✅/⏸ |
| **G10** | chars missing ≥1 mandatory dimension | **3,810 (all)** | 0 | ❌ |
| **G10** | mandatory dims with ZERO rows | **103 (source), 111 (effect)** | — | ❌ |

**Score: G1, G3, G7 pass (+G9b). G0 genre-caveated. G2, G4, G6, G10 fail. G5/G9(a,c) unmeasurable until span-id encoding.**

† **G0 genre caveat.** For Psalms a "passage" is a whole psalm/chapter, and the poetic method (§14) deliberately reads the whole chapter (Phase 2). So 150 "over budget" is largely *by design* — the per-verse focus is Phase 1, not a small unit. **G0's 12-char-span budget is not the right gate for poetic books** — the intervention plan proposes a poetic reinterpretation (per-verse Phase-1 focus; G0 measured per-verse or marked N/A). Not a true failure.
‡ **G5/G9(a,c) N/A.** Pair endpoints in the current data are **Strong's-encoded** (`H0693@ref`), not span-ids — the corpus-wide defect (violates key-on-span-id). These gates become measurable only after the intervention writes span-id endpoints.

## What this says (Psalms-specific)
- Psalms is the **best-covered** book — the only one **fully roled** (G1 = 0, from the `role-reassess-2026` pass) and clean on grounding/blanks (G3, G7). Its sound core is genuinely sound.
- **Yet it fails every completeness/integrity gate the same way as Proverbs and Isaiah** — **source and effect never read, no discovery-lookout, no completeness ledger / explicit `none`, Strong's-encoded pairs, ⅓ of characteristics without an operation.** Confirms the gaps are **method-level, not coverage-level** (cross-book finding).
- **Psalms-specific residues:** G4 = 4 flattened recurring terms (audit these), and the poetic-G0 interpretation.

## Success against this baseline (per the criteria + amendment)
Intervention succeeds when: G2, G6, G10 → 0; G10 zero-row dims (source 103, effect 111) populated; G5, G9(a/c) become measurable (span-id endpoints) and pass; G4 → 0; G1/G3/G7/G9(b) stay pass; G0 reinterpreted for poetic; audit ≥90% sound, zero fidelity failures; delta positive.

*Filed 2026-07-09 in the Psalms folder. Read-only baseline. Intervention plan: `wa-psalms-intervention-plan-20260709.md` (same folder).*
