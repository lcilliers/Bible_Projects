# Field Data Raw Dump
## Source: Code archaeology from engine/ + Session A v9 Architecture spec
## Date: 2026-03-19
## Status: Raw gathered data — not yet formatted as final JSON

---

## PROCESSING MODES

- REGISTER       → engine/register.py  → run_register()
- NEW_WORD        → engine/new_word.py  → run_new_word()       steps N1–N19
- GAP_FILL_SINGLE → engine/gap_fill.py  → run_gap_fill()       steps S1–S8
- BULK_GAP_FILL   → engine/gap_fill.py  → run_bulk_gap_fill()  steps S1–S4
- AUDIT_WORD      → engine/audit_word.py → run_audit_word()    steps A1–A10

---

## TABLE: word_registry

### REGISTER steps
```sql
SELECT MAX(no) AS m FROM word_registry;          -- next_no = (m or 0) + 1
SELECT MAX(id) AS m FROM word_registry;          -- next_id = (m or 0) + 1
INSERT INTO word_registry
  (id, no, word, source_list, category_hint, phase1_status, automation_eligible)
  VALUES (?, ?, ?, ?, ?, 'Pending', 1);
```
- word: CLI arg --word (validated lowercase + hyphens only; must be unique)
- source_list: CLI arg --source (required non-empty)
- category_hint: CLI arg --category (optional, NULL if omitted)
- phase1_status: hardcoded 'Pending'
- automation_eligible: hardcoded 1

### NEW_WORD steps
```
N1:  SELECT * FROM word_registry WHERE no = ?
     STOP if: no row / phase1_status != 'Pending' / automation_eligible = 0

N2:  SELECT id FROM wa_file_index WHERE registry_id = ?
     STOP if rows exist and --force not set

N6:  UPDATE word_registry SET last_automation_run = 'IN_PROGRESS' WHERE no = ?
     (LOCK_SENTINEL — written before any API call)

N19: UPDATE word_registry
     SET phase1_status      = ?,   -- 'Complete' if audit PASS else 'In Progress'
         phase1_term_count  = ?,   -- counts['total_terms_new']
         phase1_verse_count = ?,   -- counts['total_verses_inserted']
         last_automation_run = ?,  -- _now() UTC timestamp
         automation_run_id  = ?,   -- run_id from run_log.make_run_id()
         phase1_input_file  = ?    -- run_id (not a file path)
     WHERE no = ?
```

### GAP_FILL_SINGLE steps
```
S1:  SELECT * FROM word_registry WHERE no = ?
     UPDATE word_registry SET last_automation_run = 'IN_PROGRESS' WHERE no = ?

S7:  SELECT COUNT(*) FROM wa_verse_records
       WHERE file_id IN (?) AND (span_strong_match=1 OR span_strong_match IS NULL)
     SELECT COUNT(*) FROM wa_term_inventory WHERE file_id IN (?)
     UPDATE word_registry
     SET phase1_status       = ?,   -- 'In Progress' if audit STOP/REVIEW else unchanged
         phase1_term_count   = ?,
         phase1_verse_count  = ?,
         last_automation_run = ?,
         automation_run_id   = ?
     WHERE no = ?
```

### BULK_GAP_FILL steps
```
S1:  SELECT no, id, word, strongs_list, source_list FROM word_registry
       WHERE phase1_status = 'Pending' ORDER BY no
     -- For each word where strongs_list IS NULL:
     StepClient.get_strongs_for_word(word)
     UPDATE word_registry SET strongs_list = ? WHERE no = ?

S2 Phase A:
     UPDATE word_registry
     SET phase1_status    = 'In Progress',
         automation_run_id = ?,
         last_automation_run = ?
     WHERE no = ?
```

### AUDIT_WORD steps
```
A1/A2: SELECT * FROM word_registry WHERE no = ?  (read only)

A10:  -- recount same as S7 pattern
      UPDATE word_registry
      SET last_automation_run = ?,
          automation_run_id   = ?
      WHERE no = ?
```

