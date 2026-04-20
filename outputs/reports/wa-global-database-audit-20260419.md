# DB-Wide Review — Phase A Audit Report

| Field | Value |
| --- | --- |
| Filename | wa-global-database-audit-20260419.md |
| Produced | 2026-04-19T12:28:21.537305+00:00 |
| Source DB | `data/bible_research.db` |
| DB size | 159 MB |
| Schema version | 3.9.0 |
| Instruction | wa-global-database-review-instruction-v1_0-20260419.md |
| Baseline backup | `backups/bible_research_pre_DBR_20260419_122435.db` |

---

## §A.1 — Table Inventory

**43 tables** (excluding `sqlite_*`). Categories follow CLAUDE.md §3 table groups.

| # | Table | Category | Row count |
| --- | --- | --- | --- |
| 1 | `book_code_variants` | reference | 112 |
| 2 | `books` | reference | 66 |
| 3 | `engine_run_log` | engine_control | 620 |
| 4 | `engine_stream_checkpoint` | engine_control | 1169 |
| 5 | `mti_term_cross_refs` | mti | 464 |
| 6 | `mti_term_flags` | mti | 54 |
| 7 | `mti_terms` | mti | 7571 |
| 8 | `phase2_flag_types` | phase2_flags | 25 |
| 9 | `schema_version` | metadata | 3 |
| 10 | `session_d_observations` | session_d | 0 |
| 11 | `session_d_runs` | session_d | 0 |
| 12 | `session_d_term_links` | session_d | 0 |
| 13 | `session_d_verse_links` | session_d | 0 |
| 14 | `sources` | reference | 0 |
| 15 | `term_fetch_log` | engine_control | 2317 |
| 16 | `themes` | reference | 0 |
| 17 | `verse_context` | verse_context | 63028 |
| 18 | `verse_context_group` | verse_context | 3550 |
| 19 | `wa_cross_registry_links` | cross_registry | 158 |
| 20 | `wa_crosslink_type` | cross_registry | 11 |
| 21 | `wa_data_quality_flags` | quality_flags | 22129 |
| 22 | `wa_dim_review_cluster_log` | dimension_index | 5 |
| 23 | `wa_dimension_index` | dimension_index | 3500 |
| 24 | `wa_file_index` | wa_file_index | 206 |
| 25 | `wa_finding_catalogue_links` | observation_catalogue | 0 |
| 26 | `wa_finding_entity_links` | session_b_structured | 0 |
| 27 | `wa_lsj_parsed` | meaning_parse | 2 |
| 28 | `wa_meaning_parsed` | meaning_parse | 7449 |
| 29 | `wa_meaning_sense` | meaning_parse | 15981 |
| 30 | `wa_meaning_stem` | meaning_parse | 13 |
| 31 | `wa_obs_question_catalogue` | observation_catalogue | 194 |
| 32 | `wa_quality_flag_types` | quality_flags | 29 |
| 33 | `wa_session_b_dimensions` | session_b_structured | 2 |
| 34 | `wa_session_b_findings` | session_b_structured | 187 |
| 35 | `wa_session_research_flags` | session_research | 336 |
| 36 | `wa_term_inventory` | wa_term_data | 7550 |
| 37 | `wa_term_phase2_flags` | phase2_flags | 1580 |
| 38 | `wa_term_related_words` | wa_term_data | 101970 |
| 39 | `wa_term_root_family` | wa_term_data | 2861 |
| 40 | `wa_verse_records` | verse_records | 229778 |
| 41 | `wa_verse_term_links` | verse_records | 226791 |
| 42 | `word_registry` | registry | 214 |
| 43 | `word_run_state` | engine_control | 437 |

All tables are categorised per CLAUDE.md §3 table groups.

**A.1 summary:**
- Total tables: 43
- Categories: 18
- Uncategorised: 0

---

## §A.2 — Column Inventory and Usage Metrics

Per table, each column's metadata, usage count, cardinality, code-reference count.

### `book_code_variants`  (112 rows, 2 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | TEXT |  | YES |  | 112 | 112 | 0 |
| `book_id` | INTEGER | YES |  |  | 112 | 66 | 0 |

### `books`  (66 rows, 9 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 66 | 66 | 0 |
| `name` | TEXT | YES |  |  | 66 | 66 | 0 |
| `abbreviation` | TEXT | YES |  |  | 66 | 66 | 0 |
| `testament` | TEXT | YES |  |  | 66 | 2 | 0 |
| `book_order` | INTEGER | YES |  |  | 66 | 66 | 0 |
| `full_name` | TEXT |  |  |  | 66 | 66 | 0 |
| `short_code` | TEXT |  |  |  | 66 | 66 | 0 |
| `verse_count` | INTEGER | YES |  | 0 | 66 | 59 | 0 |
| `last_updated` | TEXT | YES |  | strftime('%Y-%m-%dT%H:%M:%S','now') | 66 | 1 | 0 |

### `engine_run_log`  (620 rows, 17 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 620 | 620 | 0 |
| `run_id` | TEXT | YES |  |  | 620 | 620 | 0 |
| `mode` | TEXT | YES |  |  | 620 | 4 | 0 |
| `target_registry_ids` | TEXT |  |  |  | 620 | 186 | 0 |
| `started_at` | TEXT | YES |  |  | 620 | 619 | 0 |
| `completed_at` | TEXT |  |  |  | 609 | 607 | 0 |
| `outcome` | TEXT |  |  |  | 620 | 4 | 0 |
| `words_attempted` | INTEGER |  |  | 0 | 620 | 3 | 0 |
| `words_complete` | INTEGER |  |  | 0 | 620 | 3 | 0 |
| `words_stopped` | INTEGER |  |  | 0 | 620 | 4 | 0 |
| `total_terms_new` | INTEGER |  |  | 0 | 620 | 73 | 0 |
| `total_terms_xref` | INTEGER |  |  | 0 | 620 | 4 | 0 |
| `total_verses_inserted` | INTEGER |  |  | 0 | 620 | 196 | 0 |
| `total_verses_filtered` | INTEGER |  |  | 0 | 620 | 15 | 0 |
| `total_meanings_parsed` | INTEGER |  |  | 0 | 620 | 97 | 0 |
| `error_detail` | TEXT |  |  |  | 336 | 299 | 0 |
| `resume_from` | TEXT |  |  |  | 0 | 0 | 0 |

### `engine_stream_checkpoint`  (1169 rows, 11 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 1169 | 1169 | 0 |
| `run_id` | TEXT | YES |  |  | 1169 | 240 | 0 |
| `stream_name` | TEXT | YES |  |  | 1169 | 9 | 0 |
| `status` | TEXT | YES |  | 'pending' | 1169 | 3 | 0 |
| `last_registry_id` | TEXT |  |  |  | 0 | 0 | 0 |
| `last_strong` | TEXT |  |  |  | 0 | 0 | 0 |
| `rows_written` | INTEGER |  |  | 0 | 1169 | 346 | 0 |
| `rows_filtered` | INTEGER |  |  | 0 | 1169 | 15 | 0 |
| `error_detail` | TEXT |  |  |  | 0 | 0 | 0 |
| `started_at` | TEXT |  |  |  | 1169 | 486 | 0 |
| `completed_at` | TEXT |  |  |  | 935 | 474 | 0 |

### `mti_term_cross_refs`  (464 rows, 7 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 464 | 464 | 0 |
| `mti_term_id` | INTEGER | YES |  |  | 464 | 280 | 0 |
| `registry` | TEXT | YES |  |  | 464 | 109 | 0 |
| `registry_fk` | INTEGER |  |  |  | 464 | 109 | 0 |
| `word` | TEXT |  |  |  | 464 | 109 | 0 |
| `part` | TEXT |  |  |  | 17 | 4 | 0 |
| `word_data_reference` | TEXT |  |  |  | 16 | 5 | 0 |

### `mti_term_flags`  (54 rows, 2 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mti_term_id` | INTEGER | YES | YES |  | 54 | 50 | 0 |
| `flag_id` | INTEGER | YES | YES |  | 54 | 4 | 0 |

### `mti_terms`  (7571 rows, 19 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 7571 | 7571 | 0 |
| `strongs_number` | TEXT |  |  |  | 7571 | 3955 | 0 |
| `transliteration` | TEXT | YES |  |  | 7571 | 3160 | 0 |
| `gloss` | TEXT | YES |  |  | 7571 | 2770 | 0 |
| `language` | TEXT |  |  |  | 7571 | 2 | 0 |
| `owning_registry` | TEXT |  |  |  | 7571 | 185 | 0 |
| `owning_registry_fk` | INTEGER |  |  |  | 4049 | 177 | 0 |
| `owning_word` | TEXT |  |  |  | 7568 | 2519 | 0 |
| `owning_part` | TEXT |  |  |  | 350 | 6 | 0 |
| `word_data_reference` | TEXT |  |  |  | 1389 | 193 | 0 |
| `word_data_ref_fk` | INTEGER |  |  |  | 1389 | 193 | 0 |
| `status` | TEXT |  |  |  | 5295 | 11 | 0 |
| `status_note` | TEXT |  |  |  | 1504 | 785 | 0 |
| `exclusion_reason` | TEXT |  |  |  | 1146 | 353 | 0 |
| `extraction_date` | TEXT |  |  |  | 7552 | 14 | 0 |
| `strongs_reconciled` | INTEGER |  |  | 0 | 7571 | 2 | 0 |
| `anchor_note` | TEXT |  |  |  | 24 | 9 | 0 |
| `last_changed` | TEXT |  |  | datetime('now') | 7571 | 268 | 0 |
| `delete_flagged` | INTEGER |  |  | 0 | 7571 | 2 | 0 |

### `phase2_flag_types`  (25 rows, 3 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 25 | 25 | 0 |
| `flag_code` | TEXT | YES |  |  | 25 | 25 | 0 |
| `description` | TEXT |  |  |  | 25 | 25 | 0 |

### `schema_version`  (3 rows, 5 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 3 | 3 | 0 |
| `version_code` | TEXT | YES |  |  | 3 | 3 | 0 |
| `applied_at` | TEXT | YES |  |  | 3 | 3 | 0 |
| `migration_history` | TEXT |  |  |  | 3 | 3 | 0 |
| `engine_min_version` | TEXT |  |  |  | 0 | 0 | 0 |

