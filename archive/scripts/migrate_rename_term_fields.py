"""
Rename term-related columns for consistent naming convention.

Convention:
  TEXT Strong's code  ->  term_id        (matches wa_term_inventory.term_id)
  INT FK -> wa_term_inventory.id  ->  term_inv_id
  INT FK -> mti_terms.id          ->  mti_term_id

Renames:
  wa_verse_records.term_id_ref        -> term_id
  wa_data_quality_flags.term_ref      -> term_id
  wa_term_related_words.term_id       -> term_inv_id
  wa_term_root_family.term_id         -> term_inv_id
  wa_term_phase2_flags.term_id        -> term_inv_id
  mti_term_cross_refs.term_id         -> mti_term_id
  mti_term_flags.term_id              -> mti_term_id
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

renames = [
    ("wa_verse_records",       "term_id_ref", "term_id"),
    ("wa_data_quality_flags",  "term_ref",    "term_id"),
    ("wa_term_related_words",  "term_id",     "term_inv_id"),
    ("wa_term_root_family",    "term_id",     "term_inv_id"),
    ("wa_term_phase2_flags",   "term_id",     "term_inv_id"),
    ("mti_term_cross_refs",    "term_id",     "mti_term_id"),
    ("mti_term_flags",         "term_id",     "mti_term_id"),
]

# ── 1. Drop indexes that reference the columns being renamed ────────────────
indexes_to_drop = [
    "idx_wavr_term_ref",       # ON wa_verse_records (term_id_ref)
    "idx_wavr_file_term_pos",  # ON wa_verse_records (file_id, term_id_ref, ...)
]
for idx in indexes_to_drop:
    conn.execute(f"DROP INDEX IF EXISTS {idx}")
    print(f"Dropped index: {idx}")

# ── 2. Rename columns ────────────────────────────────────────────────────────
for table, old_col, new_col in renames:
    conn.execute(f"ALTER TABLE {table} RENAME COLUMN {old_col} TO {new_col}")
    print(f"Renamed: {table}.{old_col} -> {new_col}")

# ── 3. Recreate indexes with updated column names ────────────────────────────
conn.execute("""
    CREATE INDEX IF NOT EXISTS idx_wavr_term_id
    ON wa_verse_records (term_id)
""")
conn.execute("""
    CREATE INDEX IF NOT EXISTS idx_wavr_file_term_pos
    ON wa_verse_records (file_id, term_id, book_id, chapter, verse_num)
""")
print("Recreated indexes: idx_wavr_term_id, idx_wavr_file_term_pos")

conn.commit()

# ── 4. Verify ────────────────────────────────────────────────────────────────
print("\n=== VERIFICATION ===")
for table, _, new_col in renames:
    cols = [r[1] for r in conn.execute(f"PRAGMA table_info({table})").fetchall()]
    has_new = new_col in cols
    print(f"  {table}.{new_col}: {'OK' if has_new else 'MISSING!'}")

idxs = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='wa_verse_records'"
).fetchall()
print(f"\nwa_verse_records indexes: {[r[0] for r in idxs]}")

conn.close()
print("\nDone.")
