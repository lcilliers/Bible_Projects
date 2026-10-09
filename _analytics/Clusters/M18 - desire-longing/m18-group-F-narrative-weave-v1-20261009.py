"""Weave of M18 group F (precious) into the narrative (#1993, item F), 2026-10-09.

Reading: m18-group-F-reading-v1-20261009.md. Register: m18-group-F-register-v1-20261009.csv.
Same mechanics as m18-group-E-narrative-weave-v1-20261009.py, with the quote check of every inserted quotation
against the ESV in iba.db (read-only). Run with --dry to check only; without it, it writes only if the check passes.
"""
import glob, importlib.util, os, re, shutil, sqlite3, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.abspath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v2-20261006.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
DATE = '20261009'

PRECIOUS = '''## Precious

The Hebrew *yāqār* and the Greek *timios*, "precious", name a worth. The same words are rendered *rare*, *costly*, *splendor*, *honor* and *dear* (Chapter 11 §4). A thing is precious when it is weighed against other things and comes out higher.

Wisdom is weighed against every want: *"She is more precious than jewels, and nothing you desire can compare with her"* (Proverbs 3:15). The comparison is not only with jewels but with *"nothing you desire"* (3:15): all of a person's wants are put on the other side of the scale. Job weighs the same thing and adds that its worth is not known: *"Man does not know its worth, and it is not found in the land of the living"* (Job 28:13); *"It cannot be valued in the gold of Ophir, in precious onyx or sapphire"* (28:16). Proverbs says what wisdom is worth. Job says that man does not know it. His chapter ends with where it is found, in the fear of the Lord (28:28; 10.2).

Faith is weighed too, and the trial shows its worth: *"so that the tested genuineness of your faith—more precious than gold that perishes though it is tested by fire—may be found to result in praise and glory and honor at the revelation of Jesus Christ"* (1 Peter 1:7). The verse before names the trial as grief: *"In this you rejoice, though now for a little while, if necessary, you have been grieved by various trials"* (1:6). The verse after names love and joy toward someone not seen: *"Though you have not seen him, you love him. Though you do not now see him, you believe in him and rejoice with joy that is inexpressible and filled with glory"* (1:8). Gold is tested by fire and still perishes. Faith is tested and is found. I read that the grief is where the worth is shown, and that the joy is held in the same time, not after it.

What is precious makes a person wait. *"See how the farmer waits for the precious fruit of the earth, being patient about it, until it receives the early and the late rains. You also, be patient. Establish your hearts, for the coming of the Lord is at hand"* (James 5:7–8). James has just spoken to the rich: *"You have laid up treasure in the last days"* (5:3); *"the wages of the laborers who mowed your fields, which you kept back by fraud, are crying out against you"* (5:4); *"You have fattened your hearts in a day of slaughter"* (5:5). Two hearts stand a few verses apart. One is fattened on what it hoarded; the other is established by waiting. I read that the farmer waits because he values the fruit, while the rich would not wait, and kept back what was owed.

What is precious can be a refuge. God lays *"a stone, a tested stone, a precious cornerstone, of a sure foundation: 'Whoever believes will not be in haste'"* (Isaiah 28:16). He says it to scoffers who had made another refuge: *"we have made lies our refuge, and in falsehood we have taken shelter"* (28:15). The one who believes is not hurried. Peter takes up the stone, *"a cornerstone chosen and precious, and whoever believes in him will not be put to shame"* (1 Peter 2:6), and adds, *"So the honor is for you who believe"* (2:7).

What a person holds precious shows in what he gives. David: *"So I have provided for the house of my God, so far as I was able … all sorts of precious stones and marble"* (1 Chronicles 29:2); and from his own treasure, *"because of my devotion to the house of my God I give it to the house of my God"* (29:3). Of the king who *"shall magnify himself above all"* (Daniel 11:37) it is said, *"He shall honor the god of fortresses instead of these. A god whom his fathers did not know he shall honor with gold and silver, with precious stones and costly gifts"* (11:38). The gifts are of one kind. David gives out of devotion to God's house. The king honours a god of fortresses, and he is a man who sets himself above every god. I read that he honours the strength he wants.

A gift can follow what was seen. The queen of Sheba came *"to test him with hard questions"* and *"told him all that was on her mind"* (1 Kings 10:1–2). When she had seen, *"there was no more breath in her"* (10:5). *"I did not believe the reports until I came and my own eyes had seen it. And behold, the half was not told me"* (10:7). Then *"she gave the king 120 talents of gold, and a very great quantity of spices and precious stones"* (10:10), and *"King Solomon gave to the queen of Sheba all that she desired"* (10:13). She came testing and doubting, and she gave after she had seen. Each gave the other.

Honour is held, and other things are kept off. *"Let marriage be held in honor among all, and let the marriage bed be undefiled"* (Hebrews 13:4), and next, *"Keep your life free from love of money, and be content with what you have, for he has said, 'I will never leave you nor forsake you'"* (13:5). One thing is held in honour; from another the life is kept free; and the reason given for contentment is his presence. Honour given by others can stand beside one who will not give it. After *"Saul was even more afraid of David. So Saul was David's enemy continually"* (1 Samuel 18:29) comes *"David had more success than all the servants of Saul, so that his name was highly esteemed"* (18:30; 10.12). The others esteemed him; Saul feared him.

Splendour can entice. Job swears: *"if I have looked at the sun when it shone, or the moon moving in splendor, and my heart has been secretly enticed, and my mouth has kissed my hand, this also would be an iniquity to be punished by the judges, for I would have been false to God above"* (Job 31:26–28). The verses before are about gold: *"If I have made gold my trust or called fine gold my confidence"* (31:24). The splendour is in the moon. The enticement is in the heart, it is secret, and it comes out in a small act, a kiss of the hand. I read the eye, the heart and the mouth in one sentence (*Through the eye*, above), and the small act counted as falseness to God.

Splendour also passes. *"But the wicked will perish; the enemies of the Lord are like the glory of the pastures; they vanish—like smoke they vanish away"* (Psalm 37:20). The psalm opens, *"Fret not yourself because of evildoers; be not envious of wrongdoers!"* (37:1; *Jealousy and envy*). I read the figure as an answer to the envy: what might be envied is the bloom of a field, and smoke.

Splendour can cover what is inside. In the vision, *"The woman was arrayed in purple and scarlet, and adorned with gold and jewels and pearls, holding in her hand a golden cup full of abominations and the impurities of her sexual immorality"* (Revelation 17:4). The cup is gold, and it is full of what is unclean. The adornment and the cup are held by the same figure (Chapter 12, *Inner and outer impurity*).
'''

