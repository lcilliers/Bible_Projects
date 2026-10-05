"""Anger unit 1 (aph H0639G, anaph H0599): face for every hit, by reading, with the parties (#1963 ruling 6.2).
Writes anger-unit1-faces-v1-20261005.csv (reference,position,face,face_name,angry_one,toward,other_parties)
and merges face/face_name into the unit pull. Read-only on iba.db (none used)."""
import csv
FACES = {
 'A': ('God angry with his people as a whole', 'God', 'his people', 'the people provoke; enemies, plunderers, plague, fire carry it'),
 'B': ('God angry with a named person or group', 'God', 'a named person or group', 'the people on whose account (Deu 1:37); a prophet sent (2Ch 25:15); an angel in the way (Num 22:22)'),
 'C': ('God angry with nations, enemies, oppressors', 'God', 'nations, kings, enemies, oppressors', 'his people or the one who cries, on whose side; the created world shaken'),
 'D': ('God\'s anger restrained, deferred, turned, ended', 'God', 'his people', 'the reason stated (his name, compassion, steadfast love)'),
 'E': ('God\'s anger not turned back', 'God', 'his people', 'the people who do not turn; his hand stretched out still'),
 'F': ('Slow to anger: the name, and forbearance', 'God', '—', 'Moses hears it; the people recite it; Jonah holds it against him; Jeremiah pleads it'),
 'G': ('Intercession before God\'s anger', 'God', 'the people, Aaron, a city', 'Moses, Gideon, Daniel speak'),
 'H': ('God\'s anger in lament, prayer and thanks', 'God', 'the one who prays, or the community', 'the psalmist, Zion, Job, Ezra, Solomon speak'),
 'I': ('God\'s anger called down on others', 'God', 'enemies, persecutors', 'the psalmist, Jeremiah, Zion ask'),
 'J': ('God\'s anger explained, asked about, presumed on', 'God', 'the wicked, a land, the speaker', 'Job\'s friends, the nations, Ezra, the self-declared innocent speak'),
 'K': ('God\'s anger borne without knowing why', 'God', 'Job', 'Job speaks; "my adversary"'),
 'L': ('Acting to turn God\'s anger away', 'God', 'the people, a king, a city', 'leaders, priests, prophets, the humble, the king act or call'),
 'M': ('God\'s anger carried out by an agent', 'God', 'Edom, Israel, Babylon, Amalek', 'Israel, Assyria, the consecrated ones, Saul (who did not)'),
 'O': ('Anger kindled by what is heard or seen', 'a person', 'the one heard of or seen', 'a report, a lie, a sight'),
 'P': ('Anger at a demand or a will thwarted', 'a person', 'the one who demands, refuses or blocks', 'a donkey; a prophet; a dismissal'),
 'Q': ('Anger against a brother, rival or kin, kept or turned', 'a person or people', 'a brother, a son, a kindred people', 'a mother sends away; God judges it'),
 'R': ('Indignation for one wronged', 'a person', 'the wrongdoer', 'the one wronged (David, the poor man, Israel)'),
 'S': ('Anger that comes with God\'s Spirit', 'Samson, Saul', 'the enemy, or the one who exposed him', 'the Spirit of the Lord rushes upon him'),
 'T': ('The anger of the one with power, and those beneath it', 'a ruler', 'a servant, the nations', 'Judah and Aaron plead; peoples struck'),
 'U': ('Enemies\' anger, as the one attacked bears it', 'enemies, kings', 'the psalmist, Ahaz and Judah', 'God preserves; "do not fear"'),
 'V': ('Anger governed: slow, quick, ruled', 'a person', '—', 'the one who quiets strife; the city taken'),
 'W': ('Another\'s anger turned away or stirred', 'a person', 'the one who answers', 'a soft answer, a gift, the wise; a harsh word, pressing'),
 'X': ('Anger\'s own course and company', 'a person', 'men, oxen, oneself', 'the friend who learns it; jealousy beside it'),
 'Y': ('Anger at what God does', 'Moses, Jonah', 'God (his act, his mercy)', 'God angry at the same time (Num 11:10)'),
 'Z': ('A man invited to pour out anger', 'Job (invited)', 'the proud', 'God speaks from the whirlwind'),
}
A = {}
def put(face, refs):
    for r in refs.split(';'):
        r = r.strip()
        if r: A[r] = face
