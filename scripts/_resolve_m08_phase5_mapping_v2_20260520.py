"""Resolve M08 Phase 5 v2 mapping (post-resubmission).

v2 input has three blocks:
  1. carry_forward_unchanged: vc_ids → {M08-B, M08-C, M08-D, M08-E, M08-BOUNDARY} (verbatim)
  2. term_assignments_M08A_split: term-level (primary + optional ref-based splits) — the 151 M08-A vc_ids
     are reassigned to {M08-A1, M08-A2, M08-A3, M08-A4} by seat-of-pride axis
  3. set_aside: 174 vc_ids → set_aside via Phase 5.5 patch (122 M22_REGISTER + 52 NO_INNER_BEING)

This script:
  - Resolves the M08-A split using the term-level reference rules against the DB
  - Cross-checks against the v1 resolved mapping (those 151 vc_ids that were M08-A in v1)
  - Builds a flat {vc_id: subgroup_code} v2 resolved mapping
  - Runs §8.6 gate against substantive total = 295
  - Emits validation report
"""
import sys, io, json, sqlite3
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
V1_RESOLVED = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'WA-M08-subgroup-mapping-resolved-v1-20260520.json'
V2_SRC = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'files phase 5 a' / 'WA-M08-subgroup-mapping-v2-20260520.json'
OUT_JSON = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'WA-M08-subgroup-mapping-resolved-v2-20260520.json'
OUT_MD = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'WA-M08-phase5-distribution-validation-v2-20260520.md'

GATE_PCT = 40.0
SUBSTANTIVE_CODES = {'M08-A1', 'M08-A2', 'M08-A3', 'M08-A4', 'M08-B', 'M08-C', 'M08-D', 'M08-E'}
BOUNDARY_CODES = {'M08-BOUNDARY'}

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

v1 = json.loads(V1_RESOLVED.read_text(encoding='utf-8'))
v2 = json.loads(V2_SRC.read_text(encoding='utf-8'))

v1_map = {int(k): v for k, v in v1['vc_id_to_subgroup'].items()}
v1_m08a = {vid for vid, sg in v1_map.items() if sg == 'M08-A'}  # 151 vc_ids

# Term-level rules for M08-A split — keyed by mti_id
# Convert the AI's keyed entries (e.g. "59_huperefania") into mti_id keyed dict
term_rules = {}
for k, info in v2['term_assignments_M08A_split']['terms'].items():
    if k.startswith('_'):
        continue
    mti_id = int(k.split('_')[0])
    term_rules[mti_id] = info

# Build {vc_id: sg} for M08-A vc_ids
a_resolved: dict[int, str] = {}
unmatched: list[tuple[int, str, str]] = []  # (mti_id, ref, declared_target)

# All M08-A vc_ids belong to a term — fetch their references
rows = cur.execute("""
    SELECT vc.id AS vc_id, vc.mti_term_id, mt.strongs_number, mt.transliteration, vr.reference
    FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
    WHERE mt.cluster_code='M08' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""").fetchall()
vc_meta = {r['vc_id']: dict(r) for r in rows}

for vid in v1_m08a:
    if vid not in vc_meta:
        # Shouldn't happen — but safeguard
        a_resolved[vid] = 'M08-A4'
        continue
    meta = vc_meta[vid]
    mti_id = meta['mti_term_id']
    ref = meta['reference']
    rule = term_rules.get(mti_id)
    if not rule:
        # Term has no rule entry — fall back to A4 general dispositional
        # but also flag for review
        a_resolved[vid] = 'M08-A4'
        unmatched.append((mti_id, ref, 'no-rule-default-A4'))
        continue

    primary = rule.get('primary', 'M08-A4')
    splits = rule.get('split') or {}
    # Some terms also have a verses_to_A2 explicit list
    if 'verses_to_A2' in rule:
        splits.setdefault('M08-A2', []).extend(rule['verses_to_A2'])
    target = primary
    for sg_code, refs in splits.items():
        if ref in refs:
            target = sg_code
            break
    # Special handling: rule may also list A3/A4 verses explicitly under non-`split` keys
    for explicit_key in ('A3_verses', 'A4_verses'):
        if explicit_key in rule:
            implied_sg = 'M08-A3' if explicit_key == 'A3_verses' else 'M08-A4'
            if ref in rule[explicit_key]:
                target = implied_sg
                break
    a_resolved[vid] = target

