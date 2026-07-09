"""Resolve M08 Phase 5 mapping from AI's term-level JSON to vc_id-level flat JSON.

Input:  Sessions/Session_Clusters/M08/files phase 5/WA-M08-subgroup-mapping-v1-20260520.json
        (term_assignments keyed by mti_id with `primary` + `split` by Bible reference)

Output: Sessions/Session_Clusters/M08/WA-M08-subgroup-mapping-resolved-v1-20260520.json
        (flat {vc_id: subgroup_code} + distribution stats)

Also computes the §8.6 distribution gate and a structural-observation flag if
non-characteristic holding sub-groups are present (M08-F / M08-G).
"""
import sys, io, json, sqlite3
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
SRC = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'files phase 5' / 'WA-M08-subgroup-mapping-v1-20260520.json'
OUT_JSON = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'WA-M08-subgroup-mapping-resolved-v1-20260520.json'
OUT_MD = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'WA-M08-phase5-distribution-validation-v1-20260520.md'

GATE_PCT = 40.0

# Sub-groups that are documented as non-characteristic holding pens (not part of substantive total per AI design)
HOLDING_CODES = {'M08-F', 'M08-G'}
BOUNDARY_CODES = {'M08-BOUNDARY'}

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

spec = json.loads(SRC.read_text(encoding='utf-8'))
subgroups = spec['subgroups']
term_asn = spec['term_assignments']

# vc_id -> subgroup_code
vc_to_sg: dict[int, str] = {}
unmatched_refs: list[tuple[int, str, str, str]] = []  # mti_id, strongs, ref, target_sg

for mti_str, info in term_asn.items():
    mti_id = int(mti_str)
    primary = info['primary']
    splits = info.get('split') or {}

    # Build reference -> target_sg map for this term's splits
    ref_to_sg: dict[str, str] = {}
    for target_sg, refs in splits.items():
        for ref in refs:
            ref_to_sg[ref.strip()] = target_sg

    # Pull all is_relevant vc rows for this term
    rows = cur.execute("""
        SELECT vc.id AS vc_id, vr.reference
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE vc.mti_term_id=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num, vc.id
    """, (mti_id,)).fetchall()

    matched_refs = set()
    for r in rows:
        vc_id = r['vc_id']
        ref = r['reference']
        target = ref_to_sg.get(ref, primary)
        vc_to_sg[vc_id] = target
        if ref in ref_to_sg:
            matched_refs.add(ref)

    # Find split refs that didn't match any vc row (e.g. typos, set_aside Phase 1 verses)
    declared_refs = set(ref_to_sg.keys())
    missing = declared_refs - matched_refs
    for ref in sorted(missing):
        unmatched_refs.append((mti_id, info['strongs'], ref, ref_to_sg[ref]))

# Distribution
per_sg = defaultdict(int)
for vc_id, sg in vc_to_sg.items():
    per_sg[sg] += 1

substantive_total = sum(v for sg, v in per_sg.items()
                        if sg not in HOLDING_CODES and sg not in BOUNDARY_CODES)
holding_total = sum(v for sg, v in per_sg.items() if sg in HOLDING_CODES)
boundary_total = sum(v for sg, v in per_sg.items() if sg in BOUNDARY_CODES)
grand_total = sum(per_sg.values())

print('=== M08 Phase 5 Resolution Summary ===')
print(f'Total vc_id assignments: {grand_total}')
print(f'  Substantive (M08-A..E): {substantive_total}')
print(f'  Holding (M08-F/G):      {holding_total}')
print(f'  BOUNDARY:               {boundary_total}')
print(f'  Unmatched split refs:   {len(unmatched_refs)}')
print()
print('Per-sub-group:')
for sg in sorted(per_sg, key=lambda s: (-per_sg[s], s)):
    is_holding = sg in HOLDING_CODES
    is_boundary = sg in BOUNDARY_CODES
    if is_holding:
        tag = 'HOLDING'
        share = '—'
    elif is_boundary:
        tag = 'BOUNDARY'
        share = '—'
    else:
        tag = 'substantive'
        pct = per_sg[sg] / substantive_total * 100 if substantive_total else 0
        share = f'{pct:.1f}%'
    print(f'  {sg:18s} {per_sg[sg]:>4d}  {share:>7s}  ({tag})  {subgroups.get(sg,"")}')

