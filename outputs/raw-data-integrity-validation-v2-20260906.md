# Raw Data Integrity Validation — Both Databases (v2, corrected)

*Escalation #1532. v2 of 2026-09-06, superseding [v1](../archive/outputs/raw-data-integrity-validation-v1-20260906.md) (archived, not deleted — kept for the record of what the first pass got wrong). v1 scoped "base data" incorrectly and, worse, presented what amounted to a clean bill of health; it took six rounds of the researcher pointing back at material already in context before the real findings surfaced. Every correction and every new finding below is the product of that review. See escalations #1532 (parent) and its children #1533-#1539 for the full, tracked list — nothing here is left unescalated.*

## What was wrong with v1, and why

v1 defined "base" as `cfg_table.category = 'data'` — a config field that only distinguishes ordinary data tables from `cfg_*` rule/log tables. It does **not** encode what "base data" actually means in this project. That meaning already exists, named, in governance settings read at the start of the session that produced v1 — before a single query was run:

> `governance.programme_stages`: *"The research programme has three main stages: **Base_data (STEP through lexical)**; Analysis (deriving understanding of the inner being); Publishing (essays and output for the results)."*

> `governance.scope_iba_db`: *"...all related tables from **STEP through Strongs, verses, meaning, and lexicals**. It is now primary for all processes and base data; **a few analysis tables (debate/passage control) are expected to migrate back to research_db.**"*

> `governance.scope_research_db`: *"The research_db (bible_research.db) is the home for **prose and findings** with all the related enabling tables."*

Under that definition, true Base_data is roughly 15 tables (the STEP-through-lexical substrate), not the 89 v1 reported — v1's figure was inflated ~5-6x by sweeping in the entire Analysis layer (`finding`, `cluster`, `hib`, `phenomenon`, `passage` and their families, `vcg_term`, etc.), the Publishing layer (`prose_section` and its family), and the app's own process-control tooling (`escalation`, `run`, `validation_result`, `file_manifest`, ...) as if all of it were base data.

