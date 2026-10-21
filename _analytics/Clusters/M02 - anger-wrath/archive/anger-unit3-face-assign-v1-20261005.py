"""Anger unit 3 (harah H2734, haron H2740, hori H2750, kaas H3707, kaas/kaas H3708A/B): face for every hit,
by reading, with the parties (#1963 ruling 6.2). Faces are labelled 3A-3Z and 3AA so they do not clash with
unit 1 (A-Z) or unit 2 (2A-2W). Faces are set by verse; a verse whose hits need different faces is set by
(reference, position) in POS.
Writes anger-unit3-faces-v1-20261005.csv (reference,position,strong,face,face_name,angry_one,toward,other_parties)
and merges face/face_name into the unit pull. No DB access."""
import csv
FACES = {
 '3A': ('God\'s anger kindled against his people: the formula, with cause and act', 'God', 'his people, Israel, Judah, the land', 'other gods, Baal of Peor, the devoted things; plunderers, kings, plague, fire, drought'),
 '3B': ('God\'s anger against a named person or group', 'God', 'Moses, Miriam and Aaron, Balaam, Uzzah, Amaziah, Eliphaz, the shepherds, those who afflict the widow', 'Aaron provided; the angel in the way; a prophet sent; Job "my servant"; the flock'),
 '3C': ('God\'s fierce anger on the nations and in the day; the earth shakes', 'God', 'adversaries, Egypt, Babylon, Elam, kings, the nations', 'his people, the psalmist, for whom; the heavens, the earth, rivers and sea'),
 '3D': ('God\'s anger turned, withdrawn, not executed; or not turned back', 'God', 'his people, Ephraim, Judah', 'the reason stated: "I am God and not a man"; Manasseh\'s provocations'),
 '3E': ('Acting or calling to turn the fierce anger away', 'God', 'the people, a city, Nineveh', 'Moses, Hezekiah, Ezra\'s officials, Oded, Nehemiah, the king of Nineveh, the prophets act or call'),
 '3F': ('Asking God not to be angry: intercession', 'God', 'the people, a city, the one who asks', 'Abraham, Moses, Gideon speak'),
 '3G': ('God\'s anger borne in lament, or explained', 'God', 'the one who prays, Zion, Job, a land', 'the psalmist, Zion, Job, Zophar, the nations who ask'),
 '3H': ('God\'s anger called down on others', 'God', 'enemies, those who taunt the builders', 'the psalmist, Nehemiah ask'),
 '3I': ('God\'s fierce wrath not carried out by the one sent', 'God', 'Amalek', 'Saul (who did not); Samuel speaks'),
 '3J': ('People provoke God to anger: what provokes', 'his people, kings', 'God', 'other gods, idols, Asherim, high places, sons burned, mediums, the work of their hands'),
 '3K': ('The provocation turns back on the provoker', 'his people', 'God, and themselves', '"Is it not themselves, to their own shame?"; "to your own harm"; "that you may be cut off"'),
 '3L': ('Provocation answered in kind; God\'s fear of the enemy\'s provocation; hearts troubled', 'God and his people, each of the other', 'his people; the nations', 'a foolish nation, those who are no people; the adversaries who would misunderstand'),
 '3M': ('Human anger kindled by what is heard or seen', 'a person', 'the one heard of or seen', 'a report, a lie, a calf and dancing, Job and his friends, an outcry'),
 '3N': ('Indignation for one wronged', 'a person', 'the wrongdoer', 'Dinah, Tamar, the poor man, the people under interest; David disgraced'),
 '3O': ('Anger at a rival honoured, a brother, or a work going forward', 'a person or people', 'a brother, a rival, the builders, the honoured one', 'God who regarded Abel; the women\'s song; the poor; the wall'),
 '3P': ('Anger at a demand, a charge or a rebuke', 'a person', 'the one who demands, charges or rebukes', 'Rachel, a donkey, Balaam, Judah, Laban, Ish-bosheth, Korah, the seer'),
 '3Q': ('Anger that comes with God\'s Spirit', 'Samson, Saul', 'the enemy, or those who told the riddle', 'the Spirit of the Lord rushes upon him; the dread of the Lord falls on the people'),
 '3R': ('The anger of the one with power, and those beneath it', 'a ruler, a father, a master', 'a servant, a daughter, David', 'Judah, Aaron, Rachel plead; Jonathan reads it'),
 '3S': ('Enemies\' anger, as the one attacked bears it', 'enemies, kings', 'the psalmist, Ahaz, Israel', 'God helps; "do not fear"; shame for the incensed'),
 '3T': ('Angry at what God does', 'David, Samuel, Jonah', 'God (his act, his regret, his mercy)', 'Uzzah struck; Saul rejected; Nineveh spared'),
 '3U': ('God asks the angry one about his anger', 'Cain, Jonah', 'Abel; God; the plant', 'God speaks: "Why are you angry?"; "Do you do well to be angry?"'),
 '3V': ('Angry with oneself', 'Joseph\'s brothers', 'themselves', 'Joseph: "God sent me before you"'),
 '3W': ('Fret not yourself', 'the one addressed', 'evildoers, the one who prospers', 'envy; the Lord waited for'),
 '3X': ('Provoked between people: rival, fool, fretful wife, foolish son', 'a rival wife, a fool, a woman, a son', 'Hannah, the one who bears it, a husband, father and mother', 'Elkanah, Eli'),
 '3Y': ('Vexation and grief borne within: eye, soul, body, heart, days', 'the sufferer', '—', 'God who sees vexation; foes; wisdom and toil'),
 '3Z': ('The fool\'s vexation, and anger lodging in the fool', 'the fool', '—', 'the prudent; the patient in spirit'),
 '3AA': ('No anger in the verse', '—', '—', 'a wall repaired; thorns ablaze'),
}
A = {}
POS = {}
def put(face, refs):
    for r in refs.split(';'):
        r = r.strip()
        if r: A[r] = face
