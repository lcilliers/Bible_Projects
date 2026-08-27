# Table reconciliation extract — research_db vs iba.db

Generated 2026-08-27 for escalation #922. **Updated same day, self-control run against the
researcher's own instruction ("count all the tables per DB and check it against the schema")** —
the v1 cut of this extract was sourced from `cfg_table` alone, which the check below shows is
incomplete on the iba.db side.

## 0. Self-control: `cfg_table` vs the actual physical schema

Counted directly from `sqlite_master` on each database file (excluding `sqlite_sequence` and
views — a view is not a table) and compared against `cfg_table`'s registration for that database:

| database | physical tables | `cfg_table` rows | gap |
|---|---|---|---|
| `bible_research.db` | 112 | 112 | **none** — every physical table is registered |
| `iba.db` | 74 | 71 | **3 physical tables missing from `cfg_table`**: `content_index`, `content_index_scan`, `file_manifest` |

Views not counted as tables either side (`bible_research.db`: `v_l2_meaning`, `v_l2_tier`;
`iba.db`: `vw_passages_by_book`) — consistent with `governance.tables`, which names "each table,"
not views, and neither database registers its views in `cfg_table`.

**The 3 missing tables, with their real shape** (none in `cfg_table`, so absent from every section
below in v1 of this extract):

| table | columns | rows |
|---|---|---|
| `content_index` | `key_type, key_value, file_path, line_number, snippet, indexed_at` | 0 |
| `content_index_scan` | `file_path, mtime, scanned_at` | 0 |
| `file_manifest` | `path, category, file_type, currency, archived, registry, word, cluster, vcb_batch, version, date, ext, size_bytes, modified_at, scanned_at` | 18,653 |

`content_index`/`content_index_scan` are the project-wide search-index tables (currently empty —
not yet rebuilt/populated). `file_manifest` is the live project file manifest (18,653 rows) —
`CLAUDE.md` §2 already names it as such; it was simply never added to `cfg_table`, a
`governance.tables` compliance gap distinct from the base/analytical disposition question #922 is
otherwise about. None of the three has a `bible_research.db` counterpart to match against — they
are iba-only infrastructure, not part of the base-data-layer migration this escalation is
otherwise tracking.

This gap is **not fixed in this document** — adding rows to `cfg_table` is itself a `cfg_*` write
and goes through `Config-Maintenance.ps1 -Step Propose` like any other, not a silent correction
here. Flagged for the researcher's decision, not actioned.

## 1. Matched by name (present in both databases), from `cfg_table`

- `bible_research.db`: 112 tables registered in `cfg_table` (= physical count, per sec 0).
- `iba.db`: 71 tables registered in `cfg_table` (74 physical — see the 3-table gap in sec 0).
- Same table name present in both: 4.

