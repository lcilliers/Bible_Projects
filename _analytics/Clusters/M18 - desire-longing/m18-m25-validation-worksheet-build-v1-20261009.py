"""Worksheet for the read-back of the M18 x M25 verses not already done with M47 (#1993, handoff item B).

Input: m18-shared-m47-m25-m02-crossref-v2-20261009.csv (M25 rows without M47: 89). For each verse it gives the
M25 face(s) from the unit faces CSVs, every M25 ledger line citing it (section + line), the narrative places,
open threads, and the passage (2 verses either side, ESV, iba.db, read-only). Groups by first M25 face.
Output: m18-m25-validation-worksheet-v1-20261009.md (working sheet, data only, no readings).
"""
import csv, glob, importlib.util, os, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
CL = os.path.normpath(os.path.join(HERE, '..'))
M25 = os.path.join(CL, 'M25 - life-death')
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
SRC = os.path.join(HERE, 'm18-shared-m47-m25-m02-crossref-v2-20261009.csv')
OUT = os.path.join(HERE, 'm18-m25-validation-worksheet-v1-20261009.md')
spec = importlib.util.spec_from_file_location('xr', os.path.join(CL, 'M64 - will-resolve', 'verse-narrative-ot-crossref-v2-20261006.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)

faces = {}
for f in sorted(glob.glob(os.path.join(M25, 'life-death-*faces-*.csv'))) + [os.path.join(M25, 'life-death-unit1-life-revived-breath-pull-v1-20261002.csv')]:
    for r in csv.DictReader(open(f, encoding='utf-8-sig')):
        try: k = xr.ref_key(r['reference'])
        except ValueError: continue
        item = f"{r['face']} {r['face_name']}"
        faces.setdefault(k, [])
        if item not in faces[k]: faces[k].append(item)

ledgers = sorted(glob.glob(os.path.join(M25, 'life-death-*ledger*.md'))) + [os.path.join(M25, 'life-death-linkage-map.md'),
          os.path.join(M25, 'life-death-unit4-h5782-reading-v1-20261004.md')]
cite = {}
for f in ledgers:
    sec = None
    for line in open(f, encoding='utf-8'):
        s = line.rstrip('\n')
        if s.startswith('#'):
            sec = s.lstrip('#').strip(); continue
        for b, ch, v, how in xr.cites(s):
            cite.setdefault((b, ch, v), [])
            item = (os.path.basename(f).replace('life-death-', '').split('-v')[0], sec, s.strip()[:400])
            if item not in cite[(b, ch, v)]: cite[(b, ch, v)].append(item)


def passage(ref):
    bk, cv = ref.rsplit(' ', 1); ch, v = map(int, cv.split(':'))
    out = []
    for n in range(v - 2, v + 3):
        r = c.execute('SELECT text FROM verse WHERE reference = ? AND deleted = 0', (f'{bk} {ch}:{n}',)).fetchone()
        if r: out.append(('**' if n == v else '') + f'{ch}:{n} {r[0]}' + ('**' if n == v else ''))
    return out


rows = [r for r in csv.DictReader(open(SRC, encoding='utf-8-sig')) if 'M25' in r['shared_with'] and 'M47' not in r['shared_with']]
groups = {}
for r in rows:
    k = xr.ref_key(r['reference'])
    fs = faces.get(k, [])
    groups.setdefault(fs[0] if fs else '(no face)', []).append((r, k))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('# M18 x M25 validation worksheet (data only)\n\n**Date:** 2026-10-09 · **Escalation:** #1993 · '
            'built by `m18-m25-validation-worksheet-build-v1-20261009.py`. 89 verses (M18 x M25, not M47). No readings here.\n\n')
    n = 0
    for g in sorted(groups):
        f.write(f'## {g} ({len(groups[g])})\n\n')
        for r, k in groups[g]:
            n += 1
            f.write(f"### {r['reference']} · cited {r['narrative_n']}\n")
            f.write(f"- M18: {r['m18_words']}\n- M25: {r['m25_words']}\n")
            if r['m02_words']: f.write(f"- M02: {r['m02_words']}\n")
            if r['delight_filter_bucket']: f.write(f"- delight filter: {r['delight_filter_bucket']}\n")
            for fc in faces.get(k, []): f.write(f'- M25 face: {fc}\n')
            for fn, sec, line in cite.get(k, []): f.write(f'- {fn} [{sec}]: {line}\n')
            if r['narrative_refs']: f.write(f"- narrative: {r['narrative_refs']}\n")
            if r['ot_refs']: f.write(f"- open threads: {r['ot_refs']}\n")
            for p in passage(r['reference']): f.write(f'  > {p}\n')
            f.write('\n')
print(n, 'verses ->', OUT)
for g in sorted(groups): print(len(groups[g]), g)
