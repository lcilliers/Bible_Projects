"""
migrate_drop_step_search_flag.py
Merges wa_term_inventory.step_search_flag into status_note, then drops the column.

Safe because:
  - Zero rows have both fields populated (confirmed by preview script).
  - 53 rows have step_search_flag set, status_note NULL  → copy to status_note.
  - 49 rows have status_note set, step_search_flag NULL  → unchanged.
  - 447 rows have both NULL → unchanged.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()
conn.execute("PRAGMA foreign_keys = ON")

# Verify no overlap before touching anything
overlap = conn.execute("""
    SELECT COUNT(*) FROM wa_term_inventory
    WHERE step_search_flag IS NOT NULL AND status_note IS NOT NULL
""").fetchone()[0]
if overlap:
    print(f"ERROR: {overlap} rows have both fields set — manual review required before proceeding.")
    conn.close()
    sys.exit(1)

flag_count = conn.execute(
    "SELECT COUNT(*) FROM wa_term_inventory WHERE step_search_flag IS NOT NULL"
).fetchone()[0]
print(f"Rows to merge: {flag_count}")

# Step 1 — copy step_search_flag → status_note where flag is set
conn.execute("""
    UPDATE wa_term_inventory
    SET status_note = step_search_flag
    WHERE step_search_flag IS NOT NULL AND status_note IS NULL
""")
updated = conn.execute(
    "SELECT COUNT(*) FROM wa_term_inventory WHERE status_note IS NOT NULL"
).fetchone()[0]
print(f"  [1] status_note populated: {updated} rows total")

# Step 2 — drop column (requires SQLite >= 3.35.0)
conn.execute("ALTER TABLE wa_term_inventory DROP COLUMN step_search_flag")
print("  [2] step_search_flag column dropped")

conn.commit()

# Verify
cols = [c[1] for c in conn.execute("PRAGMA table_info(wa_term_inventory)").fetchall()]
assert "step_search_flag" not in cols, "Column still present!"
print(f"  [3] Verified — column absent. Remaining columns: {len(cols)}")
print("✓ Migration complete")
conn.close()
