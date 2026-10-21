"""backfill_receive_exact_variant_meaning_20260810.py — ONE-OFF: give 8 pre-existing (not from
today's `receive` onboarding — created 2026-07-21/22/25, already registered under other words
before `receive` also picked them up via raw.discover) Strong's codes their own exact-variant
`strong_meaning_tree`/`strong_meaning_parsed` row, where until now only the shared BASE lemma's row
existed.

Found while confirming the parse layer for `receive`'s new codes (researcher: "confirm the parse
tables have all been generated for the new strongs") — checking coverage across all 64 `receive`
codes turned up 8 with zero `strong_meaning_parsed`, all pre-dating today: `H0935G`, `H3947G`,
`H5375H`, `H5375Q`, `H5414G`, `H7999A`, `H8085G`, `H8085L`. Same class of gap as `healing`'s 8
(BUILD.md sec93, `migration/backfill_healing_exact_variant_meaning_20260810.py`) — reuses that
script's exact mechanism (`raw.write_tree_rows` + `handlers.lexicon.rebuild_parsed_tables`), same
writers (`call2_getInfo`, `lexicon.parse`), no new write grant needed.

    python -m iba.app.migration.backfill_receive_exact_variant_meaning_20260810 --dry-run
    python -m iba.app.migration.backfill_receive_exact_variant_meaning_20260810
"""

from __future__ import annotations

import argparse
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.stepapi import Step, StepUnavailable
from ..lib.versespanmeaningreport import _base
from ..handlers.base import Ctx
from ..handlers import raw
from ..handlers.lexicon import rebuild_parsed_tables

CODES = ["H0935G", "H3947G", "H5375H", "H5375Q", "H5414G", "H7999A", "H8085G", "H8085L"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)

    missing = [c for c in CODES if not cfg.conn.execute(
        "SELECT 1 FROM strong_meaning_tree WHERE strong_variant=? AND deleted=0", (c,)).fetchone()]
    print(f"{len(CODES)} target codes; {len(missing)} still missing their own exact-variant "
         f"strong_meaning_tree row: {missing}")

    if a.dry_run:
        print("--dry-run: no changes made.")
        db.close(); cfg.close()
        return 0
    if not missing:
        print("nothing to do.")
        db.close(); cfg.close()
        return 0

    try:
        step = Step(cfg)
        step.up()
    except StepUnavailable as e:
        print(f"STEP not reachable — cannot backfill: {e}", file=sys.stderr)
        db.close(); cfg.close()
        return 1

    ctx = Ctx(db=db, cfg=cfg, step=step,
             run_id="MIGRATION-backfill-receive-exact-variant-meaning",
             word="", word_id=None, params={})
    c = {"tree": 0}
    written = 0
    for code in missing:
        v = (step.call2_getInfo(code).get("vocabInfos") or [None])[0]
        if not v:
            print(f"  {code}: STEP returned no vocabInfo — skipped")
            continue
        resolved = v.get("strongNumber", code)
        _, tree = raw._split_def(ctx, v.get("mediumDef", ""))
        if not tree:
            print(f"  {code}: no mediumDef tree text to parse — skipped")
            continue
        lemma = _base(resolved)
        raw.write_tree_rows(ctx, lemma, resolved, tree, c)
        written += 1
        print(f"  {code}: wrote its own exact-variant tree ({c['tree']} sense rows so far)")
    db.conn.commit()
    print(f"backfilled {written}/{len(missing)} code(s), {c['tree']} strong_meaning_tree row(s) "
         f"total")

    counts = rebuild_parsed_tables(Ctx(db=db, cfg=cfg, step=None,
                                       run_id="MIGRATION-backfill-receive-exact-variant-meaning",
                                       word="", word_id=None, params={}))
    print(f"parsed layer rebuilt: {counts['strong_meaning_parsed']} strong_meaning_parsed row(s)")

    remaining = [c for c in CODES if not cfg.conn.execute(
        "SELECT 1 FROM strong_meaning_parsed WHERE strong_variant=? AND deleted=0", (c,)).fetchone()]
    db.close()
    cfg.close()
    print(f"\nremaining without their own exact-variant strong_meaning_parsed row: "
         f"{len(remaining)}" + (f" — {remaining}" if remaining else ""))
    return 0 if not remaining else 1


if __name__ == "__main__":
    sys.exit(main())
