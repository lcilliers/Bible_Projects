import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

print("=== Distinct flag values in wa_data_quality_flags ===")
rows = conn.execute("""
    SELECT flag, COUNT(*) as cnt
    FROM wa_data_quality_flags
    GROUP BY flag
    ORDER BY cnt DESC
""").fetchall()
for r in rows:
    print(f"  {r[0]:40s}  {r[1]:>4}")

print()
print("=== Tables with 'flag' in name ===")
tbls = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%flag%'").fetchall()
for t in tbls:
    print(f"  {t[0]}")
    cols = conn.execute(f"PRAGMA table_info({t[0]})").fetchall()
    for c in cols:
        print(f"    {c[1]:25s}  {c[2]}")

conn.close()
