"""Item F (#1993): register of one M18 gloss group, one decision per verse, from m18-group-{G}-decisions-v1-20261009.py
and m18-group-{G}-pull-v1-20261009.csv. Usage: python m18-group-register-build-v1-20261009.py A
Output: m18-group-{G}-register-v1-20261009.csv. Asserts that every pulled verse has exactly one decision."""
import csv, importlib.util, os, sys
from collections import Counter

G = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('d', os.path.join(HERE, f'm18-group-{G}-decisions-v1-20261009.py'))
d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
rows = list(csv.DictReader(open(os.path.join(HERE, f'm18-group-{G}-pull-v1-20261009.csv'), encoding='utf-8-sig')))
refs = [r['reference'] for r in rows]
missing = [r for r in refs if r not in d.D]; extra = [k for k in d.D if k not in refs]
assert not missing and not extra, (missing, extra)
with open(os.path.join(HERE, f'm18-group-{G}-register-v1-20261009.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'decision', 'place', 'reason', 'group_words', 'other_m18_words', 'narrative_parser', 'narrative_text_found', 'text'])
    for r in rows:
        dec, place, why = d.D[r['reference']]
        w.writerow([r['reference'], dec, place, why, r['group_words'], r['other_m18_words'], r['narrative_parser'], r['narrative_text_found'], r['text']])
print(G, len(rows), Counter(v[0] for v in d.D.values()))
