"""Anger unit 4 (the rest of the Hebrew and Aramaic: qatsaph/qetseph H7107-H7111, ebrah H5678 H5674B, zaam H2194 H2195,
zaaph H2196-H2198, strife and Meribah H4079 H4808 H4809G/H, qinah H7015, saar H5590 and H6225 H6696B H5307K H6440M
H0888 H1149 H2121 H7265 H7266): face for every hit, by reading, with the parties (#1963 ruling 6.2). Faces are
labelled 4A-4Z and 4AA-4AE so they do not clash with units 1-3. Faces are set by verse; a verse whose hits need
different faces is set by (reference, position) in POS.
Writes anger-unit4-faces-v1-20261005.csv (reference,position,strong,face,face_name,angry_one,toward,other_parties)
and merges face/face_name into the unit pull. No DB access."""
import csv
FACES = {
 '4A': ("God's wrath comes upon, goes out against or uproots his people: the cause named", 'God', 'his people, Judah and Jerusalem, Jacob, the princes, that man', 'Jehoshaphat, the seer; idols, Asherim; hearts made diamond-hard; the stubborn heart; unbelief; moving the landmark; the land and its fuel'),
 '4B': ('People provoke the Lord to wrath', 'his people, the fathers', 'God', 'the wilderness, Horeb, Taberah, Massah, Kibroth-hattaavah; the God of heaven; Nebuchadnezzar'),
 '4C': ('Wrath guarded against: an order, an oath, a warning, a decree', 'God', 'the congregation, the judges and their brothers, the realm of the king', "the Levites who keep guard; the leaders and their oath; Jehoshaphat's judges; Artaxerxes; the mouth that vows; Aaron's sons not to mourn"),
 '4D': ("One person's act, and wrath on all", 'God', 'all the congregation, Israel, Judah and Jerusalem', "Korah; the eastern tribes; Achan; Joab's count; Hezekiah's proud heart; Moses and Aaron ask"),
 '4E': ('Asked: heard, or not heard; atonement made', 'God', 'the people, Moses himself, Jerusalem', 'Moses pleads; Aaron runs with the censer; the angel of the Lord asks "how long"'),
 '4F': ('Turned: for a moment, not forever; the reasons given; healed and gathered', 'God', 'his people, Zion, the one who backslides', '"the spirit would grow faint before me"; the days of Noah; everlasting love; Hezekiah humbled himself'),
 '4G': ('The indignation has a set end', 'God', 'his people, the nations', 'Daniel told; "my people" told to hide; the king who exalts himself'),
 '4H': ("The instrument of his wrath, and the instrument's excess", 'God; and the instrument', 'a godless nation, his people; the instrument in turn', "Assyria the rod; the weapons from a distant land; Babylon who showed no mercy; the nations at ease; Israel's army in a rage"),
 '4I': ("God's wrath on the nations and enemies; the earth before it", 'God', 'the nations, Egypt, Assyria, Ammon, Babylon, Edom, Gog, his enemies, the wicked', 'the heavens and earth, rivers and sea, rocks; destroying angels; his servants who see his hand'),
 '4J': ('The day of wrath, and the sayings on whom it falls', 'God', 'the land and its sinners, the evil man, the wicked, the one who falls', 'silver and gold, riches; righteousness; the mouth of forbidden women'),
 '4K': ("God's wrath borne: in body, days, prayer and lament", 'God', 'the one who prays, Zion, the anointed, "your people"', 'David, Moses (Psa 90), Asaph, the man of Lamentations, the remnant in Isaiah and Micah'),
 '4L': ("God's indignation called down on others", 'God', 'enemies', 'the psalmist asks'),
 '4M': ('Denouncing; filled with his indignation', 'Balak would have, God has not; the nations; the prophet', 'Israel; the one who acquits the wicked; the wicked house', 'Balaam who cannot; Jeremiah sitting alone'),
 '4N': ('Great wrath, its source not named', '(not named)', 'Israel', 'the king of Moab and his son offered on the wall'),
 '4O': ('Meribah: the quarrel with the Lord kept in a place name', 'the people (quarrel); God (angered)', 'God; Moses and Aaron', 'Moses who struck the rock; Levi tested there; "do not harden your hearts"'),
 '4P': ("The ruler's anger, and those beneath it", 'Pharaoh, Ahasuerus, Nebuchadnezzar, a king', 'officers, Vashti, the wise men, three Jews, the one who acts shamefully', 'the officials who fear contempt; the servant who deals wisely'),
 '4Q': ('Anger at those who did not do as commanded', 'Moses, the man of God', "the people, Aaron's sons, the officers, the king of Israel", "Aaron answers; Balaam's advice; three strikes"),
 '4R': ('Anger at a rebuke, a refusal or an unexpected answer; vexed and sullen', 'Naaman, Uzziah, Asa, Ahab', 'the prophet, the priests, the seer, Naboth', 'the servants who persuade; leprosy; the stocks; Jezebel'),
 '4S': ('Anger against one suspected or set against', 'commanders, eunuchs, officials, a king', 'David, the king, Jeremiah, the holy covenant', 'Achish; Mordecai; Irijah; the ships of Kittim'),
 '4T': ("Anger turned against God: in hunger; in folly's ruin", 'the people, a man', 'their king and their God; the Lord', 'hunger; distress and darkness; his own folly'),
 '4U': ('Wrath fierce, cruel, kept forever: cursed and judged', 'Simeon and Levi, Edom, the king of Babylon, the unjust', 'men and oxen, his brother, the peoples', 'Jacob curses; the Lord judges'),
 '4V': ('Overflow as pride and insolence; the overflowing anger that abases the proud', "the scoffer, Moab, Ephraim's princes; God (to Job)", 'the proud', 'God challenges Job'),
 '4W': ("Enemies' fury and rush, as the one attacked bears it", 'enemies, warriors', 'the psalmist, the poor, Israel', 'God who arises; "the Lord who was on our side"'),
 '4X': ('Anger borne within, with vexation and sickness', 'the one who toils', '-', 'darkness, all his days'),
 '4Y': ('Strife and quarrel between people', 'the one who sows discord, a quarrelsome man, the meddler, a backbiting tongue', 'brothers, neighbours, kinsmen', 'the lot that ends quarrels; wine; Abram and Lot'),
 '4Z': ('The quarrelsome wife', 'a wife', 'her husband', 'the corner of the housetop; the desert'),
 '4AA': ('Hostility: harassing an adversary, forbidden or turned', 'Israel; God; any armed force', 'Moab, Ammon; your adversaries; the Jews', "the Lord who gave the land to Lot's sons; the angel to be obeyed"),
 '4AB': ('Troubled, downcast or storm-tossed: no anger in the verse', 'the dreamers, the chief eunuch, Darius, the king of Syria, Zion', '-', 'Joseph asks; the king feared; Daniel; Elisha'),
 '4AC': ('Lament (qinah): the word is lament, not anger', '-', '-', 'Ezekiel, Jeremiah, Amos, David, the singing men and women, the daughters of the nations'),
 '4AD': ('No anger in the verse: storm, sea, smoke, twig, splinter, boundary', '-', '-', "the sea, the whirlwind, the mountains, Samaria's king, the locust"),
 '4AE': ("The face that falls: Cain's face; God's face that will not fall", 'Cain; God', 'Abel and God; faithless Israel', '"I am merciful"'),
}
A = {}
POS = {}
def put(face, refs):
    for r in refs.split(';'):
        r = r.strip()
        if r: A[r] = face
