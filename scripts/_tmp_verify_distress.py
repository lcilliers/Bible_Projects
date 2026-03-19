import sys
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.db_client import get_connection

conn = get_connection()
c = conn.cursor()

print("=== Distress (051) Post-Apply Verification ===")

# File index
c.execute("SELECT id, filename, part_number FROM wa_file_index WHERE registry_id='051' ORDER BY id")
rows = c.fetchall()
print(f"\nwa_file_index (registry 051): {len(rows)} rows")
for r in rows:
    print(f"  id={r[0]}  part={r[2]}  {r[1]}")

# Term inventory
c.execute("SELECT MIN(id), MAX(id), COUNT(*) FROM wa_term_inventory WHERE file_id IN (45,46,47)")
r = c.fetchone()
print(f"\nwa_term_inventory (file_ids 45-47): count={r[2]}, ids {r[0]}..{r[1]}")

# Verse records
c.execute("SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN (45,46,47)")
print(f"wa_verse_records: {c.fetchone()[0]} rows")

# Phase2 flags
c.execute("SELECT COUNT(*) FROM wa_term_phase2_flags WHERE term_inv_id IN (SELECT id FROM wa_term_inventory WHERE file_id IN (45,46,47))")
print(f"wa_term_phase2_flags: {c.fetchone()[0]} rows")

# mti_terms word_data_reference
c.execute("SELECT COUNT(*) FROM mti_terms WHERE owning_registry='051' AND word_data_reference IS NOT NULL")
not_null = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM mti_terms WHERE owning_registry='051' AND word_data_reference IS NULL")
null_count = c.fetchone()[0]
print(f"\nmti_terms (registry 051): word_data_reference set={not_null}, still null={null_count}")

# mti_term_cross_refs word_data_reference
c.execute("SELECT COUNT(*) FROM mti_term_cross_refs WHERE id IN (1,8,16,24,30,45,47,48,49,58,60,61,69) AND word_data_reference IS NOT NULL")
not_null = c.fetchone()[0]
print(f"mti_term_cross_refs (13 patched ids): word_data_reference set={not_null}/13")

# word_registry
c.execute("SELECT id, phase1_status, phase1_output_file FROM word_registry WHERE id=51")
r = c.fetchone()
print(f"\nword_registry id=51: phase1_status={r[1]}")
print(f"  phase1_output_file={r[2]}")

# Global state
c.execute("SELECT MAX(id) FROM wa_file_index")
print(f"\nGlobal MAX wa_file_index.id = {c.fetchone()[0]}")
c.execute("SELECT MAX(id) FROM wa_term_inventory")
print(f"Global MAX wa_term_inventory.id = {c.fetchone()[0]}")

conn.close()
print("\nDone.")