# §8.6 gate (against substantive total)
biggest_sg = max((sg for sg in per_sg if sg not in HOLDING_CODES and sg not in BOUNDARY_CODES),
                 key=lambda s: per_sg[s])
biggest_pct = per_sg[biggest_sg] / substantive_total * 100 if substantive_total else 0
gate_pass = biggest_pct <= GATE_PCT
print()
print(f'§8.6 gate: biggest substantive {biggest_sg} = {biggest_pct:.1f}% (threshold {GATE_PCT}%)')
print(f'Gate verdict: {"PASS" if gate_pass else "FAIL"}')

# Structural-observation flag
holding_present = holding_total > 0
print()
print(f'v2_8 §8.0 structural observation:')
if holding_present:
    print(f'  ⚠ Non-characteristic holding sub-groups present ({", ".join(sorted(HOLDING_CODES))})')
    print(f'  {holding_total} verses ({holding_total/grand_total*100:.1f}% of total) in holding sub-groups')
    print(f'  These are routed to Phase 8.5 for resolution (ROUTE-TO-CLUSTER M22 or SET-ASIDE).')
    print(f'  Researcher confirmation required: accept holding-sub-group pattern?')
else:
    print(f'  ✓ All sub-groups are characteristic (1:1 default per §8.0)')

if unmatched_refs:
    print()
    print(f'WARNING — {len(unmatched_refs)} split references did not match any is_relevant vc row:')
    for mti_id, strongs, ref, target_sg in unmatched_refs[:20]:
        print(f'  mti_id={mti_id} {strongs} ref={ref!r} → declared {target_sg} (no matching vc)')
    if len(unmatched_refs) > 20:
        print(f'  ... and {len(unmatched_refs) - 20} more')

# Write resolved JSON
resolved = {
    '_meta': {
        'cluster': 'M08',
        'phase': 5,
        'resolved_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'source': str(SRC.relative_to(REPO)).replace('\\', '/'),
        'instruction': 'wa-sessionb-cluster-instruction-v2_8-20260519.md',
        'total_assignments': grand_total,
        'substantive_total': substantive_total,
        'holding_total': holding_total,
        'boundary_total': boundary_total,
        'gate_pct': GATE_PCT,
        'biggest_substantive_sg': biggest_sg,
        'biggest_substantive_pct': round(biggest_pct, 2),
        'gate_pass': gate_pass,
        'holding_codes': sorted(HOLDING_CODES),
        'unmatched_refs_count': len(unmatched_refs),
    },
    'subgroups': subgroups,
    'vc_id_to_subgroup': {str(k): v for k, v in sorted(vc_to_sg.items())},
    'distribution': {sg: per_sg[sg] for sg in sorted(per_sg)},
    'unmatched_refs': [
        {'mti_id': mid, 'strongs': s, 'reference': r, 'target_sg': t}
        for (mid, s, r, t) in unmatched_refs
    ],
}
OUT_JSON.write_text(json.dumps(resolved, indent=2, ensure_ascii=False), encoding='utf-8')
print()
print(f'Wrote resolved JSON: {OUT_JSON.relative_to(REPO)}')
print(f'  size: {OUT_JSON.stat().st_size:,} bytes')

