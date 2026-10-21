"""Cross-reference a verse list against the inner-being narrative and the open threads register.

#1978, 2026-10-06. Read-only. v2: adds the short forms 1Co, 2Co and Php, which v1 missed. Reusable for any verse-list CSV that has a `reference` column in
iba.db form (Gen 6:5, 1Cor 4:5, Phili 1:22).
v3 (#1994, 2026-10-09): a bare citation in its own brackets, such as "(4:4)", takes the book of the
last citation in the same paragraph (one line of a chapter file, or one cell of an open-threads
row), whatever text lies between, e.g. '... (Ecclesiastes 6:9). He finds envy: "all toil" (4:4).'
v2 carried only across short connective gaps, so these were reported as not cited (#1993).
Never carried across paragraphs or a table cell boundary '|'; a citation that names another book
makes that book the one carried. The carry is refused (the citation is left uncarried, as in v2)
when the text between names another book without chapter:verse ("Ephesians speaks of …"), when
the last citation was not in brackets ("He goes back to Genesis 2:7"), when it is a parallel in
brackets beside a bare citation that had no book ("(15:54; Isaiah 25:8)"), or when the book has no
such chapter. Each guard was set by a wrong carry found in the narrative; see tokens().

For each verse it adds:
  narrative_refs : every place the verse is cited in the current chapter files
                   (chapter · section · paragraph), "book carried" when the citation is bare
                   (e.g. "8:21" after "Gen 6:5"), "book carried across text" when a bare
                   "(ch:v)" follows other text, "in range" when inside a cited range
  narrative_n    : count of those places
  ot_refs        : open-threads rows that cite the verse in any column, with the row status
  ot_pairing     : open-threads M02 pairing rows (OT-16 to OT-90) whose verse list, in
                   wa-cluster-M02-mcode-face-combinations-v1-20261005.csv, holds the verse
                   (= the verse also has an anger word), with the row status

Chapter files: the highest version of each chapter in inner-being-narrative/ (archive and the
00-index status file are excluded).

Usage: python verse-narrative-ot-crossref-v3-20261009.py IN.csv OUT.csv
"""
import csv, glob, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ANALYTICS = os.path.normpath(os.path.join(ROOT, '..', '..'))
NARR = os.path.join(ANALYTICS, 'essay', 'spirit_soul_body', 'inner-being-narrative')
OTR = os.path.join(ANALYTICS, 'cross-cluster-web', 'open-threads-register.md')
PAIRS = os.path.join(ANALYTICS, 'Clusters', 'M02 - anger-wrath', 'wa-cluster-M02-mcode-face-combinations-v1-20261005.csv')

