-- ─────────────────────────────────────────────────────────────────────────────
-- Bible_Projects – SQLite Schema
-- File:   data/schema/create_tables.sql
-- Schema version: v3.8.0
-- Last updated: 2026-04-06
-- Run via: python analytics/bible_analytics.py --init-db
--          OR: python -c "from analytics.db_client import get_connection, init_schema_from_file; conn=get_connection(); init_schema_from_file(conn); conn.close()"
-- Note: run `python -m engine.engine --migrate` after --init-db on an existing
--       database.  On a fresh DB all tables created here include migration cols,
--       so migrations are no-ops.
--
-- Table groups:
--   Section 1  — Reference tables:       books, book_code_variants, themes, sources
--   Section 2  — Registry:               word_registry
--   Section 3  — WA file index:          wa_file_index
--   Section 4  — WA term data:           wa_term_inventory, wa_term_related_words, wa_term_root_family
--   Section 5  — Phase-2 flags (shared): phase2_flag_types, wa_term_phase2_flags
--   Section 6  — WA quality flags:       wa_quality_flag_types, wa_data_quality_flags
--   Section 7  — WA cross-registry:      wa_crosslink_type, wa_cross_registry_links
--   Section 8  — WA verse records:       wa_verse_records, wa_verse_term_links
--   Section 9  — MTI tables:             mti_terms, mti_term_flags, mti_term_cross_refs
--   Section 10 — Engine control:         engine_run_log, engine_stream_checkpoint, word_run_state, term_fetch_log
--   Section 11 — Meaning parsing:        wa_meaning_parsed, wa_meaning_sense, wa_meaning_stem, wa_lsj_parsed
--   Section 12 — Schema metadata:        schema_version
--   Section 13 — Session research:       wa_session_research_flags (M13)
--   Section 14 — Session B structured:   wa_session_b_dimensions, wa_session_b_findings (M16)
--   Section 15 — Session D:              session_d_runs, session_d_verse_links, session_d_term_links, session_d_observations (M16)
--   Section 16 — Verse Context:          verse_context_group, verse_context (M18)
--   Section 17 — Dimension Index:        wa_dimension_index
-- ─────────────────────────────────────────────────────────────────────────────

PRAGMA foreign_keys = ON;

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 1 — REFERENCE TABLES
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 1.1  books ───────────────────────────────────────────────────────────────
-- Static reference: one row per Bible book (66 rows).
CREATE TABLE IF NOT EXISTS books (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT    NOT NULL UNIQUE,          -- common display name, e.g. "Genesis", "John"
    full_name    TEXT,                             -- formal title, e.g. "The Gospel According to John"
    abbreviation TEXT    NOT NULL UNIQUE,          -- scholarly short form, e.g. "Gen", "1 Cor"
    short_code   TEXT    NOT NULL UNIQUE,          -- machine code used in verse refs, e.g. "Gen", "1Co"
    testament    TEXT    NOT NULL                  -- "OT" or "NT"
                 CHECK (testament IN ('OT', 'NT')),
    book_order   INTEGER NOT NULL UNIQUE,          -- canonical order 1–66
    verse_count  INTEGER NOT NULL DEFAULT 0,       -- refreshed from verse data on demand
    last_updated TEXT    NOT NULL                  -- ISO-8601 datetime of last verse_count refresh
                 DEFAULT (strftime('%Y-%m-%dT%H:%M:%S', 'now'))
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_books_short_code ON books (short_code);

-- ── 1.2  book_code_variants ───────────────────────────────────────────────────
-- Maps every known book short code (canonical + STEP aliases) to a books.id.
-- Used by resolve_verse_refs() to derive book_id from an imported reference.
-- STEP aliases: Jude→65 (Jud), 2Jo→63 (2Jn), 3Jo→64 (3Jn), Phile→57 (Phm)
CREATE TABLE IF NOT EXISTS book_code_variants (
    code    TEXT    PRIMARY KEY,
    book_id INTEGER NOT NULL REFERENCES books(id)
);

-- ── 1.3  themes ──────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS themes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,           -- e.g. "salvation"
    description TEXT
);

-- ── 1.4  sources ─────────────────────────────────────────────────────────────
-- Reference sources: Zotero items, commentaries, lexicons, etc.
CREATE TABLE IF NOT EXISTS sources (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    zotero_key  TEXT    UNIQUE,
    title       TEXT    NOT NULL,
    author      TEXT,
    year        INTEGER,
    source_type TEXT                               -- "commentary", "lexicon", "paper", etc.
);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 2 — REGISTRY
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 2.1  word_registry ───────────────────────────────────────────────────────
-- Master list of 181 soul/inner-being words being studied.
-- One row per word; id is the registry number (not autoincrement).
CREATE TABLE IF NOT EXISTS word_registry (
    id                  INTEGER PRIMARY KEY,        -- registry number, e.g. 4, 72, 103
    no                  INTEGER,                    -- sequence number within source list
    word                TEXT    NOT NULL,           -- English word, e.g. "anger", "love"
    source_list         TEXT,                       -- "High Confidence", "Missing Inner Being Words", etc.
    category_hint       TEXT,                       -- e.g. "Emotion", "Moral/Virtue"
    phase1_input_file   TEXT,                       -- source markdown file name
    phase1_status       TEXT,                       -- import/processing status
    phase1_output_file  TEXT,                       -- produced JSON file name
    phase2_datasets     REAL,
    notes               TEXT,
    -- M03: automation tracking
    automation_eligible INTEGER DEFAULT 1,          -- 0 = excluded from batch automation
    last_automation_run TEXT,                       -- ISO-8601 datetime of last successful run
    automation_run_id   TEXT,                       -- FK to engine_run_log.run_id
    phase1_term_count   INTEGER,                    -- number of terms found in phase1 output
    phase1_verse_count  INTEGER,                    -- number of verse records loaded
    -- M11: term discovery
    strongs_list        TEXT,                       -- JSON: [{"strong":"H5315","count":148}, …] sorted by count desc
    -- M12: word description
    description         TEXT,                       -- ~100-word researcher summary of the word's theological significance
    -- M13: registry metadata
    origin              TEXT,                       -- 'original_list' | 'programme_addition'
    dimensions          TEXT,                       -- comma-delimited multi-value dimension tags (renamed from source_category in M17)
    inference_note      TEXT,                       -- reasoning note for Low Confidence / Inferred words only (researcher-set only)
    -- M16: Session B / pipeline control
    session_b_status    TEXT,                       -- 'Verse Context Reset' | 'Ready for Analysis' | 'Pre-Analysis Complete' | 'Analysis Complete' | 'Session B Complete'
    cluster_assignment  TEXT    DEFAULT 'unassigned', -- C01–C22 cluster code
    sb_classification   TEXT    DEFAULT NULL,        -- inner-being standing classification (Claude AI)
    sb_classification_reasoning TEXT DEFAULT NULL,   -- reasoning for non-confirmed classifications (Claude AI)
    carry_forward       INTEGER DEFAULT 1,          -- 1 = include in future analysis rounds
    unique_term_count   INTEGER DEFAULT 0,          -- count of OWNER-only terms
    shared_term_count   INTEGER DEFAULT 0,          -- count of terms shared with other registries
    term_sharing_ratio  REAL    DEFAULT 0.0,         -- shared / (unique + shared)
    -- M18: Verse Context
    verse_context_status TEXT   DEFAULT NULL,         -- NULL | 'In Progress' | 'Complete'
    -- Dimension Review stamps (v1.7)
    dim_review_status   TEXT    DEFAULT NULL,          -- NULL | 'Complete'
    dim_review_version  TEXT    DEFAULT NULL            -- instruction version used for review
);

