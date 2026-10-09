"""Item F (#1993), group B: the bucket-1 verses still unread after sets 1 and 2 (the 77 verb verses), for the
researcher's review. Data only. Source: m18-group-B-bucket1-list-v1-20261009.py logic, less the B1 and B2 registers.
The 'stock phrase' column is a text hint only ("seems good to you", "if it please", "as you please" and the like);
it decides nothing. Output: m18-group-B-bucket1-remaining-v1-20261009.md
"""
import csv, os, re
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: list(csv.DictReader(open(os.path.join(HERE, f), encoding='utf-8-sig')))
pull = {r['reference']: r for r in rd('m18-group-B-pull-v1-20261009.csv')}
done = {r['reference'] for f in ('m18-group-B1-register-v1-20261009.csv', 'm18-group-B2-register-v1-20261009.csv') for r in rd(f)}
hits = defaultdict(list)
for r in rd('m18-delight-pleasure-filter-v1-20261008.csv'):
    if r['reference'] in pull: hits[r['reference']].append(r)
STOCK = re.compile(r"(seems? good (to|in)|seemed good|if it please|as you please|as it pleases|whatever (seems|you) |where it pleases|wherever it suits|do (to|with) (us|me|her|them|him) (as|what|whatever)|in the (eyes|sight) of)", re.I)
by = defaultdict(list)
for ref in pull:
    if ref in done: continue
    b1 = [h for h in hits[ref] if h['filter_bucket'].startswith('1')]
    if not b1: continue
    by[b1[0]['pattern']].append((ref, b1[0]))
order = sorted(by, key=lambda p: -len(by[p]))
n = sum(len(v) for v in by.values())
with open(os.path.join(HERE, 'm18-group-B-bucket1-remaining-v1-20261009.md'), 'w', encoding='utf-8') as f:
    f.write('# M18 group B: bucket 1 verses still to read, for review\n\n'
            '**Date:** 2026-10-09 · **Escalation:** #1993 (handoff v7 item F) · data only, no readings. Script: `m18-group-B-bucket1-remaining-v1-20261009.py`.\n\n'
            f'Bucket 1 held 171 verses ([`m18-group-B-bucket1-list-v1-20261009.md`](m18-group-B-bucket1-list-v1-20261009.md)). Sets 1 and 2 read and wove the 77 verb verses. **{n} remain.** '
            'They are grouped by the pairing filter\'s pattern for the verse\'s first bucket-1 hit.\n\n'
            '- **★** = already cited or quoted in the narrative.\n'
            '- **Stock** = the verse uses a stock phrase ("seems good to you", "if it please the king", "as you please", "in the sight of"). It is a text hint only.\n\n'
            '| Pattern | Verses | Stock phrase |\n|---|---|---|\n')
    for p in order:
        f.write(f'| {p} | {len(by[p])} | {sum(1 for r, h in by[p] if STOCK.search(pull[r]["text"]))} |\n')
    sc = Counter(h['strong'] + ' ' + h['gloss'] for p in order for r, h in by[p])
    f.write('\n| Strong\'s | Verses |\n|---|---|\n' + ''.join(f'| {s} | {k} |\n' for s, k in sc.most_common()) + '\n')
    for p in order:
        f.write(f'## {p} ({len(by[p])})\n\n| # | Verse | Word | Stock | Narr | Text |\n|---|---|---|---|---|---|\n')
        rows = sorted(by[p], key=lambda x: (x[1]['strong'], bool(STOCK.search(pull[x[0]]['text']))))
        for i, (ref, h) in enumerate(rows, 1):
            r = pull[ref]
            f.write(f"| {i} | {ref} | {h['strong']} \"{h['surface']}\" | {'stock' if STOCK.search(r['text']) else ''} | "
                    f"{'★' if r['narrative_parser'] or r['narrative_text_found'] else ''} | {r['text'].replace('|', '/')} |\n")
        f.write('\n')
print(n, {p: len(v) for p, v in by.items()}, sc)
