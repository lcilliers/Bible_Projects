"""M08 Pride & Arrogance: overview extras (#2156). Read-only against iba.db.

Adds to m08-cluster-overview-pull-v1-20261015.py: gloss groups (a reading aid only), the
height words' surface split, the scan for same-sense words tagged outside M08 (OT-02 lesson),
where the deleted tag rows went, the narrative sections and passages on pride, and the
verse lists the overview names. Prints only; the CSVs come from the pull script.
"""
import csv, os, re, sqlite3
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)

# Gloss groups: a reading aid by gloss and surface, not a finding or a sub-grouping.
GROUPS = {
 'A pride, arrogance, presumption': 'H1341 H1342 H1343 H1344 H1346 H1347 H1348 H1365 H1466 H1467 H2086 H2087 H2102 H2103 H3093 H5674H H6277 H7292 H7295 H7312 H7342I H7830 H7986 G0212 G0213 G0829 G2755 G4409 G5187 G5229 G5243 G5244 G5252 G5309 G5367 G5448 G5450',
 'B height, high, lofty': 'H1361 H1363 H1364 H4791 H5920H H5945A H6967 H7314 G5308 G5311 G5313',
 'C boast, boasting': 'H1984H G2620 G2744 G2745 G2746 G4068 G5246 G6094',
 'D mock, scoff, taunt': 'H1422 H2048A H3887 H3932 H4167 H5607A H7046 H8148 H8591 G1702 G2606 G3456',
 'E majesty': 'G3168 G3172',
 'F gloss away from the cluster': 'G0193 H5719 H5953C H7293 H7296',
}
grp = {s: g for g, ss in GROUPS.items() for s in ss.split()}

hits = list(csv.DictReader(open(os.path.join(HERE, 'm08-cluster-hits-v1-20261015.csv'), encoding='utf-8')))
xref = list(csv.DictReader(open(os.path.join(HERE, 'm08-cluster-verses-crossref-v1-20261015.csv'), encoding='utf-8')))
live = {h['strong'] for h in hits}
print('ungrouped', sorted(live - set(grp)), 'grouped-not-live', sorted(set(grp) - live))

xr = {r['reference']: r for r in xref}
vg = defaultdict(set)
for h in hits: vg[h['reference']].add(grp[h['strong']][0])
print('\n# groups: strongs hits verses cited no-other-M')
for g, ss in GROUPS.items():
    ss = ss.split(); hs = [h for h in hits if h['strong'] in ss]; vs = {h['reference'] for h in hs}
    print(g, len(ss), len(hs), len(vs), sum(int(xr[v]['narrative_n']) > 0 for v in vs), sum(not xr[v]['other_mcodes'] for v in vs))
print('combos', Counter(''.join(sorted(v)) for v in vg.values()).most_common(12))

# Height words: surface that names pride vs plain height.
PRIDE = re.compile(r'proud|haught|arrogan|lofty|loftiness|exalt|pride|conceit|uplifted|lifted', re.I)
print('\n# B surface split (pride-like surface vs other)')
for s in GROUPS['B height, high, lofty'].split():
    hs = [h for h in hits if h['strong'] == s]
    p = [h for h in hs if PRIDE.search(h['surface'] or '')]
    print(s, len(hs), 'pride-like', len(p), [(h['reference'], h['surface']) for h in p][:12])

# Where the deleted rows went
print('\n# deleted rows now')
for s in ('G0757', 'H1984H', 'H6965B', 'H2778A'):
    print(s, c.execute("SELECT stepGloss FROM strong WHERE strongNumber=?", (s,)).fetchone(),
          c.execute("SELECT cluster_code, deleted FROM cluster_strong WHERE strong=?", (s,)).fetchall())

