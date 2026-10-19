"""M53 Dishonor & Disgrace: overview extras, read beside M07 (#2171). Read-only against iba.db.

Adds to m53-cluster-overview-pull-v1-20261019.py: gloss groups (a reading aid only), surface splits,
which M53 verses earlier strands already read or decided (their registers and triage files), the
scan for same-sense words outside M53, and the M07 meeting points the researcher asked for: the
verse shared, the root pairs (verb in M53, noun in M07), and M07 hits within three verses of an
M53 hit in the same chapter. Prints, and writes m53-m07-meeting-points-v1-20261019.csv.
"""
import csv, glob, os, re, sqlite3, sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
CL = os.path.dirname(HERE)
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)
TAG = 'v1-20261019'
WINDOW = 3

GROUPS = {
 'A taunt, revile': 'H2778A H1421 G3679 G3058 G3059',
 'B abase, bring low': 'H8213',
 'C mute, silence, muzzle': 'G5392 H0483 G0880 G0216 H2629',
 'D filth': 'H6675 H6674 G4508 G4507 G4509 H5206 H5708',
 'E mutilation, indecency': 'G2699 H4893A G0808',
 'F gloss away from the cluster': 'H5356B H6477',
}
grp = {s: g for g, ss in GROUPS.items() for s in ss.split()}
hits = list(csv.DictReader(open(os.path.join(HERE, f'm53-cluster-hits-{TAG}.csv'), encoding='utf-8')))
xref = list(csv.DictReader(open(os.path.join(HERE, f'm53-cluster-verses-crossref-{TAG}.csv'), encoding='utf-8')))
xr = {r['reference']: r for r in xref}
print('ungrouped', sorted({h['strong'] for h in hits} - set(grp)))

# Earlier strands: every reference in their reading registers and triage files (not archive).
seen = defaultdict(set)
for f in glob.glob(os.path.join(CL, 'M*', '*.csv')):
    name = os.path.basename(f)
    if not re.search(r'register|triage|validation|reading', name): continue
    strand = os.path.basename(os.path.dirname(f)).split(' ')[0]
    if strand in ('M53', 'M07'): continue
    try:
        for r in csv.DictReader(open(f, encoding='utf-8-sig')):
            ref = r.get('reference') or r.get('ref')
            if ref: seen[ref.strip()].add(strand)
    except Exception as e:
        print('skip', name, e)

print('\n# groups: strongs hits verses cited in-register no-other-M read-by-earlier-strand')
for g, ss in GROUPS.items():
    ss = ss.split(); hs = [h for h in hits if h['strong'] in ss]; vs = {h['reference'] for h in hs}
    print(g, len(ss), len(hs), len(vs), sum(int(xr[v]['narrative_n']) > 0 for v in vs),
          sum(xr[v]['in_claims_register'] == '1' for v in vs), sum(not xr[v]['other_mcodes'] for v in vs),
          sum(bool(seen.get(v)) for v in vs), Counter(s for v in vs for s in seen.get(v, ())).most_common())

print('\n# surface by Strong\'s (with refs where few)')
for s in grp:
    hs = [h for h in hits if h['strong'] == s]
    print(s, Counter((h['surface'] or '').strip().lower() for h in hs).most_common(10))
    if len(hs) <= 9: print('   ', [(h['reference'], h['surface']) for h in hs])

# ---- M07 meeting points
vid = {}
for r in c.execute("SELECT id, osisId, reference FROM verse WHERE deleted=0"):
    b, ch, v = r[1].split('.'); vid[r[0]] = (b, int(ch), int(v), r[2])
def cluster_hits(code):
    out = defaultdict(list)
    for v, s, su in c.execute("""SELECT vl.verse_id, vl.strong, vl.surface FROM verse_lexical vl JOIN cluster_strong cs
        ON cs.strong=vl.strong AND cs.cluster_code=? AND cs.deleted=0 WHERE vl.deleted=0""", (code,)):
        out[v].append((s, (su or '').strip()))
    return out
h53, h07 = cluster_hits('M53'), cluster_hits('M07')
gl = {s: g for s, g in c.execute("SELECT strongNumber, stepGloss FROM strong")}
by_ch07 = defaultdict(list)
for v in h07:
    b, ch, n, ref = vid[v]; by_ch07[(b, ch)].append((n, v))
rows = []
for v in sorted(h53, key=lambda v: vid[v][:3]):
    b, ch, n, ref = vid[v]
    near = sorted((abs(n2 - n), v2) for n2, v2 in by_ch07[(b, ch)] if abs(n2 - n) <= WINDOW)
    if not near: continue
    for d, v2 in near:
        rows.append([ref, grp[h53[v][0][0]][0], ' ; '.join(f'{s} "{su}"' for s, su in h53[v]), vid[v2][3], d,
                     ' ; '.join(f'{s} {gl.get(s)} "{su}"' for s, su in h07[v2])])
with open(os.path.join(HERE, f'm53-m07-meeting-points-{TAG}.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['m53_reference', 'm53_group', 'm53_words', 'm07_reference', 'distance', 'm07_words']); w.writerows(rows)
m53_with = {r[0] for r in rows}
print(f'\n# M53 verses with an M07 hit within {WINDOW} verses (same chapter):', len(m53_with), 'of', len(h53))
print('by group', Counter(grp[h53[[v for v in h53 if vid[v][3] == r][0]][0][0]][0] for r in m53_with))
print('same verse', sorted({r[0] for r in rows if r[4] == 0}))
print('distinct M07 verses touched', len({r[3] for r in rows}))
for r in rows: print(r)

# Root pairs: verb in M53, noun in M07
print('\n# root pairs')
for verb, nouns in (('H2778A', ('H2781',)), ('G3679', ('G3680', 'G3681'))):
    vv = {v for v in h53 if any(s == verb for s, _ in h53[v])}
    nv = {v for v in h07 if any(s in nouns for s, _ in h07[v])}
    near = {v for v in vv if any(vid[v][:2] == vid[x][:2] and abs(vid[v][2] - vid[x][2]) <= WINDOW for x in nv)}
    print(verb, len(vv), 'verses;', nouns, len(nv), 'verses; same verse', len(vv & nv), '; verb within 3 of noun', len(near),
          sorted(vid[v][3] for v in near))

# M07 words in M53 verses by group: what shame word sits beside which M53 word
print('\n# verses with no other M-code', [r['reference'] for r in xref if not r['other_mcodes']])
for code in ('M08', 'M09', 'M07', 'M47', 'M72', 'M65'):
    print(f'\n# shared with {code}', [r['reference'] for r in xref if code in r['other_mcodes'].split()])
print('\n# in claims register', [r['reference'] for r in xref if r['in_claims_register'] == '1'])
print('\n# not read by an earlier strand, by group')
for g, ss in GROUPS.items():
    vs = sorted({h['reference'] for h in hits if h['strong'] in ss.split()})
    print(g, [v for v in vs if not seen.get(v)])
