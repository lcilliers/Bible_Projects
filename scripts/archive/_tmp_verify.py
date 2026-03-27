#!/usr/bin/env python3
import sqlite3
conn = sqlite3.connect("data/bible_research.db")
conn.row_factory = sqlite3.Row
FILE_ID = 36
REG_NO  = 182

print("=== VERIFICATION ===\n")
for code in ["H4578","H5397","G5590"]:
    ti  = conn.execute("SELECT id FROM wa_term_inventory WHERE strongs_number=?", (code,)).fetchone()
    mti = conn.execute("SELECT id FROM mti_terms WHERE strongs_number=?", (code,)).fetchone()
    ti_s  = "GONE" if not ti  else str(ti[0])
    mti_s = "GONE" if not mti else str(mti[0])
    print(f"{code}: wa_term_inventory={ti_s}  mti_terms={mti_s}")

print()
active  = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE file_id=? AND delete_flagged=0", (FILE_ID,)).fetchone()[0]
flagged = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE file_id=? AND delete_flagged=1", (FILE_ID,)).fetchone()[0]
total   = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE file_id=?", (FILE_ID,)).fetchone()[0]
print(f"wa_term_inventory file_id=36: total={total}  active={active}  delete_flagged={flagged}")

mti_total = conn.execute("SELECT COUNT(*) FROM mti_terms WHERE owning_registry_fk=?", (REG_NO,)).fetchone()[0]
print(f"mti_terms owning_registry_fk=182: count={mti_total}")

verses = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE file_id=? AND delete_flagged=0", (FILE_ID,)).fetchone()[0]
vtl    = conn.execute(
    "SELECT COUNT(*) FROM wa_verse_term_links vtl "
    "JOIN wa_term_inventory ti ON ti.id=vtl.term_inv_id WHERE ti.file_id=?", (FILE_ID,)
).fetchone()[0]
print(f"Verses active={verses}  VTL rows={vtl}")

wr = conn.execute(
    "SELECT phase1_term_count, phase1_verse_count, last_automation_run FROM word_registry WHERE no=?",
    (REG_NO,)
).fetchone()
print(f"word_registry: phase1_term_count={wr[0]}  phase1_verse_count={wr[1]}  last_automation_run={wr[2]}")

conn.close()
print("\nDone.")
