"""_check_ib_related_span_step_coverage.py — read-only diagnostic, not
wired into the app or DB pipeline.

Takes the distinct Strong's numbers behind the "IB related" rows in
span-words-missing-from-term-list-iba-20260724.csv (per build_span_term_
reconciliation.py: words that DO occur in our loaded `span`/`verse` data,
but whose Strong's number has no lexicon coverage at all - 281 rows, 235
distinct strongs). For each, asks STEP directly (the same governed client
the app uses, lib.stepapi.Step.call3_strong) how many verses it has total,
and compares against how many DISTINCT verses we've already loaded locally
under that EXACT strong_variant (not base-stripped - sub-entry variants like
"H3068G" are genuinely distinct forms STEP itself tracks separately, see
local_verse_count()'s docstring). The difference is a preliminary sizing of
the pull still needed for full local coverage of these already-identified
IB-relevant strongs - it does not itself pull anything.

Read-only: only call3_strong (a GET) is used, no writes anywhere.

Usage:
    python -m iba.app.tools._check_ib_related_span_step_coverage [--input PATH] [--out PATH]
"""
from __future__ import annotations

import argparse
import csv
import time

from ..lib.cfg import Cfg
from ..lib.stepapi import Step, StepUnavailable

DEFAULT_INPUT = r"C:/Bible_study_projects/outputs/csv/span-words-missing-from-term-list-iba-20260724.csv"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/ib-related-span-step-coverage-iba-20260724.csv"

def load_distinct_strongs(path: str) -> list[str]:
    seen: dict[str, None] = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["ib_relevance"] == "IB related":
                seen.setdefault(row["strong"], None)
    return list(seen)


def local_verse_count(cfg: Cfg, strong: str) -> int:
    """Distinct local verse_id count for this EXACT strong_variant (not
    base-stripped) - sub-entry variants (e.g. "H3068G" vs plain "H3068")
    are genuinely distinct forms STEP itself tracks separately, confirmed
    by spot-checking H3068: STEP's own total for "H3068G" specifically
    (5521) lines up with our local "H3068G"-only count (5457), not the
    combined H3068-family total (5459) - comparing STEP's per-variant total
    against a base-aggregated local count produces a nonsensical negative
    gap."""
    cur = cfg.conn.cursor()
    cur.execute(
        "select count(distinct verse_id) from span where strong_variant = ? and deleted = 0",
        (strong,),
    )
    return cur.fetchone()[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default=DEFAULT_INPUT)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    strongs = load_distinct_strongs(args.input)
    print(f"distinct IB-related strongs: {len(strongs)}")

    cfg = Cfg()
    step = Step(cfg)
    try:
        ev = step.up()
        print(f"STEP up: {ev['base']} {ev['version']}")
    except StepUnavailable as e:
        print(f"STEP not available: {e}")
        return 1

    rows = []
    for i, strong in enumerate(strongs, 1):
        local = local_verse_count(cfg, strong)
        try:
            total, _ = step.call3_strong(strong)
            gap = total - local
            rows.append((strong, total, local, gap, "ok"))
        except Exception as e:
            rows.append((strong, -1, local, -1, f"{type(e).__name__}: {e}"))
        if i % 25 == 0 or i == len(strongs):
            print(f"  checked {i}/{len(strongs)}")
        time.sleep(0.02)

    rows.sort(key=lambda r: -r[3])

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["strong", "step_total_verses", "local_verse_count", "gap", "status"])
        writer.writerows(rows)

    ok_rows = [r for r in rows if r[4] == "ok"]
    total_gap = sum(r[3] for r in ok_rows)
    already_complete = sum(1 for r in ok_rows if r[3] <= 0)
    print(f"strongs already fully covered locally (gap <= 0): {already_complete}/{len(ok_rows)}")
    print(f"total verse-gap across all strongs: {total_gap}")
    print(f"-> {args.out}")


if __name__ == "__main__":
    main()
