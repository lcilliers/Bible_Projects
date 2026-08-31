# Schema overview

> Generated 2026-08-31T13:04:16Z by `report.schema_overview`. Introspects the live DB directly — always current, never hand-maintained.

- data tables: **41** known, **41** live

## Contents

- [Table inventory](#table-inventory)
- [Every data table, in full](#every-data-table-in-full)

<a id="table-inventory"></a>
## Table inventory

| table | rows (live) | status |
| --- | --- | --- |
| candidate_seed | 1806 |  |
| escalation | 637 |  |
| lemma_inventory | 11781 |  |
| passage | 42 | **RETIRED** |
| run | 2357 |  |
| span | 378149 |  |
| span_candidate | 83914 |  |
| strong | 15293 |  |
| strong_lexicon | 5639 |  |
| strong_lsj_parsed | 36199 |  |
| strong_meaning_parsed | 47113 |  |
| strong_meaning_tree | 40315 |  |
| strong_mounce_parsed | 5742 |  |
| strong_related | 87535 |  |
| strong_sense | 15293 |  |
| strong_verse | 132718 |  |
| validation_result | 39457 |  |
| verse | 29759 |  |
| verse_passage | 777 | **RETIRED** |
| word_registry | 180 |  |
| word_strong | 4874 |  |
| cluster | 51 |  |
| cluster_strong | 7391 |  |
| content_index | 0 |  |
| content_index_scan | 0 |  |
| debate_change_detail | 242 |  |
| escalation_history | 2313 |  |
| escalations_old | 723 |  |
| file_manifest | 16197 |  |
| folder_purpose | 959 |  |
| hib | 21 |  |
| hib_referent_option | 0 |  |
| operation | 121 |  |
| operation_party | 136 |  |
| passage_emergent_question | 3 |  |
| passage_insufficiency | 1 |  |
| passage_linkage | 3 |  |
| passage_validation_note | 4 |  |
| phenomenon | 121 |  |
| verse_hib | 235 |  |
| verse_lexical | 552353 |  |

**Retired** (2) — soft-deleted at the data level, kept for the historical record, not part of the live system: `passage` (see `reports/archive/passage-system-retirement-record-20260726.md`); `verse_passage` (see `reports/archive/passage-system-retirement-record-20260726.md`)

<a id="every-data-table-in-full"></a>
## Every data table, in full

### candidate_seed (1806 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| lemma_key | TEXT |  | ✓ | lemma_inventory.lemma_key |
| decision | TEXT |  |  |  |
| layer | TEXT |  |  |  |
| registry_match | TEXT |  |  |  |
| tag | TEXT |  |  |  |
| strong_variant | TEXT |  | ✓ |  |
| sense_seq | INTEGER |  | ✓ |  |
| step_status | TEXT |  |  |  |
| ib_referent_type | TEXT |  |  |  |
| assessed_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_candidate_seed_live_unique, idx_candidate_seed_strong_variant, idx_candidate_seed_lemma_key, sqlite_autoindex_candidate_seed_1

### escalation (637 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| version | INTEGER |  | ✓ |  |
| run_id | TEXT |  |  |  |
| source | TEXT |  | ✓ |  |
| at_step | TEXT |  |  |  |
| type | TEXT |  | ✓ |  |
| short_description | TEXT |  | ✓ |  |
| context | TEXT |  |  |  |
| comment | TEXT |  |  |  |
| tried | TEXT |  |  |  |
| state | TEXT |  | ✓ |  |
| next_action | TEXT |  |  |  |
| next_action_assigned_to | TEXT |  |  |  |
| originator | TEXT |  |  |  |
| resolution | TEXT |  |  |  |
| raised_at | TEXT |  | ✓ |  |
| answered_at | TEXT |  |  |  |
| resolution_kind | TEXT |  |  |  |
| needs_claude_followup | INTEGER |  | ✓ |  |

### lemma_inventory (11781 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| lemma_key | TEXT |  | ✓ |  |
| gloss | TEXT |  |  |  |
| language | TEXT |  |  |  |
| source | TEXT |  |  |  |
| created_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_lemma_inventory_live_unique, sqlite_autoindex_lemma_inventory_1

### passage (42 row(s) — RETIRED, see note above)

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| book | TEXT |  | ✓ |  |
| anchor_verse_id | INTEGER |  | ✓ | verse.id |
| start_chapter | INTEGER |  |  |  |
| start_verse | INTEGER |  |  |  |
| end_chapter | INTEGER |  |  |  |
| end_verse | INTEGER |  |  |  |
| ref | TEXT |  |  |  |
| verse_count | INTEGER |  |  |  |
| rule | TEXT |  |  |  |
| source | TEXT |  |  |  |
| needs_review | INTEGER |  |  |  |
| created_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
| book_label | TEXT |  |  |  |
| verse_span_meaning_path | TEXT |  |  |  |
| verse_span_meaning_written_at | TEXT |  |  |  |
| debate_path | TEXT |  |  |  |
| debate_written_at | TEXT |  |  |  |
| debate_status | TEXT |  |  |  |
| phenomena_complete_at | TEXT |  |  |  |
| open_decisions_note | TEXT |  |  |  |
| story_summary | TEXT |  |  |  |
| feasibility_note | TEXT |  |  |  |
indexes: idx_passage_live_unique, idx_passage_anchor_verse_id, idx_passage_range_live

### run (2357 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| run_id | TEXT |  | ✓ |  |
| work_package | TEXT |  |  |  |
| params | TEXT |  |  |  |
| runs_over | TEXT |  |  |  |
| config_version | TEXT |  |  |  |
| state | TEXT |  |  |  |
| resume_point | TEXT |  |  |  |
| started_at | TEXT |  |  |  |
| ended_at | TEXT |  |  |  |
| outcome | TEXT |  |  |  |
indexes: sqlite_autoindex_run_1

### span (378149 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| verse_id | INTEGER |  | ✓ | verse.id |
| position | INTEGER |  | ✓ |  |
| surface | TEXT |  |  |  |
| strong_variant | TEXT |  |  | strong.strongNumber |
| morph_code | TEXT |  |  |  |
| is_particle | INTEGER |  |  |  |
| built_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_span_live_unique, idx_span_verse_id, sqlite_autoindex_span_1

### span_candidate (83914 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| span_id | INTEGER |  | ✓ | span.id |
| lemma_key | TEXT |  |  |  |
| candidate_tag | TEXT |  |  |  |
| seed_source | TEXT |  |  |  |
| set_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_span_candidate_live_unique, idx_span_candidate_span_id, sqlite_autoindex_span_candidate_1

### strong (15293 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| strongNumber | TEXT | ✓ |  |  |
| accentedUnicode | TEXT |  |  |  |
| stepGloss | TEXT |  |  |  |
| stepTransliteration | TEXT |  |  |  |
| language | TEXT |  |  |  |
| count | INTEGER |  |  |  |
| freqList | TEXT |  |  |  |
| created_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
| origin | TEXT |  | ✓ |  |
indexes: sqlite_autoindex_strong_1

### strong_lexicon (5639 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  | strong.strongNumber |
| lsj | TEXT |  |  |  |
| mounce | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_strong_lexicon_strong, sqlite_autoindex_strong_lexicon_1

### strong_lsj_parsed (36199 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| strong | TEXT |  | ✓ | strong.strongNumber |
| sense_label | TEXT |  |  |  |
| gloss | TEXT |  |  |  |
| note | TEXT |  |  |  |
| row_type | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_strong_lsj_parsed_strong

### strong_meaning_parsed (47113 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| lemma_key | TEXT |  | ✓ |  |
| sort | INTEGER |  |  |  |
| sense_code | TEXT |  |  |  |
| gloss | TEXT |  |  |  |
| verse_refs | TEXT |  |  |  |
| note | TEXT |  |  |  |
| row_type | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
| strong_variant | TEXT |  |  | strong.strongNumber |
indexes: idx_strong_meaning_parsed_strong_variant

### strong_meaning_tree (40315 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| lemma_key | TEXT |  | ✓ |  |
| sense_code | TEXT |  |  |  |
| sense_text | TEXT |  |  |  |
| sort | INTEGER |  |  |  |
| deleted | INTEGER |  |  |  |
| strong_variant | TEXT |  |  | strong.strongNumber |
indexes: idx_strong_meaning_tree_strong_variant

### strong_mounce_parsed (5742 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| strong | TEXT |  | ✓ | strong.strongNumber |
| mounce_parsed | TEXT |  |  |  |
| row_type | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_strong_mounce_parsed_strong

### strong_related (87535 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| strong | TEXT |  | ✓ | strong.strongNumber |
| related_strong | TEXT |  | ✓ |  |
| related_form | TEXT |  |  |  |
| related_transliteration | TEXT |  |  |  |
| related_gloss | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_strong_related_strong

### strong_sense (15293 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  | strong.strongNumber |
| head | TEXT |  |  |  |
| is_own_lemma | INTEGER |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_strong_sense_strong, sqlite_autoindex_strong_sense_1

### strong_verse (132718 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| strong | TEXT |  | ✓ | strong.strongNumber |
| verse_id | INTEGER |  | ✓ | verse.id |
| deleted | INTEGER |  |  |  |
indexes: idx_strong_verse_live_unique, idx_strong_verse_verse_id, idx_strong_verse_strong, sqlite_autoindex_strong_verse_1

### validation_result (39457 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| run_id | TEXT |  | ✓ | run.run_id |
| word | TEXT |  |  |  |
| step | TEXT |  |  |  |
| check_name | TEXT |  |  |  |
| result | TEXT |  |  |  |
| detail | TEXT |  |  |  |
| ran_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_validation_result_run_id

### verse (29759 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| osisId | TEXT |  | ✓ |  |
| reference | TEXT |  |  |  |
| preview | TEXT |  |  |  |
| step_version | TEXT |  |  |  |
| created_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
| text | TEXT |  |  |  |
indexes: idx_verse_live_unique, sqlite_autoindex_verse_1

### verse_passage (777 row(s) — RETIRED, see note above)

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| passage_id | INTEGER |  | ✓ | passage.id |
| verse_id | INTEGER |  | ✓ | verse.id |
| is_anchor | INTEGER |  |  |  |
| created_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_verse_passage_live_unique, idx_verse_passage_verse_id, idx_verse_passage_passage_id, idx_verse_passage_verse_id_live

### word_registry (180 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| word | TEXT |  | ✓ |  |
| source | TEXT |  |  |  |
| status | TEXT |  |  |  |
| created_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_word_registry_live_unique, sqlite_autoindex_word_registry_1

### word_strong (4874 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| word_id | INTEGER |  | ✓ | word_registry.id |
| strong | TEXT |  | ✓ | strong.strongNumber |
| deleted | INTEGER |  |  |  |
indexes: idx_word_strong_live_unique, idx_word_strong_word_id, idx_word_strong_strong, sqlite_autoindex_word_strong_1

### cluster (51 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| cluster_code | TEXT | ✓ |  |  |
| short_name | TEXT |  |  |  |
| description | TEXT |  |  |  |
| gloss | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: sqlite_autoindex_cluster_1

### cluster_strong (7391 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| strong | TEXT |  | ✓ | strong.strongNumber |
| cluster_code | TEXT |  | ✓ | cluster.cluster_code |
| source | TEXT |  | ✓ |  |
| created_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
| confidence | TEXT |  |  |  |
| operation | INTEGER |  |  |  |
| alt_clusters | TEXT |  |  |  |
| review_flag | INTEGER |  |  |  |
| rationale | TEXT |  |  |  |

### content_index (0 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| key_type | TEXT | ✓ | ✓ |  |
| key_value | TEXT | ✓ | ✓ |  |
| file_path | TEXT | ✓ | ✓ |  |
| line_number | INTEGER | ✓ | ✓ |  |
| snippet | TEXT |  | ✓ |  |
| indexed_at | TEXT |  | ✓ |  |
indexes: ix_content_index_file, ix_content_index_key, sqlite_autoindex_content_index_1

### content_index_scan (0 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| file_path | TEXT | ✓ |  |  |
| mtime | TEXT |  | ✓ |  |
| scanned_at | TEXT |  | ✓ |  |
indexes: sqlite_autoindex_content_index_scan_1

### debate_change_detail (242 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| run_id | TEXT |  | ✓ | run.run_id |
| table_name | TEXT |  | ✓ |  |
| op | TEXT |  | ✓ |  |
| where_json | TEXT |  |  |  |
| set_json | TEXT |  |  |  |
| before_json | TEXT |  |  |  |
| applied_at | TEXT |  | ✓ |  |
| writer | TEXT |  | ✓ |  |
indexes: idx_hib_change_detail_run_id

### escalation_history (2313 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| escalation_id | INTEGER |  | ✓ | escalation.id |
| version | INTEGER |  | ✓ |  |
| run_id | TEXT |  |  |  |
| source | TEXT |  |  |  |
| at_step | TEXT |  |  |  |
| type | TEXT |  |  |  |
| short_description | TEXT |  |  |  |
| context | TEXT |  |  |  |
| comment | TEXT |  |  |  |
| tried | TEXT |  |  |  |
| state | TEXT |  | ✓ |  |
| next_action | TEXT |  |  |  |
| next_action_assigned_to | TEXT |  |  |  |
| originator | TEXT |  |  |  |
| resolution | TEXT |  |  |  |
| raised_at | TEXT |  |  |  |
| answered_at | TEXT |  | ✓ |  |
| resolution_kind | TEXT |  |  |  |
| needs_claude_followup | INTEGER |  | ✓ |  |
indexes: idx_escalation_history_escalation_id, sqlite_autoindex_escalation_history_1

### escalations_old (723 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| run_id | TEXT |  | ✓ | run.run_id |
| source | TEXT |  | ✓ |  |
| at_step | TEXT |  |  |  |
| type | TEXT |  |  |  |
| short_description | TEXT |  |  |  |
| context | TEXT |  |  |  |
| tried | TEXT |  |  |  |
| state | TEXT |  |  |  |
| next_action | TEXT |  |  |  |
| answered_at | TEXT |  |  |  |
| raised_at | TEXT |  |  |  |
| comment | TEXT |  |  |  |
| resolution | TEXT |  |  |  |
| related_activity | TEXT |  |  |  |
| next_action_assigned_to | TEXT |  |  |  |
| answered_by | TEXT |  |  |  |
indexes: idx_escalation_run_id

### file_manifest (16197 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| path | TEXT | ✓ |  |  |
| category | TEXT |  | ✓ |  |
| file_type | TEXT |  | ✓ |  |
| currency | TEXT |  | ✓ |  |
| archived | INTEGER |  | ✓ |  |
| registry | INTEGER |  |  |  |
| word | TEXT |  |  |  |
| cluster | TEXT |  |  |  |
| vcb_batch | INTEGER |  |  |  |
| version | TEXT |  |  |  |
| date | TEXT |  |  |  |
| ext | TEXT |  |  |  |
| size_bytes | INTEGER |  | ✓ |  |
| modified_at | TEXT |  | ✓ |  |
| scanned_at | TEXT |  | ✓ |  |
indexes: ix_file_manifest_registry, ix_file_manifest_currency, ix_file_manifest_category, sqlite_autoindex_file_manifest_1

### folder_purpose (959 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| folder_path | TEXT | ✓ |  |  |
| top_level_root | TEXT |  | ✓ |  |
| depth | INTEGER |  | ✓ |  |
| parent_path | TEXT |  | ✓ |  |
| direct_file_count | INTEGER |  | ✓ |  |
| recursive_file_count | INTEGER |  | ✓ |  |
| direct_subfolder_count | INTEGER |  | ✓ |  |
| top_ext_direct | TEXT |  |  |  |
| last_modified_direct | TEXT |  |  |  |
| governed_by_setting | TEXT |  |  |  |
| manifest_category | TEXT |  |  |  |
| manifest_currency | TEXT |  |  |  |
| type | TEXT |  |  |  |
| status | TEXT |  |  |  |
| usage_description | TEXT |  |  |  |
| added_at | TEXT |  | ✓ |  |
| last_reviewed_at | TEXT |  |  |  |
indexes: ix_folder_purpose_type, ix_folder_purpose_status, ix_folder_purpose_top_level_root, sqlite_autoindex_folder_purpose_1

### hib (21 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| book | TEXT |  | ✓ |  |
| label | TEXT |  | ✓ |  |
| kind | TEXT |  | ✓ |  |
| first_verse_id | INTEGER |  |  | verse.id |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_hib_first_verse_id

### hib_referent_option (0 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| hib_id | INTEGER |  | ✓ | hib.id |
| reading_text | TEXT |  | ✓ |  |
| textual_grounds | TEXT |  |  |  |
| adopted | INTEGER |  | ✓ |  |
| ordinal | INTEGER |  | ✓ |  |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_hib_referent_option_hib_id

### operation (121 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| phenomenon_id | INTEGER |  | ✓ | phenomenon.id |
| process | TEXT |  |  |  |
| action_type | TEXT |  |  |  |
| decision | TEXT |  |  |  |
| observation_text | TEXT |  |  |  |
| description_text | TEXT |  |  |  |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_operation_phenomenon_id

### operation_party (136 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| operation_id | INTEGER |  | ✓ | operation.id |
| role | TEXT |  | ✓ |  |
| kind | TEXT |  | ✓ |  |
| detail | TEXT |  |  |  |
| enablement_only | INTEGER |  | ✓ |  |
| ordinal | INTEGER |  | ✓ |  |
| created_at | TEXT |  | ✓ |  |
| hib_id | INTEGER |  |  | hib.id |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_operation_party_operation_id, idx_operation_party_hib_id

### passage_emergent_question (3 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| passage_id | INTEGER |  | ✓ | passage.id |
| verse_id | INTEGER |  |  | verse.id |
| question_text | TEXT |  | ✓ |  |
| kind | TEXT |  | ✓ |  |
| ordinal | INTEGER |  | ✓ |  |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_passage_emergent_question_verse_id, idx_passage_emergent_question_passage_id, idx_passage_emergent_question_live_unique

### passage_insufficiency (1 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| passage_id | INTEGER |  | ✓ | passage.id |
| verse_id | INTEGER |  |  | verse.id |
| note | TEXT |  | ✓ |  |
| ordinal | INTEGER |  | ✓ |  |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_passage_insufficiency_verse_id, idx_passage_insufficiency_passage_id, idx_passage_insufficiency_live_unique

### passage_linkage (3 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| passage_id | INTEGER |  | ✓ | passage.id |
| from_operation_id | INTEGER |  | ✓ | operation.id |
| to_operation_id | INTEGER |  | ✓ | operation.id |
| note | TEXT |  | ✓ |  |
| ordinal | INTEGER |  | ✓ |  |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_passage_linkage_to_operation_id, idx_passage_linkage_passage_id, idx_passage_linkage_from_operation_id, idx_passage_linkage_live_unique

### passage_validation_note (4 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| passage_id | INTEGER |  | ✓ | passage.id |
| phenomenon_id | INTEGER |  |  | phenomenon.id |
| finding_text | TEXT |  | ✓ |  |
| corrected | INTEGER |  | ✓ |  |
| ordinal | INTEGER |  | ✓ |  |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_passage_validation_note_phenomenon_id, idx_passage_validation_note_passage_id, idx_passage_validation_note_live_unique

### phenomenon (121 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| passage_id | INTEGER |  | ✓ | passage.id |
| verse_id | INTEGER |  | ✓ | verse.id |
| hib_id | INTEGER |  | ✓ | hib.id |
| description | TEXT |  | ✓ |  |
| textual_warrant | TEXT |  |  |  |
| status | TEXT |  | ✓ |  |
| ordinal | INTEGER |  | ✓ |  |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_phenomenon_verse_id, idx_phenomenon_passage_id, idx_phenomenon_hib_id, idx_phenomenon_live_unique

### verse_hib (235 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| verse_id | INTEGER |  | ✓ | verse.id |
| hib_id | INTEGER |  | ✓ | hib.id |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_verse_hib_verse_id, idx_verse_hib_hib_id, idx_verse_hib_live_unique

### verse_lexical (552353 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ | ✓ |  |
| span_id | INTEGER |  | ✓ | span.id |
| verse_id | INTEGER |  | ✓ | verse.id |
| code_ordinal | INTEGER |  | ✓ |  |
| strong | TEXT |  |  | strong.strongNumber |
| morph_code | TEXT |  |  |  |
| role | TEXT |  | ✓ |  |
| status | TEXT |  | ✓ |  |
| resolved_sense | TEXT |  |  |  |
| ambiguity_note | TEXT |  |  |  |
| created_at | TEXT |  | ✓ |  |
| deleted | INTEGER |  | ✓ |  |
indexes: idx_verse_lexical_verse_id, idx_verse_lexical_strong, idx_verse_lexical_span_id, idx_verse_lexical_live_unique
