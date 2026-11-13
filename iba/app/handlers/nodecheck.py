"""nodecheck handler -- work package `node-check` (escalation #2484).

Step node_check.report: every live node and observation against the node rules (behaviour rules B:130 and B:131), listed by check; writes a Markdown report and
a workbook (one sheet for each check) to node_check.output_dir. Reads only: the step has no write grant. The logic is in lib/nodecheck.py."""
from __future__ import annotations

import datetime
import pathlib

from ..lib import filingkit
from ..lib import nodecheck as nck
from ..lib import reportkit
from .base import Ctx, Outcome, ok

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]


def report(ctx: Ctx) -> Outcome:
    out_dir = PROJECT_ROOT / pathlib.Path(ctx.cfg.required_setting("node_check.output_dir"))
    out_dir.mkdir(parents=True, exist_ok=True)
    res = nck.run(ctx.db.conn)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    md = filingkit.versioned_path(ctx.cfg, "node-check", out_dir=out_dir, ext="md")
    md = reportkit.write_report(ctx.db.conn, ctx.step_id, md, nck.report_lines(res, ctx.run_id, stamp))
    xlsx = md.with_suffix(".xlsx")
    nck.write_workbook(xlsx, res, ctx.run_id, stamp)
    t, c = res["totals"], res["counts"]
    top = ", ".join(f"{k} {v:,}" for k, v in sorted(c.items(), key=lambda kv: -kv[1])[:5] if v)
    return ok(f"-> {md.as_posix()}\n  workbook {xlsx.as_posix()}\n  {t['live nodes']:,} live node(s), {t['live nodes with a finding']:,} with a finding; "
              f"{t['live observations']:,} live observation(s); largest: {top}", path=str(md), **{k.replace(" ", "_"): v for k, v in t.items()})
