"""Resolve M09 Phase 5 mapping from AI's reference-based JSON to flat vc_id mapping.

Input:  Sessions/Session_Clusters/M09/wa-cluster-M09-subgroup-mapping-v1-20260521.json
        (term_mappings with reference + subgroup + optional flag)

Output: Sessions/Session_Clusters/M09/wa-cluster-M09-subgroup-mapping-resolved-v1-20260521.json
        (flat {vc_id: subgroup_code} + distribution stats + §8.6 gate verdict + flag manifests)
"""
import sys, io, json, sqlite3, re
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
SRC = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'wa-cluster-M09-subgroup-mapping-v1-20260521.json'
OUT_JSON = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'wa-cluster-M09-subgroup-mapping-resolved-v1-20260521.json'
OUT_MD = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'wa-cluster-M09-phase5-distribution-validation-v1-20260521.md'

GATE_PCT = 40.0
SUBSTANTIVE_CODES = {'M09-A', 'M09-B', 'M09-C', 'M09-D', 'M09-E', 'M09-F', 'M09-G', 'M09-H'}
BOUNDARY_CODES: set[str] = set()  # M09 has no BOUNDARY sub-group (0 BOUNDARY verdicts)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

spec = json.loads(SRC.read_text(encoding='utf-8'))

# Build vc_id resolution: for each term, fetch all is_relevant vc rows with reference
vc_to_sg: dict[int, str] = {}
phase_8_5_flags: list[dict] = []
phase_5_5_flags: list[dict] = []
unmatched: list[dict] = []

for tm in spec['term_mappings']:
    mti_id = tm['mti_id']
    strongs = tm['strongs']
    # Pull all is_relevant vc rows for this term
    db_rows = cur.execute("""
        SELECT vc.id AS vc_id, vr.reference
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE vc.mti_term_id=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """, (mti_id,)).fetchall()
    db_map = {r['reference']: r['vc_id'] for r in db_rows}

    for asn in tm['assignments']:
        ref = asn['verse_ref']
        sg = asn['subgroup']
        flag = asn.get('flag')
        # Try direct match
        vc_id = db_map.get(ref)
        # Also try with non-breaking-space normalisations
        if vc_id is None:
            # Try alternative book name forms — but mostly just print unmatched
            unmatched.append({'mti_id': mti_id, 'strongs': strongs, 'reference': ref, 'target_sg': sg, 'flag': flag})
            continue
        vc_to_sg[vc_id] = sg
        if flag == 'PHASE_8_5_FLAG':
            phase_8_5_flags.append({'vc_id': vc_id, 'mti_id': mti_id, 'strongs': strongs, 'reference': ref, 'subgroup': sg})
        elif flag == 'PHASE_5_5_SET_ASIDE_CANDIDATE':
            phase_5_5_flags.append({'vc_id': vc_id, 'mti_id': mti_id, 'strongs': strongs, 'reference': ref, 'subgroup': sg})

# Distribution
per_sg = defaultdict(int)
for vc_id, sg in vc_to_sg.items():
    per_sg[sg] += 1
substantive_total = sum(per_sg[sg] for sg in SUBSTANTIVE_CODES)
grand_total = sum(per_sg.values())

print('=== M09 Phase 5 Resolution Summary ===')
print(f'Total vc_id assignments: {grand_total}')
print(f'Unmatched references: {len(unmatched)}')
print()
print('Per-sub-group:')
for sg in sorted(SUBSTANTIVE_CODES | BOUNDARY_CODES):
    n = per_sg.get(sg, 0)
    pct = n / substantive_total * 100 if sg in SUBSTANTIVE_CODES and substantive_total else 0
    pct_str = f'{pct:.1f}%' if sg in SUBSTANTIVE_CODES else '—'
    flag = '⛔' if pct > GATE_PCT else 'ok'
    print(f'  {sg:14s} {n:>4d}  {pct_str:>7s}  ({flag})')

# §8.6 gate
biggest_sg = max(SUBSTANTIVE_CODES, key=lambda s: per_sg.get(s, 0))
biggest_pct = per_sg[biggest_sg] / substantive_total * 100 if substantive_total else 0
gate_pass = biggest_pct <= GATE_PCT
print()
print(f'§8.6 gate: biggest {biggest_sg} = {biggest_pct:.1f}% (threshold {GATE_PCT}%)')
print(f'Verdict: {"PASS" if gate_pass else "FAIL"}')
print()
print(f'PHASE_8_5_FLAG vc_ids: {len(phase_8_5_flags)}')
print(f'PHASE_5_5_SET_ASIDE_CANDIDATE vc_ids: {len(phase_5_5_flags)}')

if unmatched:
    print()
    print(f'UNMATCHED references (need investigation):')
    for u in unmatched[:15]:
        print(f'  mti={u["mti_id"]} {u["strongs"]} ref={u["reference"]!r} → declared {u["target_sg"]}')

# Cross-check: expected counts from spec
print()
print('Expected vs resolved per sub-group:')
for sg_spec in spec['subgroups']:
    sg = sg_spec['subgroup_code']
    expected = sg_spec.get('expected_vc_ids', 0)
    actual = per_sg.get(sg, 0)
    flag = '✓' if expected == actual else '✗'
    print(f'  {flag} {sg}: expected={expected} resolved={actual} diff={actual-expected:+d}')

