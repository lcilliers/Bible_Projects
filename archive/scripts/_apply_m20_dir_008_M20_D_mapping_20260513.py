"""Apply DIR-20260513-008 — M20-D group-verse mapping (REFINE only)."""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
DIRECTIVE_ID = "DIR-20260513-008"

TERMS = {"G1365": 1288, "G1374": 1398}

REFINE = {
    1792: "Double-mindedness as dispositional indecision — the inner person not settling, not committing, hedging between two orientations; the consequence is instability across all of life (Jam 1:8); the remedy is purification of the heart as the seat of inner orientation (Jam 4:8)",
    3060: "Doubt as situational faith-wavering — the inner person failing to complete the move from seeing to trusting in a specific encounter; addressed directly by Jesus (Mat 14:31); coexisting with worship in the same group at the resurrection appearance (Mat 28:17)",
}

VERSES = [
    ("Jam 4:8",   "G1374", 1792, 0),
    ("Jam 1:8",   "G1374", 1792, 1),
    ("Mat 14:31", "G1365", 3060, 1),
    ("Mat 28:17", "G1365", 3060, 0),
]

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true")
args = ap.parse_args()

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs("backups/row_backups", exist_ok=True)
backup_path = os.path.join(
    "backups/row_backups",
    f"M20_D_dir_008_pre_state_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

sg = conn.execute("SELECT id FROM cluster_subgroup WHERE cluster_code='M20' AND subgroup_code='M20-D' AND COALESCE(delete_flagged,0)=0").fetchone()
SG_ID = sg["id"]
print(f"DIRECTIVE: {DIRECTIVE_ID}  Sub-group: M20-D (id={SG_ID})\n")

# Resolve verses
print("Resolving verses…")
resolved = []
for ref, strongs, target_group, is_anchor in VERSES:
    mt_id = TERMS[strongs]
    vc = conn.execute("""
        SELECT vc.id AS vc_id, vc.group_id
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
         WHERE vr.reference=? AND vr.term_id=? AND vc.mti_term_id=?
           AND COALESCE(vc.delete_flagged,0)=0
    """, (ref, strongs, mt_id)).fetchone()
    if not vc:
        raise SystemExit(f"vc not found: {ref} {strongs}")
    resolved.append({"ref": ref, "strongs": strongs, "vc_id": vc["vc_id"],
                      "cur_group": vc["group_id"], "target": target_group, "is_anchor": is_anchor})
    print(f"  {ref:12s} {strongs:8s} vc_id={vc['vc_id']:>5d} cur={vc['group_id']} → {target_group} anchor={is_anchor}")

# Backup
vc_ids = [r["vc_id"] for r in resolved]
vcg_ids = list(REFINE.keys())
pre = {
    "directive_id": DIRECTIVE_ID, "timestamp": now_utc,
    "verse_context_group_pre": [dict(r) for r in conn.execute(
        f"SELECT * FROM verse_context_group WHERE id IN ({','.join(str(i) for i in vcg_ids)})")],
    "verse_context_pre": [dict(r) for r in conn.execute(
        f"SELECT * FROM verse_context WHERE id IN ({','.join(str(i) for i in vc_ids)})")],
}
with open(backup_path, "w", encoding="utf-8") as f:
    json.dump(pre, f, indent=2, ensure_ascii=False)
print(f"\nPre-state backup → {backup_path}")
print(f"  vcg rows: {len(pre['verse_context_group_pre'])} (expected 2)")
print(f"  vc rows: {len(pre['verse_context_pre'])} (expected 4)")

if not args.live:
    print("\n[DRY-RUN] no changes. Re-run with --live.")
    sys.exit(0)

# Apply
for vcg_id, desc in REFINE.items():
    conn.execute("UPDATE verse_context_group SET context_description=? WHERE id=?", (desc, vcg_id))
for r in resolved:
    conn.execute(
        "UPDATE verse_context SET group_id=?, is_anchor=?, is_relevant=1, cluster_subgroup_id=? WHERE id=?",
        (r["target"], r["is_anchor"], SG_ID, r["vc_id"])
    )
conn.commit()

# Completion
print(f"\nAFTER:")
for r in conn.execute("""
    SELECT vcg.id, vcg.group_code, COUNT(vc.id) AS n,
           SUM(CASE WHEN vc.is_anchor=1 THEN 1 ELSE 0 END) AS n_anchor
      FROM verse_context_group vcg
      JOIN verse_context vc ON vc.group_id=vcg.id
      JOIN mti_terms mt ON mt.id=vc.mti_term_id
     WHERE mt.strongs_number IN ('G1365','G1374')
       AND COALESCE(vcg.delete_flagged,0)=0 AND COALESCE(vc.delete_flagged,0)=0
     GROUP BY vcg.id, vcg.group_code ORDER BY vcg.group_code
"""):
    mark = "✓" if r["n_anchor"]==1 else "✗"
    print(f"  id={r['id']:>4d}  {r['group_code']:15s}  verses={r['n']}  anchors={r['n_anchor']}  {mark}")
print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
conn.close()
