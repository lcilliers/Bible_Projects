"""Dump all schema facts needed to rebuild DB-Schema-Overview.docx."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# All tables
tables = [r[0] for r in conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
).fetchall()]
print("TABLES:", tables)

# Row counts
print("\n=== ROW COUNTS ===")
for t in tables:
    n = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"  {t}: {n}")

# Column info per table
print("\n=== COLUMNS ===")
for t in tables:
    cols = conn.execute(f"PRAGMA table_info({t})").fetchall()
    fks  = conn.execute(f"PRAGMA foreign_key_list({t})").fetchall()
    idxs = conn.execute(f"PRAGMA index_list({t})").fetchall()
    print(f"\n-- {t} --")
    for c in cols:
        nn = "NOT NULL" if c["notnull"] else ""
        pk = "PK" if c["pk"] else ""
        df = c["dflt_value"] or ""
        print(f"  {c['cid']:2d}  {c['name']:35s}  {c['type']:12s}  {nn:8s}  {pk:3s}  {df}")
    if fks:
        print("  FKs:")
        for fk in fks:
            print(f"    [{fk['from']}] -> {fk['table']}.{fk['to']}")
    if idxs:
        print("  Indexes:")
        for idx in idxs:
            sql = conn.execute(f"SELECT sql FROM sqlite_master WHERE name='{idx['name']}'").fetchone()
            print(f"    {idx['name']} (unique={idx['unique']})  {sql[0] or '(auto)'}")

conn.close()
