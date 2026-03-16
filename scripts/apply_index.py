"""Apply new composite index to the live DB and verify query plan improvement."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# Create the composite index
conn.execute("""
    CREATE INDEX IF NOT EXISTS idx_wavr_file_term_pos
        ON wa_verse_records (file_id, term_id, book_id, chapter, verse_num)
""")
conn.commit()
print("Index created: idx_wavr_file_term_pos")

# Verify plan is now index-only, no temp B-tree
print("\n=== QUERY PLAN AFTER: wa_verse_records file_id IN + ORDER BY ===")
for r in conn.execute(
    "EXPLAIN QUERY PLAN "
    "SELECT * FROM wa_verse_records "
    "WHERE file_id IN (22,23,24) "
    "ORDER BY term_id, book_id, chapter, verse_num"
).fetchall():
    print(f"  {dict(r)}")

conn.close()
