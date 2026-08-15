# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 26 -->
<!-- PROSE_SECTION_TYPE: prog_data_verses -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Verses and the context layer -->
<!-- PROSE_SORT_ORDER: 26 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch4-obslog-v1_0-20260423.md -->

## Verses and the context layer

The programme's verse data is held in two paired tables, with two further tables that hold classification and grouping. Together they move from raw verse records through to the structured analytical view that the dimensional and analytical work reads from.

`wa_verse_records` is the verse base — two hundred and twenty-nine thousand seven hundred and seventy-eight rows, one per occurrence of a term in a verse under the programme's extraction. Each row carries the verse text and its scriptural address (`book_id` as FK to `books`, `chapter`, `verse_num`, `testament`, `reference`, `translation` defaulting to ESV), the term it anchors to (`term_inv_id` as FK to `wa_term_inventory`, `mti_term_id` as FK to `mti_terms`, `target_word`, `transliteration`, `span_strong_match`), and the immediate textual context (`context_before`, `context_after`). The `file_id` field ties the verse row back to the processing file under which it was extracted, preserving the file-level provenance described earlier.

`wa_verse_term_links` is the paired table that attaches STEP's sub-gloss information to each verse-term occurrence. Two hundred and twenty-six thousand seven hundred and ninety-one rows carry the `step_subgloss_code` and `step_subgloss_label` that STEP assigns to a specific term use in a specific verse — the finer-grained sense tag that distinguishes, for example, *nephesh* used of a person from *nephesh* used of a desire. The link table is unique on (`verse_id`, `term_inv_id`); its cascading deletes follow the verse and the term inventory rows.

Book metadata is held in `books` (sixty-six rows — the canonical biblical books, with `name`, `abbreviation`, `testament` as `OT` or `NT`, `book_order` for canonical sequence, `verse_count`, and alternative codes). Because translations and extraction sources use different book codes — three-letter, four-letter, abbreviated, expanded — `book_code_variants` (one hundred and twelve rows) maps every known variant to the canonical `books.id`, so that a reference arriving in any code resolves to the same book.

The classification layer sits between the verse base and the analytical layer. `verse_context` is the classification grid — sixty-three thousand and twenty-eight rows, each row answering the question "how does this term function in this verse for this group". The three classification flags carry the answer. `is_relevant` is the term-level relevance decision: 1 when the term carries inner-being content in this verse, 0 when it does not. `is_anchor` is 1 for the verse designated as the anchor for its group. `is_related` is 1 for a verse that shares the group's contextual meaning with the anchor without itself being the anchor. Together the three flags partition the rows into the four possible states the logical consistency rules permit.

The set-aside records — `is_relevant = 0` — carry a `set_aside_reason` drawn from a controlled vocabulary: `no_inner_being` (the term carries no inner-being content here), `physical_only` (purely physical-process use), `spatial_only` (purely locational use), `wrong_face` (the verse has inner-being content but it is carried by a different term, not this one), or `other`. The `wrong_face` value is the vertical-pass-enabling value — it marks verses whose inner-being content belongs to another registry's analytical face and preserves that information for later rediscovery without re-reading the full corpus.

The term-level filter is the principle that governs these classifications. A verse may contain a term without the term doing any inner-being work in the verse — the term is purely syntactic, or purely locational, or names a body part without engaging an inner-being characteristic. Verse-theme filtering would let such occurrences through on the strength of the verse's overall subject; the term-level filter does not. The operative question is whether this specific term, in its specific use in this verse, is implicated in an inner-being characteristic. The classification flags record the answer.

`verse_context_group` holds the context groups that `verse_context` rows are grouped into. Three thousand five hundred and fifty rows — each carrying a human-readable `group_code` in the form `{mti_term_id}-{serial}`, a `context_description` that describes the term's inner-being engagement in this group, and an optional `notes` field. The group is the bridge between verse-level classification and term-level analysis: verses that share a contextual meaning are clustered under the same group, and the group's `context_description` is the programme's summary of what that shared meaning is. The group is where "how the term functions in verses of this kind" is recorded, rather than the classification of every verse individually.

The consistency rules that govern the classification grid are direct. A set-aside row (`is_relevant=0`) carries no group and is neither an anchor nor a related verse. An anchor row is relevant, belongs to a group, and is not also marked related. A related row is relevant, belongs to a group, and that group must have at least one active anchor. Every term must have at least one active anchor before Session B may proceed against it.

Because `mti_term_id` is the programme-wide key for a term — the same integer regardless of which registry views the term — OWNER and XREF registries query the same `verse_context` records through this key. The classification is attached to the term, not to the registry-view of the term, and the XREF inheritance described in the previous sub-section works because the classification rows live at the term level.

---
