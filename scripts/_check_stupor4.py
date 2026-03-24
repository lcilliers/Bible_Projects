import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# Broad search: word_registry notes/word for stupor
print("=== word_registry — stupor / katanuxis in any text field ===")
rows = conn.execute(
    "SELECT id, no, word, phase1_status, notes FROM word_registry "
    "WHERE word LIKE '%stupor%' OR notes LIKE '%stupor%' OR notes LIKE '%katanux%' OR notes LIKE '%G2659%'"
).fetchall()
print("Rows:", len(rows))
for r in rows:
    print("  id=%-4s  no=%-4s  word=%-20s  status=%s  notes=%s" % (r[0], r[1], r[2], r[3], r[4]))
print()

# mti_terms gloss / owning_word for stupor
print("=== mti_terms — gloss or owning_word containing stupor ===")
mti = conn.execute(
    "SELECT id, strongs_number, transliteration, gloss, owning_registry, owning_word "
    "FROM mti_terms WHERE gloss LIKE '%stupor%' OR owning_word LIKE '%stupor%'"
).fetchall()
print("Rows:", len(mti))
for r in mti:
    print("  id=%-4s  strongs=%-10s  translit=%-20s  gloss=%-30s  owner=%s / %s" % (
        r[0], r[1], r[2], r[3], r[4], r[5]))
print()

# wa_cross_registry_links notes/connection_type
print("=== wa_cross_registry_links — stupor ===")
cr = conn.execute(
    "SELECT * FROM wa_cross_registry_links WHERE note LIKE '%stupor%' OR note LIKE '%katanux%'"
).fetchall()
print("Rows:", len(cr))

conn.close()
