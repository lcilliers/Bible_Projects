"""build_strong_related_extract.py — exploratory data-prep extract, not
wired into the app or DB pipeline.

STEP's getInfo response (lib.stepapi.Step.call2_getInfo) carries a
`relatedNos` list - cross-references to other Strong's numbers STEP itself
considers related to the one queried (e.g. G4151G "spirit" relates to
G4151H, G4154, G4152, G4153) - each with its own matchingForm/
stepTransliteration/gloss. Checked against iba.db: this is NOT stored
anywhere (no table in the DB has a "related" column at all), unlike
strong_lexicon.lsj/mounce and strong.accentedUnicode/stepGloss/etc, which
ARE already captured. This script closes that gap by asking STEP directly,
per exact full Strong's code (matching the `strong` table's population -
1506 G rows == strong_lexicon exactly, 1957 H rows covering all 1693
strong_meaning_tree Hebrew base lemmas plus their sub-entries - 3463 total).

Deliberately NOT written back into iba.db: unlike strong/strong_lexicon/
strong_meaning_tree, which are populated by the app's governed raw.detail
step (handlers/raw.py, part of the new-word work package), this script
just fetches straight from STEP into a CSV, the same way every other
extract script in this file reads from an already-loaded DB table. Making
this a permanent part of onboarding (so future words get it for free,
with backfill for the 3463 already onboarded) would mean changing
handlers/raw.py and its write grant - a bigger, separate decision than
this exploratory pass.

Read-only against STEP: only call2_getInfo (a GET) is used, no writes to
iba.db anywhere.

Usage:
    python -m iba.app.tools.build_strong_related_extract [--out PATH] [--limit N]
"""
from __future__ import annotations

import argparse
import csv
import sqlite3
import time

from ..lib.cfg import Cfg, DB_PATH
from ..lib.stepapi import Step, StepUnavailable

DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/strong-related-iba-20260725.csv"


def load_strongs(db_path) -> list[str]:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("select strongNumber from strong order by strongNumber")
    return [r[0] for r in cur.fetchall()]


def fetch_related(step: Step, strongs: list[str]) -> list[tuple]:
    """Returns rows: (strong, related_strong, related_form,
    related_transliteration, related_gloss, status). One row per related
    pair; a strong with an empty relatedNos list, or a failed call, still
    gets exactly one row (related_strong="") so every queried strong is
    represented - nothing silently dropped."""
    rows = []
    for i, strong in enumerate(strongs, 1):
        try:
            info = step.call2_getInfo(strong)
            vocabs = info.get("vocabInfos") or []
            related = vocabs[0].get("relatedNos", []) if vocabs else []
            if not related:
                rows.append((strong, "", "", "", "", "ok"))
            else:
                for r in related:
                    rows.append((
                        strong,
                        r.get("strongNumber", ""),
                        r.get("matchingForm", ""),
                        r.get("stepTransliteration", ""),
                        r.get("gloss", ""),
                        "ok",
                    ))
        except Exception as e:  # STEP can 4xx/5xx on an unrecognized code
            rows.append((strong, "", "", "", "", f"{type(e).__name__}: {e}"))
        if i % 100 == 0 or i == len(strongs):
            print(f"  fetched {i}/{len(strongs)}")
        time.sleep(0.02)  # be a polite local-server citizen, not a hammer
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--limit", type=int, default=None, help="cap the number of strongs fetched (debugging)")
    args = ap.parse_args()

    strongs = load_strongs(DB_PATH)
    if args.limit:
        strongs = strongs[: args.limit]
    print(f"strongs to fetch: {len(strongs)}")

    cfg = Cfg()
    step = Step(cfg)
    try:
        ev = step.up()
        print(f"STEP up: {ev['base']} {ev['version']}, probe {ev['probe']} -> {ev['verses']} verses")
    except StepUnavailable as e:
        print(f"STEP not available: {e}")
        return 1

    rows = fetch_related(step, strongs)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["strong", "related_strong", "related_form", "related_transliteration", "related_gloss", "status"])
        writer.writerows(rows)

    errors = sum(1 for r in rows if r[5] != "ok")
    none_related = sum(1 for r in rows if r[5] == "ok" and r[1] == "")
    print(f"rows written: {len(rows)}")
    print(f"strongs with no related numbers: {none_related}")
    print(f"errors: {errors}")
    print(f"-> {args.out}")


if __name__ == "__main__":
    main()
