"""M05 status fix: mark 'Analysis Completed (Terms Added)' to reflect the 2026-05-19 M07→M05 transfer.

Per researcher decision 2026-05-21 (Option A from the M05 audit summary).

Operations:
- Op A: UPDATE cluster.status = 'Analysis Completed (Terms Added)' (was 'Analysis Completed')
        + last_updated_date = 2026-05-19T13:00:00Z (the transfer date)
- Op B: INSERT cluster_observation row recording the cha.sad + che.sed event
        (audit trail; will be picked up by future audits as a documented integration note)

Does NOT route the orphaned 165 verses — that's deferred to a full M05 retrofit session.
"""
import sys, io, sqlite3
from datetime import datetime, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
TRANSFER_DATE = '2026-05-19T13:00:00Z'  # approximate; matches the M07 Phase 4 apply
SOURCE = 'wa-cluster-M05-audit-summary-v1-20260521.md (researcher Option A 2026-05-21); reflects M07 dir-001 transfer 2026-05-19'

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print('=== PRE-CHECKS ===')
r = cur.execute("SELECT status, last_updated_date FROM cluster WHERE cluster_code='M05'").fetchone()
print(f"  M05 status (pre): {r['status']!r}")
print(f"  M05 last_updated (pre): {r['last_updated_date']!r}")
assert r['status'] == 'Analysis Completed', f'Pre-check fail: expected Analysis Completed, got {r["status"]!r}'

# Confirm the two transferred terms are in M05
for mid, label in [(338, 'H2616B cha.sad'), (1633, 'H2617B che.sed')]:
    row = cur.execute('SELECT cluster_code, strongs_number, transliteration FROM mti_terms WHERE id=?', (mid,)).fetchone()
    assert row['cluster_code'] == 'M05', f'mti_id={mid} not in M05'
    print(f"  Confirmed mti_id={mid}: {row['strongs_number']} {row['transliteration']} in M05")

# Confirm no existing cluster_observation about this transfer
n_existing = cur.execute("""
    SELECT COUNT(*) FROM cluster_observation
    WHERE cluster_code='M05' AND title LIKE '%che.sed%transfer%' AND COALESCE(delete_flagged,0)=0
""").fetchone()[0]
print(f"  Existing M05 transfer observations: {n_existing}")

print()
print('=== APPLYING ===')
cur.execute('BEGIN')
try:
    # Op A — status + last_updated
    cur.execute(
        "UPDATE cluster SET status='Analysis Completed (Terms Added)', last_updated_date=? "
        "WHERE cluster_code='M05' AND status='Analysis Completed'",
        (TRANSFER_DATE,),
    )
    assert cur.rowcount == 1
    print(f"  Op A: cluster.M05.status → 'Analysis Completed (Terms Added)', last_updated={TRANSFER_DATE}")

    # Op B — cluster_observation row
    description = (
        "M07 Phase 4 (dir-001-term-transfer, 2026-05-19) transferred 2 terms from M07 to M05 as "
        "accidental-placement corrections: H2616B cha.sad (mti_id=338, 3 is_relevant vc) and "
        "H2617B che.sed (mti_id=1633, 162 is_relevant vc). Pass A analysis on these terms shows "
        "steadfast-love / loyal-faithfulness register (M05 territory), not shame (M07 territory). "
        "The transfer changed mti_terms.cluster_code but did NOT route the 165 verses through M05's "
        "sub-group structure — they remain orphaned (no mti_term_subgroup link) on inherited registry "
        "VCGs (338-001, 1633-001/002/003). cluster.M05.status was not updated to reflect the post-closure "
        "addition until the 2026-05-21 audit. STATUS-SUFFIX corrected via this directive. STRUCTURAL "
        "ROUTING DEFERRED — to be handled in a future M05 retrofit session (researcher Option A "
        "selected 2026-05-21; full Option C retrofit anticipated as part of a batch retrofit of "
        "early-closure clusters M01/M03/M05/M06/M39/M46). Source: WA-M05-audit-against-v25-v1-20260521.md."
    )
    cur.execute(
        "INSERT INTO cluster_observation (cluster_code, characteristic_id, cluster_subgroup_id, "
        " source_phase, observation_type, target_phase, title, description, status, "
        " raised_date, source_file, created_at, last_updated_date) "
        "VALUES (?, NULL, NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        ('M05', 'post_closure', 'INTEGRATION_NOTE', 'm05_retrofit',
         'Post-closure terms added: H2616B cha.sad + H2617B che.sed transferred from M07 (2026-05-19)',
         description, 'open', NOW, SOURCE, NOW, NOW),
    )
    print(f"  Op B: cluster_observation INTEGRATION_NOTE inserted (id={cur.lastrowid})")

    conn.commit()
    print(f"  Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

print()
print('=== POST-CHECKS ===')
r = cur.execute("SELECT status, last_updated_date FROM cluster WHERE cluster_code='M05'").fetchone()
print(f"  M05 status (post): {r['status']!r}")
print(f"  M05 last_updated (post): {r['last_updated_date']!r}")
assert r['status'] == 'Analysis Completed (Terms Added)'

n_obs = cur.execute("SELECT COUNT(*) FROM cluster_observation WHERE cluster_code='M05' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"  M05 cluster_observation rows: {n_obs}")

print()
print('=== M05 STATUS FIX COMPLETE (Option A) ===')
print(f"- cluster.M05.status → 'Analysis Completed (Terms Added)'")
print(f"- cluster_observation INTEGRATION_NOTE created (post-closure terms record)")
print(f"- STRUCTURAL ROUTING OF 165 ORPHANED VERSES NOT DONE (deferred to retrofit)")
conn.close()
