"""M08 batch 5 (mocking, group D): one decision per verse (#2156). Read in passage
(m08-batch-pull-v1-20261015.py 5 2); groups emerged from the reading (m08-batch5-reading-v1-20261015.md).
Decision and route values as in the batch 1 register script.
Writes m08-batch5-register-v1-20261015.csv and checks every scope verse has one row.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. The scoffer: the one who will not be taught'
G2 = 'II. Mocking another'
G3 = 'III. Mocking God\'s messengers and word'
G4 = 'IV. Jesus mocked and laughed at'
G5 = 'V. God\'s laughter and derision'
G6 = 'VI. Made a byword'
G7 = 'VII. Other senses'
M2 = 'carried (M09 batch 2 register)'
R = [
 # I
 ('Pro 13:1', G1, 'read', 'B', '"a scoffer does not listen to rebuke"'),
 ('Pro 15:12', G1, 'read', 'B', '"A scoffer does not like to be reproved; he will not go to the wise"; "how much more the hearts" (15:11)'),
 ('Pro 9:7', G1, 'read', 'B', '"Whoever corrects a scoffer gets himself abuse"'),
 ('Pro 9:8', G1, 'read', 'B', '"Do not reprove a scoffer, or he will hate you; reprove a wise man, and he will love you"'),
 ('Pro 14:6', G1, 'read', 'B', '"A scoffer seeks wisdom in vain"'),
 ('Pro 19:25', G1, 'read', 'B', '"Strike a scoffer, and the simple will learn prudence"'),
 ('Pro 21:11', G1, 'read', 'B', '"When a scoffer is punished, the simple becomes wise"'),
 ('Pro 22:10', G1, 'read', 'B', '"Drive out a scoffer, and strife will go out"'),
 ('Pro 24:9', G1, 'read', 'B', '"the scoffer is an abomination to mankind"'),
 ('Pro 19:28', G1, 'read', 'B', '"A worthless witness mocks at justice"'),
 ('Pro 19:29', G1, 'read', 'B', '"Condemnation is ready for scoffers"'),
 ('Pro 1:22', G1, 'read', 'A B', '"How long will scoffers delight in their scoffing"; "If you turn at my reproof, behold, I will pour out my spirit to you" (1:23)'),
 ('Pro 9:12', G1, 'read', 'B', '"if you scoff, you alone will bear it"'),
 ('Pro 14:9', G1, 'read', 'B', '"Fools mock at the guilt offering, but the upright enjoy acceptance"'),
 ('Pro 20:1', G1, 'read', 'B', '"Wine is a mocker, strong drink a brawler, and whoever is led astray by it is not wise"'),
 ('Psa 1:1', G1, 'read', 'B', '"nor sits in the seat of scoffers; but his delight is in the law of the Lord" (1:2)'),
 ('Isa 28:22', G1, 'read', 'A B', '"do not scoff, lest your bonds be made strong"; "Give ear, and hear my voice" (28:23)'),
 ('Isa 29:20', G1, 'read', 'A B', '"the scoffer cease ... who by a word make a man out to be an offender"; the meek obtain fresh joy (29:19)'),
 ('Hos 7:5', G1, 'read', 'B', '"he stretched out his hand with mockers"; "none of them calls upon me" (7:7)'),
 ('Job 36:18', G1, 'read', 'B', 'Elihu to Job: "Beware lest wrath entice you into scoffing"'),
 ('Job 11:3', G1, 'read', 'B', 'Zophar to Job: "when you mock, shall no one shame you?"'),
 ('Job 21:3', G1, 'read', 'B', 'Job: "Bear with me, and I will speak, and after I have spoken, mock on"'),
 ('Pro 3:34', G1, M2, 'A B', '"Toward the scorners he is scornful, but to the humble he gives favor"'),
 # II
 ('Pro 17:5', G2, 'read', 'A B', '"Whoever mocks the poor insults his Maker; he who is glad at calamity will not go unpunished"'),
 ('Pro 30:17', G2, 'read', 'B', '"The eye that mocks a father and scorns to obey a mother"'),
 ('2Ki 2:23', G2, 'read', 'B', '"some small boys came out of the city and jeered at him, saying, Go up, you baldhead!"'),
 ('Neh 2:19', G2, 'read', 'B', '"they jeered at us and despised us"; "The God of heaven will make us prosper" (2:20)'),
 ('Neh 4:1', G2, 'read', 'B', '"he was angry and greatly enraged, and he jeered at the Jews"; "What are these feeble Jews doing?" (4:2)'),
 ('Job 16:20', G2, 'read', 'A B', '"My friends scorn me; my eye pours out tears to God"; "my witness is in heaven" (16:19)'),
 ('Job 22:19', G2, 'read', 'B', 'Eliphaz: "The righteous see it and are glad; the innocent one mocks at them"'),
 ('Psa 22:7', G2, 'read', 'A B', '"All who see me mock me ... He trusts in the Lord; let him deliver him" (22:8); "Yet you are he who took me from the womb" (22:9)'),
 ('Psa 80:6', G2, 'read', 'A B', '"our enemies laugh among themselves"; "Restore us, O God of hosts" (80:7)'),
 ('Jer 20:7', G2, 'read', 'A B', '"I have become a laughingstock all the day; everyone mocks me"; the word as "a burning fire shut up in my bones" (20:9)'),
 ('Luk 14:29', G2, 'read', 'B', '"all who see it begin to mock him, saying, This man began to build and was not able to finish"'),
 ('Hab 1:10', G2, 'read', 'B', '"At kings they scoff, and at rulers they laugh"; "whose own might is their god" (1:11)'),
 ('Eze 22:5', G2, 'read', 'A B', '"Those who are near and those who are far from you will mock you; your name is defiled"'),
 ('1Ki 18:27', G2, 'read', 'A B', 'Elijah mocked them: "Cry aloud, for he is a god ... perhaps he is asleep"; "there was no voice. No one answered" (18:29)'),
 ('2Ki 19:21', G2, 'read', 'A B', '"She despises you, she scorns you — the virgin daughter of Zion": the mocker of the Lord is scorned'),
 ('Isa 37:22', G2, 'read', 'A B', 'as 2Ki 19:21'),
 ('Gen 27:12', G2, 'read', 'B', 'Jacob: "I shall seem to be mocking him and bring a curse upon myself"'),
 ('Mat 2:16', G2, 'read', 'B', '"when he saw that he had been tricked by the wise men, became furious"'),
 ('Job 9:23', G2, 'read', 'A B', 'Job in anguish: "he mocks at the calamity of the innocent"; held as Job\'s complaint, not a statement about God'),
 ('Eze 16:31', G2, 'read', 'B', '"you were not like a prostitute, because you scorned payment"; she gave gifts to lovers (16:33)'),
 # III
 ('2Ch 36:16', G3, 'read', 'A B', '"they kept mocking the messengers of God, despising his words and scoffing at his prophets, until ... there was no remedy"; he "had compassion" (36:15)'),
 ('2Ch 30:10', G3, 'read', 'B', '"they laughed them to scorn and mocked them. However, some men ... humbled themselves" (30:11)'),
 ('Gal 6:7', G3, 'read', 'A B', '"Do not be deceived: God is not mocked, for whatever one sows, that will he also reap"'),
 # IV
 ('Mat 20:19', G4, 'read', 'A B', 'foretold: "deliver him over to the Gentiles to be mocked and flogged and crucified, and he will be raised"'),
 ('Mar 10:34', G4, 'read', 'A B', 'foretold: "they will mock him and spit on him"'),
 ('Luk 18:32', G4, 'read', 'A B', 'foretold: "will be mocked and shamefully treated"; "they understood none of these things" (18:34)'),
 ('Luk 22:63', G4, 'read', 'A B', '"mocking him as they beat him ... Prophesy! Who is it that struck you?"'),
 ('Luk 23:11', G4, 'read', 'A B', '"Herod with his soldiers treated him with contempt and mocked him"; "he made no answer" (23:9)'),
 ('Luk 23:36', G4, 'read', 'A B', '"The soldiers also mocked him"; "Father, forgive them, for they know not what they do" (23:34)'),
 ('Mar 15:20', G4, 'read', 'A B', '"when they had mocked him, they stripped him of the purple cloak"'),
 ('Mar 15:31', G4, 'read', 'A B', '"He saved others; he cannot save himself"'),
 ('Mat 27:29', G4, 'read', 'A B', '"kneeling before him, they mocked him, saying, Hail, King of the Jews!"'),
 ('Mat 27:31', G4, 'read', 'A B', '"when they had mocked him ... led him away to crucify him"'),
 ('Mat 27:41', G4, 'read', 'A B', '"He trusts in God; let God deliver him now, if he desires him" (27:43)'),
 ('Mat 9:24', G4, 'read', 'A B', '"the girl is not dead but sleeping. And they laughed at him"'),
 ('Mar 5:40', G4, 'read', 'A B', '"And they laughed at him. But he put them all outside"'),
 ('Luk 8:53', G4, 'read', 'A B', '"they laughed at him, knowing that she was dead"'),
 # V
 ('Psa 2:4', G5, 'read', 'A', '"He who sits in the heavens laughs; the Lord holds them in derision": the kings set against the Lord and his Anointed (2:2)'),
 ('Psa 59:8', G5, 'read', 'A', '"But you, O Lord, laugh at them"; they think "Who will hear us?" (59:7)'),
 ('Pro 1:26', G5, 'read', 'A B', 'wisdom: "I also will laugh at your calamity; I will mock when terror strikes you"; "because you have ignored all my counsel" (1:25)'),
 # VI
 ('1Ki 9:7', G6, 'read', 'A B', '"Israel will become a proverb and a byword among all peoples" if they serve other gods'),
 ('2Ch 7:20', G6, 'read', 'A B', 'as 1Ki 9:7: "I will make it a proverb and a byword"'),
 ('Deu 28:37', G6, 'read', 'A B', '"you shall become a horror, a proverb, and a byword"'),
 ('Jer 24:9', G6, 'read', 'A B', '"a reproach, a byword, a taunt, and a curse"; beside 24:7 "I will give them a heart to know me"'),
 ('Eze 5:15', G6, 'read', 'A B', '"You shall be a reproach and a taunt, a warning and a horror, to the nations"'),
 # VII
 ('Gen 42:23', G7, 'data', 'C', '"there was an interpreter between them"'),
 ('Isa 43:27', G7, 'data', 'C', '"your mediators transgressed against me"'),
 ('2Ch 32:31', G7, 'data', 'C', '"the envoys of the princes of Babylon" (the verse is read for its heart-testing elsewhere: 10.11)'),
 ('Isa 33:19', G7, 'data', 'C', '"stammering in a tongue that you cannot understand"'),
 ('Job 33:23', G7, 'read', 'A', '"If there be for him an angel, a mediator, one of the thousand": held for 13.2; the M08 word is "mediator" here'),
]
scope = [r['reference'] for r in csv.DictReader(open(os.path.join(HERE, 'm08-reading-scope-v1-20261015.csv'), encoding='utf-8')) if r['batch'].startswith('5 ')]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)), [x for x in refs if refs.count(x) > 1]
assert set(refs) == set(scope), (set(scope) - set(refs), set(refs) - set(scope))
with open(os.path.join(HERE, 'm08-batch5-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note']); w.writerows(R)
print(len(R), Counter(r[2] for r in R), Counter(r[1] for r in R))