**No `cfg_*` field records which stage a table belongs to** — classification below is Claude's own judgement call against each table's `grain`/`use` text, not an authoritative source. That gap is itself escalated (**#1539**) with a recommended fix (a `cfg_table.stage` column). Until that's built, treat the stage tags below as best-effort, not settled fact.

---

## (a) Live tables by programme stage

The same 89 tables v1 called "base data," now grouped by actual stage. **Base_data is the correct answer to the original request** (a/b/c/d); Analysis/Publishing/Process_control are shown alongside so nothing from v1's work is lost — only relabelled. Columns are unchanged from v1: Total/Live row counts (soft-delete-aware where a `deleted`/`delete_flagged` column exists) and same-database relations (real FK + `cfg_column.fk` documented).

### Base_data — the true answer to (a)/(b)/(c)/(d)

15 tables.

| DB | Table | Grain | Total | Live | Relates to (same DB) |
|---|---|---|---|---|---|
| `iba` | `span` | ONE ROW PER HTML <span> TAG of a verse (O3) - a tag's codes are a com… | 391417 | 378149 | -> strong (FK strong_variant->strongNumber); -> verse (FK verse_id->id); -> verse (doc verse_id->id); <- span_candidate (FK span_id->id); <- verse_lexical (FK span_id->id); <- span_candidate (doc span_id->id); <- verse_lexical (doc span_id->id) |
| `iba` | `strong` | one row per strong — unique, global to the study | 15293 | 15293 | <- word_strong (FK strong->strongNumber); <- strong_sense (FK strong->strongNumber); <- strong_lexicon (FK strong->strongNumber); <- strong_verse (FK strong->strongNumber); <- span (FK strong_variant->strongNumber); <- strong_lsj_parsed (FK strong->strongNumber); <- strong_mounce_parsed (FK strong->strongNumber); <- strong_related (FK strong->strongNumber); <- verse_lexical (FK strong->strongNumber); <- strong_meaning_parsed (FK strong_variant->strongNumber); <- strong_meaning_tree (FK strong_variant->strongNumber); <- cluster_strong (FK strong->strongNumber); <- word_strong (doc strong->strongNumber); <- strong_sense (doc strong->strongNumber); <- strong_meaning_tree (doc strong_variant->strongNumber); <- strong_lexicon (doc strong->strongNumber); <- strong_verse (doc strong->strongNumber); <- candidate_seed (doc strong_variant->strongNumber); <- strong_meaning_parsed (doc strong_variant->strongNumber); <- strong_lsj_parsed (doc strong->strongNumber); <- strong_mounce_parsed (doc strong->strongNumber); <- strong_related (doc strong->strongNumber); <- verse_lexical (doc strong->strongNumber); <- verse_lexical (doc language->language); <- cluster_strong (doc strong->strongNumber) |
| `iba` | `strong_lexicon` | one row per strong that has LSJ/Mounce (Greek) | 5639 | 5639 | -> strong (FK strong->strongNumber); -> strong (doc strong->strongNumber) |
| `iba` | `strong_lsj_parsed` | one row per LSJ sense of a strong_lexicon.lsj entry (2026-07-25 corre… | 36199 | 36199 | -> strong (FK strong->strongNumber); -> strong (doc strong->strongNumber) |
| `iba` | `strong_meaning_parsed` | one row per gloss segment of a strong_meaning_tree lemma (2026-07-25 … | 47113 | 47113 | -> strong (FK strong_variant->strongNumber); -> strong (doc strong_variant->strongNumber) |
| `iba` | `strong_meaning_tree` | one row per sense-node of a LEMMA's definition tree | 40315 | 40315 | -> strong (FK strong_variant->strongNumber); -> strong (doc strong_variant->strongNumber) |
| `iba` | `strong_mounce_parsed` | one row per Mounce sense of a strong_lexicon.mounce entry (2026-07-25… | 5742 | 5742 | -> strong (FK strong->strongNumber); -> strong (doc strong->strongNumber) |
| `iba` | `strong_related` | one row per (strong, related strong) pair STEP's getInfo returned (fe… | 87535 | 87535 | -> strong (FK strong->strongNumber); -> strong (doc strong->strongNumber) |
| `iba` | `strong_sense` | one row per strong — the sense HEAD | 15293 | 15293 | -> strong (FK strong->strongNumber); -> strong (doc strong->strongNumber) |
| `iba` | `strong_verse` | one row per (strong, verse) — unique. The m:m index. | 132718 | 132718 | -> verse (FK verse_id->id); -> strong (FK strong->strongNumber); -> strong (doc strong->strongNumber); -> verse (doc verse_id->id) |
| `iba` | `verse` | one row per verse — unique. Does NOT belong to a strong. | 29759 | 29759 | <- strong_verse (FK verse_id->id); <- span (FK verse_id->id); <- passage (FK anchor_verse_id->id); <- verse_passage (FK verse_id->id); <- hib (FK first_verse_id->id); <- verse_hib (FK verse_id->id); <- phenomenon (FK verse_id->id); <- passage_insufficiency (FK verse_id->id); <- passage_emergent_question (FK verse_id->id); <- verse_lexical (FK verse_id->id); <- verse_lexical_note (FK verse_id->id); <- strong_verse (doc verse_id->id); <- span (doc verse_id->id); <- passage (doc anchor_verse_id->id); <- verse_passage (doc verse_id->id); <- verse_lexical (doc verse_id->id); <- hib (doc first_verse_id->id); <- verse_hib (doc verse_id->id); <- phenomenon (doc verse_id->id); <- passage_insufficiency (doc verse_id->id); <- passage_emergent_question (doc verse_id->id); <- verse_lexical_note (doc verse_id->id) |
| `iba` | `verse_lexical` | one row per Strong's code within a span (span_id, code_ordinal) — a c… | 975460 | 544572 | -> strong (FK strong->strongNumber); -> verse (FK verse_id->id); -> span (FK span_id->id); -> span (doc span_id->id); -> verse (doc verse_id->id); -> strong (doc strong->strongNumber); -> strong (doc language->language); <- verse_lexical_note (FK target_verse_lexical_id->id); <- verse_lexical_note (FK verse_lexical_id->id); <- verse_lexical_note (doc verse_lexical_id->id); <- verse_lexical_note (doc target_verse_lexical_id->id) |
| `iba` | `verse_lexical_note` | one row per (verse_lexical_id, note_type) — the judgement-bearing Lay… | 173 | 173 | -> verse_lexical (FK target_verse_lexical_id->id); -> passage (FK passage_id->id); -> verse (FK verse_id->id); -> verse_lexical (FK verse_lexical_id->id); -> verse_lexical (doc verse_lexical_id->id); -> verse (doc verse_id->id); -> passage (doc passage_id->id); -> verse_lexical (doc target_verse_lexical_id->id) |
| `iba` | `word_registry` | one row per English inner-being word | 180 | 180 | <- word_strong (FK word_id->id); <- word_strong (doc word_id->id) |
| `iba` | `word_strong` | one row per (word, strong) the STEP word-search returned | 4874 | 4874 | -> strong (FK strong->strongNumber); -> word_registry (FK word_id->id); -> word_registry (doc word_id->id); -> strong (doc strong->strongNumber) |

### Base_data — retracted subsystem (pending #1528-#1531 mark-inactive decision)

3 tables.

| DB | Table | Grain | Total | Live | Relates to (same DB) |
|---|---|---|---|---|---|
| `iba` | `candidate_seed` | one row per assessed lemma — the over-inclusive Axis-A candidate asse… | 2087 | 1806 | -> lemma_inventory (FK lemma_key->lemma_key); -> lemma_inventory (doc lemma_key->lemma_key); -> strong (doc strong_variant->strongNumber) |
| `iba` | `lemma_inventory` | one row per corpus lemma (base Strong's) — the INDEPENDENT substrate … | 11781 | 11781 | <- candidate_seed (FK lemma_key->lemma_key); <- candidate_seed (doc lemma_key->lemma_key) |
| `iba` | `span_candidate` | one row per CANDIDATE span (existence = candidate) — the L4b stamp ov… | 83914 | 83914 | -> span (FK span_id->id); -> span (doc span_id->id) |

### Base_data — static reference (not STEP-sourced, but foundational)

2 tables.

| DB | Table | Grain | Total | Live | Relates to (same DB) |
|---|---|---|---|---|---|
| `bible_research` | `book_code_variants` | one row per code | 112 | 112 *(no soft-delete col)* | -> books (FK book_id->id); -> books (doc book_id->id) |
| `bible_research` | `books` | one row per id | 66 | 66 *(no soft-delete col)* | <- book_code_variants (FK book_id->id); <- wa_verse_records (FK book_id->id); <- book_code_variants (doc book_id->id); <- wa_verse_records (doc book_id->id) |

### Analysis

43 tables.

| DB | Table | Grain | Total | Live | Relates to (same DB) |
|---|---|---|---|---|---|
| `bible_research` | `characteristic_subgroup` | one row per id | 146 | 146 | -> cluster_subgroup (FK cluster_subgroup_id->id); -> characteristic (FK characteristic_id->id); -> characteristic (doc characteristic_id->id); -> cluster_subgroup (doc cluster_subgroup_id->id) |
| `bible_research` | `cluster` | one row per cluster_code | 49 | 49 *(no soft-delete col)* | <- cluster_subgroup (FK cluster_code->cluster_code); <- cluster_finding (FK cluster_code->cluster_code); <- cluster_finding (doc cluster_code->cluster_code); <- cluster_subgroup (doc cluster_code->cluster_code) |
| `bible_research` | `cluster_observation` | one row per id | 276 | 276 | -> cluster_subgroup (FK cluster_subgroup_id->id); -> characteristic (FK characteristic_id->id); -> characteristic (doc characteristic_id->id); -> cluster_subgroup (doc cluster_subgroup_id->id) |
| `bible_research` | `cluster_subgroup` | one row per id | 175 | 156 | -> cluster (FK cluster_code->cluster_code); -> cluster (doc cluster_code->cluster_code); <- mti_term_subgroup (FK cluster_subgroup_id->id); <- verse_context (FK cluster_subgroup_id->id); <- characteristic_subgroup (FK cluster_subgroup_id->id); <- cluster_observation (FK cluster_subgroup_id->id); <- cluster_finding (FK cluster_subgroup_id->id); <- characteristic_subgroup (doc cluster_subgroup_id->id); <- cluster_finding (doc cluster_subgroup_id->id); <- cluster_observation (doc cluster_subgroup_id->id); <- mti_term_subgroup (doc cluster_subgroup_id->id); <- verse_context (doc cluster_subgroup_id->id) |
| `bible_research` | `finding` | one row per id | 458096 | 53339 | <- finding_verse_index (doc finding_id->id) |
| `bible_research` | `finding_citation` | one row per id | 51148 | 51148 | — |
| `bible_research` | `finding_question_link` | one row per id | 357657 | 357315 | — |
| `bible_research` | `finding_revision` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `bible_research` | `finding_verse_index` | one row per id | 475790 | 475790 *(no soft-delete col)* | -> finding (doc finding_id->id) |
| `bible_research` | `finding_verse_link` | one row per id | 3659 | 3649 | — |
| `bible_research` | `ib_characteristic` | one row per id | 1634 | 1634 *(no soft-delete col)* | — |
| `bible_research` | `ib_observation` | one row per id | 81 | 81 *(no soft-delete col)* | — |
| `bible_research` | `passage` | one row per id | 4296 | 4296 *(no soft-delete col)* | — |
| `bible_research` | `reread_worklist` | one row per id | 150 | 150 *(no soft-delete col)* | — |
| `bible_research` | `segment_unit` | one row per id | 877 | 788 | — |
| `bible_research` | `segment_unit_verse` | one row per (unit_id, verse_id) | 11276 | 11276 *(no soft-delete col)* | — |
| `bible_research` | `session_d_observations` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `bible_research` | `session_d_runs` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `bible_research` | `session_d_term_links` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `bible_research` | `session_d_verse_links` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `bible_research` | `vcg_term` | one row per id | 5091 | 1998 | -> mti_terms (FK mti_term_id->id); -> verse_context_group (FK vcg_id->id); -> verse_context_group (doc vcg_id->id); -> mti_terms (doc mti_term_id->id) |
| `bible_research` | `verse_analysis_progress` | one row per id | 33 | 33 *(no soft-delete col)* | — |
| `bible_research` | `wa_data_quality_flags` | one row per id | 0 | 0 | -> wa_quality_flag_types (FK flag_id->id); -> wa_quality_flag_types (doc flag_id->id) |
| `bible_research` | `wa_finding_entity_links` | one row per id | 287 | 287 | -> wa_session_b_findings (FK finding_id->id); -> wa_session_b_findings (doc finding_id->id) |
| `bible_research` | `wa_obs_question_catalogue` | one row per obs_id | 434 | 131 | -> word_registry (FK source_registry_no->id); -> word_registry (doc source_registry_no->id); <- wa_flag_type_question_link (FK question_id->obs_id); <- wa_finding_catalogue_links (FK question_id->obs_id); <- cluster_finding (FK obs_id->obs_id); <- cluster_finding (doc obs_id->obs_id); <- wa_finding_catalogue_links (doc question_id->obs_id); <- wa_flag_type_question_link (doc question_id->obs_id) |
| `bible_research` | `wa_quality_flag_types` | one row per id | 3 | 3 | <- wa_flag_type_question_link (FK flag_type_id->id); <- wa_data_quality_flags (FK flag_id->id); <- wa_data_quality_flags (doc flag_id->id); <- wa_flag_type_question_link (doc flag_type_id->id) |
| `bible_research` | `wa_session_research_flags` | one row per id | 715 | 715 *(no soft-delete col)* | -> word_registry (FK cross_registry_id->id); -> wa_file_index (FK file_id->id); -> word_registry (FK registry_id->id); -> word_registry (doc registry_id->id); -> wa_file_index (doc file_id->id); -> word_registry (doc cross_registry_id->id); <- wa_prose_section_citations (FK cited_sd_pointer_id->id); <- wa_prose_section_citations (doc cited_sd_pointer_id->id) |
| `bible_research` | `wa_vocab_member` | one row per id | 39 | 39 *(no soft-delete col)* | -> wa_vocab_member (FK superseded_by_member_id->id); -> wa_vocab_set (FK set_id->id); -> wa_vocab_set (doc set_id->id); -> wa_vocab_member (doc superseded_by_member_id->id); <- wa_vocab_member (FK superseded_by_member_id->id); <- wa_vocab_member (doc superseded_by_member_id->id) |
| `bible_research` | `wa_vocab_set` | one row per id | 8 | 8 *(no soft-delete col)* | <- wa_vocab_member (FK set_id->id); <- wa_vocab_member (doc set_id->id) |
| `iba` | `cluster` | one row per cluster (M01-M46 + FLAG + T2) — the inner-being dimension… | 94 | 89 | <- cluster_strong (FK cluster_code->cluster_code); <- cluster_strong (doc cluster_code->cluster_code) |
| `iba` | `cluster_strong` | one row per (strong, cluster_code) assignment | 8929 | 7419 | -> cluster (FK cluster_code->cluster_code); -> strong (FK strong->strongNumber); -> strong (doc strong->strongNumber); -> cluster (doc cluster_code->cluster_code) |
| `iba` | `hib` | hib | 63 | 21 | -> verse (FK first_verse_id->id); -> verse (doc first_verse_id->id); <- hib_referent_option (FK hib_id->id); <- verse_hib (FK hib_id->id); <- phenomenon (FK hib_id->id); <- operation_party (FK hib_id->id); <- hib_referent_option (doc hib_id->id); <- verse_hib (doc hib_id->id); <- phenomenon (doc hib_id->id); <- operation_party (doc hib_id->id) |
| `iba` | `hib_referent_option` | hib_referent_option | 5 | 0 | -> hib (FK hib_id->id); -> hib (doc hib_id->id) |
| `iba` | `operation` | operation | 177 | 121 | -> phenomenon (FK phenomenon_id->id); -> phenomenon (doc phenomenon_id->id); <- operation_party (FK operation_id->id); <- passage_linkage (FK to_operation_id->id); <- passage_linkage (FK from_operation_id->id); <- operation_party (doc operation_id->id); <- passage_linkage (doc from_operation_id->id); <- passage_linkage (doc to_operation_id->id) |
| `iba` | `operation_party` | operation_party | 250 | 136 | -> hib (FK hib_id->id); -> operation (FK operation_id->id); -> operation (doc operation_id->id); -> hib (doc hib_id->id) |
| `iba` | `passage` | one row per passage — a reading frame (global, per book) | 18558 | 42 | -> verse (FK anchor_verse_id->id); -> verse (doc anchor_verse_id->id); <- verse_passage (FK passage_id->id); <- phenomenon (FK passage_id->id); <- passage_linkage (FK passage_id->id); <- passage_insufficiency (FK passage_id->id); <- passage_emergent_question (FK passage_id->id); <- passage_validation_note (FK passage_id->id); <- verse_lexical_note (FK passage_id->id); <- verse_passage (doc passage_id->id); <- phenomenon (doc passage_id->id); <- passage_linkage (doc passage_id->id); <- passage_insufficiency (doc passage_id->id); <- passage_emergent_question (doc passage_id->id); <- passage_validation_note (doc passage_id->id); <- verse_lexical_note (doc passage_id->id) |
| `iba` | `passage_emergent_question` | passage_emergent_question | 4 | 3 | -> verse (FK verse_id->id); -> passage (FK passage_id->id); -> passage (doc passage_id->id); -> verse (doc verse_id->id) |
| `iba` | `passage_insufficiency` | passage_insufficiency | 1 | 1 | -> verse (FK verse_id->id); -> passage (FK passage_id->id); -> passage (doc passage_id->id); -> verse (doc verse_id->id) |
| `iba` | `passage_linkage` | passage_linkage | 3 | 3 | -> operation (FK to_operation_id->id); -> operation (FK from_operation_id->id); -> passage (FK passage_id->id); -> passage (doc passage_id->id); -> operation (doc from_operation_id->id); -> operation (doc to_operation_id->id) |
| `iba` | `passage_validation_note` | passage_validation_note | 4 | 4 | -> phenomenon (FK phenomenon_id->id); -> passage (FK passage_id->id); -> passage (doc passage_id->id); -> phenomenon (doc phenomenon_id->id) |
| `iba` | `phenomenon` | phenomenon | 177 | 121 | -> hib (FK hib_id->id); -> verse (FK verse_id->id); -> passage (FK passage_id->id); -> passage (doc passage_id->id); -> verse (doc verse_id->id); -> hib (doc hib_id->id); <- operation (FK phenomenon_id->id); <- passage_validation_note (FK phenomenon_id->id); <- operation (doc phenomenon_id->id); <- passage_validation_note (doc phenomenon_id->id) |
| `iba` | `verse_hib` | verse_hib | 485 | 235 | -> hib (FK hib_id->id); -> verse (FK verse_id->id); -> verse (doc verse_id->id); -> hib (doc hib_id->id) |
| `iba` | `verse_passage` | one row per verse-in-a-passage — passage membership (L4b), keeps the … | 25690 | 777 | -> verse (FK verse_id->id); -> passage (FK passage_id->id); -> passage (doc passage_id->id); -> verse (doc verse_id->id) |

### Publishing

11 tables.

| DB | Table | Grain | Total | Live | Relates to (same DB) |
|---|---|---|---|---|---|
| `bible_research` | `prose_section` | one row per id | 1036 | 1036 | -> prose_section_type (FK section_type_id->id); -> word_registry (FK registry_id->id); -> word_registry (doc registry_id->id); -> prose_section_type (doc section_type_id->id); <- prose_section_dimension_link (doc prose_section_id->id); <- prose_section_finding_link (doc prose_section_id->id); <- wa_prose_section_citations (doc prose_section_id->id); <- prose_section_verse_link (doc prose_section_id->id) |
| `bible_research` | `prose_section_finding_link` | one row per (prose_section_id, finding_id, link_type) | 0 | 0 *(no soft-delete col)* | -> wa_session_b_findings (FK finding_id->id); -> prose_section_old_20260905 (FK prose_section_id->id); -> prose_section (doc prose_section_id->id); -> wa_session_b_findings (doc finding_id->id) |
| `bible_research` | `prose_section_fts` | no declared primary key — see cfg_column for prose_section_fts's real… | 1036 | 1036 *(no soft-delete col)* | — |
| `bible_research` | `prose_section_fts_config` | one row per k | 1 | 1 *(no soft-delete col)* | — |
| `bible_research` | `prose_section_fts_content` | one row per id | 1036 | 1036 *(no soft-delete col)* | — |
| `bible_research` | `prose_section_fts_data` | one row per id | 1110 | 1110 *(no soft-delete col)* | — |
| `bible_research` | `prose_section_fts_docsize` | one row per id | 1036 | 1036 *(no soft-delete col)* | — |
| `bible_research` | `prose_section_fts_idx` | one row per (segid, term) | 858 | 858 *(no soft-delete col)* | — |
| `bible_research` | `prose_section_type` | one row per id | 110 | 110 | <- prose_section (FK section_type_id->id); <- prose_section (doc section_type_id->id) |
| `bible_research` | `prose_section_verse_link` | one row per (prose_section_id, verse_reference, link_type) | 0 | 0 *(no soft-delete col)* | -> prose_section_old_20260905 (FK prose_section_id->id); -> prose_section (doc prose_section_id->id) |
| `bible_research` | `wa_prose_section_citations` | one row per id | 562 | 562 | -> wa_session_research_flags (FK cited_sd_pointer_id->id); -> wa_finding_catalogue_links (FK cited_qa_link_id->id); -> wa_session_b_findings (FK cited_finding_id->id); -> prose_section_old_20260905 (FK prose_section_id->id); -> prose_section (doc prose_section_id->id); -> wa_session_b_findings (doc cited_finding_id->id); -> wa_session_research_flags (doc cited_sd_pointer_id->id) |

### Process_control (the app's own tooling — neither research content nor any named stage)

15 tables.

| DB | Table | Grain | Total | Live | Relates to (same DB) |
|---|---|---|---|---|---|
| `bible_research` | `engine_run_log` | one row per id | 891 | 891 *(no soft-delete col)* | <- engine_stream_checkpoint (FK run_id->run_id); <- word_run_state (FK run_id->run_id); <- term_fetch_log (FK run_id->run_id); <- engine_stream_checkpoint (doc run_id->run_id); <- term_fetch_log (doc run_id->run_id); <- word_run_state (doc run_id->run_id) |
| `bible_research` | `engine_stream_checkpoint` | one row per id | 1948 | 1948 *(no soft-delete col)* | -> engine_run_log (FK run_id->run_id); -> engine_run_log (doc run_id->run_id) |
| `bible_research` | `record_change_log` | one row per change event against a covered target row | 1264 | 1264 *(no soft-delete col)* | — |
| `bible_research` | `schema_version` | one row per id | 16 | 16 *(no soft-delete col)* | — |
| `bible_research` | `sources` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `bible_research` | `wa_label_pattern` | one row per id | 11 | 11 *(no soft-delete col)* | — |
| `iba` | `content_index` | one row per (key_type, key_value, file_path, line_number) | 0 | 0 *(no soft-delete col)* | — |
| `iba` | `content_index_scan` | one row per file_path | 0 | 0 *(no soft-delete col)* | — |
| `iba` | `debate_change_detail` | hib_change_detail | 242 | 242 *(no soft-delete col)* | -> run (FK run_id->run_id); -> run (doc run_id->run_id) |
| `iba` | `escalation` | one row per item, current status | 805 | 805 *(no soft-delete col)* | <- escalation_history (FK escalation_id->id); <- escalation_history (doc escalation_id->id) |
| `iba` | `escalation_history` | one row per update to an item, ever | 3023 | 3023 *(no soft-delete col)* | -> escalation (FK escalation_id->id); -> escalation (doc escalation_id->id) |
| `iba` | `file_manifest` | one row per file | 16197 | 16197 *(no soft-delete col)* | — |
| `iba` | `folder_purpose` | one row per governed folder | 959 | 959 *(no soft-delete col)* | — |
| `iba` | `run` | one row per work-package run — the control record | 2694 | 2694 *(no soft-delete col)* | <- validation_result (FK run_id->run_id); <- debate_change_detail (FK run_id->run_id); <- escalations_old (FK run_id->run_id); <- validation_result (doc run_id->run_id); <- escalations_old (doc run_id->run_id); <- debate_change_detail (doc run_id->run_id) |
| `iba` | `validation_result` | one row per check a validate step ran | 48895 | 48895 | -> run (FK run_id->run_id); -> run (doc run_id->run_id) |

---

## (b) Inactive base-data-shaped tables

Unchanged from v1 — this list is unaffected by the scoping error (it was always the `category='data', inactive=1` set). Kept as one list rather than re-split by stage: nearly all of it is legacy Base_data/Analysis material in `bible_research.db`, superseded by the migration to `iba.db` (consistent with `governance.scope_iba_db` — this is *expected*, and is itself evidence the base-data migration was done reasonably completely, unlike the cluster-taxonomy propagation gap in #1535/#1536).

### iba.db — 1 inactive tables

| Table | Grain | Why inactive (from `cfg_table.use`) |
|---|---|---|
| `escalations_old` | one row per researcher interaction — the pause | Historical escalation data, frozen at the 2026-08-20 redesign cutover (v2, corrected retry of the rolled-back 2026-08-19 v1) -- 723 rows, pre-dates e… |

### bible_research.db — 65 inactive tables

| Table | Grain | Why inactive (from `cfg_table.use`) |
|---|---|---|
| `characteristic` | one row per id | The named characteristics belonging to each cluster — the distinct inner-being traits a cluster resolves into, each with a definition. 277 rows acros… |
| `cluster_finding` | one row per id | REDUNDANT (2026-08-29): fully migrated into finding (19,997 rows, provenance=cluster_finding_migration, traceable via source_legacy_ref CF: tag; char… |
| `ib_characteristic_legacy` | no declared primary key — see cfg_column for ib_characteris… | The superseded 29-row inner-being characteristic registry from 2026-07-03, retained as a backup after ib_characteristic was rebuilt on a meaning key.… |
| `lemma_faculty_map` | one row per strongs_number | Maps 1,717 Strong's lemmas to the inner-being faculty or faculties they engage (affect, cognition, volition, moral evaluation and combinations), with… |
| `lexicon` | one row per strong | A flat reference lexicon of 11,666 Strong's entries harvested wholesale from STEP on 2026-06-16 — original-script lemma, transliteration, gloss, medi… |
| `mti_term_cross_refs` | one row per id | Records the registry words that reference a term other than its owning one — the XREF side of term ownership, held as a junction between mti_terms an… |
| `mti_term_flags` | one row per (mti_term_id, flag_id) | Junction attaching Phase 2 triage flags from phase2_flag_types to terms in mti_terms; 1,005 assignments across 785 terms. In practice it uses a very … |
| `mti_term_subgroup` | one row per id | The many-to-many placement of terms into cluster sub-groups, replacing the old single-valued column on mti_terms. 1,196 placements over 740 distinct … |
| `mti_terms` | one row per id | The master term index: one row per Hebrew/Greek/Aramaic term drawn into the study, carrying the term's identity (Strong's, transliteration, gloss, la… |
| `phase2_flag_types` | one row per id | Lookup of the 25 Phase 2 flag codes an analyst may raise against a term, each with a prose definition of when it applies — e.g. thin datasets, God as… |
| `prose_section_dimension_link` | one row per (prose_section_id, dimension_id, link_type) | Declared as a many-to-many link between prose sections and dimensions, with a link_type qualifying the relationship, but it holds 0 rows. It was crea… |
| `term_collection_lexical` | one row per id | Holds collection-level lexical judgements about a term — properties asserted of the term across its whole verse set rather than in any one verse (mut… |
| `term_fetch_log` | one row per id | Per-Strong's-number record of STEP API fetches (2,377 rows), showing what was requested, what it resolved to, and how many verses came back and were … |
| `themes` | one row per id | Declared as a lookup of thematic labels but has 0 rows — created and never used. Nothing in the live model links to it; theme-like grouping is done t… |
| `ve_dimension_scoreboard` | one row per ve_nr | The rule-validation scoreboard for the 18 VE-lexical dimensions (ve_nr 101-118), holding each dimension's rule, its validation verdict and the first … |
| `ve_lexical` | one row per id | The live lexical-analysis store: one row per analytical item read off a verse, keyed to a verse span and a dimension number (ve_nr 101-118 for the ve… |
| `ve_lexical_divinv_pre_reverse_20260626` | no declared primary key — see cfg_column for ve_lexical_div… | A snapshot of 860 divine-involvement items (ve_nr 8, tier T0.1.2) produced by the divine_involvement_read_api pass on 2026-06-16, taken before their … |
| `ve_lexical_divinv_roles_premap_20260626` | no declared primary key — see cfg_column for ve_lexical_div… | A snapshot of 5,187 divine-involvement items (ve_nr 8) taken before the 2026-06-26 remap collapsed them. Comparing it against ve_lexical_legacy row b… |
| `ve_lexical_faculty_backup` | no declared primary key — see cfg_column for ve_lexical_fac… | A snapshot of 29,031 faculty items (ve_nr 7, tier T3) as produced by the v2_engine_iter1 run and dated 2026-06-16, holding the engine's term-meaning … |
| `ve_lexical_faculty_pre_reset_20260626` | no declared primary key — see cfg_column for ve_lexical_fac… | A snapshot of all 29,203 faculty items (ve_nr 7) as they stood immediately before the 2026-06-26 faculty reset. Every id still resolves in ve_lexical… |
| `ve_lexical_faculty_seat_reverse_20260626` | no declared primary key — see cfg_column for ve_lexical_fac… | A snapshot of 1,492 faculty items created on 2026-06-26 by the inferred-seat rule, which assigned a faculty by reading faculty-words elsewhere in the… |
| `ve_lexical_legacy` | one row per id | The previous generation of the lexical store, retired at the 2026-07-02 cutover and kept whole. 507,651 rows, ids 2351222 to 7123084 (no overlap with… |
| `ve_lexical_objtype_premap_20260626` | no declared primary key — see cfg_column for ve_lexical_obj… | A snapshot of 9,534 object-type items (ve_nr 16) taken before the 2026-06-26 remap. The comparison against ve_lexical_legacy is unambiguous: all thre… |
| `ve_lexical_origin_quarantine_20260626` | no declared primary key — see cfg_column for ve_lexical_ori… | A snapshot of 3,623 origin items (ve_nr 6, tier T2.9.1) quarantined on 2026-06-26. Every row is identical: the value 'received-from-outside' asserted… |
| `ve_lexical_overlay_reverse_20260626` | no declared primary key — see cfg_column for ve_lexical_ove… | A snapshot of 1,387 items reversed on 2026-06-26, mixing two dimensions: object-type (ve_nr 16, 1,128 rows) and cause (ve_nr 17, 259 rows), both prod… |
| `ve_lexical_valence_quarantine_20260626` | no declared primary key — see cfg_column for ve_lexical_val… | A snapshot of 26,993 valence items (ve_nr 21, tier T0.3.1) quarantined on 2026-06-26 — the largest withdrawal recorded in this group. All 26,993 ids … |
| `ve_lexical_verification` | one row per id | A small manual verification log: 46 hand-checked ve_lexical items, all of dimension 101 (sense) and all checked on 2026-07-14, recording whether the … |
| `ve_verification_sample` | one row per (ve_nr, verse_span_id) | The drawn sampling frame for verifying the lexical layer: 3,332 (ve_nr, verse_span_id) pairs selected across 18 dimensions from Psalms (book 19) and … |
| `verse` | one row per id | The master verse table and the anchor of the whole verse layer: one row per verse of the ESV text (25,634 rows, all 66 books), each with its text, ca… |
| `verse_context` | one row per id | The term-in-verse classification record (55,775 rows): for one verse-record and one MTI term it holds whether that occurrence is relevant to the stud… |
| `verse_context_group` | one row per id | The catalogue of verse-context groups (VCGs) — named groupings of term-in-verse occurrences that share a context, referenced by verse_context.group_i… |
| `verse_coverage` | one row per verse_id | A derived, materialised roll-up of study coverage per verse — how many spans, study terms and lexical units each verse carries, and whether it is in … |
| `verse_coverage_morphology` | one row per id | A per-word morphology extract for a narrow set of verses — 2,877 word rows covering only 326 distinct references, concentrated in Leviticus, Proverbs… |
| `verse_evidence_index` | no declared primary key — see cfg_column for verse_evidence… | The fan-in index that answers 'what evidence is bound to this verse' — 804,805 rows mapping a verse to each piece of evidence held against it, so a v… |
| `verse_evidence_orphan` | no declared primary key — see cfg_column for verse_evidence… | The reject log of the verse_evidence_index build: 222 evidence rows that could not be bound to a verse. Every row has the same single cause, making t… |
| `verse_morph_complexity` | one row per verse_id | A derived per-verse syntactic complexity profile counting content words, finite and non-finite verbs, conjunctions, prepositions and subordinators, w… |
| `verse_morphology` | one row per id | The morphological backbone of the layer: one row per word of every verse (325,507 rows), carrying the surface form, Strong's tag, morph_code and the … |
| `verse_morphology_raw` | one row per verse_id | The raw STEP HTML behind the parsed morphology — one row per verse (25,634, i.e. complete cover of the master verse table), kept so the parse in vers… |
| `verse_span_index` | one row per id | The working analytical surface over word spans (325,474 rows): it reproduces verse_morphology's columns almost exactly and adds the analytical overla… |
| `verse_term_index` | no declared primary key — see cfg_column for verse_term_ind… | A minimal derived lookup of which Strong's terms appear in which verse (275,593 rows, no primary key, indexed both ways). It is a de-duplicated proje… |
| `wa_addendum_registry` | one row per id | A one-off audit artefact: 22 observations from the April 2026 global-rules audit, each recording a problem with a rule and where its content should m… |
| `wa_cross_registry_links` | one row per id | 158 researcher-authored links between registry words, each naming the connecting Hebrew or Greek term and explaining the connection in prose — the pr… |
| `wa_crosslink_type` | one row per id | The 11 kinds of relationship that may connect two registry words, e.g. shared root, semantic opposition, causative chain. It is the controlled vocabu… |
| `wa_dim_review_cluster_log` | one row per id | A completion log for the retired dimension review: one row per C-code cluster finished, six in all (C10, C13, C17, C20, C21, C22), recorded between 2… |
| `wa_dimension_index` | one row per id | The retired dimension-review layer: 3,509 rows, one per verse_context_group, recording which of 20 named dimensions the group was assigned to and how… |
| `wa_file_index` | one row per id | One row per input file (or engine onboarding stub) that supplied a registry word's data, with the file's provenance, split-part structure and specifi… |
| `wa_file_name_pattern` | one row per id | The 23 registered filename conventions used across the programme, each given as a template such as 'wa-dim-{cluster}-extract-{YYYYMMDD}.json' with th… |
| `wa_finding_catalogue_links` | one row per id | REDUNDANT (2026-08-29): 5,456 of 6,199 rows migrated into finding_question_link (finding_id remapped via the wa_session_b_findings->finding SB: tag),… |
| `wa_flag_type_question_link` | one row per id | Maps quality-flag types to the catalogue questions that a raised flag should prompt. REDUNDANT (2026-08-29): all 12 rows link to questions that are s… |
| `wa_lsj_parsed` | one row per id | Structured parse of the Liddell-Scott-Jones classical Greek lexicon entry for a term, splitting the raw entry into gloss, domains, and philosophical … |
| `wa_meaning_parsed` | one row per id | One header row per inventory term for its parsed definition, holding the counts and derived flags of the parse whose detail lives in wa_meaning_sense… |
| `wa_meaning_sense` | one row per id | The parsed sense hierarchy of a term's definition: 17,125 rows, one per numbered sense, keyed to wa_meaning_parsed and ordered by the source's own nu… |
| `wa_meaning_stem` | one row per id | Breaks a Hebrew verb's definition down by verbal stem (Qal, Piel, Hiphil and so on) with the sense each stem carries. Effectively unused: 13 rows cov… |
| `wa_patch_type_registry` | one row per id | The 20 recognised JSON patch types, each naming the instruction that governs it and the tables it writes to — the reference-as-database record of wha… |
| `wa_rule_registry` | one row per id | The programme's global rules held as data: 59 rules with their text, rationale, application notes and supersession chain, all imported from a single … |
| `wa_session_b_dimensions` | one row per id | A near-empty remnant of the Session B per-word dimensional assessment: just 2 rows, for registries 112 and 182, raised on 27 and 28 March 2026 under … |
| `wa_session_b_findings` | one row per id | The superseded per-word Session B findings store: 2,883 findings raised April to May 2026 across 112 registries, since replaced by the universal find… |
| `wa_term_inventory` | one row per id | The per-registry term inventory: one row per term as held under a given English word's file, carrying the STEP-sourced identity, gloss, meaning text,… |
| `wa_term_phase2_flags` | one row per (term_inv_id, flag_id) | Junction attaching Phase 2 triage flags from phase2_flag_types to inventory terms: 1,570 assignments over 883 terms, using 25 distinct flag types. Br… |
| `wa_term_related_words` | one row per id | The related-word web: 103,944 rows attaching each inventory term to other lemmas STEP reports as related, by gloss, transliteration and Strong's. Ove… |
| `wa_term_root_family` | one row per id | Assigns inventory terms to a shared etymological root family by root code, so terms from one root (e.g. CHARAH, 'burn/anger') can be worked together.… |
| `wa_verse_records` | one row per id | The legacy per-term-in-verse occurrence store (247,046 rows) that predates the master verse table — one row per term found in a verse, with the verse… |
| `wa_verse_term_links` | one row per id | The junction between a wa_verse_records occurrence and a wa_term_inventory term (237,531 rows), unique on (verse_id, term_inv_id) and carrying the ST… |
| `word_registry` | one row per id | The programme's lexical entry point: one row per English inner-life word (222 rows), carrying the word's definition, provenance, cluster assignment a… |
| `word_run_state` | one row per id | Per-word outcome of each engine run: which phase the word reached, what the audit concluded and why it stopped. 539 rows over 373 runs — the audit's … |

---

## (c) Every table in both schemas, validated against (a) + (b)

Unchanged mechanics from v1 (this part was never wrong) — ground truth from each database's own `sqlite_master`, reconciled by name against `cfg_table`:

| Database | Physical tables | Registered in `cfg_table` | Physical, not registered | Registered, no physical table |
|---|---|---|---|---|
| `iba` | 78 | 78 | none | none |
| `bible_research` | 113 | 113 | none | none |

**Still zero gaps in either direction, both databases** — that finding stands unchanged from v1.

Partition by `cfg_table.category` (v1's axis) still sums correctly:

| Category | iba.db | bible_research.db | Total |
|---|---|---|---|
| Live `data` category | 41 | 48 | 89 |
| Inactive `data` category | 1 | 65 | 66 |
| `rule`+`log` (`cfg_*`) | 36 | 0 | 36 |
| **Total** | **78** | **113** | **191** |

But `category='data'` conflates four different things — the correction in this v2. The SAME 89 live rows, now by actual stage (Claude's judgement call, see the caveat above; #1539 is the fix for not having to guess):

| Stage | Count | Note |
|---|---|---|
| Base_data (true) | 15 | the actual answer to the original request |
| Base_data (retracted subsystem) | 3 | candidate_seed/span_candidate/lemma_inventory — pending #1528-#1531 |
| Base_data (static reference) | 2 | books/book_code_variants |
| Analysis | 43 | finding/cluster/hib/phenomenon/passage families etc. |
| Publishing | 11 | prose_section family |
| Process_control | 15 | escalation/run/validation_result/file_manifest etc. |
| **Total** | **89** | matches the 89 live-`data`-category count above |

---

## (d) `cfg_*` (rule/log) tables relating to each data-category table

**Scope note (v2):** this section answers "which `cfg_*` tables relate to a `category='data'` table" — that is the full 89-table v1 set (Base_data + Analysis + Publishing + Process_control together), not the narrower true-Base_data set alone. The mechanics below are unchanged from v1 (they were never wrong, only mis-labelled by the surrounding scoping error) and are kept intact rather than re-run, since re-scoping to Base_data-only would just be this same table filtered to 15 rows — the full set is more useful here.

**1. Universal, by governance design (every one of the 89, no exceptions):** `cfg_table` (registers the row) and `cfg_column` (registers every column, per `governance.table_columns`).

**2. Partial registries** — `cfg_index`, `cfg_unique`, `cfg_write_grant`, `cfg_report_csv_table` — membership unchanged from v1; see the archived v1 report for the full per-table matrix (49 of 89 tables have at least one hit). Not repeated here to keep this version focused on what changed.

**3. Direct FK / documented-FK from a `cfg_*` table into a data table:**

| From (`cfg_*`) | Column | To | Status |
|---|---|---|---|
| `iba.cfg_change_detail` (log) | `run_id` -> `run_id` | `iba.run` | active |
| `iba.cfg_lexical_code_class` (rule) | `strong_code` -> `strongNumber` | `iba.strong` | INACTIVE (table retired, escalation #1502-1505, 2026-09-05) |

**4. Cross-database references** — unchanged from v1 (3 documented-only references; see v1/archive for the full table). One addition this version: the cluster-authority relationship (#1535) is a *fifth* cross-database relationship this axis should have caught and didn't, because it isn't a column-level reference at all — it's a table-level claim of authority sitting in one table's own `use` text with no reciprocal marker on the other side. Documented fully in Finding F7 below.

---

## Findings — the complete, tracked list

Every finding below has its own escalation carrying full seed evidence for review — this section is an index and summary, not the record of truth (the escalations are). None of these are fixed yet; all are `raised`/`re-assigned`, `DecisionRequired`, awaiting the researcher.

### F1 — `cfg_index`/`cfg_report_csv_table` lack the `database` disambiguator their siblings have — **escalation #1534**
`cfg_table`/`cfg_column`/`cfg_write_grant`/`cfg_unique` were widened to `(database, table_name)` after #653/#680 established both databases share table names for different tables. `cfg_index`/`cfg_report_csv_table` were not. `cluster` and `passage` are live in both databases simultaneously and both appear in these two registries — no live misattribution today (every current row traces to an iba dispatcher step), but nothing in the schema prevents one.

### F2 — `cfg_table_purpose`/`cfg_change_detail` checked, not a risk
Both key on a bare `table_name` too, but their own documentation confirms the values are always `cfg_*` rule-table names, which are unique by construction. No escalation needed — recorded here so the check is visible, not silently skipped.

### F3 — Dangling FK: 4 tables reference a dropped table, 562 live rows affected — **escalation #1533**
`wa_prose_section_citations` (562 rows), `prose_section_finding_link`, `prose_section_verse_link`, `prose_section_dimension_link` all declare `REFERENCES "prose_section_old_20260905"(id)` — a table that does not physically exist. Distinct from the already-documented "points at a superseded-but-real legacy table" issue on the same tables. `PRAGMA foreign_keys` is off by default so no writes are failing today, but the constraint is unenforceable and would break silently if enforcement were ever turned on.

### F4 — 9 live tables carry FK dependencies on tables this same report classifies inactive — **escalation #1537**
`characteristic_subgroup`/`cluster_observation` → `characteristic`; `vcg_term` → `mti_terms` **and** `verse_context_group`; `prose_section`/`wa_obs_question_catalogue`/`wa_session_research_flags` → `word_registry`; `wa_finding_entity_links`/`prose_section_finding_link`/`wa_prose_section_citations` → `wa_session_b_findings`/`wa_finding_catalogue_links`. The `word_registry` cases are the sharpest: `bible_research.word_registry` is inactive because the live registry moved to `iba.db`, and project memory already records that the two registries' numbering **differs** — so these three columns are keyed to a divergent numbering scheme, not just "an old but harmless pointer." (`wa_session_research_flags` → `wa_file_index` is the one case that's fine — an already-documented, accepted legacy bypass.)

### F5 — Extreme, uncommented soft-delete ratios — **escalation #1538**
`passage`: 42 live of 18,558 (99.8% deleted). `verse_passage`: 777 of 25,690 (97%). `hib_referent_option`: 0 of 5 (100% — every row deleted). Verified against the real `deleted` column distribution, not inferred. May be normal churn from iterative L4b passage-building — was never confirmed either way, and a functionally-100%-dead table sitting at `inactive=0` deserves the same scrutiny as the #1528 pattern.

### F6 — The report's own "base data" scope was wrong — **escalation #1539**
Covered in full above (see "What was wrong with v1, and why"). The report-level error is corrected here (self-correctable). The underlying gap — no `cfg_*` field records a table's programme stage — is the escalated, researcher-decision part.

### F7 — No authoritative link between the two `cluster` tables, and it has already caused live data drift — **escalations #1535 (structural) + #1536 (quantified)**
`iba.cluster` claims to be the canonical successor of `bible_research.cluster` — but only in its own `use` text, one-directionally. `bible_research.cluster` gives no reciprocal acknowledgement (no inactive flag, no deprecation note), has no column capable of marking a row retired, and has been informally overloading its `status` column for this since at least June — including a live disagreement: `bible_research.cluster.status` says `M10c` was "Merged into M10 (2026-06-23)"; `iba.cluster` currently carries `M10c` as a live, standalone cluster. Consequence, quantified: **9,243** `bible_research.finding` rows and **142** `mti_terms` rows still carry 4 codes (`M17`/`M27`/`M29`/`M38`) that escalation #1525 retired via merge *this morning*, and **45 of `iba.cluster`'s 89 live codes** (the entire 2026-08-11 taxonomy-rebuild growth) have never been used anywhere in `bible_research.db` at all — cross-database cluster tagging has effectively been frozen for a month, and today's merges are just the newest, smallest instance of a much larger, pre-existing gap.

---

## Process guardrail — how this is being prevented from recurring

A new `cfg_behaviour_rule` (class=`development`, `rule_key=audit-deliverable-cross-check-before-presenting`) has been proposed via `configmaint.propose` — **`RUN-20260906_213742_853-CONFIGMAINT`, paused for researcher approval.** It requires, before any audit/validation-style deliverable is presented as findings: (1) cross-checking the open escalation queue for the same tables/domain, (2) cross-checking governance/`cfg_setting` definitions of any scoping term used, and (3) cross-checking the deliverable's own generated data for internal self-contradiction. This is a direct, durable response to how v1 was produced — every finding in this v2 was reachable from context already loaded before v1 was written; none required new information, only the cross-check v1 skipped.

---

## Escalation index for this validation

| # | What | State |
|---|---|---|
| #1532 | Parent — this validation itself | ready_for_approval |
| #1533 | F3 — dangling FK to dropped table | raised |
| #1534 | F1 — registry database-disambiguator gap | raised |
| #1535 | F7 — no cluster-table authority link (structural) | raised |
| #1536 | F7 — stale cross-DB cluster tags (quantified) | raised |
| #1537 | F4 — live tables FK into inactive tables | raised |
| #1538 | F5 — extreme soft-delete ratios | raised |
| #1539 | F6 — missing programme-stage classification field | raised |
| `RUN-20260906_213742_853-CONFIGMAINT` | Guardrail — cross-check-before-presenting rule | paused, awaiting approval |

Nothing from this validation exists only in chat — every row above is a live, queryable record.
