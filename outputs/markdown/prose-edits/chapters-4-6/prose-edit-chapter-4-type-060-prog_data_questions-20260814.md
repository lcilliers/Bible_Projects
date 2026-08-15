# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 70 -->
<!-- PROSE_SECTION_TYPE: prog_data_questions -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The question catalogue and findings -->
<!-- PROSE_SORT_ORDER: 29 -->
<!-- PROSE_VERSION: 2 -->
<!-- PROSE_SOURCE_FILE: programme-prose-v2-recommendations-v1-20260427.md -->

## The question catalogue and findings

The question catalogue and the findings layer together hold the programme's analytical output. The catalogue is the instrument by which Session B Analysis interrogates a word's evidence; the findings are what the analysis produces in answer. The two are linked through a dedicated join that records which findings speak to which questions, and the architecture supports both an accumulating catalogue and an accumulating finding record that grow together as the work proceeds.

`wa_obs_question_catalogue` carries the observation question catalogue — two hundred and six rows at present, each a question Session B is to ask against a word's evidence. Each row holds a unique `question_code`, a `section` placing the question within Session B's analytical structure, the `question_text` itself, a `pattern_type` that records the kind of inquiry the question represents, and tracking fields (`date_added`, `catalogue_version`, `status`, `deleted`). The `scope` field takes two values. A question with `scope = 'universal'` is asked of every word in the registry. A question with `scope = 'word_specific'` — or with a `source_registry_no` pointing to a particular registry — is asked only of the word it was indexed for. Session B Analysis runs the word-specific questions for a word first, then the universal questions, then produces its findings.

`wa_session_b_findings` is the programme's analytical journal. Under Architecture v2 (2026-04-27) it operates as an open-task lifecycle register: each row is an analytical observation or a CC-raised data anomaly that progresses through a defined lifecycle. The `status` field takes five values. A finding at `open` is a working observation awaiting resolution — typically a Stage 2a observation captured during a comprehensive reading, or a `DATA_ANOMALY_*` row CC wrote during post-write validation. A finding at `resolved_qa` has been linked to a catalogue question through `wa_finding_catalogue_links` — the question is the question, the source observation is the source, and the answer is recorded in the link's `session_b_note` field. A finding at `resolved_sd` has been converted to an SD pointer for Session D's cross-registry synthesis. A finding at `not_relevant` has been closed without analytical pickup, with reason captured. A finding at `superseded` has been replaced by a more precise finding through the `superseded_by_id` reference. Every analytical session works through its open findings: the obslog records the chosen outcome path for each, and Claude Code's writer updates the lifecycle state.

The Q&A architecture under v2 lives in two tables. The catalogue question is the question; the link in `wa_finding_catalogue_links` is the Q&A pair — finding_id pointing to the source observation, question_id pointing to the catalogue row, `session_b_note` carrying the answer text, and `coverage` taking one of four values. `full` records an ANSWERED Q&A with substantive evidence. `partial` records a PARTIALLY ANSWERED Q&A with qualification. `not_applicable` records a question the word's evidence does not engage — the link has no source finding (the table allows a null finding_id under M43) but records the not-applicable disposition with rationale. `no_finding` is filled by Claude Code's catalogue completeness sweep for any universal question not addressed by the analytical session — it surfaces silent misses and creates the backfill ledger for questions added to the catalogue later. With these four coverage values, every universal question for every analysed word produces a coverage row; the catalogue's coverage across the programme can be queried in a single SQL pass.

`wa_finding_entity_links` is the layer that grounds findings in the data. For every Q&A, Claude Code's writer creates entity-link rows recording which terms (mti_term_id), verses (verse_record_id), groups (verse_context_group.id), and dimensions (wa_dimension_index.id) the answer cites. The link table answers two queries that the prose alone cannot: which findings touch a particular verse — readable from the verse-link rows — and which findings speak to a particular dimension — readable from the dimension-link rows. Session D's cross-registry work reads from these link tables to discover findings that share verses or dimensions across registries.

The catalogue is generative. New questions arise from analytical work: GAP questions identify gaps in the programme's standing line of inquiry; word-specific extension questions surface the inquiries that a particular word's evidence made worth indexing for future passes on the same word. Under v2 these new questions enter `wa_obs_question_catalogue` through the writer pipeline, with `catalogue_version` field carrying the introduction marker (e.g. `v2.1-R067`). Review notes raised against existing questions land in the catalogue row's `review_note` column — the column added by migration M42 — preserving the audit trail of wording and validity observations that prior versions had no schema home for.

---