### `session_d_observations`  (0 rows, 11 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 0 | 0 | 0 |
| `run_id` | TEXT | YES |  |  | 0 | 0 | 0 |
| `observation_id` | TEXT | YES |  |  | 0 | 0 | 0 |
| `observation_type` | TEXT | YES |  |  | 0 | 0 | 0 |
| `registries_implicated` | TEXT | YES |  |  | 0 | 0 | 0 |
| `terms_implicated` | TEXT |  |  |  | 0 | 0 | 0 |
| `structural_note` | TEXT |  |  |  | 0 | 0 | 0 |
| `source_refs` | TEXT |  |  |  | 0 | 0 | 0 |
| `gate` | TEXT | YES |  |  | 0 | 0 | 0 |
| `researcher_flag` | INTEGER |  |  | 0 | 0 | 0 | 0 |
| `raised_date` | TEXT | YES |  |  | 0 | 0 | 0 |

### `session_d_runs`  (0 rows, 9 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 0 | 0 | 0 |
| `run_id` | TEXT | YES |  |  | 0 | 0 | 0 |
| `run_date` | TEXT | YES |  |  | 0 | 0 | 0 |
| `cluster_ref` | TEXT |  |  |  | 0 | 0 | 0 |
| `registries_in_scope` | TEXT | YES |  |  | 0 | 0 | 0 |
| `registries_completed_at_run` | INTEGER |  |  |  | 0 | 0 | 0 |
| `session_b_sources` | TEXT |  |  |  | 0 | 0 | 0 |
| `run_summary` | TEXT |  |  |  | 0 | 0 | 0 |
| `json_filename` | TEXT |  |  |  | 0 | 0 | 0 |

### `session_d_term_links`  (0 rows, 8 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 0 | 0 | 0 |
| `run_id` | TEXT | YES |  |  | 0 | 0 | 0 |
| `strongs_id` | TEXT | YES |  |  | 0 | 0 | 0 |
| `transliteration` | TEXT |  |  |  | 0 | 0 | 0 |
| `registry_data` | TEXT | YES |  |  | 0 | 0 | 0 |
| `status_divergence` | INTEGER |  |  | 0 | 0 | 0 | 0 |
| `gate` | TEXT | YES |  |  | 0 | 0 | 0 |
| `raised_date` | TEXT | YES |  |  | 0 | 0 | 0 |

### `session_d_verse_links`  (0 rows, 9 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 0 | 0 | 0 |
| `run_id` | TEXT | YES |  |  | 0 | 0 | 0 |
| `verse_ref` | TEXT | YES |  |  | 0 | 0 | 0 |
| `registry_ids` | TEXT | YES |  |  | 0 | 0 | 0 |
| `terms_involved` | TEXT |  |  |  | 0 | 0 | 0 |
| `overlap_count` | INTEGER |  |  |  | 0 | 0 | 0 |
| `threshold_met` | INTEGER |  |  | 0 | 0 | 0 | 0 |
| `gate` | TEXT | YES |  |  | 0 | 0 | 0 |
| `raised_date` | TEXT | YES |  |  | 0 | 0 | 0 |

### `sources`  (0 rows, 6 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 0 | 0 | 0 |
| `zotero_key` | TEXT |  |  |  | 0 | 0 | 0 |
| `title` | TEXT | YES |  |  | 0 | 0 | 0 |
| `author` | TEXT |  |  |  | 0 | 0 | 0 |
| `year` | INTEGER |  |  |  | 0 | 0 | 0 |
| `source_type` | TEXT |  |  |  | 0 | 0 | 0 |

### `term_fetch_log`  (2317 rows, 14 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 2317 | 2317 | 0 |
| `run_id` | TEXT | YES |  |  | 2317 | 17 | 0 |
| `registry_id` | TEXT | YES |  |  | 2317 | 147 | 0 |
| `strongs_input` | TEXT | YES |  |  | 2317 | 959 | 0 |
| `strongs_resolved` | TEXT |  |  |  | 2317 | 848 | 0 |
| `suffix_resolution` | INTEGER |  |  | 0 | 2317 | 2 | 0 |
| `vocab_status` | TEXT |  |  |  | 2317 | 2 | 0 |
| `verse_status` | TEXT |  |  |  | 2317 | 4 | 0 |
| `verse_count_fetched` | INTEGER |  |  | 0 | 2317 | 168 | 0 |
| `verse_count_stored` | INTEGER |  |  | 0 | 2317 | 168 | 0 |
| `verse_count_filtered` | INTEGER |  |  | 0 | 2317 | 1 | 0 |
| `span_conflict` | INTEGER |  |  | 0 | 2317 | 1 | 0 |
| `api_warnings` | TEXT |  |  |  | 0 | 0 | 0 |
| `fetched_at` | TEXT |  |  |  | 2317 | 325 | 0 |

### `themes`  (0 rows, 3 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 0 | 0 | 0 |
| `name` | TEXT | YES |  |  | 0 | 0 | 0 |
| `description` | TEXT |  |  |  | 0 | 0 | 0 |

### `verse_context`  (63028 rows, 11 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 63028 | 63028 | 0 |
| `verse_record_id` | INTEGER | YES |  |  | 63028 | 62699 | 0 |
| `mti_term_id` | INTEGER | YES |  |  | 63028 | 2591 | 0 |
| `group_id` | INTEGER |  |  |  | 35798 | 3549 | 0 |
| `is_anchor` | INTEGER | YES |  | 0 | 63028 | 2 | 0 |
| `is_relevant` | INTEGER | YES |  | 0 | 63028 | 2 | 0 |
| `is_related` | INTEGER | YES |  | 0 | 63028 | 2 | 0 |
| `notes` | TEXT |  |  | NULL | 6328 | 188 | 0 |
| `delete_flagged` | INTEGER |  |  | 0 | 63028 | 2 | 0 |
| `vertical_pass_flag` | INTEGER |  |  | 0 | 63028 | 1 | 0 |
| `set_aside_reason` | TEXT |  |  | NULL | 502 | 7 | 0 |

### `verse_context_group`  (3550 rows, 7 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 3550 | 3550 | 0 |
| `mti_term_id` | INTEGER | YES |  |  | 3550 | 2238 | 0 |
| `group_code` | TEXT | YES |  |  | 3550 | 3550 | 0 |
| `context_description` | TEXT | YES |  |  | 3550 | 3520 | 0 |
| `notes` | TEXT |  |  | NULL | 325 | 146 | 0 |
| `delete_flagged` | INTEGER |  |  | 0 | 3550 | 2 | 0 |
| `vertical_pass_flag` | INTEGER |  |  | 0 | 3550 | 1 | 0 |

### `wa_cross_registry_links`  (158 rows, 8 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 158 | 158 | 0 |
| `file_id` | INTEGER | YES |  |  | 158 | 43 | 0 |
| `linked_word` | TEXT |  |  |  | 158 | 43 | 0 |
| `linked_registry_id` | INTEGER |  |  |  | 151 | 33 | 0 |
| `connection_type_id` | INTEGER | YES |  |  | 158 | 11 | 0 |
| `connecting_term` | TEXT |  |  |  | 152 | 117 | 0 |
| `note` | TEXT |  |  |  | 158 | 156 | 0 |
| `last_changed` | TEXT |  |  |  | 146 | 2 | 0 |

### `wa_crosslink_type`  (11 rows, 3 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 11 | 11 | 0 |
| `type_code` | TEXT | YES |  |  | 11 | 11 | 0 |
| `description` | TEXT |  |  |  | 11 | 11 | 0 |

### `wa_data_quality_flags`  (22129 rows, 6 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 22129 | 22129 | 0 |
| `file_id` | INTEGER | YES |  |  | 22129 | 202 | 0 |
| `term_id` | TEXT |  |  |  | 22129 | 4243 | 0 |
| `flag_id` | INTEGER | YES |  |  | 22129 | 7 | 0 |
| `description` | TEXT |  |  |  | 22129 | 9281 | 0 |
| `last_changed` | TEXT |  |  |  | 323 | 4 | 0 |

### `wa_dim_review_cluster_log`  (5 rows, 9 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 5 | 5 | 0 |
| `cluster` | TEXT | YES |  |  | 5 | 5 | 0 |
| `completed_date` | TEXT | YES |  |  | 5 | 3 | 0 |
| `instruction_version` | TEXT | YES |  |  | 5 | 4 | 0 |
| `registry_count` | INTEGER | YES |  | 0 | 5 | 5 | 0 |
| `group_count` | INTEGER | YES |  | 0 | 5 | 5 | 0 |
| `anchored_count` | INTEGER | YES |  | 0 | 5 | 1 | 0 |
| `notes` | TEXT |  |  |  | 5 | 5 | 0 |
| `last_modified` | TEXT | YES |  | strftime('%Y-%m-%dT%H:%M:%S','now') | 5 | 5 | 0 |

### `wa_dimension_index`  (3500 rows, 23 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 3500 | 3500 | 0 |
| `verse_context_group_id` | INTEGER | YES |  |  | 3500 | 3500 | 0 |
| `mti_term_id` | INTEGER | YES |  |  | 3500 | 2195 | 0 |
| `strongs_number` | TEXT | YES |  |  | 3500 | 2195 | 0 |
| `transliteration` | TEXT |  |  |  | 3500 | 1945 | 0 |
| `gloss` | TEXT |  |  |  | 3500 | 1551 | 0 |
| `language` | TEXT |  |  |  | 3500 | 2 | 0 |
| `owning_registry_no` | INTEGER | YES |  |  | 3500 | 173 | 0 |
| `owning_registry_word` | TEXT | YES |  |  | 3500 | 173 | 0 |
| `cluster_assignment` | TEXT |  |  |  | 3500 | 22 | 0 |
| `group_code` | TEXT | YES |  |  | 3500 | 3500 | 0 |
| `context_description` | TEXT | YES |  |  | 3500 | 3478 | 0 |
| `dimension` | TEXT |  |  |  | 3250 | 24 | 0 |
| `anchor_count` | INTEGER |  |  | 0 | 3500 | 7 | 0 |
| `related_count` | INTEGER |  |  | 0 | 3500 | 98 | 0 |
| `set_aside_count` | INTEGER |  |  | 0 | 3500 | 124 | 0 |
| `total_verse_count` | INTEGER |  |  | 0 | 3500 | 101 | 0 |
| `delete_flagged` | INTEGER |  |  | 0 | 3500 | 2 | 0 |
| `dimension_confidence` | TEXT |  |  | NULL | 3500 | 5 | 0 |
| `manual_override` | INTEGER |  |  | 0 | 3500 | 2 | 0 |
| `notes` | TEXT |  |  | NULL | 1383 | 1075 | 0 |
| `last_modified` | TEXT |  |  | NULL | 3500 | 11 | 0 |
| `dominant_subject` | TEXT |  |  | NULL | 946 | 5 | 0 |

