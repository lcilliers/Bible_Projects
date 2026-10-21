"""Anger unit 2 (hemah H2534 with the heat words H2528, H2152, H2525): face for every hit, by reading,
with the parties (#1963 ruling 6.2). Faces are labelled 2A-2W so they do not clash with unit 1 (A-Z).
Writes anger-unit2-faces-v1-20261005.csv (reference,position,face,face_name,angry_one,toward,other_parties)
and merges face/face_name into the unit pull. No DB access."""
import csv
FACES = {
 '2A': ('God\'s wrath with his people, city and land: poured out, kindled, not quenched', 'God', 'his people, Jerusalem, Judah, "this place", the land', 'the people who provoke; sword, famine, pestilence, fire; man and beast, trees and fruit'),
 '2B': ('God\'s wrath on the false prophets and the wicked', 'God', 'those who whitewash the wall; the wicked', 'storm, hail, the wall'),
 '2C': ('God\'s wrath with nations, enemies, adversaries', 'God', 'nations, Edom, Gog, Egypt, adversaries', 'his people, for whom he acts; "no one to help"'),
 '2D': ('God\'s wrath joined with jealousy', 'God', 'Jerusalem as an unfaithful wife; or the nations, for Zion and the land', 'the land, mountains and hills; Zion'),
 '2E': ('God\'s wrath spent, satisfied, then calm', 'God', 'Jerusalem, Israel', '"they shall know that I am the Lord"'),
 '2F': ('God\'s wrath held back, not stirred, not poured', 'God', 'his people', 'the reason stated: compassion, his name, their humbling'),
 '2G': ('God\'s wrath poured out in bringing out, gathering and ruling', 'God', 'his scattered people', 'the peoples and countries; the mighty hand and outstretched arm'),
 '2H': ('The cup of God\'s wrath', 'God', 'Jerusalem, the nations, the wicked', 'the prophet who takes the cup; the one who takes it away'),
 '2I': ('Venom and poison: the same word', 'God, the wicked, enemies', 'the people, the righteous, Job', 'serpents, asps, things that crawl; the arrows of the Almighty'),
 '2J': ('Intercession before God\'s wrath', 'God', 'the people, Jerusalem, the remnant', 'Moses, Daniel, Ezekiel, Jeremiah speak or stand'),
 '2K': ('God\'s wrath in lament and prayer', 'God', 'the one who prays, or "we"', 'David, Heman, Ethan, Moses (Psa 90)'),
 '2L': ('Acting on God\'s wrath, or warned of it', 'God', 'the people, the king, the speaker', 'Josiah and his officials, Phinehas, Job, Elihu'),
 '2M': ('God\'s wrath called down on others', 'God', 'enemies, nations that do not know him', 'the psalmist, Jeremiah ask'),
 '2N': ('The prophet filled with God\'s wrath', 'God (in the prophet)', 'the people', 'Jeremiah, Ezekiel; the Spirit, the hand of the Lord'),
 '2O': ('God\'s wrath carried out by agents, and exceeded', 'God', 'Judah, Jerusalem, Edom', 'Israel, the lovers turned enemies, Israel\'s army; Oded the prophet'),
 '2P': ('The ruler\'s wrath, and those beneath it', 'a king or ruler', 'a queen, servants, Haman, three men, the nations', 'Joab, the wise man, Esther, the furnace'),
 '2Q': ('Wrath at a slight seen or an expectation thwarted', 'Haman, Naaman', 'Mordecai, the prophet\'s word', 'Naaman\'s servants'),
 '2R': ('The oppressor\'s wrath, feared', 'the oppressor', 'God\'s people', 'God, "your Maker", forgotten'),
 '2S': ('Wrath between people, in the sayings', 'a person', 'neighbour, brother, a man who has wronged him', 'the one who answers, gives, befriends, refrains; jealousy'),
 '2T': ('Wrath poured on a neighbour as a drink', 'the one who pours', 'neighbours', 'their nakedness gazed at'),
 '2U': ('Hot indignation at the wicked', 'the psalmist', 'the wicked who forsake the law', 'the law'),
 '2V': ('Man\'s wrath, and the remnant of wrath, with God', 'man; God', '—', 'God praised; God girds himself'),
 '2W': ('Heat itself: bread, garments, wine, famine', '—', '—', 'bread, garments, wine, famine (no anger in the verse)'),
}
A = {}
def put(face, refs):
    for r in refs.split(';'):
        r = r.strip()
        if r: A[r] = face
