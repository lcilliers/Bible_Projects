"""repurpose_passage_tracking.py — ONE-OFF, idempotent: repurposes the retired `passage`/
`verse_passage` tables (BUILD.md §23 — candidate-driven char-continuity system, retired
2026-07-26, data soft-deleted and kept for provenance, "no new passage design proposed") as the
completion-tracking record for the verse-fanout method: one row per book/range that has been run
through `report.verse_span_meaning` and/or `report.passage_debate`, cross-referenced to every
verse it covers.

Per the researcher's own framing (2026-07-27): "the passage tables becomes the record of the
passages that were processed, with a reference to the file name of the verse-span-meaning and the
file name of the debate... tracks the verses in the verse table against the passages... allows us
to keep track of the completion of all the books, and back-track to the verses." Explicitly NOT
in scope here: how the debate's own analytical *content* gets digested into the DB — "I have not
yet decided... this is still emerging." This migration tracks the fact and location of processing
only (paths, timestamps, a coarse scaffold-vs-filled signal), nothing about operations/decisions.

**Why a rebuild, not just `ALTER TABLE ADD COLUMN`, for `verse_passage`.** The live table has a
hard `UNIQUE (verse_id)` baked into its `CREATE TABLE` (not a `cfg_unique`-declared, deleted-aware
convention — an actual SQLite constraint). The 24,763 retired rows (`deleted=1`, kept per the
researcher's explicit "record kept" instruction — see BUILD.md §23's CSV export, the actual
durable provenance copy) already occupy nearly every verse_id in the Bible, so ANY new insert for
almost any verse would violate that constraint outright, blocked by dead rows. Fixed by rebuilding
the table without the inline constraint and replacing it with a partial unique index
(`WHERE deleted=0`) — preserves every existing row byte-for-byte, enforces "one CURRENT passage
per verse" for live rows only, exactly the invariant the new use needs.

**`passage` gets 6 new nullable columns** (`book_label`, `verse_span_meaning_path`,
`verse_span_meaning_written_at`, `debate_path`, `debate_written_at`, `debate_status`) plus a
partial unique index on the range identity (`book, start_chapter, start_verse, end_chapter,
end_verse`, `WHERE deleted=0`) so re-running a report for the same range upserts instead of
duplicating. The OLD candidate-system columns (`rule`, `source`, `needs_review`, `anchor_verse_id`
mode) are left exactly as they were — new rows simply don't populate `rule`/`source`/
`needs_review` (their old enum values describe an algorithm this new use doesn't run).

    python -m iba.app.migration.repurpose_passage_tracking
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

NEW_PASSAGE_COLUMNS = [
    # (name, type, ordinal, use)
    ("book_label", "TEXT", 14, "human-facing subfolder name (e.g. 'Daniel') used by the "
     "verse-analysis report writers; defaults to `book` if the caller never supplied one"),
    ("verse_span_meaning_path", "TEXT", 15, "path to this range's report.verse_span_meaning "
     "output, written by that step on success"),
    ("verse_span_meaning_written_at", "TEXT", 16, "UTC timestamp of the last "
     "report.verse_span_meaning write for this range"),
    ("debate_path", "TEXT", 17, "path to this range's report.passage_debate output "
     "(scaffold or filled — see debate_status), written by that step on success"),
    ("debate_written_at", "TEXT", 18, "UTC timestamp of the last report.passage_debate write "
     "for this range"),
    ("debate_status", "TEXT", 19, "'scaffold' (auto-generated, still has unreplaced "
     "<!-- fill in --> placeholders) or 'filled' (none remain) — a coarse, mechanically-derived "
     "completion signal only; NOT a digestion of the debate's analytical content, which is a "
     "separate, not-yet-designed question"),
]


def _column_exists(conn, table, name) -> bool:
    return any(r[1] == name for r in conn.execute(f"PRAGMA table_info({table})"))


def _dependent_views(conn) -> list[tuple[str, str]]:
    """(name, sql) for every view whose definition mentions verse_passage — must be dropped
    before the rebuild (SQLite view bodies aren't updated by a table rename/rebuild) and
    recreated after, identically, since the rebuilt table's column set is unchanged."""
    return [(r[0], r[1]) for r in conn.execute(
        "SELECT name, sql FROM sqlite_master WHERE type='view'")
        if "verse_passage" in (r[1] or "")]


def _rebuild_verse_passage(conn, report):
    if not _has_inline_unique(conn):
        report.append("verse_passage: already rebuilt (no inline UNIQUE(verse_id)) — skipped")
        return
    before = conn.execute("SELECT COUNT(*) FROM verse_passage").fetchone()[0]
    views = _dependent_views(conn)
    conn.execute("BEGIN")
    try:
        for name, _ in views:
            conn.execute(f'DROP VIEW "{name}"')
        conn.execute("""
            CREATE TABLE verse_passage_new (
              "id" INTEGER PRIMARY KEY AUTOINCREMENT,
              "passage_id" INTEGER NOT NULL,
              "verse_id" INTEGER NOT NULL,
              "is_anchor" INTEGER,
              "created_at" TEXT,
              "deleted" INTEGER DEFAULT 0,
              FOREIGN KEY ("passage_id") REFERENCES "passage"("id"),
              FOREIGN KEY ("verse_id") REFERENCES "verse"("id")
            )
        """)
        conn.execute("INSERT INTO verse_passage_new (id, passage_id, verse_id, is_anchor, "
                    "created_at, deleted) SELECT id, passage_id, verse_id, is_anchor, "
                    "created_at, deleted FROM verse_passage")
        conn.execute("DROP TABLE verse_passage")
        conn.execute("ALTER TABLE verse_passage_new RENAME TO verse_passage")
        conn.execute("CREATE UNIQUE INDEX idx_verse_passage_verse_id_live ON "
                    "verse_passage(verse_id) WHERE deleted=0")
        for _, sql in views:
            conn.execute(sql)
        after = conn.execute("SELECT COUNT(*) FROM verse_passage").fetchone()[0]
        if after != before:
            raise RuntimeError(f"row count mismatch after rebuild: {before} -> {after}")
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    report.append(f"verse_passage: rebuilt without inline UNIQUE(verse_id); partial unique "
                  f"index idx_verse_passage_verse_id_live (WHERE deleted=0) added; "
                  f"{len(views)} dependent view(s) dropped and recreated identically; "
                  f"{before} rows preserved unchanged")


def _has_inline_unique(conn) -> bool:
    sql = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='verse_passage'").fetchone()[0]
    return "UNIQUE" in sql.upper()


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _rebuild_verse_passage(conn, report)

    for name, coltype, ordinal, use in NEW_PASSAGE_COLUMNS:
        if not _column_exists(conn, "passage", name):
            conn.execute(f'ALTER TABLE passage ADD COLUMN "{name}" {coltype}')
            report.append(f"passage.{name}: column added")
        else:
            report.append(f"passage.{name}: already present")

    existing_indexes = {r[1] for r in conn.execute("PRAGMA index_list(passage)")}
    if "idx_passage_range_live" not in existing_indexes:
        conn.execute(
            "CREATE UNIQUE INDEX idx_passage_range_live ON passage "
            "(book, start_chapter, start_verse, end_chapter, end_verse) WHERE deleted=0")
        report.append("passage: partial unique index idx_passage_range_live "
                      "(book,start_chapter,start_verse,end_chapter,end_verse WHERE deleted=0) added")
    else:
        report.append("passage: idx_passage_range_live already present")

    for name, coltype, ordinal, use in NEW_PASSAGE_COLUMNS:
        if not conn.execute("SELECT 1 FROM cfg_column WHERE table_name='passage' AND name=?",
                            (name,)).fetchone():
            expectation = "enum.passage_debate_status" if name == "debate_status" else None
            conn.execute(
                'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", '
                "is_unique, dflt, fk, use, expectation, source, filled_by) "
                "VALUES ('passage',?,?,?,0,0,0,NULL,NULL,?,?,NULL,?)",
                (name, ordinal, coltype, use, expectation,
                 "report.verse_span_meaning" if name.startswith("verse_span_meaning") or
                 name == "book_label" else "report.passage_debate"))
            report.append(f"cfg_column (passage, {name}): added")
        else:
            report.append(f"cfg_column (passage, {name}): already present")

    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='passage_debate_status'").fetchone():
        conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES "
                    "('passage_debate_status','scaffold',0,0)")
        conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES "
                    "('passage_debate_status','filled',1,0)")
        report.append("cfg_enum (passage_debate_status): scaffold, filled added")
    else:
        report.append("cfg_enum (passage_debate_status): already present")

    range_key = ["book", "start_chapter", "start_verse", "end_chapter", "end_verse"]
    for i, col in enumerate(range_key):
        if not conn.execute("SELECT 1 FROM cfg_unique WHERE table_name='passage' AND col=?",
                            (col,)).fetchone():
            conn.execute("INSERT INTO cfg_unique (table_name, col, ordinal) VALUES ('passage',?,?)",
                        (col, i))
            report.append(f"cfg_unique (passage, {col}): added")
        else:
            report.append(f"cfg_unique (passage, {col}): already present")

    grants = [
        ("report.verse_span_meaning", "passage"),
        ("report.verse_span_meaning", "verse_passage"),
        ("report.passage_debate", "passage"),
        ("report.passage_debate", "verse_passage"),
    ]
    for writer, table in grants:
        if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?",
                            (writer, table)).fetchone():
            conn.execute("INSERT INTO cfg_write_grant (writer, table_name) VALUES (?,?)",
                        (writer, table))
            report.append(f"cfg_write_grant ({writer} -> {table}): added")
        else:
            report.append(f"cfg_write_grant ({writer} -> {table}): already present")

    conn.commit()
    conn.close()

    print("passage-tracking repurpose:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
