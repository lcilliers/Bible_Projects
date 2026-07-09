"""Spot-check the M08 CHAR-1 findings file against multiple quality gates.

Checks:
  1. Per-prompt: outcome code (E/S/G) present
  2. Per-prompt: [CHAR-N] marker — must be CHAR-1 only
  3. E findings: cite at least one Bible-reference-like token (e.g., "Isa 2:11", "Psa 75:7")
  4. Cited references are actually in CHAR-1's corpus (M08-A1/A2/A3/A4 is_relevant=1 vc rows)
  5. VCG references (e.g. "M08-A1-VCG-02") — present? are they real VCG codes?
  6. Cross-tier contamination signals (text patterns like "as noted in T0", "see T1", etc.)
  7. Bulk-classification signals (paragraph reuse across prompts)
  8. Length / fluency-without-citation signals
"""
import sys, io, re, sqlite3
from pathlib import Path
from collections import defaultdict, Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
FINDINGS = REPO / 'Sessions/Session_Clusters/M08/files phase 9/wa-cluster-M08-phase9-char1-Arrogant-self-elevation-findings-v1-20260521.md'
OUT = REPO / 'Sessions/Session_Clusters/M08/wa-cluster-M08-phase9-char1-spotcheck-v2-20260521.md'

text = FINDINGS.read_text(encoding='utf-8')

# Get CHAR-1's corpus from DB
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

CHAR1_SUBGROUPS = ('M08-A1', 'M08-A2', 'M08-A3', 'M08-A4')
char1_refs = set()
for r in cur.execute(f"""
    SELECT DISTINCT vr.reference
    FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
    WHERE mt.cluster_code='M08' AND cs.subgroup_code IN ({','.join('?'*len(CHAR1_SUBGROUPS))})
      AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""", CHAR1_SUBGROUPS).fetchall():
    char1_refs.add(r['reference'])
print(f'CHAR-1 corpus: {len(char1_refs)} unique verse references')

char1_vcgs = set()
for r in cur.execute(f"""
    SELECT DISTINCT vcg.group_code
    FROM verse_context_group vcg
    JOIN verse_context vc ON vc.group_id = vcg.id
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE cs.cluster_code='M08' AND cs.subgroup_code IN ({','.join('?'*len(CHAR1_SUBGROUPS))})
      AND COALESCE(vcg.delete_flagged,0)=0 AND vc.is_relevant=1
      AND COALESCE(vc.delete_flagged,0)=0
""", CHAR1_SUBGROUPS).fetchall():
    char1_vcgs.add(r['group_code'])
print(f'CHAR-1 VCGs: {len(char1_vcgs)} (e.g. {sorted(char1_vcgs)[:3]})')
conn.close()

# Reference token regex — covers common Bible-book abbreviations + chapter:verse
BIBLE_REF_RE = re.compile(r'\b(?:[1-3] ?)?[A-Z][a-z]{1,4}\.? \d+:\d+(?:[–\-]\d+)?\b')
VCG_REF_RE = re.compile(r'M08-A\d-VCG-\d+')

# Parse prompts: split by '\n---\n' between blocks
# A prompt block matches:
#   **T#.#.# — ...question...**
#   <blank>
#   **[CHAR-N]** OUTCOME — finding text...
prompt_block_re = re.compile(
    r'\*\*(T\d+\.\d+\.\d+)\s*(?:[–\-—]\s*[^*]*)?\*\*\s*\n\s*\n'
    r'\*\*\[CHAR-(\d+)\]\*\*\s+([ESG])\s+(?:—\s+)?(.*?)(?=\n---\n|\n\*\*T\d+\.\d+\.\d+|\Z)',
    re.DOTALL,
)

blocks = prompt_block_re.findall(text)
print(f'Parsed {len(blocks)} prompt blocks (expected 189)')

# Build per-tier breakdown
tier_blocks: dict[str, list] = defaultdict(list)
for code, char_n, outcome, body in blocks:
    tier = code.split('.')[0]  # T0, T1, etc.
    tier_blocks[tier].append((code, int(char_n), outcome, body.strip()))

print()
print('Per-tier block counts:')
expected = {'T0':12,'T1':24,'T2':31,'T3':33,'T4':24,'T5':21,'T6':24,'T7':20}
for t in ['T0','T1','T2','T3','T4','T5','T6','T7']:
    n = len(tier_blocks.get(t, []))
    flag = '✓' if n == expected[t] else f'✗ (expected {expected[t]})'
    print(f'  {t}: {n} {flag}')

