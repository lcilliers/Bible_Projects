"""Build a narrowed Phase 9 synthesis input + brief for the 99 missing prompts.

The first synthesis AI session for M09 (2026-05-22) produced only 90 of 189
prompt blocks — the AI dropped the .2/.3 follow-ups across T2-T7. This script
builds a narrowed package containing ONLY the 99 missing prompts, each with
its 6 per-characteristic findings stacked beneath, so a focused AI session
can complete the gap.

Output:
- Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-synthesis-missing-brief-v1-20260522.md
- Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-synthesis-missing-input-v1-20260522.md
"""
import sys, io, re, sqlite3
from pathlib import Path
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
EXISTING = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'files phase 9' / 'wa-cluster-m09-phase9-cluster-synthesis-findings-v1-20260522.md'
OUT_BRIEF = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'wa-cluster-M09-phase9-synthesis-missing-brief-v1-20260522.md'
OUT_INPUT = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'wa-cluster-M09-phase9-synthesis-missing-input-v1-20260522.md'
TODAY = datetime.now().strftime('%Y-%m-%d')

# Step 1: identify missing prompts
APPENDIX_RE = re.compile(r'^##\s+Appendix\b', re.MULTILINE | re.IGNORECASE)
text = EXISTING.read_text(encoding='utf-8')
m = APPENDIX_RE.search(text)
body = text[:m.start()] if m else text
present = set(re.findall(r'^\*\*(T\d+\.\d+\.\d+) — ', body, re.MULTILINE))

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()
all_prompts = list(cur.execute("""
    SELECT obs_id, question_code, question_text, tier, component_code, component_title
    FROM wa_obs_question_catalogue
    WHERE tier IN ('T0','T1','T2','T3','T4','T5','T6','T7') AND COALESCE(deleted,0)=0
    ORDER BY tier, component_code, prompt_seq
"""))
missing = [p for p in all_prompts if p['question_code'] not in present]
print(f'Total prompts: {len(all_prompts)}; present: {len(present)}; missing: {len(missing)}')

# Build per-char findings map for stacking
chars = list(cur.execute(
    "SELECT id, char_seq, short_name FROM characteristic WHERE cluster_code='M09' AND COALESCE(delete_flagged,0)=0 ORDER BY char_seq"
).fetchall())
print(f'Chars to stack: {[(c["char_seq"], c["short_name"]) for c in chars]}')

# Fetch all per-char findings keyed by (char_seq, obs_id)
char_findings: dict[tuple[int, int], dict] = {}
for r in cur.execute("""
    SELECT cf.obs_id, c.char_seq, c.short_name, cf.finding_status, cf.finding_text
    FROM cluster_finding cf
    JOIN characteristic c ON c.id = cf.characteristic_id
    WHERE cf.cluster_code='M09' AND COALESCE(cf.delete_flagged,0)=0
      AND cf.characteristic_id IS NOT NULL
"""):
    char_findings[(r['char_seq'], r['obs_id'])] = {'status': r['finding_status'], 'text': r['finding_text'], 'short_name': r['short_name']}
print(f'Per-char findings loaded: {len(char_findings)}')

