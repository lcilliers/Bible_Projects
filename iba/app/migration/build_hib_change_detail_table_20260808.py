"""build_hib_change_detail_table_20260808.py — ONE-OFF, idempotent: creates `hib_change_detail`,
the per-row CRUD audit trail for `hib.set`'s writes to `hib`/`hib_referent_option`/`verse_hib`
(PLAN-revise-hib-set-scope-and-crud-v1-20260808.md, researcher direction 2026-08-08: "each entry
(insert, update, delete) must have entries in the table to be able to trace the changes to the
run").

**Why a direct migration, not `configmaint.propose`.** New table = DDL — `configmaint.propose` can
only write rows on already-existing tables/columns, not create either (same carve-out class as
`build_operations_schema.py`/`bootstrap_cfg_utility.py`, GOVERNANCE.md §9B/§14). The researcher's own
explicit "we can now proceed with implementing the plan" (2026-08-08, after two full planning-mode
review/revision passes on this exact design) is the up-front design approval that carve-out
requires.

**Shape — deliberately mirrors `cfg_change_detail`** (this app's existing per-row audit trail for
`configmaint.propose` writes), not invented fresh: `run_id, table_name, op[insert|update|delete],
where_json, set_json, before_json, applied_at`. Kept as a separate table rather than reusing
`cfg_change_detail` itself — that one is scoped to config-governance writes; this one is scoped to
analytical-data writes, same shape, different concern, matching this app's convention of parallel-
but-separate tables for parallel concerns. `op` stays free text (no `cfg_enum`), matching
`cfg_change_detail.op`'s own precedent exactly — not a value this DB has ever enum-constrained.

No `deleted` column — this is an append-only audit log, rows are never corrected or removed, so the
usual soft-delete/partial-unique-index convention doesn't apply here (same reasoning `escalation`
already uses: also audit-shaped, also no `deleted` column, also just a plain single-column index on
`run_id`).

Registered as a genuine DATA table (`cfg_table` + `cfg_column`), not `cfg_*` infrastructure like
`cfg_utility` was — `hib_change_detail` holds real pipeline audit rows, the same class as `hib`/
`phenomenon`/`operation` it sits alongside. `cfg_write_grant` for `hib.set` is added in the same
migration (unlike `build_operations_schema.py`'s deliberate no-writer-yet gap — here the writer is
already fully decided, this migration IS the writer's own schema).

    python -m iba.app.migration.build_hib_change_detail_table_20260808
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import Cfg, DB_PATH
from ..lib import db as db_lib

# (table, name, ordinal, type, is_pk, notnull, is_unique, dflt, fk, use, expectation, source, filled_by)
COLUMNS = [
    ("hib_change_detail", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("hib_change_detail", "run_id", 1, "TEXT", 0, 1, 0, None, "run.run_id",
     "which run made this change -- same fk convention as escalation.run_id/validation_result.run_id",
     None, None, None),
    ("hib_change_detail", "table_name", 2, "TEXT", 0, 1, 0, None, None,
     "'hib' | 'hib_referent_option' | 'verse_hib' -- which table this row's change touched",
     None, None, None),
    ("hib_change_detail", "op", 3, "TEXT", 0, 1, 0, None, None,
     "'insert' | 'update' | 'delete' -- free text, matching cfg_change_detail.op's own precedent",
     None, None, None),
    ("hib_change_detail", "where_json", 4, "TEXT", 0, 0, 0, None, None,
     "identifies the row touched, e.g. {\"id\": 47}", None, None, None),
    ("hib_change_detail", "set_json", 5, "TEXT", 0, 0, 0, None, None,
     "the new values written (insert/update only)", None, None, None),
    ("hib_change_detail", "before_json", 6, "TEXT", 0, 0, 0, None, None,
     "prior row state (update/delete only), NULL on insert", None, None, None),
    ("hib_change_detail", "applied_at", 7, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
]

TABLES = [
    ("hib_change_detail",
     "one row per hib/hib_referent_option/verse_hib row inserted, updated, or soft-deleted by one "
     "hib.set call -- the per-run CRUD audit trail (researcher direction 2026-08-08).",
     "hib_change_detail"),
]

INDEXES = [
    ("hib_change_detail", "idx_hib_change_detail_run_id", "run_id", 0),
]


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def _registered(conn: sqlite3.Connection, table: str) -> bool:
    return conn.execute("SELECT 1 FROM cfg_table WHERE name=?", (table,)).fetchone() is not None


def _grant(conn: sqlite3.Connection, writer: str, table: str, report: list[str]) -> None:
    if not conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?",
            (writer, table)).fetchone():
        conn.execute(
            "INSERT INTO cfg_write_grant (writer, table_name, inactive) VALUES (?,?,0)",
            (writer, table))
        report.append(f"cfg_write_grant ({writer}, {table}) added")
    else:
        report.append(f"cfg_write_grant ({writer}, {table}) already present")


def run(conn: sqlite3.Connection) -> list[str]:
    """Resumable by design (same discipline as build_operations_schema.py): cfg_* registration is
    applied FIRST (table creation reads from it), then the physical table is built via
    `db.build_data_tables()` — never a hand-written `CREATE TABLE`, so the live table is provably
    identical to what `cfg_column.fk`/`cfg_index` actually declare (the exact gap BUILD.md §79 had
    to retrofit for the original 6 debate tables; not repeating it here)."""
    report: list[str] = []

    if _registered(conn, "hib_change_detail"):
        report.append("cfg_table row for hib_change_detail already present")
    else:
        conn.executemany(
            "INSERT INTO cfg_table (name, grain, use) VALUES (?,?,?)",
            [(n, g, u) for n, u, g in TABLES])
        conn.executemany(
            'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", is_unique, '
            "dflt, fk, use, expectation, source, filled_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            COLUMNS)
        report.append("cfg_table + cfg_column rows for hib_change_detail added")

    existing_idx = {r[0] for r in conn.execute(
        "SELECT DISTINCT name FROM cfg_index WHERE table_name='hib_change_detail'")}
    to_add = [(t, n, c, o) for t, n, c, o in INDEXES if n not in existing_idx]
    if to_add:
        conn.executemany(
            "INSERT INTO cfg_index (table_name, name, col, ordinal) VALUES (?,?,?,?)", to_add)
        report.append(f"cfg_index row(s) added: {[n for _, n, _, _ in to_add]}")
    else:
        report.append("cfg_index row(s) already present")

    _grant(conn, "hib.set", "hib_change_detail", report)
    conn.commit()

    if _table_exists(conn, "hib_change_detail"):
        report.append("table hib_change_detail already present")
    else:
        cfg = Cfg()
        db_lib.build_data_tables(cfg, conn)
        cfg.close()
        report.append("table hib_change_detail created via db.build_data_tables() (config-driven "
                       "DDL, FK + index applied from cfg_column/cfg_index directly)")

    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report = run(conn)
    conn.close()
    print("hib_change_detail bootstrap (PLAN-revise-hib-set-scope-and-crud-v1-20260808.md):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
