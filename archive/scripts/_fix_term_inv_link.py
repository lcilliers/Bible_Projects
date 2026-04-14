import sqlite3

DB = r"G:\My Drive\Bible_study_projects\data\bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

# FIX: set term_inv_id=173 on the orphan row
conn.execute("UPDATE wa_verse_records SET term_inv_id = 173 WHERE id = 1636")
conn.commit()

row = conn.execute("SELECT id, term_inv_id, term_id, reference FROM wa_verse_records WHERE id = 1636").fetchone()
print("Updated row:", dict(row))

remaining = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id IS NULL").fetchone()[0]
print("Remaining NULL term_inv_id rows:", remaining)
conn.close()

# --- DIAGNOSTIC (original) ---
# What word is file_id=10?
fi = conn.execute("SELECT id, filename, word, registry_id FROM wa_file_index WHERE id = 10").fetchone()
print("wa_file_index id=10:", dict(fi))

# Does G3715 exist in wa_term_inventory for file_id=10?
ti_rows = conn.execute("""
    SELECT id, term_id, strongs_number, transliteration, step_search_gloss
    FROM wa_term_inventory
    WHERE file_id = 10 AND (term_id LIKE 'G3715%' OR strongs_number LIKE 'G3715%')
""").fetchall()
print(f"\nwa_term_inventory rows for G3715 in file_id=10: {len(ti_rows)}")
for r in ti_rows:
    print(" ", dict(r))

# Also check if G3715 exists in ANY file
ti_any = conn.execute("""
    SELECT id, file_id, term_id, strongs_number, transliteration
    FROM wa_term_inventory
    WHERE term_id LIKE 'G3715%' OR strongs_number LIKE 'G3715%'
""").fetchall()
print(f"\nG3715 in wa_term_inventory (all files): {len(ti_any)}")
for r in ti_any:
    print(" ", dict(r))

# The orphan verse row itself
vr = conn.execute("SELECT * FROM wa_verse_records WHERE id = 1636").fetchone()
print("\nOrphan verse row:", dict(vr))

conn.close()
