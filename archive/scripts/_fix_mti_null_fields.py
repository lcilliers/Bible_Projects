"""
Fix Issue 2 (NULL word_data_reference — 37 rows) and
    Issue 3 (NULL strongs_number — 1 row).

Issue 2 groups:
  joy  (097) Part1 (11 rows) → fi.id 42
  joy  (097) Part2  (7 rows) → fi.id 43
  joy  (097) Part3 (10 rows) → fi.id 44
  fear (061) NULL part (3 excluded rows) → fi.id 12 (part-1 convention)
  strength (187) NULL part (6 excluded rows) → fi.id 52 (part-1 convention)

Issue 3:
  mti_terms id=354 (alupos, 'without anxiety', Greek, reg 7 anxiety):
    strongs_number = 'G0253'  (ἄλυπος — confirmed by transliteration + gloss)
    strongs_reconciled = 1
  Same fix applied to the matching wa_term_inventory row.
"""
import sqlite3

DB = r"G:\My Drive\Bible_study_projects\data\bible_research.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

print("=" * 70)
print("APPLYING ISSUE 2 FIXES — NULL word_data_reference")
print("=" * 70)

fixes = [
    # joy parts
    ("UPDATE mti_terms SET word_data_reference='42' WHERE owning_registry='097' AND owning_part='Part1' AND word_data_reference IS NULL",  "joy Part1"),
    ("UPDATE mti_terms SET word_data_reference='43' WHERE owning_registry='097' AND owning_part='Part2' AND word_data_reference IS NULL",  "joy Part2"),
    ("UPDATE mti_terms SET word_data_reference='44' WHERE owning_registry='097' AND owning_part='Part3' AND word_data_reference IS NULL",  "joy Part3"),
    # fear excluded (NULL part)
    ("UPDATE mti_terms SET word_data_reference='12' WHERE owning_registry='061' AND owning_part IS NULL AND word_data_reference IS NULL",  "fear NULL-part excluded"),
    # strength excluded (NULL part)
    ("UPDATE mti_terms SET word_data_reference='52' WHERE owning_registry='187' AND owning_part IS NULL AND word_data_reference IS NULL",  "strength NULL-part excluded"),
]

total_2 = 0
for sql, label in fixes:
    cur.execute(sql)
    n = cur.rowcount
    total_2 += n
    print(f"  {label:<30}: {n} rows updated")

print(f"\n  Total Issue 2 rows updated: {total_2}")

# Verify
cur.execute("SELECT COUNT(*) FROM mti_terms WHERE word_data_reference IS NULL")
remaining_null = cur.fetchone()[0]
print(f"  Remaining NULL wdr after fix: {remaining_null}")

print()
print("=" * 70)
print("APPLYING ISSUE 3 FIX — NULL strongs_number")
print("=" * 70)

# Fix mti_terms row id=354
cur.execute("""
    UPDATE mti_terms
    SET strongs_number     = 'G0253',
        strongs_reconciled = 1,
        status_note        = 'G0253 (alupos) assigned from transliteration+gloss match; originally not confirmed in source file.'
    WHERE id = 354
""")
print(f"  mti_terms id=354: strongs_number set to G0253, strongs_reconciled=1 ({cur.rowcount} row)")

# Fix wa_term_inventory row (same transliteration, same word / file)
# Find it first
cur.execute("""
    SELECT ti.id FROM wa_term_inventory ti
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE ti.transliteration = 'alupos' AND fi.word_registry_fk = 7
""")
ti_rows = cur.fetchall()
for row in ti_rows:
    cur.execute("""
        UPDATE wa_term_inventory
        SET strongs_number = 'G0253',
            status_note    = 'G0253 (alupos) assigned from transliteration+gloss match; originally not confirmed in source file.'
        WHERE id = ?
    """, (row[0],))
    print(f"  wa_term_inventory id={row[0]}: strongs_number set to G0253 ({cur.rowcount} row)")

conn.commit()

# Final verification
cur.execute("SELECT COUNT(*) FROM mti_terms WHERE strongs_number IS NULL AND status != 'excluded'")
remaining_strongs = cur.fetchone()[0]
print(f"\n  Remaining NULL strongs (non-excluded) after fix: {remaining_strongs}")

cur.execute("SELECT COUNT(*) FROM mti_terms WHERE strongs_number IS NULL")
all_null = cur.fetchone()[0]
print(f"  Remaining NULL strongs (all) after fix: {all_null}")

conn.close()
print("\nAll fixes applied successfully.")