### Fields summary
| field               | REGISTER | NEW_WORD | GAP_FILL_SINGLE | BULK_GAP_FILL | AUDIT_WORD |
|---------------------|----------|----------|-----------------|---------------|------------|
| id                  | INSERT   | READ     | READ            | READ          | READ       |
| no                  | INSERT   | READ     | READ            | READ          | READ       |
| word                | INSERT   | READ     | READ            | READ          | READ       |
| source_list         | INSERT   | READ→propagated | —        | READ→propagated | —     |
| category_hint       | INSERT   | —        | —               | —             | —          |
| phase1_status       | INSERT='Pending' | N1 READ; N19 UPDATE | S1 READ; S7 UPDATE | S2A UPDATE='In Progress'; S4 UPDATE | A1 READ; A10 UPDATE |
| automation_eligible | INSERT=1 | N1 READ  | —               | S1 filter     | —          |
| last_automation_run | —        | N6 LOCK_SENTINEL; N19 timestamp | S1 LOCK; S7 timestamp | S2A timestamp | A10 timestamp |
| automation_run_id   | —        | N19      | S7              | S2A; S4       | A10        |
| phase1_term_count   | —        | N19      | S7              | —             | A10        |
| phase1_verse_count  | —        | N19      | S7              | —             | A10        |
| phase1_input_file   | —        | N19=run_id | —             | —             | —          |
| strongs_list        | —        | —        | —               | S1 UPDATE     | —          |

---

## TABLE: wa_file_index

### NEW_WORD N9 INSERT (part of atomic transaction N9-N15)
```sql
-- id = get_max_id(conn, "wa_file_index") + 1
INSERT INTO wa_file_index
  (id, filename, registry_id, word_registry_fk, word,
   part_number, total_parts, is_split,
   specification, phase, produced_date, translation_used,
   source_list, testament_coverage)
VALUES
  (?,            -- get_max_id("wa_file_index")+1
   ?,            -- run_id  (e.g. RUN-20260319_143022-NEW_WORD)
   ?,            -- str(registry_id)  = word_registry.no as string
   ?,            -- reg_row['id']     = word_registry.id (PK)
   ?,            -- reg_row['word']
   NULL,         -- part_number  (legacy v3-v8; always NULL in v9)
   NULL,         -- total_parts  (legacy; always NULL in v9)
   0,            -- is_split     (legacy; always 0 in v9)
   ?,            -- SPECIFICATION constant from engine/constants.py
   'Phase 1',    -- hardcoded
   ?,            -- _today() = datetime.now(utc).strftime('%Y-%m-%d')
   'ESV',        -- hardcoded
   ?,            -- reg_row['source_list']
   NULL);        -- testament_coverage: derived later at N14
```

### NEW_WORD N14 UPDATE
```sql
SELECT DISTINCT testament FROM wa_verse_records
  WHERE file_id = ? AND span_strong_match = 1;
-- Derive: only OT rows → 'OT_only'; only NT → 'NT_only'; both → 'both'; none → NULL

UPDATE wa_file_index SET testament_coverage = ? WHERE id = ?;
UPDATE wa_term_inventory SET testament = ? WHERE id = ?;
```

### BULK_GAP_FILL S2 Phase A
```sql
-- Same INSERT schema as N9
INSERT INTO wa_file_index (...) VALUES (...);
```

### AUDIT_WORD A9
```sql
SELECT DISTINCT testament FROM wa_verse_records
  WHERE file_id = ? AND (span_strong_match = 1 OR span_strong_match IS NULL);
UPDATE wa_file_index SET testament_coverage = ? WHERE id = ?;
```

### Fields summary
| field                        | NEW_WORD         | BULK_GAP_FILL | AUDIT_WORD |
|------------------------------|------------------|---------------|------------|
| id                           | N9 INSERT        | S2A INSERT    | READ       |
| filename                     | N9 INSERT=run_id | S2A INSERT    | READ       |
| registry_id                  | N9 INSERT        | S2A INSERT    | READ       |
| word_registry_fk             | N9 INSERT        | S2A INSERT    | READ       |
| word                         | N9 INSERT        | S2A INSERT    | READ       |
| part_number                  | N9 INSERT=NULL   | S2A INSERT=NULL | —        |
| total_parts                  | N9 INSERT=NULL   | S2A INSERT=NULL | —        |
| is_split                     | N9 INSERT=0      | S2A INSERT=0  | —          |
| specification                | N9 INSERT=const  | S2A INSERT    | —          |
| phase                        | N9 INSERT='Phase 1' | S2A INSERT | —         |
| produced_date                | N9 INSERT=today  | S2A INSERT    | —          |
| translation_used             | N9 INSERT='ESV'  | S2A INSERT    | —          |
| source_list                  | N9 INSERT        | S2A INSERT    | —          |
| testament_coverage           | N9 INSERT=NULL; N14 UPDATE | — | A9 UPDATE |
| root_families_in_prior_parts | NOT WRITTEN (legacy) | —      | —          |

