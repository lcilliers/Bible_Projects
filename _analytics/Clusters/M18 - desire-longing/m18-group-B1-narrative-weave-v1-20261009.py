"""Weave of M18 group B, set 1 (the delight verbs) into the narrative (#1993, item F), 2026-10-09.

Reading: m18-group-B1-delight-reading-v1-20261009.md. Register: m18-group-B1-register-v1-20261009.csv.
Researcher ruling (verbatim): "delight associated with God goes to 13.1, separate section; HIB delight goes into 10.1".
So: God's delight goes into the 13.1 section *Delight* (including the verses first proposed for 13.1 Purposing and for
10.9). A person's delight gets one account in a new 10.1 section *Delight*. The existing 10.6 *Delight* section is moved
there whole, so delight has one account (#1930), and 10.6 keeps a pointer.
Same mechanics and quote check as m18-group-G-narrative-weave-v1-20261009.py (every inserted quotation is checked against
the ESV in iba.db, read-only). Run with --dry to check only; without it, it writes only if the check passes.
"""
import glob, importlib.util, os, re, shutil, sqlite3, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.abspath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v2-20261006.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
DATE = '20261009'


def current(prefix):
    files = glob.glob(os.path.join(NARR, prefix + '*.md'))
    assert len(files) == 1, (prefix, files)
    return files[0]


# the 10.6 Delight section, moved whole into 10.1
w6 = open(current('10-06-'), encoding='utf-8').read()
m6 = re.search(r'\n## Delight\n\n(.*?)\n\n## Wanting that owns the one who wants', w6, re.S)
assert m6, '10.6 Delight section not found'
MOVED = m6.group(1)

