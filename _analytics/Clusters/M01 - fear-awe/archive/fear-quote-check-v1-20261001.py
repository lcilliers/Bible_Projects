"""Quote check for fear-strand ledgers and narrative files (read-only).

For each markdown table row, takes the references cited in that row, fetches their
ESV text from iba.db `verse`, and checks that every double-quoted fragment (split at
"…") occurs in that text, ignoring case, punctuation and quotation marks.

Usage: python fear-quote-check-v1-20261001.py <file.md> [--prose] [--db iba/app/db/iba.db]
--prose: for chapter text. Each line (paragraph or bullet) is a unit, full book names
("1 Samuel 16:4", "Psalm 55:4") are mapped to the short forms, and the book carries
forward from earlier lines for bare references such as "(33:8)".
Book references use the iba.db short forms (Gen, Exo, 1Sa, Psa, Song, Joe ...).
Handles "Isa 2:10, 19, 21", "Jer 36:16, 23-24", "Job 4:13–16", "Eze 39:26; 34:28"
(book carried forward) and references inside parentheses.
"""
import re, sqlite3, sys

REF = re.compile(r"(?:\b([1-3]?[A-Z][a-z]{1,4})\s+)?(\d+):(\d+)(?:[–-](\d+))?((?:,\s*\d+(?:[–-]\d+)?)*)")


FULL = {"Genesis": "Gen", "Exodus": "Exo", "Leviticus": "Lev", "Numbers": "Num", "Deuteronomy": "Deu",
    "Joshua": "Jos", "Judges": "Judg", "Ruth": "Rut", "1 Samuel": "1Sa", "2 Samuel": "2Sa", "1 Kings": "1Ki",
    "2 Kings": "2Ki", "1 Chronicles": "1Ch", "2 Chronicles": "2Ch", "Ezra": "Ezr", "Nehemiah": "Neh",
    "Esther": "Est", "Job": "Job", "Psalms": "Psa", "Psalm": "Psa", "Proverbs": "Pro", "Ecclesiastes": "Ecc",
    "Song of Songs": "Song", "Isaiah": "Isa", "Jeremiah": "Jer", "Lamentations": "Lam", "Ezekiel": "Eze",
    "Daniel": "Dan", "Hosea": "Hos", "Joel": "Joe", "Amos": "Amo", "Obadiah": "Obd", "Jonah": "Jon",
    "Micah": "Mic", "Nahum": "Nah", "Habakkuk": "Hab", "Zephaniah": "Zep", "Haggai": "Hag",
    "Zechariah": "Zec", "Malachi": "Mal", "Matthew": "Mat", "Mark": "Mar", "Luke": "Luk", "John": "Joh",
    "Acts": "Act", "Romans": "Rom", "1 Corinthians": "1Cor", "2 Corinthians": "2Cor", "Galatians": "Gal",
    "Ephesians": "Eph", "Philippians": "Phili", "Colossians": "Col", "1 Thessalonians": "1Th",
    "2 Thessalonians": "2Th", "1 Timothy": "1Ti", "2 Timothy": "2Ti", "Titus": "Tit", "Philemon": "Phile",
    "Hebrews": "Heb", "James": "Jam", "1 Peter": "1Pe", "2 Peter": "2Pe", "1 John": "1Jo", "2 John": "2Jo",
    "3 John": "3Jo", "Jude": "Jude", "Revelation": "Rev"}
FULL_RE = re.compile(r"\b(" + "|".join(sorted(map(re.escape, FULL), key=len, reverse=True)) + r")(?=\s+\d+:)")


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower())).strip()


def refs_in(cell, book=None):
    out = []
    for m in REF.finditer(cell):
        if m.group(1):
            book = m.group(1)
        if not book:
            continue
        ch, v1, v2, rest = int(m.group(2)), int(m.group(3)), m.group(4), m.group(5)
        vs = list(range(v1, int(v2) + 1)) if v2 else [v1]
        for part in re.findall(r"\d+(?:[–-]\d+)?", rest or ""):
            a, _, b = part.replace("–", "-").partition("-")
            vs += list(range(int(a), int(b or a) + 1))
        out += [f"{book} {ch}:{v}" for v in vs]
    return out, book


def main():
    path = sys.argv[1]
    db = sys.argv[sys.argv.index("--db") + 1] if "--db" in sys.argv else "iba/app/db/iba.db"
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    verses = dict(con.execute("select reference, text from verse where deleted=0 and text is not null"))
    text = verses.get
    fails, checked, missing, unref = [], 0, set(), []
    parent_refs = []
    prose = "--prose" in sys.argv
    book = None
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        if prose:
            if not line.strip() or line.startswith("#"):
                continue
            body = line
            refs, book = refs_in(FULL_RE.sub(lambda m: FULL[m.group(1)], line), book)
        else:
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3:
                continue
            body, refcell = cells[1], cells[2]
            if cells[0].startswith("FE-"):
                parent_refs, _ = refs_in(body + " " + refcell)
            refs, _ = refs_in(body + " " + refcell)
            refs = refs + (parent_refs if cells[0] == "" else [])
        for m in re.finditer(r'"([^"]+)"', body):
            q = m.group(1)
            # gloss labels (*translit*, "gloss" / "gloss", H1234) are not quotations
            if re.search(r"\*,\s*$", body[:m.start()]) or re.match(r",\s*[HG]\d", body[m.end():]):
                continue
            if not refs:
                unref.append(q)
                continue
            frags = [f for f in (norm(x) for x in re.split(r"…|\[[^\]]*\]", q)) if len(f) > 2]
            if not frags:
                continue
            checked += 1
            pool = []
            for r in dict.fromkeys(refs):  # keep citation order so a quote may run across verses
                t = text(r)
                if t is None:
                    missing.add(r)
                else:
                    pool.append(norm(t))
            hay = " ".join(pool)
            bad = [f for f in frags if f not in hay]
            if bad:
                fails.append((ln, q, bad, sorted(set(refs))))
    print(f"quotes checked: {checked}; failures: {len(fails)}; refs with no verse text: {sorted(missing)}")
    if unref:
        print(f"  quoted labels with no reference in the row (not checked): {unref}")
    for ln, q, bad, refs in fails:
        print(f"  line {ln}: \"{q}\" -> not found: {bad} in {refs}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
