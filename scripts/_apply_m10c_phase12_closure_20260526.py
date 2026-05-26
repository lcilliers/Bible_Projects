"""M10c Phase 12 closure: advance cluster.status to 'Analysis Completed'.

Per v2_9 §15. Phase 11 validation passed 11/11 (see
Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase11-validation-v1-20260526.md).
"""
import sqlite3
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
conn = sqlite3.connect('database/bible_research.db')
cur = conn.cursor()

current = cur.execute("SELECT status, version FROM cluster WHERE cluster_code='M10c'").fetchone()
print(f"M10c pre: status={current[0]!r} version={current[1]!r}")
assert current[0] == 'Analysis - In Progress', f"Expected 'Analysis - In Progress', got {current[0]!r}"

cur.execute('BEGIN')
try:
    cur.execute(
        "UPDATE cluster SET status='Analysis Completed', last_updated_date=? "
        "WHERE cluster_code='M10c' AND status='Analysis - In Progress'",
        (NOW,),
    )
    assert cur.rowcount == 1
    conn.commit()
    print(f"Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

post = cur.execute("SELECT status, last_updated_date FROM cluster WHERE cluster_code='M10c'").fetchone()
print(f"M10c post: status={post[0]!r} last_updated={post[1]!r}")
assert post[0] == 'Analysis Completed'

print()
print("=== M10c PHASE 12 CLOSURE COMPLETE ===")
print("Cluster status: Analysis Completed")
print("Ready for Session C cluster publication.")
conn.close()
