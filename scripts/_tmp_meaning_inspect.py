import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
conn = get_connection()

print("=== meaning / meaning_numbered: NULL counts ===")
for col in ("meaning", "meaning_numbered"):
    null_  = conn.execute(f"SELECT COUNT(*) FROM wa_term_inventory WHERE {col} IS NULL").fetchone()[0]
    notnull = conn.execute(f"SELECT COUNT(*) FROM wa_term_inventory WHERE {col} IS NOT NULL").fetchone()[0]
    print(f"  {col:20s}  not null: {notnull:4d}   null: {null_}")

print()
print("=== Overlap ===")
both   = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE meaning IS NOT NULL AND meaning_numbered IS NOT NULL").fetchone()[0]
m_only = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE meaning IS NOT NULL AND meaning_numbered IS NULL").fetchone()[0]
n_only = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE meaning IS NULL AND meaning_numbered IS NOT NULL").fetchone()[0]
neith  = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE meaning IS NULL AND meaning_numbered IS NULL").fetchone()[0]
print(f"  Both set:              {both}")
print(f"  meaning only:          {m_only}")
print(f"  meaning_numbered only: {n_only}")
print(f"  Neither:               {neith}")

print()
print("=== meaning: sample of 5 short values ===")
for r in conn.execute("""
    SELECT id, transliteration, length(meaning), meaning
    FROM wa_term_inventory WHERE meaning IS NOT NULL
    ORDER BY length(meaning) LIMIT 5
""").fetchall():
    print(f"  id={r[0]:4d}  {r[1]:18s}  len={r[2]:4d}  {r[3][:200]}")

print()
print("=== meaning: sample of 5 long values ===")
for r in conn.execute("""
    SELECT id, transliteration, length(meaning), meaning
    FROM wa_term_inventory WHERE meaning IS NOT NULL
    ORDER BY length(meaning) DESC LIMIT 5
""").fetchall():
    print(f"\n  id={r[0]:4d}  {r[1]:18s}  len={r[2]}")
    print(f"  {r[3][:400]}")

print()
print("=== meaning_numbered: what is the stored format? (first 5 rows) ===")
for r in conn.execute("""
    SELECT id, transliteration, meaning_numbered
    FROM wa_term_inventory WHERE meaning_numbered IS NOT NULL
    ORDER BY id LIMIT 5
""").fetchall():
    print(f"\n  id={r[0]:4d}  {r[1]:18s}")
    # try to detect if it's JSON
    val = r[2]
    try:
        parsed = json.loads(val)
        print(f"  [JSON] type={type(parsed).__name__}  preview: {str(parsed)[:300]}")
    except Exception:
        print(f"  [TEXT]  {val[:300]}")

print()
print("=== meaning_numbered length distribution ===")
for r in conn.execute("""
    SELECT length(meaning_numbered), COUNT(*)
    FROM wa_term_inventory WHERE meaning_numbered IS NOT NULL
    GROUP BY length(meaning_numbered) < 200
    ORDER BY 1
""").fetchall():
    print(f"  len_bucket={'<200' if r[0]==0 else '>=200'}  count={r[1]}")

conn.close()
