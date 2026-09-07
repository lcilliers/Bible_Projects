# Raw Data Integrity Validation — Both Databases

*Escalation #1532. Generated 2026-09-06, from a live, direct query pass against `iba/app/db/iba.db` and `database/bible_research.db` plus their `cfg_table`/`cfg_column`/`cfg_index`/`cfg_unique`/`cfg_write_grant`/`cfg_report_csv_table` registrations — no step of this report is drawn from memory or from a prior document.*

## Method — how "base" is defined, grounded in live config

`cfg_table.category` (queried live) has exactly three values across both databases: `data`, `rule`, `log`. `rule` and `log` are entirely the `cfg_*` governance/audit apparatus (config settings, write grants, escalation machinery, change logs) — every single `rule`/`log` row is a `cfg_*`-prefixed table. `data` is every substantive project table in both databases — the base data this validation is scoped to. This gives a definition sourced directly from the config, not assumed:

- **base table** = `cfg_table.category = 'data'`
- **live base table** = `category='data' AND inactive=0`
- **inactive base table** = `category='data' AND inactive=1`
- **non-base table** = `category IN ('rule','log')` — the `cfg_*` series

**Totals:** 89 live base tables (41 iba, 48 bible_research) + 66 inactive base tables (1 iba, 65 bible_research) + 36 non-base `cfg_*` tables (all iba, 34 active + 2 inactive) = **191 `cfg_table` rows total**.

---

## (a) Live base data tables — relationships and live record counts

Row count columns: **Total** = `COUNT(*)`; **Live** = rows surviving the table's own soft-delete convention where one is registered in `cfg_column` (`deleted`/`delete_flagged` = 0 or NULL) — 49 of the 89 live base tables carry such a column, live in **cfg_column**, queried directly per row, not assumed uniform. Where no such column exists, Total *is* the live count (nothing to filter). **Relates to (base)** lists real, DB-enforced FKs (`PRAGMA foreign_key_list`) and documented-only references (`cfg_column.fk`, not enforced by SQLite) to/from other base tables in the SAME database — cross-database and non-base relations are in §(d), kept separate so this table answers only "how does the base-data layer itself hang together."

### iba.db — 41 live base tables

