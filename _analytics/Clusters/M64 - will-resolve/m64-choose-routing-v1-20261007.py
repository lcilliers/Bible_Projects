"""#1978 / cfg_behaviour_rule 72, 2026-10-07: route every verse of the M64 "choose" reading.
Researcher: "proceed to revise the choose reading work to isolate all the verses that will be captured in Ch13".

Routes (GOVERNANCE.md s90):
  A    another being in its own right -> Ch 13 (13.1 Divine, 13.2 Angels, 13.3 Other spirits, 13.4 Nature)
  B    the human inner being (incl. another being acting with it)
  A+B  both, described from different angles
  C    no inner-being and no other-being bearing: analysis only, not narrative
Basis used (stated in the md, for the researcher to correct):
  - a verse where God (or the Lord, Jesus) chooses, or where "chosen/elect" names those God chose, is A (13.1);
  - it is also B when the verse itself names a human inner activity or state (rejoice, fear, desire, know, believe,
    hear/listen, pray, repent, love, despise, be strong/careful, humble, and the like) -- noted in route_basis;
  - a verse where a person chooses is B; it is also A when the verse states God's own act or verdict;
  - "chosen men/chariots", "choice silver/cedars" used as a mark of quality, with no act of choosing and no inner
    bearing in the verse, is C.
Reads m64-choose-reading-v2-20261007.csv (no DB query, rule 71); writes m64-choose-reading-v3-20261007.csv.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'archive', 'm64-choose-reading-v2-20261007.csv')  # the placement (v2), archived once v3 was made
OUT = os.path.join(HERE, 'm64-choose-reading-v3-20261007.csv')

GOD_GROUPS = {
    'God chooses a place for his name', 'God chooses a people', 'The chosen / the elect (NT)',
    'God chooses the foolish, weak, low and poor', 'Jesus chooses', 'God chooses a person for a task or office',
    'God chooses what he wants (a fast, a response, whom he appoints)', 'God tries (ESV "tried")',
    'God sets a choice before a person',
}

# God-verses that are also B: the human inner element the verse names
ALSO_B = {
    'Deu 12:18': 'rejoice', 'Deu 12:21': 'whenever you desire', 'Deu 14:23': 'learn to fear the Lord',
    'Deu 16:11': 'rejoice', 'Deu 16:15': 'altogether joyful', 'Deu 17:10': 'be careful to do',
    'Deu 18:6': 'when he desires', 'Deu 31:11': 'read the law in their hearing',
    '1Ki 8:44': 'pray', '1Ki 8:48': 'repent with all their heart and soul, pray', '2Ch 6:34': 'pray',
    '2Ch 6:38': 'repent with all their heart and soul, pray', '2Ch 7:12': 'I have heard your prayer',
    'Neh 1:9': 'return to me and keep my commandments',
    'Psa 105:43': 'joy, singing', 'Psa 106:5': 'rejoice, glory', 'Isa 43:10': 'know, believe, understand',
    'Isa 44:1': 'hear', 'Isa 44:2': 'fear not', 'Isa 45:4': 'though you do not know me',
    'Isa 65:15': 'leave your name for a curse', 'Isa 65:22': 'long enjoy the work of their hands',
    'Jer 33:24': 'despised my people',
    'Eph 1:4': 'holy and blameless before him, in love', 'Col 3:12': 'compassionate hearts, kindness, humility',
    '2Pe 1:10': 'be diligent to confirm', 'Luk 18:7': 'cry to him day and night',
    '1Th 1:4': 'we know, loved by God', '2Th 2:13': 'belief in the truth', 'Tit 1:1': 'faith, knowledge of the truth',
    'Mat 24:24': 'lead astray', 'Mar 13:22': 'lead astray', '2Ti 2:10': 'I endure everything',
    'Rom 11:7': 'the rest were hardened', 'Rom 11:28': 'enemies, beloved', '1Pe 2:9': 'proclaim his excellencies',
    'Rev 17:14': 'faithful', '2Jo 1': 'whom I love in truth', 'Jam 2:5': 'rich in faith, those who love him',
    'Num 17:5': 'grumblings', '1Sa 10:24': 'the people shouted', '2Sa 6:21': 'I will celebrate',
    '1Ki 11:34': 'kept my commandments', '1Ch 28:10': 'be careful, be strong', '1Ch 29:1': 'young and inexperienced',
    '2Ch 29:11': 'do not be negligent', 'Psa 65:4': 'satisfied with the goodness of your house',
    'Isa 49:7': 'deeply despised, abhorred', '2Sa 21:6': 'the Gibeonites demand his sons',
    'Psa 106:23': 'stood in the breach', 'Luk 9:35': 'listen to him', 'Luk 23:35': 'the rulers scoffed',
    'Act 1:24': 'who know the hearts of all; they prayed', 'Act 15:7': 'hear and believe',
    '1Pe 2:4': 'rejected by men; as you come to him', '1Pe 2:6': 'whoever believes, not put to shame',
    'Isa 58:5': 'humble himself', 'Isa 66:4': 'no one answered, did not listen',
    '2Sa 24:12': 'choose one of them', '1Ch 21:10': 'choose one of them', 'Isa 48:10': 'the furnace of affliction',
    'Luk 6:13': 'he called his disciples', 'Joh 6:70': 'one of you is a devil',
    'Joh 13:18': 'lifted his heel against me', 'Joh 15:16': 'you did not choose me; bear fruit, ask',
    'Joh 15:19': 'the world hates you',
}
# person-verses that are also A: God's own act or verdict stated in the verse
ALSO_A = {
    'Deu 30:19': 'I have set before you', '1Sa 8:18': 'the Lord will not answer you',
    '1Sa 12:13': 'the Lord has set a king over you', '2Sa 16:18': 'whom the Lord ... has chosen',
    'Psa 25:12': 'him will he instruct', 'Isa 56:4': 'the things that please me',
    'Isa 65:12': 'I will destine you to the sword; what I did not delight in', 'Judg 10:14': 'go and cry out to the gods',
    'Isa 41:24': 'you are nothing ... an abomination is he who chooses you',
}
ROUTE_C = {
    'Exo 14:7': 'chosen chariots', 'Judg 20:15': 'chosen men', 'Judg 20:16': 'chosen men', 'Judg 20:34': 'chosen men',
    '1Sa 24:2': 'chosen men', '1Sa 26:2': 'chosen men', '2Sa 6:1': 'chosen men', '1Ki 12:21': 'chosen warriors',
    '2Ch 11:1': 'chosen warriors', '2Ch 13:3': 'chosen men', '2Ch 13:17': 'chosen men', '2Ch 25:5': 'choice men',
    'Song 5:15': 'choice as the cedars', 'Pro 8:19': 'choice silver',
}
EXTRA_SECTIONS = {
    'Zec 3:2': '13.3 (Satan rebuked)', '1Ti 5:21': '13.2 (the elect angels)', 'Mat 24:31': '13.2 (he will send out his angels)',
    'Mar 13:27': '13.2 (he will send out the angels)', 'Isa 43:20': '13.4 (the wild beasts will honor me)',
}
FLAGS = {
    'Gen 6:2': 'who are "the sons of God"? The verse does not say. A (13.2/13.3) or B only?',
    'Luk 6:13': 'Jesus choosing: 13.1 Divine, or the human inner being of Jesus, or both?',
    'Joh 6:70': 'Jesus choosing; and "one of you is a devil": 13.3?',
    'Joh 13:18': 'Jesus choosing: 13.1 Divine, human, or both?', 'Joh 15:16': 'Jesus choosing: 13.1 Divine, human, or both?',
    'Joh 15:19': 'Jesus choosing: 13.1 Divine, human, or both?', 'Act 1:2': 'Jesus choosing: 13.1 Divine, human, or both?',
    'Judg 5:8': 'gods chosen: do chosen gods/idols belong in 13.3 Other spirits?',
    'Judg 10:14': 'gods chosen: do chosen gods/idols belong in 13.3 Other spirits?',
    'Jos 24:15': 'gods chosen: do chosen gods/idols belong in 13.3 Other spirits?',
    'Isa 41:24': 'God addresses the idols ("you are nothing"): 13.3?',
    'Isa 40:20': 'an idol chosen and made: 13.3?',
    'Jer 49:19': 'God likens himself to a lion: is a simile from nature 13.4?',
    'Jer 50:44': 'God likens himself to a lion: is a simile from nature 13.4?',
}


def main():
    rows = list(csv.DictReader(open(SRC, encoding='utf-8-sig')))
    refs = {r['reference'] for r in rows}
    for d in (ALSO_B, ALSO_A, ROUTE_C, EXTRA_SECTIONS, FLAGS):
        bad = set(d) - refs
        assert not bad, f'not in the pull: {sorted(bad)}'
    for r in rows:
        ref, god = r['reference'], r['group'] in GOD_GROUPS
        assert not (god and ref in ROUTE_C) and not (god and ref in ALSO_A) and not (not god and ref in ALSO_B), ref
        if ref in ROUTE_C:
            route, basis = 'C', f'quality, no act of choosing: "{ROUTE_C[ref]}"'
        elif god:
            route = 'A+B' if ref in ALSO_B else 'A'
            basis = 'God chooses' + (f'; inner: {ALSO_B[ref]}' if ref in ALSO_B else '')
        else:
            route = 'A+B' if ref in ALSO_A else 'B'
            basis = 'a person chooses' + (f'; God: {ALSO_A[ref]}' if ref in ALSO_A else '')
        secs = []
        if 'A' in route:
            secs.append('13.1')
        if ref in EXTRA_SECTIONS:
            secs.append(EXTRA_SECTIONS[ref])
        r['route'], r['ch13_sections'], r['route_basis'], r['flag'] = route, '; '.join(secs), basis, FLAGS.get(ref, '')
    cols = ['reference', 'group', 'route', 'ch13_sections', 'route_basis', 'flag', 'also', 'hit_words',
            'other_m_words', 'narrative_refs', 'esv_text']
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)
    print(Counter(r['route'] for r in rows), '| Ch 13:', sum('A' in r['route'] for r in rows),
          '| flagged:', sum(bool(r['flag']) for r in rows), '->', OUT)
    for g in sorted({r['group'] for r in rows}):
        print(f'  {g}:', dict(Counter(r['route'] for r in rows if r['group'] == g)))


if __name__ == '__main__':
    main()
