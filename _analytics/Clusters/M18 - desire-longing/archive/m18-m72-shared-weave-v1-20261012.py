"""Weave of the M18 x M72 shared verses (#1993, handoff item H), 2026-10-12.

Researcher (chat 2026-10-12, verbatim): "weave §9 as proposed".
Source: m18-m72-shared-reading-v1-20261012.md §9. Text and ops from m18-m72-shared-weave-ops-v1-20261012.py (inlined);
mechanics and quote check from m18-group-C-weave-v1-20261012.py.
Run with --dry to check only; without it, it writes only if the check passes.
"""
import glob, importlib.util, os, re, shutil, sqlite3, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.abspath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v3-20261009.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
DATE = '20261012'
NL = '\n'


def current(prefix):
    files = glob.glob(os.path.join(NARR, prefix + '*.md'))
    assert len(files) == 1, (prefix, files)
    return files[0]




WHOSE = '''- **The king's pleasure, asked for.** The same words come from the asking side. Nehemiah, asked what he was requesting, first "prayed to the God of heaven", then said, "If it pleases the king, and if your servant has found favor in your sight, that you send me to Judah" (Nehemiah 2:4–5). When it was granted he named another measure behind the king's: "And the king granted me what I asked, for the good hand of my God was upon me" (2:8). Memucan put his counsel against Vashti the same way, "If it please the king, let a royal order go out from him" (Esther 1:19), but what drove it was the fear that the women would "look at their husbands with contempt" (1:17). Esther kept the form after the king had offered "even to the half of my kingdom" (5:3): "If it please the king, let the king and Haman come today to a feast that I have prepared for the king" (5:4), and again when he asked her a second time (9:12–13). I read the form as leaving the decision with the king each time, even when he had offered to hand it over. What stands behind the asking differs: prayer, the fear of contempt, silver (Haman, above), a life (7:3).'''

MAL_PEOPLE = '''Malachi has the same pairing of seeking and delight, and God answers it. The people had said, "Everyone who does evil is good in the sight of the Lord, and he delights in them", and asked, "Where is the God of justice?" (Malachi 2:17). The answer takes their own words: "And the Lord whom you seek will suddenly come to his temple; and the messenger of the covenant in whom you delight, behold, he is coming" (3:1). Then: "But who can endure the day of his coming, and who can stand when he appears? For he is like a refiner's fire" (3:2). Their seeking and their delight are taken at their word, and the question turns back on them. I read a delight in what is asked for that has not yet faced what it asks. The comparison with Isaiah 58:2 is mine; each passage says its own part. His coming as refiner is in 13.1 (*Delight*).'''

MAL_GOD = '''**His delight claimed for evildoers.** People can put God's delight on the wrong side. "You have wearied the Lord with your words. But you say, 'How have we wearied him?' By saying, 'Everyone who does evil is good in the sight of the Lord, and he delights in them.' Or by asking, 'Where is the God of justice?'" (Malachi 2:17). His answer is that the one they ask for comes, and comes to refine: "He will sit as a refiner and purifier of silver, and he will purify the sons of Levi and refine them like gold and silver, and they will bring offerings in righteousness to the Lord" (3:3). The delight they put on his lips is answered by refining, and its end is offerings in righteousness. The people's side is in 10.7.'''

DAVID = '''David's look runs in the same order, and the verses name no desire at all. It was "the time when kings go out to battle … But David remained at Jerusalem" (2 Samuel 11:1). "He saw from the roof a woman bathing; and the woman was very beautiful. And David sent and inquired about the woman" (11:2–3). "So David sent messengers and took her" (11:4). Seeing, asking and taking are all there. The wanting is not named, only done. The taking is done by a king's word: he sends, and messengers bring her, as Micah said of those who take "because it is in the power of their hand" (Micah 2:1). Nathan later named the act as despising "the word of the Lord, to do what is evil in his sight" (2 Samuel 12:9). I read the power to send as closing the gap between the look and the taking.'''

RUNNER = '''Wanting can read a sign before the news comes. As the runners came from the battle, "the king said, 'He is a good man and comes with good news'" (2 Samuel 18:27). His first question was not about the battle: "Is it well with the young man Absalom?" (18:29). The news was Absalom's death, and "the king was deeply moved" (18:33). I read the wish shaping how the runner was read.'''

HEZEKIAH = '''- **It can all be shown.** Hezekiah "welcomed them gladly. And he showed them his treasure house, the silver, the gold, the spices, the precious oil, his whole armory, all that was found in his storehouses. There was nothing in his house or in all his realm that Hezekiah did not show them" (Isaiah 39:2; 2 Kings 20:13). Isaiah asked, "What have they seen in your house?", and the answer was "They have seen all that is in my house" (Isaiah 39:4). The word that followed: "all that is in your house … shall be carried to Babylon" (39:6). Chronicles says of the same envoys that "God left him to himself, in order to test him and to know all that was in his heart" (2 Chronicles 32:31). Nothing was hidden, and it is the showing that the verses weigh.'''

