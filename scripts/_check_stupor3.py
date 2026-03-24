import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# Search by Strong's G2659 in wa_term_inventory
print("=== wa_term_inventory — G2659 ===")
rows = conn.execute(
    "SELECT id, file_id, term_id, strongs_number, transliteration, step_search_gloss, word_analysis_gloss "
    "FROM wa_term_inventory WHERE strongs_number='G2659' OR term_id='G2659'"
).fetchall()
print("Rows:", len(rows))
for r in rows:
    print("  id=%-4s  file_id=%-4s  strongs=%-10s  translit=%-20s  gloss=%s / %s" % (r[0], r[1], r[3], r[4], r[5], r[6]))
print()

# mti_terms by strongs_number
print("=== mti_terms — G2659 ===")
mti = conn.execute(
    "SELECT * FROM mti_terms WHERE strongs_number='G2659'"
).fetchall()
print("Rows:", len(mti))
for r in mti:
    print("  id=%-4s  strongs=%-10s  translit=%-20s  gloss=%-25s  owning_registry=%s  owning_word=%s" % (
        r["id"], r["strongs_number"], r["transliteration"], r["gloss"], r["owning_registry"], r["owning_word"]))
print()

# verse records for G2659
print("=== wa_verse_records — term_id=G2659 ===")
vr = conn.execute(
    "SELECT id, file_id, term_id, reference, verse_text FROM wa_verse_records WHERE term_id='G2659'"
).fetchall()
print("Rows:", len(vr))
for r in vr:
    print("  vr.id=%-5s  ref=%-15s  text=%s" % (r[0], r[3], (r[4] or "")[:100]))

conn.close()