NEW_10_1 = '''## Delight

''' + MOVED + '''

### On God's word, and on God

Delight in God's word is said beside other inner acts, and it does not take their place.
- **Beside fear.** "Blessed is the man who fears the Lord, who greatly delights in his commandments!" (Psalm 112:1). Fear and delight are said of one man in one breath (*Fear* above).
- **Beside asking to be led.** "Lead me in the path of your commandments, for I delight in it. Incline my heart to your testimonies, and not to selfish gain!" (Psalm 119:35–36). He gives his delight as the reason to be led, and in the next breath asks for his heart to be inclined. I read that delighting in the way does not make a man able to steer himself on it.
- **Beside not forgetting, and love.** "I will delight in your statutes; I will not forget your word" (Psalm 119:16), "as much as in all riches" (119:14). "I find my delight in your commandments, which I love" (119:47).
- **Inward, and at war.** "For I delight in the law of God, in my inner being, but I see in my members another law waging war against the law of my mind" (Romans 7:22–23). The delight is real and it is inward, and it does not carry the members with it. The cry that follows is in Chapter 2 (7:24), and the divided service in Chapter 7 (7:25).

Delight set on God himself comes, in these verses, after something else has been let go.
- **After envy.** "Whom have I in heaven but you? And there is nothing on earth that I desire besides you. My flesh and my heart may fail, but God is the strength of my heart and my portion forever" (Psalm 73:25–26). The same man had said, "For I was envious of the arrogant when I saw the prosperity of the wicked" (73:3).
- **After one's own pleasure.** "If you turn back your foot from the Sabbath, from doing your pleasure on my holy day … then you shall take delight in the Lord" (Isaiah 58:13–14).
- **In place of gold.** Eliphaz offers it to Job as a condition: "if you lay gold in the dust … then the Almighty will be your gold and your precious silver. For then you will delight yourself in the Almighty and lift up your face to God" (Job 22:24–26).
- **In peace.** "But the meek shall inherit the land and delight themselves in abundant peace" (Psalm 37:11), in the psalm that says "Delight yourself in the Lord" (37:4; 10.6).

Job asks it of the godless: "Will God hear his cry when distress comes upon him? Will he take delight in the Almighty? Will he call upon God at all times?" (Job 27:9–10). I read the questions as setting a cry made only in distress against calling at all times. What lies between the two is delight.

### When it looks right, and when it is missing

Delight can look right. "Yet they seek me daily and delight to know my ways, as if they were a nation that did righteousness and did not forsake the judgment of their God; they ask of me righteous judgments; they delight to draw near to God" (Isaiah 58:2). The next verse is the one above: in the day of their fast they seek their own pleasure and oppress their workers (58:3). The delight is named twice, and the "as if" once. I read that delight in drawing near can sit beside oppression without the person seeing the two together.

- **A word scorned.** "Behold, their ears are uncircumcised, they cannot listen; behold, the word of the Lord is to them an object of scorn; they take no pleasure in it" (Jeremiah 6:10). The prophet is set beside them: "Therefore I am full of the wrath of the Lord; I am weary of holding it in" (6:11). They take no pleasure in the word he carries, and he is worn out holding what it holds (10.2, 10.13).
- **Not wanting him, by reckoning.** Those who "spend their days in prosperity" say, "Depart from us! We do not desire the knowledge of your ways. What is the Almighty, that we should serve him? And what profit do we get if we pray to him?" (Job 21:13–15). The not-wanting is worked out as a sum.
- **No delight in blessing.** "He loved to curse; let curses come upon him! He did not delight in blessing; may it be far from him!" (Psalm 109:17), of one who "did not remember to show kindness, but pursued the poor and needy" (109:16). The cursing is pictured soaking in: "may it soak into his body like water, like oil into his bones!" (109:18). I read the figure as what a man delights in becoming his own substance (10.5).
- **Questioned, and overruled.** Joab asks, "why does my lord the king delight in this thing?" (2 Samuel 24:3), and "the king's word prevailed against Joab" (24:4). Afterwards "David's heart struck him after he had numbered the people" (24:10; Chapter 8). His delight was questioned by another person, overruled, and then judged by his own heart.

### In a person

- **Haste into the cost.** "And the young man did not delay to do the thing, because he delighted in Jacob's daughter" (Genesis 34:19). The thing was the circumcision her brothers had asked for "deceitfully" (34:13). The delight that had seized her (34:2; 10.6, *A person*) now hurries him into their trap.
- **A king's delight decides a life.** "She would not go in to the king again, unless the king delighted in her and she was summoned by name" (Esther 2:14). Beside it, each woman "was given whatever she desired to take with her" (2:13), and Esther "asked for nothing except what Hegai the king's eunuch, who had charge of the women, advised" (2:15). One woman's whole future hangs on another's delight. Esther does not use what she could have asked for.
- **Imagined for oneself.** Haman, reading the king's delight by his own (above), spells out the honour he thinks is his: "let royal robes be brought, which the king has worn, and the horse that the king has ridden, and on whose head a royal crown is set" (Esther 6:8). The king answers, "Hurry; take the robes and the horse, as you have said, and do so to Mordecai the Jew" (6:10). Haman proclaims it himself, and then "hurried to his house, mourning and with his head covered" (6:12). I read that the honour he designed for his own wanting became the measure of his shame.
- **Claimed falsely.** Saul thought, "Let me give her to him, that she may be a snare for him", and told his servants, "Speak to David in private and say, 'Behold, the king has delight in you'" (1 Samuel 18:21–22). The word of delight is the snare (10.11).

### Wishing

The same Hebrew word is often rendered "wish" or "desire".
- **To contend with God.** "If one wished to contend with him, one could not answer him once in a thousand times" (Job 9:3). Four chapters later the wish is declared: "But I would speak to the Almighty, and I desire to argue my case with God" (13:3), turned away from the friends: "worthless physicians are you all" (13:4). The wish he first judged hopeless, he later states.
- **To justify another.** Elihu: "If you have any words, answer me; speak, for I desire to justify you" (Job 33:32), "to bring back his soul from the pit" (33:30).
- **Not wanting a duty.** "And if the man does not wish to take his brother's wife" (Deuteronomy 25:7), and "if he persists, saying, 'I do not wish to take her'" (25:8), then the sandal and the spit, and "the name of his house shall be called in Israel, 'The house of him who had his sandal pulled off'" (25:10). The law does not force the wanting. It makes the not-wanting public, and gives it a name (10.10).
- **Favour called for over a body.** Beside Amasa, just killed, one of Joab's men calls, "Whoever favors Joab, and whoever is for David, let him follow Joab" (2 Samuel 20:11). The people stopped at the sight (20:12), and once the body was covered, "all the people went on after Joab" (20:13). I read that the sight held them back and the covering let them go.
- **A ruler's pleasure.** "Be not hasty to go from his presence. Do not take your stand in an evil cause, for he does whatever he pleases" (Ecclesiastes 8:3). A king's pleasure is a reason for care. The same words are used of God (13.1, *Delight*).

### A child's delight

- "that you may nurse and be satisfied from her consoling breast; that you may drink deeply with delight from her glorious abundance" (Isaiah 66:11), and "you shall be carried upon her hip, and bounced upon her knees. As one whom his mother comforts, so I will comfort you" (66:12–13). The delight of a child fed and dandled. The comforting in the last line is God's own (13.1). I read it as a delight that is received, not worked for.
- "The nursing child shall play over the hole of the cobra, and the weaned child shall put his hand on the adder's den. They shall not hurt or destroy in all my holy mountain" (Isaiah 11:8–9). The word for delight is a child's play, where there is no more harm and so no fear.

### God's delight in a person's hands

What God delights in is in 13.1 (*Delight*). The verses also show what a person does with it. Joshua and Caleb rest their courage on it, "If the Lord delights in us, he will bring us into this land" (Numbers 14:8). A man betrayed by his friend learns of it from what did not happen (Psalm 41:9, 11). Mockers throw it at a sufferer (Psalm 22:8). And David leaves himself to it without presuming it: "behold, here I am, let him do to me what seems good to him" (2 Samuel 15:26).
'''

