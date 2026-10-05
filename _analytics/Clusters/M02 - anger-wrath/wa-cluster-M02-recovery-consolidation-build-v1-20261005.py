"""M02 recovery: build the consolidation data (every recorded M02 finding, by ID, nothing dropped).
Read-only on iba.db; reads the M02 folder files only. No verse is read.

Writes  wa-cluster-M02-recovery-consolidation-data-v1-20261005.md  with:
  D1  every face (134), grouped by the overview's forms (party arrangement, overview v1, not yet
      approved), with its AG rows (id + headline), the U1/U2 phenomena whose verses carry it,
      and the AN rows its AG rows cite
  D2  every AN row of the 1 Oct ledger not cited in the 5 Oct files, with its disposition and
      where it was woven
  D3  every U1/U2 line whose references and quotes appear in no later file (5 Oct ledgers,
      overview, 1 Oct ledger), in full, sorted into seat lines, movement lines and process lines

Usage (project root):  python "_analytics/Clusters/M02 - anger-wrath/wa-cluster-M02-recovery-consolidation-build-v1-20261005.py"
"""
import ast, csv, glob, os, re
from collections import Counter, defaultdict

D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, 'wa-cluster-M02-recovery-consolidation-data-v1-20261005.md')
U1 = os.path.join(D, 'wa-cluster-M02-phenomena-v2-20260928.md')
U2 = os.path.join(D, 'wa-cluster-M02-unit2-phenomena-v3-20260929.md')
OCT1 = os.path.join(D, 'anger-strand-observation-ledger-v1-20261001.md')
OV = os.path.join(D, 'anger-cross-ledger-overview-v1-20261005.md')
LEDGERS = sorted(glob.glob(os.path.join(D, 'anger-observation-ledger-unit*-v1-20261005.md')))


def read(p):
    return open(p, encoding='utf-8-sig').read()


REF = re.compile(r'((?:[1-3])?[A-Z][a-z]+)\.?\s+(\d+):(\d+)(?:\s*[–-]\s*(\d+))?|(?<![\w:])(\d+):(\d+)(?:\s*[–-]\s*(\d+))?')


def refs(t):
    b, o = None, []
    for m in REF.finditer(t):
        if m.group(1):
            b, c, v, e = m.group(1), m.group(2), int(m.group(3)), m.group(4)
        else:
            c, v, e = m.group(5), int(m.group(6)), m.group(7)
        if not b:
            continue
        e = int(e) if e and int(e) >= v and int(e) - v < 15 else v
        o += [f'{b} {c}:{x}' for x in range(v, e + 1)]
    return o


out = []
p = out.append

# ---------- faces, forms ----------
faces = defaultdict(lambda: {'unit': 0, 'name': '', 'verses': set(), 'hits': 0})
for u in range(1, 6):
    for r in csv.DictReader(open(glob.glob(os.path.join(D, f'anger-unit{u}-faces-*.csv'))[0], encoding='utf-8-sig')):
        f = faces[r['face']]
        f['unit'], f['name'] = u, r['face_name']
        f['verses'].add(r['reference']); f['hits'] += 1
src = read(os.path.join(D, 'anger-overview-forms-v1-20261005.py'))
FORMS = ast.literal_eval(re.sub(r'#[^\n]*', '', re.search(r'FORMS = (\[.*?\n\])', src, re.S).group(1)))
form_of = {}
for part, form, fs in FORMS:
    for f in fs.split():
        form_of[f] = (part, form)

v5 = {r['reference']: r for r in csv.DictReader(open(os.path.join(D, 'wa-cluster-M02-phenomena-ledger-v5-20260929.csv'), encoding='utf-8-sig'))}
ph_title = {}
for doc, path in (('U1', U1), ('U2', U2)):
    t = read(path)
    for m in re.finditer(r'^## (\d+)\. (.+?) \(([A-Z]{2})[,)]', t, re.M):
        ph_title.setdefault(m.group(3), f'{doc} §{m.group(1)} {m.group(2)}')
    for m in re.finditer(r'^\| (\d+) \| ([^|]+?) \| ([A-Z]{2}) \|', t, re.M):
        ph_title.setdefault(m.group(3), f'{doc} §{m.group(1)} {m.group(2).strip()}')

# ---------- AG rows by section ----------
def expand(spec, unit):
    allf = sorted([f for f, x in faces.items() if x['unit'] == unit], key=lambda f: (len(f), f))
    got = []
    for part in re.split(r',|;| and ', spec):
        part = part.strip().split(' ')[0]
        m = re.match(r'^(\w+)\s*[–-]\s*(\w+)$', part)
        if m and m.group(1) in allf and m.group(2) in allf:
            got += allf[allf.index(m.group(1)):allf.index(m.group(2)) + 1]
        elif part in allf:
            got.append(part)
    return got