# Write resolved
resolved = {
    '_meta': {
        'cluster': 'M09',
        'phase': 5,
        'resolved_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'source': str(SRC.relative_to(REPO)).replace('\\','/'),
        'substantive_total': substantive_total,
        'grand_total': grand_total,
        'gate_pct': GATE_PCT,
        'biggest_substantive_sg': biggest_sg,
        'biggest_substantive_pct': round(biggest_pct, 2),
        'gate_pass': gate_pass,
        'unmatched_count': len(unmatched),
        'phase_8_5_flag_count': len(phase_8_5_flags),
        'phase_5_5_flag_count': len(phase_5_5_flags),
    },
    'subgroups': {sg['subgroup_code']: sg['label'] for sg in spec['subgroups']},
    'vc_id_to_subgroup': {str(k): v for k, v in sorted(vc_to_sg.items())},
    'distribution': {sg: per_sg.get(sg, 0) for sg in sorted(SUBSTANTIVE_CODES)},
    'phase_8_5_flags': phase_8_5_flags,
    'phase_5_5_flags': phase_5_5_flags,
    'unmatched': unmatched,
}
OUT_JSON.write_text(json.dumps(resolved, indent=2, ensure_ascii=False), encoding='utf-8')
print()
print(f'Wrote: {OUT_JSON.relative_to(REPO)} ({OUT_JSON.stat().st_size:,} bytes)')

# Brief validation report
lines = []
lines.append('# Phase 5 distribution validation — M09')
lines.append('')
lines.append(f'**Verdict:** {"✅ PASS — Phase 6 may proceed" if gate_pass else "⛔ FAIL"}')
lines.append(f'**Generated:** {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}')
lines.append(f'**Substantive total:** {substantive_total} verses')
lines.append(f'**§8.6 gate:** biggest substantive sub-group ≤ {GATE_PCT}% of substantive corpus')
lines.append('')
lines.append('## Sub-group distribution')
lines.append('')
lines.append('| Sub-group | Char | Verses | % of substantive | Status |')
lines.append('|---|---|---:|---:|---|')
for sg in sorted(SUBSTANTIVE_CODES):
    n = per_sg.get(sg, 0)
    pct = n / substantive_total * 100 if substantive_total else 0
    status = '⛔ EXCEEDS' if pct > GATE_PCT else 'ok'
    char = next((s.get('characteristic','?') for s in spec['subgroups'] if s['subgroup_code'] == sg), '?')
    lines.append(f'| `{sg}` | {char} | {n} | {pct:.1f}% | {status} |')
lines.append(f'| **TOTAL substantive** | | **{substantive_total}** | 100.0% | |')
lines.append('')
lines.append('## §8.6 gate diagnosis')
lines.append('')
lines.append(f'- Biggest: `{biggest_sg}` with {per_sg[biggest_sg]} verses ({biggest_pct:.1f}%)')
nb = sorted(SUBSTANTIVE_CODES, key=lambda s: -per_sg.get(s, 0))[1]
nbpct = per_sg.get(nb, 0) / substantive_total * 100 if substantive_total else 0
lines.append(f'- Next biggest: `{nb}` ({per_sg.get(nb, 0)} verses, {nbpct:.1f}%)')
lines.append('')
lines.append('## Phase 8.5 flags (11 diatassō verses)')
lines.append('')
lines.append('These are provisionally routed to M09-D for Phase 5/6 structural integrity. Phase 8.5 will resolve: SET-ASIDE or ROUTE-TO-M23.')
lines.append('')
for f in phase_8_5_flags:
    lines.append(f'- vc={f["vc_id"]} {f["strongs"]} {f["reference"]} → {f["subgroup"]}')
lines.append('')
lines.append('## Phase 5.5 set-aside candidate')
lines.append('')
for f in phase_5_5_flags:
    lines.append(f'- vc={f["vc_id"]} {f["strongs"]} {f["reference"]} (currently in {f["subgroup"]})')
lines.append('')
lines.append('## Phase 6 readiness')
lines.append('')
if gate_pass:
    lines.append('§8.6 gate PASS. Phase 6 may proceed. Recommended sequence:')
    lines.append('')
    lines.append('1. (No Phase 5.5 patch needed pre-Phase-6 — keep tapeinoō Luk 3:5 in M09-A; Phase 5.5 patch optional or defer to Phase 8.5 alongside the diatassō flags.)')
    lines.append('2. CC builds Phase 6 directive from resolved JSON.')
    lines.append('3. Phase 6 routes 109 vc_ids to verse_context_group rows under their respective sub-group codes.')
else:
    lines.append('§8.6 gate FAIL. Phase 5 must be re-submitted.')
lines.append('')
lines.append('---')
lines.append('*End of v1 validation report.*')

OUT_MD.write_text('\n'.join(lines), encoding='utf-8')
print(f'Wrote: {OUT_MD.relative_to(REPO)}')
conn.close()
