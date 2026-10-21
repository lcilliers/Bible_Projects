"""M02 recovery: mechanical roll-up tests across the M02 folder, plus the M-code co-existence
dimension, with no verse reading (researcher, 2026-10-05). iba.db opened read-only.

Researcher, verbatim (2026-10-05): "a simple query of the verse-lexical table against the 681
verses will allow is to isolate all the M-code cluster references in play across the 681 verses
... these M-codes may be spread to specific faces or operations. So no need to read all the
verses, but only the verses for the specific iterations of anger -> M-code combinations. The end
result is outstanding items to follow up when each of those M-code analysis comes into play."

Tests (each writes pass/fail lists by ID):
  T1 verse coverage: live M02 verses (verse_lexical.role) = phenomena ledger v5 = faces files
  T2 face -> ledger: every face has a B.x section in its unit ledger, and that section has AG rows
  T3 phenomenon (U1/U2) -> AG rows: per phenomenon code, how many of its verses an AG row quotes
  T4 AG -> overview: every AG id is cited in the cross-ledger overview
  T5 co-existence: verses in U1 s37 and U2 s65 that overview part F does not cite
  T6 side branches: where the no-seat pilot, the investigations and the 1 Oct ledger (AN rows)
     are cited downstream
  T7 M-code dimension: every non-M02 M-code token in the anger verses, assigned to the face of
     the nearest M02 hit in the same verse (mechanical rule), and the phenomenon of the verse

Outputs (this folder):
  wa-cluster-M02-recovery-test-results-v1-20261005.md        results of T1-T7
  wa-cluster-M02-mcode-face-combinations-v1-20261005.csv     one row per M-code x face (T7)

Usage (project root):  python "_analytics/Clusters/M02 - anger-wrath/wa-cluster-M02-recovery-tests-v1-20261005.py"
"""
import csv, glob, json, os, re, sqlite3
from collections import Counter, defaultdict

D = os.path.dirname(os.path.abspath(__file__))
OUT_MD = os.path.join(D, 'wa-cluster-M02-recovery-test-results-v1-20261005.md')
OUT_CSV = os.path.join(D, 'wa-cluster-M02-mcode-face-combinations-v1-20261005.csv')
U1 = os.path.join(D, 'wa-cluster-M02-phenomena-v2-20260928.md')
U2 = os.path.join(D, 'wa-cluster-M02-unit2-phenomena-v3-20260929.md')
OV = os.path.join(D, 'anger-cross-ledger-overview-v1-20261005.md')
db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
out = []


def p(s=''):
    out.append(s)


def read(path):
    return open(path, encoding='utf-8-sig').read()


REF = re.compile(r'((?:[1-3])?[A-Z][a-z]+)\.?\s+(\d+:\d+)|(?<![\w:])(\d+:\d+)')


def refs(text):
    """Verse references in a text; a bare 'c:v' takes the last book named."""
    book, found = None, []
    for m in REF.finditer(text):
        if m.group(1):
            book, v = m.group(1), m.group(2)
        else:
            v = m.group(3)
        if book:
            found.append(f'{book} {v}')
    return found


def codes(role):
    try:
        return json.loads(role) if role else []
    except ValueError:
        return []


def section(text, start_pat, stop_pat=r'^## '):
    """Text from the heading matching start_pat to the next heading matching stop_pat."""
    lines, keep, buf = text.splitlines(), False, []
    for ln in lines:
        if keep and re.match(stop_pat, ln):
            break
        if re.match(start_pat, ln):
            keep = True
        if keep:
            buf.append(ln)
    return '\n'.join(buf)


names = dict(db.execute("SELECT cluster_code, short_name FROM cluster"))

# ---------- inputs ----------
v5 = {r['reference']: r for r in csv.DictReader(open(os.path.join(D, 'wa-cluster-M02-phenomena-ledger-v5-20260929.csv'), encoding='utf-8-sig'))}
faces = {}           # (ref, pos) -> (unit, face, face_name); a second face at one position is kept in faces2
faces2 = []
face_name = {}
face_unit = {}
for u in range(1, 6):
    f = glob.glob(os.path.join(D, f'anger-unit{u}-faces-*.csv'))[0]
    for r in csv.DictReader(open(f, encoding='utf-8-sig')):
        k = (r['reference'], int(r['position']))
        if k in faces:
            faces2.append((k, u, r['face']))
        else:
            faces[k] = (u, r['face'], r['face_name'])
        face_name[r['face']] = r['face_name']; face_unit[r['face']] = u

m02 = defaultdict(list)
for vid, pos, role in db.execute("SELECT verse_id, position, role FROM verse_lexical WHERE deleted=0 AND role LIKE '%M02%'"):
    if 'M02' in codes(role):
        m02[vid].append(pos)
