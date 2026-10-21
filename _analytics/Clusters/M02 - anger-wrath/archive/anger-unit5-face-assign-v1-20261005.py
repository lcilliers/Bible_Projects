"""Anger unit 5 (the Greek, 25 Strong's: orge G3709, thymos G2372, orgizo G3710, eris G2054, aganakteo G0023,
mache G3163, zestos G2200, prosochthizo G4360, parorgizo G3949, paroxysmos G3948, paroxyno G3947, erethizo G2042,
dichostasia G1370, diaprio G1282, diaponeomai G1278, cholao G5520, phryasso G5433, prokaleomai G4292,
parorgismos G3950, diaparatribe G3859, orgilos G3711, logomachia G3055, thymoo G2373, thymomacheo G2371,
aganaktesis G0024): face for every hit, by reading, with the parties (#1963 ruling 6.2). Faces are labelled
5A-5Z and 5AA-5AB so they do not clash with units 1-4. Faces are set by verse; a verse whose hits need
different faces is set by (reference, position) in POS.
Writes anger-unit5-faces-v1-20261005.csv (reference,position,strong,face,face_name,angry_one,toward,other_parties)
and merges face/face_name into the unit pull. No DB access."""
import csv
FACES = {
 '5A': ("God's wrath revealed, stored up, remaining, coming: the cause named", 'God', 'the ungodly and unrighteous, the hard heart, the one who does not obey the Son, the sons of disobedience', 'the truth suppressed; the law; those who hinder the gospel; this people'),
 '5B': ('Provoked with that generation; sworn in wrath', 'God', 'the wilderness generation', 'the Holy Spirit who says "Today"; the brothers warned; the unbelieving heart'),
 '5C': ('The wrath to come, and deliverance from it', 'God', 'the Pharisees and Sadducees, the crowds; "we" once children of wrath', 'John the Baptist; Jesus who delivers; his blood; God rich in mercy'),
 '5D': ('Wrath shown and endured with patience: vessels of wrath and of mercy', 'God', 'vessels of wrath prepared for destruction', 'vessels of mercy prepared for glory'),
 '5E': ("Left to God's wrath; the authority as its servant", 'God', 'the wrongdoer, the enemy', 'the beloved who do not avenge; the governing authority with the sword; conscience'),
 '5F': ('The great day of wrath: the wrath of the Lamb; your wrath came', 'God and the Lamb', 'the kings of the earth and everyone, slave and free; the nations; this people', 'mountains and rocks; the dead; the servants, prophets and saints'),
 '5G': ('The cup, the winepress, the bowls: the wrath finished', 'God', 'the one who worships the beast; Babylon; the nations', 'angels, the four living creatures, the Lamb, the rider whose mouth holds the sword'),
 '5H': ('"With a foolish nation I will make you angry": God provokes Israel', 'Israel (made angry)', 'a foolish nation', 'God through Moses; Paul who quotes it'),
 '5I': ("Jesus's anger and indignation", 'Jesus', 'those who watched to accuse him; the disciples who rebuked the children', 'the man with the withered hand; the children'),
 '5J': ('The master and the king in the parables', 'the master, the king, the master of the house', 'the unforgiving servant, the murderers, the invited who made excuses', 'the jailers, the troops; the poor, crippled, blind and lame brought in'),
 '5K': ("The devil's great wrath; the dragon's fury", 'the devil, the dragon', 'the earth and sea, the woman, the rest of her offspring', 'the heavens who rejoice; those who keep the commandments and hold the testimony of Jesus'),
 '5L': ('Anger in the lists of what is put away', 'people', '-', 'the flesh and the Spirit; "now you must put them all away"'),
 '5M': ("A person's anger governed: be angry and do not sin; slow to anger; at a brother; in prayer; in the overseer; not in love", 'people, brothers, the overseer', 'a brother, a neighbour', 'the devil given no opportunity; the righteousness of God; the council; love'),
 '5N': ('Enraged at a word heard: crowds and councils, the nations', 'the synagogue at Nazareth, the council, the Ephesian craftsmen, the nations', 'Jesus, the apostles, Stephen, Paul, the Lord and his Anointed', 'Gamaliel; the Holy Spirit in Stephen; Artemis; David by the Holy Spirit'),
 '5O': ("The ruler's fury: Herod", 'Herod the Great, Herod Agrippa', 'the children of Bethlehem; Tyre and Sidon', 'the wise men; Blastus; an angel of the Lord'),
 '5P': ("Not afraid of the king's anger", "the king (Pharaoh)", 'Moses', '"him who is invisible"'),
 '5Q': ('Indignant at waste', 'the disciples, some there', 'the woman with the ointment', 'Jesus who defends her; the poor'),
 '5R': ('Indignant at rivals', 'the ten', 'James and John', 'Jesus, who calls them to serve'),
 '5S': ("Indignant at Jesus's works and the apostles' teaching", 'the chief priests and scribes, the ruler of the synagogue, the crowd, the priests and Sadducees', 'Jesus, the healed, the children, Peter and John', 'the woman bound eighteen years; the children crying "Hosanna"'),
 '5T': ('The older brother', 'the older son', 'his father, his brother', 'the servant who tells him'),
 '5U': ("Paul's spirit provoked; greatly annoyed", 'Paul', 'the idols of Athens; the spirit of divination', 'the slave girl; the name of Jesus Christ'),
 '5V': ('Indignation produced by godly grief', 'the Corinthians', '(their own wrong)', 'Paul, his letter'),
 '5W': ('Strife among believers, and its source', 'believers, the conceited, those who cause divisions', 'one another', 'passions at war within; the flesh; envy; foolish controversies'),
 '5X': ('The sharp disagreement', 'Paul and Barnabas', 'each other', 'Mark; Silas; the brothers who commend'),
 '5Y': ('Provoke: children to anger; one another to love; zeal that stirs', 'fathers; believers; the Corinthians', 'children; one another; the Macedonians', 'the discipline and instruction of the Lord'),
 '5Z': ('Fighting without, fear within', '(not named)', 'Paul and his companions', 'God who comforts the downcast; Titus'),
 '5AA': ('Hot and cold: no anger in the verse', '-', 'the church in Laodicea', 'the one who speaks and will spit them out'),
 '5AB': ('The passion of her sexual immorality: no anger in the verse', '-', 'all nations', 'Babylon the great; the kings and merchants'),
}
A = {}
POS = {}
def put(face, refs):
    for r in refs.split(';'):
        r = r.strip()
        if r: A[r] = face
