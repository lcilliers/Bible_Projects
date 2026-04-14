import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

print("=== Before ===")
for r in conn.execute("SELECT id, word, phase1_status, phase1_output_file, notes FROM word_registry WHERE id IN (151,154)").fetchall():
    print("  word_registry id=%-4s  word=%-10s  status=%s" % (r[0], r[1], r[2]))
fi = conn.execute("SELECT id, registry_id, word_registry_fk, word, filename FROM wa_file_index WHERE word='sorrow' ORDER BY id").fetchall()
for r in fi:
    print("  wa_file_index id=%-4s  registry_id=%-4s  word_registry_fk=%-4s  file=%s" % (r[0], r[1], r[2], r[4]))
print()

# 1. wa_file_index: re-link fi.id=31 and fi.id=32 from word_registry_fk=154 to 151
conn.execute("UPDATE wa_file_index SET word_registry_fk=151, registry_id='151' WHERE id IN (31,32)")
print("wa_file_index rows 31,32: word_registry_fk 154 -> 151")

# 2. word_registry id=151: set correct output files and notes
conn.execute("""
    UPDATE word_registry
    SET phase1_output_file = 'WA-154-sorrow-data-part1-2026-03-10.json, WA-154-sorrow-data-part2-2026-03-10.json',
        notes              = '24 terms. 2 parts. Spec v5. MTI: extracted. Data imported under registry 154 (filename mismatch); re-linked to correct registry 151 on 2026-03-19.'
    WHERE id = 151
""")
print("word_registry id=151: phase1_output_file and notes updated")

# 3. word_registry id=154: mark redundant, clear output file
conn.execute("""
    UPDATE word_registry
    SET phase1_status      = 'Redundant',
        phase1_output_file = NULL,
        notes              = 'Originally mislabelled as stupor. Data files were sorrow (WA-154-sorrow-data-part1/2-2026-03-10.json). All data re-linked to word_registry.id=151 (sorrow) on 2026-03-19. This row is a data entry error and is now redundant.'
    WHERE id = 154
""")
print("word_registry id=154: status=Redundant, phase1_output_file cleared, notes updated")

conn.commit()
print()

print("=== After ===")
for r in conn.execute("SELECT id, word, phase1_status, phase1_output_file, notes FROM word_registry WHERE id IN (151,154)").fetchall():
    print("  word_registry id=%-4s  word=%-10s  status=%-12s  output=%s" % (r[0], r[1], r[2], r[3]))
    print("    notes:", r[4])
fi2 = conn.execute("SELECT id, registry_id, word_registry_fk, word, filename FROM wa_file_index WHERE word='sorrow' ORDER BY id").fetchall()
for r in fi2:
    print("  wa_file_index id=%-4s  registry_id=%-4s  word_registry_fk=%-4s  file=%s" % (r[0], r[1], r[2], r[4]))

conn.close()
print()
print("Done.")
