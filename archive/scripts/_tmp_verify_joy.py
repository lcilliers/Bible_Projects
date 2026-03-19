import sys
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.db_client import get_connection

conn = get_connection()
cur = conn.cursor()

print("── phase2_flag_types (all 25) ──")
cur.execute("SELECT id, flag_code, CASE WHEN description IS NULL THEN '(null)' ELSE 'ok' END FROM phase2_flag_types ORDER BY id")
for r in cur.fetchall():
    print(f"  {r[0]:>3}  {r[1]:<40}  desc={r[2]}")

print()
print("── joy (097) file index entries ──")
cur.execute("SELECT id, filename, part_number FROM wa_file_index WHERE registry_id='097' ORDER BY id")
for r in cur.fetchall():
    print(f"  id={r[0]}  {r[1]}  part={r[2]}")

print()
print("── joy term inventory (ids 550-574) ──")
cur.execute("SELECT id, term_id, transliteration FROM wa_term_inventory WHERE id BETWEEN 550 AND 574 ORDER BY id")
for r in cur.fetchall():
    print(f"  {r[0]:>3}  {r[1]:<12}  {r[2]}")

print()
print("── Row counts ──")
for t in ["wa_verse_records", "wa_term_phase2_flags", "wa_term_related_words",
          "wa_term_root_family", "wa_data_quality_flags", "wa_cross_registry_links",
          "mti_term_cross_refs"]:
    cur.execute(f"SELECT COUNT(*) FROM {t}")
    print(f"  {t:<35} {cur.fetchone()[0]}")

conn.close()
