"""_apply_M40_M43_db_capture_architecture_v1_20260427.py

Schema migrations M40-M43 for the DB Capture Architecture (Approach a)
per researcher decisions in
outputs/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md
Part 11.1 + Part 12 (locked 2026-04-27).

  M40 — ALTER TABLE verse_context ADD COLUMN analysis_note TEXT
        (anchor-verse analytical commentary returns to verse records)

  M41 — CREATE TABLE wa_prose_section_citations
        (chapter prose ↔ findings/Q&As/SD pointers/observations citation index;
         enables the chapter-data coherence audit)

  M42 — ALTER TABLE wa_obs_question_catalogue ADD COLUMN review_note TEXT
        (catalogue-question wording/validity notes — replaces the homeless
         "review notes" category)

  M43 — Rebuild wa_finding_catalogue_links: finding_id INTEGER NULL
        (was NOT NULL — change permits 'no_finding' / 'not_applicable'
         coverage rows that have no source observation)

Schema version bump: 3.16.1 → 3.17.0

Single transaction; pre-migration backup; verification queries after.
Run with --dry-run first; commits only with --live.
"""
from __future__ import annotations
import argparse
import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("data", "bible_research.db")
BACKUP_DIR = "backups"
NEW_SCHEMA_VERSION = "3.17.0"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    path = os.path.join(BACKUP_DIR, f"bible_research_pre_{label}_20260427.db")
    shutil.copy2(DB_PATH, path)
    return path


