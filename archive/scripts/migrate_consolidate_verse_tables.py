"""
migrate_consolidate_verse_tables.py
────────────────────────────────────
Consolidates the verse data model:

  BEFORE
  ──────
  verse_notes        — empty research-annotation table (redundant)
  verse_theme_map    — FK child of verse_notes (empty)
  verse_source_map   — FK child of verse_notes (empty)
  wa_verse_records   — core STEP term-occurrence table (11 603 rows),
                       but with inconsistent book names and reference
                       prefixes across imports.

  AFTER
  ─────
  wa_verse_records   — single authoritative verse table, extended with:
                         book_id       INTEGER FK → books.id  (normalised)
                         chapter       INTEGER                (parsed)
                         verse_num     INTEGER                (parsed)
                         translation   TEXT DEFAULT 'ESV'     (from wa_file_index)
                         note          TEXT                   (future research)
                         claude_output TEXT                   (future Claude output)
                         created_at    TEXT                   (ISO-8601 audit)
                         updated_at    TEXT                   (ISO-8601, auto-maintained)
                       • book column    normalised → books.name
                       • reference col  normalised → '{short_code} {chapter}:{verse}'
  verse_notes, verse_theme_map, verse_source_map  — DROPPED

  books.short_code   — 3 entries corrected to match STEP dominant conventions:
                         Judges → Judg   (was Jdg)
                         1 Corinthians → 1Cor  (was 1Co)
                         2 Corinthians → 2Cor  (was 2Co)

Run from the project root:
    python scripts/migrate_consolidate_verse_tables.py

Safe to re-run: column additions are skipped if they already exist;
reference normalisation is idempotent (rows with a valid book_id are skipped).
"""

import os
import re
import sys
from datetime import datetime, timezone

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, ROOT_DIR)

from analytics.db_client import get_connection  # noqa: E402

# ── Alias map ─────────────────────────────────────────────────────────────────
# Every variant (full name, abbreviation, typo) found in wa_verse_records.book
# OR wa_verse_records.reference prefix → canonical books.name value.

REF_ALIAS: dict[str, str] = {
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
    "Judges": "Judges", "Judg": "Judges", "Jdg": "Judges",
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
    "Psalms": "Psalms", "Psa": "Psalms", "Ps": "Psalms",
    # Proverbs
    "Proverbs": "Proverbs", "Pro": "Proverbs", "Prov": "Proverbs",
    # Ecclesiastes
    "Ecclesiastes": "Ecclesiastes", "Ecc": "Ecclesiastes", "Eccl": "Ecclesiastes",
    # Song of Solomon
    "Song of Solomon": "Song of Solomon", "Song": "Song of Solomon", "Son": "Song of Solomon",
    # Isaiah
    "Isaiah": "Isaiah", "Isa": "Isaiah",
    # Jeremiah
    "Jeremiah": "Jeremiah", "Jer": "Jeremiah",
    # Lamentations
    "Lamentations": "Lamentations", "Lam": "Lamentations",
    # Ezekiel
    "Ezekiel": "Ezekiel", "Eze": "Ezekiel", "Ezek": "Ezekiel",
    # Daniel
    "Daniel": "Daniel", "Dan": "Daniel",
    # Hosea
    "Hosea": "Hosea", "Hos": "Hosea",
    # Joel
    "Joel": "Joel", "Joe": "Joel",
    # Amos
    "Amos": "Amos", "Amo": "Amos",
    # Obadiah
    "Obadiah": "Obadiah", "Obd": "Obadiah", "Obad": "Obadiah",
    # Jonah
    "Jonah": "Jonah", "Jon": "Jonah",
    # Micah
    "Micah": "Micah", "Mic": "Micah",
    # Nahum
    "Nahum": "Nahum", "Nah": "Nahum",
    # Habakkuk
    "Habakkuk": "Habakkuk", "Hab": "Habakkuk",
    # Zephaniah
    "Zephaniah": "Zephaniah", "Zep": "Zephaniah", "Zeph": "Zephaniah",
    # Haggai
    "Haggai": "Haggai", "Hag": "Haggai",
    # Zechariah
    "Zechariah": "Zechariah", "Zec": "Zechariah", "Zech": "Zechariah",
    # Malachi
    "Malachi": "Malachi", "Mal": "Malachi",
    # Matthew
    "Matthew": "Matthew", "Mat": "Matthew", "Matt": "Matthew",
    # Mark
    "Mark": "Mark", "Mar": "Mark", "Mk": "Mark",
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
    "Phi": "Philippians", "Phil": "Philippians",
    # Colossians
    "Colossians": "Colossians", "Col": "Colossians",
    # 1 Thessalonians
    "1 Thessalonians": "1 Thessalonians", "1Th": "1 Thessalonians", "1Thes": "1 Thessalonians",
    # 2 Thessalonians
    "2 Thessalonians": "2 Thessalonians", "2Th": "2 Thessalonians", "2Thes": "2 Thessalonians",
    # 1 Timothy
    "1 Timothy": "1 Timothy", "1Ti": "1 Timothy", "1Tim": "1 Timothy",
    # 2 Timothy
    "2 Timothy": "2 Timothy", "2Ti": "2 Timothy", "2Tim": "2 Timothy",
    # Titus
    "Titus": "Titus", "Tit": "Titus",
    # Philemon
    "Philemon": "Philemon", "Phm": "Philemon", "Phile": "Philemon", "Phlm": "Philemon",
    # Hebrews
    "Hebrews": "Hebrews", "Heb": "Hebrews",
    # James
    "James": "James", "Jam": "James", "Jas": "James",
    # 1 Peter
    "1 Peter": "1 Peter", "1Pe": "1 Peter", "1Pet": "1 Peter",
    # 2 Peter
    "2 Peter": "2 Peter", "2Pe": "2 Peter", "2Pet": "2 Peter",
    # 1 John
    "1 John": "1 John", "1Jn": "1 John", "1Jo": "1 John", "1Joh": "1 John",
    # 2 John
    "2 John": "2 John", "2Jn": "2 John", "2Jo": "2 John", "2Joh": "2 John",
    # 3 John
    "3 John": "3 John", "3Jn": "3 John", "3Jo": "3 John", "3Joh": "3 John",
    # Jude
    "Jude": "Jude", "Jud": "Jude",
    # Revelation
    "Revelation": "Revelation", "Rev": "Revelation",
}