put('A','Eze 7:3;Eze 7:8;Eze 43:8;Psa 106:40;Num 11:1;Num 11:33;Num 25:3;Num 32:10;Num 32:13;Num 32:14;Deu 6:15;Deu 7:4;Deu 11:17;Deu 29:20;Deu 29:23;Deu 29:27;Deu 29:28;Deu 31:17;Deu 32:22;Jos 7:1;Jos 23:16;Judg 2:14;Judg 2:20;Judg 3:8;Judg 10:7;2Sa 24:1;2Ki 13:3;2Ki 24:20;Psa 78:21;Psa 78:31;Psa 95:11;Isa 42:25;Jer 4:26;Jer 7:20;Jer 12:13;Jer 15:14;Jer 17:4;Jer 21:5;Jer 32:31;Jer 33:5;Jer 42:18;Jer 44:6;Jer 52:3;Lam 2:1;Lam 2:3;Lam 2:6;Lam 4:11;Eze 5:13;Eze 5:15;Eze 13:13;Eze 22:20;Hos 8:5;Hos 13:11;Deu 9:8;2Ki 17:18')
put('B','Exo 4:14;Deu 1:37;Deu 4:21;Num 12:9;Num 22:22;2Sa 6:7;1Ch 13:10;1Ki 11:9;2Ch 25:15;Job 42:7;Zec 10:3')
put('C','Exo 22:24;Psa 2:5;Psa 7:6;Psa 21:9;Psa 78:49;Psa 78:50;Psa 110:5;Pro 24:18;Isa 10:25;Isa 13:9;Isa 13:13;Isa 30:27;Isa 30:30;Isa 63:3;Isa 63:6;Isa 66:15;Jer 25:37;Jer 25:38;Jer 49:37;Eze 38:18;Mic 5:15;Nah 1:6;Hab 3:8;Hab 3:12;Zep 3:8')
put('D','Psa 30:5;Psa 78:38;Isa 48:9;Hos 11:9;Hos 14:4;Mic 7:18;Jer 32:37;Eze 20:8;Eze 20:21')
put('E','Isa 5:25;Isa 9:12;Isa 9:17;Isa 9:21;Isa 10:4;2Ki 23:26;Jer 23:20;Jer 30:24')
put('F','Exo 34:6;Num 14:18;Neh 9:17;Psa 86:15;Psa 103:8;Psa 145:8;Joe 2:13;Nah 1:3;Jer 15:15')
put('G','Exo 32:10;Exo 32:11;Exo 32:12;Deu 9:19;Deu 9:20;Judg 6:39;Dan 9:16')
put('H','Psa 6:1;Psa 27:9;Psa 60:1;Psa 74:1;Psa 76:7;Psa 77:9;Psa 79:5;Psa 85:3;Psa 85:5;Psa 90:7;Psa 90:11;Jer 10:24;Lam 1:12;Lam 2:21;Lam 2:22;Lam 3:43;Isa 12:1;Job 14:13;Ezr 9:14;1Ki 8:46;2Ch 6:36')
put('I','Psa 56:7;Psa 69:24;Jer 18:23;Lam 3:66')
put('J','Job 4:9;Job 20:23;Job 20:28;Job 21:17;Job 35:15;Jer 2:35;Deu 29:24;Ezr 8:22')
put('K','Job 9:5;Job 9:13;Job 16:9;Job 19:11')
put('L','Num 25:4;Deu 13:17;Jos 7:26;2Ch 12:12;2Ch 28:11;2Ch 28:13;2Ch 29:10;2Ch 30:8;Ezr 10:14;Jer 36:7;Jer 4:8;Jer 51:45;Jon 3:9;Zep 2:2;Zep 2:3;Psa 2:12')
put('M','Eze 25:14;Isa 10:5;Isa 13:3;1Sa 28:18')
put('O','Gen 39:19;Judg 9:30;Exo 32:19;Job 32:2;Job 32:3;Job 32:5')
put('P','Gen 30:2;Num 22:27;Num 24:10;2Ch 25:10')
put('Q','Gen 27:45;1Sa 17:28;1Sa 20:30;Amo 1:11;Eze 35:11')
put('R','Exo 11:8;1Sa 20:34;2Sa 12:5')
put('S','Judg 14:19;1Sa 11:6')
put('T','Gen 44:18;Exo 32:22;Isa 14:6;Dan 11:20')
put('U','Psa 55:3;Psa 124:3;Psa 138:7;Isa 7:4')
put('V','Pro 14:17;Pro 14:29;Pro 15:18;Pro 16:32;Pro 19:11;Pro 25:15;Pro 29:22')
put('W','Pro 15:1;Pro 21:14;Pro 29:8;Pro 30:33')
put('X','Gen 49:6;Gen 49:7;Job 36:13;Job 18:4;Pro 22:24;Pro 27:4;Psa 37:8')
put('Y','Num 11:10;Jon 4:2')
put('Z','Job 40:11')
pull = 'anger-unit1-aph-pull-v1-20261005.csv'
rows = list(csv.DictReader(open(pull, encoding='utf-8')))
miss = [r['reference'] for r in rows if r['reference'] not in A]
assert not miss, miss
extra = set(A) - {r['reference'] for r in rows}
assert not extra, extra
with open('anger-unit1-faces-v1-20261005.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['reference', 'position', 'face', 'face_name', 'angry_one', 'toward', 'other_parties'])
    for r in rows:
        k = A[r['reference']]; n, a, t, o = FACES[k]
        w.writerow([r['reference'], r['position'], k, n, a, t, o])
        r['face'], r['face_name'] = k, n
with open(pull, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
from collections import Counter
c = Counter(r['face'] for r in rows)
v = {k: len({r['reference'] for r in rows if r['face'] == k}) for k in c}
for k in sorted(c): print(k, c[k], v[k], FACES[k][0])
print(len(rows), 'hits; all faced')
