"""M08 Phase 8.5 — BOUNDARY resolution: promote G0193 akratēs to M08-A4-VCG-01.

Per directive WA-M08-dir-005-phase85-boundary-resolution-v1-20260521.

Operations:
- Op A: UPDATE vc_id=36675: cluster_subgroup_id -> M08-A4, group_id -> M08-A4-VCG-01
- Op B: UPDATE mti_term_subgroup for G0193: M08-BOUNDARY -> M08-A4
- Op C: INSERT vcg_term link (M08-A4-VCG-01, mti_id=1113)
- Op D: Soft-delete M08-BOUNDARY-VCG-01 + its vcg_term link
- Op E: Soft-delete M08-BOUNDARY cluster_subgroup row
"""
import sys, io, sqlite3
from datetime import datetime, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
DIRECTIVE = 'wa-cluster-M08-dir-005-phase85-boundary-resolution-v1-20260521'

VC_ID = 36675       # G0193 akratēs at 2Ti 3:3
MTI_ID = 1113       # G0193 akratēs

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Resolve IDs
csg_a4_row = cur.execute("SELECT id FROM cluster_subgroup WHERE cluster_code='M08' AND subgroup_code='M08-A4' AND COALESCE(delete_flagged,0)=0").fetchone()
csg_boundary_row = cur.execute("SELECT id FROM cluster_subgroup WHERE cluster_code='M08' AND subgroup_code='M08-BOUNDARY' AND COALESCE(delete_flagged,0)=0").fetchone()
vcg_a4_v1_row = cur.execute("SELECT id FROM verse_context_group WHERE group_code='M08-A4-VCG-01' AND COALESCE(delete_flagged,0)=0").fetchone()
vcg_boundary_v1_row = cur.execute("SELECT id FROM verse_context_group WHERE group_code='M08-BOUNDARY-VCG-01' AND COALESCE(delete_flagged,0)=0").fetchone()

assert csg_a4_row and csg_boundary_row and vcg_a4_v1_row and vcg_boundary_v1_row, "Missing required sub-group / VCG rows"
csg_a4 = csg_a4_row[0]
csg_boundary = csg_boundary_row[0]
vcg_a4_v1 = vcg_a4_v1_row[0]
vcg_boundary_v1 = vcg_boundary_v1_row[0]
print(f'Resolved: csg_a4={csg_a4} csg_boundary={csg_boundary} vcg_a4_v1={vcg_a4_v1} vcg_boundary_v1={vcg_boundary_v1}')

# Pre-checks
print()
print('=== PRE-CHECKS ===')
vc = cur.execute("SELECT id, mti_term_id, cluster_subgroup_id, group_id, is_relevant, is_anchor, COALESCE(delete_flagged,0) AS df FROM verse_context WHERE id=?", (VC_ID,)).fetchone()
assert vc, f'vc_id={VC_ID} not found'
assert vc['mti_term_id'] == MTI_ID, f'vc_id={VC_ID} mti_id mismatch'
assert vc['cluster_subgroup_id'] == csg_boundary, f'vc_id={VC_ID} not in M08-BOUNDARY'
assert vc['group_id'] == vcg_boundary_v1, f'vc_id={VC_ID} not in M08-BOUNDARY-VCG-01'
assert vc['is_relevant'] == 1
assert vc['df'] == 0
print(f'  vc_id={VC_ID}: in M08-BOUNDARY / M08-BOUNDARY-VCG-01, is_relevant=1, is_anchor={vc["is_anchor"]} OK')

# Count pre
a4_vcg01_pre = cur.execute("SELECT COUNT(*) FROM verse_context vc JOIN verse_context_group vcg ON vcg.id=vc.group_id WHERE vcg.group_code='M08-A4-VCG-01' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0").fetchone()[0]
print(f'  M08-A4-VCG-01 verse count (pre): {a4_vcg01_pre} (expected 10)')
assert a4_vcg01_pre == 10