---

## TABLE: mti_terms

### NEW_WORD N10 INSERT
```sql
-- id = get_max_id(conn, "mti_terms") + 1
INSERT INTO mti_terms
  (id, strongs_number, transliteration, gloss, language,
   owning_registry, owning_word, owning_part,
   word_data_reference, status, extraction_date, strongs_reconciled)
VALUES
  (?,            -- get_max_id("mti_terms")+1
   ?,            -- resolved strongs (e.g. H7965)
   ?,            -- vocab_map[strongs]['transliteration']
   ?,            -- vocab_map[strongs]['gloss']
   ?,            -- classify_strongs(resolved) → 'Hebrew' or 'Greek'
   ?,            -- str(registry_id)
   ?,            -- reg_row['word']
   NULL,         -- owning_part (legacy multi-part; always NULL in v9)
   ?,            -- str(file_id)   (wa_file_index.id as string)
   'extracted',  -- hardcoded
   ?,            -- _today()
   ?);           -- 1 if resolved != strongs_input else 0  (suffix resolved)
```

### BULK_GAP_FILL S2 Phase C
```sql
-- Same INSERT schema as N10
INSERT INTO mti_terms (...) VALUES (...);
```

### Fields summary
| field              | NEW_WORD      | BULK_GAP_FILL | GAP_FILL_SINGLE | AUDIT_WORD |
|--------------------|---------------|---------------|-----------------|------------|
| id                 | N10 INSERT    | S2C INSERT    | READ            | READ       |
| strongs_number     | N10 INSERT    | S2C INSERT    | READ            | READ       |
| transliteration    | N10 INSERT    | S2C INSERT    | —               | —          |
| gloss              | N10 INSERT    | S2C INSERT    | —               | —          |
| language           | N10 INSERT    | S2C INSERT    | —               | —          |
| owning_registry    | N10 INSERT    | S2C INSERT    | —               | —          |
| owning_word        | N10 INSERT    | S2C INSERT    | —               | —          |
| owning_part        | N10 INSERT=NULL | S2C INSERT=NULL | —           | —          |
| word_data_reference| N10 INSERT=file_id | S2C INSERT | —             | —          |
| status             | N10 INSERT='extracted' | S2C | —             | —          |
| extraction_date    | N10 INSERT=today | S2C INSERT  | —               | —          |
| strongs_reconciled | N10 INSERT=0or1 | S2C INSERT  | —               | —          |

---

## TABLE: mti_term_cross_refs

### NEW_WORD N13
```sql
INSERT OR IGNORE INTO mti_term_cross_refs
  (id, mti_term_id, registry, word)
  VALUES (?, ?, ?, ?);
-- get_max_id("mti_term_cross_refs")+1
-- mti_term_id = mti_terms.id for this strongs
-- registry = str(registry_id)
-- word = reg_row['word']
```

### BULK_GAP_FILL S2 Phase A
```sql
-- Same INSERT OR IGNORE as N13
INSERT OR IGNORE INTO mti_term_cross_refs (id, mti_term_id, registry, word) VALUES (...);
```

### Fields summary
| field       | NEW_WORD           | BULK_GAP_FILL |
|-------------|--------------------|--------------------|
| id          | N13 INSERT OR IGNORE | S2A INSERT OR IGNORE |
| mti_term_id | N13 INSERT         | S2A INSERT         |
| registry    | N13 INSERT=str(registry_id) | S2A INSERT |
| word        | N13 INSERT=reg_row['word'] | S2A INSERT  |

---

## TABLE: wa_term_inventory