| table | research_db inactive | iba.db inactive | note |
|---|---|---|---|
| `cluster` | 0 | 0 | Different purpose each side, both legitimately active — research_db = the 49 M-code analytical taxonomy; iba.db = the strong-to-cluster assignment substrate migrated 2026-08-11. |
| `passage` | 0 | 0 | research_db's passage register was built for research_db's own (inactive) verse table. iba.db's passage is the live book-by-book debate register. Flagged uncertain on #922 — needs a usage check before recommending inactive on the research_db side. |
| `verse` | 1 | 0 | research_db copy already correctly inactive (superseded by iba.db's verse, per the 2026-08-15 architecture correction). |
| `word_registry` | 1 | 0 | research_db copy already correctly inactive (superseded by iba.db's word_registry, the live registry). |

## 2. research_db-only tables (108)

No same-named table in iba.db. Does not mean unreplaced — several were rebuilt under a different name (e.g. `wa_verse_records` -> `verse_lexical`, `mti_terms` -> `strong`); that functional mapping is the deeper work #922 still owes, not attempted again here.

| table | inactive |
|---|---|
| `book_code_variants` | 0 |
| `books` | 0 |
| `characteristic` | 0 |
| `characteristic_subgroup` | 0 |
| `cluster_finding` | 0 |
| `cluster_observation` | 0 |
| `cluster_subgroup` | 0 |
| `engine_run_log` | 0 |
| `engine_stream_checkpoint` | 0 |
| `finding` | 0 |
| `finding_citation` | 0 |
| `finding_question_link` | 0 |
| `finding_revision` | 0 |
| `finding_verse_link` | 0 |
| `ib_characteristic` | 0 |
| `ib_characteristic_legacy` | 0 |
| `ib_observation` | 0 |
| `lemma_faculty_map` | 1 |
| `lexicon` | 1 |
| `mti_term_cross_refs` | 1 |
| `mti_term_flags` | 1 |
| `mti_term_subgroup` | 1 |
| `mti_terms` | 1 |
| `phase2_flag_types` | 1 |
| `prose_section` | 0 |
| `prose_section_dimension_link` | 0 |
| `prose_section_finding_link` | 0 |
| `prose_section_fts` | 0 |
| `prose_section_fts_config` | 0 |
| `prose_section_fts_content` | 0 |
| `prose_section_fts_data` | 0 |
| `prose_section_fts_docsize` | 0 |
| `prose_section_fts_idx` | 0 |
| `prose_section_type` | 0 |
| `prose_section_verse_link` | 0 |
| `record_change_log` | 0 |
| `reread_worklist` | 0 |
| `schema_version` | 0 |
| `segment_unit` | 0 |
| `segment_unit_verse` | 0 |
| `session_d_observations` | 0 |
| `session_d_runs` | 0 |
| `session_d_term_links` | 0 |
| `session_d_verse_links` | 0 |
| `sources` | 0 |
| `term_collection_lexical` | 1 |
| `term_fetch_log` | 1 |
| `themes` | 1 |
| `vcg_term` | 0 |
| `ve_dimension_scoreboard` | 0 |
| `ve_lexical` | 1 |
| `ve_lexical_divinv_pre_reverse_20260626` | 1 |
| `ve_lexical_divinv_roles_premap_20260626` | 1 |
| `ve_lexical_faculty_backup` | 1 |
| `ve_lexical_faculty_pre_reset_20260626` | 1 |
| `ve_lexical_faculty_seat_reverse_20260626` | 1 |
| `ve_lexical_legacy` | 1 |
| `ve_lexical_objtype_premap_20260626` | 1 |
| `ve_lexical_origin_quarantine_20260626` | 1 |
| `ve_lexical_overlay_reverse_20260626` | 1 |
| `ve_lexical_valence_quarantine_20260626` | 1 |
| `ve_lexical_verification` | 1 |
| `ve_verification_sample` | 1 |
| `verse_analysis_progress` | 0 |
| `verse_context` | 1 |
| `verse_context_group` | 1 |
| `verse_coverage` | 1 |
| `verse_coverage_morphology` | 1 |
| `verse_evidence_index` | 1 |
| `verse_evidence_orphan` | 1 |
| `verse_morph_complexity` | 1 |
| `verse_morphology` | 1 |
| `verse_morphology_raw` | 1 |
| `verse_span_index` | 1 |
| `verse_term_index` | 1 |
| `wa_addendum_registry` | 1 |
| `wa_cross_registry_links` | 1 |
| `wa_crosslink_type` | 1 |
| `wa_data_quality_flags` | 0 |
| `wa_dim_review_cluster_log` | 1 |
| `wa_dimension_index` | 0 |
| `wa_file_index` | 1 |
| `wa_file_name_pattern` | 1 |
| `wa_finding_catalogue_links` | 0 |
| `wa_finding_entity_links` | 0 |
| `wa_flag_type_question_link` | 0 |
| `wa_label_pattern` | 0 |
| `wa_lsj_parsed` | 1 |
| `wa_meaning_parsed` | 1 |
| `wa_meaning_sense` | 1 |
| `wa_meaning_stem` | 1 |
| `wa_obs_question_catalogue` | 0 |
| `wa_patch_type_registry` | 1 |
| `wa_prose_section_citations` | 0 |
| `wa_quality_flag_types` | 0 |
| `wa_rule_registry` | 1 |
| `wa_session_b_dimensions` | 0 |
| `wa_session_b_findings` | 0 |
| `wa_session_research_flags` | 0 |
| `wa_term_inventory` | 1 |
| `wa_term_phase2_flags` | 1 |
| `wa_term_related_words` | 1 |
| `wa_term_root_family` | 1 |
| `wa_verse_records` | 1 |
| `wa_verse_term_links` | 1 |
| `wa_vocab_member` | 0 |
| `wa_vocab_set` | 0 |
| `word_run_state` | 1 |

## 3. iba.db-only tables (70 — 67 in `cfg_table` + 3 found by the sec 0 self-control, not in `cfg_table`)

No same-named table in research_db — either genuinely new (the `cfg_*` config store itself, the debate pipeline, `escalation`) or the rebuilt/renamed home for something research_db used to hold under a different name. The 3 rows marked `**` are physically present but have no `cfg_table` row at all (sec 0) — their "inactive" column is blank because that flag doesn't exist for them yet, not because they're confirmed active.

| table | inactive |
|---|---|
| `candidate_seed` | 0 |
| `cfg_api` | 0 |
| `cfg_behaviour_class` | 0 |
| `cfg_behaviour_rule` | 0 |
| `cfg_book_order` | 0 |
| `cfg_candidate_rule` | 1 |
| `cfg_change_detail` | 0 |
| `**content_index` | *(not registered)* |
| `**content_index_scan` | *(not registered)* |
| `**file_manifest` | *(not registered)* |
| `cfg_change_log` | 0 |
| `cfg_column` | 0 |
| `cfg_connection` | 0 |
| `cfg_content_index_exclude` | 0 |
| `cfg_content_index_size_override` | 0 |
| `cfg_enum` | 0 |
| `cfg_escalation` | 0 |
| `cfg_escalation_requirement` | 0 |
| `cfg_escalation_transition` | 0 |
| `cfg_index` | 0 |
| `cfg_meta` | 0 |
| `cfg_method_rule` | 0 |
| `cfg_on_fail` | 0 |
| `cfg_passage` | 0 |
| `cfg_prose` | 0 |
| `cfg_prose_concept` | 0 |
| `cfg_quality_check` | 0 |
| `cfg_report` | 0 |
| `cfg_report_csv_table` | 0 |
| `cfg_report_section` | 0 |
| `cfg_setting` | 0 |
| `cfg_status_flow` | 0 |
| `cfg_step` | 0 |
| `cfg_table` | 0 |
| `cfg_unique` | 0 |
| `cfg_utility` | 0 |
| `cfg_work_package` | 0 |
| `cfg_write_grant` | 0 |
| `cluster_strong` | 0 |
| `debate_change_detail` | 0 |
| `escalation` | 0 |
| `escalation_history` | 0 |
| `escalations_old` | 1 |
| `hib` | 0 |
| `hib_referent_option` | 0 |
| `lemma_inventory` | 0 |
| `operation` | 0 |
| `operation_party` | 0 |
| `passage_emergent_question` | 0 |
| `passage_insufficiency` | 0 |
| `passage_linkage` | 0 |
| `passage_validation_note` | 0 |
| `phenomenon` | 0 |
| `run` | 0 |
| `span` | 0 |
| `span_candidate` | 0 |
| `strong` | 0 |
| `strong_lexicon` | 0 |
| `strong_lsj_parsed` | 0 |
| `strong_meaning_parsed` | 0 |
| `strong_meaning_tree` | 0 |
| `strong_mounce_parsed` | 0 |
| `strong_related` | 0 |
| `strong_sense` | 0 |
| `strong_verse` | 0 |
| `validation_result` | 0 |
| `verse_hib` | 0 |
| `verse_lexical` | 0 |
| `verse_passage` | 0 |
| `word_strong` | 0 |