# =====
# BRIEF
# =====
B = []
B.append('# M09 Phase 9 — Synthesis completion (missing 99 prompts) — brief')
B.append('')
B.append('**Cluster:** M09 — Humility, Meekness and Submission')
B.append('**Phase:** 9 cluster-synthesis completion (gap-fill)')
B.append(f'**Task date:** {TODAY}')
B.append('**Audience:** Claude AI session')
B.append('')
B.append('---')
B.append('')
B.append('## Context — why this brief exists')
B.append('')
B.append('The first M09 cluster-synthesis AI session (2026-05-22) produced 90 of 189 expected `[CLUSTER]` prompt blocks. It dropped the .2/.3 follow-up prompts across tiers T2-T7 — likely a working-memory issue (could not hold the full 189-prompt × 6-char matrix at once). T0 and T1 are fully complete (36 / 36 prompts ✓). The prose appendix is also complete.')
B.append('')
B.append('Your task: **author cluster-scope findings ONLY for the 99 missing prompts listed below.** The 90 prompts already authored are not in scope — do not re-author or revise them.')
B.append('')
B.append('---')
B.append('')
B.append('## Required inputs')
B.append('')
B.append('| # | Document | Purpose |')
B.append('|---|---|---|')
B.append(f'| 1 | **This brief** — `Sessions/Session_Clusters/M09/{OUT_BRIEF.name}` | Primary task instructions |')
B.append(f'| 2 | **Structural input (gap-fill)** — `Sessions/Session_Clusters/M09/{OUT_INPUT.name}` | The 99 missing prompts, each with its 6 per-characteristic findings stacked |')
B.append('| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |')
B.append('| 4 | **Science extract** — `Workflow/Sciences/wa-m09-humility-scienceextract-v1_0-20260513.md` | Programme-curated scientific lens for T7.3 prompts |')
B.append('| 5 | **Existing synthesis (reference only)** — `Sessions/Session_Clusters/M09/files phase 9/wa-cluster-m09-phase9-cluster-synthesis-findings-v1-20260522.md` | Read T0/T1 + the 90 already-authored prompts for context if needed; do NOT re-author |')
B.append('| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |')
B.append('')
B.append('---')
B.append('')
B.append('## Missing prompts (the 99 in scope) — by tier')
B.append('')
# Group missing by tier
from collections import defaultdict
by_tier_missing = defaultdict(list)
for p in missing:
    by_tier_missing[p['tier']].append(p['question_code'])
for t in ['T2','T3','T4','T5','T6','T7']:
    codes = by_tier_missing.get(t, [])
    if codes:
        B.append(f'**{t}** ({len(codes)} prompts): {", ".join(codes)}')
        B.append('')

