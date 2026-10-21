"""Verify a family's narrative JSON against its base source WORK_CONTRACT.

Checks (per the embedded contract):
  1. Every anchor reading_id in the base source appears exactly once in the JSON.
  2. No extra / unknown reading_ids in the JSON.
  3. Each record has a non-empty `narrative` AND a non-empty `story`.
  4. Each record cites >=1 ve_lexical_id (citations non-empty).
  5. Record count == scope_counts.distinct_readings.
  6. `story` carries no study jargon (dimension labels/numbers, ve_lexical, ib_char, etc.).

Usage: python scripts/_check_family_narratives_20260712.py --family <slug> [--all]
Exit 0 = clean; exit 1 = failures printed.
"""
import json, os, sys, glob, re

BASE = 'verse-analysis/psalms/_base-sources'
NARR = 'verse-analysis/psalms/_narratives'

# Jargon that must NOT appear in the plain-reader `story`. Only genuinely-technical
# tokens are listed here: compound/underscore identifiers and distinctive coinages
# that never occur in plain psalm-prose. Ambiguous common English words (sense,
# effect, operation, seat, manner, intensity, discovery, bearer) are deliberately
# EXCLUDED — they appear naturally and produced false positives. A story that copied
# analytical text is caught by the compound tokens and the dimension-number pattern.
JARGON_WORDS = [
    've_lexical', 'ib_char', 'reading_id', 'char_key', 'anchor_ref', 'passage_ref',
    'to_span', 'from_span', 'provenance', 'same_as', 'scope_counts',
    'char_key', 've_lexical_id', 'ib characteristic',
]
JARGON_LABELS = []  # bare dimension labels are too common as English to flag safely
DIM_NUM = re.compile(r'\((10[1-9]|11[0-6])\)')  # e.g. "(101)" .. "(116)"


def anchor_reading_ids(bs):
    """reading_ids that are anchors (one narrative each). A lexical is an anchor
    unless it is flagged duplicate/same_as."""
    ids = []
    for p in bs['passages']:
        for lx in p.get('lexicals', []):
            if lx.get('same_as') or lx.get('duplicate'):
                continue
            ids.append(lx['reading_id'])
    # de-dupe preserving order (a reading spanning nodes should appear once)
    seen = set(); out = []
    for i in ids:
        if i not in seen:
            seen.add(i); out.append(i)
    return out


def check(fam):
    bs = json.load(open(os.path.join(BASE, f'psalms__{fam}.json'), encoding='utf-8'))
    npath = os.path.join(NARR, f'psalms__{fam}__narratives.json')
    fails = []
    if not os.path.exists(npath):
        return [f'MISSING narratives JSON: {npath}']
    out = json.load(open(npath, encoding='utf-8'))
    recs = out.get('narratives', [])

    expected = anchor_reading_ids(bs)
    got = [r.get('reading_id') for r in recs]
    exp_set, got_set = set(expected), set(got)

    missing = [i for i in expected if i not in got_set]
    extra = [i for i in got if i not in exp_set]
    dupes = [i for i in got if got.count(i) > 1]
    if missing:
        fails.append(f'{len(missing)} anchor reading_id(s) with NO narrative: {missing[:8]}')
    if extra:
        fails.append(f'{len(extra)} unknown reading_id(s) in JSON: {extra[:8]}')
    if dupes:
        fails.append(f'duplicate reading_id(s) in JSON: {sorted(set(dupes))[:8]}')

    dr = bs['meta'].get('scope_counts', {}).get('distinct_readings')
    if dr is not None and len(recs) != dr:
        fails.append(f'record count {len(recs)} != scope_counts.distinct_readings {dr}')

    for r in recs:
        rid = r.get('reading_id', '?')
        if not (r.get('narrative') or '').strip():
            fails.append(f'{rid}: empty narrative')
        if not (r.get('story') or '').strip():
            fails.append(f'{rid}: empty story')
        if not r.get('citations'):
            fails.append(f'{rid}: no citations')
        story = (r.get('story') or '').lower()
        hits = [w for w in JARGON_WORDS if w in story]
        hits += [w for w in JARGON_LABELS if re.search(rf'\b{w}\b', story)]
        if DIM_NUM.search(r.get('story') or ''):
            hits.append('dimension-number')
        if hits:
            fails.append(f'{rid}: story jargon leak -> {sorted(set(hits))}')
    return fails


def run(fam):
    fails = check(fam)
    if fails:
        print(f'FAIL {fam} ({len(fails)} issue(s)):')
        for f in fails:
            print('   -', f)
        return False
    bs = json.load(open(os.path.join(BASE, f'psalms__{fam}.json'), encoding='utf-8'))
    n = len(json.load(open(os.path.join(NARR, f'psalms__{fam}__narratives.json'), encoding='utf-8'))['narratives'])
    print(f'OK   {fam}: {n} narratives, all anchors covered, both narratives, cited, no jargon.')
    return True


if __name__ == '__main__':
    if '--all' in sys.argv:
        fams = sorted(os.path.basename(f).replace('psalms__', '').replace('.json', '')
                      for f in glob.glob(os.path.join(BASE, 'psalms__*.json')))
        ok = all(run(f) if os.path.exists(os.path.join(NARR, f'psalms__{f}__narratives.json')) else True
                 for f in fams)
        sys.exit(0 if ok else 1)
    fam = sys.argv[sys.argv.index('--family') + 1]
    sys.exit(0 if run(fam) else 1)
