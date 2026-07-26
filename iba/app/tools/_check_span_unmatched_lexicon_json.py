"""_check_span_unmatched_lexicon_json.py — read-only diagnostic, not wired
into the app or DB pipeline.

For every row in `span` (370200 rows post the 2026-07-25 combined-unit
rebuild - see BUILD.md §16), checks whether EACH of its codes (a row's
strong_variant can hold more than one, space-separated, when STEP's own
HTML tags them together, e.g. "G1722 G0054" on "purity") has a
corresponding entry in lexicon-combined-iba-20260725.json
(build_lexicon_combined_extract.py's output). Each code is split into
base + sub-entry letter via lexicon_split_common.split_strong_variant(),
same as every other script here.

EXCLUDED CODES (researcher direction, 2026-07-25): a code whose own
morph token (strong_variant and morph_code are space-separated and
positionally aligned - same convention as lib.stepapi.Step.parse_spans)
starts with PREP, ADV, or CONJ is not evaluated at all - prepositions,
adverbs and conjunctions are not expected to have their own lexicon
entry, so they should never make a row look "unmatched". This is
per-CODE, not per-row: a combined tag mixing an excluded function-word
code with a real content-word code (e.g. "purity" = G1722<PREP> +
G0054<N-DSF>) still checks the content code - only the excluded code is
dropped from consideration. Match on the token PREFIX (not exact "PREP"/
"ADV"/"CONJ" only) to also catch subtyped variants seen in the data
(ADV-C/ADV-I/ADV-N/ADV-T, CONJ-N).

2026-07-25 rework (superseding the very first pass, which ran before the
span combined-unit fix and mis-split multi-code strong_variant values as
if they were one code): this version checks each constituent code
separately, then drops PREP/ADV/CONJ-tagged codes from consideration.

A CODE is matched if its base is a key in the combined JSON AND its
specific variant (including "" for no sub-entry letter) is a key under
that base's "variants" - the finest-grained thing the combined JSON
addresses. A ROW is exported here if, among its NON-EXCLUDED codes, at
least one is unmatched - match_status is "none" (no evaluable code on
the tag matched) or "partial" (some did, some didn't). A row whose codes
are ALL excluded (e.g. a bare "the" = G1722 alone, PREP) is skipped
entirely - not matched, not unmatched, not applicable.

Usage:
    python -m iba.app.tools._check_span_unmatched_lexicon_json [--json PATH] [--out PATH]
"""
from __future__ import annotations

import argparse
import csv
import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lexicon_split_common import split_strong_variant  # noqa: E402

from ..lib.cfg import DB_PATH

DEFAULT_JSON = r"C:/Bible_study_projects/outputs/json/lexicon-combined-iba-20260725.json"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/span-unmatched-lexicon-json-iba-20260725.csv"

EXCLUDED_MORPH_PREFIXES = ("PREP", "ADV", "CONJ")


def load_known_variants(json_path):
    """Returns {base: set(variant_letters_present_in_"variants")}."""
    with open(json_path, encoding="utf-8") as f:
        combined = json.load(f)
    known = {}
    for base, rec in combined.items():
        known[base] = set(rec.get("variants", {}).keys())
    return known


def code_matched(code, known):
    base, variant = split_strong_variant(code)
    return variant in known.get(base, set())


def evaluable_codes(strong_variant, morph_code):
    """(code, is_excluded) pairs, codes and morph tokens paired positionally."""
    codes = (strong_variant or "").split()
    morphs = (morph_code or "").split()
    out = []
    for i, code in enumerate(codes):
        m = morphs[i] if i < len(morphs) else ""
        excluded = m.startswith(EXCLUDED_MORPH_PREFIXES)
        out.append((code, excluded))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=DEFAULT_JSON)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    known = load_known_variants(args.json)
    print(f"combined JSON bases: {len(known)}")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "select s.id, s.verse_id, s.position, s.surface, s.strong_variant, s.morph_code, s.is_particle "
        "from span s order by s.id"
    )

    total = 0
    all_excluded = 0
    fully_matched = 0
    unmatched_rows = []
    for row_id, verse_id, position, surface, strong_variant, morph_code, is_particle in cur:
        total += 1
        pairs = evaluable_codes(strong_variant, morph_code)
        eval_codes = [c for c, excluded in pairs if not excluded]
        if not eval_codes:
            all_excluded += 1
            continue
        unmatched_codes = [c for c in eval_codes if not code_matched(c, known)]
        if not unmatched_codes:
            fully_matched += 1
        else:
            status = "none" if len(unmatched_codes) == len(eval_codes) else "partial"
            unmatched_rows.append((
                row_id, verse_id, position, surface, strong_variant,
                " ".join(unmatched_codes), status, morph_code, is_particle,
            ))

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["span_id", "verse_id", "position", "surface", "strong_variant", "unmatched_codes", "match_status", "morph_code", "is_particle"])
        writer.writerows(unmatched_rows)

    print(f"span rows total: {total}")
    print(f"rows with every code excluded (PREP/ADV/CONJ only): {all_excluded}")
    print(f"fully matched (every evaluable code covered): {fully_matched}")
    print(f"not fully matched: {len(unmatched_rows)}")
    print(f"  of which partial (some evaluable codes covered): {sum(1 for r in unmatched_rows if r[6] == 'partial')}")
    print(f"  of which none (no evaluable codes covered): {sum(1 for r in unmatched_rows if r[6] == 'none')}")
    print(f"-> {args.out}")


if __name__ == "__main__":
    main()
