# IBA DB Schema Overview

- Database: C:\Bible_study_projects\iba\app\db\iba.db
- Generated (UTC): 2026-07-19T03:35:46Z
- Tables: 33
- Views: 0
- Triggers: 0
- Indexes: 28

## Tables

### candidate_seed

- Columns: 8
- Primary key: id
- Foreign keys: 1
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| lemma_key | TEXT | 1 |  | 0 |
| decision | TEXT | 0 |  | 0 |
| layer | TEXT | 0 |  | 0 |
| registry_match | TEXT | 0 |  | 0 |
| tag | TEXT | 0 |  | 0 |
| assessed_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| lemma_key | lemma_inventory | lemma_key | NO ACTION | NO ACTION | NONE |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_candidate_seed_1 | 1 | u | 0 | lemma_key |

### cfg_api

- Columns: 4
- Primary key: name
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| name | TEXT | 0 |  | 1 |
| route | TEXT | 0 |  | 0 |
| input | TEXT | 0 |  | 0 |
| returns | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_api_1 | 1 | pk | 0 | name |

### cfg_book_order

- Columns: 2
- Primary key: book
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| book | TEXT | 0 |  | 1 |
| ordinal | INTEGER | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_book_order_1 | 1 | pk | 0 | book |

### cfg_candidate_rule

- Columns: 2
- Primary key: kind, value
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| kind | TEXT | 0 |  | 1 |
| value | TEXT | 0 |  | 2 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_candidate_rule_1 | 1 | pk | 0 | kind, value |

### cfg_change_log

- Columns: 5
- Primary key: id
- Foreign keys: 0
- Indexes: 0

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| config_version | TEXT | 0 |  | 0 |
| seed_hash | TEXT | 0 |  | 0 |
| loaded_at | TEXT | 0 |  | 0 |
| validated | INTEGER | 0 |  | 0 |

### cfg_column

- Columns: 13
- Primary key: table_name, name
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| table_name | TEXT | 0 |  | 1 |
| name | TEXT | 0 |  | 2 |
| ordinal | INTEGER | 0 |  | 0 |
| type | TEXT | 0 |  | 0 |
| is_pk | INTEGER | 0 |  | 0 |
| notnull | INTEGER | 0 |  | 0 |
| is_unique | INTEGER | 0 |  | 0 |
| dflt | TEXT | 0 |  | 0 |
| fk | TEXT | 0 |  | 0 |
| use | TEXT | 0 |  | 0 |
| expectation | TEXT | 0 |  | 0 |
| source | TEXT | 0 |  | 0 |
| filled_by | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_column_1 | 1 | pk | 0 | table_name, name |

### cfg_connection

- Columns: 2
- Primary key: key
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| key | TEXT | 0 |  | 1 |
| value | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_connection_1 | 1 | pk | 0 | key |

### cfg_enum

- Columns: 3
- Primary key: name, value
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| name | TEXT | 0 |  | 1 |
| value | TEXT | 0 |  | 2 |
| ordinal | INTEGER | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_enum_1 | 1 | pk | 0 | name, value |

### cfg_meta

- Columns: 2
- Primary key: key
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| key | TEXT | 0 |  | 1 |
| value | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_meta_1 | 1 | pk | 0 | key |

### cfg_on_fail

- Columns: 5
- Primary key: step, condition
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| step | TEXT | 0 |  | 1 |
| condition | TEXT | 0 |  | 2 |
| path | TEXT | 0 |  | 0 |
| resolver | TEXT | 0 |  | 0 |
| message | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_on_fail_1 | 1 | pk | 0 | step, condition |

### cfg_setting

- Columns: 3
- Primary key: key
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| key | TEXT | 0 |  | 1 |
| value | TEXT | 0 |  | 0 |
| use | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_setting_1 | 1 | pk | 0 | key |

### cfg_status_flow

- Columns: 4
- Primary key: entity, status
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| entity | TEXT | 0 |  | 1 |
| status | TEXT | 0 |  | 2 |
| set_by | TEXT | 0 |  | 0 |
| ordinal | INTEGER | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_status_flow_1 | 1 | pk | 0 | entity, status |

### cfg_step

- Columns: 6
- Primary key: work_package, step
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| work_package | TEXT | 0 |  | 1 |
| ordinal | INTEGER | 0 |  | 0 |
| step | TEXT | 0 |  | 2 |
| handler | TEXT | 0 |  | 0 |
| scope | TEXT | 0 |  | 0 |
| does | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_step_1 | 1 | pk | 0 | work_package, step |

### cfg_table

