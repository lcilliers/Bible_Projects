"""Pre-flight for DIR-20260513-005 (M20-A mapping apply).

Confirms: term IDs; existing VCGs (220, 222, 224, 888, 221, 223, 887);
all 30 verses resolve to vr_ids; current vc state matches directive's
expected source state. No writes.
"""
import sqlite3, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

# Term mti_ids
TERMS = {"G3308": 350, "G3309": 2709, "H1672": 259}

# Existing VCGs the directive references
REFINE_VCGS = {220: "350-001", 222: "2709-001", 224: "2709-003", 888: "259-002"}
SPLIT_VCGS  = {221: "350-002", 223: "2709-002", 887: "259-001"}

# Full verse list per directive's verse-to-group mapping (30 rows)
VERSES = [
    # (reference, strongs, target_label, is_anchor)
    ("Mat 13:22","G3308","id=220",0),("Mar 4:19","G3308","id=220",0),
    ("Luk 8:14","G3308","id=220",0),("Luk 21:34","G3308","id=220",1),
    ("1Pe 5:7","G3308","NEW-01",1),("2Cor 11:28","G3308","NEW-02",1),
    ("Mat 6:25","G3309","id=222",1),("Mat 6:27","G3309","id=222",0),
    ("Mat 6:28","G3309","id=222",0),("Mat 6:31","G3309","id=222",0),
    ("Mat 6:34","G3309","id=222",0),("Luk 12:22","G3309","id=222",0),
    ("Luk 12:25","G3309","id=222",0),("Luk 12:26","G3309","id=222",0),
    ("Phili 4:6","G3309","id=222",0),
    ("Mat 10:19","G3309","NEW-03",1),("Luk 12:11","G3309","NEW-03",0),
    ("Luk 10:41","G3309","NEW-04",1),
    ("1Cor 7:32","G3309","id=224",1),("1Cor 7:33","G3309","id=224",0),
    ("1Cor 7:34","G3309","id=224",0),("1Cor 12:25","G3309","id=224",0),
    ("Phili 2:20","G3309","id=224",0),
    ("1Sa 9:5","H1672","NEW-05",0),("1Sa 10:2","H1672","NEW-05",1),
    ("Isa 57:11","H1672","NEW-06",0),("Jer 17:8","H1672","NEW-06",1),
    ("Jer 38:19","H1672","NEW-06",0),("Jer 42:16","H1672","NEW-06",0),
    ("Psa 38:18","H1672","id=888",1),
]

print("=== Term IDs ===")
for s, expected_mt in TERMS.items():
    r = conn.execute("SELECT id, cluster_code FROM mti_terms WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0", (s,)).fetchone()
    ok = r and r["id"] == expected_mt and r["cluster_code"] == "M20"
    print(f"  {s}: mt_id={r['id'] if r else '?'} cluster={r['cluster_code'] if r else '?'} expected_mt={expected_mt}  {'✓' if ok else '✗'}")

print()
print("=== Existing VCGs ===")
for vcg_id, code in {**REFINE_VCGS, **SPLIT_VCGS}.items():
    r = conn.execute("SELECT id, group_code, COALESCE(delete_flagged,0) AS flagged FROM verse_context_group WHERE id=?", (vcg_id,)).fetchone()
    if r:
        action = "REFINE" if vcg_id in REFINE_VCGS else "SPLIT→soft-del"
        ok = r["group_code"] == code and r["flagged"] == 0
        print(f"  id={vcg_id} code={r['group_code']} flagged={r['flagged']}  ({action})  {'✓' if ok else '✗'}")
    else:
        print(f"  id={vcg_id}: NOT FOUND ✗")

