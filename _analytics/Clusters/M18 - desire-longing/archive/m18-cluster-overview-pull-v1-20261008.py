"""M18 Desire & Longing: cluster overview pull (strand start). Read-only against iba.db.

Same shape as the M64 quick summary (#1978, query v2): live cluster_strong rows only
(cs.deleted = 0), hits from verse_lexical (deleted = 0), the "other" side is every OTHER
M-cluster. Writes three CSVs next to this script and prints the figures used in the overview .md.
"""
import csv, os, sqlite3
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
CODE = 'M18'
TAG = 'v1-20261008'

c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)
c.row_factory = sqlite3.Row

strongs = c.execute("""
  SELECT cs.strong, cs.source, cs.confidence, cs.rationale, s.stepGloss, s.stepTransliteration, s.language
  FROM cluster_strong cs LEFT JOIN strong s ON s.strongNumber = cs.strong
  WHERE cs.cluster_code = ? AND cs.deleted = 0 ORDER BY cs.strong""", (CODE,)).fetchall()
deleted_rows = c.execute("SELECT strong FROM cluster_strong WHERE cluster_code=? AND deleted=1", (CODE,)).fetchall()

hits = c.execute("""
  SELECT DISTINCT v.id AS verse_id, v.reference, vl.position, vl.strong, vl.surface
  FROM verse_lexical vl
  JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.cluster_code = ? AND cs.deleted = 0
  JOIN verse v ON v.id = vl.verse_id
  WHERE vl.deleted = 0 ORDER BY v.id, vl.position""", (CODE,)).fetchall()

other = c.execute("""
  SELECT DISTINCT vl.verse_id, vl.position, vl.strong, vl.surface, cs.cluster_code, cl.short_name
  FROM verse_lexical vl
  JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0
  JOIN cluster cl ON cl.cluster_code = cs.cluster_code AND cl.deleted = 0
  WHERE vl.deleted = 0 AND cs.cluster_code LIKE 'M%' AND cs.cluster_code <> ?
    AND vl.verse_id IN (SELECT vl2.verse_id FROM verse_lexical vl2
                        JOIN cluster_strong cs2 ON cs2.strong = vl2.strong AND cs2.cluster_code = ?
                         AND cs2.deleted = 0 WHERE vl2.deleted = 0)""", (CODE, CODE)).fetchall()

gloss = {r['strong']: r['stepGloss'] for r in strongs}
info = {r['strong']: r for r in strongs}

# 1. hits CSV
with open(os.path.join(HERE, f'm18-cluster-hits-{TAG}.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'strong', 'gloss', 'surface', 'position'])
    for h in hits: w.writerow([h['reference'], h['strong'], gloss.get(h['strong']), h['surface'], h['position']])

# 2. per-Strong's summary
by_strong = defaultdict(list)
for h in hits: by_strong[h['strong']].append(h)
with open(os.path.join(HERE, f'm18-cluster-strongs-{TAG}.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['strong', 'translit', 'gloss', 'language', 'hits', 'verses', 'surface_top', 'tag_source', 'tag_confidence', 'tag_rationale'])
    rows = []
    for s in strongs:
        hs = by_strong.get(s['strong'], [])
        surf = Counter((h['surface'] or '').strip() for h in hs).most_common(6)
        rows.append([s['strong'], s['stepTransliteration'], s['stepGloss'], s['language'], len(hs),
                     len({h['verse_id'] for h in hs}), '; '.join(f'{a} ({b})' for a, b in surf),
                     s['source'], s['confidence'], s['rationale']])
    rows.sort(key=lambda r: (-r[4], r[0]))
    w.writerows(rows)

# 3. co-occurrence with other M-codes, per verse
verse_ref = {h['verse_id']: h['reference'] for h in hits}
co = defaultdict(set); co_name = {}
for o in other:
    co[o['cluster_code']].add(o['verse_id']); co_name[o['cluster_code']] = o['short_name']
with open(os.path.join(HERE, f'm18-cluster-mcode-cooccurrence-{TAG}.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'other_cluster_code', 'other_cluster_name', 'other_strong', 'other_gloss', 'other_surface', 'other_position'])
    og = {r['strongNumber']: r['stepGloss'] for r in c.execute('SELECT strongNumber, stepGloss FROM strong')}
    for o in sorted(other, key=lambda o: (o['verse_id'], o['position'])):
        w.writerow([verse_ref[o['verse_id']], o['cluster_code'], o['short_name'], o['strong'], og.get(o['strong']), o['surface'], o['position']])

# ---- figures for the .md
verses = {h['verse_id'] for h in hits}
book = lambda ref: ref.rsplit(' ', 1)[0]
books = Counter(book(verse_ref[v]) for v in verses)
per_verse = Counter(h['verse_id'] for h in hits)
multi = [v for v, n in per_verse.items() if n > 1]
test = Counter()
for h in c.execute("""SELECT DISTINCT vl.verse_id, vl.testament FROM verse_lexical vl
  JOIN cluster_strong cs ON cs.strong=vl.strong AND cs.cluster_code=? AND cs.deleted=0 WHERE vl.deleted=0""", (CODE,)):
    test[h['testament']] += 1
print('live strongs', len(strongs), 'deleted rows', [r[0] for r in deleted_rows])
print('with no hits', [s['strong'] for s in strongs if s['strong'] not in by_strong])
print('hits', len(hits), 'verses', len(verses), 'books', len(books), 'testament', dict(test))
print('verses >1 hit', len(multi))
print('top books', books.most_common(14))
print('lang', Counter(s['language'] for s in strongs))
print('sources', Counter(s['source'] for s in strongs))
print('verses with any other M', len({o['verse_id'] for o in other}))
print('cooc top', sorted(((k, co_name[k], len(v)) for k, v in co.items()), key=lambda x: -x[2])[:25])
print('m47 shared', len(co.get('M47', ())), 'm64 shared', len(co.get('M64', ())), 'm02', len(co.get('M02', ())))
pairs = Counter()
for v in multi:
    ss = sorted(h['strong'] for h in hits if h['verse_id'] == v)
    for i in range(len(ss)):
        for j in range(i + 1, len(ss)): pairs[(ss[i], ss[j])] += 1
print('within pairs', sum(pairs.values()), pairs.most_common(15))
for r in rows: print(r[:7], r[7])
