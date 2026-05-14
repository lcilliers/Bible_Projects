"""Advance M15 cluster.status to 'Analysis Completed'. All Phase 10
gates passed in DIR-025 dry-run; this completes Step 4 (status flip)."""
import shutil, sqlite3, os, sys
from datetime import datetime, timezone

DB = "database/bible_research.db"
BK_DIR = "backups"

print("Backing up DB...")
os.makedirs(BK_DIR, exist_ok=True)
bk_path = os.path.join(BK_DIR, "bible_research_pre_m15_status_complete_20260512.db")
shutil.copy2(DB, bk_path)
print(f"  Backup: {bk_path}")

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

pre = conn.execute(
    "SELECT cluster_code, status, last_updated_date FROM cluster "
    "WHERE cluster_code='M15'").fetchone()
print(f"\nPre:  status={pre['status']!r}  last_updated={pre['last_updated_date']}")

conn.execute(
    "UPDATE cluster SET status=?, last_updated_date=? "
    " WHERE cluster_code='M15'",
    ("Analysis Completed", ts),
)
conn.commit()

post = conn.execute(
    "SELECT cluster_code, status, last_updated_date FROM cluster "
    "WHERE cluster_code='M15'").fetchone()
print(f"Post: status={post['status']!r}  last_updated={post['last_updated_date']}")
print("\nCOMMIT successful.")
conn.close()
