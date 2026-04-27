"""_apply_M43_finisher_v1_20260427.py

M40/M41/M42 already applied (DDL implicit-commit during prior dry-run).
This finisher applies M43 (wa_finding_catalogue_links rebuild for finding_id NULL)
and bumps schema_version to 3.17.0 with the full M40-M43 history record.
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR, "bible_research_pre_M43_finisher_20260427.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)

    # Pre-state checks
    fid = next((r for r in conn.execute("PRAGMA table_info(wa_finding_catalogue_links)").fetchall()
                if r[1] == "finding_id"), None)
    if not fid:
        print("ERROR: wa_finding_catalogue_links.finding_id missing")
        return 2
    if fid[3] == 0:
        print("M43 already applied (finding_id NULL allowed). Will only update schema_version.")
        m43_needed = False
    else:
        print("M43 needs to apply (finding_id currently NOT NULL).")
        m43_needed = True

    if args.live:
        print("\n--- LIVE ---")
    else:
        print("\n--- DRY-RUN (no commit) ---")

    if m43_needed:
        if args.live:
            conn.execute("PRAGMA foreign_keys = OFF")
            try:
                conn.execute("""
                    CREATE TABLE wa_finding_catalogue_links_new (
                        id              INTEGER  PRIMARY KEY AUTOINCREMENT,
                        finding_id      INTEGER  REFERENCES wa_session_b_findings(id),
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
                    SELECT id, finding_id, question_id, coverage, status, pattern_type,
                           mapped_date, validated_date, validated_by, session_b_note, delete_flagged
                      FROM wa_finding_catalogue_links
                """)
                conn.execute("DROP TABLE wa_finding_catalogue_links")
                conn.execute("ALTER TABLE wa_finding_catalogue_links_new RENAME TO wa_finding_catalogue_links")
                conn.commit()
                print("M43 applied: wa_finding_catalogue_links rebuilt with finding_id NULL allowed")
            finally:
                conn.execute("PRAGMA foreign_keys = ON")

    # Schema version bump
    cur = conn.execute("SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1")
    current = cur.fetchone()[0]
    print(f"\nCurrent schema_version: {current}")

    if current != NEW_SCHEMA_VERSION:
        # Build migration_history with M40-M43 appended
        row = conn.execute("SELECT migration_history FROM schema_version ORDER BY id DESC LIMIT 1").fetchone()
        history = json.loads(row[0]) if row and row[0] else []
        ts = now_iso()
        for m, desc in [
            ("M40", "Add verse_context.analysis_note (anchor-verse analytical commentary)"),
            ("M41", "Create wa_prose_section_citations (chapter ↔ findings/Q&As/SD pointers/observations index)"),
            ("M42", "Add wa_obs_question_catalogue.review_note (catalogue maintenance notes)"),
            ("M43", "Rebuild wa_finding_catalogue_links: finding_id NULL allowed (for no_finding / not_applicable coverage rows)"),
        ]:
            history.append({"version": m, "description": desc, "applied_at": ts})

        if args.live:
            conn.execute(
                "INSERT INTO schema_version (version_code, applied_at, migration_history) VALUES (?, ?, ?)",
                (NEW_SCHEMA_VERSION, ts, json.dumps(history, ensure_ascii=False)),
            )
            conn.commit()
            print(f"schema_version bumped to {NEW_SCHEMA_VERSION}")
        else:
            print(f"[DRY-RUN] would bump schema_version to {NEW_SCHEMA_VERSION}")

    # Verify
    print("\n--- Verification ---")
    fid = next((r for r in conn.execute("PRAGMA table_info(wa_finding_catalogue_links)").fetchall()
                if r[1] == "finding_id"), None)
    print(f"  finding_id notnull: {fid[3]} (expected 0)")
    cur = conn.execute("SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1")
    print(f"  schema_version: {cur.fetchone()[0]}")
    print(f"  wa_finding_catalogue_links rows: {conn.execute('SELECT COUNT(*) FROM wa_finding_catalogue_links').fetchone()[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
