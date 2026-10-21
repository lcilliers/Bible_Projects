"""M18 delight and pleasure (overview group B, 19 Strong's): pairing pull, a mechanical first filter (#1993).

Researcher, 2026-10-08: "it looks like 2/3 of the verses are pleasant but the surface is indicative of
meanings that good rather be a qualifyer (describe another characteristic) than a actual characteristic -
pairing might help to break this down."

For each hit: the content word it attaches to (its pair), the pair's M/T code, and a few markers read
off the ESV tokens (than, eyes, evil, do, God named). A pattern is assigned by fixed, visible rules
(PATTERNS below). This is a filter to decide what needs reading, NOT a reading. Read-only against iba.db.
"""
import csv, os, re, sqlite3
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
TAG = 'v1-20261008'
GROUP_B = ('H2896A H2895 H2654A H2655 H2656 H5273A H5276 H5278 H5282 H5730B H6026 H6027 H8173B '
           'H8191 G2106 G2237 G4913 G5369 G0701').split()
GOD = {'H3068G', 'H0430G', 'H3050', 'H0136', 'G2316', 'G2962', 'G3962'}
EYES = {'H5869', 'H5869H', 'H5869G', 'G3788'}
EVIL = {'H7451A', 'H7451B', 'H7451', 'H7489A', 'H7489', 'G2556', 'G4190'}
DO = {'H6213', 'H6213A', 'H6213G', 'G4160', 'G0015', 'H3190'}
HEART = {'H3820', 'H3820A', 'H3824', 'H5315', 'H5315G', 'H7307', 'G2588', 'G5590', 'G4151'}

c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
c.row_factory = sqlite3.Row
gloss = {r[0]: r[1] for r in c.execute('SELECT strongNumber, stepGloss FROM strong')}
codes = defaultdict(set)
for r in c.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted = 0"):
    codes[r[0]].add(r[1])


def pos_kind(morph):
    m = morph or ''
    if m.startswith('HN') or m.startswith('N-'): return 'noun'
    if m.startswith('HV') or m.startswith('V-'): return 'verb'
    if m.startswith('HAa') or m.startswith('A-'): return 'adj'
    return None


def strip_variant(s):  # prefix base, for set membership tolerance
    return {s, s[:5]}


hits = c.execute(f"""SELECT vl.verse_id, v.reference, v.text, vl.position, vl.strong, vl.surface, vl.morph_code
  FROM verse_lexical vl JOIN verse v ON v.id = vl.verse_id
  WHERE vl.deleted = 0 AND vl.strong IN ({','.join('?' * len(GROUP_B))})
  ORDER BY vl.verse_id, vl.position""", GROUP_B).fetchall()

seen, rows = set(), []
for h in hits:
    key = (h['verse_id'], h['position'], h['strong'])
    if key in seen: continue
    seen.add(key)
    toks = c.execute("""SELECT position, strong, surface, morph_code FROM verse_lexical
                        WHERE verse_id = ? AND deleted = 0 ORDER BY position, code_ordinal""",
                     (h['verse_id'],)).fetchall()
    content = {}
    for t in toks:
        k = pos_kind(t['morph_code'])
        if k and t['position'] != h['position'] and t['position'] not in content and t['strong'] not in GROUP_B[:1]:
            content[t['position']] = (t['strong'], t['surface'], k)
    p = h['position']
    prev = max((q for q in content if q < p), default=None)
    nxt = min((q for q in content if q > p), default=None)
    near = lambda S, w: any((t['strong'] in S or t['strong'][:5] in S) and abs(t['position'] - p) <= w for t in toks)
    surf = (h['surface'] or '').lower()
    form = pos_kind(h['morph_code']) or 'other'
    than = any((t['surface'] or '').lower() == 'than' and t['position'] > p for t in toks) or ' than ' in h['text'].lower()
    m_eyes, m_evil, m_do = near(EYES, 3), near(EVIL, 4), near(DO, 1)
    m_heart = near(HEART, 2)
    m_god = any(t['strong'] in GOD for t in toks)
    # pair: attributive adjective -> next noun directly after; otherwise previous content word; verbs -> next
    if form == 'adj' and nxt == p + 1 and content[nxt][2] == 'noun':
        pair = nxt
    elif form == 'verb':
        pair = nxt if nxt is not None else prev
    else:
        pair = prev if prev is not None else nxt
    ps, psurf, _ = content.get(pair, ('', '', ''))
    # PATTERNS, applied in this order (first match wins)
    if re.search(r'\b(better|best)\b', surf) or (h['strong'] == 'H2896A' and than):
        pat = 'comparison (better/best, than)'
    elif m_eyes or re.search(r'\b(seem|seems|seemed|suits|suit)\b', surf):
        pat = "judged good by someone (eyes, seems, suits)"
    elif m_evil:
        pat = 'good set beside evil'
    elif m_do or re.search(r'\bdo(es|ing)? good\b', h['text'].lower()) and surf in ('good', 'well'):
        pat = 'doing good / doing well'
    elif form == 'adj' and pair == nxt and pair is not None:
        pat = 'qualifies the next noun (good X)'
    elif form == 'adj':
        pat = 'said of something (X is good)'
    elif form == 'verb':
        pat = 'verb (delight, please, be pleasant)'
    elif form == 'noun':
        pat = 'noun (delight, pleasure)'
    else:
        pat = 'other'
    rows.append(dict(reference=h['reference'], strong=h['strong'], gloss=gloss.get(h['strong']),
                     surface=h['surface'], form=form, pattern=pat,
                     pair_strong=ps, pair_gloss=gloss.get(ps, ''), pair_surface=psurf,
                     pair_codes=' '.join(sorted(codes.get(ps, ()))),
                     m_than=int(than), m_eyes=int(m_eyes), m_evil=int(m_evil), m_do=int(m_do),
                     m_heart_near=int(m_heart), m_god_in_verse=int(m_god), text=h['text']))

out = os.path.join(HERE, f'm18-delight-pleasure-pairing-{TAG}.csv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

print('rows', len(rows))
by = defaultdict(Counter)
for r in rows: by[r['strong']][r['pattern']] += 1
for s in GROUP_B:
    print(s, gloss.get(s), sum(by[s].values()), dict(by[s].most_common()))
tov = [r for r in rows if r['strong'] == 'H2896A']
print('tov patterns', Counter(r['pattern'] for r in tov).most_common())
print('tov pair codes', Counter((r['pair_codes'] or '-') for r in tov).most_common(20))
print('tov pairs (qualifies next noun)', Counter(r['pair_gloss'] for r in tov if r['pattern'].startswith('qualifies')).most_common(40))
print('tov pairs (said of)', Counter(r['pair_gloss'] for r in tov if r['pattern'].startswith('said')).most_common(40))
print('tov paired with M-code', Counter(r['pair_codes'] for r in tov if 'M' in r['pair_codes']).most_common())
