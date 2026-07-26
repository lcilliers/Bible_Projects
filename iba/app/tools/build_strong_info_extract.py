"""
Exploratory data-prep extract (not wired into the app or DB pipeline).

Reads the `strong` table - populated by the app's raw.detail step (CALL 2
getInfo per strong -> strong + sense + tree + lexicon) but never previously
pulled into any exploratory extract alongside strong_lexicon/strong_
meaning_tree. Confirmed fully populated: 3463/3463 rows have accentedUnicode/
stepGloss/stepTransliteration/count, 3451/3463 have freqList.

strongNumber is already the exact full Strong's code (variant letter
included where one exists - e.g. "G4151G"), matching strong_lexicon's key
exactly for Greek (1506/1506 identical set) and extending further for
Hebrew: 1957 rows covering all 1693 strong_meaning_tree base lemmas plus
their sub-entries, which strong_meaning_tree itself collapses away and
strong_lexicon has no Hebrew coverage for at all. Split into strong (base)
+ strong_variant via lexicon_split_common.py's split_strong_variant(), same
convention as the other three extract scripts.

Output columns:
  - strong, strong_variant: as elsewhere.
  - accented_unicode: the term's native Greek/Hebrew script form.
  - step_gloss: STEP's own short canonical gloss (distinct from Mounce's).
  - step_transliteration: phonetic transliteration.
  - count: total occurrence count in the tagged Bible version.
  - freq_list: STEP's raw per-passage frequency string, unparsed.
  - language: "Greek" or "Hebrew".

Usage:
    python build_strong_info_extract.py [--db PATH] [--out PATH]
"""
import argparse
import csv
import sqlite3

from lexicon_split_common import split_strong_variant

DEFAULT_DB = r"C:/Bible_study_projects/iba/app/db/iba.db"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/strong-info-iba-20260725.csv"


def build_rows(conn):
    cur = conn.cursor()
    cur.execute(
        "select strongNumber, accentedUnicode, stepGloss, stepTransliteration, count, freqList, language "
        "from strong order by strongNumber"
    )
    rows = []
    for strong_number, accented, gloss, translit, count, freq_list, language in cur.fetchall():
        base, variant = split_strong_variant(strong_number)
        rows.append((base, variant, accented or "", gloss or "", translit or "", count, freq_list or "", language or ""))
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
        writer.writerow(["strong", "strong_variant", "accented_unicode", "step_gloss", "step_transliteration", "count", "freq_list", "language"])
        writer.writerows(rows)

    print("rows:", len(rows))
    print("path:", args.out)


if __name__ == "__main__":
    main()
