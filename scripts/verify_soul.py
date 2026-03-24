"""Quick post-audit verification for soul (registry 182)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()
r = conn.execute(
    "SELECT no, word, phase1_status, phase1_term_count, phase1_verse_count, "
    "last_automation_run, automation_run_id FROM word_registry WHERE no=182"
).fetchone()
print(f"last_automation_run : {r['last_automation_run']}")
print(f"automation_run_id   : {r['automation_run_id']}")
print(f"phase1_status       : {r['phase1_status']}")
print(f"term_count          : {r['phase1_term_count']}")
print(f"verse_count         : {r['phase1_verse_count']}")

w = conn.execute(
    "SELECT approved_by FROM word_run_state WHERE registry_id='182' ORDER BY id DESC LIMIT 1"
).fetchone()
print(f"approved_by         : {w['approved_by'] if w else 'NOT FOUND'}")

mti = conn.execute(
    "SELECT COUNT(*) AS c FROM mti_terms WHERE owning_registry='182'"
).fetchone()
print(f"mti_terms count     : {mti['c']}")

df = conn.execute(
    "SELECT COUNT(*) AS c FROM wa_term_inventory WHERE file_id=36 AND delete_flagged=1"
).fetchone()
print(f"delete_flagged terms: {df['c']}")

vtl = conn.execute(
    "SELECT COUNT(*) AS c FROM wa_verse_term_links vtl "
    "JOIN wa_verse_records vr ON vr.id=vtl.verse_id WHERE vr.file_id=36"
).fetchone()
print(f"vtl rows            : {vtl['c']}")

qf = conn.execute(
    "SELECT COUNT(*) AS c FROM wa_data_quality_flags WHERE file_id=36"
).fetchone()
print(f"quality flags       : {qf['c']}")
