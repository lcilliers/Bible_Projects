"""
Exploratory data-prep extract (not wired into the app or DB pipeline).

Combines the row_type == "lookup" rows from all three lexicon extracts -
build_mounce_lexicon_extract.py, build_lsj_sense_extract.py,
build_meaning_tree_extract.py - into one CSV of (strong, term, source).
Each source script's build_rows(conn) is called directly (not read back off
its own CSV, so this always reflects the current DB/parsing logic), then
filtered to its lookup rows and reduced to just the Strong's number and the
lookup term itself - "headword"/"description"/"not applicable" rows and the
other per-source columns (note, verse_refs, sense_label, ...) are dropped,
since this extract is purpose-built as a flat cross-source lookup list.

A row_type == "lookup" tag is necessary but not sufficient for a usable
term, so two further gremlins are filtered here rather than upstream in the
per-source scripts (this extract's own definition of "usable lookup term",
not a correction to what "lookup" means in the source CSVs):
  - blank terms: LSJ sense blocks where the <b> gloss span was empty and
    all content sat in `note` instead (e.g. sense "I.6" of G0018) still get
    tagged "lookup" by build_lsj_sense_extract.py, since that script's
    row_type is headword-vs-not, not content-presence. 888 such rows.
  - Greek-script terms: LSJ occasionally bolds a Greek cross-reference
    alongside the English gloss in the same sense block (e.g. G0014 sense
    "I" = "do good, well, ἀγαθουργέω" - the last a cross-reference to the
    uncontracted headword, not an English lookup word), and a handful of
    strong_meaning_tree rows do the same. 846 such rows (821 lsj, 25
    meaning_tree). Dropped by requiring at least one Latin letter in the
    term.

(strong, term, source) triples are deduped: LSJ in particular can gloss two
genuinely different, separately-numbered senses of the same Strong's number
with the identical English word (e.g. G0026's sense "I" and its sub-sense
"I.2" both gloss "love" - a real LSJ distinction, not a parsing artifact;
see build_lsj_sense_extract.py's sub-label composition fix for that case
specifically). This flat list has no sense_label column to keep them apart,
so the repeat adds nothing and is dropped. The same term recurring ACROSS
different sources for one strong is kept (rows differ by source) - that's
cross-source corroboration, not a duplicate.

Rows are sorted by strong, then by the source order below, so every source's
lookup terms for a given Strong's number sit together.

ib_relevance column: a free, local, wordlist-based first pass at whether the
term's own meaning touches the inner being - "IB related" / "Could impact
IB" / "Not relevant" - via ib_relevance_classifier.classify_ib_relevance().
No DB lookups, no context: it judges the term standalone, the same way a
human skimming the list would for the obvious cases, and defers anything it
can't call confidently to "Could impact IB" for manual review. See that
module's docstring for the category wordlists and their limits.

Usage:
    python build_lexicon_lookup_extract.py [--db PATH] [--out PATH]
"""
import argparse
import csv
import re
import sqlite3

import build_mounce_lexicon_extract as mounce_mod
import build_lsj_sense_extract as lsj_mod
import build_meaning_tree_extract as meaning_mod
from ib_relevance_classifier import classify_ib_relevance

DEFAULT_DB = r"C:/Bible_study_projects/iba/app/db/iba.db"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/lexicon-lookup-terms-iba-20260724.csv"

SOURCE_ORDER = ["mounce", "lsj", "meaning_tree"]


def is_usable_lookup_term(term):
    """Non-blank, and containing at least one Latin letter (excludes stray
    Greek cross-reference forms bolded alongside the real English gloss)."""
    return bool(term.strip()) and bool(re.search(r"[A-Za-z]", term))


def build_rows(conn):
    rows = []
    for strong, term, row_type in mounce_mod.build_rows(conn):
        if row_type == "lookup" and is_usable_lookup_term(term):
            rows.append(("mounce", strong, term))

    for strong, sense_label, gloss, note, row_type in lsj_mod.build_rows(conn):
        if row_type == "lookup" and is_usable_lookup_term(gloss):
            rows.append(("lsj", strong, gloss))

    for lemma_key, sort, sense_code, gloss, verse_refs, note, row_type in meaning_mod.build_rows(conn):
        if row_type == "lookup" and is_usable_lookup_term(gloss):
            rows.append(("meaning_tree", lemma_key, gloss))

    rows = dedupe_preserve_order(rows)
    source_rank = {name: i for i, name in enumerate(SOURCE_ORDER)}
    rows.sort(key=lambda r: (r[1], source_rank[r[0]]))
    return [(strong, term, source, classify_ib_relevance(term)) for source, strong, term in rows]


def dedupe_preserve_order(items):
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    rows = build_rows(conn)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["strong", "term", "source", "ib_relevance"])
        writer.writerows(rows)

    print("rows:", len(rows))
    print("path:", args.out)


if __name__ == "__main__":
    main()
