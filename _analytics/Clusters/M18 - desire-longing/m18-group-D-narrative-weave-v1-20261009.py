"""Weave of M18 group D (jealousy, zeal) into the narrative (#1993, item F), 2026-10-09.

Reading: m18-group-D-reading-v1-20261009.md. Register: m18-group-D-register-v1-20261009.csv.
Same mechanics as m18-group-A-narrative-weave-v1-20261009.py, plus a quote check of every inserted quotation
against the ESV in iba.db (read-only). Run with --dry to check only; without it, it writes only if the check passes.
"""
import glob, importlib.util, os, re, shutil, sqlite3, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.abspath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v2-20261006.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
DATE = '20261009'

OPS = {
'10-06-': [
 ('append_line', 'They show several, and what distinguishes them is whose jealousy it is',
  ' The same Hebrew and Greek words are translated "zeal", and the verses on zeal are read here with the rest.'),
 ('after_line', 'I read that the same jealousy for God can stand with the people or end in standing alone.',
  '''**Zeal that consumes the one who has it.** *"For zeal for your house has consumed me, and the reproaches of those who reproach you have fallen on me"* (Psalm 69:9). The verse before says what it cost: *"I have become a stranger to my brothers, an alien to my mother's sons"* (69:8). The zeal eats the one who has it, and it draws onto him the reproach that was meant for God. Another psalm names what lights it: *"My zeal consumes me, because my foes forget your words"* (Psalm 119:139). The psalmist sets himself against them: *"I am small and despised, yet I do not forget your precepts"* (119:141). The first zeal is roused by insult to God's house, the second by the forgetting of his words. When Jesus drove the traders out of the temple, saying *"do not make my Father's house a house of trade"*, *"His disciples remembered that it was written, 'Zeal for your house will consume me'"* (John 2:16–17; 10.3). They understood what they saw by remembering the psalm. I read that zeal, in these verses, is not pictured as a strength the zealous one holds but as a fire that uses him up.

**Zeal for God that does not know.** Paul says of his own people, *"my heart's desire and prayer to God for them is that they may be saved. For I bear them witness that they have a zeal for God, but not according to knowledge. For, being ignorant of the righteousness of God, and seeking to establish their own, they did not submit to God's righteousness"* (Romans 10:1–3). He knows that zeal from inside, and three times he names it as his own:
- *"so extremely zealous was I for the traditions of my fathers"* (Galatians 1:14), beside *"I persecuted the church of God violently and tried to destroy it"* (1:13)
- *"as to zeal, a persecutor of the church"* (Philippians 3:6)
- *"being zealous for God as all of you are this day. I persecuted this Way to the death"* (Acts 22:3–4)

Each time, zeal and persecution stand together. In Philippians the zeal is listed among his gains, and then *"whatever gain I had, I counted as loss for the sake of Christ"* (Philippians 3:7). In Galatians what ended it was not his own correction: *"he who had set me apart before I was born, and who called me by his grace, was pleased to reveal his Son to me"* (Galatians 1:15–16). And in Acts he grants his hearers the zeal he once had. I read zeal as able to be sincere and aimed at God, and still wrong, because it runs ahead of knowing. Paul meets it with his heart's desire and prayer for them, not with contempt. Such zeal can also be stirred by a report: believers *"all zealous for the law"* had *"been told about you that you teach all the Jews who are among the Gentiles to forsake Moses"* (Acts 21:20–21).

**Zeal put on show, and zeal that set aside an oath.** Jehu says, *"Come with me, and see my zeal for the Lord"* (2 Kings 10:16). His zeal is something to be watched from his chariot. The same chapter ends on his heart: *"But Jehu was not careful to walk in the law of the Lord, the God of Israel, with all his heart"* (10:31; 13.1). Saul's zeal broke a sworn word: *"Although the people of Israel had sworn to spare them, Saul had sought to strike them down in his zeal for the people of Israel and Judah"* (2 Samuel 21:2). The guilt outlived him. Years later there was a famine *"for three years, year after year"*, and the Lord said, *"There is bloodguilt on Saul and on his house, because he put the Gibeonites to death"* (21:1). I read a zeal for one's own people that set an oath before God aside, and a guilt that came due after the zealous man was dead. Phinehas's zeal was God's own, and the wrath turned back. Saul's was for the people, and it left bloodguilt behind.

**Jealousy that is God's, in a man.** Phinehas was jealous with God's jealousy. Paul says the same of himself: *"I feel a divine jealousy for you, since I betrothed you to one husband, to present you as a pure virgin to Christ. But I am afraid that as the serpent deceived Eve by his cunning, your thoughts will be led astray from a sincere and pure devotion to Christ"* (2 Corinthians 11:2–3). The picture is the one God uses of himself, a husband's jealousy (13.1). Paul arranged the betrothal, and his jealousy is for the bridegroom. It comes joined to fear, and the fear is for their thoughts.

Zeal for others can be labour. Epaphras is *"always struggling on your behalf in his prayers, that you may stand mature and fully assured in all the will of God. For I bear him witness that he has worked hard for you"* (Colossians 4:12–13). Where the ESV has "worked hard", some manuscripts have "zeal". Zeal for good is set beside the end of fear: *"Now who is there to harm you if you are zealous for what is good? But even if you should suffer for righteousness' sake, you will be blessed. Have no fear of them, nor be troubled"* (1 Peter 3:13–14; 10.12). And it is what the redemption makes: Christ *"gave himself for us to redeem us from all lawlessness and to purify for himself a people for his own possession who are zealous for good works"* (Titus 2:14).'''),
 ('before_line', '**Jealousy among people who would be counted wise.**',
  '''**Jealousy against a person.** Joseph's brothers *"saw that their father loved him more than all his brothers, they hated him and could not speak peacefully to him"* (Genesis 37:4). After the second dream, *"his brothers were jealous of him, but his father kept the saying in mind"* (37:11). Both heard the same dream, and Jacob had just rebuked it (37:10). I read jealousy and keeping as two ways of holding the same words: the brothers hold them against the dreamer, and the father holds them in his mind (10.3).

Envy can spoil what it cannot take. Isaac *"had possessions of flocks and herds and many servants, so that the Philistines envied him"* (Genesis 26:14). The next verse tells of the wells his father's servants had dug, *"stopped and filled with earth"* (26:15). Then *"Abimelech said to Isaac, 'Go away from us, for you are much mightier than we'"* (26:16). Isaac's wealth came because *"The Lord blessed him"* (26:12). I read that the envy could not take the blessing, so it stopped the water and sent the man away.

Jealousy can be aimed at those God has set apart. *"When men in the camp were jealous of Moses and Aaron, the holy one of the Lord, the earth opened and swallowed up Dathan"* (Psalm 106:16–17). In the story their words are *"For all in the congregation are holy, every one of them, and the Lord is among them. Why then do you exalt yourselves above the assembly of the Lord?"* (Numbers 16:3). The jealousy speaks as a claim to equality. Joshua's jealousy was for Moses; theirs was against him.

It can be roused by another's following. After the sick were healed, *"the high priest rose up, and all who were with him … and filled with jealousy they arrested the apostles and put them in the public prison"* (Acts 5:17–18). At Antioch, *"when the Jews saw the crowds, they were filled with jealousy and began to contradict what was spoken by Paul, reviling him"* (13:45). Both times it is at a crowd that has come to someone else, and both times they are "filled" with it. In Jerusalem it turns to arrest, in Antioch to speech (10.5).

Envy can be pictured in a figure. Of the great tree that stands for Assyria, God says, *"I made it beautiful in the mass of its branches, and all the trees of Eden envied it"* (Ezekiel 31:9). The next verse turns to the tree's own heart: *"its heart was proud of its height"* (31:10). I read the envy of the others and the pride of the tree as two answers to the same given beauty (Chapter 12).

Jealousy between brothers can end. *"The jealousy of Ephraim shall depart, and those who harass Judah shall be cut off; Ephraim shall not be jealous of Judah, and Judah shall not harass Ephraim"* (Isaiah 11:13). Jealousy on the one side and harassing on the other end together, in the day when the Lord *"will raise a signal for the nations and will assemble the banished of Israel"* (11:12).
'''),
 ('append_line', 'And "who can stand before jealousy?" (Proverbs 27:4; 10.13).',
  ' It ends with the life. Of the dead: *"Their love and their hate and their envy have already perished, and forever they have no more share in all that is done under the sun"* (Ecclesiastes 9:6; Chapter 2).'),
 ('before_line', 'God\'s jealousy is in 13.1 (*Jealousy*).',
  '''**A husband's jealousy with no witness.** The law gives it somewhere to go. *"If the spirit of jealousy comes over him and he is jealous of his wife who has defiled herself, or if the spirit of jealousy comes over him and he is jealous of his wife, though she has not defiled herself"* (Numbers 5:14), he brings her to the priest with *"a grain offering of jealousy, a grain offering of remembrance, bringing iniquity to remembrance"*, with no oil and no frankincense on it (5:15). The law says plainly that the jealousy may be wrong: it comes over him whether she has defiled herself or not. The matter is not his to settle: *"he shall set the woman before the Lord"* (5:30), and *"The man shall be free from iniquity"* (5:31). Proverbs shows the husband whose jealousy *"will accept no compensation"* (Proverbs 6:35). Set beside him, I read the law as taking the jealousy out of the husband's hands and putting it before God.
'''),
],
'13-01-': [
 ('after_line', 'The jealousy words are used of God, and the verses say what his jealousy is for and what it is against.',
  '- **His name, in the commandment.** *"You shall not bow down to them or serve them, for I the Lord your God am a jealous God, visiting the iniquity of the fathers on the children to the third and fourth generation of those who hate me, but showing steadfast love to thousands of those who love me and keep my commandments"* (Exodus 20:5–6; Deuteronomy 5:9–10). It is given in the commandment against images, and set beside steadfast love: three or four generations against thousands. It is his name: *"for you shall worship no other god, for the Lord, whose name is Jealous, is a jealous God"* (Exodus 34:14). And it is fire: *"Take care, lest you forget the covenant of the Lord your God … For the Lord your God is a consuming fire, a jealous God"* (Deuteronomy 4:23–24). In all three, it is set against other gods and images.'),
 ('append_line', 'Again: *"they moved him to jealousy with their idols"* (Psalm 78:58).',
  ' It has a measure: Judah *"provoked him to jealousy with their sins that they committed, more than all that their fathers had done"* (1 Kings 14:22).'),
 ('append_line', '- **For Zion, ending in his dwelling.**',
  ' The first time it is said, it is the answer to an angel\'s question, *"O Lord of hosts, how long will you have no mercy on Jerusalem and the cities of Judah"* (Zechariah 1:12): *"I am exceedingly jealous for Jerusalem and for Zion. And I am exceedingly angry with the nations that are at ease; for while I was angry but a little, they furthered the disaster"* (1:14–15). Then: *"I have returned to Jerusalem with mercy"* (1:16). His jealousy for her and his anger at those who went beyond his anger are said in one breath.'),
 ('after_line', '- **For Zion, ending in his dwelling.**',
  '- **Roused by prayer, and joined to pity.** When the priests weep, *"Spare your people, O Lord, and make not your heritage a reproach, a byword among the nations. Why should they say among the peoples, \'Where is their God?\'"* (Joel 2:17), *"Then the Lord became jealous for his land and had pity on his people"* (2:18). In Ezekiel it is for his name, with mercy: *"Now I will restore the fortunes of Jacob and have mercy on the whole house of Israel, and I will be jealous for my holy name. They shall forget their shame"* (Ezekiel 39:25–26). In both, his jealousy stands with pity or mercy, and what is taken away is the people\'s reproach or shame.\n'
  '- **Zeal that does the work.** Of the child whose government has no end: *"The zeal of the Lord of hosts will do this"* (Isaiah 9:7). Of the remnant who *"shall again take root downward and bear fruit upward"*: *"The zeal of the Lord will do this"* (2 Kings 19:30–31; Isaiah 37:31–32). Here zeal is named as the one who will do what is promised.\n'
  '- **Put on, when no one stood.** *"He saw that there was no man, and wondered that there was no one to intercede; then his own arm brought him salvation"* (Isaiah 59:16). Then he dresses: *"He put on righteousness as a breastplate, and a helmet of salvation on his head; he put on garments of vengeance for clothing, and wrapped himself in zeal as a cloak"* (59:17). The figure is a warrior arming himself because no one else came. I read the cloak as the outer garment, over the rest, and his wonder at the missing intercessor as what goes before it.'),
 ('append_line', 'In the fire of his jealousy, all the earth shall be consumed"* (Zephaniah 1:18).',
  ' The New Testament names the same fire: for one who goes *"on sinning deliberately after receiving the knowledge of the truth, there no longer remains a sacrifice for sins, but a fearful expectation of judgment, and a fury of fire that will consume the adversaries"* (Hebrews 10:26–27). "Fury" is the zeal word.'),
 ('append_line', '- **Asked about in lament.**',
  ' The opposite is also asked. His zeal is missed: *"Look down from heaven and see, from your holy and beautiful habitation. Where are your zeal and your might? The stirring of your inner parts and your compassion are held back from me"* (Isaiah 63:15). It is named with his inner parts and his compassion. And it is asked to be seen: *"O Lord, your hand is lifted up, but they do not see it. Let them see your zeal for your people, and be ashamed"* (26:11).'),
 ('replace', 'and over them, met with "more grace".',
  'and over them, met with "more grace". It is also named as the doer of what he promises, and put on like a cloak when no one else stands.'),
],
'10-03-': [
 ('after_line', 'What is remembered becomes the material of thought.',
  'Remembering can read an event as it happens. When Jesus drove the traders out of the temple, *"His disciples remembered that it was written, \'Zeal for your house will consume me\'"* (John 2:17; 10.6). And the same words can be held two ways. Of Joseph\'s dream, *"his brothers were jealous of him, but his father kept the saying in mind"* (Genesis 37:11; 10.6).'),
],
'11-': [
 ('append_line', '- **Whose jealousy, and for whom.**',
  ' Zeal can be sincere, aimed at God and still wrong for lack of knowledge (Romans 10:2; Philippians 3:6). It consumes the one who has it (Psalm 69:9). It can be put on show (2 Kings 10:16), or set an oath aside (2 Samuel 21:2). Against a person it spoils what it cannot take (Genesis 26:14–15) and claims equality (Numbers 16:3; Psalm 106:16). A husband\'s jealousy, which may be wrong, is put before God (Numbers 5:14, 30).'),
],
'12-': [
 ('after_line', 'Pride is also a false likeness.',
  'Pride can grow from a beauty that was given. Of the great tree: *"I made it beautiful in the mass of its branches, and all the trees of Eden envied it"* (Ezekiel 31:9); *"Because it towered high and set its top among the clouds, and its heart was proud of its height"* (31:10). The others envied the gift, and the tree was proud of it (10.6).'),
],
}


