"""legacy_import.py — read-only helpers for the legacy-registry import batch.

Two sub-commands, both read-only:

    python -m iba.app.migration.legacy_import words          # JSON list from the OLD study DB
    python -m iba.app.migration.legacy_import pending <word> # at_step of a raised escalation (NEW app DB)

`words` reads the legacy `word_registry` in `database/bible_research.db` — opened READ-ONLY,
never modified — and returns the English words to migrate, EXCLUDING those marked deleted or
excluded (`phase1_status` in 'Excluded'/'Deleted', case-insensitive). Carries `source_list`
as provenance for the new registry's Source field.

`pending` looks in the app DB for the step a word is paused at, so the batch can tell an
approval pause (auto-answerable) from anything else (flag for review).
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sqlite3
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
OLD_DB = REPO / "database" / "bible_research.db"
NEW_DB = pathlib.Path(__file__).resolve().parents[1] / "db" / "iba.db"


def words() -> int:
    conn = sqlite3.connect(f"file:{OLD_DB.as_posix()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT word, source_list FROM word_registry "
        "WHERE word IS NOT NULL AND TRIM(word) <> '' "
        "AND LOWER(COALESCE(phase1_status,'')) NOT IN ('excluded','deleted') "
        "ORDER BY no, id").fetchall()
    conn.close()
    print(json.dumps([{"word": r["word"], "source_list": r["source_list"]} for r in rows]))
    return 0


def pending(word: str) -> int:
    conn = sqlite3.connect(NEW_DB)
    conn.row_factory = sqlite3.Row
    # escalation-reset 2026-08-16: `word` -> `source` ('new-word: <word>' for a word-scoped row).
    r = conn.execute(
        "SELECT at_step FROM escalation WHERE lower(source)=lower(?) AND state='raised' "
        "ORDER BY id DESC LIMIT 1", (f"new-word: {word}",)).fetchone()
    conn.close()
    print(r["at_step"] if r else "")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("words")
    p = sub.add_parser("pending")
    p.add_argument("word")
    a = ap.parse_args()
    return words() if a.cmd == "words" else pending(a.word)


if __name__ == "__main__":
    sys.exit(main())
