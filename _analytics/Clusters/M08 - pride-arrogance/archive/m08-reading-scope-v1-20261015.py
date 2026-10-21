"""M08 reading scope: groups A, C, D, the 42 group B pride-sense verses and group E (#2156).

Researcher, 2026-10-15 (verbatim): "mark the 34 verses forward as suggested. then start reading A,
C and D in batches.  The Ch 13 references should include a reflection on a) are any of the pride
words indicative of their characteristics? I suspect there is difference between the 'pride','most
high' of God, which is not an assumed position but a undisputed state, verses IB pride that is
mostly assumed."

Each verse goes to the first batch (in order) that holds one of its M08 words. Verses already read
in an M09 batch register are flagged (m09_read) so the batch can check the M09 reading rather than
start again. Writes m08-reading-scope-v1-20261015.csv (one row per verse).
"""
import csv, glob, os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
BATCH = [
 ('1 gaon family + majesty', 'H1341 H1342 H1343 H1344 H1346 H1347 H1348 H1466 H1467 G3168 G3172'),
 ('2 other Hebrew pride words + B pride sense (Hebrew)', 'H2086 H2087 H2102 H2103 H3093 H5674H H6277 H7292 H7295 H7312 H7342I H7830 H7986 H1365 H1361 H1363 H1364 H4791 H5920H H5945A H6967 H7314'),
 ('3 Greek pride words + B pride sense (Greek)', 'G0212 G0213 G0829 G2755 G4409 G5187 G5229 G5243 G5244 G5252 G5309 G5367 G5448 G5450 G5308 G5311 G5313'),
 ('4 boasting (C)', 'H1984H G2620 G2744 G2745 G2746 G4068 G5246 G6094'),
 ('5 mocking (D)', 'H1422 H2048A H3887 H3932 H4167 H5607A H7046 H8148 H8591 G1702 G2606 G3456'),
]
hits = list(csv.DictReader(open(os.path.join(HERE, 'm08-cluster-hits-v1-20261015.csv'), encoding='utf-8')))
bscan = {r['reference']: r['decision'] for r in csv.DictReader(open(os.path.join(HERE, 'm08-group-B-scan-triage-v1-20261015.csv'), encoding='utf-8'))}
xref = {r['reference']: r for r in csv.DictReader(open(os.path.join(HERE, 'm08-cluster-verses-crossref-v1-20261015.csv'), encoding='utf-8'))}
BWORDS = set('H1361 H1363 H1364 H4791 H5920H H5945A H6967 H7314 G5308 G5311 G5313'.split())

m09 = {}
for f in glob.glob(os.path.join(HERE, '..', 'M09 - humility-lowliness', 'm09-*register-v*.csv')):
    for r in csv.DictReader(open(f, encoding='utf-8')):
        if r.get('decision') in ('read', 'carried'): m09.setdefault(r['reference'], os.path.basename(f))

words = defaultdict(set)
for h in hits: words[h['reference']].add(h['strong'])
rows = []
for ref, ws in words.items():
    b = None
    for name, ss in BATCH:
        ss = set(ss.split())
        own = ws & ss
        if not own: continue
        # a height word only brings a verse in when the B scan judged it pride sense
        if own <= BWORDS and bscan.get(ref) != 'P pride sense': continue
        b = name; break
    if b is None: continue
    rows.append([b, ref, ' '.join(sorted(ws)), xref[ref]['narrative_places'], xref[ref]['other_mcodes'], m09.get(ref, '')])
rows.sort(key=lambda r: (r[0], r[1]))
with open(os.path.join(HERE, 'm08-reading-scope-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['batch', 'reference', 'm08_strongs', 'narrative_places', 'other_mcodes', 'm09_read_in'])
    w.writerows(rows)
c = Counter(r[0] for r in rows); m = Counter(r[0] for r in rows if r[5]); n = Counter(r[0] for r in rows if r[3])
for b, _ in BATCH: print(b, c[b], 'm09-read', m[b], 'cited', n[b])
print('total', len(rows))
