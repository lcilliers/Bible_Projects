"""M18 verses shared with M47 (Inner Seat), M25 (Life & Death) and M02 (Anger & Wrath) (#1993).

Researcher, 2026-10-09: "M18 verse bind with M47, M25 and M92. All these verses should already be in the
narrative. However their interpretation and meaning may be incomplete or too narrow and need review. so
pull all these verses into a csv". M92 does not exist in `cluster`; M02 is taken as meant (analysed
strand, 59 shared verses, OT-19) and M72 is carried as a flag column only. Read-only against iba.db.

One row per verse. The `text` column is last so verse-narrative-ot-crossref-v2 can append before it.
"""
import csv, os, sqlite3
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
OUT = os.path.join(HERE, 'm18-shared-m47-m25-m02-verses-v1-20261009.csv')
FILTER = os.path.join(HERE, 'm18-delight-pleasure-filter-v1-20261008.csv')
PARTNERS = ['M47', 'M25', 'M02']
FLAG_ONLY = ['M72']

c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
gloss = {r[0]: r[1] for r in c.execute('SELECT strongNumber, stepGloss FROM strong')}


def hits(code):
    out = defaultdict(list)
    for r in c.execute("""SELECT DISTINCT vl.verse_id, vl.position, vl.strong, vl.surface FROM verse_lexical vl
        JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.cluster_code = ? AND cs.deleted = 0
        WHERE vl.deleted = 0 ORDER BY vl.verse_id, vl.position""", (code,)):
        out[r['verse_id']].append(f"{r['strong']} {gloss.get(r['strong'], '')} \"{r['surface']}\"")
    return out


m18 = hits('M18')
part = {code: hits(code) for code in PARTNERS + FLAG_ONLY}
buckets = defaultdict(set)
for r in csv.DictReader(open(FILTER, encoding='utf-8')):
    buckets[r['reference']].add(r['filter_bucket'])

vids = sorted(v for v in m18 if any(v in part[code] for code in PARTNERS))
rows = []
for vid in vids:
    ref, text = c.execute('SELECT reference, text FROM verse WHERE id = ?', (vid,)).fetchone()
    row = {'reference': ref,
           'shared_with': ' '.join(code for code in PARTNERS if vid in part[code]),
           'm18_words': ' ; '.join(m18[vid])}
    for code in PARTNERS:
        row[f'{code.lower()}_words'] = ' ; '.join(part[code].get(vid, []))
    row['m72_flag'] = int(vid in part['M72'])
    row['delight_filter_bucket'] = ' ; '.join(sorted(buckets.get(ref, ())))
    row['text'] = text
    rows.append(row)

with open(OUT, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
from collections import Counter
print(len(rows), 'verses ->', OUT)
print(Counter(r['shared_with'] for r in rows).most_common())
print('m72 flag', sum(r['m72_flag'] for r in rows))
