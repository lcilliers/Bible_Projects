"""Cross-reference a verse list against the inner-being narrative and the open threads register.

#1978, 2026-10-06. Read-only. v2: adds the short forms 1Co, 2Co and Php, which v1 missed. Reusable for any verse-list CSV that has a `reference` column in
iba.db form (Gen 6:5, 1Cor 4:5, Phili 1:22).

For each verse it adds:
  narrative_refs : every place the verse is cited in the current chapter files
                   (chapter · section · paragraph), "book carried" when the citation is bare
                   (e.g. "8:21" after "Gen 6:5"), "in range" when inside a cited range
  narrative_n    : count of those places
  ot_refs        : open-threads rows that cite the verse in any column, with the row status
  ot_pairing     : open-threads M02 pairing rows (OT-16 to OT-90) whose verse list, in
                   wa-cluster-M02-mcode-face-combinations-v1-20261005.csv, holds the verse
                   (= the verse also has an anger word), with the row status

Chapter files: the highest version of each chapter in inner-being-narrative/ (archive and the
00-index status file are excluded).

Usage: python verse-narrative-ot-crossref-v2-20261006.py IN.csv OUT.csv
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
ALIAS = {}
for code, names in BOOKS.items():
    for n in names:
        ALIAS[n] = code
book_rx = '|'.join(sorted((re.escape(a) for a in ALIAS), key=len, reverse=True))
# A citation run: optional book, then chapter:verse with ranges, comma verses, ';'-separated chapters.
CV = r'(\d+):(\d+)[a-c]?(?:\s*[–-]\s*(?:(\d+):)?(\d+)[a-c]?)?((?:\s*,\s*\d+[a-c]?(?:\s*[–-]\s*\d+)?)*)'
TOKEN = re.compile(r'(?<![\w:])(?:(' + book_rx + r')\.?\s+)?' + CV)
CARRY_GAP = re.compile(r'^[\s;,()]*(?:and|with|beside|also|see|cf\.?)?[\s;,()]*$')


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


def cites(text):
    """Yield (book, chapter, verse, how) for every verse a line of text cites."""
    last_book, last_end = None, None
    for m in TOKEN.finditer(text):
        book = ALIAS.get(m.group(1)) if m.group(1) else None
        how = ''
        if not book:
            gap = text[last_end:m.start()] if last_end is not None else None
            if last_book and gap is not None and CARRY_GAP.match(gap):
                book, how = last_book, 'book carried'
            else:
                last_end = m.end()
                continue
        verses, single = expand(*m.group(2, 3, 4, 5, 6))
        for ch, v in sorted(verses):
            note = how
            if (ch, v) not in single:
                note = (note + '; ' if note else '') + 'in range ' + m.group(0).strip()
            yield book, ch, v, note
        last_book, last_end = book, m.end()


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