# iba.db book codes, with the full names and other short forms the narrative uses.
BOOKS = {
 'Gen': ['Genesis', 'Gen'], 'Exo': ['Exodus', 'Exo', 'Ex'], 'Lev': ['Leviticus', 'Lev'], 'Num': ['Numbers', 'Num'],
 'Deu': ['Deuteronomy', 'Deu', 'Deut'], 'Jos': ['Joshua', 'Jos', 'Josh'], 'Judg': ['Judges', 'Judg', 'Jdg'], 'Rut': ['Ruth', 'Rut'],
 '1Sa': ['1 Samuel', '1Sa', '1Sam', '1 Sam'], '2Sa': ['2 Samuel', '2Sa', '2Sam', '2 Sam'],
 '1Ki': ['1 Kings', '1Ki', '1Kgs', '1 Kgs'], '2Ki': ['2 Kings', '2Ki', '2Kgs', '2 Kgs'],
 '1Ch': ['1 Chronicles', '1Ch', '1Chr', '1 Chr'], '2Ch': ['2 Chronicles', '2Ch', '2Chr', '2 Chr'],
 'Ezr': ['Ezra', 'Ezr'], 'Neh': ['Nehemiah', 'Neh'], 'Est': ['Esther', 'Est'], 'Job': ['Job'],
 'Psa': ['Psalms', 'Psalm', 'Psa', 'Ps'], 'Pro': ['Proverbs', 'Pro', 'Prov'], 'Ecc': ['Ecclesiastes', 'Ecc', 'Eccl'],
 'Song': ['Song of Solomon', 'Song of Songs', 'Song'], 'Isa': ['Isaiah', 'Isa'], 'Jer': ['Jeremiah', 'Jer'],
 'Lam': ['Lamentations', 'Lam'], 'Eze': ['Ezekiel', 'Eze', 'Ezek'], 'Dan': ['Daniel', 'Dan'], 'Hos': ['Hosea', 'Hos'],
 'Joe': ['Joel', 'Joe'], 'Amo': ['Amos', 'Amo'], 'Obd': ['Obadiah', 'Obd', 'Obad'], 'Jon': ['Jonah', 'Jon'],
 'Mic': ['Micah', 'Mic'], 'Nah': ['Nahum', 'Nah'], 'Hab': ['Habakkuk', 'Hab'], 'Zep': ['Zephaniah', 'Zep', 'Zeph'],
 'Hag': ['Haggai', 'Hag'], 'Zec': ['Zechariah', 'Zec', 'Zech'], 'Mal': ['Malachi', 'Mal'],
 'Mat': ['Matthew', 'Mat', 'Matt'], 'Mar': ['Mark', 'Mar', 'Mrk'], 'Luk': ['Luke', 'Luk'], 'Joh': ['John', 'Joh'],
 'Act': ['Acts', 'Act'], 'Rom': ['Romans', 'Rom'], '1Cor': ['1 Corinthians', '1Cor', '1 Cor', '1Co'],
 '2Cor': ['2 Corinthians', '2Cor', '2 Cor', '2Co'], 'Gal': ['Galatians', 'Gal'], 'Eph': ['Ephesians', 'Eph'],
 'Phili': ['Philippians', 'Phili', 'Phil', 'Php'], 'Col': ['Colossians', 'Col'], '1Th': ['1 Thessalonians', '1Th', '1 Thess', '1Thess'],
 '2Th': ['2 Thessalonians', '2Th', '2 Thess', '2Thess'], '1Ti': ['1 Timothy', '1Ti', '1Tim', '1 Tim'],
 '2Ti': ['2 Timothy', '2Ti', '2Tim', '2 Tim'], 'Tit': ['Titus', 'Tit'], 'Phile': ['Philemon', 'Phile', 'Phlm'],
 'Heb': ['Hebrews', 'Heb'], 'Jam': ['James', 'Jam', 'Jas'], '1Pe': ['1 Peter', '1Pe', '1Pet', '1 Pet'],
 '2Pe': ['2 Peter', '2Pe', '2Pet', '2 Pet'], '1Jo': ['1 John', '1Jo', '1Jn', '1 Jn'], '2Jo': ['2 John', '2Jo'],
 '3Jo': ['3 John', '3Jo'], 'Jude': ['Jude'], 'Rev': ['Revelation', 'Rev'],
}
# v3: chapters per book (English versification), so a carry into a chapter the book lacks is refused.
CHAPTERS = dict(zip(BOOKS, [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8,
                            66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4,
                            28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]))
ALIAS = {}
for code, names in BOOKS.items():
    for n in names:
        ALIAS[n] = code
book_rx = '|'.join(sorted((re.escape(a) for a in ALIAS), key=len, reverse=True))
# A citation run: optional book, then chapter:verse with ranges, comma verses, ';'-separated chapters.
CV = r'(\d+):(\d+)[a-c]?(?:\s*[–-]\s*(?:(\d+):)?(\d+)[a-c]?)?((?:\s*,\s*\d+[a-c]?(?:\s*[–-]\s*\d+)?)*)'
TOKEN = re.compile(r'(?<![\w:])(?:(' + book_rx + r')\.?\s+)?' + CV)
CARRY_GAP = re.compile(r'^[\s;,()]*(?:and|with|beside|also|see|cf\.?)?[\s;,()]*$')
# v3: a bare citation opening its own brackets, "(4:4)", "( 2:24–25 )", "(65:12; 66:4)".
OPEN_BRACKET = re.compile(r'\(\s*$')
CLOSE_BRACKET = re.compile(r'\s*[);]')  # used with .match(text, pos), which anchors at pos
# v3: a book named in the text between, without chapter:verse ("Ephesians speaks of …", "Psalm 106
# calls it …"), stops the carry, so the bare citation is not given the wrong book. Full names only,
# case-sensitive, so "numbers" or "acts" in prose do not stop it.
NAMED = {names[0]: {code} for code, names in BOOKS.items()}
NAMED.update({'Psalm': {'Psa'}, 'Song of Songs': {'Song'}, 'Chronicles': {'1Ch', '2Ch'},
              'Corinthians': {'1Cor', '2Cor'}, 'Thessalonians': {'1Th', '2Th'}})
