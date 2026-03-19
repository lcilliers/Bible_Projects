"""Verify FK targets and term field values for naming audit."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# FK relationships for term_id columns
print("=== FOREIGN KEY DECLARATIONS ===")
for tbl in ("wa_term_related_words", "wa_term_root_family", "wa_term_phase2_flags",
            "mti_term_cross_refs", "mti_term_flags", "wa_verse_records"):
    fks = conn.execute(f"PRAGMA foreign_key_list({tbl})").fetchall()
    term_fks = [r for r in fks if "term" in r["from"].lower()]
    print(f"  {tbl}:")
    if term_fks:
        for r in term_fks:
            print(f"    {r['from']} -> {r['table']}.{r['to']}")
    else:
        print("    (no declared term FKs)")

print()

# wa_data_quality_flags.term_ref — all distinct values
rows = conn.execute(
    "SELECT DISTINCT term_ref FROM wa_data_quality_flags ORDER BY term_ref"
).fetchall()
print(f"=== wa_data_quality_flags.term_ref ({len(rows)} distinct values) ===")
for r in rows[:40]:
    print(f"  {repr(r[0])}")

print()

# wa_term_inventory: strongs_number vs term_id
diff_rows = conn.execute(
    "SELECT id, term_id, strongs_number FROM wa_term_inventory WHERE strongs_number != term_id"
).fetchall()
null_sn = conn.execute(
    "SELECT COUNT(*) FROM wa_term_inventory WHERE strongs_number IS NULL"
).fetchone()[0]
total = conn.execute("SELECT COUNT(*) FROM wa_term_inventory").fetchone()[0]
print(f"=== wa_term_inventory: strongs_number vs term_id (total={total}) ===")
print(f"  strongs_number IS NULL: {null_sn}")
print(f"  strongs_number != term_id: {len(diff_rows)}")
for r in diff_rows[:20]:
    print(f"  id={r[0]}  term_id={r[1]}  strongs_number={r[2]}")

conn.close()
