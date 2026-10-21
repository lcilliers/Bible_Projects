"""bootstrap_research_db_cfg_table.py — ONE-OFF: registers every `bible_research.db` table/column
into `cfg_table`/`cfg_column` as `database='bible_research'` (escalation #653).

Source is `iba/config/DBSchema/DBSchema.json` (rebuilt live today,
`python iba/scripts/build_dbschema.py --db bible_research` — 110 tables, 1,181 columns, real
profiled descriptions, not written by hand) — per `dbschema.from-the-live-db`/
`dbschema.description-from-data` (`DBSchema_maintenance.json`), this file's own descriptions ARE
"the use text derived from profiling the live data" CLAUDE.md §3 already cites it as. Reusing it
here rather than re-deriving 1,181 "use" strings by hand is the same reuse-over-duplication
discipline as every other bulk bootstrap in this app.

**Prerequisite**: `add_cfg_table_database_column.py` MUST have already run — `cfg_table`/
`cfg_column`'s PKs must include `database`, or this collides on the 4 known cross-database name
matches (`cluster`/`passage`/`verse`/`word_registry`). Checked defensively below, not assumed.

`grain` (a field `cfg_table` carries that `DBSchema.json` doesn't) derived mechanically from each
table's own `primary_key` list — "one row per <pk column(s)>" when there is one, a flat statement
when there isn't (composite business key not modelled as a DB-level PK, or none at all — both real,
both left honest rather than guessed).

`is_unique` derived from `DBSchema.json`'s own `indexes[].unique` flag (single-column unique
indexes only — a multi-column unique index doesn't make any ONE of its columns individually
unique, so it's deliberately not credited to any column here).

`expectation`/`source`/`filled_by` deliberately left NULL throughout: these encode IBA's OWN
value-quality rules and write-provenance for tables it actively writes — `bible_research.db` is
governed by the (separate, legacy) `engine/` pipeline, not `run.py`'s dispatcher, so none of those
three concepts have real content here yet. Safe by construction against every check that reads
them (`lib/valuequality.py`/`cfgquality.find_filled_by_referencing_inactive_step` both filter
`IS NOT NULL`) — verified in `BUILD.md` §125, not assumed.

Schema is DATA (bulk `cfg_table`/`cfg_column` rows describing an existing schema), same class of
exception as every other bulk bootstrap in this app (`bootstrap_cfg_utility.py`,
`populate_cfg_index_rows.py`) — not a `configmaint.propose` call.

    python -m iba.app.migration.bootstrap_research_db_cfg_table
"""

from __future__ import annotations

import json
import pathlib
import sqlite3
import sys

from ..lib.cfg import DB_PATH

DBSCHEMA_PATH = pathlib.Path(__file__).resolve().parent.parent.parent.parent / \
    "iba" / "config" / "DBSchema" / "DBSchema.json"
DATABASE = "bible_research"


def _grain_for(table: str, primary_key: list[str]) -> str:
    if not primary_key:
        return f"no declared primary key — see cfg_column for {table}'s real columns"
    if len(primary_key) == 1:
        return f"one row per {primary_key[0]}"
    return f"one row per ({', '.join(primary_key)})"


def _unique_single_columns(indexes: list[dict]) -> set[str]:
    """Columns that are the SOLE member of a unique index — a multi-column unique index doesn't
    make any one column individually unique, so those are deliberately excluded."""
    out = set()
    for idx in indexes:
        if idx.get("unique") and len(idx.get("columns") or []) == 1:
            out.add(idx["columns"][0])
    return out


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_table)")}
    if "database" not in cols:
        print("cfg_table has no 'database' column yet — run "
              "add_cfg_table_database_column.py first. Nothing done.", file=sys.stderr)
        conn.close()
        return 1

    already = conn.execute(
        "SELECT COUNT(*) FROM cfg_table WHERE database=?", (DATABASE,)).fetchone()[0]
    if already:
        print(f"cfg_table already has {already} row(s) for database={DATABASE!r} — nothing to do "
              f"(idempotent; delete them first if a genuine re-run is intended).")
        conn.close()
        return 0

    if not DBSCHEMA_PATH.exists():
        print(f"DBSchema.json not found at {DBSCHEMA_PATH} — run "
              f"iba/scripts/build_dbschema.py --db bible_research first.", file=sys.stderr)
        conn.close()
        return 1

    schema = json.loads(DBSCHEMA_PATH.read_text(encoding="utf-8"))
    if schema.get("database") != "bible_research":
        print(f"DBSchema.json's own 'database' field is {schema.get('database')!r}, not "
              f"'bible_research' — wrong capture. Nothing done.", file=sys.stderr)
        conn.close()
        return 1

    n_tables = 0
    n_columns = 0
    for table, t in schema["tables"].items():
        pk = t.get("primary_key") or []
        conn.execute(
            'INSERT INTO cfg_table (database, name, grain, "use") VALUES (?,?,?,?)',
            (DATABASE, table, _grain_for(table, pk), t.get("description") or ""))
        n_tables += 1

        fk_by_col = {fk["column"]: fk["references"] for fk in (t.get("foreign_keys") or [])}
        unique_cols = _unique_single_columns(t.get("indexes") or [])
        for ordinal, c in enumerate(t.get("columns") or []):
            conn.execute(
                'INSERT INTO cfg_column (database, table_name, name, ordinal, "type", is_pk, '
                '"notnull", is_unique, dflt, fk, "use", expectation, source, filled_by) '
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,NULL,NULL,NULL)",
                (DATABASE, table, c["name"], ordinal, c.get("type"),
                 1 if c.get("pk") else 0, 1 if c.get("notnull") else 0,
                 1 if c["name"] in unique_cols else 0,
                 str(c["default"]) if c.get("default") is not None else None,
                 fk_by_col.get(c["name"]), c.get("description") or ""))
            n_columns += 1

    conn.commit()
    conn.close()

    print(f"bible_research.db cfg_table/cfg_column bootstrap: {n_tables} table(s), "
         f"{n_columns} column(s) registered, database={DATABASE!r}, "
         f"source: DBSchema.json (schema_version {schema.get('schema_version')}, "
         f"captured {schema.get('exported_date')}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
