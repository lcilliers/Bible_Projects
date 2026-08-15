# Prose Edit — Programme — Chapter 5

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 33 -->
<!-- PROSE_SECTION_TYPE: prog_delete_discipline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Soft-Delete Discipline -->
<!-- PROSE_SORT_ORDER: 105 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose_ch5-obslog-v1_0-20260423.md -->

## Soft-delete discipline

The programme does not physically delete rows from the research database. Every removable row carries a `delete_flagged` column; where a row is to be removed from active scope, the flag is set. The row itself remains in the database, its contents intact, queryable for audit, excluded from active queries by the same filter convention throughout (`delete_flagged = 0`). The deletion trail is the audit trail.

The discipline applies uniformly across the schema. Terms carry it on `mti_terms`, and the term inventory and its dependent tables — meanings, related words, root families, flags — carry it in parallel. Verse records carry it through `wa_verse_records` and its paired `wa_verse_term_links`. The classification layer carries it on `verse_context` and `verse_context_group`. The dimensional record carries it on `wa_dimension_index`. The prose store carries it on `prose_section`. The findings layer carries it on `wa_session_b_findings` (field name `delete_flag`). Every layer is preserved through revision in the same way.

Cascades follow the ownership architecture described in the sub-section on ownership and cross-registry references. When a term is soft-deleted, the classification rows and dimensional rows that hang from it are soft-deleted with it, so the derivative layers do not misrepresent state by outliving their source. Hard-delete cascades are reserved for cases where the row was genuinely transient (raw extraction artefacts that never became analytically meaningful), and those cases pass through the operational agent under researcher review, not through automated flows.

Soft-deletion is a change to state, not to history. The term ruled out in one pass can be read back in a later one; the dimension superseded by Dimension Review's next pass can be inspected to see how the analytical frame shifted; the prose row replaced by a newer version remains linked to its successor through the supersede chain. This is the mechanism by which the programme's analytical record is honest about where it has been — findings that no longer hold are not erased, they are marked. The combined effect of soft-delete and the supersede-only lifecycle on narrative prose is that the database's history is queryable end-to-end: no evidence is lost, no interpretation is overwritten, every state change has a witness.

Soft-delete is not the same as set-aside. The set-aside mechanism, described in the sub-section on verses, records that a specific verse-term occurrence is not part of the analytical corpus for a term — the row is preserved with `is_relevant = 0` and a controlled set-aside reason, and remains a valid and active row. Soft-deletion marks a row as removed from scope entirely. A verse-context row can be set aside without being soft-deleted, and soft-deleted without having been set aside. The two mechanisms preserve different kinds of information about the same row.

The discipline's purpose is continuity under revision. The programme revisits words; phases re-run; findings are re-read on fresh extracts. If the database deleted rows when the analytical frame changed, the record of how the programme arrived at its current state would be lost. Soft-delete is the mechanism that lets the programme evolve its findings without losing the audit trail that makes the findings defensible.

---