### NEW_WORD N11 INSERT
```sql
-- id = get_max_id(conn, "wa_term_inventory") + 1
INSERT INTO wa_term_inventory
  (id, file_id, language, term_id, strongs_number, transliteration,
   step_search_gloss, word_analysis_gloss, occurrence_count,
   meaning, meaning_numbered, lsj_entry, short_def_mounce,
   testament, causative_form_present, status_note)
VALUES
  (?,    -- get_max_id("wa_term_inventory")+1
   ?,    -- file_id (wa_file_index.id)
   ?,    -- classify_strongs(resolved) → 'Hebrew'/'Greek'
   ?,    -- term_id = resolved strongs string
   ?,    -- strongs_number = resolved strongs
   ?,    -- vocab_map[strongs]['transliteration']
   ?,    -- vocab_map[strongs]['step_gloss']
   ?,    -- vocab_map[strongs]['word_analysis_gloss']
   ?,    -- vocab_map[strongs]['occurrence_count'] or NULL
   NULL, -- meaning: filled later at meaning_parser (N15)
   NULL, -- meaning_numbered: filled later
   ?,    -- vocab_map[strongs]['lsj_entry'] or NULL (Greek only)
   ?,    -- vocab_map[strongs]['short_def_mounce'] or NULL (Greek only)
   NULL, -- testament: derived at N14
   ?,    -- vocab_map[strongs]['causative_form_present'] (Hebrew; 0/1/NULL)
   NULL);-- status_note: researcher field; not written by engine
```

### GAP_FILL_SINGLE S4 COALESCE UPDATE
```sql
UPDATE wa_term_inventory
SET meaning          = ?,
    meaning_numbered = ?,
    step_search_gloss  = COALESCE(step_search_gloss, ?),
    word_analysis_gloss = COALESCE(word_analysis_gloss, ?)
WHERE id = ?;

UPDATE wa_term_inventory
SET lsj_entry = COALESCE(lsj_entry, ?)
WHERE id = ?;
-- Also calls run_parser_for_file() → meaning_parser.py (see below)
```

### AUDIT_WORD A4 COALESCE UPDATE (audit_word.py lines 309-316)
```sql
UPDATE wa_term_inventory
SET step_search_gloss   = COALESCE(NULLIF(step_search_gloss,''), ?),
    word_analysis_gloss = COALESCE(NULLIF(word_analysis_gloss,''), ?),
    meaning             = COALESCE(NULLIF(meaning,''), ?),
    meaning_numbered    = COALESCE(NULLIF(meaning_numbered,''), ?),
    occurrence_count    = COALESCE(occurrence_count, ?),
    lsj_entry          = COALESCE(NULLIF(lsj_entry,''), ?),
    short_def_mounce   = COALESCE(NULLIF(short_def_mounce,''), ?)
WHERE id = ?;
```

### meaning_parser.py → sets parsed_meaning_id FK
```sql
UPDATE wa_term_inventory SET parsed_meaning_id = ? WHERE id = ?;
```

### Fields summary
| field               | NEW_WORD     | GAP_FILL_SINGLE | BULK_GAP_FILL | AUDIT_WORD |
|---------------------|--------------|-----------------|---------------|------------|
| id                  | N11 INSERT   | READ            | S2C INSERT    | READ       |
| file_id             | N11 INSERT   | READ            | S2C INSERT    | READ       |
| language            | N11 INSERT   | —               | S2C INSERT    | —          |
| term_id             | N11 INSERT   | READ            | S2C INSERT    | READ       |
| strongs_number      | N11 INSERT   | READ            | S2C INSERT    | READ       |
| transliteration     | N11 INSERT   | —               | S2C INSERT    | —          |
| step_search_gloss   | N11 INSERT   | S4 COALESCE UPDATE | S2C INSERT | A4 COALESCE(NULLIF) UPDATE |
| word_analysis_gloss | N11 INSERT   | S4 COALESCE UPDATE | S2C INSERT | A4 COALESCE(NULLIF) UPDATE |
| occurrence_count    | N11 INSERT   | —               | S2C INSERT    | A4 COALESCE UPDATE |
| meaning             | N11 INSERT=NULL; N15 parse | S4 UPDATE | S2C→S4 parse | A4 COALESCE(NULLIF) |
| meaning_numbered    | N11 INSERT=NULL; N15 parse | S4 UPDATE | S2C→S4 parse | A4 COALESCE(NULLIF) |
| lsj_entry           | N11 INSERT (Greek) | S4 COALESCE | S2C    | A4 COALESCE(NULLIF) |
| short_def_mounce    | N11 INSERT (Greek) | —           | S2C    | A4 COALESCE(NULLIF) |
| testament           | N11 INSERT=NULL; N14 UPDATE | — | S2C=NULL | A9 via wa_file_index |
| causative_form_present | N11 INSERT (Hebrew) | —    | S2C    | —          |
| status_note         | N11 INSERT=NULL | —           | S2C=NULL | NOT WRITTEN (researcher field) |
| parsed_meaning_id   | N15 via meaning_parser UPDATE | S4 via meaning_parser | S4 | — |
| also_spelled        | N18 interactive prompt (Hebrew only) | — | — | — |
| occurrence_count_qualifier | N18 interactive prompt | — | —    | —          |
| causative_flag      | N16 flag_engine | S5           | S4     | A7         |
| lsj_domains         | N15 meaning_parser | S4 parse  | S4 parse | —        |

