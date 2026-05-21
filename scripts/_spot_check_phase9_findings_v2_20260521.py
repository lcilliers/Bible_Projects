"""Spot-check a Phase 9 per-characteristic findings file against quality gates.

Generalized version: pass --cluster M08 --char-seq 2 (etc.) and it locates the
findings file by convention and runs the same checks as the M08 CHAR-1 v1 spot-check.

Checks:
  1. Per-prompt block parsed (T#.#.# header + [CHAR-N] outcome + body)
  2. Per-tier counts match catalogue tier sizes
  3. [CHAR-N] scope marker — must match --char-seq
  4. E findings: cite at least one Bible-reference token OR a VCG code
  5. Cited refs against the characteristic's actual corpus (cross-character drift detector)
  6. Cross-tier reference signals ("see T#", "as noted in T#")
  7. Bulk-classification (identical 80-char openings across 3+ prompts)
  8. Self-check block presence

Usage:
  python scripts/_spot_check_phase9_findings_v2_20260521.py --cluster M08 --char-seq 2
"""
import sys, io, re, sqlite3, argparse
from pathlib import Path
from collections import defaultdict, Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'

TIER_SIZES = {'T0': 12, 'T1': 24, 'T2': 31, 'T3': 33, 'T4': 24, 'T5': 21, 'T6': 24, 'T7': 20}
BIBLE_REF_RE = re.compile(r'\b(?:[1-3] ?)?[A-Z][a-z]{1,4}\.? \d+:\d+(?:[–\-]\d+)?\b')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cluster', required=True, help='e.g. M08')
    ap.add_argument('--char-seq', type=int, required=True, help='e.g. 2')
    args = ap.parse_args()
    cluster = args.cluster
    char_seq = args.char_seq

    # Locate file
    folder = REPO / 'Sessions' / 'Session_Clusters' / cluster / 'files phase 9'
    candidates = sorted(folder.glob(f'wa-cluster-{cluster}-phase9-char{char_seq}-*-findings-v*.md'))
    if not candidates:
        candidates = sorted(folder.glob(f'wa-cluster-{cluster}-phase9-char{char_seq}-*findings*.md'))
    if not candidates:
        raise SystemExit(f'No findings file for {cluster} char{char_seq} in {folder}')
    findings_path = candidates[-1]
    print(f'Findings file: {findings_path.relative_to(REPO)}  ({findings_path.stat().st_size:,} bytes)')

    text = findings_path.read_text(encoding='utf-8')

    # Look up characteristic_id + sub-groups for the chosen char_seq
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    char_row = cur.execute(
        "SELECT id, short_name FROM characteristic WHERE cluster_code=? AND char_seq=? AND COALESCE(delete_flagged,0)=0",
        (cluster, char_seq),
    ).fetchone()
    if not char_row:
        raise SystemExit(f'No characteristic row for {cluster} char_seq={char_seq}')
    print(f'Characteristic: CHAR-{char_seq} ({char_row["short_name"]}) id={char_row["id"]}')

    sg_rows = cur.execute(
        """SELECT cs.subgroup_code FROM cluster_subgroup cs
           JOIN characteristic_subgroup chs ON chs.cluster_subgroup_id = cs.id
           WHERE chs.characteristic_id=? AND COALESCE(chs.delete_flagged,0)=0
             AND COALESCE(cs.delete_flagged,0)=0""",
        (char_row['id'],),
    ).fetchall()
    sg_codes = tuple(r['subgroup_code'] for r in sg_rows)
    print(f'Sub-groups: {sg_codes}')

    # Build corpus + VCG set
    placeholders = ','.join('?' * len(sg_codes))
    char_refs = set()
    for r in cur.execute(f"""
        SELECT DISTINCT vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code=? AND cs.subgroup_code IN ({placeholders})
          AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """, (cluster, *sg_codes)).fetchall():
        char_refs.add(r['reference'])
    print(f'Char-corpus refs: {len(char_refs)}')

    char_vcgs = set()
    vcg_pattern = '|'.join(re.escape(sg) for sg in sg_codes)
    for r in cur.execute(f"""
        SELECT DISTINCT vcg.group_code
        FROM verse_context_group vcg
        JOIN verse_context vc ON vc.group_id = vcg.id
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE cs.cluster_code=? AND cs.subgroup_code IN ({placeholders})
          AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
          AND COALESCE(vcg.delete_flagged,0)=0
    """, (cluster, *sg_codes)).fetchall():
        char_vcgs.add(r['group_code'])
    VCG_REF_RE = re.compile(f'(?:{vcg_pattern})-VCG-\\d+')
    print(f'Char VCG set: {sorted(char_vcgs)}')
    conn.close()

    # Parse prompt blocks
    prompt_block_re = re.compile(
        r'\*\*(T\d+\.\d+\.\d+)\s*(?:[–\-—]\s*[^*]*)?\*\*\s*\n\s*\n'
        r'\*\*\[CHAR-(\d+)\]\*\*\s+([ESG])\s+(?:—\s+)?(.*?)(?=\n---\n|\n\*\*T\d+\.\d+\.\d+|\Z)',
        re.DOTALL,
    )
    blocks = prompt_block_re.findall(text)
    print(f'Parsed {len(blocks)} prompt blocks (expected 189)')

    tier_blocks: dict[str, list] = defaultdict(list)
    for code, char_n_str, outcome, body in blocks:
        tier = code.split('.')[0]
        tier_blocks[tier].append((code, int(char_n_str), outcome, body.strip()))

    print('Per-tier:')
    for t in ['T0','T1','T2','T3','T4','T5','T6','T7']:
        n = len(tier_blocks.get(t, []))
        flag = '✓' if n == TIER_SIZES[t] else f'✗ (expected {TIER_SIZES[t]})'
        print(f'  {t}: {n} {flag}')

    out_dist = Counter(outcome for _, _, outcome, _ in blocks)
    print(f'Outcome distribution: E={out_dist["E"]} S={out_dist["S"]} G={out_dist["G"]}')

    # Checks
    scope_violations = [(c, int(n)) for c, n, _, _ in blocks if int(n) != char_seq]
    e_no_citation = []
    phantom_per_block = []  # (code, set_of_phantom_refs)
    cross_tier_re = re.compile(r'(?:as noted in|see) T\d+(?:\.\d+\.\d+)?|tier T\d+|earlier tier|prior tier', re.IGNORECASE)
    cross_tier_signals = []
    bulk_openings = Counter()

    for code, char_n, outcome, body in blocks:
        refs = BIBLE_REF_RE.findall(body)
        vcgs = VCG_REF_RE.findall(body)
        if outcome == 'E' and not refs and not vcgs:
            e_no_citation.append((code, body[:100]))

        phantom = [r for r in set(refs) if r not in char_refs]
        if phantom:
            phantom_per_block.append((code, phantom))

        if cross_tier_re.search(body):
            cross_tier_signals.append((code, cross_tier_re.search(body).group(0)))
        bulk_openings[body[:80]] += 1

    bulk_dupes = {k: v for k, v in bulk_openings.items() if v >= 3}

    self_check_present = '## Self-check' in text

    print()
    print('Quality signals:')
    print(f'  scope_violations:       {len(scope_violations)} (must be 0)')
    print(f'  e_no_citation:          {len(e_no_citation)} / {out_dist["E"]} E findings')
    print(f'  phantom_per_block:      {len(phantom_per_block)} blocks with refs outside corpus')
    print(f'  cross_tier_signals:     {len(cross_tier_signals)}')
    print(f'  bulk_duplicate_openings: {len(bulk_dupes)}')
    print(f'  Final Self-check block: {self_check_present}')

    # Write report
    out_path = REPO / f'Sessions/Session_Clusters/{cluster}/wa-cluster-{cluster}-phase9-char{char_seq}-spotcheck-v1-20260521.md'
    lines = []
    lines.append(f'# {cluster} CHAR-{char_seq} Phase 9 findings — Spot-check report')
    lines.append('')
    lines.append(f'**Source:** [{findings_path.relative_to(REPO)}]({findings_path.relative_to(REPO)})')
    lines.append(f'**Characteristic:** CHAR-{char_seq} ({char_row["short_name"]}) · id={char_row["id"]}')
    lines.append(f'**Sub-groups:** {", ".join(sg_codes)}')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## §1 — Structural')
    lines.append('')
    lines.append('| Check | Result |')
    lines.append('|---|---|')
    lines.append(f'| Prompt blocks parsed | {len(blocks)} / 189 |')
    for t in ['T0','T1','T2','T3','T4','T5','T6','T7']:
        n = len(tier_blocks.get(t, []))
        flag = '✓' if n == TIER_SIZES[t] else f'⚠ (expected {TIER_SIZES[t]})'
        lines.append(f'| {t} | {n} {flag} |')
    lines.append(f'| Outcome distribution | E={out_dist["E"]} · S={out_dist["S"]} · G={out_dist["G"]} |')
    lines.append(f'| Scope marker violations (non-CHAR-{char_seq}) | {len(scope_violations)} |')
    lines.append(f'| Final Self-check block | {"✓" if self_check_present else "✗"} |')
    lines.append('')

    lines.append('## §2 — Citation discipline')
    lines.append('')
    lines.append('| Check | Result |')
    lines.append('|---|---|')
    e_with_cite = out_dist["E"] - len(e_no_citation)
    e_pct = (e_with_cite / out_dist["E"] * 100) if out_dist["E"] else 0
    lines.append(f'| E findings citing verse/VCG | {e_with_cite} / {out_dist["E"]} ({e_pct:.1f}%) |')
    lines.append(f'| Blocks citing refs outside corpus | {len(phantom_per_block)} |')
    lines.append('')

    if e_no_citation:
        lines.append('### E findings without citation (first 15)')
        lines.append('')
        for code, snippet in e_no_citation[:15]:
            lines.append(f'- **{code}** — {snippet}…')
        lines.append('')

    if phantom_per_block:
        lines.append('### Phantom references (first 15)')
        lines.append('')
        lines.append('Note: range citations like `Psa 75:4–10` may flag here even though the individual verses are in corpus — parser limitation. Inspect each.')
        lines.append('')
        for code, refs in phantom_per_block[:15]:
            lines.append(f'- **{code}** — cited: {", ".join(sorted(refs))}')
        lines.append('')

    lines.append('## §3 — Drift signals')
    lines.append('')
    lines.append('| Check | Result |')
    lines.append('|---|---|')
    lines.append(f'| Cross-tier reference signals | {len(cross_tier_signals)} |')
    lines.append(f'| Bulk-classification candidates (≥3 identical openings) | {len(bulk_dupes)} |')
    lines.append('')

    if cross_tier_signals:
        lines.append('### Cross-tier signals (first 10)')
        lines.append('')
        for code, sig in cross_tier_signals[:10]:
            lines.append(f'- **{code}** — *"{sig}"*')
        lines.append('')

    if bulk_dupes:
        lines.append('### Bulk-classification candidates')
        lines.append('')
        for opening, n in bulk_dupes.items():
            lines.append(f'- **{n}×** {opening[:60]}…')
        lines.append('')

    lines.append('## §4 — Verdict')
    lines.append('')
    lines.append(f'- Structural completeness: {len(blocks)}/189 prompts, {len(scope_violations)} scope violations.')
    lines.append(f'- Citation discipline: {e_pct:.1f}% of E findings cite verse/VCG.')
    lines.append(f'- Phantom refs: {len(phantom_per_block)} blocks — inspect to distinguish parser artifacts (range notation) from real cross-character drift.')
    lines.append(f'- Cross-tier drift signals: {len(cross_tier_signals)}.')
    lines.append(f'- Bulk-classification: {len(bulk_dupes)} candidates.')
    lines.append('')
    lines.append('CC verdict: review the items above; if no real cross-character drift in phantom refs and citation discipline >85%, accept and apply.')
    lines.append('')
    out_path.write_text('\n'.join(lines), encoding='utf-8')
    print()
    print(f'Wrote: {out_path.relative_to(REPO)}')


if __name__ == '__main__':
    main()
