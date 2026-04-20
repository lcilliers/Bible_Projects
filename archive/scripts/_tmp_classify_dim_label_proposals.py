"""One-off: heuristic classifier producing DIR-20260420-002 directive result.

CC-side heuristic. Not a replacement for Claude AI analytical pass.
Produces: outputs/wa-global-dirresult-002-dim-label-proposals-v1-20260420.md (+ .json)
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

with open('outputs/dim-label-noncanonical-rows-20260420.json', encoding='utf-8') as f:
    rows = json.load(f)

C_POS   = '01 — Emotion — Positive'
C_NEG   = '02 — Emotion — Negative'
C_COG   = '03 — Cognition'
C_VOL   = '04 — Volition'
C_MORAL = '05 — Moral Character'
C_REL   = '06 — Relational Disposition'
C_VIT   = '07 — Vitality / Existence'
C_TRANS = '08 — Transformation'
C_AGEN  = '09 — Agency / Power'
C_DEP   = '10 — Dependence / Creatureliness'
C_DHC   = '11 — Divine-Human Correspondence'

POSITIVE_KW = ('joy','pleasure','delight','gladness','satisfaction','comfort','rejoic','cheer','happy')
NEGATIVE_KW = ('grief','fear','anger','shame','pain','distress','sorrow','overwhelm','wrath','afflict',
               'crisis','exhaust','anguish','bitter','weep','weary','mourn','terror','anxi','panic','dread','gloom')
COGNITION_KW = ('awareness','aware','perceive','perception','know','knowing','understand','discern',
                'remember','memory','conscience','attent','recognis','recognize','consider','reflect','mindful','intellect')
MORAL_KW = ('moral','virtue','integrity','uprightness','righteous','wicked','iniquit','evil',
            'worthless','corrupt','holy','purity','sin','transgress','character','disposition')
RELATIONAL_KW = ('toward another','toward others','relational','attachment','love','hatred','contempt',
                 'compassion','tenderness','pity','favour','favor','affection','fellowship','communion')
VITALITY_KW = ('life','living','alive','death','dying','dead','constitution','existence','creature',
               'creaturely','embodied','somatic','body','bodily','flesh','faint','perish','breath',
               'essential','self,','selfhood','identity','living soul','living creature','non-physical')
DHC_KW = ('divine-human','divine human','before god','before the lord','between god and',
          'divine and human','divine presence','god-ward','god ward','divine initiative',
          'image of god','mirrors god','divine-side')
DEPEND_KW = ('reliance','trust in god','depend','humility before','submit','surrender to god',
             'faith in god','call upon','look to god','cast upon','yield to god')


def matches(text, keywords):
    t = (text or '').lower()
    return sum(1 for k in keywords if k in t)


def classify_affective(ctx):
    neg = matches(ctx, NEGATIVE_KW)
    pos = matches(ctx, POSITIVE_KW)
    if neg > pos and neg >= 1:
        return (C_NEG, 'HIGH' if neg >= 2 else 'MEDIUM',
                f'Negative-valence keywords (count={neg})')
    if pos > neg and pos >= 1:
        return (C_POS, 'HIGH' if pos >= 2 else 'MEDIUM',
                f'Positive-valence keywords (count={pos})')
    return (C_NEG, 'LOW',
            'No clear valence signal; default to 02 (programme pattern). Researcher review.')


def classify_moral_conscience(ctx):
    cog = matches(ctx, COGNITION_KW)
    mor = matches(ctx, MORAL_KW)
    if cog >= 2 and cog > mor:
        return (C_COG, 'MEDIUM',
                f'Cognitive keywords dominant (cog={cog}, moral={mor}); conscience-as-awareness reading')
    if mor >= 1:
        return (C_MORAL, 'HIGH' if mor >= 2 else 'MEDIUM',
                f'Moral-character keywords present (count={mor})')
    return (C_MORAL, 'LOW',
            'Default for Moral/Conscience; no clear signal. Researcher review.')


def classify_character_disposition(ctx):
    rel = matches(ctx, RELATIONAL_KW)
    mor = matches(ctx, MORAL_KW)
    if rel >= 1 and rel >= mor:
        return (C_REL, 'MEDIUM',
                f'Relational-orientation keywords (count={rel})')
    if mor >= 1:
        return (C_MORAL, 'MEDIUM',
                f'Moral-character keywords (count={mor})')
    return (C_MORAL, 'LOW',
            'Default for Character/Disposition; no strong signal. Researcher review.')


def classify_spiritual_godward(ctx):
    dhc = matches(ctx, DHC_KW)
    dep = matches(ctx, DEPEND_KW)
    rel = matches(ctx, RELATIONAL_KW)
    if dhc >= 1:
        return (C_DHC, 'HIGH' if dhc >= 2 else 'MEDIUM',
                f'Divine-human correspondence signals (count={dhc})')
    if dep >= 1:
        return (C_DEP, 'MEDIUM',
                f'Dependence-on-God signals (count={dep})')
    if rel >= 1:
        return (C_REL, 'LOW',
                f'Relational-to-God reading (keywords={rel}); best-fit 06. CANDIDATE NEW DIMENSION — distinct Dim 12 God-ward may fit better.')
    return (C_DHC, 'LOW',
            'No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12.')


def classify_identity_selfhood(ctx):
    vit = matches(ctx, VITALITY_KW)
    if ('image of god' in (ctx or '').lower()
            or 'image of the lord' in (ctx or '').lower()):
        return (C_DHC, 'MEDIUM',
                'Image-of-God / divine reflection → 11. CANDIDATE NEW DIMENSION — distinct Identity dim possible.')
    if vit >= 2:
        return (C_VIT, 'MEDIUM',
                f'Vitality/existence keywords (count={vit}); essential-being reading; best-fit 07.')
    return (C_VIT, 'LOW',
            'Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension.')


def classify_somatic_embodied(ctx):
    vit = matches(ctx, VITALITY_KW)
    if vit >= 1:
        return (C_VIT, 'HIGH',
                f'Somatic/embodied → 07 Vitality/Existence (keywords={vit}). Phase A analyst anticipated this mapping.')
    return (C_VIT, 'MEDIUM',
            'Default for Somatic/Embodied → 07 Vitality/Existence.')


CLASSIFIERS = {
    'Affective/Emotional': classify_affective,
    'Moral/Conscience': classify_moral_conscience,
    'Character/Disposition': classify_character_disposition,
    'Spiritual/God-ward': classify_spiritual_godward,
    'Identity/Selfhood': classify_identity_selfhood,
    'Identity / Selfhood': classify_identity_selfhood,
    'Somatic/Embodied': classify_somatic_embodied,
}

results = []
for r in rows:
    ctx = r.get('context_description') or ''
    legacy = r['legacy_label']
    fn = CLASSIFIERS.get(legacy)
    if fn is None:
        proposed, conf, rationale = ('?', 'LOW', 'No classifier for legacy label')
    else:
        proposed, conf, rationale = fn(ctx)
    results.append({
        'wdi_id': r['wdi_id'],
        'legacy_label': legacy,
        'registry_no': r['registry_no'],
        'word': r['word'],
        'group_code': r['group_code'],
        'context_description': ctx,
        'proposed_canonical': proposed,
        'confidence': conf,
        'rationale': rationale,
    })

now_iso = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
prop_counts = Counter(r['proposed_canonical'] for r in results)
conf_counts = Counter(r['confidence'] for r in results)
legacy_counts = Counter(r['legacy_label'] for r in results)

md_lines = []
md_lines.append(f"# Directive Result — DIR-20260420-002 — Dim-Label Canonicalisation Proposals — 2026-04-20\n")
md_lines.append("| Field | Value |")
md_lines.append("|---|---|")
md_lines.append("| Directive | DIR-20260420-002 |")
md_lines.append("| Produced by | Claude Code — HEURISTIC CLASSIFIER (rule-based; not an AI analytical pass) |")
md_lines.append(f"| Produced at | {now_iso} |")
md_lines.append("| Scope | 110 rows across 7 non-canonical legacy labels |")
md_lines.append("| Output | Per-row canonical proposal + confidence + rationale |")
md_lines.append("| Status | CC proposals — researcher review required before encoding as DIMREVIEW patch |\n")
md_lines.append("---\n")

md_lines.append("## Producer note\n")
md_lines.append("The directive asked for per-group analytical mapping (semantic reading of context_description) — traditionally Claude AI territory. CC has produced a **heuristic rule-based classifier** applying keyword-match rules. This delivers:\n")
md_lines.append("- Mechanical consistency — same rule applies to every row with the same legacy label")
md_lines.append("- Conservative confidence — MEDIUM/LOW where the rule is not decisive")
md_lines.append("- Explicit escalation markers — LOW rows flagged for researcher review or Claude AI pass\n")
md_lines.append("**Two paths from here:**")
md_lines.append("- **(A)** Researcher accepts HIGH/MEDIUM directly → CC encodes DIMREVIEW patch; routes LOW + new-dim candidates to Claude AI")
md_lines.append("- **(B)** Researcher skips CC heuristic; waits for Claude AI analytical pass on all 110")
md_lines.append("\nCC recommendation: **(A)**.\n")
md_lines.append("---\n")

md_lines.append("## Summary\n")
md_lines.append("**Proposed canonical distribution (110 rows):**\n")
md_lines.append("| Proposed canonical | Count |\n|---|---:|")
for p, n in prop_counts.most_common():
    md_lines.append(f"| `{p}` | {n} |")
md_lines.append("")
md_lines.append("**Confidence distribution:**\n")
md_lines.append("| Confidence | Count |\n|---|---:|")
for c, n in conf_counts.most_common():
    md_lines.append(f"| {c} | {n} |")
md_lines.append("")

by_legacy_prop = {}
for r in results:
    by_legacy_prop.setdefault(r['legacy_label'], Counter())[r['proposed_canonical']] += 1
md_lines.append("**Legacy-label breakdown:**\n")
md_lines.append("| Legacy label | Rows | Dominant proposal |\n|---|---:|---|")
for legacy, counts in sorted(by_legacy_prop.items(), key=lambda x: -sum(x[1].values())):
    dom, dom_n = counts.most_common(1)[0]
    total = sum(counts.values())
    md_lines.append(f"| `{legacy}` | {total} | `{dom}` ({dom_n}/{total}) |")
md_lines.append("")

md_lines.append("---\n")
new_dim_rows = [r for r in results if 'CANDIDATE NEW DIMENSION' in (r['rationale'] or '').upper()]
md_lines.append(f"## New-dimension candidates flagged: {len(new_dim_rows)}\n")
md_lines.append("These are the vocabulary-gap cases from Phase A — best-fit under current vocabulary, but a distinct Dim 12+ may fit better. Researcher decision required.\n")

md_lines.append("---\n")
md_lines.append("## Per-row proposals\n")
md_lines.append("Grouped by legacy label, ordered by registry + group_code within each.\n")
for legacy in sorted(by_legacy_prop.keys()):
    md_lines.append(f"### {legacy} ({legacy_counts[legacy]} rows)\n")
    md_lines.append("| wdi_id | Reg | Word | Group | Context (truncated) | Proposed | Conf | Rationale |")
    md_lines.append("|---:|---:|---|---|---|---|---|---|")
    rs = [r for r in results if r['legacy_label'] == legacy]
    rs.sort(key=lambda x: (x['registry_no'], x['group_code']))
    for r in rs:
        ctx = (r['context_description'] or '').replace('|', '\\|').replace('\n', ' ')
        if len(ctx) > 120:
            ctx = ctx[:117] + '...'
        rationale = (r['rationale'] or '').replace('|', '\\|')
        if len(rationale) > 140:
            rationale = rationale[:137] + '...'
        md_lines.append(
            f"| {r['wdi_id']} | {r['registry_no']} | {r['word']} | {r['group_code']} | "
            f"{ctx} | `{r['proposed_canonical']}` | {r['confidence']} | {rationale} |"
        )
    md_lines.append("")

md_lines.append("---\n")
md_lines.append("## Next action\n")
md_lines.append("1. HIGH-confidence rows → CC encodes DIMREVIEW patch")
md_lines.append("2. MEDIUM-confidence rows → researcher accepts or requests Claude AI review")
md_lines.append("3. LOW-confidence + new-dim candidates → Claude AI analytical pass OR researcher direct decision")
md_lines.append("\nPatch naming (when produced): `PATCH-20260420-DIMREVIEW-GLOBAL-CANONICALISATION-V1.json` (cross-registry).\n")
md_lines.append("---\n")
md_lines.append("*Directive DIR-20260420-002 result — CC heuristic proposals for researcher review.*\n")

md_path = Path('outputs/wa-global-dirresult-002-dim-label-proposals-v1-20260420.md')
md_path.write_text('\n'.join(md_lines), encoding='utf-8')

json_path = Path('outputs/wa-global-dirresult-002-dim-label-proposals-v1-20260420.json')
json_path.write_text(json.dumps({
    'meta': {
        'directive_id': 'DIR-20260420-002',
        'produced_by': 'claude_code_heuristic',
        'produced_at': now_iso,
        'row_count': len(results),
        'proposed_counts': dict(prop_counts),
        'confidence_counts': dict(conf_counts),
    },
    'proposals': results,
}, indent=2, ensure_ascii=False), encoding='utf-8')

print(f'Wrote: {md_path}')
print(f'Wrote: {json_path}')
print()
print('=== Confidence distribution ===')
for c, n in conf_counts.most_common():
    print(f'  {c}: {n}')
print()
print('=== Proposed canonical distribution ===')
for p, n in prop_counts.most_common():
    print(f'  {p}: {n}')
print()
print(f'New-dimension candidates: {len(new_dim_rows)}')