---

## TABLE: wa_term_related_words

### NEW_WORD N11 (written same transaction as wa_term_inventory)
```sql
INSERT INTO wa_term_related_words
  (term_inv_id, gloss, transliteration, strongs_number)
  VALUES (?, ?, ?, ?);
-- One row per related word in vocab_map[strongs]['related_words'] list
-- term_inv_id = wa_term_inventory.id just inserted
```

### BULK_GAP_FILL S2 Phase C
```sql
-- Same INSERT schema
INSERT INTO wa_term_related_words (term_inv_id, gloss, transliteration, strongs_number)
  VALUES (?, ?, ?, ?);
```

### Fields summary
| field           | NEW_WORD   | BULK_GAP_FILL | GAP_FILL_SINGLE | AUDIT_WORD |
|-----------------|------------|---------------|-----------------|------------|
| term_inv_id     | N11 INSERT | S2C INSERT    | NOT WRITTEN     | NOT WRITTEN |
| gloss           | N11 INSERT | S2C INSERT    | NOT WRITTEN     | NOT WRITTEN |
| transliteration | N11 INSERT | S2C INSERT    | NOT WRITTEN     | NOT WRITTEN |
| strongs_number  | N11 INSERT | S2C INSERT    | NOT WRITTEN     | NOT WRITTEN |

---

## TABLE: wa_verse_records

### NEW_WORD N12 INSERT (inside atomic transaction N9-N15)
```sql
-- id = get_max_id(conn, "wa_verse_records") + 1
INSERT INTO wa_verse_records
  (id, file_id, term_inv_id, term_id, transliteration,
   book_id, reference, chapter, verse_num, testament,
   translation, verse_text, target_word,
   span_strong_match, context_before, context_after)
VALUES
  (?,         -- get_max_id("wa_verse_records")+1
   ?,         -- file_id
   ?,         -- term_inv_id (wa_term_inventory.id)
   ?,         -- term_id (strongs string e.g. H7965)
   ?,         -- transliteration
   ?,         -- book_id (integer from STEP)
   ?,         -- reference e.g. 'Gen.24.21'
   ?,         -- chapter integer
   ?,         -- verse_num integer
   ?,         -- testament e.g. 'OT'/'NT' from STEP
   'ESV',     -- hardcoded
   ?,         -- verse_text (ESV text from STEP HTML)
   ?,         -- target_word (matched word text from span)
   ?,         -- span_strong_match: 1=confirmed, 0=not found, NULL=not yet checked
   NULL,      -- context_before: Phase 2 field; NULL in Phase 1
   NULL);     -- context_after:  Phase 2 field; NULL in Phase 1
```
NOTE: span_strong_match values:
-  1 = confirmed span match
-  0 = no match found
- -1 = orphan (no verse at reference)
- NULL = not yet processed

### GAP_FILL_SINGLE S3 INSERT (same schema as N12)
```sql
-- Same INSERT for new verse records fetched during gap-fill
INSERT INTO wa_verse_records (...) VALUES (...);
```

### AUDIT_WORD A3a UPDATE
```sql
-- Update span match result after re-evaluation
UPDATE wa_verse_records
SET span_strong_match = ?,   -- 1/0/-1
    target_word       = ?,   -- updated if span found
    verse_text        = ?    -- updated if re-fetched
WHERE id = ?;

-- Mark orphan (verse reference no longer found in STEP)
UPDATE wa_verse_records SET span_strong_match = -1 WHERE id = ?;
```

