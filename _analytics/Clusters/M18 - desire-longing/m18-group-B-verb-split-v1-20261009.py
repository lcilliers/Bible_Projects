"""Item F (#1993), group B: split the 77 bucket-1 'verb' verses into delight words and pleasant/pleased words
(researcher, 2026-10-09: "split the 77 between delight related words and pleasant related words"). Split by Strong's
of the verse's first bucket-1 verb hit, so a word family stays together. Data only.
Output: m18-group-B-verb-split-v1-20261009.md (lists) and m18-group-B-verb-{delight,pleasant}-passages-v1-20261009.md
(the worksheet entries for each set, with passages).
"""
import csv, os, re
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: list(csv.DictReader(open(os.path.join(HERE, f), encoding='utf-8-sig')))
DELIGHT = {'H2654A': 'ḥāpēṣ, to delight in', 'H6026': 'ʿānag, to delight', 'H8173B': 'šāʿaʿ, to delight', 'G4913': 'synēdomai, to delight'}
PLEASANT = {'H5276': 'nāʿēm, be pleasant', 'G2106': 'eudokeō, to be pleased'}
pull = {r['reference']: r for r in rd('m18-group-B-pull-v1-20261009.csv')}
hits = defaultdict(list)
for r in rd('m18-delight-pleasure-filter-v1-20261008.csv'):
    if r['reference'] in pull: hits[r['reference']].append(r)
sets = {'delight': defaultdict(list), 'pleasant': defaultdict(list)}
for ref in pull:
    b1 = [h for h in hits[ref] if h['filter_bucket'].startswith('1')]
    if not b1 or b1[0]['pattern'] != 'verb (delight, please, be pleasant)': continue
    s = b1[0]['strong']
    sets['delight' if s in DELIGHT else 'pleasant'][s].append((ref, b1[0]['surface']))
ws = open(os.path.join(HERE, 'm18-group-B-worksheet-v1-20261009.md'), encoding='utf-8').read()
entries = {m.group(1): m.group(0) for m in re.finditer(r'^### (.+?)\n.*?(?=^### |^## |\Z)', ws, re.S | re.M)}
star = lambda r: '★' if pull[r]['narrative_parser'] or pull[r]['narrative_text_found'] else ''
with open(os.path.join(HERE, 'm18-group-B-verb-split-v1-20261009.md'), 'w', encoding='utf-8') as f:
    n = {k: sum(len(v) for v in d.values()) for k, d in sets.items()}
    f.write('# M18 group B: the 77 bucket-1 verb verses, split into delight and pleasant\n\n'
            '**Date:** 2026-10-09 · **Escalation:** #1993 (handoff v7 item F) · data only.\n\n'
            'Researcher, verbatim: *"split the 77 between delight related words and pleasant related words. and read them in two separate sessions."* '
            'The split is by Strong\'s number, so each word family stays in one set. The English surface can cross the line: *ḥāpēṣ* is rendered "pleases" or "desire" in some verses, '
            'and *eudokeō* "willing" or "content". Source: [`m18-group-B-bucket1-list-v1-20261009.md`](m18-group-B-bucket1-list-v1-20261009.md). '
            'Script: `m18-group-B-verb-split-v1-20261009.py`.\n\n'
            f'| Set | Strong\'s | Verses | Session |\n|---|---|---|---|\n'
            f"| 1. Delight | {', '.join(DELIGHT)} | {n['delight']} | first |\n| 2. Pleasant, pleased | {', '.join(PLEASANT)} | {n['pleasant']} | second |\n\n")
    for k, names in (('delight', DELIGHT), ('pleasant', PLEASANT)):
        f.write(f"## Set {'1. Delight' if k == 'delight' else '2. Pleasant, pleased'} ({n[k]})\n\n")
        for s in names:
            if s not in sets[k]: continue
            f.write(f"### {s} *{names[s]}* ({len(sets[k][s])})\n\n| # | Verse | Surface | Narr |\n|---|---|---|---|\n")
            for i, (r, sf) in enumerate(sets[k][s], 1): f.write(f'| {i} | {r} | {sf} | {star(r)} |\n')
            f.write('\n')
        with open(os.path.join(HERE, f'm18-group-B-verb-{k}-passages-v1-20261009.md'), 'w', encoding='utf-8') as g:
            g.write(f'# M18 group B, verb set {k}: passages (data only)\n\nFrom `m18-group-B-worksheet-v1-20261009.md`.\n\n')
            for s in names:
                for r, _ in sets[k].get(s, []): g.write(entries[r] + '\n')
print({k: {s: len(v) for s, v in d.items()} for k, d in sets.items()})
