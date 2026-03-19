"""Investigate wa_verse_records id=211."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

row = dict(conn.execute("SELECT * FROM wa_verse_records WHERE id=211").fetchone())
print("=== wa_verse_records id=211 ===")
for k, v in row.items():
    print(f"  {k:<20} = {repr(v)}")

fid = row["file_id"]
print()
print(f"=== wa_file_index id={fid} ===")
f = conn.execute("SELECT * FROM wa_file_index WHERE id=?", (fid,)).fetchone()
if f:
    for k in f.keys():
        print(f"  {k:<25} = {repr(f[k])}")
else:
    print(f"  No wa_file_index row for file_id={fid}")

print()
total_in_file = conn.execute(
    "SELECT COUNT(*) FROM wa_verse_records WHERE file_id=?", (fid,)
).fetchone()[0]
print(f"Total verse rows with file_id={fid}: {total_in_file}")

null_rows = conn.execute("""
    SELECT id, term_id_ref, reference, book_id, chapter, verse_num
    FROM wa_verse_records
    WHERE file_id=? AND (reference IS NULL OR book_id IS NULL)
""", (fid,)).fetchall()
print(f"Rows in file_id={fid} with NULL reference or book_id: {len(null_rows)}")
for r in null_rows:
    print(f"  id={r[0]}  term={r[1]}  ref={r[2]}  book_id={r[3]}  ch={r[4]}  vs={r[5]}")

conn.close()