put('2A', 'Eze 7:8;Deu 29:23;Deu 29:28;Isa 42:25;Jer 7:20;Jer 21:5;Jer 32:31;Jer 33:5;Jer 42:18;Jer 44:6;Lam 4:11;Lam 2:4;Eze 5:15;Eze 22:20;Eze 22:22;Eze 24:8;Eze 14:19;Eze 36:18;Eze 8:18;Eze 19:12;Lev 26:28;2Ch 36:16;2Ki 22:17;2Ch 34:25;Jer 4:4;Jer 21:12')
put('2B', 'Eze 13:13;Eze 13:15;Jer 23:19;Jer 30:23')
put('2C', 'Eze 25:17;Isa 63:3;Isa 63:5;Isa 63:6;Isa 59:18;Isa 34:2;Isa 66:15;Mic 5:15;Nah 1:6;Eze 30:15;Eze 38:18')
put('2D', 'Eze 16:38;Eze 36:6;Zec 8:2;Nah 1:2')
put('2E', 'Eze 5:13;Eze 6:12;Eze 16:42;Eze 21:17;Eze 24:13')
put('2F', 'Psa 78:38;Eze 20:8;Eze 20:13;Eze 20:21;2Ch 12:7;Isa 27:4')
put('2G', 'Eze 20:33;Eze 20:34;Jer 32:37')
put('2H', 'Isa 51:17;Isa 51:20;Isa 51:22;Jer 25:15;Job 21:20;Psa 11:6')
put('2I', 'Deu 32:24;Deu 32:33;Psa 58:4;Psa 140:3;Job 6:4')
put('2J', 'Deu 9:19;Psa 106:23;Dan 9:16;Eze 9:8;Jer 18:20')
put('2K', 'Psa 6:1;Psa 38:1;Psa 88:7;Psa 89:46;Psa 90:7')
put('2L', 'Jer 36:7;2Ki 22:13;2Ch 34:21;Num 25:11;Job 19:29;Job 36:18')
put('2M', 'Psa 59:13;Psa 79:6;Jer 10:25')
put('2N', 'Jer 6:11;Eze 3:14')
put('2O', '2Ch 28:9;Eze 23:25;Eze 25:14')
put('2P', '2Sa 11:20;Est 1:12;Est 2:1;Est 7:7;Est 7:10;Dan 3:13;Dan 3:19;Dan 11:44;Dan 8:6;Pro 16:14')
put('2Q', 'Est 3:5;Est 5:9;2Ki 5:12')
put('2R', 'Isa 51:13')
put('2S', 'Pro 15:1;Pro 15:18;Pro 21:14;Pro 22:24;Pro 27:4;Pro 29:22;Pro 19:19;Psa 37:8;Gen 27:44;Pro 6:34')
put('2T', 'Hab 2:15')
put('2U', 'Psa 119:53')
put('2V', 'Psa 76:10')
put('2W', 'Jos 9:12;Job 37:17;Lam 5:10;Hos 7:5')
pull = 'anger-unit2-hemah-pull-v1-20261005.csv'
rows = list(csv.DictReader(open(pull, encoding='utf-8')))
miss = [r['reference'] for r in rows if r['reference'] not in A]
assert not miss, miss
extra = set(A) - {r['reference'] for r in rows}
assert not extra, extra
with open('anger-unit2-faces-v1-20261005.csv', 'w', encoding='utf-8', newline='') as f:
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
