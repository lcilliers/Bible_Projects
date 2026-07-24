"""
Exploratory data-prep extract (not wired into the app or DB pipeline).

Reads strong_lexicon.mounce (an HTML string), parses it to plain text, and
explodes it into one row per sense: <br> tags split first, then commas, then
semicolons. Double quotes are stripped before the comma split (so a quoted
comma-list like "heart, affection, tenderness" also splits). Commas/
semicolons inside brackets ( ) [ ] { } still protect the clause from
splitting, so nested parenthetical explanations stay on one row. Colons are
replaced with spaces throughout.

Each output row is also tagged with a row_type via lexicon_split_common.py's
classify_row(), based on the row's word count (letters-only tokens;
punctuation like a lone "-" doesn't count):
  - not applicable: empty text, or text that is entirely wrapped in one
    bracket pair with nothing outside it (e.g. "(gen.)", "(middle/passive)")
    - these are grammatical/case labels, not lexical content.
  - lookup: 1-3 words, pure Latin script - short enough to plausibly serve
    as a verse-lookup term (e.g. "evil", "birth pain").
  - description: 4+ words, OR any Greek/Hebrew script present regardless of
    length - reads as an explanatory clause/sentence, or carries an
    original-language form/cross-reference rather than an English lookup
    term.
This is a heuristic, not a linguistic classifier - spot-check before relying
on it.

Usage:
    python build_mounce_lexicon_extract.py [--db PATH] [--out PATH]
"""
import argparse
import csv
import re
import sqlite3
from html.parser import HTMLParser

from lexicon_split_common import bracket_aware_split, classify_row

DEFAULT_DB = r"C:/Bible_study_projects/iba/app/db/iba.db"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/mounce-lexicon-parsed-iba-20260723.csv"


class RowSplittingParser(HTMLParser):
    """Strips markup tags (keeping their inner text) and treats <br> as a row break."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows = [""]

    def handle_starttag(self, tag, attrs):
        if tag == "br":
            self.rows.append("")

    def handle_data(self, data):
        self.rows[-1] += data


def parse_html_rows(html):
    if html is None:
        return [""]
    p = RowSplittingParser()
    p.feed(html)
    return [re.sub(r"\s+", " ", r).strip() for r in p.rows]


def split_on(rows, sep):
    out = []
    for strong, text in rows:
        for part in bracket_aware_split(text, sep):
            out.append((strong, part))
    return out


def build_rows(conn):
    cur = conn.cursor()
    cur.execute("select strong, mounce from strong_lexicon")

    rows = []
    for strong, mounce in cur.fetchall():
        for segment in parse_html_rows(mounce):
            rows.append((strong, segment))

    rows = [(strong, text.replace('"', "")) for strong, text in rows]
    rows = split_on(rows, ",")
    rows = split_on(rows, ";")
    rows = [(strong, re.sub(r"\s+", " ", text.replace(":", " ")).strip()) for strong, text in rows]
    return [(strong, text, classify_row(text)) for strong, text in rows]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    rows = build_rows(conn)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["strong", "mounce_parsed", "row_type"])
        writer.writerows(rows)

    print("rows:", len(rows))
    print("path:", args.out)


if __name__ == "__main__":
    main()
