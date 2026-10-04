"""Faces for the unit 4 supplement (H6974 "to awake", tagged T3; decision 4 approved #1949), 22 hits in 21 verses.
Every verse named by reading. Refuses to write if a hit is unfaced or an assignment matches no hit.
Usage (from this folder): python life-death-unit4-supplement-face-assign-v1-20261004.py
then, from the repo root: strand-unit-pull-v1-20261002.py <pull.csv> --faces <faces.csv>
"""
import csv, sys
PULL = 'life-death-unit4-supplement-h6974-pull-v1-20261004.csv'
OUT = 'life-death-unit4-supplement-faces-v1-20261004.csv'
NAMES = {
    'W01': 'Not roused from the sleep of death', 'W03': 'No breath to be woken',
    'W06': 'God called to awake', 'W07': 'God roused, or holding back',
    'W18': 'The dead waking', 'W19': 'The child not awakened', 'W20': 'A perpetual sleep',
    'W21': 'Waking kept by God', 'W22': 'The end awakened',
    'W23': 'Waking in the inner being', 'W17': 'Not the inner being',
}
F = {
    'W01': ['Job 14:12'], 'W03': ['Hab 2:19'], 'W06': ['Psa 59:5', 'Psa 35:23', 'Psa 44:23'], 'W07': ['Psa 73:20'],
    'W18': ['Dan 12:2', 'Isa 26:19', 'Psa 17:15'], 'W19': ['2Ki 4:31'], 'W20': ['Jer 51:39', 'Jer 51:57'],
    'W21': ['Psa 3:5', 'Psa 139:18'], 'W22': ['Eze 7:6'],
    'W23': ['Pro 23:35', 'Isa 29:8', 'Joe 1:5', 'Pro 6:22'], 'W17': ['1Sa 26:12', 'Jer 31:26'],
}
by_ref = {r: f for f, refs in F.items() for r in refs}
rows = list(csv.DictReader(open(PULL, encoding='utf-8')))
used, out, missing = set(), [], []
for r in rows:
    f = by_ref.get(r['reference'])
    if f is None:
        missing.append(r['reference']); continue
    used.add(r['reference'])
    out.append({'reference': r['reference'], 'position': r['position'], 'face': f, 'face_name': NAMES[f]})
unused = set(by_ref) - used
if missing or unused:
    sys.exit(f'unfaced: {missing}; unmatched: {sorted(unused)}')
with open(OUT, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['reference', 'position', 'face', 'face_name']); w.writeheader(); w.writerows(out)
from collections import Counter
print(len(out), 'hits faced;', dict(sorted(Counter(o['face'] for o in out).items())))
