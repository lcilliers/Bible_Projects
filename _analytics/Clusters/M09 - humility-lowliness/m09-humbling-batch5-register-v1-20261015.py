"""M09 humbling fan-out, batch 5 (submission): one decision per verse (#2148).

Words: G5292 hypotage (M09), G5293 hypotasso (M23), G0506 anypotaktos (M75), G5226 hypeiko (T3);
verses not already in batches 1-4. Each read by Claude in its passage (+-3 verses). Groups emerged from
the reading (m09-humbling-batch5-reading-v1-20261015.md). Writes m09-humbling-batch5-register-v1-20261015.csv.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. Submitting oneself to God, or refusing'
G2 = 'II. Submission among people, and the ground given for it'
G3 = 'III. The insubordinate'
G4 = 'IV. All things subjected to Christ; the Son subject'
G5 = 'V. Spirits and creation subjected'
R = [
 ('Jam 4:7', G1, 'read', 'A B', '"Submit yourselves therefore to God. Resist the devil"; between "gives grace to the humble" (4:6) and "Humble yourselves" (4:10)'),
 ('Heb 12:9', G1, 'read', 'A B', '"Shall we not much more be subject to the Father of spirits and live?" under discipline "for our good" (12:10)'),
 ('Rom 10:3', G1, 'read', 'A B', '"seeking to establish their own, they did not submit to God\'s righteousness"; "zeal for God, but not according to knowledge" (10:2)'),
 ('Rom 8:7', G1, 'read', 'A B', '"the mind that is set on the flesh is hostile to God, for it does not submit to God\'s law; indeed, it cannot"'),
 ('2Cor 9:13', G1, 'read', 'B', '"your submission that comes from your confession of the gospel of Christ, and the generosity of your contribution"'),
 ('Rom 13:1', G2, 'read', 'A B', '"Let every person be subject to the governing authorities. For there is no authority except from God"'),
 ('Rom 13:5', G2, 'read', 'A B', '"not only to avoid God\'s wrath but also for the sake of conscience" (OT-103.44)'),
 ('1Pe 2:13', G2, 'read', 'A B', '"Be subject for the Lord\'s sake to every human institution"; "Live as people who are free ... as servants of God" (2:16)'),
 ('1Pe 2:18', G2, 'read', 'A B', '"Servants, be subject ... not only to the good and gentle but also to the unjust"; "mindful of God"; "Christ also suffered ... leaving you an example" (2:19-21)'),
 ('Tit 3:1', G2, 'read', 'B', '"submissive to rulers and authorities ... ready for every good work"; "For we ourselves were once foolish, disobedient" (3:3)'),
 ('Tit 2:9', G2, 'read', 'B', 'bondservants "submissive ... not argumentative ... so that in everything they may adorn the doctrine of God our Savior"'),
 ('Eph 5:21', G2, 'read', 'B', '"submitting to one another out of reverence for Christ"'),
 ('Eph 5:22', G2, 'read', 'B', '"Wives, submit to your own husbands, as to the Lord"'),
 ('Eph 5:24', G2, 'read', 'B', '"as the church submits to Christ"; "Husbands, love your wives, as Christ loved the church and gave himself up for her" (5:25)'),
 ('Col 3:18', G2, 'read', 'B', '"as is fitting in the Lord"; "Husbands, love your wives, and do not be harsh with them" (3:19)'),
 ('1Pe 3:1', G2, 'read', 'B', '"so that even if some do not obey the word, they may be won without a word by the conduct of their wives"'),
 ('1Pe 3:5', G2, 'read', 'B', '"the holy women who hoped in God used to adorn themselves, by submitting"; "do not fear anything that is frightening" (3:6); husbands "showing honor" (3:7)'),
 ('Tit 2:5', G2, 'read', 'B', '"submissive to their own husbands, that the word of God may not be reviled"'),
 ('1Cor 14:34', G2, 'read', 'B', '"should be in submission, as the Law also says" (order in the assembly; "God is not a God of confusion but of peace", 14:33)'),
 ('1Ti 2:11', G2, 'read', 'B', '"Let a woman learn quietly with all submissiveness"'),
 ('1Cor 16:16', G2, 'read', 'B', '"be subject to such as these": the household of Stephanas, "devoted ... to the service of the saints" (16:15)'),
 ('Heb 13:17', G2, 'read', 'B', '"Obey your leaders and submit to them, for they are keeping watch over your souls, as those who will have to give an account"'),
 ('1Cor 14:32', G2, 'read', 'B', '"the spirits of prophets are subject to prophets": a person\'s own spirit under him, for order and peace'),
 ('Gal 2:5', G2, 'read', 'B', '"to them we did not yield in submission even for a moment, so that the truth of the gospel might be preserved"'),
 ('1Ti 3:4', G2, 'carried', 'C', 'data in the no-other-M-code reading'),
 ('Tit 1:10', G3, 'read', 'B', '"many who are insubordinate, empty talkers and deceivers"'),
 ('Tit 1:6', G3, 'data', 'C', 'children "not open to the charge of debauchery or insubordination" (overseer requirement)'),
 ('1Ti 1:9', G3, 'data', 'C', '"for the lawless and disobedient" (G0506) in the list the law is laid down for'),
 ('1Cor 15:27', G4, 'read', 'A', '"God has put all things in subjection under his feet"; he who subjected is excepted'),
 ('1Cor 15:28', G4, 'read', 'A', '"then the Son himself will also be subjected to him who put all things in subjection under him, that God may be all in all"'),
 ('Eph 1:22', G4, 'read', 'A', '"he put all things under his feet and gave him as head over all things to the church"'),
 ('1Pe 3:22', G4, 'read', 'A', '"at the right hand of God, with angels, authorities, and powers having been subjected to him"'),
 ('Heb 2:5', G4, 'read', 'A', '"it was not to angels that God subjected the world to come"'),
 ('Heb 2:8', G4, 'read', 'A B', '"putting everything in subjection under his feet ... we do not yet see"; "him who for a little while was made lower than the angels, namely Jesus" (2:9)'),
 ('Luk 2:51', G4, 'read', 'A B', '"he went down with them and came to Nazareth and was submissive to them. And his mother treasured up all these things in her heart"'),
 ('Luk 10:17', G5, 'read', 'A B', '"even the demons are subject to us in your name!" (13.3)'),
 ('Luk 10:20', G5, 'read', 'A B', '"do not rejoice in this, that the spirits are subject to you, but rejoice that your names are written in heaven"'),
 ('Rom 8:20', G5, 'read', 'A', '"the creation was subjected to futility, not willingly, but because of him who subjected it, in hope" (13.4)'),
]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)) == 38
with open(os.path.join(HERE, 'm09-humbling-batch5-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note'])
    w.writerows(R)
print(Counter(r[1] for r in R)); print(Counter(r[2] for r in R))