B.append('---')
B.append('')
B.append('## What you are producing')
B.append('')
B.append('For each of the 99 missing prompts, author ONE cluster-scope finding examining what surfaces when the 6 characteristics\' findings are compared.')
B.append('')
B.append('### Output format')
B.append('')
B.append('Use the SAME parser-safe format as the cluster-synthesis session:')
B.append('')
B.append('```')
B.append('**T#.#.# — question text excerpt (optional)**')
B.append('')
B.append('**[CLUSTER]** E — Cluster-scope finding text. Cite specific characteristics by name and the specific patterns/divergences/anchors they reveal when compared.')
B.append('')
B.append('---')
B.append('```')
B.append('')
B.append('**Scope marker** is `**[CLUSTER]**` (CC\'s loader sets characteristic_id=NULL, finding_status=\'cluster_synthesis\'). Do NOT use [CHAR-N] markers in the output.')
B.append('')
B.append('**Outcome codes:**')
B.append('- **E** — evidenced; comparative pattern across chars supports a cluster-scope answer')
B.append('- **S** — silent; no meaningful cluster-level pattern beyond per-char answers')
B.append('- **G** — gap; cluster-level pattern would require evidence the 6 chars\' findings don\'t supply')
B.append('')
B.append('---')
B.append('')
B.append('## ⚠️ TIER-BY-TIER STAGED EXECUTION — MANDATORY ⚠️')
B.append('')
B.append('**Known prior failure:** the prior synthesis session dropped 99 of 189 prompts when trying to hold the whole matrix in working memory. **Do not repeat that pattern.** This narrowed brief is exactly the gap-fill — proceed tier-by-tier with self-evaluation between.')
B.append('')
B.append('### Hard procedural sequence (per tier)')
B.append('')
B.append('Tiers to process: T2 → T3 → T4 → T5 → T6 → T7 (T0/T1 already complete; not in scope).')
B.append('')
B.append('For each tier in this brief\'s missing-prompt scope, you MUST:')
B.append('')
B.append('1. **OPEN TIER** — announce: *"Starting Tier T{N} — {missing prompt count} missing prompts to author."*')
B.append('2. **READ THE STACKED FINDINGS** — for each missing prompt in this tier, re-read the 6 stacked per-characteristic findings in §3 of the structural input. Do not rely on memorised summaries from prior tiers.')
B.append('3. **AUTHOR THIS TIER\'S MISSING PROMPTS** — one cluster-scope finding per missing prompt. No skipping. No "I\'ll come back later".')
B.append('4. **WRITE TO DISK** — emit the tier\'s complete missing-prompt section as a contiguous markdown block. Each block has a `## T{N} — gap-fill` header (or similar) and the missing prompts with their findings below.')
B.append('5. **SELF-EVALUATE** — run the gate (see below).')
B.append('6. **PROCEED or ALERT** — if PASS, immediately begin next tier in the same response; if FAIL, announce ALERT and STOP.')
B.append('')
B.append('### Self-evaluation gate (per tier)')
B.append('')
B.append('| # | Check | PASS criterion | If FAIL |')
B.append('|---|---|---|---|')
B.append('| 1 | **Prompt count** | All missing prompts in this tier authored | ALERT — name the still-missing prompts |')
B.append('| 2 | **Scope marker** | Every block uses `**[CLUSTER]**` (no `[CHAR-N]`) | ALERT |')
B.append('| 3 | **Citation discipline** | Every E finding names which characteristics contribute what; ideally also names specific verses where relevant | ALERT |')
B.append('| 4 | **No re-authoring** | Did not author or revise any of the 90 already-present prompts | ALERT |')
B.append('| 5 | **Distinct findings** | No two prompts share an identical 80-char opening | ALERT |')
B.append('')
B.append('Document the self-evaluation inline at the end of each tier block.')
B.append('')
B.append('---')
B.append('')
B.append('## Output structure')
B.append('')
B.append('Write your output as a single markdown file at:')
B.append('')
B.append(f'`Sessions/Session_Clusters/M09/files phase 9/wa-cluster-M09-phase9-synthesis-missing-findings-v1-{TODAY.replace("-","")}.md`')
B.append('')
B.append('Suggested document structure:')
B.append('')
B.append('```markdown')
B.append('# M09 Phase 9 — Synthesis gap-fill — findings')
B.append('')
B.append('**Date:** 2026-05-22')
B.append('**Scope:** 99 missing prompts (T2-T7 follow-up subprompts)')
B.append('**Prompts authored:** 99 / 99')
B.append('')
B.append('## T2 — gap-fill (17 prompts)')
B.append('')
B.append('**T2.2.2 — [question text]**')
B.append('')
B.append('**[CLUSTER]** E — finding text comparing how the 6 characteristics answer this...')
B.append('')
B.append('---')
B.append('')
B.append('[... rest of T2 missing prompts ...]')
B.append('')
B.append('T2 self-evaluation: 17/17 ✓ scope-clean ✓ ... → PASS. Proceeding to T3.')
B.append('')
B.append('## T3 — gap-fill (20 prompts)')
B.append('...')
B.append('```')
B.append('')
B.append('At the end of T7, after the last self-evaluation passes, post a final Self-check:')
B.append('')
B.append('```markdown')
B.append('## Self-check')
B.append('')
B.append('- Missing prompts authored: 99 / 99 ✓')
B.append('- All blocks use **[CLUSTER]** scope marker ✓')
B.append('- Per-tier evaluations: T2 ✓ T3 ✓ T4 ✓ T5 ✓ T6 ✓ T7 ✓')
B.append('- No re-authoring of the 90 existing prompts ✓')
B.append('```')
B.append('')
B.append('---')
B.append('')
B.append('## After T7 + Self-check')
B.append('')
B.append('1. Confirm the gap-fill findings file is on disk.')
B.append('2. Ping CC: "M09 synthesis gap-fill ready".')
B.append('3. CC merges the gap-fill into the existing 90-prompt synthesis file, validates the merged 189-row total, applies to `cluster_finding` (finding_status=\'cluster_synthesis\').')
B.append('')
B.append('---')
B.append('')
B.append('*End of brief. Load the structural input (#2) and begin **Tier T2** in your first response.*')

