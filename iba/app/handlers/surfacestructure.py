"""surfacestructure handlers -- work package `surface-structure` (#2361, module 2 of 5 of the surface cycle), one step per Surface-Structure.ps1 action.

Status computes the structure of the surfaces of collection a and compares it with the evidence rows in surface_derivation (read-only).
Match does the same and writes the difference: new evidence rows added, rows no longer produced set to deleted = 1; a second Match with
the same inputs changes nothing. -Check makes Match a preview. Show prints one surface's structure record and its evidence rows.
Everything is read from surface_term, cfg_base_construct and cfg_setting (module structure); no file is read. A missing setting or
surface is the routed condition 'refused' and writes nothing. See lib/surfacestructure.py for the method."""
from __future__ import annotations

import json

from ..lib import surfacestructure as ss
from .base import Ctx, Outcome, fail, ok


def _compute(ctx: Ctx):
    vals = ss.read_settings(ctx.cfg)
    surfaces, cons, outside = ss.load_inputs(ctx.cfg.conn, ctx.cfg)
    res = ss.analyse(surfaces, cons, outside, vals)
    return vals, cons, res


def _summary(res: dict, plan: dict) -> list[str]:
    n_hits = collections_count(res["hits"])
    c = res["counts"]
    return [f"surfaces of collection a: {len(res['surfaces'])}; hits {len(res['hits'])} ({n_hits})",
            "status: " + "; ".join(f"{k} {v}" for k, v in sorted(c.items(), key=lambda kv: -kv[1])),
            f"sibling groups: {len(res['sibling_groups'])}; roots {res['roots_before']}, after siblings {res['roots_after_siblings']}",
            f"evidence in the tables: {plan['kept']} rows as computed; {len(plan['add'])} to add; {sum(len(i) for _, i in plan['remove'])} to supersede"]


def collections_count(hits):
    out = {}
    for h in hits:
        out[h["direction"]] = out.get(h["direction"], 0) + 1
    return ", ".join(f"{k} {v}" for k, v in sorted(out.items()))


def status(ctx: Ctx) -> Outcome:
    try:
        vals, cons, res = _compute(ctx)
    except ss.StructureError as exc:
        return fail("refused", str(exc))
    plan = ss.plan_write(ctx.cfg.conn, ss.desired_evidence(res, cons))
    return ok("\n  ".join(_summary(res, plan)), hits=len(res["hits"]), to_add=len(plan["add"]),
              to_supersede=sum(len(i) for _, i in plan["remove"]))


def match(ctx: Ctx) -> Outcome:
    try:
        vals, cons, res = _compute(ctx)
    except ss.StructureError as exc:
        return fail("refused", str(exc))
    conn = ctx.cfg.conn
    plan = ss.plan_write(conn, ss.desired_evidence(res, cons))
    lines = _summary(res, plan)
    check = str(ctx.params.get("Check", "")).lower() in ("1", "true", "yes")
    if check:
        return ok("PREVIEW (nothing written)\n  " + "\n  ".join(lines), to_add=len(plan["add"]),
                  to_supersede=sum(len(i) for _, i in plan["remove"]))
    done = ss.write(conn, ctx.run_id, plan)
    conn.execute("UPDATE run SET settings_snapshot=?, counts=? WHERE run_id=?",
                 (json.dumps({"settings": vals, "constructs": len(cons)}), json.dumps(done), ctx.run_id))
    conn.commit()
    return ok("\n  ".join(lines) + f"\n  written: {done['added']} added, {done['superseded']} superseded, {done['kept']} unchanged",
              added=done["added"], superseded=done["superseded"], kept=done["kept"])


def show(ctx: Ctx) -> Outcome:
    sf = (ctx.params.get("Surface") or "").strip().lower()
    if not sf:
        return fail("refused", "-Surface is required: the surface text to show")
    try:
        vals, cons, res = _compute(ctx)
    except ss.StructureError as exc:
        return fail("refused", str(exc))
    rec = next((r for r in res["surfaces"] if r["surface"] == sf), None)
    if rec is None:
        return fail("refused", f"{sf!r} is not a surface of collection a (live, in a group of cfg_setting surfaces.scope_groups 'a')")
    rows = ctx.cfg.conn.execute(
        "SELECT d.method, d.evidence, d.kind, d.base_word, d.accepted, d.deleted FROM surface_derivation d JOIN surface_term t ON t.id=d.term_id "
        "WHERE t.surface=? AND d.method IN ('structure','sibling') ORDER BY d.deleted, d.method, d.evidence", (sf,)).fetchall()
    lines = [f"{sf}: {rec['status_v2']} (status 1: {rec['status']}); group {rec['group']}; form {rec['form']}",
             f"bases {rec['bases']}; roots {rec['roots']}; derived by {rec['derived_by']}; pointed at by {rec['pointed_at_by']}",
             f"opposite leads {rec['opposite_leads']}; other leads {rec['other_leads']}; starts-with leads {rec['starts_with_leads']}",
             f"outside-list bases {rec['base_outside_input']}; sibling group {rec['sibling_group'] or '-'} via {rec['sibling_via']}",
             "evidence rows (structure and sibling) in surface_derivation:"]
    lines += [f"  {'DELETED ' if r[5] else ''}{r[0]} {r[1]} {r[2]} -> {r[3]} (accepted {r[4]})" for r in rows] or ["  none"]
    return ok("\n  ".join(lines), surface=sf)
