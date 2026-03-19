import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

# H7965H and H8001 term_inventory rows
print("=== H7965H and H8001 in wa_term_inventory ===")
rows = conn.execute("""
    SELECT id, file_id, strongs_number, transliteration, occurrence_count, testament, status_note
    FROM wa_term_inventory
    WHERE strongs_number IN ('H7965H','H8001') AND file_id IN (48,49,50)
""").fetchall()
for r in rows: print(dict(r))

# H7965H verses currently stored
print("\n=== wa_verse_records for H7965H ===")
rows = conn.execute("""
    SELECT vr.id, vr.reference, vr.term_id, vr.span_strong_match
    FROM wa_verse_records vr
    JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
    WHERE ti.strongs_number = 'H7965H'
""").fetchall()
for r in rows: print(dict(r))

# H8001 verses currently stored
print("\n=== wa_verse_records for H8001 ===")
rows = conn.execute("""
    SELECT vr.id, vr.reference, vr.term_id, vr.span_strong_match
    FROM wa_verse_records vr
    JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
    WHERE ti.strongs_number = 'H8001'
""").fetchall()
for r in rows: print(dict(r))
