"""Anger overview part F input: in the 681 M02 verses, which other M-clusters' tagged words
share the verse, and how many stand within 3 positions of an M02 hit (iba.db read-only).
Same measure as the fear overview §F ("verses shared / near (<=3 words)"). Tag co-occurrence
only: it points to verses to read, it is not a relation (#1919).

Usage (project root):  python "_analytics/Clusters/M02 - anger-wrath/anger-cooccurrence-v1-20261005.py" [--top N] [--examples CODE]
"""
import sqlite3, sys
from collections import defaultdict

db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
tags = defaultdict(set)
for code, s in db.execute("SELECT cluster_code, strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%'"):
    tags[s].add(code)
names = dict(db.execute("SELECT cluster_code, short_name FROM cluster"))
m02 = {s for s, c in tags.items() if 'M02' in c}
q = ','.join('?' * len(m02))
vids = sorted({r[0] for r in db.execute(
    f"SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND strong IN ({q})", sorted(m02))})
shared, near, ex = defaultdict(set), defaultdict(set), defaultdict(list)
refs = dict(db.execute(f"SELECT id, reference FROM verse WHERE id IN ({','.join(map(str, vids))})"))
for i in range(0, len(vids), 400):
    chunk = vids[i:i + 400]
    rows = defaultdict(list)
    for vid, pos, st, surf in db.execute(
            f"SELECT verse_id, position, strong, surface FROM verse_lexical WHERE deleted=0 "
            f"AND verse_id IN ({','.join(map(str, chunk))})"):
        rows[vid].append((pos, st, surf))
    for vid, toks in rows.items():
        hits = [p for p, s, _ in toks if s in m02]
        for p, s, surf in toks:
            for c in tags.get(s, ()):
                if c == 'M02':
                    continue
                shared[c].add(vid)
                if any(abs(p - h) <= 3 for h in hits):
                    near[c].add(vid)
                    if len(ex[c]) < 12:
                        ex[c].append(f'{refs[vid]} "{surf}" ({s})')
top = int(sys.argv[sys.argv.index('--top') + 1]) if '--top' in sys.argv else 40
order = sorted(shared, key=lambda c: -len(shared[c]))
print(f'M02 verses: {len(vids)}; clusters sharing a verse: {len(shared)}; '
      f'with 20+ shared verses: {sum(len(v) >= 20 for v in shared.values())}')
for c in order[:top]:
    print(f'{c} {names.get(c, "")}: shared {len(shared[c])} / near {len(near[c])}')
if '--examples' in sys.argv:
    for c in sys.argv[sys.argv.index('--examples') + 1].split(','):
        print(c, '; '.join(ex[c]))