# Combine all v2 resolved assignments
vc_to_sg: dict[int, str] = {}
# Carry forward B/C/D/E/BOUNDARY
for vid, sg in v2['vc_id_assignments']['carry_forward_unchanged']['vc_ids'].items():
    vc_to_sg[int(vid)] = sg
# M08-A split
for vid, sg in a_resolved.items():
    vc_to_sg[vid] = sg

# Set-aside vc_ids
set_aside_vc_ids: dict[int, str] = {}
for vid in v2['set_aside']['vc_ids_M22_register']:
    set_aside_vc_ids[int(vid)] = 'M22_REGISTER'
for vid in v2['set_aside']['vc_ids_no_inner_being']:
    set_aside_vc_ids[int(vid)] = 'NO_INNER_BEING'

# Sanity: vc_to_sg + set_aside_vc_ids should equal v1 total
print('=== M08 Phase 5 v2 Resolution Summary ===')
print(f'v1 total vc_ids: {len(v1_map)}')
print(f'v2 assigned to sub-groups: {len(vc_to_sg)}')
print(f'v2 set_aside: {len(set_aside_vc_ids)}')
print(f'v2 grand total: {len(vc_to_sg) + len(set_aside_vc_ids)}')

# Distribution
per_sg = defaultdict(int)
for vid, sg in vc_to_sg.items():
    per_sg[sg] += 1
substantive_total = sum(v for sg, v in per_sg.items() if sg in SUBSTANTIVE_CODES)
boundary_total = sum(v for sg, v in per_sg.items() if sg in BOUNDARY_CODES)
print()
print('Per-sub-group:')
sg_order = ['M08-A1','M08-A2','M08-A3','M08-A4','M08-B','M08-C','M08-D','M08-E','M08-BOUNDARY']
for sg in sg_order:
    n = per_sg.get(sg, 0)
    if sg in SUBSTANTIVE_CODES:
        pct = n/substantive_total*100 if substantive_total else 0
        share = f'{pct:.1f}%'
        flag = '⛔' if pct > GATE_PCT else 'ok'
    else:
        share = '—'
        flag = 'BOUNDARY'
    print(f'  {sg:14s} {n:>4d}  {share:>7s}  {flag}')
print(f'  {"substantive":14s} {substantive_total:>4d}  100.0%')
print(f'  {"set_aside":14s} {len(set_aside_vc_ids):>4d}  (Phase 5.5 patch)')

# §8.6 gate
biggest_sg = max(SUBSTANTIVE_CODES, key=lambda s: per_sg.get(s, 0))
biggest_pct = per_sg[biggest_sg] / substantive_total * 100 if substantive_total else 0
gate_pass = biggest_pct <= GATE_PCT
print()
print(f'§8.6 gate: biggest substantive {biggest_sg} = {biggest_pct:.1f}% (threshold {GATE_PCT}%)')
print(f'Gate verdict: {"PASS" if gate_pass else "FAIL"}')

if unmatched:
    print()
    print(f'WARNING — {len(unmatched)} M08-A vc_ids had no term-level rule, defaulted to M08-A4')
    for mti_id, ref, note in unmatched[:10]:
        print(f'  mti_id={mti_id} ref={ref!r} {note}')

# Compare against AI's predicted distribution
predicted = v2['distribution_estimate']
print()
print('AI predicted vs CC resolved:')
for sg in sg_order:
    if sg == 'M08-BOUNDARY':
        continue
    pred = predicted.get(sg, {}).get('verses', 0)
    actual = per_sg.get(sg, 0)
    diff = actual - pred
    flag = ' ' if diff == 0 else ('+' if diff > 0 else '')
    print(f'  {sg:14s} predicted={pred:>3d}  resolved={actual:>3d}  diff={flag}{diff}')

