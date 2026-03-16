"""
db_client.py
────────────
SQLite database utilities for Bible_Projects.

Provides:
  - get_connection()          — open/create the SQLite database
  - init_schema_from_file()   — run data/schema/create_tables.sql
  - import_json_records()     — bulk-insert a list of dicts into a table
  - query_to_json()           — run SQL and return results as a list of dicts
  - export_table_to_json()    — dump an entire table to a list of dicts

Configuration (read from .env):
  DB_PATH   — path to the .db file, relative to project root
              default: data/bible_research.db

See docs/data_setup.md for full usage instructions.
"""

import json
import os
import sqlite3
from typing import Any, Optional

import pandas as pd
from dotenv import load_dotenv

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
load_dotenv(os.path.join(ROOT_DIR, ".env"))

_DEFAULT_SCHEMA = os.path.join(ROOT_DIR, "data", "schema", "create_tables.sql")

# Allowed table names — must match exactly what is in create_tables.sql.
# This list is the sole authoritative whitelist used to prevent SQL injection
# when table names are interpolated into query strings.
_ALLOWED_TABLES = frozenset({
    "books",
    "themes",
    "sources",
    "verse_notes",
    "verse_theme_map",
    "verse_source_map",
})


def _validate_table(table: str) -> str:
    """Return ``table`` if it is a known table name, otherwise raise ValueError."""
    if table not in _ALLOWED_TABLES:
        raise ValueError(
            f"Unknown table {table!r}. Allowed tables: {sorted(_ALLOWED_TABLES)}"
        )
    return table


# ── Connection ───────────────────────────────────────────────────────────────

def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Open (or create) the SQLite database and return a connection.

    Parameters
    ----------
    db_path : str, optional
        Path to the ``.db`` file. Falls back to the ``DB_PATH`` environment
        variable, then to ``data/bible_research.db`` relative to the project root.

    Returns
    -------
    sqlite3.Connection
        Connection with ``row_factory`` set to ``sqlite3.Row`` so that query
        results can be accessed by column name.
    """
    if db_path is None:
        db_path = os.getenv("DB_PATH", os.path.join(ROOT_DIR, "data", "bible_research.db"))

    # Ensure the parent directory exists
    os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")  # better concurrent read performance
    return conn


# ── Schema initialisation ────────────────────────────────────────────────────

def init_schema_from_file(
    conn: sqlite3.Connection,
    schema_path: Optional[str] = None,
) -> None:
    """Execute the SQL schema file to create tables if they do not exist.

    Parameters
    ----------
    conn : sqlite3.Connection
        Open database connection.
    schema_path : str, optional
        Path to the ``.sql`` file. Defaults to
        ``data/schema/create_tables.sql`` relative to the project root.
    """
    if schema_path is None:
        schema_path = _DEFAULT_SCHEMA

    with open(schema_path, "r", encoding="utf-8") as f:
        sql = f.read()

    conn.executescript(sql)
    conn.commit()


# ── JSON import ──────────────────────────────────────────────────────────────

def import_json_records(
    conn: sqlite3.Connection,
    table: str,
    records: list,
    if_exists: str = "append",
) -> int:
    """Bulk-insert a list of dicts (e.g. from Claude's JSON output) into a table.

    Uses ``pandas.DataFrame.to_sql`` for efficient batch inserts.

    Parameters
    ----------
    conn : sqlite3.Connection
        Open database connection.
    table : str
        Target table name (must exist in the database).
    records : list of dict
        Each dict represents one row; keys must match column names.
        Extra keys (e.g. ``"theme_tags"``, ``"source_refs"``) that are not
        columns in ``table`` are silently dropped before insertion.
    if_exists : str
        Passed to ``pandas.DataFrame.to_sql``: ``"append"`` (default) adds rows;
        ``"replace"`` drops and recreates the table first.

    Returns
    -------
    int
        Number of rows successfully inserted.
    """
    if not records:
        return 0

    df = pd.DataFrame(records)

    # ── Drop keys that are not columns in the target table ──────────────────
    _validate_table(table)
    cursor = conn.execute(f"PRAGMA table_info({table})")
    columns = {row["name"] for row in cursor.fetchall()}
    df = df[[col for col in df.columns if col in columns]]

    df.to_sql(table, conn, if_exists=if_exists, index=False, method="multi")
    conn.commit()
    return len(df)


def import_json_file(
    conn: sqlite3.Connection,
    json_path: str,
    table: str,
) -> int:
    """Load a JSON file and import all records into ``table``.

    Parameters
    ----------
    conn : sqlite3.Connection
        Open database connection.
    json_path : str
        Path to the JSON file (array of record objects).
    table : str
        Target table name.

    Returns
    -------
    int
        Number of rows inserted.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        records = json.load(f)

    if not isinstance(records, list):
        raise ValueError(
            f"Expected a JSON array of records in {json_path!r}, got {type(records).__name__}."
        )

    return import_json_records(conn, table, records)


# ── Query / export ───────────────────────────────────────────────────────────

def query_to_json(conn: sqlite3.Connection, sql: str, params: Any = ()) -> list:
    """Run a SQL SELECT and return the results as a list of dicts.

    Suitable for exporting data for Claude to read.

    Parameters
    ----------
    conn : sqlite3.Connection
        Open database connection.
    sql : str
        SQL SELECT statement.
    params : tuple or dict, optional
        Bound parameters for the query.

    Returns
    -------
    list of dict
        Each dict represents one row.
    """
    cursor = conn.execute(sql, params)
    return [dict(row) for row in cursor.fetchall()]


def export_table_to_json(
    conn: sqlite3.Connection,
    table: str,
    output_path: Optional[str] = None,
    limit: Optional[int] = None,
) -> list:
    """Dump an entire table (or a row-limited slice) to a list of dicts.

    Optionally writes the result to a JSON file in ``data/exports/``.

    Parameters
    ----------
    conn : sqlite3.Connection
        Open database connection.
    table : str
        Table name to export.
    output_path : str, optional
        If provided, write JSON to this file path.
    limit : int, optional
        Maximum number of rows to export. Exports all rows if ``None``.

    Returns
    -------
    list of dict
        Exported rows.
    """
    sql = f"SELECT * FROM {_validate_table(table)}"
    if limit is not None:
        sql += f" LIMIT {int(limit)}"

    rows = query_to_json(conn, sql)

    if output_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(rows, f, indent=2, ensure_ascii=False)

    return rows


# ── Diagnostics ──────────────────────────────────────────────────────────────

def list_tables(conn: sqlite3.Connection) -> list:
    """Return the names of all user tables in the database."""
    rows = query_to_json(
        conn,
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name",
    )
    return [r["name"] for r in rows]


def row_count(conn: sqlite3.Connection, table: str) -> int:
    """Return the number of rows in ``table``."""
    result = conn.execute(
        f"SELECT COUNT(*) AS n FROM {_validate_table(table)}"
    ).fetchone()
    return result["n"]
