"""Historical diagnostic: book/reference/book_id discrepancy analysis (book column now removed)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

rows = [dict(r) for r in conn.execute("""
    SELECT id, file_id, term_id, reference, book_id, chapter, verse_num, testament
    FROM wa_verse_records
    ORDER BY id
""").fetchall()]

# --- 1. What does the books table look like? ---
books_rows = conn.execute("SELECT id, name, short_code, abbreviation, book_order FROM books ORDER BY book_order").fetchall()
books_by_id = {r["id"]: dict(r) for r in books_rows}

print("=== BOOKS TABLE (id, name, short_code, abbreviation) ===")
for b in books_rows:
    print(f"  {b['id']:3d}  {b['name']:30s}  {b['short_code']:8s}  {b['abbreviation']}")

print()

# --- 2. reference vs books table lookup ---
print("=== REFERENCE vs BOOKS TABLE (sample) ===")
# Sample first 20 rows where reference present
sample = [r for r in rows if r["reference"]][:20]
for r in sample:
    bk_id = r["book_id"]
    books_entry = books_by_id.get(bk_id, {})
    print(f"  id={r['id']:6d}  reference={r['reference']:20s}  "
          f"books.short_code={books_entry.get('short_code','?'):8s}  "
          f"books.name={books_entry.get('name','?')}")

print()

# --- 3. Single-chapter books: NULL chapter/verse_num ---
print("=== NULL chapter/verse_num rows (12 single-chapter books + 1 NULL) ===")
null_ch = [r for r in rows if r["chapter"] is None]
for r in null_ch:
    bk_entry = books_by_id.get(r["book_id"], {})
    print(f"  id={r['id']:6d}  ref={str(r['reference']):15s}  "
          f"book_id={r['book_id']}  ch={r['chapter']}  vs={r['verse_num']}"
          f"  [short_code={bk_entry.get('short_code','?')}]")

print()

# --- 4. Parse test: can we extract chapter/verse from these references? ---
import re

def parse_ref(ref):
    """Try to parse chapter:verse or single-chapter-book verse from a reference string."""
    if not ref:
        return None, None
    # Standard: "Gen 3:16" or "Act 10:28"
    m = re.search(r'(\d+):(\d+)', ref)
    if m:
        return int(m.group(1)), int(m.group(2))
    # Single-chapter books: "Obd 17", "Jude 16", "Phile 22", "2Jo 5", "3Jo 14"
    m2 = re.search(r'\s(\d+)$', ref)
    if m2:
        return 1, int(m2.group(1))   # chapter = 1, verse = the number
    return None, None

print("=== PARSE TEST for single-chapter references ===")
for r in null_ch:
    if r["reference"]:
        ch, vs = parse_ref(r["reference"])
        print(f"  ref={r['reference']:15s}  parsed ch={ch}  vs={vs}")

conn.close()
