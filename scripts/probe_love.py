"""Probe the 'love' word chain from registry to verses."""
from analytics.db_client import get_connection

conn = get_connection()

print("=== word_registry: love ===")
rows = conn.execute("SELECT * FROM word_registry WHERE word LIKE '%love%'").fetchall()
for r in rows:
    print(dict(r))

print("\n=== wa_file_index: love ===")
rows = conn.execute("SELECT * FROM wa_file_index WHERE word LIKE '%love%'").fetchall()
for r in rows:
    print(dict(r))

print("\n=== mti_terms: love ===")
rows = conn.execute("SELECT * FROM mti_terms WHERE owning_word LIKE '%love%'").fetchall()
for r in rows:
    print(dict(r))

print("\n=== wa_term_inventory: love file_ids ===")
rows = conn.execute("""
    SELECT wti.*, wfi.word, wfi.registry_id
    FROM wa_term_inventory wti
    JOIN wa_file_index wfi ON wfi.id = wti.file_id
    WHERE wfi.word LIKE '%love%'
""").fetchall()
print(f"  {len(rows)} term_inventory rows")
for r in rows:
    print(dict(r))

conn.close()
