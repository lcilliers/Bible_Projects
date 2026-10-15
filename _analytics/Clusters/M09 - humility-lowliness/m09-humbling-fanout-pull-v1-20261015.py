"""M09 fan-out: humbling oneself (#2148). Read-only against iba.db.

Researcher, 2026-10-15, on Claude's recommendation (overview v3, chat): "proceed as suggested" --
fan out the humbling-oneself thread across clusters now; the poor/needy work becomes threads.

Word set (overview v3 s3A, s3C, s3D/3E.1, s5), taken in three tiers:
  WHOLE   every verse of the Strong's (the word itself names humbling, lowliness, meekness,
          contrition or submission)
  SURFACE only verses where the surface names it (surface lens, feedback_surface_is_the_sensitivity_lens):
          broad words whose humbling sense is one face among many
  JOINED  only verses where a broken/crushed surface sits in the same verse as heart, spirit or soul
Writes the verse list with the words, tier, other M-codes, narrative places and text; prints the counts.
"""
import csv, os, re, sqlite3
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
TAG = 'v1-20261015'
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)

WHOLE = {
    # M09 group A, C, D, E
    'H3665': 'M09', 'H8217': 'M09', 'H8214': 'M09', 'H8215': 'M09', 'H6800A': 'M09', 'H6800B': 'M09',
    'H7807': 'M09', 'G5011': 'M09', 'G5012': 'M09', 'G5013': 'M09', 'G5014': 'M09', 'G0036': 'M09',
    'H1793A': 'M09', 'G5292': 'M09', 'H6035': 'M09',
    # outside M09
    'H6038': 'M05', 'H6037': 'M05', 'G4239': 'M05', 'G4235': 'M05', 'G4236': 'M05', 'G4240': 'M05',
    'H8213': 'M53', 'H5223': 'M73', 'G5293': 'M23', 'G0506': 'M75', 'G5226': 'T3',
}
SURFACE = {  # strong: (cluster, surface regex)
    'H6041': ('M24', r'humbl|lowl|meek'),
    'H6031B': ('M24', r'humbl|lowl|submit'),
    'H7817': ('T3', r'humbl'),
    'H1794': ('M10', r'contrit'),
    'H1792': ('M10', r'contrit'),
    'G5391': ('M05', r'humbl'),
}
BROKEN = r'contrit|broken|crush|stricken'
INNER = ('H3820', 'H3824', 'H7307G', 'G2588', 'G4151', 'H5315G', 'H5315H')

def rows_for(strong):
    return c.execute("""SELECT vl.verse_id, vl.strong, vl.surface FROM verse_lexical vl
                        WHERE vl.deleted = 0 AND vl.strong = ?""", (strong,)).fetchall()

hit = defaultdict(list)   # verse_id -> [(strong, cluster, surface, tier)]
for s, cl in WHOLE.items():
    for v, st, sf in rows_for(s):
        hit[v].append((st, cl, (sf or '').strip(), 'whole'))
for s, (cl, pat) in SURFACE.items():
    for v, st, sf in rows_for(s):
        if sf and re.search(pat, sf, re.I):
            hit[v].append((st, cl, sf.strip(), 'surface'))
# joined: broken/crushed surface + heart/spirit/soul in the same verse (any Strong's, excluding particles)
inner_v = {r[0] for r in c.execute(
    "SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted = 0 AND (" +
    ' OR '.join("strong LIKE ?" for _ in INNER) + ")", [i + '%' for i in INNER])}
for v, st, sf in c.execute("SELECT verse_id, strong, surface FROM verse_lexical WHERE deleted = 0"):
    if v in inner_v and sf and re.search(BROKEN, sf, re.I) and not re.match(r'[HG]9\d\d\d$|H0853|H1931|H3588A|H3966|H5704', st):
        cl = ' '.join(r[0] for r in c.execute("SELECT cluster_code FROM cluster_strong WHERE strong=? AND deleted=0", (st,)))
        if st not in WHOLE and st not in SURFACE and not any(st.startswith(i) for i in INNER):
            hit[v].append((st, cl, sf.strip(), 'joined'))

# drop JOINED hits where the broken thing is not the heart/spirit (checked by reading the 28 candidates
# listed in overview v3 s3D/3E.1: kingdoms, horns, bows, snares, a city wall, plans, winds)
JOINED_OUT = {'Dan 11:4', 'Dan 8:25', 'Dan 8:8', 'Eze 44:7', 'Isa 19:10', 'Psa 124:7', 'Psa 37:15',
              'Pro 25:28', 'Job 17:11', 'Psa 31:12', 'Psa 143:3', 'Isa 53:10'}
ref = {}; text = {}
for v in list(hit):
    r, t = c.execute("SELECT reference, text FROM verse WHERE id=?", (v,)).fetchone()
    ref[v], text[v] = r, t or ''
    if r in JOINED_OUT:
        hit[v] = [h for h in hit[v] if h[3] != 'joined']
    if not hit[v]:
        del hit[v]

mc = defaultdict(set)
ids = ','.join(map(str, hit))
for v, code in c.execute(f"""SELECT DISTINCT vl.verse_id, cs.cluster_code FROM verse_lexical vl
    JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0
    WHERE vl.deleted = 0 AND cs.cluster_code LIKE 'M%' AND vl.verse_id IN ({ids})"""):
    mc[v].add(code)
cited = defaultdict(set)
for v, chno in c.execute(f"""SELECT nc.verse_id, ch.chapter_no FROM narrative_citation nc
    JOIN narrative_chapter ch ON ch.id = nc.chapter_id AND ch.inactive = 0
    WHERE nc.last_version IS NULL AND nc.verse_id IN ({ids})"""):
    cited[v].add(chno)

out = os.path.join(HERE, f'm09-humbling-fanout-verses-{TAG}.csv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'words', 'tiers', 'in_m09', 'other_mcodes', 'narrative_chapters', 'text'])
    for v in sorted(hit):
        hs = hit[v]
        w.writerow([ref[v], ' ; '.join(f'{s} [{cl}] "{sf}"' for s, cl, sf, _ in hs),
                    ' '.join(sorted({h[3] for h in hs})), int(any(h[1] == 'M09' for h in hs)),
                    ' '.join(sorted(mc[v])), ' '.join(sorted(cited[v])), text[v]])

per = Counter(); perv = defaultdict(set)
for v, hs in hit.items():
    for s, cl, sf, tier in hs:
        per[(s, cl, tier)] += 1; perv[(s, cl, tier)].add(v)
print('verses', len(hit), '| with an M09 word', sum(1 for hs in hit.values() if any(h[1] == 'M09' for h in hs)),
      '| outside M09 only', sum(1 for hs in hit.values() if not any(h[1] == 'M09' for h in hs)))
print('cited', sum(1 for v in hit if cited[v]))
for k in sorted(perv, key=lambda k: (k[1] != 'M09', -len(perv[k]))):
    print(k, len(perv[k]))
