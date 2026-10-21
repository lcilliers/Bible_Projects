"""Item F (#1993), group B: the verses left to read (after filtering) that hold at least one bucket-1 hit
(inner-being candidate) in the pairing filter. Data only. Output: m18-group-B-bucket1-list-v1-20261009.md
"""
import csv, os
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: list(csv.DictReader(open(os.path.join(HERE, f), encoding='utf-8-sig')))
pull = {r['reference']: r for r in rd('m18-group-B-pull-v1-20261009.csv')}
hits = defaultdict(list)
for r in rd('m18-delight-pleasure-filter-v1-20261008.csv'):
    if r['reference'] in pull: hits[r['reference']].append(r)
b1 = [ref for ref in pull if any(h['filter_bucket'].startswith('1') for h in hits[ref])]
# group by the pattern of the first bucket-1 hit in the verse
by = defaultdict(list)
for ref in b1:
    h = next(h for h in hits[ref] if h['filter_bucket'].startswith('1'))
    by[h['pattern']].append((ref, h))
with open(os.path.join(HERE, 'm18-group-B-bucket1-list-v1-20261009.md'), 'w', encoding='utf-8') as f:
    f.write('# M18 group B: bucket 1 (inner-being candidates) among the verses left to read\n\n'
            '**Date:** 2026-10-09 · **Escalation:** #1993 (handoff v7 item F) · data only, no readings.\n\n'
            f'Of the 448 verses left after filtering ([`m18-group-B-verse-list-v1-20261009.md`](m18-group-B-verse-list-v1-20261009.md)), '
            f'**{len(b1)}** hold at least one hit the pairing filter put in bucket 1 '
            '([`m18-delight-pleasure-pairing-filter-v1-20261008.md`](m18-delight-pleasure-pairing-filter-v1-20261008.md) §2.3). '
            'Grouped by the filter pattern of the verse\'s first bucket-1 hit. ★ = already in the narrative (cited or text found). '
            'Script: `m18-group-B-bucket1-list-v1-20261009.py`.\n\n| Pattern | Verses |\n|---|---|\n')
    for p in sorted(by, key=lambda p: -len(by[p])): f.write(f'| {p} | {len(by[p])} |\n')
    sc = Counter(h['strong'] + ' ' + h['gloss'] for ref in b1 for h in hits[ref] if h['filter_bucket'].startswith('1'))
    f.write('\n| Strong\'s (bucket-1 hits) | Hits |\n|---|---|\n')
    for s, n in sc.most_common(): f.write(f'| {s} | {n} |\n')
    f.write('\n')
    for p in sorted(by, key=lambda p: -len(by[p])):
        f.write(f'## {p} ({len(by[p])})\n\n| # | Verse | Word | Text | Narr |\n|---|---|---|---|---|\n')
        for i, (ref, h) in enumerate(by[p], 1):
            r = pull[ref]
            t = r['text'].replace('|', '/')
            f.write(f"| {i} | {ref} | {h['strong']} \"{h['surface']}\" | {t} | {'★' if r['narrative_parser'] or r['narrative_text_found'] else ''} |\n")
        f.write('\n')
print(len(b1), {p: len(v) for p, v in by.items()})
