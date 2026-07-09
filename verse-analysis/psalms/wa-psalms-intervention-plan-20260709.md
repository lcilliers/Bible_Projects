# Psalms — intervention plan to bring the book to standard (2026-07-09)

> Plan to move Psalms from its baseline (`wa-psalms-reread-baseline-20260709.md`) to "successfully re-read" against the nine gates + audit. Built on the **standard instructions**: the authoritative cycle (`wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`), the **poetic chapter-driven method §14** (`wa-verse-analysis-method-v1-20260702.md`), the VE-lexical catalogue (dimension definitions), and the success-criteria + interpretation-guidance docs. **DB-writing — awaiting approval before execution (step c).**

## 1. Diagnosis → this is an AUGMENTATION, not a rebuild
Psalms is the best-covered book: **fully roled (G1✅), grounded (G3✅), no silent blanks (G7✅), 76,321 sound lexical rows.** Its structure is fine (passages set; poetic chapter model correct). So the intervention **keeps the sound core and fills the depth gaps** — it does *not* soft-delete-and-rebuild (unlike the Proverbs F-frame case). What must change:

| gate | gap | intervention |
|---|---|---|
| G2 | 1,847 chars with **no operation(106)** | read & record the governing predicate for each |
| G10 | **all 3,810** chars missing a mandatory dim; **source(103) & effect(111) never recorded** | complete the mandatory ledger per characteristic; **write explicit `none`** where the verse is silent |
| G6 | 976 candidate verses with **no discovery** | run the mandatory discovery-lookout (114) on every verse |
| G9/G5 | pair endpoints **Strong's-encoded** | migrate endpoints to **span-ids** (see §4) |
| G4 | 4 recurring terms read identically | audit & differentiate |
| G0 | 150 passages "over budget" | **reinterpret for poetic** (§3, decision) — not a true failure |

## 2. Method — poetic chapter-driven (§14), per chapter
For each psalm (chapter), in canonical order:
- **Phase 1 — per-verse lexical completion.** For every characteristic span in the verse, complete its dimensions per the catalogue and cycle §3A principles: take mechanical dims from morphology; **read source, target(+object-type), bearer, seat, manner, effect** from the verse+context; **record the operation**; write **explicit `none`** for any mandatory dim the verse is silent on (P4). Encode every pair endpoint as a **span-id**. Run the **discovery-lookout** on the verse (record a finding or `discovery: none`).
- **Phase 2 — whole-chapter synthesis + read-back.** Read the chapter as a whole (the poetic unit); lay the chapter's lexicals beside the text for sensibility; log systemic residuals; capture chapter-level notes. (This is where poetic cross-verse movement is honoured — the passage-level equivalent of belonging.)
- **Chapter close:** run `_check_reread_measures_v3_20260709.py --book Psalms` and confirm the chapter's spans moved toward pass; fix before moving on.

## 3. Provenance & governance
- Tags: `ve_lexical.source_provenance='reread-psalms-2026'`; `verse.process_marker='reread-psalms-2026'`; `verse_span_index.role_provenance` stays `read-2026` (roles already sound) unless a role is corrected.
- Every write **backed up + integrity-gated** (`_check_integrity_controls --snapshot` pre → apply → post → `--compare`). Per chapter, never cross-book.
- Legacy sound rows are **revised/augmented in place** (not deleted); superseded values soft-deleted with provenance.

## 4. Decisions needed before execution (your call)
1. **G0 for poetic** — adopt the poetic reinterpretation: measure digestion **per verse** (Phase-1 focus), and mark the passage-level G0 **N/A for poetic books**? *(Recommend yes — whole-chapter reading is the method, not a defect.)*
2. **Pair-endpoint migration (Strong's → span-id)** — two-track: **(a)** mechanically resolve endpoints that are unambiguous (`Hxxxx@ref` where that strong occurs once in the referenced verse) → span-id; **(b)** re-read the ambiguous ones (strong repeats in the verse) during Phase 1. *(Recommend this two-track; I'll dry-run the mechanical resolvability first to size (a) vs (b).)*
3. **Pilot chapter first** — run the full intervention on **Psalm 1** (6 verses, foundational, small), re-measure, and file a pilot delta for your review **before** rolling to the rest of the Psalter. *(Recommend yes — proves the method + the gate-delta on a small unit before 150 chapters.)*
4. **Augment-in-place confirmed** (not rebuild)? *(Recommend yes — Psalms' core is sound.)*

## 5. Sequence
(a) baseline ✅ filed → (b) **this plan → approval** → (c) **pilot Psalm 1**: intervene, re-measure, file pilot delta → review → (d) roll out by chapter, re-measuring at each close; at book close run the **25-unit read-back audit** + compute the full delta vs baseline → success report. Iterate any chapter that doesn't reach pass.

## 6. Definition of done (Psalms)
G2, G4, G6, G10 → 0; source(103) & effect(111) populated; G5/G9(a,c) measurable via span-ids and pass; G1/G3/G7/G9(b) stay pass; G0 poetic-reinterpreted; audit ≥90% sound / zero fidelity failures; positive delta vs baseline.

*Filed 2026-07-09. Awaiting approval on §4 (four decisions) before executing step (c) — the pilot.*