CREATE INDEX IF NOT EXISTS idx_wr_no         ON word_registry (no);
CREATE INDEX IF NOT EXISTS idx_wr_vc_status  ON word_registry (verse_context_status);
CREATE INDEX IF NOT EXISTS idx_wr_sb_status  ON word_registry (session_b_status);
CREATE INDEX IF NOT EXISTS idx_wr_cluster    ON word_registry (cluster_assignment);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 3 — WA FILE INDEX
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 3.1  wa_file_index ───────────────────────────────────────────────────────
-- One row per imported Session A JSON file (or file part).
-- All WA tables reference this via file_id FK.
CREATE TABLE IF NOT EXISTS wa_file_index (
    id                          INTEGER PRIMARY KEY AUTOINCREMENT,
    filename                    TEXT    NOT NULL,
    registry_id                 TEXT    NOT NULL,   -- matches word_registry.id (stored as TEXT)
    word_registry_fk            INTEGER REFERENCES word_registry(id),
    word                        TEXT    NOT NULL,   -- English word, e.g. "anger"
    part_number                 INTEGER,            -- null for single-part words
    total_parts                 INTEGER,
    is_split                    INTEGER,            -- boolean 0/1
    schema_version              TEXT,
    phase                       TEXT,
    produced_date               TEXT,
    source_file                 TEXT,
    translation_used            TEXT,
    specification               TEXT,
    revision_note               TEXT,
    source_list                 TEXT,
    category                    TEXT,
    testament_coverage          TEXT,               -- "OT_only", "NT_only", "both"
    root_families_in_prior_parts TEXT,              -- JSON array of root family labels
    last_changed                TEXT    DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_wa_fi_reg  ON wa_file_index (registry_id);
CREATE INDEX IF NOT EXISTS idx_wa_fi_word ON wa_file_index (word);
CREATE INDEX IF NOT EXISTS idx_wa_fi_wrfk ON wa_file_index (word_registry_fk);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 4 — WA TERM DATA
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 4.1  wa_term_inventory ───────────────────────────────────────────────────
-- One row per term extracted from a Session A JSON file.
-- Holds all per-term metadata: glosses, meaning, occurrence counts, flags.
--
-- Note on step_search_flag: this column was removed 2026-03-16.
-- Its content was merged into status_note before dropping.
CREATE TABLE IF NOT EXISTS wa_term_inventory (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id                 INTEGER NOT NULL REFERENCES wa_file_index(id),
    language                TEXT    NOT NULL,       -- "Hebrew" or "Greek"
    term_id                 TEXT    NOT NULL,       -- STEP internal code, e.g. "H8441", "G0026"
    strongs_number          TEXT,                   -- canonical Strong's number (may differ from term_id)
    transliteration         TEXT    NOT NULL,       -- e.g. "to.e.vah", "a.ga.pe"
    step_search_gloss       TEXT,                   -- English label from STEP search heading
    word_analysis_gloss     TEXT,                   -- gloss from STEP word analysis block
    occurrence_count        INTEGER,
    occurrence_count_qualifier TEXT,                -- "about", "exactly", etc.
    meaning                 TEXT,                   -- full meaning block, multi-line
    meaning_numbered        TEXT,                   -- same content, semicolon/pipe-delimited
    also_spelled            TEXT,                   -- alternate spelling / Strong's variant (JSON)
    lsj_entry               TEXT,                   -- Greek only: full LSJ lexicon text
    testament               TEXT,                   -- "OT", "NT", or "both"
    god_as_subject          INTEGER DEFAULT 0,      -- boolean: term applied to God/Holy Spirit
    somatic_link            INTEGER DEFAULT 0,      -- boolean: inner state linked to bodily expression
    causative_form_present  INTEGER DEFAULT 0,      -- boolean: Hiphil/Piel (Heb) or causative sense present
    status_note             TEXT,                   -- import-time researcher notes and flags (merged from step_search_flag 2026-03-16)
    last_changed            TEXT    DEFAULT (datetime('now')),
    -- M04: meaning parsing linkage
    short_def_mounce        TEXT,                   -- short definition from Mounce lexicon
    parsed_meaning_id       INTEGER,                -- FK to wa_meaning_parsed.id (set after M06 parse)
    -- M12: ownership and soft-delete
    delete_flagged          INTEGER DEFAULT 0,      -- soft-delete flag (XREF verses delete_flagged)
    -- M16: Session B classification
    evidential_status       TEXT    DEFAULT NULL,    -- confirmed | plausible | uncertain | instrumental | relational_only
    retention_note          TEXT    DEFAULT NULL,    -- reasoning for non-confirmed terms
    term_owner_type         TEXT    DEFAULT NULL     -- 'OWNER' | 'XREF'
);

CREATE INDEX IF NOT EXISTS idx_wa_ti_file    ON wa_term_inventory (file_id);
CREATE INDEX IF NOT EXISTS idx_wa_ti_strongs ON wa_term_inventory (strongs_number);
CREATE INDEX IF NOT EXISTS idx_wa_ti_id      ON wa_term_inventory (term_id);
CREATE INDEX IF NOT EXISTS idx_wa_ti_lang    ON wa_term_inventory (language);
CREATE INDEX IF NOT EXISTS idx_wa_ti_owner   ON wa_term_inventory (term_owner_type, delete_flagged);
CREATE INDEX IF NOT EXISTS idx_wa_ti_strongs_owner ON wa_term_inventory (strongs_number, term_owner_type, delete_flagged);

-- ── 4.2  wa_term_related_words ────────────────────────────────────────────────
-- Related words cluster for each term (from the STEP word analysis block).
-- Columns root_language, root_gloss, note added 2026-03-17.
CREATE TABLE IF NOT EXISTS wa_term_related_words (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    term_inv_id       INTEGER NOT NULL REFERENCES wa_term_inventory(id),
    gloss             TEXT,
    transliteration   TEXT,
    strongs_number    TEXT,              -- e.g. "H7965", "G1515"
    relationship_note TEXT               -- brief note on how this word relates to the term
);

CREATE INDEX IF NOT EXISTS idx_wa_rw ON wa_term_related_words (term_inv_id);

-- ── 4.3  wa_term_root_family ──────────────────────────────────────────────────
-- Root family labels assigned to each term (may span multiple families).
-- Columns root_language, root_gloss, note added 2026-03-17.
CREATE TABLE IF NOT EXISTS wa_term_root_family (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    term_inv_id   INTEGER NOT NULL REFERENCES wa_term_inventory(id),
    root_code     TEXT    NOT NULL,                -- e.g. "TSR", "CHARAH", "LUPE"
    root_language TEXT,                            -- "Hebrew", "Greek", "Aramaic"
    root_gloss    TEXT,                            -- brief English gloss for the root
    note          TEXT                             -- any additional note about this root membership
);

CREATE INDEX IF NOT EXISTS idx_wa_rf ON wa_term_root_family (term_inv_id);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 5 — PHASE-2 FLAGS  (shared by WA and MTI)
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 5.1  phase2_flag_types ───────────────────────────────────────────────────
-- Lookup table for Phase 2 analytical flags.
-- Consolidated 2026-03-16 from wa_phase2_flag_types (12 codes) + mti_phase2_flags (1 code)
-- + SOMATIC_EXPRESSION (moved from quality flags).  14 codes total.
--
-- Both wa_term_phase2_flags and mti_term_flags FK to this single table.
CREATE TABLE IF NOT EXISTS phase2_flag_types (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    flag_code   TEXT    NOT NULL UNIQUE,           -- e.g. "GOD_AS_SUBJECT", "SOMATIC_INNER_LINK"
    description TEXT
);

-- ── 5.2  wa_term_phase2_flags ─────────────────────────────────────────────────
-- Junction: WA inventory term ↔ phase2_flag_types (many-to-many).
CREATE TABLE IF NOT EXISTS wa_term_phase2_flags (
    term_inv_id INTEGER NOT NULL REFERENCES wa_term_inventory(id),
    flag_id     INTEGER NOT NULL REFERENCES phase2_flag_types(id),
    PRIMARY KEY (term_inv_id, flag_id)
);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 6 — WA QUALITY FLAGS
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 6.1  wa_quality_flag_types ───────────────────────────────────────────────
-- Two-level lookup: flag_group / flag_code.
-- Created 2026-03-16.  25 codes across 4 groups (22 original + 3 added by M02):
--   DATA_COVERAGE (8): NO_VERSES, THIN_DATA, SMALL_VERSE_SAMPLE, NO_WORD_ANALYSIS,
--                      UNCERTAIN_MEANING, ARAMAIC_EQUIVALENT,
--                      SPAN_RESOLUTION_CONFLICT, SPAN_FILTER_APPLIED
--   IMPORT_STATUS (8): STRONGS_RECONCILED, OCCURRENCE_COUNT_MISMATCH,
--                      FORMAT_ERROR_IN_SOURCE, FORMAT_ISSUE_RESOLVED, PARSE_ERROR,
--                      TERMS_IN_HEADER_NOT_IN_STEP, DUPLICATE_IN_SOURCE, DUPLICATE_RESOLVED
--   TERM_ANALYSIS (5): CONSOLIDATION_CANDIDATE, MULTI_SENSE_ENTRY, CROSS_REGISTRY,
--                      CROSS_PART_ROOT, PERIPHERAL_TERM
--   NOTE (4):          NOTE, NOTE_ON_ROOT_FAMILY, ANOMALY_NOTE, SPAN_BACK_POPULATED
CREATE TABLE IF NOT EXISTS wa_quality_flag_types (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    flag_group  TEXT    NOT NULL,                  -- "DATA_COVERAGE", "IMPORT_STATUS", "TERM_ANALYSIS", "NOTE"
    flag_code   TEXT    NOT NULL UNIQUE,
    description TEXT
);

-- ── 6.2  wa_data_quality_flags ────────────────────────────────────────────────
-- One row per quality flag raised against a file/term combination.
-- Normalised 2026-03-16: free-text flag column replaced by flag_id FK.
-- Slash-combined flag rows were split into separate rows during migration.
CREATE TABLE IF NOT EXISTS wa_data_quality_flags (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id     INTEGER NOT NULL REFERENCES wa_file_index(id),
    term_id     TEXT,                              -- Strong's/STEP code of the flagged term
    flag_id     INTEGER NOT NULL REFERENCES wa_quality_flag_types(id),
    description TEXT,
    last_changed TEXT
);

CREATE INDEX IF NOT EXISTS idx_wdqf_file ON wa_data_quality_flags (file_id);
CREATE INDEX IF NOT EXISTS idx_wdqf_flag ON wa_data_quality_flags (flag_id);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 7 — WA CROSS-REGISTRY LINKS
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 7.1  wa_crosslink_type ───────────────────────────────────────────────────
-- Lookup for cross-registry connection types.
-- Created 2026-03-16.  7 codes:
--   SHARED_TERM, SEMANTIC_OVERLAP, SHARED_ROOT, SHARED_VERSE,
--   THEOLOGICAL, CO_OCCURRENCE, SEMANTIC_OPPOSITION
CREATE TABLE IF NOT EXISTS wa_crosslink_type (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    type_code   TEXT    NOT NULL UNIQUE,
    description TEXT
);

-- ── 7.2  wa_cross_registry_links ─────────────────────────────────────────────
-- Links between word registry entries discovered during Phase 1 extraction.
-- Normalised 2026-03-16:
--   connection_type TEXT  →  connection_type_id INTEGER FK → wa_crosslink_type
--   linked_registry_id TEXT → INTEGER nullable FK → word_registry
-- 7 rows have linked_registry_id = NULL (composite or unresolvable names).
CREATE TABLE IF NOT EXISTS wa_cross_registry_links (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id             INTEGER NOT NULL REFERENCES wa_file_index(id),
    linked_word         TEXT,                      -- English word as captured in source
    linked_registry_id  INTEGER REFERENCES word_registry(id),  -- nullable: resolved where possible
    connection_type_id  INTEGER NOT NULL REFERENCES wa_crosslink_type(id),
    connecting_term     TEXT,                      -- transliterated Hebrew/Greek term text
    note                TEXT,
    last_changed        TEXT
);

CREATE INDEX IF NOT EXISTS idx_wa_xrl_file   ON wa_cross_registry_links (file_id);
CREATE INDEX IF NOT EXISTS idx_wa_xrl_linked ON wa_cross_registry_links (linked_registry_id);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 8 — WA VERSE RECORDS
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 8.1  wa_verse_records ────────────────────────────────────────────────────
-- CORE RESEARCH TABLE.
-- One row per term occurrence in a verse (sourced from STEP Bible Word Analysis).
-- A single verse may appear multiple times if multiple terms from that verse are studied.
--
-- IMPORT WORKFLOW:
--   1. Populate: file_id, term_inv_id, term_id, transliteration,
--                translation, reference, testament, verse_text
--   2. Call resolve_verse_refs(conn) — derives book_id, chapter, verse_num
--      from reference via book_code_variants.
--
-- note and claude_output are populated through ongoing research.
CREATE TABLE IF NOT EXISTS wa_verse_records (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id         INTEGER NOT NULL REFERENCES wa_file_index(id),
    term_inv_id     INTEGER REFERENCES wa_term_inventory(id),
    term_id         TEXT,                          -- Strong's / STEP code, e.g. "H8441", "G26"
    transliteration TEXT,                          -- e.g. "to.e.vah", "a.ga.pe"
    book_id         INTEGER REFERENCES books(id),  -- derived via resolve_verse_refs()
    reference       TEXT,                          -- STEP reference as imported, e.g. "Gen 43:32"
    chapter         INTEGER,                       -- derived from reference
    verse_num       INTEGER,                       -- derived from reference
    testament       TEXT,                          -- "OT" or "NT"
    translation     TEXT    NOT NULL DEFAULT 'ESV',
    verse_text      TEXT,
    note            TEXT,                          -- research annotation / analysis
    claude_output   TEXT,                          -- raw Claude response (JSON string)
    last_changed    TEXT    DEFAULT (datetime('now')),
    created_at      TEXT,
    updated_at      TEXT,                          -- maintained by trigger below
    -- M05: span filter and context
    target_word       TEXT,                        -- exact surface word matched in this verse
    span_strong_match INTEGER,                     -- 1 = Strong's confirmed in verse span; 0 = absent; NULL = unchecked
    context_before    TEXT,                        -- ~5 words before target_word
    context_after     TEXT                         -- ~5 words after target_word
);

-- Trigger: keep updated_at current on every UPDATE
CREATE TRIGGER IF NOT EXISTS wa_verse_records_updated_at
AFTER UPDATE ON wa_verse_records
BEGIN
    UPDATE wa_verse_records
    SET updated_at = strftime('%Y-%m-%dT%H:%M:%S','now')
    WHERE id = NEW.id;
END;

CREATE INDEX IF NOT EXISTS idx_wavr_book_ch_v    ON wa_verse_records (book_id, chapter, verse_num);
CREATE INDEX IF NOT EXISTS idx_wavr_term_id      ON wa_verse_records (term_id);
CREATE INDEX IF NOT EXISTS idx_wavr_reference    ON wa_verse_records (reference);
CREATE INDEX IF NOT EXISTS idx_wa_vr_term        ON wa_verse_records (term_inv_id);

-- Composite: filters by file_id, sorts by term + canonical verse position.
-- Covers: WHERE file_id IN (...)  ORDER BY term_id, book_id, chapter, verse_num
CREATE INDEX IF NOT EXISTS idx_wavr_file_term_pos
    ON wa_verse_records (file_id, term_id, book_id, chapter, verse_num);
CREATE INDEX IF NOT EXISTS idx_wavr_term_del
    ON wa_verse_records (term_inv_id, delete_flagged);

-- ── 8.2  wa_verse_term_links ─────────────────────────────────────────────────
-- Junction table: many-to-many relationship between verse records and terms.
-- A verse that contains multiple soul-family terms gets one row per term.
-- The primary term_inv_id on wa_verse_records is kept for backward compatibility;
-- the full cross-reference lives here.
CREATE TABLE IF NOT EXISTS wa_verse_term_links (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    verse_id            INTEGER NOT NULL REFERENCES wa_verse_records(id) ON DELETE CASCADE,
    term_inv_id         INTEGER NOT NULL REFERENCES wa_term_inventory(id) ON DELETE CASCADE,
    step_subgloss_code  TEXT,       -- e.g. 'H5315H'
    step_subgloss_label TEXT,       -- e.g. 'soul: life'
    span_strong_match   INTEGER,    -- 1 = target_word confirmed in span, NULL = unconfirmed
    target_word         TEXT,       -- English word(s) in the tagged span
    created_at          TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now')),
    UNIQUE (verse_id, term_inv_id)
);

CREATE INDEX IF NOT EXISTS idx_vtl_verse ON wa_verse_term_links (verse_id);
CREATE INDEX IF NOT EXISTS idx_vtl_term  ON wa_verse_term_links (term_inv_id);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 9 — MTI TABLES
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 9.1  mti_terms ───────────────────────────────────────────────────────────
-- MTI (Mounce Term Index) extracted terms.
-- One row per term per word studied.
CREATE TABLE IF NOT EXISTS mti_terms (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    strongs_number      TEXT,                      -- nullable; not unique (sub-entries share root)
    transliteration     TEXT    NOT NULL,
    gloss               TEXT    NOT NULL,
    language            TEXT,
    owning_registry     TEXT,                      -- registry number of the parent word (text, legacy)
    owning_registry_fk  INTEGER REFERENCES word_registry(id),  -- M12: integer FK to word_registry.id
    owning_word         TEXT,                      -- English word this term belongs to
    owning_part         TEXT,                      -- part number (raw: '1', 'Part1', 1, null)
    word_data_reference TEXT,                      -- future FK to wa_file_index
    word_data_ref_fk    INTEGER REFERENCES wa_file_index(id),  -- M12: integer FK to wa_file_index.id
    status              TEXT,                      -- extracted | extracted_thin | delete | excluded | candidate_delete | NULL
    status_note         TEXT,
    exclusion_reason    TEXT,
    extraction_date     TEXT,
    strongs_reconciled  INTEGER DEFAULT 0,         -- boolean 0/1
    anchor_note         TEXT,
    last_changed        TEXT    DEFAULT (datetime('now')),
    delete_flagged      INTEGER DEFAULT 0          -- M12: soft-delete flag
);

CREATE INDEX IF NOT EXISTS idx_mti_terms_strongs  ON mti_terms (strongs_number);
CREATE INDEX IF NOT EXISTS idx_mti_terms_registry ON mti_terms (owning_registry);
CREATE INDEX IF NOT EXISTS idx_mti_terms_word     ON mti_terms (owning_word);
CREATE INDEX IF NOT EXISTS idx_mti_terms_status   ON mti_terms (status);
CREATE INDEX IF NOT EXISTS idx_mti_terms_reg_fk   ON mti_terms (owning_registry_fk);
CREATE INDEX IF NOT EXISTS idx_mti_status_del     ON mti_terms (status, delete_flagged);
CREATE INDEX IF NOT EXISTS idx_mti_strongs_status  ON mti_terms (strongs_number, status);

-- ── 9.2  mti_term_flags ──────────────────────────────────────────────────────
-- Junction: MTI term ↔ phase2_flag_types (many-to-many).
-- Shares phase2_flag_types lookup with wa_term_phase2_flags (Section 5).
CREATE TABLE IF NOT EXISTS mti_term_flags (
    mti_term_id INTEGER NOT NULL REFERENCES mti_terms(id),
    flag_id     INTEGER NOT NULL REFERENCES phase2_flag_types(id),
    PRIMARY KEY (mti_term_id, flag_id)
);

-- ── 9.3  mti_term_cross_refs ─────────────────────────────────────────────────
-- Cross-references from an MTI term to another word registry entry.
CREATE TABLE IF NOT EXISTS mti_term_cross_refs (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    mti_term_id         INTEGER NOT NULL REFERENCES mti_terms(id),
    registry            TEXT    NOT NULL,
    word                TEXT,
    part                TEXT,                      -- raw as-imported (mixed types)
    word_data_reference TEXT,                      -- future FK to wa_file_index
    UNIQUE (mti_term_id, registry, word, part)
);

CREATE INDEX IF NOT EXISTS idx_cross_refs_term_id  ON mti_term_cross_refs (mti_term_id);
CREATE INDEX IF NOT EXISTS idx_cross_refs_registry ON mti_term_cross_refs (registry, word);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 10 — ENGINE CONTROL & RUN TRACKING  (M02)
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 10.1  engine_run_log ─────────────────────────────────────────────────────
-- One row per engine run (NEW_WORD, AUDIT_WORD, GAP_FILL, BULK).
-- run_id is a UUID string generated at run start.
CREATE TABLE IF NOT EXISTS engine_run_log (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id                TEXT    NOT NULL UNIQUE,
    mode                  TEXT    NOT NULL,            -- "NEW_WORD", "AUDIT_WORD", "GAP_FILL", "BULK"
    target_registry_ids   TEXT,                        -- JSON array of registry ids targeted
    started_at            TEXT    NOT NULL,
    completed_at          TEXT,
    outcome               TEXT,                        -- "complete", "stopped", "error"
    words_attempted       INTEGER DEFAULT 0,
    words_complete        INTEGER DEFAULT 0,
    words_stopped         INTEGER DEFAULT 0,
    total_terms_new       INTEGER DEFAULT 0,
    total_terms_xref      INTEGER DEFAULT 0,
    total_verses_inserted INTEGER DEFAULT 0,
    total_verses_filtered INTEGER DEFAULT 0,
    total_meanings_parsed INTEGER DEFAULT 0,
    error_detail          TEXT,
    resume_from           TEXT                         -- registry_id to resume from after interruption
);

-- ── 10.2  engine_stream_checkpoint ───────────────────────────────────────────
-- Tracks progress of individual data streams within a run.
CREATE TABLE IF NOT EXISTS engine_stream_checkpoint (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id           TEXT    NOT NULL REFERENCES engine_run_log(run_id),
    stream_name      TEXT    NOT NULL,
    status           TEXT    NOT NULL DEFAULT 'pending',
    last_registry_id TEXT,
    last_strong      TEXT,
    rows_written     INTEGER DEFAULT 0,
    rows_filtered    INTEGER DEFAULT 0,
    error_detail     TEXT,
    started_at       TEXT,
    completed_at     TEXT
);

-- ── 10.3  word_run_state ─────────────────────────────────────────────────────
-- One row per word per run: tracks per-word outcome and researcher approval.
CREATE TABLE IF NOT EXISTS word_run_state (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id              TEXT    NOT NULL REFERENCES engine_run_log(run_id),
    registry_id         TEXT    NOT NULL,
    word                TEXT    NOT NULL,
    phase_reached       TEXT,
    audit_result        TEXT,
    audit_detail        TEXT,
    stop_reason         TEXT,
    researcher_approved INTEGER DEFAULT 0,
    approved_by         TEXT,
    approved_at         TEXT
);

-- ── 10.4  term_fetch_log ─────────────────────────────────────────────────────
-- One row per Strong's number fetched during a run.
-- Records STEP API call outcomes and span filter statistics.
CREATE TABLE IF NOT EXISTS term_fetch_log (
    id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id               TEXT    NOT NULL REFERENCES engine_run_log(run_id),
    registry_id          TEXT    NOT NULL,
    strongs_input        TEXT    NOT NULL,
    strongs_resolved     TEXT,
    suffix_resolution    INTEGER DEFAULT 0,
    vocab_status         TEXT,
    verse_status         TEXT,
    verse_count_fetched  INTEGER DEFAULT 0,
    verse_count_stored   INTEGER DEFAULT 0,
    verse_count_filtered INTEGER DEFAULT 0,
    span_conflict        INTEGER DEFAULT 0,
    api_warnings         TEXT,
    fetched_at           TEXT
);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 11 — MEANING PARSING  (M06–M09)
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 11.1  wa_meaning_parsed ──────────────────────────────────────────────────
-- One row per parsed wa_term_inventory entry (1:1 with term).
-- Parent record for wa_meaning_sense and wa_meaning_stem rows.
CREATE TABLE IF NOT EXISTS wa_meaning_parsed (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    term_inv_id         INTEGER NOT NULL UNIQUE REFERENCES wa_term_inventory(id),
    strongs_number      TEXT    NOT NULL,
    language            TEXT    NOT NULL,
    top_sense_count     INTEGER DEFAULT 0,
    stem_count          INTEGER DEFAULT 0,
    has_causative_stem  INTEGER DEFAULT 0,
    has_domain_tags     INTEGER DEFAULT 0,
    parsed_at           TEXT    NOT NULL,
    parse_version       TEXT    NOT NULL,
    parse_warnings      TEXT
);

CREATE INDEX IF NOT EXISTS idx_meaning_parsed_term_inv ON wa_meaning_parsed (term_inv_id);

-- ── 11.2  wa_meaning_sense ───────────────────────────────────────────────────
-- Hierarchical sense entries parsed from a term's meaning block.
-- sort_order preserves the original parse order within the meaning text.
CREATE TABLE IF NOT EXISTS wa_meaning_sense (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    parsed_meaning_id  INTEGER NOT NULL REFERENCES wa_meaning_parsed(id),
    level_code         TEXT    NOT NULL,
    level_depth        INTEGER NOT NULL,
    parent_level_code  TEXT,
    sense_text         TEXT,
    is_stem_label      INTEGER DEFAULT 0,
    stem_label         TEXT,
    domain_tag         TEXT,
    sort_order         INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_meaning_sense_parsed ON wa_meaning_sense (parsed_meaning_id);
CREATE INDEX IF NOT EXISTS idx_meaning_sense_level  ON wa_meaning_sense (parsed_meaning_id, level_code);

-- ── 11.3  wa_meaning_stem ────────────────────────────────────────────────────
-- Stem-level summary for Hebrew/Greek terms (Hiphil, Piel, causative, etc.).
CREATE TABLE IF NOT EXISTS wa_meaning_stem (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    parsed_meaning_id INTEGER NOT NULL REFERENCES wa_meaning_parsed(id),
    stem_name         TEXT    NOT NULL,
    stem_type         TEXT,
    sense_count       INTEGER DEFAULT 0,
    top_sense_text    TEXT
);

CREATE INDEX IF NOT EXISTS idx_meaning_stem_parsed ON wa_meaning_stem (parsed_meaning_id);

-- ── 11.4  wa_lsj_parsed ──────────────────────────────────────────────────────
-- Greek-only: structured fields parsed from the raw LSJ lexicon entry.
-- term_inv_id is UNIQUE — one parse record per term.
CREATE TABLE IF NOT EXISTS wa_lsj_parsed (
    id                     INTEGER PRIMARY KEY AUTOINCREMENT,
    term_inv_id            INTEGER NOT NULL UNIQUE REFERENCES wa_term_inventory(id),
    raw_lsj                TEXT,
    lsj_gloss              TEXT,
    lsj_domains            TEXT,
    lsj_philosophical_note TEXT,
    lsj_etymology_note     TEXT,
    lsj_cognate_forms      TEXT,
    parsed_at              TEXT    NOT NULL,
    parse_version          TEXT    NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_lsj_parsed_term ON wa_lsj_parsed (term_inv_id);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 12 — SCHEMA METADATA  (M01)
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 12.1  schema_version ─────────────────────────────────────────────────────
-- Single row (id=1) tracking the applied schema version and migration history.
-- version_code is updated by the final migration of each release group.
-- On a fresh --init-db this row should be seeded to the current version;
-- subsequent --migrate runs are then no-ops.
CREATE TABLE IF NOT EXISTS schema_version (
    id                 INTEGER PRIMARY KEY,
    version_code       TEXT    NOT NULL,            -- e.g. "3.8.0"
    applied_at         TEXT    NOT NULL,            -- ISO-8601 datetime of last update
    migration_history  TEXT,                        -- JSON array of applied migration refs
    engine_min_version TEXT                         -- minimum engine version required
);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 13 — SESSION RESEARCH FLAGS  (M13)
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 13.1  wa_session_research_flags ──────────────────────────────────────────
-- Cross-session research flags for Sessions B, C, and D findings.
-- flag_code: PH2_*, SB_FINDING, SB_DIMENSION, SB_INNER_BEING, SD_POINTER, SD_CLUSTER,
--            CANDIDATE_REGISTRY_WORD, VOLUME_LIMITATION
CREATE TABLE IF NOT EXISTS wa_session_research_flags (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    registry_id       INTEGER NOT NULL REFERENCES word_registry(id),
    file_id           INTEGER REFERENCES wa_file_index(id),
    flag_code         TEXT    NOT NULL,             -- structured code (see above)
    flag_label        TEXT    NOT NULL UNIQUE,      -- human-readable unique label
    strongs_reference TEXT,                         -- Strong's number(s) implicated
    cross_registry_id INTEGER REFERENCES word_registry(id),
    priority          TEXT    DEFAULT 'MEDIUM',     -- HIGH | MEDIUM | LOW
    session_target    TEXT    DEFAULT 'D',          -- B | C | D
    description       TEXT    NOT NULL,             -- full finding description
    session_raised    TEXT    NOT NULL,             -- session in which flag was raised
    raised_date       TEXT    NOT NULL,             -- ISO-8601
    resolved          INTEGER NOT NULL DEFAULT 0,
    resolved_date     TEXT,
    resolved_note     TEXT
);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 14 — SESSION B STRUCTURED  (M16)
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 14.1  wa_session_b_dimensions ────────────────────────────────────────────
-- Dimensional profile per registry — populated during Session B extraction.
CREATE TABLE IF NOT EXISTS wa_session_b_dimensions (
    id                          INTEGER PRIMARY KEY AUTOINCREMENT,
    registry_id                 INTEGER NOT NULL REFERENCES word_registry(id),
    file_id                     INTEGER REFERENCES wa_file_index(id),
    relational_environment      INTEGER DEFAULT 0,
    relational_environment_note TEXT,
    spirit_soul_body            INTEGER DEFAULT 0,
    spirit_soul_body_note       TEXT,
    inner_operations            INTEGER DEFAULT 0,
    inner_operations_note       TEXT,
    being                       INTEGER DEFAULT 0,
    being_note                  TEXT,
    raised_date                 TEXT    NOT NULL,   -- ISO-8601
    session_b_instruction       TEXT    NOT NULL    -- instruction version used
);

-- ── 14.2  wa_session_b_findings ──────────────────────────────────────────────
-- Key findings per registry — populated during Session B extraction.
CREATE TABLE IF NOT EXISTS wa_session_b_findings (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    finding_id            TEXT    NOT NULL UNIQUE,
    registry_id           INTEGER NOT NULL REFERENCES word_registry(id),
    file_id               INTEGER REFERENCES wa_file_index(id),
    finding_type          TEXT    NOT NULL,         -- finding category
    finding               TEXT    NOT NULL,         -- full finding text
    anchor_verses         TEXT,                     -- supporting verse references
    raised_date           TEXT    NOT NULL,         -- ISO-8601
    session_b_instruction TEXT    NOT NULL          -- instruction version used
);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 15 — SESSION D  (M16)
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 15.1  session_d_runs ─────────────────────────────────────────────────────
-- Session D run metadata and scope.
CREATE TABLE IF NOT EXISTS session_d_runs (
    id                          INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id                      TEXT    NOT NULL UNIQUE,
    run_date                    TEXT    NOT NULL,
    cluster_ref                 TEXT,               -- cluster(s) in scope
    registries_in_scope         TEXT    NOT NULL,   -- JSON array of registry ids
    registries_completed_at_run INTEGER,
    session_b_sources           TEXT,               -- Session B input files used
    run_summary                 TEXT,
    json_filename               TEXT
);

-- ── 15.2  session_d_verse_links ──────────────────────────────────────────────
-- Cross-registry verse-level linkages discovered in Session D.
CREATE TABLE IF NOT EXISTS session_d_verse_links (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id          TEXT    NOT NULL,
    verse_ref       TEXT    NOT NULL,
    registry_ids    TEXT    NOT NULL,               -- JSON array of registry ids sharing this verse
    terms_involved  TEXT,                           -- Strong's numbers at this verse
    overlap_count   INTEGER,
    threshold_met   INTEGER DEFAULT 0,
    gate            TEXT    NOT NULL,               -- gate classification
    raised_date     TEXT    NOT NULL
);

-- ── 15.3  session_d_term_links ───────────────────────────────────────────────
-- Cross-registry term-level linkages discovered in Session D.
CREATE TABLE IF NOT EXISTS session_d_term_links (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id            TEXT    NOT NULL,
    strongs_id        TEXT    NOT NULL,
    transliteration   TEXT,
    registry_data     TEXT    NOT NULL,             -- JSON: registries where this term appears
    status_divergence INTEGER DEFAULT 0,           -- 1 = status differs across registries
    gate              TEXT    NOT NULL,
    raised_date       TEXT    NOT NULL
);

-- ── 15.4  session_d_observations ─────────────────────────────────────────────
-- Structural observations from Session D synthesis.
CREATE TABLE IF NOT EXISTS session_d_observations (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id                TEXT    NOT NULL,
    observation_id        TEXT    NOT NULL UNIQUE,
    observation_type      TEXT    NOT NULL,
    registries_implicated TEXT    NOT NULL,
    terms_implicated      TEXT,
    structural_note       TEXT,
    source_refs           TEXT,
    gate                  TEXT    NOT NULL,
    researcher_flag       INTEGER DEFAULT 0,
    raised_date           TEXT    NOT NULL
);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 16 — VERSE CONTEXT  (M18)
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 16.1  verse_context_group ────────────────────────────────────────────────
-- Contextual meaning groups per term. Each group describes one way a term
-- engages the inner being across its verse corpus.
-- Populated by Claude AI classification → VERSECONTEXT patches.
CREATE TABLE IF NOT EXISTS verse_context_group (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    mti_term_id         INTEGER NOT NULL REFERENCES mti_terms(id),
    group_code          TEXT    NOT NULL UNIQUE,    -- '{mti_term_id}-{serial}', e.g. '235-001'
    context_description TEXT    NOT NULL,           -- brief inner-being engagement description
    notes               TEXT    DEFAULT NULL,
    delete_flagged      INTEGER DEFAULT 0,          -- 0 = active; 1 = dissolved
    vertical_pass_flag  INTEGER DEFAULT 0           -- 0 = not analysed; 1 = vertical pass complete
);

CREATE INDEX IF NOT EXISTS idx_vcg_mti ON verse_context_group (mti_term_id);

-- ── 16.2  verse_context ──────────────────────────────────────────────────────
-- Per-verse classification: relevance, group assignment, anchor/related status.
-- One row per verse per term per group (dual-context = 2 rows, different groups).
-- UNIQUE on (verse_record_id, mti_term_id, group_id).
CREATE TABLE IF NOT EXISTS verse_context (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    verse_record_id  INTEGER NOT NULL REFERENCES wa_verse_records(id),
    mti_term_id      INTEGER NOT NULL REFERENCES mti_terms(id),
    group_id         INTEGER REFERENCES verse_context_group(id),  -- NULL if is_relevant = 0
    is_anchor        INTEGER NOT NULL DEFAULT 0,   -- 1 = anchor verse for its group
    is_relevant      INTEGER NOT NULL DEFAULT 0,   -- 0 = set aside; 1 = inner-being relevant
    is_related       INTEGER NOT NULL DEFAULT 0,   -- 1 = shares group meaning with anchor
    notes            TEXT    DEFAULT NULL,          -- dual-context flags, borderline notes
    delete_flagged   INTEGER DEFAULT 0,
    vertical_pass_flag INTEGER DEFAULT 0,          -- 0 = not analysed; 1 = vertical pass complete
    set_aside_reason TEXT    DEFAULT NULL,          -- no_inner_being | wrong_face | divine_subject | avf_homograph | pending_revision
    UNIQUE (verse_record_id, mti_term_id, group_id)
);

CREATE INDEX IF NOT EXISTS idx_vc_vr        ON verse_context (verse_record_id);
CREATE INDEX IF NOT EXISTS idx_vc_mti       ON verse_context (mti_term_id);
CREATE INDEX IF NOT EXISTS idx_vc_mti_del   ON verse_context (mti_term_id, delete_flagged);
CREATE INDEX IF NOT EXISTS idx_vc_grp       ON verse_context (group_id);
CREATE INDEX IF NOT EXISTS idx_vc_grp_anchor ON verse_context (group_id, is_anchor, delete_flagged);

-- Logical consistency rules (enforced by application, not constraints):
--   R1: is_relevant = 0 → group_id IS NULL, is_anchor = 0, is_related = 0
--   R2: is_anchor = 1  → is_relevant = 1, is_related = 0, group_id NOT NULL
--   R3: is_related = 1 → is_relevant = 1, group_id references a group with at least one active anchor
--   R4: Every term must have at least one active anchor before Session B may proceed

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 17 — DIMENSION INDEX
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 17.1  wa_dimension_index ─────────────────────────────────────────────────
-- Denormalized index of verse_context_group records with theological dimension
-- classification. Populated by scripts/populate_dimension_index.py.
-- dimension field: classified by Claude AI or mechanical keyword matching.
CREATE TABLE IF NOT EXISTS wa_dimension_index (
    id                       INTEGER PRIMARY KEY AUTOINCREMENT,
    verse_context_group_id   INTEGER NOT NULL REFERENCES verse_context_group(id),
    mti_term_id              INTEGER NOT NULL REFERENCES mti_terms(id),
    strongs_number           TEXT    NOT NULL,
    transliteration          TEXT,
    gloss                    TEXT,
    language                 TEXT,
    owning_registry_no       INTEGER NOT NULL,
    owning_registry_word     TEXT    NOT NULL,
    cluster_assignment       TEXT,
    group_code               TEXT    NOT NULL,
    context_description      TEXT    NOT NULL,
    dimension                TEXT,                  -- one of 14 controlled values (see populate script) or NULL
    dimension_confidence     TEXT    DEFAULT NULL,  -- KEYWORD_STRONG | KEYWORD_WEAK | CLAUDE_AI | UNCLASSIFIED
    manual_override          INTEGER DEFAULT 0,     -- 1 = researcher override, preserved on repopulate
    notes                    TEXT    DEFAULT NULL,
    last_modified            TEXT    DEFAULT NULL,
    anchor_count             INTEGER DEFAULT 0,
    related_count            INTEGER DEFAULT 0,
    set_aside_count          INTEGER DEFAULT 0,
    total_verse_count        INTEGER DEFAULT 0,
    delete_flagged           INTEGER DEFAULT 0,
    dominant_subject         TEXT    DEFAULT NULL     -- GOD | HUMAN | OTHER_HUMAN | UNSEEN | NONE — assigned during Dimension Review
);

CREATE INDEX IF NOT EXISTS idx_wdi_vcg ON wa_dimension_index (verse_context_group_id);
CREATE INDEX IF NOT EXISTS idx_wdi_dim ON wa_dimension_index (dimension);

-- ═════════════════════════════════════════════════════════════════════════════
-- SECTION 18 — DIMENSION REVIEW CLUSTER LOG  (v1.7)
-- ═════════════════════════════════════════════════════════════════════════════

-- ── 18.1  wa_dim_review_cluster_log ──────────────────────────────────────────
-- One row per cluster when Dimension Review is complete.
-- Session B gates on this table containing a record for the cluster.
CREATE TABLE IF NOT EXISTS wa_dim_review_cluster_log (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    cluster             TEXT    NOT NULL UNIQUE,
    completed_date      TEXT    NOT NULL,
    instruction_version TEXT    NOT NULL,
    registry_count      INTEGER NOT NULL DEFAULT 0,
    group_count         INTEGER NOT NULL DEFAULT 0,
    anchored_count      INTEGER NOT NULL DEFAULT 0,
    notes               TEXT,
    last_modified       TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now'))
);


