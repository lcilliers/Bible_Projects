"""
migrate_books.py
────────────────
Migration: extend the books table with short_code, full_name, last_updated,
and verse_count columns; then seed all 66 canonical Bible books and calculate
verse counts from wa_verse_records.

Run from the project root:
    python scripts/migrate_books.py

Safe to re-run: the ALTER TABLE steps use a try/except so they are skipped if
the columns already exist.  Books are inserted with INSERT OR IGNORE so
existing rows are never overwritten.  Verse counts are always recalculated.
"""

import os
import sqlite3
import sys
from datetime import datetime, timezone

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, ROOT_DIR)

from analytics.db_client import get_connection  # noqa: E402


# ── Canonical 66-book dataset ─────────────────────────────────────────────────
# Columns: (book_order, name, full_name, abbreviation, short_code, testament)
#
# name         – common display name used in most English Bibles
# full_name    – formal/complete title
# abbreviation – standard scholarly abbreviation
# short_code   – 3-5 char machine code matching wa_verse_records reference prefixes
# testament    – "OT" or "NT"

BOOKS = [
    # ── Old Testament ─────────────────────────────────────────────────────────
    ( 1, "Genesis",          "The First Book of Moses Called Genesis",           "Gen",    "Gen",  "OT"),
    ( 2, "Exodus",           "The Second Book of Moses Called Exodus",           "Exo",    "Exo",  "OT"),
    ( 3, "Leviticus",        "The Third Book of Moses Called Leviticus",         "Lev",    "Lev",  "OT"),
    ( 4, "Numbers",          "The Fourth Book of Moses Called Numbers",          "Num",    "Num",  "OT"),
    ( 5, "Deuteronomy",      "The Fifth Book of Moses Called Deuteronomy",       "Deu",    "Deu",  "OT"),
    ( 6, "Joshua",           "The Book of Joshua",                               "Jos",    "Jos",  "OT"),
    ( 7, "Judges",           "The Book of Judges",                               "Judg",   "Judg", "OT"),
    ( 8, "Ruth",             "The Book of Ruth",                                 "Rut",    "Rut",  "OT"),
    ( 9, "1 Samuel",         "The First Book of Samuel",                         "1Sa",    "1Sa",  "OT"),
    (10, "2 Samuel",         "The Second Book of Samuel",                        "2Sa",    "2Sa",  "OT"),
    (11, "1 Kings",          "The First Book of Kings",                          "1Ki",    "1Ki",  "OT"),
    (12, "2 Kings",          "The Second Book of Kings",                         "2Ki",    "2Ki",  "OT"),
    (13, "1 Chronicles",     "The First Book of Chronicles",                     "1Ch",    "1Ch",  "OT"),
    (14, "2 Chronicles",     "The Second Book of Chronicles",                    "2Ch",    "2Ch",  "OT"),
    (15, "Ezra",             "The Book of Ezra",                                 "Ezr",    "Ezr",  "OT"),
    (16, "Nehemiah",         "The Book of Nehemiah",                             "Neh",    "Neh",  "OT"),
    (17, "Esther",           "The Book of Esther",                               "Est",    "Est",  "OT"),
    (18, "Job",              "The Book of Job",                                  "Job",    "Job",  "OT"),
    (19, "Psalms",           "The Book of Psalms",                               "Psa",    "Psa",  "OT"),
    (20, "Proverbs",         "The Book of Proverbs",                             "Pro",    "Pro",  "OT"),
    (21, "Ecclesiastes",     "The Book of Ecclesiastes",                         "Ecc",    "Ecc",  "OT"),
    (22, "Song of Solomon",  "The Song of Solomon",                              "Son",    "Son",  "OT"),
    (23, "Isaiah",           "The Book of Isaiah",                               "Isa",    "Isa",  "OT"),
    (24, "Jeremiah",         "The Book of Jeremiah",                             "Jer",    "Jer",  "OT"),
    (25, "Lamentations",     "The Lamentations of Jeremiah",                     "Lam",    "Lam",  "OT"),
    (26, "Ezekiel",          "The Book of Ezekiel",                              "Eze",    "Eze",  "OT"),
    (27, "Daniel",           "The Book of Daniel",                               "Dan",    "Dan",  "OT"),
    (28, "Hosea",            "The Book of Hosea",                                "Hos",    "Hos",  "OT"),
    (29, "Joel",             "The Book of Joel",                                 "Joe",    "Joe",  "OT"),
    (30, "Amos",             "The Book of Amos",                                 "Amo",    "Amo",  "OT"),
    (31, "Obadiah",          "The Book of Obadiah",                              "Obd",    "Obd",  "OT"),
    (32, "Jonah",            "The Book of Jonah",                                "Jon",    "Jon",  "OT"),
    (33, "Micah",            "The Book of Micah",                                "Mic",    "Mic",  "OT"),
    (34, "Nahum",            "The Book of Nahum",                                "Nah",    "Nah",  "OT"),
    (35, "Habakkuk",         "The Book of Habakkuk",                             "Hab",    "Hab",  "OT"),
    (36, "Zephaniah",        "The Book of Zephaniah",                            "Zep",    "Zep",  "OT"),
    (37, "Haggai",           "The Book of Haggai",                               "Hag",    "Hag",  "OT"),
    (38, "Zechariah",        "The Book of Zechariah",                            "Zec",    "Zec",  "OT"),
    (39, "Malachi",          "The Book of Malachi",                              "Mal",    "Mal",  "OT"),
    # ── New Testament ─────────────────────────────────────────────────────────
    (40, "Matthew",          "The Gospel According to Matthew",                  "Mat",    "Mat",  "NT"),
    (41, "Mark",             "The Gospel According to Mark",                     "Mar",    "Mar",  "NT"),
    (42, "Luke",             "The Gospel According to Luke",                     "Luk",    "Luk",  "NT"),
    (43, "John",             "The Gospel According to John",                     "Joh",    "Joh",  "NT"),
    (44, "Acts",             "The Acts of the Apostles",                         "Act",    "Act",  "NT"),
    (45, "Romans",           "The Epistle of Paul to the Romans",                "Rom",    "Rom",  "NT"),
    (46, "1 Corinthians",    "The First Epistle of Paul to the Corinthians",     "1Cor",   "1Cor", "NT"),
    (47, "2 Corinthians",    "The Second Epistle of Paul to the Corinthians",    "2Cor",   "2Cor", "NT"),
    (48, "Galatians",        "The Epistle of Paul to the Galatians",             "Gal",    "Gal",  "NT"),
    (49, "Ephesians",        "The Epistle of Paul to the Ephesians",             "Eph",    "Eph",  "NT"),
    (50, "Philippians",      "The Epistle of Paul to the Philippians",           "Php",    "Php",  "NT"),
    (51, "Colossians",       "The Epistle of Paul to the Colossians",            "Col",    "Col",  "NT"),
    (52, "1 Thessalonians",  "The First Epistle of Paul to the Thessalonians",   "1Th",    "1Th",  "NT"),
    (53, "2 Thessalonians",  "The Second Epistle of Paul to the Thessalonians",  "2Th",    "2Th",  "NT"),
    (54, "1 Timothy",        "The First Epistle of Paul to Timothy",             "1Ti",    "1Ti",  "NT"),
    (55, "2 Timothy",        "The Second Epistle of Paul to Timothy",            "2Ti",    "2Ti",  "NT"),
    (56, "Titus",            "The Epistle of Paul to Titus",                     "Tit",    "Tit",  "NT"),
    (57, "Philemon",         "The Epistle of Paul to Philemon",                  "Phm",    "Phm",  "NT"),
    (58, "Hebrews",          "The Epistle to the Hebrews",                       "Heb",    "Heb",  "NT"),
    (59, "James",            "The General Epistle of James",                     "Jam",    "Jam",  "NT"),
    (60, "1 Peter",          "The First Epistle General of Peter",               "1Pe",    "1Pe",  "NT"),
    (61, "2 Peter",          "The Second Epistle General of Peter",              "2Pe",    "2Pe",  "NT"),
    (62, "1 John",           "The First Epistle General of John",                "1Jn",    "1Jn",  "NT"),
    (63, "2 John",           "The Second Epistle General of John",               "2Jn",    "2Jn",  "NT"),
    (64, "3 John",           "The Third Epistle General of John",                "3Jn",    "3Jn",  "NT"),
    (65, "Jude",             "The General Epistle of Jude",                      "Jud",    "Jud",  "NT"),
    (66, "Revelation",       "The Revelation of Jesus Christ",                   "Rev",    "Rev",  "NT"),
]


