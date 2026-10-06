"""Unit pull for a strand: one row per hit of the given Strong's numbers, with the full ESV text.

Same row pattern as the fear and life-death unit pulls (reference, position, strong, surface,
negated, divine_near, text, face, face_name). Face columns are left empty, to be filled by
reading (merge with --faces).
  negated     = a verse_lexical.is_negator word within 2 positions before the hit (approximate)
  divine_near = a T7 Party-Divine Strong's within 5 positions of the hit (approximate)
iba.db opened read-only.

Usage:
  python strand-unit-pull-v1-20261002.py OUT.csv H4191 H4194 ...
  python strand-unit-pull-v1-20261002.py OUT.csv --faces FACES.csv   (merge faces into OUT.csv)
FACES.csv columns: reference,position,face,face_name
"""
import csv, sqlite3, sys
from collections import defaultdict

out = sys.argv[1]
if len(sys.argv) > 2 and sys.argv[2] == '--faces':
    faces = {}
    with open(sys.argv[3], encoding='utf-8') as f:
        for r in csv.DictReader(f):
            faces[(r['reference'], r['position'])] = (r['face'], r['face_name'])
    with open(out, encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    missing = 0
    for r in rows:
        k = (r['reference'], r['position'])
        if k in faces:
            r['face'], r['face_name'] = faces[k]
        if not r['face']:
            missing += 1
    with open(out, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f'{len(rows)} rows; {missing} without a face')
    sys.exit(0)

strongs = sys.argv[2:]
db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
t7 = {r[0] for r in db.execute("SELECT strong FROM cluster_strong WHERE cluster_code='T7' AND deleted=0")}
q = ','.join('?' * len(strongs))
hits = db.execute(f"""SELECT v.id, v.reference, vl.position, vl.strong, vl.surface, v.text
    FROM verse_lexical vl JOIN verse v ON v.id = vl.verse_id
    WHERE vl.deleted = 0 AND v.deleted = 0 AND vl.strong IN ({q})
    ORDER BY v.id, vl.position""", strongs).fetchall()
vids = sorted({h[0] for h in hits})
ctx = defaultdict(list)
for i in range(0, len(vids), 500):
    chunk = vids[i:i + 500]
    for vid, pos, st, neg in db.execute(
            f"SELECT verse_id, position, strong, is_negator FROM verse_lexical WHERE deleted=0 "
            f"AND verse_id IN ({','.join(map(str, chunk))})"):
        ctx[vid].append((pos, st, neg))
with open(out, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'position', 'strong', 'surface', 'negated', 'divine_near', 'text', 'face', 'face_name'])
    for vid, ref, pos, st, surf, text in hits:
        neg = int(any(o[2] and 0 < pos - o[0] <= 2 for o in ctx[vid]))
        div = int(any(o[1] in t7 and abs(o[0] - pos) <= 5 for o in ctx[vid]))
        w.writerow([ref, pos, st, surf, neg, div, text or '', '', ''])
print(f'{len(hits)} hits in {len(vids)} verses; {sum(1 for h in hits if not h[5])} without text')