### `wa_file_index`  (206 rows, 20 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 206 | 206 | 0 |
| `filename` | TEXT | YES |  |  | 206 | 75 | 0 |
| `registry_id` | TEXT | YES |  |  | 206 | 184 | 0 |
| `word_registry_fk` | INTEGER |  |  |  | 206 | 184 | 0 |
| `word` | TEXT | YES |  |  | 206 | 184 | 0 |
| `part_number` | INTEGER |  |  |  | 39 | 3 | 0 |
| `total_parts` | INTEGER |  |  |  | 39 | 3 | 0 |
| `is_split` | INTEGER |  |  |  | 206 | 2 | 0 |
| `schema_version` | TEXT |  |  |  | 57 | 5 | 0 |
| `phase` | TEXT |  |  |  | 205 | 10 | 0 |
| `produced_date` | TEXT |  |  |  | 205 | 17 | 0 |
| `source_file` | TEXT |  |  |  | 57 | 54 | 0 |
| `translation_used` | TEXT |  |  |  | 205 | 1 | 0 |
| `specification` | TEXT |  |  |  | 206 | 8 | 0 |
| `revision_note` | TEXT |  |  |  | 6 | 3 | 0 |
| `source_list` | TEXT |  |  |  | 201 | 6 | 0 |
| `category` | TEXT |  |  |  | 13 | 6 | 0 |
| `testament_coverage` | TEXT |  |  |  | 204 | 3 | 0 |
| `root_families_in_prior_parts` | TEXT |  |  |  | 22 | 22 | 0 |
| `last_changed` | TEXT |  |  | datetime('now') | 206 | 42 | 0 |

### `wa_finding_catalogue_links`  (0 rows, 11 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 0 | 0 | 0 |
| `finding_id` | INTEGER | YES |  |  | 0 | 0 | 0 |
| `question_id` | INTEGER | YES |  |  | 0 | 0 | 0 |
| `coverage` | TEXT |  |  |  | 0 | 0 | 0 |
| `status` | TEXT | YES |  | 'suggested' | 0 | 0 | 0 |
| `pattern_type` | TEXT |  |  |  | 0 | 0 | 0 |
| `mapped_date` | TEXT |  |  |  | 0 | 0 | 0 |
| `validated_date` | TEXT |  |  |  | 0 | 0 | 0 |
| `validated_by` | TEXT |  |  |  | 0 | 0 | 0 |
| `session_b_note` | TEXT |  |  |  | 0 | 0 | 0 |
| `delete_flagged` | INTEGER | YES |  | 0 | 0 | 0 | 0 |

### `wa_finding_entity_links`  (0 rows, 7 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 0 | 0 | 0 |
| `finding_id` | INTEGER | YES |  |  | 0 | 0 | 0 |
| `entity_type` | TEXT | YES |  |  | 0 | 0 | 0 |
| `entity_id` | INTEGER |  |  |  | 0 | 0 | 0 |
| `entity_strongs` | TEXT |  |  |  | 0 | 0 | 0 |
| `raised_date` | TEXT | YES |  |  | 0 | 0 | 0 |
| `delete_flagged` | INTEGER | YES |  | 0 | 0 | 0 | 0 |

### `wa_lsj_parsed`  (2 rows, 10 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 2 | 2 | 0 |
| `term_inv_id` | INTEGER | YES |  |  | 2 | 2 | 0 |
| `raw_lsj` | TEXT |  |  |  | 2 | 2 | 0 |
| `lsj_gloss` | TEXT |  |  |  | 2 | 2 | 0 |
| `lsj_domains` | TEXT |  |  |  | 1 | 1 | 0 |
| `lsj_philosophical_note` | TEXT |  |  |  | 0 | 0 | 0 |
| `lsj_etymology_note` | TEXT |  |  |  | 0 | 0 | 0 |
| `lsj_cognate_forms` | TEXT |  |  |  | 0 | 0 | 0 |
| `parsed_at` | TEXT | YES |  |  | 2 | 2 | 0 |
| `parse_version` | TEXT | YES |  |  | 2 | 1 | 0 |

### `wa_meaning_parsed`  (7449 rows, 11 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 7449 | 7449 | 0 |
| `term_inv_id` | INTEGER | YES |  |  | 7449 | 7449 | 0 |
| `strongs_number` | TEXT | YES |  |  | 7449 | 3 | 0 |
| `language` | TEXT | YES |  |  | 7449 | 2 | 0 |
| `top_sense_count` | INTEGER |  |  | 0 | 7449 | 7 | 0 |
| `stem_count` | INTEGER |  |  | 0 | 7449 | 4 | 0 |
| `has_causative_stem` | INTEGER |  |  | 0 | 7449 | 2 | 0 |
| `has_domain_tags` | INTEGER |  |  | 0 | 7449 | 1 | 0 |
| `parsed_at` | TEXT | YES |  |  | 7449 | 208 | 0 |
| `parse_version` | TEXT | YES |  |  | 7449 | 1 | 0 |
| `parse_warnings` | TEXT |  |  |  | 5533 | 1 | 0 |

### `wa_meaning_sense`  (15981 rows, 10 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 15981 | 15981 | 0 |
| `parsed_meaning_id` | INTEGER | YES |  |  | 15981 | 7450 | 0 |
| `level_code` | TEXT | YES |  |  | 15981 | 120 | 0 |
| `level_depth` | INTEGER | YES |  |  | 15981 | 3 | 0 |
| `parent_level_code` | TEXT |  |  |  | 339 | 4 | 0 |
| `sense_text` | TEXT |  |  |  | 15981 | 6797 | 0 |
| `is_stem_label` | INTEGER |  |  | 0 | 15981 | 1 | 0 |
| `stem_label` | TEXT |  |  |  | 0 | 0 | 0 |
| `domain_tag` | TEXT |  |  |  | 0 | 0 | 0 |
| `sort_order` | INTEGER | YES |  |  | 15981 | 35 | 0 |

### `wa_meaning_stem`  (13 rows, 6 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 13 | 13 | 0 |
| `parsed_meaning_id` | INTEGER | YES |  |  | 13 | 3 | 0 |
| `stem_name` | TEXT | YES |  |  | 13 | 8 | 0 |
| `stem_type` | TEXT |  |  |  | 13 | 4 | 0 |
| `sense_count` | INTEGER |  |  | 0 | 13 | 5 | 0 |
| `top_sense_text` | TEXT |  |  |  | 13 | 13 | 0 |

### `wa_obs_question_catalogue`  (194 rows, 12 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obs_id` | INTEGER |  | YES |  | 194 | 194 | 0 |
| `question_code` | TEXT | YES |  |  | 194 | 194 | 0 |
| `section` | TEXT | YES |  |  | 194 | 9 | 0 |
| `source_word` | TEXT |  |  |  | 194 | 5 | 0 |
| `source_registry_no` | INTEGER |  |  |  | 194 | 5 | 0 |
| `question_text` | TEXT | YES |  |  | 194 | 194 | 0 |
| `pattern_type` | TEXT |  |  |  | 0 | 0 | 0 |
| `scope` | TEXT | YES |  | 'universal' | 194 | 1 | 0 |
| `status` | TEXT | YES |  | 'active' | 194 | 1 | 0 |
| `deleted` | INTEGER | YES |  | 0 | 194 | 1 | 0 |
| `date_added` | TEXT | YES |  |  | 194 | 1 | 0 |
| `catalogue_version` | TEXT | YES |  |  | 194 | 1 | 0 |

### `wa_quality_flag_types`  (29 rows, 7 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 29 | 29 | 0 |
| `flag_group` | TEXT | YES |  |  | 29 | 7 | 0 |
| `flag_code` | TEXT | YES |  |  | 29 | 29 | 0 |
| `description` | TEXT |  |  |  | 28 | 28 | 0 |
| `deprecated` | INTEGER |  |  | 0 | 29 | 2 | 0 |
| `deprecation_note` | TEXT |  |  |  | 3 | 1 | 0 |
| `category` | TEXT |  |  |  | 15 | 4 | 0 |

### `wa_session_b_dimensions`  (2 rows, 13 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 2 | 2 | 0 |
| `registry_id` | INTEGER | YES |  |  | 2 | 2 | 0 |
| `file_id` | INTEGER |  |  |  | 2 | 2 | 0 |
| `relational_environment` | INTEGER |  |  | 0 | 2 | 1 | 0 |
| `relational_environment_note` | TEXT |  |  |  | 2 | 2 | 0 |
| `spirit_soul_body` | INTEGER |  |  | 0 | 2 | 1 | 0 |
| `spirit_soul_body_note` | TEXT |  |  |  | 2 | 2 | 0 |
| `inner_operations` | INTEGER |  |  | 0 | 2 | 1 | 0 |
| `inner_operations_note` | TEXT |  |  |  | 2 | 2 | 0 |
| `being` | INTEGER |  |  | 0 | 2 | 1 | 0 |
| `being_note` | TEXT |  |  |  | 2 | 2 | 0 |
| `raised_date` | TEXT | YES |  |  | 2 | 2 | 0 |
| `session_b_instruction` | TEXT | YES |  |  | 2 | 2 | 0 |

### `wa_session_b_findings`  (187 rows, 20 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 187 | 187 | 0 |
| `finding_id` | TEXT | YES |  |  | 187 | 187 | 0 |
| `registry_id` | INTEGER | YES |  |  | 187 | 110 | 0 |
| `file_id` | INTEGER |  |  |  | 20 | 2 | 0 |
| `finding_type` | TEXT | YES |  |  | 187 | 23 | 0 |
| `finding` | TEXT | YES |  |  | 187 | 187 | 0 |
| `anchor_verses` | TEXT |  |  |  | 75 | 74 | 0 |
| `raised_date` | TEXT | YES |  |  | 187 | 9 | 0 |
| `session_b_instruction` | TEXT | YES |  |  | 187 | 10 | 0 |
| `pass_ref` | TEXT |  |  |  | 0 | 0 | 0 |
| `study_segment` | TEXT |  |  |  | 0 | 0 | 0 |
| `delete_flag` | INTEGER |  |  | 0 | 187 | 1 | 0 |
| `obsolete_reason` | TEXT |  |  |  | 0 | 0 | 0 |
| `obsolete_date` | TEXT |  |  |  | 0 | 0 | 0 |
| `superseded_by_id` | INTEGER |  |  |  | 0 | 0 | 0 |
| `related_finding_id` | INTEGER |  |  |  | 0 | 0 | 0 |
| `resolution_note` | TEXT |  |  |  | 0 | 0 | 0 |
| `thin_evidence` | INTEGER |  |  | 0 | 187 | 1 | 0 |
| `status` | TEXT |  |  | 'pending' | 187 | 2 | 0 |
| `term_id` | INTEGER |  |  |  | 0 | 0 | 0 |

