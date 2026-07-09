"""M08 Phase 4 — term transfers + status advance.

Op A: UPDATE mti_terms.cluster_code 'M08' -> destination for the 3 transfers:
  - id=3081 G0830 authairetos -> M29
  - id=4335 H1984I ha.lal     -> M16
  - id=1312 H7989 shal.lit    -> M23

Op N: UPDATE cluster.status 'Data - In Progress' -> 'Analysis - In Progress'
      for M08.

Per directive WA-M08-dir-001-term-transfer-v1-20260520.md.
BOUNDARY G0193 akrates (mti_id=1113) has no Phase 4 write.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

# (mti_id, strongs, translit, destination_cluster)
TRANSFERS = [
    (3081, 'G0830', 'authairetos', 'M29'),
    (4335, 'H1984I', 'ha.lal',     'M16'),
    (1312, 'H7989', 'shal.lit',    'M23'),
]

conn = sqlite3.connect(DB)
cur = conn.cursor()

# Pre-checks
print("=== PRE-CHECKS ===")
for mti_id, strongs, translit, dest in TRANSFERS:
    r = cur.execute(
        "SELECT cluster_code, COALESCE(delete_flagged,0) FROM mti_terms WHERE id=?",
        (mti_id,),
    ).fetchone()
    if not r or r[0] != 'M08' or r[1] != 0:
        raise SystemExit(f"FAIL: mti_id={mti_id} ({strongs}) expected cluster_code='M08', delete_flagged=0; got {r}")
    print(f"  mti_id={mti_id} {strongs} {translit}: cluster_code='M08' OK (target {dest})")

cluster_pre = cur.execute("SELECT status FROM cluster WHERE cluster_code='M08'").fetchone()
print(f"  cluster.M08.status = {cluster_pre[0]!r}")
if cluster_pre[0] != 'Data - In Progress':
    raise SystemExit(f"FAIL: expected cluster.M08.status='Data - In Progress', got {cluster_pre[0]!r}")

# Counts pre
counts_pre = {}
for cc in ('M08','M16','M23','M29'):
    counts_pre[cc] = cur.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (cc,),
    ).fetchone()[0]
    print(f"  {cc} term count (pre): {counts_pre[cc]}")

# Apply
print()
print("=== APPLYING ===")
cur.execute('BEGIN')
try:
    n_total = 0
    for mti_id, strongs, translit, dest in TRANSFERS:
        cur.execute(
            "UPDATE mti_terms SET cluster_code=?, last_changed=? "
            "WHERE id=? AND cluster_code='M08' AND COALESCE(delete_flagged,0)=0",
            (dest, NOW, mti_id),
        )
        if cur.rowcount != 1:
            raise RuntimeError(f"Op A: expected 1 row for mti_id={mti_id}, got {cur.rowcount}")
        print(f"  Op A: mti_id={mti_id} {strongs} {translit} -> {dest}")
        n_total += cur.rowcount
    if n_total != 3:
        raise RuntimeError(f"Op A total: expected 3, got {n_total}")

    # Op N
    cur.execute(
        "UPDATE cluster SET status='Analysis - In Progress', last_updated_date=? "
        "WHERE cluster_code='M08' AND status='Data - In Progress'",
        (NOW,),
    )
    n_status = cur.rowcount
    if n_status != 1:
        raise RuntimeError(f"Op N: expected 1 row, got {n_status}")
    print(f"  Op N: cluster.M08.status -> 'Analysis - In Progress'")

    conn.commit()
    print(f"  Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# Post-checks
print()
print("=== POST-CHECKS ===")
for mti_id, strongs, translit, dest in TRANSFERS:
    r = cur.execute(
        "SELECT cluster_code FROM mti_terms WHERE id=?",
        (mti_id,),
    ).fetchone()
    print(f"  mti_id={mti_id} {strongs} {translit}: cluster_code={r[0]!r} (expected {dest!r})")
    assert r[0] == dest

cluster_post = cur.execute("SELECT status FROM cluster WHERE cluster_code='M08'").fetchone()[0]
print(f"  cluster.M08.status = {cluster_post!r}")
assert cluster_post == 'Analysis - In Progress'

# Counts post
deltas = {'M08': -3, 'M16': +1, 'M23': +1, 'M29': +1}
for cc in ('M08','M16','M23','M29'):
    n = cur.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (cc,),
    ).fetchone()[0]
    expected = counts_pre[cc] + deltas[cc]
    print(f"  {cc} term count (post): {n} (expected {expected})")
    assert n == expected, f"{cc} post-count mismatch"

print()
print("=== M08 PHASE 4 COMPLETE ===")
print("- 3 terms transferred: G0830->M29, H1984I->M16, H7989->M23")
print("- 18 STAYS-with-cross-register-flag terms remain in M08 (carried forward via verdict doc)")
print("- 1 BOUNDARY (G0193 akrates) remains in M08 (resolved at Phase 5/6 + 8.5)")
print("- Cluster status: Analysis - In Progress")
print("Ready for Phase 5 — Sub-group formation (v2_8 §8; characteristic-driven).")
conn.close()
