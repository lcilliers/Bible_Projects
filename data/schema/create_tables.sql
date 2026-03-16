-- ─────────────────────────────────────────────────────────────────────────────
-- Bible_Projects – SQLite Schema
-- File:   data/schema/create_tables.sql
-- Run via: python analytics/bible_analytics.py --init-db
--          OR: python -c "from analytics.db_client import get_connection, init_schema_from_file; conn=get_connection(); init_schema_from_file(conn); conn.close()"
-- ─────────────────────────────────────────────────────────────────────────────

PRAGMA foreign_keys = ON;

-- ── 1. books ─────────────────────────────────────────────────────────────────
-- Static reference table: one row per Bible book (66 rows).
CREATE TABLE IF NOT EXISTS books (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,           -- e.g. "John"
    abbreviation TEXT   NOT NULL UNIQUE,           -- e.g. "Jn"
    testament   TEXT    NOT NULL                   -- "OT" or "NT"
                CHECK (testament IN ('OT', 'NT')),
    book_order  INTEGER NOT NULL UNIQUE            -- canonical order 1–66
);

-- ── 2. themes ────────────────────────────────────────────────────────────────
-- Research themes and topic tags used to classify verse notes.
CREATE TABLE IF NOT EXISTS themes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,           -- e.g. "salvation"
    description TEXT
);

-- ── 3. sources ───────────────────────────────────────────────────────────────
-- Reference sources: Zotero items, commentaries, lexicons, etc.
CREATE TABLE IF NOT EXISTS sources (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    zotero_key  TEXT    UNIQUE,                    -- Zotero item key (nullable)
    title       TEXT    NOT NULL,
    author      TEXT,
    year        INTEGER,
    source_type TEXT                               -- "commentary", "lexicon", "paper", etc.
);

-- ── 4. verse_notes ───────────────────────────────────────────────────────────
-- MAIN RESEARCH TABLE. One row per annotated verse (expected ~20 000 rows).
-- New records are added via JSON imports from Claude.
CREATE TABLE IF NOT EXISTS verse_notes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id     INTEGER NOT NULL REFERENCES books(id),
    chapter     INTEGER NOT NULL CHECK (chapter >= 1),
    verse       INTEGER NOT NULL CHECK (verse >= 1),
    translation TEXT    NOT NULL DEFAULT 'ESV',    -- e.g. "ESV", "NIV", "KJV"
    original_text TEXT,                            -- Hebrew / Greek source text
    note        TEXT,                              -- Research annotation / analysis
    claude_output TEXT,                            -- Raw Claude response (JSON string)
    created_at  TEXT    NOT NULL                   -- ISO-8601, e.g. "2026-01-15T10:30:00"
                DEFAULT (strftime('%Y-%m-%dT%H:%M:%S', 'now')),
    updated_at  TEXT    NOT NULL
                DEFAULT (strftime('%Y-%m-%dT%H:%M:%S', 'now')),
    UNIQUE (book_id, chapter, verse, translation)  -- one note per verse per translation
);

-- Trigger: keep updated_at current on every UPDATE
CREATE TRIGGER IF NOT EXISTS verse_notes_updated_at
AFTER UPDATE ON verse_notes
BEGIN
    UPDATE verse_notes
    SET updated_at = strftime('%Y-%m-%dT%H:%M:%S', 'now')
    WHERE id = NEW.id;
END;

-- ── 5. verse_theme_map ───────────────────────────────────────────────────────
-- Many-to-many: verse_notes ↔ themes
CREATE TABLE IF NOT EXISTS verse_theme_map (
    verse_note_id INTEGER NOT NULL REFERENCES verse_notes(id) ON DELETE CASCADE,
    theme_id      INTEGER NOT NULL REFERENCES themes(id)      ON DELETE CASCADE,
    PRIMARY KEY (verse_note_id, theme_id)
);

-- ── 6. verse_source_map ──────────────────────────────────────────────────────
-- Many-to-many: verse_notes ↔ sources
CREATE TABLE IF NOT EXISTS verse_source_map (
    verse_note_id INTEGER NOT NULL REFERENCES verse_notes(id)  ON DELETE CASCADE,
    source_id     INTEGER NOT NULL REFERENCES sources(id)      ON DELETE CASCADE,
    page_ref      TEXT,                                        -- optional page / section ref
    PRIMARY KEY (verse_note_id, source_id)
);

-- ── Indexes for common query patterns ────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_verse_notes_book    ON verse_notes (book_id);
CREATE INDEX IF NOT EXISTS idx_verse_notes_ref     ON verse_notes (book_id, chapter, verse);
CREATE INDEX IF NOT EXISTS idx_verse_notes_created ON verse_notes (created_at);
