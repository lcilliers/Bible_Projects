"""Step 2 of the anger process (#1963): reconcile the five unit pulls and faces files
against the live M02 vocabulary in iba.db (read-only), hit by hit.

Checks:
  1. every live M02 Strong's (cluster_strong, not deleted) is in exactly one unit
  2. every live hit (verse_lexical, not deleted, verse not deleted) is in a unit pull, and no pull row is extra
  3. every pull row has a face, and every faces row matches a pull row
  4. the strong on each pull row matches the live strong
  5. verse coverage against the M02 phenomena ledger v5
Hits are compared as multisets of (reference, position, strong), because one span can hold
two codes for the same Strong's (1Sa 20:7, unit 3 data note).

Usage (from the project root):  python "_analytics/Clusters/M02 - anger-wrath/anger-reconciliation-v1-20261005.py"
"""
import csv, glob, os, sqlite3
from collections import Counter, defaultdict

D = os.path.dirname(os.path.abspath(__file__))
db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)

live = [r[0] for r in db.execute(
    "SELECT strong FROM cluster_strong WHERE cluster_code='M02' AND deleted=0 ORDER BY strong")]
print(f'live M02 Strong\'s: {len(live)} ({len(set(live))} distinct); '
      f'Hebrew/Aramaic {sum(s[0] == "H" for s in live)}, Greek {sum(s[0] == "G" for s in live)}')

live_hits = Counter()
per_strong = Counter()
for s in live:  # one Strong's at a time, so the strong index is used
    for ref, pos in db.execute(
            "SELECT v.reference, vl.position FROM verse_lexical vl JOIN verse v ON v.id = vl.verse_id "
            "WHERE vl.strong = ? AND vl.deleted = 0 AND v.deleted = 0", (s,)):
        live_hits[(ref, str(pos), s)] += 1
        per_strong[s] += 1
live_verses = {k[0] for k in live_hits}
print(f'live hits: {sum(live_hits.values())} in {len(live_verses)} verses')

pull_hits = Counter(); unit_of = defaultdict(set); no_face = []; unit_rows = Counter()
face_keys = Counter(); pull_keys = Counter()
for u in range(1, 6):
    pull = [f for f in glob.glob(os.path.join(D, f'anger-unit{u}-*pull*.csv'))][0]
    faces = glob.glob(os.path.join(D, f'anger-unit{u}-faces-*.csv'))[0]
    for r in csv.DictReader(open(pull, encoding='utf-8')):
        pull_hits[(r['reference'], r['position'], r['strong'])] += 1
        pull_keys[(r['reference'], r['position'])] += 1
        unit_of[r['strong']].add(u); unit_rows[u] += 1
        if not r['face'].strip():
            no_face.append((u, r['reference'], r['position']))
    for r in csv.DictReader(open(faces, encoding='utf-8')):
        if not r['face'].strip():
            no_face.append((u, r['reference'], r['position'], 'faces file'))
        face_keys[(r['reference'], r['position'])] += 1
print('pull rows by unit:', dict(unit_rows), '= total', sum(unit_rows.values()))

missing = live_hits - pull_hits
extra = pull_hits - live_hits
print('1. Strong\'s in more than one unit:', {s: sorted(u) for s, u in unit_of.items() if len(u) > 1} or 'none')
print('   live Strong\'s in no unit:', [s for s in live if s not in unit_of] or 'none')
print('   unit Strong\'s not live in M02:', [s for s in unit_of if s not in live] or 'none')
print('   live Strong\'s with no hits:', [s for s in live if not per_strong[s]] or 'none')
print('2. live hits missing from the pulls:', sum(missing.values()), list(missing)[:10])
print('   pull rows not live:', sum(extra.values()), list(extra)[:10])
print('3. rows without a face:', len(no_face), no_face[:10])
fk_missing = pull_keys - face_keys
fk_extra = {k for k in face_keys if k not in pull_keys}
print('   pull (reference, position) keys with no faces row:', sum(fk_missing.values()), list(fk_missing)[:10])
print('   faces rows matching no pull row:', len(fk_extra), list(fk_extra)[:10])
print('   (faces files are keyed by reference + position; 1Sa 20:7 carries two hits at one position)')
print('4. strong mismatches: covered by check 2 (the multiset includes the strong)')

v5 = {r['reference'] for r in csv.DictReader(
    open(os.path.join(D, 'wa-cluster-M02-phenomena-ledger-v5-20260929.csv'), encoding='utf-8'))}
print(f'5. ledger v5 verses {len(v5)}; live verses not in v5 {len(live_verses - v5)}; '
      f'v5 verses not live {len(v5 - live_verses)}')
print('per Strong\'s (hits):', ', '.join(f'{s} {per_strong[s]}' for s in live))
