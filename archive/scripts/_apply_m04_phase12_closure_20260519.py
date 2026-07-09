"""M04 Phase 12 closure — apply directive WA-M04-dir-006.

Op B: UPDATE cluster.status='Analysis Completed' for M04.
"""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

conn = sqlite3.connect(DB)
cur = conn.cursor()

current = cur.execute(
    "SELECT cluster_code, status, version, last_updated_date FROM cluster WHERE cluster_code='M04'"
).fetchone()
print(f"M04 pre-update: status={current[1]!r} version={current[2]!r} last_updated={current[3]!r}")

if current[1] != 'Analysis - In Progress':
    raise SystemExit(
        f"FAIL: expected status='Analysis - In Progress', got {current[1]!r}. "
        f"Closure directive cannot proceed."
    )

cur.execute('BEGIN')
try:
    cur.execute(
        "UPDATE cluster SET status='Analysis Completed', last_updated_date=? "
        "WHERE cluster_code='M04' AND status='Analysis - In Progress'",
        (NOW,),
    )
    rows_affected = cur.rowcount
    if rows_affected != 1:
        raise RuntimeError(f"Expected 1 row affected, got {rows_affected}")
    conn.commit()
    print(f"Op B committed: {rows_affected} row updated.")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# Post-verify
post = cur.execute(
    "SELECT status, last_updated_date FROM cluster WHERE cluster_code='M04'"
).fetchone()
print(f"M04 post-update: status={post[0]!r} last_updated={post[1]!r}")
assert post[0] == 'Analysis Completed', "Status assertion failed"
assert post[1] == NOW, "Timestamp assertion failed"
print()
print("=== M04 Phase 12 CLOSURE COMPLETE ===")
print("Cluster status: Analysis Completed")
print("Ready for Session C cluster publication.")
conn.close()
