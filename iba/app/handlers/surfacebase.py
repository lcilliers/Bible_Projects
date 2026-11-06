"""surfacebase handlers -- work package `surface-base` (#2359, #2361), the table route of the AI base.

Ask asks the AI, through lib/aiclient.py, for the base of the surfaces the resolve module leaves unmatched (and, with -Retry, the failed): prompt
base.word, role judge, one ai_call row per attempt, a run_batch row per run; it reads and writes tables only. A usage problem (a missing setting, an
inactive prompt) is the routed condition 'refused' and writes nothing. The earlier file route (Status and Run with a batch file) was retired in stage 6."""
from __future__ import annotations

import sys

from ..lib import surfacebase as sb
from .base import Ctx, Outcome, fail, ok


def ask(ctx: Ctx) -> Outcome:
    """Ask the AI for the base of the surfaces the resolve module leaves `unmatched` (and, with -Retry, `ai_failed`), through lib/aiclient.py:
    prompt base.word, role judge; one ai_call row per attempt; the words come from the tables, no file is read or written. -Limit n stops after n
    words. Afterwards run Surface-Resolve.ps1 -Action Run: it reads the calls and decides the bases."""
    from ..lib import aiclient as ai
    from ..lib import batchcontrol as bc
    from ..lib import surfacejudge as sj
    from ..lib import surfaceresolve as sr
    from ..lib import surfacestructure as ss
    conn = ctx.cfg.conn
    try:
        limit = ctx.params.get("Limit")
        if limit not in (None, ""):
            if not str(limit).isdigit() or int(limit) < 1:
                raise ai.AiError(f"-Limit is a whole number of at least 1, not {limit!r}")
            limit = int(limit)
        else:
            limit = None
        retry = str(ctx.params.get("Retry", "")).lower() in ("1", "true", "yes")
        rel = ctx.cfg.setting("surface_judge.base_relations")
        pat = ctx.cfg.setting("surface_judge.base_form_pattern")
        if rel is None or pat is None:
            raise ai.AiError("cfg_setting surface_judge.base_relations or surface_judge.base_form_pattern is missing")
        decided, _ = sr.decisions(conn, ctx.cfg)
        want = {"unmatched"} | ({"ai_failed"} if retry else set())
        todo = sorted((t for t, d in decided if d["state"] in want), key=lambda t: t["surface"])
        if limit:
            todo = todo[:limit]
        client = ai.AiClient(ctx.cfg, "ai_base", "base", ctx.run_id)
        client.model("judge"), client.prompt("base.word")
    except (ai.AiError, sr.ResolveError, ss.StructureError) as exc:
        return fail("refused", str(exc))
    if not todo:
        return ok("nothing to ask: no surface is waiting for an AI base" + (" (none failed either)" if retry else " (-Retry also asks the failed ones)"), asked=0)
    bvals = {"base_relations": rel, "base_form_pattern": pat}
    bid = bc.start_batch(conn, ctx.run_id, "surface-base", "surface_base.ask", f"ask:{ctx.run_id}", 1, bc.content_key([t["surface"] for t in todo]))
    client.batch_id = bid
    asked = ok_n = bad_n = 0
    t0 = __import__("time").time()
    try:
        with client.session(["judge"]):
            for t in todo:
                w = t["surface"]
                r = client.call("judge", "base.word", {"surface": w}, ("surface_term", t["id"]), check=lambda a, w=w: sb.check_answer(a, w, bvals),
                                result_of=lambda a, w=w: (a.get("base") or w))
                asked += 1
                ok_n += r["outcome"] == "answered"
                bad_n += r["outcome"] != "answered"
                print(f"{w!r}: {r['outcome']}" + (f" {r['answer'].get('relation')} {r['answer'].get('base')!r}" if r["outcome"] == "answered" else f" {r['error'][:80]}"),
                      file=sys.stderr, flush=True)
    except ai.AiHalted as exc:
        conn.execute("UPDATE run_batch SET model_role='judge', model=?, calls=?, secs=? WHERE id=?", (client.model("judge")[1], asked, round(__import__("time").time() - t0, 1), bid))
        bc.fail_batch(conn, bid, str(exc))
        return fail("halted", f"halted after {asked} words: {exc}", asked=asked, answered=ok_n, not_usable=bad_n)
    except (ai.AiError, sj.JudgeError) as exc:
        bc.fail_batch(conn, bid, str(exc))
        return fail("refused", str(exc))
    conn.execute("UPDATE run_batch SET model_role='judge', model=?, calls=?, secs=? WHERE id=?", (client.model("judge")[1], asked, round(__import__("time").time() - t0, 1), bid))
    bc.commit_batch(conn, bid)
    return ok(f"asked {asked} words: {ok_n} answered, {bad_n} not usable; batch {bid}. Next: Surface-Resolve.ps1 -Action Run", asked=asked, answered=ok_n, not_usable=bad_n)