ag = {}
face_ag = defaultdict(list)
for u, path in enumerate(LEDGERS, 1):
    sec_faces = []
    for ln in read(path).splitlines():
        m = re.match(r'^### (B\.\d+) (.+)$', ln)
        if m:
            sec_faces = []
            # '(faces 3M–3T)', '(face 5AA; 5AB is read in AG-216)', or a bare '(2T)'
            for spec in re.findall(r'\((?:faces?) ([^)]+)\)', m.group(2)) + re.findall(r'\((\w{1,3})\)', m.group(2)):
                sec_faces += expand(spec, u)
            continue
        if ln.startswith('## '):
            sec_faces = []
        if ln.startswith('| AG-'):
            c = [x.strip() for x in ln.split('|')]
            head = re.match(r'\*\*(.+?)\*\*', c[2])
            ag[c[1]] = {'unit': u, 'head': head.group(1) if head else c[2][:100], 'an': sorted(set(re.findall(r'AN-(?:H)?\d+', ln))),
                        'disp': c[-2], 'faces': list(sec_faces)}
            for f in sec_faces:
                face_ag[f].append(c[1])

ov = read(OV)
ov_cited = set(re.findall(r'AG-\d+', '\n'.join(l for l in ov.splitlines() if not re.match(r'^\| unit \d', l))))
for a, b in re.findall(r'AG-(\d+)\s*(?:to|–|-)\s*(?:AG-)?(\d+)', '\n'.join(l for l in ov.splitlines() if not re.match(r'^\| unit \d', l))):
    ov_cited.update(f'AG-{i:02d}' for i in range(int(a), int(b) + 1))

p('# M02 recovery: consolidation data (v1)')
p('')
p('**Date:** 2026-10-05 · **Generated by** `wa-cluster-M02-recovery-consolidation-build-v1-20261005.py` (read-only; rerun to refresh). '
  'Companion to `wa-cluster-M02-recovery-consolidation-v1-20261005.md`, which explains it. **No verse was read; nothing here is a new reading.** '
  'Each item is quoted or named from the file that holds it, with its ID, so that no recorded finding depends on remembering where it was.')
p('')
p(f'Counts: faces {len(faces)} · AG rows {len(ag)} · AG rows cited in the overview {len(set(ag) & ov_cited)} '
  '(mark **ov** below) · AN rows cited in an AG row are listed with it.')
p('')

# ---------- D1 ----------
p('## D1. Every face, with its AG rows, U1/U2 phenomena and AN rows')
p('')
p('Grouped by the overview v1 forms (part B, arrangement by party, ruling 6.2). The grouping is the overview\'s and is **not yet approved** (#1974); '
  'the faces and AG rows come from the five approved ledgers.')
p('')
by_form = defaultdict(list)
for f in faces:
    by_form[form_of.get(f, ('B.?', 'not placed in a form'))].append(f)
order = [(pt, fm) for pt, fm, _ in FORMS] + [k for k in by_form if k not in [(pt, fm) for pt, fm, _ in FORMS]]
seen = set()
for key in order:
    if key in seen or key not in by_form:
        continue
    seen.add(key)
    p(f'### {key[0]} {key[1]}')
    p('')
    p('| face | name | hits / verses | AG rows (headline) | U1/U2 phenomena of its verses | AN cited |')
    p('|---|---|---|---|---|---|')
    for f in sorted(by_form[key], key=lambda f: (faces[f]['unit'], len(f), f)):
        x = faces[f]
        ags = face_ag.get(f, [])
        agtxt = '<br>'.join(f'{a}{" **ov**" if a in ov_cited else ""}: {ag[a]["head"]}' for a in ags) or '—'
        phc = Counter(v5[v]['phenomenon'] or '(none)' for v in x['verses'] if v in v5)
        phtxt = '; '.join(f'{c} {ph_title.get(c, "no anger in the verse" if c == "(none)" else "")[:48]} ({n})' for c, n in phc.most_common())
        an = sorted({n for a in ags for n in ag[a]['an']})
        p(f'| {f} | {x["name"]} | {x["hits"]} / {len(x["verses"])} | {agtxt} | {phtxt} | {", ".join(an) or "—"} |')
    p('')

# ---------- D2 ----------
later = ''.join(read(f) for f in LEDGERS) + ov
cited_an = set(re.findall(r'\bAN-(?:H)?\d+', later))
oct1 = read(OCT1).splitlines()
woven = []
qsec, rows, sec = False, [], None
for ln in oct1:
    if ln.startswith('## '):
        sec = ln[3:]
        qsec = ln.startswith('## Q.')
    if not ln.startswith('| AN-'):
        continue
    c = [x.strip() for x in ln.split('|')]
    if qsec:
        woven.append((c[1], c[2] if len(c) > 3 else ''))
    else:
        rows.append((c[1], sec, c[2], c[-2]))


