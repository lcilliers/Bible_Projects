"""Check the quotations a chapter edit added against the ESV text in iba.db (read-only).

Usage: python narrative-quote-check-v1-20261014.py NEW.md [OLD.md]
Checks every quotation in the lines of NEW that are not in OLD (all of NEW when OLD is omitted).
Same matching as ../M02 - anger-wrath/m02-pairing-gaps-weave-v1-20261013.py check(): each part between
ellipses, split at clause punctuation, must be found (normalised) inside one ESV verse.
"""
import re, sqlite3, sys

new = open(sys.argv[1], encoding='utf-8').read().split('\n')
old = set(open(sys.argv[2], encoding='utf-8').read().split('\n')) if len(sys.argv) > 2 else set()
text = '\n'.join(l for l in new if l not in old)

con = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
norm = lambda t: re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', t.lower())).strip()
VERSES = [norm(t or '') for (t,) in con.execute('select text from verse where deleted=0')]

bad, n = [], 0
for q in re.findall(r'(?:^|(?<=[\s(*—]))"([^"\n]+?)"(?=[*\s).,;:!?]|$)', text, flags=re.M):
    for part in q.split('…'):
        if len(norm(part).split()) < 3:
            continue
        n += 1
        chunks = [norm(c) for c in re.split(r'[.;?!,]\s', part) if len(norm(c).split()) >= 3]
        if not all(any(c in v for v in VERSES) for c in chunks):
            bad.append(part)
print(f'quote parts checked: {n}; failing: {len(bad)}')
for x in bad:
    print('  !', x[:170])
