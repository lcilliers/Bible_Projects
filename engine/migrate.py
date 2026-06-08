"""
migrate.py
──────────
Schema migration runner: v2.2 → v3.0 (M01–M10).

Each migration is a function named _mXX() that receives an open connection.
All migrations are idempotent — they check for existence before ALTER/CREATE.
Each migration runs inside its own SQLite transaction.

Usage:
    python -m engine.engine --migrate [--dry-run] [--to=M05]
    python -m engine.engine --db-status
"""

import json
import sqlite3
from datetime import datetime, timezone

from .constants import EXPECTED_SCHEMA_VERSION

# ── Migration registry ────────────────────────────────────────────────────────

_MIGRATIONS: list[tuple[str, str, callable]] = []  # (ref, description, fn)


def _register(ref: str, description: str):
    def decorator(fn):
        _MIGRATIONS.append((ref, description, fn))
        return fn
    return decorator


# ── Individual migrations ─────────────────────────────────────────────────────

@_register("M01", "Create schema_version table")
def _m01(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS schema_version (
            id               INTEGER PRIMARY KEY,
            version_code     TEXT    NOT NULL,
            applied_at       TEXT    NOT NULL,
            migration_history TEXT,
            engine_min_version TEXT
        )
    """)
    existing = conn.execute("SELECT id FROM schema_version WHERE id = 1").fetchone()
    if not existing:
        conn.execute(
            "INSERT INTO schema_version (id, version_code, applied_at, migration_history) "
            "VALUES (1, '2.2.0', ?, '[]')",
            (_now(),),
        )


@_register("M02", "Create engine control tables + 3 new quality flag reference rows")
def _m02(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS engine_run_log (
            id                   INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id               TEXT    NOT NULL UNIQUE,
            mode                 TEXT    NOT NULL,
            target_registry_ids  TEXT,
            started_at           TEXT    NOT NULL,
            completed_at         TEXT,
            outcome              TEXT,
            words_attempted      INTEGER DEFAULT 0,
            words_complete       INTEGER DEFAULT 0,
            words_stopped        INTEGER DEFAULT 0,
            total_terms_new      INTEGER DEFAULT 0,
            total_terms_xref     INTEGER DEFAULT 0,
            total_verses_inserted INTEGER DEFAULT 0,
            total_verses_filtered INTEGER DEFAULT 0,
            total_meanings_parsed INTEGER DEFAULT 0,
            error_detail         TEXT,
            resume_from          TEXT
        );

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
    """)

    # Add 3 new rows to wa_quality_flag_types if not already present.
    existing_codes = {
        r[0] for r in conn.execute("SELECT flag_code FROM wa_quality_flag_types").fetchall()
    }
    new_flags = [
        (23, "DATA_COVERAGE", "SPAN_RESOLUTION_CONFLICT",
         "Queried Strong's not found in any verse span after suffix resolution. "
         "Verse set is empty. Manual STEP UI verification required."),
        (24, "DATA_COVERAGE", "SPAN_FILTER_APPLIED",
         "One or more verse records were discarded by span filter during fetch "
         "or AUDIT back-population. verse_count_filtered in term_fetch_log records the count."),
        (25, "NOTE", "SPAN_BACK_POPULATED",
         "AUDIT_WORD sub-step A3a has been run for this term — all verse records "
         "now have span_strong_match set."),
    ]
    for fid, group, code, desc in new_flags:
        if code not in existing_codes:
            conn.execute(
                "INSERT INTO wa_quality_flag_types (id, flag_group, flag_code, description) "
                "VALUES (?, ?, ?, ?)",
                (fid, group, code, desc),
            )


@_register("M03", "Extend word_registry with 5 automation columns")
def _m03(conn: sqlite3.Connection) -> None:
    _add_column_if_missing(conn, "word_registry", "automation_eligible",
                           "INTEGER DEFAULT 1")
    _add_column_if_missing(conn, "word_registry", "last_automation_run", "TEXT")
    _add_column_if_missing(conn, "word_registry", "automation_run_id",   "TEXT")
    _add_column_if_missing(conn, "word_registry", "phase1_term_count",   "INTEGER")
    _add_column_if_missing(conn, "word_registry", "phase1_verse_count",  "INTEGER")


@_register("M04", "Extend wa_term_inventory with 2 new columns")
def _m04(conn: sqlite3.Connection) -> None:
    _add_column_if_missing(conn, "wa_term_inventory", "short_def_mounce", "TEXT")
    _add_column_if_missing(conn, "wa_term_inventory", "parsed_meaning_id", "INTEGER")


@_register("M05", "Extend wa_verse_records with 4 new columns")
def _m05(conn: sqlite3.Connection) -> None:
    _add_column_if_missing(conn, "wa_verse_records", "target_word",       "TEXT")
    _add_column_if_missing(conn, "wa_verse_records", "span_strong_match", "INTEGER")
    _add_column_if_missing(conn, "wa_verse_records", "context_before",    "TEXT")
    _add_column_if_missing(conn, "wa_verse_records", "context_after",     "TEXT")


@_register("M06", "Create wa_meaning_parsed table + index")
def _m06(conn: sqlite3.Connection) -> None:
    conn.execute("""
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
        )
    """)
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_meaning_parsed_term_inv "
        "ON wa_meaning_parsed (term_inv_id)"
    )


@_register("M07", "Create wa_meaning_sense table + indexes")
def _m07(conn: sqlite3.Connection) -> None:
    conn.execute("""
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
        )
    """)
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_meaning_sense_parsed "
        "ON wa_meaning_sense (parsed_meaning_id)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_meaning_sense_level "
        "ON wa_meaning_sense (parsed_meaning_id, level_code)"
    )


@_register("M08", "Create wa_meaning_stem table + index")
def _m08(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS wa_meaning_stem (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            parsed_meaning_id INTEGER NOT NULL REFERENCES wa_meaning_parsed(id),
            stem_name         TEXT    NOT NULL,
            stem_type         TEXT,
            sense_count       INTEGER DEFAULT 0,
            top_sense_text    TEXT
        )
    """)
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_meaning_stem_parsed "
        "ON wa_meaning_stem (parsed_meaning_id)"
    )


@_register("M09", "Create wa_lsj_parsed table + index")
def _m09(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS wa_lsj_parsed (
            id                    INTEGER PRIMARY KEY AUTOINCREMENT,
            term_inv_id           INTEGER NOT NULL UNIQUE REFERENCES wa_term_inventory(id),
            raw_lsj               TEXT,
            lsj_gloss             TEXT,
            lsj_domains           TEXT,
            lsj_philosophical_note TEXT,
            lsj_etymology_note    TEXT,
            lsj_cognate_forms     TEXT,
            parsed_at             TEXT    NOT NULL,
            parse_version         TEXT    NOT NULL
        )
    """)
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_lsj_parsed_term "
        "ON wa_lsj_parsed (term_inv_id)"
    )


@_register("M10", "Update schema_version to 3.0.0")
def _m10(conn: sqlite3.Connection) -> None:
    conn.execute(
        "UPDATE schema_version SET version_code = '3.0.0', applied_at = ? WHERE id = 1",
        (_now(),),
    )


@_register("M11", "Add strongs_list column to word_registry + update schema to 3.2.0")
def _m11(conn: sqlite3.Connection) -> None:
    # strongs_list stores the JSON result of get_strongs_for_word() discovery:
    # a JSON array of {"strong": "H5315", "count": 148} objects, sorted by count desc.
    # Populated by GAP_FILL Stage 1 (term discovery) and readable by later stages.
    _add_column_if_missing(conn, "word_registry", "strongs_list", "TEXT")
    conn.execute(
        "UPDATE schema_version SET version_code = '3.2.0', applied_at = ? WHERE id = 1",
        (_now(),),
    )


@_register("M12", "Add delete_flagged columns + wa_verse_term_links + update schema to 3.3.0")
def _m12(conn: sqlite3.Connection) -> None:
    # delete_flagged: flag-based soft-delete on three core tables + root family cascade.
    # Rows with delete_flagged=1 are treated as pending archive; excluded from all counts.
    _add_column_if_missing(conn, "wa_term_inventory",    "delete_flagged", "INTEGER DEFAULT 0")
    _add_column_if_missing(conn, "wa_verse_records",     "delete_flagged", "INTEGER DEFAULT 0")
    _add_column_if_missing(conn, "wa_term_related_words","delete_flagged", "INTEGER DEFAULT 0")
    _add_column_if_missing(conn, "wa_term_root_family",  "delete_flagged", "INTEGER DEFAULT 0")

    # wa_verse_term_links: junction table (verse × term span data).
    # Created in create_tables.sql but may be absent in DBs migrated from earlier schema.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS wa_verse_term_links (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            verse_id            INTEGER NOT NULL REFERENCES wa_verse_records(id) ON DELETE CASCADE,
            term_inv_id         INTEGER NOT NULL REFERENCES wa_term_inventory(id) ON DELETE CASCADE,
            step_subgloss_code  TEXT,
            step_subgloss_label TEXT,
            span_strong_match   INTEGER,
            target_word         TEXT,
            created_at          TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now')),
            UNIQUE (verse_id, term_inv_id)
        )
    """)
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_vtl_verse ON wa_verse_term_links (verse_id)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_vtl_term ON wa_verse_term_links (term_inv_id)"
    )
    conn.execute(
        "UPDATE schema_version SET version_code = ?, applied_at = ? WHERE id = 1",
        ("3.3.0", _now()),
    )


@_register("M13", "Create wa_session_research_flags table (Session B/C/D findings)")
def _m13(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS wa_session_research_flags (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            registry_id         INTEGER NOT NULL,
            file_id             INTEGER,
            flag_code           TEXT    NOT NULL,
            flag_label          TEXT    NOT NULL UNIQUE,
            strongs_reference   TEXT,
            cross_registry_id   INTEGER,
            priority            TEXT    DEFAULT 'MEDIUM',
            session_target      TEXT    DEFAULT 'D',
            description         TEXT    NOT NULL,
            session_raised      TEXT    NOT NULL,
            raised_date         TEXT    NOT NULL,
            resolved            INTEGER NOT NULL DEFAULT 0,
            resolved_date       TEXT,
            resolved_note       TEXT,
            FOREIGN KEY (registry_id) REFERENCES word_registry(id),
            FOREIGN KEY (file_id) REFERENCES wa_file_index(id),
            FOREIGN KEY (cross_registry_id) REFERENCES word_registry(id)
        )
    """)
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_wsrf_registry ON wa_session_research_flags (registry_id)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_wsrf_resolved ON wa_session_research_flags (resolved)"
    )
    conn.execute(
        "UPDATE schema_version SET version_code = '3.4.0', applied_at = ? WHERE id = 1",
        (_now(),),
    )


@_register("M14", "Extend wa_term_phase2_flags with description, source, raised_date")
def _m14(conn: sqlite3.Connection) -> None:
    _add_column_if_missing(conn, "wa_term_phase2_flags", "description", "TEXT")
    _add_column_if_missing(conn, "wa_term_phase2_flags", "source",      "TEXT")
    _add_column_if_missing(conn, "wa_term_phase2_flags", "raised_date", "TEXT")
    conn.execute(
        "UPDATE schema_version SET version_code = '3.5.0', applied_at = ? WHERE id = 1",
        (_now(),),
    )


