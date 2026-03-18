"""
db.py
─────
Database access helpers for the engine.
Wraps analytics/db_client.py and adds engine-specific queries.
"""

import os
import sys

# Allow importing from analytics/ at project root.
_ROOT = os.path.join(os.path.dirname(__file__), "..")
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from analytics.db_client import get_connection as _base_get_connection  # noqa: E402


def get_connection(db_path: str | None = None):
    """Return a WAL-mode SQLite connection (row_factory = sqlite3.Row)."""
    conn = _base_get_connection(db_path)
    # WAL already set by db_client; set busy_timeout so concurrent readers
    # don't instantly fail on a write lock.
    conn.execute("PRAGMA busy_timeout = 5000")
    return conn


def get_schema_version(conn) -> str | None:
    """Return the current schema version string, or None if table absent."""
    try:
        row = conn.execute("SELECT version_code FROM schema_version WHERE id = 1").fetchone()
        return row["version_code"] if row else None
    except Exception:
        return None


def get_registry_row(conn, registry_id: int):
    """Return the word_registry row for registry_id, or None."""
    return conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_id,)
    ).fetchone()


def get_max_id(conn, table: str) -> int:
    """Return MAX(id) for a table, or 0 if empty."""
    row = conn.execute(f"SELECT MAX(id) AS m FROM {table}").fetchone()  # noqa: S608
    return row["m"] or 0


def get_book_id(conn, book_code: str) -> int | None:
    """Resolve an OSIS book code to books.id via book_code_variants."""
    row = conn.execute(
        "SELECT book_id FROM book_code_variants WHERE code = ?", (book_code,)
    ).fetchone()
    return row["book_id"] if row else None
