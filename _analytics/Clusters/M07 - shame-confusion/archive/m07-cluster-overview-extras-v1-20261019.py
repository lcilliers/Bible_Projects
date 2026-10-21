"""M07 Shame & Confusion: overview extras (#2171). Read-only against iba.db.

Adds to m07-cluster-overview-pull-v1-20261019.py (adapted from m08-cluster-overview-extras-v1-20261015.py):
gloss groups (a reading aid only), surface splits within one Strong's, the scan for same-sense words
tagged outside M07 (OT-02 lesson), the narrative sections, passages and claims on shame, and the verse
lists the overview names. Prints only; the CSVs come from the pull script.
"""
import csv, os, re, sqlite3, sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)
TAG = 'v1-20261019'

# Gloss groups: a reading aid by gloss and surface, not a finding or a sub-grouping.
GROUPS = {
 'A be ashamed, put to shame, confounded': 'H0954 H3637 H2659 G0153 G1870 G2617 G1788',
 'B shame, disgrace (nouns)': 'H1322 H3639 H3640 H0955 H1317 H8218 G0152 G0150 G1791',
 'C reproach, taunt': 'H2781 H2617B H2616B G3680 G3681 G0176',
 'D dishonor, contempt': 'H7036 H7034 H7022 H6173 G0818 G0819 G0820 G1165 G3856',
 'E curse': 'H7045 H3994 H8381 G2671 G0685 G2652',
 'F gloss away from the cluster': 'G0577',
}
grp = {s: g for g, ss in GROUPS.items() for s in ss.split()}

hits = list(csv.DictReader(open(os.path.join(HERE, f'm07-cluster-hits-{TAG}.csv'), encoding='utf-8')))
xref = list(csv.DictReader(open(os.path.join(HERE, f'm07-cluster-verses-crossref-{TAG}.csv'), encoding='utf-8')))
live = {h['strong'] for h in hits}
print('ungrouped', sorted(live - set(grp)), 'grouped-not-live', sorted(set(grp) - live))

xr = {r['reference']: r for r in xref}
vg = defaultdict(set)
for h in hits: vg[h['reference']].add(grp[h['strong']][0])
print('\n# groups: strongs hits verses cited in-register no-other-M')
for g, ss in GROUPS.items():
    ss = ss.split(); hs = [h for h in hits if h['strong'] in ss]; vs = {h['reference'] for h in hs}
    print(g, len(ss), len(hs), len(vs), sum(int(xr[v]['narrative_n']) > 0 for v in vs),
          sum(xr[v]['in_claims_register'] == '1' for v in vs), sum(not xr[v]['other_mcodes'] for v in vs))
print('combos', Counter(''.join(sorted(v)) for v in vg.values()).most_common(12))

# Surface splits within one Strong's (pointers for the change-of-character reading, #1919)
print('\n# surface splits')
for s in ('H0954', 'H3637', 'H2659', 'G1788', 'H2781', 'H3639', 'H7036', 'H7034', 'H7045', 'H2617B', 'G0176', 'G0577', 'H8218', 'H6173', 'G1165'):
    hs = [h for h in hits if h['strong'] == s]
    print(s, Counter((h['surface'] or '').strip().lower() for h in hs).most_common(12))
    if len(hs) <= 12: print('   ', [(h['reference'], h['surface']) for h in hs])
print('\n# H0954 by stem (morph) and surface')
for r in c.execute("""SELECT vl.morph_code, lower(trim(vl.surface)), count(*) FROM verse_lexical vl
   WHERE vl.strong='H0954' AND vl.deleted=0 GROUP BY 1,2 ORDER BY 3 DESC LIMIT 25"""): print(r)
for s in ('G1788',):
    print(s, [(h['reference'], h['surface']) for h in hits if h['strong'] == s])

