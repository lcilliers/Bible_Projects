"""Apply DIR-20260513-002 — M20 term rebind: H5074 na.dad and G0560 apelpizo → M18.

Authored per wa-sessionb-cluster-instruction §7 / wa-directive-instruction §11.6.
The directive references mti_terms.cluster_subgroup_id (removed in M46) — that
clause is a noop on current schema. Only mti_terms.cluster_code is updated.

Backup → dry-run → live.
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
DIRECTIVE_ID = "DIR-20260513-002"
TARGETS = [("H5074", "na.dad", 5571), ("G0560", "apelpizo", 402)]
NEW_CLUSTER = "M18"
SRC_CLUSTER = "M20"

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true")
args = ap.parse_args()

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs("backups/row_backups", exist_ok=True)
backup_path = os.path.join(
    "backups/row_backups",
    f"mti_terms_M20_term_rebind_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

print(f"DIRECTIVE: {DIRECTIVE_ID}")
print(f"Operation: UPDATE mti_terms SET cluster_code='{NEW_CLUSTER}' WHERE strongs_number IN ('H5074','G0560')")
print()

# Pre-state
print("BEFORE:")
before_rows = []
for strongs, translit, expected_mt_id in TARGETS:
    r = conn.execute(
        "SELECT * FROM mti_terms WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0",
        (strongs,)
    ).fetchone()
    if not r:
        raise SystemExit(f"Term {strongs} not found")
    d = dict(r)
    before_rows.append(d)
    print(f"  {strongs:8s} mti_id={d['id']}  cluster_code={d['cluster_code']}  last_changed={d['last_changed']}")
    if d['id'] != expected_mt_id:
        raise SystemExit(f"Pre-check fail: {strongs} expected mti_id={expected_mt_id}, got {d['id']}")
    if d['cluster_code'] != SRC_CLUSTER:
        raise SystemExit(f"Pre-check fail: {strongs} expected cluster_code={SRC_CLUSTER}, got {d['cluster_code']}")

# Backup
with open(backup_path, "w", encoding="utf-8") as f:
    json.dump({"directive_id": DIRECTIVE_ID, "timestamp": now_utc, "rows": before_rows},
              f, indent=2, ensure_ascii=False)
print(f"\nBackup → {backup_path}")

print(f"\nProposed: cluster_code  '{SRC_CLUSTER}'  →  '{NEW_CLUSTER}' for both terms")
print(f"           last_changed bump to {now_utc}")

if not args.live:
    print("\n[DRY-RUN] no changes. Re-run with --live.")
    sys.exit(0)

# Apply
conn.execute(
    "UPDATE mti_terms SET cluster_code=?, last_changed=? "
    "WHERE strongs_number IN ('H5074','G0560') AND cluster_code=?",
    (NEW_CLUSTER, now_utc, SRC_CLUSTER)
)
changed = conn.total_changes
conn.commit()

# COMPLETION CONFIRMATION (the runnable subset of the directive's queries)
print(f"\nAFTER (rows changed: {changed}, expected 2):")
for strongs, translit, expected_mt_id in TARGETS:
    r = dict(conn.execute(
        "SELECT id, strongs_number, cluster_code, last_changed FROM mti_terms WHERE strongs_number=?",
        (strongs,)
    ).fetchone())
    print(f"  {r['strongs_number']:8s} mti_id={r['id']}  cluster_code={r['cluster_code']}")

# Term counts
print(f"\nCluster term counts:")
for code in (SRC_CLUSTER, NEW_CLUSTER):
    n = conn.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (code,)
    ).fetchone()[0]
    print(f"  {code}: {n} active terms")

# Verse_context unchanged (sanity)
print(f"\nverse_context row counts (unchanged):")
for strongs, _, mt_id in TARGETS:
    n = conn.execute(
        "SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0",
        (mt_id,)
    ).fetchone()[0]
    print(f"  {strongs} (mt_id={mt_id}): {n} active vc rows")

# VCG 1306 intact
vcg = conn.execute(
    "SELECT id, group_code, COALESCE(delete_flagged,0) AS flagged FROM verse_context_group WHERE id=1306"
).fetchone()
print(f"\nVCG 1306: id={vcg['id']}  group_code={vcg['group_code']}  flagged={vcg['flagged']}")

if changed != 2:
    raise SystemExit(f"\nUnexpected row count: {changed} (expected 2)")
for strongs, _, _ in TARGETS:
    r = conn.execute("SELECT cluster_code FROM mti_terms WHERE strongs_number=?", (strongs,)).fetchone()
    if r["cluster_code"] != NEW_CLUSTER:
        raise SystemExit(f"Post-state mismatch on {strongs}")

print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
conn.close()
