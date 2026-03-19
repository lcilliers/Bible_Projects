"""Audit all term reference fields across every table."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

tables = [r[0] for r in conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
).fetchall()]

print("=== TERM-RELATED COLUMNS ACROSS ALL TABLES ===\n")
term_keywords = ("term", "strongs", "strong", "ref", "inv")

for tbl in tables:
    cols = conn.execute(f"PRAGMA table_info({tbl})").fetchall()
    term_cols = [c for c in cols if any(k in c[1].lower() for k in term_keywords)]
    if term_cols:
        count = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
        print(f"  {tbl}  ({count} rows)")
        for c in term_cols:
            # Sample distinct values
            try:
                sample = conn.execute(
                    f"SELECT {c[1]}, COUNT(*) FROM {tbl} GROUP BY {c[1]} ORDER BY COUNT(*) DESC LIMIT 3"
                ).fetchall()
                vals = ", ".join(f"{repr(r[0])} ({r[1]})" for r in sample)
            except Exception:
                vals = "(error)"
            print(f"    {c[1]:<30}  type={c[2]:<10}  notnull={c[3]}  sample: {vals[:100]}")
        print()

conn.close()
