"""Apply DIR-20260513-005 — M20-A group-verse mapping.

Operations:
  - REFINE: update context_description on 4 existing VCGs (220, 222, 224, 888)
  - SPLIT: soft-delete 3 existing VCGs (221, 223, 887); INSERT 6 NEW VCGs
  - UPDATE 30 verse_context rows: group_id, is_anchor, is_relevant, cluster_subgroup_id

Backup → dry-run → live.
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
DIRECTIVE_ID = "DIR-20260513-005"
SG_CODE = "M20-A"
SG_ID = None  # resolved below

# Term mti_ids
TERMS = {"G3308": 350, "G3309": 2709, "H1672": 259}

# REFINE: vcg_id → new context_description
REFINE = {
    220: "Anxiety as choking weight on the inner person — cares of the world, riches, and pleasures operating together to strangle spiritual fruitfulness and prevent the word from maturing in the inner person",
    222: "Anxiety about material provision — the inner person preoccupied with food, drink, clothing, the body, and tomorrow; addressed by Jesus as both futile (cannot add a single hour) and unnecessary (God provides)",
    224: "The anxiety-faculty rightly directed — merimnaō naming the intensity of directed concern for God's things and for others' welfare; the same inner faculty that produces anxiety when misdirected is the substance of devotion and love when rightly oriented",
    888: "Anxiety as the fuel of contrition — da.ag naming the inner energy that drives genuine sorrow over sin; the anxious, troubled quality of the inner person directed toward personal wrongdoing rather than external threat",
}

# SPLIT: soft-delete these vcg_ids
SPLIT_DELETE = [221, 223, 887]

# NEW VCGs to insert (label key → (group_code, context_description))
NEW_VCGS = {
    "NEW-01": ("M20-A-NEW-01", "Anxiety cast onto God — the person currently carrying real anxieties commanded to transfer the weight to God, with the theological ground: he cares for you (1Pe 5:7)"),
    "NEW-02": ("M20-A-NEW-02", "Pastoral burden as the weight of love — merimna naming the daily pressure of apostolic care for the churches; love expressed as a carried burden over time (2Cor 11:28)"),
    "NEW-03": ("M20-A-NEW-03", "Anticipatory anxiety about speech and defence under threat — anxiety directed toward a specific future performance situation; the remedy named is Spirit-provision in the moment (Mat 10:19; Luk 12:11)"),
    "NEW-04": ("M20-A-NEW-04", "Anxiety as proliferation — the inner person anxious and troubled about many things; attentional scattering across multiplicity, contrasted with the one-thing orientation of the non-anxious person (Luk 10:41)"),
    "NEW-05": ("M20-A-NEW-05", "Relational anxiety — worried concern for an absent or endangered person; anxiety as the dark face of relational love when the loved one is missing or at risk; voiced as distress seeking resolution (1Sa 9:5; 1Sa 10:2)"),
    "NEW-06": ("M20-A-NEW-06", "Anxiety in the face of concrete external threats — and its structural opposite; da.ag applied to real, named dangers (Isa 57:11; Jer 38:19; Jer 42:16); Jer 17:8 as the structural opposite: rootedness in God producing non-anxiety even under genuine threat — the most precise OT statement of what anxiety, at its core, is"),
}

# Verse list: (vc_id, target_label, is_anchor). vc_ids resolved from pre-flight.
VERSE_ASSIGNMENTS = [
    (2673, "id=220", 0), (2674, "id=220", 0), (2675, "id=220", 0), (2672, "id=220", 1),
    (2676, "NEW-01", 1), (2677, "NEW-02", 1),
    (2679, "id=222", 1), (2680, "id=222", 0), (2681, "id=222", 0), (2682, "id=222", 0),
    (2683, "id=222", 0), (2684, "id=222", 0), (2685, "id=222", 0), (2686, "id=222", 0),
    (2678, "id=222", 0),
    (2688, "NEW-03", 1), (2689, "NEW-03", 0),
    (2687, "NEW-04", 1),
    (2690, "id=224", 1), (2691, "id=224", 0), (2692, "id=224", 0), (2693, "id=224", 0),
    (2694, "id=224", 0),
    (14783, "NEW-05", 0), (14786, "NEW-05", 1),
    (14789, "NEW-06", 0), (14784, "NEW-06", 1), (14787, "NEW-06", 0), (14788, "NEW-06", 0),
    (14785, "id=888", 1),
]

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true")
args = ap.parse_args()

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs("backups/row_backups", exist_ok=True)
backup_path = os.path.join(
    "backups/row_backups",
    f"M20_A_dir_005_pre_state_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

# Resolve M20-A sub_group_id
sg = conn.execute(
    "SELECT id FROM cluster_subgroup WHERE cluster_code='M20' AND subgroup_code='M20-A' AND COALESCE(delete_flagged,0)=0"
).fetchone()
if not sg: raise SystemExit("M20-A cluster_subgroup not found")
SG_ID = sg["id"]
print(f"DIRECTIVE: {DIRECTIVE_ID}  Sub-group: M20-A (id={SG_ID})\n")

# Pre-state snapshot
vc_ids_touched = [v[0] for v in VERSE_ASSIGNMENTS]
vcg_ids_touched = list(REFINE.keys()) + SPLIT_DELETE
pre_state = {
    "directive_id": DIRECTIVE_ID,
    "timestamp": now_utc,
    "verse_context_group_pre": [dict(r) for r in conn.execute(
        f"SELECT * FROM verse_context_group WHERE id IN ({','.join(str(i) for i in vcg_ids_touched)})"
    )],
    "verse_context_pre": [dict(r) for r in conn.execute(
        f"SELECT * FROM verse_context WHERE id IN ({','.join(str(i) for i in vc_ids_touched)})"
    )],
}
with open(backup_path, "w", encoding="utf-8") as f:
    json.dump(pre_state, f, indent=2, ensure_ascii=False)
print(f"Pre-state backup → {backup_path}")
print(f"  vcg rows captured: {len(pre_state['verse_context_group_pre'])} (expected 7)")
print(f"  vc rows captured: {len(pre_state['verse_context_pre'])} (expected 30)")

print(f"\nProposed operations:")
print(f"  REFINE (UPDATE context_description): {len(REFINE)} VCGs")
print(f"  SPLIT — soft-delete: {len(SPLIT_DELETE)} VCGs")
print(f"  NEW VCG INSERTs: {len(NEW_VCGS)}")
print(f"  verse_context UPDATEs: {len(VERSE_ASSIGNMENTS)}")

if not args.live:
    print("\n[DRY-RUN] no changes. Re-run with --live.")
    sys.exit(0)

# --- LIVE APPLY ---

# 1. REFINE existing VCGs
for vcg_id, new_desc in REFINE.items():
    conn.execute(
        "UPDATE verse_context_group SET context_description=? WHERE id=?",
        (new_desc, vcg_id)
    )

# 2. SPLIT — soft-delete originals
for vcg_id in SPLIT_DELETE:
    conn.execute(
        "UPDATE verse_context_group SET delete_flagged=1, notes=COALESCE(notes||' | ','')||? WHERE id=?",
        (f"{DIRECTIVE_ID}: SPLIT — content migrated to NEW VCGs ({now_utc})", vcg_id)
    )

# 3. NEW VCGs — insert
new_vcg_ids = {}
for key, (code, desc) in NEW_VCGS.items():
    cur = conn.execute(
        "INSERT INTO verse_context_group (group_code, context_description, notes, delete_flagged, vertical_pass_flag) "
        "VALUES (?, ?, ?, 0, 0)",
        (code, desc, f"{DIRECTIVE_ID}: created by SPLIT")
    )
    new_vcg_ids[key] = cur.lastrowid
print(f"\n  NEW VCG ids: {new_vcg_ids}")

# 4. verse_context UPDATEs
def resolve_target(label):
    if label.startswith("id="):
        return int(label[3:])
    return new_vcg_ids[label]

for vc_id, target_label, is_anchor in VERSE_ASSIGNMENTS:
    target_group_id = resolve_target(target_label)
    conn.execute(
        "UPDATE verse_context SET group_id=?, is_anchor=?, is_relevant=1, cluster_subgroup_id=? "
        "WHERE id=?",
        (target_group_id, is_anchor, SG_ID, vc_id)
    )

conn.commit()

# --- COMPLETION CONFIRMATION ---
print(f"\nAFTER:")

# Q1: verse count per VCG for M20-A terms
print("\n  Q1 — Verse count per active VCG (M20-A terms):")
rows = list(conn.execute("""
    SELECT vcg.id, vcg.group_code, COUNT(vc.id) AS n
      FROM verse_context_group vcg
      JOIN verse_context vc ON vc.group_id=vcg.id
      JOIN mti_terms mt ON mt.id=vc.mti_term_id
     WHERE mt.cluster_code='M20'
       AND mt.strongs_number IN ('G3308','G3309','H1672')
       AND COALESCE(vcg.delete_flagged,0)=0
       AND COALESCE(vc.delete_flagged,0)=0
     GROUP BY vcg.id, vcg.group_code
     ORDER BY vcg.group_code
