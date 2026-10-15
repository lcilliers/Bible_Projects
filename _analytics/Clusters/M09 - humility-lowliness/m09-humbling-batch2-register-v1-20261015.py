"""M09 humbling fan-out, batch 2 (the humble, lowly, meek; humility): one decision per verse (#2148).

Words: H6035, H6041 (humble surface), H8217, H6800A/B, H7807, H6038, H6037; verses not already in batch 1.
Every verse was read by Claude in its passage (+-3 verses). Groups emerged from the reading
(m09-humbling-batch2-reading-v1-20261015.md). Decision values as batch 1, plus:
  thread   the word is in its afflicted/poor sense; the verse is carried by OT-105 (#2149), where the
           poor/needy split already codes it (m09-poor-needy-split-v1-20261015.csv)
Writes m09-humbling-batch2-register-v1-20261015.csv.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. The humble before God: who they are, what he does'
G2 = 'II. Humility: before honor, with the fear of the Lord'
G3 = 'III. A lowly and contrite spirit: where God dwells and looks'
G4 = 'IV. Lowliness in the one who leads, and in God'
G5 = 'V. Made low for what they did'
G6 = 'VI. The same words for the afflicted and poor'
G7 = 'VII. Data'
R = [
 ('Zep 2:3', G1, 'read', 'B', '"Seek the Lord, all you humble of the land ... seek humility": the humble are told to seek humility'),
 ('Zep 3:12', G1, 'read', 'A B', '"a people humble and lowly. They shall seek refuge" after the "proudly exultant ones" removed (3:11); no injustice, no lies (3:13)'),
 ('Psa 149:4', G1, 'read', 'A', '"the Lord takes pleasure in his people; he adorns the humble with salvation"'),
 ('Psa 25:9', G1, 'read', 'A B', '"He leads the humble in what is right, and teaches the humble his way"; the speaker asks pardon (25:7, 11)'),
 ('Pro 3:34', G1, 'read', 'A B', '"Toward the scorners he is scornful, but to the humble he gives favor"'),
 ('Psa 76:9', G1, 'read', 'A', '"God arose to establish judgment, to save all the humble of the earth"'),
 ('Isa 29:19', G1, 'read', 'A B', '"The meek shall obtain fresh joy in the Lord"; the scoffer ceases (29:20)'),
 ('Psa 37:11', G1, 'read', 'B', '"the meek shall inherit the land"; "Refrain from anger ... Fret not yourself" (37:8); "those who wait for the Lord" (37:9)'),
 ('Psa 138:6', G1, 'read', 'A B', '"though the Lord is high, he regards the lowly, but the haughty he knows from afar"'),
 ('Job 5:11', G1, 'read', 'A', 'Eliphaz: "he sets on high those who are lowly, and those who mourn are lifted to safety"'),
 ('Psa 34:2', G1, 'read', 'B', '"My soul makes its boast in the Lord; let the humble hear and be glad"; "I sought the Lord, and he answered me" (34:4)'),
 ('Psa 69:32', G1, 'read', 'B', '"When the humble see it they will be glad; you who seek God, let your hearts revive"; the speaker "afflicted and in pain" (69:29)'),
 ('Isa 11:4', G1, 'read', 'A', '"decide with equity for the meek of the earth": the shoot of Jesse, who will not judge by what his eyes see (11:3)'),
 ('Pro 15:33', G2, 'read', 'B', '"The fear of the Lord is instruction in wisdom, and humility comes before honor"; listening to reproof (15:31-32)'),
 ('Pro 18:12', G2, 'read', 'B', '"Before destruction a man\'s heart is haughty, but humility comes before honor"; answering before hearing (18:13)'),
 ('Pro 22:4', G2, 'read', 'B', '"The reward for humility and fear of the Lord is riches and honor and life"'),
 ('Pro 11:2', G2, 'read', 'B', '"When pride comes, then comes disgrace, but with the humble is wisdom"'),
 ('Mic 6:8', G2, 'read', 'A B', '"to walk humbly with your God", answering "With what shall I come before the Lord ... burnt offerings?" (6:6-7)'),
 ('Isa 57:15', G3, 'read', 'A B', '"I dwell in the high and holy place, and also with him who is of a contrite and lowly spirit, to revive"'),
 ('Isa 66:2', G3, 'read', 'A B', '"this is the one to whom I will look: he who is humble and contrite in spirit and trembles at my word"; against the house and the offerings (66:1, 3)'),
 ('Isa 61:1', G3, 'read', 'A B', '"to bind up the brokenhearted" beside "good news to the poor" (OT-105 holds the poor side)'),
 ('Zec 9:9', G4, 'read', 'A B', '"your king is coming to you ... humble and mounted on a donkey"; chariot and war horse cut off, "he shall speak peace" (9:10)'),
 ('Psa 45:4', G4, 'read', 'A B', '"ride out victoriously for the cause of truth and meekness and righteousness"'),
 ('2Sa 22:36', G4, 'read', 'A B', '"your gentleness made me great": the humility noun (H6038), of God'),
 ('Psa 18:35', G4, 'read', 'A B', 'parallel: "your right hand supported me, and your gentleness made me great" (H6037)'),
 ('Num 12:3', G4, 'carried', 'B', 'no-other-M-code reading, group A'),
 ('2Sa 6:22', G4, 'carried', 'B', 'no-other-M-code reading, group A (H8217 "abased")'),
 ('Mal 2:9', G5, 'read', 'A B', '"I make you despised and abased before all the people, inasmuch as you ... show partiality in your instruction"'),
 ('Eze 17:14', G5, 'read', 'B', '"that the kingdom might be humble and not lift itself up, and keep his covenant"; the king rebelled, despised the oath (17:15-16)'),
 ('Eze 29:14', G5, 'read', 'A', 'Egypt "a lowly kingdom"'),
 ('Eze 29:15', G5, 'read', 'A B', '"never again exalt itself"; "never again be the reliance of the house of Israel" (29:16)'),
 ('Psa 22:26', G6, 'thread', 'A B', '"The afflicted shall eat and be satisfied ... May your hearts live forever" (split code G; OT-105)'),
 ('Amo 2:7', G6, 'thread', 'B', '"turn aside the way of the afflicted" (split code P; OT-105)'),
 ('Pro 14:21', G6, 'thread', 'B', '"blessed is he who is generous to the poor" (split code P; OT-105)'),
 ('Psa 10:12', G6, 'thread', 'A', '"forget not the afflicted" (split code G; OT-105)'),
 ('Psa 10:17', G6, 'thread', 'A B', '"you hear the desire of the afflicted; you will strengthen their heart" (split code G; OT-105)'),
 ('Psa 9:12', G6, 'thread', 'A', '"he does not forget the cry of the afflicted" (split code G; OT-105)'),
 ('Job 24:4', G6, 'thread', 'B', '"They thrust the poor off the road" (split code P; OT-105)'),
 ('Lev 13:20', G7, 'data', 'C', '"deeper than the skin"'),
 ('Lev 13:21', G7, 'data', 'C', 'same'),
 ('Lev 13:26', G7, 'data', 'C', 'same'),
 ('Lev 14:37', G7, 'carried', 'C', 'data in the no-other-M-code reading'),
 ('Eze 17:6', G7, 'data', 'C', '"a low spreading vine" (surface artefact "and its")'),
]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)) == 43, (len(refs), len(set(refs)))
with open(os.path.join(HERE, 'm09-humbling-batch2-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note'])
    w.writerows(R)
print(Counter(r[1] for r in R)); print(Counter(r[2] for r in R))