# mti_term_subgroup pre
mts_row = cur.execute("SELECT id, cluster_subgroup_id, placement_note FROM mti_term_subgroup WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (MTI_ID,)).fetchall()
print(f'  mti_term_subgroup rows for G0193 (pre): {len(mts_row)}')
for r in mts_row:
    print(f'    id={r["id"]} csg_id={r["cluster_subgroup_id"]} note={r["placement_note"]!r}')

# Apply
print()
print('=== APPLYING ===')
cur.execute('BEGIN')
try:
    # Op A — reroute the vc row
    cur.execute(
        "UPDATE verse_context SET cluster_subgroup_id=?, group_id=? WHERE id=? AND COALESCE(delete_flagged,0)=0",
        (csg_a4, vcg_a4_v1, VC_ID),
    )
    assert cur.rowcount == 1
    print(f'  Op A: vc_id={VC_ID} -> M08-A4 / M08-A4-VCG-01')

    # Op B — update mti_term_subgroup link
    cur.execute(
        "UPDATE mti_term_subgroup SET cluster_subgroup_id=?, placement_note=?, last_updated_date=? "
        "WHERE mti_term_id=? AND cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
        (csg_a4,
         '[primary] 1 verse — promoted from BOUNDARY at Phase 8.5 (per dir-005); supportive/qualifying register for CHAR-1 NT vice catalogue',
         NOW, MTI_ID, csg_boundary),
    )
    assert cur.rowcount == 1
    print(f'  Op B: mti_term_subgroup for G0193: M08-BOUNDARY -> M08-A4')

    # Op C — insert vcg_term link
    cur.execute(
        "INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note, delete_flagged, created_at, last_updated_date) "
        "VALUES (?, ?, ?, 0, ?, ?)",
        (vcg_a4_v1, MTI_ID, 'Phase 8.5 promotion from M08-BOUNDARY', NOW, NOW),
    )
    print(f'  Op C: inserted vcg_term link (M08-A4-VCG-01, G0193)')

    # Op D — soft-delete M08-BOUNDARY-VCG-01 + its vcg_term link
    note_vcg = f'Dissolved at M08 Phase 8.5 {NOW} (BOUNDARY resolved — G0193 promoted to M08-A4; per {DIRECTIVE})'
    cur.execute(
        "UPDATE verse_context_group SET delete_flagged=1, notes=? WHERE id=? AND COALESCE(delete_flagged,0)=0",
        (note_vcg, vcg_boundary_v1),
    )
    assert cur.rowcount == 1
    cur.execute(
        "UPDATE vcg_term SET delete_flagged=1, last_updated_date=? WHERE vcg_id=? AND COALESCE(delete_flagged,0)=0",
        (NOW, vcg_boundary_v1),
    )
    n_vt_d = cur.rowcount
    print(f'  Op D: M08-BOUNDARY-VCG-01 soft-deleted; {n_vt_d} vcg_term link(s) soft-deleted')

    # Op E — soft-delete M08-BOUNDARY cluster_subgroup
    note_csg = f'Dissolved at M08 Phase 8.5 {NOW} (BOUNDARY resolved — G0193 promoted to M08-A4; per {DIRECTIVE})'
    cur.execute(
        "UPDATE cluster_subgroup SET delete_flagged=1, notes=?, last_updated_date=? WHERE id=? AND COALESCE(delete_flagged,0)=0",
        (note_csg, NOW, csg_boundary),
    )
    assert cur.rowcount == 1
    print(f'  Op E: M08-BOUNDARY cluster_subgroup soft-deleted')

    conn.commit()
    print(f'  Committed at {NOW}')
except Exception:
    conn.rollback()
    print('ROLLED BACK')
    raise

# Post-checks
print()
print('=== POST-CHECKS ===')

vc_post = cur.execute("""
    SELECT cs.subgroup_code, vcg.group_code FROM verse_context vc
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    JOIN verse_context_group vcg ON vcg.id = vc.group_id
    WHERE vc.id = ?
""", (VC_ID,)).fetchone()
print(f'  vc_id={VC_ID} now in: subgroup={vc_post["subgroup_code"]!r} VCG={vc_post["group_code"]!r}')
assert vc_post['subgroup_code'] == 'M08-A4'
assert vc_post['group_code'] == 'M08-A4-VCG-01'

a4_vcg01_post = cur.execute("SELECT COUNT(*) FROM verse_context vc JOIN verse_context_group vcg ON vcg.id=vc.group_id WHERE vcg.group_code='M08-A4-VCG-01' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0").fetchone()[0]
print(f'  M08-A4-VCG-01 verse count (post): {a4_vcg01_post} (expected 11)')
assert a4_vcg01_post == 11

n_active_sg = cur.execute("SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f'  Active M08 sub-groups (post): {n_active_sg} (expected 8)')
assert n_active_sg == 8

n_active_vcgs = cur.execute("SELECT COUNT(*) FROM verse_context_group WHERE group_code LIKE 'M08-%-VCG-%' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f'  Active M08 VCGs (post): {n_active_vcgs} (expected 24)')
assert n_active_vcgs == 24

n_substantive = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE mt.cluster_code='M08' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""").fetchone()[0]
print(f'  M08 is_relevant verse count (post): {n_substantive} (expected 293, unchanged)')
assert n_substantive == 293

# Verify M08-BOUNDARY VCG soft-deleted
boundary_active = cur.execute("SELECT COUNT(*) FROM verse_context_group WHERE group_code='M08-BOUNDARY-VCG-01' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f'  M08-BOUNDARY-VCG-01 active rows: {boundary_active} (expected 0)')
assert boundary_active == 0

# vcg_term for G0193 in M08-A4-VCG-01 exists
new_link = cur.execute("""
    SELECT id, placement_note FROM vcg_term
    WHERE vcg_id=? AND mti_term_id=? AND COALESCE(delete_flagged,0)=0
""", (vcg_a4_v1, MTI_ID)).fetchone()
print(f'  New vcg_term link for G0193 in M08-A4-VCG-01: id={new_link["id"]} note={new_link["placement_note"]!r}')

print()
print('=== M08 PHASE 8.5 COMPLETE ===')
print(f'- G0193 akratēs (vc_id=36675) promoted from M08-BOUNDARY to M08-A4-VCG-01')
print(f'- M08-BOUNDARY-VCG-01 + M08-BOUNDARY cluster_subgroup soft-deleted')
print(f'- M08 now: 8 sub-groups, 24 VCGs, 293 is_relevant verses')
print(f'- mti_term_subgroup + vcg_term links updated')
print('Ready for Phase 8.7 — Characteristic mapping confirmation (v2_8 §11B).')
conn.close()
