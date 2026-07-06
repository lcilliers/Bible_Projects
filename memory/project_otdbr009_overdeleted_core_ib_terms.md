---
name: project_otdbr009_overdeleted_core_ib_terms
description: OT-DBR-009 dedup over-deleted core IB terms (prayer, wisdom, to-pray) from the active registry.
metadata:
  type: project
---

During Psalms Gate-1 completeness (2026-07-06) a second integrity defect surfaced beyond the missing terms: **17 characteristic strongs existed in `mti_terms` but EVERY row was delete-flagged — no active term at all.** These include **prayer (H8605), wisdom H2451 ḥokmah, to-pray (H6419 palal), desire (H3970), goodness (H2898), to-exult, to-laugh**. They had been entirely removed from the active inner-being registry — almost certainly casualties of the **unresolved OT-DBR-009** mti_terms dedup, which over-deleted (flagged all duplicate rows including the survivor).

Fix applied for Psalms: reactivated exactly the one row each new gate1 verse-record references (`status='extracted_thin'`, `delete_flagged=0`, `anchor_note='gate1-psalms-2026-reactivated'`) — since no active row existed, this yields exactly one active term each. **But OT-DBR-009 itself is still open** and will keep producing these holes in other books until resolved — when processing each book's Gate-1, expect more core terms found only as delete-flagged rows. Treat OT-DBR-009 as materially affecting study integrity, not a cosmetic dedup. Related: [[project_per_book_corrective_pipeline]], [[feedback_enumerate_link_tables_first]].
