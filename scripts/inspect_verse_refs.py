"""Extract book/reference fields from wa_verse_records for inspection."""
import sys, os, csv
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# Full distinct picture of how these fields relate to each other
rows = conn.execute("""
    SELECT
        id,
        file_id,
        term_id,
        reference,
        book_id,
        chapter,
        verse_num,
        testament
    FROM wa_verse_records
    ORDER BY file_id, term_id, book_id, chapter, verse_num
""").fetchall()

rows = [dict(r) for r in rows]
total = len(rows)

# Diagnostic counts
null_ref     = sum(1 for r in rows if r["reference"] is None)
null_bookid  = sum(1 for r in rows if r["book_id"]  is None)
null_chapter = sum(1 for r in rows if r["chapter"]  is None)
null_versenum= sum(1 for r in rows if r["verse_num"] is None)

print(f"Total rows : {total:,}")
print(f"NULL reference : {null_ref}")
print(f"NULL book_id   : {null_bookid}")
print(f"NULL chapter   : {null_chapter}")
print(f"NULL verse_num : {null_versenum}")

# Write CSV for inspection
out_path = os.path.join(os.path.dirname(__file__), "..", "outputs",
                        "wa_verse_records_refs_inspect.csv")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "id","file_id","term_id","reference",
        "book_id","chapter","verse_num","testament"])
    writer.writeheader()
    writer.writerows(rows)
print(f"\nFull CSV: {os.path.abspath(out_path)}")

# Print first 60 rows as quick console scan
print(f"\n{'id':>6}  {'fid':>4}  {'term':12}  {'reference':20}  "
      f"{'bk_id':>6}  {'ch':>4}  {'vs':>4}  {'tst':4}")
print("-" * 90)
for r in rows[:60]:
    print(f"{r['id']:>6}  {r['file_id']:>4}  {str(r['term_id'] or ''):12}  "
          f"{str(r['reference'] or ''):20}  "
          f"{str(r['book_id'] or ''):>6}  {str(r['chapter'] or ''):>4}  "
          f"{str(r['verse_num'] or ''):>4}  {str(r['testament'] or ''):4}")

if len(rows) > 60:
    print(f"  ... ({len(rows)-60} more rows in CSV)")

# Also show NULL/problem rows specifically
problems = [r for r in rows if r["book_id"] is None
            or r["reference"] is None or r["chapter"] is None]
if problems:
    print(f"\n=== ROWS WITH ANY NULL in reference/book_id/chapter ({len(problems)}) ===")
    for r in problems:
        print(f"  id={r['id']} file_id={r['file_id']} term={r['term_id']} "
              f"ref={r['reference']!r} "
              f"book_id={r['book_id']} ch={r['chapter']} vs={r['verse_num']}")

conn.close()
