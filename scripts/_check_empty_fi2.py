import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

UNCLEAR_FI = [73, 145, 169, 176]   # consciousness, meekness, resolve, sensuality

# 1. Full word_registry details for the 4 unclear words
print("=== Unclear words — full word_registry record ===")
rows = conn.execute("""
    SELECT wr.id, wr.no, wr.word, wr.phase1_status, wr.source_list,
           wr.phase1_output_file, wr.strongs_list, wr.notes
    FROM wa_file_index fi
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    WHERE fi.id IN (73, 145, 169, 176)
    ORDER BY fi.id
""").fetchall()
for r in rows:
    print("  wr.id=%-4s  no=%-4s  word=%-20s  status=%-12s  source=%s" % (r[0], r[1], r[2], r[3], r[4]))
    print("    phase1_output_file : %s" % r[5])
    print("    strongs_list       : %s" % (r[6][:120] if r[6] else "NULL"))
    print("    notes              : %s" % (r[7] or "NULL"))
    print()

# 2. Dependency check for ALL 37 empty fi rows
print("=== Dependency check for all 37 empty file_index rows ===")

# Get all empty fi ids
empty_fi_ids = [r[0] for r in conn.execute("""
    SELECT fi.id FROM wa_file_index fi
    LEFT JOIN wa_term_inventory ti ON ti.file_id = fi.id
    GROUP BY fi.id HAVING COUNT(ti.id) = 0
""").fetchall()]

dep_tables = [
    ("wa_term_inventory",       "file_id"),
    ("wa_verse_records",        "file_id"),
    ("wa_cross_registry_links", "file_id"),
    ("wa_data_quality_flags",   "file_id"),
]

ph = ",".join("?" * len(empty_fi_ids))
print("Checking %d file_index ids: %s" % (len(empty_fi_ids), empty_fi_ids))
print()

any_deps = False
for table, col in dep_tables:
    rows = conn.execute(
        "SELECT %s, COUNT(*) cnt FROM %s WHERE %s IN (%s) GROUP BY %s ORDER BY %s" % (col, table, col, ph, col, col),
        empty_fi_ids
    ).fetchall()
    if rows:
        any_deps = True
        print("  %s has rows for these file_ids:" % table)
        for r in rows:
            print("    file_id=%-4s  count=%s" % (r[0], r[1]))
    else:
        print("  %s : 0 rows" % table)

if not any_deps:
    print()
    print("No dependencies found — all 37 rows are safe to delete.")

conn.close()
