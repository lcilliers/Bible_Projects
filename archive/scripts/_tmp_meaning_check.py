import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analytics.db_client import get_connection

conn = get_connection()

print("=== wa_term_inventory meaning field population ===")
for col in ["meaning", "meaning_numbered", "lsj_entry"]:
    n = conn.execute(
        f"SELECT COUNT(*) FROM wa_term_inventory WHERE {col} IS NOT NULL AND TRIM({col}) != ''"
    ).fetchone()[0]
    print(f"  {col:30s}: {n} rows populated")

print()
print("=== Meaning tables row counts ===")
for tbl in ["wa_meaning_parsed", "wa_meaning_sense", "wa_meaning_stem", "wa_lsj_parsed"]:
    n = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
    print(f"  {tbl:30s}: {n}")

n = conn.execute(
    "SELECT COUNT(*) FROM wa_term_inventory WHERE parsed_meaning_id IS NOT NULL"
).fetchone()[0]
print(f"\n  parsed_meaning_id linked (wti):   {n}")

print()
print("=== Total terms in wa_term_inventory ===")
total = conn.execute("SELECT COUNT(*) FROM wa_term_inventory").fetchone()[0]
print(f"  Total terms: {total}")

print()
print("=== Terms: meaning col populated, NO wa_meaning_parsed link ===")
rows = conn.execute("""
    SELECT wti.id, wti.term_id, wti.strongs_number,
           SUBSTR(wti.meaning, 1, 70) AS snip,
           wti.parsed_meaning_id
    FROM wa_term_inventory wti
    WHERE (wti.meaning IS NOT NULL AND TRIM(wti.meaning) != '')
      AND wti.parsed_meaning_id IS NULL
    ORDER BY wti.id
    LIMIT 40
""").fetchall()
print(f"  Count: {len(rows)}")
for r in rows:
    print(f"  [{r[0]:4d}] {str(r[1]):12s} {str(r[2]):12s}  meaning='{r[3]}'")

print()
print("=== Terms: meaning col populated AND has wa_meaning_parsed link ===")
n2 = conn.execute("""
    SELECT COUNT(*) FROM wa_term_inventory wti
    WHERE (wti.meaning IS NOT NULL AND TRIM(wti.meaning) != '')
      AND wti.parsed_meaning_id IS NOT NULL
""").fetchone()[0]
print(f"  Count: {n2}")

print()
print("=== Terms: no meaning col, no parsed_meaning_id (true blanks) ===")
n3 = conn.execute("""
    SELECT COUNT(*) FROM wa_term_inventory wti
    WHERE (wti.meaning IS NULL OR TRIM(wti.meaning) = '')
      AND wti.parsed_meaning_id IS NULL
""").fetchone()[0]
n4 = conn.execute("""
    SELECT COUNT(*) FROM wa_term_inventory wti
    WHERE (wti.meaning IS NULL OR TRIM(wti.meaning) = '')
      AND wti.parsed_meaning_id IS NOT NULL
""").fetchone()[0]
print(f"  No meaning col, no link  : {n3}")
print(f"  No meaning col, has link : {n4}  (meaning is in separate tables only)")

print()
print("=== Distinct words with wa_meaning_parsed data ===")
rows2 = conn.execute("""
    SELECT wr.word, COUNT(DISTINCT wti.id) AS terms, COUNT(DISTINCT mp.id) AS parsed
    FROM word_registry wr
    JOIN wa_file_index wfi ON wfi.word_registry_fk = wr.id
    JOIN wa_term_inventory wti ON wti.file_id = wfi.id
    LEFT JOIN wa_meaning_parsed mp ON mp.term_inv_id = wti.id
    GROUP BY wr.id, wr.word
    HAVING parsed > 0
    ORDER BY wr.word
""").fetchall()
print(f"  Words with any meaning parsed data: {len(rows2)}")
for r in rows2:
    print(f"  {r[0]:25s}  terms={r[1]}  mp_rows={r[2]}")

conn.close()
