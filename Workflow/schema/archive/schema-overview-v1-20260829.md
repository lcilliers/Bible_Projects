# Schema overview

> Generated 2026-08-29T13:19:51Z by `report.schema_overview`. Introspects the live DB directly — always current, never hand-maintained.

- data tables: **21** known, **41** live

## Contents

- [Table inventory](#table-inventory)
- [Every data table, in full](#every-data-table-in-full)

<a id="table-inventory"></a>
## Table inventory

| table | rows (live) | status |
| --- | --- | --- |
| candidate_seed | 1806 |  |
| escalation | 328 |  |
| lemma_inventory | 11781 |  |
| passage | 42 | **RETIRED** |
| run | 2106 |  |
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
| validation_result | 39165 |  |
| verse | 29759 |  |
| verse_passage | 777 | **RETIRED** |
| word_registry | 180 |  |
| word_strong | 4874 |  |

**Retired** (2) — soft-deleted at the data level, kept for the historical record, not part of the live system: `passage` (see `reports/archive/passage-system-retirement-record-20260726.md`); `verse_passage` (see `reports/archive/passage-system-retirement-record-20260726.md`)

**Live but not in `DATA_TABLES`** (a new table — add it to `schemareport.DATA_TABLES` deliberately): cluster, cluster_strong, content_index, content_index_scan, debate_change_detail, escalation_history, escalations_old, file_manifest, folder_purpose, hib, hib_referent_option, operation, operation_party, passage_emergent_question, passage_insufficiency, passage_linkage, passage_validation_note, phenomenon, verse_hib, verse_lexical

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

### escalation (328 row(s))

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

### run (2106 row(s))

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

### validation_result (39165 row(s))

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
