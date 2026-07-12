---
name: project_otdbr009_overdeleted_core_ib_terms
description: OT-DBR-009 dedup over-deleted core IB terms (prayer, wisdom, to-pray) from the active registry.
metadata:
  type: project
---

During Psalms Gate-1 completeness (2026-07-06) a second integrity defect surfaced beyond the missing terms: **17 characteristic strongs existed in `mti_terms` but EVERY row was delete-flagged — no active term at all.** These include **prayer (H8605), wisdom H2451 ḥokmah, to-pray (H6419 palal), desire (H3970), goodness (H2898), to-exult, to-laugh**. They had been entirely removed from the active inner-being registry — almost certainly casualties of the **unresolved OT-DBR-009** mti_terms dedup, which over-deleted (flagged all duplicate rows including the survivor).

The finding STANDS, but the *fix* I applied (reactivating rows under `anchor_note='gate1-psalms-2026-reactivated'`) was part of the **rejected Gate-1 bypass and is being rolled back** — proper handling is via engine onboarding (reconcile mti to the surviving `wa_term_inventory` OWNER rows). Note: for 9 of these the `wa_term_inventory` OWNER row survived while only the `mti_terms` row was deleted — so OT-DBR-009 deletes `mti_terms` (and cluster junctions) but not always inventory. **OT-DBR-009 itself is still open** and will keep producing these holes in every book until resolved — when doing each book's Gate-1, expect more core terms found only as delete-flagged `mti_terms`. Treat it as materially affecting study integrity, not a cosmetic dedup. Full state in files: `Workflow/Sessionlogs/wa-session-log-20260706-psalms-corrective-and-gate1-rework.md`. Related: [[project_per_book_corrective_pipeline]], [[feedback_enumerate_link_tables_first]].