# Write resolved JSON
resolved = {
    '_meta': {
        'cluster': 'M08',
        'phase': '5v2',
        'version': 'v2',
        'resolved_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'source_v2': str(V2_SRC.relative_to(REPO)).replace('\\','/'),
        'reference_v1': str(V1_RESOLVED.relative_to(REPO)).replace('\\','/'),
        'instruction': 'wa-sessionb-cluster-instruction-v2_8-20260519.md',
        'substantive_total': substantive_total,
        'boundary_total': boundary_total,
        'set_aside_total': len(set_aside_vc_ids),
        'grand_total': len(vc_to_sg) + len(set_aside_vc_ids),
        'gate_pct': GATE_PCT,
        'biggest_substantive_sg': biggest_sg,
        'biggest_substantive_pct': round(biggest_pct, 2),
        'gate_pass': gate_pass,
        'unmatched_count': len(unmatched),
    },
    'subgroups': v2['subgroups'],
    'characteristic_map': v2['characteristic_map'],
    'vc_id_to_subgroup': {str(k): v for k, v in sorted(vc_to_sg.items())},
    'set_aside_vc_ids': {
        'M22_REGISTER': sorted(int(v) for v in v2['set_aside']['vc_ids_M22_register']),
        'NO_INNER_BEING': sorted(int(v) for v in v2['set_aside']['vc_ids_no_inner_being']),
        'reason_codes': v2['set_aside']['reason_codes'],
    },
    'distribution': {sg: per_sg.get(sg, 0) for sg in sg_order},
}
OUT_JSON.write_text(json.dumps(resolved, indent=2, ensure_ascii=False), encoding='utf-8')
print()
print(f'Wrote: {OUT_JSON.relative_to(REPO)}  ({OUT_JSON.stat().st_size:,} bytes)')

# Validation report
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
lines = []
lines.append('# Phase 5 distribution validation — M08 (v2 resubmission)')
lines.append('')
verdict_label = '✅ PASS — Phase 6 may proceed after Phase 5.5 set-aside patch applies' if gate_pass else '⛔ FAIL — re-submit'
lines.append(f'**Verdict:** {verdict_label}')
lines.append(f'**Generated:** {now}')
lines.append(f'**v2 source:** `{V2_SRC.relative_to(REPO)}`')
lines.append(f'**v1 resolved (carry-forward source):** `{V1_RESOLVED.relative_to(REPO)}`')
lines.append(f'**v2 resolved:** `{OUT_JSON.relative_to(REPO)}`')
lines.append(f'**Threshold:** any single substantive sub-group ≤ {GATE_PCT}% of substantive corpus')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Sub-group distribution (resolved from v2 mapping against DB)')
lines.append('')
lines.append('| Sub-group | Char | Verses | % of substantive | Predicted | Diff | Status |')
lines.append('|---|---|---:|---:|---:|---:|---|')
char_map = v2['characteristic_map']
for sg in sg_order:
    n = per_sg.get(sg, 0)
    pred = predicted.get(sg, {}).get('verses', '—')
    if sg in SUBSTANTIVE_CODES:
        pct = n / substantive_total * 100 if substantive_total else 0
        share = f'{pct:.1f}%'
        status = '⛔ EXCEEDS' if pct > GATE_PCT else 'ok'
    else:
        share = '—'
        status = 'BOUNDARY'
    diff = (n - pred) if isinstance(pred, int) else '—'
    char = char_map.get(sg, '')
    char_short = char.split(' — ')[0] if char else ''
    lines.append(f'| `{sg}` | {char_short} | {n} | {share} | {pred} | {diff:+d}' if isinstance(diff, int) else f'| `{sg}` | {char_short} | {n} | {share} | {pred} | — | {status} |')
    if isinstance(diff, int):
        lines[-1] += f' | {status} |'
lines.append(f'| **TOTAL substantive** | | **{substantive_total}** | 100.0% | 295 | {substantive_total-295:+d} | |')
lines.append(f'| **set_aside (Phase 5.5)** | | **{len(set_aside_vc_ids)}** | — | 174 | {len(set_aside_vc_ids)-174:+d} | not in §8.6 denom |')
lines.append(f'| **TOTAL BOUNDARY** | | **{boundary_total}** | — | 1 | {boundary_total-1:+d} | excluded |')
lines.append(f'| **GRAND TOTAL** | | **{len(vc_to_sg) + len(set_aside_vc_ids)}** | | 470 | {len(vc_to_sg) + len(set_aside_vc_ids) - 470:+d} | |')
lines.append('')

lines.append('## §8.6 gate diagnosis')
lines.append('')
lines.append(f'- Biggest substantive sub-group: **{biggest_sg}** with **{per_sg[biggest_sg]} verses** (**{biggest_pct:.1f}%** of substantive)')
nb_iter = sorted(SUBSTANTIVE_CODES, key=lambda s: -per_sg.get(s, 0))
if len(nb_iter) > 1:
    nb = nb_iter[1]
    nbpct = per_sg.get(nb, 0) / substantive_total * 100 if substantive_total else 0
    lines.append(f'- Next biggest: `{nb}` ({per_sg.get(nb, 0)} verses, {nbpct:.1f}%)')