ADD_13_1_STRENGTH = '''**Not strength, and truth within.** "let not the mighty man boast in his might … but let him who boasts boast in this, that he understands and knows me, that I am the Lord who practices steadfast love, justice, and righteousness in the earth. For in these things I delight, declares the Lord" (Jeremiah 9:23–24). "His delight is not in the strength of the horse, nor his pleasure in the legs of a man, but the Lord takes pleasure in those who fear him, in those who hope in his steadfast love" (Psalm 147:10–11). Strength is turned down twice, once as a boast and once as a delight. And his delight looks inward: "Behold, you delight in truth in the inward being, and you teach me wisdom in the secret heart" (Psalm 51:6), said by one who has just said "in sin did my mother conceive me" (51:5). He delights in truth where it is hidden, and he teaches there.
'''

ADD_13_1_WHOM = '''**Whom he delights in, and why.** "He brought me out into a broad place; he rescued me, because he delighted in me" (2 Samuel 22:20; Psalm 18:19). His delight is the reason given for the rescue. It is given as a name: "you shall be called My Delight Is in Her, and your land Married; for the Lord delights in you" (Isaiah 62:4), in place of Forsaken and Desolate, "as the bridegroom rejoices over the bride, so shall your God rejoice over you" (62:5). It holds a man who falls: "The steps of a man are established by the Lord, when he delights in his way; though he fall, he shall not be cast headlong, for the Lord upholds his hand" (Psalm 37:23–24). The fall is not denied. And it can be seen by a stranger. The queen of Sheba, who "did not believe the reports until I came and my own eyes had seen it" (1 Kings 10:7), says, "Blessed be the Lord your God, who has delighted in you and set you on the throne of Israel! Because the Lord loved Israel forever, he has made you king, that you may execute justice and righteousness" (1 Kings 10:9; 2 Chronicles 9:8). She reads his delight from what she saw, and names what it is for.

**His delight in people's mouths.** Joshua and Caleb: "If the Lord delights in us, he will bring us into this land and give it to us" (Numbers 14:8), with "do not fear the people of the land" (14:9); the congregation "said to stone them with stones" (14:10). A man whose "close friend in whom I trusted, who ate my bread, has lifted his heel against me" (Psalm 41:9) says, "By this I know that you delight in me: my enemy will not shout in triumph over me" (41:11). The mockers: "He trusts in the Lord; let him deliver him; let him rescue him, for he delights in him!" (Psalm 22:8). The words that are thanks in Psalm 18:19 are a taunt here, and the sufferer answers God, not them: "Yet you are he who took me from the womb" (22:9). David will not presume it: "But if he says, 'I have no pleasure in you,' behold, here I am, let him do to me what seems good to him" (2 Samuel 15:26). What the person does with it is in 10.1 (*Delight*).
'''

