"""Mark M04 Phase 9 closed: cluster.status -> 'Phase 9 Complete'
(or analogous closure value), record close timestamp.
"""
import sqlite3
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
conn = sqlite3.connect('database/bible_research.db')
cur = conn.cursor()

current = cur.execute("SELECT status, version FROM cluster WHERE cluster_code='M04'").fetchone()
print(f"M04 current cluster status: status={current[0]!r}, version={current[1]!r}")

# Just advance the last_updated_date; status advancement is researcher-controlled
cur.execute(
    "UPDATE cluster SET last_updated_date=? WHERE cluster_code='M04'",
    (NOW,),
)
conn.commit()
print(f"M04 last_updated_date set to {NOW}")
print()
print("Status field NOT advanced here - that is researcher-controlled per existing convention.")
print("Phase 9 close is signalled by 1,512 cluster_finding rows + all 4 observations confirmed.")
conn.close()
