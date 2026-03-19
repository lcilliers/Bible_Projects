"""Integrity checks on wa_verse_records."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# ── a) Files with no verses ───────────────────────────────────────────────────
print("=== a) wa_file_index entries with NO verse records ===")
empty_files = conn.execute("""
    SELECT f.id, f.filename, f.word, f.part_number, f.testament_coverage
    FROM wa_file_index f
    LEFT JOIN wa_verse_records v ON v.file_id = f.id
    WHERE v.id IS NULL
    ORDER BY f.id
""").fetchall()
if empty_files:
    print(f"  {'id':>4}  {'filename':<50}  {'word':<20}  part  testament_coverage")
    for r in empty_files:
        print(f"  {r[0]:>4}  {str(r[1]):<50}  {str(r[2]):<20}  {str(r[3]):<5} {str(r[4])}")
else:
    print("  None — every file has at least one verse record.")

print()

# ── b) Referential integrity ──────────────────────────────────────────────────
print("=== b) Referential integrity ===")

# file_id orphans (wa_verse_records.file_id not in wa_file_index)
bad_file_id = conn.execute("""
    SELECT COUNT(*) FROM wa_verse_records v
    LEFT JOIN wa_file_index f ON f.id = v.file_id
    WHERE f.id IS NULL
""").fetchone()[0]
print(f"  Orphan file_id (no match in wa_file_index): {bad_file_id}")

# term_inv_id orphans (where not null)
bad_term_inv = conn.execute("""
    SELECT COUNT(*) FROM wa_verse_records v
    LEFT JOIN wa_term_inventory t ON t.id = v.term_inv_id
    WHERE v.term_inv_id IS NOT NULL AND t.id IS NULL
""").fetchone()[0]
print(f"  Orphan term_inv_id (not null, no match in wa_term_inventory): {bad_term_inv}")

# NULL term_inv_id count
null_term_inv = conn.execute(
    "SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id IS NULL"
).fetchone()[0]
total = conn.execute("SELECT COUNT(*) FROM wa_verse_records").fetchone()[0]
print(f"  NULL term_inv_id: {null_term_inv} / {total} rows")

# book_id orphans
bad_book_id = conn.execute("""
    SELECT COUNT(*) FROM wa_verse_records v
    LEFT JOIN books b ON b.id = v.book_id
    WHERE v.book_id IS NOT NULL AND b.id IS NULL
""").fetchone()[0]
print(f"  Orphan book_id (not null, no match in books): {bad_book_id}")

print()

# ── c) NULLs in key fields ────────────────────────────────────────────────────
print("=== c) NULL counts in transliteration, testament, verse_text, created_at ===")
for col in ("transliteration", "testament", "verse_text", "created_at"):
    n = conn.execute(
        f"SELECT COUNT(*) FROM wa_verse_records WHERE {col} IS NULL"
    ).fetchone()[0]
    pct = n / total * 100
    print(f"  {col:<20}  NULL: {n:>5}  ({pct:.1f}%)")

# Show any NULL testament rows — small set expected
null_test = conn.execute("""
    SELECT id, term_id, file_id, reference, testament
    FROM wa_verse_records WHERE testament IS NULL LIMIT 10
""").fetchall()
if null_test:
    print()
    print("  NULL testament sample:")
    for r in null_test:
        print(f"    id={r[0]}  term={r[1]}  file_id={r[2]}  ref={r[3]}")

# Show NULL created_at rows
null_ca = conn.execute("""
    SELECT id, term_id, file_id, reference, created_at
    FROM wa_verse_records WHERE created_at IS NULL LIMIT 10
""").fetchall()
if null_ca:
    print()
    print("  NULL created_at sample:")
    for r in null_ca:
        print(f"    id={r[0]}  term={r[1]}  file_id={r[2]}  ref={r[3]}")

conn.close()