def where_woven(an):
    n = int(re.sub(r'\D', '', an) or 0) if not an.startswith('AN-H') else None
    hits = []
    for ids, place in woven:
        nums = set()
        for a, b in re.findall(r'(\d+)\s*[–-]\s*(\d+)', ids):
            nums.update(range(int(a), int(b) + 1))
        nums.update(int(x) for x in re.findall(r'(?<![–\d-])(\d+)(?![–\d-])', ids))
        if n is not None and n in nums:
            hits.append(place)
    return '; '.join(hits) or '—'


p('## D2. AN rows (1 Oct ledger) not cited in the 5 Oct files')
p('')
p('The 1 Oct ledger was woven into the narrative on 2026-10-01 (its §Q). These rows are therefore in the chapter files, '
  'but no 5 Oct unit ledger or the overview cites them. **Chapter numbers in "woven in" are those of 2026-10-01**: '
  'old Ch 9 is now Ch 2 and old Ch 2–8 are now Ch 3–9 (#1936); 10.x and Ch 11–15 are unchanged.')
p('')
p('| AN | section | observation | disposition | woven in (1 Oct §Q) |')
p('|---|---|---|---|---|')
n2 = 0
for an, sec, obs, disp in rows:
    if an in cited_an:
        continue
    n2 += 1
    p(f'| {an} | {sec[:40]} | {obs} | {disp} | {where_woven(an)} |')
p('')
p(f'- AN rows in the 1 Oct ledger: {len(rows)} · not cited in the 5 Oct files: **{n2}**')
p('')

# ---------- D3 ----------
later_all = later + read(OCT1)
LR = set(refs(later_all))


def norm(s):
    return re.sub(r'[^a-z ]', '', s.lower().replace('’', "'"))


LTN = norm(later_all)


def quote_carried(q):
    w = norm(q).split()
    return len(w) >= 4 and any(' '.join(w[i:i + 6]) in LTN for i in range(0, max(1, len(w) - 5)))


PROCESS_SECS = {'0', '36', '39', '67', '§R-V', '§X'}
SEAT = re.compile(r'\*\*Seat|\*\*Outside|\*\*In the verse|Genuine|Spurious|Life-sense|life-sense|Divine\b|divine\b|not inner-being|Person-sense|Appetite-sense|Kinship-sense|\bseat\b', re.I)
groups = {'seat': [], 'movement': [], 'process': []}
for doc, path in (('U1', U1), ('U2', U2)):
    sec = head = None
    for i, ln in enumerate(read(path).splitlines(), 1):
        m = re.match(r'^## (\S+?)\.? (.*)', ln)
        if m:
            sec, head = m.group(1), m.group(2)
            continue
        if not sec or ln.startswith('|') or not ln.strip():
            continue
        rs = list(dict.fromkeys(refs(ln)))
        if not rs:
            continue
        qs = re.findall(r'["“]([^"”]{15,})["”]', ln)
        miss = [r for r in rs if r not in LR and not any(quote_carried(q) for q in qs)]
        if not miss:
            continue
        if sec in PROCESS_SECS:
            kind = 'process'
        elif SEAT.search(ln):
            kind = 'seat'
        else:
            kind = 'movement'
        groups[kind].append((doc, sec, head, i, miss, ln.strip()))

labels = {'seat': 'D3a. Seat lines not carried (heart, soul, spirit and the like, in or around the verse: the M47 connection)',
          'movement': 'D3b. Movement lines not carried (where it comes from, how it co-exists, what it leads to)',
          'process': 'D3c. Process lines (how the reading was done, context lists, bearing on earlier work): not findings'}
p('## D3. U1/U2 lines whose references and quotes appear in no later file')
p('')
p('A line counts as carried when any of its references, or six running words of any quote in it, appears in a 5 Oct ledger, the overview '
  'or the 1 Oct ledger. These lines meet neither test. They are given **in full**, so their detail is not lost. U1 = '
  '`wa-cluster-M02-phenomena-v2-20260928.md`, U2 = `wa-cluster-M02-unit2-phenomena-v3-20260929.md`, with line numbers.')
p('')
for kind in ('seat', 'movement', 'process'):
    rows3 = groups[kind]
    p(f'### {labels[kind]}: {len(rows3)} lines')
    p('')
    last = None
    for doc, sec, head, i, miss, ln in rows3:
        if (doc, sec) != last:
            p(f'**{doc} §{sec}** {head[:120]}')
            p('')
            last = (doc, sec)
        p(f'- {doc} L{i} (not carried: {", ".join(miss)}): {ln.lstrip("- ")}')
    p('')

open(OUT, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('written', OUT)
print('D3 lines:', {k: len(v) for k, v in groups.items()}, '· D2 AN not cited:', n2)
print('faces placed:', sum(1 for f in faces if f in form_of), 'of', len(faces), '· faces with no AG:', [f for f in faces if not face_ag.get(f)])
