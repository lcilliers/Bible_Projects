"""Faces for life-death unit 4 (H5782 "to rouse"), 78 hits in 64 verses. Every verse named by reading.
Refuses to write if any hit is unfaced, or if any assignment matches no hit.
Usage (from this folder):
  python life-death-unit4-face-assign-v1-20261004.py
  then, from the repo root: strand-unit-pull-v1-20261002.py <pull.csv> --faces <faces.csv>
"""
import csv, sys
PULL = 'life-death-unit4-roused-stirred-pull-v1-20261004.csv'
OUT = 'life-death-unit4-faces-v1-20261004.csv'
NAMES = {
    'W01': 'Not roused from the sleep of death',
    'W02': 'Sheol roused',
    'W03': 'No breath to be woken',
    'W04': 'God stirs up the spirit',
    'W05': 'God stirs up a person or people',
    'W06': 'God called to awake',
    'W07': 'God roused, or holding back',
    'W08': 'Wake yourself (the people)',
    'W09': 'Rousing oneself toward God',
    'W10': 'The heart awake',
    'W11': 'Love not stirred before its time',
    'W12': 'Hatred and strife',
    'W13': 'The ear awakened',
    'W14': 'Awake to praise',
    'W15': 'Woken for a vision',
    'W16': 'The sword roused against the shepherd',
    'W17': 'Not the inner being',
}
F = {
    'W01': ['Job 14:12'], 'W02': ['Isa 14:9'], 'W03': ['Hab 2:19'],
    'W04': ['1Ch 5:26', '2Ch 21:16', '2Ch 36:22', 'Ezr 1:1', 'Ezr 1:5', 'Hag 1:14', 'Jer 51:1', 'Jer 51:11'],
    'W05': ['Isa 41:2', 'Isa 41:25', 'Isa 45:13', 'Isa 13:17', 'Jer 50:9', 'Eze 23:22', 'Joe 3:7', 'Zec 9:13'],
    'W06': ['Psa 7:6', 'Psa 35:23', 'Psa 44:23', 'Psa 59:4', 'Isa 51:9', 'Psa 80:2'],
    'W07': ['Zec 2:13', 'Isa 42:13', 'Psa 73:20', 'Psa 78:38', 'Job 8:6'],
    'W08': ['Isa 51:17', 'Isa 52:1'], 'W09': ['Isa 64:7'], 'W10': ['Song 5:2'],
    'W11': ['Song 2:7', 'Song 3:5', 'Song 8:4', 'Song 8:5'],
    'W12': ['Pro 10:12', 'Job 17:8', 'Job 31:29', 'Dan 11:25'],
    'W13': ['Isa 50:4'], 'W14': ['Psa 57:8', 'Judg 5:12'], 'W15': ['Zec 4:1'], 'W16': ['Zec 13:7'],
    'W17': ['Jer 6:22', 'Jer 25:32', 'Jer 50:41', 'Joe 3:9', 'Joe 3:12', 'Dan 11:2', '2Sa 23:18', '1Ch 11:11',
            '1Ch 11:20', 'Isa 10:26', 'Job 3:8', 'Job 41:10', 'Song 4:16', 'Deu 32:11', 'Hos 7:4', 'Isa 15:5', 'Mal 2:12'],
}
by_ref = {}
for f, refs in F.items():
    for r in refs:
        assert r not in by_ref, r
        by_ref[r] = f
rows = list(csv.DictReader(open(PULL, encoding='utf-8')))
used, out, missing = set(), [], []
for r in rows:
    f = by_ref.get(r['reference'])
    if f is None:
        missing.append(r['reference'])
        continue
    used.add(r['reference'])
    out.append({'reference': r['reference'], 'position': r['position'], 'face': f, 'face_name': NAMES[f]})
unused = set(by_ref) - used
if missing or unused:
    sys.exit(f'unfaced: {missing}; unmatched assignments: {sorted(unused)}')
with open(OUT, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['reference', 'position', 'face', 'face_name']); w.writeheader(); w.writerows(out)
from collections import Counter
c = Counter(o['face'] for o in out)
print(len(out), 'hits faced;', dict(sorted(c.items())))
