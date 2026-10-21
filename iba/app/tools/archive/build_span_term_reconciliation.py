"""
Exploratory data-prep extract (not wired into the app or DB pipeline).

Reconciles the combined lexicon lookup-term list (build_lexicon_lookup_
extract.py's output CSV - one row per (strong, term, source)) against the
`span` table (every actual word occurrence in the live Bible text: one row
per (verse_id, position), carrying `surface` = the English word/phrase shown
for that occurrence and `strong_variant` = the Strong's number it renders).
Grammatical particles (`is_particle = 1` - definite article, conjunctions,
etc.) AND a further hand-verified set of Hebrew/Greek function words not
caught by that flag (FUNCTION_WORD_STRONGS - the direct-object marker,
copula, prepositions, conjunctions, pronouns, particles) are excluded from
span entirely - see load_span()'s docstring.

Both directions join on STRONG ALONE, not (word, strong) - a span strong_
variant's trailing single-letter sub-entry suffix (e.g. "H8165G") is
stripped to base form ("H8165") first, since the term list only carries
base-form Strong's numbers. Word-level mismatches are deliberately not
gaps: a lexicon gloss can be a real, correct synonym for a Strong's number
that this particular translation simply never chose as the rendering
anywhere it occurs, and a span word can be the translation's actual
rendering of a Strong's number our lexicon tables simply haven't loaded a
matching gloss for yet - neither is a genuine gap by itself. Two real gaps,
written to separate CSVs:
  - span rows whose base-form strong never appears anywhere in the term
    list at all: a possible "missing term" signal - this Strong's number
    has no lexicon coverage whatsoever, not just a missing rendering of it.
  - term list rows whose base-form strong never appears anywhere in span at
    all: a possible "missing verse" signal - this Strong's number never
    occurs in the live text under any word, so the verses containing it may
    not have been loaded into `span` at all.

Both lists are DISTINCT rows, not the raw row counts.

The span-side output also carries an ib_relevance column - the same free,
local, wordlist-based classify_ib_relevance() used in build_lexicon_lookup_
extract.py, applied to the span word itself - so the exception list can be
filtered down to its "IB related" rows first rather than triaged in one
undifferentiated 97K-row block.

Usage:
    python build_span_term_reconciliation.py [--db PATH] [--terms PATH]
        [--span-out PATH] [--terms-out PATH]
"""
import argparse
import csv
import re
import sqlite3

from ib_relevance_classifier import classify_ib_relevance

DEFAULT_DB = r"C:/Bible_study_projects/iba/app/db/iba.db"
DEFAULT_TERMS = r"C:/Bible_study_projects/outputs/csv/lexicon-lookup-terms-iba-20260724.csv"
DEFAULT_SPAN_OUT = r"C:/Bible_study_projects/outputs/csv/span-words-missing-from-term-list-iba-20260724.csv"
DEFAULT_TERMS_OUT = r"C:/Bible_study_projects/outputs/csv/term-list-words-missing-from-span-iba-20260724.csv"


def normalize(word):
    return re.sub(r"\s+", " ", word.strip().strip(".,;:!?'\"()[]{}").lower()).strip()


BASE_STRONG_RE = re.compile(r"^([HG]\d{4})[A-Za-z]?$")


def base_strong(strong):
    """Strips a span strong_variant's trailing single-letter sub-entry
    suffix (e.g. "H8165G" -> "H8165"), matching the term list's base-form
    Strong's numbers."""
    m = BASE_STRONG_RE.match(strong)
    return m.group(1) if m else strong


