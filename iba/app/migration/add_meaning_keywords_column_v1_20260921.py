"""add_meaning_keywords_column_v1_20260921.py — ONE-OFF migration, escalation #1824 v3,
researcher instruction verbatim: "similarity is not matching sentences. Similarly to matching
keys. For instance to check for matching word meaning: match a) surface b) meaning extraction
keywords c) morph."

Adds `ib_observation.meaning_keywords` (TEXT, nullable, JSON array) -- a short, structured list of
key terms the LLM extracts alongside its free-form `obs_text`, used for the NEW structured-key
same/broaden/new matching path (`recordingpass.py`'s own `_keyword_match_candidate`), separate from
the existing prose-similarity path. `ib_observation.stable_key` already exists but is documented
(`cfg_column`) for a different, unrelated purpose (the old JSON-file-provenance architecture, 0 of
8466 live rows ever populated) -- repurposing an already-named column for something else would be
exactly the confusing overloading this session has been correcting elsewhere; a new column is the
honest choice.

Idempotent (checks for the column's existence before adding).

    python -m iba.app.migration.add_meaning_keywords_column_v1_20260921
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH


def apply_migration(conn: sqlite3.Connection) -> str:
    cols = [r[1] for r in conn.execute("PRAGMA table_info(ib_observation)").fetchall()]
    if "meaning_keywords" in cols:
        return "meaning_keywords: column already exists -- no-op"
    conn.execute("ALTER TABLE ib_observation ADD COLUMN meaning_keywords TEXT")
    conn.execute(
        'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
        "is_unique, dflt, fk, use, expectation, source, filled_by, inactive) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        ("iba", "ib_observation", "meaning_keywords", None, "TEXT", 0, 0, 0, None, None,
         "JSON array of short key terms/concepts the LLM extracts alongside obs_text, used by "
         "recordingpass.py's structured-key same/broaden/new matching (surface+morph+keywords) "
         "-- escalation #1824, 2026-09-21. NULL for stages/questions not yet using this path "
         "(everything except the new M0.7 family so far); the existing text-similarity path "
         "remains the fallback wherever this is NULL.",
         None, "escalation #1824, researcher instruction 2026-09-21", None, 0))
    return "meaning_keywords: column added + registered in cfg_column"


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    try:
        report = apply_migration(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
