import sqlite3
import warnings
import sys
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.db_client import resolve_verse_refs

DB = r"G:\My Drive\Bible_study_projects\data\bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

# Step 1: Find Philippians books.id
php = conn.execute("SELECT id, name, short_code FROM books WHERE name LIKE '%Philip%'").fetchone()
print("Philippians row:", dict(php))

# Check existing Phil* variants
existing = conn.execute("SELECT code, book_id FROM book_code_variants WHERE code LIKE 'Phil%'").fetchall()
print("Existing Phil* variants:", [dict(r) for r in existing])

# Step 2: Insert Phili alias if not already present
phili_exists = conn.execute("SELECT COUNT(*) FROM book_code_variants WHERE code = 'Phili'").fetchone()[0]
if phili_exists:
    print("Phili alias already exists — skipping insert.")
else:
    conn.execute("INSERT INTO book_code_variants (code, book_id) VALUES ('Phili', ?)", (php["id"],))
    conn.commit()
    print(f"Inserted: Phili -> books.id={php['id']} ({php['name']})")

# Step 3: Run resolve_verse_refs for all NULL rows
print("\nRunning resolve_verse_refs(only_missing=True)...")
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    updated = resolve_verse_refs(conn, only_missing=True)
    for w in caught:
        print("WARNING:", w.message)

print(f"Rows updated: {updated}")

# Step 4: Verify
null_after = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE book_id IS NULL").fetchone()[0]
null_fi51  = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE file_id = 51 AND book_id IS NULL").fetchone()[0]
resolved_fi51 = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE file_id = 51 AND book_id IS NOT NULL").fetchone()[0]
print(f"\nPost-fix:")
print(f"  Total NULL book_id across all rows:   {null_after}")
print(f"  gladness (file_id=51) NULL book_id:   {null_fi51}")
print(f"  gladness (file_id=51) resolved:       {resolved_fi51}")

conn.close()