### `wa_session_research_flags`  (336 rows, 15 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 336 | 336 | 0 |
| `registry_id` | INTEGER | YES |  |  | 336 | 72 | 0 |
| `file_id` | INTEGER |  |  |  | 125 | 21 | 0 |
| `flag_code` | TEXT | YES |  |  | 336 | 15 | 0 |
| `flag_label` | TEXT | YES |  |  | 336 | 336 | 0 |
| `strongs_reference` | TEXT |  |  |  | 160 | 119 | 0 |
| `cross_registry_id` | INTEGER |  |  |  | 151 | 70 | 0 |
| `priority` | TEXT |  |  | 'MEDIUM' | 336 | 3 | 0 |
| `session_target` | TEXT |  |  | 'D' | 336 | 2 | 0 |
| `description` | TEXT | YES |  |  | 336 | 336 | 0 |
| `session_raised` | TEXT | YES |  |  | 336 | 35 | 0 |
| `raised_date` | TEXT | YES |  |  | 336 | 14 | 0 |
| `resolved` | INTEGER | YES |  | 0 | 336 | 1 | 0 |
| `resolved_date` | TEXT |  |  |  | 0 | 0 | 0 |
| `resolved_note` | TEXT |  |  |  | 0 | 0 | 0 |

### `wa_term_inventory`  (7550 rows, 26 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 7550 | 7550 | 0 |
| `file_id` | INTEGER | YES |  |  | 7550 | 206 | 0 |
| `language` | TEXT | YES |  |  | 7550 | 2 | 0 |
| `term_id` | TEXT | YES |  |  | 7550 | 3908 | 0 |
| `strongs_number` | TEXT |  |  |  | 7541 | 3894 | 0 |
| `transliteration` | TEXT | YES |  |  | 7550 | 3115 | 0 |
| `step_search_gloss` | TEXT |  |  |  | 7550 | 2736 | 0 |
| `word_analysis_gloss` | TEXT |  |  |  | 7541 | 2733 | 0 |
| `occurrence_count` | INTEGER |  |  |  | 7530 | 378 | 0 |
| `occurrence_count_qualifier` | TEXT |  |  |  | 642 | 4 | 0 |
| `meaning` | TEXT |  |  |  | 77 | 74 | 0 |
| `meaning_numbered` | TEXT |  |  |  | 86 | 4 | 0 |
| `also_spelled` | TEXT |  |  |  | 18 | 17 | 0 |
| `lsj_entry` | TEXT |  |  |  | 2214 | 1241 | 0 |
| `testament` | TEXT |  |  |  | 7539 | 3 | 0 |
| `god_as_subject` | INTEGER |  |  | 0 | 7550 | 2 | 0 |
| `somatic_link` | INTEGER |  |  | 0 | 7550 | 2 | 0 |
| `causative_form_present` | INTEGER |  |  | 0 | 7550 | 2 | 0 |
| `status_note` | TEXT |  |  |  | 177 | 142 | 0 |
| `last_changed` | TEXT |  |  | datetime('now') | 7550 | 221 | 0 |
| `short_def_mounce` | TEXT |  |  |  | 2207 | 1266 | 0 |
| `parsed_meaning_id` | INTEGER |  |  |  | 7449 | 7449 | 0 |
| `delete_flagged` | INTEGER |  |  | 0 | 7550 | 2 | 0 |
| `evidential_status` | TEXT |  |  | NULL | 155 | 3 | 0 |
| `retention_note` | TEXT |  |  | NULL | 53 | 49 | 0 |
| `term_owner_type` | TEXT |  |  | NULL | 7093 | 2 | 0 |

### `wa_term_phase2_flags`  (1580 rows, 7 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `term_inv_id` | INTEGER | YES | YES |  | 1580 | 891 | 0 |
| `flag_id` | INTEGER | YES | YES |  | 1580 | 25 | 0 |
| `description` | TEXT |  |  |  | 17 | 13 | 0 |
| `source` | TEXT |  |  |  | 1119 | 4 | 0 |
| `raised_date` | TEXT |  |  |  | 1119 | 2 | 0 |
| `delete_flagged` | INTEGER |  |  | 0 | 1580 | 2 | 0 |
| `obsolete_reason` | TEXT |  |  |  | 1 | 1 | 0 |

### `wa_term_related_words`  (101970 rows, 7 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 101970 | 101970 | 0 |
| `term_inv_id` | INTEGER | YES |  |  | 101970 | 7318 | 0 |
| `gloss` | TEXT |  |  |  | 101970 | 4516 | 0 |
| `transliteration` | TEXT |  |  |  | 101968 | 4776 | 0 |
| `strongs_number` | TEXT |  |  |  | 100373 | 6964 | 0 |
| `relationship_note` | TEXT |  |  |  | 315 | 8 | 0 |
| `delete_flagged` | INTEGER |  |  | 0 | 101970 | 1 | 0 |

### `wa_term_root_family`  (2861 rows, 7 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 2861 | 2861 | 0 |
| `term_inv_id` | INTEGER | YES |  |  | 2861 | 2860 | 0 |
| `root_code` | TEXT | YES |  |  | 2861 | 964 | 0 |
| `root_language` | TEXT |  |  |  | 2227 | 3 | 0 |
| `root_gloss` | TEXT |  |  |  | 2227 | 591 | 0 |
| `note` | TEXT |  |  |  | 2234 | 17 | 0 |
| `delete_flagged` | INTEGER |  |  | 0 | 2861 | 2 | 0 |

### `wa_verse_records`  (229778 rows, 23 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 229778 | 229778 | 0 |
| `file_id` | INTEGER | YES |  |  | 229778 | 205 | 0 |
| `term_inv_id` | INTEGER |  |  |  | 229778 | 7034 | 0 |
| `term_id` | TEXT |  |  |  | 229777 | 3737 | 0 |
| `transliteration` | TEXT |  |  |  | 229777 | 3008 | 0 |
| `testament` | TEXT |  |  |  | 229778 | 2 | 0 |
| `reference` | TEXT |  |  |  | 229778 | 27516 | 0 |
| `verse_text` | TEXT |  |  |  | 229778 | 30087 | 0 |
| `last_changed` | TEXT |  |  | datetime('now') | 229778 | 805 | 0 |
| `book_id` | INTEGER |  |  |  | 229777 | 66 | 0 |
| `chapter` | INTEGER |  |  |  | 229778 | 150 | 0 |
| `verse_num` | INTEGER |  |  |  | 229778 | 176 | 0 |
| `translation` | TEXT | YES |  | 'ESV' | 229778 | 1 | 0 |
| `note` | TEXT |  |  |  | 0 | 0 | 0 |
| `claude_output` | TEXT |  |  |  | 0 | 0 | 0 |
| `created_at` | TEXT |  |  |  | 180607 | 193 | 0 |
| `updated_at` | TEXT |  |  |  | 225888 | 14 | 0 |
| `target_word` | TEXT |  |  |  | 226585 | 9112 | 0 |
| `span_strong_match` | INTEGER |  |  |  | 226520 | 1 | 0 |
| `context_before` | TEXT |  |  |  | 193375 | 75843 | 0 |
| `context_after` | TEXT |  |  |  | 193375 | 66701 | 0 |
| `delete_flagged` | INTEGER |  |  | 0 | 229778 | 2 | 0 |
| `mti_term_id` | INTEGER |  |  | NULL | 224529 | 3648 | 0 |

### `wa_verse_term_links`  (226791 rows, 8 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 226791 | 226791 | 0 |
| `verse_id` | INTEGER | YES |  |  | 226791 | 226782 | 0 |
| `term_inv_id` | INTEGER | YES |  |  | 226791 | 7033 | 0 |
| `step_subgloss_code` | TEXT |  |  |  | 226719 | 3612 | 0 |
| `step_subgloss_label` | TEXT |  |  |  | 226697 | 2563 | 0 |
| `span_strong_match` | INTEGER |  |  |  | 226529 | 1 | 0 |
| `target_word` | TEXT |  |  |  | 226594 | 9114 | 0 |
| `created_at` | TEXT |  |  | strftime('%Y-%m-%dT%H:%M:%S','now') | 226791 | 492 | 0 |

### `word_registry`  (214 rows, 31 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 214 | 214 | 0 |
| `no` | INTEGER |  |  |  | 214 | 214 | 0 |
| `word` | TEXT | YES |  |  | 214 | 210 | 0 |
| `source_list` | TEXT |  |  |  | 214 | 6 | 0 |
| `category_hint` | TEXT |  |  |  | 36 | 22 | 0 |
| `phase1_input_file` | TEXT |  |  |  | 46 | 46 | 0 |
| `phase1_status` | TEXT |  |  |  | 214 | 3 | 0 |
| `phase1_output_file` | TEXT |  |  |  | 32 | 32 | 0 |
| `phase2_datasets` | REAL |  |  |  | 30 | 7 | 0 |
| `notes` | TEXT |  |  |  | 213 | 213 | 0 |
| `automation_eligible` | INTEGER |  |  | 1 | 214 | 2 | 0 |
| `last_automation_run` | TEXT |  |  |  | 213 | 14 | 0 |
| `automation_run_id` | TEXT |  |  |  | 213 | 184 | 0 |
| `phase1_term_count` | INTEGER |  |  |  | 214 | 75 | 0 |
| `phase1_verse_count` | INTEGER |  |  |  | 214 | 170 | 0 |
| `strongs_list` | TEXT |  |  |  | 213 | 184 | 0 |
| `description` | TEXT |  |  |  | 210 | 210 | 0 |
| `origin` | TEXT |  |  |  | 212 | 2 | 0 |
| `dimensions` | TEXT |  |  |  | 188 | 15 | 0 |
| `inference_note` | TEXT |  |  |  | 24 | 21 | 0 |
| `session_b_status` | TEXT |  |  |  | 184 | 3 | 0 |
| `cluster_assignment` | TEXT |  |  | "unassigned" | 214 | 22 | 0 |
| `sb_classification` | TEXT |  |  | NULL | 7 | 4 | 0 |
| `sb_classification_reasoning` | TEXT |  |  | NULL | 5 | 5 | 0 |
| `carry_forward` | INTEGER |  |  | 1 | 213 | 1 | 0 |
| `unique_term_count` | INTEGER |  |  | 0 | 214 | 41 | 0 |
| `shared_term_count` | INTEGER |  |  | 0 | 214 | 66 | 0 |
| `term_sharing_ratio` | REAL |  |  | 0.0 | 214 | 99 | 0 |
| `verse_context_status` | TEXT |  |  | NULL | 184 | 2 | 0 |
| `dim_review_status` | TEXT |  |  | NULL | 35 | 1 | 0 |
| `dim_review_version` | TEXT |  |  | NULL | 35 | 4 | 0 |

