"""Inspect indexes and query plans relevant to the word-extract chain."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

print("=== EXISTING INDEXES ===")
rows = conn.execute(
    "SELECT name, tbl_name, sql FROM sqlite_master WHERE type='index' ORDER BY tbl_name, name"
).fetchall()
for r in rows:
    print(f"  [{r['tbl_name']}]  {r['name']}")
    if r['sql']:
        print(f"    {r['sql']}")

plans = [
    ("wa_file_index by word",
     "SELECT * FROM wa_file_index WHERE word = 'love'"),
    ("mti_terms by owning_registry",
     "SELECT * FROM mti_terms WHERE owning_registry = '103'"),
    ("wa_term_inventory by file_id IN",
     "SELECT * FROM wa_term_inventory WHERE file_id IN (22,23,24)"),
    ("wa_term_related_words by term_inv_id IN",
     "SELECT * FROM wa_term_related_words WHERE term_inv_id IN (327,328,329,330,331)"),
    ("wa_term_root_family by term_inv_id IN",
     "SELECT * FROM wa_term_root_family WHERE term_inv_id IN (327,328,329,330,331)"),
    ("wa_term_phase2_flags by term_inv_id IN",
     "SELECT * FROM wa_term_phase2_flags WHERE term_inv_id IN (327,328,329,330,331)"),
    ("wa_cross_registry_links by file_id IN",
     "SELECT * FROM wa_cross_registry_links WHERE file_id IN (22,23,24)"),
    ("wa_data_quality_flags by file_id IN",
     "SELECT * FROM wa_data_quality_flags WHERE file_id IN (22,23,24)"),
    ("wa_verse_records by file_id IN + ORDER BY",
     "SELECT * FROM wa_verse_records WHERE file_id IN (22,23,24) ORDER BY term_id, book_id, chapter, verse_num"),
    ("mti_term_flags by term_id IN",
     "SELECT * FROM mti_term_flags WHERE term_id IN (533,534,535,536,537)"),
    ("mti_term_cross_refs by term_id IN",
     "SELECT * FROM mti_term_cross_refs WHERE term_id IN (533,534,535,536,537)"),
]

for label, sql in plans:
    print(f"\n=== QUERY PLAN: {label} ===")
    for r in conn.execute(f"EXPLAIN QUERY PLAN {sql}").fetchall():
        print(f"  {dict(r)}")

conn.close()
