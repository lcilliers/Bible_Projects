"""Apply DIR-20260513-007 — M20-C group-verse mapping.

M20-C is more complex: shared verses across ka.ah (H3512A) and ka.eh (H3512B).
Schema note: verse_context_group has no mti_term_id column — VCGs are not term-
owned; vc rows from multiple terms can point to the same VCG. So shared-verse
ka.ah + ka.eh rows can co-exist in the same new VCG.
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
DIRECTIVE_ID = "DIR-20260513-007"

TERMS = {"G0120": 2078, "G1573": 603, "G3642": 1403, "H3512A": 574, "H3512B": 1700}

REFINE = {
    489:  "Discouragement as the inner state produced by interpersonal provocation — one person's provoking act creating another's loss of heart; the relational origin of the characteristic named explicitly (Col 3:21)",
    2657: "The fainthearted soul — the inner person diminished in courage (oligopsuchos: small-souled), requiring the response of being drawn alongside (paraklēsis) rather than correction or practical assistance (1Th 5:14)",
}
SPLIT_DELETE = [1014, 2716, 2739]
NEW_VCGS = {
    "NEW-01": ("M20-C-NEW-01", "Discouragement inflicted on the vulnerable — the disheartened as the specific target of cruelty (Psa 109:16: the brokenhearted pursued to death) and deceptive spiritual speech (Eze 13:22: false prophets disheartening the righteous falsely); the inner state of the vulnerable making them a target"),
    "NEW-02": ("M20-C-NEW-02", "Discouragement producing inner retreat — loss of resolve under military-political pressure, expressed immediately in withdrawal and turning back (Dan 11:30)"),
    "NEW-03": ("M20-C-NEW-03", "Loss of heart in sustained effort — long-haul endurance failing under temporal frustration; the discouragement that accumulates from persistent prayer (Luk 18:1), ministry (2Cor 4:1), doing good (Gal 6:9; 2Th 3:13), bearing another's suffering (Eph 3:13); countered by theological means (mercy received, future harvest) not circumstantial relief"),
    "NEW-04": ("M20-C-NEW-04", "Loss of heart and the inner person's renewal — the outer person wasting away while the inner person is renewed day by day; physical decline cannot produce inner collapse when the inner person is sustained by God; the outer/inner distinction named precisely (2Cor 4:16)"),
    "NEW-05": ("M20-C-NEW-05", "The crushed and sinking — total inner overwhelm of the helpless; ka.ah in its most acute form: the victim crushed, sinking down, and falling under superior might; complete inner collapse with no capacity for resistance (Psa 10:10)"),
}

# (reference, strongs, target, is_anchor)
VERSES = [
    ("Col 3:21",   "G0120",   "id=489",  1),
    ("1Th 5:14",   "G3642",   "id=2657", 1),
    ("Psa 109:16", "H3512B",  "NEW-01",  0),
    ("Eze 13:22",  "H3512B",  "NEW-01",  1),
    ("Dan 11:30",  "H3512B",  "NEW-02",  1),
    ("Psa 109:16", "H3512A",  "NEW-01",  0),
    ("Eze 13:22",  "H3512A",  "NEW-01",  0),
    ("Dan 11:30",  "H3512A",  "NEW-02",  0),
    ("Psa 10:10",  "H3512A",  "NEW-05",  1),
    ("Luk 18:1",   "G1573",   "NEW-03",  1),
    ("2Cor 4:1",   "G1573",   "NEW-03",  0),
    ("2Cor 4:16",  "G1573",   "NEW-04",  1),
    ("Gal 6:9",    "G1573",   "NEW-03",  0),
    ("Eph 3:13",   "G1573",   "NEW-03",  0),
    ("2Th 3:13",   "G1573",   "NEW-03",  0),
]

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true")
args = ap.parse_args()

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs("backups/row_backups", exist_ok=True)
backup_path = os.path.join(
    "backups/row_backups",
    f"M20_C_dir_007_pre_state_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

sg = conn.execute("SELECT id FROM cluster_subgroup WHERE cluster_code='M20' AND subgroup_code='M20-C' AND COALESCE(delete_flagged,0)=0").fetchone()
SG_ID = sg["id"]
print(f"DIRECTIVE: {DIRECTIVE_ID}  Sub-group: M20-C (id={SG_ID})\n")

# Resolve verses — look up vc via reference+mti_term_id; do not require an
# active vr row (Psa 10:10 H3512A is a known case where the vr is soft-deleted
# under XREF but the vc still references that vr_id and is itself active).
print("Resolving verses…")
resolved = []
for ref, strongs, target, is_anchor in VERSES:
    mt_id = TERMS[strongs]
    vc = conn.execute("""
        SELECT vc.id AS vc_id, vc.group_id, vc.verse_record_id
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
         WHERE vr.reference=? AND vr.term_id=? AND vc.mti_term_id=?
           AND COALESCE(vc.delete_flagged,0)=0
    """, (ref, strongs, mt_id)).fetchone()
    if not vc:
        raise SystemExit(f"vc not found: {ref} {strongs} (mt_id={mt_id})")
    resolved.append({"ref": ref, "strongs": strongs, "vr_id": vc["verse_record_id"],
                      "vc_id": vc["vc_id"], "cur_group": vc["group_id"],
                      "target": target, "is_anchor": is_anchor})
    print(f"  {ref:12s} {strongs:8s} vc_id={vc['vc_id']:>5d} cur={vc['group_id']} → {target}")

# Backup
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
print(f"  vcg rows: {len(pre['verse_context_group_pre'])} (expected 5)")
print(f"  vc rows: {len(pre['verse_context_pre'])} (expected 15)")

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
print("\n  VCG verse_context-row counts (M20-C terms, active):")
total = 0
all_anchors_ok = True
for r in conn.execute("""
    SELECT vcg.id, vcg.group_code, COUNT(vc.id) AS n,
           SUM(CASE WHEN vc.is_anchor=1 THEN 1 ELSE 0 END) AS n_anchor
      FROM verse_context_group vcg
      JOIN verse_context vc ON vc.group_id=vcg.id
      JOIN mti_terms mt ON mt.id=vc.mti_term_id
     WHERE mt.strongs_number IN ('G0120','G1573','G3642','H3512A','H3512B')
       AND COALESCE(vcg.delete_flagged,0)=0 AND COALESCE(vc.delete_flagged,0)=0
     GROUP BY vcg.id, vcg.group_code ORDER BY vcg.group_code
"""):
    mark = "✓" if r["n_anchor"] == 1 else "✗"
    if r["n_anchor"] != 1: all_anchors_ok = False
    total += r["n"]
    print(f"    id={r['id']:>4d}  {r['group_code']:20s}  rows={r['n']}  anchors={r['n_anchor']}  {mark}")
print(f"    Total vc rows: {total} (expected 15)  anchors all=1: {'✓' if all_anchors_ok else '✗'}")

print("\n  Soft-deleted VCGs:")
for r in conn.execute("SELECT id, group_code, delete_flagged FROM verse_context_group WHERE id IN (1014,2716,2739)"):
    mark = "✓" if r["delete_flagged"]==1 else "✗"
    print(f"    id={r['id']:>4d} code={r['group_code']:18s} flagged={r['delete_flagged']}  {mark}")

print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
conn.close()
