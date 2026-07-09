"""M07 Phase 6 — sub-group structural apply + verse routing.

Per v2_8 §9. Per directive WA-M07-dir-002-subgroup-assign-v1-20260519.md.

Operations:
- Op 0: Soft-delete 2 orphan vc rows (vc 34973 Php 3:19 G0152, vc 49397
        Php 3:2 G2699). Same cleanup pattern as M04 Step 1 orphan
        precedent. Brings is_relevant from 365 to 363, matching the
        Phase 5 mapping exactly.
- Op A: INSERT 9 cluster_subgroup rows (M07-A through M07-H + M07-BOUNDARY).
- Op B: INSERT mti_term_subgroup rows for every (term, sub-group) pair
        derived from the mapping.
- Op C: UPDATE verse_context.cluster_subgroup_id for every is_relevant
        vc row per the mapping.
- Op D: skipped — cluster.status already advanced to 'Analysis - In
        Progress' by Phase 4 (dir-001).
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
DIRECTIVE_ID = 'wa-cluster-M07-dir-002-subgroup-assign-v1-20260519'
MAPPING_PATH = Path('Sessions/Session_Clusters/M07/WA-M07-subgroup-mapping-v1-20260519.json')

# Sub-group definitions (subgroup_code -> label, core_description from Phase 5 §2)
SUBGROUPS = [
    ('M07-A', 'Shame as unjust inner wound',
     'Verses where shame is experienced as an undeserved inner wound — felt by the innocent, righteous, suffering, or faithful. Shame as inner impact of what is done to a person by enemies, circumstances, or the collapse of trust placed in unreliable human powers. Represents CHAR-1a (volume-split partition of CHAR-1 Shame as experienced inner state).'),
    ('M07-B', 'Shame as moral consequence and judgment',
     'Verses where shame falls as the deserved, fitting outcome of moral failure, sin, idolatry, folly, or wickedness. Includes corrective shame invoked to produce moral change, and the absence of shame (seared conscience) as moral collapse. Represents CHAR-1b (volume-split partition of CHAR-1).'),
    ('M07-C', 'Shame before God: conscience, guilt, and divine encounter',
     'Verses where shame operates in the vertical relationship between person and God — guilt-consciousness before the holy, covenant failure, soul exposure in divine presence. The promise of not being put to shame in God\'s presence is the positive pole. Represents CHAR-1c (volume-split partition of CHAR-1).'),
    ('M07-D', 'Humiliation as enforced abasement',
     'Verses where the inner-being characteristic is the enforced downward movement of standing — humiliation through social demotion, military defeat, physical exposure, or divine judgment on pride. Bodily/social visibility of the humiliation prominent. Represents CHAR-2.'),
    ('M07-E', 'Dishonour as relational worth-denial',
     'Verses where the inner-being characteristic is the relational denial of worth — treating persons as having less value than they possess, or stripping them of due honour. Operates between persons or person and God as the failure or refusal to acknowledge worth. Represents CHAR-3.'),
    ('M07-F', 'Shamefulness as moral-evaluative judgment',
     'Verses where the inner-being characteristic is the moral-evaluative judgment of what is shameful, indecent, or degraded — conscience\'s recognition that certain conduct violates inner propriety. Qualitative assessment of shame, not the experienced state. Includes inverted conscience (Phili 3:19) and perverted will (Hos 4:18). Represents CHAR-4.'),
    ('M07-G', 'Shame produced by contempt and rejection',
     'Verses where shame is produced by contempt and rejection — the received face of dismissive devaluation. Mechanism is contempt; characteristic within M07 is shame inflicted on the recipient. CROSS-REGISTER FLAG: M06 (contempt-projection as source-side). Represents CHAR-5.'),
    ('M07-H', 'Innocence as structural counter to shame',
     'Verses where inner moral innocence — clean conscience, blameless will, hands free of deliberate wrongdoing — functions as the structural protection against or counter to shame. Innocence as the inner state that protects against guilt-shame (Gen 20:5; Psa 26:6), is expected to shield from shame-like suffering (Psa 73:13), and whose absence sustains the shamed condition (Hos 8:5). CROSS-REGISTER FLAG: M12 (innocence as primary purity register). Represents CHAR-6.'),
    ('M07-BOUNDARY', 'BOUNDARY terms pending researcher resolution',
     'Verses of terms whose Phase 3 verdict was BOUNDARY — cluster membership or verse-level meaning requires researcher decision before substantive sub-group assignment. Five BOUNDARY terms: G2699 katatomē (1v, minimal inner-being content), H4893A mish.chat (1v, outward physical), H5206 ni.dah (1v, M07/M12 boundary), H8213 sha.phel (24v, M07/M09 split — most analytically significant), H8400 te.val.lul (0v, data gap).'),
]

# Orphans to soft-delete (Op 0)
ORPHAN_VC_IDS = [34973, 49397]

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Load mapping
with open(MAPPING_PATH, encoding='utf-8') as f:
    mapping_data = json.load(f)
mappings = mapping_data['mappings']
print(f"Loaded {len(mappings)} mappings from {MAPPING_PATH.name}")

# === PRE-CHECKS ===
print("\n=== PRE-CHECKS ===")

# Op 0 pre
for vc_id in ORPHAN_VC_IDS:
    r = cur.execute(
        "SELECT vc.is_relevant, vc.analysis_note, COALESCE(vc.delete_flagged,0), vr.delete_flagged "
        "FROM verse_context vc JOIN wa_verse_records vr ON vr.id = vc.verse_record_id WHERE vc.id=?",
        (vc_id,),
    ).fetchone()
    if not r:
        raise SystemExit(f"FAIL: orphan vc_id={vc_id} not found")
    assert r[0] == 1, f"orphan vc_id={vc_id} not is_relevant"
    assert r[1] is None or r[1].strip() == '', f"orphan vc_id={vc_id} has analysis_note"
    assert r[2] == 0, f"orphan vc_id={vc_id} already soft-deleted"
    assert r[3] == 1, f"orphan vc_id={vc_id}'s vr is NOT soft-deleted (unexpected)"
    print(f"  orphan vc_id={vc_id}: is_relevant=1, no analysis_note, vc.del=0, vr.del=1 — OK")

# Op A pre: no sub-groups yet
n_existing_sg = cur.execute(
    "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0"
).fetchone()[0]
print(f"  Pre-existing M07 sub-groups: {n_existing_sg}")
assert n_existing_sg == 0, "M07 sub-groups already exist"

# Build vc_id lookup from mappings (Reference + mti_id -> vc_id)
ref_term_to_vc = {}
for r in cur.execute(
    """
    SELECT vc.id, vc.mti_term_id, vr.reference
    FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
    WHERE mt.cluster_code='M07' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """
).fetchall():
    ref_term_to_vc[(r['mti_term_id'], r['reference'])] = r['id']

# Resolve every mapping entry to a vc_id
unresolved = []
resolved = []
for m in mappings:
    key = (m['mti_id'], m['reference'])
    if key in ref_term_to_vc:
        resolved.append({'vc_id': ref_term_to_vc[key], 'subgroup': m['subgroup'], 'mti_id': m['mti_id']})
    else:
        unresolved.append(m)
print(f"  Mappings resolved to vc_ids: {len(resolved)} / {len(mappings)}")
if unresolved:
    print(f"  UNRESOLVED ({len(unresolved)}):")
    for u in unresolved[:5]:
        print(f"    {u}")
    raise SystemExit("FAIL: some mappings could not be resolved to vc_ids")

# === APPLY ===
print("\n=== APPLYING ===")
cur.execute('BEGIN')
try:
    # Op 0 — soft-delete orphans
    for vc_id in ORPHAN_VC_IDS:
        cur.execute(
            "UPDATE verse_context SET delete_flagged=1 WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (vc_id,),
        )
        assert cur.rowcount == 1
    print(f"  Op 0: soft-deleted {len(ORPHAN_VC_IDS)} orphan vc rows")

    # Op A — INSERT cluster_subgroup rows
    sg_id_by_code = {}
    for idx, (code, label, descr) in enumerate(SUBGROUPS):
        cur.execute(
            "INSERT INTO cluster_subgroup (cluster_code, subgroup_code, label, core_description, "
            " sort_order, status, version, source, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('M07', code, label, descr, idx, 'active', 'v1', DIRECTIVE_ID, NOW, NOW),
        )
        sg_id_by_code[code] = cur.lastrowid
    print(f"  Op A: inserted {len(SUBGROUPS)} cluster_subgroup rows")

    # Op B — INSERT mti_term_subgroup rows (primary per Phase 5 §3; secondary as additional rows)
    # Build per-term sub-group sets from resolved mappings + count
    term_sg_counts = defaultdict(lambda: defaultdict(int))
    for r in resolved:
        term_sg_counts[r['mti_id']][r['subgroup']] += 1
    # Also add BOUNDARY terms' sub-group assignment even if their mapping went there
    # (already covered by mappings)

    n_links = 0
    for mti_id, sg_counts in term_sg_counts.items():
        # Sort by descending count to identify primary
        sorted_sg = sorted(sg_counts.items(), key=lambda x: -x[1])
        primary_sg = sorted_sg[0][0]
        for sg, count in sorted_sg:
            note = f"[primary] {count} verses" if sg == primary_sg else f"[secondary] {count} verses"
            cur.execute(
                "INSERT INTO mti_term_subgroup (mti_term_id, cluster_subgroup_id, placement_note, "
                " created_at, last_updated_date) VALUES (?, ?, ?, ?, ?)",
                (mti_id, sg_id_by_code[sg], note, NOW, NOW),
            )
            n_links += 1
    print(f"  Op B: inserted {n_links} mti_term_subgroup rows")

    # Op C — UPDATE verse_context.cluster_subgroup_id
    n_routed = 0
    for r in resolved:
        cur.execute(
            "UPDATE verse_context SET cluster_subgroup_id=? "
            "WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (sg_id_by_code[r['subgroup']], r['vc_id']),
        )
        n_routed += cur.rowcount
    print(f"  Op C: routed {n_routed} verses to sub-groups (expected {len(resolved)})")
    assert n_routed == len(resolved)

    # Op D skipped — Phase 4 already advanced status

    conn.commit()
    print(f"  Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# === POST-CHECKS ===
print("\n=== POST-CHECKS ===")

# Per-sub-group verse counts
print("Per-sub-group verse counts:")
for code in [s[0] for s in SUBGROUPS]:
    n = cur.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id "
        "WHERE cs.cluster_code='M07' AND cs.subgroup_code=? AND vc.is_relevant=1 "
        "AND COALESCE(vc.delete_flagged,0)=0",
        (code,),
    ).fetchone()[0]
    print(f"  {code}: {n}")

# Total
n_routed_final = cur.execute(
    "SELECT COUNT(*) FROM verse_context vc "
    "JOIN mti_terms mt ON mt.id = vc.mti_term_id "
    "WHERE mt.cluster_code='M07' AND vc.is_relevant=1 "
    "AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NOT NULL"
).fetchone()[0]
n_unrouted = cur.execute(
    "SELECT COUNT(*) FROM verse_context vc "
    "JOIN mti_terms mt ON mt.id = vc.mti_term_id "
    "WHERE mt.cluster_code='M07' AND vc.is_relevant=1 "
    "AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NULL"
).fetchone()[0]
print(f"\nRouted is_relevant verses: {n_routed_final}")
print(f"Unrouted is_relevant verses: {n_unrouted}")
assert n_unrouted == 0, f"FAIL: {n_unrouted} is_relevant verses unrouted"

# Cluster status (already 'Analysis - In Progress' from Phase 4)
cluster_status = cur.execute("SELECT status FROM cluster WHERE cluster_code='M07'").fetchone()[0]
print(f"\nCluster M07 status: {cluster_status!r}")

print("\n=== M07 PHASE 6 COMPLETE ===")
print(f"- 2 orphans soft-deleted (Op 0)")
print(f"- 9 cluster_subgroup rows created (Op A)")
print(f"- {n_links} mti_term_subgroup rows created (Op B)")
print(f"- {n_routed_final} verses routed (Op C)")
print(f"- Status flip skipped (already advanced at Phase 4)")
print("Ready for Phase 7 — VCG design (v2_8 §10).")
conn.close()
