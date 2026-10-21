"""M08 batch 2 (the other Hebrew pride words and the Hebrew group B pride-sense verses): one decision
per verse (#2156). Read in passage (m08-batch-pull-v1-20261015.py 2 2); groups emerged from the reading
(m08-batch2-reading-v1-20261015.md). Decision and route values as in the batch 1 register script.
Writes m08-batch2-register-v1-20261015.csv and checks every scope verse has one row.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. The heart lifted up'
G2 = 'II. Presumption: going beyond what was given'
G3 = 'III. The insolent against others'
G4 = 'IV. Lifted against God, and brought down'
G5 = 'V. The other face: not lifted up, or lifted toward God'
G6 = 'VI. Other beings and nature'
G7 = 'VII. Other senses'
M1 = 'carried (M09 batch 1 register)'
M2 = 'carried (M09 batch 2 register)'
R = [
 # I
 ('2Ch 26:16', G1, 'read', 'B', '"when he was strong, he grew proud, to his destruction"; enters the temple to burn incense; "It is not for you" (26:18)'),
 ('2Ch 32:25', G1, 'read', 'A B', '"did not make return according to the benefit done to him, for his heart was proud"; after healing and gifts (32:23-24)'),
 ('2Ch 32:26', G1, M1, 'A B', 'humbled himself for the pride of his heart'),
 ('Dan 5:20', G1, 'read', 'A B', '"when his heart was lifted up and his spirit was hardened so that he dealt proudly"; the greatness was given by the Most High (5:18-19)'),
 ('Eze 28:2', G1, 'read', 'A B', '"your heart is proud, and you have said, I am a god ... yet you are but a man, and no god"'),
 ('Eze 28:5', G1, 'read', 'B', '"your heart has become proud in your wealth"; by wisdom and trade (28:4)'),
 ('Eze 28:17', G1, 'read', 'A B', '"Your heart was proud because of your beauty; you corrupted your wisdom for the sake of your splendor"; blameless till unrighteousness found (28:15)'),
 ('Eze 31:10', G1, 'read', 'A B', '"its heart was proud of its height"; "I made it beautiful" (31:9)'),
 ('Pro 16:5', G1, 'read', 'A B', '"Everyone who is arrogant in heart is an abomination to the Lord"'),
 ('Pro 18:12', G1, M2, 'B', 'before destruction a heart is haughty; beside a rich man\'s wealth "like a high wall in his imagination" (18:11)'),
 ('Pro 21:4', G1, 'read', 'B', '"Haughty eyes and a proud heart, the lamp of the wicked, are sin"; the Lord weighs the heart (21:2)'),
 ('Psa 101:5', G1, 'read', 'B', '"Whoever has a haughty look and an arrogant heart I will not endure": the king\'s resolve'),
 ('Ecc 7:8', G1, 'read', 'B', '"the patient in spirit is better than the proud in spirit"; then anger in the spirit (7:9)'),
 ('Obd 3', G1, 'read', 'A B', '"The pride of your heart has deceived you ... who say in your heart, Who will bring me down"'),
 ('Obd 4', G1, 'read', 'A B', '"Though you soar aloft like the eagle ... from there I will bring you down"'),
 ('Jer 49:16', G1, 'read', 'A B', '"The horror you inspire has deceived you, and the pride of your heart"'),
 ('Hab 2:5', G1, 'read', 'B', '"an arrogant man who is never at rest. His greed is as wide as Sheol"; 2:4 "his soul is puffed up; it is not upright"'),
 ('Psa 10:4', G1, 'read', 'B', '"In the pride of his face the wicked does not seek him; all his thoughts are, There is no God"'),
 ('Isa 10:12', G1, 'read', 'A B', '"the speech of the arrogant heart ... and the boastful look in his eyes": "By the strength of my hand I have done it" (10:13)'),
 ('Isa 3:16', G1, 'read', 'B', 'the daughters of Zion haughty, "outstretched necks, glancing wantonly"; after the spoil of the poor (3:14-15)'),
 ('Pro 17:19', G1, 'read', 'B', '"he who makes his door high seeks destruction"; with loving transgression and strife'),
 ('Eze 16:30', G1, 'read', 'B', '"How sick is your heart ... the deeds of a brazen prostitute"; "you scorned payment" (16:31)'),
 # II
 ('Deu 17:12', G2, 'read', 'B', '"acts presumptuously by not obeying the priest ... or the judge"'),
 ('Deu 17:13', G2, 'read', 'B', '"all the people shall hear and fear and not act presumptuously again"'),
 ('Deu 18:20', G2, 'read', 'A B', '"the prophet who presumes to speak a word in my name that I have not commanded him"'),
 ('Deu 18:22', G2, 'read', 'B', '"the prophet has spoken it presumptuously. You need not be afraid of him"'),
 ('Deu 1:43', G2, 'read', 'B', 'told not to go up, "you would not listen; but you rebelled ... and presumptuously went up"; then wept (1:45)'),
 ('Neh 9:16', G2, 'read', 'A B', '"acted presumptuously and stiffened their neck"; "not mindful of the wonders" (9:17); God ready to forgive'),
 ('Neh 9:29', G2, 'read', 'A B', '"you warned them in order to turn them back ... Yet they acted presumptuously"'),
 ('Psa 19:13', G2, 'read', 'A B', '"Keep back your servant also from presumptuous sins; let them not have dominion over me"'),
 ('Exo 21:14', G2, 'read', 'B', '"if a man willfully attacks another to kill him by cunning": set against the one who did not lie in wait (21:13)'),
 ('1Sa 17:28', G2, 'read', 'B', 'Eliab, angry: "I know your presumption and the evil of your heart"; David: "What have I done now?"'),
 ('Jer 13:15', G2, 'read', 'B', '"Hear and give ear; be not proud, for the Lord has spoken": hearing named as the opposite (with Jer 13:17, batch 1)'),
 ('Pro 11:2', G2, M2, 'B', '"When pride comes, then comes disgrace, but with the humble is wisdom"'),
 ('Pro 13:10', G2, 'read', 'B', '"By insolence comes nothing but strife, but with those who take advice is wisdom"'),
 ('Pro 14:16', G2, 'read', 'B', '"a fool is reckless and careless": the wise is cautious and turns from evil'),
 ('Pro 21:24', G2, 'read', 'B', '"Scoffer is the name of the arrogant, haughty man who acts with arrogant pride"'),
 # III
 ('Psa 119:21', G3, 'read', 'A B', '"You rebuke the insolent, accursed ones, who wander from your commandments"'),
 ('Psa 119:51', G3, 'read', 'B', '"The insolent utterly deride me, but I do not turn away from your law"'),
 ('Psa 119:69', G3, 'read', 'B', '"The insolent smear me with lies"; "their heart is unfeeling like fat" (119:70)'),
 ('Psa 119:78', G3, 'read', 'B', '"they have wronged me with falsehood; as for me, I will meditate on your precepts"'),
 ('Psa 119:85', G3, 'read', 'B', '"The insolent have dug pitfalls for me; they do not live according to your law"'),
 ('Psa 119:122', G3, 'read', 'A B', '"Give your servant a pledge of good; let not the insolent oppress me"'),
 ('Psa 86:14', G3, 'read', 'B', '"insolent men have risen up against me ... and they do not set you before them"'),
 ('Psa 56:2', G3, 'read', 'B', '"many attack me proudly"; "When I am afraid, I put my trust in you" (56:3)'),
 ('Psa 94:4', G3, 'read', 'B', '"They pour out their arrogant words; all the evildoers boast"'),
 ('Psa 73:8', G3, 'read', 'B', '"They scoff and speak with malice; loftily they threaten oppression"; "set their mouths against the heavens" (73:9)'),
 ('Psa 40:4', G3, 'read', 'B', '"Blessed is the man who makes the Lord his trust, who does not turn to the proud"'),
 ('Isa 3:5', G3, 'read', 'B', '"the youth will be insolent to the elder, and the despised to the honorable"'),
 ('Exo 18:11', G3, 'read', 'A B', 'Jethro: "Now I know that the Lord is greater than all gods, because in this affair they dealt arrogantly with the people"'),
 ('Neh 9:10', G3, 'read', 'A', '"you knew that they acted arrogantly against our fathers. And you made a name for yourself"'),
 ('Eze 16:50', G3, 'read', 'B', '"They were haughty and did an abomination before me"; after 16:49 (batch 1)'),
 ('Jer 43:2', G3, 'read', 'B', '"all the insolent men said to Jeremiah, You are telling a lie"; did not obey (43:4)'),
 ('Mal 3:15', G3, 'read', 'B', '"now we call the arrogant blessed"; "It is vain to serve God" (3:14); the Lord heard those who feared him (3:16)'),
 # IV
 ('2Ki 19:22', G4, 'read', 'A B', '"Against whom have you raised your voice and lifted your eyes to the heights? Against the Holy One of Israel!"'),
 ('Isa 37:23', G4, 'read', 'A B', 'as 2Ki 19:22'),
 ('Psa 75:5', G4, 'read', 'A B', '"do not lift up your horn on high"; "it is God who executes judgment, putting down one and lifting up another" (75:7)'),
 ('1Sa 2:3', G4, 'read', 'A B', 'Hannah: "Talk no more so very proudly ... for the Lord is a God of knowledge, and by him actions are weighed"; the mighty broken, the feeble strengthened (2:4)'),
 ('Jer 50:29', G4, 'read', 'A B', '"she has proudly defied the Lord, the Holy One of Israel"'),
 ('Jer 50:31', G4, 'read', 'A', '"Behold, I am against you, O proud one"'),
 ('Jer 50:32', G4, 'read', 'A B', '"The proud one shall stumble and fall, with none to raise him up"'),
 ('Mal 4:1', G4, 'read', 'A B', '"all the arrogant and all evildoers will be stubble"; for those who fear his name, healing (4:2)'),
 ('Eze 7:10', G4, 'read', 'A B', '"the rod has blossomed; pride has budded"'),
 ('Eze 31:14', G4, 'read', 'A B', '"in order that no trees ... may grow to towering height ... For they are all given over to death"'),
 ('Isa 22:16', G4, 'read', 'A B', 'Shebna "cut out a tomb on the height"; "you shame of your master\'s house" (22:18)'),
 ('Isa 2:11', G4, M1, 'A B', 'haughty looks brought low, the Lord alone exalted'),
 ('Isa 2:17', G4, M1, 'A B', 'as 2:11'),
 ('Isa 5:15', G4, M1, 'A B', 'the eyes of the haughty brought low; 5:16 the Lord exalted in justice'),
 ('Isa 10:33', G4, M1, 'A B', 'the great in height hewn down'),
 ('Isa 26:5', G4, M1, 'A B', 'the lofty city laid low; "The foot tramples it, the feet of the poor" (26:6)'),
 # V
 ('2Ch 17:6', G5, 'read', 'A B', '"His heart was courageous [lifted up] in the ways of the Lord"; he had sought the God of his father (17:4)'),
 ('Psa 131:1', G5, 'read', 'B', '"my heart is not lifted up; my eyes are not raised too high"; "I have calmed and quieted my soul" (131:2)'),
 ('Psa 138:3', G5, 'read', 'A B', '"On the day I called, you answered me; my strength of soul you increased" (the word glossed "be assertive")'),
 ('Psa 138:6', G5, M2, 'A B', '"though the Lord is high, he regards the lowly, but the haughty he knows from afar"'),
 # VI
 ('Job 41:34', G6, 'read', 'A', 'Leviathan "sees everything that is high; he is king over all the sons of pride"'),
 ('Job 28:8', G6, 'data', 'C', '"The proud beasts have not trodden it"'),
 # VII
 ('Pro 25:3', G7, 'read', 'B', '"As the heavens for height ... so the heart of kings is unsearchable": height as the measure of the heart, no pride'),
 ('Pro 28:25', G7, 'read', 'B', '"A greedy man stirs up strife, but the one who trusts in the Lord will be enriched" (ESV greedy)'),
 ('Gen 25:29', G7, 'data', 'C', '"Jacob was cooking stew"'),
 ('Pro 6:3', G7, 'data', 'C', '"plead urgently with your neighbor"'),
 ('Song 6:5', G7, 'data', 'C', '"they overwhelm me"'),
]
scope = [r['reference'] for r in csv.DictReader(open(os.path.join(HERE, 'm08-reading-scope-v1-20261015.csv'), encoding='utf-8')) if r['batch'].startswith('2 ')]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)), [x for x in refs if refs.count(x) > 1]
assert set(refs) == set(scope), (set(scope) - set(refs), set(refs) - set(scope))
with open(os.path.join(HERE, 'm08-batch2-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note']); w.writerows(R)
print(len(R), Counter(r[2] for r in R), Counter(r[1] for r in R))
