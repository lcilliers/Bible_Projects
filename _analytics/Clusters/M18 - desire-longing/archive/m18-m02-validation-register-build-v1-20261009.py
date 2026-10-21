"""Register of the M18 x M02 read-back (#1993, handoff item C; OT-19): one decision per verse, with its reason.

Input: m18-shared-m47-m25-m02-crossref-v2-20261009.csv (M02 rows without M47 or M25: 51), read beside the M25 ledgers
in m18-m02-validation-worksheet-v1-20261009.md. Output: m18-m02-validation-register-v1-20261009.csv.
Decisions: a = missed, add; b = new perspective, add; c = error, realign; confirmed; carried (by a parallel);
held (named thread); route C (no inner-being bearing for the M18 word). 'proposed_place' is a proposal only:
nothing is woven until the researcher instructs. 'ch2' marks a verse whose natural M25 place is Ch 2 (OT-08 hold).
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'm18-shared-m47-m25-m02-crossref-v2-20261009.csv')
OUT = os.path.join(HERE, 'm18-m02-validation-register-v1-20261009.csv')

D = {  # reference: (decision, proposed_place, ch2, reason)
 'Deu 6:15': ('confirmed', '10.13; 13.1 Jealousy', '', 'In 10.13. God’s jealousy beside anger, where other gods are set beside him (6:14). 13.1 Jealousy now points to it.'),
 'Deu 11:17': ('route C', '', '', '"the good land": tov qualifies the land. The anger and the land (AG-05) are in 10.13.'),
 'Deu 29:20': ('b', '13.1 Jealousy', '', 'In Ch 11 and 13.1 Willing (29:19-20). Not said: "the anger of the Lord and his jealousy will smoke against that man", the man who "blesses himself in his heart" (29:19).'),
 'Jos 23:16': ('route C', '', '', '"the good land": qualifier. 23:14-15 woven in 10.2 this session.'),
 'Eze 5:13': ('b', '13.1 Jealousy', '', 'In 10.13 four times. Not said: "that I have spoken in my jealousy"; its stated end is knowing ("they shall know that I am the Lord").'),
 'Deu 4:21': ('route C', '', '', '"the good land": qualifier. Moses’ exclusion "because of you" is in 10.13 (Deu 3:26).'),
 'Zep 3:8': ('a', '13.1 Jealousy', '', 'Not cited. "in the fire of my jealousy all the earth shall be consumed", and the next verse: "I will change the speech of the peoples to a pure speech, that all of them may call upon the name of the Lord" (3:9).'),
 'Mic 7:18': ('b', '13.1 Delight (what he delights in)', '', 'In 10.9. Not said in 13.1: "He does not retain his anger forever, because he delights in steadfast love". The ground of the anger’s end is his delight.'),
 'Psa 79:5': ('b', '13.1 Jealousy', '', 'In 10.13. Not said: "Will your jealousy burn like fire?", followed by "Pour out your anger on the nations" (79:6): asked to end on them and turn on others.'),
 '2Ch 12:12': ('confirmed', '10.13', '', 'In 10.13. "conditions were good in Judah": tov qualifier.'),
 'Pro 27:4': ('confirmed', '10.13; 10.6', '', 'In 10.13 and pointed to from 10.6 Jealousy and envy. Sound.'),
 'Lam 2:4': ('b', '10.6 Taken away', '', 'In 10.13 for the poured fury. Not said: "he has killed all who were delightful in our eyes", the Lord "like an enemy" (2:4-5).'),
 'Eze 16:38': ('a', '13.1 Jealousy', '', 'Not cited. "the blood of wrath and jealousy", in the setting of adultery (16:36-37).'),
 'Eze 36:6': ('confirmed', '13.1 Jealousy', '', 'Woven earlier today in 13.1 Jealousy with 36:5 (held items).'),
 'Nah 1:2': ('a', '13.1 Jealousy', '', 'Not cited. "The Lord is a jealous and avenging God ... and keeps wrath for his enemies", beside "The Lord is slow to anger" (1:3).'),
 'Zec 8:2': ('b', '13.1 Jealousy', '', 'In 10.13. Not said: "I am jealous for Zion with great jealousy", followed by "I have returned to Zion" (8:3).'),
 'Eze 16:42': ('b', '13.1 Jealousy', '', 'In 10.13. Not said: "my jealousy shall depart from you. I will be calm"; then "Because you have not remembered" (16:43).'),
 'Num 25:11': ('b', '10.6 Jealousy and envy', '', 'In 10.9 and 10.4. Not set beside Elijah: both jealous for God; Phinehas "jealous with my jealousy" turned back the wrath and was given "my covenant of peace" (25:12).'),
 'Eze 23:25': ('a', '13.1 Jealousy', '', 'Not cited. "I will direct my jealousy against you, that they may deal with you in fury": the lovers turned enemies carry it (23:22-24).'),
 '2Ki 5:12': ('a', '10.7 Whose measure', '', 'Not cited (5:11 in 10.1, 5:13 in 10.13). "Are not Abana and Pharpar ... better than all the waters of Israel?": his own measure set against the prophet’s word; his servants’ question turns him.'),
 'Pro 6:34': ('c', '10.1 When feeling changes character', '', 'In 10.1, 10.13, Ch 11. 10.1 said "Grief makes it tender; jealousy makes it hard" as if the verse said it; it is a reading. Restated with "I read" (test batch 4.5).'),
 'Deu 32:16': ('a', '13.1 Jealousy (what provokes it)', '', 'Not cited. "They stirred him to jealousy with strange gods"; Jeshurun "grew fat, and kicked" (32:15); "You were unmindful of the Rock that bore you" (32:18).'),
 '1Ki 14:15': ('route C', '', '', '"this good land": qualifier. The Asherim provoking is in 10.13.'),
 'Psa 78:58': ('a', '13.1 Jealousy (what provokes it)', '', 'Not cited. "they moved him to jealousy with their idols"; "When God heard, he was full of wrath" (78:59).'),
 'Deu 32:21': ('a', '13.1 Jealousy (answered in kind)', '', 'Not cited. "They have made me jealous with what is no god ... So I will make them jealous with those who are no people".'),
 'Psa 112:10': ('a', '10.6 Evil desire', '', 'Not cited. "The wicked man sees it and is angry; he gnashes his teeth and melts away; the desire of the wicked will perish!" Sight of another’s honour (112:9). No verse names envy here (anger ledger F.6), so it is placed under evil desire, not envy.'),
 '1Sa 20:7': ('confirmed', '10.10', '', 'In 10.10. "If he says, Good!": tov as the word of assent.'),
 'Psa 37:1': ('a', '10.6 Jealousy and envy', '', 'Not cited (37:7-8 are). "Fret not yourself because of evildoers; be not envious of wrongdoers!", answered by "they will soon fade" (37:2) and trust, delight, commit, be still (37:3-7). Test batch 4.6.'),
 'Pro 24:19': ('a', '10.6 Jealousy and envy', '', 'Not cited. "Fret not yourself because of evildoers, and be not envious of the wicked, for the evil man has no future" (24:19-20); after "Do not rejoice when your enemy falls" (24:17).'),
 'Pro 21:19': ('carried', '10.10 (Pro 21:9)', '', 'The quarrelsome wife proverb, carried by 21:9.'),
 'Job 6:2': ('a', '10.5 The pause between', '', 'Not narrated (the anger ledger listed it as in the chapters; a text search finds it nowhere). The M18 word is "calamity"; the verse weighs vexation: "heavier than the sand of the sea; therefore my words have been rash" (6:3).'),
 'Zec 7:14': ('route C', '', '', '"the pleasant land was made desolate": qualifier. The diamond-hard hearts (7:12) are in Ch 4.'),
 'Isa 60:10': ('a', '13.1 Delight', '', 'Not cited. "for in my wrath I struck you, but in my favor I have had mercy on you": favour after wrath, as Psa 30:5 in 10.13.'),
 'Dan 11:36': ('a', '10.7 Willing (the will made absolute)', '', 'Not cited. "the king shall do as he wills. He shall exalt himself ... He shall prosper till the indignation is accomplished": the absolute will with a set end, beside Dan 5:19-21 already there.'),
 'Eze 38:19': ('a', '13.1 Jealousy', '', 'Not cited. "in my jealousy and in my blazing wrath ... there shall be a great earthquake"; all creatures and people "shall quake at my presence" (38:20).'),
 'Pro 11:23': ('a', '10.6 Evil desire', '', 'Not cited. "The desire of the righteous ends only in good, the expectation of the wicked in wrath": where a desire ends.'),
 'Zep 1:18': ('a', '13.1 Jealousy', '', 'Not cited. "Neither their silver nor their gold shall be able to deliver them ... In the fire of his jealousy, all the earth shall be consumed".'),
 'Pro 14:35': ('a', '10.10 Anger between people', '', 'Not cited. "A servant who deals wisely has the king’s favor, but his wrath falls on one who acts shamefully": the ground of the ruler’s favour and wrath, beside Pro 19:12.'),
 'Pro 19:12': ('confirmed', '10.10, 10.13', '', 'In 10.10 and 10.13. Sound.'),
 'Pro 19:13': ('route C', '', '', 'The M18 word means "ruin".'),
 'Pro 21:9': ('confirmed', '10.10', '', 'In 10.10. tov comparative.'),
 'Pro 25:24': ('carried', '10.10 (Pro 21:9)', '', 'Same proverb as 21:9.'),
 'Rom 9:22': ('a', '13.1 Willing', '', 'Not cited (9:18-20 are). "What if God, desiring to show his wrath and to make known his power, has endured with much patience vessels of wrath": desire, wrath and patience in one question.'),
 '2Cor 12:20': ('a', '10.10 Friends, company and care', '', 'Not cited. "I fear that perhaps when I come I may find you not as I wish, and that you may find me not as you wish": two wishes about each other, and fear.'),
 'Gal 5:20': ('confirmed', '10.13, Ch 12', '', 'Cited three times. Sound.'),
 'Rom 13:13': ('a', '10.6 Jealousy and envy', '', 'Not cited. "not in quarreling and jealousy", with "wake from sleep" (13:11) and "make no provision for the flesh, to gratify its desires" (13:14).'),
 'Luk 15:28': ('b', '10.7 Willing', '', 'In 10.13 four times for anger. Not said: the will that stays outside, "refused to go in", and the father who comes out.'),
 '2Cor 7:11': ('confirmed', '10.1, 10.13, Ch 14', '', 'Cited three times; longing and zeal are named in the list there. Sound.'),
 '1Cor 3:3': ('a', '10.6 Jealousy and envy', '', 'Not cited. "while there is jealousy and strife among you, are you not of the flesh", said to "infants in Christ" fed with milk (3:1-2).'),
 'Jam 4:1': ('confirmed', '10.6, 10.10, 10.13, Ch 12', '', 'Cited four times. Sound.'),
 '2Cor 9:2': ('a', 'Ch 11 sec 6', '', 'Not cited. "your zeal has stirred up most of them": zeal passing to others.'),
}

rows = [r for r in csv.DictReader(open(SRC, encoding='utf-8-sig')) if 'M02' in r['shared_with'] and 'M47' not in r['shared_with'] and 'M25' not in r['shared_with']]
missing = [r['reference'] for r in rows if r['reference'] not in D]
extra = [k for k in D if k not in {r['reference'] for r in rows}]
assert not missing and not extra, (missing, extra)
with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'decision', 'proposed_place', 'ch2_natural_place', 'reason', 'shared_with', 'm18_words', 'm02_words',
                'narrative_n_before', 'narrative_refs_before', 'ot_refs', 'text'])
    for r in rows:
        d, p, c2, why = D[r['reference']]
        w.writerow([r['reference'], d, p, c2, why, r['shared_with'], r['m18_words'], r['m02_words'], r['narrative_n'],
                    r['narrative_refs'], r['ot_refs'], r['text']])
print(len(rows), Counter(v[0] for v in D.values()))
print('ch2', [k for k, v in D.items() if v[2]])