vref = {}
ids = list(m02)
for i in range(0, len(ids), 400):
    ch = ids[i:i + 400]
    for vid, ref in db.execute(f"SELECT id, reference FROM verse WHERE deleted=0 AND id IN ({','.join(map(str, ch))})"):
        vref[vid] = ref
m02 = {v: ps for v, ps in m02.items() if v in vref}
live_verses = set(vref.values())
face_verses = {k[0] for k in faces}

# phenomenon code -> (unit doc, section number, title), from the U1/U2 headings
ph_sec = {}
for doc, path in (('U1', U1), ('U2', U2)):
    for m in re.finditer(r'^## (\d+)\. (.+?) \(([A-Z]{2})\)', read(path), re.M):
        ph_sec.setdefault(m.group(3), (doc, int(m.group(1)), m.group(2)))
    for m in re.finditer(r'^\| (\d+) \| ([^|]+?) \| ([A-Z]{2}) \|', read(path), re.M):  # summary-table codes
        ph_sec.setdefault(m.group(3), (doc, int(m.group(1)), m.group(2).strip()))
ph_sec[''] = ('—', 0, 'no phenomenon: side none/other in ledger v5 (no anger in the verse)')

p('# M02 recovery: roll-up test results (v1)')
p()
p('**Date:** 2026-10-05 · **Generated by** `wa-cluster-M02-recovery-tests-v1-20261005.py` (read-only; rerun to refresh). '
  '**No verse was read to produce this file.** Every line is a count or an ID list from the files and iba.db.')
p()

# ---------- T1 ----------
p('## T1. Verse coverage')
p()
p(f'- live M02 verses (verse_lexical.role holds M02, verse not deleted): **{len(live_verses)}**, hits **{sum(len(x) for x in m02.values())}**')
p(f'- phenomena ledger v5 verses: **{len(v5)}** · faces-file verses: **{len(face_verses)}** · faces-file rows: **{len(faces) + len(faces2)}**'
  f' (positions holding a second face: {[(k[0], k[1], f) for k, u, f in faces2]}; T7 uses the first face there)')
for label, a, b in (('live not in v5', live_verses, set(v5)), ('v5 not live', set(v5), live_verses),
                    ('live not in faces', live_verses, face_verses), ('faces not live', face_verses, live_verses)):
    d = sorted(a - b)
    p(f'- {label}: {len(d)}' + (f' — {", ".join(d)}' if d else ''))
nohit = [(vref[v], q) for v, ps in m02.items() for q in ps if (vref[v], q) not in faces]
p(f'- M02 hits (by role) with no face row: {len(nohit)}' + (f' — {nohit[:20]}' if nohit else ''))
p(f'- phenomenon codes in v5 with no U1/U2 heading: {sorted({r["phenomenon"] for r in v5.values()} - set(ph_sec)) or "none"}')
p()

# ---------- ledgers: sections and AG rows ----------
def expand(spec, unit):
    """Face list from a heading like 'faces 3M–3T' or 'faces G, H, I' against the unit's faces."""
    allf = sorted([f for f, u in face_unit.items() if u == unit], key=lambda f: (len(f), f))
    got = []
    for part in re.split(r',|;| and ', spec):
        part = part.strip().split(' ')[0]
        m = re.match(r'^(\w+)\s*[–-]\s*(\w+)$', part)
        if m and m.group(1) in allf and m.group(2) in allf:
            a, b = allf.index(m.group(1)), allf.index(m.group(2))
            got += allf[a:b + 1]
        elif part in allf:
            got.append(part)
    return got


ag_rows = {}          # AG id -> dict(unit, section, verses)
face_sec = defaultdict(list)   # face -> [(unit, section heading)]
sec_ag = defaultdict(list)
for u in range(1, 6):
    path = glob.glob(os.path.join(D, f'anger-observation-ledger-unit{u}-*.md'))[0]
    sec = None
    for ln in read(path).splitlines():
        m = re.match(r'^### (B\.\d+) (.+)$', ln)
        if m:
            sec = f'U{u} {m.group(1)}'
            for spec in re.findall(r'\((?:faces?|face) ([^)]+)\)', m.group(2)) + re.findall(r'\((\w{1,3})\)', m.group(2)):
                for f in expand(spec, u):
                    face_sec[f].append(sec)
            continue
        if re.match(r'^## ', ln):
            sec = None
        if ln.startswith('| AG-'):
            c = [x.strip() for x in ln.split('|')]
            ag_rows[c[1]] = {'unit': u, 'section': sec, 'verses': refs(c[4])}
            if sec:
                sec_ag[sec].append(c[1])

# ---------- T2 ----------
p('## T2. Face → ledger section → AG rows')
p()
nosec = sorted([f for f in face_unit if not face_sec.get(f)], key=lambda f: (face_unit[f], len(f), f))
noag = sorted([f for f in face_unit if face_sec.get(f) and not any(sec_ag.get(s) for s in face_sec[f])],
              key=lambda f: (face_unit[f], len(f), f))
