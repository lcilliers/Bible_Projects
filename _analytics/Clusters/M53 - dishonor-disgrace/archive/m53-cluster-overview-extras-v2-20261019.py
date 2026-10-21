"""M53 Dishonor & Disgrace: overview extras v2 (#2171). Read-only against iba.db.

v2 (researcher, 2026-10-19: "you did not do a full summary of M53"): adds what v1 left out, in the
shape of the M07 overview: the scan for same-sense words tagged outside M53 (OT-02 lesson), surfaces
per Strong's with stems, books, within-M53 pairs, the full co-occurrence table, testament, narrative
word counts in the current chapter files, claims with M53 words, and the cited verses by chapter.
v1 (m53-cluster-overview-extras-v1-20261019.py) still produces the meeting-points CSV.
"""
import csv, glob, os, re, sqlite3, sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..', '..')
DB = os.path.join(ROOT, 'iba', 'app', 'db', 'iba.db')
NARR = os.path.join(ROOT, '_analytics', 'essay', 'spirit_soul_body', 'inner-being-narrative')
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)
TAG = 'v1-20261019'
hits = list(csv.DictReader(open(os.path.join(HERE, f'm53-cluster-hits-{TAG}.csv'), encoding='utf-8')))
xref = list(csv.DictReader(open(os.path.join(HERE, f'm53-cluster-verses-crossref-{TAG}.csv'), encoding='utf-8')))
strongs = list(csv.DictReader(open(os.path.join(HERE, f'm53-cluster-strongs-{TAG}.csv'), encoding='utf-8')))

print('# books'); print(Counter(r['reference'].rsplit(' ', 1)[0] for r in xref).most_common(40))
print('\n# per Strong\'s: hits, verses, surfaces, stems')
for s in strongs:
    st = Counter((m or '??')[2:3] if s['strong'].startswith('H') else (m or '?').split('-')[0]
                 for (m,) in c.execute("SELECT morph_code FROM verse_lexical WHERE strong=? AND deleted=0", (s['strong'],)))
    print(s['strong'], s['translit'], s['gloss'], s['hits'], s['verses'], '|', s['surface_top'], '| stems', dict(st), '|', s['tag_source'])

print('\n# within-M53 pairs')
pv = defaultdict(list)
for h in hits: pv[h['reference']].append(h['strong'])
pairs = Counter()
for ref, ss in pv.items():
    ss = sorted(ss)
    for i in range(len(ss)):
        for j in range(i + 1, len(ss)): pairs[(ss[i], ss[j])] += 1
print({ref: ss for ref, ss in pv.items() if len(ss) > 1}, pairs.most_common())

print('\n# co-occurrence, all M-codes (verses)')
co = Counter()
for r in xref:
    for m in r['other_mcodes'].split(): co[m] += 1
names = dict(c.execute("SELECT cluster_code, short_name FROM cluster"))
print([(m, names.get(m), n) for m, n in co.most_common()])

print('\n# cited by chapter (current citations)')
cited = Counter()
for r in xref:
    for p in r['narrative_places'].split(' | '):
        if p: cited[p.split(' ')[0]] += 1
print(cited.most_common())

# Same-sense scan outside M53
pat = r'taunt|revil|mock|scoff|insult|defi|defy|jeer|deride|derision|rail|mute|dumb|speechless|silen|muzzle|filth|dung|excrement|polluted|unclean|abase|brought low|lowly|mutilat|indecen|exposed|marred|disfigur'
rx = re.compile(pat, re.I)
m53 = {r[0] for r in c.execute("SELECT strong FROM cluster_strong WHERE cluster_code='M53' AND deleted=0")}
tag = defaultdict(set)
for s, cc in c.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0"): tag[s].add(cc)
gl = dict(c.execute("SELECT strongNumber, stepGloss FROM strong"))
tr = dict(c.execute("SELECT strongNumber, stepTransliteration FROM strong"))
m53v = {r[0] for r in c.execute("""SELECT DISTINCT vl.verse_id FROM verse_lexical vl JOIN cluster_strong cs
   ON cs.strong=vl.strong AND cs.cluster_code='M53' AND cs.deleted=0 WHERE vl.deleted=0""")}
citedv = {r[0] for r in c.execute("""SELECT nc.verse_id FROM narrative_citation nc JOIN narrative_chapter ch
   ON ch.id=nc.chapter_id AND ch.inactive=0 WHERE nc.last_version IS NULL""")}
surf = defaultdict(Counter); vv = defaultdict(set)
for vid, s, su in c.execute("SELECT verse_id, strong, surface FROM verse_lexical WHERE deleted=0"):
    if s in m53: continue
    vv[s].add(vid)
    if su and rx.search(su): surf[s][su.strip().lower()] += 1
rows = []
for s in set(surf) | {s for s, g in gl.items() if g and rx.search(g) and s not in m53}:
    if not vv[s] or re.match(r'H90\d\d|H0853|H3588A|H0834A|H5921A|H1961|H3605|H4616|H0408|H3808|G1722', s): continue
    n = sum(surf[s].values())
    if n < 2 and not (gl.get(s) and rx.search(gl[s])): continue
    rows.append((s, tr.get(s), gl.get(s), ' '.join(sorted(tag[s])) or '-', len(vv[s]), len(vv[s] & m53v), len(vv[s] & citedv), n,
                 '; '.join(f'{a} ({b})' for a, b in surf[s].most_common(4))))
print('\n# outside M53 scan')
for r in sorted(rows, key=lambda r: -r[7]): print(r)

# Narrative word counts in the current chapter files (narrative_passage holds only told passages)
print('\n# words in current chapter files')
files = [f for f in glob.glob(os.path.join(NARR, '*.md'))]
wc = defaultdict(Counter)
for f in files:
    t = open(f, encoding='utf-8').read()
    for w in re.findall(r'\b(taunt\w*|revil\w*|mock\w*|scoff\w*|insult\w*|defie\w*|defy\w*|jeer\w*|mute|speechless|silenc\w*|muzzl\w*|filth\w*|dung|abase\w*|brought low|indecen\w*|marred)\b', t, re.I):
        wc[w.lower()][os.path.basename(f)[:5]] += 1
for w, cc in sorted(wc.items(), key=lambda x: -sum(x[1].values())): print(w, sum(cc.values()), cc.most_common(6))
print('\n# narrative sections with M53 words in the heading')
for r in c.execute("""SELECT ch.chapter_no, ns.heading FROM narrative_section ns JOIN narrative_chapter ch ON ch.id=ns.chapter_id
   AND ch.inactive=0 WHERE ns.last_version IS NULL"""):
    if r[1] and re.search(r'taunt|revil|mock|scoff|insult|silen|mute|filth|low|clean|disgrac|dishono', r[1], re.I): print(r)
print('\n# claims with M53 words')
for r in c.execute("SELECT claim_ref, substr(claim_text,1,130) FROM narrative_claim WHERE status='current'"):
    if re.search(r'taunt|revil|mock|scoff|insult|defi|silen|mute|filth|brought low|abase|lowly|low ', r[1], re.I): print(r)
print('\n# testament', Counter('NT' if r['reference'].split()[0] in ('Mat','Mar','Luk','Joh','Act','Rom','1Cor','2Cor','Gal','Eph','Phili','Col','1Th','2Th','1Ti','2Ti','Tit','Phm','Heb','Jam','1Pe','2Pe','1Jo','2Jo','3Jo','Jud','Rev') else 'OT' for r in xref))