- Columns: 3
- Primary key: name
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| name | TEXT | 0 |  | 1 |
| grain | TEXT | 0 |  | 0 |
| use | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_table_1 | 1 | pk | 0 | name |

### cfg_unique

- Columns: 3
- Primary key: table_name, col
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| table_name | TEXT | 0 |  | 1 |
| col | TEXT | 0 |  | 2 |
| ordinal | INTEGER | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_unique_1 | 1 | pk | 0 | table_name, col |

### cfg_work_package

- Columns: 3
- Primary key: name
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| name | TEXT | 0 |  | 1 |
| ps_script | TEXT | 0 |  | 0 |
| runs_over | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_work_package_1 | 1 | pk | 0 | name |

### cfg_write_grant

- Columns: 2
- Primary key: writer, table_name
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| writer | TEXT | 0 |  | 1 |
| table_name | TEXT | 0 |  | 2 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_cfg_write_grant_1 | 1 | pk | 0 | writer, table_name |

### escalation

- Columns: 12
- Primary key: id
- Foreign keys: 1
- Indexes: 0

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| run_id | TEXT | 1 |  | 0 |
| word | TEXT | 0 |  | 0 |
| at_step | TEXT | 0 |  | 0 |
| type | TEXT | 0 |  | 0 |
| question | TEXT | 0 |  | 0 |
| preset | TEXT | 0 |  | 0 |
| tried | TEXT | 0 |  | 0 |
| state | TEXT | 0 |  | 0 |
| answer | TEXT | 0 |  | 0 |
| answered_at | TEXT | 0 |  | 0 |
| raised_at | TEXT | 0 |  | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| run_id | run | run_id | NO ACTION | NO ACTION | NONE |

### lemma_inventory

- Columns: 7
- Primary key: id
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| lemma_key | TEXT | 1 |  | 0 |
| gloss | TEXT | 0 |  | 0 |
| language | TEXT | 0 |  | 0 |
| source | TEXT | 0 |  | 0 |
| created_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_lemma_inventory_1 | 1 | u | 0 | lemma_key |

### passage

- Columns: 14
- Primary key: id
- Foreign keys: 1
- Indexes: 0

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| book | TEXT | 1 |  | 0 |
| anchor_verse_id | INTEGER | 1 |  | 0 |
| start_chapter | INTEGER | 0 |  | 0 |
| start_verse | INTEGER | 0 |  | 0 |
| end_chapter | INTEGER | 0 |  | 0 |
| end_verse | INTEGER | 0 |  | 0 |
| ref | TEXT | 0 |  | 0 |
| verse_count | INTEGER | 0 |  | 0 |
| rule | TEXT | 0 |  | 0 |
| source | TEXT | 0 |  | 0 |
| needs_review | INTEGER | 0 |  | 0 |
| created_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| anchor_verse_id | verse | id | NO ACTION | NO ACTION | NONE |

### run

- Columns: 11
- Primary key: id
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| run_id | TEXT | 1 |  | 0 |
| work_package | TEXT | 0 |  | 0 |
| params | TEXT | 0 |  | 0 |
| runs_over | TEXT | 0 |  | 0 |
| config_version | TEXT | 0 |  | 0 |
| state | TEXT | 0 |  | 0 |
| resume_point | TEXT | 0 |  | 0 |
| started_at | TEXT | 0 |  | 0 |
| ended_at | TEXT | 0 |  | 0 |
| outcome | TEXT | 0 |  | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_run_1 | 1 | u | 0 | run_id |

### span

- Columns: 9
- Primary key: id
- Foreign keys: 2
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| verse_id | INTEGER | 1 |  | 0 |
| position | INTEGER | 1 |  | 0 |
| surface | TEXT | 0 |  | 0 |
| strong_variant | TEXT | 0 |  | 0 |
| morph_code | TEXT | 0 |  | 0 |
| is_particle | INTEGER | 0 |  | 0 |
| built_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| strong_variant | strong | strongNumber | NO ACTION | NO ACTION | NONE |
| verse_id | verse | id | NO ACTION | NO ACTION | NONE |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_span_1 | 1 | u | 0 | verse_id, position |

### span_candidate

- Columns: 7
- Primary key: id
- Foreign keys: 1
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| span_id | INTEGER | 1 |  | 0 |
| lemma_key | TEXT | 0 |  | 0 |
| candidate_tag | TEXT | 0 |  | 0 |
| seed_source | TEXT | 0 |  | 0 |
| set_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| span_id | span | id | NO ACTION | NO ACTION | NONE |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_span_candidate_1 | 1 | u | 0 | span_id |

