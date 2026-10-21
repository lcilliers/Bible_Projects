"""M07 + M53 reading sets (#2171). Read-only against iba.db.

Researcher, chat 2026-10-19 (verbatim): "Agreed: read M53 A (taunt, revile) with M07 C (reproach) as
one set, and M53 E with M07 D. Keep it under 2171."

Set 1: M53 A (taunt, revile) + M07 C (reproach). Set 2: M53 E (indecency, mutilation) + M07 D
(dishonor, contempt). For each verse: the set words, every other M-coded word and T-coded word
(guide v2 §3.1, one set-based query), narrative places, claim source, earlier-strand decisions,
and a passage unit (same chapter, runs of set verses no more than 3 verses apart), so verses are read
in their passage. Writes m07-m53-reading-set-v1-20261019.csv and prints the passage units.
"""
import csv, glob, os, re, sqlite3, sys
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
CL = os.path.dirname(HERE)
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)
GAP = 3
SETS = {
 '1 reproach': {'M53': 'H2778A H1421 G3679 G3058 G3059', 'M07': 'H2781 H2617B H2616B G3680 G3681 G0176'},
 '2 dishonor': {'M53': 'G0808 G2699 H4893A', 'M07': 'H7036 H7034 H7022 H6173 G0818 G0819 G0820 G1165 G3856'},
}
setof = {}
for name, d in SETS.items():
    for code, ss in d.items():
        for s in ss.split(): setof[s] = (name, code)

V = {}
for vid, osis, ref in c.execute("SELECT id, osisId, reference FROM verse WHERE deleted=0"):
    b, ch, v = osis.split('.'); V[vid] = (b, int(ch), int(v), ref)
gl = {s: g for s, g in c.execute("SELECT strongNumber, stepGloss FROM strong")}
tags = defaultdict(set)
for s, cc in c.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0"): tags[s].add(cc)

rows = c.execute("SELECT verse_id, position, strong, surface FROM verse_lexical WHERE deleted=0 AND strong IN (%s)"
                 % ','.join('?' * len(setof)), list(setof)).fetchall()
inset = defaultdict(list)
for vid, pos, s, su in rows: inset[vid].append((pos, s, (su or '').strip()))
ids = list(inset)
words = defaultdict(list)
for i in range(0, len(ids), 500):
    chunk = ids[i:i + 500]
    for vid, pos, s, su in c.execute("SELECT verse_id, position, strong, surface FROM verse_lexical WHERE deleted=0 AND verse_id IN (%s) ORDER BY verse_id, position"
                                     % ','.join('?' * len(chunk)), chunk):
        words[vid].append((pos, s, (su or '').strip()))
cited = defaultdict(set)
for vid, chno, head in c.execute("""SELECT nc.verse_id, ch.chapter_no, ns.heading FROM narrative_citation nc
    JOIN narrative_chapter ch ON ch.id=nc.chapter_id AND ch.inactive=0 LEFT JOIN narrative_section ns ON ns.id=nc.section_id
    WHERE nc.last_version IS NULL"""):
    cited[vid].add(f'{chno} {head or ""}'.strip())
claimsrc = defaultdict(set)
for vid, ref in c.execute("""SELECT s.verse_id, cl.claim_ref FROM narrative_claim_source s JOIN narrative_claim cl ON cl.id=s.claim_id
    WHERE s.verse_id IS NOT NULL AND cl.status='current'"""): claimsrc[vid].add(ref)
seen = defaultdict(set)
for f in glob.glob(os.path.join(CL, 'M*', '*.csv')):
    if not re.search(r'register|triage|validation|reading', os.path.basename(f)): continue
    strand = os.path.basename(os.path.dirname(f)).split(' ')[0]
    if strand in ('M53', 'M07'): continue
    try:
        for r in csv.DictReader(open(f, encoding='utf-8-sig')):
            ref = r.get('reference') or r.get('ref')
            if ref: seen[ref.strip()].add(strand)
    except Exception:
        pass

# passage units per set: same chapter, consecutive set verses at most GAP apart
units = {}
for name in SETS:
    vs = sorted((V[v][:3], v) for v in inset if any(setof[s][0] == name for _, s, _ in inset[v]))
    n = 0; prev = None
    for key, v in vs:
        if not (prev and prev[:2] == key[:2] and key[2] - prev[2] <= GAP): n += 1
        units[(name, v)] = n; prev = key

out = []
for (name, v), u in sorted(units.items(), key=lambda x: (x[0][0], x[1], V[x[0][1]][:3])):
    b, ch, n, ref = V[v]
    sw = [(s, su) for _, s, su in inset[v] if setof[s][0] == name]
    other_m, tcodes = [], []
    for _, s, su in words[v]:
        if s in setof and setof[s][0] == name: continue
        for cc in sorted(tags[s]):
            (other_m if cc.startswith('M') else tcodes).append(f'{cc} {s} {gl.get(s)} "{su}"')
    out.append([name, f'{name[0]}-{u:03d}', ref, ' ; '.join(f'{setof[s][1]} {s} "{su}"' for s, su in sw),
                ' ; '.join(other_m), ' ; '.join(t for t in tcodes if t.split()[0] in ('T3', 'T4', 'T7', 'T8', 'T9', 'T11', 'T14')),
                ' | '.join(sorted(cited[v])), ' '.join(sorted(claimsrc[v])), ' '.join(sorted(seen.get(ref, ())))])
with open(os.path.join(HERE, 'm07-m53-reading-set-v1-20261019.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['set', 'passage_unit', 'reference', 'set_words', 'other_mcode_words', 'party_and_operation_tcodes', 'narrative_places', 'claim_sources', 'earlier_strands'])
    w.writerows(out)

for name in SETS:
    rs = [r for r in out if r[0] == name]
    us = defaultdict(list)
    for r in rs: us[r[1]].append(r)
    print(f'\n## set {name}: {len(rs)} verses, {len(us)} passage units; cited {sum(bool(r[6]) for r in rs)}; '
          f'claim sources {sum(bool(r[7]) for r in rs)}; read by an earlier strand {sum(bool(r[8]) for r in rs)}; '
          f'M07 only {sum("M53" not in r[3] for r in rs)}, M53 only {sum("M07" not in r[3] for r in rs)}, both {sum("M53" in r[3] and "M07" in r[3] for r in rs)}')
    print('unit sizes', Counter(len(v) for v in us.values()).most_common())
    for u, rr in us.items():
        print(u, len(rr), ' '.join(r[2] for r in rr), '|', ' '.join(sorted({w.split()[1] for r in rr for w in r[3].split(' ; ')})))
