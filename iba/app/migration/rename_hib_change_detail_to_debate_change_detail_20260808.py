"""rename_hib_change_detail_to_debate_change_detail_20260808.py — ONE-OFF, idempotent: renames
`hib_change_detail` to `debate_change_detail`.

**Why.** `hib_change_detail` (built this same day, §81) is about to hold audit rows for
`passage`/`verse_passage`, `phenomenon`, `operation`/`operation_party`, and the four `closing.set`
tables too — the researcher's own direction was "full CRUD is required for all table update
controls," extending the §81 treatment across every debate writer, not just `hib.set`. A table named
`hib_change_detail` holding `passage`/`phenomenon`/`operation` rows would mislead the next reader —
same class of gap `rename_span_reading_to_lexical.py` fixed once already in this app (a table's own
name outgrown by its actual scope). Cheap now (7 rows, one call site) — expensive to leave.

**Why a direct migration, not `configmaint.propose` row-by-row.** `ALTER TABLE ... RENAME TO` is
DDL, and `cfg_table`/`cfg_column`/`cfg_write_grant`/`cfg_index` all need their `table_name`/`name`
row updated to match in the same unit of work — same carve-out class as
`rename_span_reading_to_lexical.py` itself (GOVERNANCE.md §9B/§14).

    python -m iba.app.migration.rename_hib_change_detail_to_debate_change_detail_20260808
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

OLD, NEW = "hib_change_detail", "debate_change_detail"


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def run(conn: sqlite3.Connection) -> list[str]:
    report: list[str] = []

    if _table_exists(conn, NEW):
        report.append(f"table {NEW} already present")
    elif _table_exists(conn, OLD):
        conn.execute(f"ALTER TABLE {OLD} RENAME TO {NEW}")
        report.append(f"table {OLD} renamed to {NEW}")
    else:
        report.append(f"neither {OLD} nor {NEW} exists — nothing to rename (unexpected)")

    if conn.execute("SELECT 1 FROM cfg_table WHERE name=?", (NEW,)).fetchone():
        report.append(f"cfg_table row for {NEW} already present")
    elif conn.execute("SELECT 1 FROM cfg_table WHERE name=?", (OLD,)).fetchone():
        conn.execute(
            "UPDATE cfg_table SET name=?, "
            "use='one row per hib/hib_referent_option/verse_hib/passage/verse_passage/phenomenon/"
            "operation/operation_party/passage_linkage/passage_insufficiency/"
            "passage_emergent_question/passage_validation_note row inserted, updated, or "
            "soft-deleted by hib.set/passage.build/phenomenon.set/operation.set/closing.set -- "
            "the per-run CRUD audit trail shared by every debate writer (researcher direction "
            "2026-08-08).' WHERE name=?", (NEW, OLD))
        report.append(f"cfg_table row renamed {OLD} -> {NEW}, use text broadened")

    for cfg_tab, col in (("cfg_column", "table_name"), ("cfg_write_grant", "table_name"),
                         ("cfg_index", "table_name")):
        n = conn.execute(f"SELECT COUNT(*) FROM {cfg_tab} WHERE {col}=?", (OLD,)).fetchone()[0]
        if n:
            conn.execute(f"UPDATE {cfg_tab} SET {col}=? WHERE {col}=?", (NEW, OLD))
            report.append(f"{cfg_tab}: {n} row(s) repointed {OLD} -> {NEW}")
        else:
            report.append(f"{cfg_tab}: no {OLD} rows left to repoint")

    conn.commit()
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report = run(conn)
    conn.close()
    print(f"{OLD} -> {NEW} rename:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
