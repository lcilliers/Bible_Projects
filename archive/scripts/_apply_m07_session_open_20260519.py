"""M07 session-open: advance cluster.status + clear stale registry flag.

- cluster.status: 'Not started' -> 'Data - In Progress' (M07)
- word_registry.phase1_status: 'In Progress' -> 'Complete' (reg#146 shame —
  stale; last_automation_run='AUDITED' RUN-20260325 confirms registry
  Phase 1 completed)
"""
import sqlite3
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
conn = sqlite3.connect('database/bible_research.db')
cur = conn.cursor()

# Pre-checks
cur_cluster = cur.execute("SELECT status FROM cluster WHERE cluster_code='M07'").fetchone()
print(f"M07 pre: cluster.status={cur_cluster[0]!r}")
assert cur_cluster[0] == 'Not started', f"Expected 'Not started', got {cur_cluster[0]!r}"

cur_reg = cur.execute(
    "SELECT phase1_status, last_automation_run, verse_context_status FROM word_registry WHERE id=146"
).fetchone()
print(f"reg#146 (shame) pre: phase1_status={cur_reg[0]!r} last_automation_run={cur_reg[1]!r} vc_status={cur_reg[2]!r}")
assert cur_reg[0] == 'In Progress'
assert cur_reg[1] == 'AUDITED'
assert cur_reg[2] == 'Complete'

cur.execute('BEGIN')
try:
    # Op 1 — advance M07 cluster status
    cur.execute(
        "UPDATE cluster SET status='Data - In Progress', last_updated_date=? "
        "WHERE cluster_code='M07' AND status='Not started'",
        (NOW,),
    )
    assert cur.rowcount == 1, f"cluster UPDATE affected {cur.rowcount} rows"

    # Op 2 — clear stale reg#146 phase1_status flag
    cur.execute(
        "UPDATE word_registry SET phase1_status='Complete' "
        "WHERE id=146 AND phase1_status='In Progress' "
        "AND last_automation_run='AUDITED' AND verse_context_status='Complete'",
    )
    assert cur.rowcount == 1, f"reg#146 UPDATE affected {cur.rowcount} rows"

    conn.commit()
    print("Both ops committed.")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# Post-verify
post_cluster = cur.execute("SELECT status, last_updated_date FROM cluster WHERE cluster_code='M07'").fetchone()
print(f"M07 post: cluster.status={post_cluster[0]!r} last_updated={post_cluster[1]!r}")
post_reg = cur.execute("SELECT phase1_status FROM word_registry WHERE id=146").fetchone()
print(f"reg#146 (shame) post: phase1_status={post_reg[0]!r}")

assert post_cluster[0] == 'Data - In Progress'
assert post_reg[0] == 'Complete'
print()
print("=== M07 session-open complete; ready for Phase 1 UT review ===")
conn.close()
