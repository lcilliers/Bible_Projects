"""
Migration: book_code_variants table + drop book column from wa_verse_records.

Run once:
    python scripts/migrate_verse_refs.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# ── 1. Create book_code_variants ─────────────────────────────────────────────
conn.execute("""
    CREATE TABLE IF NOT EXISTS book_code_variants (
        code    TEXT    PRIMARY KEY,
        book_id INTEGER NOT NULL REFERENCES books(id)
    )
""")
print("Created book_code_variants.")

# ── 2. Populate from books.short_code (all 66) ───────────────────────────────
books = conn.execute("SELECT id, short_code FROM books").fetchall()
conn.executemany(
    "INSERT OR IGNORE INTO book_code_variants (code, book_id) VALUES (?, ?)",
    [(b["short_code"], b["id"]) for b in books]
)
print(f"Inserted {len(books)} canonical short_code entries.")

# ── 3. Add the 4 known STEP alias variants ───────────────────────────────────
#   STEP sends these codes but books.short_code differs:
#     Jude  -> book_id=65 (Jude,     short_code=Jud)
#     2Jo   -> book_id=63 (2 John,   short_code=2Jn)
#     3Jo   -> book_id=64 (3 John,   short_code=3Jn)
#     Phile -> book_id=57 (Philemon, short_code=Phm)
step_aliases = [
    ("Jude",  65),
    ("2Jo",   63),
    ("3Jo",   64),
    ("Phile", 57),
]
conn.executemany(
    "INSERT OR IGNORE INTO book_code_variants (code, book_id) VALUES (?, ?)",
    step_aliases
)
print(f"Inserted {len(step_aliases)} STEP alias variants.")

total = conn.execute("SELECT COUNT(*) FROM book_code_variants").fetchone()[0]
print(f"Total entries in book_code_variants: {total}")

# ── 4. Drop stale indexes that reference book, or are superseded ─────────────
#   idx_wa_vr_book    : indexed the book (text name) column — dropping with column
#   idx_wa_vr_ref     : duplicate of idx_wavr_reference (added in schema v2)
#   idx_wa_vr_file    : superseded by idx_wavr_file_term_pos (composite, same leading col)
for idx in ("idx_wa_vr_book", "idx_wa_vr_ref", "idx_wa_vr_file"):
    conn.execute(f"DROP INDEX IF EXISTS {idx}")
    print(f"Dropped index {idx}.")

# ── 5. Drop the book column from wa_verse_records ────────────────────────────
conn.execute("ALTER TABLE wa_verse_records DROP COLUMN book")
conn.commit()
print("Dropped 'book' column from wa_verse_records.")

# ── 6. Verify ─────────────────────────────────────────────────────────────────
cols = [r[1] for r in conn.execute("PRAGMA table_info(wa_verse_records)").fetchall()]
print(f"\nwa_verse_records columns ({len(cols)}):")
for c in cols:
    print(f"  {c}")

# Spot-check variant lookup
print("\nVariant lookup spot-check:")
for code in ["Gen", "Jude", "2Jo", "3Jo", "Phile", "Phm", "Jud", "2Jn", "3Jn"]:
    row = conn.execute(
        "SELECT bcv.code, b.name FROM book_code_variants bcv JOIN books b ON b.id=bcv.book_id WHERE bcv.code=?",
        (code,)
    ).fetchone()
    if row:
        print(f"  {code:8s} -> {row[1]}")
    else:
        print(f"  {code:8s} -> NOT FOUND")

conn.close()
print("\nDone.")
