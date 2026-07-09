"""Apply DIR-20260513-004 — M20 status bump Data - In Progress → Analysis - In Progress.

Remediation of dir-003 omission. Backup → dry-run → live.
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
DIRECTIVE_ID = "DIR-20260513-004"
CLUSTER = "M20"
PRE_STATUS = "Data - In Progress"
NEW_STATUS = "Analysis - In Progress"

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true")
args = ap.parse_args()

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs("backups/row_backups", exist_ok=True)
backup_path = os.path.join(
    "backups/row_backups",
    f"cluster_{CLUSTER}_pre_status_bump_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

before = dict(conn.execute(
    "SELECT * FROM cluster WHERE cluster_code=?", (CLUSTER,)
).fetchone())
print(f"DIRECTIVE: {DIRECTIVE_ID}")
print(f"BEFORE: status={before['status']!r}  last_updated={before['last_updated_date']!r}")

with open(backup_path, "w", encoding="utf-8") as f:
    json.dump({"directive_id": DIRECTIVE_ID, "timestamp": now_utc, "row": before},
              f, indent=2, ensure_ascii=False)
print(f"Backup → {backup_path}")

if before["status"] != PRE_STATUS:
    if before["status"] == NEW_STATUS:
        print(f"\nNoop: status already {NEW_STATUS!r}")
        sys.exit(0)
    raise SystemExit(f"Pre-check fail: expected {PRE_STATUS!r}, got {before['status']!r}")

print(f"\nProposed: status {PRE_STATUS!r} → {NEW_STATUS!r}")
print(f"          last_updated_date → {now_utc}")

if not args.live:
    print("\n[DRY-RUN] no changes. Re-run with --live.")
    sys.exit(0)

conn.execute(
    "UPDATE cluster SET status=?, last_updated_date=? "
    "WHERE cluster_code=? AND status=?",
    (NEW_STATUS, now_utc, CLUSTER, PRE_STATUS)
)
changed = conn.total_changes
conn.commit()

after = dict(conn.execute(
    "SELECT cluster_code, status, last_updated_date FROM cluster WHERE cluster_code=?",
    (CLUSTER,)
).fetchone())
print(f"\nAFTER (rows changed: {changed}):")
print(f"  cluster_code={after['cluster_code']}  status={after['status']!r}  last_updated={after['last_updated_date']}")

if changed != 1:
    raise SystemExit(f"Unexpected row count: {changed} (expected 1)")
if after["status"] != NEW_STATUS:
    raise SystemExit("Post-state mismatch")

# Untouched-table check: 4 Analysis Completed clusters still 4
ac = conn.execute("SELECT COUNT(*) FROM cluster WHERE status='Analysis Completed'").fetchone()[0]
print(f"\nUntouched-table check: 'Analysis Completed' count = {ac} (expected 4)")
if ac != 4:
    raise SystemExit("Untouched-table check failed")

print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
conn.close()