# Write distribution-validation report
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
lines = []
lines.append(f'# Phase 5 distribution validation — M08')
lines.append('')
verdict_label = '✅ PASS — Phase 6 may proceed (subject to structural observation below)' if gate_pass else '⛔ FAIL — Phase 5 must be re-submitted'
lines.append(f'**Verdict:** {verdict_label}')
lines.append(f'**Generated:** {now}')
lines.append(f'**Mapping (resolved):** `{OUT_JSON.relative_to(REPO)}`')
lines.append(f'**Mapping (AI source):** `{SRC.relative_to(REPO)}`')
lines.append(f'**Threshold:** any single substantive sub-group ≤ {GATE_PCT}% of substantive corpus')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Sub-group distribution')
lines.append('')
lines.append('| Sub-group | Verses | % of substantive | Type | Status |')
lines.append('|---|---:|---:|---|---|')
for sg in sorted(per_sg, key=lambda s: (-per_sg[s], s)):
    n = per_sg[sg]
    if sg in HOLDING_CODES:
        share = '—'; typ = 'Holding (non-characteristic)'; status = '⚠ §8.0 observation'
    elif sg in BOUNDARY_CODES:
        share = '—'; typ = 'BOUNDARY'; status = 'excluded from gate'
    else:
        pct = n / substantive_total * 100 if substantive_total else 0
        share = f'{pct:.1f}%'; typ = 'Characteristic'
        status = '⛔ EXCEEDS THRESHOLD' if pct > GATE_PCT else 'ok'
    desc = subgroups.get(sg, '')
    lines.append(f'| `{sg}` | {n} | {share} | {typ} | {status} |')
lines.append(f'| **TOTAL substantive** | **{substantive_total}** | 100.0% | | |')
lines.append(f'| **TOTAL holding** | **{holding_total}** | — | | |')
lines.append(f'| **TOTAL BOUNDARY** | **{boundary_total}** | — | | |')
lines.append(f'| **GRAND TOTAL** | **{grand_total}** | | | |')
lines.append('')
lines.append('## §8.6 gate diagnosis')
lines.append('')
lines.append(f'- Biggest substantive sub-group: **{biggest_sg}** with **{per_sg[biggest_sg]} verses** (**{biggest_pct:.1f}%** of substantive)')
nb_iter = sorted((sg for sg in per_sg if sg not in HOLDING_CODES and sg not in BOUNDARY_CODES), key=lambda s: -per_sg[s])
if len(nb_iter) > 1:
    nb = nb_iter[1]
    nbpct = per_sg[nb] / substantive_total * 100
    lines.append(f'- Next biggest: `{nb}` ({per_sg[nb]} verses, {nbpct:.1f}%)')
