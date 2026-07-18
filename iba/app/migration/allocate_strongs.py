"""allocate_strongs.py — ONE-OFF: allocate uncovered candidate strongs to registry words.

For each candidate lemma that cleanly matches exactly one registry word (by its curated
synonym / word-stem), this:
  1. adds the strong UNDER that registry word (word_strong link), and
  2. pulls the raw layer for JUST that strong — call2 (meaning) if not already held, and
     call3 (its verses/spans) — via raw.detail_one / raw.verses_one. The word's OTHER
     strongs are NOT re-pulled.
  3. sets candidate_seed.registry_match (resolving the double-control; the record of the
     allocation, so it is auditable and reversible).

Ambiguous (multi-match) and no-match candidates are left for the semantic pass.

    python -m iba.app.migration.allocate_strongs           # dry-run: show the plan
    python -m iba.app.migration.allocate_strongs --apply    # do it
"""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.stepapi import Step
from ..handlers.base import Ctx
from ..handlers import raw

REPO = pathlib.Path(__file__).resolve().parents[3]
SYNONYMS = REPO / "research/discovery/registry-synonyms-curated-20260707.json"


def _tok(s: str) -> list[str]:
    return [w for w in re.findall(r"[a-z]+", (s or "").lower()) if len(w) > 2]


def _match(gt: list[str], tset: set) -> bool:
    for a in gt:
        for b in tset:
            if a == b or (min(len(a), len(b)) >= 4 and (a.startswith(b) or b.startswith(a))):
                return True
    return False


def clean_allocations(db: Db) -> list[tuple[str, str]]:
    """(lemma_key, registry_word) for candidates matching EXACTLY ONE registry word."""
    reg = [r["word"] for r in db.rows("SELECT word FROM word_registry WHERE deleted=0")]
    syn = json.loads(SYNONYMS.read_text(encoding="utf-8")).get("synonyms", {})
    terms = {}
    for w in reg:
        t = set(_tok(w))
        for s in syn.get(w, []):
            t |= set(_tok(s))
        terms[w] = t
    out = []
    for r in db.rows("SELECT cs.lemma_key, li.gloss FROM candidate_seed cs "
                     "JOIN lemma_inventory li ON li.lemma_key=cs.lemma_key "
                     "WHERE cs.decision='candidate' AND cs.registry_match IS NULL AND cs.deleted=0"):
        gt = _tok(r["gloss"])
        hits = [w for w in reg if _match(gt, terms[w])]
        if len(hits) == 1:
            out.append((r["lemma_key"], hits[0]))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="apply (default is dry-run)")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)
    for t in ("word_strong",):
        if t not in cfg.may_write("migration"):
            print(f"write-grant violation: 'migration' may not write {t!r}", file=sys.stderr)
            return 1
    alloc = clean_allocations(db)
    print(f"clean allocations: {len(alloc)} candidate strong(s) -> registry words")
    if not a.apply:
        print("DRY-RUN — re-run with --apply to add each strong under its word and pull its raw layer.")
        db.close(); cfg.close(); return 0

    step = Step(cfg)
    ctx = Ctx(db=db, cfg=cfg, step=step, run_id="ALLOCATE", word="", word_id=None,
              params={}, step_id="allocate")
    cd = {"strong": 0, "sense": 0, "tree": 0, "lexicon": 0, "skipped": 0, "no_vocab": 0}
    cv = {"strong_verse": 0, "verse_new": 0, "span_new": 0, "short": 0}
    wid = {r["word"]: r["id"] for r in db.rows("SELECT id, word FROM word_registry WHERE deleted=0")}
    done = 0
    for strong, word in alloc:
        ctx.word, ctx.word_id = word, wid[word]
        # 1. add the strong UNDER the word (grant: migration)
        db.upsert("word_strong", {"word_id": wid[word], "strong": strong, "deleted": 0})
        # 2. targeted per-strong pull — NOT the whole word
        raw.detail_one(ctx, strong, cd)
        raw.verses_one(ctx, strong, cv)
        # 3. resolve the double-control (the allocation record)
        db.update("candidate_seed", {"lemma_key": strong}, registry_match=word)
        done += 1
        if done % 25 == 0:
            db.conn.commit()
            print(f"  {done}/{len(alloc)} … (+{cv['strong_verse']} strong_verse, {cv['span_new']} span)")
    db.close()
    cfg.close()
    print(f"applied {done} allocation(s). detail: +{cd['strong']} strong, {cd['skipped']} already held. "
          f"verses: +{cv['verse_new']} new verse, +{cv['strong_verse']} strong_verse, +{cv['span_new']} span.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
