# Prose Edit — Programme — Chapter 5

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 32 -->
<!-- PROSE_SECTION_TYPE: prog_validation_standard -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Document Validation Standard -->
<!-- PROSE_SORT_ORDER: 104 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose_ch5-obslog-v1_0-20260423.md -->

## Document validation and quality-flag architecture

The programme's validation standard operates at the boundary between phases. Each phase of the pipeline — Session A, Verse Context, Dimension Review, Session B, Session C, Session D — has a defined inflection point at which the phase's work is complete for a given word or cluster. The inflection point is the validation gate: if its completeness test is satisfied, the word advances; if not, the work stays where it is.

Inflection-point completeness is concrete, not judgemental. At Verse Context, it is that every OWNER term has every verse classified, every active group anchored, and the word re-exported. At Dimension Review, it is that every active group in the cluster has a dimension assigned, a dominant subject set, and `dim_review_status = Complete` on its registry. At Session B, it is that every standing catalogue question has been answered against the word's evidence and every finding is traceable to a specific verse, term, or lexical source. Each test is specifiable; each test can be run by query.

Gap status is a controlled vocabulary. The registry's phase-status fields (`phase1_status`, `verse_context_status`, `dim_review_status`, `session_b_status`) take values from a fixed set so the programme's state is always expressible in the same terms: work is `Pending` until it has begun, `In-Progress` while it is in flight, `Complete` when its inflection point has been passed, and `Blocked` where a dependency has not been resolved. A word whose status field does not resolve to one of these values is itself a validation failure. The fields are not narrative commentary on how the work is going; they are the state the programme commits to, and they are the basis on which the next phase is entitled to begin against the word.

Cross-document consistency is part of the standard. A finding recorded in Session B is traceable to the anchor verse it rests on in the verse-context layer. A dimension assigned in Dimension Review is traceable to the group it is attached to. An instruction cited in an observations log is referred to under the `[current]` convention, so the reference remains valid as instruction documents are revised. Inconsistency between documents or between the documents and the database is a validation failure and is resolved before the phase is marked complete.

Validation is enforced by the mechanisms described in the sub-sections this chapter points to. Controlled-vocabulary validators reject off-vocabulary values at patch application, as described in the sub-section on dimensions. The anchor-verse minimum is enforced at the completion check for each registry, as described in the sub-section on the anchor verse. The patch review gate, described in the sub-section on the two-AI division, is itself a validation step: every change passes through the researcher before it enters the record. The standard is not one instrument; it is the composite effect of these mechanisms applied at every boundary.

A pass that closes without its inflection point satisfied has not closed. This is the governing principle: there is no soft completion. A word that fails its validation gate stays at the phase it was in, and the gap that caused the failure is itself an observation the programme records and acts on.

**Quality flags.** Alongside the inflection-point mechanism, the programme carries a quality-flag architecture for recording that a specific record's state is questioned without blocking the phase from advancing. A quality flag is a row in one of the flag tables — `wa_data_quality_flags` for record-level flags on terms and files, `wa_session_research_flags` for session-level analytical flags including cross-registry pointers — that names the nature of the concern and links it to the entity it questions. The flag vocabulary is held in `wa_quality_flag_types`; the junction `wa_flag_type_question_link` records which flag patterns activate which catalogue questions, so that a record carrying a flag of a given type brings the relevant questions into view for the phase that can resolve it.

Quality flags are not findings. A flag is the programme's record that attention is due on a row, not the programme's record of an analytical conclusion about the row. A flag is raised when a pass notices a condition it cannot resolve within its own scope, and it is carried forward to the phase that can. Raising a flag does not stop the current phase; resolving the flag belongs to the phase that has the analytical frame to address it. The flag's lifecycle tracks this: a flag is raised with a date, resolved with a resolution note, and preserved in the record so the audit trail carries what was questioned and what the resolution was.

Quality flags and the validation standard are complementary. The validation standard closes the phase when the inflection point is satisfied. The quality flag carries forward a specific concern that the phase closure did not resolve — because the concern belonged to a later phase — without holding the closure open. Together they give the programme a way to advance work on words whose phase-level closure is sound while keeping record-level concerns visible until the right phase can act on them.

---
