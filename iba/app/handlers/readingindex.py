"""readingindex handlers -- work package `reading-index` (#2228 tool 2).

Build indexes the study files under reading_index.roots into reading_file, reading_section and reading_ref
(its write grants checked on every write); Report writes the coverage report under
reading_index.output_dir. The logic is in lib/readingindex.py."""
from __future__ import annotations

import pathlib

from ..lib import narrativeregister as nr
from ..lib import readingindex as ri
from ..lib import reportkit
from .base import Ctx, Outcome, ok

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]


def build(ctx: Ctx) -> Outcome:
    w = nr.Writer(ctx.cfg.conn, ctx.step_id, "Claude")
    return ok(ri.build(ctx.cfg, w, PROJECT_ROOT))


def report(ctx: Ctx) -> Outcome:
    lines, console = ri.report(ctx.cfg, ctx.params)
    path = pathlib.Path(ctx.cfg.required_setting("reading_index.output_dir")) / "reading-index-coverage.md"
    out = reportkit.write_report(ctx.db.conn, ctx.step_id, path, lines)
    return ok(f"-> {out}\n  {console}", path=str(out))