put('4A', '2Ch 19:2;2Ch 24:18;2Ch 29:8;Zec 7:12;Deu 29:28;Deu 29:20;Zec 1:2;Psa 78:21;Psa 78:59;Psa 78:62;Deu 1:34;Jer 21:5;Hos 5:10;Eze 22:21;Eze 22:24;Eze 22:31;Isa 9:19;Hos 13:11;Jer 7:29')
put('4B', 'Deu 9:7;Deu 9:8;Deu 9:22;Zec 8:14;Ezr 5:12')
put('4C', 'Num 1:53;Num 18:5;Jos 9:20;2Ch 19:10;Ezr 7:23;Ecc 5:6;Lev 10:6')
put('4D', 'Num 16:22;Jos 22:18;Jos 22:20;1Ch 27:24;2Ch 32:25')
put('4E', 'Deu 9:19;Deu 3:26;Num 16:46;Zec 1:12')
put('4F', 'Isa 54:8;Isa 54:9;Isa 57:16;Isa 57:17;Isa 60:10;Jer 32:37;2Ch 32:26;Psa 85:3')
put('4G', 'Dan 8:19;Dan 11:36;Isa 26:20;Isa 10:25')
put('4H', 'Isa 10:5;Isa 10:6;Isa 13:5;Jer 50:25;Zec 1:15;Isa 47:6;2Ch 28:9')
put('4I', 'Isa 34:2;Eze 21:31;Jer 50:13;Jer 10:10;Nah 1:6;Zep 3:8;Hab 3:8;Hab 3:12;Psa 78:49;Isa 30:27;Isa 30:30;Mal 1:4;Isa 66:14;Psa 7:11;Eze 38:19')
put('4J', 'Zep 1:15;Zep 1:18;Eze 7:19;Pro 11:4;Pro 11:23;Job 21:30;Isa 13:9;Isa 13:13;Pro 22:14')
put('4K', 'Psa 38:1;Psa 38:3;Psa 102:10;Lam 2:2;Lam 2:6;Lam 3:1;Lam 5:22;Psa 90:9;Psa 90:11;Psa 89:38;Psa 74:1;Psa 80:4;Isa 64:5;Isa 64:9;Mic 7:9')
put('4L', 'Psa 69:24')
put('4M', 'Num 23:7;Num 23:8;Pro 24:24;Mic 6:10;Jer 15:17')
put('4N', '2Ki 3:27')
put('4O', 'Exo 17:7;Num 20:13;Num 20:24;Num 27:14;Deu 32:51;Deu 33:8;Psa 81:7;Psa 95:8;Psa 106:32')
put('4P', 'Gen 40:2;Gen 41:10;Est 1:12;Est 1:18;Dan 2:12;Dan 3:13;Pro 14:35;Pro 19:12;Pro 20:2')
put('4Q', 'Exo 16:20;Lev 10:16;Num 31:14;2Ki 13:19')
put('4R', '2Ki 5:11;2Ch 26:19;2Ch 16:10;1Ki 21:4;1Ki 20:43')
put('4S', '1Sa 29:4;Est 2:21;Jer 37:15;Dan 11:30')
put('4T', 'Isa 8:21;Pro 19:3')
put('4U', 'Gen 49:7;Amo 1:11;Isa 14:6;Pro 22:8')
put('4V', 'Pro 21:24;Isa 16:6;Jer 48:30;Hos 7:16;Job 40:11')
put('4W', 'Psa 7:6;Psa 124:5;Hab 3:14')
put('4X', 'Ecc 5:17')
put('4Y', 'Pro 6:14;Pro 18:18;Pro 18:19;Pro 23:29;Pro 26:21;Pro 26:17;Pro 25:23;Gen 13:8')
put('4Z', 'Pro 19:13;Pro 21:9;Pro 21:19;Pro 25:24;Pro 27:15')
put('4AA', 'Deu 2:9;Deu 2:19;Exo 23:22;Est 8:11')
put('4AB', 'Gen 40:6;Dan 1:10;Dan 6:14;2Ki 6:11;Isa 54:11')
put('4AC', 'Eze 32:2;Eze 32:16;Amo 8:10;Amo 5:1;Eze 26:17;Eze 27:2;Eze 27:32;Eze 28:12;Eze 19:1;Eze 19:14;2Ch 35:25;Jer 9:10;Jer 9:20;Eze 2:10;2Sa 1:17')
put('4AD', 'Jon 1:11;Jon 1:13;Jon 1:15;Zec 7:14;Hos 13:3;Exo 19:18;Psa 144:5;Psa 104:32;Hos 10:7;Joe 1:7;Eze 47:19;Eze 48:28')
put('4AE', 'Gen 4:5;Jer 3:12')
# Jer 7:29: the lament raised (4AC) and the generation of his wrath (4A) in one verse
POS[('Jer 7:29', '4')] = '4AC'
pull = 'anger-unit4-rest-hebrew-pull-v1-20261005.csv'
rows = list(csv.DictReader(open(pull, encoding='utf-8')))
miss = [r['reference'] for r in rows if r['reference'] not in A]
assert not miss, miss
extra = set(A) - {r['reference'] for r in rows}
assert not extra, extra
with open('anger-unit4-faces-v1-20261005.csv', 'w', encoding='utf-8', newline='') as f:
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
