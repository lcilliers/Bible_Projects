# Schema overview

> Generated 2026-07-30T05:31:54Z by `report.schema_overview`. Introspects the live DB directly — always current, never hand-maintained.

- data tables: **21** known, **21** live

## Contents

- [Table inventory](#table-inventory)
- [Every data table, in full](#every-data-table-in-full)

## Table inventory

| table | rows (live) | status |
| --- | --- | --- |
| candidate_seed | 1806 |  |
| escalation | 387 |  |
| lemma_inventory | 11781 |  |
| passage | 24 | **RETIRED** |
| run | 1070 |  |
| span | 370200 |  |
| span_candidate | 83914 |  |
| strong | 4585 |  |
| strong_lexicon | 1506 |  |
| strong_lsj_parsed | 10020 |  |
| strong_meaning_parsed | 16628 |  |
| strong_meaning_tree | 14292 |  |
| strong_mounce_parsed | 1547 |  |
| strong_related | 34347 |  |
| strong_sense | 4585 |  |
| strong_verse | 112446 |  |
| validation_result | 18989 |  |
| verse | 29037 |  |
| verse_passage | 480 | **RETIRED** |
| word_registry | 178 |  |
| word_strong | 4796 |  |

**Retired** (2) — soft-deleted at the data level, kept for the historical record, not part of the live system: `passage` (see `reports/archive/passage-system-retirement-record-20260726.md`); `verse_passage` (see `reports/archive/passage-system-retirement-record-20260726.md`)

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
indexes: sqlite_autoindex_candidate_seed_1

### escalation (387 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| run_id | TEXT |  | ✓ | run.run_id |
| word | TEXT |  |  |  |
| at_step | TEXT |  |  |  |
| type | TEXT |  |  |  |
| question | TEXT |  |  |  |
| preset | TEXT |  |  |  |
| tried | TEXT |  |  |  |
| state | TEXT |  |  |  |
| answer | TEXT |  |  |  |
| answered_at | TEXT |  |  |  |
| raised_at | TEXT |  |  |  |
| comment | TEXT |  |  |  |

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
indexes: sqlite_autoindex_lemma_inventory_1

### passage (24 row(s) — RETIRED, see note above)

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
indexes: idx_passage_range_live

### run (1070 row(s))

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

### span (370200 row(s))

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
indexes: sqlite_autoindex_span_1

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
indexes: sqlite_autoindex_span_candidate_1

### strong (4585 row(s))

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
indexes: sqlite_autoindex_strong_1

### strong_lexicon (1506 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  | strong.strongNumber |
| lsj | TEXT |  |  |  |
| mounce | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: sqlite_autoindex_strong_lexicon_1

### strong_lsj_parsed (10020 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| strong | TEXT |  | ✓ | strong.strongNumber |
| sense_label | TEXT |  |  |  |
| gloss | TEXT |  |  |  |
| note | TEXT |  |  |  |
| row_type | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |

### strong_meaning_parsed (16628 row(s))

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
| strong_variant | TEXT |  |  |  |

### strong_meaning_tree (14292 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| lemma_key | TEXT |  | ✓ |  |
| sense_code | TEXT |  |  |  |
| sense_text | TEXT |  |  |  |
| sort | INTEGER |  |  |  |
| deleted | INTEGER |  |  |  |
| strong_variant | TEXT |  |  |  |

### strong_mounce_parsed (1547 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| strong | TEXT |  | ✓ | strong.strongNumber |
| mounce_parsed | TEXT |  |  |  |
| row_type | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |

### strong_related (34347 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| strong | TEXT |  | ✓ | strong.strongNumber |
| related_strong | TEXT |  | ✓ |  |
| related_form | TEXT |  |  |  |
| related_transliteration | TEXT |  |  |  |
| related_gloss | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |

### strong_sense (4585 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| strong | TEXT | ✓ |  | strong.strongNumber |
| head | TEXT |  |  |  |
| is_own_lemma | INTEGER |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: sqlite_autoindex_strong_sense_1

### strong_verse (112446 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| strong | TEXT |  | ✓ | strong.strongNumber |
| verse_id | INTEGER |  | ✓ | verse.id |
| deleted | INTEGER |  |  |  |
indexes: sqlite_autoindex_strong_verse_1

### validation_result (18989 row(s))

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

### verse (29037 row(s))

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
indexes: sqlite_autoindex_verse_1

### verse_passage (480 row(s) — RETIRED, see note above)

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| passage_id | INTEGER |  | ✓ | passage.id |
| verse_id | INTEGER |  | ✓ | verse.id |
| is_anchor | INTEGER |  |  |  |
| created_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: idx_verse_passage_verse_id_live

### word_registry (178 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| word | TEXT |  | ✓ |  |
| source | TEXT |  |  |  |
| status | TEXT |  |  |  |
| created_at | TEXT |  |  |  |
| deleted | INTEGER |  |  |  |
indexes: sqlite_autoindex_word_registry_1

### word_strong (4796 row(s))

| column | type | pk | notnull | fk |
| --- | --- | --- | --- | --- |
| id | INTEGER | ✓ |  |  |
| word_id | INTEGER |  | ✓ | word_registry.id |
| strong | TEXT |  | ✓ | strong.strongNumber |
| deleted | INTEGER |  |  |  |
indexes: sqlite_autoindex_word_strong_1
