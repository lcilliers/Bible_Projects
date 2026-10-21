"""Backfill every live `strong` code's own exact-variant `strong_meaning_tree` row where STEP
actually has content for it -- escalation #1655, researcher instruction, verbatim, 2026-09-10:
"every strong code must agree with span (at the same grain as span, therefore variant level...)
every parse must support the strong table code... fix the code, and rerun the entire parse."

This is the BROADENED continuation of `fix_strong_meaning_tree_collapse.py` (2026-07-26). That
migration fixed the write-guard bug (a sibling's own tree text used to be silently discarded if
ANY row already existed for the base lemma) but deliberately narrowed its own backfill to
"genuine collapse" siblings only (a stepGloss-vocabulary-overlap heuristic), on the stated
assumption that same-root stem-split siblings would "just re-store the identical text the
base-fallback already serves." Checked live, corpus-wide, before writing anything here: FALSE for
the overwhelming majority of what that narrowing excluded -- of 522 live strong codes with no
exact-variant tree row, 519 return real, STEP-confirmed tree content when queried directly by
their own exact code (only 3 -- H0430H/H1121A/H5945H -- have genuinely empty mediumDef).

Uses the exact same repair mechanism as the 2026-07-26 migration (`handlers/raw.py:
write_tree_rows`, `_split_def`) -- not new logic, just applied to its full, correct scope instead
of a narrowed subset. Safe to re-run: the guard is keyed on the exact (lemma_key, strong_variant)
pair, so an already-backfilled code is skipped, never duplicated or overwritten.

Rebuilds the parsed layer once at the end (lexicon.parse), matching every other raw-layer
migration/backfill in this codebase.

    python -m iba.app.migration.backfill_all_strong_meaning_tree_gaps_v1_20260910 --dry-run
    python -m iba.app.migration.backfill_all_strong_meaning_tree_gaps_v1_20260910
"""

from __future__ import annotations

import argparse
import re
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.stepapi import Step, StepUnavailable
from ..handlers.base import Ctx
from ..handlers import raw
from ..handlers.lexicon import rebuild_parsed_tables

_BASE_RE = re.compile(r"^([HG]\d+)([A-Z]*)$")


def _base(code: str) -> str:
    m = _BASE_RE.match(code)
    return m.group(1) if m else code


def find_gap_codes(conn) -> list[str]:
    live = [r[0] for r in conn.execute("SELECT strongNumber FROM strong WHERE deleted=0")]
    have_tree = {r[0] for r in conn.execute(
        "SELECT DISTINCT strong_variant FROM strong_meaning_tree WHERE deleted=0")}
    return sorted(c for c in live if c not in have_tree)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)

    gap_codes = find_gap_codes(cfg.conn)
    print(f"{len(gap_codes)} live strong code(s) with no exact-variant strong_meaning_tree row")

    try:
        step = Step(cfg)
        step.up()
    except StepUnavailable as e:
        print(f"STEP is not reachable — cannot proceed: {e}")
        cfg.close()
        return 1

    ctx = Ctx(db=db, cfg=cfg, step=step,
             run_id="MIGRATION-backfill-all-strong-meaning-tree-gaps",
             word="", word_id=None, params={})

    written = []
    step_empty = []
    errors = []
    c = {"tree": 0}

    for i, code in enumerate(gap_codes):
        if i % 50 == 0:
            print(f"...{i}/{len(gap_codes)}", file=sys.stderr)
        try:
            v = (step.call2_getInfo(code).get("vocabInfos") or [None])[0]
        except Exception as e:
            errors.append((code, str(e)))
            continue
        if not v:
            step_empty.append(code)
            continue
        resolved = v.get("strongNumber", code)
        _, tree = raw._split_def(ctx, v.get("mediumDef", ""))
        if not tree:
            step_empty.append(code)
            continue
        lemma = _base(resolved)
        if ctx.db.get("strong_meaning_tree", lemma_key=lemma, strong_variant=resolved):
            continue  # already backfilled (re-run)
        if a.dry_run:
            written.append(code)
            continue
        raw.write_tree_rows(ctx, lemma, resolved, tree, c)
        written.append(code)

    print(f"\nbackfilled: {len(written)}/{len(gap_codes)} code(s) now have their own "
         f"strong_meaning_tree row ({c['tree']} sense row(s) written)")
    print(f"confirmed STEP-empty (no data at variant grain, not a bug): {len(step_empty)}"
         + (f" — {step_empty}" if step_empty else ""))
    if errors:
        print(f"errors: {len(errors)} — {errors}")

    if a.dry_run:
        print("\n--dry-run: no changes made. Re-run without --dry-run to apply.")
        cfg.close()
        return 0

    db.conn.commit()

    counts = rebuild_parsed_tables(Ctx(db=db, cfg=cfg, step=None,
                                       run_id="MIGRATION-backfill-all-strong-meaning-tree-gaps",
                                       word="", word_id=None, params={}))
    print(f"parsed layer rebuilt: {counts['strong_meaning_parsed']} strong_meaning_parsed row(s)")

    remaining = find_gap_codes(cfg.conn)
    print(f"\nremaining strong code(s) with no exact-variant tree row: {len(remaining)}"
         + (f" — {remaining}" if len(remaining) <= 20 else f" (first 20: {remaining[:20]})"))

    db.close()
    cfg.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