### `word_run_state`  (437 rows, 11 cols)

| col | type | NOT NULL | PK | default | non-NULL | distinct | code refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | INTEGER |  | YES |  | 437 | 437 | 0 |
| `run_id` | TEXT | YES |  |  | 437 | 271 | 0 |
| `registry_id` | TEXT | YES |  |  | 437 | 278 | 0 |
| `word` | TEXT | YES |  |  | 437 | 209 | 0 |
| `phase_reached` | TEXT |  |  |  | 437 | 4 | 0 |
| `audit_result` | TEXT |  |  |  | 437 | 3 | 0 |
| `audit_detail` | TEXT |  |  |  | 437 | 375 | 0 |
| `stop_reason` | TEXT |  |  |  | 8 | 7 | 0 |
| `researcher_approved` | INTEGER |  |  | 0 | 437 | 1 | 0 |
| `approved_by` | TEXT |  |  |  | 230 | 1 | 0 |
| `approved_at` | TEXT |  |  |  | 0 | 0 | 0 |

### §A.2 Cross-findings

**Total columns:** 464 across 43 tables.

**Columns with zero non-NULL anywhere** (25) — CLEANUP_CANDIDATE if also zero code references:

| table | column | table row count |
| --- | --- | --- |
| `engine_run_log` | `resume_from` | 620 |
| `engine_stream_checkpoint` | `last_registry_id` | 1169 |
| `engine_stream_checkpoint` | `last_strong` | 1169 |
| `engine_stream_checkpoint` | `error_detail` | 1169 |
| `schema_version` | `engine_min_version` | 3 |
| `term_fetch_log` | `api_warnings` | 2317 |
| `wa_lsj_parsed` | `lsj_philosophical_note` | 2 |
| `wa_lsj_parsed` | `lsj_etymology_note` | 2 |
| `wa_lsj_parsed` | `lsj_cognate_forms` | 2 |
| `wa_meaning_sense` | `stem_label` | 15981 |
| `wa_meaning_sense` | `domain_tag` | 15981 |
| `wa_obs_question_catalogue` | `pattern_type` | 194 |
| `wa_session_b_findings` | `pass_ref` | 187 |
| `wa_session_b_findings` | `study_segment` | 187 |
| `wa_session_b_findings` | `obsolete_reason` | 187 |
| `wa_session_b_findings` | `obsolete_date` | 187 |
| `wa_session_b_findings` | `superseded_by_id` | 187 |
| `wa_session_b_findings` | `related_finding_id` | 187 |
| `wa_session_b_findings` | `resolution_note` | 187 |
| `wa_session_b_findings` | `term_id` | 187 |
| `wa_session_research_flags` | `resolved_date` | 336 |
| `wa_session_research_flags` | `resolved_note` | 336 |
| `wa_verse_records` | `note` | 229778 |
| `wa_verse_records` | `claude_output` | 229778 |
| `word_run_state` | `approved_at` | 437 |

**Single-value columns** (same value across all rows where row count > 10, cardinality 1): 19 — INFORMATIONAL:

| table | column | distinct | non-NULL |
| --- | --- | --- | --- |
| `books` | `last_updated` | 1 | 66 |
| `term_fetch_log` | `verse_count_filtered` | 1 | 2317 |
| `term_fetch_log` | `span_conflict` | 1 | 2317 |
| `verse_context` | `vertical_pass_flag` | 1 | 63028 |
| `verse_context_group` | `vertical_pass_flag` | 1 | 3550 |
| `wa_meaning_parsed` | `has_domain_tags` | 1 | 7449 |
| `wa_meaning_parsed` | `parse_version` | 1 | 7449 |
| `wa_meaning_sense` | `is_stem_label` | 1 | 15981 |
| `wa_obs_question_catalogue` | `scope` | 1 | 194 |
| `wa_obs_question_catalogue` | `status` | 1 | 194 |
| `wa_obs_question_catalogue` | `deleted` | 1 | 194 |
| `wa_obs_question_catalogue` | `date_added` | 1 | 194 |
| `wa_obs_question_catalogue` | `catalogue_version` | 1 | 194 |
| `wa_session_b_findings` | `delete_flag` | 1 | 187 |
| `wa_session_b_findings` | `thin_evidence` | 1 | 187 |
| `wa_session_research_flags` | `resolved` | 1 | 336 |
| `wa_term_related_words` | `delete_flagged` | 1 | 101970 |
| `wa_verse_records` | `translation` | 1 | 229778 |
| `word_run_state` | `researcher_approved` | 1 | 437 |

**Zero code references** (not PK): 419 — CLEANUP_CANDIDATE if no external consumer:

| table | zero-ref columns |
| --- | --- |
| `book_code_variants` | `book_id` |
| `books` | `name`, `abbreviation`, `testament`, `book_order`, `full_name`, `short_code`, `verse_count`, `last_updated` |
| `engine_run_log` | `run_id`, `mode`, `target_registry_ids`, `started_at`, `completed_at`, `outcome`, `words_attempted`, `words_complete`, `words_stopped`, `total_terms_new`, `total_terms_xref`, `total_verses_inserted`, `total_verses_filtered`, `total_meanings_parsed`, `error_detail`, `resume_from` |
| `engine_stream_checkpoint` | `run_id`, `stream_name`, `status`, `last_registry_id`, `last_strong`, `rows_written`, `rows_filtered`, `error_detail`, `started_at`, `completed_at` |
| `mti_term_cross_refs` | `mti_term_id`, `registry`, `registry_fk`, `word`, `part`, `word_data_reference` |
| `mti_terms` | `strongs_number`, `transliteration`, `gloss`, `language`, `owning_registry`, `owning_registry_fk`, `owning_word`, `owning_part`, `word_data_reference`, `word_data_ref_fk`, `status`, `status_note`, `exclusion_reason`, `extraction_date`, `strongs_reconciled`, `anchor_note`, `last_changed`, `delete_flagged` |
| `phase2_flag_types` | `flag_code`, `description` |
| `schema_version` | `version_code`, `applied_at`, `migration_history`, `engine_min_version` |
| `session_d_observations` | `run_id`, `observation_id`, `observation_type`, `registries_implicated`, `terms_implicated`, `structural_note`, `source_refs`, `gate`, `researcher_flag`, `raised_date` |
| `session_d_runs` | `run_id`, `run_date`, `cluster_ref`, `registries_in_scope`, `registries_completed_at_run`, `session_b_sources`, `run_summary`, `json_filename` |
| `session_d_term_links` | `run_id`, `strongs_id`, `transliteration`, `registry_data`, `status_divergence`, `gate`, `raised_date` |
| `session_d_verse_links` | `run_id`, `verse_ref`, `registry_ids`, `terms_involved`, `overlap_count`, `threshold_met`, `gate`, `raised_date` |
| `sources` | `zotero_key`, `title`, `author`, `year`, `source_type` |
| `term_fetch_log` | `run_id`, `registry_id`, `strongs_input`, `strongs_resolved`, `suffix_resolution`, `vocab_status`, `verse_status`, `verse_count_fetched`, `verse_count_stored`, `verse_count_filtered`, `span_conflict`, `api_warnings`, `fetched_at` |
| `themes` | `name`, `description` |
| `verse_context` | `verse_record_id`, `mti_term_id`, `group_id`, `is_anchor`, `is_relevant`, `is_related`, `notes`, `delete_flagged`, `vertical_pass_flag`, `set_aside_reason` |
| `verse_context_group` | `mti_term_id`, `group_code`, `context_description`, `notes`, `delete_flagged`, `vertical_pass_flag` |
| `wa_cross_registry_links` | `file_id`, `linked_word`, `linked_registry_id`, `connection_type_id`, `connecting_term`, `note`, `last_changed` |
| `wa_crosslink_type` | `type_code`, `description` |
| `wa_data_quality_flags` | `file_id`, `term_id`, `flag_id`, `description`, `last_changed` |
| `wa_dim_review_cluster_log` | `cluster`, `completed_date`, `instruction_version`, `registry_count`, `group_count`, `anchored_count`, `notes`, `last_modified` |
| `wa_dimension_index` | `verse_context_group_id`, `mti_term_id`, `strongs_number`, `transliteration`, `gloss`, `language`, `owning_registry_no`, `owning_registry_word`, `cluster_assignment`, `group_code`, `context_description`, `dimension`, `anchor_count`, `related_count`, `set_aside_count`, `total_verse_count`, `delete_flagged`, `dimension_confidence`, `manual_override`, `notes`, `last_modified`, `dominant_subject` |
| `wa_file_index` | `filename`, `registry_id`, `word_registry_fk`, `word`, `part_number`, `total_parts`, `is_split`, `schema_version`, `phase`, `produced_date`, `source_file`, `translation_used`, `specification`, `revision_note`, `source_list`, `category`, `testament_coverage`, `root_families_in_prior_parts`, `last_changed` |
| `wa_finding_catalogue_links` | `finding_id`, `question_id`, `coverage`, `status`, `pattern_type`, `mapped_date`, `validated_date`, `validated_by`, `session_b_note`, `delete_flagged` |
| `wa_finding_entity_links` | `finding_id`, `entity_type`, `entity_id`, `entity_strongs`, `raised_date`, `delete_flagged` |
| `wa_lsj_parsed` | `term_inv_id`, `raw_lsj`, `lsj_gloss`, `lsj_domains`, `lsj_philosophical_note`, `lsj_etymology_note`, `lsj_cognate_forms`, `parsed_at`, `parse_version` |
| `wa_meaning_parsed` | `term_inv_id`, `strongs_number`, `language`, `top_sense_count`, `stem_count`, `has_causative_stem`, `has_domain_tags`, `parsed_at`, `parse_version`, `parse_warnings` |
| `wa_meaning_sense` | `parsed_meaning_id`, `level_code`, `level_depth`, `parent_level_code`, `sense_text`, `is_stem_label`, `stem_label`, `domain_tag`, `sort_order` |
| `wa_meaning_stem` | `parsed_meaning_id`, `stem_name`, `stem_type`, `sense_count`, `top_sense_text` |
| `wa_obs_question_catalogue` | `question_code`, `section`, `source_word`, `source_registry_no`, `question_text`, `pattern_type`, `scope`, `status`, `deleted`, `date_added`, `catalogue_version` |
| `wa_quality_flag_types` | `flag_group`, `flag_code`, `description`, `deprecated`, `deprecation_note`, `category` |
| `wa_session_b_dimensions` | `registry_id`, `file_id`, `relational_environment`, `relational_environment_note`, `spirit_soul_body`, `spirit_soul_body_note`, `inner_operations`, `inner_operations_note`, `being`, `being_note`, `raised_date`, `session_b_instruction` |
| `wa_session_b_findings` | `finding_id`, `registry_id`, `file_id`, `finding_type`, `finding`, `anchor_verses`, `raised_date`, `session_b_instruction`, `pass_ref`, `study_segment`, `delete_flag`, `obsolete_reason`, `obsolete_date`, `superseded_by_id`, `related_finding_id`, `resolution_note`, `thin_evidence`, `status`, `term_id` |
| `wa_session_research_flags` | `registry_id`, `file_id`, `flag_code`, `flag_label`, `strongs_reference`, `cross_registry_id`, `priority`, `session_target`, `description`, `session_raised`, `raised_date`, `resolved`, `resolved_date`, `resolved_note` |
| `wa_term_inventory` | `file_id`, `language`, `term_id`, `strongs_number`, `transliteration`, `step_search_gloss`, `word_analysis_gloss`, `occurrence_count`, `occurrence_count_qualifier`, `meaning`, `meaning_numbered`, `also_spelled`, `lsj_entry`, `testament`, `god_as_subject`, `somatic_link`, `causative_form_present`, `status_note`, `last_changed`, `short_def_mounce`, `parsed_meaning_id`, `delete_flagged`, `evidential_status`, `retention_note`, `term_owner_type` |
| `wa_term_phase2_flags` | `description`, `source`, `raised_date`, `delete_flagged`, `obsolete_reason` |
| `wa_term_related_words` | `term_inv_id`, `gloss`, `transliteration`, `strongs_number`, `relationship_note`, `delete_flagged` |
| `wa_term_root_family` | `term_inv_id`, `root_code`, `root_language`, `root_gloss`, `note`, `delete_flagged` |
| `wa_verse_records` | `file_id`, `term_inv_id`, `term_id`, `transliteration`, `testament`, `reference`, `verse_text`, `last_changed`, `book_id`, `chapter`, `verse_num`, `translation`, `note`, `claude_output`, `created_at`, `updated_at`, `target_word`, `span_strong_match`, `context_before`, `context_after`, `delete_flagged`, `mti_term_id` |
| `wa_verse_term_links` | `verse_id`, `term_inv_id`, `step_subgloss_code`, `step_subgloss_label`, `span_strong_match`, `target_word`, `created_at` |
| `word_registry` | `no`, `word`, `source_list`, `category_hint`, `phase1_input_file`, `phase1_status`, `phase1_output_file`, `phase2_datasets`, `notes`, `automation_eligible`, `last_automation_run`, `automation_run_id`, `phase1_term_count`, `phase1_verse_count`, `strongs_list`, `description`, `origin`, `dimensions`, `inference_note`, `session_b_status`, `cluster_assignment`, `sb_classification`, `sb_classification_reasoning`, `carry_forward`, `unique_term_count`, `shared_term_count`, `term_sharing_ratio`, `verse_context_status`, `dim_review_status`, `dim_review_version` |
| `word_run_state` | `run_id`, `registry_id`, `word`, `phase_reached`, `audit_result`, `audit_detail`, `stop_reason`, `researcher_approved`, `approved_by`, `approved_at` |

