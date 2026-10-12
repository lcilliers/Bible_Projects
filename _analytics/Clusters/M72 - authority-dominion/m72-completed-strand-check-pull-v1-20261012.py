"""M72 check of the completed strands (#1998). Read-only.

Researcher, chat 2026-10-12 (verbatim): "check if §5 - other M-Codes - where the primary M_code as already been
completed (m25, M47, M18, M01, M02) appropriately considered the where the authority is coming from or the impact of
the authority on the characteristic".

One row per M72 verse that also holds an M25, M47, M18, M01 or M02 word (overview §5). Columns: the partner strands,
the M72 words with their gloss group (overview §3; all groups except B are qualifiers under the scope ruling), the
partner words, the narrative places, and a working aid `authority_named_in_paragraph`: for each narrative paragraph
that cites the verse, whether the paragraph text holds any of the verse's M72 surface words (e.g. "king", "hand",
"authority"). It is a pointer for reading, not a decision: a paragraph can name the king as "Saul" or "Pharaoh".

Output: m72-completed-strand-check-v1-20261012.csv
Usage: python m72-completed-strand-check-pull-v1-20261012.py
"""
import csv, importlib.util, os, re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v3-20261009.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
src = open(os.path.join(HERE, 'm72-focus-pull-v1-20261012.py'), encoding='utf-8').read()
ns = {}
exec(src[src.index('GROUPS = {'):src.index('GROUP = {')], ns)
GROUP = {s: g for g, v in ns['GROUPS'].items() for s in v.split()}
PARTNERS = ['M25', 'M47', 'M18', 'M01', 'M02']


def paragraphs():
    """(book, ch, v) -> list of (place, paragraph text), same parse as crossref v3 narrative_index."""
    idx = defaultdict(list)
    for f in xr.current_chapters():
        title, section, para, buf = None, '(opening)', 0, []

        def flush():
            if not buf:
                return
            text = ' '.join(buf)
            seen = set()
            for b, c, v, how in xr.cites(text):
                place = f'{title or os.path.basename(f)} · {section} · ¶{para}'
                if (b, c, v, place) not in seen:
                    seen.add((b, c, v, place))
                    idx[(b, c, v)].append((place, text))
        for line in open(f, encoding='utf-8'):
            s = line.strip()
            if s.startswith('# '):
                flush(); buf = []; title = s[2:].strip(); continue
            if s.startswith('#'):
                flush(); buf = []; section, para = s.lstrip('#').strip(), 0; continue
            if not s:
                flush(); buf = []; continue
            if not buf:
                para += 1
            buf.append(s)
        flush()
    return idx


def norm(ref):
    b, cv = ref.split(' ', 1)
    return ref if ':' in cv else f'{b} 1:{cv}'


hits = defaultdict(list)
for r in csv.DictReader(open(os.path.join(HERE, 'm72-cluster-hits-v1-20261012.csv'), encoding='utf-8')):
    hits[r['reference']].append(r)
partner = defaultdict(lambda: defaultdict(list))
for r in csv.DictReader(open(os.path.join(HERE, 'm72-cluster-mcode-cooccurrence-v1-20261012.csv'), encoding='utf-8')):
    if r['other_cluster_code'] in PARTNERS:
        partner[r['reference']][r['other_cluster_code']].append(f'{r["other_gloss"]} "{r["other_surface"]}"')
xref = {r['reference']: r for r in csv.DictReader(open(os.path.join(HERE, 'm72-cluster-verses-crossref-v1-20261012.csv'), encoding='utf-8-sig'))}
paras = paragraphs()

rows = []
for ref in sorted(partner, key=lambda x: list(hits).index(x)):
    m72 = hits[ref]
    groups = sorted({GROUP[h['strong']] for h in m72})
    surfaces = {h['surface'].strip().lower().rstrip('’s').rstrip("'s") for h in m72 if h['surface']}
    key = xr.ref_key(norm(ref))
    ps = paras.get(key, [])
    named = []
    for place, text in ps:
        t = text.lower()
        named.append('yes' if any(re.search(r'\b' + re.escape(s), t) for s in surfaces if len(s) > 2) else 'no')
    rows.append({
        'reference': ref,
        'partners': ' '.join(p for p in PARTNERS if p in partner[ref]),
        'm72_groups': ''.join(groups),
        'b_in_verse': int('B' in groups),
        'm72_words': ' ; '.join(f'{GROUP[h["strong"]]}: {h["strong"]} {h["gloss"]} "{h["surface"]}"' for h in m72),
        'partner_words': ' ; '.join(f'{p} {w}' for p in PARTNERS for w in partner[ref].get(p, [])),
        'narrative_n': xref[norm(ref)]['narrative_n'],
        'narrative_refs': xref[norm(ref)]['narrative_refs'],
        'authority_named_in_paragraph': ' ; '.join(named),
        'ot_pairing': xref[norm(ref)]['ot_pairing'],
    })
out = os.path.join(HERE, 'm72-completed-strand-check-v1-20261012.csv')
with open(out, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), '->', os.path.basename(out))
cited = [r for r in rows if r['narrative_n'] != '0']
print('cited', len(cited), '| not cited', len(rows) - len(cited))
print('cited: authority named in some citing paragraph', sum(1 for r in cited if 'yes' in r['authority_named_in_paragraph']),
      '| in none', sum(1 for r in cited if 'yes' not in r['authority_named_in_paragraph']))
for p in PARTNERS:
    rs = [r for r in rows if p in r['partners'].split()]
    c = [r for r in rs if r['narrative_n'] != '0']
    print(p, len(rs), 'cited', len(c), 'named', sum(1 for r in c if 'yes' in r['authority_named_in_paragraph']), 'B', sum(r['b_in_verse'] for r in rs))
print('groups (verse level):', Counter(r['m72_groups'] for r in rows).most_common(10))
