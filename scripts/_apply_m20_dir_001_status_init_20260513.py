"""Apply DIR-20260513-M20-001 — M20 status-init.

Per wa-sessionb-cluster-instruction-v1_4 §4.1. Transitions M20 from
'Not started' to 'Data - In Progress'.

Backup → dry-run → live (with --live).
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
CLUSTER = "M20"
NEW_STATUS = "Data - In Progress"
PRE_STATUS = "Not started"
DIRECTIVE_ID = "DIR-20260513-M20-001"

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true")
args = ap.parse_args()

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs("backups/row_backups", exist_ok=True)
backup_path = os.path.join(
    "backups/row_backups",
    f"cluster_{CLUSTER}_pre_status_init_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

before = dict(conn.execute(
    "SELECT * FROM cluster WHERE cluster_code = ?", (CLUSTER,)
).fetchone())
print("BEFORE:")
for k in ("cluster_code","status","version","bucket","last_updated_date"):
    print(f"  {k:25s} = {before[k]!r}")

with open(backup_path, "w", encoding="utf-8") as f:
    json.dump({"directive_id": DIRECTIVE_ID, "timestamp": now_utc, "row": before},
              f, indent=2, ensure_ascii=False)
print(f"\nBackup → {backup_path}")

# Pre-check: status must be 'Not started'
if before["status"] != PRE_STATUS:
    if before["status"] == NEW_STATUS:
        print(f"\nNoop: status already {NEW_STATUS!r}.")
        sys.exit(0)
    raise SystemExit(
        f"Pre-check failed: expected status={PRE_STATUS!r}, found {before['status']!r}. "
        f"Refusing to apply."
    )

print(f"\nProposed UPDATE:")
print(f"  status:            {before['status']!r}  →  {NEW_STATUS!r}")
print(f"  last_updated_date: {before['last_updated_date']!r}  →  {now_utc!r}")

if not args.live:
    print("\n[DRY-RUN] no changes. Re-run with --live.")
    sys.exit(0)

# Apply
conn.execute(
    "UPDATE cluster SET status=?, last_updated_date=? "
    "WHERE cluster_code=? AND status=?",
    (NEW_STATUS, now_utc, CLUSTER, PRE_STATUS)
)
changed = conn.total_changes
conn.commit()

# COMPLETION CONFIRMATION
after = dict(conn.execute(
    "SELECT cluster_code, status, last_updated_date FROM cluster WHERE cluster_code=?",
    (CLUSTER,)
).fetchone())
completed_count = conn.execute(
    "SELECT COUNT(*) FROM cluster WHERE status='Analysis Completed'"
).fetchone()[0]

print(f"\nAFTER (rows changed: {changed}):")
for k in ("cluster_code","status","last_updated_date"):
    print(f"  {k:25s} = {after[k]!r}")
print(f"\nUntouched-table check:")
print(f"  cluster.status='Analysis Completed' count: {completed_count}  (expected: 4)")

if changed != 1:
    raise SystemExit(f"Unexpected row count: {changed} (expected 1)")
if after["status"] != NEW_STATUS:
    raise SystemExit(f"Post-state mismatch")
if completed_count != 4:
    raise SystemExit(f"Untouched-table check failed")

print(f"\n[LIVE] DIR-20260513-M20-001 applied successfully.")
conn.close()