---

## §A.3 — Foreign Key Graph

**44 registered foreign keys** (via `PRAGMA foreign_key_list`).

| child_table.col | → | parent_table.col | ON UPDATE | ON DELETE |
| --- | --- | --- | --- | --- |
| `book_code_variants.book_id` | → | `books.id` | NO ACTION | NO ACTION |
| `engine_stream_checkpoint.run_id` | → | `engine_run_log.run_id` | NO ACTION | NO ACTION |
| `mti_term_cross_refs.registry_fk` | → | `word_registry.id` | NO ACTION | NO ACTION |
| `mti_term_cross_refs.mti_term_id` | → | `mti_terms.id` | NO ACTION | CASCADE |
| `mti_term_flags.flag_id` | → | `phase2_flag_types.id` | NO ACTION | NO ACTION |
| `mti_term_flags.mti_term_id` | → | `mti_terms.id` | NO ACTION | NO ACTION |
| `mti_terms.word_data_ref_fk` | → | `wa_file_index.id` | NO ACTION | NO ACTION |
| `mti_terms.owning_registry_fk` | → | `word_registry.id` | NO ACTION | RESTRICT |
| `term_fetch_log.run_id` | → | `engine_run_log.run_id` | NO ACTION | NO ACTION |
| `verse_context.group_id` | → | `verse_context_group.id` | NO ACTION | NO ACTION |
| `verse_context.mti_term_id` | → | `mti_terms.id` | NO ACTION | NO ACTION |
| `verse_context.verse_record_id` | → | `wa_verse_records.id` | NO ACTION | NO ACTION |
| `verse_context_group.mti_term_id` | → | `mti_terms.id` | NO ACTION | NO ACTION |
| `wa_cross_registry_links.connection_type_id` | → | `wa_crosslink_type.id` | NO ACTION | NO ACTION |
| `wa_cross_registry_links.linked_registry_id` | → | `word_registry.id` | NO ACTION | NO ACTION |
| `wa_cross_registry_links.file_id` | → | `wa_file_index.id` | NO ACTION | NO ACTION |
| `wa_data_quality_flags.flag_id` | → | `wa_quality_flag_types.id` | NO ACTION | NO ACTION |
| `wa_data_quality_flags.file_id` | → | `wa_file_index.id` | NO ACTION | NO ACTION |
| `wa_dimension_index.mti_term_id` | → | `mti_terms.id` | NO ACTION | NO ACTION |
| `wa_dimension_index.verse_context_group_id` | → | `verse_context_group.id` | NO ACTION | NO ACTION |
| `wa_file_index.word_registry_fk` | → | `word_registry.id` | NO ACTION | RESTRICT |
| `wa_finding_catalogue_links.question_id` | → | `wa_obs_question_catalogue.obs_id` | NO ACTION | NO ACTION |
| `wa_finding_catalogue_links.finding_id` | → | `wa_session_b_findings.id` | NO ACTION | NO ACTION |
| `wa_finding_entity_links.finding_id` | → | `wa_session_b_findings.id` | NO ACTION | NO ACTION |
| `wa_lsj_parsed.term_inv_id` | → | `wa_term_inventory.id` | NO ACTION | NO ACTION |
| `wa_meaning_parsed.term_inv_id` | → | `wa_term_inventory.id` | NO ACTION | NO ACTION |
| `wa_meaning_sense.parsed_meaning_id` | → | `wa_meaning_parsed.id` | NO ACTION | NO ACTION |
| `wa_meaning_stem.parsed_meaning_id` | → | `wa_meaning_parsed.id` | NO ACTION | NO ACTION |
| `wa_obs_question_catalogue.source_registry_no` | → | `word_registry.id` | NO ACTION | NO ACTION |
| `wa_session_b_findings.term_id` | → | `mti_terms.id` | NO ACTION | SET NULL |
| `wa_session_research_flags.cross_registry_id` | → | `word_registry.id` | NO ACTION | NO ACTION |
| `wa_session_research_flags.file_id` | → | `wa_file_index.id` | NO ACTION | NO ACTION |
| `wa_session_research_flags.registry_id` | → | `word_registry.id` | NO ACTION | NO ACTION |
| `wa_term_inventory.file_id` | → | `wa_file_index.id` | NO ACTION | RESTRICT |
| `wa_term_phase2_flags.flag_id` | → | `phase2_flag_types.id` | NO ACTION | NO ACTION |
| `wa_term_phase2_flags.term_inv_id` | → | `wa_term_inventory.id` | NO ACTION | NO ACTION |
| `wa_term_related_words.term_inv_id` | → | `wa_term_inventory.id` | NO ACTION | CASCADE |
| `wa_term_root_family.term_inv_id` | → | `wa_term_inventory.id` | NO ACTION | CASCADE |
| `wa_verse_records.book_id` | → | `books.id` | NO ACTION | NO ACTION |
| `wa_verse_records.term_inv_id` | → | `wa_term_inventory.id` | NO ACTION | RESTRICT |
| `wa_verse_records.file_id` | → | `wa_file_index.id` | NO ACTION | RESTRICT |
| `wa_verse_term_links.term_inv_id` | → | `wa_term_inventory.id` | NO ACTION | CASCADE |
| `wa_verse_term_links.verse_id` | → | `wa_verse_records.id` | NO ACTION | CASCADE |
| `word_run_state.run_id` | → | `engine_run_log.run_id` | NO ACTION | NO ACTION |

### FK Fan Metrics

**Fan-in (table receives N FK references):**

| table | incoming FKs |
| --- | --- |
| `word_registry` | 7 |
| `wa_term_inventory` | 7 |
| `mti_terms` | 6 |
| `wa_file_index` | 6 |
| `engine_run_log` | 3 |
| `books` | 2 |
| `phase2_flag_types` | 2 |
| `verse_context_group` | 2 |
| `wa_verse_records` | 2 |
| `wa_session_b_findings` | 2 |
| `wa_meaning_parsed` | 2 |
| `wa_crosslink_type` | 1 |
| `wa_quality_flag_types` | 1 |
| `wa_obs_question_catalogue` | 1 |

**Fan-out (table has N outgoing FKs to others):**

| table | outgoing FKs |
| --- | --- |
| `verse_context` | 3 |
| `wa_cross_registry_links` | 3 |
| `wa_session_research_flags` | 3 |
| `wa_verse_records` | 3 |
| `mti_term_cross_refs` | 2 |
| `mti_term_flags` | 2 |
| `mti_terms` | 2 |
| `wa_data_quality_flags` | 2 |
| `wa_dimension_index` | 2 |
| `wa_finding_catalogue_links` | 2 |
| `wa_term_phase2_flags` | 2 |
| `wa_verse_term_links` | 2 |
| `book_code_variants` | 1 |
| `engine_stream_checkpoint` | 1 |
| `term_fetch_log` | 1 |

### FK Utility Assessment Notes

- FKs on `file_id` columns across WA-family tables (`wa_term_inventory.file_id`, `wa_verse_records.file_id`, `wa_data_quality_flags.file_id`, etc.) add join complexity. The parent registry is reachable through alternative paths (via `word_registry.id`). Candidate for SIMPLIFICATION in the Change Plan (see A.3 candidate block below).
- `verse_context` has three FKs (`verse_record_id`, `group_id`, `mti_term_id`); `mti_term_id` may be derivable from `group_id` → `verse_context_group.mti_term_id`. Candidate for assessment.
- `wa_dimension_index` references both `verse_context_group_id` AND stores `mti_term_id`, `strongs_number`, `owning_registry_no`, `owning_registry_word`, `group_code` — multiple denormalised copies that could derive from FK. Candidate for CLEANUP.

