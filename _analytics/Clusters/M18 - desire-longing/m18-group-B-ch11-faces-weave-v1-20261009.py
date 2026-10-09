"""Weave of M18 group B: the three Ch 11 §4 faces proposed in sets 1 and 2 (#1993, item F), 2026-10-09.

Readings: m18-group-B1-delight-reading-v1-20261009.md §12, m18-group-B2-pleasant-reading-v1-20261009.md §6. Researcher: "proceed with Ch 11".
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


OPS = {
'11-': [
 ('after_line', '- **Delight.** The Hebrew *ḥāpēṣ*',
  '- **God\'s delight in a person.** It is the thanks of the rescued: "he rescued me, because he delighted in me" (Psalm 18:19). It is the mockers\' taunt over a sufferer: "let him rescue him, for he delights in him!" (Psalm 22:8). The claim is the same. The sufferer does not answer the mockers; he answers God: "Yet you are he who took me from the womb" (22:9) (13.1).\n'
  '- **An offering.** "For you will not delight in sacrifice, or I would give it" (Psalm 51:16). Three verses on: "then will you delight in right sacrifices, in burnt offerings and whole burnt offerings" (51:19). It is the same offering. Between the two stands "a broken and contrite heart, O God, you will not despise" (51:17) (13.1).\n'
  '- **Being well pleased.** The Greek *eudokeō* is the Father\'s word over the Son: "This is my beloved Son, with whom I am well pleased" (Matthew 3:17). It is also Paul\'s word for weaknesses he had pleaded three times to lose: "I am content with weaknesses, insults, hardships, persecutions, and calamities" (2 Corinthians 12:10). Between his pleading and his contentment stands the answer, "My grace is sufficient for you" (12:9) (10.1).'),
 ('after_line', '- **Who speaks it, and to what end.**',
  '- **Whose mouth it is in.** That God delights in a man is thanks from the one rescued and a taunt from those who watch him suffer (Psalm 18:19; 22:8, §4 above).'),
 ('after_line', '- **The answer it meets.**',
  '- **What the one who brings it brings first.** The same offering is refused and then delighted in, and what comes between is a broken heart (Psalm 51:16–19, §4 above). The same weakness is pleaded against and then pleases, and what comes between is God\'s answer (2 Corinthians 12:8–10).'),
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
