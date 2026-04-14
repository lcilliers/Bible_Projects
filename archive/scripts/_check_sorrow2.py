import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
import json

conn = get_connection()

# All word_registry rows where word='sorrow'
print("=== word_registry rows where word='sorrow' ===")
rows = conn.execute(
    "SELECT id, no, word, phase1_status, phase1_output_file FROM word_registry WHERE word='sorrow' ORDER BY id"
).fetchall()
for r in rows:
    print("  id=%-4s  no=%-4s  status=%-12s  output_file=%s" % (r[0], r[1], r[3], r[4]))
print()

# wa_file_index rows for word='sorrow'
print("=== wa_file_index rows where word='sorrow' ===")
fi = conn.execute(
    "SELECT id, registry_id, word_registry_fk, word, filename FROM wa_file_index WHERE word='sorrow' ORDER BY id"
).fetchall()
for r in fi:
    print("  fi.id=%-4s  registry_id=%-4s  word_registry_fk=%-4s  file=%s" % (r[0], r[1], r[2], r[4]))
print()

# wa_term_inventory rows for these file_ids
fids = [r[0] for r in fi]
if fids:
    ph = ",".join("?" * len(fids))
    ti = conn.execute(
        "SELECT id, file_id, term_id, strongs_number, transliteration FROM wa_term_inventory WHERE file_id IN (%s) ORDER BY id" % ph,
        fids
    ).fetchall()
    print("wa_term_inventory rows (file_ids %s): %d" % (fids, len(ti)))
    for r in ti:
        print("  id=%-4s  file_id=%-4s  term_id=%-10s  strongs=%-10s  translit=%s" % (r[0], r[1], r[2], r[3], r[4]))
    print()

    vr_count = conn.execute(
        "SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN (%s)" % ph, fids
    ).fetchone()[0]
    print("wa_verse_records rows for sorrow file_ids: %d" % vr_count)
    print()

conn.close()

# JSON file top-level summary
for fname in [
    r"G:\My Drive\Bible_study_projects\data\imports\WA\Session_A_Data\WA-154-sorrow-data-part1-2026-03-10.json",
    r"G:\My Drive\Bible_study_projects\data\imports\WA\Session_A_Data\WA-154-sorrow-data-part2-2026-03-10.json",
]:
    print("=== %s ===" % os.path.basename(fname))
    with open(fname, encoding="utf-8") as f:
        data = json.load(f)
    for k, v in data.items():
        if isinstance(v, list):
            print("  %-30s list[%d]" % (k, len(v)))
        elif isinstance(v, dict):
            print("  %-30s dict(%d keys)" % (k, len(v)))
        else:
            print("  %-30s %s" % (k, v))
    print()
