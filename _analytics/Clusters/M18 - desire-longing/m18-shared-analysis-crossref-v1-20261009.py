"""For each M18 shared verse, find where the M47, M25 and M02 cluster analyses cite it (#1993).

Input: m18-shared-m47-m25-m02-crossref-v1-20261009.csv (pull + narrative/open-threads crossref).
Scans the current (non-archive) .md and .csv files in each partner cluster folder with the citation
parser of verse-narrative-ot-crossref-v2 (M64 folder), and adds per partner:
  {code}_analysis_n, {code}_analysis_files  (file names, with the section heading for .md files,
                                             and the face/group column value for .csv rows when present)
Read-only; no DB query.
"""
import csv, glob, importlib.util, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CL = os.path.normpath(os.path.join(HERE, '..'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(CL, 'M64 - will-resolve', 'verse-narrative-ot-crossref-v2-20261006.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)

FOLDERS = {'M47': 'M47 - inner-seat', 'M25': 'M25 - life-death', 'M02': 'M02 - anger-wrath'}
SRC = os.path.join(HERE, 'm18-shared-m47-m25-m02-crossref-v1-20261009.csv')
OUT = os.path.join(HERE, 'm18-shared-m47-m25-m02-crossref-v2-20261009.csv')
FACE_COLS = ('face', 'face_id', 'face_code', 'group', 'faces', 'face_label')


def index_folder(path):
    idx = {}
    for f in sorted(glob.glob(os.path.join(path, '*.md')) + glob.glob(os.path.join(path, '*.csv'))):
        name = os.path.basename(f)
        if f.endswith('.md'):
            section = ''
            for line in open(f, encoding='utf-8', errors='replace'):
                s = line.strip()
                if s.startswith('#'):
                    section = s.lstrip('#').strip()[:60]
                    continue
                for b, ch, v, how in xr.cites(s):
                    idx.setdefault((b, ch, v), set()).add(f'{name} § {section}' if section else name)
        else:
            try:
                rows = list(csv.DictReader(open(f, encoding='utf-8-sig', errors='replace')))
            except Exception:
                continue
            for r in rows:
                face = next((r[k] for k in FACE_COLS if k in r and r[k]), '')
                for val in r.values():
                    if not isinstance(val, str):
                        continue
                    for b, ch, v, how in xr.cites(val):
                        idx.setdefault((b, ch, v), set()).add(f'{name}' + (f' [{face[:40]}]' if face else ''))
    return idx


idx = {code: index_folder(os.path.join(CL, folder)) for code, folder in FOLDERS.items()}
rows = list(csv.DictReader(open(SRC, encoding='utf-8-sig')))
cols = list(rows[0])
new = []
for code in FOLDERS:
    new += [f'{code.lower()}_analysis_n', f'{code.lower()}_analysis_files']
cols = cols[:-1] + new + cols[-1:]
for r in rows:
    k = xr.ref_key(r['reference'])
    for code in FOLDERS:
        places = sorted(idx[code].get(k, ()))
        r[f'{code.lower()}_analysis_n'] = len(places)
        r[f'{code.lower()}_analysis_files'] = ' | '.join(places)
with open(OUT, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)

print(len(rows), '->', OUT)
for code in FOLDERS:
    s = [r for r in rows if code in r['shared_with']]
    inan = [r for r in s if int(r[f'{code.lower()}_analysis_n'])]
    cited = [r for r in s if int(r['narrative_n'])]
    both = [r for r in inan if int(r['narrative_n'])]
    print(code, 'shared', len(s), 'in its analysis', len(inan), 'cited in narrative', len(cited),
          'analysed+cited', len(both), 'analysed not cited', len(inan) - len(both),
          'neither', sum(1 for r in s if not int(r[f'{code.lower()}_analysis_n']) and not int(r['narrative_n'])))
