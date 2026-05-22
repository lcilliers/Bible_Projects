"""M08 Phase 7 — CC validation of AI VCG output per v2_8 §10.9.

Validates:
- JSON parses
- Every vc_id is a real M08 is_relevant=1 vc (delete_flagged=0)
- Every vc_id used exactly once across all VCGs (no duplicates)
- Per-sub-group: sum of VCG members = sub-group's is_relevant count in DB
- Total = 296
- Every anchor_vc_id is in its VCG's verses array
- BOUNDARY VCG contains every is_relevant vc of every BOUNDARY term
- M09-C VCGs reflect M22 cross-register flag (informational check)
"""
import sys, io, json, sqlite3
from pathlib import Path
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB = Path('database/bible_research.db')
JSON_PATH = Path('Sessions/Session_Clusters/M09/wa-cluster-M09-vcg-creation-v1-20260522.json')
CLUSTER = 'M09'

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

with open(JSON_PATH, encoding='utf-8') as f:
    data = json.load(f)

print('=== M08 Phase 7 — CC VALIDATION ===')
print(f'JSON: {JSON_PATH}')
print(f'_meta: {data.get("_meta", {})}')
print()

# DB ground truth
db_vcs = {}
for r in cur.execute("""
    SELECT vc.id, cs.subgroup_code, vc.is_anchor
    FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""", (CLUSTER,)).fetchall():
    db_vcs[r['id']] = (r['subgroup_code'], r['is_anchor'])
print(f'DB M09 is_relevant vc count: {len(db_vcs)} (expected 109)')
print()

sg_expected = defaultdict(int)
for vc_id, (sg, _) in db_vcs.items():
    sg_expected[sg] += 1
print('DB per-sub-group expected counts:')
for sg in sorted(sg_expected.keys()):
    print(f'  {sg}: {sg_expected[sg]}')
print()

print('=== Walking the JSON ===')
errors = []
seen_vc_ids = {}
total_in_json = 0
total_vcgs = 0
all_vcg_specs = []

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

            if 'key_verses' in vcg:
                errors.append(f"{code}: uses 'key_verses' field — must be 'verses'")
            if 'members' in vcg:
                errors.append(f"{code}: uses 'members' field — must be 'verses'")

            sg_total += len(verses)
            total_in_json += len(verses)

            if anchor is None:
                errors.append(f'{code}: anchor_vc_id is None')
            elif anchor not in verses:
                errors.append(f'{code}: anchor_vc_id={anchor} not in verses array')

            for vc_id in verses:
                if vc_id not in db_vcs:
                    errors.append(f'{code}: vc_id={vc_id} not a M08 is_relevant vc (phantom)')
                    continue
                db_sg = db_vcs[vc_id][0]
                if db_sg != sg_code:
                    errors.append(f"{code}: vc_id={vc_id} routed at Phase 6 to '{db_sg}' but JSON places it in '{sg_code}'")
                if vc_id in seen_vc_ids:
                    prev_code, prev_sg = seen_vc_ids[vc_id]
                    errors.append(f'vc_id={vc_id} in two VCGs: {prev_code} ({prev_sg}) and {code} ({sg_code})')
                seen_vc_ids[vc_id] = (code, sg_code)

            all_vcg_specs.append({
                'subgroup_code': sg_code,
                'provisional_code': code,
                'description': desc,
                'verses': verses,
                'anchor_vc_id': anchor,
            })

        if sg_total != sg_expected.get(sg_code, 0):
            errors.append(f'{sg_code}: JSON sum {sg_total} != DB expected {sg_expected.get(sg_code, 0)}')
        else:
            print(f'  {sg_code}: {sg_total} verses across {len(sg_data["vcgs"])} VCGs — sum OK')

print()
print(f'Total verses in JSON: {total_in_json}')
print(f'Total VCGs: {total_vcgs}')
print()

missing = set(db_vcs.keys()) - set(seen_vc_ids.keys())
if missing:
    errors.append(f'{len(missing)} M08 is_relevant vc_ids NOT covered by any VCG')
    for vc_id in sorted(missing)[:10]:
        errors.append(f'  missing: vc_id={vc_id} (sub-group={db_vcs[vc_id][0]})')

# BOUNDARY check
boundary_vcs = {r[0] for r in cur.execute("""
    SELECT vc.id FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE mt.cluster_code='M09' AND cs.subgroup_code='M09-BOUNDARY'
      AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""").fetchall()}
boundary_in_json = set()
for spec in all_vcg_specs:
    if spec['subgroup_code'] == 'M09-BOUNDARY':
        boundary_in_json.update(spec['verses'])
print(f'DB BOUNDARY vc count: {len(boundary_vcs)}')
print(f'JSON BOUNDARY vc count: {len(boundary_in_json)}')
if boundary_vcs != boundary_in_json:
    missing_b = boundary_vcs - boundary_in_json
    extra_b = boundary_in_json - boundary_vcs
    if missing_b:
        errors.append(f'BOUNDARY: {len(missing_b)} vc_ids in DB but not in JSON')
    if extra_b:
        errors.append(f'BOUNDARY: {len(extra_b)} vc_ids in JSON but not in DB')

# Informational: check M09-C VCGs for M22 flag indication
print()
print('=== Cross-register flag check (informational) ===')
m08c_descs = [s['description'].lower() for s in all_vcg_specs if s['subgroup_code'] == 'M09-C']
has_m22 = any('m22' in d or 'god-directed' in d or 'praise' in d or 'glorying' in d for d in m08c_descs)
print(f'  M09-C VCGs: {len(m08c_descs)}; M22/God-directed/glorying mention present: {has_m22}')
m08e_descs = [s['description'].lower() for s in all_vcg_specs if s['subgroup_code'] == 'M09-E']
has_m23 = any('m23' in d or 'strength' in d or 'power' in d or 'authority' in d or 'dominion' in d for d in m08e_descs)
print(f'  M09-E VCGs: {len(m08e_descs)}; M23/strength/power/authority mention present: {has_m23}')

print()
if errors:
    print(f'=== VALIDATION FAILED — {len(errors)} errors ===')
    for e in errors[:30]:
        print(f'  - {e}')
    if len(errors) > 30:
        print(f'  ... and {len(errors) - 30} more')
    sys.exit(1)
else:
    print('=== VALIDATION PASSED ===')
    print(f'Ready to apply: {total_vcgs} VCGs across {len(data["subgroups"])} sub-groups, {total_in_json} verse assignments.')
conn.close()
