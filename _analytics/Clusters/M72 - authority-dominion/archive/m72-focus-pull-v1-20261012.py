"""M72 focus pull (#1998): gloss group B (ruling as an act) and group D (hand as power). Read-only against iba.db.

Researcher ruling, chat 2026-10-12 (verbatim): "M72 need to be treated with care. Group A and C words should all be
treated at most as a qualifyer. These verses should only be read in full within the context of the primary M-code. D
and E is likely to be mostly about divine, and should be read only in as much as it describes the character of God.
It seems that B is the main focus for the purposes of the study, with D where, it applies to humans."

One row per verse. Columns: the group's M72 words, the other M72 words (A/C/E/F, qualifiers at most), the other
M-codes, the narrative citations and open-thread rows (from m72-cluster-verses-crossref-v1-20261012.csv), whether the
verse is one of the 182 M18 x M72 verses (OT-98), and for D a working aid `hand_holder_aid`:
  divine   = the hand word is in construct and the next word is a divine party (verse_lexical party_kind / T7)
  human    = in construct and the next word is a human or corporate party (party_kind human / T8 / T11)
  other    = not resolved mechanically (pronoun suffix, "into the hand of" with an article, etc.): read to decide
The aid is a pointer to a verse to read, not a decision (filters are working aids, #1993).
The `text` column is last.

Usage: python m72-focus-pull-v1-20261012.py
"""
import csv, os, sqlite3
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
XREF = os.path.join(HERE, 'm72-cluster-verses-crossref-v1-20261012.csv')
M18 = os.path.join(HERE, '..', 'M18 - desire-longing', 'm18-m72-shared-triage-v2-20261012.csv')

GROUPS = {
    'A': 'H4428G H4430 H4427A G0932 H4467 H4438 H4437 H4468 G0936 G0937 G0938G G4821 G0934 H3678G H1002 H1055 G0933 H0643',
    'B': 'H4910 H7287A H4475 H7985 H7990 H7980 G2961 H7981 H8323A G1850 G2634 G2963 H7989 H4474 H7786 G2715 G5247 H2632 H4915B H4951 G0831 G1018 G2230 H4896 G1849',
    'C': 'H8269 H7218H H5387A G2962H H7336',
    'D': 'H3027H',
    'E': 'H6635B G4519 H5943',
    'F': 'G0746 G2233 G2583',
}
GROUP = {s: g for g, v in GROUPS.items() for s in v.split()}

c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
gloss = {r[0]: r[1] for r in c.execute('SELECT strongNumber, stepGloss FROM strong')}

m72 = defaultdict(list)       # verse_id -> [(group, strong, surface, position, morph)]
other = defaultdict(list)     # verse_id -> other M-code words
for vid, pos, strong, surf, morph, code in c.execute("""SELECT vl.verse_id, vl.position, vl.strong, vl.surface, vl.morph_code, cs.cluster_code
        FROM verse_lexical vl JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0 AND cs.cluster_code LIKE 'M%'
        WHERE vl.deleted = 0 ORDER BY vl.verse_id, vl.position"""):
    if code == 'M72':
        m72[vid].append((GROUP[strong], strong, surf, pos, morph))
    else:
        other[vid].append(f'{code} {gloss.get(strong, "")} "{surf}"')


def holder(vid, pos, morph):
    if not morph or 'c' not in morph[3:6]:
        return 'other'
    nxt = c.execute("""SELECT role, party_kind FROM verse_lexical WHERE verse_id = ? AND position = ? AND deleted = 0
                       AND code_ordinal = 0""", (vid, pos + 1)).fetchone()
    if not nxt:
        return 'other'
    role, party = nxt[0] or '', nxt[1] or ''
    if party == 'divine' or 'T7' in role:
        return 'divine'
    if party == 'human' or 'T8' in role or 'T11' in role:
        return 'human'
    return 'other'


def norm(ref):
    b, cv = ref.split(' ', 1)
    return ref if ':' in cv else f'{b} 1:{cv}'


xref = {r['reference']: r for r in csv.DictReader(open(XREF, encoding='utf-8-sig'))}
m18 = {r['reference'] for r in csv.DictReader(open(M18, encoding='utf-8-sig'))}

for g in ('B', 'D'):
    rows = []
    for vid in sorted(v for v in m72 if any(w[0] == g for w in m72[v])):
        ref, text = c.execute('SELECT reference, text FROM verse WHERE id = ?', (vid,)).fetchone()
        own = [w for w in m72[vid] if w[0] == g]
        rest = [w for w in m72[vid] if w[0] != g]
        x = xref[norm(ref)]
        row = {'reference': ref,
               f'{g.lower()}_words': ' ; '.join(f'{s} {gloss.get(s, "")} "{su}"' for _, s, su, _, _ in own),
               'other_m72_words': ' ; '.join(f'{gg}: {s} {gloss.get(s, "")} "{su}"' for gg, s, su, _, _ in rest),
               'other_mcodes': ' ; '.join(other[vid])}
        if g == 'D':
            row['hand_holder_aid'] = ' ; '.join(holder(vid, p, m) for _, _, _, p, m in own)
        row.update({'narrative_n': x['narrative_n'], 'narrative_refs': x['narrative_refs'], 'ot_refs': x['ot_refs'],
                    'ot_pairing': x['ot_pairing'], 'in_m18_182': int(ref in m18), 'text': text})
        rows.append(row)
    out = os.path.join(HERE, f'm72-group-{g}-verses-v1-20261012.csv')
    with open(out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(g, len(rows), 'verses ->', os.path.basename(out))
    if g == 'D':
        from collections import Counter
        print(' hand holder aid (per hit):', Counter(h for r in rows for h in r['hand_holder_aid'].split(' ; ')))
        print(' verses with any human holder:', sum(1 for r in rows if 'human' in r['hand_holder_aid']),
              '| all divine:', sum(1 for r in rows if set(r['hand_holder_aid'].split(' ; ')) == {'divine'}))
