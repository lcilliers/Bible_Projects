import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
import json

conn = get_connection()

# word_registry entry
wr = conn.execute("SELECT * FROM word_registry WHERE id=151").fetchone()
print("word_registry id=151:")
for k in wr.keys():
    print("  %-35s %s" % (k, wr[k]))
print()

# wa_file_index rows for sorrow
fi = conn.execute(
    "SELECT * FROM wa_file_index WHERE word_registry_fk=151 OR word='sorrow' ORDER BY id"
).fetchall()
print("wa_file_index rows for sorrow:", len(fi))
for r in fi:
    print("  id=%s  registry_id=%s  word_registry_fk=%s  word=%s  file=%s" % (
        r["id"], r["registry_id"], r["word_registry_fk"], r["word"], r["filename"]))
print()

# mti_terms for sorrow (owning_registry=151)
mti = conn.execute(
    "SELECT id, term_id, transliteration, language, owning_registry FROM mti_terms WHERE owning_registry='151' ORDER BY id"
).fetchall()
print("mti_terms for owning_registry='151':", len(mti))
for r in mti:
    print("  id=%s  term_id=%-10s  translit=%-15s  lang=%s" % (r[0], r[1], r[2], r[3]))
print()

# Also check word_registry id=154
wr2 = conn.execute("SELECT id, no, word, phase1_status, phase1_output_file FROM word_registry WHERE id=154").fetchone()
print("word_registry id=154:", dict(wr2) if wr2 else "NOT FOUND")
print()

# mti_terms columns
mti_cols = [r[1] for r in conn.execute("PRAGMA table_info(mti_terms)").fetchall()]
print("mti_terms columns:", mti_cols)

# mti_terms for sorrow (owning_registry 151 and 154)


# Summarise import files
for fname in [
    r"G:\My Drive\Bible_study_projects\data\imports\WA\Session_A_Data\WA-154-sorrow-data-part1-2026-03-10.json",
    r"G:\My Drive\Bible_study_projects\data\imports\WA\Session_A_Data\WA-154-sorrow-data-part2-2026-03-10.json",
]:
    print("=== %s ===" % os.path.basename(fname))
    with open(fname, encoding="utf-8") as f:
        data = json.load(f)
    # Print top-level keys and basic counts
    for k, v in data.items():
        if isinstance(v, list):
            print("  %-30s list[%d]" % (k, len(v)))
        elif isinstance(v, dict):
            print("  %-30s dict(%d keys)" % (k, len(v)))
        else:
            print("  %-30s %s" % (k, v))
    print()
