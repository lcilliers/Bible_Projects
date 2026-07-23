"""retention.py — log growth / run-health visibility for the append-only audit tables
(`run`, `escalation`, `validation_result`). No pruning or deletion here — that is a policy
decision for the researcher, not this app's to assume (raised 2026-07-22: "are there a
maintenance routine to maintain log file, else they will grow out of hand" — this is the
routine's READ side: a persisted status report, run on demand, showing exactly what would need
a decision. A delete/archive routine is a deliberate next step once a retention POLICY is chosen,
not built here.

Also identifies CHAINED-package runs stuck mid-sequence with no escalation pending — these are
NOT relabelled 'done' (see migration/fix_stuck_run_states.py's reasoning: a chained run stuck
mid-sequence may genuinely be an abandoned/incomplete run, e.g. a standalone `candidate.seed`
test that was never meant to continue to `candidate.set` — relabelling it would misrepresent what
happened). They are archival CANDIDATES, surfaced here for a real decision.
"""

from __future__ import annotations

import datetime
import pathlib

from . import reportkit


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _age_days(iso: str) -> float:
    try:
        dt = datetime.datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    except (ValueError, TypeError):
        return 0.0
    return (datetime.datetime.now(datetime.timezone.utc) - dt).total_seconds() / 86400


def build(cfg) -> dict:
    conn = cfg.conn
    out: dict = {}

    out["run_total"] = conn.execute("SELECT COUNT(*) FROM run").fetchone()[0]
    out["run_by_state"] = [dict(r) for r in conn.execute(
        "SELECT state, COUNT(*) n FROM run GROUP BY state ORDER BY n DESC")]
    out["run_oldest"] = conn.execute("SELECT MIN(started_at) FROM run").fetchone()[0]
    out["run_newest"] = conn.execute("SELECT MAX(started_at) FROM run").fetchone()[0]

    out["escalation_total"] = conn.execute("SELECT COUNT(*) FROM escalation").fetchone()[0]
    out["escalation_open"] = conn.execute(
        "SELECT COUNT(*) FROM escalation WHERE state='raised'").fetchone()[0]
    out["escalation_answered"] = conn.execute(
        "SELECT COUNT(*) FROM escalation WHERE state='answered'").fetchone()[0]

    out["validation_result_total"] = conn.execute("SELECT COUNT(*) FROM validation_result").fetchone()[0]
    out["validation_result_oldest"] = conn.execute("SELECT MIN(ran_at) FROM validation_result").fetchone()[0]

    # real failures (state='failed'), last 7 days, excluding obvious self-test run_ids
    out["recent_failed"] = [dict(r) for r in conn.execute("""
        SELECT run_id, work_package, runs_over, outcome, ended_at FROM run
        WHERE state='failed' AND ended_at IS NOT NULL
        ORDER BY ended_at DESC LIMIT 50
    """)]

    # chained-package runs stuck mid-sequence, no raised escalation — archival candidates, not
    # relabelled (see module docstring)
    out["stuck_chained"] = [dict(r) for r in conn.execute("""
        SELECT r.run_id, r.work_package, r.state, r.resume_point, r.runs_over, r.started_at
        FROM run r JOIN cfg_work_package wp ON wp.name = r.work_package
        WHERE wp.chained = 1 AND r.state IN ('running','paused')
        AND NOT EXISTS (SELECT 1 FROM escalation e WHERE e.run_id = r.run_id AND e.state='raised')
        ORDER BY r.started_at
    """)]

    out["oldest_open_escalations"] = [dict(r) for r in conn.execute("""
        SELECT id, run_id, word, at_step, question, raised_at FROM escalation
        WHERE state='raised' ORDER BY raised_at LIMIT 50
    """)]

    return out


def _tbl(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        L.append("| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |")
    return L


def write_report(cfg, path: pathlib.Path) -> pathlib.Path:
    d = build(cfg)

    intro = [
        f"> Generated {_now()}. Read-only visibility — no rows deleted or archived here. "
        f"A retention/deletion POLICY is a separate decision; this report exists so that decision "
        f"can be made with real numbers, not a guess.",
    ]

    sections = {
        "summary": (
            [f"- `run`: **{d['run_total']}** rows, oldest {d['run_oldest']}, newest {d['run_newest']}"]
            + [f"  - {r['state']}: {r['n']}" for r in d["run_by_state"]]
            + [f"- `escalation`: **{d['escalation_total']}** rows — {d['escalation_open']} open "
               f"(raised), {d['escalation_answered']} answered",
               f"- `validation_result`: **{d['validation_result_total']}** rows, oldest "
               f"{d['validation_result_oldest']}"]),
        "stuck_chained": (
            [f"**{len(d['stuck_chained'])}** run(s): a chained work package (new-word / "
             f"set-candidates / build-passages) stopped mid-sequence with nothing currently "
             f"pending on it. May be a real abandoned run, or a deliberate standalone single-step "
             f"test (e.g. `candidate.seed` run directly without a book) — needs a human look, not "
             f"an automatic relabel.", ""]
            + _tbl(["run_id", "work_package", "state", "resume_point", "runs_over", "started_at"],
                  [[r["run_id"], r["work_package"], r["state"], r["resume_point"], r["runs_over"],
                    r["started_at"]] for r in d["stuck_chained"][:200]])),
        "open_escalations": _tbl(
            ["id", "run_id", "word", "at_step", "question", "raised_at"],
            [[r["id"], r["run_id"], r["word"], r["at_step"], r["question"][:120], r["raised_at"]]
             for r in d["oldest_open_escalations"]]),
        "recent_failed": _tbl(
            ["run_id", "work_package", "runs_over", "outcome", "ended_at"],
            [[r["run_id"], r["work_package"], r["runs_over"], (r["outcome"] or "")[:120],
              r["ended_at"]] for r in d["recent_failed"]]),
    }

    L = reportkit.render_scaffold(cfg.conn, "retention.report", sections, intro=intro)
    reportkit.write_csv_pairing(cfg.conn, "retention.report", path.parent / "export")
    reportkit.write_report(cfg.conn, "retention.report", path, L)
    return path