"""))
for r in rows:
    print(f"    id={r['id']:>4d}  {r['group_code']:25s}  verses={r['n']}")
print(f"    Total VCGs: {len(rows)} (expected 10)")

# Q2: anchor count per VCG = 1
print("\n  Q2 — Anchor count per VCG (should be 1 each):")
for r in conn.execute("""
    SELECT vcg.group_code, SUM(CASE WHEN vc.is_anchor=1 THEN 1 ELSE 0 END) AS n_anchor,
           COUNT(*) AS n_total
      FROM verse_context_group vcg
      JOIN verse_context vc ON vc.group_id=vcg.id
      JOIN mti_terms mt ON mt.id=vc.mti_term_id
     WHERE mt.cluster_code='M20' AND mt.strongs_number IN ('G3308','G3309','H1672')
       AND COALESCE(vcg.delete_flagged,0)=0 AND COALESCE(vc.delete_flagged,0)=0
     GROUP BY vcg.group_code ORDER BY vcg.group_code
"""):
    mark = "✓" if r["n_anchor"] == 1 else "✗"
    print(f"    {r['group_code']:25s}  anchors={r['n_anchor']}  total={r['n_total']}  {mark}")

# Q3: soft-deleted VCGs
print("\n  Q3 — Soft-deleted VCGs (221, 223, 887):")
for r in conn.execute(
    "SELECT id, group_code, delete_flagged FROM verse_context_group WHERE id IN (221,223,887)"
):
    mark = "✓" if r["delete_flagged"] == 1 else "✗"
    print(f"    id={r['id']:>4d} code={r['group_code']:15s} flagged={r['delete_flagged']}  {mark}")

# Q4: total verse_context rows for M20-A unchanged
total = conn.execute("""
    SELECT COUNT(*) FROM verse_context vc
      JOIN mti_terms mt ON mt.id=vc.mti_term_id
     WHERE mt.strongs_number IN ('G3308','G3309','H1672')
       AND COALESCE(vc.delete_flagged,0)=0
""").fetchone()[0]
print(f"\n  Q4 — Total active vc rows for M20-A terms: {total} (expected 30)")

# Q5: na.dad set-asides untouched
nadad = conn.execute(
    "SELECT COUNT(*) FROM verse_context WHERE mti_term_id=5571 AND is_relevant=0 AND COALESCE(delete_flagged,0)=0"
).fetchone()[0]
print(f"  Q5 — na.dad set-aside rows (mt_id=5571): {nadad} (expected 13)")

print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
conn.close()
