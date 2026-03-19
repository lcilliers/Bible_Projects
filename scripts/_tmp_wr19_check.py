import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

# Check parse warnings for H8001 and H2013
print("=== Parse warnings ===")
rows = conn.execute("""
    SELECT ti.id AS ti_id, ti.file_id, ti.strongs_number, ti.transliteration, mp.parse_warnings
    FROM wa_meaning_parsed mp
    JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id
    WHERE ti.file_id IN (48,49,50) AND mp.parse_warnings IS NOT NULL
""").fetchall()
for r in rows:
    print(dict(r))

# Check NOTE flag type
print("\n=== wa_quality_flag_types NOTE ===")
rows = conn.execute("SELECT * FROM wa_quality_flag_types WHERE flag_code = 'NOTE'").fetchall()
for r in rows:
    print(dict(r))

# Check existing NOTE flags for file_ids 48-50
print("\n=== existing NOTE flags ===")
rows = conn.execute("""
    SELECT dqf.*, qt.flag_code FROM wa_data_quality_flags dqf
    JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id
    WHERE dqf.file_id IN (48,49,50) AND qt.flag_code = 'NOTE'
""").fetchall()
for r in rows:
    print(dict(r))
