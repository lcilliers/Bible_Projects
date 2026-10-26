"""priorcapture handlers -- work package `prior-capture` (escalation #2305).

Steps prior_capture.prepare (the document's JSON, read-only), prior_capture.record (the filled JSON written whole or
refused whole) and prior_capture.report (where the capture stands, read-only). The logic is in lib/priorcapture.py.
A Refused is the routed condition 'refused' (cfg_on_fail: report-continue)."""
from __future__ import annotations

import json
import pathlib

from ..lib import filingkit
from ..lib import narrativeregister as nr
from ..lib import priorcapture as pc
from ..lib import reportkit
from .base import Ctx, Outcome, fail, ok

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]


def _dir(ctx: Ctx) -> pathlib.Path:
    return PROJECT_ROOT / pathlib.Path(ctx.cfg.required_setting("prior_capture.output_dir"))


def _out(ctx: Ctx, topic: str, ext: str) -> pathlib.Path:
    path = filingkit.versioned_path(ctx.cfg, topic, out_dir=_dir(ctx), ext=ext)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _may(ctx: Ctx, table: str) -> None:
    if table not in ctx.cfg.may_write(ctx.step_id):
        raise PermissionError(f"write-grant violation: {ctx.step_id!r} may not write {table!r}")


def prepare(ctx: Ctx) -> Outcome:
    try:
        data = pc.prepare(ctx.db.conn, PROJECT_ROOT, ctx.params.get("File"))
    except nr.Refused as exc:
        return fail("refused", str(exc))
    path = _out(ctx, f"capture-{data['file']['id']:03d}", "json")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    c = data["counts"]
    return ok(f"-> {path.as_posix()}\n  {data['file']['path']}: {c['lines']} line(s) naming {c['verses']} verse(s), "
              f"{c['unresolved_refs']} reference(s) to no single verse, {len(data['october'])} October id(s) already "
              f"recorded. Fill findings and every line's answer, then -Step Record -File <this file>.",
              path=str(path), **c)


def record(ctx: Ctx) -> Outcome:
    for t in ("ib_observation", "ib_node", "prior_capture_line", "reading_file"):
        _may(ctx, t)
    f = pathlib.Path(ctx.params.get("File") or "")
    f = f if f.is_absolute() else PROJECT_ROOT / f
    conn = ctx.db.conn
    try:
        if not f.is_file():
            raise nr.Refused(f"-File is required and must exist: {f.as_posix()!r}")
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except ValueError as exc:
            raise nr.Refused(f"{f.as_posix()} is not JSON: {exc}")
        plan = pc.check(ctx.cfg, PROJECT_ROOT, data)
        counts = pc.write(conn, plan, ctx.run_id)
        conn.commit()
    except nr.Refused as exc:
        conn.rollback()
        return fail("refused", str(exc))
    except Exception:
        conn.rollback()
        raise
    path = _dir(ctx) / f"capture-{plan['file']['id']:03d}-report.md"
    out = reportkit.write_report(conn, ctx.step_id, path, pc.report_lines(plan, counts))
    return ok(f"-> {out}\n  {plan['file']['path']}: {counts['status']}; {counts['observations_new']} observation(s) "
              f"written, {counts['observations_reused']} joined, {counts['nodes']} node(s), {counts['lines']} line(s) "
              f"answered", path=str(out), **{k: v for k, v in counts.items() if k != "ids"})


def report(ctx: Ctx) -> Outcome:
    lines, console = pc.report(ctx.db.conn)
    out = reportkit.write_report(ctx.db.conn, ctx.step_id, _dir(ctx) / "capture-status.md", lines)
    return ok(f"-> {out}\n  {console}", path=str(out))
