"""#1978, 2026-10-07: the M-codes used together with the "choose" words in the 222 verses the narrative does not
cite. Researcher: "the next perspective to prepare is to extract all the M-codes that are used in
conjunction with these 222 verses."

Per cfg_behaviour_rule reuse-extracted-base-data-set-based-mcode (#1980): no DB query. The M-coded words of
every verse were already read from verse_lexical + cluster_strong by the pull (m64-choose-verses-pull-v2) into
the column other_m_words of m64-choose-reading-v2-20261007.csv; this script only aggregates that column.
The ten "choose" Strong's are not in other_m_words; other M64 words are.

Writes m64-choose-mcode-cooccurrence-v1-20261007.csv: one row per M-code (verses, words, Strong's, groups, verse list).
Usage: python m64-choose-mcode-cooccurrence-v1-20261007.py [--all]   (--all = all 232 verses, not only uncited)
"""
import csv, os, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'm64-choose-reading-v2-20261007.csv')
ALL = '--all' in sys.argv
OUT = os.path.join(HERE, f'm64-choose-mcode-cooccurrence{"-all" if ALL else ""}-v1-20261007.csv')
WORD = re.compile(r'^(M\d+) (\S+) (.*?) "(.*)" @(\d+)$')  # pull format: code strong gloss "surface" @pos


def main():
    verses = [r for r in csv.DictReader(open(SRC, encoding='utf-8-sig')) if ALL or not r['narrative_refs']]
    by = defaultdict(lambda: {'verses': [], 'rows': 0, 'strongs': defaultdict(int), 'groups': defaultdict(set)})
    none = 0
    for r in verses:
        if not r['other_m_words']:
            none += 1
            continue
        for w in r['other_m_words'].split(' | '):
            m = WORD.match(w.strip())
            assert m, f'unparsed in {r["reference"]}: {w}'
            code, strong, gloss = m.group(1), m.group(2), m.group(3)
            d = by[code]
            if r['reference'] not in d['verses']:
                d['verses'].append(r['reference'])
            d['rows'] += 1
            d['strongs'][f'{strong} {gloss}'] += 1
            d['groups'][r['group']].add(r['reference'])
    order = sorted(by, key=lambda k: (-len(by[k]['verses']), k))
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['cluster_code', 'verses', 'rows', 'strongs', 'groups', 'verse_list'])
        for k in order:
            d = by[k]
            w.writerow([k, len(d['verses']), d['rows'],
                        ' | '.join(f'{s} ({n})' for s, n in sorted(d['strongs'].items(), key=lambda i: -i[1])),
                        ' | '.join(f'{g} ({len(v)})' for g, v in sorted(d['groups'].items(), key=lambda i: -len(i[1]))),
                        ', '.join(d['verses'])])
    print(f'{len(verses)} verses; {len(verses) - none} with an M-coded word, {none} without; '
          f'{sum(d["rows"] for d in by.values())} word rows; {len(by)} M-codes -> {OUT}')


if __name__ == '__main__':
    main()
