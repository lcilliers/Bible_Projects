"""Pull the held items for #1993 (researcher 2026-10-09: complete the accumulating outstanding items).
OT-95 jealousy verses, OT-96 tov verses, OT-15 H2552 hits, #1942 H5782 inner-being hits (unit 4 sec E) and LD-149/LD-155.
Each verse with its passage (2 either side), ESV, iba.db read-only. Output: m18-held-items-passages-v1-20261009.md (data only).
"""
import os, sqlite3
HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
OUT = os.path.join(HERE, 'm18-held-items-passages-v1-20261009.md')

def hits(strong):
    return [r[0] for r in c.execute("""select distinct v.reference from verse_lexical l join verse v on v.id=l.verse_id
        where l.deleted=0 and v.deleted=0 and l.strong like ? order by v.id""", (strong + '%',))]

groups = {
 'OT-95 jealousy (M18 x M47, and M25 Isa 42:13)': ['1Ki 19:10', '1Ki 19:14', 'Eze 36:5', 'Jam 3:14', 'Jam 4:5', 'Num 11:29', 'Pro 23:17', 'Eze 8:3', 'Psa 73:3', 'Isa 42:13'],
 'OT-96 tov (M18 x M47)': ['Isa 38:3', '2Ki 20:3', 'Gen 1:21', 'Ecc 7:26', 'Lam 3:25', 'Psa 73:1', 'Psa 125:4', '2Ch 19:3', 'Pro 14:14', 'Jos 23:14'],
 'OT-15 H2552 to warm': hits('H2552'),
 '#1942 H5782 i) God stirring up / roused': ['Psa 7:6', 'Psa 35:23', 'Psa 44:23', 'Psa 59:4', 'Psa 80:2', 'Isa 51:9', 'Zec 2:13', 'Isa 42:13', 'Psa 73:20', 'Job 8:6'],
 '#1942 H5782 ii) God stirring up others against people': ['2Ch 21:16', 'Jer 51:1', 'Jer 51:11', '1Ch 5:26', 'Eze 23:22', 'Isa 13:17', 'Jer 50:9', 'Joe 3:7', 'Zec 9:13', 'Isa 41:2', 'Isa 41:25'],
 '#1942 H5782 God stirring a spirit toward good': ['Ezr 1:1', 'Ezr 1:5', '2Ch 36:22', 'Hag 1:14', 'Isa 45:13'],
 '#1942 H5782 iii) the inner being stirred': ['Isa 51:17', 'Isa 52:1', 'Isa 64:7', 'Song 5:2', 'Song 2:7', 'Song 3:5', 'Song 8:4', 'Song 8:5', 'Pro 10:12', 'Job 17:8', 'Job 31:29', 'Dan 11:25', 'Isa 50:4', 'Psa 57:8', 'Judg 5:12', 'Zec 4:1'],
 '#1942 LD-155 H6974 waking in the inner being': ['Pro 23:35', 'Isa 29:8', 'Joe 1:5', 'Pro 6:22'],
}

def passage(ref):
    bk, cv = ref.rsplit(' ', 1); ch, v = map(int, cv.split(':'))
    out = []
    for n in range(v - 2, v + 3):
        r = c.execute('SELECT text FROM verse WHERE reference = ? AND deleted = 0', (f'{bk} {ch}:{n}',)).fetchone()
        if r: out.append(('**' if n == v else '') + f'{ch}:{n} {r[0]}' + ('**' if n == v else ''))
    return out

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('# Held items: passages (data only)\n\n**Date:** 2026-10-09 · **Escalation:** #1993, #1942 · built by `m18-held-items-pull-v1-20261009.py`.\n\n')
    for g, refs in groups.items():
        f.write(f'## {g} ({len(refs)})\n\n')
        for r in refs:
            f.write(f'### {r}\n')
            for p in passage(r): f.write(f'> {p}\n')
            f.write('\n')
        print(len(refs), g)
