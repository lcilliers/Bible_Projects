"""One-time (idempotent) correction: add verse.text = plain-text of verse.preview.

verse.preview holds STEP HTML (morph/strong word spans + a leading verse-number
span). That HTML is retained (span data derives from it); this adds a sibling
`text` column carrying clean, tag-free verse text for reports/exports.

Safe to re-run: adds the column only if missing and repopulates every row.

Usage:
    python iba/scripts/_apply_verse_plaintext_column.py [--db PATH] [--dry-run]
"""
import argparse
import html
import re
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def to_text(preview: str) -> str:
    if not preview:
        return ""
    s = preview
    # drop the leading verse-number span (e.g. <span class='verseNumber'>Rom 1:1</span>)
    s = re.sub(r"<span[^>]*class='verseNumber'[^>]*>.*?</span>", " ", s, flags=re.I | re.S)
    # strip all remaining tags
    s = re.sub(r"<[^>]+>", " ", s)
    # unescape HTML entities
    s = html.unescape(s)
    # collapse whitespace and tidy spaces before punctuation
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([,.;:!?])", r"\1", s)
    return s


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