ADD_13_1_OFFERING = '''**Not the offering itself.** Five verses say he does not delight in sacrifice, and each sets something else in its place.
- "What to me is the multitude of your sacrifices? says the Lord; I have had enough of burnt offerings of rams and the fat of well-fed beasts; I do not delight in the blood of bulls, or of lambs, or of goats" (Isaiah 1:11). Two verses on: "I cannot endure iniquity and solemn assembly" (1:13).
- "In sacrifice and offering you have not delighted, but you have given me an open ear" (Psalm 40:6), and the answer: "I delight to do your will, O my God; your law is within my heart" (40:8).
- "For you will not delight in sacrifice, or I would give it; you will not be pleased with a burnt offering. The sacrifices of God are a broken spirit; a broken and contrite heart, O God, you will not despise" (Psalm 51:16–17).
- "For I desire steadfast love and not sacrifice, the knowledge of God rather than burnt offerings" (Hosea 6:6), after "Your love is like a morning cloud, like the dew that goes early away" (6:4). The "love" of 6:4 and the "steadfast love" of 6:6 are one Hebrew word, *ḥesed*. What he desires is the very thing their love lacks: that it last.
- And then: "then will you delight in right sacrifices, in burnt offerings and whole burnt offerings" (Psalm 51:19). The offerings he did not delight in (51:16) he will delight in, after the broken heart.

The verses do not say he has no use for offerings; David says he would give them. Each names something inward that comes first: an ear opened, the law in the heart, a broken heart, a love that lasts. I read that the offering is weighed by what is inside the one who brings it.
'''

ADD_13_1_PLEASES = '''Three more verses say it. "Our God is in the heavens; he does all that he pleases" (Psalm 115:3), answering "Why should the nations say, 'Where is their God?'" (115:2), beside idols that "have mouths, but do not speak" (115:5). "The Lord was pleased, for his righteousness' sake, to magnify his law and make it glorious" (Isaiah 42:21). The pleasure has a reason, and it is set beside a servant who "sees many things, but does not observe them" (42:20). And of his word: "it shall not return to me empty, but it shall accomplish that which I purpose" (Isaiah 55:11), where "purpose" is the delight word. The same words are used of a king, "he does whatever he pleases" (Ecclesiastes 8:3), in 10.1.
'''

OPS = {
'10-01-': [
 ('replace', 'Anger, fear and anxiety are the feelings I have followed through their verses so far.',
  'Anger, fear, anxiety and delight are the feelings I have followed through their verses so far.'),
 ('replace', 'Fear and anxiety have sections of their own,', 'Fear, anxiety and delight have sections of their own,'),
 ('before_line', '## When feeling changes character', NEW_10_1),
 ('after_line', '- **Provoking** is what love does not do.',
  '- **Delight** is set on God\'s commandments by the man who fears him (Psalm 112:1), and on war by the peoples God scatters (Psalm 68:30). The same claim about God\'s delight is thanks in one psalm and a taunt in another (Psalm 18:19; 22:8). The section on delight above sets out what it is set on.'),
],
'10-06-': [
 ('replace', '\n## Delight\n\n' + MOVED + '\n\n## Wanting that owns',
  '\n## Delight\n\nDelight has its own account in 10.1 (*Delight*). Beside wanting it shows what a want is set on, and how it can end or be misread. The verses are given there.\n\n## Wanting that owns'),
 ('replace', 'is below (*Delight*)', 'is in 10.1 (*Delight*)'),
],
'13-01-': [
 ('before_line', '**What he desires.** The verses also give', ADD_13_1_STRENGTH),
 ('before_line', '**What he has no pleasure in.**', ADD_13_1_WHOM),
 ('before_line', '**He does what pleases him.**', ADD_13_1_OFFERING),
 ('before_line', 'His delight stands beside his choosing', ADD_13_1_PLEASES),
 ('replace', 'What a person delights in is in 10.6.', 'What a person delights in is in 10.1 (*Delight*).'),
],
}


def apply(text, mode, anchor, ins):
    lines = text.split('\n')
    if mode == 'replace':
        assert text.count(anchor) == 1, ('replace count', anchor[:60], text.count(anchor))
        return text.replace(anchor, ins)
    idx = [i for i, l in enumerate(lines) if anchor in l]
    assert len(idx) == 1, (mode, anchor[:60], idx)
    i = idx[0]
    if mode == 'after_line':
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
        if mode == 'replace' or ins is NEW_10_1:
            ins = ins.replace(anchor, '').replace(MOVED, '')  # moved text was checked when first woven
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
                text = norm(verse_text(book, ch, range(min(vs) - 1, max(vs) + 2)))
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
