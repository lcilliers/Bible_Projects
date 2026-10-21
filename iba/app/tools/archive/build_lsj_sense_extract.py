"""
Exploratory data-prep extract (not wired into the app or DB pipeline).

Reads strong_lexicon.lsj (an LSJ classical-Greek lexicon entry, HTML string)
and splits it by sense rather than by punctuation. LSJ entries use
<Level1>/<Level2>/<Level3>/<Level4> tags to mark sense divisions (e.g. "I",
"II", "II.2", "II.2.b") - each such tag starts a new output row. A sub-sense
nested under the first, usually-implicit "I" carries only a bare numeric
label in LSJ's own source text ("2" instead of "I.2") - composed back onto
its parent here (see the pass after the "relabel first sense as I" step;
measured: 3856 of 25775 rows, 662 strongs affected pre-fix).

Within each sense block, text is separated by role, not concatenated:
  - gloss: text inside <b>...</b> spans - the actual definitional wording
    (e.g. "reply, answer", "playing a part"). Exact-duplicate gloss
    fragments within the same block are deduped (LSJ sometimes bolds the
    same word twice for the same sense).
  - note:  everything else in the block except citation links - dialect/
    grammar labels (<i>...</i>), connective prose, Greek example phrases.
  - <a>...</a> link text is discarded entirely: it's citation shorthand
    ("Refs 5th c.BC+", "NT+4th c.BC+"), not meaning content. The citation
    detail lives in the link's title attribute, which is not surfaced here.

The entry's headword (Greek lemma + morphology, before the first sense tag)
is emitted as its own row with sense_label "headword".

(2026-07-25: this sense's gloss is now kept whole, NOT exploded on comma/
semicolon - matching the same fix in build_meaning_tree_extract.py and
build_mounce_lexicon_extract.py: checking back against STEP showed internal
commas in a bold span are punctuation within one sense, not sense
separators, e.g. G0026's block "I.2" bolds "love" and "brotherly love,
charity," as two phrases - the comma inside the second one is not a third
sense.  sense_label and note are still repeated across rows when a block
has more than one <b> span, since gloss reassembly across spans in the same
block is unchanged here - flagged, not fixed, in this pass.) Every row is
tagged row_type: "headword" for the headword row(s), "lookup" for every
sense row - unlike Mounce, there is no word-count-based lookup/description
split here, since the gloss/note separation already isolates the
definitional wording from the surrounding prose.

strong is split into strong (base code) + strong_variant, matching
build_mounce_lexicon_extract.py/build_meaning_tree_extract.py - see
lexicon_split_common.py's split_strong_variant().

This is a different object from build_mounce_lexicon_extract.py's flat
term list: one row per SENSE (multi-row per strong is expected), with
gloss/note kept in separate columns rather than merged into one string.

Usage:
    python build_lsj_sense_extract.py [--db PATH] [--out PATH]
"""
import argparse
import csv
import re
import sqlite3
from html.parser import HTMLParser

from lexicon_split_common import split_strong_variant

DEFAULT_DB = r"C:/Bible_study_projects/iba/app/db/iba.db"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/lsj-sense-parsed-iba-20260725.csv"

LEVEL_TAGS = {"level1", "level2", "level3", "level4"}
TOP_LEVEL_LABEL_RE = re.compile(r"^[IVXLCDM]+$")
BARE_SUBLABEL_RE = re.compile(r"^\d+[a-z]*$")


class SenseParser(HTMLParser):
    """
    LSJ entries almost always leave the first sense ("I") without an explicit
    <LevelN> tag - only later senses (II, III, ...) get one (measured: 1478
    of 1505 entries). So <br> tags are also treated as block boundaries, not
    just <LevelN> tags; empty blocks (e.g. a bare <br><br> before a Level
    tag) are dropped later, and the first surviving unlabeled block after
    the headword is relabeled "I".
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = [{"label": "headword", "gloss": [], "note": []}]
        self.in_bold = False
        self.in_link = False
        self.in_level_label = False

    def handle_starttag(self, tag, attrs):
        if tag in LEVEL_TAGS:
            self.blocks.append({"label": "", "gloss": [], "note": []})
            self.in_level_label = True
        elif tag == "br":
            self.blocks.append({"label": "", "gloss": [], "note": []})
        elif tag == "b":
            self.in_bold = True
        elif tag == "a":
            self.in_link = True

    def handle_endtag(self, tag):
        if tag in LEVEL_TAGS:
            self.in_level_label = False
        elif tag == "b":
            self.in_bold = False
        elif tag == "a":
            self.in_link = False

    def handle_data(self, data):
        if self.in_link:
            return
        if self.in_level_label:
            self.blocks[-1]["label"] += data
        elif self.in_bold:
            self.blocks[-1]["gloss"].append(data)
        else:
            self.blocks[-1]["note"].append(data)


def clean(s):
    s = re.sub(r"\[\s*\]", "", s)  # empty brackets left by a stripped <a> link
    return re.sub(r"\s+", " ", s).strip()


def dedupe_preserve_order(items):
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def parse_lsj_rows(strong, strong_variant, html):
    if not html:
        return [(strong, strong_variant, "", "", "", "lookup")]

    p = SenseParser()
    p.feed(html)

    parsed = []
    for i, block in enumerate(p.blocks):
        label = clean(block["label"]).lstrip("_") or ("headword" if i == 0 else "")
        gloss_parts = dedupe_preserve_order(
            [clean(g).rstrip(",").strip() for g in block["gloss"] if clean(g)]
        )
        gloss = ", ".join(gloss_parts)
        note = clean(" ".join(block["note"]))
        if not label and not gloss and not note:
            continue  # empty block from a bare <br> that precedes a <LevelN> tag
        parsed.append([strong, label, gloss, note])

    # the first sense after the headword is conventionally "I" even when LSJ
    # leaves it unlabeled (see SenseParser docstring)
    for row in parsed[1:]:
        if row[1] == "":
            row[1] = "I"
        break

    # A sub-sense nested directly under the (usually implicit) first "I" gets
    # a bare numeric label from LSJ's own source text ("2", "3", ...), unlike
    # a sub-sense under a later, explicitly-<LevelN>-tagged top level, which
    # already carries the composed label in the source ("II.2", "II.2.b").
    # Compose the bare ones the same way here, from the nearest preceding
    # top-level Roman-numeral label - otherwise two genuinely different
    # senses (e.g. LSJ G0026's "I" and its unlabeled sub-sense "2", both
    # glossing "love") look identical and indistinguishable downstream.
    current_top = None
    for row in parsed:
        label = row[1]
        if label == "headword":
            continue
        if TOP_LEVEL_LABEL_RE.match(label):
            current_top = label
        elif BARE_SUBLABEL_RE.match(label) and current_top:
            row[1] = f"{current_top}.{label}"

    final_rows = []
    for row_strong, label, gloss, note in parsed:
        row_type = "headword" if label == "headword" else "lookup"
        final_rows.append((row_strong, strong_variant, label, gloss, note, row_type))
    return final_rows


def build_rows(conn):
    cur = conn.cursor()
    cur.execute("select strong, lsj from strong_lexicon")

    rows = []
    for strong, lsj in cur.fetchall():
        base, variant = split_strong_variant(strong)
        rows.extend(parse_lsj_rows(base, variant, lsj))
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
        writer.writerow(["strong", "strong_variant", "sense_label", "gloss", "note", "row_type"])
        writer.writerows(rows)

    print("rows:", len(rows))
    print("path:", args.out)


if __name__ == "__main__":
    main()
