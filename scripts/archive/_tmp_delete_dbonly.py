#!/usr/bin/env python3
"""
Delete H4578, H5397, G5590 from all tables.
Researcher confirmed deletion 2026-03-23.
Backup taken: data/bible_research.db.bak_Before_Delete_DBOnly_20260323_205118
"""
import sqlite3, os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB    = os.path.join(_ROOT, "data", "bible_research.db")

CODES    = ["H4578", "H5397", "G5590"]
TI_IDS   = [490, 491, 493]      # wa_term_inventory.id
MTI_IDS  = [515, 516, 517]      # mti_terms.id
FILE_ID  = 36
REG_NO   = 182

conn = sqlite3.connect(DB)
conn.execute("PRAGMA foreign_keys = OFF")   # deleting in order; disable FK enforcement
cur  = conn.cursor()

print("=== DELETE: child tables first ===\n")

# 1. wa_data_quality_flags  (uses file_id + term_id TEXT)
cur.executemany(
    "DELETE FROM wa_data_quality_flags WHERE file_id=? AND term_id=?",
    [(FILE_ID, c) for c in CODES]
)
print(f"wa_data_quality_flags deleted: {cur.rowcount} rows (last stmt)")

# Re-check total
total = conn.execute(
    "SELECT COUNT(*) FROM wa_data_quality_flags WHERE file_id=? AND term_id IN ('H4578','H5397','G5590')",
    (FILE_ID,)
).fetchone()[0]
print(f"  remaining quality flags for these codes: {total}")

# 2. wa_term_root_family  (uses term_inv_id)
cur.execute(
    "DELETE FROM wa_term_root_family WHERE term_inv_id IN (490,491,493)"
)
print(f"\nwa_term_root_family deleted: {cur.rowcount} rows")

# 3. wa_term_related_words  (uses term_inv_id)
cur.execute(
    "DELETE FROM wa_term_related_words WHERE term_inv_id IN (490,491,493)"
)
print(f"wa_term_related_words deleted: {cur.rowcount} rows")

# 4. wa_verse_term_links  (uses term_inv_id — already 0 but belt-and-braces)
cur.execute(
    "DELETE FROM wa_verse_term_links WHERE term_inv_id IN (490,491,493)"
)
print(f"wa_verse_term_links deleted: {cur.rowcount} rows")

# 5. wa_term_phase2_flags  (uses term_inv_id)
cur.execute(
    "DELETE FROM wa_term_phase2_flags WHERE term_inv_id IN (490,491,493)"
)
print(f"wa_term_phase2_flags deleted: {cur.rowcount} rows")

# 6. wa_meaning_sense / wa_meaning_stem / wa_lsj_parsed / wa_meaning_parsed
#    (all use term_inv_id or link through parsed_meaning_id — check for rows)
for tbl in ("wa_meaning_parsed", "wa_meaning_sense", "wa_meaning_stem", "wa_lsj_parsed"):
    cols = [r[1] for r in conn.execute(f"PRAGMA table_info({tbl})").fetchall()]
    if "term_inv_id" in cols:
        cur.execute(f"DELETE FROM {tbl} WHERE term_inv_id IN (490,491,493)")
        print(f"{tbl} deleted: {cur.rowcount} rows")

print("\n=== DELETE: mti_terms ===")
cur.execute("DELETE FROM mti_terms WHERE id IN (515,516,517)")
print(f"mti_terms deleted: {cur.rowcount} rows")

print("\n=== DELETE: wa_term_inventory ===")
cur.execute("DELETE FROM wa_term_inventory WHERE id IN (490,491,493)")
print(f"wa_term_inventory deleted: {cur.rowcount} rows")

print("\n=== UPDATE: word_registry counts ===")
# Recount from DB
new_term_count = conn.execute(
    "SELECT COUNT(*) FROM wa_term_inventory WHERE file_id=? AND delete_flagged=0",
    (FILE_ID,)
).fetchone()[0]
new_delete_flagged = conn.execute(
    "SELECT COUNT(*) FROM wa_term_inventory WHERE file_id=? AND delete_flagged=1",
    (FILE_ID,)
).fetchone()[0]

cur.execute(
    "UPDATE word_registry SET term_count=? WHERE no=?",
    (new_term_count, REG_NO)
)
print(f"word_registry.term_count → {new_term_count} (delete_flagged remaining: {new_delete_flagged})")

conn.commit()
conn.execute("PRAGMA foreign_keys = ON")
conn.close()

print("\n=== DONE ===")
