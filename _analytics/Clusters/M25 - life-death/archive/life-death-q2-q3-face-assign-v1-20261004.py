"""Faces for the Q2 (soul and spirit with death) and Q3 (heart with death) focused pulls, 2026-10-04.
Every verse named by reading; where two hits in one verse read differently, the override is by
(reference, Strong's prefix). Refuses to write if a hit is unfaced or an assignment matches no hit.
Usage (from this folder): python life-death-q2-q3-face-assign-v1-20261004.py
then, from the repo root, merge each with strand-unit-pull-v1-20261002.py <pull.csv> --faces <faces.csv>
"""
import csv, sys
from collections import Counter

Q2_NAMES = {
    'S01': 'The soul departs', 'S02': 'The spirit and breath at death',
    'S03': 'The soul dies, or asks to die', 'S04': 'The soul near death, or brought to it',
    'S05': 'The soul delivered from death while living', 'S06': 'The soul beyond death',
    'S07': 'Spirit and life set against death', 'S08': 'The soul as a dead body',
    'S09': "Sheol's and death's appetite", 'S10': 'Life sought, risked or taken (law and narrative)',
    'S11': 'Not the inner being',
}
Q2 = {
    'S01': ['Gen 35:18'],
    'S02': ['Luk 23:46', 'Ecc 8:8', 'Psa 104:29', 'Jam 2:26', 'Gen 6:17', 'Gen 7:22', 'Ecc 3:19'],
    'S03': ['Num 23:10', 'Judg 16:30', 'Eze 18:4', 'Eze 18:20', 'Jon 4:8', '1Ki 19:4', 'Jon 4:3', 'Job 7:15',
            'Num 21:5', 'Job 36:14', 'Job 21:25'],
    'S04': ['Isa 53:12', 'Mat 26:38', 'Mar 14:34', 'Judg 16:16', 'Psa 88:3', 'Psa 107:18', 'Job 33:22',
            'Psa 143:3', '2Sa 1:9', '1Sa 20:3', 'Pro 8:36', '1Sa 2:33', 'Gen 27:4'],
    'S05': ['Psa 30:3', 'Psa 33:19', 'Psa 56:13', 'Psa 86:13', 'Psa 116:8', 'Jos 2:13', 'Job 33:18', 'Job 33:28',
            'Job 33:30', 'Isa 38:17', 'Jam 5:20', 'Pro 23:14', 'Eze 3:19', 'Eze 33:9', 'Psa 89:48', 'Gen 19:19',
            'Pro 19:16'],
    'S06': ['Psa 49:15', 'Psa 16:10', 'Act 2:27', 'Act 2:31'],
    'S07': ['Rom 8:2', 'Rom 8:6', 'Rom 8:10', 'Rom 8:11', 'Rom 8:13', 'Rom 7:6', 'Rom 1:4', 'Heb 9:14', '1Pe 4:6',
            'Eze 18:31', 'Rev 14:13', 'Rev 2:11', 'Rev 3:1', 'Luk 2:26'],
    'S08': ['Lev 21:11', 'Num 6:6', 'Num 19:11', 'Num 19:13', 'Num 19:18'],
    'S09': ['Isa 5:14', 'Hab 2:5'],
    'S10': ['Deu 19:6', 'Deu 19:11', 'Deu 22:26', 'Deu 24:7', 'Num 35:30', 'Num 35:31', 'Lev 24:17', 'Exo 31:14',
            'Jos 2:14', 'Jos 20:9', 'Judg 5:18', '1Sa 19:5', '1Sa 19:11', '1Sa 28:9', '2Sa 14:7', 'Jer 11:21',
            'Jer 21:9', 'Jer 38:2', 'Jer 26:19', 'Jer 38:16', 'Exo 4:19', 'Mat 2:20', 'Phili 2:30', 'Rev 12:11',
            'Psa 35:7', 'Psa 78:50', 'Eze 13:19', '2Sa 14:14', 'Lam 1:19'],
    'S11': ['Eze 5:12', 'Job 1:19', 'Isa 11:4', 'Rev 8:9', 'Rev 16:3', 'Gen 23:8', 'Lev 26:30', 'Pro 19:18'],
}
Q2_OVERRIDE = {('Jon 4:8', 'H7307'): 'S11'}   # the scorching east wind; the nephesh hit stays S03

Q3_NAMES = {
    'H01': 'The heart in anguish before death', 'H02': 'The heart at the moment of death',
    'H03': 'The heart dies before the body', 'H04': 'The heart while living, then the dead',
    'H05': 'The heart and the way to death', 'H06': 'Believing in the heart the raising from the dead',
    'H07': 'The heart searched, and death as judgment', 'H08': 'Love strong as death, set on the heart',
    'H09': 'The heart in narratives of killing (data)', 'H10': 'Idiom: the heart of the seas',
}
Q3 = {
    'H01': ['Psa 55:4', 'Lam 1:20', 'Act 21:13'], 'H02': ['1Sa 4:20'], 'H03': ['1Sa 25:37', 'Psa 31:12'],
    'H04': ['Ecc 9:3'], 'H05': ['Pro 10:21', 'Eze 18:31', 'Ecc 7:26'], 'H06': ['Rom 10:9'], 'H07': ['Rev 2:23'],
    'H08': ['Song 8:6'],
    'H09': ['Deu 19:6', '2Sa 13:28', '2Sa 13:33', '2Sa 18:3', '2Ch 22:9', 'Exo 9:7', 'Psa 109:16'],
    'H10': ['Eze 28:8'],
}

def run(pull, out, faces, names, override):
    by_ref = {}
    for f, refs in faces.items():
        for r in refs:
            assert r not in by_ref, r
            by_ref[r] = f
    rows = list(csv.DictReader(open(pull, encoding='utf-8')))
    used, res, missing = set(), [], []
    for r in rows:
        f = override.get((r['reference'], r['strong'][:5])) or by_ref.get(r['reference'])
        if f is None:
            missing.append(r['reference']); continue
        used.add(r['reference'])
        res.append({'reference': r['reference'], 'position': r['position'], 'face': f, 'face_name': names[f]})
    unused = set(by_ref) - used
    if missing or unused:
        sys.exit(f'{pull}: unfaced {missing}; unmatched {sorted(unused)}')
    with open(out, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['reference', 'position', 'face', 'face_name']); w.writeheader(); w.writerows(res)
    print(pull, len(res), 'hits faced;', dict(sorted(Counter(x['face'] for x in res).items())))

run('life-death-q2-soul-spirit-death-pull-v1-20261004.csv', 'life-death-q2-faces-v1-20261004.csv', Q2, Q2_NAMES, Q2_OVERRIDE)
run('life-death-q3-heart-death-pull-v1-20261004.csv', 'life-death-q3-faces-v1-20261004.csv', Q3, Q3_NAMES, {})
