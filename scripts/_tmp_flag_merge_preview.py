import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
conn = get_connection()

print("=== status_note: NULL / not NULL ===")
null_s  = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE status_note IS NULL").fetchone()[0]
total_s = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE status_note IS NOT NULL").fetchone()[0]
print(f"  Not NULL: {total_s}   NULL: {null_s}")

print()
print("=== Overlap: both fields set ===")
both = conn.execute("""
    SELECT COUNT(*) FROM wa_term_inventory
    WHERE step_search_flag IS NOT NULL AND status_note IS NOT NULL
""").fetchone()[0]
flag_only = conn.execute("""
    SELECT COUNT(*) FROM wa_term_inventory
    WHERE step_search_flag IS NOT NULL AND status_note IS NULL
""").fetchone()[0]
note_only = conn.execute("""
    SELECT COUNT(*) FROM wa_term_inventory
    WHERE step_search_flag IS NULL AND status_note IS NOT NULL
""").fetchone()[0]
print(f"  Both set:            {both}")
print(f"  flag only (note NULL): {flag_only}")
print(f"  note only (flag NULL): {note_only}")

print()
print("=== Rows where both are set — merged preview ===")
for r in conn.execute("""
    SELECT id, transliteration, step_search_flag, status_note
    FROM wa_term_inventory
    WHERE step_search_flag IS NOT NULL AND status_note IS NOT NULL
    ORDER BY id
""").fetchall():
    print(f"\n  id={r[0]}  trans={r[1]}")
    print(f"  FLAG : {r[2][:120]}")
    print(f"  NOTE : {r[3][:120]}")

print()
print("=== Sample: flag only rows (first 5) ===")
for r in conn.execute("""
    SELECT id, transliteration, step_search_flag
    FROM wa_term_inventory
    WHERE step_search_flag IS NOT NULL AND status_note IS NULL
    ORDER BY id LIMIT 5
""").fetchall():
    print(f"\n  id={r[0]}  trans={r[1]}")
    print(f"  FLAG : {r[2][:200]}")

conn.close()
