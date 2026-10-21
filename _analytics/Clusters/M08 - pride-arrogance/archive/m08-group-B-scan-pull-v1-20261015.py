"""M08 group B (height words): scan pull (#2156). Read-only against iba.db.

Researcher, 2026-10-15 (verbatim): "group B - lets do one more scan of these, it seems they are
mostly data.  Set them aside as data unless the terms are supporting other M-codes".
Writes one row per group B verse: the B words with surface, the other M-coded words in the verse
(code, Strong's, surface), narrative citations, and the ESV text. The decision columns are filled
in the triage CSV, not here.
"""
import csv, os, sqlite3
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
B = 'H1361 H1363 H1364 H4791 H5920H H5945A H6967 H7314 G5308 G5311 G5313'.split()
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)

q = ','.join('?' * len(B))
bhits = c.execute(f"""SELECT v.id, v.reference, v.text, vl.strong, vl.surface, vl.position FROM verse_lexical vl
  JOIN verse v ON v.id = vl.verse_id WHERE vl.deleted = 0 AND vl.strong IN ({q}) ORDER BY v.id, vl.position""", B).fetchall()
vids = sorted({r[0] for r in bhits})
ref = {r[0]: r[1] for r in bhits}; text = {r[0]: r[2] for r in bhits}
bw = defaultdict(list)
for r in bhits: bw[r[0]].append(f'{r[3]} "{(r[4] or "").strip()}"')

other = defaultdict(list)
vq = ','.join('?' * len(vids))
for vid, code, s, su in c.execute(f"""SELECT DISTINCT vl.verse_id, cs.cluster_code, vl.strong, vl.surface FROM verse_lexical vl
   JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0 AND cs.cluster_code LIKE 'M%'
   WHERE vl.deleted = 0 AND vl.verse_id IN ({vq}) AND vl.strong NOT IN ({q})""", vids + B):
    other[vid].append(f'{code} {s} "{(su or "").strip()}"')
cit = defaultdict(set)
for vid, ch in c.execute(f"""SELECT nc.verse_id, ch.chapter_no FROM narrative_citation nc JOIN narrative_chapter ch
   ON ch.id = nc.chapter_id AND ch.inactive = 0 WHERE nc.last_version IS NULL AND nc.verse_id IN ({vq})""", vids):
    cit[vid].add(ch)

out = os.path.join(HERE, 'm08-group-B-scan-v1-20261015.csv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['n', 'reference', 'b_words', 'other_mwords', 'narrative', 'text'])
    for i, v in enumerate(vids, 1):
        w.writerow([i, ref[v], ' ; '.join(bw[v]), ' ; '.join(sorted(other[v])), ' '.join(sorted(cit[v])), text[v]])
print(len(vids), 'verses ->', out)
