"""backfill_healing_exact_variant_meaning_20260810.py — ONE-OFF: give 8 of `healing`'s (id 184)
curated Strong's codes their own exact-variant `strong_meaning_tree`/`strong_meaning_parsed` row,
where until now only the shared BASE lemma's row existed.

Found auditing all 44 `healing` codes across every meaning/lexical table (researcher: "take these
new strongs into all the meaning tables"): `strong`/`span`/`verse_lexical` are complete for all 44
(confirmed live — the whole-Bible `lexical.build` pass already covers every one; two apparent
"NO-SPAN" cases, H1455/H8644, are combined-tag spans a plain `strong_variant` string match misses,
not real gaps — `verse_lexical` already carries them correctly). `strong_meaning_tree`/
`strong_meaning_parsed` are the one real gap: 8 sub-lettered codes have NEVER had their own
call2_getInfo pulled — only their base lemma's shared entry exists (`H7965` for all six `H7965G-L`
"peace" sub-senses, `H5414` for `H5414P` "to give: do", `H2492` for `H2492A` "be healthy").

This is the SAME class of gap `migration/fix_strong_meaning_tree_collapse.py` (2026-07-26,
BUILD.md sec24/sec25) built the fix for and reuses its exact mechanism (`raw.write_tree_rows` +
`handlers.lexicon.rebuild_parsed_tables`) — but that script only backfills codes its own
"genuine collapse" detector flags (sibling's stepGloss shares NO vocabulary with the base tree —
e.g. H3581A "reptile" vs H3581B "strength"). These 8 codes are same-root stem/sense-splits, not
homonym collapses (H7965I "peace: well-being" DOES share vocabulary with base H7965's own tree
text — "welfare, health, prosperity" is right there) — that script's own documented policy
deliberately does NOT re-fetch this class, on the reasoning that the base-fallback already serves
equivalent content with no real data loss. Overridden here on the researcher's direct instruction
for this specific curated set — `healing` is a small, hand-picked list where per-sense exactness
matters more than the general 362/470-codes-not-worth-a-live-call economy that policy was built
around.

`detail_one` itself is a no-op for all 8 (`if ctx.db.get("strong", strongNumber=code): skip` —
every one already has a `strong` row from the bulk dictionary import) — `write_tree_rows` bypasses
that guard entirely, matching `fix_strong_meaning_tree_collapse.py`'s own approach exactly.

    python -m iba.app.migration.backfill_healing_exact_variant_meaning_20260810 --dry-run
    python -m iba.app.migration.backfill_healing_exact_variant_meaning_20260810
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

CODES = ["H7965G", "H7965H", "H7965I", "H7965J", "H7965K", "H7965L", "H2492A", "H5414P"]


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
             run_id="MIGRATION-backfill-healing-exact-variant-meaning",
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
                                       run_id="MIGRATION-backfill-healing-exact-variant-meaning",
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
