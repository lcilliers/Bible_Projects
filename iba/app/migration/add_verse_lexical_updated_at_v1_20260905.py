"""add_verse_lexical_updated_at_v1_20260905.py — ONE-OFF. Escalation #1520 root-cause redesign
(researcher's own verdict 2026-09-05: "you have designed lexical findings system that seems to me
to be highly inefficient, and have a high risk of errors and rework requirements... build a proper
CRUD system with proper controls" — full record `iba/docs/1520-verse-lexical-crud-safety-review-
v1-20260905.md`).

`write_readings_for_span` (`iba/app/lib/lexical.py`) is being converted from "always soft-delete +
insert a fresh row, even for identical content" to a real in-place UPDATE for a slot whose content
changed, and a true no-op for a slot whose content didn't — matching this codebase's own already-
correct precedent (`handlers/operations.py:phenomenon_set`, which uses in-place UPDATE precisely
because `phenomenon.id` has a downstream FK dependent, exactly `verse_lexical`'s own situation via
`verse_lexical_note`). The old convention's stated reason for churning every row's id on every run
was "so created_at reflects the last run that confirmed it" — this column replaces that signal
without requiring the id (and every dependent FK) to churn: `updated_at` is set on a genuine
content-changing UPDATE, left NULL on a row that has never been revised since it was first built.

What this does, in iba.db, one statement: `ALTER TABLE verse_lexical ADD COLUMN updated_at TEXT`.
Nullable, no default expression, additive only — SQLite allows this in place, no rebuild-and-copy
needed (unlike the passage_id-nullable migration this session, which changed an existing NOT NULL
constraint and needed the full rename/recreate/copy dance). Zero risk to the 544k+ live rows.

Idempotent: checks the live column list before acting.

    python -m iba.app.migration.add_verse_lexical_updated_at_v1_20260905
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        cols = [r[1] for r in conn.execute("PRAGMA table_info(verse_lexical)")]
        if "updated_at" in cols:
            print("add_verse_lexical_updated_at_v1_20260905: no-op — "
                  "verse_lexical.updated_at already exists.")
            return 0

        conn.execute("ALTER TABLE verse_lexical ADD COLUMN updated_at TEXT")
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("add_verse_lexical_updated_at_v1_20260905: verse_lexical.updated_at column added "
          "(nullable, no rows touched).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