NAMED_BOOK = re.compile(r'(?<!\w)(' + '|'.join(sorted(map(re.escape, NAMED), key=len, reverse=True)) + r')(?!\w)')


def names_other_book(gap, book):
    """True when the text between names a book other than `book`."""
    return any(book not in NAMED[n] for n in NAMED_BOOK.findall(gap))


def expand(ch, v1, ch2, v2, extra):
    """Return the set of (chapter, verse) a citation covers, and the subset named singly."""
    ch, v1 = int(ch), int(v1)
    out = {(ch, v1)}
    single = {(ch, v1)}
    if v2:
        ch2 = int(ch2) if ch2 else ch
        v2 = int(v2)
        if ch2 == ch:
            out |= {(ch, v) for v in range(v1, v2 + 1)}
        else:
            out |= {(ch, v) for v in range(v1, v1 + 200)} | {(ch2, v) for v in range(1, v2 + 1)}
            out |= {(c, v) for c in range(ch + 1, ch2) for v in range(1, 200)}
    for part in re.findall(r'\d+[a-c]?(?:\s*[–-]\s*\d+)?', extra or ''):
        nums = [int(x) for x in re.findall(r'\d+', part)]
        if len(nums) == 2:
            out |= {(ch, v) for v in range(nums[0], nums[1] + 1)}
        else:
            out.add((ch, nums[0]))
            single.add((ch, nums[0]))
    return out, single


def open_bracket(text, pos):
    """Position of the '(' that `pos` lies inside on the line, or -1."""
    o = text.rfind('(', 0, pos)
    return o if o > text.rfind(')', 0, pos) else -1


def tokens(text):
    """Yield (match, book, how) for every citation in a line of text whose book is known.

    v3 rule 'book carried across text': a bare "(ch:v)" opening its own brackets takes the book of
    the last citation, whatever text lies between, unless
      - the text between holds a '|' (table cell) or names another book;
      - that citation was not itself in brackets (an in-prose "goes back to Genesis 2:7");
      - that citation is a parallel, sharing its brackets with a bare citation that had no book
        (in "(15:54; Isaiah 25:8)" ... "(15:55)", 15:55 belongs to the paragraph's own book,
        named in an earlier paragraph, not to Isaiah);
      - the chapter does not exist in that book (e.g. "(Ecclesiastes 7:9)" ... "(15:28)").
    """
    last_book, last_end, book_end, src_ok, orphan_brackets = None, None, None, False, set()
    for m in TOKEN.finditer(text):
        book = ALIAS.get(m.group(1)) if m.group(1) else None
        how = ''
        if not book:
            gap = text[last_end:m.start()] if last_end is not None else None
            alone = OPEN_BRACKET.search(text, 0, m.start()) and CLOSE_BRACKET.match(text, m.end())
            if last_book and gap is not None and CARRY_GAP.match(gap):
                book, how = last_book, 'book carried'
            elif (last_book and alone and src_ok
                  and '|' not in text[book_end:m.start()]
                  and not names_other_book(text[book_end:m.start()], last_book)
                  and max(int(m.group(2)), int(m.group(4) or 0)) <= CHAPTERS[last_book]):
                book, how = last_book, 'book carried across text'
            else:
                orphan_brackets.add(open_bracket(text, m.start()))
                last_end = m.end()
                continue
        yield m, book, how
        last_book, last_end, book_end = book, m.end(), m.end()
        o = open_bracket(text, m.start())
        src_ok = o >= 0 and o not in orphan_brackets


