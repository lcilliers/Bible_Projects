"""apply_semantic_allocation.py — apply an explicit candidate→word mapping (the semantic pass).

Reads a JSON mapping {strong: registry_word | "REJECT" | "NEW"} and, for each uncovered
candidate:
  - registry_word -> add the strong UNDER that word (word_strong) + targeted per-strong raw
    pull (detail_one/verses_one) + set candidate_seed.registry_match.
  - REJECT       -> candidate_seed.decision = 'rejected' (not inner-being; removed from the seed).
  - NEW          -> left as-is (a genuine new-word candidate) and reported.

Same targeted pull as allocate_strongs — the word's other strongs are never re-pulled.

    python -m iba.app.migration.apply_semantic_allocation --map <file.json>          # dry-run
    python -m iba.app.migration.apply_semantic_allocation --map <file.json> --apply
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.stepapi import Step
from ..handlers.base import Ctx
from ..handlers import raw


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--map", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)
    for t in ("word_strong", "candidate_seed"):
        if t not in cfg.may_write("migration"):
            print(f"write-grant violation: 'migration' may not write {t!r}", file=sys.stderr)
            return 1

    mp = json.loads(pathlib.Path(a.map).read_text(encoding="utf-8"))["map"]
    reg = {r["word"]: r["id"] for r in db.rows("SELECT id, word FROM word_registry WHERE deleted=0")}
    # only act on genuinely-uncovered candidates
    uncovered = {r["lemma_key"] for r in db.rows(
        "SELECT lemma_key FROM candidate_seed WHERE decision='candidate' "
        "AND registry_match IS NULL AND deleted=0")}

    to_alloc, to_reject, to_new, bad = {}, [], [], []
    for strong, target in mp.items():
        if strong not in uncovered:
            continue
        if target == "REJECT":
            to_reject.append(strong)
        elif target == "NEW":
            to_new.append(strong)
        elif target in reg:
            to_alloc[strong] = target
        else:
            bad.append((strong, target))

    print(f"mapping: allocate {len(to_alloc)} · reject {len(to_reject)} · new {len(to_new)} "
          f"· unknown-word {len(bad)} · (of {len(uncovered)} uncovered)")
    if bad:
        print("  unknown registry words:", bad[:10])
    if not a.apply:
        byword = collections.Counter(to_alloc.values())
        print("  allocations by word:", dict(byword.most_common(15)))
        db.close(); cfg.close(); return 0

    step = Step(cfg)
    ctx = Ctx(db=db, cfg=cfg, step=step, run_id="SEMANTIC", word="", word_id=None,
              params={}, step_id="allocate")
    cd = {"strong": 0, "sense": 0, "tree": 0, "lexicon": 0, "skipped": 0, "no_vocab": 0}
    cv = {"strong_verse": 0, "verse_new": 0, "span_new": 0, "short": 0}
    done = 0
    for strong, word in to_alloc.items():
        ctx.word, ctx.word_id = word, reg[word]
        db.upsert("word_strong", {"word_id": reg[word], "strong": strong, "deleted": 0})
        raw.detail_one(ctx, strong, cd)
        raw.verses_one(ctx, strong, cv)
        db.update("candidate_seed", {"lemma_key": strong}, registry_match=word)
        done += 1
        if done % 25 == 0:
            db.conn.commit(); print(f"  allocated {done}/{len(to_alloc)} …")
    for strong in to_reject:
        db.update("candidate_seed", {"lemma_key": strong}, decision="rejected")
    db.close()
    cfg.close()
    print(f"applied: {done} allocated (+{cd['strong']} strong, +{cv['strong_verse']} strong_verse, "
          f"+{cv['span_new']} span), {len(to_reject)} rejected, {len(to_new)} left as new-word candidates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
