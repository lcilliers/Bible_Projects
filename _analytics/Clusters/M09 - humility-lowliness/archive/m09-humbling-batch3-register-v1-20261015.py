"""M09 humbling fan-out, batch 3 (the contrite and broken heart or spirit): one decision per verse (#2148).

Words: H1793A (M09), H5223 (M73), H1794/H1792 "contrite" (M10), and the joined set: H7665 (M24/T3),
H5218B and H7115 (T2), H2254B (M10), H3512A (M20), H2490A (T3); plus Psa 38:8 (H1794 "crushed",
the known miss named in the scope). Verses not already in batches 1-2. Each read by Claude in its
passage (+-4 verses). Groups emerged from the reading (m09-humbling-batch3-reading-v1-20261015.md).
Writes m09-humbling-batch3-register-v1-20261015.csv.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. The broken and contrite heart before God'
G2 = 'II. A heart or spirit broken by what it bears'
G3 = 'III. The crushed spirit in Proverbs'
G4 = 'IV. God broken over a heart'
G5 = 'V. Data'
R = [
 ('Psa 51:17', G1, 'read', 'A B', '"The sacrifices of God are a broken spirit; a broken and contrite heart, O God, you will not despise" against sacrifice (51:16); after bloodguiltiness (51:14)'),
 ('Psa 34:18', G1, 'read', 'A B', '"The Lord is near to the brokenhearted and saves the crushed in spirit"; the righteous cry (34:17), many afflictions (34:19)'),
 ('Psa 147:3', G1, 'read', 'A B', '"He heals the brokenhearted and binds up their wounds"; gathers the outcasts (147:2), lifts up the humble (147:6)'),
 ('Psa 38:8', G1, 'read', 'A B', '"I am feeble and crushed; I groan because of the tumult of my heart"; from his iniquities (38:4); "all my longing is before you" (38:9)'),
 ('Psa 69:20', G2, 'read', 'B', '"Reproaches have broken my heart, so that I am in despair. I looked for pity, but there was none"'),
 ('Psa 109:22', G2, 'read', 'B', '"I am poor and needy, and my heart is stricken within me"; scorn, fasting, gaunt (109:23-25); also OT-106'),
 ('Psa 109:16', G2, 'read', 'B', 'the accuser "pursued the poor and needy and the brokenhearted, to put them to death"; "did not remember to show kindness"; also OT-105 (split code P)'),
 ('Job 17:1', G2, 'read', 'B', '"My spirit is broken; my days are extinct"; mockers about me (17:2)'),
 ('Exo 6:9', G2, 'read', 'A B', '"they did not listen to Moses, because of their broken spirit and harsh slavery", after the promise (6:6-8)'),
 ('Jer 23:9', G2, 'read', 'B', '"My heart is broken within me; all my bones shake ... because of the Lord and because of his holy words"; the land full of adulterers (23:10)'),
 ('Pro 15:13', G3, 'read', 'B', '"A glad heart makes a cheerful face, but by sorrow of heart the spirit is crushed"'),
 ('Pro 17:22', G3, 'read', 'B', '"A joyful heart is good medicine, but a crushed spirit dries up the bones"'),
 ('Pro 18:14', G3, 'read', 'B', '"A man\'s spirit will endure sickness, but a crushed spirit who can bear?"'),
 ('Eze 6:9', G4, 'read', 'A B', '"how I have been broken over their whoring heart that has departed from me"; "they will be loathsome in their own sight"'),
 ('2Sa 4:4', G5, 'data', 'C', '"crippled in his feet" (H5223, the "contrite" of Isa 66:2)'),
 ('2Sa 9:3', G5, 'data', 'C', 'same; David\'s kindness to Mephibosheth (9:1, 7) is not this word'),
]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)) == 16
with open(os.path.join(HERE, 'm09-humbling-batch3-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note'])
    w.writerows(R)
print(Counter(r[1] for r in R)); print(Counter(r[2] for r in R))