def cites(text):
    """Yield (book, chapter, verse, how) for every verse a line of text cites."""
    for m, book, how in tokens(text):
        verses, single = expand(*m.group(2, 3, 4, 5, 6))
        for ch, v in sorted(verses):
            note = how
            if (ch, v) not in single:
                note = (note + '; ' if note else '') + 'in range ' + m.group(0).strip()
            yield book, ch, v, note


def ref_key(ref):
    b, cv = ref.rsplit(' ', 1)
    c, v = cv.split(':')
    return b, int(c), int(v)


def current_chapters():
    best = {}
    for f in glob.glob(os.path.join(NARR, '*.md')):
        name = os.path.basename(f)
        if name.startswith('00-'):
            continue
        m = re.match(r'(.+)-v(\d+)-\d{8}\.md$', name)
        if not m:
            continue
        if m.group(1) not in best or int(m.group(2)) > best[m.group(1)][0]:
            best[m.group(1)] = (int(m.group(2)), f)
    return sorted(f for _, f in best.values())


def narrative_index():
    idx = {}
    for f in current_chapters():
        title, section, para, in_para = None, '(opening)', 0, False
        for line in open(f, encoding='utf-8'):
            s = line.strip()
            if s.startswith('# '):
                title = s[2:].strip()
                continue
            if s.startswith('#'):
                section, para, in_para = s.lstrip('#').strip(), 0, False
                continue
            if not s:
                in_para = False
                continue
            if not in_para:
                para += 1
                in_para = True
            for b, c, v, how in cites(s):
                place = f'{title or os.path.basename(f)} · {section} · ¶{para}' + (f' ({how})' if how else '')
                idx.setdefault((b, c, v), [])
                if place not in idx[(b, c, v)]:
                    idx[(b, c, v)].append(place)
    return idx


def ot_rows():
    rows = []
    for line in open(OTR, encoding='utf-8'):
        if line.startswith('| OT-'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            status = cells[-1]
            st = 'resolved' if 'resolved' in status.lower()[:40] else ('touched' if status.lower().startswith('touched') else 'open')
            rows.append((cells[0], ' | '.join(cells[1:]), st))  # every column: thread, raised, trigger, status
    return rows


def main(inp, outp):
    narr = narrative_index()
    ots = ot_rows()
    ot_cites = {}
    pair_ot = {}
    for oid, text, st in ots:
        for b, c, v, how in cites(text):
            ot_cites.setdefault((b, c, v), set()).add(f'{oid} ({st})')
        m = re.search(r'Anger \(M02\) and .*?\((M\d+)\)', text)
        if m:
            pair_ot[m.group(1)] = (oid, st)
    pair_verses = {}
    for r in csv.DictReader(open(PAIRS, encoding='utf-8-sig')):
        if r['mcode'] in pair_ot:
            oid, st = pair_ot[r['mcode']]
            for ref in r['verse_list'].split(';'):
                ref = ref.strip()
                if ref:
                    pair_verses.setdefault(ref_key(ref), set()).add(f'{oid} {r["mcode"]} {r["cluster"]} ({st})')
    rows = list(csv.DictReader(open(inp, encoding='utf-8-sig')))
    cols = list(rows[0].keys())
    cols = cols[:-1] + ['narrative_n', 'narrative_refs', 'ot_refs', 'ot_pairing'] + cols[-1:]
    with open(outp, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in rows:
            k = ref_key(r['reference'])
            places = narr.get(k, [])
            r['narrative_n'] = len(places)
            r['narrative_refs'] = ' | '.join(places)
            r['ot_refs'] = ' | '.join(sorted(ot_cites.get(k, [])))
            r['ot_pairing'] = ' | '.join(sorted(pair_verses.get(k, []), key=lambda x: int(x[3:x.index(' ')])))
            w.writerow(r)
    print(f'{len(rows)} verses -> {outp}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