def current(prefix):
    files = glob.glob(os.path.join(NARR, prefix + '*.md'))
    assert len(files) == 1, (prefix, files)
    return files[0]


def apply(text, mode, anchor, ins):
    lines = text.split('\n')
    if mode == 'replace':
        assert text.count(anchor) == 1, ('replace count', anchor[:60], text.count(anchor))
        return text.replace(anchor, ins)
    idx = [i for i, l in enumerate(lines) if anchor in l]
    assert len(idx) == 1, (mode, anchor[:60], idx)
    i = idx[0]
    if mode == 'append_line':
        lines[i] += ins
    elif mode == 'after_line':
        if lines[i].startswith('- ') and ins.startswith('- '):
            lines[i + 1:i + 1] = [ins]
        else:
            lines[i + 1:i + 1] = ['', ins]
    elif mode == 'before_line':
        lines[i:i] = [ins.rstrip('\n'), '']
    return '\n'.join(lines)


# ---------------------------------------------------------------- quote check (inserted text only)
c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)


def norm(s):
    s = unicodedata.normalize('NFKC', s).lower()
    s = re.sub(r'\[[^\]]*\]', ' ', s)
    s = s.replace('’', "'").replace('‘', "'")
    s = re.sub(r"[^a-z0-9' ]", ' ', s)
    s = s.replace("'", '')
    return re.sub(r'\s+', ' ', s).strip()


