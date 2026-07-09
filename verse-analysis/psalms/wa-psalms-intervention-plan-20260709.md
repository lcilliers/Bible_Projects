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

## 4. Decisions — RESOLVED (researcher, 2026-07-09)
1. **G0 stays a valid gate — NOT N/A.** The measure judges the **effectiveness and sound construction of the read unit**, whether that unit is the whole poem (poetic Phase 2) or an associated-verse sub-passage. A large psalm (e.g. 65 char-spans) is a real signal to read it in **focused units** (stanza / associated-verse passages, or the per-verse Phase-1 step) so each read is sound. G0 is satisfied by focused reading, never waived.
2. **Pair migration — two-track confirmed.** Judge that each pair makes sense: **mechanical span-id resolution where it satisfies the requirement**, else **resolve by reading the context**. (Dry-run resolvability first to size mechanical vs read.)
3. **Pilots = Psalm 4, 23, 78** (small · famous/medium · large historical — spans the size range incl. the large-poem G0 case).
4. **Augment-in-place** (not rebuild). **After the three pilots complete, proceed to complete the entire book autonomously — no per-step approval.** Rules are stable; if one is genuinely unclear, fix it once and record it, do not re-litigate.

## 5. Sequence
(a) baseline ✅ filed → (b) **this plan → approval** → (c) **pilot Psalm 1**: intervene, re-measure, file pilot delta → review → (d) roll out by chapter, re-measuring at each close; at book close run the **25-unit read-back audit** + compute the full delta vs baseline → success report. Iterate any chapter that doesn't reach pass.

## 6. Definition of done (Psalms)
G2, G4, G6, G10 → 0; source(103) & effect(111) populated; G5/G9(a,c) measurable via span-ids and pass; G1/G3/G7/G9(b) stay pass; G0 poetic-reinterpreted; audit ≥90% sound / zero fidelity failures; positive delta vs baseline.

*Filed 2026-07-09. Awaiting approval on §4 (four decisions) before executing step (c) — the pilot.*
