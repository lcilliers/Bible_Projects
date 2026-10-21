"""
db.py
─────
Database access helpers for the engine.
Wraps analytics/db_client.py and adds engine-specific queries.
"""

import os
import sys

_ROOT = os.path.join(os.path.dirname(__file__), "..")
# analytics/ lives under scripts/ since the 2026-04-27 folder restructure.
# Add scripts/ to sys.path so `from analytics.* import ...` keeps working.
_SCRIPTS = os.path.join(_ROOT, "scripts")
if _SCRIPTS not in sys.path:
    sys.path.insert(0, _SCRIPTS)

from analytics.db_client import get_connection as _base_get_connection  # noqa: E402


def get_connection(db_path: str | None = None):
    """Return a WAL-mode SQLite connection (row_factory = sqlite3.Row)."""
    conn = _base_get_connection(db_path)
    # WAL already set by db_client; set busy_timeout so concurrent readers
    # don't instantly fail on a write lock.
    conn.execute("PRAGMA busy_timeout = 5000")
    return conn


def get_schema_version(conn) -> str | None:
    """Return the current schema version string, or None if table absent.

    Reads the row with max id, which after M27 rebuild (2026-04-19) reflects the
    latest applied version chronologically. For older schemas where id=1 held
    the current version, this still works because max(id) == 1.
    """
    try:
        row = conn.execute(
            "SELECT version_code FROM schema_version "
            "WHERE id = (SELECT MAX(id) FROM schema_version)"
        ).fetchone()
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


def resolve_verse_and_span(conn, reference: str, strongs: str):
    """Resolve (verse_id, verse_span_id) for a new verse-record from its reference + strong.

    verse_id from the `verse` row; verse_span_id from the master-index (`verse_span_index`) span
    for that verse+strong — exact strong first, else base strong; first occurrence (lowest
    word_index). Returns (None, None)/(vid, None) when nothing resolves. Added 2026-07-07 to fix
    the omission that left onboarded verse-records unlinked to the verse/master index.
    """
    if not reference:
        return None, None
    v = conn.execute("SELECT id FROM verse WHERE reference = ?", (reference,)).fetchone()
    if not v:
        return None, None
    vid = v["id"]
    b = strongs[:-1] if (strongs and len(strongs) > 1 and strongs[-1].isalpha() and strongs[0] in "HG") else strongs
    sp = conn.execute(
        "SELECT id FROM verse_span_index WHERE verse_id=? AND primary_strong=? ORDER BY word_index LIMIT 1",
        (vid, strongs)).fetchone()
    if not sp:
        sp = conn.execute(
            "SELECT id FROM verse_span_index WHERE verse_id=? AND substr(primary_strong,1,5)=? ORDER BY word_index LIMIT 1",
            (vid, b)).fetchone()
    return vid, (sp["id"] if sp else None)
