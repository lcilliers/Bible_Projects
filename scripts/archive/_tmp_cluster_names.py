import sqlite3, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass
conn = sqlite3.connect("database/bible_research.db")
conn.row_factory = sqlite3.Row
print("cluster columns:")
for r in conn.execute("PRAGMA table_info(cluster)"):
    print(f"  {r['name']:20s} {r['type']}")
print()
print("Sample rows (4 completed clusters):")
for r in conn.execute("SELECT cluster_code, gloss, description FROM cluster WHERE cluster_code IN ('M05','M06','M15','M26') ORDER BY cluster_code"):
    g_len = len(r["gloss"] or "")
    d_len = len(r["description"] or "")
    print(f"\n  {r['cluster_code']}:")
    print(f"    gloss ({g_len} chars):       {(r['gloss'] or '')[:80]}")
    print(f"    description ({d_len} chars): {(r['description'] or '')[:200]}")
print()
print("Lengths summary across all 47 cluster rows:")
for r in conn.execute("""
    SELECT cluster_code, LENGTH(gloss) AS g_len, LENGTH(description) AS d_len
      FROM cluster ORDER BY g_len DESC LIMIT 8
"""):
    print(f"  {r['cluster_code']:8s}  gloss={r['g_len']:>5d}  descr={r['d_len']:>5d}")
print("...")
for r in conn.execute("""
    SELECT cluster_code, LENGTH(gloss) AS g_len, LENGTH(description) AS d_len
      FROM cluster ORDER BY g_len ASC LIMIT 5
"""):
    print(f"  {r['cluster_code']:8s}  gloss={r['g_len']:>5d}  descr={r['d_len']:>5d}")
conn.close()
