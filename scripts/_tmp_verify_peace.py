import sys
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.db_client import get_connection

conn = get_connection()
c = conn.cursor()

c.execute("SELECT id, part_number, filename FROM wa_file_index WHERE registry_id='117'")
for r in c.fetchall():
    print(f"  file_index id={r[0]} part={r[1]} {r[2]}")

c.execute("SELECT MIN(id), MAX(id), COUNT(*) FROM wa_term_inventory WHERE file_id IN (48,49,50)")
r = c.fetchone()
print(f"wa_term_inventory: count={r[2]}, ids {r[0]}..{r[1]}")

c.execute("SELECT COUNT(*) FROM mti_terms WHERE owning_registry='117' AND word_data_reference IS NOT NULL")
print(f"mti_terms word_data_reference set: {c.fetchone()[0]}/34")

c.execute("SELECT phase1_output_file FROM word_registry WHERE id=117")
print(f"word_registry id=117 phase1_output_file: {c.fetchone()[0]}")

c.execute("SELECT MAX(id) FROM wa_file_index")
print(f"Global MAX wa_file_index.id = {c.fetchone()[0]}")
c.execute("SELECT MAX(id) FROM wa_term_inventory")
print(f"Global MAX wa_term_inventory.id = {c.fetchone()[0]}")

conn.close()
