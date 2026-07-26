"""
Exploratory data-prep extract (not wired into the app or DB pipeline).

Reads strong_lexicon.mounce (an HTML string), parses it to plain text, and
explodes it into one row per sense, split ONLY on <br> tags (the source's
real line breaks - 41 of 1506 rows have one).

(2026-07-25: comma/semicolon/colon splitting removed, matching the same
fix in build_meaning_tree_extract.py - checking back against STEP showed
those are punctuation inside one sense, not sense separators; the only
delimiter that actually marks a new sense in these lexicon sources is a
line break. E.g. G0928H's mounce text "anguish<br>to torture, torment;
(passive) to be tortured, tormented, in pain" is two senses ("anguish" and
the "to torture..." clause), not five. Quote-stripping is also removed -
it existed only to let a quoted comma-list split, which no longer
applies, so literal quote characters in the source are now preserved
rather than silently dropped.)

strong_lexicon.strong itself is split into two output columns, strong
(base code) and strong_variant (trailing sub-entry letter, e.g. "G0928H"
-> strong="G0928", strong_variant="H"; "G0014" -> strong="G0014",
strong_variant=""). This exists to join cleanly against
strong_meaning_tree, which never carries a sub-entry letter (confirmed:
3169/3169 distinct lemma_key values have no trailing letter) - it collapses
sub-lettered senses to the base lemma. 49 of 1506 mounce rows have a
variant (suffixes seen: G, H, I, J, K); 9 rows don't fit the
[GH]dddd[letters]* shape at all (5-digit codes like "G20125") - those pass
through unsplit (strong_variant="") since they already match
strong_meaning_tree's lemma_key for the same term as-is.

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

from lexicon_split_common import classify_row, split_strong_variant

DEFAULT_DB = r"C:/Bible_study_projects/iba/app/db/iba.db"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/mounce-lexicon-parsed-iba-20260725.csv"


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


def build_rows(conn):
    cur = conn.cursor()
    cur.execute("select strong, mounce from strong_lexicon")

    rows = []
    for strong, mounce in cur.fetchall():
        base, variant = split_strong_variant(strong)
        for segment in parse_html_rows(mounce):
            rows.append((base, variant, segment))

    return [(base, variant, text, classify_row(text)) for base, variant, text in rows]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    rows = build_rows(conn)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["strong", "strong_variant", "mounce_parsed", "row_type"])
        writer.writerows(rows)

    print("rows:", len(rows))
    print("path:", args.out)


if __name__ == "__main__":
    main()
