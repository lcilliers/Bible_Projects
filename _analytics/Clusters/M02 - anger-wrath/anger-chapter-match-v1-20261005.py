"""Which verses of a unit pull are already cited in the inner-being narrative chapter files (read-only).

Reads every current chapter file (not archive/), maps full book names to the iba.db short forms and carries the
book forward to bare references, as the quote checker's --prose mode does (so "(7:19)" after "Jeremiah 7:18" counts).
Usage: python anger-chapter-match-v1-20261005.py PULL.csv
Prints: verses matched / total, a count per chapter file, and the matched references per chapter."""
import csv, glob, importlib.util, os, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
QC = os.path.join(ROOT, '..', '..', 'cross-cluster-web', 'fear', 'fear-quote-check-v1-20261001.py')
spec = importlib.util.spec_from_file_location('qc', QC); qc = importlib.util.module_from_spec(spec); spec.loader.exec_module(qc)
CH = os.path.join(ROOT, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative', '*.md')

cited = defaultdict(set)
for path in sorted(glob.glob(CH)):
    key = os.path.basename(path).split('-v')[0]
    book = None
    for line in open(path, encoding='utf-8'):
        if line.startswith('#'):
            continue
        refs, book = qc.refs_in(qc.FULL_RE.sub(lambda m: qc.FULL[m.group(1)], line), book)
        for r in refs:
            cited[r].add(key)

pull = sys.argv[1]
verses = sorted({r['reference'] for r in csv.DictReader(open(pull, encoding='utf-8'))})
by_ch = defaultdict(list)
hit = [v for v in verses if v in cited]
for v in hit:
    for k in cited[v]:
        by_ch[k].append(v)
print(f'{len(hit)} of {len(verses)} verses cited in the chapters')
for k, vs in sorted(by_ch.items(), key=lambda x: -len(x[1])):
    print(f'{k}: {len(vs)}  ' + '; '.join(vs))