| Table | Grain | Total | Live | Relates to (base, this DB) |
|---|---|---|---|---|
| `candidate_seed` | one row per assessed lemma — the over-inclusive Axis-A candidate assessment | 2087 | 1806 | → lemma_inventory (FK lemma_key→lemma_key); → lemma_inventory (doc lemma_key→lemma_key); → strong (doc strong_variant→strongNumber) |
| `cluster` | one row per cluster (M01-M46 + FLAG + T2) — the inner-being dimension taxonomy | 94 | 89 | ← cluster_strong (FK cluster_code→cluster_code); ← cluster_strong (doc cluster_code→cluster_code) |
| `cluster_strong` | one row per (strong, cluster_code) assignment | 8929 | 7419 | → cluster (FK cluster_code→cluster_code); → strong (FK strong→strongNumber); → strong (doc strong→strongNumber); → cluster (doc cluster_code→cluster_code) |
| `content_index` | one row per (key_type, key_value, file_path, line_number) | 0 | 0 *(no soft-delete col)* | — |
| `content_index_scan` | one row per file_path | 0 | 0 *(no soft-delete col)* | — |
| `debate_change_detail` | hib_change_detail | 242 | 242 *(no soft-delete col)* | → run (FK run_id→run_id); → run (doc run_id→run_id) |
| `escalation` | one row per item, current status | 805 | 805 *(no soft-delete col)* | ← escalation_history (FK escalation_id→id); ← escalation_history (doc escalation_id→id) |
| `escalation_history` | one row per update to an item, ever | 3023 | 3023 *(no soft-delete col)* | → escalation (FK escalation_id→id); → escalation (doc escalation_id→id) |
| `file_manifest` | one row per file | 16197 | 16197 *(no soft-delete col)* | — |
| `folder_purpose` | one row per governed folder | 959 | 959 *(no soft-delete col)* | — |
| `hib` | hib | 63 | 21 | → verse (FK first_verse_id→id); → verse (doc first_verse_id→id); ← hib_referent_option (FK hib_id→id); ← verse_hib (FK hib_id→id); ← phenomenon (FK hib_id→id); ← operation_party (FK hib_id→id); ← hib_referent_option (doc hib_id→id); ← verse_hib (doc hib_id→id); ← phenomenon (doc hib_id→id); ← operation_party (doc hib_id→id) |
| `hib_referent_option` | hib_referent_option | 5 | 0 | → hib (FK hib_id→id); → hib (doc hib_id→id) |
| `lemma_inventory` | one row per corpus lemma (base Strong's) — the INDEPENDENT substrate the seed net runs ov… | 11781 | 11781 | ← candidate_seed (FK lemma_key→lemma_key); ← candidate_seed (doc lemma_key→lemma_key) |
| `operation` | operation | 177 | 121 | → phenomenon (FK phenomenon_id→id); → phenomenon (doc phenomenon_id→id); ← operation_party (FK operation_id→id); ← passage_linkage (FK to_operation_id→id); ← passage_linkage (FK from_operation_id→id); ← operation_party (doc operation_id→id); ← passage_linkage (doc from_operation_id→id); ← passage_linkage (doc to_operation_id→id) |
| `operation_party` | operation_party | 250 | 136 | → hib (FK hib_id→id); → operation (FK operation_id→id); → operation (doc operation_id→id); → hib (doc hib_id→id) |
| `passage` | one row per passage — a reading frame (global, per book) | 18558 | 42 | → verse (FK anchor_verse_id→id); → verse (doc anchor_verse_id→id); ← verse_passage (FK passage_id→id); ← phenomenon (FK passage_id→id); ← passage_linkage (FK passage_id→id); ← passage_insufficiency (FK passage_id→id); ← passage_emergent_question (FK passage_id→id); ← passage_validation_note (FK passage_id→id); ← verse_lexical_note (FK passage_id→id); ← verse_passage (doc passage_id→id); ← phenomenon (doc passage_id→id); ← passage_linkage (doc passage_id→id); ← passage_insufficiency (doc passage_id→id); ← passage_emergent_question (doc passage_id→id); ← passage_validation_note (doc passage_id→id); ← verse_lexical_note (doc passage_id→id) |
| `passage_emergent_question` | passage_emergent_question | 4 | 3 | → verse (FK verse_id→id); → passage (FK passage_id→id); → passage (doc passage_id→id); → verse (doc verse_id→id) |
| `passage_insufficiency` | passage_insufficiency | 1 | 1 | → verse (FK verse_id→id); → passage (FK passage_id→id); → passage (doc passage_id→id); → verse (doc verse_id→id) |
| `passage_linkage` | passage_linkage | 3 | 3 | → operation (FK to_operation_id→id); → operation (FK from_operation_id→id); → passage (FK passage_id→id); → passage (doc passage_id→id); → operation (doc from_operation_id→id); → operation (doc to_operation_id→id) |
| `passage_validation_note` | passage_validation_note | 4 | 4 | → phenomenon (FK phenomenon_id→id); → passage (FK passage_id→id); → passage (doc passage_id→id); → phenomenon (doc phenomenon_id→id) |
| `phenomenon` | phenomenon | 177 | 121 | → hib (FK hib_id→id); → verse (FK verse_id→id); → passage (FK passage_id→id); → passage (doc passage_id→id); → verse (doc verse_id→id); → hib (doc hib_id→id); ← operation (FK phenomenon_id→id); ← passage_validation_note (FK phenomenon_id→id); ← operation (doc phenomenon_id→id); ← passage_validation_note (doc phenomenon_id→id) |
| `run` | one row per work-package run — the control record | 2694 | 2694 *(no soft-delete col)* | ← validation_result (FK run_id→run_id); ← debate_change_detail (FK run_id→run_id); ← escalations_old (FK run_id→run_id); ← validation_result (doc run_id→run_id); ← escalations_old (doc run_id→run_id); ← debate_change_detail (doc run_id→run_id) |
| `span` | ONE ROW PER HTML <span> TAG of a verse (O3) - a tag's codes are a combined unit as STEP i… | 391417 | 378149 | → strong (FK strong_variant→strongNumber); → verse (FK verse_id→id); → verse (doc verse_id→id); ← span_candidate (FK span_id→id); ← verse_lexical (FK span_id→id); ← span_candidate (doc span_id→id); ← verse_lexical (doc span_id→id) |
| `span_candidate` | one row per CANDIDATE span (existence = candidate) — the L4b stamp over the L4a span | 83914 | 83914 | → span (FK span_id→id); → span (doc span_id→id) |
| `strong` | one row per strong — unique, global to the study | 15293 | 15293 | ← word_strong (FK strong→strongNumber); ← strong_sense (FK strong→strongNumber); ← strong_lexicon (FK strong→strongNumber); ← strong_verse (FK strong→strongNumber); ← span (FK strong_variant→strongNumber); ← strong_lsj_parsed (FK strong→strongNumber); ← strong_mounce_parsed (FK strong→strongNumber); ← strong_related (FK strong→strongNumber); ← verse_lexical (FK strong→strongNumber); ← strong_meaning_parsed (FK strong_variant→strongNumber); ← strong_meaning_tree (FK strong_variant→strongNumber); ← cluster_strong (FK strong→strongNumber); ← word_strong (doc strong→strongNumber); ← strong_sense (doc strong→strongNumber); ← strong_meaning_tree (doc strong_variant→strongNumber); ← strong_lexicon (doc strong→strongNumber); ← strong_verse (doc strong→strongNumber); ← candidate_seed (doc strong_variant→strongNumber); ← strong_meaning_parsed (doc strong_variant→strongNumber); ← strong_lsj_parsed (doc strong→strongNumber); ← strong_mounce_parsed (doc strong→strongNumber); ← strong_related (doc strong→strongNumber); ← verse_lexical (doc strong→strongNumber); ← verse_lexical (doc language→language); ← cluster_strong (doc strong→strongNumber) |
| `strong_lexicon` | one row per strong that has LSJ/Mounce (Greek) | 5639 | 5639 | → strong (FK strong→strongNumber); → strong (doc strong→strongNumber) |
| `strong_lsj_parsed` | one row per LSJ sense of a strong_lexicon.lsj entry (2026-07-25 corrected parse) | 36199 | 36199 | → strong (FK strong→strongNumber); → strong (doc strong→strongNumber) |
| `strong_meaning_parsed` | one row per gloss segment of a strong_meaning_tree lemma (2026-07-25 corrected parse) | 47113 | 47113 | → strong (FK strong_variant→strongNumber); → strong (doc strong_variant→strongNumber) |
| `strong_meaning_tree` | one row per sense-node of a LEMMA's definition tree | 40315 | 40315 | → strong (FK strong_variant→strongNumber); → strong (doc strong_variant→strongNumber) |
| `strong_mounce_parsed` | one row per Mounce sense of a strong_lexicon.mounce entry (2026-07-25 corrected parse) | 5742 | 5742 | → strong (FK strong→strongNumber); → strong (doc strong→strongNumber) |
| `strong_related` | one row per (strong, related strong) pair STEP's getInfo returned (fetched 2026-07-25) | 87535 | 87535 | → strong (FK strong→strongNumber); → strong (doc strong→strongNumber) |
| `strong_sense` | one row per strong — the sense HEAD | 15293 | 15293 | → strong (FK strong→strongNumber); → strong (doc strong→strongNumber) |
| `strong_verse` | one row per (strong, verse) — unique. The m:m index. | 132718 | 132718 | → verse (FK verse_id→id); → strong (FK strong→strongNumber); → strong (doc strong→strongNumber); → verse (doc verse_id→id) |
| `validation_result` | one row per check a validate step ran | 48895 | 48895 | → run (FK run_id→run_id); → run (doc run_id→run_id) |
| `verse` | one row per verse — unique. Does NOT belong to a strong. | 29759 | 29759 | ← strong_verse (FK verse_id→id); ← span (FK verse_id→id); ← passage (FK anchor_verse_id→id); ← verse_passage (FK verse_id→id); ← hib (FK first_verse_id→id); ← verse_hib (FK verse_id→id); ← phenomenon (FK verse_id→id); ← passage_insufficiency (FK verse_id→id); ← passage_emergent_question (FK verse_id→id); ← verse_lexical (FK verse_id→id); ← verse_lexical_note (FK verse_id→id); ← strong_verse (doc verse_id→id); ← span (doc verse_id→id); ← passage (doc anchor_verse_id→id); ← verse_passage (doc verse_id→id); ← verse_lexical (doc verse_id→id); ← hib (doc first_verse_id→id); ← verse_hib (doc verse_id→id); ← phenomenon (doc verse_id→id); ← passage_insufficiency (doc verse_id→id); ← passage_emergent_question (doc verse_id→id); ← verse_lexical_note (doc verse_id→id) |
| `verse_hib` | verse_hib | 485 | 235 | → hib (FK hib_id→id); → verse (FK verse_id→id); → verse (doc verse_id→id); → hib (doc hib_id→id) |
| `verse_lexical` | one row per Strong's code within a span (span_id, code_ordinal) — a compound span yields … | 975460 | 544572 | → strong (FK strong→strongNumber); → verse (FK verse_id→id); → span (FK span_id→id); → span (doc span_id→id); → verse (doc verse_id→id); → strong (doc strong→strongNumber); → strong (doc language→language); ← verse_lexical_note (FK target_verse_lexical_id→id); ← verse_lexical_note (FK verse_lexical_id→id); ← verse_lexical_note (doc verse_lexical_id→id); ← verse_lexical_note (doc target_verse_lexical_id→id) |
| `verse_lexical_note` | one row per (verse_lexical_id, note_type) — the judgement-bearing Layer-2 finding for one… | 173 | 173 | → verse_lexical (FK target_verse_lexical_id→id); → passage (FK passage_id→id); → verse (FK verse_id→id); → verse_lexical (FK verse_lexical_id→id); → verse_lexical (doc verse_lexical_id→id); → verse (doc verse_id→id); → passage (doc passage_id→id); → verse_lexical (doc target_verse_lexical_id→id) |
| `verse_passage` | one row per verse-in-a-passage — passage membership (L4b), keeps the raw verse pristine | 25690 | 777 | → verse (FK verse_id→id); → passage (FK passage_id→id); → passage (doc passage_id→id); → verse (doc verse_id→id) |
| `word_registry` | one row per English inner-being word | 180 | 180 | ← word_strong (FK word_id→id); ← word_strong (doc word_id→id) |
| `word_strong` | one row per (word, strong) the STEP word-search returned | 4874 | 4874 | → strong (FK strong→strongNumber); → word_registry (FK word_id→id); → word_registry (doc word_id→id); → strong (doc strong→strongNumber) |

### bible_research.db — 48 live base tables

| Table | Grain | Total | Live | Relates to (base, this DB) |
|---|---|---|---|---|
| `book_code_variants` | one row per code | 112 | 112 *(no soft-delete col)* | → books (FK book_id→id); → books (doc book_id→id) |
| `books` | one row per id | 66 | 66 *(no soft-delete col)* | ← book_code_variants (FK book_id→id); ← wa_verse_records (FK book_id→id); ← book_code_variants (doc book_id→id); ← wa_verse_records (doc book_id→id) |
| `characteristic_subgroup` | one row per id | 146 | 146 | → cluster_subgroup (FK cluster_subgroup_id→id); → characteristic (FK characteristic_id→id); → characteristic (doc characteristic_id→id); → cluster_subgroup (doc cluster_subgroup_id→id) |
| `cluster` | one row per cluster_code | 49 | 49 *(no soft-delete col)* | ← cluster_subgroup (FK cluster_code→cluster_code); ← cluster_finding (FK cluster_code→cluster_code); ← cluster_finding (doc cluster_code→cluster_code); ← cluster_subgroup (doc cluster_code→cluster_code) |
| `cluster_observation` | one row per id | 276 | 276 | → cluster_subgroup (FK cluster_subgroup_id→id); → characteristic (FK characteristic_id→id); → characteristic (doc characteristic_id→id); → cluster_subgroup (doc cluster_subgroup_id→id) |
| `cluster_subgroup` | one row per id | 175 | 156 | → cluster (FK cluster_code→cluster_code); → cluster (doc cluster_code→cluster_code); ← mti_term_subgroup (FK cluster_subgroup_id→id); ← verse_context (FK cluster_subgroup_id→id); ← characteristic_subgroup (FK cluster_subgroup_id→id); ← cluster_observation (FK cluster_subgroup_id→id); ← cluster_finding (FK cluster_subgroup_id→id); ← characteristic_subgroup (doc cluster_subgroup_id→id); ← cluster_finding (doc cluster_subgroup_id→id); ← cluster_observation (doc cluster_subgroup_id→id); ← mti_term_subgroup (doc cluster_subgroup_id→id); ← verse_context (doc cluster_subgroup_id→id) |
| `engine_run_log` | one row per id | 891 | 891 *(no soft-delete col)* | ← engine_stream_checkpoint (FK run_id→run_id); ← word_run_state (FK run_id→run_id); ← term_fetch_log (FK run_id→run_id); ← engine_stream_checkpoint (doc run_id→run_id); ← term_fetch_log (doc run_id→run_id); ← word_run_state (doc run_id→run_id) |
| `engine_stream_checkpoint` | one row per id | 1948 | 1948 *(no soft-delete col)* | → engine_run_log (FK run_id→run_id); → engine_run_log (doc run_id→run_id) |
| `finding` | one row per id | 458096 | 53339 | ← finding_verse_index (doc finding_id→id) |
| `finding_citation` | one row per id | 51148 | 51148 | — |
| `finding_question_link` | one row per id | 357657 | 357315 | — |
| `finding_revision` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `finding_verse_index` | one row per id | 475790 | 475790 *(no soft-delete col)* | → finding (doc finding_id→id) |
| `finding_verse_link` | one row per id | 3659 | 3649 | — |
| `ib_characteristic` | one row per id | 1634 | 1634 *(no soft-delete col)* | — |
| `ib_observation` | one row per id | 81 | 81 *(no soft-delete col)* | — |
| `passage` | one row per id | 4296 | 4296 *(no soft-delete col)* | — |
| `prose_section` | one row per id | 1036 | 1036 | → prose_section_type (FK section_type_id→id); → word_registry (FK registry_id→id); → word_registry (doc registry_id→id); → prose_section_type (doc section_type_id→id); ← prose_section_dimension_link (doc prose_section_id→id); ← prose_section_finding_link (doc prose_section_id→id); ← wa_prose_section_citations (doc prose_section_id→id); ← prose_section_verse_link (doc prose_section_id→id) |
| `prose_section_finding_link` | one row per (prose_section_id, finding_id, link_type) | 0 | 0 *(no soft-delete col)* | → wa_session_b_findings (FK finding_id→id); → prose_section_old_20260905 (FK prose_section_id→id); → prose_section (doc prose_section_id→id); → wa_session_b_findings (doc finding_id→id) |
| `prose_section_fts` | no declared primary key — see cfg_column for prose_section_fts's real columns | 1036 | 1036 *(no soft-delete col)* | — |
| `prose_section_fts_config` | one row per k | 1 | 1 *(no soft-delete col)* | — |
| `prose_section_fts_content` | one row per id | 1036 | 1036 *(no soft-delete col)* | — |
| `prose_section_fts_data` | one row per id | 1110 | 1110 *(no soft-delete col)* | — |
| `prose_section_fts_docsize` | one row per id | 1036 | 1036 *(no soft-delete col)* | — |
| `prose_section_fts_idx` | one row per (segid, term) | 858 | 858 *(no soft-delete col)* | — |
| `prose_section_type` | one row per id | 110 | 110 | ← prose_section (FK section_type_id→id); ← prose_section (doc section_type_id→id) |
| `prose_section_verse_link` | one row per (prose_section_id, verse_reference, link_type) | 0 | 0 *(no soft-delete col)* | → prose_section_old_20260905 (FK prose_section_id→id); → prose_section (doc prose_section_id→id) |
| `record_change_log` | one row per change event against a covered target row | 1264 | 1264 *(no soft-delete col)* | — |
| `reread_worklist` | one row per id | 150 | 150 *(no soft-delete col)* | — |
| `schema_version` | one row per id | 16 | 16 *(no soft-delete col)* | — |
| `segment_unit` | one row per id | 877 | 788 | — |
| `segment_unit_verse` | one row per (unit_id, verse_id) | 11276 | 11276 *(no soft-delete col)* | — |
| `session_d_observations` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `session_d_runs` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `session_d_term_links` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `session_d_verse_links` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `sources` | one row per id | 0 | 0 *(no soft-delete col)* | — |
| `vcg_term` | one row per id | 5091 | 1998 | → mti_terms (FK mti_term_id→id); → verse_context_group (FK vcg_id→id); → verse_context_group (doc vcg_id→id); → mti_terms (doc mti_term_id→id) |
| `verse_analysis_progress` | one row per id | 33 | 33 *(no soft-delete col)* | — |
| `wa_data_quality_flags` | one row per id | 0 | 0 | → wa_quality_flag_types (FK flag_id→id); → wa_quality_flag_types (doc flag_id→id) |
| `wa_finding_entity_links` | one row per id | 287 | 287 | → wa_session_b_findings (FK finding_id→id); → wa_session_b_findings (doc finding_id→id) |
| `wa_label_pattern` | one row per id | 11 | 11 *(no soft-delete col)* | — |
| `wa_obs_question_catalogue` | one row per obs_id | 434 | 131 | → word_registry (FK source_registry_no→id); → word_registry (doc source_registry_no→id); ← wa_flag_type_question_link (FK question_id→obs_id); ← wa_finding_catalogue_links (FK question_id→obs_id); ← cluster_finding (FK obs_id→obs_id); ← cluster_finding (doc obs_id→obs_id); ← wa_finding_catalogue_links (doc question_id→obs_id); ← wa_flag_type_question_link (doc question_id→obs_id) |
| `wa_prose_section_citations` | one row per id | 562 | 562 | → wa_session_research_flags (FK cited_sd_pointer_id→id); → wa_finding_catalogue_links (FK cited_qa_link_id→id); → wa_session_b_findings (FK cited_finding_id→id); → prose_section_old_20260905 (FK prose_section_id→id); → prose_section (doc prose_section_id→id); → wa_session_b_findings (doc cited_finding_id→id); → wa_session_research_flags (doc cited_sd_pointer_id→id) |
| `wa_quality_flag_types` | one row per id | 3 | 3 | ← wa_flag_type_question_link (FK flag_type_id→id); ← wa_data_quality_flags (FK flag_id→id); ← wa_data_quality_flags (doc flag_id→id); ← wa_flag_type_question_link (doc flag_type_id→id) |
| `wa_session_research_flags` | one row per id | 715 | 715 *(no soft-delete col)* | → word_registry (FK cross_registry_id→id); → wa_file_index (FK file_id→id); → word_registry (FK registry_id→id); → word_registry (doc registry_id→id); → wa_file_index (doc file_id→id); → word_registry (doc cross_registry_id→id); ← wa_prose_section_citations (FK cited_sd_pointer_id→id); ← wa_prose_section_citations (doc cited_sd_pointer_id→id) |
| `wa_vocab_member` | one row per id | 39 | 39 *(no soft-delete col)* | → wa_vocab_member (FK superseded_by_member_id→id); → wa_vocab_set (FK set_id→id); → wa_vocab_set (doc set_id→id); → wa_vocab_member (doc superseded_by_member_id→id); ← wa_vocab_member (FK superseded_by_member_id→id); ← wa_vocab_member (doc superseded_by_member_id→id) |
| `wa_vocab_set` | one row per id | 8 | 8 *(no soft-delete col)* | ← wa_vocab_member (FK set_id→id); ← wa_vocab_member (doc set_id→id) |

---

## (b) Inactive base tables

### iba.db — 1 inactive base tables

| Table | Grain | Why inactive (from `cfg_table.use`) |
|---|---|---|
| `escalations_old` | one row per researcher interaction — the pause | Historical escalation data, frozen at the 2026-08-20 redesign cutover (v2, corrected retry of the rolled-back 2026-08-19 v1) -- 723 rows, pre-dates escalation_… |

### bible_research.db — 65 inactive base tables

| Table | Grain | Why inactive (from `cfg_table.use`) |
|---|---|---|
| `characteristic` | one row per id | The named characteristics belonging to each cluster — the distinct inner-being traits a cluster resolves into, each with a definition. 277 rows across 35 clust… |
| `cluster_finding` | one row per id | REDUNDANT (2026-08-29): fully migrated into finding (19,997 rows, provenance=cluster_finding_migration, traceable via source_legacy_ref CF: tag; characteristic… |
| `ib_characteristic_legacy` | no declared primary key — see cfg_column for ib_characteristic_legacy… | The superseded 29-row inner-being characteristic registry from 2026-07-03, retained as a backup after ib_characteristic was rebuilt on a meaning key. Its rows … |
| `lemma_faculty_map` | one row per strongs_number | Maps 1,717 Strong's lemmas to the inner-being faculty or faculties they engage (affect, cognition, volition, moral evaluation and combinations), with a stated … |
| `lexicon` | one row per strong | A flat reference lexicon of 11,666 Strong's entries harvested wholesale from STEP on 2026-06-16 — original-script lemma, transliteration, gloss, medium definit… |
| `mti_term_cross_refs` | one row per id | Records the registry words that reference a term other than its owning one — the XREF side of term ownership, held as a junction between mti_terms and word_reg… |
| `mti_term_flags` | one row per (mti_term_id, flag_id) | Junction attaching Phase 2 triage flags from phase2_flag_types to terms in mti_terms; 1,005 assignments across 785 terms. In practice it uses a very narrow sli… |
| `mti_term_subgroup` | one row per id | The many-to-many placement of terms into cluster sub-groups, replacing the old single-valued column on mti_terms. 1,196 placements over 740 distinct terms, so … |
| `mti_terms` | one row per id | The master term index: one row per Hebrew/Greek/Aramaic term drawn into the study, carrying the term's identity (Strong's, transliteration, gloss, language), w… |
| `phase2_flag_types` | one row per id | Lookup of the 25 Phase 2 flag codes an analyst may raise against a term, each with a prose definition of when it applies — e.g. thin datasets, God as subject o… |
| `prose_section_dimension_link` | one row per (prose_section_id, dimension_id, link_type) | Declared as a many-to-many link between prose sections and dimensions, with a link_type qualifying the relationship, but it holds 0 rows. It was created, keyed… |
| `term_collection_lexical` | one row per id | Holds collection-level lexical judgements about a term — properties asserted of the term across its whole verse set rather than in any one verse (mutability, t… |
| `term_fetch_log` | one row per id | Per-Strong's-number record of STEP API fetches (2,377 rows), showing what was requested, what it resolved to, and how many verses came back and were stored. It… |
| `themes` | one row per id | Declared as a lookup of thematic labels but has 0 rows — created and never used. Nothing in the live model links to it; theme-like grouping is done through the… |
| `ve_dimension_scoreboard` | one row per ve_nr | The rule-validation scoreboard for the 18 VE-lexical dimensions (ve_nr 101-118), holding each dimension's rule, its validation verdict and the first verse wher… |
| `ve_lexical` | one row per id | The live lexical-analysis store: one row per analytical item read off a verse, keyed to a verse span and a dimension number (ve_nr 101-118 for the verse-level … |
| `ve_lexical_divinv_pre_reverse_20260626` | no declared primary key — see cfg_column for ve_lexical_divinv_pre_re… | A snapshot of 860 divine-involvement items (ve_nr 8, tier T0.1.2) produced by the divine_involvement_read_api pass on 2026-06-16, taken before their reversal o… |
| `ve_lexical_divinv_roles_premap_20260626` | no declared primary key — see cfg_column for ve_lexical_divinv_roles_… | A snapshot of 5,187 divine-involvement items (ve_nr 8) taken before the 2026-06-26 remap collapsed them. Comparing it against ve_lexical_legacy row by row show… |
| `ve_lexical_faculty_backup` | no declared primary key — see cfg_column for ve_lexical_faculty_backu… | A snapshot of 29,031 faculty items (ve_nr 7, tier T3) as produced by the v2_engine_iter1 run and dated 2026-06-16, holding the engine's term-meaning derivation… |
| `ve_lexical_faculty_pre_reset_20260626` | no declared primary key — see cfg_column for ve_lexical_faculty_pre_r… | A snapshot of all 29,203 faculty items (ve_nr 7) as they stood immediately before the 2026-06-26 faculty reset. Every id still resolves in ve_lexical_legacy wi… |
| `ve_lexical_faculty_seat_reverse_20260626` | no declared primary key — see cfg_column for ve_lexical_faculty_seat_… | A snapshot of 1,492 faculty items created on 2026-06-26 by the inferred-seat rule, which assigned a faculty by reading faculty-words elsewhere in the verse rat… |
| `ve_lexical_legacy` | one row per id | The previous generation of the lexical store, retired at the 2026-07-02 cutover and kept whole. 507,651 rows, ids 2351222 to 7123084 (no overlap with ve_lexica… |
| `ve_lexical_objtype_premap_20260626` | no declared primary key — see cfg_column for ve_lexical_objtype_prema… | A snapshot of 9,534 object-type items (ve_nr 16) taken before the 2026-06-26 remap. The comparison against ve_lexical_legacy is unambiguous: all three source v… |
| `ve_lexical_origin_quarantine_20260626` | no declared primary key — see cfg_column for ve_lexical_origin_quaran… | A snapshot of 3,623 origin items (ve_nr 6, tier T2.9.1) quarantined on 2026-06-26. Every row is identical: the value 'received-from-outside' asserted purely be… |
| `ve_lexical_overlay_reverse_20260626` | no declared primary key — see cfg_column for ve_lexical_overlay_rever… | A snapshot of 1,387 items reversed on 2026-06-26, mixing two dimensions: object-type (ve_nr 16, 1,128 rows) and cause (ve_nr 17, 259 rows), both produced by re… |
| `ve_lexical_valence_quarantine_20260626` | no declared primary key — see cfg_column for ve_lexical_valence_quara… | A snapshot of 26,993 valence items (ve_nr 21, tier T0.3.1) quarantined on 2026-06-26 — the largest withdrawal recorded in this group. All 26,993 ids resolve in… |
| `ve_lexical_verification` | one row per id | A small manual verification log: 46 hand-checked ve_lexical items, all of dimension 101 (sense) and all checked on 2026-07-14, recording whether the stored rea… |
| `ve_verification_sample` | one row per (ve_nr, verse_span_id) | The drawn sampling frame for verifying the lexical layer: 3,332 (ve_nr, verse_span_id) pairs selected across 18 dimensions from Psalms (book 19) and Proverbs (… |
| `verse` | one row per id | The master verse table and the anchor of the whole verse layer: one row per verse of the ESV text (25,634 rows, all 66 books), each with its text, canonical id… |
| `verse_context` | one row per id | The term-in-verse classification record (55,775 rows): for one verse-record and one MTI term it holds whether that occurrence is relevant to the study, which v… |
| `verse_context_group` | one row per id | The catalogue of verse-context groups (VCGs) — named groupings of term-in-verse occurrences that share a context, referenced by verse_context.group_id. Only 1,… |
| `verse_coverage` | one row per verse_id | A derived, materialised roll-up of study coverage per verse — how many spans, study terms and lexical units each verse carries, and whether it is in scope. It … |
| `verse_coverage_morphology` | one row per id | A per-word morphology extract for a narrow set of verses — 2,877 word rows covering only 326 distinct references, concentrated in Leviticus, Proverbs and Galat… |
| `verse_evidence_index` | no declared primary key — see cfg_column for verse_evidence_index's r… | The fan-in index that answers 'what evidence is bound to this verse' — 804,805 rows mapping a verse to each piece of evidence held against it, so a verse's ful… |
| `verse_evidence_orphan` | no declared primary key — see cfg_column for verse_evidence_orphan's … | The reject log of the verse_evidence_index build: 222 evidence rows that could not be bound to a verse. Every row has the same single cause, making this a smal… |
| `verse_morph_complexity` | one row per verse_id | A derived per-verse syntactic complexity profile counting content words, finite and non-finite verbs, conjunctions, prepositions and subordinators, with a summ… |
| `verse_morphology` | one row per id | The morphological backbone of the layer: one row per word of every verse (325,507 rows), carrying the surface form, Strong's tag, morph_code and the language/p… |
| `verse_morphology_raw` | one row per verse_id | The raw STEP HTML behind the parsed morphology — one row per verse (25,634, i.e. complete cover of the master verse table), kept so the parse in verse_morpholo… |
| `verse_span_index` | one row per id | The working analytical surface over word spans (325,474 rows): it reproduces verse_morphology's columns almost exactly and adds the analytical overlay — role, … |
| `verse_term_index` | no declared primary key — see cfg_column for verse_term_index's real … | A minimal derived lookup of which Strong's terms appear in which verse (275,593 rows, no primary key, indexed both ways). It is a de-duplicated projection of v… |
| `wa_addendum_registry` | one row per id | A one-off audit artefact: 22 observations from the April 2026 global-rules audit, each recording a problem with a rule and where its content should migrate. En… |
| `wa_cross_registry_links` | one row per id | 158 researcher-authored links between registry words, each naming the connecting Hebrew or Greek term and explaining the connection in prose — the pre-cluster … |
| `wa_crosslink_type` | one row per id | The 11 kinds of relationship that may connect two registry words, e.g. shared root, semantic opposition, causative chain. It is the controlled vocabulary behin… |
| `wa_dim_review_cluster_log` | one row per id | A completion log for the retired dimension review: one row per C-code cluster finished, six in all (C10, C13, C17, C20, C21, C22), recorded between 2026-04-09 … |
| `wa_dimension_index` | one row per id | The retired dimension-review layer: 3,509 rows, one per verse_context_group, recording which of 20 named dimensions the group was assigned to and how its verse… |
| `wa_file_index` | one row per id | One row per input file (or engine onboarding stub) that supplied a registry word's data, with the file's provenance, split-part structure and specification ver… |
| `wa_file_name_pattern` | one row per id | The 23 registered filename conventions used across the programme, each given as a template such as 'wa-dim-{cluster}-extract-{YYYYMMDD}.json' with the instruct… |
| `wa_finding_catalogue_links` | one row per id | REDUNDANT (2026-08-29): 5,456 of 6,199 rows migrated into finding_question_link (finding_id remapped via the wa_session_b_findings->finding SB: tag), traceable… |
| `wa_flag_type_question_link` | one row per id | Maps quality-flag types to the catalogue questions that a raised flag should prompt. REDUNDANT (2026-08-29): all 12 rows link to questions that are status=redu… |
| `wa_lsj_parsed` | one row per id | Structured parse of the Liddell-Scott-Jones classical Greek lexicon entry for a term, splitting the raw entry into gloss, domains, and philosophical and etymol… |
| `wa_meaning_parsed` | one row per id | One header row per inventory term for its parsed definition, holding the counts and derived flags of the parse whose detail lives in wa_meaning_sense and wa_me… |
| `wa_meaning_sense` | one row per id | The parsed sense hierarchy of a term's definition: 17,125 rows, one per numbered sense, keyed to wa_meaning_parsed and ordered by the source's own numbering (1… |
| `wa_meaning_stem` | one row per id | Breaks a Hebrew verb's definition down by verbal stem (Qal, Piel, Hiphil and so on) with the sense each stem carries. Effectively unused: 13 rows covering just… |
| `wa_patch_type_registry` | one row per id | The 20 recognised JSON patch types, each naming the instruction that governs it and the tables it writes to — the reference-as-database record of what a patch … |
| `wa_rule_registry` | one row per id | The programme's global rules held as data: 59 rules with their text, rationale, application notes and supersession chain, all imported from a single JSON docum… |
| `wa_session_b_dimensions` | one row per id | A near-empty remnant of the Session B per-word dimensional assessment: just 2 rows, for registries 112 and 182, raised on 27 and 28 March 2026 under instructio… |
| `wa_session_b_findings` | one row per id | The superseded per-word Session B findings store: 2,883 findings raised April to May 2026 across 112 registries, since replaced by the universal finding table.… |
| `wa_term_inventory` | one row per id | The per-registry term inventory: one row per term as held under a given English word's file, carrying the STEP-sourced identity, gloss, meaning text, occurrenc… |
| `wa_term_phase2_flags` | one row per (term_inv_id, flag_id) | Junction attaching Phase 2 triage flags from phase2_flag_types to inventory terms: 1,570 assignments over 883 terms, using 25 distinct flag types. Broader in c… |
| `wa_term_related_words` | one row per id | The related-word web: 103,944 rows attaching each inventory term to other lemmas STEP reports as related, by gloss, transliteration and Strong's. Overwhelmingl… |
| `wa_term_root_family` | one row per id | Assigns inventory terms to a shared etymological root family by root code, so terms from one root (e.g. CHARAH, 'burn/anger') can be worked together. 2,861 row… |
| `wa_verse_records` | one row per id | The legacy per-term-in-verse occurrence store (247,046 rows) that predates the master verse table — one row per term found in a verse, with the verse text, con… |
| `wa_verse_term_links` | one row per id | The junction between a wa_verse_records occurrence and a wa_term_inventory term (237,531 rows), unique on (verse_id, term_inv_id) and carrying the STEP sub-glo… |
| `word_registry` | one row per id | The programme's lexical entry point: one row per English inner-life word (222 rows), carrying the word's definition, provenance, cluster assignment and the per… |
| `word_run_state` | one row per id | Per-word outcome of each engine run: which phase the word reached, what the audit concluded and why it stopped. 539 rows over 373 runs — the audit's verdict hi… |

---

## (c) Every table in both schemas, validated against (a) + (b)

Ground truth pulled directly from each database's own `sqlite_master`, independent of `cfg_table`, then reconciled by name (not by count alone, which can hide a coincidental match):

| Database | Physical tables (`sqlite_master`) | Registered in `cfg_table` | Physical, not registered | Registered, no physical table |
|---|---|---|---|---|
| `iba` | 78 | 78 | none | none |
| `bible_research` | 113 | 113 | none | none |

**Result: zero gaps in either direction, both databases.** Every physical table is registered in `cfg_table`; every `cfg_table` row names a table that physically exists. `governance.tables` ("each table in the project must be listed in cfg_table... applies to all databases") is being honoured in full, both directions, as of this check.

Partition of the full register by category, confirming (a) + (b) + non-base accounts for every single row, nothing dropped or double-counted:

| Category | iba.db | bible_research.db | Total |
|---|---|---|---|
| Live base (`data`, inactive=0) | 41 | 48 | 89 |
| Inactive base (`data`, inactive=1) | 1 | 65 | 66 |
| Non-base (`rule`+`log`, i.e. `cfg_*`) | 36 | 0 | 36 |
| **Total** | **78** | **113** | **191** |

78 (iba physical) + 113 (bible_research physical) = 191 = 191 (sum of every category above). No table excluded from this validation in either direction.

---

## (d) Non-base (`cfg_*`) tables relating to each live base table

"Relates to" is read broadly per the instruction, not FK-only. Four distinct mechanisms found, all confirmed live, none assumed:

**1. Universal, by governance design (every live base table, no exceptions):**
- `cfg_table` -- registers this exact row (SS a/c above).
- `cfg_column` -- registers every one of this table's columns (`governance.table_columns`).

**2. Partial registries -- a table-name-keyed `cfg_*` table that names *some* live base tables, not all** (membership below is exact, queried live, not inferred from naming convention):

| Registry (`category`) | Keyed by | Scope confirmed | What a hit means |
|---|---|---|---|
| `cfg_index` (rule) | `table_name` (no `database` column) | iba.db only -- every value it holds names a live iba table | a secondary (non-FK/non-UNIQUE) index is declared for this table |
| `cfg_unique` (rule) | `database` + `table_name` | both databases | a documented compound-uniqueness rule exists for this table |
| `cfg_write_grant` (rule) | `database` + `table_name`, `inactive` | both databases | an active writer is granted write access to this table |
| `cfg_report_csv_table` (rule) | `table_name` (no `database` column) | iba.db only -- confirmed by inspecting every associated `step` value (`passage.validate`, `report.cluster`, `report.registry`, `report.span_analysis`, `validation.book` -- all iba dispatcher steps) | this table is a named CSV-export target of a report step |

Per-table membership (only tables with at least one hit shown; every other live base table has none beyond the two universal registries above):

| Table | cfg_index | cfg_unique | cfg_write_grant | cfg_report_csv_table |
|---|---|---|---|---|
| `bible_research.prose_section` |  |  | ✓ |  |
| `bible_research.prose_section_finding_link` |  | ✓ |  |  |
| `bible_research.prose_section_fts_idx` |  | ✓ |  |  |
| `bible_research.prose_section_type` |  |  | ✓ |  |
| `bible_research.prose_section_verse_link` |  |  | ✓ |  |
| `bible_research.record_change_log` |  |  | ✓ |  |
| `bible_research.segment_unit_verse` |  | ✓ |  |  |
| `bible_research.wa_data_quality_flags` |  |  | ✓ |  |
| `bible_research.wa_obs_question_catalogue` |  |  | ✓ |  |
| `iba.candidate_seed` | ✓ | ✓ | ✓ | ✓ |
| `iba.cluster` |  |  | ✓ | ✓ |
| `iba.cluster_strong` |  |  | ✓ | ✓ |
| `iba.content_index` |  | ✓ |  |  |
| `iba.debate_change_detail` | ✓ |  | ✓ |  |
| `iba.escalation` |  |  | ✓ | ✓ |
| `iba.escalation_history` | ✓ | ✓ | ✓ |  |
| `iba.hib` | ✓ |  | ✓ |  |
| `iba.hib_referent_option` | ✓ |  | ✓ |  |
| `iba.lemma_inventory` |  |  | ✓ |  |
| `iba.operation` | ✓ |  | ✓ |  |
| `iba.operation_party` | ✓ |  | ✓ |  |
| `iba.passage` | ✓ | ✓ | ✓ | ✓ |
| `iba.passage_emergent_question` | ✓ | ✓ | ✓ |  |
| `iba.passage_insufficiency` | ✓ | ✓ | ✓ |  |
| `iba.passage_linkage` | ✓ | ✓ | ✓ |  |
| `iba.passage_validation_note` | ✓ | ✓ | ✓ |  |
| `iba.phenomenon` | ✓ | ✓ | ✓ |  |
| `iba.run` |  |  | ✓ | ✓ |
| `iba.span` | ✓ | ✓ | ✓ | ✓ |
| `iba.span_candidate` | ✓ |  |  | ✓ |
| `iba.strong` |  |  | ✓ | ✓ |
| `iba.strong_lexicon` | ✓ |  | ✓ | ✓ |
| `iba.strong_lsj_parsed` | ✓ |  | ✓ | ✓ |
| `iba.strong_meaning_parsed` | ✓ |  | ✓ | ✓ |
| `iba.strong_meaning_tree` | ✓ |  | ✓ | ✓ |
| `iba.strong_mounce_parsed` | ✓ |  | ✓ | ✓ |
| `iba.strong_related` | ✓ |  | ✓ | ✓ |
| `iba.strong_sense` | ✓ |  | ✓ | ✓ |
| `iba.strong_verse` | ✓ | ✓ | ✓ |  |
| `iba.validation_result` | ✓ |  | ✓ | ✓ |
| `iba.verse` |  |  | ✓ | ✓ |
| `iba.verse_hib` | ✓ | ✓ | ✓ |  |
| `iba.verse_lexical` | ✓ | ✓ | ✓ |  |
| `iba.verse_lexical_note` |  |  | ✓ |  |
| `iba.verse_passage` | ✓ |  | ✓ | ✓ |
| `iba.word_registry` |  |  | ✓ | ✓ |
| `iba.word_strong` | ✓ | ✓ | ✓ | ✓ |

**3. Direct FK / documented-FK from a specific `cfg_*` table into a specific base table** (both real SQL-declared FKs, confirmed via `PRAGMA foreign_key_list`, and identically documented in `cfg_column.fk`):

| From (`cfg_*`, category) | Column | To (base table) | Status |
|---|---|---|---|
| `iba.cfg_change_detail` (log) | `run_id` -> `run_id` | `iba.run` | active |
| `iba.cfg_lexical_code_class` (rule) | `strong_code` -> `strongNumber` | `iba.strong` | INACTIVE (table retired, escalation #1502-1505, 2026-09-05) |

No other `cfg_*` table carries a real or documented FK into a base table -- every other relation in this section is the table-name-keyed registry pattern in (2), not a scalar FK.

**4. Cross-database references** (SQLite cannot enforce a FK across two `.db` files, so every one of these is documentary-only in `cfg_column.use`/`cfg_table.use` -- confirmed by reading that text directly, not inferred from column naming):

| From | Column | To | Nature |
|---|---|---|---|
| `bible_research.wa_data_quality_flags` | `strong_id` | `iba.strong` | documented-only, no enforced FK (SQLite cannot FK across database files); cfg_table.use for wa_data_quality_flags states strong_id's natural target is iba.db's own strong table |
| `bible_research.finding_verse_index` | `verse_id` | `iba.verse` | documented as iba.db verse.id (escalation #1051), resolved via wa_verse_records.reference text match, never a direct cross-db FK |
| `iba.cfg_prose_concept` | `chapter` | `bible_research.prose_section_type` | documented as bible_research.db prose_section_type.chapter_no; no FK (cfg_prose_chapter table removed 2026-08-27, escalation #918) |

All three are one-directional documentation notes, not enforced constraints -- each is bible_research.db <-> iba.db naming the other side's table in its own `use` text. No fourth instance was found after a full-text search of both `cfg_column.use`/`.expectation` and `cfg_table.use`/`.grain` for `iba.db`, `bible_research.db`, `research_db`, `cross-database`, `cross database`, `across database`, `cannot FK`, `no FK`, `other database`.

---

## Findings surfaced by this validation

These are genuine anomalies found while building the report above, not requested output types (a)-(d) themselves -- surfaced here per the instruction to check every step against `cfg.*`, since the check itself turned up gaps in that config.

### F1. `cfg_index` and `cfg_report_csv_table` lack the `database` disambiguator their sibling registries already carry, and both currently hold names that are genuinely ambiguous

`cfg_table`, `cfg_column`, `cfg_write_grant` and `cfg_unique` were each widened to a `(database, table_name)` compound key after escalations #653/#680 established that `iba.db` and `bible_research.db` **genuinely share table names for different tables** (their own words: `word_registry`/`cluster`/`passage`/`verse`). `cfg_index` and `cfg_report_csv_table` were never widened -- both still key on `table_name` alone.

Checked live whether this gap is theoretical or has actually bitten: `cluster` and `passage` are **live, active tables in both databases** at the same time (`iba.cluster`/`iba.passage` both `inactive=0`; `bible_research.cluster`/`bible_research.passage` both `inactive=0`) and both names appear in `cfg_report_csv_table` (and `passage` in `cfg_index`).

Read every associated `cfg_report_csv_table.step` value for these rows (`passage.validate`, `validation.book`, `report.cluster`, `report.registry`, `report.span_analysis`) -- all are `module.step` names from the iba dispatcher, so in practice every current row resolves unambiguously to `iba.db`'s own tables, not `bible_research.db`'s. **No live misattribution exists today.** But the schema does not prevent one: nothing stops a future row from being added for a `bible_research.db`-side report step using the bare name `cluster` or `passage`, and it would collide silently with the iba-side rows already there, with no column to tell them apart -- the exact condition escalation #653/#680 were raised to close for the other four registries.

`verse` and `word_registry` also appear in `cfg_report_csv_table`, but the `bible_research.db` side of each is already `inactive=1`, so those two are not currently exposed to the same risk.

Not fixed here -- this is a structural/schema question (same shape as #653/#680, which went through `configmaint.propose`), not a data correction, so it is left for the researcher's decision rather than applied unilaterally.

### F2. `cfg_table_purpose` and `cfg_change_detail` also key on a bare `table_name`, but confirmed scoped to `cfg_*` tables only -- not a live risk

Checked and excluded from F1: both columns' own `cfg_column.use` text is explicit that their `table_name` values name **rule tables** (`cfg_table_purpose`: "cfg_table.name of the rule table this entry is about"; `cfg_change_detail`: "which cfg_* table changed"), never base data tables. Since `cfg_*` table names are unique by construction (only one database registers `cfg_*` rows), there is no cross-database collision surface here.

### F3. Four `bible_research.db` link tables carry a real, physically-declared FK to a table that no longer exists -- `prose_section_old_20260905` -- and one of them holds 562 live rows

Found while diffing every base table's real (`PRAGMA foreign_key_list`) FKs against its documented (`cfg_column.fk`) ones -- the two disagreed on the target table for exactly this group, which is what surfaced it. Confirmed directly against the live schema (`sqlite_master.sql`), not inferred:

| Table | Live rows | Declared FK | Target exists? |
|---|---|---|---|
| `wa_prose_section_citations` | **562** | `prose_section_id INTEGER ... REFERENCES "prose_section_old_20260905"(id)` | **No** -- `SELECT * FROM prose_section_old_20260905` fails with `no such table` |
| `prose_section_finding_link` | 0 | same | No |
| `prose_section_verse_link` | 0 | same | No |
| `prose_section_dimension_link` | 0 | same | No |

This is distinct from, and in addition to, the already-documented issue on `prose_section_finding_link`/`wa_prose_section_citations` (their own `cfg_table.use` text already says their *other* FKs point at legacy tables like `wa_session_b_findings` -- true, and those legacy targets **do** still physically exist, just superseded). The `prose_section_old_20260905` target is different: it does not exist at all. All four tables' `prose_section_id` column was declared against whatever `prose_section` was renamed to mid-migration on 2026-09-05, and never repointed at the `prose_section` table that exists today (1,036 rows) -- consistent with SQLite's lack of `ALTER TABLE ... DROP CONSTRAINT`, where a table-rename-and-rebuild migration leaves dependent tables' inline `REFERENCES` clauses stale unless each is explicitly rebuilt too.

Because SQLite only validates FKs when `PRAGMA foreign_keys=ON` for the connection performing the write (confirmed default OFF for a fresh connection to this file, checked live), the 562 existing `wa_prose_section_citations` rows are not currently at risk of rejection -- but the declared constraint is unenforceable and misleading (it cannot resolve `prose_section_id` against anything), and any future write path that does turn FK enforcement on for this file would break on this table without warning. Not fixed here -- a schema rebuild (SQLite requires recreating the table to change a `REFERENCES` clause) is a data-structure change, not a data correction, and is raised as its own escalation for a decision rather than applied unilaterally.

---

## Summary

| Check | Result |
|---|---|
| (a) Live base tables enumerated, related, counted | 89 tables (41 iba + 48 bible_research) |
| (b) Inactive base tables enumerated | 66 tables (1 iba + 65 bible_research) |
| (c) Every physical table validated against (a)+(b)+non-base | 191/191 accounted for, 0 gaps either direction, both databases |
| (d) Non-base relations per live base table | 2 universal registries (all 89) + 4 partial registries (49 of 89 have >=1 hit) + 2 direct FK/documented-FK (1 active, 1 retired) + 3 documented cross-database references |
| Anomalies found while validating | F1 (live, unfixed schema gap in `cfg_index`/`cfg_report_csv_table`), F2 (checked, not a risk), F3 (dangling FK to a dropped table, 562 live rows affected) |
