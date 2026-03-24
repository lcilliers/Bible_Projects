import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# Search wa_term_inventory for katanuxis / stupor
print("=== wa_term_inventory — katanuxis / stupor ===")
rows = conn.execute(
    "SELECT id, file_id, term_id, strongs_number, transliteration, step_search_gloss, word_analysis_gloss "
    "FROM wa_term_inventory "
    "WHERE transliteration LIKE '%katanux%' OR step_search_gloss LIKE '%stupor%' OR word_analysis_gloss LIKE '%stupor%' "
    "ORDER BY id"
).fetchall()
print("Rows found:", len(rows))
for r in rows:
    print("  id=%-4s  file_id=%-4s  term_id=%-10s  strongs=%-10s  translit=%-20s  gloss=%s / %s" % (
        r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
print()

# Search mti_terms columns
mti_cols = [c[1] for c in conn.execute("PRAGMA table_info(mti_terms)").fetchall()]
print("mti_terms columns:", mti_cols)
mti = conn.execute(
    "SELECT * FROM mti_terms WHERE transliteration LIKE '%katanux%' ORDER BY id"
).fetchall()
print("mti_terms katanuxis rows:", len(mti))
for r in mti:
    print("  id=%-4s  owning_registry=%-6s  transliteration=%s" % (r["id"], r["owning_registry"], r["transliteration"]))
print()

# Also check verse records for those term_inv_ids
if rows:
    ti_ids = [r[0] for r in rows]
    ph = ",".join("?" * len(ti_ids))
    vr = conn.execute(
        "SELECT id, file_id, term_id, reference, verse_text FROM wa_verse_records WHERE term_inv_id IN (%s)" % ph,
        ti_ids
    ).fetchall()
    print("wa_verse_records for katanuxis term_inv_ids:", len(vr))
    for r in vr:
        print("  vr.id=%-5s  term_id=%-10s  ref=%-15s  text=%s" % (r[0], r[2], r[3], r[4][:80] if r[4] else None))

conn.close()