p(f'- faces: **{len(face_unit)}** · AG rows: **{len(ag_rows)}** · AG rows outside a B.x section: '
  f'{sorted([a for a, r in ag_rows.items() if not r["section"]]) or "none"}')
p(f'- faces with no B.x section heading naming them: **{len(nosec)}**' + (f' — {", ".join(nosec)}' if nosec else ''))
p(f'- faces whose section has no AG row: **{len(noag)}**' + (f' — {", ".join(noag)}' if noag else ''))
p('- (a face named only inside a section body, not its heading, shows here as "no heading"; check those by hand)')
p()

# ---------- T3 ----------
quoted = defaultdict(set)
for a, r in ag_rows.items():
    for v in r['verses']:
        quoted[v].add(a)
outside = sorted({v for v in quoted if v not in v5})
by_ph = defaultdict(list)
for ref, r in v5.items():
    by_ph[r['phenomenon']].append(ref)
verse_faces = defaultdict(Counter)
for (ref, pos), (u, f, n) in faces.items():
    verse_faces[ref][f] += 1
p('## T3. U1/U2 phenomenon → AG rows (does an AG row quote any of its verses?)')
p()
p(f'- AG rows quote **{sum(1 for v in v5 if quoted.get(v))}** of the {len(v5)} verses; every verse is covered by a face (T1).')
p(f'- verse references in AG rows outside the 681: **{len(outside)}** (context verses, or parse slips) — {", ".join(outside)}')
p()
p('| phenomenon | U1/U2 § | title | verses | quoted in AG | AG rows | faces its verses carry |')
p('|---|---|---|---:|---:|---|---|')
rows3 = []
for ph, vs in by_ph.items():
    q = [v for v in vs if quoted.get(v)]
    ags = sorted({a for v in q for a in quoted[v]}, key=lambda a: int(a[3:]))
    fc = Counter()
    for v in vs:
        fc.update(verse_faces[v])
    doc, n, t = ph_sec.get(ph, ('?', 0, '?'))
    rows3.append((len(q) / len(vs), doc, n, ph or '(none)', t, len(vs), len(q), ags, fc))
for frac, doc, n, ph, t, nv, nq, ags, fc in sorted(rows3, key=lambda x: (x[0], x[1], x[2])):
    p(f'| {ph} | {doc} §{n} | {t[:60]} | {nv} | {nq} | {", ".join(ags) or "—"} | {", ".join(f"{k} {c}" for k, c in fc.most_common())} |')
p()
p(f'- phenomena with **no** verse quoted in an AG row: **{sum(1 for r in rows3 if r[6] == 0)}** of {len(rows3)}. '
  'These are the places where U1/U2 detail may not have been carried into the unit ledgers; each is checked by reading '
  'only that U1/U2 section against the faces listed beside it.')
p()

# ---------- T4 ----------
ov = read(OV)
cited = set()
for ln in ov.splitlines():
    if re.match(r'^\| unit \d', ln):     # the sources table states each unit's whole range
        continue
    for a, b in re.findall(r'AG-(\d+)\s*(?:to|–|-)\s*(?:AG-)?(\d+)', ln):
        cited.update(f'AG-{i:02d}' for i in range(int(a), int(b) + 1))
    cited.update(re.findall(r'AG-\d+', ln))
notcited = sorted([a for a in ag_rows if a not in cited], key=lambda a: int(a[3:]))
p('## T4. AG rows → overview')
p()
p(f'- AG rows in the five ledgers: **{len(ag_rows)}** · cited in the overview (ranges expanded, sources table excluded): '
  f'**{len(set(ag_rows) & cited)}** · not cited: **{len(notcited)}**')
if notcited:
    p(f'- not cited: {", ".join(notcited)}')
p()

# ---------- T5 ----------
partF = section(ov, r'^## F\b')
fref = set(refs(partF))
p('## T5. Co-existence (U1 §37, U2 §65) → overview part F')
p()
for doc, path, num in (('U1', U1, 37), ('U2', U2, 65)):
    s = section(read(path), rf'^## {num}\. ')
    rs = sorted(set(refs(s)))
    miss = [r for r in rs if r not in fref]
    p(f'- {doc} §{num}: {len(rs)} verse references; cited in part F: {len(rs) - len(miss)}; not cited: **{len(miss)}**')
p(f'- overview part F found: {"yes" if partF else "NO"} ({len(partF.splitlines())} lines, {len(fref)} verse references)')
p()

