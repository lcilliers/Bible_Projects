"""Anger overview part F, from the lexical analysis itself (iba.db read-only).

For every live verse that holds an M02 hit, read every live verse_lexical token and the
cluster codes the lexical analysis gave that occurrence (verse_lexical.role, a JSON list).
Every code other than M02 is a co-existing cluster. Writes:
  anger-coexistence-lexical-v1-20261005.csv          one row per co-existing token
  anger-coexistence-lexical-summary-v1-20261005.csv  one row per cluster code
and prints a cross-check against the per-word tag table (cluster_strong) and against the
observation layer (ib_node) for the same verses.

"near" = within 3 positions of an M02 hit in the same verse (as the fear overview §F).
The M02 hits are found by role, not by Strong's, so the lexical analysis is the only source.

Usage (project root):  python "_analytics/Clusters/M02 - anger-wrath/anger-coexistence-lexical-v1-20261005.py"
"""
import csv, json, os, sqlite3
from collections import Counter, defaultdict

D = os.path.dirname(os.path.abspath(__file__))
db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
names = dict(db.execute("SELECT cluster_code, short_name FROM cluster"))
gloss = dict(db.execute("SELECT strongNumber, stepGloss FROM strong"))


def codes(role):
    try:
        return json.loads(role) if role else []
    except ValueError:
        return []


# 1. the M02 hits, by role
m02 = defaultdict(list)
for vid, pos, role in db.execute("SELECT verse_id, position, role FROM verse_lexical WHERE deleted=0 AND role LIKE '%M02%'"):
    if 'M02' in codes(role):
        m02[vid].append(pos)
live = {r[0]: r[1] for r in db.execute(
    f"SELECT id, reference FROM verse WHERE deleted=0 AND id IN ({','.join(map(str, m02))})")}
m02 = {v: p for v, p in m02.items() if v in live}
print(f'M02 hits by role: {sum(len(p) for p in m02.values())} in {len(m02)} verses')

# 2. every token in those verses
rows, shared, near, hits, surf, on_word = [], defaultdict(set), defaultdict(set), Counter(), defaultdict(Counter), Counter()
vids = sorted(m02)
for i in range(0, len(vids), 400):
    chunk = vids[i:i + 400]
    for vid, pos, st, s, role in db.execute(
            f"SELECT verse_id, position, strong, surface, role FROM verse_lexical WHERE deleted=0 "
            f"AND verse_id IN ({','.join(map(str, chunk))}) ORDER BY verse_id, position"):
        cs = [c for c in codes(role) if c != 'M02']
        if not cs:
            continue
        dist = min(abs(pos - h) for h in m02[vid])
        if dist == 0:  # the M02 token itself also carries a second code (e.g. T14 on 'aph'):
            for c in cs:  # counted apart, not as a co-existing word
                on_word[c] += 1
            rows.append([live[vid], pos, st, s, gloss.get(st, ''), '|'.join(cs), 0])
            continue
        for c in cs:
            shared[c].add(vid); hits[c] += 1
            surf[c][f'{(s or "").strip()} ({st})'] += 1
            if dist <= 3:
                near[c].add(vid)
        rows.append([live[vid], pos, st, s, gloss.get(st, ''), '|'.join(cs), dist])

with open(os.path.join(D, 'anger-coexistence-lexical-v1-20261005.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['reference', 'position', 'strong', 'surface', 'gloss', 'codes', 'distance_to_M02'])
    w.writerows(rows)

order = sorted(shared, key=lambda c: (c[0] != 'M', -len(shared[c])))
with open(os.path.join(D, 'anger-coexistence-lexical-summary-v1-20261005.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['code', 'name', 'verses_shared', 'verses_near', 'tokens', 'distinct_words', 'top_surfaces'])
    for c in order:
        w.writerow([c, names.get(c, ''), len(shared[c]), len(near[c]), hits[c], len(surf[c]),
                    '; '.join(f'{k} {n}' for k, n in surf[c].most_common(12))])

m = [c for c in order if c.startswith('M')]
print(f'co-existing codes: {len(order)} (M-clusters {len(m)}, '
      f'with 20+ shared verses {sum(len(shared[c]) >= 20 for c in m)}; other codes {[c for c in order if not c.startswith("M")]})')
for c in order:
    print(f'{c} {names.get(c, "")}: shared {len(shared[c])} / near {len(near[c])} / tokens {hits[c]} / words {len(surf[c])}')

# 3. cross-check with cluster_strong (the per-word tag table) for the same verses
tagmap = defaultdict(set)
for code, st in db.execute("SELECT cluster_code, strong FROM cluster_strong WHERE deleted=0"):
    tagmap[st].add(code)
cs_shared = defaultdict(set)
for i in range(0, len(vids), 400):
    chunk = vids[i:i + 400]
    for vid, st in db.execute(f"SELECT verse_id, strong FROM verse_lexical WHERE deleted=0 AND verse_id IN ({','.join(map(str, chunk))})"):
        for c in tagmap.get(st, ()):
            if c != 'M02':
                cs_shared[c].add(vid)
diff = {c: (len(shared.get(c, ())), len(cs_shared.get(c, ()))) for c in set(shared) | set(cs_shared)
        if c.startswith('M') and len(shared.get(c, ())) != len(cs_shared.get(c, ()))}
print('second codes on the M02 word itself (not counted above):', dict(on_word))
print('role vs cluster_strong, M-codes that differ (role, tag table):', diff or 'none')

# 4. the observation layer: other clusters' ib_node rows on these verses
refs = set(live.values())
obs = Counter()
for code, ref in db.execute("SELECT cluster_code, verse_reference FROM ib_node"):
    if ref in refs and code != 'M02':
        obs[code] += 1
print('ib_node rows by other clusters on the anger verses:', dict(obs.most_common()) or 'none')
