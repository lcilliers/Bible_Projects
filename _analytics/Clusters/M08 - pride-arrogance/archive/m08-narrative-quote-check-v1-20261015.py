"""M08 weave quote check (#2156): every double-quoted part in the given narrative lines (or files) must
occur in the ESV text of iba.db `verse`, joined in canonical order (cfg_book_order, chapter, verse),
punctuation and case normalised. Parts are split on the ellipsis (… or ...). Read-only.

Usage: python m08-narrative-quote-check-v1-20261015.py <file.md> [...]
       python m08-narrative-quote-check-v1-20261015.py --added <old.md> <new.md>   (only lines added in new)
"""
import difflib, os, re, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
c = sqlite3.connect(f'file:{os.path.join(HERE, "..", "..", "..", "iba", "app", "db", "iba.db")}?mode=ro', uri=True)
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r"[“”‘’\"'—–,;:.!?()\[\]*_-]", ' ', s)).strip().lower()
order = {b: o for b, o in c.execute('SELECT book, ordinal FROM cfg_book_order')}
rows = []
for o, t in c.execute('SELECT osisId, text FROM verse WHERE deleted = 0'):
    b, ch, v = o.rsplit('.', 2)
    rows.append((order.get(b, 999), int(ch), int(v), norm(t or '')))
corpus = ' '.join(r[3] for r in sorted(rows))

def check(lines, label):
    parts = bad = 0
    for line in lines:
        for q in re.findall(r'"([^"]{3,}?)"', line):
            for p in re.split(r'\s*(?:…|\.\.\.)\s*', q):
                p = re.sub(r'\[[^\]]*\]', ' ', p)
                if len(norm(p).split()) < 2: continue
                parts += 1
                if norm(p) not in corpus:
                    bad += 1; print('  FAIL:', p[:160])
    print(label, 'quote parts', parts, 'failures', bad)
    return bad

args = sys.argv[1:]
if args and args[0] == '--added':
    old = open(args[1], encoding='utf-8').read().splitlines()
    new = open(args[2], encoding='utf-8').read().splitlines()
    added = [l[1:] for l in difflib.unified_diff(old, new, lineterm='', n=0) if l.startswith('+') and not l.startswith('+++')]
    sys.exit(1 if check(added, os.path.basename(args[2]) + ' (added lines)') else 0)
for f in args:
    check(open(f, encoding='utf-8').read().splitlines(), os.path.basename(f))
