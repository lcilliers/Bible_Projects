"""
_fix_null_term_id.py
─────────────────────
Fix 1: Copy strongs_number from wa_term_inventory into wa_verse_records.term_id
for all rows where term_id IS NULL but term_inv_id is set.
"""
import sqlite3

DB = r"G:\My Drive\Bible_study_projects\data\bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

before = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE term_id IS NULL").fetchone()[0]
print(f"Rows with null term_id before fix: {before}")

conn.execute("""
    UPDATE wa_verse_records
    SET term_id = (
        SELECT ti.strongs_number
        FROM wa_term_inventory ti
        WHERE ti.id = wa_verse_records.term_inv_id
    )
    WHERE term_id IS NULL
      AND term_inv_id IS NOT NULL
      AND EXISTS (
        SELECT 1 FROM wa_term_inventory ti
        WHERE ti.id = wa_verse_records.term_inv_id
          AND ti.strongs_number IS NOT NULL
      )
""")
conn.commit()

after = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE term_id IS NULL").fetchone()[0]
print(f"Rows with null term_id after fix:  {after}")
print(f"Rows updated: {before - after}")

conn.close()
