"""M08 batch 4 (boasting, group C): one decision per verse (#2156). Read in passage
(m08-batch-pull-v1-20261015.py 4 2); groups emerged from the reading (m08-batch4-reading-v1-20261015.md).
Decision and route values as in the batch 1 register script.
Writes m08-batch4-register-v1-20261015.csv and checks every scope verse has one row.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. Boasting in oneself and what one has'
G2 = 'II. Boasting excluded: the gift and the measure'
G3 = 'III. Boasting in the Lord'
G4 = 'IV. Boasting in weakness'
G5 = 'V. Boasting of others'
G6 = 'VI. Mercy triumphs'
M2 = 'carried (M09 batch 2 register)'
M4 = 'carried (M09 batch 4 register)'
R = [
 # I
 ('Jer 9:23', G1, 'read', 'B', '"Let not the wise man boast in his wisdom, let not the mighty man boast in his might, let not the rich man boast in his riches"'),
 ('Psa 49:6', G1, 'read', 'B', '"those who trust in their wealth and boast of the abundance of their riches"; "no man can ransom another" (49:7)'),
 ('Jer 49:4', G1, 'read', 'B', '"Why do you boast of your valleys ... who trusted in her treasures, saying, Who will come against me?"'),
 ('Psa 52:1', G1, 'read', 'A B', '"Why do you boast of evil, O mighty man? The steadfast love of God endures all the day"'),
 ('Psa 10:3', G1, 'read', 'B', '"the wicked boasts of the desires of his soul"'),
 ('1Ki 20:11', G1, 'read', 'B', '"Let not him who straps on his armor boast himself as he who takes it off"'),
 ('Pro 27:1', G1, 'read', 'B', '"Do not boast about tomorrow ... Let another praise you, and not your own mouth" (27:2)'),
 ('Pro 25:14', G1, 'read', 'B', '"a man who boasts of a gift he does not give"'),
 ('Pro 20:14', G1, 'read', 'B', '"Bad, bad, says the buyer, but when he goes away, then he boasts"'),
 ('Jam 3:5', G1, 'read', 'B', '"the tongue is a small member, yet it boasts of great things"'),
 ('Jam 3:14', G1, 'read', 'B', '"if you have bitter jealousy and selfish ambition in your hearts, do not boast and be false to the truth"'),
 ('2Pe 2:18', G1, 'read', 'B', '"speaking loud boasts of folly, they entice by sensual passions"'),
 ('Jude 16', G1, 'read', 'B', '"grumblers, malcontents ... loud-mouthed boasters, showing favoritism to gain advantage"'),
 ('Psa 97:7', G1, 'read', 'A B', '"All worshipers of images are put to shame, who make their boast in worthless idols"; "you, O Lord, are most high" (97:9)'),
 ('1Cor 5:6', G1, 'read', 'B', '"Your boasting is not good. Do you not know that a little leaven leavens the whole lump?"'),
 ('Gal 6:13', G1, 'read', 'B', '"they desire to have you circumcised that they may boast in your flesh"; "a good showing in the flesh" (6:12)'),
 ('2Cor 11:12', G1, 'read', 'B', '"those who would like to claim that in their boasted mission they work on the same terms as we do" (OT-97 M18 forward)'),
 ('2Cor 11:18', G1, 'read', 'B', '"Since many boast according to the flesh, I too will boast"'),
 ('2Cor 5:12', G1, 'read', 'B', '"those who boast about outward appearance and not about what is in the heart"'),
 ('Rom 2:17', G1, 'read', 'A B', '"if you call yourself a Jew and rely on the law and boast in God"; "do you not teach yourself?" (2:21)'),
 ('Rom 2:23', G1, 'read', 'A B', '"You who boast in the law dishonor God by breaking the law"'),
 # II
 ('1Cor 1:29', G2, 'read', 'A B', '"so that no human being might boast in the presence of God"; God chose the foolish, weak, low (1:27-28)'),
 ('1Cor 4:7', G2, 'read', 'B', '"What do you have that you did not receive? If then you received it, why do you boast as if you did not receive it?"'),
 ('Eph 2:9', G2, 'read', 'A B', '"not a result of works, so that no one may boast"; "it is the gift of God" (2:8)'),
 ('Rom 3:27', G2, 'read', 'A B', '"Then what becomes of our boasting? It is excluded ... by the law of faith"'),
 ('Rom 4:2', G2, 'read', 'A B', '"if Abraham was justified by works, he has something to boast about, but not before God"'),
 ('1Cor 3:21', G2, 'read', 'B', '"let no one boast in men. For all things are yours ... and you are Christ\'s, and Christ is God\'s"'),
 ('Rom 11:18', G2, 'read', 'B', '"do not be arrogant toward the branches ... it is not you who support the root, but the root that supports you"'),
 ('Gal 6:4', G2, 'read', 'B', '"let each one test his own work, and then his reason to boast will be in himself alone and not in his neighbor"; 6:3 "thinks he is something, when he is nothing"'),
 ('2Cor 10:13', G2, 'read', 'A B', '"we will not boast beyond limits, but will boast only with regard to the area of influence God assigned to us"'),
 ('2Cor 10:15', G2, 'read', 'B', '"We do not boast beyond limit in the labors of others"'),
 ('2Cor 10:16', G2, 'read', 'B', '"without boasting of work already done in another\'s area of influence"'),
 ('1Cor 9:15', G2, 'read', 'B', '"I would rather die than have anyone deprive me of my ground for boasting": preaching free of charge (9:18)'),
 ('1Cor 9:16', G2, 'read', 'B', '"if I preach the gospel, that gives me no ground for boasting. For necessity is laid upon me"'),
 # III
 ('1Cor 1:31', G3, 'read', 'A B', '"Let the one who boasts, boast in the Lord"; Christ "became to us wisdom from God" (1:30)'),
 ('2Cor 10:17', G3, 'read', 'A B', 'as 1Co 1:31; "not the one who commends himself ... but the one whom the Lord commends" (10:18)'),
 ('Jer 9:24', G3, 'read', 'A B', '"let him who boasts boast in this, that he understands and knows me, that I am the Lord who practices steadfast love, justice, and righteousness"'),
 ('Psa 34:2', G3, M2, 'A B', '"My soul makes its boast in the Lord; let the humble hear and be glad"'),
 ('Psa 44:8', G3, 'read', 'A B', '"In God we have boasted continually"; "not in my bow do I trust" (44:6); then "But you have rejected us" (44:9)'),
 ('Psa 105:3', G3, 'read', 'A B', '"Glory in his holy name; let the hearts of those who seek the Lord rejoice!"'),
 ('1Ch 16:10', G3, 'read', 'A B', 'as Psa 105:3'),
 ('Isa 41:16', G3, 'read', 'A B', '"you shall rejoice in the Lord; in the Holy One of Israel you shall glory"; "Fear not, you worm Jacob" (41:14)'),
 ('Isa 45:25', G3, 'read', 'A B', '"In the Lord all the offspring of Israel shall be justified and shall glory"; "Only in the Lord ... are righteousness and strength" (45:24)'),
 ('Jer 4:2', G3, 'read', 'A B', 'if you return and swear in truth, "nations shall bless themselves in him, and in him shall they glory"'),
 ('Psa 63:11', G3, 'read', 'A B', '"all who swear by him shall exult"'),
 ('Psa 64:10', G3, 'read', 'A B', '"Let the righteous one rejoice in the Lord and take refuge in him! Let all the upright in heart exult!"'),
 ('Psa 106:5', G3, 'read', 'A B', '"that I may glory with your inheritance"'),
 ('Gal 6:14', G3, 'read', 'A B', '"far be it from me to boast except in the cross of our Lord Jesus Christ"'),
 ('Phili 3:3', G3, 'read', 'A B', '"glory in Christ Jesus and put no confidence in the flesh"; "I have more" (3:4)'),
 ('Rom 5:2', G3, 'read', 'A B', '"we rejoice [boast] in hope of the glory of God"'),
 ('Rom 5:3', G3, 'read', 'A B', '"we rejoice [boast] in our sufferings, knowing that suffering produces endurance"'),
 ('Rom 5:11', G3, 'read', 'A B', '"we also rejoice [boast] in God through our Lord Jesus Christ, through whom we have now received reconciliation"'),
 ('Heb 3:6', G3, 'read', 'A B', '"if indeed we hold fast our confidence and our boasting in our hope"'),
 ('2Cor 1:12', G3, 'read', 'A B', '"our boast is this, the testimony of our conscience ... not by earthly wisdom but by the grace of God"'),
 # IV
 ('2Cor 11:16', G4, 'read', 'B', '"accept me as a fool, so that I too may boast a little"'),
 ('2Cor 11:17', G4, 'read', 'B', '"What I am saying with this boastful confidence, I say not as the Lord would but as a fool"'),
 ('2Cor 11:30', G4, 'read', 'B', '"If I must boast, I will boast of the things that show my weakness"'),
 ('2Cor 12:1', G4, 'read', 'B', '"I must go on boasting. Though there is nothing to be gained by it"'),
 ('2Cor 12:5', G4, 'read', 'B', '"on my own behalf I will not boast, except of my weaknesses"'),
 ('2Cor 12:6', G4, 'read', 'B', '"I refrain from it, so that no one may think more of me than he sees in me or hears from me" (OT-97 M18 forward)'),
 ('2Cor 12:9', G4, 'read', 'A B', '"I will boast all the more gladly of my weaknesses, so that the power of Christ may rest upon me"'),
 ('2Cor 10:8', G4, 'read', 'A B', '"if I boast a little too much of our authority, which the Lord gave for building you up and not for destroying you"'),
 ('2Cor 11:10', G4, 'read', 'B', '"this boasting of mine will not be silenced": serving without burdening them (11:9)'),
 # V
 ('2Cor 7:4', G5, 'read', 'B', '"I have great pride in you; I am filled with comfort. In all our affliction, I am overflowing with joy"'),
 ('2Cor 7:14', G5, 'read', 'B', '"whatever boasts I made to him about you, I was not put to shame"'),
 ('2Cor 8:24', G5, 'read', 'B', '"give proof before the churches of your love and of our boasting about you"'),
 ('2Cor 9:2', G5, 'read', 'B', '"your readiness, of which I boast about you"; "your zeal has stirred up most of them"'),
 ('2Cor 9:3', G5, 'read', 'B', '"so that our boasting about you may not prove empty"'),
 ('2Cor 9:4', G5, 'read', 'B', '"we would be humiliated ... for being so confident"'),
 ('2Cor 1:14', G5, 'read', 'B', '"on the day of our Lord Jesus you will boast of us as we will boast of you"'),
 ('1Th 2:19', G5, 'read', 'B', '"what is our hope or joy or crown of boasting before our Lord Jesus at his coming? Is it not you?"'),
 ('2Th 1:4', G5, 'read', 'B', '"we ourselves boast about you in the churches of God for your steadfastness and faith"'),
 ('Phili 1:26', G5, 'read', 'B', '"so that in me you may have ample cause to glory in Christ Jesus"'),
 ('Phili 2:16', G5, 'read', 'B', '"so that in the day of Christ I may be proud that I did not run in vain"'),
 ('Rom 15:17', G5, 'read', 'B', '"I have reason to be proud of my work for God ... what Christ has accomplished through me" (15:18)'),
 ('1Cor 15:31', G5, 'read', 'B', '"by my pride in you, which I have in Christ Jesus our Lord, I die every day!"'),
 ('Jam 1:9', G5, M4, 'B', '"Let the lowly brother boast in his exaltation, and the rich in his humiliation"'),
 # VI
 ('Jam 2:13', G6, 'read', 'A B', '"judgment is without mercy to one who has shown no mercy. Mercy triumphs over judgment"'),
]
scope = [r['reference'] for r in csv.DictReader(open(os.path.join(HERE, 'm08-reading-scope-v1-20261015.csv'), encoding='utf-8')) if r['batch'].startswith('4 ')]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)), [x for x in refs if refs.count(x) > 1]
assert set(refs) == set(scope), (set(scope) - set(refs), set(refs) - set(scope))
with open(os.path.join(HERE, 'm08-batch4-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note']); w.writerows(R)
print(len(R), Counter(r[2] for r in R), Counter(r[1] for r in R))
