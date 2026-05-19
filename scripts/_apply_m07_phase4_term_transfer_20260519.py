"""M07 Phase 4 — term transfers + status advance.

Op A: UPDATE mti_terms.cluster_code 'M07' -> 'M05' for H2616B (id=338)
      and H2617B (id=1633).
Op N: UPDATE cluster.status 'Data - In Progress' -> 'Analysis - In Progress'
      for M07.

Per directive WA-M07-dir-001-term-transfer-v1-20260519.md.
"""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TRANSFERS = [
    (338, 'H2616B', 'cha.sad'),
    (1633, 'H2617B', 'che.sed'),
]

conn = sqlite3.connect(DB)
cur = conn.cursor()

# Pre-checks
print("=== PRE-CHECKS ===")
for mti_id, strongs, translit in TRANSFERS:
    r = cur.execute(
        "SELECT cluster_code, COALESCE(delete_flagged,0) FROM mti_terms WHERE id=?",
        (mti_id,),
    ).fetchone()
    if not r or r[0] != 'M07' or r[1] != 0:
        raise SystemExit(f"FAIL: mti_id={mti_id} ({strongs}) expected cluster_code='M07', delete_flagged=0; got {r}")
    print(f"  mti_id={mti_id} {strongs} {translit}: cluster_code='M07' OK")

cluster_pre = cur.execute("SELECT status FROM cluster WHERE cluster_code='M07'").fetchone()
print(f"  cluster.M07.status = {cluster_pre[0]!r}")
if cluster_pre[0] != 'Data - In Progress':
    raise SystemExit(f"FAIL: expected cluster.M07.status='Data - In Progress', got {cluster_pre[0]!r}")

# Counts pre
m07_pre = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
m05_pre = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M05' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"  M07 term count (pre): {m07_pre}")
print(f"  M05 term count (pre): {m05_pre}")

# Apply
print()
print("=== APPLYING ===")
cur.execute('BEGIN')
try:
    # Op A
    cur.execute(
        "UPDATE mti_terms SET cluster_code='M05', last_changed=? "
        "WHERE id IN (338, 1633) AND cluster_code='M07' AND COALESCE(delete_flagged,0)=0",
        (NOW,),
    )
    n_transferred = cur.rowcount
    if n_transferred != 2:
        raise RuntimeError(f"Op A: expected 2 rows, got {n_transferred}")
    print(f"  Op A: {n_transferred} mti_terms moved M07 -> M05")

    # Op N
    cur.execute(
        "UPDATE cluster SET status='Analysis - In Progress', last_updated_date=? "
        "WHERE cluster_code='M07' AND status='Data - In Progress'",
        (NOW,),
    )
    n_status = cur.rowcount
    if n_status != 1:
        raise RuntimeError(f"Op N: expected 1 row, got {n_status}")
    print(f"  Op N: cluster.M07.status -> 'Analysis - In Progress'")

    conn.commit()
    print(f"  Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# Post-checks
print()
print("=== POST-CHECKS ===")
for mti_id, strongs, translit in TRANSFERS:
    r = cur.execute(
        "SELECT cluster_code FROM mti_terms WHERE id=?",
        (mti_id,),
    ).fetchone()
    print(f"  mti_id={mti_id} {strongs} {translit}: cluster_code={r[0]!r}")
    assert r[0] == 'M05'

cluster_post = cur.execute("SELECT status FROM cluster WHERE cluster_code='M07'").fetchone()[0]
print(f"  cluster.M07.status = {cluster_post!r}")
assert cluster_post == 'Analysis - In Progress'

m07_post = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
m05_post = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M05' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"  M07 term count (post): {m07_post} (expected {m07_pre - 2})")
print(f"  M05 term count (post): {m05_post} (expected {m05_pre + 2})")
assert m07_post == m07_pre - 2
assert m05_post == m05_pre + 2

print()
print("=== M07 PHASE 4 COMPLETE ===")
print("- 2 terms transferred to M05 (chesed root family — accidental placement)")
print("- 8 cross-register flagged STAYS (carried forward via verdict doc)")
print("- 5 BOUNDARY terms remain in M07 (resolved at Phase 5/6 + 8.5)")
print("- Cluster status: Analysis - In Progress")
print("Ready for Phase 5 — Sub-group formation (v2_7 §8).")
conn.close()
