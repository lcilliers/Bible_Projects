"""M09 group B (poor, needy) + H6035: data markers for where the researcher's observation on the
dimensions of poor/needy (chat 2026-10-15, #2148) can be tested in the verses. Read-only.

Markers are a working aid only (feedback_filters_are_working_aids_not_decision_items): they point
to verses to read, they do not decide what a verse says. A verse may carry several markers.
  self      : the speaker names himself poor/needy ("I am", "me", "my", "we are")
  inner     : an M47 inner-seat word in the verse (heart, spirit, soul ...)
  wealth    : an M46 wealth word in the verse (rich, riches ...)
  appeal    : an M42 prayer or M41 being-heard word in the verse
  harm      : an M10 violence, M06 malice/oppression or M58 wickedness word in the verse
  care      : an M05 kindness or M50 grace/mercy word in the verse
  none      : no marker
Writes m09-poor-needy-dimension-markers-v1-20261015.csv with the ESV text.
"""
import csv, os, re, sqlite3
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)
B = 'H0034 H1800 H7326 H4134 H4542 H2489 H6199 G4434 G3993 G4433 H6035'.split()
q = ','.join('?' * len(B))
hits = c.execute(f"""SELECT DISTINCT v.id, v.reference, v.text, vl.strong, vl.surface FROM verse_lexical vl
  JOIN verse v ON v.id = vl.verse_id WHERE vl.deleted = 0 AND vl.strong IN ({q}) ORDER BY v.id""", B).fetchall()
words = defaultdict(list); text = {}; ref = {}
for vid, r, t, s, sf in hits:
    words[vid].append(f'{s} "{(sf or "").strip()}"'); text[vid] = t or ''; ref[vid] = r
mc = defaultdict(set)
for vid, code in c.execute(f"""SELECT DISTINCT vl.verse_id, cs.cluster_code FROM verse_lexical vl
  JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0
  WHERE vl.deleted = 0 AND cs.cluster_code LIKE 'M%' AND vl.verse_id IN ({','.join(map(str, words))})"""):
    mc[vid].add(code)
SELF = re.compile(r"\b(I am|I was|I have been|we are|me|my)\b[^.;:]{0,40}\b(poor|needy|afflicted|lowly|meek|humble)|\b(poor|needy|afflicted)\b[^.;:]{0,25}\b(am I|I am|me)\b", re.I)
M = {'inner': {'M47'}, 'wealth': {'M46'}, 'appeal': {'M42', 'M41'}, 'harm': {'M10', 'M06', 'M58'}, 'care': {'M05', 'M50'}}
rows = []; cnt = Counter()
for vid in words:
    mk = ['self'] if SELF.search(text[vid]) else []
    mk += [k for k, v in M.items() if mc[vid] & v]
    if not mk: mk = ['none']
    for m in mk: cnt[m] += 1
    rows.append([ref[vid], ' ; '.join(words[vid]), ' '.join(mk), ' '.join(sorted(mc[vid] - {'M09'})), text[vid]])
with open(os.path.join(HERE, 'm09-poor-needy-dimension-markers-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'm09_words', 'markers', 'other_mcodes', 'text']); w.writerows(rows)
print('verses', len(rows), dict(cnt))
for r in rows:
    if any(m in r[2].split() for m in ('self', 'inner', 'wealth')): print('|', r[0], '|', r[2], '|', r[4][:230])