lines.append('')
lines.append('## §8.0 structural observation — holding sub-groups')
lines.append('')
if holding_present:
    lines.append('⚠ **Two non-characteristic holding sub-groups are present** in this Phase 5 design:')
    lines.append('')
    for sg in sorted(HOLDING_CODES):
        n = per_sg.get(sg, 0)
        desc = subgroups.get(sg, '')
        lines.append(f'- `{sg}` ({n} verses) — {desc}')
    lines.append('')
    lines.append(f'Total holding verses: **{holding_total}** ({holding_total/grand_total*100:.1f}% of all assignments).')
    lines.append('')
    lines.append('### Rationale (from AI design §5)')
    lines.append('')
    lines.append('M08\'s polysemic height vocabulary (rum, ga.on, ga.vah, ga.a.vah, ha.lal, ma.rom, etc.) carries genuine dual reference: same lexeme used for human pride AND for divine majesty / God-directed glorying. Phase 1 filtered most divine-majesty uses, but ~120 surfaced as `is_relevant` to M08 because the verse carries M22-register content that requires post-Phase-5 routing. Similarly, archō has 48 temporal-narrative-marker uses that have no inner-being content at all.')
    lines.append('')
    lines.append('Per v2_8 §6.3.2, these terms STAY in M08 because *some* verses evidence M08-relational content. But not every verse of a STAYS term is itself a pride verse. The AI\'s design routes those non-M08 verses to two holding sub-groups:')
    lines.append('')
    lines.append('- **M08-F** (cross-register holding) — verses with M22-register content, awaiting Phase 8.5 ROUTE-TO-CLUSTER M22 or SET-ASIDE decision.')
    lines.append('- **M08-G** (marginal/narrative holding) — verses with no inner-being content (narrative markers, neutral assertiveness), awaiting Phase 8.5 SET-ASIDE decision.')
    lines.append('')
    lines.append('### Compliance question for researcher')
    lines.append('')
    lines.append('v2_8 §8.0 states: *"A sub-group represents a characteristic. Default 1:1; volume-split via §8.6 40% gate is the documented exception."*')
    lines.append('')
    lines.append('Holding sub-groups are a **third pattern** not yet documented in v2_8. They emerge naturally from the M08-specific reality of polysemic vocabulary surviving Phase 1, but they violate the "sub-groups represent characteristics" rule literally read.')
    lines.append('')
    lines.append('**Three resolution options for researcher consideration:**')
    lines.append('')
    lines.append('1. **Accept (default).** Treat M08-F / M08-G as documented holding-pen sub-groups for cross-register content. Phase 8.5 resolves them (ROUTE-TO-CLUSTER M22 or SET-ASIDE). Codify the pattern in v2_9 of the instruction (new §8.4.2 — "Cross-register holding sub-groups for polysemic vocabulary").')
    lines.append('')
    lines.append('2. **Set-aside at Phase 5.** Mark the holding-sub-group verses as `set_aside_reason="non-M08-content (M22-register OR no-inner-being)"` via a Phase 5.5 patch, before Phase 6 routing. Removes the holding sub-groups from the cluster structure. Loses the audit trail of which terms contributed which residuals.')
    lines.append('')
    lines.append('3. **Push back to AI.** Ask AI to re-route these verses into existing substantive sub-groups (e.g. M08-A as "self-elevation including divine majesty by contrast"). Risks distorting characteristic definitions and reduces analytical clarity.')
    lines.append('')
    lines.append('**Recommended (CC):** Option 1 — the holding-sub-group pattern is honest, preserves audit trail, and aligns with v2_8 spirit (Phase 8.5 was already the documented BOUNDARY-resolution mechanism; extending it to polysemic-residual resolution is a natural fit).')
else:
    lines.append('✓ All sub-groups are characteristic (1:1 default per §8.0).')
lines.append('')
lines.append('## Unmatched split references')
lines.append('')
if unmatched_refs:
    lines.append(f'**{len(unmatched_refs)}** split references declared by AI did not match any `is_relevant=1` `verse_context` row:')
    lines.append('')
    lines.append('| mti_id | Strong\'s | Reference | Declared target |')
    lines.append('|---:|---|---|---|')
    for mid, s, r, t in unmatched_refs[:50]:
        lines.append(f'| {mid} | {s} | {r} | {t} |')
    if len(unmatched_refs) > 50:
        lines.append(f'| ... | | (and {len(unmatched_refs)-50} more) | |')
    lines.append('')
    lines.append('Likely cause: AI cited references that were Phase 1 SET-ASIDE (not is_relevant) or are in the term\'s set-aside corpus. Verses fall to the primary sub-group by default — no action required unless researcher decides to follow up.')
else:
    lines.append('✓ All split references match `is_relevant=1` verse_context rows.')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Phase 6 readiness')
lines.append('')
if gate_pass:
    lines.append('The §8.6 gate passes. **Phase 6 may proceed once the §8.0 structural observation is acknowledged by the researcher** (see "Three resolution options" above).')
else:
    lines.append('The §8.6 gate fails. Phase 5 must be re-submitted.')
lines.append('')
lines.append('---')
lines.append('')
lines.append('*End of validation report.*')

OUT_MD.write_text('\n'.join(lines), encoding='utf-8')
print(f'Wrote validation report: {OUT_MD.relative_to(REPO)}')
print(f'  size: {OUT_MD.stat().st_size:,} bytes')
conn.close()