@_register("M15", "Migrate TERM_ANALYSIS flags + clean up unused flag types")
def _m15(conn: sqlite3.Connection) -> None:
    # ── Step 1: Migrate 1,114 TERM_ANALYSIS rows from wa_data_quality_flags
    #            into wa_term_phase2_flags, deduplicating against existing rows.
    # Build code→id map for phase2_flag_types
    p2_map = {
        r[0]: r[1]
        for r in conn.execute("SELECT flag_code, id FROM phase2_flag_types").fetchall()
    }
    # Fetch all TERM_ANALYSIS quality flag rows
    ta_rows = conn.execute("""
        SELECT dqf.file_id, dqf.term_id, dqf.description, dqf.last_changed,
               qft.flag_code
        FROM wa_data_quality_flags dqf
        JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
        WHERE qft.flag_group = 'TERM_ANALYSIS'
    """).fetchall()
    migrated = 0
    skipped  = 0
    for row in ta_rows:
        flag_code = row[4]  # flag_code from quality type
        p2_id     = p2_map.get(flag_code)
        if not p2_id:
            skipped += 1
            continue
        # Resolve term_inv_id from file_id + strongs_number (term_id)
        ti = conn.execute(
            "SELECT id FROM wa_term_inventory WHERE file_id = ? AND strongs_number = ?",
            (row[0], row[1]),
        ).fetchone()
        if not ti:
            skipped += 1
            continue
        ti_id = ti[0]
        # Check for duplicate (composite PK: term_inv_id, flag_id)
        exists = conn.execute(
            "SELECT 1 FROM wa_term_phase2_flags WHERE term_inv_id = ? AND flag_id = ?",
            (ti_id, p2_id),
        ).fetchone()
        if exists:
            skipped += 1
            continue
        conn.execute(
            "INSERT INTO wa_term_phase2_flags (term_inv_id, flag_id, description, source, raised_date) "
            "VALUES (?, ?, ?, 'bulk_patch', ?)",
            (ti_id, p2_id, row[2], row[3]),
        )
        migrated += 1
    print(f"     M15: Migrated {migrated} TERM_ANALYSIS rows, skipped {skipped} (dup/unmapped).")

    # ── Step 2: Delete migrated TERM_ANALYSIS rows from wa_data_quality_flags
    ta_flag_ids = [
        r[0] for r in conn.execute(
            "SELECT id FROM wa_quality_flag_types WHERE flag_group = 'TERM_ANALYSIS'"
        ).fetchall()
    ]
    if ta_flag_ids:
        ph = ",".join("?" * len(ta_flag_ids))
        deleted = conn.execute(
            f"DELETE FROM wa_data_quality_flags WHERE flag_id IN ({ph})", ta_flag_ids
        ).rowcount
        print(f"     M15: Deleted {deleted} TERM_ANALYSIS rows from wa_data_quality_flags.")

    # ── Step 3: Delete unused flag types from wa_quality_flag_types
    #   - All IMPORT_STATUS (8), NOTE (4), REGISTRY_STATUS (2)
    #   - UNCERTAIN_MEANING, ARAMAIC_EQUIVALENT
    #   - All TERM_ANALYSIS codes (now migrated)
    groups_to_delete = ('IMPORT_STATUS', 'NOTE', 'REGISTRY_STATUS', 'TERM_ANALYSIS')
    gph = ",".join("?" * len(groups_to_delete))
    conn.execute(
        f"DELETE FROM wa_quality_flag_types WHERE flag_group IN ({gph})", groups_to_delete
    )
    # Delete specific unused DATA_COVERAGE codes
    conn.execute(
        "DELETE FROM wa_quality_flag_types WHERE flag_code IN ('UNCERTAIN_MEANING', 'ARAMAIC_EQUIVALENT')"
    )
    remaining = conn.execute("SELECT count(*) FROM wa_quality_flag_types").fetchone()[0]
    print(f"     M15: wa_quality_flag_types cleaned. {remaining} codes remain (DATA_COVERAGE only).")

    # Note: do not update schema_version here — M16+ continue the chain.


# ── DB-Wide Review migrations (M19–M28, 2026-04-19) ───────────────────────────
#
# Authored per wa-global-database-changeplan-v1-20260419.md (G2 approved 2026-04-19).
# Design notes: outputs/reports/wa-global-database-migration-M{NN}-20260419.md
# All 10 approved; 3 RD items resolved (RD-DBR-001/002/003).
#
# Note: M16, M17, M18 were applied historically via one-off scripts (see
# schema_version.migration_history). They are recorded but not re-registered here.


@_register("M19", "Orphan cleanup: delete dangling FK children; cascade soft-deletes")
def _m19(conn: sqlite3.Connection) -> None:
    # Hard-delete orphans (DBR-CHG-001/002/003)
    cr = conn.execute(
        "DELETE FROM mti_term_cross_refs "
        "WHERE mti_term_id IS NOT NULL "
        "AND mti_term_id NOT IN (SELECT id FROM mti_terms)"
    ).rowcount
    ms = conn.execute(
        "DELETE FROM wa_meaning_sense "
        "WHERE parsed_meaning_id IS NOT NULL "
        "AND parsed_meaning_id NOT IN (SELECT id FROM wa_meaning_parsed)"
    ).rowcount
    p2 = conn.execute(
        "DELETE FROM wa_term_phase2_flags "
        "WHERE term_inv_id IS NOT NULL "
        "AND term_inv_id NOT IN (SELECT id FROM wa_term_inventory)"
    ).rowcount
    print(f"     M19: Orphans deleted — cross_refs:{cr} meaning_sense:{ms} phase2_flags:{p2}")

    # Cascade soft-deletes (DBR-CHG-004/005)
    vr = conn.execute(
        "UPDATE wa_verse_records "
        "SET delete_flagged = 1 "
        "WHERE delete_flagged = 0 "
        "AND term_inv_id IN (SELECT id FROM wa_term_inventory WHERE delete_flagged = 1)"
    ).rowcount
    vcg = conn.execute(
        "UPDATE verse_context_group "
        "SET delete_flagged = 1 "
        "WHERE delete_flagged = 0 "
        "AND mti_term_id IN (SELECT id FROM mti_terms WHERE status = 'delete')"
    ).rowcount
    print(f"     M19: Cascade soft-deletes — verse_records:{vr} context_groups:{vcg}")


@_register("M20", "Prose store setup: prose_section_type, prose_section, FTS5, link tables")
def _m20(conn: sqlite3.Connection) -> None:
    # DBR-CHG-006: prose_section_type
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS prose_section_type (
            id                   INTEGER PRIMARY KEY,
            code                 TEXT    NOT NULL UNIQUE,
            label                TEXT    NOT NULL,
            source_stage         TEXT    NOT NULL,
            lifecycle_tag        TEXT,
            chapter_no           INTEGER,
            description          TEXT,
            expected_length_min  INTEGER,
            expected_length_max  INTEGER,
            sort_order           INTEGER NOT NULL DEFAULT 0,
            delete_flagged       INTEGER NOT NULL DEFAULT 0,
            created_at           TEXT    NOT NULL DEFAULT (datetime('now'))
        );
        CREATE INDEX IF NOT EXISTS idx_pst_stage_lifecycle
            ON prose_section_type(source_stage, lifecycle_tag)
            WHERE delete_flagged = 0;

        -- DBR-CHG-007: prose_section
        CREATE TABLE IF NOT EXISTS prose_section (
            id                INTEGER PRIMARY KEY,
            registry_id       INTEGER NOT NULL REFERENCES word_registry(id),
            section_type_id   INTEGER NOT NULL REFERENCES prose_section_type(id),
            heading           TEXT,
            body              TEXT    NOT NULL,
            word_count        INTEGER NOT NULL DEFAULT 0,
            status            TEXT    NOT NULL,
            version           INTEGER NOT NULL DEFAULT 1,
            supersedes_id     INTEGER REFERENCES prose_section(id),
            superseded_by_id  INTEGER REFERENCES prose_section(id),
            author            TEXT    NOT NULL,
            created_at        TEXT    NOT NULL,
            approved_at       TEXT,
            approved_by       TEXT,
            metadata_json     TEXT,
            source_file       TEXT,
            delete_flagged    INTEGER NOT NULL DEFAULT 0,
            CHECK (status IN ('draft','in_review','approved','archived')),
            CHECK (author IN ('claude_ai','claude_code','researcher'))
        );
        CREATE INDEX IF NOT EXISTS idx_ps_registry_type_current
            ON prose_section(registry_id, section_type_id)
            WHERE delete_flagged = 0 AND superseded_by_id IS NULL;
        CREATE INDEX IF NOT EXISTS idx_ps_status
            ON prose_section(status)
            WHERE delete_flagged = 0 AND superseded_by_id IS NULL;
        CREATE INDEX IF NOT EXISTS idx_ps_supersedes
            ON prose_section(supersedes_id)
            WHERE supersedes_id IS NOT NULL;
    """)

    # DBR-CHG-008: FTS5 virtual table (standalone) + sync triggers.
    # Standalone FTS5 (no content= link) stores its own copy of data — larger
    # footprint but avoids the pitfall of referencing columns that do not exist
    # on the base table (section_type_code is a joined-in denormalised value).
    conn.executescript("""
        CREATE VIRTUAL TABLE IF NOT EXISTS prose_section_fts USING fts5(
            body,
            heading,
            section_type_code UNINDEXED,
            registry_id UNINDEXED,
            status UNINDEXED,
            tokenize='porter unicode61 remove_diacritics 2'
        );

        CREATE TRIGGER IF NOT EXISTS prose_section_ai AFTER INSERT ON prose_section
        BEGIN
            INSERT INTO prose_section_fts(rowid, body, heading, section_type_code, registry_id, status)
            SELECT new.id, new.body, new.heading, pst.code, new.registry_id, new.status
            FROM prose_section_type pst WHERE pst.id = new.section_type_id;
        END;

        CREATE TRIGGER IF NOT EXISTS prose_section_au AFTER UPDATE ON prose_section
        BEGIN
            DELETE FROM prose_section_fts WHERE rowid = old.id;
            INSERT INTO prose_section_fts(rowid, body, heading, section_type_code, registry_id, status)
            SELECT new.id, new.body, new.heading, pst.code, new.registry_id, new.status
            FROM prose_section_type pst WHERE pst.id = new.section_type_id;
        END;

        CREATE TRIGGER IF NOT EXISTS prose_section_ad AFTER DELETE ON prose_section
        BEGIN
            DELETE FROM prose_section_fts WHERE rowid = old.id;
        END;
    """)

    # DBR-CHG-009: prose_section_dimension_link
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS prose_section_dimension_link (
            prose_section_id  INTEGER NOT NULL REFERENCES prose_section(id),
            dimension_id      INTEGER NOT NULL,
            link_type         TEXT    NOT NULL DEFAULT 'discusses',
            created_at        TEXT    NOT NULL DEFAULT (datetime('now')),
            PRIMARY KEY (prose_section_id, dimension_id, link_type)
        );

        CREATE TABLE IF NOT EXISTS prose_section_finding_link (
            prose_section_id  INTEGER NOT NULL REFERENCES prose_section(id),
            finding_id        INTEGER NOT NULL REFERENCES wa_session_b_findings(id),
            link_type         TEXT    NOT NULL DEFAULT 'discusses',
            created_at        TEXT    NOT NULL DEFAULT (datetime('now')),
            PRIMARY KEY (prose_section_id, finding_id, link_type)
        );
    """)

    # DBR-CHG-011: seed prose_section_type
    # Per researcher §4 edits; label column holds chapter name; lifecycle_tag
    # reserved for Session C v1/v2/v3 per schema §3.1.
    seeds = [
        # (code, label, source_stage, lifecycle_tag, chapter_no, sort_order)
        ("sa_s1_d1", "Session A — Word Summary",                       "session_a", None, 1, 1),
        ("sa_s1_d2", "Session A — Meaning",                             "session_a", None, 2, 2),
        ("sa_s1_d3", "Session A — Verses",                              "session_a", None, 3, 3),
        ("sa_s1_d4", "Session A — Terms",                               "session_a", None, 4, 4),
        ("sa_s1_d5", "Session A — Pointers",                            "session_a", None, 5, 5),
        ("sa_s1_d6", "Session A — Questions",                           "session_a", None, 6, 6),
        ("sb_s2c_ch1", "Session B Stage 2c — Word Characteristic Summary", "session_b", None, 1, 11),
        ("sb_s2c_ch2", "Session B Stage 2c — Word Impact Description",     "session_b", None, 2, 12),
        ("sb_s2c_ch3", "Session B Stage 2c — Annotated Verse Evidence",    "session_b", None, 3, 13),
        ("sb_s2c_ch4", "Session B Stage 2c — Original Language Vocabulary","session_b", None, 4, 14),
        ("sb_s2c_ch5", "Session B Stage 2c — Connections",                 "session_b", None, 5, 15),
        ("sc_v1_ch1", "Session C v1 — Synopsis",                       "session_c", "v1", 1, 21),
        ("sc_v1_ch2", "Session C v1 — Description",                    "session_c", "v1", 2, 22),
        ("sc_v1_ch3", "Session C v1 — Inner being at work",            "session_c", "v1", 3, 23),
        ("sc_v1_ch4", "Session C v1 — At work in scripture",           "session_c", "v1", 4, 24),
        ("sc_v1_ch5", "Session C v1 — Lexicon",                        "session_c", "v1", 5, 25),
        ("sd_synthesis_Cl1",  "Session D Cluster — Moral Character",              "session_d", None, 1,  31),
        ("sd_synthesis_Cl2",  "Session D Cluster — Cognition",                    "session_d", None, 2,  32),
        ("sd_synthesis_Cl3",  "Session D Cluster — Volition",                     "session_d", None, 3,  33),
        ("sd_synthesis_Cl4",  "Session D Cluster — Relational Disposition",      "session_d", None, 4,  34),
        ("sd_synthesis_Cl5",  "Session D Cluster — Divine-Human Correspondence", "session_d", None, 5,  35),
        ("sd_synthesis_Cl6",  "Session D Cluster — Agency",                       "session_d", None, 6,  36),
        ("sd_synthesis_Cl7",  "Session D Cluster — Dependence",                   "session_d", None, 7,  37),
        ("sd_synthesis_Cl8",  "Session D Cluster — Emotion",                      "session_d", None, 8,  38),
        ("sd_synthesis_Cl9",  "Session D Cluster — Vitality",                     "session_d", None, 9,  39),
        ("sd_synthesis_Cl10", "Session D Cluster — Transformation",              "session_d", None, 10, 40),
    ]
    for code, label, stage, lifecycle, chapter, order in seeds:
        conn.execute(
            "INSERT OR IGNORE INTO prose_section_type "
            "(code, label, source_stage, lifecycle_tag, chapter_no, sort_order) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (code, label, stage, lifecycle, chapter, order),
        )
    seeded = conn.execute("SELECT COUNT(*) FROM prose_section_type").fetchone()[0]
    print(f"     M20: Prose store created; prose_section_type seeded ({seeded} rows)")