# Same-sense words outside M08 (gloss or surface)
print('\n# outside M08: gloss/surface scan')
pat = r'proud|pride|arrogan|haught|boast|mock|scoff|scorn|insolen|conceit|presum|lofty|derid|jeer|brag|puffed|self-exalt|exalt'
rx = re.compile(pat, re.I)
m08 = {r[0] for r in c.execute("SELECT strong FROM cluster_strong WHERE cluster_code='M08' AND deleted=0")}
tag = defaultdict(set)
for s, cc in c.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0"): tag[s].add(cc)
gl = {s: g for s, g in c.execute("SELECT strongNumber, stepGloss FROM strong")}
tr = {s: t for s, t in c.execute("SELECT strongNumber, stepTransliteration FROM strong")}
m08v = {r[0] for r in c.execute("""SELECT DISTINCT vl.verse_id FROM verse_lexical vl JOIN cluster_strong cs
   ON cs.strong=vl.strong AND cs.cluster_code='M08' AND cs.deleted=0 WHERE vl.deleted=0""")}
cited = {r[0] for r in c.execute("""SELECT nc.verse_id FROM narrative_citation nc JOIN narrative_chapter ch
   ON ch.id=nc.chapter_id AND ch.inactive=0 WHERE nc.last_version IS NULL""")}
surf = defaultdict(Counter); vv = defaultdict(set)
for vid, s, su in c.execute("SELECT verse_id, strong, surface FROM verse_lexical WHERE deleted=0"):
    if s in m08: continue
    vv[s].add(vid)
    if su and rx.search(su): surf[s][su.strip().lower()] += 1
rows = []
for s in set(surf) | {s for s, g in gl.items() if g and rx.search(g) and s not in m08}:
    n = sum(surf[s].values())
    if not vv[s]: continue
    if n < 2 and not (gl.get(s) and rx.search(gl[s])): continue
    rows.append((s, tr.get(s), gl.get(s), ' '.join(sorted(tag[s])) or '-', len(vv[s]), len(vv[s] & m08v),
                 len(vv[s] & cited), n, '; '.join(f'{a} ({b})' for a, b in surf[s].most_common(4))))
for r in sorted(rows, key=lambda r: -r[7]): print(r)

# Narrative: sections and passages on pride now
print('\n# narrative sections with pride words in heading')
for r in c.execute("""SELECT ch.chapter_no, ns.heading FROM narrative_section ns JOIN narrative_chapter ch ON ch.id=ns.chapter_id
   AND ch.inactive=0 WHERE ns.last_version IS NULL""" ):
    if r[1] and re.search(r'pride|proud|boast|mock|scoff|lifted|high|arrogan|lower|humil', r[1], re.I): print(r)
print('\n# word counts in current passages, by chapter')
wc = defaultdict(Counter)
for ch, t in c.execute("""SELECT ch.chapter_no, np.passage_text FROM narrative_passage np JOIN narrative_chapter ch
   ON ch.id=np.chapter_id AND ch.inactive=0 WHERE np.last_version IS NULL"""):
    for w in re.findall(r'\b(pride|proud|arrogan\w*|haught\w*|boast\w*|mock\w*|scoff\w*|lifted up|conceit\w*|presum\w*|insolen\w*)\b', t or '', re.I):
        wc[w.lower()][ch] += 1
for w, cc in sorted(wc.items(), key=lambda x: -sum(x[1].values())): print(w, sum(cc.values()), cc.most_common(6))
print('\n# claims with pride words')
for r in c.execute("SELECT claim_ref, status, substr(claim_text,1,110) FROM narrative_claim"):
    if r[2] and re.search(r'pride|proud|boast|mock|scoff|arrogan|haught|lifted', r[2], re.I): print(r)

# Verse lists the overview names
print('\n# no other M-code', [r['reference'] for r in xref if not r['other_mcodes']])
print('\n# shared with M09', [r['reference'] for r in xref if 'M09' in r['other_mcodes'].split()])
print('\n# in claims register', [r['reference'] for r in xref if r['in_claims_register'] == '1'])
