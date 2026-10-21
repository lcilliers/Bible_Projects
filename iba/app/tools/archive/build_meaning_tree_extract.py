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
sense (lemma_key + sort). An earlier version of this script further
exploded each gloss on comma/semicolon (the split shared with
build_mounce_lexicon_extract.py/build_lsj_sense_extract.py via
lexicon_split_common.py's split_multi_gloss()) - but checking back against
STEP showed that was wrong for this table: a <b> span like "to celebrate,
praise;" (G0021) or "goodness, virtue, beneficence," (G0019) is ONE
sense/synonym-group as STEP displays it, not several independently
splittable ones - the internal commas are punctuation inside a single
definition, not sense separators. (2026-07-25: comma/semicolon/colon
splitting removed; the only sense-separator this script now recognises is
a literal line break. No row in strong_meaning_tree currently contains
one, so each <b> span - and any no-markup outline row - currently yields
exactly one gloss row; this only takes effect if line-break-delimited
senses appear in the source later.) lemma_key/sort/sense_code are repeated
across rows exploded from the same source row (multiple <b> spans still
produce multiple rows - see SEGMENT-SCOPED refs/notes below).

SEGMENT-SCOPED refs/notes (2026-07-25 rework): 774 of 9454 source rows
(~8%) contain more than one <b>...</b> span, each typically followed by
its own <ref> citation(s) - e.g. G0019: "<b>goodness, virtue,
beneficence,</b> <ref>Rom.15.14</ref> <ref>Eph.5.9</ref> <b>generosity,</b>
<ref>Gal.5.22</ref>". An earlier version of this script extracted
verse_refs/note once per source row and stamped the same aggregate string
onto every exploded gloss row, which misattributed refs across unrelated
<b> spans (Gal.5.22 would land on "goodness" too). SegmentParser below
instead groups the row into one "segment" per <b> span (plus any leading
text before the first <b>, folded into that first segment) and scopes
verse_refs/note to the segment a gloss actually came from. This is the
requirement driving the rework: every ref/note stays attached to the exact
gloss span it followed in the source, and nothing in sense_text is
dropped - untagged leading/connective text, <i> notes, <greek> forms, and
ref keys all still land in some segment's note/refs/gloss, never discarded.

Output columns:
  - lemma_key, sort: as-is from the source row.
  - sense_code: sense_code column, or an embedded outline-code prefix
    extracted from sense_text (see above), or "" if neither is present.
  - gloss: the full text of one <b>...</b> span (Thayer/Vine rows, kept
    intact - not split on internal commas/semicolons/colons), or the
    entire remaining text when there is no <b> markup at all (outline
    rows). Only split further on a literal line break in the source, of
    which there are currently none in this table.
  - verse_refs: the ref='...' key values (case preserved, e.g.
    "Act.14.17") belonging to this gloss's own segment (the <b> span it
    came from, plus any refs trailing it up to the next <b> span),
    semicolon-joined in source order. A single ref tag can itself contain
    a squished multi-verse citation (e.g. "Mat.4.24; 8:16;") - that is
    kept as one entry, not further split, since it isn't reliably
    decomposable.
  - note: text from this gloss's own segment that isn't the <b> gloss
    itself or a ref citation - <i> usage/dialect notes, <greek>
    original-language forms, connective prose between spans. The ref
    tag's own display text (e.g. "Acts 14:17") is dropped here since it's
    redundant with verse_refs.
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

lemma_key is split into strong (base code) + strong_variant via
lexicon_split_common.py's split_strong_variant() - the same split
build_mounce_lexicon_extract.py applies to strong_lexicon.strong - so both
extracts carry matching strong/strong_variant columns. In practice
strong_variant is always "" here: lemma_key never carries a sub-entry
letter (confirmed 3169/3169 distinct values), which is exactly why the two
sources needed this common split to join cleanly (see
build_meaning_mounce_combined.py).

Usage:
    python build_meaning_tree_extract.py [--db PATH] [--out PATH]
