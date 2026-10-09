"""Weave of M18 group B, set 2 (the pleasant/pleased verbs) into the narrative (#1993, item F), 2026-10-09.

Reading: m18-group-B2-pleasant-reading-v1-20261009.md. Register: m18-group-B2-register-v1-20261009.csv.
Placement as ruled for set 1 (researcher, verbatim): "delight associated with God goes to 13.1, separate section; HIB
delight goes into 10.1". Same mechanics and quote check as m18-group-B1-narrative-weave-v1-20261009.py.
Run with --dry to check only; without it, it writes only if the check passes.
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


PLEASANT = '''### What is found pleasant

Another word, "be pleasant", says what a person finds pleasant, and it is said of very different things.
- **A land, at a price.** "Issachar is a strong donkey, crouching between the sheepfolds. He saw that a resting place was good, and that the land was pleasant, so he bowed his shoulder to bear, and became a servant at forced labor" (Genesis 49:14–15). The figure is a strong animal lying down. He sees the rest and the land as pleasant, and for them he takes the load. I read that strength settles for comfort, and the comfort costs it its freedom.
- **A loved one.** "How beautiful and pleasant you are, O loved one, with all your delights!" (Song of Solomon 7:6), after "a king is held captive in the tresses" (7:5). The one who delights is held by what he delights in, and the song says it as praise.
- **A friend, in grief.** "I am distressed for you, my brother Jonathan; very pleasant have you been to me; your love to me was extraordinary, surpassing the love of women" (2 Samuel 1:26). The pleasantness is spoken only at the loss, inside the lament "How the mighty have fallen" (1:25, 27; 10.10).
- **What is stolen.** Folly calls to the simple: "Stolen water is sweet, and bread eaten in secret is pleasant." "But he does not know that the dead are there, that her guests are in the depths of Sheol" (Proverbs 9:17–18). Water and bread are ordinary. What makes them sweet in her call is that they are stolen and hidden. The guest knows the pleasure and does not know where he is.
- **Food refused, a blow taken, words offered.** "let me not eat of their delicacies! Let a righteous man strike me—it is a kindness; let him rebuke me—it is oil for my head; let my head not refuse it" (Psalm 141:4–5). Then, "they shall hear my words, for they are pleasant" (141:6). He turns from what is pleasant to eat among evildoers, and calls a righteous man's blow a kindness. I read that what is pleasant to him has been turned around: the rebuke is oil, the delicacy is refused (10.5).
- **The reward of a rebuke.** "Whoever says to the wicked, 'You are in the right,' will be cursed by peoples, abhorred by nations, but those who rebuke the wicked will have delight, and a good blessing will come upon them" (Proverbs 24:24–25). Delight comes to the one who says the hard word, not the soft one (Chapter 11).
- **Content with what he asked to lose.** "Three times I pleaded with the Lord about this, that it should leave me. But he said to me, 'My grace is sufficient for you, for my power is made perfect in weakness'" (2 Corinthians 12:8–9). Then: "For the sake of Christ, then, I am content with weaknesses, insults, hardships, persecutions, and calamities. For when I am weak, then I am strong" (12:10). The word for "content" is the word for being well pleased. He is pleased with what he pleaded to be rid of, after the answer, and "for the sake of Christ".
'''

MOUNTAIN = '''**The voice again, on the mountain.** Peter was saying, "Lord, it is good that we are here. If you wish, I will make three tents here", when "a voice from the cloud said, 'This is my beloved Son, with whom I am well pleased; listen to him'" (Matthew 17:4–5). The words of the baptism come back with a command added. "When the disciples heard this, they fell on their faces and were terrified. But Jesus came and touched them, saying, 'Rise, and have no fear'" (17:6–7). The Father's pleasure, spoken to them, frightens them, and the Son lifts them. Peter recalls it years later as the ground of what he preaches: "we did not follow cleverly devised myths … we ourselves heard this very voice borne from heaven, for we were with him on the holy mountain" (2 Peter 1:16–18), and the word is to be heeded "until the day dawns and the morning star rises in your hearts" (1:19).

**His good pleasure gives.** "Fear not, little flock, for it is your Father's good pleasure to give you the kingdom" (Luke 12:32), after "your Father knows that you need them" (12:30; 10.12). What pleases him is to give. "For since, in the wisdom of God, the world did not know God through wisdom, it pleased God through the folly of what we preach to save those who believe" (1 Corinthians 1:21). His pleasure chooses the way the world calls folly. "For in him all the fullness of God was pleased to dwell, and through him to reconcile to himself all things" (Colossians 1:19–20), and the next words are "And you, who once were alienated and hostile in mind, doing evil deeds" (1:21). His pleasure reaches those who were hostile to him.
'''

NOT_PLEASED = '''Not pleased, though they shared it all: "and all ate the same spiritual food, and all drank the same spiritual drink. For they drank from the spiritual Rock that followed them, and the Rock was Christ. Nevertheless, with most of them God was not pleased, for they were overthrown in the wilderness" (1 Corinthians 10:3–5). The next verse says why the account is given: "that we might not desire evil as they did" (10:6; 10.6). Sharing in what he gave did not make them pleasing to him.
'''

HEBREWS = '''Hebrews reads Psalm 40 as the words of Christ: "Sacrifices and offerings you have not desired, but a body have you prepared for me; in burnt offerings and sin offerings you have taken no pleasure. Then I said, 'Behold, I have come to do your will, O God'" (Hebrews 10:5–7). It draws the end: "And by that will we have been sanctified through the offering of the body of Jesus Christ once for all" (10:10). What he had no pleasure in is set aside for a will done in a body.
'''

OPS = {
'10-01-': [
 ('before_line', "### A child's delight", PLEASANT),
 ('after_line', "- **A ruler's pleasure.**",
  '- **Willing, because it could not be borne.** "Therefore when we could bear it no longer, we were willing to be left behind at Athens alone, and we sent Timothy" (1 Thessalonians 3:1–2), "that no one be moved by these afflictions" (3:3). Paul chose to be alone rather than not know how they stood. The longing that follows is in 10.6 (3:6–7).'),
],
'13-01-': [
 ('before_line', '**Whom he delights in, and why.**', MOUNTAIN),
 ('before_line', '**Not the offering itself.**', NOT_PLEASED),
 ('before_line', '**He does what pleases him.**', HEBREWS),
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