### Fields summary
| field             | NEW_WORD       | GAP_FILL_SINGLE | BULK_GAP_FILL | AUDIT_WORD |
|-------------------|----------------|-----------------|---------------|------------|
| id                | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| file_id           | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| term_inv_id       | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| term_id           | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| transliteration   | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| book_id           | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| reference         | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| chapter           | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| verse_num         | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| testament         | N12 INSERT     | S3 INSERT       | S3 INSERT     | READ       |
| translation       | N12 INSERT='ESV' | S3 INSERT='ESV' | S3='ESV'   | READ       |
| verse_text        | N12 INSERT     | S3 INSERT       | S3 INSERT     | A3a UPDATE (if re-fetched) |
| target_word       | N12 INSERT     | S3 INSERT       | S3 INSERT     | A3a UPDATE |
| span_strong_match | N12 INSERT=0/1/NULL | S3 INSERT  | S3 INSERT     | A3a UPDATE |
| context_before    | N12 INSERT=NULL (Phase 2) | NULL  | NULL   | NOT WRITTEN |
| context_after     | N12 INSERT=NULL (Phase 2) | NULL  | NULL   | NOT WRITTEN |

---

## TABLE: wa_meaning_parsed

### meaning_parser.py (called at N15 / S4 / BULK S4)
```sql
-- Check for existing record (idempotent)
SELECT id FROM wa_meaning_parsed WHERE term_inv_id = ?;

-- If exists: delete child rows first (cascade not set — manual delete)
DELETE FROM wa_meaning_sense WHERE parsed_meaning_id = ?;
DELETE FROM wa_meaning_stem  WHERE parsed_meaning_id = ?;
DELETE FROM wa_lsj_parsed    WHERE term_inv_id = ?;
DELETE FROM wa_meaning_parsed WHERE id = ?;

-- Insert new record
-- id = get_max_id(conn, "wa_meaning_parsed") + 1
INSERT INTO wa_meaning_parsed
  (id, term_inv_id, strongs_number, language,
   top_sense_count, stem_count, has_causative_stem, has_domain_tags,
   parsed_at, parse_version, parse_warnings)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
-- parse_version = PARSER_VERSION constant from meaning_parser.py
-- parsed_at     = _now() UTC timestamp
```

### Fields summary
| field              | NEW_WORD N15 | GAP_FILL S4 | BULK S4 | AUDIT_WORD |
|--------------------|--------------|-------------|---------|------------|
| id                 | INSERT       | INSERT (re-parse) | INSERT | — |
| term_inv_id        | INSERT       | INSERT      | INSERT  | — |
| strongs_number     | INSERT       | INSERT      | INSERT  | — |
| language           | INSERT       | INSERT      | INSERT  | — |
| top_sense_count    | INSERT       | INSERT      | INSERT  | — |
| stem_count         | INSERT       | INSERT      | INSERT  | — |
| has_causative_stem | INSERT       | INSERT      | INSERT  | — |
| has_domain_tags    | INSERT       | INSERT      | INSERT  | — |
| parsed_at          | INSERT=_now() | INSERT     | INSERT  | — |
| parse_version      | INSERT=const | INSERT      | INSERT  | — |
| parse_warnings     | INSERT       | INSERT      | INSERT  | — |

---

## TABLE: wa_meaning_sense

### meaning_parser.py — one row per sense node
```sql
INSERT INTO wa_meaning_sense
  (parsed_meaning_id, level_code, level_depth, parent_level_code,
   sense_text, is_stem_label, stem_label, domain_tag, sort_order)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
-- parsed_meaning_id = wa_meaning_parsed.id just inserted
-- Data source: parse_term(vocab) → parsed["sense_nodes"] list
```

### Fields summary: all fields written at N15/S4 INSERT; deleted+reinserted on re-parse

---

## TABLE: wa_meaning_stem

### meaning_parser.py — one row per stem node
```sql
INSERT INTO wa_meaning_stem
  (parsed_meaning_id, stem_name, stem_type, sense_count, top_sense_text)
VALUES (?, ?, ?, ?, ?);
-- Data source: parse_term(vocab) → parsed["stem_nodes"] list
```

### Fields summary: all fields written at N15/S4 INSERT; deleted+reinserted on re-parse

---

## TABLE: wa_lsj_parsed

