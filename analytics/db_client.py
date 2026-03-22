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
    "book_code_variants",
    "books",
    "themes",
    "sources",
    "wa_verse_records",
    "wa_file_index",
    "wa_term_inventory",
    "wa_term_related_words",
    "wa_term_root_family",
    "wa_term_flags",
    "wa_term_phase2_flags",
    "phase2_flag_types",
    "wa_quality_flag_types",
    "wa_cross_registry_links",
    "wa_crosslink_type",
    "wa_data_quality_flags",
    "word_registry",
    "mti_terms",
    "mti_term_flags",
    "mti_term_cross_refs",
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
    mode = conn.execute("PRAGMA journal_mode").fetchone()[0]
    if mode != "delete":
        raise RuntimeError(
            f"Database journal_mode is '{mode}', expected 'delete'. "
            "Do not run engine scripts in WAL mode on Google Drive."
        )
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


# ── Books helpers ─────────────────────────────────────────────────────────────

# Alias map: every spelling found in source tables → canonical books.name value.
# Extend this dict if new abbreviation variants appear in imported data.
_BOOK_ALIASES: dict = {
    "Genesis": "Genesis", "Gen": "Genesis",
    "Exodus": "Exodus", "Exo": "Exodus",
    "Leviticus": "Leviticus", "Lev": "Leviticus",
    "Numbers": "Numbers", "Num": "Numbers",
    "Deuteronomy": "Deuteronomy", "Deu": "Deuteronomy",
    "Joshua": "Joshua", "Jos": "Joshua",
    "Judges": "Judges", "Judg": "Judges",
    "Ruth": "Ruth", "Rut": "Ruth",
    "1 Samuel": "1 Samuel", "1Sa": "1 Samuel",
    "2 Samuel": "2 Samuel", "2Sa": "2 Samuel",
    "1 Kings": "1 Kings", "1Ki": "1 Kings",
    "2 Kings": "2 Kings", "2Ki": "2 Kings",
    "1 Chronicles": "1 Chronicles", "1Ch": "1 Chronicles",
    "2 Chronicles": "2 Chronicles", "2Ch": "2 Chronicles",
    "Ezra": "Ezra", "Ezr": "Ezra",
    "Nehemiah": "Nehemiah", "Neh": "Nehemiah",
    "Esther": "Esther", "Est": "Esther",
    "Job": "Job",
    "Psalms": "Psalms", "Psa": "Psalms",
    "Proverbs": "Proverbs", "Pro": "Proverbs",
    "Ecclesiastes": "Ecclesiastes", "Ecc": "Ecclesiastes",
    "Song of Solomon": "Song of Solomon", "Song": "Song of Solomon", "Son": "Song of Solomon",
    "Isaiah": "Isaiah", "Isa": "Isaiah",
    "Jeremiah": "Jeremiah", "Jer": "Jeremiah",
    "Lamentations": "Lamentations", "Lam": "Lamentations",
    "Ezekiel": "Ezekiel", "Eze": "Ezekiel",
    "Daniel": "Daniel", "Dan": "Daniel",
    "Hosea": "Hosea", "Hos": "Hosea",
    "Joel": "Joel", "Joe": "Joel",
    "Amos": "Amos", "Amo": "Amos",
    "Obadiah": "Obadiah", "Obd": "Obadiah",
    "Jonah": "Jonah", "Jon": "Jonah",
    "Micah": "Micah", "Mic": "Micah",
    "Nahum": "Nahum", "Nah": "Nahum",
    "Habakkuk": "Habakkuk", "Hab": "Habakkuk",
    "Zephaniah": "Zephaniah", "Zep": "Zephaniah",
    "Haggai": "Haggai", "Hag": "Haggai",
    "Zechariah": "Zechariah", "Zec": "Zechariah",
    "Malachi": "Malachi", "Mal": "Malachi",
    "Matthew": "Matthew", "Mat": "Matthew",
    "Mark": "Mark", "Mar": "Mark",
    "Luke": "Luke", "Luk": "Luke",
    "John": "John", "Joh": "John",
    "Acts": "Acts", "Act": "Acts",
    "Romans": "Romans", "Rom": "Romans",
    "1 Corinthians": "1 Corinthians", "1Co": "1 Corinthians", "1Cor": "1 Corinthians",
    "2 Corinthians": "2 Corinthians", "2Co": "2 Corinthians", "2Cor": "2 Corinthians",
    "Galatians": "Galatians", "Gal": "Galatians",
    "Ephesians": "Ephesians", "Eph": "Ephesians",
    "Philippians": "Philippians", "Php": "Philippians", "Phili": "Philippians",
    "Colossians": "Colossians", "Col": "Colossians",
    "1 Thessalonians": "1 Thessalonians", "1Th": "1 Thessalonians",
    "2 Thessalonians": "2 Thessalonians", "2Th": "2 Thessalonians",
    "1 Timothy": "1 Timothy", "1Ti": "1 Timothy",
    "2 Timothy": "2 Timothy", "2Ti": "2 Timothy",
    "Titus": "Titus", "Tit": "Titus",
    "Philemon": "Philemon", "Phm": "Philemon",
    "Hebrews": "Hebrews", "Heb": "Hebrews",
    "James": "James", "Jam": "James",
    "1 Peter": "1 Peter", "1Pe": "1 Peter",
    "2 Peter": "2 Peter", "2Pe": "2 Peter",
    "1 John": "1 John", "1Jn": "1 John", "1Jo": "1 John",
    "2 John": "2 John", "2Jn": "2 John", "2Jo": "2 John",
    "3 John": "3 John", "3Jn": "3 John",
    "Jude": "Jude",
    "Revelation": "Revelation", "Rev": "Revelation",
}


