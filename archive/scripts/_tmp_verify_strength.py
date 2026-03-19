import sys; sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.db_client import get_connection
conn = get_connection()

print("=== strength (registry 187) import summary ===\n")

rows = conn.execute(
    "SELECT id, filename, part_number, total_parts, testament_coverage "
    "FROM wa_file_index WHERE registry_id='187' ORDER BY part_number"
).fetchall()
print("wa_file_index:")
for r in rows:
    print(f"  id={r[0]}  part={r[2]}/{r[3]}  testament={r[4]}  file={r[1]}")
print()

new = conn.execute(
    "SELECT COUNT(*) FROM mti_terms WHERE owning_registry='187' AND status='extracted'"
).fetchone()[0]
excl = conn.execute(
    "SELECT COUNT(*) FROM mti_terms WHERE owning_registry='187' AND status='excluded'"
).fetchone()[0]
print(f"mti_terms: {new} extracted, {excl} excluded")
print()

inv = conn.execute(
    "SELECT COUNT(*) FROM wa_term_inventory ti "
    "JOIN wa_file_index fi ON ti.file_id=fi.id WHERE fi.registry_id='187'"
).fetchone()[0]
print(f"wa_term_inventory: {inv} terms")
print()

vr = conn.execute(
    "SELECT COUNT(*) FROM wa_verse_records vr "
    "JOIN wa_file_index fi ON vr.file_id=fi.id WHERE fi.registry_id='187'"
).fetchone()[0]
print(f"wa_verse_records: {vr} verses")
print()

wr = conn.execute(
    "SELECT no, word, phase1_status, phase1_output_file FROM word_registry WHERE no=187"
).fetchone()
print(f"word_registry: no={wr[0]}  word={wr[1]}  status={wr[2]}")
print(f"  output_file: {wr[3]}")
print()

print("New MAX ids:")
for tbl in ["wa_file_index", "mti_terms", "wa_term_inventory", "wa_verse_records"]:
    mx = conn.execute(f"SELECT MAX(id) FROM {tbl}").fetchone()[0]
    print(f"  {tbl}: {mx}")

conn.close()
