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
    # This migration updates the version_code and records full migration history.
    # It runs last and its completion is the canonical signal that migration is done.
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