### strong

- Columns: 9
- Primary key: strongNumber
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| strongNumber | TEXT | 0 |  | 1 |
| accentedUnicode | TEXT | 0 |  | 0 |
| stepGloss | TEXT | 0 |  | 0 |
| stepTransliteration | TEXT | 0 |  | 0 |
| language | TEXT | 0 |  | 0 |
| count | INTEGER | 0 |  | 0 |
| freqList | TEXT | 0 |  | 0 |
| created_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_strong_1 | 1 | pk | 0 | strongNumber |

### strong_lexicon

- Columns: 4
- Primary key: strong
- Foreign keys: 1
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| strong | TEXT | 0 |  | 1 |
| lsj | TEXT | 0 |  | 0 |
| mounce | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| strong | strong | strongNumber | NO ACTION | NO ACTION | NONE |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_strong_lexicon_1 | 1 | pk | 0 | strong |

### strong_meaning_tree

- Columns: 6
- Primary key: id
- Foreign keys: 0
- Indexes: 0

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| lemma_key | TEXT | 1 |  | 0 |
| sense_code | TEXT | 0 |  | 0 |
| sense_text | TEXT | 0 |  | 0 |
| sort | INTEGER | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

### strong_sense

- Columns: 4
- Primary key: strong
- Foreign keys: 1
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| strong | TEXT | 0 |  | 1 |
| head | TEXT | 0 |  | 0 |
| is_own_lemma | INTEGER | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| strong | strong | strongNumber | NO ACTION | NO ACTION | NONE |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_strong_sense_1 | 1 | pk | 0 | strong |

### strong_verse

- Columns: 4
- Primary key: id
- Foreign keys: 2
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| strong | TEXT | 1 |  | 0 |
| verse_id | INTEGER | 1 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| verse_id | verse | id | NO ACTION | NO ACTION | NONE |
| strong | strong | strongNumber | NO ACTION | NO ACTION | NONE |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_strong_verse_1 | 1 | u | 0 | strong, verse_id |

### validation_result

- Columns: 9
- Primary key: id
- Foreign keys: 1
- Indexes: 0

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| run_id | TEXT | 1 |  | 0 |
| word | TEXT | 0 |  | 0 |
| step | TEXT | 0 |  | 0 |
| check_name | TEXT | 0 |  | 0 |
| result | TEXT | 0 |  | 0 |
| detail | TEXT | 0 |  | 0 |
| ran_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| run_id | run | run_id | NO ACTION | NO ACTION | NONE |

### verse

- Columns: 7
- Primary key: id
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| osisId | TEXT | 1 |  | 0 |
| reference | TEXT | 0 |  | 0 |
| preview | TEXT | 0 |  | 0 |
| step_version | TEXT | 0 |  | 0 |
| created_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_verse_1 | 1 | u | 0 | osisId |

### verse_passage

- Columns: 6
- Primary key: id
- Foreign keys: 2
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| passage_id | INTEGER | 1 |  | 0 |
| verse_id | INTEGER | 1 |  | 0 |
| is_anchor | INTEGER | 0 |  | 0 |
| created_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| verse_id | verse | id | NO ACTION | NO ACTION | NONE |
| passage_id | passage | id | NO ACTION | NO ACTION | NONE |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_verse_passage_1 | 1 | u | 0 | verse_id |

### word_registry

- Columns: 6
- Primary key: id
- Foreign keys: 0
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| word | TEXT | 1 |  | 0 |
| source | TEXT | 0 |  | 0 |
| status | TEXT | 0 |  | 0 |
| created_at | TEXT | 0 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_word_registry_1 | 1 | u | 0 | word |

### word_strong

- Columns: 4
- Primary key: id
- Foreign keys: 2
- Indexes: 1

| Column | Type | Not Null | Default | PK Ordinal |
|---|---|---:|---|---:|
| id | INTEGER | 0 |  | 1 |
| word_id | INTEGER | 1 |  | 0 |
| strong | TEXT | 1 |  | 0 |
| deleted | INTEGER | 0 | 0 | 0 |

Foreign keys:

| From | To Table | To Column | On Update | On Delete | Match |
|---|---|---|---|---|---|
| strong | strong | strongNumber | NO ACTION | NO ACTION | NONE |
| word_id | word_registry | id | NO ACTION | NO ACTION | NONE |

Indexes:

| Name | Unique | Origin | Partial | Columns |
|---|---:|---|---:|---|
| sqlite_autoindex_word_strong_1 | 1 | u | 0 | word_id, strong |

## Views

- None

## Triggers

- None