put('3A', 'Psa 106:40;Num 11:1;Num 11:33;Num 25:3;Num 32:10;Num 32:13;Num 32:14;Deu 6:15;Deu 7:4;Deu 11:17;Deu 29:27;Deu 31:17;Jos 7:1;Jos 23:16;Judg 2:14;Judg 2:20;Judg 3:8;Judg 10:7;2Sa 24:1;2Ki 13:3;Isa 5:25;Hos 8:5;Lam 4:11;Lam 2:3;Jer 4:26;Jer 12:13;Eze 7:12;Eze 7:14;Num 11:10')
put('3B', 'Exo 4:14;Num 12:9;Num 22:22;2Sa 6:7;1Ch 13:10;2Ch 25:15;Job 42:7;Zec 10:3;Exo 22:24')
put('3C', 'Exo 15:7;Psa 2:5;Psa 78:49;Isa 13:9;Isa 13:13;Jer 25:37;Jer 25:38;Jer 49:37;Zep 3:8;Nah 1:6;Hab 3:8;2Sa 22:8;Psa 18:7')
put('3D', 'Hos 11:9;Psa 85:3;Jer 30:24;Jos 7:26;Eze 16:42;2Ki 23:26')
put('3E', 'Num 25:4;Deu 13:17;2Ch 28:11;2Ch 28:13;2Ch 29:10;2Ch 30:8;Ezr 10:14;Jon 3:9;Zep 2:2;Jer 51:45;Jer 4:8;Neh 13:18')
put('3F', 'Exo 32:10;Exo 32:11;Exo 32:12;Gen 18:30;Gen 18:32;Judg 6:39;Deu 9:18')
put('3G', 'Psa 88:16;Lam 1:12;Psa 85:4;Job 19:11;Job 10:17;Job 20:23;Deu 29:24')
put('3H', 'Psa 69:24;Neh 4:5')
put('3I', '1Sa 28:18')
put('3J', 'Deu 32:16;Eze 8:17;2Ki 22:17;2Ch 34:25;Deu 4:25;Deu 31:29;Judg 2:12;1Ki 14:9;1Ki 14:15;1Ki 15:30;1Ki 16:2;1Ki 16:7;1Ki 16:13;1Ki 16:26;1Ki 16:33;1Ki 21:22;1Ki 22:53;2Ki 17:11;2Ki 17:17;2Ki 21:6;2Ki 21:15;2Ki 23:19;2Ch 28:25;2Ch 33:6;Psa 78:58;Psa 106:29;Isa 65:3;Jer 7:18;Jer 8:19;Jer 11:17;Jer 25:6;Jer 32:29;Jer 32:30;Jer 32:32;Jer 44:3;Eze 16:26;Eze 20:28;Hos 12:14;Deu 32:19')
put('3K', 'Jer 7:19;Jer 25:7;Jer 44:8')
put('3L', 'Deu 32:21;Deu 32:27;Eze 32:9')
put('3M', 'Gen 39:19;Judg 9:30;Exo 32:19;Job 32:2;Job 32:3;Job 32:5')
put('3N', 'Gen 34:7;2Sa 12:5;2Sa 13:21;Neh 5:6;1Sa 20:34;Exo 11:8')
put('3O', 'Gen 4:5;1Sa 17:28;1Sa 18:8;1Sa 20:30;Neh 4:1;Neh 4:7;Psa 112:10;Song 1:6;2Sa 19:42')
put('3P', 'Gen 30:2;Num 22:27;Num 24:10;2Ch 25:10;Gen 31:36;2Sa 3:8;Num 16:15;2Ch 16:10')
put('3Q', 'Judg 14:19;1Sa 11:6')
put('3R', 'Gen 44:18;Exo 32:22;Gen 31:35;1Sa 20:7')
put('3S', 'Psa 124:3;Isa 7:4;Isa 41:11;Isa 45:24')
put('3T', '2Sa 6:8;1Ch 13:11;Jon 4:1;1Sa 15:11')
put('3U', 'Gen 4:6;Jon 4:4;Jon 4:9')
put('3V', 'Gen 45:5')
put('3W', 'Psa 37:1;Psa 37:7;Psa 37:8;Pro 24:19')
put('3X', '1Sa 1:6;1Sa 1:7;Pro 21:19;Pro 27:3;Pro 17:25')
put('3Y', '1Sa 1:16;Psa 6:7;Psa 31:9;Psa 10:14;Job 6:2;Job 17:7;Ecc 1:18;Ecc 2:23;Ecc 5:17;Ecc 7:3;Ecc 11:10')
put('3Z', 'Pro 12:16;Job 5:2;Ecc 7:9')
put('3AA', 'Neh 3:20;Psa 58:9')
# 2Ki 23:26: the burning not turned (3D) and Manasseh's provocations (3J) in one verse
POS[('2Ki 23:26', '13')] = '3J'
POS[('2Ki 23:26', '16')] = '3J'
pull = 'anger-unit3-harah-kaas-pull-v1-20261005.csv'
rows = list(csv.DictReader(open(pull, encoding='utf-8')))
miss = [r['reference'] for r in rows if r['reference'] not in A]
assert not miss, miss
extra = set(A) - {r['reference'] for r in rows}
assert not extra, extra
with open('anger-unit3-faces-v1-20261005.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['reference', 'position', 'strong', 'face', 'face_name', 'angry_one', 'toward', 'other_parties'])
    for r in rows:
        k = POS.get((r['reference'], r['position']), A[r['reference']]); n, a, t, o = FACES[k]
        w.writerow([r['reference'], r['position'], r['strong'], k, n, a, t, o])
        r['face'], r['face_name'] = k, n
with open(pull, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
from collections import Counter
c = Counter(r['face'] for r in rows)
v = {k: len({r['reference'] for r in rows if r['face'] == k}) for k in c}
for k in sorted(c, key=lambda x: (len(x), x)): print(k, c[k], v[k], FACES[k][0])
print(len(rows), 'hits; all faced')