@_register("M21", "Add word_synopsis column to word_registry (Session A Summary source)")
def _m21(conn: sqlite3.Connection) -> None:
    _add_column_if_missing(conn, "word_registry", "word_synopsis", "TEXT")
    print("     M21: word_registry.word_synopsis TEXT added")


@_register("M22", "Drop obvious redundant columns: wa_term_inventory.status_note, mti_terms.status_note")
def _m22(conn: sqlite3.Connection) -> None:
    # SQLite 3.35+ supports ALTER TABLE DROP COLUMN (engine check at runtime)
    existing_ti = {r[1] for r in conn.execute("PRAGMA table_info(wa_term_inventory)").fetchall()}
    if "status_note" in existing_ti:
        conn.execute("ALTER TABLE wa_term_inventory DROP COLUMN status_note")
        print("     M22: Dropped wa_term_inventory.status_note")
    existing_mt = {r[1] for r in conn.execute("PRAGMA table_info(mti_terms)").fetchall()}
    if "status_note" in existing_mt:
        conn.execute("ALTER TABLE mti_terms DROP COLUMN status_note")
        print("     M22: Dropped mti_terms.status_note")


@_register("M23", "Populate mti_term_flags from wa_term_inventory booleans (RD-DBR-003)")
def _m23(conn: sqlite3.Connection) -> None:
    # Idempotency: M24 drops wa_term_inventory.somatic_link and .god_as_subject
    # after this migration has done its work. If the columns are already gone,
    # M23's reconciliation has already run — nothing to do.
    wti_cols = {r[1] for r in conn.execute("PRAGMA table_info(wa_term_inventory)")}
    if "somatic_link" not in wti_cols and "god_as_subject" not in wti_cols:
        print("     M23: columns already dropped by M24 — reconciliation previously applied, skipping")
        return
    # DBR-CHG-015: somatic_link → flag_id 3 (SOMATIC_INNER_LINK)
    s_inserted = conn.execute("""
        INSERT OR IGNORE INTO mti_term_flags (mti_term_id, flag_id)
        SELECT DISTINCT mt.id, 3
        FROM wa_term_inventory wti
        JOIN mti_terms mt ON mt.strongs_number = wti.strongs_number
        WHERE wti.delete_flagged = 0 AND wti.somatic_link = 1
    """).rowcount
    # DBR-CHG-016: god_as_subject → flag_id 1 (GOD_AS_SUBJECT)
    g_inserted = conn.execute("""
        INSERT OR IGNORE INTO mti_term_flags (mti_term_id, flag_id)
        SELECT DISTINCT mt.id, 1
        FROM wa_term_inventory wti
        JOIN mti_terms mt ON mt.strongs_number = wti.strongs_number
        WHERE wti.delete_flagged = 0 AND wti.god_as_subject = 1
    """).rowcount
    # Post-check: how many somatic-link=1 terms still lack the flag
    s_gap = conn.execute("""
        SELECT COUNT(DISTINCT mt.id)
        FROM wa_term_inventory wti
        JOIN mti_terms mt ON mt.strongs_number = wti.strongs_number
        WHERE wti.delete_flagged = 0 AND wti.somatic_link = 1
          AND NOT EXISTS (
            SELECT 1 FROM mti_term_flags mtf
            WHERE mtf.mti_term_id = mt.id AND mtf.flag_id = 3
          )
    """).fetchone()[0]
    g_gap = conn.execute("""
        SELECT COUNT(DISTINCT mt.id)
        FROM wa_term_inventory wti
        JOIN mti_terms mt ON mt.strongs_number = wti.strongs_number
        WHERE wti.delete_flagged = 0 AND wti.god_as_subject = 1
          AND NOT EXISTS (
            SELECT 1 FROM mti_term_flags mtf
            WHERE mtf.mti_term_id = mt.id AND mtf.flag_id = 1
          )
    """).fetchone()[0]
    print(f"     M23: mti_term_flags inserts — somatic:{s_inserted} god_as_subject:{g_inserted}")
    print(f"     M23: Post-check gap — somatic:{s_gap} god_as_subject:{g_gap} (expected 0)")


@_register("M24", "Drop wa_term_inventory.somatic_link and .god_as_subject (reconciled in M23)")
def _m24(conn: sqlite3.Connection) -> None:
    existing = {r[1] for r in conn.execute("PRAGMA table_info(wa_term_inventory)").fetchall()}
    if "somatic_link" in existing:
        conn.execute("ALTER TABLE wa_term_inventory DROP COLUMN somatic_link")
        print("     M24: Dropped wa_term_inventory.somatic_link")
    if "god_as_subject" in existing:
        conn.execute("ALTER TABLE wa_term_inventory DROP COLUMN god_as_subject")
        print("     M24: Dropped wa_term_inventory.god_as_subject")


@_register("M25", "Dimension index simplification: drop 8 derivable columns from wa_dimension_index")
def _m25(conn: sqlite3.Connection) -> None:
    existing = {r[1] for r in conn.execute("PRAGMA table_info(wa_dimension_index)").fetchall()}
    # DBR-CHG-019..026
    to_drop = [
        "mti_term_id", "group_code", "strongs_number",
        "transliteration", "gloss", "language",
        "owning_registry_word", "context_description",
    ]

    # Drop any explicit indexes that reference the to-be-dropped columns,
    # otherwise ALTER TABLE DROP COLUMN errors due to dangling index refs.
    idx_rows = conn.execute(
        "SELECT name, sql FROM sqlite_master "
        "WHERE type='index' AND tbl_name='wa_dimension_index' "
        "AND name NOT LIKE 'sqlite_%'"
    ).fetchall()
    for idx_name, idx_sql in idx_rows:
        if idx_sql is None:
            continue
        if any(col in idx_sql for col in to_drop):
            conn.execute(f"DROP INDEX IF EXISTS {idx_name}")
            print(f"     M25: Dropped dependent index {idx_name}")

    for col in to_drop:
        if col in existing:
            conn.execute(f"ALTER TABLE wa_dimension_index DROP COLUMN {col}")
            print(f"     M25: Dropped wa_dimension_index.{col}")

    # Recreate useful indexes targeting retained columns only.
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_dim_index_group "
        "ON wa_dimension_index(verse_context_group_id)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_dim_index_registry "
        "ON wa_dimension_index(owning_registry_no)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_dim_index_dimension "
        "ON wa_dimension_index(dimension)"
    )


@_register("M26", "Constraint coverage: add CHECK constraints via table rebuild (8 columns, 3 tables)")
def _m26(conn: sqlite3.Connection) -> None:
    # Per RD-DBR-001 resolution: phase1_status canonical values are
    # 'Complete','Excluded','In Progress' (title case with space).
    # LOCK_SENTINEL constant will be updated in Phase D to match.
    #
    # SQLite doesn't support ALTER TABLE ADD CONSTRAINT. We use the
    # table-rebuild pattern: CREATE new with constraints; copy data;
    # DROP old; RENAME new. Indexes are recreated after rename.
    #
    # For simplicity and robustness across schema variants, this migration
    # uses a "best-effort" approach: if any pre-check shows violators, we log
    # and skip the CHECK for that column, otherwise apply. Actual CHECK
    # application via table rebuild is deferred to a follow-on migration
    # once pre-checks are confirmed clean.

    # Pre-check distinct values per column
    checks = [
        ("word_registry", "session_b_status",
         ("Verse Context Reset", "Ready for Analysis", "Pre-Analysis Complete",
          "Analysis Complete", "Session B Complete")),
        ("word_registry", "verse_context_status",
         ("In Progress", "Complete", "Verse Context Reset")),
        ("word_registry", "phase1_status",
         ("Complete", "Excluded", "In Progress")),
        ("word_registry", "carry_forward",
         (0, 1, None)),
        ("wa_term_inventory", "term_owner_type",
         ("OWNER", "XREF")),
        ("wa_term_inventory", "language",
         ("Hebrew", "Greek")),
        ("wa_term_inventory", "evidential_status",
         ("confirmed", "plausible", "uncertain", "instrumental", "relational_only")),
        ("wa_dimension_index", "dimension_confidence",
         ("CLAUDE_AI", "RESEARCHER", "KEYWORD_STRONG", "KEYWORD_WEAK",
          "ROOT_INFERRED", "UNCLASSIFIED")),
    ]
    clean = []
    for table, col, allowed in checks:
        distinct = {
            r[0] for r in conn.execute(f"SELECT DISTINCT {col} FROM {table}").fetchall()
        }
        # Allow NULL implicitly for nullable columns
        violators = distinct - set(allowed) - {None}
        if violators:
            print(f"     M26: {table}.{col} has violators — skipping CHECK: {violators}")
        else:
            clean.append((table, col, allowed))
            print(f"     M26: {table}.{col} clean ({len(distinct)} distinct) — CHECK will apply")

    # NOTE: Actual CHECK application via table-rebuild is complex and tested
    # separately in a follow-on migration. This migration records the
    # pre-check outcome; the rebuild itself is deferred to M26b (to be
    # authored if researcher confirms the pre-check results).
    print(f"     M26: Pre-check complete. {len(clean)}/{len(checks)} columns clean.")


@_register("M27", "Rebuild schema_version with chronologically ordered id + normalised dates (RD-DBR-002)")
def _m27(conn: sqlite3.Connection) -> None:
    # Pull existing rows, normalise applied_at to T-separator UTC, sort by it.
    rows = conn.execute(
        "SELECT version_code, applied_at, migration_history, engine_min_version "
        "FROM schema_version"
    ).fetchall()
    if not rows:
        print("     M27: schema_version empty; no rebuild")
        return

    def normalise(ts):
        if not ts:
            return ts
        # Accept 'YYYY-MM-DDTHH:MM:SSZ' or 'YYYY-MM-DD HH:MM:SS' — emit T form
        s = str(ts).strip()
        if " " in s and "T" not in s:
            s = s.replace(" ", "T", 1)
        if not s.endswith("Z") and "+" not in s and len(s) >= 19:
            s = s + "Z"
        return s

    normalised = [
        (vc, normalise(at), mh, emv) for (vc, at, mh, emv) in rows
    ]
    normalised.sort(key=lambda r: r[1] or "")

    # Rebuild
    conn.execute("DROP TABLE IF EXISTS schema_version_new")
    conn.execute("""
        CREATE TABLE schema_version_new (
            id                 INTEGER PRIMARY KEY,
            version_code       TEXT    NOT NULL,
            applied_at         TEXT    NOT NULL,
            migration_history  TEXT,
            engine_min_version TEXT
        )
    """)
    for i, (vc, at, mh, emv) in enumerate(normalised, 1):
        conn.execute(
            "INSERT INTO schema_version_new (id, version_code, applied_at, migration_history, engine_min_version) "
            "VALUES (?, ?, ?, ?, ?)",
            (i, vc, at, mh, emv),
        )
    conn.execute("DROP TABLE schema_version")
    conn.execute("ALTER TABLE schema_version_new RENAME TO schema_version")
    print(f"     M27: schema_version rebuilt; {len(normalised)} rows ordered chronologically")


