"""repair_strong_sense_head.py — ONE-OFF: repair the <br>-vs-\\n parser bug, both the levels it hit.

handlers/raw.py:_split_def split a STEP mediumDef on a literal "\\n" after stripping the
meaning.head_marker prefix. For a subset of vocabInfos entries STEP's tree uses literal "<br>" tags
instead of real newlines as its separator. Two distinct failure levels, both from the same root
cause, both fixed by the same code change (handlers/raw.py, 2026-07-21: <br> now normalised to \\n
before any splitting):

  1. HEAD level — no real "\\n" anywhere at all: the WHOLE marker-stripped remainder (head text +
     <br>-joined tree) landed in `strong_sense.head`, and `strong_meaning_tree` was never
     populated for that lemma. Detected via cfg_column.expectation='nohtml' on strong_sense.head.
  2. TREE level (found 2026-07-21, a follow-up question after the head-level fix shipped) — head
     and the first tree line WERE separated by a real "\\n", but the tree's OWN internal lines used
     "<br>" between sub-senses (e.g. "1) ...<br>1a) ...<br>1b) ..."). detail_one's tree-line split
     (`tree.split("\\n")`) then found nothing to split on, so the entire tree landed in ONE
     strong_meaning_tree row, <br> tags and all. Detected via
     cfg_column.expectation='pattern:raw.meaning_tree_clean_pattern' on
     strong_meaning_tree.sense_text (a <ref>-tolerant pattern — STEP's own citation markup in
     Greek prose entries, BUILD.md sec7, is a DIFFERENT, accepted, already-documented limitation,
     not this bug, and must not be flagged).

Identifies both affected sets FROM THE LIVE DATA (the two expectations above), not a fixed list,
so a future re-run after a further STEP refresh would catch any new occurrence of either shape.
For each affected LEMMA_KEY (the union of both sets' lemmas):
  1. delete strong/strong_sense rows for EVERY strong sharing that lemma_key (not just the one
     that showed the symptom — the tree is shared and written once, so a full clean rebuild needs
     every variant re-fetched through the fixed parser),
  2. delete strong_meaning_tree rows for the lemma_key,
  3. re-run raw.detail_one for every one of those strongs, which re-fetches call2_getInfo through
     the now-fixed _split_def.

Read-only dry-run first, then live, per this app's existing --dry-run convention:

    python -m iba.app.migration.repair_strong_sense_head --dry-run
    python -m iba.app.migration.repair_strong_sense_head
"""

from __future__ import annotations

import argparse
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.stepapi import Step
from ..lib import valuequality as vq
from ..handlers.base import Ctx
from ..handlers import raw


def _head_violations(cfg: Cfg) -> list[str]:
    return [r[0] for r in cfg.conn.execute(
        "SELECT strong FROM strong_sense WHERE head LIKE '%<%' AND deleted=0")]


def _tree_violation_lemmas(cfg: Cfg) -> list[str]:
    f = vq.scan_column(cfg, "strong_meaning_tree", "sense_text", "pattern:raw.meaning_tree_clean_pattern")
    if not f.violations:
        return []
    import re
    pattern = re.compile(cfg.setting("raw.meaning_tree_clean_pattern"))
    rows = cfg.conn.execute("SELECT DISTINCT lemma_key, sense_text FROM strong_meaning_tree").fetchall()
    return sorted({r[0] for r in rows if not pattern.match(r[1] or "")})


def _strongs_for_lemmas(cfg: Cfg, lemma_keys: set[str]) -> list[str]:
    if not lemma_keys:
        return []
    all_strongs = [r[0] for r in cfg.conn.execute("SELECT strongNumber FROM strong")]
    return sorted(s for s in all_strongs if raw._base(s) in lemma_keys)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)

    head_bad = _head_violations(cfg)
    tree_bad_lemmas = _tree_violation_lemmas(cfg)
    lemma_keys = {raw._base(s) for s in head_bad} | set(tree_bad_lemmas)
    if not lemma_keys:
        print("no strong_sense.head or strong_meaning_tree.sense_text violations — nothing to repair")
        cfg.close()
        return 0

    strongs = _strongs_for_lemmas(cfg, lemma_keys)
    print(f"{len(head_bad)} head-level violation(s), {len(tree_bad_lemmas)} tree-level lemma(s) "
         f"-> {len(lemma_keys)} affected lemma_key(s), {len(strongs)} strong(s) to re-fetch:")
    print("  " + ", ".join(strongs[:20]) + (" ..." if len(strongs) > 20 else ""))

    if a.dry_run:
        print("\n--dry-run: no changes made. Re-run without --dry-run to apply.")
        cfg.close()
        return 0

    for code in strongs:
        db.conn.execute("DELETE FROM strong_sense WHERE strong=?", (code,))
        db.conn.execute("DELETE FROM strong WHERE strongNumber=?", (code,))
    for lk in lemma_keys:
        db.conn.execute("DELETE FROM strong_meaning_tree WHERE lemma_key=?", (lk,))
    db.conn.commit()
    print(f"deleted {len(strongs)} strong/strong_sense row(s), "
          f"strong_meaning_tree for {len(lemma_keys)} lemma_key(s)")

    step = Step(cfg)
    ctx = Ctx(db=db, cfg=cfg, step=step, run_id="MIGRATION-repair-strong-sense-head",
             word="", word_id=None, params={})
    c = {"strong": 0, "sense": 0, "tree": 0, "lexicon": 0, "skipped": 0, "no_vocab": 0}
    for code in strongs:
        raw.detail_one(ctx, code, c)
    db.close()
    cfg.close()

    print(f"re-fetched: {c['strong']} strong, {c['sense']} sense, {c['tree']} tree row(s), "
          f"{c['no_vocab']} no-vocab")

    cfg2 = Cfg()
    remaining_head = _head_violations(cfg2)
    remaining_tree = _tree_violation_lemmas(cfg2)
    cfg2.close()
    print(f"\nremaining: {len(remaining_head)} head violation(s), {len(remaining_tree)} tree lemma(s)" +
         ("" if not (remaining_head or remaining_tree) else f" — {remaining_head + remaining_tree}"))
    return 0 if not (remaining_head or remaining_tree) else 1


if __name__ == "__main__":
    sys.exit(main())
