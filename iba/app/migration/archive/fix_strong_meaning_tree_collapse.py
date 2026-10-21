"""fix_strong_meaning_tree_collapse.py — ONE-OFF + structural fix: strong_meaning_tree gains
`strong_variant`, closing the base-collapse root cause BUILD.md sec19/sec20/sec24 all named but
none of them fixed (sec24's own words: "not a schema fix... strong_meaning_tree's own
base-collapse root cause is unchanged"). Researcher's direct instruction 2026-07-26: "fix it
properly" (answering the open item left in the prior session log).

The bug (confirmed live via H3581A/H3581B, BUILD.md sec19/sec24): `handlers/raw.py:detail_one`
fetches call2_getInfo PER EXACT resolved code every time — the response tree text IS already
code-specific by the time it's in hand. But the old WRITE guard was `if tree and not
ctx.db.get("strong_meaning_tree", lemma_key=lemma):` — keyed on the BASE alone. Whichever sibling
code got detailed FIRST silently claimed the one base row; every OTHER sibling's own (already
correctly fetched) tree text was discarded, not written anywhere. For same-root stem-splits
(H0935G Qal "come" / H0935P Hiphil "bring", 362/470 = 77% of sub-lettered codes with a sibling)
this is harmless — STEP returns one shared, already stem-labeled combined entry for the whole
family, so the discarded copy would have said the same thing anyway. For genuine homonym collapses
(108/470 = 23%, e.g. H3581A "reptile" vs H3581B "strength" — zero vocabulary overlap) it is real,
silent data loss: the sibling's OWN correct sense was fetched from STEP and then thrown away.

Fix, in three parts (mirrors migration/add_candidate_seed_strong_variant.py's precedent exactly —
same shape of gap, same fix):

  1. PHYSICAL: add `strong_variant` to strong_meaning_tree AND strong_meaning_parsed (the parsed
     table derives 1:1 from the tree and is fully rebuilt by lexicon.parse every run, so it needs
     the same column to carry the same fact through to readers). No UNIQUE constraint exists on
     either table today (dedup is a manual application-level guard, same as every other raw.py
     write — confirmed live, no cfg_unique row for strong_meaning_tree or any strong-family raw
     table) so — unlike candidate_seed's own migration — this is a plain ADD COLUMN, no table
     rebuild needed. Existing rows default to `strong_variant = lemma_key` (the "applies to
     whole/unsplit base" convention, identical to candidate_seed.strong_variant's own default rule)
     since which sibling ORIGINALLY produced a pre-fix row is not recoverable from the data as it
     stands.
  2. CODE (companion changes, same session, not duplicated here): handlers/raw.py's write guard now
     keys on (lemma_key, strong_variant=resolved) instead of lemma_key alone; lib/lexiconparse.py +
     handlers/lexicon.py carry strong_variant through the parse rebuild; lib/versespanmeaningreport.
     py + tools/build_verse_span_meaning_extract.py's readers prefer an exact strong_variant match,
     falling back to the base/unsplit row — matching candidate_seed.set()'s own "prefers an exact
     strong_variant match, falling back to the base row" precedent (GOVERNANCE.md sec10).
  3. BACKFILL (this script, live-detected, not a fixed list — same discipline as
     migration/repair_strong_sense_head.py): every sub-lettered strong with a sibling whose OWN
     stepGloss shares NO vocabulary with the shared/base tree text (lib.versespanmeaningreport.
     gloss_supported_by_tree — the exact same signal the report itself already uses to flag
     [AMBIGUOUS]) is a genuine collapse. For each, live-refetch call2_getInfo(code) (STEP required)
     and write ITS OWN strong_meaning_tree row under (lemma_key, strong_variant=code) via
     handlers/raw.py:write_tree_rows — without touching the existing base/unsplit row, which stays
     as the correct fallback for any sibling this pass does NOT touch. The 362/470 same-root
     stem-split majority is deliberately NOT re-fetched here — no data was lost for those, and
     re-fetching them would just re-store the identical text the base-fallback already serves, at
     the cost of 362 needless live STEP calls.

Then rebuilds the parsed layer once at the end (equivalent to lexicon.parse) so
strong_meaning_parsed reflects both the new column and the backfilled rows immediately, without a
separate manual step.

    python -m iba.app.migration.fix_strong_meaning_tree_collapse --dry-run
    python -m iba.app.migration.fix_strong_meaning_tree_collapse
"""

from __future__ import annotations

import argparse
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.stepapi import Step, StepUnavailable
from ..lib.versespanmeaningreport import BASE_RE, _base, gloss_supported_by_tree, sibling_variant_codes
from ..handlers.base import Ctx
from ..handlers import raw
from ..handlers.lexicon import rebuild_parsed_tables


