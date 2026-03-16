-- ─────────────────────────────────────────────────────────────────────────────
-- Bible_Projects – SQLite Schema
-- File:   data/schema/create_tables.sql
-- Last updated: 2026-03-16
-- Run via: python analytics/bible_analytics.py --init-db
--          OR: python -c "from analytics.db_client import get_connection, init_schema_from_file; conn=get_connection(); init_schema_from_file(conn); conn.close()"
--
-- Table groups:
--   Section 1  — Reference tables:       books, book_code_variants, themes, sources
--   Section 2  — Registry:               word_registry
--   Section 3  — WA file index:          wa_file_index
--   Section 4  — WA term data:           wa_term_inventory, wa_term_related_words, wa_term_root_family
--   Section 5  — Phase-2 flags (shared): phase2_flag_types, wa_term_phase2_flags
--   Section 6  — WA quality flags:       wa_quality_flag_types, wa_data_quality_flags
--   Section 7  — WA cross-registry:      wa_crosslink_type, wa_cross_registry_links
--   Section 8  — WA verse records:       wa_verse_records
--   Section 9  — MTI tables:             mti_terms, mti_term_flags, mti_term_cross_refs
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
    notes               TEXT
);

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
    last_changed            TEXT    DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_wa_ti_file    ON wa_term_inventory (file_id);
CREATE INDEX IF NOT EXISTS idx_wa_ti_strongs ON wa_term_inventory (strongs_number);
CREATE INDEX IF NOT EXISTS idx_wa_ti_id      ON wa_term_inventory (term_id);
CREATE INDEX IF NOT EXISTS idx_wa_ti_lang    ON wa_term_inventory (language);

-- ── 4.2  wa_term_related_words ────────────────────────────────────────────────
-- Related words cluster for each term (from the STEP word analysis block).
CREATE TABLE IF NOT EXISTS wa_term_related_words (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    term_inv_id     INTEGER NOT NULL REFERENCES wa_term_inventory(id),
    gloss           TEXT,
    transliteration TEXT
);

CREATE INDEX IF NOT EXISTS idx_wa_rw ON wa_term_related_words (term_inv_id);

-- ── 4.3  wa_term_root_family ──────────────────────────────────────────────────
-- Root family labels assigned to each term (may span multiple families).
CREATE TABLE IF NOT EXISTS wa_term_root_family (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    term_inv_id INTEGER NOT NULL REFERENCES wa_term_inventory(id),
    root_code   TEXT    NOT NULL                   -- e.g. "TSR", "CHARAH", "LUPE"
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
-- Created 2026-03-16.  22 codes across 4 groups:
--   DATA_COVERAGE (6): NO_VERSES, THIN_DATA, SMALL_VERSE_SAMPLE, NO_WORD_ANALYSIS,
--                      UNCERTAIN_MEANING, ARAMAIC_EQUIVALENT
--   IMPORT_STATUS (8): STRONGS_RECONCILED, OCCURRENCE_COUNT_MISMATCH,
--                      FORMAT_ERROR_IN_SOURCE, FORMAT_ISSUE_RESOLVED, PARSE_ERROR,
--                      TERMS_IN_HEADER_NOT_IN_STEP, DUPLICATE_IN_SOURCE, DUPLICATE_RESOLVED
--   TERM_ANALYSIS (5): CONSOLIDATION_CANDIDATE, MULTI_SENSE_ENTRY, CROSS_REGISTRY,
--                      CROSS_PART_ROOT, PERIPHERAL_TERM
--   NOTE (3):          NOTE, NOTE_ON_ROOT_FAMILY, ANOMALY_NOTE
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
    updated_at      TEXT                           -- maintained by trigger below
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
    owning_registry     TEXT,                      -- registry number of the parent word
    owning_word         TEXT,                      -- English word this term belongs to
    owning_part         TEXT,                      -- part number (raw: '1', 'Part1', 1, null)
    word_data_reference TEXT,                      -- future FK to wa_file_index
    status              TEXT,
    status_note         TEXT,
    exclusion_reason    TEXT,
    extraction_date     TEXT,
    strongs_reconciled  INTEGER DEFAULT 0,         -- boolean 0/1
    anchor_note         TEXT,
    last_changed        TEXT    DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_mti_terms_strongs  ON mti_terms (strongs_number);
CREATE INDEX IF NOT EXISTS idx_mti_terms_registry ON mti_terms (owning_registry);
CREATE INDEX IF NOT EXISTS idx_mti_terms_word     ON mti_terms (owning_word);
CREATE INDEX IF NOT EXISTS idx_mti_terms_status   ON mti_terms (status);

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

