import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
conn = get_connection()

print("=== wa_cross_registry_links schema ===")
for c in conn.execute("PRAGMA table_info(wa_cross_registry_links)").fetchall():
    print(f"  {c[1]:30s}  {c[2]}")
n = conn.execute("SELECT COUNT(*) FROM wa_cross_registry_links").fetchone()[0]
print(f"  --> {n} rows total")

print()
print("=== Distinct connection_type values ===")
for r in conn.execute("""
    SELECT connection_type, COUNT(*) cnt
    FROM wa_cross_registry_links
    GROUP BY connection_type
    ORDER BY cnt DESC
""").fetchall():
    print(f"  {str(r[0]):35s}  {r[1]}")

print()
print("=== Distinct connecting_term values ===")
for r in conn.execute("""
    SELECT connecting_term, COUNT(*) cnt
    FROM wa_cross_registry_links
    GROUP BY connecting_term
    ORDER BY cnt DESC
""").fetchall():
    print(f"  {str(r[0]):35s}  {r[1]}")

print()
print("=== Sample rows (first 20) ===")
rows = conn.execute("""
    SELECT id, file_id, linked_word, linked_registry_id,
           connection_type, connecting_term, note
    FROM wa_cross_registry_links
    ORDER BY file_id, id
    LIMIT 20
""").fetchall()
for r in rows:
    print(f"  id={r[0]:4d}  file={r[1]:3d}  linked={str(r[2]):20s}  "
          f"reg_id={str(r[3]):4s}  type={str(r[4]):25s}  term={str(r[5])}")

conn.close()
