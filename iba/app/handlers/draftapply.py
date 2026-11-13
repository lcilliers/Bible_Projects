"""draftapply handlers -- work package `draft-apply` (escalation #2498).

Steps draft_apply.check (the load file applied inside a savepoint and rolled back: what a run would do, every problem; writes nothing to any
table) and draft_apply.apply (the same, kept, in one transaction; the whole file refused on any problem). The logic is in lib/draftapply.py.
A Refused is the routed condition 'refused' (cfg_on_fail: report-continue). Each step writes its result to draft_apply.output_dir."""
from __future__ import annotations

import json
import pathlib

from ..lib import draftapply as da
from ..lib import filingkit
from ..lib import reportkit
from .base import Ctx, Outcome, fail, ok

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]


def _load(ctx: Ctx) -> dict:
    f = pathlib.Path(ctx.params.get("File") or "")
    f = f if f.is_absolute() else PROJECT_ROOT / f
    if not f.is_file():
        raise da.Refused(f"-File is required and must exist: {f.as_posix()!r}")
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except ValueError as exc:
        raise da.Refused(f"{f.as_posix()} is not JSON: {exc}")


def _report(ctx: Ctx, res: dict, verb: str) -> pathlib.Path:
    out_dir = PROJECT_ROOT / pathlib.Path(ctx.cfg.required_setting("draft_apply.output_dir"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = filingkit.versioned_path(ctx.cfg, f"draft-{verb}", out_dir=out_dir, ext="md")
    lines = [f"# Draft {verb}", "", f"Run {ctx.run_id}. kept: {res['kept']}.", "",
             "| | count |", "|---|---|"] + [f"| {k.replace('_', ' ')} | {res[k]} |" for k in
                                             ("enriched", "added", "left", "nodes_added", "roles_set", "text_changed", "already_present") if k in res]
    for key, title in (("nodes_not_written_no_collection", "Nodes not written: no collection can carry them"),
                       ("nodes_not_written_out_of_scope", "Nodes not written: the verse is out of scope (B:130)")):
        lines += ["", f"## {title}", ""] + [f"- {x['row']}: {x['verse']} {x['surface']} ({x['strong']})" for x in res[key]]
    lines += ["", "## Rows", ""] + [f"- {r['row']}: {r['action']} observation {r['observation']}, nodes added {r['nodes_added']}" for r in res["rows"]]
    return reportkit.write_report(ctx.db.conn, ctx.step_id, path, lines)


def check(ctx: Ctx) -> Outcome:
    try:
        res = da.apply(ctx.db.conn, _load(ctx), ctx.run_id, keep=False)
    except da.Refused as exc:
        ctx.db.conn.rollback()
        return fail("refused", str(exc))
    out = _report(ctx, res, "check")
    return ok(f"-> {out}\n  would enrich {res['enriched']}, add {res['added']}, leave {res['left']}; {res['nodes_added']} node(s) added, "
              f"{res['roles_set']} role(s) set; nothing written", path=str(out))


def apply(ctx: Ctx) -> Outcome:
    for t in ("ib_observation", "ib_node", "ib_observation_change"):
        if t not in ctx.cfg.may_write(ctx.step_id):
            raise PermissionError(f"write-grant violation: {ctx.step_id!r} may not write {t!r}")
    conn = ctx.db.conn
    try:
        res = da.apply(conn, _load(ctx), ctx.run_id, keep=True)
        conn.commit()
    except da.Refused as exc:
        conn.rollback()
        return fail("refused", str(exc))
    except Exception:
        conn.rollback()
        raise
    out = _report(ctx, res, "apply")
    return ok(f"-> {out}\n  enriched {res['enriched']}, added {res['added']}, left {res['left']}; {res['nodes_added']} node(s) added, "
              f"{res['roles_set']} role(s) set", path=str(out))
