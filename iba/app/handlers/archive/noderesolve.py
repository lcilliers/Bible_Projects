"""noderesolve handlers -- work package `node-resolve` (escalation #2308).

Steps node_resolve.plan (what the sweep would fill on ib_node, read-only; writes the plan JSON and a report) and
node_resolve.apply (the plan written, node by node, only into null columns still unchanged since the plan). The logic is
in lib/noderesolve.py. A Refused is the routed condition 'refused' (cfg_on_fail: report-continue)."""
from __future__ import annotations

import json
import pathlib

from ..lib import filingkit
from ..lib import narrativeregister as nr
from ..lib import noderesolve as nrv
from ..lib import reportkit
from .base import Ctx, Outcome, fail, ok

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]


def _dir(ctx: Ctx) -> pathlib.Path:
    return PROJECT_ROOT / pathlib.Path(ctx.cfg.required_setting("node_resolve.output_dir"))


def _out(ctx: Ctx, topic: str, ext: str) -> pathlib.Path:
    path = filingkit.versioned_path(ctx.cfg, topic, out_dir=_dir(ctx), ext=ext)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def plan(ctx: Ctx) -> Outcome:
    p = nrv.plan(ctx.db.conn)
    path = _out(ctx, "resolve-plan", "json")
    path.write_text(json.dumps(p, ensure_ascii=False) + "\n", encoding="utf-8")
    rep = reportkit.write_report(ctx.db.conn, ctx.step_id, path.with_suffix(".md"), nrv.report_lines(p))
    c = p["counts"]
    return ok(f"-> {path.as_posix()}\n  {c.get('nodes examined', 0)} node(s) examined; {len(p['changes'])} to be filled "
              f"({c.get('verse_lexical_id', 0)} occurrence id(s), {c.get('cluster_subgroup_code', 0)} subgroup code(s)); "
              f"report {rep}", path=str(path), **c)


def apply(ctx: Ctx) -> Outcome:
    if "ib_node" not in ctx.cfg.may_write(ctx.step_id):
        raise PermissionError(f"write-grant violation: {ctx.step_id!r} may not write 'ib_node'")
    f = pathlib.Path(ctx.params.get("File") or "")
    f = f if f.is_absolute() else PROJECT_ROOT / f
    conn = ctx.db.conn
    try:
        if not f.is_file():
            raise nr.Refused(f"-File is required and must exist: {f.as_posix()!r}")
        try:
            p = json.loads(f.read_text(encoding="utf-8"))
        except ValueError as exc:
            raise nr.Refused(f"{f.as_posix()} is not JSON: {exc}")
        if p.get("kind") != "node-resolve":
            raise nr.Refused("the file is not a node-resolve plan (-Step Plan builds it)")
        res = nrv.apply(conn, p)
        conn.commit()
    except nr.Refused as exc:
        conn.rollback()
        return fail("refused", str(exc))
    except Exception:
        conn.rollback()
        raise
    out = reportkit.write_report(conn, ctx.step_id, _out(ctx, "resolve-applied", "md"), nrv.report_lines(p, res))
    return ok(f"-> {out}\n  {res['applied']} node(s) written, {res['stale']} skipped as changed since the plan",
              path=str(out), **{k: v for k, v in res.items() if k != "stale_ids"})