# Quality scoring
scope_marker_violations = []
e_without_citation = []
phantom_refs_per_block = []  # blocks citing refs not in CHAR-1 corpus
phantom_vcgs_per_block = []
cross_tier_signals = []
bulk_class_signals = []

# Patterns suggesting cross-tier reference (drift)
cross_tier_re = re.compile(r'(?:as noted in|see) T\d+(?:\.\d+\.\d+)?|tier T\d+|earlier tier|prior tier', re.IGNORECASE)

for code, char_n_str, outcome, body in blocks:
    char_n = int(char_n_str)
    if char_n != 1:
        scope_marker_violations.append((code, char_n))

    refs = BIBLE_REF_RE.findall(body)
    vcgs = VCG_REF_RE.findall(body)

    if outcome == 'E' and not refs and not vcgs:
        e_without_citation.append((code, body[:80]))

    bad_refs = [r for r in refs if r not in char1_refs]
    if bad_refs:
        # Also accept refs with minor punctuation variants — but most should match
        phantom_refs_per_block.append((code, list(set(bad_refs)), refs))

    bad_vcgs = [v for v in vcgs if v not in char1_vcgs]
    if bad_vcgs:
        phantom_vcgs_per_block.append((code, list(set(bad_vcgs))))

    if cross_tier_re.search(body):
        cross_tier_signals.append((code, cross_tier_re.search(body).group(0)))

# Bulk classification: detect identical opening clauses across consecutive prompts
opening_clauses = [(code, body[:150]) for code, _, _, body in blocks]
opening_counter = Counter(c[1][:80] for c in opening_clauses)
# Flag any opening that appears 3+ times
bulk_openings = {k:v for k,v in opening_counter.items() if v >= 3}

# Outcome distribution
out_dist = Counter(outcome for _, _, outcome, _ in blocks)
print()
print(f'Outcome distribution: E={out_dist["E"]}, S={out_dist["S"]}, G={out_dist["G"]}')

# Sample 30 prompts (~4 per tier) for the report
import random
random.seed(42)
samples = []
for t in ['T0','T1','T2','T3','T4','T5','T6','T7']:
    blocks_t = tier_blocks.get(t, [])
    n_take = min(4, len(blocks_t))
    samples.extend(random.sample(blocks_t, n_take))

# Build report
lines = []
lines.append(f'# M08 CHAR-1 Phase 9 findings — Spot-check report')
lines.append('')
lines.append(f'**Source:** [{FINDINGS.relative_to(REPO)}]({FINDINGS.relative_to(REPO)})')
lines.append(f'**Date:** 2026-05-21')
lines.append(f'**Method:** parser-based grading + 30-prompt random sample')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## §1 — Structural completeness')
lines.append('')
lines.append('| Check | Result |')
lines.append('|---|---|')
lines.append(f'| Total prompt blocks parsed | {len(blocks)} / 189 expected |')
for t in ['T0','T1','T2','T3','T4','T5','T6','T7']:
    n = len(tier_blocks.get(t, []))
    flag = '✓' if n == expected[t] else f'⚠ (expected {expected[t]})'
    lines.append(f'| {t} prompts | {n} {flag} |')
lines.append(f'| Outcome distribution | E={out_dist["E"]} · S={out_dist["S"]} · G={out_dist["G"]} |')
lines.append(f'| `[CHAR-N]` marker violations (non-CHAR-1) | {len(scope_marker_violations)} |')
lines.append('')

lines.append('## §2 — Citation discipline')
lines.append('')
lines.append('| Check | Result |')
lines.append('|---|---|')
lines.append(f'| E findings with NO Bible-ref AND no VCG-ref | {len(e_without_citation)} |')
lines.append(f'| Blocks citing references NOT in CHAR-1 corpus | {len(phantom_refs_per_block)} |')
lines.append(f'| Blocks citing VCGs NOT in CHAR-1\'s VCG set | {len(phantom_vcgs_per_block)} |')
lines.append('')

if e_without_citation:
    lines.append('### E findings without citation (first 10)')
    lines.append('')
    for code, snippet in e_without_citation[:10]:
        lines.append(f'- **{code}** — {snippet}…')
    lines.append('')

