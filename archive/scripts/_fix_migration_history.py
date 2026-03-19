"""One-time fix: deduplicate migration_history in schema_version table."""
import json
import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

row = conn.execute("SELECT migration_history FROM schema_version WHERE id = 1").fetchone()
if not row:
    print("No schema_version row found.")
    conn.close()
    exit(1)

history = json.loads(row["migration_history"])
print(f"Before: {len(history)} entries")
for e in history:
    print(f"  {e.get('version')}  {e.get('applied_at', '')[:19]}")

seen: set[str] = set()
deduped = []
for e in history:
    v = e.get("version", "")
    if v not in seen:
        seen.add(v)
        deduped.append(e)

print(f"\nAfter:  {len(deduped)} entries")
for e in deduped:
    print(f"  {e.get('version')}  {e.get('applied_at', '')[:19]}")

if len(deduped) == len(history):
    print("\nNo duplicates found — nothing to do.")
else:
    conn.execute(
        "UPDATE schema_version SET migration_history = ? WHERE id = 1",
        (json.dumps(deduped),),
    )
    conn.commit()
    print(f"\nRemoved {len(history) - len(deduped)} duplicate(s). DB updated.")

conn.close()