def _ensure_column(conn, table: str, column: str) -> bool:
    cols = {r[1] for r in conn.execute(f"PRAGMA table_info({table})")}
    if column in cols:
        return False
    conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} TEXT")
    conn.execute(f"UPDATE {table} SET {column} = lemma_key WHERE {column} IS NULL")
    return True


def _lemma_meaning_text(conn, lemma_key: str) -> str:
    rows = conn.execute(
        "SELECT gloss FROM strong_meaning_parsed WHERE lemma_key=? ORDER BY sort, id",
        (lemma_key,)).fetchall()
    return "; ".join(r[0] for r in rows if r[0])


def _detect_genuine_collapses(conn) -> list[str]:
    codes = [r[0] for r in conn.execute(
        "SELECT strongNumber FROM strong WHERE deleted=0 ORDER BY strongNumber")]
    out = []
    for code in codes:
        m = BASE_RE.match(code)
        if not m or not m.group(2):
            continue  # only sub-lettered codes can be affected
        base = _base(code)
        siblings = sibling_variant_codes(conn, base, exclude=code)
        if not siblings:
            continue
        gloss = conn.execute(
            "SELECT stepGloss FROM strong WHERE strongNumber=?", (code,)).fetchone()[0]
        tree_text = _lemma_meaning_text(conn, base)
        if tree_text and not gloss_supported_by_tree(gloss, tree_text):
            out.append(code)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)

    added_tree = "strong_variant" not in {r[1] for r in cfg.conn.execute(
        "PRAGMA table_info(strong_meaning_tree)")}
    added_parsed = "strong_variant" not in {r[1] for r in cfg.conn.execute(
        "PRAGMA table_info(strong_meaning_parsed)")}

    genuine = _detect_genuine_collapses(cfg.conn)
    print(f"strong_meaning_tree.strong_variant: {'to add' if added_tree else 'already present'}")
    print(f"strong_meaning_parsed.strong_variant: {'to add' if added_parsed else 'already present'}")
    print(f"{len(genuine)} genuinely-collapsed sub-lettered code(s) detected live "
         f"(sibling exists, own stepGloss shares no vocabulary with the shared tree): "
         + (", ".join(genuine) if genuine else "(none)"))

    if a.dry_run:
        print("\n--dry-run: no changes made. Re-run without --dry-run to apply.")
        cfg.close()
        return 0

    _ensure_column(db.conn, "strong_meaning_tree", "strong_variant")
    _ensure_column(db.conn, "strong_meaning_parsed", "strong_variant")
    db.conn.commit()
    print("schema: strong_variant column present on both tables, "
         "existing rows defaulted to strong_variant = lemma_key")

    if genuine:
        try:
            step = Step(cfg)
            step.up()
        except StepUnavailable as e:
            print(f"\nSTEP is not reachable — cannot backfill the {len(genuine)} genuine "
                 f"collapse(s): {e}")
            db.close(); cfg.close()
            return 1
        ctx = Ctx(db=db, cfg=cfg, step=step, run_id="MIGRATION-fix-strong-meaning-tree-collapse",
                 word="", word_id=None, params={})
        c = {"tree": 0}
        written = 0
        for code in genuine:
            v = (step.call2_getInfo(code).get("vocabInfos") or [None])[0]
            if not v:
                continue
            resolved = v.get("strongNumber", code)
            _, tree = raw._split_def(ctx, v.get("mediumDef", ""))
            if not tree:
                continue
            lemma = _base(resolved)
            if ctx.db.get("strong_meaning_tree", lemma_key=lemma, strong_variant=resolved):
                continue  # already has its own row (e.g. re-run after a partial prior pass)
            raw.write_tree_rows(ctx, lemma, resolved, tree, c)
            written += 1
        db.conn.commit()
        print(f"backfilled: {written}/{len(genuine)} genuine collapse(s) now have their own "
             f"strong_meaning_tree row ({c['tree']} sense row(s) written)")

    counts = rebuild_parsed_tables(Ctx(db=db, cfg=cfg, step=None, run_id="MIGRATION-fix-strong-meaning-tree-collapse",
                                       word="", word_id=None, params={}))
    print(f"parsed layer rebuilt: {counts['strong_meaning_parsed']} strong_meaning_parsed row(s)")

    # Precise check: does every detected genuine collapse now have its OWN exact-variant tree
    # row? (Not re-running _detect_genuine_collapses — after backfill its lemma_key-pooled text
    # includes the new row too, which would mask exactly the thing being verified here.)
    remaining = [c for c in genuine if not cfg.conn.execute(
        "SELECT 1 FROM strong_meaning_tree WHERE strong_variant=? AND deleted=0", (c,)).fetchone()]
    db.close()
    cfg.close()
    print(f"\nremaining genuinely-collapsed code(s) with no exact-variant row of their own: "
         f"{len(remaining)}" + (f" — {remaining}" if remaining else ""))
    return 0 if not remaining else 1


if __name__ == "__main__":
    sys.exit(main())
