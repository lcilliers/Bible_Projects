"""M72 group B: pull the passage (verse +/- N) for every verse triaged 'read' (#1998).

Reads m72-group-B-role-triage-v1-20261012.csv; ESV text from iba.db `verse` (read-only).
Usage: python m72-group-B-passage-pull-v1-20261012.py [N=4]
Writes m72-group-B-passages-v1-20261012.md (working file for the readings).
"""
import csv, os, re, sqlite3, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 4
con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
rows = [r for r in csv.DictReader(open(os.path.join(HERE, 'm72-group-B-role-triage-v1-20261012.csv'), encoding='utf-8-sig')) if r['decision'] == 'read']
out = ['# M72 group B: passages for the verses read (working file)', '', f'Verse +/- {N}, ESV from iba.db `verse`. Missing verses are not in the table.', '']
for g in sorted({r['group_or_forward'] for r in rows}):
    out.append(f'## {g}')
    for r in [x for x in rows if x['group_or_forward'] == g]:
        m = re.match(r'(.+) (\d+):(\d+)$', r['reference'])
        if m:
            bk, ch, v = m.group(1), int(m.group(2)), int(m.group(3))
            key = lambda vv: f'{bk} {ch}:{vv}'
        else:  # single-chapter book, stored as 'Jude 8'
            bk, v = r['reference'].rsplit(' ', 1); v = int(v)
            key = lambda vv: f'{bk} {vv}'
        out.append(f"### {r['reference']} ({r['note']})")
        for vv in range(max(1, v - N), v + N + 1):
            t = con.execute('select text from verse where reference=? and deleted=0', (key(vv),)).fetchone()
            if t:
                mark = '**' if vv == v else ''
                out.append(f'- {mark}{vv}{mark} {t[0]}')
        out.append('')
open(os.path.join(HERE, 'm72-group-B-passages-v1-20261012.md'), 'w', encoding='utf-8').write('\n'.join(out))
print(len(rows), 'verses')
