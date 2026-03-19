"""Inspect wa_data_quality_flags table."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# Schema
cols = conn.execute("PRAGMA table_info(wa_data_quality_flags)").fetchall()
print("=== SCHEMA ===")
for c in cols:
    print(f"  {c[0]:>2}  {c[1]:<30}  {c[2]:<12}  notnull={c[3]}  default={c[4]}")

print()

# Row counts
total = conn.execute("SELECT COUNT(*) FROM wa_data_quality_flags").fetchone()[0]
print(f"Total rows: {total}")

print()

# Distinct values of flag column
for col in ("flag",):
    rows = conn.execute(
        f"SELECT {col}, COUNT(*) AS cnt FROM wa_data_quality_flags GROUP BY {col} ORDER BY cnt DESC"
    ).fetchall()
    print(f"  {col} breakdown:")
    for r in rows:
        print(f"    {str(r[0]):<50}  {r[1]}")
    print()

# Files represented
file_rows = conn.execute(
    "SELECT file_id, COUNT(*) AS cnt FROM wa_data_quality_flags GROUP BY file_id ORDER BY file_id"
).fetchall()
print("  file_id breakdown:")
for r in file_rows:
    fi = conn.execute("SELECT word, filename FROM wa_file_index WHERE id=?", (r[0],)).fetchone()
    fname = fi["filename"] if fi else "?"
    word  = fi["word"]     if fi else "?"
    print(f"    file_id={r[0]}  {word:<20}  {fname:<50}  flags={r[1]}")
print()

# Sample rows — full content
print("=== SAMPLE ROWS (first 20) ===")
rows = conn.execute("SELECT * FROM wa_data_quality_flags ORDER BY id LIMIT 20").fetchall()
for row in rows:
    print(f"  --- id={row['id']} ---")
    for k in row.keys():
        if row[k] is not None:
            val = str(row[k])
            print(f"    {k:<30} = {val[:120]}")
    print()

conn.close()
