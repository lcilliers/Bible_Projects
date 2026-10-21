"""M09 humbling fan-out, batch 1 (Hebrew humbling and bringing low): one decision per verse (#2148).

Every verse was read by Claude in its passage (scratch pull of the batch-1 verses with +-3 verses).
Groups are the phenomena that emerged from the reading, not a frame laid over it (see the reading
m09-humbling-batch1-reading-v1-20261015.md). Decision values:
  read     read for the humbling act; carried into the account
  carried  already read in the no-other-M-code reading (m09-no-other-mcode-reading-v1-20261015.md)
  forward  the passage joins another inner act that is not humbling; marked for that strand
  data     no inner-being bearing for this study (route C)
Route: A = God / other beings (13.x), B = the human inner being, A B = both, C = data.
Writes m09-humbling-batch1-register-v1-20261015.csv.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. Humbling oneself before God'
G2 = 'II. God humbles: testing, teaching, answering'
G3 = 'III. The proud brought low, the lowly raised'
G4 = 'IV. Taking the lower place'
G5 = 'V. Humbled or made to submit by another person'
G6 = 'VI. Subdued in war'
G7 = 'VII. Low in other senses'
R = [
 # I
 ('2Ch 12:6', G1, 'read', 'B', 'king and princes humbled themselves and said "The Lord is righteous" after "You abandoned me"'),
 ('2Ch 12:7', G1, 'read', 'A B', '"When the Lord saw that they humbled themselves" : some deliverance, yet servants (12:8)'),
 ('2Ch 12:12', G1, 'read', 'A B', 'wrath turned; then 12:14 "he did not set his heart to seek the Lord"'),
 ('2Ch 32:26', G1, 'read', 'A B', 'Hezekiah humbled himself "for the pride of his heart" (32:25)'),
 ('1Ki 21:29', G1, 'read', 'A B', '"Have you seen how Ahab has humbled himself before me?" sackcloth, fasting, dejected (21:27)'),
 ('2Ki 22:19', G1, 'read', 'A B', 'Josiah: heart penitent, humbled himself when he heard, tore clothes, wept; "I also have heard you"'),
 ('2Ch 34:27', G1, 'read', 'A B', 'parallel: "your heart was tender"'),
 ('2Ch 33:12', G1, 'read', 'A B', 'Manasseh in distress entreated and humbled himself greatly; God moved; "Manasseh knew that the Lord was God"'),
 ('2Ch 33:19', G1, 'read', 'B', 'the record: his sin "before he humbled himself"'),
 ('2Ch 33:23', G1, 'read', 'B', 'Amon "did not humble himself ... as Manasseh his father had"; guilt more and more'),
 ('2Ch 36:12', G1, 'read', 'B', 'Zedekiah did not humble himself before Jeremiah; stiffened neck, hardened heart (36:13)'),
 ('2Ch 7:14', G1, 'read', 'A B', 'humble themselves, pray, seek my face, turn : hear, forgive, heal'),
 ('Lev 26:41', G1, 'read', 'A B', '"if then their uncircumcised heart is humbled" with confession (26:40) and amends'),
 ('Dan 10:12', G1, 'read', 'A B', '"set your heart to understand and humbled yourself before your God": heard from the first day'),
 ('Ezr 8:21', G1, 'read', 'A B', 'fast to humble ourselves before God, seeking a safe journey; ashamed to ask the king (8:22)'),
 ('Exo 10:3', G1, 'read', 'A B', '"How long will you refuse to humble yourself before me?" (Pharaoh; hardened heart 10:1)'),
 ('Dan 5:22', G1, 'read', 'B', 'Belshazzar "have not humbled your heart, though you knew all this"; lifted up himself (5:23)'),
 ('Isa 58:3', G1, 'read', 'A B', '"Why have we humbled ourselves, and you take no knowledge of it?" own pleasure, oppress workers'),
 ('Isa 58:5', G1, 'read', 'A B', '"a day for a person to humble himself?" the chosen fast: share bread, cover the naked (58:6-7)'),
 ('2Ch 30:11', G1, 'carried', 'B', 'read in the no-other-M-code reading, group A'),
 # II
 ('Deu 8:2', G2, 'read', 'A B', 'humble you, testing you "to know what was in your heart"'),
 ('Deu 8:3', G2, 'read', 'A B', 'humbled you, let you hunger, fed you manna "that he might make you know"'),
 ('Deu 8:16', G2, 'read', 'A B', '"to humble you and test you, to do you good in the end"; against the heart lifted up (8:14, 17)'),
 ('Deu 9:3', G2, 'read', 'A B', 'God subdues the nations; "Do not say in your heart ... because of my righteousness" (9:4-6)'),
 ('Psa 107:12', G2, 'read', 'A B', '"he bowed their hearts down with hard labor" after rebelling; then they cried (107:13)'),
 ('2Ch 28:19', G2, 'read', 'A B', 'the Lord humbled Judah; Ahaz "in the time of his distress ... yet more faithless" (28:22)'),
 ('Job 30:11', G2, 'read', 'B', '"God has loosed my cord and humbled me" : others cast off restraint, abhor, spit (30:10)'),
 ('Psa 55:19', G2, 'read', 'A B', 'God will humble them "because they do not change and do not fear God"; the false companion (55:20-21)'),
 ('Dan 4:37', G2, 'read', 'A B', '"those who walk in pride he is able to humble" (Nebuchadnezzar, reason returned)'),
 # III
 ('Job 40:11', G3, 'read', 'A B', '"look on everyone who is proud and abase him": God to Job; only then "your own right hand can save you" (40:14)'),
 ('Job 40:12', G3, 'read', 'A B', 'same'),
 ('Pro 29:23', G3, 'read', 'B', '"One\'s pride will bring him low, but he who is lowly in spirit will obtain honor"'),
 ('Pro 16:19', G3, 'read', 'B', '"better to be of a lowly spirit with the poor than to divide the spoil with the proud" (16:18 pride before destruction)'),
 ('Isa 2:9', G3, 'read', 'A B', 'man humbled; land full of silver, gold, idols; bow down to the work of their hands (2:7-8)'),
 ('Isa 2:11', G3, 'read', 'A B', '"haughty looks ... lofty pride ... the Lord alone will be exalted"'),
 ('Isa 2:12', G3, 'read', 'A B', 'a day against all that is proud and lofty'),
 ('Isa 2:17', G3, 'read', 'A B', 'repeats 2:11'),
 ('Isa 5:15', G3, 'read', 'A B', '"the eyes of the haughty are brought low"; revellers who do not regard the deeds of the Lord (5:12)'),
 ('Isa 13:11', G3, 'read', 'A B', '"the pomp of the arrogant ... the pompous pride of the ruthless"'),
 ('Isa 25:11', G3, 'read', 'A B', 'Moab\'s "pompous pride together with the skill of his hands"'),
 ('Isa 10:33', G3, 'read', 'A', 'the lofty hewn down (Assyria, as trees)'),
 ('Isa 26:5', G3, 'read', 'A B', 'the lofty city laid low; "the feet of the poor" trample it (26:6); trust (26:3-4)'),
 ('Job 22:29', G3, 'read', 'B', 'Eliphaz: "when they are humbled you say, \'It is because of pride\'; but he saves the lowly"'),
 ('Psa 147:6', G3, 'read', 'A', '"The Lord lifts up the humble; he casts the wicked to the ground"'),
 ('Psa 75:7', G3, 'read', 'A B', '"putting down one and lifting up another"; to the boastful, "Do not boast" (75:4-6)'),
 ('1Sa 2:7', G3, 'read', 'A', 'Hannah: "The Lord makes poor and makes rich; he brings low and he exalts"'),
 ('Eze 17:24', G3, 'read', 'A', '"I bring low the high tree, and make high the low tree"'),
 ('Eze 21:26', G3, 'read', 'A B', '"Exalt that which is low, and bring low that which is exalted": crown removed from the profane prince'),
 ('2Sa 22:28', G3, 'read', 'A B', '"You save a humble people, but your eyes are on the haughty to bring them down"'),
 ('Psa 18:27', G3, 'read', 'A B', 'parallel: "the haughty eyes you bring down"'),
 ('Dan 4:17', G3, 'read', 'A', '"sets over it the lowliest of men"'),
 # IV
 ('Pro 25:7', G4, 'read', 'B', '"Do not put yourself forward ... better to be told, Come up here, than to be put lower" (cf. Luk 14:8-11)'),
 ('Jer 13:18', G4, 'read', 'B', '"Take a lowly seat" to king and queen mother; "be not proud" (13:15); "my soul will weep in secret for your pride" (13:17)'),
 # V
 ('Judg 16:5', G5, 'read', 'B', 'the lords bribe Delilah to find Samson\'s strength "that we may bind him to humble him"'),
 ('Gen 16:9', G5, 'read', 'A B', '"Return to your mistress and submit to her" after Sarai dealt harshly; "the Lord has listened to your affliction" (16:11)'),
 ('Psa 89:22', G5, 'read', 'A', '"the wicked shall not humble him" (God\'s promise to David)'),
 ('Dan 5:19', G5, 'read', 'A B', 'Nebuchadnezzar "whom he would, he humbled", greatness given by God; then his heart lifted up (5:20)'),
 # VI
 ('Judg 3:30', G6, 'data', 'C', 'Moab subdued'),
 ('Judg 4:23', G6, 'data', 'C', 'God subdued Jabin'),
 ('Judg 8:28', G6, 'data', 'C', 'Midian subdued; Gideon\'s ephod a snare (8:27) not this word'),
 ('Judg 11:33', G6, 'carried', 'C', 'data in the no-other-M-code reading'),
 ('1Sa 7:13', G6, 'data', 'C', 'Philistines subdued (M72 D forward, now decided)'),
 ('2Sa 8:1', G6, 'data', 'C', 'Philistines subdued (M72 D forward, now decided)'),
 ('1Ch 18:1', G6, 'data', 'C', 'parallel (M72 D forward, now decided)'),
 ('1Ch 20:4', G6, 'data', 'C', 'Philistines subdued'),
 ('1Ch 17:10', G6, 'data', 'A', 'God promises to subdue David\'s enemies'),
 ('2Ch 13:18', G6, 'forward', 'B', 'Israel subdued "because they relied on the Lord": reliance, for the trust strand'),
 ('Neh 9:24', G6, 'carried', 'B', 'read and woven in M18 group C (M72 D forward, now decided)'),
 ('Psa 81:14', G6, 'forward', 'A B', '"Israel would not submit to me ... gave them over to their stubborn hearts" (81:11-12): M30'),
 ('Psa 106:42', G6, 'forward', 'A B', '"rebellious in their purposes ... brought low"; he heard their cry (106:43-44): M30 (M72 D forward, now decided)'),
 ('Isa 25:5', G6, 'data', 'A', 'God subdues the foreigners\' noise; 25:4 "a stronghold to the poor" belongs to OT-105'),
 # VII
 ('Psa 113:6', G7, 'read', 'A', '"who looks far down on the heavens and the earth": the same verb, of God looking down; then he raises the poor (113:7)'),
 ('Isa 57:9', G7, 'forward', 'B', '"sent down even to Sheol"; 57:10-11 not saying "hopeless", dread, lying, not remembering: M01, M14'),
 ('Ecc 12:4', G7, 'forward', 'B', 'old age: "all the daughters of song are brought low": M25 (Ch 2)'),
 ('Isa 29:4', G7, 'data', 'C', 'Ariel brought low, speech from the dust'),
 ('Isa 32:19', G7, 'data', 'C', 'city laid low'),
 ('Isa 40:4', G7, 'data', 'C', 'every mountain made low: the way prepared'),
 ('Isa 25:12', G7, 'data', 'C', 'fortifications laid low'),
 ('Dan 7:24', G7, 'data', 'C', 'a king puts down three kings (vision)'),
]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)) == 79, (len(refs), len(set(refs)))
with open(os.path.join(HERE, 'm09-humbling-batch1-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note'])
    w.writerows(R)
print(Counter(r[1] for r in R)); print(Counter(r[2] for r in R))
