"""Fix bad word_data_reference values in mti_terms (Issue 1)."""
import sqlite3

DB = r"G:\My Drive\Bible_study_projects\data\bible_research.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Group A — Peace: placeholder numeric WDR → correct fi.ids 48/49/50
cur.execute("UPDATE mti_terms SET word_data_reference = '48' WHERE owning_word='peace' AND owning_part='1'")
a1 = cur.rowcount
cur.execute("UPDATE mti_terms SET word_data_reference = '49' WHERE owning_word='peace' AND owning_part='2'")
a2 = cur.rowcount
cur.execute("UPDATE mti_terms SET word_data_reference = '50' WHERE owning_word='peace' AND owning_part='3'")
a3 = cur.rowcount

# Group B — Gladness: pre-automation markdown filename → correct fi.id 51
cur.execute("UPDATE mti_terms SET word_data_reference = '51' WHERE word_data_reference = 'word_gladness.md'")
b = cur.rowcount

conn.commit()

print(f"Group A (peace):  part1={a1} rows, part2={a2} rows, part3={a3} rows  (total {a1+a2+a3})")
print(f"Group B (gladness): {b} rows")
print(f"Total updated: {a1+a2+a3+b}")

# Verify: re-check how many wdr values are not in wa_file_index
cur.execute("""
    SELECT COUNT(*) FROM mti_terms
    WHERE word_data_reference IS NOT NULL
      AND CAST(word_data_reference AS INTEGER) NOT IN (SELECT id FROM wa_file_index)
""")
remaining = cur.fetchone()[0]
print(f"Bad wdr remaining after fix: {remaining}")

conn.close()
