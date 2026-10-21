"""M18 x M47 read-back: one recorded decision per verse (208), joined to the cross-reference data (#1993).

Decisions are the result of reading each verse in its passage beside the M47 batch C reading and the
narrative (worksheet m18-m47-validation-worksheet-v1-20261009.md). Categories (researcher, 2026-10-09):
  a  not narrated because something was missed -> added
  b  narrated, but the reading adds a perspective -> added
  c  an error -> realigned
  confirmed  narrated, sound, placement stands
  parallel   not cited itself; a cited parallel or the same passage carries it
  held-jealousy  held for the M18 jealousy account (OT-95)
  held-tov       generic good/better (tov) rows, held for the delight-filter decision on #1993 (OT-96)
  C          no inner-being or other-being bearing in the M18 word here (rule 72, route C)
Output: m18-m47-validation-register-v1-20261009.csv. No DB query.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'm18-shared-m47-m25-m02-crossref-v2-20261009.csv')
OUT = os.path.join(HERE, 'm18-m47-validation-register-v1-20261009.csv')

D = {
 # R1 / R2 / R3
 'Ecc 6:2': ('a', '10.6', 'unsatisfied soul: lacks nothing it desires, no power to enjoy (batch C 1.10); not narrated'),
 'Isa 38:3': ('held-tov', '', '"done what is good in your sight": tov judged good by God'),
 '1Ch 28:9': ('confirmed', '10.4, 10.7, 10.9, 13.1', 'ESV "willing mind" (delighting soul) quoted in five places'),
 '2Ki 20:3': ('held-tov', '', 'parallel of Isa 38:3'),
 '1Ch 29:9': ('a', '10.7 Willing', 'people rejoiced because they gave willingly; not narrated'),
 'Isa 53:10': ('a', '13.1 Delight', '"the will of the Lord" twice is the delight word (H2654A, H2656); God\'s own pleasure; not narrated'),
 # data notes
 'Psa 38:12': ('confirmed', '10.4', 'M18 word is "ruin" (havvah) in hostile speech'),
 'Ecc 2:17': ('c', 'Ch 5', 'Ch 5 called these death-wishes "exhaustion"; the verse gives the ground "grievous ... vanity"; restated with the ground (from batch G section 6)'),
 'Ecc 2:11': ('confirmed', '10.6', ''),
 'Ecc 4:4': ('a', '10.6', 'envy named as the source of toil, striving after wind (batch C 1.9); not narrated'),
 'Ecc 4:6': ('a', '10.6', 'the Preacher\'s counterweight to 4:4: a handful of quietness'),
 'Psa 40:14': ('a', '10.6', 'delight aimed at another\'s hurt; the M18 face was not carried'),
 'Psa 70:2': ('a', '10.6', 'as Psa 40:14'),
 'Deu 12:20': ('confirmed', 'Ch 5', ''),
 'Deu 14:26': ('b', 'Ch 5', 'the desire is spent before the Lord, with rejoicing (14:26b); only "whatever your appetite craves" was quoted'),
 'Ecc 6:9': ('confirmed', '10.6', ''),
 'Judg 9:2': ('C', '', 'generic "better" (batch C data note 4)'),
 '2Pe 2:10': ('a', 'Ch 7', 'flesh desire and contempt of authority; not narrated'),
 '1Ki 19:10': ('held-jealousy', '', 'Elijah "very jealous for the Lord" with his life sought; zeal is a face of jealousy'),
 '1Ki 19:14': ('held-jealousy', '', 'as 1Ki 19:10'),
 'Num 11:18': ('a', '10.6', '"better for us in Egypt": the craving story of Num 11 was not narrated (10.6 had only Psa 78:30)'),
 '2Sa 18:3': ('C', '', 'generic "better" (batch C data note 4)'),
 'Deu 12:21': ('confirmed', '10.7, Ch 11', ''),
 'Col 2:1': ('C', '', 'idiom: "I want you to know"; flesh = face'),
 'Gal 1:16': ('a', '13.1 Delight', 'God "was pleased to reveal his Son"; batch C set it aside as the flesh idiom only'),
 'Deu 12:15': ('parallel', 'Ch 5', 'same law as Deu 12:20, cited'),
 'Gen 1:21': ('held-tov', '', '"God saw that it was good": a tov row about God'),
 'Ecc 2:26': ('a', '10.6', 'part of 2:24-26: joy given to the one who pleases God'),
 'Dan 1:15': ('C', '', 'generic "better" (batch C data note 4)'),
 'Ecc 1:14': ('parallel', '10.6', 'the refrain, carried by Ecc 2:11'),
 # 1.1
 'Job 33:20': ('confirmed', 'Ch 2, Ch 11', ''),
 'Pro 16:26': ('confirmed', 'Ch 5', ''),
 'Mic 7:1': ('confirmed', 'Ch 5', ''),
 'Gen 34:8': ('a', '10.6', 'longing for a person, spoken in a story of outrage (34:2); not narrated'),
 '1Sa 2:16': ('C', '', 'idiom "as much as you wish (your soul desires)"; the idiom is already stated in Ch 5'),
 '2Sa 3:21': ('b', 'Ch 5', 'the soul-desire idiom as the scope of a rule'),
 '1Ki 11:37': ('b', 'Ch 5', 'as 2Sa 3:21; God\'s word to Jeroboam'),
 '1Sa 23:20': ('b', 'Ch 5', 'as 2Sa 3:21; the Ziphites to Saul'),
 # 1.2
 'Psa 119:20': ('b', 'Ch 5, 10.6', 'cited only in a range in 10.2; the soul\'s longing for God\'s rules'),
 'Isa 26:8': ('a', 'Ch 5, 10.6', 'desire of the soul with waiting; not narrated'),
 'Psa 63:1': ('confirmed', 'Ch 5, Ch 7', ''),
 'Isa 26:9': ('confirmed', 'Ch 1, Ch 3', ''),
 'Pro 25:25': ('confirmed', 'Ch 5, 10.2', ''),
 'Psa 84:2': ('confirmed', 'Ch 2, Ch 5, Ch 7, 10.9', ''),
 'Psa 42:2': ('confirmed', 'Ch 2, 10.6, 10.9', ''),
 'Psa 42:1': ('confirmed', 'Ch 5', ''),
 # 1.3
 'Mat 5:28': ('a', '10.6, Ch 4', 'desire in the heart, through the eye, counted as the deed; not narrated (test batch)'),
 '2Ti 2:22': ('a', '10.6', 'flee youthful passions, with those who call on the Lord from a pure heart'),
 '1Cor 7:37': ('a', '10.6', 'desire under control, determined in the heart'),
 'Psa 10:17': ('a', '10.6', 'God hears the desire of the afflicted'),
 'Rom 1:24': ('b', '10.6', 'cited only in a Held range in Ch 12; given up in the lusts of their hearts'),
 '1Th 2:17': ('a', '10.6', 'longing for people: heart present, body absent'),
 'Pro 6:25': ('a', '10.6', 'desire in the heart, with the eyes (beside Mat 5:28)'),
 'Psa 21:2': ('a', '10.6', 'the heart\'s desire given'),
 'Psa 37:4': ('confirmed', 'Ch 4, 10.6', ''),
 'Pro 13:12': ('confirmed', 'Ch 2, 10.6', ''),
 # 1.4
 'Exo 25:2': ('parallel', '10.7, Ch 4', 'carried by Exo 35:21-22'),
 'Exo 35:21': ('confirmed', 'Ch 3, Ch 4, Ch 6, 10.7', ''),
 '1Cor 10:27': ('C', '', 'idiom "you are disposed to go"'),
 'Heb 13:18': ('a', 'Ch 8', 'a clear conscience, desiring to act honorably'),
 '1Ch 29:17': ('b', '13.1 Delight, 10.7 Willing', 'cited in Ch 14 for 29:18 only; God has pleasure in uprightness; freely offered from an upright heart'),
 'Exo 35:29': ('parallel', '10.7', 'carried by Exo 35:21-22'),
 'Judg 5:9': ('a', '10.7 Willing', 'commanders who offered themselves willingly'),
 # 1.6
 'Pro 16:32': ('confirmed', 'Ch 6, 10.13, Ch 11', ''),
 'Est 5:9': ('confirmed', 'Ch 4, 10.10, 10.13, Ch 11', ''),
 'Ecc 7:3': ('confirmed', '10.1, 10.13, Ch 11', ''),
 'Pro 17:27': ('confirmed', 'Ch 6, 10.1', ''),
 'Psa 94:19': ('confirmed', '10.1, 10.4, Ch 11', ''),
 '2Sa 13:28': ('confirmed', '10.5, Ch 11', ''),
 'Judg 16:25': ('confirmed', 'Ch 11', ''),
 '1Sa 16:16': ('a', 'Ch 6', 'the harmful spirit and the lyre (with 16:23); only 16:14 was narrated'),
 '1Ki 8:66': ('confirmed', 'Ch 11', ''),
 'Judg 19:6': ('parallel', 'Ch 11, 10.7', 'Judg 19:7-10 and 19:22 carry the scene'),
 'Est 1:10': ('confirmed', '10.1, Ch 11', ''),
 'Jer 6:16': ('a', '10.7', 'rest for souls offered and refused ("We will not walk in it")'),
 '2Ch 7:10': ('parallel', 'Ch 11', 'parallel of 1Ki 8:66'),
 '1Sa 25:36': ('confirmed', 'Ch 11', ''),
 'Ecc 7:8': ('confirmed', 'Ch 6', ''),
 '1Sa 16:23': ('a', 'Ch 6', 'Saul refreshed and well, the harmful spirit departed'),
 'Neh 9:20': ('a', 'Ch 6', 'God gave his good Spirit to instruct them (the Spirit acting on persons)'),
 'Psa 143:10': ('a', 'Ch 6, 10.7', 'teach me to do your will; your good Spirit lead me'),
 'Pro 16:19': ('a', 'Ch 12', 'a lowly spirit set against the proud, the verse after 16:18'),
 'Pro 15:15': ('a', '10.1', 'the cheerful of heart has a continual feast'),
 'Ecc 7:2': ('a', '10.1', 'the verse before Ecc 7:3: the living lay it to heart'),
 'Ecc 9:7': ('a', 'Ch 11', 'a merry heart grounded in God\'s approval: a face the threshold section lacked'),
 'Pro 2:10': ('confirmed', 'Ch 3, Ch 4, 10.2', ''),
 'Pro 16:24': ('a', '10.5', 'gracious words: sweetness to the soul and health to the body'),
 # 1.7
 '2Ki 1:13': ('a', 'Ch 5', 'a life precious in another\'s sight'),
 'Isa 43:4': ('a', '13.1 Delight, Ch 5', 'precious in God\'s eyes'),
 '1Sa 26:21': ('a', 'Ch 5', 'Saul: my life was precious in your eyes (10.7 carries 26:23-24 only)'),
 'Act 20:24': ('a', 'Ch 5', 'not counting one\'s own life precious'),
 '1Ki 19:4': ('confirmed', 'Ch 2', ''),
 'Jon 4:8': ('c', 'Ch 5', 'used in the Ch 5 correction: only the second wish comes with faintness'),
 'Psa 72:14': ('a', 'Ch 5', 'precious is their blood in his sight'),
 'Jon 4:3': ('c', 'Ch 5', 'Ch 5 "exhaustion" misread; 4:1-2 give anger at God\'s mercy; Ch 2 stands (test batch)'),
 'Mat 16:25': ('a', 'Ch 5', 'whoever would save his life will lose it'),
 'Mar 8:35': ('a', 'Ch 5', 'parallel of Mat 16:25, cited with it'),
 'Luk 9:24': ('a', 'Ch 5', 'parallel of Mat 16:25, cited with it'),
 'Psa 49:8': ('a', 'Ch 5', 'the ransom of a life is costly; Ch 2 cites Psa 49:10-19 only (Ch 2 placement is on hold, so it goes to Ch 5)'),
 'Pro 6:26': ('a', 'Ch 5', 'a married woman hunts down a precious life'),
 '2Ki 1:14': ('a', 'Ch 5', 'with 2Ki 1:13'),
 # 1.8
 'Eze 36:5': ('held-jealousy', '', 'God\'s hot jealousy'),
 'Jam 3:14': ('held-jealousy', '', 'bitter jealousy in the heart'),
 'Jam 4:5': ('held-jealousy', '', 'he yearns jealously over the spirit (spirit class U)'),
 'Num 11:29': ('held-jealousy', '', 'Moses: are you jealous for my sake?'),
 'Song 8:6': ('confirmed', '10.6', ''),
 'Num 5:14': ('confirmed', 'Ch 6', ''),
 'Num 5:30': ('parallel', 'Ch 6', 'parallel of Num 5:14'),
 'Pro 23:17': ('held-jealousy', '', 'let not your heart envy sinners'),
 'Pro 14:30': ('confirmed', 'Ch 2, Ch 3, Ch 4, Ch 7', ''),
 # 1.9
 'Jer 2:24': ('a', '10.6', 'desire as a drive no one restrains, in Israel going after the Baals (2:25)'),
 'Jer 14:6': ('C', '', 'drought: wild donkeys pant for air; no inner bearing'),
 # 1.10
 'Isa 66:3': ('confirmed', '10.6, 10.7, Ch 11', ''),
 'Pro 10:3': ('a', '10.6', 'God thwarts the craving of the wicked'),
 'Mic 7:3': ('a', '10.6', 'the evil desire of the soul, uttered'),
 'Psa 10:3': ('a', '10.6', 'the wicked boasts of the desires of his soul; Ch 11 cites Psa 10:2, 4 and skips 10:3'),
 'Pro 13:4': ('a', '10.6', 'the sluggard\'s soul craves and gets nothing'),
 'Ecc 6:3': ('a', '10.6', 'with Ecc 6:2'),
 'Num 11:4': ('a', '10.6', 'the strong craving in the wilderness'),
 'Pro 21:10': ('a', '10.6', 'the soul of the wicked desires evil'),
 'Pro 19:2': ('a', '10.6', 'desire without knowledge'),
 # 1.11
 'Eph 2:3': ('confirmed', '10.13, Ch 12, Ch 14', ''),
 'Rom 13:14': ('a', 'Ch 7', 'no provision for the flesh'),
 'Gal 5:24': ('a', 'Ch 7', 'the flesh crucified with its desires'),
 '1Jo 2:16': ('confirmed', 'Ch 7, Ch 12', ''),
 'Gal 5:16': ('a', 'Ch 7', 'walk by the Spirit, not gratify the desires of the flesh'),
 '2Pe 2:18': ('a', 'Ch 7', 'enticing by passions of the flesh'),
 'Joh 1:13': ('a', '10.7 Willing', 'born not of the will of the flesh or of man, but of God'),
 '1Pe 4:2': ('a', 'Ch 7', 'no longer for human passions but for the will of God'),
 '1Pe 2:11': ('confirmed', 'Ch 7, Ch 12', ''),
 'Gal 5:17': ('confirmed', 'Ch 7, Ch 9, Ch 12', ''),
 'Rom 7:18': ('confirmed', 'Ch 7', ''),
 # 1.12
 'Eph 6:6': ('a', '10.7 Willing', 'doing the will of God from the heart (soul)'),
 '2Pe 1:21': ('a', 'Ch 6', 'carried along by the Holy Spirit, not the will of man'),
 'Joh 3:8': ('confirmed', 'Ch 6', ''),
 'Act 13:22': ('a', '13.1 Delight', 'a man after my heart, who will do all my will'),
 '1Ki 8:18': ('a', '13.1 Delight', 'you did well that it was in your heart'),
 '2Ki 10:30': ('a', '13.1 Delight', 'all that was in my heart; set beside Jehu\'s heart (10:31)'),
 '2Ch 6:8': ('a', '13.1 Delight', 'parallel of 1Ki 8:18, cited with it'),
 'Mat 12:18': ('confirmed', '13.1', ''),
 'Heb 10:38': ('a', '13.1 Delight', 'my soul has no pleasure in him'),
 'Job 23:13': ('a', '13.1 Delight', 'what he desires, that he does'),
 'Pro 21:1': ('c', '13.1 Delight, Ch 4', 'Ch 4 listed it as a state of the heart; it is a heart directed where the Lord pleases (test batch)'),
 '1Pe 4:19': ('a', 'Ch 5', 'souls entrusted to a faithful Creator'),
 # 1.13
 'Rev 22:17': ('confirmed', '10.6', ''),
 '1Pe 1:12': ('a', '13.2', 'angels long to look; first content for 13.2'),
 'Rom 1:11': ('a', '10.6', 'longing to see people'),
 '1Pe 2:2': ('a', '10.6', 'long for the pure spiritual milk'),
 '1Cor 14:12': ('a', '10.6', 'eagerness for the Spirit turned to building up the church'),
 # 3.2 / 3.3 / 6.1 / 7.1 / 8.6 / 9.3
 'Eze 22:27': ('a', '10.6', 'destroying lives to get dishonest gain'),
 'Pro 1:19': ('a', '10.6', 'greed takes away the life of its possessors'),
 'Rom 15:27': ('a', '10.7 Willing', 'Macedonia and Achaia pleased to give'),
 'Lam 3:25': ('held-tov', '', '"The Lord is good to those who wait": a tov row about God'),
 '2Ch 15:15': ('a', '10.6', 'sought him with their whole desire, and he was found'),
 '2Ch 19:3': ('held-tov', '', '"some good is found in you": tov judged by God'),
 'Pro 13:19': ('a', '10.6', 'a desire fulfilled is sweet to the soul'),
 'Psa 119:70': ('b', '10.6', 'Ch 4 quotes only "unfeeling like fat"; the verse sets "but I delight in your law" against it'),
 # not in batch C
 'Psa 57:1': ('C', '', '"storms of destruction" (havvah)'),
 'Pro 11:20': ('a', '13.1 Delight', 'blameless ways are his delight'),
 'Gen 49:6': ('confirmed', 'Ch 5, 10.13, Ch 11', ''),
 'Ecc 7:26': ('held-tov', '', '"he who pleases God": tov'),
 'Isa 38:17': ('a', '13.1 Delight', 'in love (H2836A) you have delivered my life'),
 'Ecc 2:24': ('a', '10.6', 'enjoyment named as from the hand of God'),
 'Gal 6:12': ('a', 'Ch 7', 'a good showing in the flesh'),
 'Pro 15:30': ('confirmed', 'Ch 3', ''),
 'Pro 12:25': ('confirmed', '10.1', ''),
 'Deu 18:6': ('confirmed', 'Ch 11', ''),
 'Deu 21:14': ('a', '10.6', 'delight ended, and her own want (soul) protected'),
 'Isa 55:2': ('b', '10.6', 'cited in 10.2 for hearing; the invitation to delight in what satisfies'),
 'Eze 24:25': ('a', '10.6', 'the soul\'s desire taken away'),
 'Gal 6:13': ('a', 'Ch 7', 'with Gal 6:12'),
 '1Ki 10:2': ('C', '', 'precious stones; "all that was on her mind"'),
 '2Ch 9:1': ('C', '', 'parallel of 1Ki 10:2'),
 '2Ch 30:22': ('C', '', '"good skill"; spoke to the heart (M47 face only)'),
 'Eze 24:21': ('a', '10.6', 'with Eze 24:25'),
 'Col 2:18': ('C', '', '"insisting on" asceticism: the M18 word is an idiom here'),
 '1Sa 9:20': ('C', '', '"all that is desirable in Israel": kingship offered; no inner act of desire'),
 'Jon 1:14': ('a', '13.1 Delight', 'you, O Lord, have done as it pleased you'),
 'Isa 58:3': ('confirmed', '10.7', ''),
 'Isa 58:5': ('confirmed', '10.7', 'quoted in 10.7 as "(58:5)"; the cross-reference script missed the bare citation'),
 'Act 7:39': ('a', '10.7', 'refusing the one who received living oracles; in their hearts they turned to Egypt'),
 '1Th 2:8': ('a', '10.6', 'affectionately desirous; ready to share our own selves'),
 '1Sa 1:8': ('confirmed', 'Ch 11', ''),
 '1Sa 27:1': ('confirmed', 'Ch 4, 10.0', ''),
 'Est 6:6': ('a', '10.6', 'Haman reads the king\'s delight by his own'),
 'Est 7:3': ('C', '', 'court formula "if it please the king"'),
 'Psa 45:1': ('a', '10.5', 'the heart overflows; the tongue a ready pen'),
 'Ecc 3:17': ('C', '', 'the M18 word is "matter"'),
 'Isa 21:4': ('a', '10.6', 'the twilight longed for turned into trembling'),
 'Luk 3:22': ('a', '13.1 Delight', 'with you I am well pleased, the Spirit descending'),
 'Isa 57:13': ('C', '', '"collection of idols" carried off by the wind'),
 'Psa 125:4': ('held-tov', '', '"Do good, O Lord, to those who are good": tov'),
 'Pro 14:14': ('held-tov', '', '"a good man": tov'),
 'Jos 23:14': ('held-tov', '', '"all the good things": tov'),
 'Eze 8:3': ('held-jealousy', '', 'the image of jealousy that provokes to jealousy'),
 'Rev 18:14': ('a', '10.6', 'the fruit your soul longed for gone'),
 'Hos 13:15': ('C', '', 'every precious thing stripped by the east wind'),
 'Pro 18:2': ('a', '10.6', 'a fool takes no pleasure in understanding'),
 'Rut 4:15': ('confirmed', 'Ch 5', ''),
 'Psa 73:1': ('held-tov', '', '"God is good to Israel": tov; its 73:3 envy goes with the jealousy account'),
 'Ecc 2:3': ('parallel', '10.6', 'the pleasure trial of Ecc 2:1-11, carried by 2:11'),
 'Lam 1:11': ('C', '', 'treasures traded for food'),
 'Deu 28:56': ('C', '', '"delicate": refinement under siege; held in M47 batch F section 6 for the tender heart'),
 'Psa 19:14': ('confirmed', '10.5', ''),
 'Col 1:9': ('a', '10.7 Willing', 'filled with the knowledge of his will'),
 '1Cor 4:21': ('confirmed', '10.10', ''),
 '1Cor 12:1': ('C', '', 'idiom "I do not want you to be uninformed"'),
 'Gal 3:2': ('C', '', 'idiom "Let me ask you"'),
}

rows = [r for r in csv.DictReader(open(SRC, encoding='utf-8-sig')) if 'M47' in r['shared_with']]
refs = [r['reference'] for r in rows]
missing = [x for x in refs if x not in D]
extra = [x for x in D if x not in refs]
assert not missing and not extra, (missing, extra)

with open(OUT, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'decision', 'placed_in', 'reason', 'shared_with', 'm18_words', 'm47_words',
                'narrative_n_before', 'narrative_refs_before', 'm47_analysis_files', 'text'])
    for r in rows:
        dec, tgt, why = D[r['reference']]
        w.writerow([r['reference'], dec, tgt, why, r['shared_with'], r['m18_words'], r['m47_words'],
                    r['narrative_n'], r['narrative_refs'], r['m47_analysis_files'], r['text']])
print(len(rows), '->', OUT)
print(Counter(v[0] for v in D.values()))
tg = Counter()
for v in D.values():
    if v[0] in ('a', 'b', 'c'):
        for t in v[1].split(', '): tg[t.split(' ')[0] if not t.startswith('13') else t] += 1
print(tg)