def verse_text(book, ch, vs):
    out = []
    for v in vs:
        r = c.execute('SELECT text FROM verse WHERE reference = ? AND deleted = 0', (f'{book} {ch}:{v}',)).fetchone()
        if r: out.append(r[0])
    return ' '.join(out)


QUOTE = re.compile(r'"([^"]+)"')
fails, checked = [], 0
for prefix, ops in OPS.items():
    for mode, anchor, ins in ops:
        if mode == 'replace': ins = ins.replace(anchor, '')
        last_book = None
        for line in ins.split('\n'):
            for m in QUOTE.finditer(line):
                frag = m.group(1)
                if len(frag.split()) < 3: continue
                tail = line[m.end():]
                cm = re.search(r'\(([^()]*\d+:\d+[^()]*)\)', tail)
                if not cm: continue
                cites = list(xr.cites(cm.group(1)))
                if not cites:
                    bare = re.match(r'\s*(\d+):(\d+)(?:[–-](\d+))?', cm.group(1))
                    if bare and last_book:
                        a, b = int(bare.group(2)), int(bare.group(3) or bare.group(2))
                        cites = [(last_book, int(bare.group(1)), v, '') for v in range(a, b + 1)]
                else:
                    last_book = cites[0][0]
                if not cites: fails.append(f'{prefix}: no citation parsed for "{frag[:50]}"'); continue
                book, ch = cites[0][0], cites[0][1]
                vs = sorted({v for b, cc, v, h in cites if b == book and cc == ch})
                text = norm(verse_text(book, ch, range(min(vs), max(vs) + 2)))
                for part in re.split(r'…|\.\.\.', frag):
                    p = norm(part)
                    if p and p not in text:
                        fails.append(f'{prefix}: "{part.strip()[:70]}" not in {book} {ch}:{vs}')
                checked += 1
print(f'quotes checked: {checked}; failures: {len(fails)}')
for f in fails: print('  FAIL', f)

dry = '--dry' in sys.argv
for prefix, ops in OPS.items():
    src = current(prefix)
    text = open(src, encoding='utf-8').read()
    for mode, anchor, ins in ops:
        text = apply(text, mode, anchor, ins)
    m = re.match(r'(.*-v)(\d+)-(\d{8})\.md$', os.path.basename(src))
    new = os.path.join(NARR, f'{m.group(1)}{int(m.group(2)) + 1}-{DATE}.md')
    print(os.path.basename(src), '->', os.path.basename(new))
    if dry or fails: continue
    shutil.copy2(src, os.path.join(NARR, 'archive', os.path.basename(src)))
    open(new, 'w', encoding='utf-8').write(text)
    os.remove(src)
if fails and not dry: sys.exit('not applied: fix failures first')
