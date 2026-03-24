import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

# fi.id rows to KEEP (backlog words with strongs_list, awaiting new-word import)
KEEP = {73, 145, 169, 176}  # consciousness, meekness, resolve, sensuality

# Identify the 33 to delete (empty fi rows minus the 4 kept)
delete_ids = [r[0] for r in conn.execute("""
    SELECT fi.id FROM wa_file_index fi
    LEFT JOIN wa_term_inventory ti ON ti.file_id = fi.id
    GROUP BY fi.id HAVING COUNT(ti.id) = 0
""").fetchall() if r[0] not in KEEP]

print("fi rows to delete (%d): %s" % (len(delete_ids), delete_ids))
print()

ph = ",".join("?" * len(delete_ids))

# Show what we are about to delete
words = conn.execute(
    "SELECT id, word, word_registry_fk FROM wa_file_index WHERE id IN (%s) ORDER BY id" % ph,
    delete_ids
).fetchall()
print("%-6s  %-5s  word" % ("fi.id", "wr_fk"))
for r in words:
    print("  %-6s  %-5s  %s" % (r[0], r[2], r[1]))
print()

# Before counts
dqf_before = conn.execute("SELECT COUNT(*) FROM wa_data_quality_flags WHERE file_id IN (%s)" % ph, delete_ids).fetchone()[0]
fi_before  = conn.execute("SELECT COUNT(*) FROM wa_file_index WHERE id IN (%s)" % ph, delete_ids).fetchone()[0]
print("Before: wa_data_quality_flags=%d  wa_file_index=%d" % (dqf_before, fi_before))

# Step 1: delete quality flags for these file_ids
conn.execute("DELETE FROM wa_data_quality_flags WHERE file_id IN (%s)" % ph, delete_ids)

# Step 2: delete the file_index rows
conn.execute("DELETE FROM wa_file_index WHERE id IN (%s)" % ph, delete_ids)

conn.commit()

# After counts
dqf_after = conn.execute("SELECT COUNT(*) FROM wa_data_quality_flags WHERE file_id IN (%s)" % ph, delete_ids).fetchone()[0]
fi_after  = conn.execute("SELECT COUNT(*) FROM wa_file_index WHERE id IN (%s)" % ph, delete_ids).fetchone()[0]
print("After : wa_data_quality_flags=%d  wa_file_index=%d" % (dqf_after, fi_after))
print()

# Confirm kept rows still present
kept = conn.execute("SELECT id, word, word_registry_fk FROM wa_file_index WHERE id IN (73,145,169,176) ORDER BY id").fetchall()
print("Kept file_index rows (%d):" % len(kept))
for r in kept:
    print("  fi.id=%-4s  wr_fk=%-4s  word=%s" % (r[0], r[2], r[1]))

# Final totals
fi_total = conn.execute("SELECT COUNT(*) FROM wa_file_index").fetchone()[0]
ti_total = conn.execute("SELECT COUNT(*) FROM wa_term_inventory").fetchone()[0]
print()
print("wa_file_index total now : %d" % fi_total)
print("wa_term_inventory total : %d" % ti_total)

conn.close()
print()
print("Done.")
