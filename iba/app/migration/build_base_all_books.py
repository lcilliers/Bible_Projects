"""build_base_all_books.py — stamp candidates + build passages for EVERY book present.

Passaging is per book. This runs the two base steps — candidate.set (stamp span_candidate)
then passage.build (recompute passages from the stamp) — for each book in the verse table,
in canonical order. Re-runnable: both steps clean-rebuild their book's rows. Writes a
per-book transcript (passages, review flags) to iba/app/reports/.

The candidate seed must already be current (run the seed migration / it is kept current by
the new-word coupling). This does no STEP calls — it reads span + span_candidate only.

    python -m iba.app.migration.build_base_all_books                 # char-continuity (default)
    python -m iba.app.migration.build_base_all_books --rule maximal
"""

from __future__ import annotations

import argparse
import datetime
import pathlib
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.stepapi import Step
from ..handlers.base import Ctx
from ..handlers import candidate, passage


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rule", choices=["char-continuity", "maximal"], default="char-continuity")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)
    step = Step(cfg)
    order = cfg.book_order()
    books = [r["b"] for r in db.rows(
        "SELECT DISTINCT substr(osisId,1,instr(osisId,'.')-1) AS b FROM verse WHERE deleted=0")]
    books.sort(key=lambda b: order.get(b, 999))

    print(f"base build over {len(books)} book(s), rule={a.rule}\n")
    rows = []
    tot = {"stamped": 0, "passages": 0, "review": 0}
    for b in books:
        ctx = Ctx(db=db, cfg=cfg, step=step, run_id="BASE", word=b, word_id=None,
                  params={"Book": b, "Rule": a.rule}, step_id="")
        o1 = candidate.set(ctx)
        stamped = o1.counts.get("span_candidate", 0) if o1.condition == "ok" else 0
        if o1.condition == "ok":
            o2 = passage.build(ctx)
        else:
            o2 = None
        db.conn.commit()
        if o2 is not None and o2.condition == "ok":
            npass = o2.counts.get("passages", 0)
            nrev = o2.counts.get("needs_review", 0)
        else:
            npass = nrev = 0
        note = "" if (o1.condition == "ok" and o2 and o2.condition == "ok") else \
               (o1.message if o1.condition != "ok" else (o2.message if o2 else ""))
        rows.append((b, stamped, npass, nrev, note))
        tot["stamped"] += stamped; tot["passages"] += npass; tot["review"] += nrev
        flag = f"  ⚠ {nrev} need review" if nrev else ""
        print(f"  {b:8} stamped {stamped:5}  passages {npass:5}{flag}  {note}")

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")
    L = [f"# Base build — all books ({stamp})", "",
         f"> candidate.set + passage.build over {len(books)} books, rule `{a.rule}`. "
         f"Totals: {tot['stamped']} candidate spans, **{tot['passages']} passages**, "
         f"**{tot['review']} flagged for review** (> review_over verses).", "",
         "| book | candidate spans | passages | needs review | note |",
         "| --- | --: | --: | --: | --- |"]
    for b, s, p, r, n in rows:
        L.append(f"| {b} | {s} | {p} | {r} | {n} |")
    out = pathlib.Path("iba/app/reports") / f"base-build-all-books-{stamp}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    db.close(); cfg.close()
    print(f"\nTOTAL: {tot['stamped']} candidate spans · {tot['passages']} passages · "
          f"{tot['review']} need review\ntranscript: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
