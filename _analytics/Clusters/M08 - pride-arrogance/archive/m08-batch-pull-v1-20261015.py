"""M08 batch pull (#2156): one batch's verses, each in its passage (+-N verses of the same chapter
that exist in iba.db `verse`), with the M08 words and their surfaces. Read-only.

Usage: python m08-batch-pull-v1-20261015.py <batch number 1-5> [context, default 3]
Writes a scratch text file to $M08_SCRATCH (default: next to this script): m08-batch{n}-passages-v1-20261015.txt
"""
import csv, os, sqlite3, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
n = sys.argv[1]; k = int(sys.argv[2]) if len(sys.argv) > 2 else 3
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)

scope = [r for r in csv.DictReader(open(os.path.join(HERE, 'm08-reading-scope-v1-20261015.csv'), encoding='utf-8')) if r['batch'].startswith(n + ' ')]
hits = defaultdict(list)
for h in csv.DictReader(open(os.path.join(HERE, 'm08-cluster-hits-v1-20261015.csv'), encoding='utf-8')):
    hits[h['reference']].append(f"{h['strong']} {h['gloss']} \"{h['surface']}\"")
osis = {r[0]: r[1] for r in c.execute('SELECT reference, osisId FROM verse WHERE deleted = 0')}
text = {r[0]: (r[1], r[2]) for r in c.execute('SELECT osisId, reference, text FROM verse WHERE deleted = 0')}

out = os.path.join(os.environ.get('M08_SCRATCH', HERE), f'm08-batch{n}-passages-v1-20261015.txt')
with open(out, 'w', encoding='utf-8') as f:
    for r in scope:
        o = osis[r['reference']]; b, ch, v = o.rsplit('.', 2)
        f.write(f"=== {r['reference']} | {' ; '.join(hits[r['reference']])} | cited: {r['narrative_places'] or '-'} | other M: {r['other_mcodes'] or '-'} | M09: {r['m09_read_in'] or '-'}\n")
        for i in range(int(v) - k, int(v) + k + 1):
            t = text.get(f'{b}.{ch}.{i}')
            if t: f.write(('>> ' if i == int(v) else '   ') + f'{i} {t[1]}\n')
        f.write('\n')
print(len(scope), 'verses ->', out)