# ---------- T6 ----------
p('## T6. Side branches and the 1 Oct ledger: where each is cited downstream')
p()
later = sorted(glob.glob(os.path.join(D, 'anger-*.md')))
for label, pat in (('no-seat pilot', r'noseat|no-seat|no seat'),
                   ('hardening investigation', r'hardening|#1890'),
                   ('heavy-hand investigation', r'heavy-hand|heavy hand|#1892'),
                   ('1 Oct strand ledger', r'anger-strand-observation-ledger-v1-20261001')):
    hits = [os.path.basename(f) for f in later if re.search(pat, read(f), re.I) and 'v1-20261001' not in f]
    p(f'- {label}: cited in {len(hits)} later file(s)' + (f' — {", ".join(hits)}' if hits else ''))
an = sorted(set(re.findall(r'\bAN-\d+', read(os.path.join(D, 'anger-strand-observation-ledger-v1-20261001.md')))), key=lambda a: int(a[3:]))
an_later = set()
for f in later:
    if 'v1-20261001' not in f:
        an_later.update(re.findall(r'\bAN-\d+', read(f)))
p(f'- AN ids in the 1 Oct ledger: {len(an)} ({an[0] if an else ""}–{an[-1] if an else ""}); cited in the 5 Oct files: {len(an_later & set(an))}; '
  f'not cited: {len(set(an) - an_later)}')
p()

# ---------- T7 ----------
combo = defaultdict(lambda: {'verses': set(), 'near': set(), 'tokens': 0, 'surf': Counter(), 'ph': Counter()})
on_word = Counter()
other = Counter()
for i in range(0, len(ids), 400):
    ch = [v for v in ids[i:i + 400] if v in m02]
    for vid, pos, st, s, role in db.execute(
            f"SELECT verse_id, position, strong, surface, role FROM verse_lexical WHERE deleted=0 "
            f"AND verse_id IN ({','.join(map(str, ch))}) ORDER BY verse_id, position"):
        cs = [c for c in codes(role) if c != 'M02']
        if not cs:
            continue
        ref = vref[vid]
        h = min(m02[vid], key=lambda x: (abs(x - pos), x))
        d = abs(h - pos)
        for c in cs:
            if not c.startswith('M'):
                other[c] += 1
                continue
            if d == 0:
                on_word[c] += 1
                continue
            u, f, n = faces.get((ref, h), (0, '?', '?'))
            k = combo[(c, f)]
            k['verses'].add(ref); k['tokens'] += 1
            k['surf'][f'{(s or "").strip()} ({st})'] += 1
            k['ph'][v5.get(ref, {}).get('phenomenon', '?')] += 1
            if d <= 3:
                k['near'].add(ref)

per_m = defaultdict(set)
for (c, f), k in combo.items():
    per_m[c] |= k['verses']
with open(OUT_CSV, 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['mcode', 'cluster', 'face', 'unit', 'face_name', 'verses', 'verses_near', 'tokens',
                'phenomena', 'surfaces', 'verse_list'])
    for (c, f), k in sorted(combo.items(), key=lambda x: (-len(per_m[x[0][0]]), x[0][0], -len(x[1]['verses']))):
        w.writerow([c, names.get(c, ''), f, face_unit.get(f, ''), face_name.get(f, ''), len(k['verses']), len(k['near']),
                    k['tokens'], '; '.join(f'{a} {b}' for a, b in k['ph'].most_common()),
                    '; '.join(f'{a} {b}' for a, b in k['surf'].most_common(8)),
                    '; '.join(sorted(k['verses']))])

p('## T7. M-code dimension: anger → M-code combinations (verse_lexical, no reading)')
p()
p('**Rule:** a token carrying another M-code is assigned to the face of the nearest M02 hit in the same verse '
  '(ties go to the earlier hit). "near" = within 3 positions. Codes on the M02 word itself are listed apart. '
  f'Full combination list: `{os.path.basename(OUT_CSV)}` (one row per M-code × face, with verse lists).')
p()
p(f'- M-codes co-existing with anger: **{len(per_m)}** · M-code × face combinations: **{len(combo)}** · '
  f'combinations with 3+ verses: **{sum(1 for k in combo.values() if len(k["verses"]) >= 3)}**')
p(f'- second M-codes on the M02 word itself: {dict(on_word.most_common()) or "none"}')
p(f'- non-M codes (T-codes, FLAG), tokens, not carried further: {dict(other.most_common())}')
p()
p('| M-code | cluster | verses | faces | top faces (verses) |')
p('|---|---|---:|---:|---|')
for c in sorted(per_m, key=lambda c: -len(per_m[c])):
    fs = sorted([(f, len(k['verses'])) for (cc, f), k in combo.items() if cc == c], key=lambda x: -x[1])
    p(f'| {c} | {names.get(c, "")} | {len(per_m[c])} | {len(fs)} | {", ".join(f"{f} {n}" for f, n in fs[:6])} |')
p()

open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out[:40]))
print(f'... written: {OUT_MD}\n            {OUT_CSV}')
