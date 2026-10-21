"""M08 group B (height words): scan decisions (#2156). Reads m08-group-B-scan-v1-20261015.csv and
writes m08-group-B-scan-triage-v1-20261015.csv with one decision per verse.

Researcher, 2026-10-15 (verbatim): "group B - lets do one more scan of these, it seems they are
mostly data.  Set them aside as data unless the terms are supporting other M-codes".

Decisions (each verse read in full; the height word's role is judged against the verse's act):
  P  = pride sense: the height word itself names pride, a lifted-up self, or its being brought low
       (or, once, its other face). Not data; it is M08's own sense and is read with group A.
  S  = supports another M-code: the height word takes part in what another M-coded word in the
       verse says (its measure, its ground, its object, its outcome). Code(s) given.
  D  = data: a measure, a place, a direction or a setting. Note 'God on high' where the height is
       God's dwelling or exaltation with no other M-code joined (13.1 may draw on these later);
       note 'figure' where the verse is the picture whose pride is named elsewhere in the passage.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))

P = {  # n: note
 1: 'what is exalted among men, an abomination (M58); God knows hearts (M47)',
 2: 'arrogant in heart (M47); abomination (M58)', 3: 'haughty and did abomination (M58)',
 4: 'pride of his face; no thought of God (M06)', 8: 'heart proud (M47); wrath (M02)',
 9: 'humbled himself for the pride of his heart (M09, M47)', 13: 'lofty opinion raised against the knowledge of God (M15)',
 25: 'stacked pride words with loftiness (M47 heart)', 26: 'haughty in my holy mountain (M08, M56)',
 27: 'talk so very proudly (M65, M15)', 29: 'loftily they threaten (M65)', 30: 'lift up your horn, haughty neck (M08, M65)',
 31: 'be not proud, hear (M41)', 36: 'heart proud in wealth (M47, M46)', 42: 'do not become proud, but fear (M01, M13)',
 43: 'the great in height hewn down, the lofty brought low (M53): figure of the proud',
 46: 'a haughty spirit before a fall (M47)', 47: 'makes his door high, seeks destruction (M83)',
 48: 'heart haughty before destruction (M47, M05 humility)', 49: 'do not be haughty, associate with the lowly (M09, M63)',
 56: 'daughters of Zion haughty (no other M-code)', 63: 'heart proud, I am a god (M47)',
 64: 'heart proud of its height (M47): the cedar figure named', 65: 'pride of heart deceived; lofty dwelling (M47, M14)',
 75: 'soar aloft like the eagle; I will bring you down (follows Obd 3)',
 102: 'lifted your eyes to the heights against the Holy One (M53 mocked)', 104: 'as 2Ki 19:22 (M53 mocked)',
 108: 'grew proud, to his destruction (M47, M57)', 109: 'heart proud because of beauty (M47, M16)',
 110: 'proud in spirit (M47, M18 better)', 113: 'OTHER FACE: heart lifted up (courageous) in the ways of the Lord (M47); change of character (#1919)',
 117: 'heart not lifted up, eyes not raised (M47)', 120: 'pride of heart; height of the hill; nest as high as the eagle (M47, M08)',
 121: 'no tree to grow to towering height: the lesson of the cedar (M25 death)', 126: 'eyes of the haughty brought low (M53)',
 127: 'inhabitants of the height, the lofty city, laid low (M53)', 138: 'adorn yourself with dignity: God to Job before 40:11-12 (M08 majesty, M71)',
 145: 'many attack me proudly (M06, M10)', 153: 'Shebna carves a tomb on the height (no M-code; passage 22:15-19)',
 161: 'the haughty he knows from afar (M09 lowly, M15)', 162: 'sees everything that is high; king over the sons of pride (M08)',
 169: 'haughty look and arrogant heart (M47, M14)',
}
S = {  # n: (codes, note)
 6: ('M14', 'they return, but not upward: a treacherous turning'),
 7: ('M01', 'afraid of what is high, in old age'),
 10: ('M12', 'your judgments are on high, out of his sight (the wicked)'),
 12: ('M51', 'nor height nor depth will separate us from the love of God'),
 16: ('M09 M47', 'the high and holy One dwells with the contrite and lowly spirit'),
 18: ('M18 M45', 'evil gain to set his nest on high, safe from harm'),
 23: ('M09 M08', 'the lowly brother boasts in his exaltation'),
 32: ('M09 M53', 'I bring low the high tree and make high the low tree'),
 38: ('M23', 'Babylon fortifies her strong height against the Lord'),
 40: ('M53', "the boast against the Lord: 'I have gone up the heights' (mocked)"),
 41: ('M16 M22', 'my servant acts wisely, is high and lifted up (13.1: Jesus)'),
 51: ('M47', 'not the height of his stature; the Lord looks on the heart'),
 53: ('M53', 'as Isa 37:24 (mocked)'),
 62: ('M09 M53', 'exalt that which is low, bring low that which is exalted'),
 69: ('M23', 'lift up your eyes on high and see who created these: his might'),
 70: ('M31 M42', 'bent on turning away, though they call to the Most High'),
 73: ('M09 M22', 'he sets on high those who are lowly'),
 81: ('M22', 'set high above the nations in praise, fame and honour'),
 85: ('M50 M01', 'as high as the heavens, so great his steadfast love to those who fear him'),
 103: ('M12 M61', 'the Lord exalted in justice (13.1; after 5:15 man brought low)'),
 107: ('M41', 'fasting like yours will not make your voice heard on high'),
 115: ('M12', 'God sets the righteous with kings, and they are exalted'),
 119: ('M06 M76', 'my ways higher than your ways, my thoughts than your thoughts'),
 123: ('M09 M12', 'oppression of the poor; the high official watched by a higher'),
 124: ('M19', 'your high walls, in which you trusted'),
 128: ('M41 M54', 'obey, and the Lord will set you high above the nations'),
 131: ('M16 M46', 'folly set in high places, the rich in a low place'),
 136: ('M15', 'higher than heaven: what can you know?'),
 147: ('M12', 'your righteousness reaches the high heavens'),
 154: ('M73 M03', 'the highest people of the earth languish'),
 156: ('M24', 'my eyes are weary with looking upward'),
 159: ('M36', 'bow before God on high: with burnt offerings? (Mic 6:6-8)'),
 176: ('M23 M51', 'strength to comprehend the breadth, length, height and depth (of the love of Christ, v19)'),
 177: ('M12 M61', 'a high priest holy, innocent, exalted above the heavens (13.1: Jesus)'),
}
GOD = {14, 21, 24, 59, 67, 68, 76, 78, 84, 87, 101, 105, 116, 122, 134, 137, 141, 146, 148, 149, 150, 155, 174, 188, 205}
FIGURE = {37: 'Eze 31: the cedar; pride named in 31:10', 168: 'Eze 31: the cedar; pride named in 31:10',
          203: 'Dan 4: the tree; pride named in 4:30, 4:37', 210: 'Dan 4: the tree; pride named in 4:30, 4:37',
          211: 'Dan 4: the tree; pride named in 4:30, 4:37',
          39: 'M72 forward mark (group B triage): the vine towers among the boughs; no pride or other act named in the verse',
          82: 'Saul taller than any (cf 1Sa 16:7, which is S)'}
NOTE = {142: 'Job: my witness is on high (an act with no M-code)', 14: 'God raised David on high'}

rows = list(csv.DictReader(open(os.path.join(HERE, 'm08-group-B-scan-v1-20261015.csv'), encoding='utf-8')))
assert not (set(P) & set(S)), set(P) & set(S)
out = os.path.join(HERE, 'm08-group-B-scan-triage-v1-20261015.csv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['n', 'reference', 'decision', 'supports_mcodes', 'note', 'b_words', 'other_mwords', 'narrative', 'text'])
    for r in rows:
        n = int(r['n'])
        if n in P: d, codes, note = 'P pride sense', '', P[n]
        elif n in S: d, (codes, note) = 'S supports', S[n]
        else:
            d, codes = 'D data', ''
            note = '; '.join(x for x in ('God on high' if n in GOD else '', FIGURE.get(n, ''), NOTE.get(n, '')) if x)
        w.writerow([n, r['reference'], d, codes, note, r['b_words'], r['other_mwords'], r['narrative'], r['text']])
print(out)
