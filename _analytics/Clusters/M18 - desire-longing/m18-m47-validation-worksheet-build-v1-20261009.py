"""Worksheet for validating the 208 M18 x M47 verses against the M47 batch C reading and the narrative (#1993).

Input: m18-shared-m47-m25-m02-crossref-v2-20261009.csv. For each M47-shared verse, finds the batch C
section(s) that cite it (heading + the bullet line), the other M47 batch files citing it, the narrative
places, and the passage (2 verses either side, ESV, iba.db, read-only). Groups the verses by their first
batch C section, in file order; verses not in batch C go to a final group.
Output: m18-m47-validation-worksheet-v1-20261009.md (working sheet, data only, no readings).
"""
import csv, importlib.util, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
CL = os.path.normpath(os.path.join(HERE, '..'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
BC = os.path.join(CL, 'M47 - inner-seat', 'M47-x-willing-desiring-batchC-v3-20260928.md')
SRC = os.path.join(HERE, 'm18-shared-m47-m25-m02-crossref-v2-20261009.csv')
OUT = os.path.join(HERE, 'm18-m47-validation-worksheet-v1-20261009.md')
spec = importlib.util.spec_from_file_location('xr', os.path.join(CL, 'M64 - will-resolve', 'verse-narrative-ot-crossref-v2-20261006.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)

c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)

# batch C: verse -> [(section, line)]
order, bc = [], {}
section = None
for line in open(BC, encoding='utf-8'):
    s = line.rstrip('\n')
    if s.startswith('### ') or s.startswith('## '):
        section = s.lstrip('#').strip()
        if section not in order: order.append(section)
        continue
    for b, ch, v, how in xr.cites(s):
        bc.setdefault((b, ch, v), [])
        item = (section, s.strip()[:400])
        if item not in bc[(b, ch, v)]: bc[(b, ch, v)].append(item)


def passage(ref):
    bk, cv = ref.rsplit(' ', 1); ch, v = map(int, cv.split(':'))
    out = []
    for n in range(v - 2, v + 3):
        r = c.execute('SELECT text FROM verse WHERE reference = ? AND deleted = 0', (f'{bk} {ch}:{n}',)).fetchone()
        if r: out.append(('**' if n == v else '') + f'{ch}:{n} {r[0]}' + ('**' if n == v else ''))
    return out


rows = [r for r in csv.DictReader(open(SRC, encoding='utf-8-sig')) if 'M47' in r['shared_with']]
groups = {}
for r in rows:
    k = xr.ref_key(r['reference'])
    secs = bc.get(k, [])
    g = secs[0][0] if secs else '(not cited in batch C)'
    groups.setdefault(g, []).append((r, secs))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('# M18 x M47 validation worksheet (data only)\n\n**Date:** 2026-10-09 · **Escalation:** #1993 · '
            'built by `m18-m47-validation-worksheet-build-v1-20261009.py`. No readings here; see the validation register.\n\n')
    n = 0
    for g in order + ['(not cited in batch C)']:
        if g not in groups: continue
        f.write(f'## {g} ({len(groups[g])})\n\n')
        for r, secs in groups[g]:
            n += 1
            f.write(f"### {r['reference']} · cited {r['narrative_n']}\n")
            f.write(f"- M18: {r['m18_words']}\n- M47: {r['m47_words']}\n")
            if r['m25_words']: f.write(f"- M25: {r['m25_words']}\n")
            if r['m02_words']: f.write(f"- M02: {r['m02_words']}\n")
            if r['delight_filter_bucket']: f.write(f"- delight filter: {r['delight_filter_bucket']}\n")
            for sec, line in secs: f.write(f'- batch C [{sec}]: {line}\n')
            others = [p for p in r['m47_analysis_files'].split(' | ') if p and 'batchC' not in p
                      and not p.startswith('cluster') and 'classification' not in p]
            if others: f.write(f"- other M47 files: {' | '.join(others)}\n")
            if r['narrative_refs']: f.write(f"- narrative: {r['narrative_refs']}\n")
            if r['ot_refs']: f.write(f"- open threads: {r['ot_refs']}\n")
            for p in passage(r['reference']): f.write(f'  > {p}\n')
            f.write('\n')
print(n, 'verses ->', OUT)
for g in order + ['(not cited in batch C)']:
    if g in groups: print(len(groups[g]), g)
