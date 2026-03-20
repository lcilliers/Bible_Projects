"""
One-off: reset word_registry.phase1_status for all 170 'In Progress' words.

Rules (per researcher instruction):
  - Words with wa_file_index data (fi >= 1)         -> 'Complete'
  - Words with no data but have xref/mti records    -> 'Complete'
  - Words with no data AND no xref/mti at all       -> 'Excluded'
"""
import sqlite3

DB = "../data/bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")

# ── Identify the three groups ─────────────────────────────────────────────────
all_ip = conn.execute(
    "SELECT id FROM word_registry WHERE phase1_status = 'In Progress'"
).fetchall()
ip_ids = [r["id"] for r in all_ip]

complete_ids = []
excluded_ids = []

for wid in ip_ids:
    fi = conn.execute(
        "SELECT COUNT(*) FROM wa_file_index WHERE word_registry_fk = ?", (wid,)
    ).fetchone()[0]
    ti = conn.execute(
        "SELECT COUNT(*) FROM wa_term_inventory ti"
        " JOIN wa_file_index fi ON fi.id = ti.file_id"
        " WHERE fi.word_registry_fk = ?", (wid,)
    ).fetchone()[0]
    xref = conn.execute(
        "SELECT COUNT(*) FROM mti_term_cross_refs WHERE registry = ?", (str(wid),)
    ).fetchone()[0]
    mti = conn.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE owning_registry = ?", (str(wid),)
    ).fetchone()[0]

    if fi > 0 or ti > 0 or xref > 0 or mti > 0:
        complete_ids.append(wid)
    else:
        excluded_ids.append(wid)

print("In Progress breakdown:")
print("  -> Complete:  %d" % len(complete_ids))
print("  -> Excluded:  %d" % len(excluded_ids))
print("  Total:        %d (expected 170)" % (len(complete_ids) + len(excluded_ids)))

# ── Apply UPDATEs ─────────────────────────────────────────────────────────────
if complete_ids:
    conn.execute(
        "UPDATE word_registry SET phase1_status = 'Complete'"
        " WHERE id IN (%s)" % ",".join("?" * len(complete_ids)),
        complete_ids
    )

if excluded_ids:
    conn.execute(
        "UPDATE word_registry SET phase1_status = 'Excluded'"
        " WHERE id IN (%s)" % ",".join("?" * len(excluded_ids)),
        excluded_ids
    )

conn.commit()

# ── Verify ────────────────────────────────────────────────────────────────────
print("\nword_registry phase1_status after update:")
for r in conn.execute(
    "SELECT phase1_status, COUNT(*) AS cnt FROM word_registry"
    " GROUP BY phase1_status ORDER BY cnt DESC"
).fetchall():
    print("  %-16s  %d" % (str(r["phase1_status"]), r["cnt"]))

# Confirm no In Progress remain
remaining = conn.execute(
    "SELECT COUNT(*) FROM word_registry WHERE phase1_status = 'In Progress'"
).fetchone()[0]
print("\n  'In Progress' remaining: %d  %s" % (remaining, "OK" if remaining == 0 else "!! PROBLEM"))

# List the Excluded words for the record
print("\nExcluded words (%d):" % len(excluded_ids))
ex_rows = conn.execute(
    "SELECT id, word FROM word_registry WHERE phase1_status = 'Excluded' ORDER BY id"
).fetchall()
for r in ex_rows:
    print("  id=%-4d  %s" % (r["id"], r["word"]))

conn.close()
