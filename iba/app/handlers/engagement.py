"""engagement handlers -- work package `engagement` (#2406): what each surface of a collection does for the inner being, one step per
Engagement.ps1 action.

Pull writes the working file of one collection (a view of the tables, never overwritten). Record checks a filled assessment against its pull,
whole, and writes it in one transaction (nothing is written when anything is wrong; -Check previews). Group sets the surface-level group of each
member surface from its assessments (-Check previews); a surface that moves out of the study group is reported and raised as one escalation for
the collection, never unlinked (R4). Check reports every member surface against its verses to engagement.report_path. The rule is in
lib/engagement.py; every value is a cfg_setting of module `engagement`. A usage problem is the routed condition 'refused' and writes nothing."""
from __future__ import annotations

import json
import pathlib

from ..lib import engagement as eg
from .base import Ctx, Outcome, escalate, fail, ok


def _flag(ctx, name):
    return str(ctx.params.get(name, "")).lower() in ("1", "true", "yes")


def pull(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    try:
        content = eg.pull(conn, ctx.cfg, ctx.params.get("Collection"))
        path = eg.next_path(ctx.cfg, "pull", content["collection"]["name"])
    except (eg.EngagementError, KeyError) as exc:
        return fail("refused", str(exc))
    eg.write_json(path, content)
    n_items = sum(len(s["items"]) for s in content["surfaces"])
    return ok(f"{path.as_posix()}: collection {content['collection']['name']}, {len(content['surfaces'])} member surfaces, {n_items} surface items, "
              f"{len(content['existing_observations'])} existing observations on their verses", surfaces=len(content["surfaces"]), items=n_items,
              existing=len(content["existing_observations"]))


def record(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    errors: list = []
    try:
        filled = eg.load_json(ctx.params.get("File") or "")
        if not filled.get("pull"):
            return fail("refused", "the assessment file names no `pull` (the working file it was made from)")
        pulled = eg.load_json(filled["pull"])
        plan = eg.check_assessment(conn, ctx.cfg, pulled, filled, errors)
    except (eg.EngagementError, KeyError) as exc:
        return fail("refused", str(exc))
    if errors:
        return fail("refused", f"{len(errors)} problem(s), nothing written:\n  " + "\n  ".join(errors[:60]) + (f"\n  ... and {len(errors) - 60} more" if len(errors) > 60 else ""))
    lines = (f"collection {pulled['collection']['name']}: {plan['evaluations']} evaluations; {len(plan['plan'])} observations "
             f"({sum(len(p['nodes']) for p in plan['plan'])} nodes); existing observations: {len(plan['existing'])} actions")
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written): " + lines, observations=len(plan["plan"]))
    try:
        conn.execute("SAVEPOINT engagement_record")
        done = eg.record(conn, ctx.cfg, ctx.run_id, plan, "Claude")
        conn.execute("RELEASE engagement_record")
    except (eg.Refused, eg.EngagementError, KeyError) as exc:
        conn.execute("ROLLBACK TO engagement_record")
        conn.execute("RELEASE engagement_record")
        return fail("refused", f"{exc}; nothing written")
    ids = done.pop("ids")
    conn.execute("UPDATE run SET counts=? WHERE run_id=?", (json.dumps(done), ctx.run_id))
    conn.commit()
    return ok(lines + f"\n  written: {done['observations']} new observations ({done['reused']} already live), {done['nodes']} nodes; existing: "
              f"{done['accepted']} accepted, {done['modified']} modified, {done['deleted']} deleted, {done['merged']} merged, {done['left']} left", **done)


def group(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    try:
        pl = eg.group_plan(conn, ctx.cfg, ctx.params.get("Collection"))
    except (eg.EngagementError, KeyError) as exc:
        return fail("refused", str(exc))
    lines = [f"collection {pl['collection']}: to change {len(pl['change'])}, as set {len(pl['same'])}, not assessed {len(pl['unassessed'])}, "
             f"held (confirmed by the researcher) {len(pl['held'])}"]
    lines += [f"  {s}: {b} ({st}) -> {n}  roles {', '.join(r) or 'none'}" for _, s, b, st, n, r in pl["change"]]
    lines += [f"  not assessed: {s} ({m} of {t} verse items without an assessment)" for s, m, t in pl["unassessed"]]
    lines += [f"  held: {s} stays {b} (the assessment says {n})" for s, b, n in pl["held"]]
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written)\n" + "\n".join(lines), change=len(pl["change"]))
    n = eg.group_write(conn, ctx.cfg, ctx.run_id, pl)
    conn.execute("UPDATE run SET counts=? WHERE run_id=?", (json.dumps({"changed": n}), ctx.run_id))
    conn.commit()
    none = eg.settings(ctx.cfg)["group_rule"]["none"]
    tier = dict(pl["to_other"])
    left = [(c[1], tier.get(c[1], "")) for c in pl["change"] if c[4] == none]
    msg = "\n".join(lines) + f"\n  written: {n} group(s)"
    if left:
        names = ", ".join(f"{s} ({t})" for s, t in left)
        return escalate("member_left_study", f"Collection {pl['collection']}: member surface(s) {names} now have the group other after the engagement assessment, "
                        "so they leave collection a while still linked to the collection. This step never changes a collection (R4). To decide: unlink them "
                        "(set the link deleted), keep them, or question the collection as malformed. Afterwards run Surface-Resolve.ps1 -Action Run -Check and "
                        "Surface-Group.ps1 -Action Repoint -Check. " + msg, {"collection": pl["collection"], "surfaces": [s for s, _ in left]},
                        tried=msg, resolution_kind="decision_required", title=f"Members of {pl['collection']} left the study group"[:60], changed=n)
    return ok(msg, changed=n)


def review(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    try:
        content = eg.review_pull(conn, ctx.cfg, ctx.params.get("Collection"))
        path = eg.next_path(ctx.cfg, "review", content["collection"]["name"])
    except (eg.EngagementError, KeyError) as exc:
        return fail("refused", str(exc))
    n_items = sum(len(s["items"]) for s in content["surfaces"])
    if not n_items:
        return ok(f"collection {content['collection']['name']}: no verse to review ({content['verses_set_aside']} verses already set aside, "
                  f"{content['not_yet_assessed_verses']} verses not yet assessed); no file written", items=0)
    eg.write_json(path, content)
    return ok(f"{path.as_posix()}: {len(content['verses'])} verses with no bearing in any member surface, {n_items} items to read again; "
              f"{content['verses_set_aside']} verses already set aside", verses=len(content["verses"]), items=n_items)


def close(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    errors: list = []
    try:
        filled = eg.load_json(ctx.params.get("File") or "")
        if not filled.get("review"):
            return fail("refused", "the file names no `review` (the review file it was made from)")
        rpull = eg.load_json(filled["review"])
        plan = eg.check_close(conn, ctx.cfg, rpull, filled, errors)
    except (eg.EngagementError, KeyError) as exc:
        return fail("refused", str(exc))
    if errors:
        return fail("refused", f"{len(errors)} problem(s), nothing written:\n  " + "\n  ".join(errors[:60]))
    lines = (f"collection {rpull['collection']['name']}: {len(plan['confirm'])} confirmed no bearing, {len(plan['reopen'])} reopened, "
             f"{len(plan['plan'])} observations for the reopened")
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written): " + lines, confirm=len(plan["confirm"]), reopen=len(plan["reopen"]))
    try:
        conn.execute("SAVEPOINT engagement_close")
        done = eg.close(conn, ctx.cfg, ctx.run_id, plan, "Claude")
        conn.execute("RELEASE engagement_close")
    except (eg.Refused, eg.EngagementError, KeyError) as exc:
        conn.execute("ROLLBACK TO engagement_close")
        conn.execute("RELEASE engagement_close")
        return fail("refused", f"{exc}; nothing written")
    done.pop("ids")
    conn.execute("UPDATE run SET counts=? WHERE run_id=?", (json.dumps(done), ctx.run_id))
    conn.commit()
    return ok(lines + f"\n  written: {done['confirmed']} confirmed, {done['reopened']} reopened ({done['observations']} new observations, {done['nodes']} nodes)", **done)


def check(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    try:
        res = eg.check_collection(conn, ctx.cfg, ctx.params.get("Collection"))
        path = eg.next_path(ctx.cfg, "check", res["collection"], "md")
    except (eg.EngagementError, KeyError) as exc:
        return fail("refused", str(exc))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(eg.report_text(res), encoding="utf-8")
    msg = f"{path.as_posix()}: {len(res['surfaces'])} member surfaces, {res['failing']} not fully assessed"
    if res["failing"]:
        return fail("not_assessed", msg + " (" + ", ".join(r["surface"] for r in res["surfaces"] if r["unassessed"] or not r["items"]) + ")")
    return ok(msg, surfaces=len(res["surfaces"]), failing=0)
