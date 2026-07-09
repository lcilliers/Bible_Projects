"""Merge M09 original synthesis (90 prompts + appendix) + gap-fill (99 prompts) into 189-row file.

Output: Sessions/Session_Clusters/M09/files phase 9/wa-cluster-M09-phase9-cluster-synthesis-findings-MERGED-v1-20260522.md

Interleaves prompt blocks by T-code in canonical order. Preserves the prose appendix
from the original file.
"""
import sys, io, re, sqlite3
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
ORIG = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'files phase 9' / 'wa-cluster-m09-phase9-cluster-synthesis-findings-v1-20260522.md'
GAP = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'files phase 9' / 'wa-cluster-M09-phase9-synthesis-missing-findings-v1-20260522.md'
OUT = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'files phase 9' / 'wa-cluster-M09-phase9-cluster-synthesis-findings-MERGED-v1-20260522.md'

# Canonical prompt order
conn = sqlite3.connect(DB)
all_codes = [r[0] for r in conn.execute("""
    SELECT question_code FROM wa_obs_question_catalogue
    WHERE tier IN ('T0','T1','T2','T3','T4','T5','T6','T7') AND COALESCE(deleted,0)=0
    ORDER BY tier, component_code, prompt_seq
""").fetchall()]
print(f'Canonical prompt count: {len(all_codes)}')

# Split each file into prompt-block dict
PROMPT_HEADER_RE = re.compile(r'^\*\*(T\d+\.\d+\.\d+) — ', re.MULTILINE)
APPENDIX_RE = re.compile(r'^##\s+Appendix\b', re.MULTILINE | re.IGNORECASE)


def parse_blocks(path: Path) -> tuple[dict[str, str], str]:
    """Return (code → block text, appendix text). The block text is the full prompt block
    starting from **T#.#.# — ... and ending at the next prompt header or appendix or self-check."""
    text = path.read_text(encoding='utf-8')
    m_app = APPENDIX_RE.search(text)
    body = text[:m_app.start()] if m_app else text
    appendix = text[m_app.start():] if m_app else ''

    matches = list(PROMPT_HEADER_RE.finditer(body))
    blocks: dict[str, str] = {}
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(body)
        block = body[start:end].rstrip()
        # Strip a trailing self-check section if it's inside the last block
        # (We assume self-check is delimited by ## Self-check at start of line)
        sc_m = re.search(r'\n## (?:Self-check|self-check)', block)
        if sc_m:
            block = block[:sc_m.start()].rstrip()
        blocks[m.group(1)] = block
    return blocks, appendix


orig_blocks, orig_appendix = parse_blocks(ORIG)
gap_blocks, gap_appendix = parse_blocks(GAP)
print(f'Original blocks parsed: {len(orig_blocks)}')
print(f'Gap-fill blocks parsed: {len(gap_blocks)}')

# Diagnostics
orig_codes = set(orig_blocks.keys())
gap_codes = set(gap_blocks.keys())
overlap = orig_codes & gap_codes
missing = set(all_codes) - orig_codes - gap_codes
print(f'Overlap: {len(overlap)} (must be 0)')
print(f'Missing from both: {len(missing)} (must be 0)')
assert overlap == set()
assert missing == set()

# Build merged file
out_lines = []
out_lines.append('# M09 Phase 9 — Cluster Synthesis — findings (MERGED v1)')
out_lines.append('')
out_lines.append('**Date:** 2026-05-22')
out_lines.append('**Cluster:** M09 — Humility, Meekness and Submission')
out_lines.append('**Source files merged:**')
out_lines.append(f'- `{ORIG.relative_to(REPO)}` (90 prompts + prose appendix; T0/T1 complete; T2-T7 .1 of each prompt-group)')
out_lines.append(f'- `{GAP.relative_to(REPO)}` (99 prompts; T2-T7 .2/.3 follow-up subprompts — gap-fill session)')
out_lines.append('')
out_lines.append('**Prompts present:** 189 / 189 ✓')
out_lines.append('')
out_lines.append('---')
out_lines.append('')

for code in all_codes:
    if code in orig_blocks:
        out_lines.append(orig_blocks[code])
    else:
        out_lines.append(gap_blocks[code])
    out_lines.append('')
    out_lines.append('---')
    out_lines.append('')

# Append the original prose appendix (gap-fill file may have a small self-check; ignore that)
if orig_appendix:
    out_lines.append(orig_appendix)

OUT.write_text('\n'.join(out_lines), encoding='utf-8')
print(f'\nWrote merged: {OUT.relative_to(REPO)}  ({OUT.stat().st_size:,} bytes)')

# Sanity: count prompts in merged
merged = OUT.read_text(encoding='utf-8')
m_app = APPENDIX_RE.search(merged)
merged_body = merged[:m_app.start()] if m_app else merged
merged_codes = set(PROMPT_HEADER_RE.findall(merged_body))
print(f'Merged file prompts (in body): {len(merged_codes)} (expected 189)')
conn.close()