# Same-sense words outside M07 (gloss or surface)
print('\n# outside M07: gloss/surface scan')
pat = r'asham|shame|disgrac|reproach|dishonou?r|humiliat|confound|confusion|blush|contempt|despis|curse|insult|taunt|scorn|abase|disappoint|naked|accurs'
rx = re.compile(pat, re.I)
m07 = {r[0] for r in c.execute("SELECT strong FROM cluster_strong WHERE cluster_code='M07' AND deleted=0")}
tag = defaultdict(set)
for s, cc in c.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0"): tag[s].add(cc)
gl = {s: g for s, g in c.execute("SELECT strongNumber, stepGloss FROM strong")}
tr = {s: t for s, t in c.execute("SELECT strongNumber, stepTransliteration FROM strong")}
m07v = {r[0] for r in c.execute("""SELECT DISTINCT vl.verse_id FROM verse_lexical vl JOIN cluster_strong cs
   ON cs.strong=vl.strong AND cs.cluster_code='M07' AND cs.deleted=0 WHERE vl.deleted=0""")}
cited = {r[0] for r in c.execute("""SELECT nc.verse_id FROM narrative_citation nc JOIN narrative_chapter ch
   ON ch.id=nc.chapter_id AND ch.inactive=0 WHERE nc.last_version IS NULL""")}
surf = defaultdict(Counter); vv = defaultdict(set)
for vid, s, su in c.execute("SELECT verse_id, strong, surface FROM verse_lexical WHERE deleted=0"):
    if s in m07: continue
    vv[s].add(vid)
    if su and rx.search(su): surf[s][su.strip().lower()] += 1
rows = []
for s in set(surf) | {s for s, g in gl.items() if g and rx.search(g) and s not in m07}:
    n = sum(surf[s].values())
    if not vv[s]: continue
    if n < 2 and not (gl.get(s) and rx.search(gl[s])): continue
    rows.append((s, tr.get(s), gl.get(s), ' '.join(sorted(tag[s])) or '-', len(vv[s]), len(vv[s] & m07v),
                 len(vv[s] & cited), n, '; '.join(f'{a} ({b})' for a, b in surf[s].most_common(4))))
for r in sorted(rows, key=lambda r: -r[7]): print(r)

# Narrative: sections and passages on shame now
print('\n# narrative sections with shame words in heading')
for r in c.execute("""SELECT ch.chapter_no, ns.heading FROM narrative_section ns JOIN narrative_chapter ch ON ch.id=ns.chapter_id
   AND ch.inactive=0 WHERE ns.last_version IS NULL"""):
    if r[1] and re.search(r'shame|asham|disgrac|reproach|honou?r|curse|confus|blush|naked|contempt|despis', r[1], re.I): print(r)
print('\n# word counts in current passages, by chapter')
wc = defaultdict(Counter)
for ch, t in c.execute("""SELECT ch.chapter_no, np.passage_text FROM narrative_passage np JOIN narrative_chapter ch
   ON ch.id=np.chapter_id AND ch.inactive=0 WHERE np.last_version IS NULL"""):
    for w in re.findall(r'\b(shame\w*|ashamed|disgrac\w*|reproach\w*|dishono\w*|humiliat\w*|confound\w*|confusion|blush\w*|curse\w*|cursing|accursed|contempt|despis\w*)\b', t or '', re.I):
        wc[w.lower()][ch] += 1
for w, cc in sorted(wc.items(), key=lambda x: -sum(x[1].values())): print(w, sum(cc.values()), cc.most_common(8))
print('\n# claims with shame words')
for r in c.execute("SELECT claim_ref, status, substr(claim_text,1,120) FROM narrative_claim"):
    if r[2] and re.search(r'shame|asham|disgrac|reproach|dishono|humiliat|confound|blush|curse|contempt|despis', r[2], re.I): print(r)

# Verse lists the overview names
print('\n# no other M-code', len([r for r in xref if not r['other_mcodes']]), [r['reference'] for r in xref if not r['other_mcodes']])
for code in ('M08', 'M09', 'M02', 'M01', 'M18', 'M64', 'M25', 'M20'):
    print(f'\n# shared with {code}', [r['reference'] for r in xref if code in r['other_mcodes'].split()])
print('\n# in claims register', [r['reference'] for r in xref if r['in_claims_register'] == '1'])
print('\n# M07 Strong\'s in the narrative passage text? cited verses per group')