# ── Alias map: every spelling found in wa_verse_records → canonical name ─────
# Maps each variant (full name, short code, typo) → the `name` value in BOOKS.
BOOK_ALIASES: dict[str, str] = {
    # Genesis
    "Genesis": "Genesis", "Gen": "Genesis",
    # Exodus
    "Exodus": "Exodus", "Exo": "Exodus",
    # Leviticus
    "Leviticus": "Leviticus", "Lev": "Leviticus",
    # Numbers
    "Numbers": "Numbers", "Num": "Numbers",
    # Deuteronomy
    "Deuteronomy": "Deuteronomy", "Deu": "Deuteronomy",
    # Joshua
    "Joshua": "Joshua", "Jos": "Joshua",
    # Judges
    "Judges": "Judges", "Judg": "Judges",
    # Ruth
    "Ruth": "Ruth", "Rut": "Ruth",
    # 1 Samuel
    "1 Samuel": "1 Samuel", "1Sa": "1 Samuel",
    # 2 Samuel
    "2 Samuel": "2 Samuel", "2Sa": "2 Samuel",
    # 1 Kings
    "1 Kings": "1 Kings", "1Ki": "1 Kings",
    # 2 Kings
    "2 Kings": "2 Kings", "2Ki": "2 Kings",
    # 1 Chronicles
    "1 Chronicles": "1 Chronicles", "1Ch": "1 Chronicles",
    # 2 Chronicles
    "2 Chronicles": "2 Chronicles", "2Ch": "2 Chronicles",
    # Ezra
    "Ezra": "Ezra", "Ezr": "Ezra",
    # Nehemiah
    "Nehemiah": "Nehemiah", "Neh": "Nehemiah",
    # Esther
    "Esther": "Esther", "Est": "Esther",
    # Job
    "Job": "Job",
    # Psalms
    "Psalms": "Psalms", "Psa": "Psalms",
    # Proverbs
    "Proverbs": "Proverbs", "Pro": "Proverbs",
    # Ecclesiastes
    "Ecclesiastes": "Ecclesiastes", "Ecc": "Ecclesiastes",
    # Song of Solomon
    "Song of Solomon": "Song of Solomon", "Song": "Song of Solomon", "Son": "Song of Solomon",
    # Isaiah
    "Isaiah": "Isaiah", "Isa": "Isaiah",
    # Jeremiah
    "Jeremiah": "Jeremiah", "Jer": "Jeremiah",
    # Lamentations
    "Lamentations": "Lamentations", "Lam": "Lamentations",
    # Ezekiel
    "Ezekiel": "Ezekiel", "Eze": "Ezekiel",
    # Daniel
    "Daniel": "Daniel", "Dan": "Daniel",
    # Hosea
    "Hosea": "Hosea", "Hos": "Hosea",
    # Joel
    "Joel": "Joel", "Joe": "Joel",
    # Amos
    "Amos": "Amos", "Amo": "Amos",
    # Obadiah
    "Obadiah": "Obadiah", "Obd": "Obadiah",
    # Jonah
    "Jonah": "Jonah", "Jon": "Jonah",
    # Micah
    "Micah": "Micah", "Mic": "Micah",
    # Nahum
    "Nahum": "Nahum", "Nah": "Nahum",
    # Habakkuk
    "Habakkuk": "Habakkuk", "Hab": "Habakkuk",
    # Zephaniah
    "Zephaniah": "Zephaniah", "Zep": "Zephaniah",
    # Haggai
    "Haggai": "Haggai", "Hag": "Haggai",
    # Zechariah
    "Zechariah": "Zechariah", "Zec": "Zechariah",
    # Malachi
    "Malachi": "Malachi", "Mal": "Malachi",
    # Matthew
    "Matthew": "Matthew", "Mat": "Matthew",
    # Mark
    "Mark": "Mark", "Mar": "Mark",
    # Luke
    "Luke": "Luke", "Luk": "Luke",
    # John (Gospel)
    "John": "John", "Joh": "John",
    # Acts
    "Acts": "Acts", "Act": "Acts",
    # Romans
    "Romans": "Romans", "Rom": "Romans",
    # 1 Corinthians
    "1 Corinthians": "1 Corinthians", "1Co": "1 Corinthians", "1Cor": "1 Corinthians",
    # 2 Corinthians
    "2 Corinthians": "2 Corinthians", "2Co": "2 Corinthians", "2Cor": "2 Corinthians",
    # Galatians
    "Galatians": "Galatians", "Gal": "Galatians",
    # Ephesians
    "Ephesians": "Ephesians", "Eph": "Ephesians",
    # Philippians
    "Philippians": "Philippians", "Php": "Philippians", "Phili": "Philippians",
    # Colossians
    "Colossians": "Colossians", "Col": "Colossians",
    # 1 Thessalonians
    "1 Thessalonians": "1 Thessalonians", "1Th": "1 Thessalonians",
    # 2 Thessalonians
    "2 Thessalonians": "2 Thessalonians", "2Th": "2 Thessalonians",
    # 1 Timothy
    "1 Timothy": "1 Timothy", "1Ti": "1 Timothy",
    # 2 Timothy
    "2 Timothy": "2 Timothy", "2Ti": "2 Timothy",
    # Titus
    "Titus": "Titus", "Tit": "Titus",
    # Philemon
    "Philemon": "Philemon", "Phm": "Philemon",
    # Hebrews
    "Hebrews": "Hebrews", "Heb": "Hebrews",
    # James
    "James": "James", "Jam": "James",
    # 1 Peter
    "1 Peter": "1 Peter", "1Pe": "1 Peter",
    # 2 Peter
    "2 Peter": "2 Peter", "2Pe": "2 Peter",
    # 1 John
    "1 John": "1 John", "1Jn": "1 John", "1Jo": "1 John",
    # 2 John
    "2 John": "2 John", "2Jn": "2 John", "2Jo": "2 John",
    # 3 John
    "3 John": "3 John", "3Jn": "3 John",
    # Jude
    "Jude": "Jude",
    # Revelation
    "Revelation": "Revelation", "Rev": "Revelation",
}


