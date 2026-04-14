import sqlite3, json

DB = r"G:\My Drive\Bible_study_projects\data\bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Full breakdown of all unresolved book prefixes (null book_id)
cur.execute("""
    SELECT SUBSTR(reference, 1, INSTR(reference||' ', ' ')-1) as book_prefix, COUNT(*) as cnt
    FROM wa_verse_records WHERE book_id IS NULL
    GROUP BY book_prefix ORDER BY cnt DESC
""")
print("=== NULL book_id — all prefixes ===")
for r in cur.fetchall():
    print(f"  {r['book_prefix']:15s} {r['cnt']}")

# Check which of those prefixes are missing from book_code_variants
cur.execute("""
    SELECT DISTINCT SUBSTR(reference, 1, INSTR(reference||' ', ' ')-1) as book_prefix
    FROM wa_verse_records WHERE book_id IS NULL
""")
prefixes = [r['book_prefix'] for r in cur.fetchall()]
print("\n=== Missing from book_code_variants ===")
for p in prefixes:
    cur.execute("SELECT COUNT(*) FROM book_code_variants WHERE code = ?", (p,))
    count = cur.fetchone()[0]
    if count == 0:
        print(f"  MISSING: '{p}'")

# The 1 null term_inv_id row
cur.execute("""
    SELECT id, file_id, term_id, reference, transliteration
    FROM wa_verse_records WHERE term_inv_id IS NULL
""")
print("\n=== NULL term_inv_id rows ===")
for r in cur.fetchall():
    print(dict(r))

# Check what file_id=51 is
cur.execute("SELECT id, filename, word, registry_id FROM wa_file_index WHERE id=51")
r = cur.fetchone()
print(f"\n=== wa_file_index id=51 ===")
print(dict(r) if r else "NOT FOUND")

conn.close()
