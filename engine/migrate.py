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

    conn.execute(
        "UPDATE schema_version SET version_code = ?, applied_at = ? WHERE id = 1",
        (EXPECTED_SCHEMA_VERSION, _now()),
    )


# ── Runner ────────────────────────────────────────────────────────────────────

def check_version(conn) -> tuple[str | None, bool]:
    """Return (current_version, needs_migration)."""
    from .db import get_schema_version
    ver = get_schema_version(conn)
    return ver, ver != EXPECTED_SCHEMA_VERSION


def run_migrations(conn, dry_run: bool = False, stop_at: str | None = None,
                   verbose: bool = True) -> list[str]:
    """Apply all pending migrations. Returns list of applied migration refs."""
    from .db import get_schema_version

    applied = []
    for ref, description, fn in _MIGRATIONS:
        if stop_at and ref > stop_at:
            break
        if dry_run:
            if verbose:
                print(f"  [DRY-RUN] {ref}: {description}")
            applied.append(ref)
            continue
        try:
            with conn:
                fn(conn)
            if verbose:
                print(f"  ✓ {ref}: {description}")
            applied.append(ref)
            _update_migration_history(conn, ref, description)
        except Exception as exc:
            print(f"  ✗ {ref}: {description} — FAILED: {exc}")
            raise

    if not dry_run and applied:
        ver = get_schema_version(conn)
        if verbose:
            print(f"\nSchema version now: {ver}")

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
    try:
        row = conn.execute(
            "SELECT migration_history FROM schema_version WHERE id = 1"
        ).fetchone()
        history = json.loads(row[0] or "[]")
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
            "UPDATE schema_version SET migration_history = ? WHERE id = 1",
            (json.dumps(history),),
        )
    except Exception:
        pass  # Non-critical — migration still succeeded
