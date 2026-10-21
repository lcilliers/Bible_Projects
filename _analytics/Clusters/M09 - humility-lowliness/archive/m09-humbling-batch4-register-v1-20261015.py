"""M09 humbling fan-out, batch 4 (Greek humility and meekness): one decision per verse (#2148).

Words: G5011-G5014 tapein- (M09), G0036 (M09), the praus family G4235/G4236/G4239/G4240 (M05),
G5391 "humble mind" (M05); verses not already in batches 1-3. Each read by Claude in its passage
(-4/+3 verses). Groups emerged from the reading (m09-humbling-batch4-reading-v1-20261015.md).
Decision values as before; 'thread' = carried by an open thread (here OT-05).
Writes m09-humbling-batch4-register-v1-20261015.csv.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. Humbling oneself, and being exalted'
G2 = 'II. Christ lowly, humbled, meek'
G3 = 'III. Humility toward one another'
G4 = 'IV. Gentleness and meekness in how one meets others and the word'
G5 = 'V. A low estate, and where the boast goes'
G6 = 'VI. The humility-word turned to a show'
G7 = 'VII. Other'
R = [
 ('Luk 18:14', G1, 'read', 'A B', 'the tax collector "standing far off ... beat his breast ... God, be merciful to me, a sinner!" against "I am not like other men"; justified'),
 ('Mat 18:4', G1, 'read', 'B', '"Whoever humbles himself like this child is the greatest"; "unless you turn and become like children" (18:3)'),
 ('Mat 23:12', G1, 'carried', 'B', 'no-other-M-code reading, group A'),
 ('Luk 14:11', G1, 'carried', 'B', 'no-other-M-code reading, group A'),
 ('Jam 4:10', G1, 'carried', 'A B', 'no-other-M-code reading, group A'),
 ('1Pe 5:6', G1, 'read', 'A B', '"Humble yourselves ... under the mighty hand of God ... casting all your anxieties on him, because he cares for you" (5:6-7)'),
 ('Jam 4:6', G1, 'read', 'A B', '"God opposes the proud but gives grace to the humble" (Pro 3:34); after the passions at war, friendship with the world (4:1-4)'),
 ('Phili 2:8', G2, 'read', 'A B', '"he humbled himself by becoming obedient to the point of death"; emptied himself, form of a servant (2:6-7); therefore God exalted him (2:9)'),
 ('Mat 11:29', G2, 'read', 'A B', '"learn from me, for I am gentle and lowly in heart, and you will find rest for your souls"'),
 ('Mat 21:5', G2, 'read', 'A', '"your king is coming to you, humble, and mounted on a donkey" (Zec 9:9 fulfilled)'),
 ('Act 8:33', G2, 'read', 'A', '"In his humiliation justice was denied him" (Isa 53), the lamb that is silent (8:32)'),
 ('2Cor 10:1', G2, 'read', 'A B', '"by the meekness and gentleness of Christ"; Paul quotes the charge "humble when face to face with you, but bold ... when I am away"'),
 ('Phili 2:3', G3, 'read', 'B', '"Do nothing from selfish ambition or conceit, but in humility count others more significant than yourselves"; "Have this mind ... which is yours in Christ Jesus" (2:5)'),
 ('Rom 12:16', G3, 'read', 'B', '"Do not be haughty, but associate with the lowly. Never be wise in your own sight."'),
 ('Eph 4:2', G3, 'read', 'B', '"with all humility and gentleness, with patience, bearing with one another in love"; eager to maintain unity (4:3)'),
 ('Col 3:12', G3, 'read', 'B', '"Put on ... compassionate hearts, kindness, humility, meekness, and patience"; bearing with, forgiving (3:13)'),
 ('1Pe 3:8', G3, 'read', 'B', '"unity of mind, sympathy, brotherly love, a tender heart, and a humble mind"; not repaying evil (3:9)'),
 ('1Pe 5:5', G3, 'read', 'A B', '"Clothe yourselves, all of you, with humility toward one another"; elders "not domineering" (5:3)'),
 ('Act 20:19', G3, 'read', 'B', 'Paul "serving the Lord with all humility and with tears and with trials"'),
 ('Gal 6:1', G4, 'read', 'B', '"restore him in a spirit of gentleness. Keep watch on yourself, lest you too be tempted"; "if anyone thinks he is something, when he is nothing" (6:3)'),
 ('2Ti 2:25', G4, 'read', 'A B', '"correcting his opponents with gentleness. God may perhaps grant them repentance"'),
 ('1Pe 3:15', G4, 'read', 'B', '"make a defense ... yet do it with gentleness and respect"'),
 ('1Cor 4:21', G4, 'read', 'B', '"Shall I come to you with a rod, or with love in a spirit of gentleness?" to the arrogant (4:18-19)'),
 ('Tit 3:2', G4, 'read', 'B', '"to be gentle, and to show perfect courtesy toward all people. For we ourselves were once foolish" (3:3)'),
 ('Jam 3:13', G4, 'read', 'B', '"show his works in the meekness of wisdom"; against "bitter jealousy and selfish ambition in your hearts" (3:14)'),
 ('Jam 1:21', G4, 'read', 'A B', '"receive with meekness the implanted word"; "quick to hear, slow to speak, slow to anger" (1:19)'),
 ('1Pe 3:4', G4, 'read', 'A B', '"the hidden person of the heart with the imperishable beauty of a gentle and quiet spirit, which in God\'s sight is very precious"'),
 ('Gal 5:23', G4, 'read', 'A B', 'gentleness in "the fruit of the Spirit"; "Let us not become conceited" (5:26)'),
 ('1Ti 6:11', G4, 'read', 'B', '"Pursue righteousness, godliness, faith, love, steadfastness, gentleness" against the love of money (6:10)'),
 ('Mat 5:5', G4, 'read', 'A B', '"Blessed are the meek, for they shall inherit the earth" beside "poor in spirit" (5:3), "those who mourn" (5:4)'),
 ('Jam 1:9', G5, 'read', 'B', '"Let the lowly brother boast in his exaltation"'),
 ('Jam 1:10', G5, 'read', 'B', '"and the rich in his humiliation, because like a flower of the grass he will pass away"'),
 ('Luk 1:48', G5, 'read', 'A B', '"he has looked on the humble estate of his servant"'),
 ('Luk 1:52', G5, 'carried', 'A B', 'no-other-M-code reading, group A'),
 ('1Cor 1:28', G5, 'read', 'A B', '"God chose what is low and despised in the world ... so that no human being might boast"; "boast in the Lord" (1:29-31)'),
 ('2Cor 7:6', G5, 'read', 'A B', '"God, who comforts the downcast, comforted us by the coming of Titus"; "fear within" (7:5)'),
 ('Phili 4:12', G5, 'read', 'B', '"I know how to be brought low, and I know how to abound"; "I have learned ... to be content" (4:11)'),
 ('2Cor 11:7', G5, 'read', 'B', '"humbling myself so that you might be exalted, because I preached God\'s gospel to you free of charge"'),
 ('2Cor 12:21', G5, 'read', 'A B', '"my God may humble me before you, and I may have to mourn over many ... who ... have not repented"'),
 ('Col 2:18', G6, 'read', 'B', '"insisting on asceticism ... puffed up without reason by his sensuous mind" (G5012, the humility noun)'),
 ('Col 2:23', G6, 'read', 'B', '"self-made religion and asceticism and severity to the body, but they are of no value in stopping the indulgence of the flesh"'),
 ('Phili 3:21', G7, 'thread', 'A B', '"our lowly body" transformed: OT-05 (the body raised) already holds this word'),
 ('Luk 3:5', G7, 'data', 'C', '"every mountain and hill shall be made low" (Isa 40:4 quoted)'),
]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)) == 43
with open(os.path.join(HERE, 'm09-humbling-batch4-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note'])
    w.writerows(R)
print(Counter(r[1] for r in R)); print(Counter(r[2] for r in R))
