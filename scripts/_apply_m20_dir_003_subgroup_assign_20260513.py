"""Apply DIR-20260513-003 — M20 sub-group assignment.

Creates 4 cluster_subgroup rows (M20-A through M20-D) and 12 mti_term_subgroup
placements (one per term). Per wa-sessionb-cluster-instruction §7.

Backup → dry-run → live.
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
DIRECTIVE_ID = "DIR-20260513-003"
CLUSTER_CODE = "M20"

SUBGROUPS = [
    ("M20-A", "Anxiety and Worry",                  1),
    ("M20-B", "Despair and Hopelessness",           2),
    ("M20-C", "Discouragement and Loss of Heart",   3),
    ("M20-D", "Doubt and Indecision",               4),
]

# (strongs_number, sub_group_code)
TERM_PLACEMENTS = [
    ("H1672",  "M20-A"), ("G3309",  "M20-A"), ("G3308",  "M20-A"),
    ("H2976",  "M20-B"), ("G1820",  "M20-B"),
    ("G1573",  "M20-C"), ("H3512A", "M20-C"), ("H3512B", "M20-C"),
    ("G0120",  "M20-C"), ("G3642",  "M20-C"),
    ("G1365",  "M20-D"), ("G1374",  "M20-D"),
]

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true")
args = ap.parse_args()

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
backup_dir = "backups/row_backups"
os.makedirs(backup_dir, exist_ok=True)
backup_path = os.path.join(
    backup_dir,
    f"M20_subgroup_assign_pre_state_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

print(f"DIRECTIVE: {DIRECTIVE_ID}")
print()

# Pre-state snapshot — what does cluster_subgroup and mti_term_subgroup look like
pre_state = {
    "directive_id": DIRECTIVE_ID,
    "timestamp": now_utc,
    "cluster_subgroup_M20_pre": [dict(r) for r in conn.execute(
        "SELECT * FROM cluster_subgroup WHERE cluster_code='M20'"
    )],
    "mti_term_subgroup_M20_pre": [dict(r) for r in conn.execute("""
        SELECT mts.* FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id=mts.mti_term_id
         WHERE mt.cluster_code='M20'
    """)],
}
with open(backup_path, "w", encoding="utf-8") as f:
    json.dump(pre_state, f, indent=2, ensure_ascii=False)
print(f"Pre-state backup → {backup_path}")
print(f"  cluster_subgroup M20 rows pre-state: {len(pre_state['cluster_subgroup_M20_pre'])} (expected 0)")
print(f"  mti_term_subgroup M20 rows pre-state: {len(pre_state['mti_term_subgroup_M20_pre'])} (expected 0)")

# Resolve term strongs → mti_id
print("\nResolving term IDs:")
term_id_map = {}
for strongs, sg_code in TERM_PLACEMENTS:
    r = conn.execute(
        "SELECT id, transliteration, cluster_code FROM mti_terms "
        "WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0",
        (strongs,)
    ).fetchone()
    if not r:
        raise SystemExit(f"Term {strongs} not found")
    if r["cluster_code"] != CLUSTER_CODE:
        raise SystemExit(f"Term {strongs} not in {CLUSTER_CODE} (cluster_code={r['cluster_code']})")
    term_id_map[strongs] = r["id"]
    print(f"  {strongs:8s} mt_id={r['id']:>5d}  {r['transliteration']:18s} → {sg_code}")

print(f"\nProposed inserts:")
print(f"  cluster_subgroup: 4 rows ({', '.join(sg[0] for sg in SUBGROUPS)})")
print(f"  mti_term_subgroup: 12 rows")

if not args.live:
    print("\n[DRY-RUN] no changes. Re-run with --live.")
    sys.exit(0)

# --- LIVE APPLY ---
# Insert cluster_subgroup rows
sg_id_map = {}
for sg_code, label, sort_order in SUBGROUPS:
    cur = conn.execute(
        "INSERT INTO cluster_subgroup "
        "(cluster_code, subgroup_code, label, core_description, sort_order, "
        " status, version, source, delete_flagged, created_at, last_updated_date) "
        "VALUES (?, ?, ?, '', ?, 'active', 'v1', ?, 0, ?, ?)",
        (CLUSTER_CODE, sg_code, label, sort_order, DIRECTIVE_ID, now_utc, now_utc)
    )
    sg_id_map[sg_code] = cur.lastrowid

# Insert mti_term_subgroup rows
placement_note = f"{DIRECTIVE_ID} — Phase 4 subgroup-assign"
for strongs, sg_code in TERM_PLACEMENTS:
    conn.execute(
        "INSERT INTO mti_term_subgroup "
        "(mti_term_id, cluster_subgroup_id, placement_note, delete_flagged, "
        " created_at, last_updated_date) "
        "VALUES (?, ?, ?, 0, ?, ?)",
        (term_id_map[strongs], sg_id_map[sg_code], placement_note, now_utc, now_utc)
    )

conn.commit()

# --- COMPLETION CONFIRMATION ---
print("\nAFTER:")
print("\n  Sub-group rows for M20:")
for r in conn.execute(
    "SELECT subgroup_code, label, sort_order FROM cluster_subgroup "
    "WHERE cluster_code='M20' AND COALESCE(delete_flagged,0)=0 ORDER BY sort_order"
):
    print(f"    {r['subgroup_code']}  ({r['sort_order']})  {r['label']}")

print("\n  Term-to-sub-group assignments:")
for r in conn.execute("""
    SELECT cs.subgroup_code, mt.strongs_number, mt.transliteration
      FROM mti_term_subgroup mts
      JOIN mti_terms mt ON mt.id=mts.mti_term_id
      JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
     WHERE cs.cluster_code='M20' AND COALESCE(mts.delete_flagged,0)=0
     ORDER BY cs.subgroup_code, mt.strongs_number
"""):
    print(f"    {r['subgroup_code']}  {r['strongs_number']:8s}  {r['transliteration']}")

print("\n  Term counts per sub-group:")
counts = {}
for r in conn.execute("""
    SELECT cs.subgroup_code, COUNT(*) AS n
      FROM mti_term_subgroup mts
      JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
     WHERE cs.cluster_code='M20' AND COALESCE(mts.delete_flagged,0)=0
     GROUP BY cs.subgroup_code ORDER BY cs.subgroup_code
"""):
    counts[r["subgroup_code"]] = r["n"]
    print(f"    {r['subgroup_code']}: {r['n']}")
expected = {"M20-A": 3, "M20-B": 2, "M20-C": 5, "M20-D": 2}
if counts != expected:
    raise SystemExit(f"Count mismatch: got {counts}, expected {expected}")

# Unassigned check
unassigned = list(conn.execute("""
    SELECT mt.strongs_number FROM mti_terms mt
     WHERE mt.cluster_code='M20' AND COALESCE(mt.delete_flagged,0)=0
       AND mt.id NOT IN (
           SELECT mts.mti_term_id FROM mti_term_subgroup mts
             JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
            WHERE cs.cluster_code='M20' AND COALESCE(mts.delete_flagged,0)=0
       )
"""))
print(f"\n  Unassigned M20 terms: {len(unassigned)} (expected 0)")
if unassigned:
    for r in unassigned:
        print(f"    {r['strongs_number']}")
    raise SystemExit("Unassigned terms found")

print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
conn.close()