def resolve_verse_refs(
    conn: sqlite3.Connection,
    only_missing: bool = True,
) -> int:
    """Parse ``reference`` strings and populate ``book_id``, ``chapter``,
    and ``verse_num`` in ``wa_verse_records``.

    Uses the ``book_code_variants`` table to resolve any STEP short code
    (or known alias) to the correct ``book_id``.  Call this after every
    import that writes rows with only a ``reference`` value.

    Parameters
    ----------
    only_missing : bool
        When ``True`` (default), only rows where at least one of
        ``book_id``, ``chapter``, or ``verse_num`` is NULL are processed.
        Set ``False`` to reprocess every row that has a ``reference``.

    Returns
    -------
    int
        Number of rows updated.
    """
    import re
    import warnings

    where = (
        "WHERE reference IS NOT NULL "
        "AND (book_id IS NULL OR chapter IS NULL OR verse_num IS NULL)"
        if only_missing
        else "WHERE reference IS NOT NULL"
    )
    rows = conn.execute(
        f"SELECT id, reference FROM wa_verse_records {where}"
    ).fetchall()

    # Build code -> book_id lookup from the variants table
    variants: dict = {
        r["code"]: r["book_id"]
        for r in conn.execute(
            "SELECT code, book_id FROM book_code_variants"
        ).fetchall()
    }

    updates = []
    skipped = []
    for row in rows:
        ref = (row["reference"] or "").strip()
        parts = ref.split(" ", 1)
        if len(parts) != 2:
            skipped.append(row["id"])
            continue
        code, loc = parts
        book_id = variants.get(code)
        if not book_id:
            skipped.append(row["id"])
            continue
        try:
            if ":" in loc:
                ch, vs = loc.split(":", 1)
                chapter, verse_num = int(ch), int(vs)
            else:
                # Single-chapter book: reference is "Code versenum"
                chapter, verse_num = 1, int(loc)
        except ValueError:
            skipped.append(row["id"])
            continue
        updates.append((book_id, chapter, verse_num, row["id"]))

    if updates:
        conn.executemany(
            "UPDATE wa_verse_records "
            "SET book_id=?, chapter=?, verse_num=? WHERE id=?",
            updates,
        )
        conn.commit()

    if skipped:
        warnings.warn(
            f"resolve_verse_refs: {len(skipped)} row(s) could not be resolved "
            f"(unknown code or bad format). ids={skipped[:10]}"
            f"{'...' if len(skipped) > 10 else ''}"
        )

    return len(updates)


def update_book_verse_counts(conn: sqlite3.Connection) -> dict:
    """Refresh ``books.verse_count`` with the number of *distinct* verses
    per book recorded in ``wa_verse_records``.

    Counts by (chapter, verse_num) per book_id — so a verse that appears
    under multiple terms is only counted once.

    Returns
    -------
    dict
        ``{"updated": <n books updated>}``
    """
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    rows = conn.execute(
        "SELECT book_id, COUNT(DISTINCT chapter || ':' || verse_num) AS cnt"
        " FROM wa_verse_records"
        " WHERE book_id IS NOT NULL"
        " GROUP BY book_id"
    ).fetchall()

    updated = 0
    for book_id, cnt in rows:
        result = conn.execute(
            "UPDATE books SET verse_count = ?, last_updated = ? WHERE id = ?",
            (cnt, now, book_id),
        )
        updated += result.rowcount

    conn.commit()
    return {"updated": updated}