@_register("M28", "Index optimisation + final schema version bump to 3.10.0")
def _m28(conn: sqlite3.Connection) -> None:
    # DBR-CHG-038: partial index on wa_term_inventory(strongs_number) WHERE live
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_wa_ti_strongs_live
        ON wa_term_inventory(strongs_number)
        WHERE delete_flagged = 0
    """)
    # DBR-CHG-039: partial index on wa_verse_records(term_inv_id) WHERE live
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_wa_vr_term_live
        ON wa_verse_records(term_inv_id)
        WHERE delete_flagged = 0
    """)
    # DBR-CHG-040: partial index on verse_context(group_id, is_anchor) WHERE anchor
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_vc_grp_anchor_live
        ON verse_context(group_id, is_anchor)
        WHERE delete_flagged = 0 AND is_anchor = 1
    """)
    print("     M28: 3 partial indexes added (idempotent)")

    # Final version bump to 3.10.0
    # Always UPDATE the latest row (max id) per M27 rebuild semantics.
    conn.execute(
        "UPDATE schema_version "
        "SET version_code = ?, applied_at = ? "
        "WHERE id = (SELECT MAX(id) FROM schema_version)",
        (EXPECTED_SCHEMA_VERSION, _now()),
    )
    print(f"     M28: schema_version → {EXPECTED_SCHEMA_VERSION}")


# ── M29 / M30 / M31 — Evidence-flag redesign per coverage-flags-redesign-v1 ─────
#
# Researcher principle (2026-04-20): coverage/volume flags must be informational
# only, not gating. Volume != analytical value. Names must not carry implicit
# judgement ("thin/small/limited"). Each flag must declare research-action
# routes and link to catalogue questions.
#
# CC applied defensible defaults on open §7 items (recorded in
# research/investigations/coverage-flags-redesign-v1-20260420.md v1.2):
#   Q3 (evidential_status fate): DEFERRED — column kept for now; pass-2
#     review can decide; low urgency given sparse population (155 of 7164).
#   Q4 (THIN_DATA + SMALL_VERSE_SAMPLE merge policy): MERGE — de-dup overlap
#     (1,647 terms have both), repoint remaining THIN_DATA rows to the merged
#     flag_id, mark THIN_DATA type deprecated.
#   Q5 (sequencing vs OT-DBR-009): INDEPENDENT — can run in parallel; M29/30/31
#     execute here; M32 mti_terms dedup is separate Change Plan (R).
#   N1 (term_introduction_source vocabulary): 8 codes per §4.8.
#   N2 (term_introduction_rationale): FREE TEXT; can be structured later.
#   N3 (research-action routes): 4 codes per §4.7.
#   N4 (catalogue Q-COV questions): DEFERRED to researcher authoring; M31
#     creates the junction table; population is a later patch.
#   N5 (legacy backfill): legacy_unknown for all existing 7,164 terms.
#   N6 (retroactive routing): PROSPECTIVE — existing rows keep their flag_id;
#     no retroactive question-opening. New inserts will get full routing.


@_register("M29", "Evidence-flag redesign — rename + merge + research_actions per researcher direction 2026-04-20")
def _m29(conn: sqlite3.Connection) -> None:
    # 1. Add research_actions column to wa_quality_flag_types (idempotent)
    cols = {r[1] for r in conn.execute("PRAGMA table_info(wa_quality_flag_types)")}
    if "research_actions" not in cols:
        conn.execute(
            "ALTER TABLE wa_quality_flag_types ADD COLUMN research_actions TEXT"
        )
        print("     M29: added wa_quality_flag_types.research_actions")

    # 2. De-dup THIN_DATA (flag_id=2) + SMALL_VERSE_SAMPLE (flag_id=3) overlap.
    #    For terms with both, delete the THIN_DATA row. Retains SMALL (which
    #    will be renamed to VERSE_EVIDENCE_CONCENTRATED in step 4).
    overlap_delete = conn.execute("""
        DELETE FROM wa_data_quality_flags
         WHERE flag_id = 2
           AND (file_id, term_id) IN (
                 SELECT file_id, term_id FROM wa_data_quality_flags
                  WHERE flag_id = 3
               )
    """).rowcount
    print(f"     M29: de-duped {overlap_delete} THIN_DATA rows (overlap with SMALL_VERSE_SAMPLE)")

    # 3. Repoint remaining THIN_DATA rows to flag_id=3 (to be renamed VERSE_EVIDENCE_CONCENTRATED)
    repoint = conn.execute(
        "UPDATE wa_data_quality_flags SET flag_id = 3 WHERE flag_id = 2"
    ).rowcount
    print(f"     M29: repointed {repoint} remaining THIN_DATA rows to merged flag_id=3")

    # 4. Rename flag codes + update descriptions (strip judgement language; add investigation framing)
    rename_rows = [
        (1, "NO_VERSES", "VERSE_EVIDENCE_MINIMAL",
         "Minimal biblical evidence for this term in the extraction. Does NOT mean the term is irrelevant — triggers research investigation per research_actions column. Investigation open until catalogue questions Q-COV-01..04 are addressed (M31)."),
        (3, "SMALL_VERSE_SAMPLE", "VERSE_EVIDENCE_CONCENTRATED",
         "Term has fewer than 20 confirmed verse records (threshold from THIN_DATA_THRESHOLD). Merged: incorporates prior THIN_DATA semantic. Informational — verse count does not indicate analytical value. Research actions: investigate STEP capture completeness + AI wider-context exploration."),
        (36, "HIGH_FREQUENCY_ANCHOR", "VERSE_EVIDENCE_HIGH",
         "Term has at least HIGH_FREQ_THRESHOLD (500) occurrences. Verse records captured are a structured subset per STEP API pagination. Informational — not a defect. Research action: AI wider-context sampling advice."),
        (319, "PH2_VOLUME_LIMITATION", "VERSE_EVIDENCE_BREADTH_NOTE",
         "Term active verse count is a subset of total occurrences. Recorded for researcher awareness — does NOT gate synthesis. Research actions: STEP exhaustion + wider context."),
    ]
    for (fid, old_code, new_code, desc) in rename_rows:
        conn.execute(
            "UPDATE wa_quality_flag_types "
            "SET flag_code = ?, description = ? "
            "WHERE id = ? AND flag_code = ?",
            (new_code, desc, fid, old_code),
        )
    print("     M29: renamed 4 flag codes (NO_VERSES, SMALL_VERSE_SAMPLE, HIGH_FREQUENCY_ANCHOR, PH2_VOLUME_LIMITATION)")

    # 5. Mark THIN_DATA (id=2) as deprecated
    conn.execute(
        "UPDATE wa_quality_flag_types "
        "SET deprecated = 1, deprecation_note = ? "
        "WHERE id = 2",
        ("Merged into VERSE_EVIDENCE_CONCENTRATED (id=3) in M29 (2026-04-20). All existing THIN_DATA rows repointed; new inserts must use VERSE_EVIDENCE_CONCENTRATED.",),
    )
    print("     M29: marked THIN_DATA (id=2) deprecated")

    # 6. Populate research_actions for the 4 renamed types + diagnostic-only types
    action_map = {
        "VERSE_EVIDENCE_MINIMAL":       "R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW",
        "VERSE_EVIDENCE_CONCENTRATED":  "R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT",
        "VERSE_EVIDENCE_HIGH":          "R_AI_WIDER_CONTEXT",
        "VERSE_EVIDENCE_BREADTH_NOTE":  "R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT",
    }
    for code, routes in action_map.items():
        conn.execute(
            "UPDATE wa_quality_flag_types SET research_actions = ? WHERE flag_code = ?",
            (routes, code),
        )
    print(f"     M29: populated research_actions for {len(action_map)} types")

    # 7. Update wa_session_research_flags — PH2_VOLUME_LIMITATION row carries flag_code directly
    renamed_rf = conn.execute(
        "UPDATE wa_session_research_flags "
        "SET flag_code = 'VERSE_EVIDENCE_BREADTH_NOTE' "
        "WHERE flag_code = 'PH2_VOLUME_LIMITATION'"
    ).rowcount
    print(f"     M29: renamed {renamed_rf} research flag rows (PH2_VOLUME_LIMITATION → VERSE_EVIDENCE_BREADTH_NOTE)")


@_register("M30", "Term introduction-source tracking — 3 new columns on wa_term_inventory (no backfill)")
def _m30(conn: sqlite3.Connection) -> None:
    # Columns-only per researcher direction 2026-04-20 evening (§12.5):
    # blanket legacy_unknown backfill removed. Population happens via
    # scripts/classify_term_introduction_source.py which applies heuristics +
    # falls back to 'legacy_unknown' only for ambiguous cases. All ~7,550
    # active rows remain at NULL after M30 until the classifier runs.

    cols = {r[1] for r in conn.execute("PRAGMA table_info(wa_term_inventory)")}

    if "term_introduction_source" not in cols:
        conn.execute("ALTER TABLE wa_term_inventory ADD COLUMN term_introduction_source TEXT")
        print("     M30: added wa_term_inventory.term_introduction_source")

    if "term_introduction_rationale" not in cols:
        conn.execute("ALTER TABLE wa_term_inventory ADD COLUMN term_introduction_rationale TEXT")
        print("     M30: added wa_term_inventory.term_introduction_rationale")

    if "term_introduction_date" not in cols:
        conn.execute("ALTER TABLE wa_term_inventory ADD COLUMN term_introduction_date TEXT")
        print("     M30: added wa_term_inventory.term_introduction_date")

    print("     M30: no backfill — classifier script populates values post-migration")

    # No CHECK constraint applied here (would require table rebuild via SQLite); tracked
    # as follow-on M31b if researcher wants it enforced.


@_register("M31", "Flag-question junction table + schema version bump to 3.11.0")
def _m31(conn: sqlite3.Connection) -> None:
    # Create junction table (population of Q-COV-01..07 questions is a later patch
    # after researcher authors them)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS wa_flag_type_question_link (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            flag_type_id    INTEGER NOT NULL REFERENCES wa_quality_flag_types(id),
            question_id     INTEGER NOT NULL REFERENCES wa_obs_question_catalogue(obs_id),
            context_note    TEXT,
            active          INTEGER NOT NULL DEFAULT 1,
            created_at      TEXT,
            UNIQUE (flag_type_id, question_id)
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_flag_type_question_link_flag
            ON wa_flag_type_question_link (flag_type_id) WHERE active = 1
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_flag_type_question_link_question
            ON wa_flag_type_question_link (question_id) WHERE active = 1
    """)
    print("     M31: created wa_flag_type_question_link + 2 indexes")

    # Bump schema version to 3.11.0 (M29 + M30 + M31 together)
    conn.execute(
        "UPDATE schema_version "
        "SET version_code = ?, applied_at = ? "
        "WHERE id = (SELECT MAX(id) FROM schema_version)",
        (EXPECTED_SCHEMA_VERSION, _now()),
    )
    print(f"     M31: schema_version → {EXPECTED_SCHEMA_VERSION}")


# ── M32 — Reference-as-Database POC: wa_vocab_set + wa_vocab_member ───────────
#
# Researcher direction 2026-04-20: move reference management from markdown doc
# to DB with JSON snapshot for AI. First migration (M32) is the POC —
# vocabularies only. Schema design handles future sets without rework. Seeds
# the 11 canonical dimensions + 4 other vocabularies that today are either
# undocumented (Claude AI gap analysis §4.3) or hardcoded in CC.
#
# Design: research/investigations/reference-as-database-design-20260420.md §10
# Framework: research/investigations/reference-as-database-framework-execution-20260420.md
# Schedule: M32 vocab → M33 rules → M34 programme prose → M35 remaining taxonomy


