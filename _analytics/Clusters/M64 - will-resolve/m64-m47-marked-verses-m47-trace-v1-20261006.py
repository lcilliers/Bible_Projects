"""#1978, 2026-10-06: mark the 29 uncited M64 x M47 verses with no same-pair lead for deeper analysis
and reading, and trace each one through the M47 folder. Read-only.

For each verse:
  m47_places   : every M47 reading file (current versions, .md) and section that cites it
  m47_route    : read (quoted in a reading section) · set aside (only in data notes, cross-reference
                 or a ruling item) · not quoted (in the M47 data CSVs only)
  source_match : the M47 places that fall inside a section the narrative index records as a source
                 for a chapter (00-index-and-status, "Built from (M47)" column), with that chapter

Usage: python m64-m47-marked-verses-m47-trace-v1-20261006.py
"""
import csv, glob, importlib.util, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
M47 = os.path.normpath(os.path.join(HERE, '..', 'M47 - inner-seat'))
IN = os.path.join(HERE, 'm64-m47-uncited-verses-v1-20261006.csv')
OUT_CSV = os.path.join(HERE, 'm64-m47-marked-verses-v1-20261006.csv')
OUT_MD = os.path.join(HERE, 'm64-m47-marked-verses-v1-20261006.md')
MARK = 'marked for deeper analysis and reading (researcher, 2026-10-06, #1978)'

spec = importlib.util.spec_from_file_location('xref', os.path.join(HERE, 'verse-narrative-ot-crossref-v2-20261006.py'))
xref = importlib.util.module_from_spec(spec)
spec.loader.exec_module(xref)

FILE_CODE = {'depiction': 'dep', 'batchA': 'A', 'batchB': 'B', 'batchC': 'C', 'batchD': 'D',
             'batchE': 'E', 'batchF': 'F', 'batchG': 'G', 'batchH': 'H'}
# Sources named in 00-index-and-status-v1-20260930.md, "Built from (M47)" column (read 2026-10-06).
SOURCES = {
    'dep': [('1', 'Ch 1'), ('2.1', 'Ch 4'), ('2.2', 'Ch 5'), ('2.3', 'Ch 6'), ('2.4', 'Ch 7'), ('2.5', 'Ch 8'),
            ('2.6', 'Ch 8'), ('3.1', 'Ch 3'), ('3.2', 'Ch 3'), ('3.3', 'Ch 3'), ('3.4', 'Ch 9'), ('3.5', 'Ch 7'),
            ('3.6', 'Ch 3'), ('3.7', 'Ch 3'), ('3.8', 'Ch 3')],
    'B': [('1', 'Ch 4'), ('9', 'Ch 4'), ('8', 'Ch 9')], 'C': [('1', 'Ch 5')], 'D': [('3.4', 'Ch 6'), ('9.2', 'Ch 6')],
    'E': [('11', 'Ch 14')], 'F': [('2', 'Ch 3'), ('3', 'Ch 5')], 'G': [('4', 'Ch 5'), ('5', 'Ch 5'), ('7', 'Ch 7')],
    'H': [('5.3', 'Ch 4'), ('6.2', 'Ch 8')],
}
SET_ASIDE = ('0', 'X')  # data notes; cluster cross-reference


def sec_no(heading):
    m = re.match(r'(R\d+|X|\d+(?:\.\d+)?)', heading)
    return m.group(1) if m else heading[:12]


def main():
    rows = [r for r in csv.DictReader(open(IN, encoding='utf-8-sig')) if not r['same_pair_cited']]
    keys = {xref.ref_key(r['reference']): r for r in rows}
    places = {r['reference']: [] for r in rows}
    for f in sorted(glob.glob(os.path.join(M47, '*.md'))):
        code = next((c for k, c in FILE_CODE.items() if k in os.path.basename(f)), None)
        if not code:
            continue
        heading = ''
        for line in open(f, encoding='utf-8'):
            if line.startswith('#'):
                heading = line.strip('# \n')
                continue
            for b, c, v, _ in xref.cites(line):
                if (b, c, v) in keys:
                    p = (code, sec_no(heading), heading[:70])
                    lst = places[keys[(b, c, v)]['reference']]
                    if p not in lst:
                        lst.append(p)
    for r in rows:
        ps = places[r['reference']]
        reading = [p for p in ps if p[1] not in SET_ASIDE and not p[1].startswith('R')]
        r['status'] = MARK
        r['m47_places'] = ' | '.join(f'{c} §{h}' for c, _, h in ps)
        r['m47_route'] = 'read' if reading else ('set aside' if ps else 'not quoted')
        match = []
        for c, n, h in reading:
            for pre, ch in SOURCES.get(c, []):
                if n == pre or n.startswith(pre + '.'):
                    match.append(f'{c} §{n} -> {ch}')
            if 'Cross-cutting' in h:
                match.append(f'{c} §{n} -> Part 10 ("cross-cutting §s of batches A-F")')
        r['source_match'] = ' | '.join(dict.fromkeys(match))
    cols = ['reference', 'status', 'm47_route', 'm47_places', 'source_match', 'm64_words', 'm47_words', 'esv_text']
    with open(OUT_CSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    print(f'{len(rows)} verses marked -> {OUT_CSV}')
    return rows


if __name__ == '__main__':
    main()