OPS = {
'10-06-': [
 ('before_line', '## Possessions', PRECIOUS),
 ('after_line', "Longing for God's word is pictured as breathing hard",
  'Steadfast love is called precious, and the valuing becomes shelter: *"How precious is your steadfast love, O God! The children of mankind take refuge in the shadow of your wings. They feast on the abundance of your house, and you give them drink from the river of your delights"* (Psalm 36:7–8). The psalm opens on the other man: *"there is no fear of God before his eyes"* (36:1; Chapter 12). What is valued here is not a gift but his love. I read that the valuing draws them near: they shelter, feast and drink in his house.'),
 ('after_line', 'Greed harms more than the greedy.',
  'Proverbs gives two ways to fill a house. The sinners\' enticement: *"we shall find all precious goods, we shall fill our houses with plunder"* (Proverbs 1:13). Wisdom\'s: *"By wisdom a house is built, and by understanding it is established; by knowledge the rooms are filled with all precious and pleasant riches"* (24:3–4). The second stands in the chapter that opens, *"Be not envious of evil men, nor desire to be with them, for their hearts devise violence"* (24:1–2). The want is the same, a full house. What fills it differs, and so does the heart behind it. And the want can stop short: *"Whoever is slothful will not roast his game, but the diligent man will get precious wealth"* (12:27). I read the slothful man as one who has caught the game and will not finish it.'),
 ('after_line', 'The loss takes many forms.',
  'The lament over Babylon shows what was grieved. The merchants weep *"since no one buys their cargo anymore, cargo of gold, silver, jewels, pearls"*, and the list runs on to *"horses and chariots, and slaves, that is, human souls"* (Revelation 18:11–13). Human souls stand last in a list of goods. The cry is for the adornment: *"Alas, alas, for the great city that was clothed in fine linen, in purple and scarlet, adorned with gold, with jewels, and with pearls! For in a single hour all this wealth has been laid waste"* (18:16–17). I read that the grief is for the trade and the wealth, and not for the souls in the cargo.'),
],
'10-04-': [
 ('after_line', '- A whole people looked at the servant of the Lord',
  '- A price can be set on a person, and called lordly in irony: "Then the Lord said to me, \'Throw it to the potter\'—the lordly price at which I was priced by them" (Zechariah 11:13). It was thirty pieces of silver (11:12). Matthew reads it of the silver Judas brought back when he "changed his mind": "the price of him on whom a price had been set by some of the sons of Israel" (Matthew 27:3, 9).'),
],
'13-01-': [
 ('after_line', '- A people valued:',
  '- A son held dear while spoken against. Ephraim grieves: *"after I had turned away, I relented, and after I was instructed, I struck my thigh; I was ashamed, and I was confounded, because I bore the disgrace of my youth"* (Jeremiah 31:19). God answers: *"Is Ephraim my dear son? Is he my darling child? For as often as I speak against him, I do remember him still. Therefore my heart yearns for him; I will surely have mercy on him, declares the Lord"* (31:20). Speaking against him and remembering him go on together, and the yearning is given as the reason for mercy (10.3, 10.13).\n'
  '- A price paid: *"you were ransomed from the futile ways inherited from your forefathers, not with perishable things such as silver or gold, but with the precious blood of Christ, like that of a lamb without blemish or spot"* (1 Peter 1:18–19). Isaiah speaks of men given in exchange for a people precious in his eyes (above). Peter names the price as the blood of Christ, and what it ransoms from as ways inherited.'),
],
'12-': [
 ('after_line', 'Pride can grow from a beauty that was given.',
  'The king of Tyre is lamented in the same way. *"You were in Eden, the garden of God; every precious stone was your covering"* (Ezekiel 28:13). *"You were blameless in your ways from the day you were created, till unrighteousness was found in you"* (28:15). *"In the abundance of your trade you were filled with violence in your midst, and you sinned"* (28:16). *"Your heart was proud because of your beauty; you corrupted your wisdom for the sake of your splendor"* (28:17). The covering was prepared for him on the day he was made. The heart took the beauty as its ground, and wisdom was spent for splendour. I read the order the verses give: given, blameless, then trade, violence and a proud heart.'),
],
'10-02-': [
 ('after_line', 'Hearing can be taken away, and then wanted.',
  'Before Samuel, *"the word of the Lord was rare in those days; there was no frequent vision"* (1 Samuel 3:1). The word for *rare* is the word for *precious*. When the call came, the boy did not know it: *"Samuel did not yet know the Lord, and the word of the Lord had not yet been revealed to him"* (3:7). Three times he ran to Eli, until *"Eli perceived that the Lord was calling the boy"* and taught him the answer, *"Speak, Lord, for your servant hears"* (3:8–9). The old priest, whose eyes were growing dim (3:2), knew the voice the boy could not yet place. I read hearing that had to be learned, in a time when the word was rare.'),
],
'10-10-': [
 ('before_line', 'Love between two people has its own time in the Song',
  'Company can be too much. *"If you have found honey, eat only enough for you, lest you have your fill of it and vomit it. Let your foot be seldom in your neighbor\'s house, lest he have his fill of you and hate you"* (Proverbs 25:16–17). The neighbour is set beside honey: sweet, and turned by too much into its opposite. The word for *seldom* is the word for *precious*. I read that the visit is kept rare so that it stays welcome.\n'),
],
'10-05-': [
 ('after_line', 'David prays that both ends of the path',
  'What comes out can be sorted. Jeremiah complained, *"Why is my pain unceasing, my wound incurable, refusing to be healed? Will you be to me like a deceitful brook, like waters that fail?"* (Jeremiah 15:18). The answer calls the prophet himself to turn: *"If you return, I will restore you, and you shall stand before me. If you utter what is precious, and not what is worthless, you shall be as my mouth. They shall turn to you, but you shall not turn to them"* (15:19). Precious and worthless are both possible in his mouth. I read the call to return as the answer to the complaint: what he utters is to be sorted before he can be God\'s mouth.'),
],
'10-13-': [
 ('replace', 'Gamaliel stopped it by having the men put outside',
  'Gamaliel, "a teacher of the law held in honor by all the people", stopped it by having the men put outside'),
],
'11-': [
 ('after_line', '- **Knowing that a choice was made.**',
  '- **Precious.** The Hebrew *yāqār* is wisdom weighed above *"nothing you desire"* (Proverbs 3:15), the word *"rare in those days"* (1 Samuel 3:1), a visit kept *seldom* (Proverbs 25:17), *"the moon moving in splendor"* that entices a heart (Job 31:26–27), a name *"highly esteemed"* (1 Samuel 18:30), *"the lordly price"* set on a shepherd (Zechariah 11:13), and a son *"dear"* while spoken against (Jeremiah 31:20). The Greek *timios* is faith tested by fire (1 Peter 1:7), the blood of Christ (1:19), and the jewels of Babylon (Revelation 17:4). What differs is who values, what the thing is weighed against, and whether its worth is known: man does not know wisdom\'s worth (Job 28:13), and Saul would not give the esteem the others gave (1 Samuel 18:29–30). (10.6 *Precious*.)'),
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
