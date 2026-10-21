"""Coverage of a strand's verses by face: narrative citation and register claims (read-only).

Usage: python life-death-ot02-face-coverage-v1-20261014.py CROSSCHECK.csv FACES.csv OUT.csv [DATA_FACES]
CROSSCHECK = output of life-death-claim-register-crosscheck-v2 (one row per verse x citing paragraph).
FACES      = a unit faces file (reference, position, face, face_name); a verse takes every face of its hits.
DATA_FACES = comma list of faces read as data only (default D01,D02,D03,D26,D27).
Writes one row per verse: reference, faces, data_only (every face is a data face), cited (chapters/sections),
claims (refs), status = both | narrative_only | register_only | neither. Prints a table per face.
"""
import csv, sys
from collections import defaultdict, Counter

cc, faces_f, out = sys.argv[1:4]
data = set((sys.argv[4] if len(sys.argv) > 4 else 'D01,D02,D03,D26,D27').split(','))

faces, names = defaultdict(set), {}
for r in csv.DictReader(open(faces_f, encoding='utf-8-sig')):
    faces[r['reference']].add(r['face']); names[r['face']] = r['face_name']

v = {}
for r in csv.DictReader(open(cc, encoding='utf-8-sig')):
    e = v.setdefault(r['reference'], {'strongs': r['strongs_in_verse'], 'cited': set(), 'claims': set()})
    if r['chapter']:
        e['cited'].add(f"{r['chapter']} {r['section']}")
    for c in filter(None, (x.strip() for x in r['claims_sourcing_verse'].split(' | '))):
        e['claims'].add(c.split(':')[0])

rows, per = [], defaultdict(Counter)
for ref, e in v.items():
    fs = faces.get(ref, {'(no face)'})
    st = ('both' if e['cited'] and e['claims'] else 'narrative_only' if e['cited']
          else 'register_only' if e['claims'] else 'neither')
    do = all(f in data for f in fs)
    rows.append({'reference': ref, 'faces': ' '.join(sorted(fs)), 'data_only': int(do), 'status': st,
                 'cited': ' | '.join(sorted(e['cited'])), 'claims': ' | '.join(sorted(e['claims'])),
                 'strongs': e['strongs']})
    for f in fs:
        per[f][st] += 1

with open(out, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)

print('| face | name | verses | both | narrative only | register only | neither |')
print('|---|---|---|---|---|---|---|')
for fc in sorted(per):
    c = per[fc]
    print(f"| {fc}{' (data)' if fc in data else ''} | {names.get(fc, '')} | {sum(c.values())} | {c['both']} | "
          f"{c['narrative_only']} | {c['register_only']} | {c['neither']} |")
t = Counter(r['status'] for r in rows); d = Counter(r['status'] for r in rows if r['data_only'])
print(f"\nverses {len(rows)}: {dict(t)}; data-only verses {sum(d.values())}: {dict(d)}")
