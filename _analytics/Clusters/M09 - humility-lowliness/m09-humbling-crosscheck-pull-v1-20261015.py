"""M09 humbling fan-out: cross-check against the narrative, the claims register, M08 and M47 (#2148).

Researcher, 2026-10-15: "proceed with the comparison, and the cross check" (scope s3: "the cross-check
against M08 Pride, M47 and the narrative"). Read-only against iba.db.

For every verse decided 'read' or 'carried' in batch registers 1-5 (plus the 7 group-A verses of the
no-other-M-code reading, which sit in the fan-out set):
  - narrative citations now (narrative_citation, last_version IS NULL, active chapters): chapter, section,
    and whether the citing passage text carries the humbling angle (HUM regex on narrative_passage.passage_text)
  - claims-register sources (narrative_claim_source.verse_id -> narrative_claim.claim_ref)
  - M08 / M47 co-occurrence (from the fan-out verse CSV), and for M47 verses the inner-seat surface words
    and whether the verse is cited in any faculty chapter (Ch 3-9)
Writes m09-humbling-crosscheck-v1-20261015.csv and prints the summary figures.
"""
import csv, glob, os, re, sqlite3
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)
HUM = re.compile(r'humbl|lowl|lowli|meek|contrit|humility|gentle|submi|subject|abase|brought low|broken|crushed', re.I)
FACULTY = {'03', '04', '05', '06', '07', '08', '09'}

dec = {}
for f in sorted(glob.glob(os.path.join(HERE, 'm09-humbling-batch*-register-v1-20261015.csv'))):
    b = re.search(r'batch(\d)', f).group(1)
    for r in csv.DictReader(open(f, encoding='utf-8')):
        if r['decision'] in ('read', 'carried'):
            dec[r['reference']] = (b, r['group'], r['decision'], r['route'])
fan = {r['reference']: r for r in csv.DictReader(open(os.path.join(HERE, 'm09-humbling-fanout-verses-v1-20261015.csv'), encoding='utf-8'))}

vid = {}
for ref in dec:
    vid[ref] = c.execute("SELECT id FROM verse WHERE reference=?", (ref,)).fetchone()[0]
# v1 note: narrative_citation.passage_id is almost always NULL (narrative_passage holds only the
# claims-register passages), so the citing paragraph is found in the current chapter file instead:
# every paragraph (line) of that file containing the citation as written.
NARR = os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative')
paras = {}
for chno, fname in c.execute("SELECT chapter_no, current_file FROM narrative_chapter WHERE inactive=0 AND current_file IS NOT NULL"):
    paras[chno] = open(os.path.join(NARR, fname), encoding='utf-8').read().split('\n')
cit = defaultdict(list)
for v, chno, head, asw in c.execute("""SELECT nc.verse_id, ch.chapter_no, ns.heading, nc.ref_as_written
    FROM narrative_citation nc JOIN narrative_chapter ch ON ch.id = nc.chapter_id AND ch.inactive = 0
    LEFT JOIN narrative_section ns ON ns.id = nc.section_id
    WHERE nc.last_version IS NULL"""):
    lines = [l for l in paras.get(chno, []) if asw and asw in l]
    cit[v].append((chno, head or '', any(HUM.search(l) for l in lines)))
reg = defaultdict(set)
for v, ref in c.execute("""SELECT s.verse_id, cl.claim_ref FROM narrative_claim_source s
    JOIN narrative_claim cl ON cl.id = s.claim_id WHERE s.verse_id IS NOT NULL"""):
    reg[v].add(ref)
inner = defaultdict(list)
INNER = ('H3820', 'H3824', 'H7307', 'H5315', 'G2588', 'G4151', 'G5590', 'G3563', 'G1271')
for v, s, sf in c.execute("SELECT verse_id, strong, surface FROM verse_lexical WHERE deleted=0"):
    if v in set(vid.values()) and s.startswith(INNER):
        inner[v].append((sf or '').strip())

rows = []
for ref, (b, g, d, route) in sorted(dec.items(), key=lambda x: (x[1][0], x[0])):
    v = vid[ref]; f = fan.get(ref, {})
    om = f.get('other_mcodes', '').split()
    places = cit[v]
    rows.append({
        'reference': ref, 'batch': b, 'group': g, 'decision': d, 'route': route,
        'cited_n': len(places),
        'cited_places': ' | '.join(sorted({f'{ch} {h}' for ch, h, _ in places})),
        'cited_with_angle': int(any(a for _, _, a in places)),
        'cited_without_angle_only': int(bool(places) and not any(a for _, _, a in places)),
        'ch12_pride': int(any(ch == '12' and 'Pride' in h for ch, h, _ in places)),
        'claims': ' '.join(sorted(reg[v])),
        'm08': int('M08' in om), 'm47': int('M47' in om),
        'inner_words': '; '.join(sorted(set(inner[v]))),
        'in_faculty_chapter': int(any(ch in FACULTY for ch, _, _ in places)),
    })
out = os.path.join(HERE, 'm09-humbling-crosscheck-v1-20261015.csv')
with open(out, 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

N = len(rows)
cited = [r for r in rows if r['cited_n']]
print('verses', N, 'cited', len(cited), 'cited with angle', sum(r['cited_with_angle'] for r in rows),
      'cited without angle only', sum(r['cited_without_angle_only'] for r in rows), 'not cited', N - len(cited))
print('in claims register', sum(1 for r in rows if r['claims']))
print('chapters citing', Counter(p.split(' ')[0] for r in rows for p in r['cited_places'].split(' | ') if p).most_common())
m08 = [r for r in rows if r['m08']]
print('M08', len(m08), 'in Ch12 pride section', sum(r['ch12_pride'] for r in m08), [r['reference'] for r in m08 if r['ch12_pride']])
m47 = [r for r in rows if r['m47'] or r['inner_words']]
print('inner-seat word verses', len(m47), 'in a faculty chapter', sum(r['in_faculty_chapter'] for r in m47))
print('inner-seat verses not in a faculty chapter:', [(r['reference'], r['inner_words']) for r in m47 if not r['in_faculty_chapter']])
print('cited without the angle:', [(r['reference'], r['cited_places']) for r in rows if r['cited_without_angle_only']])
