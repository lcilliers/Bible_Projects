"""make_verse_lexical_note_passage_id_nullable_v1_20260905.py — ONE-OFF. Escalation #1451, the
Window 1 Layer 2 verse-scoped redesign (researcher's own 4-question design pass, 2026-09-05,
`iba/docs/1451-window1-layer2-verse-scoped-redesign-v1-20260905.md`): "if the lexical for a verse
can be built without compromises, the whole passage concept will fall away." `lexical.enrich` no
longer requires (or is given) a `passage` row -- `verse_lexical_note.passage_id` was `NOT NULL`
with an FK to `passage`, which would refuse every insert once the handler stops resolving one.

What this does, in iba.db, one transaction, direct write (schema evolution is migration-script
territory): rebuilds `verse_lexical_note` with `passage_id` now NULLABLE, identical DDL otherwise.
Zero live rows existed at the time of this migration (confirmed: `SELECT COUNT(*) FROM
verse_lexical_note` = 0 -- the only prior use was a throwaway test fixture, escalation #1450,
created and fully deleted) -- no data to copy, no risk.

Idempotent: checks the live column's nullability before acting.

    python -m iba.app.migration.make_verse_lexical_note_passage_id_nullable_v1_20260905
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_NEW_DDL = """
    CREATE TABLE "verse_lexical_note" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      "verse_lexical_id" INTEGER NOT NULL,
      "verse_id" INTEGER NOT NULL,
      "passage_id" INTEGER,
      "note_type" TEXT NOT NULL,
      "resolution_status" TEXT NOT NULL,
      "target_verse_lexical_id" INTEGER,
      "related_verse_lexical_ids" TEXT,
      "value_text" TEXT,
      "evidence_text" TEXT,
      "created_at" TEXT NOT NULL,
      "deleted" INTEGER NOT NULL DEFAULT 0,
      FOREIGN KEY ("verse_lexical_id") REFERENCES "verse_lexical"("id"),
      FOREIGN KEY ("verse_id") REFERENCES "verse"("id"),
      FOREIGN KEY ("passage_id") REFERENCES "passage"("id"),
      FOREIGN KEY ("target_verse_lexical_id") REFERENCES "verse_lexical"("id")
    )
"""

_COLUMNS = [
    "id", "verse_lexical_id", "verse_id", "passage_id", "note_type", "resolution_status",
    "target_verse_lexical_id", "related_verse_lexical_ids", "value_text", "evidence_text",
    "created_at", "deleted",
]


def _passage_id_is_nullable(conn: sqlite3.Connection) -> bool:
    for row in conn.execute("PRAGMA table_info(verse_lexical_note)"):
        if row[1] == "passage_id":
            return row[3] == 0   # notnull flag: 0 = nullable, 1 = NOT NULL
    raise RuntimeError("verse_lexical_note.passage_id column not found")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []
    try:
        if _passage_id_is_nullable(conn):
            print("make_verse_lexical_note_passage_id_nullable_v1_20260905: no-op — "
                  "passage_id is already nullable.")
            return 0

        before_count = conn.execute("SELECT COUNT(*) FROM verse_lexical_note").fetchone()[0]

        conn.execute("ALTER TABLE verse_lexical_note RENAME TO verse_lexical_note_old_20260905")
        report.append("verse_lexical_note renamed to verse_lexical_note_old_20260905")

        conn.execute(_NEW_DDL)
        report.append("verse_lexical_note recreated with passage_id nullable")

        col_list = ", ".join(_COLUMNS)
        conn.execute(
            f"INSERT INTO verse_lexical_note ({col_list}) "
            f"SELECT {col_list} FROM verse_lexical_note_old_20260905"
        )
        after_count = conn.execute("SELECT COUNT(*) FROM verse_lexical_note").fetchone()[0]
        report.append(f"rows copied: {after_count} (source had {before_count})")
        if after_count != before_count:
            raise RuntimeError(
                f"row count mismatch after copy: {after_count} != {before_count}")

        conn.execute("DROP TABLE verse_lexical_note_old_20260905")
        report.append("verse_lexical_note_old_20260905 dropped")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("make_verse_lexical_note_passage_id_nullable_v1_20260905:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