# Hebrew/Greek function words NOT caught by is_particle (they don't carry
# the H9xxx/G9xxx pattern) but behave identically: their `surface` text in
# span is essentially borrowed from whichever adjacent content word STEP's
# tagging attached to that position, since the marker/preposition/pronoun/
# conjunction/copula itself carries no independent English gloss. Found by
# querying span for the strongs with the most DISTINCT surface words
# attached (2026-07-24) - a real content word has natural but bounded
# synonym variety; H0853 alone had 2,111 distinct "renderings". Every code
# below was individually confirmed against known Hebrew/Greek grammar
# (direct-object marker, copula "to be", prepositions, conjunctions,
# pronouns, demonstratives, interrogatives, particles) - none of them could
# ever have a real mounce/lsj/meaning_tree entry, so comparing them against
# the term list only manufactures guaranteed, meaningless "missing" rows,
# same as particles. Deliberately does NOT include common-but-real light
# verbs (say, do, make, come, give...) or generic nouns (day, year, son,
# face...) that showed the same statistical pattern - those carry actual
# (if generic) lexical content and are handled by classify_ib_relevance's
# GENERIC_VERB_WORDS/GENERIC_NOUN_WORDS instead, not excluded here.
FUNCTION_WORD_STRONGS = {
    "H0853", "H1961", "H5921", "H3588", "H0834", "H0413", "H1931", "H3808",
    "H5973", "H3605", "G2532", "H1571", "H0854", "H5704", "H2088", "H4480",
    "G1161", "H8033", "H1992", "G1722", "G0846", "H1768", "H3651", "H0428",
    "H4994", "H0518", "H0859", "H2009", "H0176", "H0408", "H5750", "H2063",
    "H0589", "G2596", "H4100", "G3739", "G1510", "H0369", "H0996", "H3644",
    "H0310", "G3303", "G1519", "H4310", "G3361", "G5100", "H0637", "H4616",
    "H0595",
    # interrogative particles/adverbs - found 2026-07-24 via a user spot-
    # check on H4069 (maddua, "why"): these didn't make the original top-80-
    # by-distinct-word cutoff (they're much rarer overall than "the"/"and"),
    # but show the identical fingerprint at smaller scale - one dominant,
    # correct rendering plus a handful of occurrence-count-1/2 noise words
    # borrowed from an adjacent position. Each individually confirmed by
    # querying span directly before adding.
    "H4069", "H4970", "H0335", "H0575", "G4459", "G5101", "G4219", "G4226",
    "G1302", "G2444", "H0645", "H1097",
    # numeral "carrier" strongs - same borrowed-surface artifact, one word
    # per compound numeral phrase ("300", "four hundred", ...)
    "H3967", "H0505", "H0259", "H8147",
}


def load_span(conn):
    """Returns (counts, base_strongs_present):
    counts = {(word, strong_variant): occurrence_count} - exact, unstripped.
    base_strongs_present = set of base-form Strong's numbers occurring
    anywhere in span, under any word.

    Excludes is_particle=1 rows (grammatical particles - definite article,
    conjunctions, etc., typically H9xxx/G9xxx codes) and FUNCTION_WORD_
    STRONGS (see above): a particle's or function word's `surface` text is
    whatever adjacent real word STEP's tagging happened to attach to that
    position, not its own lexical content, and neither could ever have a
    real mounce/lsj/meaning_tree entry - comparing them against the term
    list only manufactures guaranteed, meaningless "missing" rows (measured:
    138,043 of 534,075 span rows, 26%, are particles; FUNCTION_WORD_STRONGS
    is a further ~50 codes on top of that)."""
    cur = conn.cursor()
    cur.execute("select surface, strong_variant from span where deleted = 0 and is_particle = 0")
    counts = {}
    base_strongs_present = set()
    for surface, strong_variant in cur.fetchall():
        if base_strong(strong_variant) in FUNCTION_WORD_STRONGS:
            continue
        word = normalize(surface)
        base_strongs_present.add(base_strong(strong_variant))
        if not word:
            continue
        key = (word, strong_variant)
        counts[key] = counts.get(key, 0) + 1
    return counts, base_strongs_present


def load_terms(terms_path):
    """Returns (rows, base_strongs_present):
    rows = [(strong, word, source), ...] - exact, unstripped, one per source.
    base_strongs_present = set of base-form Strong's numbers occurring
    anywhere in the term list, under any word."""
    rows = []
    base_strongs_present = set()
    with open(terms_path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            word = normalize(row["term"])
            base_strongs_present.add(base_strong(row["strong"]))
            if not word:
                continue
            rows.append((row["strong"], word, row["source"]))
    return rows, base_strongs_present


def build_rows(conn, terms_path):
    span_counts, span_base_strongs = load_span(conn)
    term_rows, term_base_strongs = load_terms(terms_path)

    span_only = [
        (strong, word, count, classify_ib_relevance(word))
        for (word, strong), count in span_counts.items()
        if base_strong(strong) not in term_base_strongs
    ]
    span_only.sort(key=lambda r: (-r[2], r[0], r[1]))

    terms_only_sources = {}
    for strong, word, source in term_rows:
        if base_strong(strong) not in span_base_strongs:
            terms_only_sources.setdefault((strong, word), set()).add(source)
    terms_only = [
        (strong, word, ";".join(sorted(srcs)))
        for (strong, word), srcs in terms_only_sources.items()
    ]
    terms_only.sort(key=lambda r: (r[0], r[1]))

    return span_only, terms_only


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--terms", default=DEFAULT_TERMS)
    ap.add_argument("--span-out", default=DEFAULT_SPAN_OUT)
    ap.add_argument("--terms-out", default=DEFAULT_TERMS_OUT)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    span_only, terms_only = build_rows(conn, args.terms)

    with open(args.span_out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["strong", "word", "occurrence_count", "ib_relevance"])
        writer.writerows(span_only)

    with open(args.terms_out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["strong", "word", "source"])
        writer.writerows(terms_only)

    print("span words not in term list:", len(span_only), "->", args.span_out)
    print("term list words not in span:", len(terms_only), "->", args.terms_out)


if __name__ == "__main__":
    main()
