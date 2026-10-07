"""#1978, 2026-10-07: reading placement for the M64 "choose" pull (H0977, G0830, H7148, G0140, G4401).
Each verse in m64-choose-verses-v1-20261007.csv is placed in ONE group by who chooses and what is chosen,
as the verse itself states it. Verses that also carry a second object are noted in `also`.
Asserts every pulled verse is placed exactly once, then writes m64-choose-reading-v1-20261007.csv.
"""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'm64-choose-verses-v1-20261007.csv')
OUT = os.path.join(HERE, 'm64-choose-reading-v1-20261007.csv')

GROUPS = {
    'God chooses a place for his name': (
        'Deu 12:5,Deu 12:11,Deu 12:14,Deu 12:18,Deu 12:21,Deu 12:26,Deu 14:23,Deu 14:24,Deu 14:25,Deu 15:20,'
        'Deu 16:2,Deu 16:6,Deu 16:7,Deu 16:11,Deu 16:15,Deu 16:16,Deu 17:8,Deu 17:10,Deu 18:6,Deu 26:2,Deu 31:11,'
        'Jos 9:27,1Ki 8:16,1Ki 8:44,1Ki 8:48,1Ki 11:13,1Ki 11:32,1Ki 11:36,1Ki 14:21,2Ki 21:7,2Ki 23:27,'
        '2Ch 6:5,2Ch 6:6,2Ch 6:34,2Ch 6:38,2Ch 7:12,2Ch 7:16,2Ch 12:13,2Ch 33:7,Neh 1:9,Psa 132:13,'
        'Zec 1:17,Zec 2:12,Zec 3:2'),
    'God chooses a people': (
        'Deu 4:37,Deu 7:6,Deu 7:7,Deu 10:15,Deu 14:2,1Ki 3:8,Psa 33:12,Psa 47:4,Psa 78:67,Psa 78:68,Psa 135:4,'
        'Isa 14:1,Isa 41:8,Isa 41:9,Isa 43:10,Isa 44:1,Isa 44:2,Jer 33:24,Eze 20:5'),
    'God chooses a person for a task or office': (
        'Num 16:5,Num 16:7,Num 17:5,Deu 17:15,Deu 18:5,Deu 21:5,1Sa 2:28,1Sa 10:24,1Sa 16:8,1Sa 16:9,1Sa 16:10,'
        '2Sa 6:21,1Ki 11:34,1Ch 15:2,1Ch 28:4,1Ch 28:5,1Ch 28:6,1Ch 28:10,1Ch 29:1,2Ch 29:11,Neh 9:7,Psa 65:4,'
        'Psa 78:70,Psa 89:19,Psa 105:26,Isa 49:7,Hag 2:23,Mat 12:18,Act 10:41'),
    'God chooses what he wants (a fast, a response, whom he appoints)': (
        'Isa 58:5,Isa 58:6,Isa 66:4,Pro 21:3,Jer 49:19,Jer 50:44'),
    'God tries (ESV "tried")': 'Isa 48:10',
    'God sets a choice before a person': '2Sa 24:12,1Ch 21:10',
    'A person chooses the Lord, life, his ways, the good': (
        'Deu 30:19,Jos 24:15,Jos 24:22,Psa 25:12,Psa 84:10,Psa 119:30,Psa 119:173,Job 34:4,Isa 7:15,Isa 7:16,'
        'Isa 56:4'),
    'A person chooses other gods, their own ways, what God does not delight in': (
        'Judg 5:8,Judg 10:14,Isa 1:29,Isa 40:20,Isa 41:24,Isa 65:12,Isa 66:3,Pro 1:29,Pro 3:31,Job 15:5,Job 36:21'),
    'A person chooses death rather than life': 'Job 7:15,Jer 8:3',
    'A person chooses a king or takes a side': '1Sa 8:18,1Sa 12:13,1Sa 20:30,2Sa 16:18',
    "A person's own decision, desire or accord": (
        '2Sa 15:15,2Sa 19:38,Job 9:14,Job 29:25,Job 34:33,Deu 23:16,2Cor 8:3,2Cor 8:17'),
    'Men selected (for battle or leadership)': (
        'Exo 14:7,Exo 17:9,Exo 18:25,Num 16:2,Num 26:9,Jos 8:3,Judg 20:15,Judg 20:16,Judg 20:34,1Sa 13:2,1Sa 24:2,'
        '1Sa 26:2,2Sa 6:1,2Sa 10:9,2Sa 17:1,1Ki 12:21,1Ch 19:10,2Ch 11:1,2Ch 13:3,2Ch 13:17,2Ch 25:5'),
    'A thing chosen for oneself by sight or use': 'Gen 6:2,Gen 13:11,1Sa 17:40,1Ki 18:23,1Ki 18:25',
    '"Choice": the best, preferred over': 'Pro 8:10,Pro 8:19,Pro 10:20,Pro 16:16,Pro 22:1,Song 5:15',
}
ALSO = {
    '1Ki 8:16': 'also God chooses a person (David)',
    '2Ch 6:5': 'also God chooses (no) man as prince',
    '2Ch 6:6': 'also God chooses a person (David)',
    '1Ch 28:4': 'also God chooses a tribe (Judah)',
    'Psa 78:68': 'also a place (Mount Zion)',
    'Isa 66:4': 'also a person chooses what God does not delight in (second hit)',
    '2Ki 23:27': 'God casts off the city he chose',
    'Psa 78:67': 'God did not choose (Ephraim)',
    'Jer 33:24': "people say the Lord rejected the clans he chose",
    '1Sa 16:8': 'not chosen', '1Sa 16:9': 'not chosen', '1Sa 16:10': 'not chosen',
    '1Sa 12:13': 'also the Lord has set a king over you',
    '2Sa 16:18': 'the Lord, the people and the men of Israel all choose',
    'Isa 40:20': 'chooses wood for an idol',
}


def main():
    place = {}
    for g, refs in GROUPS.items():
        for ref in (x.strip() for x in refs.split(',')):
            assert ref not in place, f'{ref} placed twice ({place[ref]} / {g})'
            place[ref] = g
    rows = list(csv.DictReader(open(SRC, encoding='utf-8-sig')))
    pulled = {r['reference'] for r in rows}
    missing, extra = pulled - set(place), set(place) - pulled
    assert not missing and not extra, f'unplaced: {sorted(missing)}; not in pull: {sorted(extra)}'
    cols = ['reference', 'group', 'also', 'hit_words', 'other_m_words', 'narrative_refs', 'esv_text']
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            r['group'] = place[r['reference']]
            r['also'] = ALSO.get(r['reference'], '')
            w.writerow(r)
    from collections import Counter
    for g, n in Counter(place.values()).items():
        print(f'{n:4}  {g}')
    print(f'{len(rows)} verses placed -> {OUT}')


if __name__ == '__main__':
    main()