def migration_history_for_new_row(conn) -> str:
    """Read most-recent schema_version.migration_history and append M40-M43."""
    row = conn.execute(
        "SELECT migration_history FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()
    history = json.loads(row[0]) if row and row[0] else []
    new_entries = [
        {
            "version": "M40",
            "description": "Add verse_context.analysis_note (anchor-verse analytical commentary)",
            "applied_at": now_iso(),
        },
        {
            "version": "M41",
            "description": "Create wa_prose_section_citations (chapter ↔ findings/Q&As/SD pointers/observations index)",
            "applied_at": now_iso(),
        },
        {
            "version": "M42",
            "description": "Add wa_obs_question_catalogue.review_note (catalogue maintenance notes)",
            "applied_at": now_iso(),
        },
        {
            "version": "M43",
            "description": "Rebuild wa_finding_catalogue_links: finding_id NULL allowed (for no_finding / not_applicable coverage rows)",
            "applied_at": now_iso(),
        },
    ]
    history.extend(new_entries)
    return json.dumps(history, ensure_ascii=False)


def apply_M40(conn):
    print("M40: ALTER TABLE verse_context ADD COLUMN analysis_note TEXT")
    conn.execute("ALTER TABLE verse_context ADD COLUMN analysis_note TEXT")


def apply_M41(conn):
    print("M41: CREATE TABLE wa_prose_section_citations")
    conn.execute("""
        CREATE TABLE wa_prose_section_citations (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            prose_section_id    INTEGER NOT NULL REFERENCES prose_section(id),
            cited_finding_id    INTEGER REFERENCES wa_session_b_findings(id),
            cited_qa_link_id    INTEGER REFERENCES wa_finding_catalogue_links(id),
            cited_sd_pointer_id INTEGER REFERENCES wa_session_research_flags(id),
            cited_observation_seq TEXT,                -- e.g. 'OBS-026' as raw token from prose
            citation_form       TEXT NOT NULL,         -- the literal text in the prose
            paragraph_no        INTEGER,               -- optional: which paragraph in the section
            delete_flagged      INTEGER NOT NULL DEFAULT 0,
            created_at          TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
        )
    """)
    conn.execute("CREATE INDEX idx_psc_section ON wa_prose_section_citations(prose_section_id)")
    conn.execute("CREATE INDEX idx_psc_finding ON wa_prose_section_citations(cited_finding_id)")
    conn.execute("CREATE INDEX idx_psc_qa ON wa_prose_section_citations(cited_qa_link_id)")
    conn.execute("CREATE INDEX idx_psc_sd ON wa_prose_section_citations(cited_sd_pointer_id)")


def apply_M42(conn):
    print("M42: ALTER TABLE wa_obs_question_catalogue ADD COLUMN review_note TEXT")
    conn.execute("ALTER TABLE wa_obs_question_catalogue ADD COLUMN review_note TEXT")


def apply_M43(conn):
    """Rebuild wa_finding_catalogue_links to allow finding_id NULL.

    SQLite cannot relax NOT NULL via ALTER TABLE; standard 6-step procedure:
    """
    print("M43: Rebuild wa_finding_catalogue_links (finding_id NULL allowed)")
    conn.execute("PRAGMA foreign_keys = OFF")
    try:
        conn.execute("""
            CREATE TABLE wa_finding_catalogue_links_new (
                id              INTEGER  PRIMARY KEY AUTOINCREMENT,
                finding_id      INTEGER  REFERENCES wa_session_b_findings(id),  -- now NULL allowed
                question_id     INTEGER  NOT NULL REFERENCES wa_obs_question_catalogue(obs_id),
                coverage        TEXT,
                status          TEXT     NOT NULL DEFAULT 'suggested',
                pattern_type    TEXT,
                mapped_date     TEXT,
                validated_date  TEXT,
                validated_by    TEXT,
                session_b_note  TEXT,
                delete_flagged  INTEGER  NOT NULL DEFAULT 0,
                UNIQUE (finding_id, question_id)
            )
        """)
        conn.execute("""
            INSERT INTO wa_finding_catalogue_links_new
                (id, finding_id, question_id, coverage, status, pattern_type,
                 mapped_date, validated_date, validated_by, session_b_note, delete_flagged)
            SELECT
                id, finding_id, question_id, coverage, status, pattern_type,
                mapped_date, validated_date, validated_by, session_b_note, delete_flagged
              FROM wa_finding_catalogue_links
        """)
        conn.execute("DROP TABLE wa_finding_catalogue_links")
        conn.execute("ALTER TABLE wa_finding_catalogue_links_new RENAME TO wa_finding_catalogue_links")
    finally:
        conn.execute("PRAGMA foreign_keys = ON")


def update_schema_version(conn):
    print(f"Bumping schema_version to {NEW_SCHEMA_VERSION}")
    history = migration_history_for_new_row(conn)
    conn.execute(
        "INSERT INTO schema_version (version_code, applied_at, migration_history) VALUES (?, ?, ?)",
        (NEW_SCHEMA_VERSION, now_iso(), history),
    )


def verify(conn):
    """Read-back checks."""
    print("\n--- Verification ---")
    # M40
    cur = conn.execute("PRAGMA table_info(verse_context)")
    cols = [r[1] for r in cur.fetchall()]
    assert "analysis_note" in cols, f"M40 verify failed: analysis_note not in {cols}"
    print("  ✓ M40 — verse_context.analysis_note present")

    # M41
    cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='wa_prose_section_citations'")
    assert cur.fetchone(), "M41 verify failed: wa_prose_section_citations not found"
    cur = conn.execute("PRAGMA table_info(wa_prose_section_citations)")
    n_cols = len(list(cur.fetchall()))
    print(f"  ✓ M41 — wa_prose_section_citations created ({n_cols} cols)")

    # M42
    cur = conn.execute("PRAGMA table_info(wa_obs_question_catalogue)")
    cols = [r[1] for r in cur.fetchall()]
    assert "review_note" in cols, f"M42 verify failed: review_note not in {cols}"
    print("  ✓ M42 — wa_obs_question_catalogue.review_note present")

    # M43 — finding_id should now allow NULL (notnull=0)
    cur = conn.execute("PRAGMA table_info(wa_finding_catalogue_links)")
    finding_id_col = next((r for r in cur.fetchall() if r[1] == "finding_id"), None)
    assert finding_id_col is not None, "M43 verify failed: finding_id missing"
    assert finding_id_col[3] == 0, f"M43 verify failed: finding_id notnull={finding_id_col[3]} (expected 0)"
    print("  ✓ M43 — wa_finding_catalogue_links.finding_id NULL allowed")

    # Row count preserved
    cur = conn.execute("SELECT COUNT(*) FROM wa_finding_catalogue_links")
    print(f"  ✓ wa_finding_catalogue_links row count: {cur.fetchone()[0]} (was 0; should still be 0)")

    # Schema version
    cur = conn.execute("SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1")
    print(f"  ✓ schema_version now: {cur.fetchone()[0]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true", help="commit; default is dry-run")
    args = ap.parse_args()

    if args.live:
        backup = take_backup("M40_M43_db_capture_arch")
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        with conn:
            apply_M40(conn)
            apply_M41(conn)
            apply_M42(conn)
            apply_M43(conn)
            update_schema_version(conn)

            verify(conn)

            if not args.live:
                print("\n[DRY-RUN] rolling back.")
                raise sqlite3.IntegrityError("dry-run rollback (intentional)")
        print("\n[LIVE] migrations committed.")
    except sqlite3.IntegrityError as e:
        if args.live:
            raise
        # dry-run rollback path
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
