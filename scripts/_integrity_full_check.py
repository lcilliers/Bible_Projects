import sqlite3, json

DB = r"G:\My Drive\Bible_study_projects\database\bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

results = {}

# Total
results["total_rows"] = conn.execute("SELECT COUNT(*) FROM wa_verse_records").fetchone()[0]

# FK orphans
checks = [
    ("orphan_file_id",     "LEFT JOIN wa_file_index fi ON vr.file_id = fi.id WHERE fi.id IS NULL"),
    ("orphan_term_inv_id", "LEFT JOIN wa_term_inventory ti ON vr.term_inv_id = ti.id WHERE vr.term_inv_id IS NOT NULL AND ti.id IS NULL"),
    ("orphan_book_id",     "LEFT JOIN books b ON vr.book_id = b.id WHERE vr.book_id IS NOT NULL AND b.id IS NULL"),
]
for key, clause in checks:
    results[key] = conn.execute(f"SELECT COUNT(*) FROM wa_verse_records vr {clause}").fetchone()[0]

# NULL fields (required to be populated for a fully resolved row)
null_checks = [
    ("null_file_id",     "file_id IS NULL"),
    ("null_book_id",     "book_id IS NULL"),
    ("null_chapter",     "chapter IS NULL"),
    ("null_verse_num",   "verse_num IS NULL"),
    ("null_term_inv_id", "term_inv_id IS NULL"),
    ("null_term_id",     "term_id IS NULL"),
    ("null_reference",   "reference IS NULL"),
    ("null_testament",   "testament IS NULL"),
    ("null_verse_text",  "verse_text IS NULL OR verse_text = ''"),
]
for key, cond in null_checks:
    results[key] = conn.execute(f"SELECT COUNT(*) FROM wa_verse_records WHERE {cond}").fetchone()[0]

# Span fields (expected NULL for pre-M05 imports — informational only)
results["span_strong_match_null"] = conn.execute(
    "SELECT COUNT(*) FROM wa_verse_records WHERE span_strong_match IS NULL").fetchone()[0]
results["target_word_null"] = conn.execute(
    "SELECT COUNT(*) FROM wa_verse_records WHERE target_word IS NULL OR target_word = ''").fetchone()[0]

conn.close()
print(json.dumps(results, indent=2))
