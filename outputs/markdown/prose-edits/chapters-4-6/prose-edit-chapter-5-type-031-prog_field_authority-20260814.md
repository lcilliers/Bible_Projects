# Prose Edit — Programme — Chapter 5

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 34 -->
<!-- PROSE_SECTION_TYPE: prog_field_authority -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Record consistency with sources -->
<!-- PROSE_SORT_ORDER: 106 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose_ch5-obslog-v1_0-20260423.md -->

## Record consistency with sources

The programme's research record is a derived record. It rests on primary sources — STEP Bible for lexical and verse data, the researcher's analytical judgement for classifications and findings — and it accumulates interpretation over time through a phased pipeline. Three disciplines keep the record consistent with the sources it derives from: field authority when the schema holds the same information in more than one place; finding-reference consistency when an analytical conclusion's state changes; and STEP data provenance for the lexical layer that the whole programme builds on.

**Field authority.** Parts of the database hold the same information in more than one place. This is not a design flaw; it is the footprint of an architecture that evolved as the programme's understanding of its own data improved. Where a newer canonical field and an older source field overlap, the programme names one as authoritative, and the others defer to it. The principle is that every piece of information has exactly one field that wins on conflict.

Two field-authority rules are currently in force. For somatic classification, the authoritative field is `mti_term_flags` — the many-to-many link between a term and the set of classification flag types. The redundant `wa_term_inventory.somatic_link` is not authoritative: where the two disagree, `mti_term_flags` is correct. For `god_as_subject` and `somatic_link`, both fields carry a high error rate from bulk operations that populated them ahead of per-term verification; before a pass relies on either field, the value is verified against the actual verse evidence for the term. The verification, not the stored value, is the basis on which the pass proceeds.

Where a field-authority rule is in force, deprecation is the correct path for the non-authoritative field. The older field is not removed — the soft-delete discipline and the commitment to preserving state mean its values remain queryable for audit — but new writes go to the authoritative field, and reads that depend on current truth come from the authoritative field. The alternative — letting two fields each be consulted and the caller pick — is the pattern the two rules above were written to correct. The schema still carries fields whose authority status has not been explicitly ruled on; those are governance gaps awaiting resolution, not silent authorities.

**Finding-reference consistency.** A finding's state can change. The sub-section on the question catalogue and findings describes the three dispositions a finding can take: absorption into an existing catalogue question, promotion to a new word-specific question, or closure as obsolete on re-reading. When a finding's state changes, the references that point to it — other findings that cite it, catalogue-question links that record its coverage of a question, prose passages that elaborate it — must remain consistent with its new state.

The mechanism is carried in the schema. A finding that is superseded by a revised finding carries `superseded_by_id` pointing to its successor; the successor carries its own unique identifier; both rows remain in the database, linked through the supersede chain. A finding that is obsoleted carries `obsolete_reason` and `obsolete_date`. Catalogue-question links are preserved with their original `suggested` or `validated` state so that the history of how a finding was connected to questions is auditable through its lifecycle. Prose that cites a finding through `prose_section_finding_link` holds its link to the finding record regardless of the finding's state — the link is what makes it possible, on re-reading, to see that a prose passage rests on a finding that has since been superseded or obsoleted, and to adjust the prose accordingly.

The principle is that a reference to a finding is a reference to the finding's identity in the record, not to the finding's state at the moment of reference. A reference stays valid as the finding's state evolves; its meaning is updated by following the supersede chain or reading the `obsolete_reason` on the target row. The programme does not silently update references when findings change state, because silent updates would lose the history that the supersede-only lifecycle exists to preserve.

**STEP data provenance.** STEP Bible is the primary source for every term and every verse in the programme's corpus. Strong's numbers, transliterations, glosses, meaning text, verse references, and sub-gloss labels all originate in STEP. The database's term and verse layers carry what STEP returned at the time of extraction; STEP itself remains the authority to which the stored record traces back.

The extraction provenance is held in `term_fetch_log` — one row per registry-STEP extraction run, recording what was requested, what came back (verse counts fetched, stored, filtered), which Strong's numbers were resolved or needed suffix reconciliation, and any API warnings STEP returned. Every term row in `mti_terms` carries `extraction_date` and `last_changed`; every term row may carry `strongs_reconciled` to record that the Strong's number has been reviewed for suffix and spelling variants. The chain from STEP at a given date, through the extraction log, to the stored term and its verse records, is traceable end-to-end.

Re-extraction is the mechanism by which the record is brought current. When STEP updates a Strong's number, revises a gloss, or adds or removes a verse occurrence for a term, the programme's stored copy does not update automatically; it is a derived snapshot, not a live mirror. A re-extraction is authored as a Session A run against the affected registry, the new rows are imported, and the provenance markers are updated. The preceding rows are preserved through the soft-delete discipline, so the history of what STEP said at earlier extraction times remains queryable.

The three disciplines share a common principle: the programme's record is a derived record, and its integrity depends on the traceable chain from source to stored row being preserved across every revision the programme makes.

---
