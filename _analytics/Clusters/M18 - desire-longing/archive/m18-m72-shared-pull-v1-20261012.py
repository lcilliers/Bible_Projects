"""M18 verses shared with M72 Authority & Dominion (#1993, handoff v7 item H).

Researcher, 2026-10-12: "next the M18 strand overview, item F, lists M72 (Authority & Dominion), which shares
182 verses with M18, as recorded so it isn't lost." Read-only against iba.db.

One row per shared verse, with every M18 decision already made for it (all registers and role triages in
this folder) and the delight-filter bucket. Rows with no decision are the verses the M18 strand has not read.
The `text` column is last so verse-narrative-ot-crossref-v3 can append before it.

Usage: python m18-m72-shared-pull-v1-20261012.py
"""
import csv, glob, os, sqlite3
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
OUT = os.path.join(HERE, 'm18-m72-shared-verses-v1-20261012.csv')
FILTER = os.path.join(HERE, 'm18-delight-pleasure-filter-v1-20261008.csv')

c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
words = defaultdict(lambda: defaultdict(list))
for vid, code, strong, gloss, surf in c.execute("""SELECT DISTINCT vl.verse_id, cs.cluster_code, vl.strong, st.stepGloss, vl.surface
        FROM verse_lexical vl JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0 AND cs.cluster_code LIKE 'M%'
        LEFT JOIN strong st ON st.strongNumber = vl.strong WHERE vl.deleted = 0 ORDER BY vl.verse_id, vl.position"""):
    words[vid][code].append(f'{strong} {gloss} "{surf}"')

decisions = defaultdict(list)
for f in sorted(glob.glob(os.path.join(HERE, 'm18-*register-v*.csv')) + glob.glob(os.path.join(HERE, 'm18-*triage-v*.csv'))):
    tag = os.path.basename(f)[4:].rsplit('-v', 1)[0]
    for r in csv.DictReader(open(f, encoding='utf-8-sig')):
        place = r.get('place') or r.get('proposed_place') or r.get('placed_in') or r.get('forward_to') or r.get('group_or_forward') or ''
        decisions[r['reference']].append(f"{tag}: {r.get('decision', '')}" + (f' ({place})' if place else ''))
buckets = defaultdict(set)
for r in csv.DictReader(open(FILTER, encoding='utf-8-sig')):
    buckets[r['reference']].add(r['filter_bucket'])

rows = []
for vid in sorted(v for v in words if 'M18' in words[v] and 'M72' in words[v]):
    ref, text = c.execute('SELECT reference, text FROM verse WHERE id = ?', (vid,)).fetchone()
    rows.append({'reference': ref,
                 'm18_decisions': ' | '.join(decisions.get(ref, [])),
                 'delight_filter_bucket': ' ; '.join(sorted(buckets.get(ref, ()))),
                 'm18_words': ' ; '.join(words[vid]['M18']),
                 'm72_words': ' ; '.join(words[vid]['M72']),
                 'other_mcodes': ' ; '.join(f'{k} {w}' for k in sorted(words[vid]) if k not in ('M18', 'M72') for w in words[vid][k]),
                 'text': text})
with open(OUT, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), 'verses ->', OUT, '|', sum(1 for r in rows if not r['m18_decisions']), 'with no M18 decision')
