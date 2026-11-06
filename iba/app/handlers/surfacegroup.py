"""surfacegroup handlers -- work package `surface-group` (#2361, module 1 of 5 of the surface cycle), one step per Surface-Group.ps1 action.

Status reads the tables and says what the group repoint rule would do; Repoint does it: bases whose derived words agree and are all
inflections, with the base in an automatic group (cfg_setting group.repoint_auto_base_groups), are corrected to the group of their derived words
(surface_event correct); the other pairs become held_pair flags for the researcher; -Base names a proposed base the researcher accepts.
-Check previews. A second Repoint with the same inputs changes nothing. No file is read; a missing setting or an unknown -Base is the routed
condition 'refused' and writes nothing. See lib/surfacegroup.py for the rule."""
from __future__ import annotations

import json

from ..lib import surfacegroup as sg
from ..lib import surfacestructure as ss
from .base import Ctx, Outcome, fail, ok


def _plan(ctx: Ctx):
    vals = sg.read_settings(ctx.cfg)
    res, cons, pairs, flagged = sg.load(ctx.cfg.conn, ctx.cfg)
    return vals, sg.propose(pairs, flagged, vals), pairs


def _lines(plan: dict, pairs: dict) -> list[str]:
    return [f"pairs: {sum(len(v) for v in pairs.values())} of {len(pairs)} bases outside collection a with a derived word in it",
            f"to correct by rule: {len(plan['apply'])}" + (": " + ", ".join(sorted(plan["apply"])[:12]) + (" ..." if len(plan["apply"]) > 12 else "") if plan["apply"] else ""),
            f"proposed, need the researcher (-Base): {len(plan['review'])}" + (": " + ", ".join(sorted(plan["review"])) if plan["review"] else ""),
            f"held (not an inflection, or derived words disagree): {len(plan['held'])}" + (": " + ", ".join(sorted(plan["held"])) if plan["held"] else ""),
            f"already carrying a held_pair flag (left to that reading): {len(plan['skipped'])}"]


def status(ctx: Ctx) -> Outcome:
    try:
        vals, plan, pairs = _plan(ctx)
    except (sg.GroupError, ss.StructureError) as exc:
        return fail("refused", str(exc))
    return ok("\n  ".join(_lines(plan, pairs)), to_correct=len(plan["apply"]), proposed=len(plan["review"]), held=len(plan["held"]))


def repoint(ctx: Ctx) -> Outcome:
    try:
        vals, plan, pairs = _plan(ctx)
    except (sg.GroupError, ss.StructureError) as exc:
        return fail("refused", str(exc))
    named = {b.strip().lower() for b in str(ctx.params.get("Base") or "").split(",") if b.strip()}
    unknown = sorted(named - set(plan["review"]) - set(plan["apply"]))
    if unknown:
        return fail("refused", f"-Base names {unknown}, which the rule does not propose (only the 'proposed' bases can be named): run Status")
    lines = _lines(plan, pairs)
    if str(ctx.params.get("Check", "")).lower() in ("1", "true", "yes"):
        return ok("PREVIEW (nothing written)\n  " + "\n  ".join(lines), to_correct=len(plan["apply"]), proposed=len(plan["review"]))
    conn = ctx.cfg.conn
    done = sg.write(conn, ctx.run_id, plan, named)
    conn.execute("UPDATE run SET settings_snapshot=?, counts=? WHERE run_id=?", (json.dumps(vals), json.dumps(done), ctx.run_id))
    conn.commit()
    note = "\n  a base now in collection a: run Surface-Structure.ps1 -Action Match to refresh the structure evidence" if done["corrected"] else ""
    return ok("\n  ".join(lines) + f"\n  written: {done['corrected']} corrected, {done['flagged']} flagged{note}", **done)


def judge(ctx: Ctx) -> Outcome:
    """Ask the AI for the group of the surfaces not yet judged (group_state unjudged, and with -Retry failed), through lib/aiclient.py: prompt
    group.word, role judge; one ai_call row per attempt; the group, the reason and the model are stored on the surface_term with a surface_event.
    The words come from the tables; no file is read or written. -Limit n stops after n words."""
    import sys
    import time

    from ..lib import aiclient as ai
    from ..lib import batchcontrol as bc
    from ..lib import surfacejudge as sj
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
        groups, stored_as = ctx.cfg.setting("surface_judge.groups"), ctx.cfg.setting("surface_judge.group_stored_as") or {}
        if not groups:
            raise ai.AiError("cfg_setting surface_judge.groups is missing")
        want = ("unjudged", "failed") if retry else ("unjudged",)
        todo = conn.execute("SELECT id, surface FROM surface_term WHERE deleted=0 AND origin='surface' AND group_state IN (%s) ORDER BY surface"
                            % ",".join("?" * len(want)), want).fetchall()
        if limit:
            todo = todo[:limit]
        client = ai.AiClient(ctx.cfg, "group", "group", ctx.run_id)
        model = client.model("judge")
        client.prompt("group.word")
    except ai.AiError as exc:
        return fail("refused", str(exc))
    if not todo:
        return ok("nothing to judge: every surface has a group" + ("" if retry else " (-Retry also asks the failed ones)"), asked=0)
    bid = bc.start_batch(conn, ctx.run_id, "surface-group", "group.judge", f"judge:{ctx.run_id}", 1, bc.content_key([r[1] for r in todo]))
    client.batch_id = bid
    asked = done = bad = 0
    t0 = time.time()

    def finish(status_fn):
        conn.execute("UPDATE run_batch SET model_role='judge', model=?, calls=?, secs=? WHERE id=?", (model[1], asked, round(time.time() - t0, 1), bid))
        status_fn()

    try:
        with client.session(["judge"]):
            for tid, w in todo:
                r = client.call("judge", "group.word", {"surface": w}, ("surface_term", tid), check=lambda a: sj.check_word(a, groups),
                                result_of=lambda a: stored_as.get(a["group"], a["group"]))
                asked += 1
                if r["outcome"] == "answered":
                    g = stored_as.get(r["answer"]["group"], r["answer"]["group"])
                    conn.execute("UPDATE surface_term SET surface_group=?, group_reason=?, group_judged_by=?, group_state='judged', run_id=?, "
                                 "updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now') WHERE id=?", (g, r["answer"].get("reason"), model[1], ctx.run_id, tid))
                    conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                                 "VALUES ('surface_term',?,'set_group','surface_group',NULL,?,'surface-group',?,?,'surface-group')",
                                 (tid, g, f"ai_call {r['call_id']}", ctx.run_id))
                    done += 1
                else:
                    conn.execute("UPDATE surface_term SET group_state='failed', run_id=? WHERE id=?", (ctx.run_id, tid))
                    bad += 1
                conn.commit()
                print(f"{w!r}: {r['outcome']}", file=sys.stderr, flush=True)
    except ai.AiHalted as exc:
        finish(lambda: bc.fail_batch(conn, bid, str(exc)))
        return fail("halted", f"halted after {asked} words: {exc}", asked=asked, judged=done, failed=bad)
    except (ai.AiError, sj.JudgeError) as exc:
        bc.fail_batch(conn, bid, str(exc))
        return fail("refused", str(exc))
    finish(lambda: bc.commit_batch(conn, bid))
    return ok(f"asked {asked} words: {done} judged, {bad} failed; batch {bid}. Next: Surface-Group.ps1 -Action Repoint -Check", asked=asked, judged=done, failed=bad)
