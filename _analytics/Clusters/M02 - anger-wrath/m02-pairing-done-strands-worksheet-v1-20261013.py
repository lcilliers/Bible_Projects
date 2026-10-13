"""OT-16/29/30/51/62 (M02 pairings with strands already read: M72, M25, M01, M20, M64).
Builds the verse list for the check, 2026-10-13. Read-only.
Output: m02-pairing-done-strands-verses-v1-20261013.csv (reference, mcode, faces, surfaces)
Then run ../M64 - will-resolve/verse-narrative-ot-crossref-v3-20261009.py on it for narrative placements.
"""
import csv, os, sqlite3
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
MCODES = ['M01', 'M25', 'M64', 'M20']  # M72: OT-16's M72 item already closed by #1998
rows = defaultdict(lambda: {'faces': [], 'surfaces': []})
for r in csv.DictReader(open(os.path.join(HERE, 'wa-cluster-M02-mcode-face-combinations-v1-20261005.csv'), encoding='utf-8-sig')):
    if r['mcode'] not in MCODES:
        continue
    for ref in [s.strip() for s in r['verse_list'].split(';') if s.strip()]:
        k = (r['mcode'], ref)
        rows[k]['faces'].append(f"{r['face']} {r['face_name']}")
        rows[k]['surfaces'].append(r['surfaces'])
db = sqlite3.connect('file:' + os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db') + '?mode=ro', uri=True)
cols = [c[1] for c in db.execute('pragma table_info(verse)')]
tcol = next(c for c in ('text', 'verse_text', 'esv_text') if c in cols)
out = os.path.join(HERE, 'm02-pairing-done-strands-verses-v1-20261013.csv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'mcode', 'faces', 'pair_surfaces', 'text'])
    for (m, ref), d in sorted(rows.items()):
        t = db.execute(f'select {tcol} from verse where reference=?', (ref,)).fetchone() if 'reference' in cols else None
        w.writerow([ref, m, ' / '.join(d['faces']), ' / '.join(d['surfaces']), t[0] if t else ''])
print(len(rows), cols)