_REF_RE = re.compile(r"^(\S+)\s+(\d+):(\d+)$")


# ─────────────────────────────────────────────────────────────────────────────
# Step 1 – correct three short_code values in books
# ─────────────────────────────────────────────────────────────────────────────

def fix_book_short_codes(conn) -> None:
    print("\n── Step 1: fix books.short_code for 3 books ──")
    corrections = [
        ("Judges",         "Judg"),   # was Jdg
        ("1 Corinthians",  "1Cor"),   # was 1Co
        ("2 Corinthians",  "2Cor"),   # was 2Co
    ]
    for name, new_code in corrections:
        existing = conn.execute(
            "SELECT short_code FROM books WHERE name = ?", (name,)
        ).fetchone()
        if existing and existing[0] == new_code:
            print(f"  · {name}: short_code already correct ({new_code})")
        else:
            conn.execute(
                "UPDATE books SET short_code = ? WHERE name = ?", (new_code, name)
            )
            old = existing[0] if existing else "?"
            print(f"  ✓ {name}: {old} → {new_code}")
    conn.commit()


# ─────────────────────────────────────────────────────────────────────────────
# Step 2 – add new columns to wa_verse_records
# ─────────────────────────────────────────────────────────────────────────────

def _col_exists(conn, table: str, column: str) -> bool:
    return any(
        r[1] == column
        for r in conn.execute(f"PRAGMA table_info({table})").fetchall()
    )


def add_columns(conn) -> None:
    print("\n── Step 2: add new columns to wa_verse_records ──")
    new_cols = [
        ("book_id",      "INTEGER REFERENCES books(id)"),
        ("chapter",      "INTEGER"),
        ("verse_num",    "INTEGER"),
        ("translation",  "TEXT NOT NULL DEFAULT 'ESV'"),
        ("note",         "TEXT"),
        ("claude_output","TEXT"),
        # SQLite ALTER TABLE does not allow function-based defaults;
        # these are added as plain TEXT and backfilled below.
        ("created_at",   "TEXT"),
        ("updated_at",   "TEXT"),
    ]
    for col, defn in new_cols:
        if _col_exists(conn, "wa_verse_records", col):
            print(f"  · {col}: already exists")
        else:
            conn.execute(f"ALTER TABLE wa_verse_records ADD COLUMN {col} {defn}")
            print(f"  + {col}: added")

    # Backfill timestamps for rows where they are still NULL
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    conn.execute(
        "UPDATE wa_verse_records SET created_at = ?, updated_at = ?"
        " WHERE created_at IS NULL OR updated_at IS NULL",
        (now, now),
    )
    conn.commit()