JER44 = '''A refusal to hear can stand on a reading of the past. The survivors in Egypt told Jeremiah, "As for the word that you have spoken to us in the name of the Lord, we will not listen to you" (Jeremiah 44:16). Their reason was what they remembered: "For then we had plenty of food, and prospered, and saw no disaster. But since we left off making offerings to the queen of heaven and pouring out drink offerings to her, we have lacked everything" (44:17–18). They had seen the ruin (44:2; 10.13, *Seen and not taken in*) and read it the other way. I read the refusal as resting on their own account of cause and effect.'''

AMOS = '''- A people at ease can be made to reckon itself: "Pass over to Calneh, and see … Are you better than these kingdoms? Or is their territory greater than your territory" (Amos 6:2), said to those "at ease in Zion" (6:1) who "put far away the day of disaster" (6:3).'''

BAKER = '''What is heard can also set another speaking. "When the chief baker saw that the interpretation was favorable, he said to Joseph, 'I also had a dream'" (Genesis 40:16). He spoke on the strength of the other man's outcome. His own was death (40:19).'''

SHIMEI = '''An oath can begin as plain assent. Shimei, told to stay in Jerusalem on pain of death, answered the king, "What you say is good; as my lord the king has said, so will your servant do" (1 Kings 2:38). Three years later he went after his runaway servants, and Solomon called his word an oath: "Why then have you not kept your oath to the Lord and the commandment with which I commanded you?" (2:43). The agreement given to the king was counted as sworn to the Lord.'''

OPS = {
'10-07-': [
 ('after_line', "- **Another's will, given the whole decision.**", WHOSE),
 ('after_line', 'The same passage opens on what they appear to be doing', MAL_PEOPLE),
],
'13-01-': [
 ('after_line', "**His delight in people's mouths.**", MAL_GOD),
],
'10-06-': [
 ('after_line', 'Coveting runs in the order the woman', DAVID),
 ('after_line', 'Wanting speaks in the heart, and it drives thinking.', RUNNER),
],
'10-11-': [
 ('after_line', '- **It can be not hidden at all.**', HEZEKIAH),
],
'10-02-': [
 ('after_line', '**Hearing is the main way in.**', JER44),
],
'10-04-': [
 ('after_line', '- People reckon by the surface:', AMOS),
],
'10-05-': [
 ('after_line', "By people: Esau's private sentence", BAKER),
 ('after_line', 'The oath Scripture records most often', SHIMEI),
],
'11-patterns': [
 ('replace', '"Absalom stole the hearts of the men of Israel" (2 Samuel 15:6).',
  'Absalom told each man who came with a case, "See, your claims are good and right, but there is no man designated by the king to hear you" (2 Samuel 15:3), and so "Absalom stole the hearts of the men of Israel" (15:6).'),
],
}


def apply(text, mode, anchor, ins):
    lines = text.split(NL)
    if mode == 'replace':
        assert text.count(anchor) == 1, ('replace count', anchor[:60], text.count(anchor))
        return text.replace(anchor, ins)
    idx = [i for i, l in enumerate(lines) if l.startswith(anchor) or (not anchor.startswith('- ') and anchor in l and l.startswith(anchor[:20]))]
    assert len(idx) == 1, (mode, anchor[:60], idx)
    i = idx[0]
    if mode == 'after_line':
        if lines[i].startswith('- ') and ins.startswith('- '):
            lines[i + 1:i + 1] = [ins]
        else:
            lines[i + 1:i + 1] = ['', ins]
    elif mode == 'before_line':
        lines[i:i] = [ins.rstrip(NL), '']
    return NL.join(lines)


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
        for line in ins.split(NL):
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
                text = norm(verse_text(book, ch, range(min(vs) - 2, max(vs) + 3)))
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
    text = re.sub(NL + '{3,}', NL + NL, text)
    m = re.match(r'(.*-v)(\d+)-(\d{8})\.md$', os.path.basename(src))
    new = os.path.join(NARR, f'{m.group(1)}{int(m.group(2)) + 1}-{DATE}.md')
    print(os.path.basename(src), '->', os.path.basename(new))
    if dry or fails: continue
    shutil.copy2(src, os.path.join(NARR, 'archive', os.path.basename(src)))
    open(new, 'w', encoding='utf-8').write(text)
    os.remove(src)
if fails and not dry: sys.exit('not applied: fix failures first')
