"""rename_span_reading_to_lexical.py — ONE-OFF, idempotent: renames the `span_reading` table (and
every `cfg_*` row that names it, the `verse-span-reading` work package, and the two steps under it)
to "the lexical" — `verse_lexical` / `verse-lexical` / `lexical.build` / `report.verse_lexical`.

**Why a direct migration, not `configmaint.propose` row-by-row.** `ALTER TABLE ... RENAME TO` is
DDL — `configmaint.propose` can only write rows on already-existing tables/columns, not rename a
table (same carve-out class as `bootstrap_cfg_utility.py`/`bootstrap_span_reading.py` itself,
GOVERNANCE.md §9B/§14): a direct, documented, idempotent bootstrap. The researcher's own explicit
direction this session ("B1 — proceed") is the up-front approval that carve-out requires.

**Why the rename.** The researcher's own words, 2026-08-05: *"throughout the study we referred to
the verse-span-meaning as the lexical. I think we need to return to that terminology. the new
terminology introduced [`span_reading`, "T1-T3"] is all very confusing."* `span_reading`/T1-T3 was
this session's own dev-only working name for the mechanical base-reading engine
(`t1-t3-design-decisions-20260805.md`) — it was never meant to permanently replace the study's own
long-standing term. This migration is pure renaming: no column shape, no data, no logic changes —
every row that already existed under the old name still exists, unaltered, under the new one.

    python -m iba.app.migration.rename_span_reading_to_lexical
"""

from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def run(conn: sqlite3.Connection) -> None:
    if _table_exists(conn, "verse_lexical") and not _table_exists(conn, "span_reading"):
        print("already renamed — nothing to do")
        return
    if not _table_exists(conn, "span_reading"):
        raise RuntimeError("neither span_reading nor verse_lexical exists — nothing to rename")

    conn.execute("ALTER TABLE span_reading RENAME TO verse_lexical")

    # cfg_work_package (complete_message caught late — end-to-end verification run against Dan 8
    # surfaced "COMPLETE — span_reading built..." still using the old name)
    conn.execute(
        "UPDATE cfg_work_package SET name='verse-lexical', "
        "ps_script='iba/app/ps/VerseLexical.ps1', "
        "complete_message=REPLACE(complete_message,'span_reading','lexical') "
        "WHERE name='verse-span-reading'")

    # cfg_step (work_package + step name + handler, both rows)
    conn.execute(
        "UPDATE cfg_step SET work_package='verse-lexical', step='lexical.build', "
        "handler='iba.app.handlers.lexical:build', "
        "does=REPLACE(REPLACE(does,'span_reading','verse_lexical'),'span-reading','verse-lexical') "
        "WHERE work_package='verse-span-reading' AND step='span_reading.build'")
    conn.execute(
        "UPDATE cfg_step SET work_package='verse-lexical', step='report.verse_lexical', "
        "handler='iba.app.handlers.reports:lexical_report', "
        "does=REPLACE(REPLACE(does,'span_reading','verse_lexical'),'span-reading','verse-lexical') "
        "WHERE work_package='verse-span-reading' AND step='report.span_reading'")

    # cfg_setting
    conn.execute(
        "UPDATE cfg_setting SET key='report.verse_lexical_output_pattern', "
        "value='\"{book}-{range}-verse-lexical.md\"', "
        "use=REPLACE(REPLACE(use,'span_reading','verse_lexical'),'span-reading','verse-lexical') "
        "WHERE key='report.span_reading_output_pattern'")

    # cfg_table
    conn.execute(
        "UPDATE cfg_table SET name='verse_lexical', "
        "use=REPLACE(use,'span_reading','verse_lexical') "
        "WHERE name='span_reading'")

    # cfg_column (all 12 rows)
    conn.execute(
        "UPDATE cfg_column SET table_name='verse_lexical' WHERE table_name='span_reading'")

    # cfg_report
    conn.execute(
        "UPDATE cfg_report SET step='report.verse_lexical', "
        "title=REPLACE(title,'span_reading','verse_lexical') "
        "WHERE step='report.span_reading'")

    # cfg_report_section (2 rows)
    conn.execute(
        "UPDATE cfg_report_section SET step='report.verse_lexical' "
        "WHERE step='report.span_reading'")

    # cfg_write_grant
    conn.execute(
        "UPDATE cfg_write_grant SET writer='lexical.build', table_name='verse_lexical' "
        "WHERE writer='span_reading.build' AND table_name='span_reading'")

    # cfg_unique (2 rows)
    conn.execute(
        "UPDATE cfg_unique SET table_name='verse_lexical' WHERE table_name='span_reading'")

    # cfg_on_fail (2 rows)
    conn.execute(
        "UPDATE cfg_on_fail SET step='lexical.build' "
        "WHERE step='span_reading.build' AND condition='unreachable'")
    conn.execute(
        "UPDATE cfg_on_fail SET step='report.verse_lexical', "
        "message=REPLACE(REPLACE(REPLACE(message,'span_reading rows','verse_lexical rows'),"
        "'span_reading.build','lexical.build'),'verse-span-reading','verse-lexical') "
        "WHERE step='report.span_reading' AND condition='no-readings'")

    # cfg_utility
    conn.execute(
        "UPDATE cfg_utility SET module='lexical', file_path='iba/app/lib/lexical.py', "
        "purpose=REPLACE(REPLACE(purpose,'spanreading.py','lexical.py'),'`span_reading`','the "
        "lexical (`verse_lexical`)') "
        "WHERE module='spanreading'")

    conn.commit()
    print("renamed: span_reading -> verse_lexical (table, cfg_work_package, cfg_step x2, "
          "cfg_setting, cfg_table, cfg_column x12, cfg_report, cfg_report_section x2, "
          "cfg_write_grant, cfg_unique x2, cfg_on_fail x2, cfg_utility)")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
