"""Look up H8262_taav_loathe across all related tables."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# --- wa_term_inventory (id=10 from the verse record) and by term_id match ---
print("=== wa_term_inventory ===")
rows = conn.execute(
    "SELECT * FROM wa_term_inventory WHERE id=10 OR term_id LIKE '%8262%' OR transliteration LIKE '%taav%'"
).fetchall()
for row in rows:
    for k in row.keys():
        print(f"  {k:<30} = {repr(row[k])}")
    print()

if not rows:
    print("  No match found.")

# --- wa_term_related_words for file_id=1 (abomination file) ---
# wa_term_related_words uses term_id; show all from file perspective via wa_term_inventory ids
inv_ids = [r["id"] for r in rows]
print("=== wa_term_related_words (for matched term ids) ===")
for inv_id in inv_ids:
    rels = conn.execute(
        "SELECT * FROM wa_term_related_words WHERE id=?", (inv_id,)
    ).fetchall()
    for r in rels:
        for k in r.keys():
            print(f"  {k:<30} = {repr(r[k])}")
        print()

# Also check by term_id value
print("=== wa_term_related_words (by term_id value) ===")
for row in rows:
    tid = row["term_id"]
    rels = conn.execute(
        "SELECT * FROM wa_term_related_words WHERE term_id=?", (tid,)
    ).fetchall()
    print(f"  term_id={tid!r}: {len(rels)} entries")
    for r in rels:
        for k in r.keys():
            print(f"    {k:<30} = {repr(r[k])}")
        print()

# --- wa_term_root_family ---
print("=== wa_term_root_family ===")
for row in rows:
    tid = row["term_id"]
    roots = conn.execute(
        "SELECT * FROM wa_term_root_family WHERE term_id=?", (tid,)
    ).fetchall()
    print(f"  term_id={tid!r}: {len(roots)} root family entries")
    for r in roots:
        for k in r.keys():
            print(f"    {k:<30} = {repr(r[k])}")
        print()

# --- verse records ---
print("=== wa_verse_records ===")
vrows = conn.execute(
    "SELECT id, file_id, term_id_ref, transliteration, reference, book_id, chapter, verse_num, verse_text "
    "FROM wa_verse_records WHERE term_id_ref LIKE '%8262%' OR term_id_ref LIKE '%taav%'"
).fetchall()
print(f"  {len(vrows)} verse record(s) matching H8262/taav")
for r in vrows:
    print(f"  id={r[0]}  file_id={r[1]}  term={r[2]}  ref={r[4]}  ch={r[6]}  vs={r[7]}")
    if r[8]:
        print(f"    verse_text: {r[8][:100]}")

conn.close()