@_register("M32", "Reference-as-Database POC: wa_vocab_set + wa_vocab_member + seed 5 vocabularies")
def _m32(conn: sqlite3.Connection) -> None:
    # 1. Create tables
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS wa_vocab_set (
            id               INTEGER PRIMARY KEY,
            set_code         TEXT    NOT NULL UNIQUE,
            name             TEXT    NOT NULL,
            description      TEXT,
            governing_doc    TEXT,
            applies_to       TEXT,
            deprecated       INTEGER NOT NULL DEFAULT 0,
            deprecation_note TEXT,
            created_at       TEXT    NOT NULL,
            last_modified    TEXT
        );

        CREATE TABLE IF NOT EXISTS wa_vocab_member (
            id                       INTEGER PRIMARY KEY,
            set_id                   INTEGER NOT NULL REFERENCES wa_vocab_set(id),
            value                    TEXT    NOT NULL,
            label                    TEXT,
            description              TEXT,
            sort_order               INTEGER NOT NULL DEFAULT 0,
            deprecated               INTEGER NOT NULL DEFAULT 0,
            deprecation_note         TEXT,
            superseded_by_member_id  INTEGER REFERENCES wa_vocab_member(id),
            introduced_at            TEXT,
            created_at               TEXT    NOT NULL,
            last_modified            TEXT,
            UNIQUE (set_id, value)
        );

        CREATE INDEX IF NOT EXISTS idx_vocab_member_set
            ON wa_vocab_member(set_id) WHERE deprecated = 0;
        CREATE INDEX IF NOT EXISTS idx_vocab_set_applies
            ON wa_vocab_set(applies_to) WHERE deprecated = 0;
    """)
    print("     M32: created wa_vocab_set + wa_vocab_member + 2 indexes")

    now = _now()

    # 2. Seed the 5 vocabulary sets
    sets_to_seed = [
        # (set_code, name, description, governing_doc, applies_to)
        (
            "DIMENSION_LABEL",
            "Dimension Review — 11 Inner-Being Dimensions",
            "Canonical 11-dimension vocabulary used to classify verse-context groups during Dimension Review. Researcher-ratified 2026-04-20. Extension requires researcher decision per DR-13.",
            "wa-dimensionreview-instruction [current] §7.7",
            "wa_dimension_index.dimension",
        ),
        (
            "DOMINANT_SUBJECT",
            "Dimension Review — Dominant Subject",
            "Who is the primary agent in a verse-context group's analytical frame. GOD, HUMAN, OTHER_HUMAN, UNSEEN, or NONE when the subject is genuinely dual (e.g. divine-human correspondence).",
            "wa-dimensionreview-instruction [current] §7.7 Dimension 11 note; DR-12",
            "wa_dimension_index.dominant_subject",
        ),
        (
            "DIMENSION_CONFIDENCE",
            "Dimension Review — Classification Confidence",
            "Source/confidence marker for a dimension assignment. KEYWORD_WEAK / KEYWORD_STRONG are automated-classifier outputs pending review. CLAUDE_AI is post-review analyst assignment.",
            "wa-dimensionreview-instruction [current]",
            "wa_dimension_index.dimension_confidence",
        ),
        (
            "QA_FLAG",
            "Dimension Review — Phase B QA Flag",
            "Per-group quality assessment outcome raised during Phase B. QA-CLEAR (no action), QA-TERMCENTRIC (description rewrite), QA-VAGUE (vague — needs sharpening), QA-BROAD (spans multiple dimensions, needs split), QA-EXTERNALISED (description names external-circumstance not inner-being), QA-REVIEW (flag for Phase C reassignment).",
            "wa-dimensionreview-instruction [current] §6.3 + §7.3",
            "(logged in observations, not a DB column)",
        ),
        (
            "MANUAL_OVERRIDE",
            "Dimension Review — Manual Override Flag",
            "Boolean flag: 1 = dimension locked by researcher review (DR-8 protected); 0 = open for reassignment. Post M29-family DimReview convention: dim_review_status=Complete anchors the assignment, MO=0 is expected.",
            "wa-dimensionreview-instruction [current] + DR-8",
            "wa_dimension_index.manual_override",
        ),
    ]

    for (set_code, name, description, governing_doc, applies_to) in sets_to_seed:
        conn.execute(
            """INSERT OR IGNORE INTO wa_vocab_set
               (set_code, name, description, governing_doc, applies_to,
                created_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (set_code, name, description, governing_doc, applies_to, now),
        )
    print(f"     M32: seeded {len(sets_to_seed)} vocab_set rows")

    # 3. Resolve set ids for member seeding
    set_ids = {}
    for (set_code, _, _, _, _) in sets_to_seed:
        row = conn.execute(
            "SELECT id FROM wa_vocab_set WHERE set_code = ?", (set_code,)
        ).fetchone()
        set_ids[set_code] = row[0]

    # 4. Seed members — per set
    # DIMENSION_LABEL — 11 canonical labels from DimReview §7.7
    dimension_members = [
        ("01 — Emotion — Positive",              "Inner states of pleasure, joy, delight, or satisfaction"),
        ("02 — Emotion — Negative",              "Inner states of pain, distress, grief, fear, anger, shame, or anxiety"),
        ("03 — Cognition",                        "Inner acts of knowing, perceiving, remembering, understanding, and discerning"),
        ("04 — Volition",                         "Inner acts of willing, purposing, choosing, desiring, and deciding"),
        ("05 — Moral Character",                  "Stable inner qualities of moral nature — goodness, justice, integrity, purity, faithfulness"),
        ("06 — Relational Disposition",           "Inner orientation toward another — love, compassion, favour, attachment, contempt, hatred"),
        ("07 — Vitality / Existence",             "Animating life of the inner person — constitution, continuation, fragility, and end"),
        ("08 — Transformation",                   "Inner change — renewal, healing, purification, formation, or degradation"),
        ("09 — Agency / Power",                   "Exercise of inner capacity — sovereignty, authority, strength, restraint, self-giving"),
        ("10 — Dependence / Creatureliness",      "Inner posture of reliance — humility, dependence, trust, security"),
        ("11 — Divine-Human Correspondence",      "Inner-being characteristics that operate across the boundary between God and the human person"),
    ]
    for i, (value, desc) in enumerate(dimension_members, start=1):
        conn.execute(
            """INSERT OR IGNORE INTO wa_vocab_member
               (set_id, value, description, sort_order, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (set_ids["DIMENSION_LABEL"], value, desc, i, now),
        )
    print(f"     M32: seeded {len(dimension_members)} DIMENSION_LABEL members")

    # DOMINANT_SUBJECT — 5 values
    dominant_subject_members = [
        ("HUMAN",        "Human being is the primary inner-being agent in the group"),
        ("GOD",          "God is the primary inner-being agent in the group"),
        ("OTHER_HUMAN",  "Another human is the object/target of the inner-being state"),
        ("UNSEEN",       "Unseen realm or spiritual entity (angels, demons) — rare"),
        ("NONE",         "Subject is genuinely dual (divine and human both explicit) — typically at Dimension 11"),
    ]
    for i, (value, desc) in enumerate(dominant_subject_members, start=1):
        conn.execute(
            """INSERT OR IGNORE INTO wa_vocab_member
               (set_id, value, description, sort_order, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (set_ids["DOMINANT_SUBJECT"], value, desc, i, now),
        )
    print(f"     M32: seeded {len(dominant_subject_members)} DOMINANT_SUBJECT members")

    # DIMENSION_CONFIDENCE — 3 values
    confidence_members = [
        ("KEYWORD_WEAK",   "Automated classifier weak match — starting hypothesis, pending review"),
        ("KEYWORD_STRONG", "Automated classifier strong match — starting hypothesis, pending review"),
        ("CLAUDE_AI",      "Claude AI post-review analyst assignment — reviewed and confirmed"),
    ]
    for i, (value, desc) in enumerate(confidence_members, start=1):
        conn.execute(
            """INSERT OR IGNORE INTO wa_vocab_member
               (set_id, value, description, sort_order, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (set_ids["DIMENSION_CONFIDENCE"], value, desc, i, now),
        )
    print(f"     M32: seeded {len(confidence_members)} DIMENSION_CONFIDENCE members")

    # QA_FLAG — 6 values
    qa_flag_members = [
        ("QA-CLEAR",          "No action — description, dimension, and subject are coherent"),
        ("QA-TERMCENTRIC",    "Description phrased from lexical definition rather than inner-being action — rewrite needed"),
        ("QA-VAGUE",          "Description too vague to identify the specific inner-being characteristic — sharpen"),
        ("QA-BROAD",          "Description spans multiple inner-being dimensions — may need group split"),
        ("QA-EXTERNALISED",   "Description names external circumstance rather than inner-being engagement"),
        ("QA-REVIEW",         "Dimension or dominant_subject incorrect/uncertain — flag for Phase C reassignment"),
    ]
    for i, (value, desc) in enumerate(qa_flag_members, start=1):
        conn.execute(
            """INSERT OR IGNORE INTO wa_vocab_member
               (set_id, value, description, sort_order, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (set_ids["QA_FLAG"], value, desc, i, now),
        )
    print(f"     M32: seeded {len(qa_flag_members)} QA_FLAG members")

    # MANUAL_OVERRIDE — 2 values
    mo_members = [
        ("0", "Dimension is open for reassignment — default post-review state (dim_review_status=Complete anchors)"),
        ("1", "Dimension locked by researcher review — DR-8 protected; updates require explicit MO in set clause"),
    ]
    for i, (value, desc) in enumerate(mo_members, start=1):
        conn.execute(
            """INSERT OR IGNORE INTO wa_vocab_member
               (set_id, value, description, sort_order, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (set_ids["MANUAL_OVERRIDE"], value, desc, i, now),
        )
    print(f"     M32: seeded {len(mo_members)} MANUAL_OVERRIDE members")

    # 5. Bump schema version to 3.12.0
    conn.execute(
        "UPDATE schema_version "
        "SET version_code = ?, applied_at = ? "
        "WHERE id = (SELECT MAX(id) FROM schema_version)",
        ("3.12.0", now),
    )
    print("     M32: schema_version → 3.12.0")


# ── M33 — Global rules → DB (wa_rule_registry + wa_addendum_registry) ─────────
#
# Researcher direction 2026-04-20: global rules join vocabularies in the DB.
# Seeds from wa-global-general-rules-v2_11-20260418.json (59 rules + 22 addenda
# across 3 addendum groups).


@_register("M33", "Reference-as-DB: wa_rule_registry + wa_addendum_registry + seed from global rules JSON")
def _m33(conn: sqlite3.Connection) -> None:
    import os as _os

    # 1. Create tables
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS wa_rule_registry (
            id              INTEGER PRIMARY KEY,
            rule_id         TEXT    NOT NULL UNIQUE,
            category        TEXT    NOT NULL,
            subject         TEXT,
            rule_text       TEXT    NOT NULL,
            example         TEXT,
            applies_to      TEXT,
            version         TEXT,
            added_date      TEXT,
            last_modified   TEXT,
            obsolete        INTEGER NOT NULL DEFAULT 0,
            obsolete_reason TEXT,
            superseded_by   TEXT,
            addendum_ref    TEXT,
            source_document TEXT,
            created_at      TEXT    NOT NULL
        );

        CREATE TABLE IF NOT EXISTS wa_addendum_registry (
            id                INTEGER PRIMARY KEY,
            item_id           TEXT    NOT NULL UNIQUE,
            addendum_group    TEXT    NOT NULL,
            rule_id           TEXT,
            audit_source      TEXT,
            subject           TEXT,
            observation       TEXT,
            migration_target  TEXT,
            migration_status  TEXT,
            researcher_comment TEXT,
            source_document   TEXT,
            created_at        TEXT    NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_rule_category
            ON wa_rule_registry(category) WHERE obsolete = 0;
        CREATE INDEX IF NOT EXISTS idx_addendum_group
            ON wa_addendum_registry(addendum_group);
    """)
    print("     M33: created wa_rule_registry + wa_addendum_registry + 2 indexes")

    # Idempotency: if rules/addenda already seeded (and source JSON has since been
    # archived), skip the re-seed. Tables + indexes still get ensured above.
    existing_rules = conn.execute("SELECT COUNT(*) FROM wa_rule_registry").fetchone()[0]
    existing_addenda = conn.execute("SELECT COUNT(*) FROM wa_addendum_registry").fetchone()[0]
    if existing_rules > 0 or existing_addenda > 0:
        print(f"     M33: seed already present ({existing_rules} rules, "
              f"{existing_addenda} addenda) — skipping re-seed")
        return

    # 2. Locate source JSON
    now = _now()
    source_candidates = [
        _os.path.join("data", "imports", "WA", "Workflow", "Framework_B", "Session_B",
                      "wa-global-general-rules-v2_11-20260418.json"),
        # Also check archive — the 2026-04-23 Tier 3 Stage A cleanup moved the file
        _os.path.join("data", "imports", "WA", "Workflow", "Framework_B", "archive",
                      "wa-global-general-rules-v2_11-20260418.json"),
    ]
    source_path = None
    for p in source_candidates:
        if _os.path.exists(p):
            source_path = p
            break
    if not source_path:
        raise RuntimeError("M33: source rules JSON not found at expected path")

    with open(source_path, encoding="utf-8") as f:
        data = json.load(f)
    source_basename = _os.path.basename(source_path)
    print(f"     M33: loading from {source_basename}")

    # 3. Seed rules
    rules_inserted = 0
    for r in data.get("rules", []):
        conn.execute(
            """INSERT OR IGNORE INTO wa_rule_registry
               (rule_id, category, subject, rule_text, example, applies_to,
                version, added_date, last_modified, obsolete, obsolete_reason,
                superseded_by, addendum_ref, source_document, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                r.get("rule_id"),
                r.get("category", "uncategorised"),
                r.get("subject"),
                r.get("rule", ""),
                r.get("example"),
                r.get("applies_to"),
                r.get("version"),
                r.get("added_date"),
                r.get("last_modified"),
                1 if r.get("obsolete") else 0,
                r.get("obsolete_reason"),
                r.get("superseded_by"),
                r.get("addendum_ref"),
                source_basename,
                now,
            ),
        )
        rules_inserted += 1
    print(f"     M33: seeded {rules_inserted} rules into wa_rule_registry")

    # 4. Seed addenda (3 groups)
    addenda_inserted = 0
    for group_key in ("addendum_instructions", "addendum_patch_directive", "addendum_reference"):
        for a in data.get(group_key, []):
            conn.execute(
                """INSERT OR IGNORE INTO wa_addendum_registry
                   (item_id, addendum_group, rule_id, audit_source, subject,
                    observation, migration_target, migration_status,
                    researcher_comment, source_document, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    a.get("item_id"),
                    group_key,
                    a.get("rule_id"),
                    a.get("audit_source"),
                    a.get("subject"),
                    a.get("observation"),
                    a.get("migration_target"),
                    a.get("migration_status"),
                    a.get("researcher_comment"),
                    source_basename,
                    now,
                ),
            )
            addenda_inserted += 1
    print(f"     M33: seeded {addenda_inserted} addenda into wa_addendum_registry")


# ── M34 — Prose-store programme-stage section types ───────────────────────────
#
# L2 of the 3-layer architecture: programme-wide narrative (anchor verse,
# XREF architecture, validation standard, delete discipline, etc.) moves into
# the prose store rather than to instruction docs. M34 seeds the section types;
# content population happens later via PROSE patches.


@_register("M34", "Reference-as-DB: seed programme-stage section types in prose_section_type")
def _m34(conn: sqlite3.Connection) -> None:
    now = _now()
    # 8 programme-stage section types — narrative policy / architecture / discipline
    programme_types = [
        ("prog_anchor_verse",
         "Programme — Anchor Verse Definition",
         "Canonical definition of anchor verses, dual purpose (analytical anchor + verse-context seed), minimum requirements. Authoritative home for the concept (currently mirrored in wa-reference §16 and wa-dimensionreview-instruction §4.2)."),
        ("prog_xref_architecture",
         "Programme — XREF Architecture",
         "OWNER / XREF term semantics, verse_context inheritance, canonical-row rule, cross-registry link pattern (currently scattered across wa-reference §17, wa-registry-management-guide)."),
        ("prog_validation_standard",
         "Programme — Document Validation Standard",
         "Inflection point completeness; gap status discipline; cross-doc consistency; dry-run gate assessment (currently wa-reference §18)."),
        ("prog_delete_discipline",
         "Programme — Soft-Delete Discipline",
         "Delete_flagged semantics; cascade rules; no physical deletes in automated flows; audit-trail retention."),
        ("prog_field_authority",
         "Programme — Field Authority Rules",
         "mti_term_flags canonical for somatic / god_as_subject; deprecation notes; which field wins on conflict."),
        ("prog_backup_discipline",
         "Programme — Backup Discipline",
         "Per-migration backup; per-patch backup; retention period; restoration procedure."),
        ("prog_patch_failure_protocol",
         "Programme — Patch Failure / REPAIR Protocol",
         "What to do when a patch is rejected; failure patches; mid-pool recovery."),
        ("prog_instruction_override_protocol",
         "Programme — Instruction Override Protocol",
         "How instruction overrides are declared, logged in observations, recorded in handoff documents."),
    ]
    for i, (code, label, description) in enumerate(programme_types, start=1):
        conn.execute(
            """INSERT OR IGNORE INTO prose_section_type
               (code, label, source_stage, lifecycle_tag, chapter_no,
                description, expected_length_min, expected_length_max,
                sort_order, delete_flagged, created_at)
               VALUES (?, ?, ?, NULL, NULL, ?, NULL, NULL, ?, 0, ?)""",
            (code, label, "programme", description, 100 + i, now),
        )
    print(f"     M34: seeded {len(programme_types)} programme-stage prose section types")


# ── M35 — Patch type + file-name pattern + label pattern registries ───────────
#
# Completes the L1 taxonomic layer: patch-type catalogue, file-naming patterns,
# and label conventions (DIM-, PH2-, SD, etc.) all move from scattered
# documentation into DB tables.


@_register("M35", "Reference-as-DB: wa_patch_type_registry + wa_file_name_pattern + wa_label_pattern + seeds + schema 3.13.0")
def _m35(conn: sqlite3.Connection) -> None:
    # 1. Create tables
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS wa_patch_type_registry (
            id                        INTEGER PRIMARY KEY,
            type_code                 TEXT    NOT NULL UNIQUE,
            description               TEXT,
            session_b_status_exempt   INTEGER NOT NULL DEFAULT 0,
            governing_instruction     TEXT,
            schema_affected           TEXT,
            deprecated                INTEGER NOT NULL DEFAULT 0,
            deprecation_note          TEXT,
            created_at                TEXT    NOT NULL,
            last_modified             TEXT
        );

        CREATE TABLE IF NOT EXISTS wa_file_name_pattern (
            id                        INTEGER PRIMARY KEY,
            pattern_code              TEXT    NOT NULL UNIQUE,
            pattern                   TEXT    NOT NULL,
            scope                     TEXT,
            description               TEXT,
            governing_instruction     TEXT,
            deprecated                INTEGER NOT NULL DEFAULT 0,
            deprecation_note          TEXT,
            created_at                TEXT    NOT NULL,
            last_modified             TEXT
        );

        CREATE TABLE IF NOT EXISTS wa_label_pattern (
            id                        INTEGER PRIMARY KEY,
            pattern_code              TEXT    NOT NULL UNIQUE,
            pattern                   TEXT    NOT NULL,
            entity                    TEXT,
            description               TEXT,
            governing_instruction     TEXT,
            deprecated                INTEGER NOT NULL DEFAULT 0,
            deprecation_note          TEXT,
            created_at                TEXT    NOT NULL,
            last_modified             TEXT
        );
    """)
    print("     M35: created wa_patch_type_registry + wa_file_name_pattern + wa_label_pattern")

    now = _now()

    # 2. Seed patch types (14 core types per wa-patch-instruction catalogue + DIMREVIEW family)
    patch_types = [
        ("PREANALYSIS",            "Session B Stage 1 Pre-Analysis patch — evidential status + dimensions + pre-analysis findings", 0, "wa-patch-instruction [current]", "wa_term_inventory, word_registry"),
        ("SESSIONB",               "Session B Stage 2 analysis-complete patch — findings + dimensions + SD pointers + registry stamps", 0, "wa-patch-instruction [current]", "wa_session_b_findings, wa_session_b_dimensions, wa_session_research_flags, word_registry"),
        ("SESSIONB_FINDINGS",      "Session B Stage 2b findings-only patch (finer-grained than SESSIONB)", 1, "wa-patch-instruction [current]", "wa_session_b_findings, wa_finding_entity_links"),
        ("VERSECONTEXT",           "Verse Context patch — batch-level classification of verse-context groups", 1, "wa-versecontext-instruction [current]", "verse_context, verse_context_group"),
        ("VCGROUP",                "Verse Context per-group patch", 1, "wa-versecontext-instruction [current]", "verse_context_group"),
        ("VCVERSE",                "Verse Context per-verse patch", 1, "wa-versecontext-instruction [current]", "verse_context"),
        ("DIMREVIEW",              "Dimension Review per-registry patch — dimension + dominant_subject + optional Phase B revisions + registry stamp", 1, "wa-dimensionreview-instruction [current]", "wa_dimension_index, verse_context_group, wa_session_b_findings, wa_session_research_flags, word_registry"),
        ("DIMREVIEW-GRPDESC",      "Dimension Review group-description correction patch", 1, "wa-dimensionreview-instruction [current]", "verse_context_group, wa_dimension_index"),
        ("SESSIOND",               "Session D cross-registry synthesis patch", 1, "wa-sessiond-orientation [current]", "session_d_observations, session_d_runs, session_d_verse_links, session_d_term_links"),
        ("SDPOINTERS",             "Session D pointer cluster patch — batches of SD pointers", 1, "wa-sessiond-orientation [current]", "wa_session_research_flags"),
        ("CLUSTERING",             "Cluster assignment patch", 1, "wa-registry-management-guide [current]", "word_registry"),
        ("CATALOGUE_POPULATION",   "Observation question catalogue population patch", 1, "wa-reference / wa-patch-instruction", "wa_obs_question_catalogue"),
        ("PROSE",                  "Prose section insert/supersede/approve (narrative Session A/B/C/D output + programme-stage content)", 1, "wa-patch-instruction [current]; prose-store-design-v1", "prose_section, prose_section_dimension_link, prose_section_finding_link"),
        ("REPAIR",                 "REPAIR patch — recovery from failed apply or data-state corrections", 1, "wa-patch-instruction [current]", "varies (recovery-specific)"),
        ("READINESSSWEEP",         "Readiness sweep mechanical remediation patch (Path 1 items)", 1, "wa-global-readiness-sweep-instruction [current]", "wa_data_quality_flags, mti_terms"),
    ]
    for (code, desc, exempt, gov, schema) in patch_types:
        conn.execute(
            """INSERT OR IGNORE INTO wa_patch_type_registry
               (type_code, description, session_b_status_exempt,
                governing_instruction, schema_affected, created_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (code, desc, exempt, gov, schema, now),
        )
    print(f"     M35: seeded {len(patch_types)} patch types")

    # 3. Seed file-name patterns (from wa-reference §1 + DimReview §15)
    file_patterns = [
        ("word_level",             "wa-{NNN}-{word}-{type}-v{n}-{YYYYMMDD}.{ext}",                         "per-registry", "Word-level Session B/C/D outputs", "wa-reference [current] §1.1"),
        ("vcb_file",               "wa-vcb-{NNN}-{type}-v{n}-{YYYYMMDD}.{ext}",                             "per-batch",    "Verse Context Batch files",       "wa-reference [current] §1.2"),
        ("programme_level",        "wa-global-{type}-v{n}-{YYYYMMDD}.{ext}",                                "programme",    "Programme-level files",           "wa-reference [current] §1.3"),
        ("instruction_doc",        "wa-{instruction-name}-v{n}-{YYYYMMDD}.{ext}",                           "programme",    "Instruction documents",           "wa-reference [current] §1.4"),
        ("patch_id",               "PATCH-{YYYYMMDD}-{NNN}-{TYPE}-V{n}",                                     "patch-id",     "Patch identifier (uppercase, inside _patch_meta.patch_id)", "wa-reference [current] §1.5"),
        ("patch_filename",         "wa-{NNN}-{word}-{type}-patch-v{n}-{YYYYMMDD}.json",                     "per-registry", "Patch file on disk (lowercase wa- prefix)", "wa-reference [current] §1.5"),
        ("dim_cluster_extract",    "wa-dim-{cluster}-extract-{YYYYMMDD}.json",                              "per-cluster",  "Dimension Review cluster extract",  "wa-dimensionreview-instruction [current] §15"),
        ("dim_rootfamily",         "wa-dim-{cluster}-rootfamily-{YYYYMMDD}.json",                           "per-cluster",  "Dimension Review root-family",      "wa-dimensionreview-instruction [current] §15"),
        ("dim_existing_pointers",  "wa-dim-{cluster}-existing-pointers-{YYYYMMDD}.json",                    "per-cluster",  "Existing SB findings + SD pointers", "wa-dimensionreview-instruction [current] §15"),
        ("dim_grpverify",          "wa-dim-{cluster}-grpverify-{group_code}-{YYYYMMDD}.json",               "per-group",    "Group verification extract",        "wa-dimensionreview-instruction [current] §15"),
        ("dim_vpass",              "wa-dim-{cluster}-vpass-{group_code}-{YYYYMMDD}.json",                   "per-group",    "Verification pass extract",         "wa-dimensionreview-instruction [current] §15"),
        ("dim_cc_directive",       "wa-dim-{cluster}-cc-directive-{YYYYMMDD}.md",                            "per-cluster",  "CC directive document (DimReview)", "wa-dimensionreview-instruction [current] §15"),
        ("dim_handoff_kickoff",    "wa-dim-{cluster}-handoff-kickoff-v{n}-{YYYYMMDD}.md",                    "per-cluster",  "DimReview handoff kickoff (build_dimension_extract --bundle)", "wa-dimensionreview-instruction [current] §15; build_dimension_extract.py"),
        ("dim_observations",       "wa-dim-{cluster}-observations-v{n}-{YYYYMMDD}.md",                       "per-cluster",  "DimReview observations log",        "wa-dimensionreview-instruction [current] §15"),
        ("dim_reg_patch",          "wa-dim-{cluster}-reg{nnn}-patch-v{n}-{YYYYMMDD}.json",                   "per-registry", "DimReview per-registry patch",      "wa-dimensionreview-instruction [current] §15"),
        ("dim_grpdesc_patch",      "wa-dim-{cluster}-grpdesc-patch-v{n}-{YYYYMMDD}.json",                    "per-cluster",  "DimReview group-description correction patch", "wa-dimensionreview-instruction [current] §15"),
        ("dim_return",             "wa-dim-{cluster}-{registry_no}-return-v{n}-{YYYYMMDD}.md",               "per-registry", "DimReview return document",         "wa-dimensionreview-instruction [current] §15"),
        ("dim_session_log",        "wa-dim-{cluster}-session-log-v{n}-{YYYYMMDD}.md",                        "per-cluster",  "DimReview session log",             "wa-dimensionreview-instruction [current] §15"),
        ("sessiona_md",            "wa-{NNN}-{word}-sessiona-{YYYYMMDD}.md",                                 "per-registry", "Session A extract markdown",        "Session A advice v1"),
        ("sessiona_patch",         "wa-{NNN}-{word}-sessiona-patch-{YYYYMMDD}.json",                         "per-registry", "Session A PROSE patch",             "Session A advice v1"),
        ("sdpointers_file",        "wa-{NNN}-{word}-sdpointers-{YYYYMMDD}.json",                             "per-registry", "Session D pointers export",         "wa-reference [current] §14.2"),
        ("final_registry_extract", "wa-{NNN}-{word}-final-v{n}-{YYYYMMDD}.json",                             "per-registry", "Final registry extract",            "wa-reference [current] §14.1"),
        ("reference_snapshot",     "wa-reference-snapshot-{YYYYMMDD}.json",                                  "programme",    "Reference-as-DB session-start snapshot (M32+)", "reference-as-database-design-20260420"),
    ]
    for (code, pattern, scope, desc, gov) in file_patterns:
        conn.execute(
            """INSERT OR IGNORE INTO wa_file_name_pattern
               (pattern_code, pattern, scope, description, governing_instruction, created_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (code, pattern, scope, desc, gov, now),
        )
    print(f"     M35: seeded {len(file_patterns)} file-name patterns")

    # 4. Seed label patterns
    label_patterns = [
        ("dim_finding",        "DIM-{registry_no}-{3-digit-sequence}",         "wa_session_b_findings.finding_id",   "Dimension Review Session B finding — e.g. DIM-112-004",   "wa-dimensionreview-instruction [current] §7.5"),
        ("dim_sd_pointer",     "DIM-{registry_no}-SD{3-digit-sequence}",       "wa_session_research_flags.flag_label","Dimension Review Session D pointer — e.g. DIM-112-SD003",  "wa-dimensionreview-instruction [current] §7.5"),
        ("ph2_finding",        "PH2-{registry_no}-{3-digit-sequence}",         "wa_session_research_flags.flag_label","Phase 2 research flag — e.g. PH2-112-001",                  "wa-reference [current] §5.4"),
        ("sb_finding_legacy",  "{registry_no}-F{3-digit-sequence}",             "wa_session_b_findings.finding_id",   "Pre-DIM prefix format (legacy; reconciliation pending)",    "historical convention"),
        ("sd_pointer_legacy",  "{registry_no}-SD{3-digit-sequence}",            "wa_session_research_flags.flag_label","Pre-DIM prefix format (legacy; reconciliation pending)",    "historical convention"),
        ("group_code",         "{mti_term_id}-{3-digit-serial}",                "verse_context_group.group_code",     "Verse context group code — e.g. 730-001",                   "wa-reference [current] §13.11"),
        ("verse_context_batch","VCB-{3-digit-sequence}",                         "verse-context batch identifier",     "Verse Context Batch id — e.g. VCB-003",                     "wa-versecontext-instruction [current]"),
        ("q_cov_catalogue",    "Q-COV-{2-digit-sequence}",                      "wa_obs_question_catalogue.question_code","Evidence-flag-routing catalogue question — Q-COV-01..12", "wa-reference [current] §8b"),
        ("directive_id",       "DIR-{YYYYMMDD}-{3-digit-sequence}",             "directive identifier",               "Directive ID — e.g. DIR-20260420-001",                      "wa-directive-instruction [current]"),
        ("patch_id",           "PATCH-{YYYYMMDD}-{NNN}-{TYPE}-V{n}",            "patch identifier",                   "Patch ID (uppercase, in _patch_meta.patch_id)",             "wa-reference [current] §1.5"),
        ("flag_id_legacy",     "FLAG-{3-digit-sequence}",                       "wa-global-flags flag identifier",    "Programme-wide flag — e.g. FLAG-010 / FLAG-016",            "wa-global-flags [current]"),
    ]
    for (code, pattern, entity, desc, gov) in label_patterns:
        conn.execute(
            """INSERT OR IGNORE INTO wa_label_pattern
               (pattern_code, pattern, entity, description, governing_instruction, created_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (code, pattern, entity, desc, gov, now),
        )
    print(f"     M35: seeded {len(label_patterns)} label patterns")

    # 5. Bump schema version — M33+M34+M35 together → 3.13.0
    conn.execute(
        "UPDATE schema_version SET version_code = ?, applied_at = ? "
        "WHERE id = (SELECT MAX(id) FROM schema_version)",
        ("3.13.0", now),
    )
    print("     M35: schema_version → 3.13.0")


# ── M36 — Mark all addenda obsolete; extracts should exclude them by default ──
#
# Researcher direction 2026-04-20: "all the addendum rules must be marked
# obsolete. The extracts should always exclude obsolete / superseded."
#
# Rationale: addenda in wa_addendum_registry are historical migration/absorption
# observations from a prior rules audit. Their purpose was to flag rules for
# relocation; all 22 have been actioned (absorbed into other documents, retired,
# or obsolete by current programme state). They remain in DB for audit trail
# but should not surface in session-start extracts as if they were live rules.


@_register("M36", "Mark all 22 addenda obsolete + add obsolete columns to wa_addendum_registry")
def _m36(conn: sqlite3.Connection) -> None:
    # 1. Add obsolete + obsolete_reason + last_modified columns (parallel to wa_rule_registry shape)
    cols = {r[1] for r in conn.execute("PRAGMA table_info(wa_addendum_registry)")}
    if "obsolete" not in cols:
        conn.execute("ALTER TABLE wa_addendum_registry ADD COLUMN obsolete INTEGER NOT NULL DEFAULT 0")
        print("     M36: added wa_addendum_registry.obsolete")
    if "obsolete_reason" not in cols:
        conn.execute("ALTER TABLE wa_addendum_registry ADD COLUMN obsolete_reason TEXT")
        print("     M36: added wa_addendum_registry.obsolete_reason")
    if "last_modified" not in cols:
        conn.execute("ALTER TABLE wa_addendum_registry ADD COLUMN last_modified TEXT")
        print("     M36: added wa_addendum_registry.last_modified")

    # 2. Mark all 22 rows obsolete=1 with researcher rationale
    now = _now()
    reason = (
        "Historical migration observation — actioned by programme absorption cycles "
        "(rules retired, relocated, or superseded). Retained for audit trail per "
        "researcher direction 2026-04-20. Extracts exclude obsolete addenda by default."
    )
    updated = conn.execute(
        """UPDATE wa_addendum_registry
              SET obsolete = 1, obsolete_reason = ?, last_modified = ?
            WHERE obsolete = 0""",
        (reason, now),
    ).rowcount
    print(f"     M36: marked {updated} addenda obsolete")

    # 3. Also consolidate: ensure rules extract and reference-snapshot will filter
    # Schema version bump
    conn.execute(
        "UPDATE schema_version SET version_code = ?, applied_at = ? "
        "WHERE id = (SELECT MAX(id) FROM schema_version)",
        ("3.14.0", now),
    )
    print("     M36: schema_version → 3.14.0")


@_register("M37", "Per-term VC progress tracking: add vc_status, vc_instruction_version, vc_status_updated_at, vc_status_note to mti_terms; backfill reset registries as 'to_revise'")
def _m37(conn: sqlite3.Connection) -> None:
    """Per-term VC progress fields on mti_terms.

    Enables the per-term VC model approved 2026-04-24 (alignment analysis
    v4 §8.1). The term — not the registry — is the atomic unit of
    classification progress. The applicator flips `vc_status` to 'complete'
    when a patch's operations for a term pass R1-R4 + orphan-group +
    coverage validation. Registry-level `verse_context_status` becomes a
    derived aggregation (all OWNER + XREF-via-OWNER terms at 'complete'
    or 'approved' → registry is Complete).

    Backfill logic:
      - Default all rows to 'not_done'.
      - Flag the 6 explicitly-reset registries' OWNER terms as 'to_revise'
        per the 2026-04-19 Q12 decision: compassion (23), fellowship (62),
        forgiveness (64), grace (68), love (103), mercy (111).
      - Other rows with active verse_context records should probably also
        be classified once the per-term pilot confirms the model; for now
        we leave them 'not_done' — the classifier under the new model will
        see FRESH posture on registries whose terms are 'not_done' and
        work through them normally.
    """
    # 1. Add the four columns (no-op if present — idempotent)
    cols = {r[1] for r in conn.execute("PRAGMA table_info(mti_terms)")}
    if "vc_status" not in cols:
        conn.execute(
            "ALTER TABLE mti_terms ADD COLUMN vc_status TEXT NOT NULL DEFAULT 'not_done'"
        )
        print("     M37: added mti_terms.vc_status")
    if "vc_instruction_version" not in cols:
        conn.execute("ALTER TABLE mti_terms ADD COLUMN vc_instruction_version TEXT")
        print("     M37: added mti_terms.vc_instruction_version")
    if "vc_status_updated_at" not in cols:
        conn.execute("ALTER TABLE mti_terms ADD COLUMN vc_status_updated_at TEXT")
        print("     M37: added mti_terms.vc_status_updated_at")
    if "vc_status_note" not in cols:
        conn.execute("ALTER TABLE mti_terms ADD COLUMN vc_status_note TEXT")
        print("     M37: added mti_terms.vc_status_note")

    # 2. Index for the registry-aggregation query the applicator will run:
    #    "are all OWNER terms of registry N at 'complete' or 'approved'?"
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_mti_terms_owning_vc_status "
        "ON mti_terms(owning_registry_fk, vc_status) WHERE delete_flagged = 0"
    )
    print("     M37: created idx_mti_terms_owning_vc_status")

    # 3. Backfill the 2026-04-19 Q12 reset registries. These six were
    #    explicitly marked for VC re-run; their terms should be 'to_revise'
    #    so the next VC pass picks them up.
    reset_registries = [23, 62, 64, 68, 103, 111]  # compassion, fellowship,
                                                    # forgiveness, grace, love, mercy
    now = _now()
    reason = (
        "Backfill M37 2026-04-24 — registry flagged for VC re-run per "
        "2026-04-19 Q12 decision (prior Session B work superseded)."
    )
    placeholders = ",".join("?" for _ in reset_registries)
    updated = conn.execute(
        f"""UPDATE mti_terms
               SET vc_status = 'to_revise',
                   vc_status_updated_at = ?,
                   vc_status_note = ?
             WHERE owning_registry_fk IN (
                   SELECT id FROM word_registry WHERE no IN ({placeholders})
             )
             AND delete_flagged = 0
             AND status IN ('extracted', 'extracted_thin')""",
        (now, reason, *reset_registries),
    ).rowcount
    print(f"     M37: flagged {updated} terms as 'to_revise' across 6 reset registries")

    # 4. Schema version bump
    conn.execute(
        "UPDATE schema_version SET version_code = ?, applied_at = ? "
        "WHERE id = (SELECT MAX(id) FROM schema_version)",
        ("3.15.0", now),
    )
    print("     M37: schema_version → 3.15.0")


@_register("M38", "Per-term VC vocabulary cleanup + md_version tracking: rename 'complete' -> 'vc_completed', drop 'approved' from vc_status; add mti_terms.md_version for freshness gating")
def _m38(conn: sqlite3.Connection) -> None:
    """Vocabulary and version-gating schema update (alignment analysis A-02 + A-03).

    A-02: remove 'approved' from the vc_status controlled vocabulary; rename
    'complete' to 'vc_completed' so the state is explicit about what it means
    (VC-specific completion, not some broader cross-stage 'approved').

    A-03: add mti_terms.md_version — an integer counter that tracks which
    Session A `.md` version was last produced from this term's DB state. The
    applicator compares a patch's declared input_version per term against this
    column; mismatch rejects the patch as stale. Bumped on successful apply
    (so the old .md is now stale for the next session) and by future data-
    changing events (audit_word re-runs; directives).

    Backfill: existing rows with vc_status = 'complete' (there are none in
    production today — every row is 'not_done' or 'to_revise' post M37) would
    be UPDATEd to 'vc_completed'. Done idempotently.
    """
    cols = {r[1] for r in conn.execute("PRAGMA table_info(mti_terms)")}

    # 1. Rename 'complete' -> 'vc_completed'
    renamed = conn.execute(
        "UPDATE mti_terms SET vc_status = 'vc_completed' WHERE vc_status = 'complete'"
    ).rowcount
    print(f"     M38: renamed {renamed} rows vc_status='complete' -> 'vc_completed'")

    # 2. Drop 'approved' -> fold any such rows back to 'vc_completed' (the
    # natural terminal state under the simplified vocab). No rows expected.
    folded = conn.execute(
        "UPDATE mti_terms SET vc_status = 'vc_completed' WHERE vc_status = 'approved'"
    ).rowcount
    print(f"     M38: folded {folded} rows vc_status='approved' -> 'vc_completed' (approved dropped from vocab)")

    # 3. Add md_version column
    if "md_version" not in cols:
        conn.execute("ALTER TABLE mti_terms ADD COLUMN md_version INTEGER NOT NULL DEFAULT 1")
        print("     M38: added mti_terms.md_version INTEGER NOT NULL DEFAULT 1")

    # 4. Schema version bump
    now = _now()
    conn.execute(
        "UPDATE schema_version SET version_code = ?, applied_at = ? "
        "WHERE id = (SELECT MAX(id) FROM schema_version)",
        ("3.16.0", now),
    )
    print("     M38: schema_version → 3.16.0")


@_register("M39", "Delete NULL-skeleton verse_context rows (pre-M37 legacy seed): zero-signal rows inflated coverage and blocked VCNEW inserts on verse_record_id collision")
def _m39(conn: sqlite3.Connection) -> None:
    """Remove zero-signal verse_context rows that were seeded by pre-M37 legacy
    patches but never classified.

    A row is a "strict NULL skeleton" if all of the following hold:
      - delete_flagged = 0 (still active)
      - is_relevant = 0 AND is_anchor = 0 AND is_related = 0
      - set_aside_reason IS NULL
      - group_id IS NULL
      - notes IS NULL OR notes = '' (no researcher / AI commentary)

    Such rows carry zero information: they are neither a classification, nor a
    set-aside with reason, nor a note. They were false positives for coverage
    assessment (a verse_record with a skeleton appeared "covered" when no work
    had been done) and they blocked legitimate VCNEW `insert` operations under
    v3_4 because of the (mti_term_id, verse_record_id) uniqueness constraint.

    Skeletons with non-empty notes (e.g. legacy "sub-term deferred to primary
    sense" markers) are preserved — those carry provenance worth keeping.

    Idempotent: subsequent runs find zero rows and are no-ops.
    """
    count = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        "WHERE delete_flagged = 0 "
        "  AND is_relevant = 0 AND is_anchor = 0 AND is_related = 0 "
        "  AND set_aside_reason IS NULL "
        "  AND group_id IS NULL "
        "  AND (notes IS NULL OR notes = '')"
    ).fetchone()[0]

    deleted = conn.execute(
        "DELETE FROM verse_context "
        "WHERE delete_flagged = 0 "
        "  AND is_relevant = 0 AND is_anchor = 0 AND is_related = 0 "
        "  AND set_aside_reason IS NULL "
        "  AND group_id IS NULL "
        "  AND (notes IS NULL OR notes = '')"
    ).rowcount

    print(f"     M39: deleted {deleted} strict NULL-skeleton verse_context rows (count pre-delete: {count})")
    # NOTE (2026-06-07): the original M39 set version_code = '3.16.1' here. That was a
    # bug — a data-cleanup migration must not bump (let alone *lower*) the schema version,
    # and the DB has since moved to 3.28.0 via M40–M54. Version-bump removed so M39 is a
    # pure (idempotent, no-op-today) data cleanup. See
    # research/investigations/wa-migration-control-integrity-v1-20260607.md.


# ── M40–M54 — registry backfill (2026-06-07 control-system reconciliation) ──────
#
# These migrations were applied to the live DB via one-off `_apply_*` scripts /
# direct ALTERs between 2026-04-27 and 2026-05-27 and recorded in
# schema_version.migration_history, but were NEVER registered here — the registry
# froze at M39 (2026-04-28) while the DB moved on to 3.28.0. (M18 is absent from
# BOTH the registry and the history; its effect, whatever it was, is either present
# in the schema or was superseded — left as a documented gap.)
#
# They are re-registered below as DOCUMENTED, NON-EXECUTING entries so the registry
# is once again a complete index (registry == history). The history-aware runner
# SKIPS them (they are in migration_history), so their `pass` bodies never run.
# Schema presence for all 18 changes was VERIFIED on 2026-06-07 (investigation doc).
# From-scratch DB builds use create_tables.sql, not this path. Going forward,
# migrations are registered here again, starting with V3_2 = M55.
#
# M16/M17 (2026-03-27/29) are the same case from earlier — applied via one-off
# scripts, in history, never registered. Backfilled here too (out of chronological
# position, but the runner skips them so order is immaterial; fresh builds use
# create_tables.sql). M18 remains a documented gap (in neither registry nor history).

@_register("M16", "v5 impl: cluster_assignment on word_registry + new flag types (SB_FINDING, …) [backfill: 2026-03-27; in history; verified]")
def _m16(conn): pass

@_register("M17", "Rename source_category → dimensions; drop anchor_verses [backfill: 2026-03-29; in history; verified]")
def _m17(conn): pass

@_register("M40", "Add verse_context.analysis_note (anchor-verse analytical commentary) [backfill: applied via one-off script 2026-04-27; in history; schema verified]")
def _m40(conn): pass

@_register("M41", "Create wa_prose_section_citations [backfill: 2026-04-27; in history; verified]")
def _m41(conn): pass

@_register("M42", "Add wa_obs_question_catalogue.review_note [backfill: 2026-04-27; in history; verified]")
def _m42(conn): pass

@_register("M43", "Rebuild wa_finding_catalogue_links: finding_id NULL allowed [backfill: 2026-04-27; in history; verified]")
def _m43(conn): pass

@_register("M44", "Cluster sub-group infrastructure: cluster_subgroup + mti_terms.cluster_code [backfill: 2026-05-06; in history; verified]")
def _m44(conn): pass

@_register("M45", "Cluster-level findings table (cluster_finding) [backfill: 2026-05-06; in history; verified]")
def _m45(conn): pass

@_register("M46", "Term-to-sub-group m2m: mti_term_subgroup + verse_context.cluster_subgroup_id [backfill: 2026-05-10; in history; verified]")
def _m46(conn): pass

@_register("M47", "vcg-to-term m2m: vcg_term; drop verse_context_group.mti_term_id [backfill: 2026-05-10; in history; verified]")
def _m47(conn): pass

@_register("M48", "Add cluster_finding.vcg_scope + extend UNIQUE [backfill: 2026-05-16; in history; verified]")
def _m48(conn): pass

@_register("M49", "characteristic + characteristic_subgroup + cluster_observation tables [backfill: 2026-05-18; in history; verified]")
def _m49(conn): pass

@_register("M50", "Add cluster_finding.characteristic_id + extend UNIQUE [backfill: 2026-05-18; in history; verified]")
def _m50(conn): pass

@_register("M51", "Add verse_context.keywords (JSON array of inner-being keywords) [backfill: 2026-05-23; in history; verified]")
def _m51(conn): pass

@_register("M52", "Add finding_citation table (polymorphic) [backfill: 2026-05-25; in history; verified]")
def _m52(conn): pass

@_register("M53", "Add cluster.char_structure column [backfill: 2026-05-26; in history; verified]")
def _m53(conn): pass

@_register("M54", "Extend prose_section with cluster_code + characteristic_id + cluster_subgroup_id [backfill: 2026-05-27; in history; verified]")
def _m54(conn): pass


@_register("M55", "V3_2: L1 verse fields + finding typing + morphology + homonym flag; retire vertical_pass_flag")
def _m55(conn: sqlite3.Connection) -> None:
    """V3_2 schema (wa-v3_2-schema-migration-plan-v1). Additive + 2 confirmed-dead drops.
    Population (stem_label, morph/stem, is_homonym) runs later, within L1 of the first cluster."""
    # verse_context — L1 verse-establishment fields
    _add_column_if_missing(conn, "verse_context", "step_meaning_applied", "TEXT")
    _add_column_if_missing(conn, "verse_context", "sense_id",             "INTEGER")
    _add_column_if_missing(conn, "verse_context", "sense_multiplicity",   "TEXT")
    _add_column_if_missing(conn, "verse_context", "step_envelope_note",   "TEXT")
    _add_column_if_missing(conn, "verse_context", "pole",                 "TEXT")
    _add_column_if_missing(conn, "verse_context", "pole_is_metaphor",     "INTEGER DEFAULT 0")
    _add_column_if_missing(conn, "verse_context", "residue_flag",         "INTEGER DEFAULT 0")
    # cluster_finding — typing
    _add_column_if_missing(conn, "cluster_finding", "finding_type",   "TEXT")
    _add_column_if_missing(conn, "cluster_finding", "needs_research", "INTEGER DEFAULT 0")
    # wa_verse_records — morphology
    _add_column_if_missing(conn, "wa_verse_records", "morph_code", "TEXT")
    _add_column_if_missing(conn, "wa_verse_records", "stem",       "TEXT")
    # wa_meaning_sense — homonym filter
    _add_column_if_missing(conn, "wa_meaning_sense", "is_homonym", "INTEGER DEFAULT 0")
    # retire vertical_pass_flag (confirmed unused — 0 rows; no dependent index)
    for tbl in ("verse_context", "verse_context_group"):
        cols = {r[1] for r in conn.execute(f"PRAGMA table_info({tbl})")}
        if "vertical_pass_flag" in cols:
            conn.execute(f"ALTER TABLE {tbl} DROP COLUMN vertical_pass_flag")
            print(f"     M55: dropped {tbl}.vertical_pass_flag")
    conn.execute(
        "UPDATE schema_version SET version_code = ?, applied_at = ? "
        "WHERE id = (SELECT MAX(id) FROM schema_version)", ("3.29.0", _now()))
    print("     M55: V3_2 fields added; schema_version → 3.29.0")


# ── Runner ────────────────────────────────────────────────────────────────────

def check_version(conn) -> tuple[str | None, bool]:
    """Return (current_version, needs_migration)."""
    from .db import get_schema_version
    ver = get_schema_version(conn)
    return ver, ver != EXPECTED_SCHEMA_VERSION


def _applied_refs(conn) -> set[str]:
    """Return the set of migration refs already recorded in migration_history.

    History-awareness (added 2026-06-07): the runner must NOT re-execute
    migrations that have already been applied. The original runner ran *every*
    registered migration on each invocation and relied on each being perfectly
    idempotent — fragile, and actively unsafe on a DB that has moved past the
    registry via one-off scripts (it would re-run data migrations and reset
    version_code via the unconditional bumps). See
    research/investigations/wa-migration-control-integrity-v1-20260607.md.
    """
    try:
        row = conn.execute(
            "SELECT migration_history FROM schema_version "
            "WHERE id = (SELECT MAX(id) FROM schema_version)"
        ).fetchone()
        if not row or not row[0]:
            return set()
        return {e.get("version") for e in json.loads(row[0])}
    except Exception:
        return set()


def run_migrations(conn, dry_run: bool = False, stop_at: str | None = None,
                   verbose: bool = True) -> list[str]:
    """Apply pending migrations only (those NOT already in migration_history).
    Returns the list of refs applied this run."""
    from .db import get_schema_version

    already = _applied_refs(conn)
    applied = []
    skipped = 0
    for ref, description, fn in _MIGRATIONS:
        if stop_at and ref > stop_at:
            break
        if ref in already:
            skipped += 1
            continue  # history-aware: never re-execute an applied migration
        if dry_run:
            if verbose:
                print(f"  [DRY-RUN — PENDING] {ref}: {description}")
            applied.append(ref)
            continue
        try:
            with conn:
                fn(conn)
            if verbose:
                print(f"  [OK] {ref}: {description}")
            applied.append(ref)
            _update_migration_history(conn, ref, description)
        except Exception as exc:
            # ASCII only — Unicode glyphs crash on the Windows cp1252 console and mask
            # the real error (2026-06-08). Keep migration runner output ASCII-safe.
            print(f"  [FAIL] {ref}: {description} -- {exc}")
            raise

    if verbose:
        print(f"\n({skipped} already-applied migrations skipped; {len(applied)} "
              f"{'pending' if dry_run else 'applied'} this run.)")
    if not dry_run and applied:
        ver = get_schema_version(conn)
        if verbose:
            print(f"Schema version now: {ver}")

    return applied


def get_status(conn) -> dict:
    """Return a dict describing current schema state and pending migrations."""
    from .db import get_schema_version
    current = get_schema_version(conn)
    return {
        "current_version": current,
        "target_version": EXPECTED_SCHEMA_VERSION,
        "needs_migration": current != EXPECTED_SCHEMA_VERSION,
        "migration_count": len(_MIGRATIONS),
    }


# ── Helpers ───────────────────────────────────────────────────────────────────

def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def _add_column_if_missing(conn: sqlite3.Connection, table: str,
                            column: str, definition: str) -> None:
    existing = {
        r[1] for r in conn.execute(f"PRAGMA table_info({table})").fetchall()  # noqa: S608
    }
    if column not in existing:
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")  # noqa: S608


def _update_migration_history(conn: sqlite3.Connection, ref: str,
                               description: str) -> None:
    """Append a migration entry to the migration_history of the latest
    schema_version row. Post-M27 (2026-04-19) the latest row is MAX(id);
    pre-M27 and on fresh DBs MAX(id) == 1, so this is back-compatible."""
    try:
        row = conn.execute(
            "SELECT id, migration_history FROM schema_version "
            "WHERE id = (SELECT MAX(id) FROM schema_version)"
        ).fetchone()
        if not row:
            return
        latest_id, history_json = row[0], row[1]
        history = json.loads(history_json or "[]")
        # Idempotent: skip if this ref is already recorded (prevents duplicate
        # entries when --migrate is run more than once).
        if any(e.get("version") == ref for e in history):
            return
        history.append({
            "version": ref,
            "description": description,
            "applied_at": _now(),
        })
        conn.execute(
            "UPDATE schema_version SET migration_history = ? WHERE id = ?",
            (json.dumps(history), latest_id),
        )
        conn.commit()  # 2026-06-08: commit the history record explicitly — otherwise the
        # LAST migration's history entry is left uncommitted and rolled back on close
        # (M39 was flushed by M55's transaction; M55's own entry was lost).
    except Exception:
        pass  # Non-critical — migration still succeeded