print()
print("=== Verse resolution: 30 verses → vr_ids + current vc state ===")
ok_count = 0
missing_vr = []
wrong_group = []
verse_data = []
for ref, strongs, target, is_anchor in VERSES:
    mt_id = TERMS[strongs]
    vr = conn.execute(
        "SELECT id FROM wa_verse_records WHERE reference=? AND term_id=? AND COALESCE(delete_flagged,0)=0",
        (ref, strongs)
    ).fetchone()
    if not vr:
        missing_vr.append((ref, strongs))
        continue
    vr_id = vr["id"]
    vc = conn.execute(
        "SELECT id, group_id, is_anchor, is_relevant, cluster_subgroup_id FROM verse_context "
        "WHERE verse_record_id=? AND mti_term_id=? AND COALESCE(delete_flagged,0)=0",
        (vr_id, mt_id)
    ).fetchone()
    vc_id = vc["id"] if vc else None
    cur_grp = vc["group_id"] if vc else None
    verse_data.append({
        "ref": ref, "strongs": strongs, "vr_id": vr_id, "vc_id": vc_id,
        "current_group_id": cur_grp, "target_label": target, "target_anchor": is_anchor,
        "vc_exists": vc is not None,
    })
    ok_count += 1

print(f"  resolved: {ok_count} / 30")
if missing_vr:
    print(f"  MISSING vr (no wa_verse_records row): {missing_vr}")

# Show vc presence / current group_id summary
print()
print("=== Per-verse pre-state ===")
print(f"  {'ref':12s} {'strongs':8s} {'vr_id':>6s} {'vc_id':>6s} {'cur_group':>10s} → {'target':14s} anchor")
for v in verse_data:
    cur = v["current_group_id"] if v["current_group_id"] is not None else "—"
    vc_id = v["vc_id"] if v["vc_id"] is not None else "(no vc)"
    print(f"  {v['ref']:12s} {v['strongs']:8s} {v['vr_id']:>6d} {vc_id:>6} {cur:>10}   {v['target_label']:14s} {v['target_anchor']}")

# Count vc rows missing
missing_vc = [v for v in verse_data if not v["vc_exists"]]
print()
print(f"  Verses with NO existing vc row (would need INSERT): {len(missing_vc)}")
for m in missing_vc:
    print(f"    {m['ref']:12s} {m['strongs']:8s} vr_id={m['vr_id']}")

# Confirm current group_ids match expected source
print()
print("=== Source-state consistency check ===")
# Group source mapping: which existing group_id should each verse currently be in?
expected_source = {
    # REFINE — verses should already be in their target VCG
    "Mat 13:22": 220, "Mar 4:19": 220, "Luk 8:14": 220, "Luk 21:34": 220,
    "Mat 6:25": 222, "Mat 6:27": 222, "Mat 6:28": 222, "Mat 6:31": 222,
    "Mat 6:34": 222, "Luk 12:22": 222, "Luk 12:25": 222, "Luk 12:26": 222, "Phili 4:6": 222,
    "1Cor 7:32": 224, "1Cor 7:33": 224, "1Cor 7:34": 224, "1Cor 12:25": 224, "Phili 2:20": 224,
    "Psa 38:18": 888,
    # SPLIT — verses currently in old VCG (will be moved)
    "1Pe 5:7": 221, "2Cor 11:28": 221,
    "Mat 10:19": 223, "Luk 12:11": 223, "Luk 10:41": 223,
    "1Sa 9:5": 887, "1Sa 10:2": 887,
    "Isa 57:11": 887, "Jer 17:8": 887, "Jer 38:19": 887, "Jer 42:16": 887,
}
mismatches = []
for v in verse_data:
    exp = expected_source.get(v["ref"])
    if v["current_group_id"] != exp:
        mismatches.append((v["ref"], v["current_group_id"], exp))
if not mismatches:
    print("  All 30 verses currently in expected source VCGs. ✓")
else:
    print(f"  {len(mismatches)} mismatches:")
    for ref, cur, exp in mismatches:
        print(f"    {ref}: current={cur}  expected_source={exp}")

print()
print(f"=== Summary ===")
print(f"  Pre-flight {'PASS' if not missing_vr and not missing_vc and not mismatches else 'FAIL'}")

conn.close()
