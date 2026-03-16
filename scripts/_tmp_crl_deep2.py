import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
conn = get_connection()

wr_ids   = {r[0] for r in conn.execute("SELECT id FROM word_registry").fetchall()}
wr_words = {r[0]: r[1] for r in conn.execute("SELECT id, word FROM word_registry").fetchall()}
rows = [dict(r) for r in conn.execute("SELECT * FROM wa_cross_registry_links ORDER BY id").fetchall()]

# 1. All distinct linked_registry_id values
print("=== distinct linked_registry_id values ===")
for r in conn.execute("""
    SELECT linked_registry_id, COUNT(*) cnt
    FROM wa_cross_registry_links
    GROUP BY linked_registry_id ORDER BY cnt DESC
""").fetchall():
    val = r[0]
    try:
        in_wr = int(val) in wr_ids if val is not None else False
        word  = wr_words.get(int(val), "?") if val and val != "unknown" else "n/a"
    except (ValueError, TypeError):
        in_wr = False
        word  = "n/a"
    print(f"  {str(val):8s}  cnt={r[1]:3d}  in_word_registry={in_wr}  word={word}")

# 2. Does linked_word match word_registry.word?
print()
print("=== linked_word vs word_registry.word (sample 20) ===")
for r in conn.execute("""
    SELECT crl.id, crl.linked_word, crl.linked_registry_id,
           wr.word AS wr_word
    FROM wa_cross_registry_links crl
    LEFT JOIN word_registry wr ON CAST(crl.linked_registry_id AS INTEGER) = wr.id
    WHERE crl.linked_registry_id != 'unknown'
    LIMIT 20
""").fetchall():
    match = "ok" if r[1] and r[3] and r[1].lower() == r[3].lower() else "MISMATCH"
    print(f"  id={r[0]:4d}  linked_word={str(r[1]):18s}  reg_id={str(r[2]):5s}  "
          f"wr.word={str(r[3]):18s}  {match}")

# 3. Show 'unknown' rows
print()
print("=== linked_registry_id = 'unknown' rows ===")
for r in conn.execute("""
    SELECT id, file_id, linked_word, linked_registry_id, connection_type, connecting_term, note
    FROM wa_cross_registry_links WHERE linked_registry_id = 'unknown'
""").fetchall():
    print(f"  id={r[0]}  file={r[1]}  linked_word={r[2]!r}  type={r[4]!r}  term={r[5]!r}")

# 4. Does connecting_term correlate to wa_term_inventory?
print()
print("=== Does connecting_term match any wa_term_inventory.transliteration? ===")
translit = {r[0].lower() for r in conn.execute(
    "SELECT transliteration FROM wa_term_inventory WHERE transliteration IS NOT NULL").fetchall()}
ct_vals = [r[0] for r in conn.execute(
    "SELECT DISTINCT connecting_term FROM wa_cross_registry_links WHERE connecting_term IS NOT NULL").fetchall()]
ct_match   = [v for v in ct_vals if v.lower() in translit]
ct_nomatch = [v for v in ct_vals if v.lower() not in translit]
print(f"  Distinct connecting_term values: {len(ct_vals)}")
print(f"  Match wa_term_inventory.transliteration: {len(ct_match)}")
print(f"  No match (sample 10): {ct_nomatch[:10]}")

# 5. Links per file
print()
print("=== links per file (top 15) ===")
for r in conn.execute("""
    SELECT crl.file_id, fi.word, COUNT(*) cnt
    FROM wa_cross_registry_links crl
    JOIN wa_file_index fi ON fi.id = crl.file_id
    GROUP BY crl.file_id ORDER BY cnt DESC LIMIT 15
""").fetchall():
    print(f"  file={r[0]:3d}  word={str(r[1]):20s}  links={r[2]}")

conn.close()