put('5A', 'Rom 1:18;Rom 2:5;Rom 2:8;Joh 3:36;Eph 5:6;Col 3:6;1Th 2:16;Rom 4:15')
put('5B', 'Heb 3:10;Heb 3:11;Heb 3:17;Heb 4:3')
put('5C', 'Mat 3:7;Luk 3:7;Rom 5:9;1Th 1:10;1Th 5:9;Eph 2:3')
put('5D', 'Rom 9:22')
put('5E', 'Rom 12:19;Rom 13:4;Rom 13:5')
put('5F', 'Rev 6:16;Rev 6:17;Rev 11:18;Luk 21:23')
put('5G', 'Rev 14:10;Rev 14:19;Rev 15:1;Rev 15:7;Rev 16:1;Rev 16:19;Rev 19:15')
put('5H', 'Rom 10:19')
put('5I', 'Mar 3:5;Mar 10:14')
put('5J', 'Mat 18:34;Mat 22:7;Luk 14:21')
put('5K', 'Rev 12:12;Rev 12:17')
put('5L', 'Rom 1:29;Rom 13:13;2Cor 12:20;Gal 5:20;Eph 4:31;Col 3:8')
put('5M', 'Eph 4:26;Jam 1:19;Jam 1:20;Mat 5:22;1Ti 2:8;Tit 1:7;1Cor 13:5')
put('5N', 'Luk 4:28;Act 5:33;Act 7:54;Act 19:28;Act 4:25')
put('5O', 'Mat 2:16;Act 12:20')
put('5P', 'Heb 11:27')
put('5Q', 'Mat 26:8;Mar 14:4')
put('5R', 'Mat 20:24;Mar 10:41')
put('5S', 'Luk 13:14;Joh 7:23;Mat 21:15;Act 4:2')
put('5T', 'Luk 15:28')
put('5U', 'Act 17:16;Act 16:18')
put('5V', '2Cor 7:11')
put('5W', 'Jam 4:1;1Cor 1:11;1Cor 3:3;Phili 1:15;1Ti 6:4;1Ti 6:5;Tit 3:9;2Ti 2:23;Rom 16:17;Gal 5:26')
put('5X', 'Act 15:39')
put('5Y', 'Eph 6:4;Col 3:21;Heb 10:24;2Cor 9:2')
put('5Z', '2Cor 7:5')
put('5AA', 'Rev 3:15;Rev 3:16')
put('5AB', 'Rev 14:8;Rev 18:3')
# Rev 11:18: the nations raged (5N, position 1); your wrath came (5F, position 4)
POS[('Rev 11:18', '1')] = '5N'
pull = 'anger-unit5-greek-pull-v1-20261005.csv'
rows = list(csv.DictReader(open(pull, encoding='utf-8')))
miss = [r['reference'] for r in rows if r['reference'] not in A]
assert not miss, miss
extra = set(A) - {r['reference'] for r in rows}
assert not extra, extra
with open('anger-unit5-faces-v1-20261005.csv', 'w', encoding='utf-8', newline='') as f:
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
