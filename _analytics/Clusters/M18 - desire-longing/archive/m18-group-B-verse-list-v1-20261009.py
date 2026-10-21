"""Item F (#1993), group B: compact list of the verses still to read after filtering (data only).
Reads m18-group-B-pull-v1-20261009.csv (built by m18-group-pull-worksheet-v1-20261009.py B) and adds the pairing
filter bucket of each hit as a hint only (m18-delight-pleasure-filter-v1-20261008.csv). Output: m18-group-B-verse-list-v1-20261009.md
"""
import csv, os
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: list(csv.DictReader(open(os.path.join(HERE, f), encoding='utf-8-sig')))
pull = rd('m18-group-B-pull-v1-20261009.csv')
WANT = set('H2896A H2654A H2656 G2106 H2895 H2655 H5273A H6026 H8191 H5276 H5278 H8173B G2237 G0701 H6027 H5282 H5730B G4913 G5369'.split())
hits = [h for h in rd('m18-cluster-hits-v1-20261008.csv') if h['strong'] in WANT]
bucket = defaultdict(set)
for r in rd('m18-delight-pleasure-filter-v1-20261008.csv'):
    bucket[(r['reference'], r['strong'])].add(r['filter_bucket'])
keep = {r['reference'] for r in pull}
allv = {h['reference'] for h in hits}
B = lambda ref, s: '/'.join(sorted(b.strip()[:1] for b in bucket.get((ref, s), []))) or '-'
by = defaultdict(list)
for r in pull: by[r['first_strong']].append(r)
vb = Counter()
for r in pull:
    bs = {B(r['reference'], w.split()[0]) for w in r['group_words'].split(' ; ')}
    vb['1' if any('1' in b for b in bs) else ('2' if any('2' in b for b in bs) else '3')] += 1
with open(os.path.join(HERE, 'm18-group-B-verse-list-v1-20261009.md'), 'w', encoding='utf-8') as f:
    f.write('# M18 group B (delight, pleasure): verses to read after filtering\n\n'
            '**Date:** 2026-10-09 · **Escalation:** #1993 (handoff v7 item F) · data only, no readings.\n\n'
            'Built from [`m18-group-B-pull-v1-20261009.csv`](m18-group-B-pull-v1-20261009.csv) (script `m18-group-pull-worksheet-v1-20261009.py B`); '
            f'passages are in [`m18-group-B-worksheet-v1-20261009.md`](m18-group-B-worksheet-v1-20261009.md). List script: `m18-group-B-verse-list-v1-20261009.py`.\n\n'
            '## 1. The filter\n\n'
            f'| | Verses |\n|---|---|\n| Group B verses (19 Strong\'s, {len(hits)} hits) | {len(allv)} |\n'
            f'| Dropped: already decided in the M47, M25, M02 read-backs or groups A, D, E, F, G | {len(allv - keep)} |\n'
            f'| **To read** | **{len(keep)}** |\n\n'
            f'Of the {len(keep)}, {sum(1 for r in pull if r["narrative_parser"] or r["narrative_text_found"])} are already cited or quoted somewhere in the narrative. '
            'They are still read, because a citation is verse-level and does not mean the M18 word is covered (#1987).\n\n'
            'The pairing bucket is shown as a hint only (1 = inner-being candidate, 2 = qualifies another characteristic, 3 = qualifies a thing, person, place or act). '
            'It does not take a verse out of the reading. By the strongest bucket per verse: '
            f'bucket 1: {vb["1"]}, bucket 2: {vb["2"]}, bucket 3: {vb["3"]}.\n\n'
            '★ = already in the narrative (cited or text found).\n\n## 2. The verses, by Strong\'s\n\n')
    for s in sorted(by, key=lambda s: -len(by[s])):
        g = by[s][0]['group_words'].split(' ; ')[0]
        gloss = g.split('"')[0].split(' ', 1)[1].strip()
        f.write(f'### {s} {gloss} ({len(by[s])})\n\n| # | Verse | Word(s) | Bucket | Narr |\n|---|---|---|---|---|\n')
        for i, r in enumerate(by[s], 1):
            ws = r['group_words'].split(' ; ')
            surf = ', '.join(w.split('"')[1] for w in ws if '"' in w)
            bk = ', '.join(sorted({B(r['reference'], w.split()[0]) for w in ws}))
            f.write(f"| {i} | {r['reference']} | {surf} | {bk} | {'★' if r['narrative_parser'] or r['narrative_text_found'] else ''} |\n")
        f.write('\n')
print(len(allv), len(allv - keep), len(keep), dict(vb))