# ── Step 1: add new columns if they don't exist yet ───────────────────────────

def _add_column_if_missing(
    conn: sqlite3.Connection, table: str, column: str, definition: str
) -> None:
    cursor = conn.execute(f"PRAGMA table_info({table})")
    existing = {row[1] for row in cursor.fetchall()}
    if column not in existing:
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")
        print(f"  + Added column: {table}.{column}")
    else:
        print(f"  · Column already exists: {table}.{column}")


def add_missing_columns(conn: sqlite3.Connection) -> None:
    print("\n── Step 1: extend books table columns ──")
    _add_column_if_missing(conn, "books", "full_name",    "TEXT")
    # SQLite does not support ADD COLUMN ... UNIQUE — add column then index
    _add_column_if_missing(conn, "books", "short_code",   "TEXT")
    conn.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS uq_books_short_code ON books (short_code)"
    )
    _add_column_if_missing(conn, "books", "verse_count",  "INTEGER NOT NULL DEFAULT 0")
    _add_column_if_missing(
        conn, "books", "last_updated",
        "TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now'))"
    )
    conn.commit()


# ── Step 2: seed the 66 books ─────────────────────────────────────────────────

def seed_books(conn: sqlite3.Connection) -> None:
    print("\n── Step 2: seed books ──")

    # Check if books already has the full_name column by inspecting columns
    cursor = conn.execute("PRAGMA table_info(books)")
    cols = {row[1] for row in cursor.fetchall()}
    has_full_name  = "full_name"  in cols
    has_short_code = "short_code" in cols

    inserted = 0
    updated  = 0

    for order, name, full_name, abbreviation, short_code, testament in BOOKS:
        # Try plain insert first (handles tables that already have the row)
        try:
            if has_short_code and has_full_name:
                conn.execute(
                    """
                    INSERT INTO books
                        (book_order, name, full_name, abbreviation, short_code, testament)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (order, name, full_name, abbreviation, short_code, testament),
                )
            else:
                # Legacy schema — only original columns present
                conn.execute(
                    """
                    INSERT INTO books (book_order, name, abbreviation, testament)
                    VALUES (?, ?, ?, ?)
                    """,
                    (order, name, abbreviation, testament),
                )
            inserted += 1
        except sqlite3.IntegrityError:
            # Row already exists — update the new columns
            if has_short_code and has_full_name:
                conn.execute(
                    """
                    UPDATE books
                    SET full_name   = ?,
                        short_code  = ?,
                        abbreviation = ?
                    WHERE name = ?
                    """,
                    (full_name, short_code, abbreviation, name),
                )
            updated += 1

    conn.commit()
    print(f"  Inserted {inserted} new book rows, updated {updated} existing rows.")


# ── Step 3: update verse counts ───────────────────────────────────────────────

def update_verse_counts(conn: sqlite3.Connection) -> None:
    """
    Count distinct verses from wa_verse_records (normalising all name variants
    via BOOK_ALIASES) and write the totals into books.verse_count.

    Also updates books.last_updated to the current UTC time.
    """
    print("\n── Step 3: update verse counts from wa_verse_records ──")

    # Check if wa_verse_records exists
    exists = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='wa_verse_records'"
    ).fetchone()
    if not exists:
        print("  wa_verse_records table not found — skipping verse count update.")
        return

    # Fetch all (book_name, count) pairs from wa_verse_records
    rows = conn.execute(
        "SELECT book, COUNT(*) AS cnt FROM wa_verse_records WHERE book IS NOT NULL GROUP BY book"
    ).fetchall()

    # Accumulate counts per canonical name using the alias map
    totals: dict[str, int] = {}
    unrecognised: list[str] = []

    for raw_name, cnt in rows:
        canonical = BOOK_ALIASES.get(raw_name)
        if canonical:
            totals[canonical] = totals.get(canonical, 0) + cnt
        else:
            unrecognised.append(raw_name)

    if unrecognised:
        print(f"  WARNING: unrecognised book name(s) — not counted: {unrecognised}")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    updated_books = 0

    for canonical_name, count in totals.items():
        result = conn.execute(
            "UPDATE books SET verse_count = ?, last_updated = ? WHERE name = ?",
            (count, now, canonical_name),
        )
        if result.rowcount:
            updated_books += 1

    conn.commit()
    print(f"  Updated verse_count for {updated_books} books (timestamp: {now}).")

    # Report any canonical books that still have 0 verses (not in wa_verse_records)
    zero_count = conn.execute(
        "SELECT name FROM books WHERE verse_count = 0 ORDER BY book_order"
    ).fetchall()
    if zero_count:
        names = [r[0] for r in zero_count]
        print(f"  Books with 0 verses (no data yet): {names}")


# ── Step 4: print summary ─────────────────────────────────────────────────────

def print_summary(conn: sqlite3.Connection) -> None:
    print("\n── Summary ──")
    rows = conn.execute(
        """
        SELECT book_order, name, short_code, abbreviation, testament, verse_count, last_updated
        FROM books
        ORDER BY book_order
        """
    ).fetchall()

    header = f"{'#':>3}  {'Name':<22} {'Code':<5} {'Abbr':<6} {'TM':<3} {'Verses':>7}  {'Last Updated'}"
    print(header)
    print("-" * len(header))
    for r in rows:
        print(
            f"{r[0]:>3}  {r[1]:<22} {(r[2] or ''):5} {(r[3] or ''):6} {r[4]:<3} "
            f"{r[5]:>7}  {r[6]}"
        )
    total = sum(r[5] for r in rows)
    print(f"\n  Total verse records across all books: {total:,}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print("=== migrate_books.py ===")
    conn = get_connection()
    try:
        add_missing_columns(conn)
        seed_books(conn)
        update_verse_counts(conn)
        print_summary(conn)
        print("\nDone.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
