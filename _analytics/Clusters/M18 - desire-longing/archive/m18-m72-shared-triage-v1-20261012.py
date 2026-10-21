"""Role triage of the M18 x M72 shared verses (#1993, handoff v7 item H). Rule 73, triage order GOVERNANCE.md §91.

Input: m18-m72-shared-crossref-v1-20261012.csv (m18-m72-shared-pull-v1 + crossref v3). The 131 verses with an earlier
M18 decision keep it (decision 'decided earlier'). The 51 with none get the decision below; the readings are in
m18-m72-shared-reading-v1-20261012.md. Nothing is woven.

decision: read (the M18 word carries the account the verse belongs to) · carried (already placed by its operation)
          · no-carrier (the act has no M-code in the verse; read by its act) · forward (the M18 word qualifies another
          cluster's characteristic; marked forward, OT-98) · data
Usage: python m18-m72-shared-triage-v1-20261012.py
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
INP = os.path.join(HERE, 'm18-m72-shared-crossref-v1-20261012.csv')
OUT = os.path.join(HERE, 'm18-m72-shared-triage-v1-20261012.csv')

# reference: (m18_role, m72_role, decision, home_or_forward, route, note)
D = {
    'Neh 2:5': ('measure', "standalone: the one whose pleasure decides", 'read', '10.7 Whose measure', 'B', "asked under the king's pleasure, after prayer (2:4)"),
    'Neh 2:7': ('measure', 'standalone', 'read', '10.7 Whose measure', 'B', 'second ask; granted "for the good hand of my God" (2:8)'),
    'Est 1:19': ('measure; "better" qualifies a person', 'standalone', 'read', '10.7 Whose measure', 'B', "counsel framed by the king's pleasure, grounded in fear of contempt (1:17-18)"),
    'Est 5:4': ('measure', 'standalone', 'read', '10.7 Whose measure', 'B', 'asks under his pleasure after he has offered half the kingdom (5:3)'),
    'Est 9:13': ('measure', 'standalone', 'read', '10.7 Whose measure', 'B', 'asks again under his pleasure; the king grants (9:14)'),
    'Mal 3:1': ("characteristic: the people's delight", 'qualifier: names the speaker (Lord of hosts)', 'read', '10.7 (beside Isa 58:2); 13.1', 'A, B', 'delight in the one they demanded (2:17); "who can endure" (3:2)'),
    'Est 3:9': ('measure', 'standalone', 'carried', '10.7 Whose measure', 'B', 'already the case "Another\'s will, given the whole decision"'),
    'Neh 1:11': ('measure of fear', 'standalone', 'carried', '10.9 Fear before God', 'B', '"delight to fear your name" already read as fear with delight'),
    '1Sa 19:4': ('qualifier of speech and deeds', 'standalone', 'carried', '10.10 Loyalty and honour', 'B', ''),
    '2Ch 21:13': ('qualifier: "better than you"', 'standalone', 'carried', '13.1 Stirring (in range)', 'A, B', ''),
    'Est 1:11': ('qualifier of a person', 'standalone', 'carried', '10.1 How a feeling rises; Ch 11 §2', 'B', ''),
    '2Ki 10:3': ('qualifier: "best"', 'standalone', 'carried', '10.7 Whose measure; 10.12 (by 10:4-5)', 'B', 'the taunt; the answer (10:4-5) is placed'),
    '2Sa 15:3': ('qualifier: a verdict given to win favour', 'standalone', 'carried', 'Ch 11 §1 (by 15:6)', 'B', 'the words by which hearts were stolen; propose adding them where 15:6 stands'),
    'Gen 1:18': ("characteristic of God's seeing", 'qualifier: what the lights do', 'carried', '10.6 Through the eye -> 13.4 (by Gen 1:21, 25, 31)', 'A', 'same formula as the verses already noted'),
    '2Sa 11:2': ('qualifier of the one seen', "setting: the king's house; the power to send", 'no-carrier', '10.6 Coveting', 'B', 'saw, inquired, sent, took (11:2-4); no desire word in the verses'),
    '2Sa 18:27': ('qualifier of man and news', 'standalone', 'no-carrier', '10.6 Wanting speaks, and drives thinking', 'B', 'the king reads the runner as good news; his question is Absalom (18:29)'),
    '2Ki 20:13': ('qualifier of things shown', 'qualifier: the whole realm', 'no-carrier', '10.11', 'B', 'shows everything; pointer 2Ch 32:31'),
    'Isa 39:2': ('qualifier of things shown', 'qualifier: the whole realm', 'no-carrier', '10.11 (with 2Ki 20:13)', 'B', 'parallel; "gladly"'),
    'Jer 44:17': ('ground: "prospered"', 'standalone: kings and officials of the past', 'no-carrier', '10.2 (beside "we will not listen", 44:16)', 'B', 'prosperity read as proof of the offerings (44:17-18)'),
    'Gen 40:16': ('qualifier of the interpretation', 'standalone', 'no-carrier', '10.5', 'B', "he spoke when he saw the other's outcome was good"),
    '1Ki 2:38': ('assent', 'standalone', 'no-carrier', '10.5 The oath', 'B', 'agrees; breaks it (2:39-43, "not kept your oath to the Lord")'),
    'Amo 6:2': ('comparison: "better"', 'qualifier: other kingdoms', 'no-carrier', '10.4 (beside Amos 6:1)', 'B', 'the comparison puts the at-ease to the question'),
    'Gen 31:29': ('merism: "good or bad"', 'characteristic: power to harm', 'forward', 'M72; M58', 'A, B', "power held back by God's word in a dream (31:24)"),
    '1Ki 22:8': ('ground: what he wants to hear', 'standalone', 'forward', 'M06; M43', 'B', 'hates the prophet who never says good of him'),
    '1Ki 22:18': ('ground', 'standalone', 'forward', 'M43; M06', 'B', 'same, after the word'),
    '2Ch 18:17': ('ground', 'standalone', 'forward', 'M43; M06', 'B', 'parallel of 1Ki 22:18'),
    '1Ki 22:13': ('measure of the speech asked for', 'standalone', 'forward', 'M65; M43', 'B', 'pressed to speak favourably; refuses (22:14)'),
    '2Ch 18:12': ('measure of the speech asked for', 'standalone', 'forward', 'M65; M43', 'B', 'parallel of 1Ki 22:13'),
    'Ezr 7:9': ("qualifier of God's hand", "characteristic: God's hand on a person", 'forward', 'M72', 'A, B', 'pointer 7:10 (set his heart)'),
    'Ezr 8:18': ("qualifier of God's hand", 'characteristic', 'forward', 'M72', 'A, B', ''),
    'Neh 2:8': ("qualifier of God's hand", "characteristic; the king's grant", 'forward', 'M72', 'A, B', "the grant named as God's hand, after 1:11 and 2:4"),
    'Neh 2:18': ("qualifier of God's hand; \"good work\"", 'characteristic', 'forward', 'M72; M23', 'A, B', 'told, and they "strengthened their hands"'),
    '1Sa 15:28': ('qualifier: "better than you"', 'characteristic: the kingdom torn and given', 'forward', 'M72', 'A, B', 'after "you have rejected the word" (15:26)'),
    'Isa 52:7': ('qualifier of the news', 'characteristic: "Your God reigns"', 'forward', 'M70; M72', 'A, B', ''),
    'Ecc 4:13': ('comparison', 'standalone', 'forward', 'M16; M15', 'B', 'a king who no longer knew how to take advice'),
    'Jer 22:15': ('qualifier: "it was well"', 'standalone: what makes a king', 'forward', 'M12', 'A, B', '"Is not this to know me?" (22:16)'),
    '1Ki 2:32': ('comparison', 'standalone', 'forward', 'M12', 'B', ''),
    '2Ch 19:11': ('qualifier of persons', 'standalone', 'forward', 'M23', 'B', 'pointer 19:9 (fear, faithfulness, whole heart)'),
    'Judg 11:25': ('comparison', 'standalone', 'forward', 'M26', 'B', ''),
    'Est 8:17': ('qualifier of the feast', 'standalone', 'forward', 'M04; M01', 'B', ''),
    'Jer 33:11': ('characteristic of God, in the song', 'qualifier: the name', 'forward', 'M49', 'A, B', '"for the Lord is good"'),
    'Zec 8:19': ('qualifier of feasts', 'qualifier: the name', 'forward', 'M04', 'A, B', 'fasts turned to feasts; "love truth and peace"'),
    'Est 2:9': ('qualifier of a place', 'standalone', 'forward', 'M50; M05', 'B', ''),
    'Dan 1:4': ('qualifier of appearance', 'standalone', 'forward', 'M16; M15', 'B', ''),
    'Exo 3:8': ('qualifier of a land', 'qualifier: hand of the Egyptians', 'forward', 'M45', 'A', 'pointer 3:7 (I know their sufferings)'),
    'Gen 41:35': ('qualifier of years', 'qualifier', 'data', '', 'C', ''),
    'Isa 5:9': ('qualifier of houses', 'qualifier: the name', 'data', '', 'C', 'the woe is in 5:8'),
    'Est 2:2': ('qualifier of persons sought', 'standalone', 'data', '', 'C', 'pointer Est 2:1, 2:4'),
    'Est 2:3': ('qualifier of persons sought', 'standalone', 'data', '', 'C', ''),
    'Est 7:9': ('qualifier of a word spoken', 'standalone', 'data', '', 'C', "the king's wrath (7:7, 10) is the passage's act"),
    '1Ki 2:18': ('assent', 'standalone', 'data', '', 'C', 'pointer 1Ki 2:15 for M72 ("the kingdom was mine")'),
}

rows = list(csv.DictReader(open(INP, encoding='utf-8-sig')))
out = []
for r in rows:
    ref = r['reference']
    if r['m18_decisions']:
        assert ref not in D, ref
        rec = ('', '', 'decided earlier', r['m18_decisions'], '', '')
    else:
        rec = D[ref]
    out.append({'reference': ref, 'm18_role': rec[0], 'm72_role': rec[1], 'decision': rec[2], 'home_or_forward': rec[3],
                'route': rec[4], 'note': rec[5], 'm18_words': r['m18_words'], 'm72_words': r['m72_words'],
                'other_mcodes': r['other_mcodes'], 'narrative_refs': r['narrative_refs'], 'text': r['text']})
missing = set(D) - {r['reference'] for r in rows}
assert not missing, missing
with open(OUT, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)
print(len(out), '->', OUT)
print(Counter(r['decision'] for r in out))
