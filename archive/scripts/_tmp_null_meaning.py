import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
conn = get_connection()

rows = conn.execute("""
    SELECT id, language, term_id, transliteration,
           CASE WHEN meaning IS NULL THEN 'NULL' ELSE 'EMPTY_STR' END as why,
           meaning_numbered
    FROM wa_term_inventory
    WHERE meaning IS NULL OR meaning = ''
    ORDER BY language, id
""").fetchall()

print(f"Total terms with no meaning: {len(rows)}")
print()
for r in rows:
    mn = str(r[5])[:60] if r[5] else None
    print(f"  id={r[0]:4d}  {r[1]:6s}  {r[2]:20s}  {r[3]:22s}  meaning={r[4]}  meaning_numbered={mn}")

conn.close()