"""
import argparse
import csv
import html
import re
import sqlite3
from html.parser import HTMLParser

from lexicon_split_common import classify_row, split_strong_variant

DEFAULT_DB = r"C:/Bible_study_projects/iba/app/db/iba.db"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/strong-meaning-tree-parsed-iba-20260725.csv"

OUTLINE_CODE_RE = re.compile(r"^(\d+[a-zA-Z0-9]*\))\s*(.*)$", re.S)
REF_TAG_RE = re.compile(r"""<ref=['"]([^'"]*)['"]>""")
LINEBREAK_RE = re.compile(r"[\r\n]+")


def split_by_linebreak(text):
    """Explode a gloss on line breaks only - NOT comma/semicolon/colon (see
    module docstring: checking back against STEP showed internal commas in
    a <b> span are punctuation within one sense, not sense separators)."""
    if not text:
        return []
    return [p for p in (clean(part) for part in LINEBREAK_RE.split(text)) if p]


def normalize_refs(text):
    # <ref='Act.14.17'>display</ref> uses a nameless '=value' pseudo-attribute
    # that HTMLParser can't parse as a real attribute - rewrite it to a
    # well-formed <ref key="..."> so the key survives into SegmentParser
    # (previously the key was pulled out via a separate whole-string regex
    # pass, which is what let refs drift away from their owning segment).
    def repl(m):
        return '<ref key="%s">' % html.escape(m.group(1), quote=True)

    return REF_TAG_RE.sub(repl, text)


class SegmentParser(HTMLParser):
    """Splits sense_text into one segment per <b> span (leading text before
    the first <b> folds into that first segment), so verse_refs/note stay
    scoped to the gloss they actually followed instead of being pooled
    across the whole row."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.segments = [{"gloss": [], "refs": [], "note": []}]
        self.cur = self.segments[0]
        self.in_bold = False
        self.in_ref = False

    def handle_starttag(self, tag, attrs):
        if tag == "b":
            if not self.in_bold:
                self.in_bold = True
                if self.cur["gloss"]:
                    # already-filled segment -> this <b> starts a new one
                    self.cur = {"gloss": [], "refs": [], "note": []}
                    self.segments.append(self.cur)
        elif tag == "ref":
            self.in_ref = True
            self.cur["refs"].append(dict(attrs).get("key", ""))

    def handle_endtag(self, tag):
        if tag == "b":
            self.in_bold = False
        elif tag == "ref":
            self.in_ref = False

    def handle_data(self, data):
        if self.in_ref:
            return  # display text is redundant with the extracted ref key
        if self.in_bold:
            self.cur["gloss"].append(data)
        else:
            self.cur["note"].append(data)


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


def parse_sense_text(strong, strong_variant, sort, sense_code, sense_text):
    code, remaining = extract_sense_code(sense_code, sense_text)

    p = SegmentParser()
    p.feed(normalize_refs(remaining))

    rows = []
    for seg in p.segments:
        gloss_parts = dedupe_preserve_order([clean(g) for g in seg["gloss"] if clean(g)])
        gloss = ", ".join(gloss_parts)
        note = clean(" ".join(seg["note"]))
        verse_refs = "; ".join(r for r in seg["refs"] if r)

        if not gloss and note:
            # no <b> markup in this segment (e.g. no <b> at all in the row)
            # - what's there is already just a plain gloss
            gloss, note = note, ""

        for part in (split_by_linebreak(gloss) or [gloss]):
            rows.append((strong, strong_variant, sort, code, part, verse_refs, note, classify_row(part)))
    return rows


def build_rows(conn):
    cur = conn.cursor()
    cur.execute("select lemma_key, sort, sense_code, sense_text from strong_meaning_tree order by lemma_key, sort")
    rows = []
    for lemma_key, sort, sense_code, sense_text in cur.fetchall():
        strong, strong_variant = split_strong_variant(lemma_key)
        rows.extend(parse_sense_text(strong, strong_variant, sort, sense_code, sense_text))
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
        writer.writerow(["strong", "strong_variant", "sort", "sense_code", "gloss", "verse_refs", "note", "row_type"])
        writer.writerows(rows)

    print("rows:", len(rows))
    print("path:", args.out)


if __name__ == "__main__":
    main()
