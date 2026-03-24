import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# Get the 37 empty fi rows with their word_registry details
rows = conn.execute("""
    SELECT fi.id AS fi_id, fi.word_registry_fk, fi.word AS fi_word, fi.filename,
           wr.phase1_status, wr.phase1_output_file, wr.strongs_list, wr.notes
    FROM wa_file_index fi
    LEFT JOIN wa_term_inventory ti ON ti.file_id = fi.id
    LEFT JOIN word_registry wr ON wr.id = fi.word_registry_fk
    GROUP BY fi.id
    HAVING COUNT(ti.id) = 0
    ORDER BY fi.id
""").fetchall()

print("%-6s  %-5s  %-22s  %-12s  %-45s  strongs  notes" % ("fi.id","wr_fk","word","status","phase1_output_file"))
print("-" * 160)
for r in rows:
    notes_short = (r["notes"] or "")[:50].replace("\n", " ")
    output = (r["phase1_output_file"] or "NULL")[:45]
    print("%-6s  %-5s  %-22s  %-12s  %-45s  %-8s  %s" % (
        r["fi_id"], r["word_registry_fk"], r["fi_word"], r["phase1_status"] or "NULL",
        output, "yes" if r["strongs_list"] else "NULL", notes_short))

conn.close()
