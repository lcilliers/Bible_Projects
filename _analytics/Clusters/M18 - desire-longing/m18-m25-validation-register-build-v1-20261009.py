"""Register of the M18 x M25 read-back (#1993, handoff item B): one decision per verse, with its reason.

Input: m18-shared-m47-m25-m02-crossref-v2-20261009.csv (M25 rows without M47: 89), read beside the M25 ledgers
in m18-m25-validation-worksheet-v1-20261009.md. Output: m18-m25-validation-register-v1-20261009.csv.
Decisions: a = missed, add; b = new perspective, add; c = error, realign; confirmed; carried (by a parallel);
held (named thread); route C (no inner-being bearing for the M18 word). 'proposed_place' is a proposal only:
nothing is woven until the researcher instructs. 'ch2' marks a verse whose natural M25 place is Ch 2 (OT-08 hold).
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'm18-shared-m47-m25-m02-crossref-v2-20261009.csv')
OUT = os.path.join(HERE, 'm18-m25-validation-register-v1-20261009.csv')

D = {  # reference: (decision, proposed_place, ch2, reason)
 'Tit 3:3': ('a', '10.6', '', 'Not cited. "slaves to various passions and pleasures, passing our days in malice and envy"; the passage answers it (3:4-5, the washing of regeneration). Desire that masters a person: 10.6 has no verse for it.'),
 'Luk 8:14': ('a', '10.6', '', 'Not cited; 8:15 is in Ch 4 and 10.1. Those "choked by the cares and riches and pleasures of life, and their fruit does not mature": pleasures crowding out the word.'),
 'Judg 8:32': ('carried', 'Ch 2 (Gen 25:8)', '', '"died in a good old age": the same formula as Gen 25:8, already in Ch 2. tov qualifies the age.'),
 '1Ch 29:28': ('carried', 'Ch 2 (Gen 25:8)', '', '"died at a good age, full of days, riches, and honor": same formula as Gen 25:8.'),
 'Est 2:7': ('route C', '', '', '"lovely to look at": tov qualifies appearance; the death is a notice (D01).'),
 '1Sa 26:16': ('route C', '', '', '"This thing that you have done is not good": a verdict on an act; the oath is M25 data (L01).'),
 '1Sa 19:1': ('a', '10.10 Loyalty and honour', '', 'Not cited. Saul orders David killed, "But Jonathan, Saul\'s son, delighted much in David", and warns him (19:2). Delight in a person standing against a father\'s order.'),
 '2Sa 14:32': ('route C', '', '', 'Absalom: "It would be better for me to be there still": tov "better" in a demand; no desire face.'),
 '1Ki 2:42': ('route C', '', '', 'Shimei: "What you say is good; I will obey": a formula of assent. (2:44 "you know in your own heart" is not M18.)'),
 'Hos 2:3': ('route C', '', '', '"kill her with thirst": thirst as the image of judgement on the faithless wife; no one\'s want is named.'),
 '1Sa 2:25': ('a', '13.1 Delight (He does what pleases him)', '', 'Not cited. Eli\'s sons "would not listen to the voice of their father, for it was the will of the Lord to put them to death". "will" is the delight word. Quote as stated; no explanation added.'),
 'Jer 42:22': ('a', '10.6', '', 'Not cited; 42:16 is in 10.1 and 10.12. "in the place where you desire to go to live": a desire held against the word they asked for (42:20-21).'),
 'Hos 9:16': ('carried', '10.6 (Eze 24:21, 25)', '', '"I will put their beloved [desired] children to death": what is desired taken away, the same face as Eze 24:21, 25 in 10.6.'),
 'Judg 13:23': ('confirmed', '10.4', '', 'In 10.4 (13:22-23). "If the Lord had meant [delighted] to kill us": she reasons from what God wants. Sound.'),
 'Judg 15:18': ('b', '10.6 (the thirst answered: thirst spoken to God)', '', 'Moved from carried after the probing reading (m18-m25-inner-being-reading §7). 15:19 is in Ch 6 and Ch 2. Not said: the thirsty man speaks to God from what God has done, "You have granted this great salvation ... shall I now die of thirst", against Israel accusing Moses at Rephidim (Exo 17:3).'),
 '2Ch 32:11': ('route C', '', '', 'Sennacherib\'s taunt: "give you over to die by famine and by thirst".'),
 '2Sa 19:37': ('route C', '', '', '"whatever seems good to you": idiom. The inner verse is 19:35 ("Can I discern what is pleasant"), already in 10.7 and Ch 11; 19:38 is in 10.6.'),
 'Deu 4:22': ('route C', '', '', '"that good land": tov qualifies the land.'),
 'Ecc 7:1': ('confirmed', 'Ch 2', '', 'In Ch 2 "What death is". tov comparative ("better"). Sound.'),
 'Joh 21:23': ('a', '13.1 Willing; 10.7 Willing (21:18)', '', 'Not cited. Peter’s own will overruled (21:18), his comparison with another (21:21), Christ’s will answering both (21:22); the rumour misread it (21:23). Reading §11.'),
 'Gen 25:8': ('confirmed', 'Ch 2', '', 'In Ch 2. tov qualifies the age.'),
 'Ecc 9:4': ('confirmed', 'Ch 2', '', 'In Ch 2 "Life weighed". tov comparative. Sound.'),
 'Exo 14:12': ('a', '10.6 (Wanting shaped by fear); pointers 10.12 and Ch 2', 'yes', 'Not cited; 14:10, 14:13 in 10.12. Fear makes slavery preferable: "better for us to serve the Egyptians than to die in the wilderness"; beside Jer 42 and Num 11:18 (reading §8). Ch 2 Wanting to die pointer (OT-08 holds rework, not additions).'),
 'Gen 30:1': ('confirmed', 'Ch 2, 10.6', '', 'In Ch 2 and 10.6. Envy (H7065) noted for the jealousy account (OT-95); not moved.'),
 'Exo 17:3': ('b', '10.6 (Unmet, and wanting against God)', '', 'Already quoted in 10.5 Grumbling as a bare citation (17:3), missed by the parser. Not said: the thirst spoken as accusation to Moses, against Samson asking God (Judg 15:18).'),
 'Rev 9:6': ('confirmed', 'Ch 2', '', 'In Ch 2 "Wanting to die". Sound.'),
 '2Sa 1:23': ('confirmed', '10.10', '', 'In 10.10. "lovely" qualifies Saul and Jonathan. Sound.'),
 'Eze 18:18': ('route C', '', '', '"did what is not good among his people": tov qualifies acts.'),
 'Jam 1:15': ('confirmed', 'Ch 2, 10.6, Ch 12', '', 'Cited four times. Sound.'),
 'Job 5:2': ('confirmed', 'Ch 2, 10.1, 10.13, Ch 11, Ch 12', '', 'Cited five times. Jealousy noted for OT-95; not moved.'),
 'Pro 21:25': ('confirmed', 'Ch 2, 10.6, Ch 11', '', 'Cited three times. 21:26 "All day long he craves and craves" is the next verse, not in this set (for item F).'),
 'Eze 18:23': ('b', '13.1 Delight (what he has no pleasure in)', '', 'In Ch 2 for turning and living. The M18 side is not said: "Have I any pleasure in the death of the wicked". 13.1 Delight has what he delights in, and Heb 10:38, but not this.'),
 'Eze 18:32': ('b', '13.1 Delight (with 18:23)', '', 'In Ch 11 and Ch 14. "For I have no pleasure in the death of anyone": with 18:23.'),
 'Eze 33:11': ('b', '13.1 Delight (with 18:23)', '', 'In Ch 2. "As I live ... I have no pleasure in the death of the wicked": with 18:23; his own oath (LD-96).'),
 'Col 3:5': ('confirmed', 'Ch 2, 10.6, Ch 11, Ch 12, Ch 14', '', 'Cited five times. Sound.'),
 'Psa 116:15': ('b', '13.1 Delight (what he delights in)', '', 'In Ch 2 "Dying to the Lord". "Precious in the sight of the Lord is the death of his saints": the precious word, said of God\'s sight, beside Isa 43:4 "precious in my eyes".'),
 'Ecc 10:1': ('route C', '', '', '"a little folly outweighs wisdom and honor": the precious word means "weighs more"; dead flies are D27.'),
 'Isa 50:2': ('route C', '', '', '"their fish stink for lack of water and die of thirst": God\'s rebuke on the sea; no want named.'),
 'Joh 5:21': ('b', '13.1 Willing', '', 'In Ch 2 "Made alive". The M18 side is not said: "so also the Son gives life to whom he will".'),
 '1Sa 29:6': ('route C', '', '', 'Achish: "it seems right ... the lords do not approve of you": idiom "good in the eyes".'),
 'Rut 3:13': ('a', '10.7 Willing (A plan meets another person\'s will)', '', 'Not cited for this verse (Ch 11 has 3:7-9). Boaz allows for the nearer redeemer\'s will: "if he is not willing to redeem you, then, as the Lord lives, I will redeem you". Same shape as Gen 24:5-8 already there. "willing" is H2654.'),
 'Eze 35:11': ('confirmed', '10.13', '', 'In 10.13. Envy noted for OT-95; not moved.'),
 'Dan 8:4': ('route C', '', '', 'The ram in a vision: "He did as he pleased and became great". Noted for item F: the kings who do as they please (Dan 11:3, 16, 36) are one face.'),
 'Psa 104:11': ('a', '13.4 Nature', '', 'Not cited. "they give drink to every beast of the field; the wild donkeys quench their thirst": creatures\' thirst met by God, nature in its own right (route A). 13.4 is empty: this would be its first content.'),
 'Psa 68:30': ('a', '10.6 (delight list)', '', 'Not cited; only 68:20 is in Ch 2. "scatter the peoples who delight in war": delight set on war.'),
 'Gen 1:25': ('a', '13.1 Delight or 13.4 Nature (researcher call); 10.6 via Gen 3:6', '', 'OT-96 hold withdrawn (filter is a working aid, researcher 2026-10-09). "God saw that it was good": God’s look of approval; the same seeing-that-it-is-good is the woman’s in Gen 3:6 (reading §6).'),
 'Isa 57:4': ('route C', '', '', 'H6026 here means mocking. Read with OT-15 (held items reading section 3): the passage goes on to burning with lust (57:5), woven in 10.6 As heat.'),
 'Deu 5:33': ('carried', 'Ch 2, 10.10 (Exo 20:12)', '', '"that it may go well with you, and that you may live long": the promise formula, carried by Exo 20:12.'),
 'Ecc 8:12': ('confirmed', '10.4', '', 'In 10.4. tov in "it will be well". Sound.'),
 'Ecc 8:13': ('carried', '10.4 (8:12)', '', 'The other half of 8:12.'),
 '1Pe 3:10': ('b', '10.6 (wanting life itself)', '', 'In Ch 2 and 10.5 for the tongue. The want is not said: "Whoever desires to love life and see good days". Test batch 4.4.'),
 'Psa 34:12': ('a', '10.6 (Wanting life); Ch 2 Life weighed (see good, with Job 7:7)', 'yes', 'Not cited; only its NT quotation is. "desires life ... that he may see good" against Job 7:7 "never again see good". Test batch 4.4; reading §1.'),
 'Pro 8:35': ('a', '13.1 Delight (whom he is pleased with); Ch 2 Life set before a person (8:36)', 'yes', 'Not cited. Favour by finding, in daily waiting at Wisdom’s gates (8:34); "all who hate me love death" (8:36). Reading §11, §14.'),
 'Pro 16:15': ('route C', '', '', 'A king\'s favour "like the clouds that bring the spring rain": the favour of a ruler, a simile; no inner act.'),
 'Mat 19:17': ('a', '10.7 Willing (the will invited); 10.6 possessions', '', 'Not cited. "If you would enter life" and "If you would be perfect" (19:21); "went away sorrowful, for he had great possessions" (19:22). Restate 10.7’s Isaiah 1 sentence (reading §10). OT-01 touched.'),
 '2Cor 1:8': ('confirmed', 'Ch 2', '', 'In Ch 2. The M18 word is the idiom "we do not want you to be unaware".'),
 'Ecc 6:12': ('a', '10.6 (Ecclesiastes paragraph)', '', 'OT-96 hold withdrawn. "who knows what is good for man while he lives ... which he passes like a shadow": wanting assumes knowing what is good; closes the 6:2-9 passage already in 10.6 (reading §4).'),
 'Ecc 5:18': ('a', '10.6 (Ecclesiastes paragraph)', '', 'Not cited. "what I have seen to be good and fitting is to eat and drink and find enjoyment ... for this is his lot"; 5:19-20 "this is the gift of God", "God keeps him occupied with joy in his heart". Beside 2:24-26, already woven.'),
 'Ecc 8:15': ('a', '10.6 (Ecclesiastes paragraph)', '', 'Not cited. "And I commend joy, for man has nothing better under the sun but to eat and drink and be joyful".'),
 'Luk 15:13': ('route C', '', '', 'The M18 word is "far" (gloss group G).'),
 'Ecc 3:12': ('a', '10.6 (Ecclesiastes paragraph)', '', 'Not cited for this verse. "nothing better for them than to be joyful and to do good as long as they live"; 3:13 "this is God\'s gift to man".'),
 'Psa 63:3': ('confirmed', '10.9', '', 'In 10.9. tov comparative. Sound.'),
 'Psa 145:16': ('confirmed', '10.6', '', 'In 10.6. Sound.'),
 'Psa 16:11': ('a', '10.6 (aimed at the living God)', '', 'Not cited. "in your presence there is fullness of joy; at your right hand are pleasures forevermore". 16:9-10 is in Q2-05.'),
 'Psa 27:4': ('b', '10.6 (aimed at the living God)', '', 'In Ch 2 for "all the days of my life". Not said: "One thing have I asked of the Lord, that will I seek after ... to gaze upon the beauty of the Lord".'),
 'Rev 21:6': ('carried', '10.6 (Rev 22:17)', '', '"To the thirsty I will give from the spring of the water of life without payment": carried by Rev 22:17 in 10.6.'),
 'Joh 4:14': ('b', '10.6 (the thirst answered)', '', 'In Ch 2 "Where life flows from". Not said: "whoever drinks of the water that I will give him will never be thirsty again"; the woman asks for it (4:15).'),
 'Joh 6:40': ('a', '13.1 Willing', '', 'Not cited. The Father’s will has content (6:39-40); the Son "not to do my own will" (6:38) means 13.1’s Gethsemane "one place" sentence must be restated. Reading §11.'),
 '2Ti 1:1': ('route C', '', '', '"by the will of God": the opening formula of a letter.'),
 'Joh 6:35': ('a', '10.6 (the thirst answered)', '', 'Not cited. "whoever comes to me shall not hunger, and whoever believes in me shall never thirst".'),
 'Joh 5:40': ('b', '10.7 Willing (Refusing God refuses something good)', '', 'In 10.4 (5:39-40) for thinking. Not said: "you refuse [are not willing] to come to me that you may have life". Life is what is offered.'),
 '2Ti 3:12': ('a', '10.7 Willing', '', 'Not cited. "all who desire to live a godly life in Christ Jesus will be persecuted": the will set on godliness, beside "the will turned toward harm".'),
 'Jam 4:15': ('confirmed', 'Ch 2, 10.7', '', 'In Ch 2 and 10.7 Planning. Sound.'),
 'Tit 2:12': ('a', '10.6', '', 'Not cited. Grace "training us to renounce ungodliness and worldly passions": with Tit 3:3.'),
 'Rom 11:15': ('route C', '', '', '"their acceptance": God\'s receiving of Israel, not desire. LD-129 (life from the dead) is an M25 matter.'),
 '2Cor 5:4': ('confirmed', '10.6', '', 'In 10.6. Sound.'),
 'Gen 2:9': ('confirmed', 'Ch 2', '', 'In Ch 2. "pleasant to the sight" qualifies trees. Noted for item F: Gen 3:6 uses the same desire word for the tree, and is not in this set.'),
 'Psa 30:5': ('confirmed', '10.13, Ch 11', '', 'In 10.13 and Ch 11. Sound.'),
 '1Cor 7:39': ('route C', '', '', '"free to be married to whom she wishes": a legal provision (L31). 7:37 "having his desire under control" is already in 10.6.'),
 'Act 26:5': ('route C', '', '', '"if they are willing to testify": idiom.'),
 'Psa 119:40': ('b', '10.6 (Aimed at God)', '', 'Already quoted in Ch 2 Life asked for as a bare citation (119:40), which the cross-reference parser missed (handoff item I). Not said: the longing with the eye turned from worthless things (119:37), and that the longing does not give the life.'),
 'Psa 119:77': ('a', '10.6 (delight list, God\'s word)', '', 'Not cited. "Let your mercy come to me, that I may live; for your law is my delight": beside 119:70.'),
 'Pro 15:27': ('a', '10.6 (possessions paragraph)', '', 'Not cited. "Whoever is greedy for unjust gain troubles his own household, but he who hates bribes will live": beside Pro 1:19.'),
 'Eze 20:25': ('route C', '', '', '"statutes that were not good": tov qualifies statutes. LD-30 and OT-01 are M25 matters.'),
 'Isa 13:17': ('route C', '', '', 'The Medes "do not delight in gold": an oracle naming God\'s instrument; the delight phrase says gold will not turn them.'),
 'Isa 42:13': ('a', '13.1 Jealousy (roused after long restraint)', '', 'OT-95 hold withdrawn and read (held items reading section 1): zeal as a warrior and a woman in labour (42:13-14).'),
 'Song 2:7': ('confirmed', 'Ch 11', '', 'In Ch 11 ("until it pleases"). The love verses are handed to #1942 (on hold).'),
 'Song 3:5': ('carried', 'Ch 11 (Song 2:7)', '', 'The same refrain as 2:7.'),
 'Song 8:4': ('carried', 'Ch 11 (Song 2:7)', '', 'The same refrain as 2:7.'),
}

rows = [r for r in csv.DictReader(open(SRC, encoding='utf-8-sig')) if 'M25' in r['shared_with'] and 'M47' not in r['shared_with']]
missing = [r['reference'] for r in rows if r['reference'] not in D]
extra = [k for k in D if k not in {r['reference'] for r in rows}]
assert not missing and not extra, (missing, extra)
with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'decision', 'proposed_place', 'ch2_natural_place', 'reason', 'shared_with', 'm18_words', 'm25_words',
                'narrative_n_before', 'narrative_refs_before', 'ot_refs', 'text'])
    for r in rows:
        d, p, c2, why = D[r['reference']]
        w.writerow([r['reference'], d, p, c2, why, r['shared_with'], r['m18_words'], r['m25_words'], r['narrative_n'],
                    r['narrative_refs'], r['ot_refs'], r['text']])
print(len(rows), Counter(v[0] for v in D.values()))
print('ch2', [k for k, v in D.items() if v[2]])
