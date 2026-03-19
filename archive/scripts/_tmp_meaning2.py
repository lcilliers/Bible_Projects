import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
conn = get_connection()

print("=== Rows where BOTH are set — side by side (short meaning rows) ===")
for r in conn.execute("""
    SELECT id, transliteration, meaning, meaning_numbered
    FROM wa_term_inventory
    WHERE meaning IS NOT NULL AND meaning_numbered IS NOT NULL
      AND length(meaning) BETWEEN 10 AND 200
    ORDER BY id LIMIT 6
""").fetchall():
    print(f"  id={r[0]}  {r[1]}")
    print(f"    meaning:          {r[2][:200]}")
    print(f"    meaning_numbered: {r[3][:200]}")
    print()

print("=== meaning_numbered ONLY (2 rows, no meaning) ===")
for r in conn.execute("""
    SELECT id, transliteration, meaning, meaning_numbered
    FROM wa_term_inventory
    WHERE meaning IS NULL AND meaning_numbered IS NOT NULL
""").fetchall():
    print(f"  id={r[0]}  {r[1]}  meaning={r[2]!r}")
    print(f"    numbered: {r[3][:300]}")
    print()

print("=== meaning is empty string ===")
n = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE meaning = ''").fetchone()[0]
print(f"  count: {n}")

print()
print("=== Both set — one row where they DIFFER clearly ===")
for r in conn.execute("""
    SELECT id, transliteration, meaning, meaning_numbered
    FROM wa_term_inventory
    WHERE meaning IS NOT NULL AND meaning_numbered IS NOT NULL
      AND meaning != meaning_numbered
    ORDER BY length(meaning_numbered) DESC LIMIT 3
""").fetchall():
    print(f"\n  id={r[0]}  {r[1]}")
    print(f"    meaning:          {r[2][:400]}")
    print(f"    meaning_numbered: {r[3][:400]}")

conn.close()
