"""Apply DIR-20260513-006 — M20-B group-verse mapping."""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
DIRECTIVE_ID = "DIR-20260513-006"

TERMS = {"G1820": 808, "H2976": 394}

REFINE = {
    660: "Despair as the outer limit of inner endurance — the inner person burdened beyond capacity, despaired of life itself (2Cor 1:8); and the edge approached but not crossed under God's sustaining grace, perplexed but not driven to despair (2Cor 4:8)"
}
SPLIT_DELETE = [1238]
NEW_VCGS = {
    "NEW-01": ("M20-B-NEW-01", "Despair as volitional act — the heart actively surrendered to hopelessness (Ecc 2:20); despair as the natural terminus of exhausted pursuit when all options are gone (1Sa 27:1); despair leaving a recognisable inner signature in speech — the despairing man's words are wind (Job 6:26)"),
    "NEW-02": ("M20-B-NEW-02", "Despair as declaration — the word of hopelessness spoken or withheld, and its consequences; the declaration not made (Isa 57:10: 'you did not say it is hopeless') illuminating the characteristic by its resistance; the declaration made (Jer 2:25: 'it is hopeless, I have loved foreigners') closing off the path of return"),
    "NEW-03": ("M20-B-NEW-03", "Despair weaponised — hopelessness-language deployed to foreclose repentance and justify continued rebellion; 'that is in vain, we will follow our own plans' (Jer 18:12); the darkest dimension of the characteristic: despair as a posture used against the inner person's own potential for transformation"),
}

# Verses to assign: (reference, strongs, target_label, is_anchor)
VERSES = [
    ("2Cor 1:8", "G1820", "id=660", 1),
    ("2Cor 4:8", "G1820", "id=660", 0),
    ("Ecc 2:20", "H2976", "NEW-01", 1),
    ("1Sa 27:1", "H2976", "NEW-01", 0),
    ("Job 6:26", "H2976", "NEW-01", 0),
    ("Isa 57:10","H2976", "NEW-02", 0),
    ("Jer 2:25", "H2976", "NEW-02", 1),
    ("Jer 18:12","H2976", "NEW-03", 1),
]

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true")
args = ap.parse_args()

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs("backups/row_backups", exist_ok=True)
backup_path = os.path.join(
    "backups/row_backups",
    f"M20_B_dir_006_pre_state_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

# Resolve M20-B sub_group_id
sg = conn.execute(
    "SELECT id FROM cluster_subgroup WHERE cluster_code='M20' AND subgroup_code='M20-B' AND COALESCE(delete_flagged,0)=0"
).fetchone()
SG_ID = sg["id"]
print(f"DIRECTIVE: {DIRECTIVE_ID}  Sub-group: M20-B (id={SG_ID})\n")

# Resolve verses
print("Resolving verses…")
resolved = []
for ref, strongs, target, is_anchor in VERSES:
    mt_id = TERMS[strongs]
    vr = conn.execute(
        "SELECT id FROM wa_verse_records WHERE reference=? AND term_id=? AND COALESCE(delete_flagged,0)=0",
        (ref, strongs)
    ).fetchone()
    if not vr:
        raise SystemExit(f"vr not found: {ref} {strongs}")
    vc = conn.execute(
        "SELECT id, group_id FROM verse_context "
        "WHERE verse_record_id=? AND mti_term_id=? AND COALESCE(delete_flagged,0)=0",
        (vr["id"], mt_id)
    ).fetchone()
    if not vc:
        raise SystemExit(f"vc not found: {ref} {strongs}")
    resolved.append({"ref": ref, "strongs": strongs, "vr_id": vr["id"], "vc_id": vc["id"],
                      "cur_group": vc["group_id"], "target": target, "is_anchor": is_anchor})
    print(f"  {ref:12s} {strongs:8s}  vc_id={vc['id']:>5d}  cur_group={vc['cur_group'] if False else vc['group_id']} → {target}")

# Pre-state backup
vc_ids = [r["vc_id"] for r in resolved]
vcg_ids = list(REFINE.keys()) + SPLIT_DELETE
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
print(f"  vc rows: {len(pre['verse_context_pre'])} (expected 8)")

print(f"\nProposed: REFINE {len(REFINE)} | SPLIT-delete {len(SPLIT_DELETE)} | NEW VCG {len(NEW_VCGS)} | vc updates {len(VERSES)}")

if not args.live:
    print("\n[DRY-RUN] no changes. Re-run with --live.")
    sys.exit(0)

# --- APPLY ---
for vcg_id, desc in REFINE.items():
    conn.execute("UPDATE verse_context_group SET context_description=? WHERE id=?", (desc, vcg_id))
for vcg_id in SPLIT_DELETE:
    conn.execute(
        "UPDATE verse_context_group SET delete_flagged=1, notes=COALESCE(notes||' | ','')||? WHERE id=?",
        (f"{DIRECTIVE_ID}: SPLIT — content migrated ({now_utc})", vcg_id)
    )
new_ids = {}
for key, (code, desc) in NEW_VCGS.items():
    cur = conn.execute(
        "INSERT INTO verse_context_group (group_code, context_description, notes, delete_flagged, vertical_pass_flag) "
        "VALUES (?, ?, ?, 0, 0)",
        (code, desc, f"{DIRECTIVE_ID}: created by SPLIT")
    )
    new_ids[key] = cur.lastrowid
print(f"\n  NEW VCG ids: {new_ids}")

def resolve(label):
    if label.startswith("id="): return int(label[3:])
    return new_ids[label]

for r in resolved:
    conn.execute(
        "UPDATE verse_context SET group_id=?, is_anchor=?, is_relevant=1, cluster_subgroup_id=? WHERE id=?",
        (resolve(r["target"]), r["is_anchor"], SG_ID, r["vc_id"])
    )

conn.commit()

# --- COMPLETION ---
print(f"\nAFTER:")
print("\n  VCG verse counts (M20-B terms, active):")
for r in conn.execute("""
    SELECT vcg.id, vcg.group_code, COUNT(vc.id) AS n,
           SUM(CASE WHEN vc.is_anchor=1 THEN 1 ELSE 0 END) AS n_anchor
      FROM verse_context_group vcg
      JOIN verse_context vc ON vc.group_id=vcg.id
      JOIN mti_terms mt ON mt.id=vc.mti_term_id
     WHERE mt.strongs_number IN ('G1820','H2976')
       AND COALESCE(vcg.delete_flagged,0)=0 AND COALESCE(vc.delete_flagged,0)=0
     GROUP BY vcg.id, vcg.group_code ORDER BY vcg.group_code
"""):
    mark = "✓" if r["n_anchor"] == 1 else "✗"
    print(f"    id={r['id']:>4d}  {r['group_code']:18s}  verses={r['n']}  anchors={r['n_anchor']}  {mark}")

print("\n  Soft-deleted VCGs (1238):")
for r in conn.execute("SELECT id, group_code, delete_flagged FROM verse_context_group WHERE id=1238"):
    print(f"    id={r['id']} code={r['group_code']} flagged={r['delete_flagged']}  {'✓' if r['delete_flagged']==1 else '✗'}")

total = conn.execute("""
    SELECT COUNT(*) FROM verse_context vc
      JOIN mti_terms mt ON mt.id=vc.mti_term_id
     WHERE mt.strongs_number IN ('G1820','H2976') AND COALESCE(vc.delete_flagged,0)=0
""").fetchone()[0]
print(f"\n  Total active vc rows for M20-B terms: {total} (expected 8)")

print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
conn.close()