# ─────────────────────────────────────────────────────────────────────────────
# Step 3 – normalise book, reference, populate book_id / chapter / verse_num
# ─────────────────────────────────────────────────────────────────────────────

def normalise_references(conn) -> None:
    print("\n── Step 3: normalise book names and references ──")

    # Build name → (id, short_code) lookup from books table
    book_lookup: dict[str, tuple[int, str]] = {}
    for row in conn.execute("SELECT id, name, short_code FROM books").fetchall():
        book_lookup[row[1]] = (row[0], row[2])

    # Fetch all rows that still need normalisation (book_id IS NULL)
    rows = conn.execute(
        "SELECT id, book, reference FROM wa_verse_records WHERE book_id IS NULL"
    ).fetchall()

    print(f"  Rows to normalise: {len(rows)}")

    updated = 0
    skipped = 0
    unresolved: list[str] = []

    for row_id, raw_book, raw_ref in rows:
        # ── resolve canonical book name ───────────────────────────────────
        canonical_name = REF_ALIAS.get(raw_book)

        # If book column didn't resolve, try the reference prefix
        if canonical_name is None and raw_ref:
            prefix = raw_ref.split(" ")[0]
            canonical_name = REF_ALIAS.get(prefix)

        if canonical_name is None:
            unresolved.append(f"id={row_id} book={raw_book!r} ref={raw_ref!r}")
            skipped += 1
            continue

        book_info = book_lookup.get(canonical_name)
        if book_info is None:
            unresolved.append(f"id={row_id} canonical={canonical_name!r} not in books table")
            skipped += 1
            continue

        book_id, short_code = book_info

        # ── parse chapter / verse from reference ─────────────────────────
        chapter: int | None = None
        verse: int | None = None
        norm_ref: str | None = None

        if raw_ref:
            m = _REF_RE.match(raw_ref.strip())
            if m:
                chapter = int(m.group(2))
                verse   = int(m.group(3))
                norm_ref = f"{short_code} {chapter}:{verse}"

        conn.execute(
            """
            UPDATE wa_verse_records
            SET book_id     = ?,
                book        = ?,
                reference   = COALESCE(?, reference),
                chapter     = ?,
                verse_num   = ?
            WHERE id = ?
            """,
            (book_id, canonical_name, norm_ref, chapter, verse, row_id),
        )
        updated += 1

    conn.commit()
    print(f"  Normalised: {updated}  |  Skipped/unresolved: {skipped}")
    if unresolved:
        print("  Unresolved rows:")
        for u in unresolved[:20]:
            print(f"    {u}")
        if len(unresolved) > 20:
            print(f"    … and {len(unresolved) - 20} more")


# ─────────────────────────────────────────────────────────────────────────────
# Step 4 – populate translation from wa_file_index
# ─────────────────────────────────────────────────────────────────────────────

def populate_translation(conn) -> None:
    print("\n── Step 4: populate translation from wa_file_index ──")

    # Check if the column exists in wa_file_index
    if not _col_exists(conn, "wa_file_index", "translation_used"):
        print("  wa_file_index.translation_used column not found — skipping")
        return

    conn.execute("""
        UPDATE wa_verse_records
        SET translation = (
            SELECT COALESCE(fi.translation_used, 'ESV')
            FROM wa_file_index fi
            WHERE fi.id = wa_verse_records.file_id
        )
        WHERE file_id IS NOT NULL
    """)
    conn.commit()
    updated = conn.execute(
        "SELECT COUNT(*) FROM wa_verse_records WHERE translation != 'ESV'"
    ).fetchone()[0]
    total = conn.execute("SELECT COUNT(*) FROM wa_verse_records").fetchone()[0]
    print(f"  Translation populated for {total} rows ({updated} non-ESV)")


# ─────────────────────────────────────────────────────────────────────────────
# Step 5 – add updated_at trigger and search index
# ─────────────────────────────────────────────────────────────────────────────

def add_trigger_and_index(conn) -> None:
    print("\n── Step 5: add trigger and index ──")

    conn.executescript("""
        CREATE TRIGGER IF NOT EXISTS wa_verse_records_updated_at
        AFTER UPDATE ON wa_verse_records
        BEGIN
            UPDATE wa_verse_records
            SET updated_at = strftime('%Y-%m-%dT%H:%M:%S','now')
            WHERE id = NEW.id;
        END;

        CREATE INDEX IF NOT EXISTS idx_wavr_book_ch_v
            ON wa_verse_records (book_id, chapter, verse_num);

        CREATE INDEX IF NOT EXISTS idx_wavr_term_id
            ON wa_verse_records (term_id);

        CREATE INDEX IF NOT EXISTS idx_wavr_reference
            ON wa_verse_records (reference);
    """)
    conn.commit()
    print("  Trigger wa_verse_records_updated_at: created (or already existed)")
    print("  Indexes on (book_id,chapter,verse_num), term_id, reference: created")


