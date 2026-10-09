"""Weave of M18 group E (thirst, hunger) into the narrative (#1993, item F), 2026-10-09.

Reading: m18-group-E-reading-v1-20261009.md. Register: m18-group-E-register-v1-20261009.csv.
Same mechanics as m18-group-D-narrative-weave-v1-20261009.py, plus a quote check of every inserted quotation
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
 ('after_line', 'The thirst is answered with water:',
  '''At the feast the offer is made aloud, and the water now flows outward: *"Jesus stood up and cried out, 'If anyone thirsts, let him come to me and drink. Whoever believes in me, as the Scripture has said, Out of his heart will flow rivers of living water.'"* John adds, *"Now this he said about the Spirit, whom those who believed in him were to receive"* (John 7:37–39; Chapter 6). At the well the spring wells up *"in him"*. At the feast rivers flow *"out of his heart"*. I read a want that is met and then becomes a source for others.

The one who offered the water thirsted: *"After this, Jesus, knowing that all was now finished, said (to fulfill the Scripture), 'I thirst.'"* He was given sour wine, and then he said, *"It is finished"* (John 19:28–30). The psalm puts the thirst beside the want of comfort: *"I looked for pity, but there was none, and for comforters, but I found none. They gave me poison for food, and for my thirst they gave me sour wine to drink"* (Psalm 69:20–21). He says "I thirst" knowing what it fulfils. I read the want spoken, not hidden, and answered with sour wine.

The want can be aimed at righteousness, and then it is called blessed: *"Blessed are those who hunger and thirst for righteousness, for they shall be satisfied"* (Matthew 5:6). God's answer to plain thirst is given with its reason. *"When the poor and needy seek water, and there is none, and their tongue is parched with thirst, I the Lord will answer them; I the God of Israel will not forsake them"* (Isaiah 41:17). *"They shall not hunger or thirst, neither scorching wind nor sun shall strike them, for he who has pity on them will lead them, and by springs of water will guide them"* (Isaiah 49:10). The end is said in nearly the same words: *"They shall hunger no more, neither thirst anymore; the sun shall not strike them, nor any scorching heat. For the Lamb in the midst of the throne will be their shepherd, and he will guide them to springs of living water, and God will wipe away every tear from their eyes"* (Revelation 7:16–17). The thirst and the tears are answered together.

A thirst met can be forgotten. *"You gave them bread from heaven for their hunger and brought water for them out of the rock for their thirst … But they and our fathers acted presumptuously and stiffened their neck"*; they *"were not mindful of the wonders that you performed among them"* (Nehemiah 9:15–17). Isaiah sets the same memory beside the wicked: *"They did not thirst when he led them through the deserts; he made water flow for them from the rock … There is no peace, says the Lord, for the wicked"* (Isaiah 48:21–22). I read a want met so fully that it was no longer felt, and the giver forgotten with it (10.3).

Thirst also comes as judgment, and the verses name the inner ground each time. Joyless service in plenty: *"Because you did not serve the Lord your God with joyfulness and gladness of heart, because of the abundance of all things, therefore you shall serve your enemies whom the Lord will send against you, in hunger and thirst"* (Deuteronomy 28:47–48). A choice of what he did not delight in: *"you did what was evil in my eyes and chose what I did not delight in"* (Isaiah 65:12), so *"my servants shall drink, but you shall be thirsty … my servants shall sing for gladness of heart, but you shall cry out for pain of heart and shall wail for breaking of spirit"* (65:13–14). The outward thirst is matched by pain of heart and a broken spirit. Drink without regard: those who *"run after strong drink"* (5:11) and *"do not regard the deeds of the Lord"* (5:12) end *"parched with thirst"*, and the lack named is knowledge: *"my people go into exile for lack of knowledge"* (Isaiah 5:13). The drinkers end thirsty.

Hunger and thirst can be borne for others. *"To the present hour we hunger and thirst, we are poorly dressed and buffeted and homeless, and we labor, working with our own hands. When reviled, we bless; when persecuted, we endure"* (1 Corinthians 4:11–12). Paul's longer list ends *"in hunger and thirst, often without food, in cold and exposure. And, apart from other things, there is the daily pressure on me of my anxiety for all the churches"* (2 Corinthians 11:27–28). The bodily wants are listed and passed over. The weight he names last is inside, and it is for others.

A bodily want can be the setting of a vision. Peter *"became hungry and wanted something to eat, but while they were preparing it, he fell into a trance"* (Acts 10:10), and saw a sheet let down full of animals (10:11–12). The verses do not say why it came then.'''),
],
'10-10-': [
 ('before_line', 'Love between two people has its own time in the Song',
  '''Another's thirst can be met, refused or used. The King names it as his own: *"I was thirsty and you gave me drink"*, and the righteous ask, *"Lord, when did we see you hungry and feed you, or thirsty and give you drink?"* (Matthew 25:35, 37). The others ask the same: *"Lord, when did we see you hungry or thirsty or a stranger or naked or sick or in prison, and did not minister to you?"* (Matthew 25:44). The answer is *"as you did it to one of the least of these my brothers, you did it to me"* (Matthew 25:40). Neither side knew whom they met. I read that what was done or not done to the thirsty was done to him, whether they knew it or not.

Boaz meets a stranger's thirst: *"when you are thirsty, go to the vessels and drink what the young men have drawn."* Ruth answers, *"Why have I found favor in your eyes, that you should take notice of me, since I am a foreigner?"* (Ruth 2:9–10). Jael meets Sisera's: *"Please give me a little water to drink, for I am thirsty. So she opened a skin of milk and gave him a drink and covered him"* (Judges 4:19), and then she took the tent peg (4:21; 10.5). The same act, given drink and covered, is care in one tent and a trap in the other.

Thirst can be left unmet by those who should meet it. In the siege, *"Even jackals offer the breast; they nurse their young; but the daughter of my people has become cruel … The tongue of the nursing infant sticks to the roof of its mouth for thirst; the children beg for food, but no one gives to them"* (Lamentations 4:3–4). The animals are set above the people. And the worker thirsts among what he makes for another: *"they tread the winepresses, but suffer thirst … yet God charges no one with wrong"* (Job 24:11–12; 10.9).
'''),
],
'10-02-': [
 ('after_line', 'What a person listens to shows what he is:',
  'Hearing can be taken away, and then wanted. *"Behold, the days are coming, declares the Lord God, when I will send a famine on the land—not a famine of bread, nor a thirst for water, but of hearing the words of the Lord. They shall wander from sea to sea … to seek the word of the Lord, but they shall not find it. In that day the lovely virgins and the young men shall faint for thirst"* (Amos 8:11–13). The famine is not of the word but of hearing it. The bodily thirst comes in the same day.'),
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
