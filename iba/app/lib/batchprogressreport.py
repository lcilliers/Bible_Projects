"""batchprogressreport.py — read-only live progress over `run_batch` (escalation #1756). Lets the
researcher see how far a long-running batch step has gotten WITHOUT waiting for it to finish or
reading a background process's raw stdout — the whole point of writing a `run_batch` row per batch
rather than only logging to a CSV/console.

Filters are all optional and combine with AND: `-RunId` narrows to one specific run, `-Step`/
`-SelectorKey` narrow to one step/selector (e.g. every M49 batch across every run_id that ever
touched it, live or historical). No filters at all reports every run_batch row currently
`status='running'` (the live-right-now view) plus a short recent-activity tail.
"""

from __future__ import annotations

import datetime

from . import reportkit


def _elapsed(started_at: str, ended_at: str | None) -> str:
    start = datetime.datetime.strptime(started_at, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=datetime.timezone.utc)
    end = (datetime.datetime.strptime(ended_at, "%Y-%m-%dT%H:%M:%SZ").replace(
           tzinfo=datetime.timezone.utc) if ended_at else
           datetime.datetime.now(datetime.timezone.utc))
    seconds = int((end - start).total_seconds())
    return f"{seconds // 60}m{seconds % 60:02d}s"


def generate(conn, run_id: str | None = None, step: str | None = None,
            selector_key: str | None = None):
    where, params = [], []
    if run_id:
        where.append("run_id=?")
        params.append(run_id)
    if step:
        where.append("step=?")
        params.append(step)
    if selector_key:
        where.append("selector_key=?")
        params.append(selector_key)
    clause = f"WHERE {' AND '.join(where)}" if where else ""

    rows = [dict(r) for r in conn.execute(
        f"SELECT * FROM run_batch {clause} ORDER BY id DESC LIMIT 500", params)]

    running = [r for r in rows if r["status"] == "running"]
    committed = [r for r in rows if r["status"] == "committed"]
    failed = [r for r in rows if r["status"] == "failed"]
    total_cost = sum(r["cost_usd"] or 0 for r in committed)

    # If no explicit filter was given at all, the "live right now" view is every currently-running
    # row DB-wide, not the last 500 rows regardless of filter -- that's the actual live-monitor use
    # case (found live building this: without this branch, an unfiltered call would just dump
    # whatever's most recent, running or not, which isn't "what's in progress right now").
    if not (run_id or step or selector_key):
        running = [dict(r) for r in conn.execute(
            "SELECT * FROM run_batch WHERE status='running' ORDER BY started_at")]

    intro = [
        f"> Generated {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} "
        f"by `report.batch_progress`."
        + (f" Filtered: run_id={run_id!r}" if run_id else "")
        + (f" step={step!r}" if step else "")
        + (f" selector_key={selector_key!r}" if selector_key else ""),
        "",
        f"- currently running: **{len(running)}**",
        f"- committed (this view): **{len(committed)}**",
        f"- failed (this view): **{len(failed)}**",
        f"- total spend (this view): **${total_cost:.4f}**",
    ]
    sections = {
        "summary": [
            f"{len(running)} running, {len(committed)} committed, {len(failed)} failed "
            f"(view limited to the most recent 500 rows unless filtered)",
        ],
        "running_now": (
            [f"`{r['step']}` / `{r['selector_key']}` batch {r['batch_ordinal']} -- run "
             f"`{r['run_id']}`, running {_elapsed(r['started_at'], None)} (started "
             f"{r['started_at']})" for r in running]
            or ["(none currently running)"]),
        "recent_failures": (
            [f"`{r['step']}` / `{r['selector_key']}` batch {r['batch_ordinal']} -- run "
             f"`{r['run_id']}`, failed at {r['ended_at']} (started {r['started_at']}, "
             f"after {_elapsed(r['started_at'], r['ended_at'])}): {r['error_message']}"
             for r in failed[:20]]
            or ["(none)"]),
        "recent_committed": (
            [f"`{r['step']}` / `{r['selector_key']}` batch {r['batch_ordinal']} -- run "
             f"`{r['run_id']}`, committed at {r['ended_at']} (started {r['started_at']}, "
             f"{_elapsed(r['started_at'], r['ended_at'])}), ${(r['cost_usd'] or 0):.4f}"
             for r in committed[:20]]
            or ["(none)"]),
    }
    return reportkit.render_scaffold(conn, "report.batch_progress", sections, intro=intro)
