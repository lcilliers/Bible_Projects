"""Anger overview part B: merge the 134 unit faces (five faces CSVs) into forms by party
(ruling 6.2), and count hits and distinct verses per form. The grouping is the overview's
arrangement (R); the counts are from the faces files. Every face must be used exactly once.

Usage (from this folder or anywhere):  python anger-overview-forms-v1-20261005.py
"""
import csv, glob, os
from collections import Counter, defaultdict

D = os.path.dirname(os.path.abspath(__file__))
FORMS = [  # (part, form, faces)
    ('B.1', 'With his people, or with those who do wrong: the cause named', 'A 2A 3A 4A 5A'),
    ('B.1', 'With a named person or group', 'B 3B'),
    ('B.1', 'On the false prophets and the wicked', '2B'),
    ('B.1', 'On nations, enemies and oppressors; the earth before it', 'C 2C 3C 4I'),
    ('B.1', 'Joined with jealousy', '2D'),
    ('B.1', 'Restrained, held back, turned; for a moment', 'D 2F 3D 4F'),
    ('B.1', 'Not turned back', 'E'),
    ('B.1', 'Spent, satisfied; a set end', '2E 4G'),
    ('B.1', '"Slow to anger": the proclaimed name', 'F'),
    ('B.1', 'In the bringing out and the gathering', '2G'),
    ('B.1', 'The cup, the winepress, the bowls', '2H 5G'),
    ('B.1', 'The day of wrath; the wrath to come, and deliverance', '4J 5C 5F'),
    ('B.1', 'Shown, and endured with patience', '5D'),
    ('B.1', 'Guarded against; one acts and all bear it', '4C 4D'),
    ('B.1', 'Great wrath, source not named', '4N'),
    ('B.2', 'People provoke God: what provokes', '3J 4B 5B'),
    ('B.2', 'The provocation turns on the provoker', '3K'),
    ('B.2', 'Answered in kind; God provokes', '3L 5H'),
    ('B.2', 'Meribah: the quarrel kept in a place', '4O'),
    ('B.3', 'Intercession; asking him not to be angry; standing between', 'G 2J 3F 4E'),
    ('B.3', 'Lament and prayer; borne in body and days', 'H 2K 3G 4K K'),
    ('B.3', 'Acting or calling to turn it away; warned of it', 'L 2L 3E'),
    ('B.3', 'Called down on others', 'I 2M 3H 4L'),
    ('B.3', 'Explained, asked about, presumed on', 'J'),
    ('B.3', 'The prophet filled with it; denouncing', '2N 4M'),
    ('B.4', 'Carried out by agents and instruments, and exceeded', 'M 2O 3I 4H 5E'),
    ('B.5', "Jesus's anger and indignation", '5I'),
    ('B.5', 'The master in the parables', '5J'),
    ('B.5', "The devil's great wrath; the dragon's fury", '5K'),
    ('B.6', 'Kindled by what is heard or seen', 'O 3M 5N'),
    ('B.6', 'At a demand, a slight, an expectation, a charge or a rebuke', 'P 2Q 3P 4R'),
    ('B.6', "At a rival's honour, a brother, kin", 'Q 3O 5R 5T'),
    ('B.6', 'Indignation: for one wronged, at waste, at good done, at idols, at one\'s own wrong', 'R 3N 2U 5Q 5S 5U 5V'),
    ('B.6', "With God's Spirit", 'S 3Q'),
    ('B.6', 'The ruler\'s anger, and those beneath it', 'T 2P 3R 4P 5O'),
    ('B.6', 'At an order not kept', '4Q'),
    ('B.6', 'Against one suspected or set against', '4S'),
    ('B.6', "Enemies' anger, as the attacked bear it", 'U 2R 3S 4W 5P'),
    ('B.6', 'Governed in the sayings: slow, quick, turned, stirred', 'V W 2S'),
    ('B.6', 'Its course and company; kept forever and cursed; overflow as pride', 'X 4U 4V'),
    ('B.6', '"Fret not yourself"', '3W'),
    ('B.6', "The fool's vexation", '3Z'),
    ('B.6', 'Put away and governed (the Greek lists and sayings)', '5L 5M'),
    ('B.6', 'At what God does; turned against God', 'Y 3T 4T'),
    ('B.6', 'God asks the angry one; a man invited to pour it out', '3U Z'),
    ('B.6', 'Angry with oneself', '3V'),
    ('B.6', 'Vexation and grief borne within', '3Y 4X'),
    ('B.6', 'Provoked between people; provoking to anger or to love', '3X 5Y'),
    ('B.6', 'Strife and quarrel', '4Y 4Z 5W 5X 5Z'),
    ('B.6', 'Hostility forbidden and taken up', '4AA'),
    ('B.6', 'Wrath poured on a neighbour as a drink', '2T'),
    ('B.7', 'Venom and poison (the same word)', '2I'),
    ('B.7', "Man's wrath and the remnant of wrath (one verse)", '2V'),
    ('B.7', 'The face that falls (Cain; God)', '4AE'),
    ('B.8', 'No anger in the verse', '2W 3AA 4AB 4AC 4AD 5AA 5AB'),
]
hits, verses, units = Counter(), defaultdict(set), defaultdict(set)
for u in range(1, 6):
    for r in csv.DictReader(open(glob.glob(os.path.join(D, f'anger-unit{u}-faces-*.csv'))[0], encoding='utf-8')):
        hits[r['face']] += 1; verses[r['face']].add(r['reference']); units[r['face']].add(u)
used = Counter(f for _, _, fs in FORMS for f in fs.split())
assert not [f for f in used if used[f] > 1], 'face used twice'
assert set(used) == set(hits), (set(hits) - set(used), set(used) - set(hits))
part_h, part_v = Counter(), defaultdict(set)
for part, form, fs in FORMS:
    fl = fs.split(); h = sum(hits[f] for f in fl); v = set().union(*(verses[f] for f in fl))
    us = sorted(set().union(*(units[f] for f in fl)))
    part_h[part] += h; part_v[part] |= v
    print(f'{part} | {form} | {fs} | {h} / {len(v)} | {",".join(map(str, us))}')
print({p: f'{part_h[p]} / {len(part_v[p])}' for p in part_h}, 'total', sum(part_h.values()))
