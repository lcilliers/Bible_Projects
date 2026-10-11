"""Tests for verse-narrative-ot-crossref-v3 against the archived v2 (#1994, 2026-10-09). Read-only.

1. Synthetic cases for the v3 carry rule and each of its guards.
2. Whole narrative: no place v2 finds is lost by v3; every new 'book carried across text' is listed,
   and where a quotation stands right before the bare citation, its words are checked against the
   ESV text of the carried verse in iba.db `verse` (read-only). The rest are listed for reading.
3. Optional: a verse-list CSV run through both versions and diffed (places lost / gained).

Usage: python verse-narrative-ot-crossref-v3-test-v1-20261009.py [IN.csv]
Exit code = number of failed synthetic cases + places lost.
"""
import csv, importlib.util, os, re, sqlite3, sys, tempfile, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
IBA = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
IBA_MAIN = r'C:\Bible_study_projects\iba\app\db\iba.db'  # a git worktree has no iba.db of its own


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


v2 = load('v2', os.path.join(HERE, 'archive', 'verse-narrative-ot-crossref-v2-20261006.py'))
v3 = load('v3', os.path.join(HERE, 'verse-narrative-ot-crossref-v3-20261009.py'))
# v2 now sits one folder deeper in archive/, so its own relative paths miss; give it v3's.
v2.NARR, v2.OTR, v2.PAIRS = v3.NARR, v3.OTR, v3.PAIRS

CASES = [
    ('quote between', 'He asks "what is the gain" (Ecclesiastes 6:9). He finds envy: "all toil ... wind" (4:4).', {('Ecc', 6, 9), ('Ecc', 4, 4)}),
    ('range after quote', '"enjoy" (Ecclesiastes 2:24–25). "joy" (2:26).', {('Ecc', 2, 24), ('Ecc', 2, 25), ('Ecc', 2, 26)}),
    ('chain of bare', '"x" (1 Samuel 16:14). lyre (16:16), and "refreshed" (16:23).', {('1Sa', 16, 14), ('1Sa', 16, 16), ('1Sa', 16, 23)}),
    ('other book resets', '"a" (Ecclesiastes 6:9). "b" (Psalm 4:4). "c" (4:8).', {('Ecc', 6, 9), ('Psa', 4, 4), ('Psa', 4, 8)}),
    ('no book in line', 'He said "x" (4:4).', set()),
    ('not in own brackets', '"a" (Ecclesiastes 6:9). See also 4:4 and the rest (as at 4:6).', {('Ecc', 6, 9)}),
    ('bracket with text after', '"a" (Ecclesiastes 6:9). "b" (4:4, ESV).', {('Ecc', 6, 9)}),
    ('table cell boundary', 'Ecc 6:9 | "b" (4:4)', {('Ecc', 6, 9)}),
    ('v2 short gap kept', '(Joshua 24:15; 24:21)', {('Jos', 24, 15), ('Jos', 24, 21)}),
    ('prose names other book', '"x" (Romans 12:1). Ephesians speaks of being "renewed" (4:23).', {('Rom', 12, 1)}),
    ('prose names book, chapter only', '"x" (Numbers 16:10). Psalm 106 calls it jealousy (106:16).', {('Num', 16, 10)}),
    ('prose names same book', '"x" (Ecclesiastes 6:9). Ecclesiastes adds "envy" (4:4).', {('Ecc', 6, 9), ('Ecc', 4, 4)}),
    ('lowercase word not a book', '"x" (Psalm 90:12). In numbers and acts he is "wise" (90:14).', {('Psa', 90, 12), ('Psa', 90, 14)}),
    ('unbracketed source', 'He goes back to Genesis 2:7. "the last Adam" (15:45).', {('Gen', 2, 7)}),
    ('parallel beside uncarried bare', '"changed" (15:51). "swallowed" (15:54; Isaiah 25:8). "sting" (15:55).', {('Isa', 25, 8)}),
    ('parallel source, later bare', '"a" (15:54; Isaiah 25:8). Later "b" (26:3).', {('Isa', 25, 8)}),
    ('chapter not in book', '"angry" (Ecclesiastes 7:9). "ponders" (15:28).', {('Ecc', 7, 9)}),
    ('uncarried at start, then named book', '"x" (119:88). "Give us life" (Psalm 80:18). "my comfort" (119:50).', {('Psa', 80, 18), ('Psa', 119, 50)}),
    ('bare-only bracket carried', '"x" (Isaiah 66:3). not met (65:12; 66:4) or met (56:4).', {('Isa', 66, 3), ('Isa', 65, 12), ('Isa', 66, 4), ('Isa', 56, 4)}),
    ('bracket, comma verses', '"a" (Ecclesiastes 6:9). "b" (4:4, 6).', {('Ecc', 6, 9), ('Ecc', 4, 4), ('Ecc', 4, 6)}),
]