# ─────────────────────────────────────────────────────────────────────────────
# Step 6 – drop redundant tables and old trigger
# ─────────────────────────────────────────────────────────────────────────────

def drop_redundant_tables(conn) -> None:
    print("\n── Step 6: drop verse_notes, verse_theme_map, verse_source_map ──")

    # Confirm all three are empty before dropping
    for tbl in ("verse_theme_map", "verse_source_map", "verse_notes"):
        exists = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tbl,)
        ).fetchone()
        if not exists:
            print(f"  · {tbl}: already absent")
            continue
        n = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
        if n > 0:
            print(f"  ⚠ {tbl} has {n} rows — skipping drop (manual review needed)")
            continue
        conn.execute(f"DROP TABLE {tbl}")
        print(f"  ✓ {tbl}: dropped")

    # Drop the stale verse_notes trigger if it still exists
    conn.execute("DROP TRIGGER IF EXISTS verse_notes_updated_at")
    print("  ✓ verse_notes_updated_at trigger: removed")

    conn.commit()


# ─────────────────────────────────────────────────────────────────────────────
# Step 7 – refresh books.verse_count using book_id (distinct verses per book)
# ─────────────────────────────────────────────────────────────────────────────

def refresh_verse_counts(conn) -> None:
    print("\n── Step 7: refresh books.verse_count (distinct verses per book) ──")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    # Count distinct (chapter, verse_num) per book_id — not raw rows, which
    # would overcount books appearing under multiple terms
    rows = conn.execute("""
        SELECT book_id, COUNT(DISTINCT chapter || ':' || verse_num) AS cnt
        FROM wa_verse_records
        WHERE book_id IS NOT NULL
        GROUP BY book_id
    """).fetchall()

    for book_id, cnt in rows:
        conn.execute(
            "UPDATE books SET verse_count = ?, last_updated = ? WHERE id = ?",
            (cnt, now, book_id),
        )

    conn.commit()
    print(f"  Updated verse_count for {len(rows)} books.")


# ─────────────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────────────

def print_summary(conn) -> None:
    print("\n── Summary ──")
    total = conn.execute("SELECT COUNT(*) FROM wa_verse_records").fetchone()[0]
    null_book = conn.execute(
        "SELECT COUNT(*) FROM wa_verse_records WHERE book_id IS NULL"
    ).fetchone()[0]
    null_ref = conn.execute(
        "SELECT COUNT(*) FROM wa_verse_records WHERE reference IS NULL"
    ).fetchone()[0]
    print(f"  wa_verse_records total rows  : {total:,}")
    print(f"  Rows with NULL book_id       : {null_book}")
    print(f"  Rows with NULL reference     : {null_ref}")

    print("\n  Reference sample (10 rows):")
    for r in conn.execute(
        "SELECT id, book, reference, chapter, verse_num, book_id FROM wa_verse_records"
        " WHERE book_id IS NOT NULL LIMIT 10"
    ).fetchall():
        print(f"    {dict(r)}")

    print()
    print(f"  {'#':>3}  {'Book':<22} {'Code':<6} {'Distinct Verses':>15}  {'Last Updated'}")
    print("  " + "-" * 65)
    for r in conn.execute(
        "SELECT b.book_order, b.name, b.short_code, b.verse_count, b.last_updated"
        " FROM books b ORDER BY b.book_order"
    ).fetchall():
        print(f"  {r[0]:>3}  {r[1]:<22} {(r[2] or ''):6} {r[3]:>15}  {r[4]}")

    total_v = conn.execute("SELECT SUM(verse_count) FROM books").fetchone()[0]
    print(f"\n  Total distinct verse-book pairs: {total_v:,}")


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    print("=== migrate_consolidate_verse_tables.py ===")
    conn = get_connection()
    try:
        fix_book_short_codes(conn)
        add_columns(conn)
        normalise_references(conn)
        populate_translation(conn)
        add_trigger_and_index(conn)
        drop_redundant_tables(conn)
        refresh_verse_counts(conn)
        print_summary(conn)
        print("\nDone.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
