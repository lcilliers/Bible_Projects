"""Fix NULL chapter/verse_num for single-chapter book rows in wa_verse_records."""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# Preview what will be updated
to_fix = conn.execute("""
    SELECT id, reference, book, book_id, chapter, verse_num
    FROM wa_verse_records
    WHERE chapter IS NULL AND reference IS NOT NULL AND book_id IS NOT NULL
""").fetchall()
print(f"Rows to fix: {len(to_fix)}")
for r in to_fix:
    m = re.search(r'\s(\d+)$', r[1])
    vs = int(m.group(1)) if m else '?'
    print(f"  id={r[0]:6d}  ref={r[1]:15s}  -> chapter=1  verse_num={vs}")

# Apply fix
conn.execute("""
    UPDATE wa_verse_records
    SET chapter = 1,
        verse_num = CAST(TRIM(SUBSTR(reference, INSTR(reference, ' ') + 1)) AS INTEGER)
    WHERE chapter IS NULL
      AND reference IS NOT NULL
      AND book_id IS NOT NULL
""")
conn.commit()

# Verify none remaining
remaining = conn.execute(
    "SELECT COUNT(*) FROM wa_verse_records WHERE chapter IS NULL AND reference IS NOT NULL"
).fetchone()[0]
print(f"\nNULL chapter rows with reference remaining: {remaining}")

# Spot-check
print("\nSpot-check fixed rows:")
for r in conn.execute("""
    SELECT id, reference, book, chapter, verse_num
    FROM wa_verse_records WHERE id IN (1421, 1621, 3726, 3730, 3731, 6653)
""").fetchall():
    print(f"  id={r[0]}  ref={r[1]:15s}  book={r[2]:15s}  ch={r[3]}  vs={r[4]}")

conn.close()
print("\nDone.")
