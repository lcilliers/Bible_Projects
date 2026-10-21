"""Pull every verse for a list of Strong's numbers, one row per hit (read-only on iba.db).

Usage: python life-death-strong-verse-pull-v1-20261013.py OUT.csv H4191 H4194 ...
Columns: reference, position, strong, gloss, surface, negated, other_m_words
(strong:surface:M-code; ... for the other M-coded words in the verse), text.
Ordered by canonical book order, chapter, verse, position.
"""
import csv, sqlite3, sys
from collections import defaultdict

out, strongs = sys.argv[1], sys.argv[2:]
db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
q = ','.join('?' * len(strongs))
order = {b: o for b, o in db.execute("SELECT book, ordinal FROM cfg_book_order")}

rows = db.execute(f"""SELECT v.id, v.osisId, v.reference, vl.position, vl.strong, s.stepGloss,
                             vl.surface, vl.is_negator, v.text
                      FROM verse_lexical vl
                      JOIN verse v ON v.id = vl.verse_id AND v.deleted = 0
                      LEFT JOIN strong s ON s.strongNumber = vl.strong
                      WHERE vl.deleted = 0 AND vl.strong IN ({q})""", strongs).fetchall()
vids = {r[0] for r in rows}

others = defaultdict(list)
if vids:
    vq = ','.join('?' * len(vids))
    for vid, pos, st, surf, code in db.execute(f"""SELECT vl.verse_id, vl.position, vl.strong, vl.surface,
                   cs.cluster_code
            FROM verse_lexical vl
            JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0 AND cs.cluster_code LIKE 'M%'
            JOIN cluster c ON c.cluster_code = cs.cluster_code AND c.deleted = 0
            WHERE vl.deleted = 0 AND vl.verse_id IN ({vq}) AND vl.strong NOT IN ({q})
            ORDER BY vl.verse_id, vl.position""", [*vids, *strongs]):
        others[vid].append(f'{st}:{surf}:{code}')

def key(r):
    b, ch, vs = r[1].split('.')
    return (order.get(b, 999), int(ch), int(vs), r[3] or 0)

rows.sort(key=key)
with open(out, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'position', 'strong', 'gloss', 'surface', 'negated', 'other_m_words', 'text'])
    for vid, osis, ref, pos, st, gl, surf, neg, text in rows:
        w.writerow([ref, pos, st, gl, surf, neg, '; '.join(others[vid]), text or ''])

per = defaultdict(lambda: [0, set()])
for r in rows:
    per[r[4]][0] += 1; per[r[4]][1].add(r[0])
for s in strongs:
    print(f'{s}: {per[s][0]} hits, {len(per[s][1])} verses')
print(f'total: {len(rows)} hits in {len(vids)} verses; {sum(1 for r in rows if not r[8])} hits without text')