### meaning_parser.py — Greek only; one row per term
```sql
INSERT INTO wa_lsj_parsed
  (term_inv_id, raw_lsj, lsj_gloss, lsj_domains,
   lsj_philosophical_note, lsj_etymology_note, lsj_cognate_forms,
   parsed_at, parse_version)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
-- Only inserted when parsed["lsj_fields"] is non-empty (Greek terms only)
-- raw_lsj = vocab_map[strongs].get('lsj_entry', '')
-- lsj_* fields = parsed["lsj_fields"] subdict
```

### Fields summary: all fields written at N15/S4 INSERT for Greek terms only

---

## TABLE: wa_data_quality_flags

### flag_engine.py (called at N16 / S5 / A7)
```sql
-- Flag type lookup
SELECT id FROM wa_quality_flag_types WHERE flag_code = ?;

INSERT INTO wa_data_quality_flags
  (file_id, term_id, flag_id, description)
  VALUES (?, ?, ?, ?);
-- file_id    = wa_file_index.id
-- term_id    = strongs_number string
-- flag_id    = wa_quality_flag_types.id (FK)
-- description = generated description string
```

### Flags evaluated (derivable — no researcher judgment needed)
- HIGH_FREQUENCY_ANCHOR: occurrence_count >= HIGH_FREQ_THRESHOLD (constants.py)
- THIN_DATA:             occurrence_count < THIN_DATA_THRESHOLD (constants.py)
- SMALL_VERSE_SAMPLE:   confirmed verse count < SMALL_VERSE_SAMPLE_THRESHOLD
- NO_WORD_ANALYSIS:     meaning IS NULL
- NO_VERSES:            zero confirmed verses AND no SPAN_RESOLUTION_CONFLICT
- SPAN_RESOLUTION_CONFLICT: queued during fetch step (N8/S3); written here

### Fields summary
| field       | NEW_WORD N16 | GAP_FILL S5 | BULK S4 | AUDIT_WORD A7 |
|-------------|--------------|-------------|---------|----------------|
| file_id     | INSERT       | INSERT      | INSERT  | INSERT         |
| term_id     | INSERT       | INSERT      | INSERT  | INSERT         |
| flag_id     | INSERT (FK)  | INSERT      | INSERT  | INSERT         |
| description | INSERT       | INSERT      | INSERT  | INSERT         |

---

## TABLE: engine_run_log

### run_log.py open_run() — called at start of every mode
```sql
INSERT INTO engine_run_log
  (run_id, mode, target_registry_ids, started_at, outcome)
  VALUES (?, ?, ?, ?, 'RUNNING');
-- run_id              = make_run_id(mode) → f"RUN-{ts}-{mode}"
-- mode                = 'NEW_WORD'/'GAP_FILL'/'BULK_GAP_FILL'/'AUDIT_WORD'
-- target_registry_ids = comma-separated string of registry no values
-- started_at          = _now() UTC
-- outcome             = 'RUNNING' (initial)
```

### run_log.py close_run() — called at end of every mode
```sql
UPDATE engine_run_log
SET completed_at          = ?,    -- _now()
    outcome               = ?,    -- 'COMPLETE'/'STOPPED'/'ERROR'
    words_attempted       = ?,
    words_complete        = ?,
    words_stopped         = ?,
    total_terms_new       = ?,
    total_terms_xref      = ?,
    total_verses_inserted = ?,
    total_verses_filtered = ?,
    total_meanings_parsed = ?,
    error_detail          = ?     -- json.dumps(errors) or NULL
WHERE run_id = ?;
```

### Fields summary: all fields written by all modes (open_run + close_run)

---

## TABLE: word_run_state

### run_log.py write_word_run_state() — called at N17/S6/BULK S4/A8
```sql
INSERT INTO word_run_state
  (run_id, registry_id, word, phase_reached,
   audit_result, audit_detail, stop_reason)
VALUES (?, ?, ?, ?, ?, ?, ?);
-- registry_id  = str(registry_id).zfill(3)  e.g. '007'
-- phase_reached = step label e.g. 'N17'/'GAP_FILL_S6'
-- audit_result  = 'PASS'/'STOP'/'REVIEW'/'UNKNOWN'
-- audit_detail  = json.dumps(dict)
-- stop_reason   = string or NULL
```

