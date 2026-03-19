import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
conn = get_connection()

print("=== wa_term_inventory schema ===")
for c in conn.execute("PRAGMA table_info(wa_term_inventory)").fetchall():
    nn = "NOT NULL" if c[3] else ""
    print(f"  {c[0]:2d}  {c[1]:35s}  {c[2]:12s}  {nn}")
n = conn.execute("SELECT COUNT(*) FROM wa_term_inventory").fetchone()[0]
print(f"  --> {n} rows total")

print()
print("=== step_search_flag: distinct values ===")
for r in conn.execute("""
    SELECT step_search_flag, COUNT(*) cnt
    FROM wa_term_inventory
    GROUP BY step_search_flag
    ORDER BY cnt DESC
""").fetchall():
    print(f"  {str(r[0]):40s}  {r[1]}")

print()
print("=== step_search_gloss: NULL / not NULL ===")
null_g  = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE step_search_gloss IS NULL").fetchone()[0]
total_g = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE step_search_gloss IS NOT NULL").fetchone()[0]
print(f"  Not NULL: {total_g}   NULL: {null_g}")

print()
print("=== step_search_flag: NULL / not NULL ===")
null_f  = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE step_search_flag IS NULL").fetchone()[0]
total_f = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE step_search_flag IS NOT NULL").fetchone()[0]
print(f"  Not NULL: {total_f}   NULL: {null_f}")

print()
print("=== Sample: step_search_gloss vs step_search_flag vs word_analysis_gloss (30 rows) ===")
for r in conn.execute("""
    SELECT id, language, term_id, strongs_number, transliteration,
           step_search_gloss, step_search_flag, word_analysis_gloss
    FROM wa_term_inventory
    ORDER BY id
    LIMIT 30
""").fetchall():
    print(f"  id={r[0]:4d}  {r[1]:3s}  {str(r[2]):12s}  {str(r[3]):10s}  "
          f"trans={str(r[4]):18s}  "
          f"gloss={str(r[5]):25s}  "
          f"flag={str(r[6]):30s}  "
          f"wa_gloss={str(r[7])[:30]}")

print()
print("=== step_search_flag: sample of each distinct value ===")
flags = [r[0] for r in conn.execute(
    "SELECT DISTINCT step_search_flag FROM wa_term_inventory WHERE step_search_flag IS NOT NULL"
).fetchall()]
for flag in flags:
    samples = conn.execute("""
        SELECT transliteration, step_search_gloss, language
        FROM wa_term_inventory WHERE step_search_flag = ? LIMIT 3
    """, (flag,)).fetchall()
    print(f"\n  flag={flag!r}")
    for s in samples:
        print(f"    {str(s[2]):3s}  {str(s[0]):20s}  gloss={str(s[1])}")

conn.close()
