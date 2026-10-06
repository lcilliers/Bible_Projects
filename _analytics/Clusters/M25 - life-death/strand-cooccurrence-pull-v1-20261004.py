"""Co-occurrence pull for a strand question: one row per hit of a TARGET word in a verse that also
holds at least one PARTNER word. Strong's are given as base codes and matched by prefix, so H5315
covers H5315G..H5315N. iba.db opened read-only.

Columns: reference, position, strong, surface, partners (strong:surface; ...), text, face, face_name.
Face columns are left empty, to be filled by reading (merge with strand-unit-pull --faces, same keys).

Usage (from the repo root):
  python strand-cooccurrence-pull-v1-20261004.py OUT.csv --target H5315 G5590 --partner H4191 H4194 ...
"""
import csv, sqlite3, sys
from collections import defaultdict

args = sys.argv[1:]
out = args[0]
ti, pi = args.index('--target'), args.index('--partner')
target = args[ti + 1:pi] if ti < pi else args[ti + 1:]
partner = args[pi + 1:] if pi > ti else args[pi + 1:ti]

db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
def like(codes):
    return ' OR '.join('vl.strong LIKE ?' for _ in codes), [c + '%' for c in codes]

tw, tp = like(target)
pw, pp = like(partner)
pv = defaultdict(list)
for vid, st, surf in db.execute(f"SELECT vl.verse_id, vl.strong, vl.surface FROM verse_lexical vl "
                                f"WHERE vl.deleted=0 AND ({pw})", pp):
    pv[vid].append(f'{st}:{surf}')
rows = db.execute(f"""SELECT v.id, v.reference, vl.position, vl.strong, vl.surface, v.text
    FROM verse_lexical vl JOIN verse v ON v.id = vl.verse_id
    WHERE vl.deleted=0 AND v.deleted=0 AND ({tw}) ORDER BY v.id, vl.position""", tp).fetchall()
rows = [r for r in rows if r[0] in pv]
with open(out, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'position', 'strong', 'surface', 'partners', 'text', 'face', 'face_name'])
    for vid, ref, pos, st, surf, text in rows:
        w.writerow([ref, pos, st, surf, '; '.join(pv[vid]), text or '', '', ''])
print(f'{len(rows)} hits in {len({r[0] for r in rows})} verses; {sum(1 for r in rows if not r[5])} without text')