### Fields summary
| field         | Written by        |
|---------------|-------------------|
| id            | auto PK           |
| run_id        | INSERT (all modes) |
| registry_id   | INSERT (zfill 3)  |
| word          | INSERT            |
| phase_reached | INSERT            |
| audit_result  | INSERT            |
| audit_detail  | INSERT (JSON)     |
| stop_reason   | INSERT or NULL    |
| created_at    | DEFAULT timestamp |

---

## TABLE: engine_stream_checkpoint

### run_log.py upsert_checkpoint() — called during BULK_GAP_FILL streams
```sql
-- Check if exists
SELECT id FROM engine_stream_checkpoint WHERE run_id = ? AND stream_name = ?;

-- If exists: UPDATE
UPDATE engine_stream_checkpoint
SET status          = ?,
    last_registry_id = ?,
    last_strong      = ?,
    rows_written     = ?,
    rows_filtered    = ?,
    error_detail     = ?,
    completed_at     = CASE WHEN ? IN ('complete','failed') THEN ? ELSE completed_at END
WHERE run_id = ? AND stream_name = ?;

-- If new: INSERT
INSERT INTO engine_stream_checkpoint
  (run_id, stream_name, status, last_registry_id, last_strong,
   rows_written, rows_filtered, error_detail, started_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
```

---

## TABLE: term_fetch_log

### run_log.py log_fetch() — called at N7 (NEW_WORD vocab fetch) and S2/S3 fetches
```sql
INSERT INTO term_fetch_log
  (run_id, registry_id, strongs_input, strongs_resolved,
   suffix_resolution, vocab_status, verse_status,
   verse_count_fetched, verse_count_stored,
   verse_count_filtered, span_conflict, api_warnings, fetched_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
-- suffix_resolution = 1 if strongs_resolved != strongs_input else 0
-- api_warnings      = json.dumps(list) or NULL
-- fetched_at        = _now()
```

---

## TABLE: schema_version

### db.py get_schema_version()
```sql
SELECT version_code FROM schema_version WHERE id = 1;
-- Read at N5 (NEW_WORD) to confirm EXPECTED_SCHEMA_VERSION matches
-- Never written by engine modes — set by migration scripts only
```

---

## API CALLS (analytics/step_client.py)

```
StepClient().get_vocab_info(strongs)
  → GET /vocab?strong={strongs}&version=ESV
  → returns vocab_map dict with keys:
      transliteration, gloss, step_gloss, word_analysis_gloss,
      occurrence_count, lsj_entry, short_def_mounce,
      causative_form_present, related_words[]

StepClient().get_verse_records_with_html(strongs)
  → GET /passage?strong={strongs}&version=ESV
  → returns raw verse list with span HTML
  → then: filter_verse_records(raw, resolved, html_map) in span_filter.py
      → outputs: stored[], filtered[], span_conflicts (set of term_ids)

StepClient.get_strongs_for_word(word)
  → GET /search?q={word}&version=ESV (text search — BULK_GAP_FILL S1 only)
  → tallies span strong= codes across results
  → returns JSON array: [{"strong": "H7965", "count": 148}, ...]
```

---

## SPEC RULES SUMMARY (Session A v9 Architecture §1-§9)

- §1.2: Registry is the anchor — every run begins and ends with a word_registry row
- §1.3: All writes must be idempotent
- §7.1: --register writes Pending/automation_eligible=1
- §7.4: LOCK_SENTINEL ('IN_PROGRESS') must be written before any API call; stale lock (>2 hrs) → warning
- §7.2 N1: STOP if phase1_status != Pending OR automation_eligible = 0
- §7.2 N2: STOP if wa_file_index rows exist for registry_id (unless --force)
- §7.2 N5: STOP if schema version != EXPECTED_SCHEMA_VERSION
- §7.3: part_number/total_parts/is_split are legacy columns — always NULL/0 in v9
- §5.2: span_strong_match: 1=confirmed, 0=not found, -1=orphan, NULL=unprocessed
- §5.5: context_before/context_after are Phase 2 fields — NULL in Phase 1
- §9:   specification='Session A v9 Automation'; phase='Phase 1'; translation='ESV'
- §8.1: Audit checks WR-01 to WR-20 — STOP/REVIEW class per check
- §4 M03: All sequential IDs must use SELECT MAX(id)+1 live — never hardcode
