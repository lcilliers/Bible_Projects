import sys, os, glob
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# All registry rows mentioning stupor
rows = conn.execute(
    "SELECT id, no, word, phase1_status, source_list, notes FROM word_registry WHERE word LIKE '%stupor%' ORDER BY id"
).fetchall()
print("word_registry rows for 'stupor':", len(rows))
for r in rows:
    print("  id=%-4s  no=%-4s  word=%-20s  status=%-12s  source=%s" % (r[0], r[1], r[2], r[3], r[4]))
    print("  notes:", r[5])
print()

# wa_file_index rows for stupor
fi = conn.execute(
    "SELECT id, registry_id, word_registry_fk, word, filename FROM wa_file_index WHERE word LIKE '%stupor%' ORDER BY id"
).fetchall()
print("wa_file_index rows for 'stupor':", len(fi))
for r in fi:
    print("  fi.id=%-4s  registry_id=%-4s  word_registry_fk=%-4s  word=%-15s  file=%s" % (r[0], r[1], r[2], r[3], r[4]))
print()

conn.close()

# Import files on disk
base = r"G:\My Drive\Bible_study_projects\data\imports"
matches = glob.glob(os.path.join(base, "**", "*stupor*"), recursive=True)
print("Import files on disk matching 'stupor':", len(matches))
for m in matches:
    print(" ", m)