---

## §A.4 — Index Inventory

**86 indexes** defined (auto + explicit).

- Auto-indexes (from PRIMARY KEY / UNIQUE): 25
- Explicit indexes (from CREATE INDEX): 61

### Explicit Indexes

| name | table | columns | unique | partial WHERE |
| --- | --- | --- | --- | --- |
| `uq_books_short_code` | `books` | short_code | YES |  |
| `idx_cross_refs_registry` | `mti_term_cross_refs` | registry, word |  |  |
| `idx_cross_refs_term_id` | `mti_term_cross_refs` | mti_term_id |  |  |
| `idx_mti_del` | `mti_terms` | delete_flagged |  |  |
| `idx_mti_status_del` | `mti_terms` | status, delete_flagged |  |  |
| `idx_mti_strongs_status` | `mti_terms` | strongs_number, status |  |  |
| `idx_mti_terms_reg_fk` | `mti_terms` | owning_registry_fk |  |  |
| `idx_mti_terms_registry` | `mti_terms` | owning_registry |  |  |
| `idx_mti_terms_status` | `mti_terms` | status |  |  |
| `idx_mti_terms_strongs` | `mti_terms` | strongs_number |  |  |
| `idx_mti_terms_word` | `mti_terms` | owning_word |  |  |
| `idx_vc_grp` | `verse_context` | group_id |  |  |
| `idx_vc_grp_anchor` | `verse_context` | group_id, is_anchor, delete_flagged |  |  |
| `idx_vc_mti` | `verse_context` | mti_term_id |  |  |
| `idx_vc_mti_del` | `verse_context` | mti_term_id, delete_flagged |  |  |
| `idx_vc_vr` | `verse_context` | verse_record_id |  |  |
| `idx_vcg_mti` | `verse_context_group` | mti_term_id |  |  |
| `idx_wa_xrl_file` | `wa_cross_registry_links` | file_id |  |  |
| `idx_wa_xrl_linked` | `wa_cross_registry_links` | linked_registry_id |  |  |
| `idx_wdqf_file` | `wa_data_quality_flags` | file_id |  |  |
| `idx_wdqf_flag` | `wa_data_quality_flags` | flag_id |  |  |
| `idx_dim_index_dimension` | `wa_dimension_index` | dimension |  |  |
| `idx_dim_index_group` | `wa_dimension_index` | verse_context_group_id |  |  |
| `idx_dim_index_mti` | `wa_dimension_index` | mti_term_id |  |  |
| `idx_dim_index_registry` | `wa_dimension_index` | owning_registry_no |  |  |
| `idx_wdi_conf` | `wa_dimension_index` | dimension_confidence |  |  |
| `idx_wdi_del` | `wa_dimension_index` | delete_flagged |  |  |
| `idx_wa_fi_reg` | `wa_file_index` | registry_id |  |  |
| `idx_wa_fi_word` | `wa_file_index` | word |  |  |
| `idx_wa_fi_wrfk` | `wa_file_index` | word_registry_fk |  |  |
| `idx_wfel_entity` | `wa_finding_entity_links` | entity_type, entity_id |  |  |
| `idx_wfel_finding_id` | `wa_finding_entity_links` | finding_id |  |  |
| `idx_lsj_parsed_term` | `wa_lsj_parsed` | term_inv_id |  |  |
| `idx_meaning_parsed_term_inv` | `wa_meaning_parsed` | term_inv_id |  |  |
| `idx_meaning_sense_level` | `wa_meaning_sense` | parsed_meaning_id, level_code |  |  |
| `idx_meaning_sense_parsed` | `wa_meaning_sense` | parsed_meaning_id |  |  |
| `idx_meaning_stem_parsed` | `wa_meaning_stem` | parsed_meaning_id |  |  |
| `idx_wsrf_registry` | `wa_session_research_flags` | registry_id |  |  |
| `idx_wsrf_resolved` | `wa_session_research_flags` | resolved |  |  |
| `idx_wa_ti_del` | `wa_term_inventory` | delete_flagged |  |  |
| `idx_wa_ti_file` | `wa_term_inventory` | file_id |  |  |
| `idx_wa_ti_id` | `wa_term_inventory` | term_id |  |  |
| `idx_wa_ti_lang` | `wa_term_inventory` | language |  |  |
| `idx_wa_ti_owner` | `wa_term_inventory` | term_owner_type, delete_flagged |  |  |
| `idx_wa_ti_strongs` | `wa_term_inventory` | strongs_number |  |  |
| `idx_wa_ti_strongs_owner` | `wa_term_inventory` | strongs_number, term_owner_type, delete_flagged |  |  |
| `idx_wa_rw` | `wa_term_related_words` | term_inv_id |  |  |
| `idx_wa_rf` | `wa_term_root_family` | term_inv_id |  |  |
| `idx_wa_vr_term` | `wa_verse_records` | term_inv_id |  |  |
| `idx_wavr_book_ch_v` | `wa_verse_records` | book_id, chapter, verse_num |  |  |
| `idx_wavr_del` | `wa_verse_records` | delete_flagged |  |  |
| `idx_wavr_file_term_pos` | `wa_verse_records` | file_id, term_id, book_id, chapter, verse_num |  |  |
| `idx_wavr_reference` | `wa_verse_records` | reference |  |  |
| `idx_wavr_term_del` | `wa_verse_records` | term_inv_id, delete_flagged |  |  |
| `idx_wavr_term_id` | `wa_verse_records` | term_id |  |  |
| `idx_vtl_term` | `wa_verse_term_links` | term_inv_id |  |  |
| `idx_vtl_verse` | `wa_verse_term_links` | verse_id |  |  |
| `idx_wr_cluster` | `word_registry` | cluster_assignment |  |  |
| `idx_wr_no` | `word_registry` | no |  |  |
| `idx_wr_sb_status` | `word_registry` | session_b_status |  |  |
| `idx_wr_vc_status` | `word_registry` | verse_context_status |  |  |

### Tables > 1000 rows without explicit indexes (3)

| table | rows |
| --- | --- |
| `engine_stream_checkpoint` | 1169 |
| `term_fetch_log` | 2317 |
| `wa_term_phase2_flags` | 1580 |

Candidate for INDEX_ADDITION in the Change Plan if common queries scan them.

---

## §A.5 — Constraint Inventory

- **NOT NULL constraints:** 141
- **CHECK constraints:** 1 (in 1 tables)
- **UNIQUE constraints (declared):** 22

### CHECK constraints per table

| table | CHECK count |
| --- | --- |
| `books` | 1 |

### Constraint Coverage Gaps

| table | column | gap |
| --- | --- | --- |
| `word_registry` | `session_b_status` | Controlled vocabulary per CLAUDE.md §17.1 — no CHECK |
| `word_registry` | `verse_context_status` | Controlled vocabulary per CLAUDE.md §17.2 — no CHECK |
| `word_registry` | `phase1_status` | Controlled vocabulary (Complete/Excluded/In Progress) — no CHECK |
| `word_registry` | `carry_forward` | Boolean 0/1 — no CHECK |
| `wa_term_inventory` | `term_owner_type` | Controlled 'OWNER'/'XREF' — no CHECK |
| `wa_term_inventory` | `language` | Controlled 'Hebrew'/'Greek' per CLAUDE.md §3 — no CHECK |
| `wa_term_inventory` | `evidential_status` | Controlled vocabulary per CLAUDE.md §17.4 — no CHECK |
| `wa_dimension_index` | `dimension_confidence` | Controlled vocabulary — no CHECK |

---

## §A.6 — Orphan Rows

For each registered FK, count rows whose parent does not exist.

| child | → parent | orphans |
| --- | --- | --- |
| `book_code_variants.book_id` | `books.id` | 0 |
| `engine_stream_checkpoint.run_id` | `engine_run_log.run_id` | 0 |
| `mti_term_cross_refs.registry_fk` | `word_registry.id` | 0 |
| `mti_term_cross_refs.mti_term_id` | `mti_terms.id` | 2 |
| `mti_term_flags.flag_id` | `phase2_flag_types.id` | 0 |
| `mti_term_flags.mti_term_id` | `mti_terms.id` | 0 |
| `mti_terms.word_data_ref_fk` | `wa_file_index.id` | 0 |
| `mti_terms.owning_registry_fk` | `word_registry.id` | 0 |
| `term_fetch_log.run_id` | `engine_run_log.run_id` | 0 |
| `verse_context.group_id` | `verse_context_group.id` | 0 |
| `verse_context.mti_term_id` | `mti_terms.id` | 0 |
| `verse_context.verse_record_id` | `wa_verse_records.id` | 0 |
| `verse_context_group.mti_term_id` | `mti_terms.id` | 0 |
| `wa_cross_registry_links.connection_type_id` | `wa_crosslink_type.id` | 0 |
| `wa_cross_registry_links.linked_registry_id` | `word_registry.id` | 0 |
| `wa_cross_registry_links.file_id` | `wa_file_index.id` | 0 |
| `wa_data_quality_flags.flag_id` | `wa_quality_flag_types.id` | 0 |
| `wa_data_quality_flags.file_id` | `wa_file_index.id` | 0 |
| `wa_dimension_index.mti_term_id` | `mti_terms.id` | 0 |
| `wa_dimension_index.verse_context_group_id` | `verse_context_group.id` | 0 |
| `wa_file_index.word_registry_fk` | `word_registry.id` | 0 |
| `wa_finding_catalogue_links.question_id` | `wa_obs_question_catalogue.obs_id` | 0 |
| `wa_finding_catalogue_links.finding_id` | `wa_session_b_findings.id` | 0 |
| `wa_finding_entity_links.finding_id` | `wa_session_b_findings.id` | 0 |
| `wa_lsj_parsed.term_inv_id` | `wa_term_inventory.id` | 0 |
| `wa_meaning_parsed.term_inv_id` | `wa_term_inventory.id` | 0 |
| `wa_meaning_sense.parsed_meaning_id` | `wa_meaning_parsed.id` | 25 |
| `wa_meaning_stem.parsed_meaning_id` | `wa_meaning_parsed.id` | 0 |
| `wa_obs_question_catalogue.source_registry_no` | `word_registry.id` | 0 |
| `wa_session_b_findings.term_id` | `mti_terms.id` | 0 |
| `wa_session_research_flags.cross_registry_id` | `word_registry.id` | 0 |
| `wa_session_research_flags.file_id` | `wa_file_index.id` | 0 |
| `wa_session_research_flags.registry_id` | `word_registry.id` | 0 |
| `wa_term_inventory.file_id` | `wa_file_index.id` | 0 |
| `wa_term_phase2_flags.flag_id` | `phase2_flag_types.id` | 0 |
| `wa_term_phase2_flags.term_inv_id` | `wa_term_inventory.id` | 10 |
| `wa_term_related_words.term_inv_id` | `wa_term_inventory.id` | 0 |
| `wa_term_root_family.term_inv_id` | `wa_term_inventory.id` | 0 |
| `wa_verse_records.book_id` | `books.id` | 0 |
| `wa_verse_records.term_inv_id` | `wa_term_inventory.id` | 0 |
| `wa_verse_records.file_id` | `wa_file_index.id` | 0 |
| `wa_verse_term_links.term_inv_id` | `wa_term_inventory.id` | 0 |
| `wa_verse_term_links.verse_id` | `wa_verse_records.id` | 0 |
| `word_run_state.run_id` | `engine_run_log.run_id` | 0 |

