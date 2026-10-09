"""Weave of M18 group G (gloss away from desire) into the narrative (#1993, item F), 2026-10-09.

Reading: m18-group-G-reading-v1-20261009.md. Register: m18-group-G-register-v1-20261009.csv.
Same mechanics as m18-group-F-narrative-weave-v1-20261009.py, with the quote check of every inserted quotation
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
'14-': [
 ('before_line', '## Kept whole',
  '''## Brought near

Paul describes the state before in terms of distance and of hope: *"remember that you were at that time separated from Christ, alienated from the commonwealth of Israel and strangers to the covenants of promise, having no hope and without God in the world. But now in Christ Jesus you who once were far off have been brought near by the blood of Christ"* (Ephesians 2:12–13). Being far off is named as having no hope. The nearness is not reached by the one who was far. It is made: *"have been brought near"*.

The same passage ends a hostility between people: *"For he himself is our peace, who has made us both one and has broken down in his flesh the dividing wall of hostility"* (2:14), *"thereby killing the hostility. And he came and preached peace to you who were far off and peace to those who were near. For through him we both have access in one Spirit to the Father"* (2:16–18). Those who were far and those who were near receive the same peace. I read two distances closed together: from God, and between the two peoples, with the hostility itself put to death.
'''),
],
'10-09-': [
 ('after_line', '- **And he thinks of me.**',
  '- **Sought, and not far.** Paul tells the Athenians that God set the times and places of the nations *"that they should seek God, and perhaps feel their way toward him and find him. Yet he is actually not far from each one of us"* (Acts 17:27). The seeking is a groping in the dark; the one sought is close by. The next verse is *"In him we live and move and have our being"* (17:28; Chapter 2).\n'
  '- **Recognised, and gone to.** At the lake, *"That disciple whom Jesus loved therefore said to Peter, \'It is the Lord!\' When Simon Peter heard that it was the Lord, he put on his outer garment, for he was stripped for work, and threw himself into the sea. The other disciples came in the boat, dragging the net full of fish, for they were not far from the land"* (John 21:7–8). One sees and says it; one hears and leaps; the others come in with the catch. I read the same recognition met in three ways, none of them rebuked.'),
],
'10-10-': [
 ('after_line', 'How a person rates himself, or another, can be put in the words',
  'A son rates himself, and a father will not hear it out. The younger son prepares his words: *"I am no longer worthy to be called your son. Treat me as one of your hired servants"* (Luke 15:19). *"But while he was still a long way off, his father saw him and felt compassion, and ran and embraced him and kissed him"* (15:20). The son begins the speech, *"Father, I have sinned against heaven and before you. I am no longer worthy to be called your son"* (15:21), and the father speaks over it: *"Bring quickly the best robe, and put it on him"* (15:22). The line about the hired servant is never said. The father saw him first, from far off, and the compassion came before any word. I read that the son\'s own rating of himself is set aside, not argued with.'),
],
'10-04-': [
 ('after_line', '- Being reckoned trustworthy carries a charge.',
  '- A man can be reckoned worthy by others and reckon himself not. The elders said of the centurion, "He is worthy to have you do this for him, for he loves our nation" (Luke 7:4–5). He sent word, "Lord, do not trouble yourself, for I am not worthy to have you come under my roof. Therefore I did not presume to come to you. But say the word, and let my servant be healed" (7:6–7). Jesus "marveled at him" (7:9).'),
],
'10-06-': [
 ('after_line', 'A longing for home can stand beside fear.',
  'A wish can be for others to have what one has. Agrippa says, *"In a short time would you persuade me to be a Christian?"* Paul answers, *"Whether short or long, I would to God that not only you but also all who hear me this day might become such as I am—except for these chains"* (Acts 26:28–29). He wishes his hearers everything he has except the chains he stands in.'),
],
'10-02-': [
 ('after_line', 'Before Samuel, *"the word of the Lord was rare',
  'Hearing can stop at a single word. Paul tells the crowd of his vision in the temple: *"Make haste and get out of Jerusalem quickly, because they will not accept your testimony about me"* (Acts 22:18). He objected that they knew his past: *"Lord, they themselves know that in one synagogue after another I imprisoned and beat those who believed in you"* (22:19). The answer was *"Go, for I will send you far away to the Gentiles"* (22:21). Then *"Up to this word they listened to him. Then they raised their voices and said, \'Away with such a fellow from the earth! For he should not be allowed to live\'"* (22:22). They heard him through the persecution and the vision; the word "Gentiles" ended their hearing. Paul had thought his past would make them listen; the Lord had said it would not.\n\n'
  'Words that are heard can be pictured as tools. The Preacher *"sought to find words of delight, and uprightly he wrote words of truth"* (Ecclesiastes 12:10). *"The words of the wise are like goads, and like nails firmly fixed are the collected sayings; they are given by one Shepherd. My son, beware of anything beyond these"* (12:11–12). A goad drives an animal on; a nail holds something in place. I read the figure as two works of the same words on the hearer: they move him, and they fix in him. Delight is in the search for the words, and the words are given by one Shepherd.'),
],
'10-05-': [
 ('after_line', 'Speech can cover the heart instead of showing it.',
  'Prayer can be used as cover. *"Beware of the scribes, who like to walk around in long robes and like greetings in the marketplaces"*, *"who devour widows\' houses and for a pretense make long prayers. They will receive the greater condemnation"* (Mark 12:38, 40). The next scene is a widow: *"this poor widow has put in more than all those who are contributing to the offering box. For they all contributed out of their abundance, but she out of her poverty has put in everything she had, all she had to live on"* (12:43–44). The long prayer covers the taking of widows\' houses. The widow says nothing in the passage, and gives everything.'),
],
'10-11-': [
 ('after_line', 'There is a false shelter too:',
  'What was seen can be covered with money and a story. The guards *"told the chief priests all that had taken place"* (Matthew 28:11). The elders *"gave a sufficient sum of money to the soldiers and said, \'Tell people, His disciples came by night and stole him away while we were asleep. And if this comes to the governor\'s ears, we will satisfy him and keep you out of trouble\'"* (28:12–14). *"So they took the money and did as they were directed. And this story has been spread among the Jews to this day"* (28:15). The truth was told to them first; they paid to hide it, and promised safety to those who carried the lie.'),
],
'03-': [
 ('replace', 'and Jesus says he answered wisely (Mark 12:33–34)',
  'and Jesus, seeing that he answered wisely, says, "You are not far from the kingdom of God" (Mark 12:33–34)'),
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
