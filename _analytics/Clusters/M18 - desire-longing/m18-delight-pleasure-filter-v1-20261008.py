"""M18 delight and pleasure: filter buckets from the pairing CSV (#1993). No DB query.

Input: m18-delight-pleasure-pairing-v1-20261008.csv (from ...-pairing-pull-v1-20261008.py).
Adds one column, `filter_bucket`, by these rules, first match wins:
  1 inner-being candidate  - judged good by someone (eyes/seems/suits); or heart, soul or spirit
                              within 2 words; or a delight/pleasure verb or noun outside the tov pair
                              (H2896A, H2895)
  2 qualifies another characteristic - the paired word carries an M-code
  3 qualifies a thing, person, place or act - everything else
`m_god_in_verse` is carried as is: God named in the verse, not "God is the subject" (that needs reading).
A filter for deciding what to read, not a reading.
"""
import csv, os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'm18-delight-pleasure-pairing-v1-20261008.csv')
OUT = os.path.join(HERE, 'm18-delight-pleasure-filter-v1-20261008.csv')
TOV = {'H2896A', 'H2895'}

rows = list(csv.DictReader(open(SRC, encoding='utf-8')))
for r in rows:
    has_m = any(code.startswith('M') for code in r['pair_codes'].split())
    if (r['pattern'].startswith('judged') or r['m_heart_near'] == '1'
            or (r['strong'] not in TOV and r['form'] in ('verb', 'noun'))):
        b = '1 inner-being candidate'
    elif has_m:
        b = '2 qualifies another characteristic'
    else:
        b = '3 qualifies a thing, person, place or act'
    r['filter_bucket'] = b

with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def show(sel, label):
    print('\n==', label, len(sel), 'hits,', len({r['reference'] for r in sel}), 'verses')
    for b, n in sorted(Counter(r['filter_bucket'] for r in sel).items()):
        s = [r for r in sel if r['filter_bucket'] == b]
        print(f'  {b}: {n} (God named in verse: {sum(r["m_god_in_verse"] == "1" for r in s)})')
        print('     patterns', Counter(r['pattern'] for r in s).most_common())

show(rows, 'all group B')
show([r for r in rows if r['strong'] == 'H2896A'], 'H2896A tov')
show([r for r in rows if r['strong'] != 'H2896A'], 'the other 18')
pc = Counter()
for r in rows:
    if r['filter_bucket'].startswith('2'):
        for code in r['pair_codes'].split():
            if code.startswith('M'): pc[code] += 1
print('\nbucket 2 by paired M-code', pc.most_common())
print('bucket 2 pairs', Counter(r['pair_gloss'] for r in rows if r['filter_bucket'].startswith('2')).most_common(45))
print('per strong x bucket')
by = defaultdict(Counter)
for r in rows: by[r['strong']][r['filter_bucket'][0]] += 1
for s, cnt in sorted(by.items(), key=lambda x: -sum(x[1].values())): print(' ', s, rows and next(r['gloss'] for r in rows if r['strong'] == s), dict(cnt))