**3 FK(s) with orphans — BROKEN_INVARIANT.**

- `mti_term_cross_refs.mti_term_id` → `mti_terms.id`: **2** orphans
- `wa_meaning_sense.parsed_meaning_id` → `wa_meaning_parsed.id`: **25** orphans
- `wa_term_phase2_flags.term_inv_id` → `wa_term_inventory.id`: **10** orphans

### Soft-delete cascade check

Rows where a parent is `delete_flagged = 1` but child is `delete_flagged = 0` — cascade inconsistency.

| parent | parent flag | child | relationship | cascade inconsistencies |
| --- | --- | --- | --- | --- |
| `wa_term_inventory` | `delete_flagged` | `wa_verse_records` | `.term_inv_id = parent.id` | 6 |
| `wa_file_index` | `delete_flagged` | `wa_term_inventory` | `.file_id = parent.id` | error: no such column: p.delete_flagged |
| `mti_terms` | `status` | `verse_context_group` | `.mti_term_id = parent.id` | 7 |

---

## §A.7 — Type Inconsistencies

### Date/timestamp columns — format check

Columns looking like date/time (TEXT type): 29

Spot-check (first 3 non-NULL values each):

| table.column | sample values |
| --- | --- |
| `engine_run_log.started_at` | 2026-03-18T10:57:05 · 2026-03-18T13:41:33 · 2026-03-18T13:43:56 |
| `engine_run_log.completed_at` | 2026-03-18T10:57:40 · 2026-03-18T13:41:49 · 2026-03-18T13:43:56 |
| `engine_stream_checkpoint.started_at` | 2026-03-18T10:57:05 · 2026-03-18T13:41:33 · 2026-03-18T13:45:19 |
| `engine_stream_checkpoint.completed_at` | 2026-03-18T10:57:40 · 2026-03-18T13:41:49 · 2026-03-18T13:53:16 |
| `mti_terms.extraction_date` | 2026-03-28 · 2026-03-12 · 2026-03-15 |
| `schema_version.applied_at` | 2026-04-16 05:17:38 · 2026-03-29T12:52:09Z · 2026-03-29T12:54:48Z |
| `session_d_observations.raised_date` |  |
| `session_d_runs.run_date` |  |
| `session_d_term_links.raised_date` |  |
| `session_d_verse_links.raised_date` |  |
| `term_fetch_log.fetched_at` | 2026-03-18T13:41:33 · 2026-03-18T13:41:34 · 2026-03-18T13:41:35 |
| `wa_dim_review_cluster_log.completed_date` | 2026-04-09 · 2026-04-11 · 2026-04-13 |
| `wa_file_index.produced_date` | 2026-03-07 · 2026-03-08 · 2026-03-12 |
| `wa_finding_catalogue_links.mapped_date` |  |
| `wa_finding_catalogue_links.validated_date` |  |
| `wa_finding_entity_links.raised_date` |  |
| `wa_lsj_parsed.parsed_at` | 2026-03-18T15:12:36 · 2026-03-19T17:05:06 |
| `wa_meaning_parsed.parsed_at` | 2026-03-18T14:05:50 · 2026-03-18T14:05:51 · 2026-03-18T14:05:53 |
| `wa_obs_question_catalogue.date_added` | 20260416 |
| `wa_session_b_dimensions.raised_date` | 2026-03-27 · 2026-03-28 |
| `wa_session_b_findings.raised_date` | 2026-03-27 · 2026-03-28 · 2026-04-06 |
| `wa_session_b_findings.obsolete_date` |  |
| `wa_session_research_flags.raised_date` | 2026-03-24 · 2026-03-25 · 2026-03-26 |
| `wa_session_research_flags.resolved_date` |  |
| `wa_term_phase2_flags.raised_date` | 2026-03-19T18:18:06Z · 2026-04-11 |
| `wa_verse_records.created_at` | 2026-03-16T12:41:52 · 2026-03-23T14:08:04 · 2026-03-23T20:22:00 |
| `wa_verse_records.updated_at` | 2026-03-28T22:13:19 · 2026-03-28T22:14:06 · 2026-04-06T18:26:33 |
| `wa_verse_term_links.created_at` | 2026-03-23T14:08:04 · 2026-03-23T20:22:00 · 2026-03-24T07:03:16 |
| `word_run_state.approved_at` |  |

### `schema_version` specific findings

| id | version_code | applied_at |
| --- | --- | --- |
| 1 | 3.9.0 | 2026-04-16 05:17:38 |
| 2 | 3.7.1 | 2026-03-29T12:52:09Z |
| 3 | 3.8.0 | 2026-03-29T12:54:48Z |

- **Finding:** `id` does NOT reflect application order. Row id=1 has the newest version (3.9.0), id=3 has older (3.8.0). Likely caused by re-insertion or data restore; schema does not protect against.
- **Finding:** date format inconsistency — 2 rows use `T`-separator ISO-8601 with `Z` suffix; 1 row uses space-separator local time. Normalise to a single format.

### Lock sentinel casing

- `engine/constants.py::LOCK_SENTINEL = 'IN_PROGRESS'` (uppercase with underscore)
- `word_registry.phase1_status` actual values include `'In Progress'` (title case with space)
- **One of the two is wrong.** Either the constant never matched (dead code for that check) or the value was stored with wrong casing.

### Boolean column value check (0/1 standard)

| table.column | distinct values |
| --- | --- |
| `word_registry.carry_forward` | 1 |
| `wa_term_inventory.delete_flagged` | 0, 1 |
| `wa_term_inventory.god_as_subject` | 1, 0 |
| `wa_term_inventory.somatic_link` | 0, 1 |
| `wa_verse_records.delete_flagged` | 0, 1 |
| `verse_context.is_anchor` | 0, 1 |
| `verse_context.is_related` | 0, 1 |
| `verse_context.is_relevant` | 1, 0 |
| `wa_session_b_findings.delete_flag` | 0 |
| `wa_session_research_flags.resolved` | 0 |

### Strong's number prefix casing

| prefix | count |
| --- | --- |
| `G` | 2270 |
| `H` | 5297 |
| `P` | 4 |

---

## §A.8 — Redundant Column Confirmation

Known candidates from CLAUDE.md §17.6, confirmed against live usage metrics.

| table | column | total rows | non-NULL | distinct | code refs | recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| `mti_terms` | `status_note` | 7571 | 1504 | 785 | 0 | REVIEW |
| `wa_term_inventory` | `god_as_subject` | 7550 | 7550 | 2 | 0 | REVIEW |
| `wa_term_inventory` | `somatic_link` | 7550 | 7550 | 2 | 0 | REVIEW |
| `wa_term_inventory` | `status_note` | 7550 | 177 | 142 | 0 | DROP |
| `word_registry` | `inference_note` | 214 | 24 | 21 | 0 | REVIEW |

### Cross-check: `somatic_link` vs `mti_term_flags`

cross-check error: no such column: mf.id

### Cross-check: `god_as_subject` vs `mti_term_flags`

- `wa_term_inventory.god_as_subject = 1`: 220 rows

### Cross-check: `status_note` columns

- `wa_term_inventory.status_note IS NOT NULL`: 177
- `mti_terms.status_note IS NOT NULL`: 1504

### Cross-check: `word_registry.inference_note`

- `word_registry.inference_note IS NOT NULL`: 24

---

## §Summary

### Tag distribution of findings

| Tag | Count | Disposition |
| --- | --- | --- |
| INFORMATIONAL | (various — see body) | No action required |
| CLEANUP_CANDIDATE | 25 null-only + 419 zero-ref + 5 known redundant | Review for drop |
| BROKEN_INVARIANT | 3 orphan FK(s) (if any) | Must be resolved before FK additions |
| RISK | Schema-version id ordering; date format inconsistency; lock-sentinel casing | To remediate in Phase B bundles |

### Candidate Change Plan bundles (preview — to be formalised in Phase B)

1. **Redundant column removal — Terms** — DROP `wa_term_inventory.god_as_subject`, `somatic_link`, `status_note`; DROP `mti_terms.status_note` pending research flag assessment.
2. **Redundant column removal — Registry** — DROP `word_registry.inference_note` pending researcher confirmation of zero non-NULL rows.
3. **New registry field** — ADD `word_registry.word_synopsis TEXT` (per Session A advice Q7).
4. **Prose store setup** — M_P1–M_P6 per prose store design: `prose_section_type`, `prose_section`, FTS5, link tables, seed.
5. **Type normalisation — schema_version** — rebuild with surrogate key matching application order; normalise date format to T-separator UTC.
6. **Type normalisation — lock sentinel** — decide: update `engine/constants.py::LOCK_SENTINEL` to match data (`'In Progress'`), or UPDATE data to match constant. Requires researcher decision (RD item).
7. **Dimension index simplification** — review `wa_dimension_index` denormalised copies; retain only `verse_context_group_id`; others derivable.
8. **FK graph simplification** — review redundant `file_id` FKs across WA-family tables where registry is reachable via term.
9. **Constraint coverage** — add CHECK constraints on 8+ controlled-vocabulary columns (§A.5 gap list).
10. **Index optimisation** — review list of large tables without explicit indexes.

### Open items to raise as RD at Phase B kick-off

- **RD candidate:** Lock sentinel casing — `'IN_PROGRESS'` (constant) vs `'In Progress'` (data). Which is canonical?
- **RD candidate:** schema_version table — rebuild or leave historical rows as-is and only normalise going forward?

---

## G1 Approval Block

Status: [X] APPROVED — PROCEED to Phase B  [ ] REVISIONS REQUESTED — see markup

Date: 2026-04-19

Reviewer: le Roux Cilliers

Notes: Looks good — not as bad as expected, but definite room for improvements. Proceed with Phase B to investigate further and plan migrations.

---

*End of Phase A audit report — 2026-04-19*