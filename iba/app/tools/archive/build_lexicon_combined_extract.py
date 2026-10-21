"""
Exploratory data-prep extract (not wired into the app or DB pipeline).

Combines all three lexicon extract scripts into one record per base Strong's
code - JSON, not CSV, because the sources have different row shapes
(meaning-tree rows carry sort/sense_code/verse_refs/note; lsj rows carry
sense_label; mounce rows carry neither), so there's no single flat column
set to hold all three without padding every side with nulls.

  - build_meaning_tree_extract.py (strong_meaning_tree): never carries a
    sub-entry letter - collapses to the base lemma. Placed directly under
    the base record as "meaning" (not nested per-variant, since it never
    varies).
  - build_lsj_sense_extract.py (strong_lexicon.lsj) and
    build_mounce_lexicon_extract.py (strong_lexicon.mounce): both keyed by
    strong_lexicon.strong, which DOES carry a sub-entry letter in 49 of
    1506 rows (e.g. "G4151G" vs "G4151H" - two distinct dictionary entries
    for the same base lemma, each with its own lsj/mounce text).

  - build_strong_info_extract.py (`strong` table): also keyed by the exact
    full code, same as lsj/mounce - and since `strong` covers Hebrew
    sub-entries that strong_lexicon never had (1957 H rows vs 0), wiring it
    in creates "variants" entries for Hebrew codes that previously had
    none at all (lsj/mounce only ever existed for Greek).
  - build_strong_related_extract.py (STEP's relatedNos, fetched live - not
    stored in iba.db at all): read here from its own pre-fetched CSV, not
    re-fetched on every combine run - unlike the other three sources this
    one costs a live network round trip per code (3463 of them), so it's
    fetched once by its own script and cached to disk.

2026-07-25 rework (previous version flagged as confusing): lsj/mounce used
to sit in flat top-level lists with strong_variant as a buried per-item
field - two genuinely different sub-entries (e.g. G4151G and G4151H,
which happen to have near-identical English glosses) read as unexplained
duplicates that way. They're now grouped under "variants", keyed by the
variant letter (or "" for the ~82% of codes with no sub-entry letter at
all), so everything belonging to one specific dictionary entry sits
together, separately from any sibling sub-entry.

Output shape (JSON object keyed by base strong code):
  {
    "G4151": {
      "strong": "G4151",
      "meaning": [ {sort, sense_code, gloss, verse_refs, note, row_type}, ... ],
      "variants": {
        "G": {
          "lsj": [ {sense_label, gloss, note, row_type}, ... ],
          "mounce": [ {mounce_parsed, row_type}, ... ],
          "strong_info": {accented_unicode, step_gloss, step_transliteration, count, freq_list, language} | null,
          "related": [ {related_strong, related_form, related_transliteration, related_gloss}, ... ]
        },
        "H": { ... }
      }
    },
    ...
  }

Usage:
    python build_lexicon_combined_extract.py [--db PATH] [--related-csv PATH] [--out PATH]
"""
import argparse
import csv
import json
import sqlite3

import build_lsj_sense_extract as lsj
import build_meaning_tree_extract as mt
import build_mounce_lexicon_extract as mn
import build_strong_info_extract as si

DEFAULT_DB = r"C:/Bible_study_projects/iba/app/db/iba.db"
DEFAULT_RELATED_CSV = r"C:/Bible_study_projects/outputs/csv/strong-related-iba-20260725.csv"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/json/lexicon-combined-iba-20260725.json"


def get_record(combined, strong):
    return combined.setdefault(strong, {"strong": strong, "meaning": [], "variants": {}})


def get_variant(record, strong_variant):
    return record["variants"].setdefault(
        strong_variant, {"lsj": [], "mounce": [], "strong_info": None, "related": []}
    )


def load_related(path):
    """related_strong is the FULL code as STEP returned it (its own base+
    variant, not necessarily matching the queried strong's variant) - split
    it the same way so a related-number's own sub-entry is visible too."""
    by_full_strong = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row["related_strong"]:
                continue  # "ok" with an empty relatedNos list, or a failed call
            related_base, related_variant = si.split_strong_variant(row["related_strong"])
            by_full_strong.setdefault(row["strong"], []).append({
                "related_strong": related_base,
                "related_strong_variant": related_variant,
                "related_form": row["related_form"],
                "related_transliteration": row["related_transliteration"],
                "related_gloss": row["related_gloss"],
            })
    return by_full_strong


def build_combined(conn, related_csv_path=None):
    combined = {}

    for strong, strong_variant, sort, sense_code, gloss, verse_refs, note, row_type in mt.build_rows(conn):
        rec = get_record(combined, strong)
        rec["meaning"].append({
            "sort": sort,
            "sense_code": sense_code,
            "gloss": gloss,
            "verse_refs": verse_refs,
            "note": note,
            "row_type": row_type,
        })

    for strong, strong_variant, sense_label, gloss, note, row_type in lsj.build_rows(conn):
        rec = get_record(combined, strong)
        get_variant(rec, strong_variant)["lsj"].append({
            "sense_label": sense_label,
            "gloss": gloss,
            "note": note,
            "row_type": row_type,
        })

    for strong, strong_variant, text, row_type in mn.build_rows(conn):
        rec = get_record(combined, strong)
        get_variant(rec, strong_variant)["mounce"].append({
            "mounce_parsed": text,
            "row_type": row_type,
        })

    for strong, strong_variant, accented, step_gloss, translit, count, freq_list, language in si.build_rows(conn):
        rec = get_record(combined, strong)
        get_variant(rec, strong_variant)["strong_info"] = {
            "accented_unicode": accented,
            "step_gloss": step_gloss,
            "step_transliteration": translit,
            "count": count,
            "freq_list": freq_list,
            "language": language,
        }

    if related_csv_path:
        related_by_full = load_related(related_csv_path)
        for full_strong, related_list in related_by_full.items():
            base, variant = si.split_strong_variant(full_strong)
            rec = get_record(combined, base)
            get_variant(rec, variant)["related"] = related_list

    return combined


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--related-csv", default=DEFAULT_RELATED_CSV)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    combined = build_combined(conn, args.related_csv)

    variant_count = sum(len(r["variants"]) for r in combined.values())
    multi_variant = sum(1 for r in combined.values() if len(r["variants"]) > 1)
    with_related = sum(1 for r in combined.values() for v in r["variants"].values() if v["related"])
    with_info = sum(1 for r in combined.values() for v in r["variants"].values() if v["strong_info"])

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)

    print("base strong codes:", len(combined))
    print("total variant entries:", variant_count)
    print("base codes with more than one variant:", multi_variant)
    print("variants with strong_info:", with_info)
    print("variants with related numbers:", with_related)
    print("path:", args.out)


if __name__ == "__main__":
    main()
