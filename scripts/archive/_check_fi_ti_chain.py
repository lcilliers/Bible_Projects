import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

fi_count = conn.execute("SELECT COUNT(*) FROM wa_file_index").fetchone()[0]
ti_count = conn.execute("SELECT COUNT(*) FROM wa_term_inventory").fetchone()[0]
print("wa_file_index rows    :", fi_count)
print("wa_term_inventory rows:", ti_count)
print()

# 1. wa_term_inventory rows with no parent in wa_file_index (orphaned terms)
orphan_ti = conn.execute("""
    SELECT ti.id, ti.file_id, ti.term_id, ti.strongs_number, ti.transliteration
    FROM wa_term_inventory ti
    LEFT JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE fi.id IS NULL
    ORDER BY ti.id
""").fetchall()
print("wa_term_inventory rows with NO wa_file_index parent:", len(orphan_ti))
for r in orphan_ti:
    print("  ti.id=%-4s  file_id=%-4s  term_id=%-10s  strongs=%-10s  translit=%s" % (
        r[0], r[1], r[2], r[3], r[4]))
print()

# 2. wa_file_index rows with NO wa_term_inventory entries
empty_fi = conn.execute("""
    SELECT fi.id, fi.registry_id, fi.word_registry_fk, fi.word, fi.filename,
           COUNT(ti.id) AS term_count
    FROM wa_file_index fi
    LEFT JOIN wa_term_inventory ti ON ti.file_id = fi.id
    GROUP BY fi.id
    HAVING term_count = 0
    ORDER BY fi.id
""").fetchall()
print("wa_file_index rows with ZERO wa_term_inventory entries:", len(empty_fi))
for r in empty_fi:
    print("  fi.id=%-4s  registry_id=%-4s  word_registry_fk=%-4s  word=%-20s  file=%s" % (
        r[0], r[1], r[2], r[3], r[4]))
print()

# 3. Summary: term counts per file (min/max/avg for health check)
stats = conn.execute("""
    SELECT MIN(cnt), MAX(cnt), AVG(cnt)
    FROM (
        SELECT fi.id, COUNT(ti.id) AS cnt
        FROM wa_file_index fi
        LEFT JOIN wa_term_inventory ti ON ti.file_id = fi.id
        GROUP BY fi.id
    )
""").fetchone()
print("Term count per file_index row — min=%s  max=%s  avg=%.1f" % (stats[0], stats[1], stats[2]))

conn.close()
