"""openitem handlers -- work package `open-item` (#2236), one step per Open-Item.ps1 action.

Add, Reword and Split register items to a clear purpose (lib/openitem.py); each takes its parameters or -File
(a JSON list of item specs; for Split, the parts of one item) and runs as one unit: any refusal writes nothing.
Due lists the worded items that come back when a cluster is worked; Review writes the stragglers report under
open_item.output_dir. A refusal is the routed condition 'refused'."""
from __future__ import annotations

import json
import pathlib

from ..lib import narrativeregister as nr
from ..lib import openitem as oi
from ..lib import reportkit
from .base import Ctx, Outcome, fail, ok


def _who(ctx: Ctx) -> str:
    who = ctx.params.get("By") or "Claude"
    if who not in ("Claude", "Researcher"):
        raise oi.ItemError("-By is Claude or Researcher")
    return who


def _specs(ctx: Ctx) -> list[dict]:
    f = ctx.params.get("File")
    if not f:
        return [oi.spec_from(ctx.params)]
    p = pathlib.Path(f)
    if not p.is_file():
        raise oi.ItemError(f"-File not found: {p.as_posix()}")
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise oi.ItemError("-File holds a JSON list of item specs")
    return [oi.spec_from(x) for x in data]


def _unit(ctx: Ctx, fn) -> Outcome:
    conn = ctx.cfg.conn
    conn.execute("SAVEPOINT open_item")
    try:
        lines = fn(_who(ctx), nr.Writer(conn, ctx.step_id, "Claude"))
    except (oi.ItemError, ValueError, PermissionError) as exc:
        conn.execute("ROLLBACK TO open_item")
        conn.execute("RELEASE open_item")
        return fail("refused", str(exc))
    conn.execute("RELEASE open_item")
    conn.commit()
    return ok("\n  ".join(lines), items=len(lines))


def add(ctx: Ctx) -> Outcome:
    return _unit(ctx, lambda who, w: [oi.add(ctx.cfg, ctx.db, w, s, who) for s in _specs(ctx)])


def reword(ctx: Ctx) -> Outcome:
    return _unit(ctx, lambda who, w: [oi.reword(ctx.cfg, ctx.db, w, s, who) for s in _specs(ctx)])


def split(ctx: Ctx) -> Outcome:
    """-Item with -File (the parts of that item), or -File alone holding {"splits": [{"item", "parts": [...]}]}
    to split several items in one unit."""
    f = ctx.params.get("File")
    if f and not ctx.params.get("Item"):
        p = pathlib.Path(f)
        data = json.loads(p.read_text(encoding="utf-8")) if p.is_file() else None
        if not isinstance(data, dict) or not isinstance(data.get("splits"), list):
            return fail("refused", "Split without -Item takes -File holding {\"splits\": [{\"item\": \"OT-nn.n\", \"parts\": [...]}]}")
        return _unit(ctx, lambda who, w: [oi.split(ctx.cfg, ctx.db, w, s["item"], [oi.spec_from(x) for x in s["parts"]], who)
                                          for s in data["splits"]])
    return _unit(ctx, lambda who, w: [oi.split(ctx.cfg, ctx.db, w, ctx.params.get("Item"), _specs(ctx), who)])


def due(ctx: Ctx) -> Outcome:
    home = (ctx.params.get("Cluster") or "").strip()
    if not home:
        return fail("refused", "-Cluster (the cluster being worked) is required")
    rows = oi.due(ctx.cfg, home)
    return ok(f"{len(rows)} open item(s) come back when {home} is worked" + "".join(
        f"\n  {r['item']} {r['value']} ({r['target_verses']} verses): {r['read_for']}" for r in rows), items=len(rows))


def review(ctx: Ctx) -> Outcome:
    lines, console = oi.review(ctx.cfg)
    path = pathlib.Path(ctx.cfg.required_setting("open_item.output_dir")) / "open-items-review.md"
    out = reportkit.write_report(ctx.db.conn, ctx.step_id, path, lines)
    return ok(f"-> {out}\n  {console}", path=str(out))
