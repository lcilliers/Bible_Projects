"""Item F (#1993): pull one M18 gloss group, drop verses already decided in the read-back registers, and build a
reading worksheet (data only). Reusable for every group: python m18-group-pull-worksheet-v1-20261009.py A

For each remaining verse: the group's M18 word(s) in it, any other M18 words, the other M-codes in the verse
(from m18-cluster-mcode-cooccurrence-v1-20261008.csv), the narrative places (citation parser of
verse-narrative-ot-crossref-v2, M64 folder) plus a text search of the current chapters (catches bare citations the
parser misses, handoff item I), and the passage (2 verses either side, ESV, iba.db, read-only).
Outputs: m18-group-{G}-pull-v1-20261009.csv and m18-group-{G}-worksheet-v1-20261009.md. Groups by Strong's.
"""
import csv, glob, importlib.util, os, re, sqlite3, sys

GROUPS = {
 'A': 'G1939 H0183 H2530A H8378 G1937 H1942 H2532A H4261 G1971 H1214I H2836A H7602A H0185 H7469 H2531 H3700 H2837 '
      'G3713 G5389 H6165 H8669 G1972 H8373 H0035 H0404 H2968 H3616 H3970 H8375 H7904 G1938 G1973 G1974 G2442 G2691',
 'D': 'H7068 H7065 G2205 G2207 H7067H H7072 G2208 G2581 H7067G',
 'E': 'H6772 G1372 H6770 G1373 G4361',
 'F': 'H3368 G5093 H3365 H3357',
 'G': 'G3117 H4723C G3048 G0275 H0627 H2841 H6899',
 'C': 'G2309 G2307 H7522 H2974 H5068 G4288 H5069 G0594 G4356',
 'B': 'H2896A H2654A H2656 G2106 H2895 H2655 H5273A H6026 H8191 H5276 H5278 H8173B G2237 G0701 H6027 H5282 H5730B G4913 G5369',
}
G = sys.argv[1]
WANT = set(GROUPS[G].split())
HERE = os.path.dirname(os.path.abspath(__file__))
CL = os.path.normpath(os.path.join(HERE, '..'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(CL, 'M64 - will-resolve', 'verse-narrative-ot-crossref-v2-20261006.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)

decided = set()
for f in ['m18-m47-validation-register-v1-20261009.csv', 'm18-m25-validation-register-v1-20261009.csv',
          'm18-m02-validation-register-v1-20261009.csv'] + [
          os.path.basename(g) for g in glob.glob(os.path.join(HERE, 'm18-group-*-register-v1-*.csv'))
          if not os.path.basename(g).startswith(f'm18-group-{G}-')]:  # finished groups are skipped by later groups
    decided |= {r['reference'] for r in csv.DictReader(open(os.path.join(HERE, f), encoding='utf-8-sig'))}

hits = list(csv.DictReader(open(os.path.join(HERE, 'm18-cluster-hits-v1-20261008.csv'), encoding='utf-8-sig')))
m18_by_verse = {}
for h in hits:
    m18_by_verse.setdefault(h['reference'], []).append(h)
other = {}
for r in csv.DictReader(open(os.path.join(HERE, 'm18-cluster-mcode-cooccurrence-v1-20261008.csv'), encoding='utf-8-sig')):
    other.setdefault(r['reference'], set()).add(f"{r['other_cluster_code']} {r['other_gloss']} \"{r['other_surface']}\"")

nidx = xr.narrative_index()
norm = lambda s: ' '.join(re.sub(r"[^a-z ]", ' ', s.lower().replace('’', "'").replace("'", '')).split())
chap = {os.path.basename(f).split('-v')[0]: norm(open(f, encoding='utf-8').read()) for f in xr.current_chapters()}


def textfound(text):
    w = norm(text).split(); found = set()
    for i in range(0, max(1, len(w) - 6), 2):
        frag = ' '.join(w[i:i + 7])
        for k, v in chap.items():
            if frag in v: found.add(k)
    return sorted(found)


def full(ref):  # single-chapter books are stored as 'Jude 18' in iba.db; the parser wants chapter 1
    bk, cv = ref.rsplit(' ', 1)
    return ref if ':' in cv else f'{bk} 1:{cv}'


def passage(ref):
    bk, cv = ref.rsplit(' ', 1)
    if ':' in cv: ch, v = map(int, cv.split(':')); fmt = lambda n: f'{bk} {ch}:{n}'; lab = lambda n: f'{ch}:{n}'
    else: v = int(cv); fmt = lambda n: f'{bk} {n}'; lab = lambda n: f'{n}'
    out = []
    for n in range(v - 2, v + 3):
        r = c.execute('SELECT text FROM verse WHERE reference = ? AND deleted = 0', (fmt(n),)).fetchone()
        if r: out.append(('**' if n == v else '') + f'{lab(n)} {r[0]}' + ('**' if n == v else ''))
    return out


def vtext(ref):
    r = c.execute('SELECT text FROM verse WHERE reference = ? AND deleted = 0', (ref,)).fetchone()
    return r[0] if r else ''


order, rows = [], {}
for h in hits:
    if h['strong'] not in WANT or h['reference'] in decided: continue
    ref = h['reference']
    if ref not in rows:
        order.append(ref); rows[ref] = {'first': h['strong'], 'group': [], }
    rows[ref]['group'].append(f"{h['strong']} {h['gloss']} \"{h['surface']}\"")

OUTC = os.path.join(HERE, f'm18-group-{G}-pull-v1-20261009.csv')
OUTM = os.path.join(HERE, f'm18-group-{G}-worksheet-v1-20261009.md')
by_strong = {}
with open(OUTC, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'first_strong', 'group_words', 'other_m18_words', 'other_mcodes', 'narrative_parser', 'narrative_text_found', 'text'])
    for ref in order:
        try: k = xr.ref_key(full(ref))
        except ValueError: k = None
        r = rows[ref]
        others18 = [f"{h['strong']} {h['gloss']} \"{h['surface']}\"" for h in m18_by_verse.get(ref, []) if h['strong'] not in WANT]
        t = vtext(ref)
        r.update(others18=others18, mc=sorted(other.get(ref, [])), npar=nidx.get(k, []) if k else [], ntext=textfound(t), text=t)
        w.writerow([ref, r['first'], ' ; '.join(r['group']), ' ; '.join(others18), ' ; '.join(r['mc']), ' | '.join(r['npar']), ' ; '.join(r['ntext']), t])
        by_strong.setdefault(r['first'], []).append(ref)

with open(OUTM, 'w', encoding='utf-8') as f:
    f.write(f'# M18 group {G}: reading worksheet (data only)\n\n**Date:** 2026-10-09 · **Escalation:** #1993 (handoff item F) · built by '
            f'`m18-group-pull-worksheet-v1-20261009.py {G}`. {len(order)} verses, after dropping {len(decided)} verses already decided '
            'in the M47, M25 and M02 read-backs. No readings here.\n\n')
    for s in sorted(by_strong, key=lambda s: -len(by_strong[s])):
        f.write(f'## {s} ({len(by_strong[s])})\n\n')
        for ref in by_strong[s]:
            r = rows[ref]
            f.write(f"### {ref}\n- M18 ({G}): {' ; '.join(r['group'])}\n")
            if r['others18']: f.write(f"- other M18: {' ; '.join(r['others18'])}\n")
            if r['mc']: f.write(f"- other M-codes: {' ; '.join(r['mc'][:8])}\n")
            if r['npar']: f.write(f"- narrative (cited): {' | '.join(r['npar'])}\n")
            if r['ntext']: f.write(f"- narrative (text found): {' ; '.join(r['ntext'])}\n")
            for p in passage(ref): f.write(f'  > {p}\n')
            f.write('\n')
print(G, len(order), 'verses;', sum(1 for r in order if rows[r]['npar'] or rows[r]['ntext']), 'already in the narrative somewhere')
for s in sorted(by_strong, key=lambda s: -len(by_strong[s])): print(len(by_strong[s]), s)
