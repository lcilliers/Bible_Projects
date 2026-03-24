import sqlite3, json

DB = r"G:\My Drive\Bible_study_projects\data\bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

results = {}

cur.execute("SELECT COUNT(*) FROM wa_verse_records")
results["total_rows"] = cur.fetchone()[0]

cur.execute("""
    SELECT COUNT(*) FROM wa_verse_records vr
    LEFT JOIN wa_file_index fi ON vr.file_id = fi.id
    WHERE fi.id IS NULL
""")
results["orphan_file_id"] = cur.fetchone()[0]

cur.execute("""
    SELECT COUNT(*) FROM wa_verse_records vr
    LEFT JOIN wa_term_inventory ti ON vr.term_inv_id = ti.id
    WHERE vr.term_inv_id IS NOT NULL AND ti.id IS NULL
""")
results["orphan_term_inv_id"] = cur.fetchone()[0]

cur.execute("""
    SELECT COUNT(*) FROM wa_verse_records vr
    LEFT JOIN books b ON vr.book_id = b.id
    WHERE vr.book_id IS NOT NULL AND b.id IS NULL
""")
results["orphan_book_id"] = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM wa_verse_records WHERE book_id IS NULL")
results["null_book_id"] = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id IS NULL")
results["null_term_inv_id"] = cur.fetchone()[0]

cur.execute("""
    SELECT DISTINCT vr.file_id FROM wa_verse_records vr
    LEFT JOIN wa_file_index fi ON vr.file_id = fi.id
    WHERE fi.id IS NULL LIMIT 10
""")
results["sample_orphan_file_ids"] = [r[0] for r in cur.fetchall()]

cur.execute("""
    SELECT DISTINCT vr.term_inv_id FROM wa_verse_records vr
    LEFT JOIN wa_term_inventory ti ON vr.term_inv_id = ti.id
    WHERE vr.term_inv_id IS NOT NULL AND ti.id IS NULL LIMIT 10
""")
results["sample_orphan_term_inv_ids"] = [r[0] for r in cur.fetchall()]

cur.execute("""
    SELECT id, file_id, term_id, reference FROM wa_verse_records
    WHERE book_id IS NULL LIMIT 10
""")
results["sample_null_book_id"] = [dict(r) for r in cur.fetchall()]

cur.execute("""
    SELECT SUBSTR(reference, 1, INSTR(reference||' ', ' ')-1) as book_prefix, COUNT(*) as cnt
    FROM wa_verse_records WHERE book_id IS NULL
    GROUP BY book_prefix ORDER BY cnt DESC LIMIT 10
""")
results["null_book_id_by_prefix"] = [dict(r) for r in cur.fetchall()]

conn.close()
print(json.dumps(results, indent=2))
