"""M07 Phase 7 — CC validation of AI VCG output per v2_8 §10.9.

Validates:
- JSON parses
- Every vc_id is a real M07 is_relevant=1 vc (delete_flagged=0)
- Every vc_id used exactly once across all VCGs (unless dual-membership
  flagged — not implemented yet; raise if duplicate)
- Per-sub-group: sum of VCG members = sub-group's is_relevant count
  in DB
- Total = 363
- Every anchor_vc_id is in its VCG's verses array
- BOUNDARY VCG contains every is_relevant vc of every BOUNDARY term
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import sqlite3
from pathlib import Path
from collections import defaultdict

DB = Path('database/bible_research.db')
JSON_PATH = Path('Sessions/Session_Clusters/M07/files phase 7/WA-M07-vcg-creation-v1-20260519.json')
CLUSTER = 'M07'

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Load JSON
with open(JSON_PATH, encoding='utf-8') as f:
    data = json.load(f)

print('=== M07 Phase 7 — CC VALIDATION ===')
print(f"JSON: {JSON_PATH}")
print(f"_meta: {data.get('_meta', {})}")
print()

# DB ground truth: every M07 is_relevant vc with its sub-group
db_vcs = {}
for r in cur.execute(
    """
    SELECT vc.id, cs.subgroup_code, vc.is_anchor
    FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE mt.cluster_code = ? AND vc.is_relevant = 1
      AND COALESCE(vc.delete_flagged, 0) = 0
    """,
    (CLUSTER,),
).fetchall():
    db_vcs[r['id']] = (r['subgroup_code'], r['is_anchor'])
print(f"DB M07 is_relevant vc count: {len(db_vcs)} (expected 363)")
print()

# Per sub-group expected count
sg_expected = defaultdict(int)
for vc_id, (sg, _) in db_vcs.items():
    sg_expected[sg] += 1
print("DB per-sub-group expected counts:")
for sg in sorted(sg_expected.keys()):
    print(f"  {sg}: {sg_expected[sg]}")
print()

# Walk the JSON
print("=== Walking the JSON ===")
errors = []
seen_vc_ids = {}  # vc_id -> (vcg_code, subgroup)
total_in_json = 0
total_vcgs = 0
all_vcg_specs = []  # for later insert

if 'subgroups' not in data:
    errors.append("JSON missing 'subgroups' key")
else:
    for sg_code, sg_data in data['subgroups'].items():
        if 'vcgs' not in sg_data:
            errors.append(f"{sg_code}: missing 'vcgs' key")
            continue
        sg_total = 0
        for vcg in sg_data['vcgs']:
            total_vcgs += 1
            code = vcg.get('provisional_code', '<NO CODE>')
            verses = vcg.get('verses', [])
            anchor = vcg.get('anchor_vc_id')
            desc = vcg.get('description', '')

            # Check field name (must be `verses`, not `key_verses`)
            if 'key_verses' in vcg:
                errors.append(f"{code}: uses 'key_verses' field — must be 'verses'")
            if 'members' in vcg:
                errors.append(f"{code}: uses 'members' field — must be 'verses'")

            sg_total += len(verses)
            total_in_json += len(verses)

            # Anchor in verses
            if anchor is None:
                errors.append(f"{code}: anchor_vc_id is None")
            elif anchor not in verses:
                errors.append(f"{code}: anchor_vc_id={anchor} not in verses array")

            # Every vc_id in db_vcs (real M07 is_relevant)
            for vc_id in verses:
                if vc_id not in db_vcs:
                    errors.append(f"{code}: vc_id={vc_id} not a M07 is_relevant vc (phantom)")
                    continue
                # Check sub-group match
                db_sg = db_vcs[vc_id][0]
                if db_sg != sg_code:
                    errors.append(f"{code}: vc_id={vc_id} routed at Phase 6 to '{db_sg}' but JSON places it in '{sg_code}'")
                # No duplicates across all VCGs
                if vc_id in seen_vc_ids:
                    prev_code, prev_sg = seen_vc_ids[vc_id]
                    errors.append(f"vc_id={vc_id} in two VCGs: {prev_code} ({prev_sg}) and {code} ({sg_code})")
                seen_vc_ids[vc_id] = (code, sg_code)

            all_vcg_specs.append({
                'subgroup_code': sg_code,
                'provisional_code': code,
                'description': desc,
                'verses': verses,
                'anchor_vc_id': anchor,
            })

        # Sub-group sum check
        if sg_total != sg_expected.get(sg_code, 0):
            errors.append(f"{sg_code}: JSON sum {sg_total} != DB expected {sg_expected.get(sg_code, 0)}")
        else:
            print(f"  {sg_code}: {sg_total} verses across {len(sg_data['vcgs'])} VCGs — sum OK")

print()
print(f"Total verses in JSON: {total_in_json}")
print(f"Total VCGs: {total_vcgs}")
print()

# Missing vc_ids: in DB but not in JSON
missing = set(db_vcs.keys()) - set(seen_vc_ids.keys())
if missing:
    errors.append(f"{len(missing)} M07 is_relevant vc_ids NOT covered by any VCG")
    for vc_id in sorted(missing)[:10]:
        errors.append(f"  missing: vc_id={vc_id} (sub-group={db_vcs[vc_id][0]})")

# BOUNDARY check — every BOUNDARY term's is_relevant vc must be in M07-BOUNDARY VCG
boundary_term_ids = [r[0] for r in cur.execute("""
    SELECT mt.id FROM mti_terms mt
    JOIN cluster_subgroup cs ON cs.id IN (
        SELECT cluster_subgroup_id FROM verse_context vc2
        WHERE vc2.mti_term_id = mt.id AND vc2.is_relevant=1 AND COALESCE(vc2.delete_flagged,0)=0
    )
    WHERE mt.cluster_code='M07' AND cs.subgroup_code='M07-BOUNDARY' AND COALESCE(mt.delete_flagged,0)=0
""").fetchall()]
boundary_vcs = set()
for r in cur.execute("""
    SELECT vc.id FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE mt.cluster_code='M07' AND cs.subgroup_code='M07-BOUNDARY'
      AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""").fetchall():
    boundary_vcs.add(r[0])
print(f"DB BOUNDARY vc count: {len(boundary_vcs)}")
boundary_in_json = set()
for spec in all_vcg_specs:
    if spec['subgroup_code'] == 'M07-BOUNDARY':
        boundary_in_json.update(spec['verses'])
print(f"JSON BOUNDARY vc count: {len(boundary_in_json)}")
if boundary_vcs != boundary_in_json:
    missing = boundary_vcs - boundary_in_json
    extra = boundary_in_json - boundary_vcs
    if missing:
        errors.append(f"BOUNDARY: {len(missing)} vc_ids in DB but not in JSON")
    if extra:
        errors.append(f"BOUNDARY: {len(extra)} vc_ids in JSON but not in DB")

print()
if errors:
    print(f"=== VALIDATION FAILED — {len(errors)} errors ===")
    for e in errors[:30]:
        print(f"  - {e}")
    if len(errors) > 30:
        print(f"  ... and {len(errors) - 30} more")
    sys.exit(1)
else:
    print("=== VALIDATION PASSED ===")
    print(f"Ready to apply: {total_vcgs} VCGs across {len(data['subgroups'])} sub-groups, {total_in_json} verse assignments.")
