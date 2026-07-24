"""_check_missing_strongs_in_step.py — read-only diagnostic, not wired into
the app or DB pipeline.

Takes the distinct `strong` values from term-list-words-missing-from-span-
iba-20260724.csv (Strong's numbers with lexicon term-list coverage but no
occurrence anywhere in `span` - a possible "missing verse" signal, per
build_span_term_reconciliation.py) and asks STEP directly, via the same
governed client the app uses (lib.stepapi.Step.call3_strong), whether STEP
itself has any verses for that Strong's number at all.

This distinguishes two different reasons a strong could be absent from
`span`:
  - STEP has zero verses for it: the strong itself is thin/unused in this
    STEP module (or a bad/obsolete code) - `span` being empty is expected,
    not a loading gap.
  - STEP has verses for it: `span` should have rows for those verses but
    doesn't - a genuine loading gap (the verses containing this strong were
    not built into `span`), worth following up.

Read-only: only call3_strong (a GET) is used, no writes anywhere.

Usage:
    python -m iba.app.tools._check_missing_strongs_in_step [--input PATH] [--out PATH]
"""
from __future__ import annotations

import argparse
import csv
import time

from ..lib.cfg import Cfg
from ..lib.stepapi import Step, StepUnavailable

DEFAULT_INPUT = r"C:/Bible_study_projects/outputs/csv/term-list-words-missing-from-span-iba-20260724.csv"
DEFAULT_OUT = r"C:/Bible_study_projects/outputs/csv/missing-strongs-step-verse-check-iba-20260724.csv"


def load_distinct_strongs(path: str) -> list[str]:
    seen: dict[str, None] = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            seen.setdefault(row["strong"], None)
    return list(seen)


def check_strongs(step: Step, strongs: list[str]) -> list[tuple[str, int, str]]:
    """Returns [(strong, step_verse_count, status), ...].
    status is "ok" or an error message from a failed call."""
    rows = []
    for i, strong in enumerate(strongs, 1):
        try:
            total, _ = step.call3_strong(strong)
            rows.append((strong, total, "ok"))
        except Exception as e:  # STEP can 4xx/5xx on an unrecognized code
            rows.append((strong, -1, f"{type(e).__name__}: {e}"))
        if i % 25 == 0 or i == len(strongs):
            print(f"  checked {i}/{len(strongs)}")
        time.sleep(0.02)  # be a polite local-server citizen, not a hammer
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default=DEFAULT_INPUT)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    strongs = load_distinct_strongs(args.input)
    print(f"distinct strongs to check: {len(strongs)}")

    cfg = Cfg()
    step = Step(cfg)
    try:
        ev = step.up()
        print(f"STEP up: {ev['base']} {ev['version']}, probe {ev['probe']} -> {ev['verses']} verses")
    except StepUnavailable as e:
        print(f"STEP not available: {e}")
        return 1

    rows = check_strongs(step, strongs)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["strong", "step_verse_count", "status"])
        writer.writerows(rows)

    zero = sum(1 for _, n, s in rows if s == "ok" and n == 0)
    has_verses = sum(1 for _, n, s in rows if s == "ok" and n > 0)
    errors = sum(1 for _, n, s in rows if s != "ok")
    print(f"zero verses in STEP: {zero}")
    print(f"has verses in STEP (span loading gap): {has_verses}")
    print(f"errors: {errors}")
    print(f"-> {args.out}")


if __name__ == "__main__":
    main()
