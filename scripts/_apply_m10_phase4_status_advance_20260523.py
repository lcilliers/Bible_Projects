"""M10 Phase 4 — status advance only (zero TRANSFERS, 6 BOUNDARY at Phase 3).

Per directive wa-cluster-M10-dir-001-phase4-status-advance-v1-20260523.md.

57/63 terms STAYS (13 with cross-register flag) + 6 BOUNDARY (recorded at
Phase 3 as cluster_observation rows). No mti_terms.cluster_code changes
required. Only cluster.status transitions from 'Data - In Progress' to
'Analysis - In Progress'.
"""
import sys, io, sqlite3
from datetime import datetime, timezone
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
conn = sqlite3.connect('database/bible_research.db')
cur = conn.cursor()

print('=== PRE ===')
r = cur.execute("SELECT status FROM cluster WHERE cluster_code='M10'").fetchone()
print(f'  cluster.M10.status: {r[0]!r}')
assert r[0] == 'Data - In Progress'
n_terms = cur.execute(
    "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M10' AND COALESCE(delete_flagged,0)=0"
).fetchone()[0]
print(f'  M10 active terms: {n_terms}')
assert n_terms == 63

print()
print('=== APPLY ===')
cur.execute('BEGIN')
try:
    cur.execute(
        "UPDATE cluster SET status='Analysis - In Progress', last_updated_date=? "
        "WHERE cluster_code='M10' AND status='Data - In Progress'",
        (NOW,),
    )
    assert cur.rowcount == 1
    conn.commit()
    print(f'  Committed at {NOW}')
except Exception:
    conn.rollback()
    print('ROLLED BACK')
    raise

print()
print('=== POST ===')
r = cur.execute(
    "SELECT status, last_updated_date FROM cluster WHERE cluster_code='M10'"
).fetchone()
print(f'  cluster.M10.status: {r[0]!r} last_updated={r[1]}')
assert r[0] == 'Analysis - In Progress'
n_terms_post = cur.execute(
    "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M10' AND COALESCE(delete_flagged,0)=0"
).fetchone()[0]
print(f'  M10 active terms (post): {n_terms_post}')
assert n_terms_post == 63

print()
print('=== M10 PHASE 4 COMPLETE ===')
print('- 0 term transfers (57 STAYS + 6 BOUNDARY at Phase 3)')
print('- 6 BOUNDARY observations recorded for Phase 8.5 resolution')
print('- 13 cross-register flags travel narratively to Phase 5/7')
print('- Cluster status: Analysis - In Progress')
print('Ready for Phase 5 — Sub-group formation (v2_8 §8; characteristic-driven).')
conn.close()