if phantom_refs_per_block:
    lines.append('### Phantom references (first 10) — citing verses not in CHAR-1 corpus')
    lines.append('')
    lines.append('Note: M08 has 174 verses set-aside at Phase 5.5 (M22-register / narrative). If the AI cites them, that\'s a drift signal (those verses are no longer in CHAR-1\'s active corpus).')
    lines.append('')
    for code, bad, _ in phantom_refs_per_block[:10]:
        lines.append(f'- **{code}** — cited: {", ".join(sorted(bad)[:8])}')
    lines.append('')

lines.append('## §3 — Drift signals')
lines.append('')
lines.append('| Check | Result |')
lines.append('|---|---|')
lines.append(f'| Cross-tier reference signals (e.g. "as noted in T0") | {len(cross_tier_signals)} |')
lines.append(f'| Bulk-classification signals (identical 80-char openings appearing 3+ times) | {len(bulk_openings)} |')
lines.append('')

if cross_tier_signals:
    lines.append('### Cross-tier reference signals (first 15)')
    lines.append('')
    for code, sig in cross_tier_signals[:15]:
        lines.append(f'- **{code}** — text: *"{sig}"*')
    lines.append('')

if bulk_openings:
    lines.append('### Bulk-classification candidates')
    lines.append('')
    for opening, n in bulk_openings.items():
        # Find which prompts share this opening
        sharing = [c for c, o in opening_clauses if o[:80] == opening]
        lines.append(f'- **{n}× identical opening** across: {", ".join(sharing)}')
        lines.append(f'  > {opening}…')
    lines.append('')

lines.append('## §4 — 30-prompt random sample (4 per tier)')
lines.append('')
lines.append('Showing each sampled prompt with: outcome, ref-count, VCG-count, and a snippet of the finding body. Verify the analytical depth and grounding by inspection.')
lines.append('')
lines.append('| Tier | Prompt | Outcome | Refs cited | VCGs cited | Body snippet |')
lines.append('|---|---|:-:|:-:|:-:|---|')
for code, char_n, outcome, body in samples:
    tier = code.split('.')[0]
    refs = set(BIBLE_REF_RE.findall(body))
    vcgs = set(VCG_REF_RE.findall(body))
    refs_str = f'{len(refs)}'
    vcgs_str = f'{len(vcgs)}'
    snippet = body[:120].replace('|', '\\|').replace('\n', ' ')
    lines.append(f'| {tier} | {code} | {outcome} | {refs_str} | {vcgs_str} | {snippet}… |')
lines.append('')

lines.append('## §5 — Verdict (CC reading)')
lines.append('')
# Compute scores
total_blocks = len(blocks)
e_count = out_dist['E']
e_with_citation = e_count - len(e_without_citation)
e_citation_pct = e_with_citation / e_count * 100 if e_count else 0
phantom_pct = len(phantom_refs_per_block) / total_blocks * 100
cross_tier_pct = len(cross_tier_signals) / total_blocks * 100

lines.append(f'- **Structural completeness:** {len(blocks)}/189 prompts parsed, scope markers {"clean" if not scope_marker_violations else "BROKEN"}.')
lines.append(f'- **Citation discipline:** {e_citation_pct:.1f}% of E findings cite at least one Bible-ref or VCG. Phantom-ref rate: {phantom_pct:.1f}%.')
lines.append(f'- **Cross-tier drift signals:** {cross_tier_pct:.1f}% of blocks contain explicit "as noted in T#" phrasing. (Some cross-tier coherence is expected and not necessarily drift — this is informational only.)')
lines.append(f'- **Bulk-classification signals:** {len(bulk_openings)} identical openings detected (3+ occurrences each).')
lines.append('')
lines.append('### Researcher decision points')
lines.append('')
lines.append('1. Sample the 30 prompts in §4 — does the analytical depth match what you expect at characteristic scope?')
lines.append('2. Inspect any phantom-reference cases in §2 — are they actual set-aside verses or just punctuation variants?')
lines.append('3. Inspect cross-tier signals in §3 — are they legitimate cross-tier coherence or contamination?')
lines.append('')
lines.append('---')
lines.append('')
lines.append('*End of spot-check report.*')

OUT.write_text('\n'.join(lines), encoding='utf-8')
print()
print(f'Wrote: {OUT.relative_to(REPO)} ({OUT.stat().st_size:,} bytes)')
print()
print(f'Key signals: e_no_citation={len(e_without_citation)}, phantom_refs={len(phantom_refs_per_block)}, cross_tier={len(cross_tier_signals)}, bulk={len(bulk_openings)}')
