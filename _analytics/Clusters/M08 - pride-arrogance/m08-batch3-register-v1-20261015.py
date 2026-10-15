"""M08 batch 3 (the Greek pride words and the Greek group B pride-sense verses): one decision per
verse (#2156). Read in passage (m08-batch-pull-v1-20261015.py 3 2); groups emerged from the reading
(m08-batch3-reading-v1-20261015.md). Decision and route values as in the batch 1 register script.
Writes m08-batch3-register-v1-20261015.csv and checks every scope verse has one row.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. Puffed up: knowledge, party, talk'
G2 = 'II. How one thinks of oneself'
G3 = 'III. From the heart, and in the lists'
G4 = 'IV. Opposed, scattered, and the seat of God'
G5 = 'V. Christ preeminent'
M4 = 'carried (M09 batch 4 register)'
R = [
 # I
 ('1Cor 8:1', G1, 'read', 'B', '"This knowledge puffs up, but love builds up"; "if anyone loves God, he is known by God" (8:3)'),
 ('1Cor 4:6', G1, 'read', 'B', '"that none of you may be puffed up in favor of one against another"; 4:7 "What do you have that you did not receive?"'),
 ('1Cor 4:18', G1, 'read', 'B', '"Some are arrogant, as though I were not coming to you"'),
 ('1Cor 4:19', G1, 'read', 'B', '"I will find out not the talk of these arrogant people but their power"'),
 ('1Cor 5:2', G1, 'read', 'B', '"And you are arrogant! Ought you not rather to mourn?"'),
 ('1Cor 13:4', G1, 'read', 'B', '"love does not envy or boast; it is not arrogant"; 13:2 without love "I am nothing"'),
 ('Col 2:18', G1, M4, 'B', '"puffed up without reason by his sensuous mind, and not holding fast to the Head" (2:19)'),
 ('1Ti 3:6', G1, 'read', 'A B', '"not a recent convert, or he may become puffed up with conceit and fall into the condemnation of the devil"'),
 ('1Ti 6:4', G1, 'read', 'B', '"he is puffed up with conceit and understands nothing. He has an unhealthy craving for controversy"'),
 ('2Ti 3:4', G1, 'read', 'B', '"swollen with conceit, lovers of pleasure rather than lovers of God"; "the appearance of godliness" (3:5)'),
 ('2Cor 12:20', G1, 'read', 'B', 'among "quarreling, jealousy, anger, hostility, slander, gossip, conceit, and disorder"'),
 ('Gal 5:26', G1, 'read', 'B', '"Let us not become conceited, provoking one another, envying one another"; keep in step with the Spirit (5:25)'),
 # II
 ('Rom 12:3', G2, 'read', 'A B', '"not to think of himself more highly than he ought to think, but to think with sober judgment, each according to the measure of faith that God has assigned"'),
 ('Rom 12:16', G2, M4, 'B', '"Do not be haughty, but associate with the lowly. Never be wise in your own sight"'),
 ('Rom 11:20', G2, 'read', 'A B', '"So do not become proud, but fear"; 11:18 "it is not you who support the root, but the root that supports you"'),
 ('2Cor 10:5', G2, 'read', 'B', '"every lofty opinion raised against the knowledge of God, and take every thought captive to obey Christ"'),
 ('2Cor 12:7', G2, 'read', 'A B', '"to keep me from becoming conceited because of the surpassing greatness of the revelations, a thorn was given me"; "my power is made perfect in weakness" (12:9)'),
 ('1Ti 6:17', G2, 'read', 'A B', '"charge them not to be haughty, nor to set their hopes on the uncertainty of riches, but on God, who richly provides"'),
 # III
 ('Mar 7:22', G3, 'read', 'B', '"from within, out of the heart of man, come ... pride, foolishness. All these evil things come from within"'),
 ('Rom 1:30', G3, 'read', 'A B', '"insolent, haughty, boastful": after "they did not see fit to acknowledge God" (1:28)'),
 ('2Ti 3:2', G3, 'read', 'B', '"lovers of self, lovers of money, proud, arrogant"; "lovers of pleasure rather than lovers of God" (3:4)'),
 ('1Jo 2:16', G3, 'read', 'A B', '"the desires of the flesh and the desires of the eyes and pride of life — is not from the Father but is from the world"'),
 ('Tit 1:7', G3, 'read', 'B', 'an overseer "as God\'s steward ... must not be arrogant [self-willed]"'),
 ('2Pe 2:10', G3, 'read', 'A B', '"Bold and willful, they do not tremble as they blaspheme the glorious ones"; angels greater in might do not (2:11)'),
 # IV
 ('Jam 4:6', G4, M4, 'A B', '"God opposes the proud but gives grace to the humble"'),
 ('1Pe 5:5', G4, M4, 'A B', 'as Jam 4:6, with "Clothe yourselves, all of you, with humility"'),
 ('Luk 1:51', G4, 'read', 'A B', '"he has scattered the proud in the thoughts of their hearts"; "exalted those of humble estate" (1:52)'),
 ('Luk 16:15', G4, 'read', 'A B', '"You are those who justify yourselves before men, but God knows your hearts. For what is exalted among men is an abomination"'),
 ('Jam 4:16', G4, 'read', 'B', '"you boast in your arrogance. All such boasting is evil"; "If the Lord wills" (4:15)'),
 ('2Th 2:4', G4, 'read', 'A B', '"exalts himself against every so-called god ... takes his seat in the temple of God, proclaiming himself to be God"'),
 # V
 ('Col 1:18', G5, 'read', 'A', '"that in everything he might be preeminent"; "in him all the fullness of God was pleased to dwell" (1:19)'),
]
scope = [r['reference'] for r in csv.DictReader(open(os.path.join(HERE, 'm08-reading-scope-v1-20261015.csv'), encoding='utf-8')) if r['batch'].startswith('3 ')]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)), [x for x in refs if refs.count(x) > 1]
assert set(refs) == set(scope), (set(scope) - set(refs), set(refs) - set(scope))
with open(os.path.join(HERE, 'm08-batch3-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note']); w.writerows(R)
print(len(R), Counter(r[2] for r in R), Counter(r[1] for r in R))
