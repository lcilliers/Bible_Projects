"""
export_database_schema.py
─────────────────────────
Exports the live database schema to a JSON report for use as an AI project
reference file.

Output structure per table:
  - sql:       the CREATE TABLE statement
  - columns:   list of {name, type, notnull, default}
  - indexes:   list of {name, unique}
  - row_count: current row count

Run:
    python scripts/export_database_schema.py
    python scripts/export_database_schema.py --output path/to/output.json
"""

import argparse
import datetime
import json
import os
import sqlite3
import sys

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
DB_PATH = os.path.join(ROOT_DIR, "data", "bible_research.db")
DEFAULT_OUTPUT_DIR = os.path.join(ROOT_DIR, "data", "schema")


def get_schema_version(conn):
    """Read the current schema version from the schema_version table.

    Uses MAX(id) pattern — after M27 rebuild (2026-04-19) id=1 is the earliest
    applied version chronologically; the latest is at MAX(id). Back-compatible
    with pre-M27 schemas where MAX(id) == 1.
    """
    try:
        row = conn.execute(
            "SELECT version_code FROM schema_version "
            "WHERE id = (SELECT MAX(id) FROM schema_version)"
        ).fetchone()
        return row[0] if row else "unknown"
    except Exception:
        return "unknown"


def export_schema(conn):
    """Query all schema facts from the live database."""
    tables_raw = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' "
        "AND name != 'sqlite_sequence' ORDER BY name"
    ).fetchall()

    tables = {}
    for (tname,) in tables_raw:
        # CREATE TABLE statement
        sql_row = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' AND name=?",
            (tname,),
        ).fetchone()
        create_sql = sql_row[0] if sql_row else None

        # Columns via PRAGMA
        cols_raw = conn.execute(f"PRAGMA table_info([{tname}])").fetchall()
        columns = []
        for c in cols_raw:
            columns.append({
                "name": c[1],
                "type": c[2],
                "notnull": bool(c[3]),
                "default": c[4],  # None if no default
            })

        # Indexes via PRAGMA
        idxs_raw = conn.execute(f"PRAGMA index_list([{tname}])").fetchall()
        indexes = []
        for idx in idxs_raw:
            indexes.append({
                "name": idx[1],
                "unique": bool(idx[2]),
            })

        # Row count
        row_count = conn.execute(f"SELECT COUNT(*) FROM [{tname}]").fetchone()[0]

        tables[tname] = {
            "sql": create_sql,
            "columns": columns,
            "indexes": indexes,
            "row_count": row_count,
        }

    return tables


def main():
    parser = argparse.ArgumentParser(
        description="Export database schema to JSON reference report."
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path. Default: data/schema/database-schema-YYYYMMDD.json",
    )
    parser.add_argument(
        "--db",
        default=DB_PATH,
        help=f"Database path. Default: {DB_PATH}",
    )
    args = parser.parse_args()

    if not os.path.exists(args.db):
        print(f"ERROR: Database not found at {args.db}")
        sys.exit(1)

    conn = sqlite3.connect(args.db)
    conn.row_factory = None  # use tuple rows for PRAGMA compatibility

    today = datetime.date.today().strftime("%Y%m%d")
    schema_version = get_schema_version(conn)

    print(f"Exporting schema from: {args.db}")
    print(f"Schema version: {schema_version}")

    tables = export_schema(conn)
    conn.close()

    report = {
        "schema_version": schema_version,
        "exported_date": datetime.date.today().isoformat(),
        "table_count": len(tables),
        "tables": tables,
    }

    if args.output:
        out_path = args.output
    else:
        out_path = os.path.join(DEFAULT_OUTPUT_DIR, f"database-schema-v{schema_version}-{today}.json")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\nTables exported: {len(tables)}")
    for tname, tdata in sorted(tables.items()):
        print(f"  {tname}: {tdata['row_count']:,} rows, "
              f"{len(tdata['columns'])} cols, {len(tdata['indexes'])} indexes")
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