def synthetic():
    bad = 0
    for name, text, want in CASES:
        got = {(b, c, v) for b, c, v, _ in v3.cites(text)}
        bad += got != want
        print(('PASS' if got == want else 'FAIL'), name, '' if got == want else f'| want {sorted(want)} got {sorted(got)}')
    # a paragraph is one line: nothing carries from one line to the next
    two = [list(v3.cites(t)) for t in ('"a" (Ecclesiastes 6:9).', '"b" (4:4).')]
    ok = two[1] == []
    bad += not ok
    print(('PASS' if ok else 'FAIL'), 'no carry to the next line')
    ch = v3.CHAPTERS
    ok = len(ch) == 66 and sum(ch.values()) == 1189 and ch['Psa'] == 150 and ch['Mal'] == 4 and ch['Jude'] == 1
    bad += not ok
    print(('PASS' if ok else 'FAIL'), 'chapter table (66 books, 1189 chapters)')
    return bad


def norm(s):
    s = unicodedata.normalize('NFKD', s).lower().replace('\u2019', '')
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', s)).strip()


QUOTE = re.compile(r'["\u201c]\*?([^"\u201c\u201d*]{4,}?)\*?["\u201d]\*?[\])]?\s*\(\s*$')


def narrative():
    i2, i3 = v2.narrative_index(), v3.narrative_index()
    lost = [(k, p) for k in i2 for p in i2[k] if p not in i3.get(k, [])]
    print(f'\nNarrative places: v2 {sum(map(len, i2.values()))}, v3 {sum(map(len, i3.values()))}, lost {len(lost)}')
    for k, p in lost:
        print('  LOST', k, p)
    db_path = IBA if os.path.exists(IBA) else IBA_MAIN
    db = sqlite3.connect(f'file:{db_path}?mode=ro', uri=True)
    vt = lambda b, c, v: (db.execute('select text from verse where reference=? and deleted=0', (f'{b} {c}:{v}',)).fetchone() or [''])[0]
    n = ok = 0
    to_read = []
    for f in v3.current_chapters():
        for line in open(f, encoding='utf-8'):
            s = line.strip()
            for m, book, how in v3.tokens(s):
                if how != 'book carried across text':
                    continue
                n += 1
                verses, _ = v3.expand(*m.group(2, 3, 4, 5, 6))
                text = ' '.join(vt(book, c, v) for c, v in sorted(verses) if len(verses) < 40)
                q = QUOTE.search(s, 0, m.start())
                frags = [norm(x) for x in re.split(r'\u2026|\.\.\.|\[[^\]]*\]', q.group(1))] if q else []
                frags = [x for x in frags if x]
                if q and text and all(x in norm(text) for x in frags):
                    ok += 1
                else:
                    to_read.append(f'{book} {m.group(0)} | {os.path.basename(f)} | {s[max(0, m.start() - 120):m.end() + 1]}')
    print(f'Carried across text: {n}; quotation before it matches the ESV verse: {ok}; to read: {len(to_read)}')
    for r in to_read:
        print('  READ', r)
    return len(lost)


def csv_diff(inp):
    tmp = tempfile.mkdtemp()
    out2, out3 = os.path.join(tmp, 'v2.csv'), os.path.join(tmp, 'v3.csv')
    v2.main(inp, out2)
    v3.main(inp, out3)
    a = {r['reference']: r for r in csv.DictReader(open(out2, encoding='utf-8-sig'))}
    b = {r['reference']: r for r in csv.DictReader(open(out3, encoding='utf-8-sig'))}
    lost = gained = 0
    found = []
    for k in a:
        for col in ('narrative_refs', 'ot_refs', 'ot_pairing'):
            pa, pb = set(filter(None, a[k][col].split(' | '))), set(filter(None, b[k][col].split(' | ')))
            for p in sorted(pa - pb):
                print('  LOST', k, col, p)
            for p in sorted(pb - pa):
                print('  GAIN', k, col, p)
            lost += len(pa - pb)
            gained += len(pb - pa)
        if a[k]['narrative_n'] == '0' and b[k]['narrative_n'] != '0':
            found.append(k)
    print(f'CSV {os.path.basename(inp)}: {len(a)} rows, places lost {lost}, gained {gained}; not cited in v2, cited in v3: {len(found)}')
    print('  ' + '; '.join(found))
    return lost


if __name__ == '__main__':
    fails = synthetic() + narrative()
    if len(sys.argv) > 1:
        fails += csv_diff(sys.argv[1])
    sys.exit(fails)
