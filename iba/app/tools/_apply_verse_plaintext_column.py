"""One-time (idempotent) correction: add verse.text = plain-text of verse.preview.

verse.preview holds STEP HTML (morph/strong word spans + a leading verse-number
span). That HTML is retained (span data derives from it); this adds a sibling
`text` column carrying clean, tag-free verse text for reports/exports.

Safe to re-run: adds the column only if missing and repopulates every row.

Registered 2026-09-10 (escalation #1662): the derivation itself moved to
lib/stepapi.py:preview_to_text (single source of truth, also now called at
insert time by handlers/raw.py:verses_one) -- this script re-imports it rather
than keeping its own copy, and stays useful as the catch-up backfill for any
row ingestion left behind (e.g. rows written before that wiring existed).

Usage:
    python iba/app/tools/_apply_verse_plaintext_column.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from iba.app.lib.stepapi import preview_to_text as to_text  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def column_exists(cur, table: str, col: str) -> bool:
    return any(r[1] == col for r in cur.execute(f"PRAGMA table_info({table})"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute("BEGIN")
        if not column_exists(cur, "verse", "text"):
            cur.execute("ALTER TABLE verse ADD COLUMN text TEXT")
            print("ADDED COLUMN verse.text")
        else:
            print("COLUMN verse.text already present")

        rows = cur.execute("SELECT id, preview FROM verse").fetchall()
        updates = [(to_text(r["preview"]), r["id"]) for r in rows]
        cur.executemany("UPDATE verse SET text = ? WHERE id = ?", updates)
        print(f"POPULATED verse.text for {len(updates)} rows")

        sample = cur.execute(
            "SELECT reference, text FROM verse "
            "WHERE reference LIKE 'Rom %' AND deleted=0 ORDER BY id LIMIT 3"
        ).fetchall()

        if args.dry_run:
            conn.rollback()
            print("DRY-RUN: rolled back")
        else:
            conn.commit()
            print("COMMITTED")

        for s in sample:
            print(f"  {s['reference']}: {s['text']}")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