OUT_BRIEF.write_text('\n'.join(B), encoding='utf-8')
print(f'\nWrote brief: {OUT_BRIEF.relative_to(REPO)}  ({OUT_BRIEF.stat().st_size:,} bytes)')

# =====
# INPUT (structural)
# =====
S = []
S.append('# M09 Phase 9 — Synthesis gap-fill — structural input')
S.append('')
S.append(f'**Date:** {TODAY}')
S.append('**Cluster:** M09 — Humility, Meekness and Submission')
S.append(f'**Scope:** the 99 missing prompts (T2-T7 follow-up subprompts)')
S.append('')
S.append('---')
S.append('')
S.append('## §1 — Cluster overview')
S.append('')
S.append('M09 has 6 characteristics:')
S.append('')
S.append('| Char | Short name | Sub-groups | Verses |')
S.append('|---:|---|---|---:|')
for c in chars:
    sgs = list(cur.execute("""
        SELECT cs.subgroup_code,
               (SELECT COUNT(*) FROM verse_context vc JOIN cluster_subgroup cs2 ON cs2.id=vc.cluster_subgroup_id
                WHERE cs2.subgroup_code=cs.subgroup_code AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0) AS n
        FROM characteristic_subgroup chs
        JOIN cluster_subgroup cs ON cs.id=chs.cluster_subgroup_id
        WHERE chs.characteristic_id=? AND COALESCE(chs.delete_flagged,0)=0 ORDER BY cs.subgroup_code
    """, (c['id'],)).fetchall())
    sg_str = ', '.join(f"{r['subgroup_code']}({r['n']}V)" for r in sgs)
    total = sum(r['n'] for r in sgs)
    S.append(f"| {c['char_seq']} | {c['short_name']} | {sg_str} | {total} |")
S.append('')
S.append('---')
S.append('')
S.append('## §2 — How to read this file')
S.append('')
S.append('Each of the 99 missing prompts is presented below with the 6 per-characteristic findings stacked verbatim from `cluster_finding`. Read all 6 before authoring the cluster-scope row for that prompt.')
S.append('')
S.append('Format per prompt:')
S.append('')
S.append('```')
S.append('### T#.#.# — {question text}')
S.append('')
S.append('**[CHAR-1] {short_name}** ({status}): {finding text}')
S.append('**[CHAR-2] {short_name}** ({status}): {finding text}')
S.append('... (all 6 chars)')
S.append('```')
S.append('')
S.append('---')
S.append('')
S.append('## §3 — Missing prompts with stacked per-characteristic findings')
S.append('')

# Group missing by tier
missing_by_tier = defaultdict(list)
for p in missing:
    missing_by_tier[p['tier']].append(p)

for tier in ['T2','T3','T4','T5','T6','T7']:
    tier_missing = missing_by_tier.get(tier, [])
    if not tier_missing:
        continue
    S.append(f'### {tier} — {len(tier_missing)} missing prompts')
    S.append('')
    for p in tier_missing:
        code = p['question_code']
        S.append(f'#### {code} — {p["question_text"]}')
        S.append('')
        S.append(f'_Tier: {p["tier"]}_  _Component: {p["component_code"]} {p["component_title"]}_')
        S.append('')
        # Stack 6 chars
        for c in chars:
            key = (c['char_seq'], p['obs_id'])
            f = char_findings.get(key)
            if f:
                S.append(f"**[CHAR-{c['char_seq']}] {c['short_name']}** ({f['status']}):")
                S.append(f"{f['text']}")
            else:
                S.append(f"**[CHAR-{c['char_seq']}] {c['short_name']}** (MISSING — no finding row found)")
            S.append('')
        S.append('---')
        S.append('')

OUT_INPUT.write_text('\n'.join(S), encoding='utf-8')
print(f'Wrote input: {OUT_INPUT.relative_to(REPO)}  ({OUT_INPUT.stat().st_size:,} bytes)')
conn.close()
