"""M08 quote check (#2156): every *"..."* quote in a reading .md, split on ' ... ', must occur in
the ESV text of iba.db `verse` joined in id order (punctuation-normalised); quotes right after
"verbatim" (the researcher's words) are skipped. Read-only. Prints failures.

Usage: python m08-quote-check-v1-20261015.py <reading.md> [...]
"""
import os, re, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db')
c = sqlite3.connect(f'file:{os.path.abspath(DB)}?mode=ro', uri=True)
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'[“”‘’"\'—–,;:.!?()\[\]-]', ' ', s)).strip().lower()
# verse.id is not canonical; order by book (cfg_book_order), chapter, verse so quotes across verses match
order = {b: o for b, o in c.execute('SELECT book, ordinal FROM cfg_book_order')}
rows = []
for o, t in c.execute('SELECT osisId, text FROM verse WHERE deleted = 0'):
    b, ch, v = o.rsplit('.', 2)
    rows.append((order.get(b, 999), int(ch), int(v), norm(t or '')))
corpus = ' '.join(r[3] for r in sorted(rows))
for path in sys.argv[1:]:
    md = open(path, encoding='utf-8').read()
    # researcher quotes (right after 'verbatim') are not ESV and are skipped
    quotes = [m.group(1) for m in re.finditer(r'\*"([^*]+?)"\*', md) if 'verbatim' not in md[max(0, m.start() - 40):m.start()]]
    bad = []; parts = 0
    for q in quotes:
        for p in re.split(r'\s*\.\.\.\s*', q):
            p = re.sub(r'\[[^\]]*\]', ' ', p)
            if len(norm(p)) < 3: continue
            parts += 1
            if norm(p) not in corpus: bad.append(p)
    print(os.path.basename(path), 'quotes', len(quotes), 'parts', parts, 'failures', len(bad))
    for b in bad: print('  FAIL:', b)