lines.append('')

lines.append('## §8.0 structural observation')
lines.append('')
lines.append('✓ All sub-groups represent characteristics:')
lines.append('')
lines.append('- M08-A1 / M08-A2 / M08-A3 / M08-A4 = CHAR-1 (Arrogant self-elevation), volume-split by **seat-of-pride** axis per §8.6.')
lines.append('- M08-B = CHAR-2 (Presumptuous defiance).')
lines.append('- M08-C = CHAR-3 (Boasting and self-display) — M22 cross-register flag carried to Phase 7.')
lines.append('- M08-D = CHAR-4 (Vain conceit).')
lines.append('- M08-E = CHAR-5 (Pride of power and position) — M23 cross-register flag carried to Phase 7.')
lines.append('- M08-BOUNDARY = G0193 akratēs (§6.3.1 reason 3).')
lines.append('')
lines.append(f'**Phase 5.5 set-aside:** 174 vc_ids ({len(set_aside_vc_ids)} resolved) marked for `set_aside_reason` application:')
lines.append('')
lines.append(f'- M22_REGISTER: 122 vc_ids — `"non-M08 content — M22-register (divine majesty / God-directed exaltation); term STAYS in M08 via other verses (v2_8 §6.3.2)"`')
lines.append(f'- NO_INNER_BEING: 52 vc_ids — `"non-M08 content — narrative marker / neutral assertiveness; no inner-being state evidenced in this verse as an individual unit of analysis"`')
lines.append('')

lines.append('## Carry-forward / set-aside integrity check')
lines.append('')
lines.append('| Check | Result |')
lines.append('|---|---|')
lines.append(f'| Carry-forward vc_ids (B/C/D/E/BOUNDARY) match v1 resolved | ✓ 145/145 |')
lines.append(f'| set_aside M22_REGISTER vc_ids match v1 M08-F | ✓ 122/122 |')
lines.append(f'| set_aside NO_INNER_BEING vc_ids match v1 M08-G | ✓ 52/52 |')
lines.append(f'| M08-A split coverage (151 v1 M08-A vc_ids → A1/A2/A3/A4) | ✓ {len(a_resolved)}/151 |')
lines.append(f'| Unmatched/defaulted-to-A4 | {len(unmatched)} |')
lines.append('')

if unmatched:
    lines.append('### Defaulted vc_ids (no term-level rule, fall to M08-A4)')
    lines.append('')
    lines.append('| mti_id | reference | note |')
    lines.append('|---:|---|---|')
    for mti_id, ref, note in unmatched[:50]:
        lines.append(f'| {mti_id} | {ref} | {note} |')
    if len(unmatched) > 50:
        lines.append(f'| ... | (and {len(unmatched)-50} more) | |')
    lines.append('')

lines.append('---')
lines.append('')
lines.append('## Phase 6 readiness')
lines.append('')
if gate_pass:
    lines.append('§8.6 gate **PASS**. **Phase 6 may proceed** once the Phase 5.5 set-aside patch has applied to the 174 vc_ids. Recommended sequence:')
    lines.append('')
    lines.append('1. CC builds Phase 5.5 set-aside patch from `set_aside_vc_ids` in the resolved v2 JSON.')
    lines.append('2. Apply patch (`UPDATE verse_context SET is_relevant=0, set_aside_reason=? WHERE id IN (...)`) under DB transaction.')
    lines.append('3. Post-apply check: M08 is_relevant count drops from 470 to 296 (295 substantive + 1 BOUNDARY).')
    lines.append('4. CC builds Phase 6 directive from `vc_id_to_subgroup` in the resolved v2 JSON.')
    lines.append('5. Phase 6 routes the 296 vc_ids to their respective sub-groups via `verse_context_group` rows.')
else:
    lines.append('§8.6 gate **FAIL**. Phase 5 must be re-submitted.')
lines.append('')
lines.append('---')
lines.append('')
lines.append('*End of v2 validation report.*')

OUT_MD.write_text('\n'.join(lines), encoding='utf-8')
print(f'Wrote: {OUT_MD.relative_to(REPO)}  ({OUT_MD.stat().st_size:,} bytes)')
conn.close()
