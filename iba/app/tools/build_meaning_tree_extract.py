"""
Exploratory data-prep extract (not wired into the app or DB pipeline).

Reads lemma_key, sort, sense_code, sense_text from strong_meaning_tree and
parses sense_text (an HTML string) into structured columns. Unlike the
mounce/lsj extracts, this table is already one row per sense (lemma_key +
sort), so no row-splitting is needed - only per-row parsing.

The table mixes two source styles, discovered by inspection:
  1. Thayer/Vine-style prose (mostly Greek terms): <b>gloss</b> spans plus
     <ref='Book.Ch.Vs'>display</ref> verse citations, <i>...</i> usage
     notes, <greek>...</greek> original-language forms.
  2. BDB/Strong's-outline style (mostly Hebrew terms): short hierarchical
     phrases with no markup, numbered/lettered (e.g. "1a1a) to find,
     secure..."). The outline code is normally in the sense_code column,
     but for 229 of 3773 sense_code-empty rows it is instead embedded as a
     literal prefix on sense_text - this script detects and extracts that
     prefix into sense_code, matching the rows where it's already a column.

Unlike the mounce/lsj extracts, this table started out already one row per
sense (lemma_key + sort) - but the assembled gloss can still bundle several
comma/semicolon-delimited terms in one string (e.g. "to do good, confer
benefits"), so that gloss is exploded further, one row per term (bracket-
aware split shared with build_mounce_lexicon_extract.py/build_lsj_sense_
extract.py via lexicon_split_common.py). lemma_key/sort/sense_code/
verse_refs/note are repeated across the split rows; multi-row-per-
(lemma_key, sort) is therefore expected.

Output columns:
  - lemma_key, sort: as-is from the source row.
  - sense_code: sense_code column, or an embedded outline-code prefix
    extracted from sense_text (see above), or "" if neither is present.
  - gloss: one exploded term from the <b>...</b> span text (Thayer/Vine
    rows), or from the entire remaining text when there is no <b> markup
    at all (outline rows, which are already just a short gloss with no
    separate commentary).
  - verse_refs: the raw ref='...' key values (case preserved, e.g.
    "Act.14.17"), semicolon-joined in source order. A single ref tag can
    itself contain a squished multi-verse citation (e.g. "Mat.4.24; 8:16;")
    - that is kept as one entry, not further split, since it isn't
    reliably decomposable.
  - note: any remaining text that isn't part of a <b> gloss or a ref
    citation - <i> usage/dialect notes, <greek> original-language forms,
    connective prose. The ref tag's own display text (e.g. "Acts 14:17")
    is dropped here since it's redundant with verse_refs.
  - row_type: lexicon_split_common.py's classify_row() applied to the
    exploded term itself - lookup / description / not applicable, same
    scheme as build_mounce_lexicon_extract.py (word count, plus any Greek/
    Hebrew script forces non-lookup). Needed here specifically because,
    unlike the lsj extract, an outline-style row with no <b> markup at all
    dumps its ENTIRE sense_text into gloss via the fallback above - so gloss
    alone can still be a long descriptive clause, or can embed the original
    Hebrew/Greek term (e.g. a cross-reference like "or Judah (Aramaic
    יְהוּד)") rather than a clean English lookup word.

A handful of source rows carry stray pseudo-tags that embed a Strong's
number right after a word, e.g. "Jerusalem<H3389>" - these aren't real
markup (no closing tag) and are left to fall through to `note` as generic,
unhandled tags; they are not treated specially.

Usage:
    python build_meaning_tree_extract.py [--db PATH] [--out PATH]
"""
import argparse
import csv
import re
import sqlite3
from html.parser import HTMLParser

from lexicon_split_common import classify_row, split_multi_gloss

DEFAULT_DB = r"C:/Bible_study_projects/iba/app/db/iba.db"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/strong-meaning-tree-parsed-iba-20260723.csv"

OUTLINE_CODE_RE = re.compile(r"^(\d+[a-zA-Z0-9]*\))\s*(.*)$", re.S)
REF_TAG_RE = re.compile(r"""<ref=['"]([^'"]*)['"]>""")


class MeaningParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.gloss = []
        self.note = []
        self.in_bold = False
        self.in_ref = False

    def handle_starttag(self, tag, attrs):
        if tag == "b":
            self.in_bold = True
        elif tag == "ref":
            self.in_ref = True

    def handle_endtag(self, tag):
        if tag == "b":
            self.in_bold = False
        elif tag == "ref":
            self.in_ref = False

    def handle_data(self, data):
        if self.in_ref:
            return  # display text is redundant with the extracted ref key
        if self.in_bold:
            self.gloss.append(data)
        else:
            self.note.append(data)


def clean(s):
    return re.sub(r"\s+", " ", s).strip().strip(",").strip()


def dedupe_preserve_order(items):
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def extract_sense_code(sense_code, sense_text):
    if sense_code:
        return clean(sense_code), sense_text
    m = OUTLINE_CODE_RE.match(sense_text)
    if m:
        return m.group(1), m.group(2)
    return "", sense_text


def parse_sense_text(lemma_key, sort, sense_code, sense_text):
    code, remaining = extract_sense_code(sense_code, sense_text)

    verse_refs = "; ".join(REF_TAG_RE.findall(remaining))
    normalized = REF_TAG_RE.sub("<ref>", remaining)

    p = MeaningParser()
    p.feed(normalized)

    gloss_parts = dedupe_preserve_order([clean(g) for g in p.gloss if clean(g)])
    gloss = ", ".join(gloss_parts)
    note = clean(" ".join(p.note))

    if not gloss and note:
        # no <b> markup at all - the whole row is already just a plain gloss
        gloss, note = note, ""

    gloss_parts = split_multi_gloss(gloss) or [gloss]
    return [(lemma_key, sort, code, part, verse_refs, note, classify_row(part)) for part in gloss_parts]


def build_rows(conn):
    cur = conn.cursor()
    cur.execute("select lemma_key, sort, sense_code, sense_text from strong_meaning_tree order by lemma_key, sort")
    rows = []
    for row in cur.fetchall():
        rows.extend(parse_sense_text(*row))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    rows = build_rows(conn)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["lemma_key", "sort", "sense_code", "gloss", "verse_refs", "note", "row_type"])
        writer.writerows(rows)

    print("rows:", len(rows))
    print("path:", args.out)


if __name__ == "__main__":
    main()
