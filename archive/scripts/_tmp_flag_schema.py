import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

# Schema of wa_data_quality_flags
print("=== wa_data_quality_flags schema ===")
rows = conn.execute("PRAGMA table_info(wa_data_quality_flags)").fetchall()
for r in rows:
    print(dict(r))

# Sample existing flags for file_id 48
print("\n=== existing flags file_id=48 (sample 5) ===")
rows = conn.execute("""
    SELECT dqf.*, qt.flag_code, qt.flag_group FROM wa_data_quality_flags dqf
    JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id
    WHERE dqf.file_id = 48 LIMIT 5
""").fetchall()
for r in rows:
    print(dict(r))

# NOTE flag type id
print("\n=== NOTE flag type ===")
r = conn.execute("SELECT * FROM wa_quality_flag_types WHERE flag_code = 'NOTE'").fetchone()
print(dict(r))
