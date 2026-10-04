"""Faces for the unit 3 supplement (LD-138 approved, #1940): H2416C / H2416D, 109 hits.
Every "life" hit is named by verse after reading; the rest are assigned by surface
(beasts, living creatures) and checked by reading. Refuses to write if a hit is unfaced.
Usage: python life-death-unit3-supplement-face-assign-v1-20261004.py  (then merge with --faces)
"""
import csv, sys
PULL = 'life-death-unit3-supplement-h2416c-pull-v1-20261004.csv'
OUT = 'life-death-unit3-supplement-faces-v1-20261004.csv'
NAMES = {
    'L33': 'Life brought back from the pit',
    'L34': 'Life given over',
    'L35': 'New life found for strength',
    'L36': 'The life of the poor, not to be forgotten',
    'L14': 'Life weighed from within',
    'L06': 'Living creatures',
    'L07': 'Not the inner being',
}
BY_VERSE = {
    'Job 33:18': 'L33', 'Job 33:20': 'L33', 'Job 33:22': 'L33', 'Job 33:28': 'L33',
    'Psa 78:50': 'L34', 'Job 36:14': 'L34',
    'Isa 57:10': 'L35',
    'Psa 74:19': 'L36',
    'Psa 143:3': 'L14', 'Eze 7:13': 'L14',   # already read: LD-58, LD-112
    'Job 38:39': 'L07', '2Sa 23:11': 'L07', '2Sa 23:13': 'L07', 'Psa 68:10': 'L07',
}
rows = list(csv.DictReader(open(PULL, encoding='utf-8')))
out, missing = [], []
for r in rows:
    ref, s = r['reference'], r['surface'].lower()
    f = BY_VERSE.get(ref)
    if ref == 'Psa 74:19' and 'beast' in s:
        f = 'L06'   # hit level: the same verse has "wild beasts" (H2416C) and "life" (H2416D)
    if f is None and ref.startswith('Eze ') and 'living creature' in s:
        f = 'L07'   # the living creatures (cherubim) of Ezekiel's vision
    if f is None and any(w in s for w in ('beast', 'animal', 'living creature', 'living thing')):
        f = 'L06'
    if f is None:
        missing.append(ref + ' ' + r['surface'])
    else:
        out.append({'reference': ref, 'position': r['position'], 'face': f, 'face_name': NAMES[f]})
if missing:
    sys.exit('unfaced: ' + '; '.join(missing))
with open(OUT, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['reference', 'position', 'face', 'face_name']); w.writeheader(); w.writerows(out)
from collections import Counter
print(len(out), 'faced', Counter(o['face'] for o in out))
