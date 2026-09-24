"""session_close.py — session-close checks: escalation update coverage, governance/config/doc
drift signal, and BUILD.md tracking-id coverage for the current Claude Code session (escalation
#1875, researcher design approval 2026-09-24).

**Detection only**, per the approved design split (escalation #1875 resolution, v4): this handler
mechanically detects gaps and always persists a report. It never writes a remediation itself —
REMEDIATION is the separate `.claude/commands/session-close.md` slash command's job, driven by
Claude reading this report plus the session's own transcript content. Only Claude, reading the
real conversation, can compose a faithful escalation comment or supersession note; this handler can
only say WHAT looks missing, not write the sentence that fills it.

Three checks:
  (a) escalation update coverage — every escalation id this session actually touched via
      `Escalation.ps1` (found by regexing the session's own JSONL transcript for the CLI's own
      `raised — #N` / `escalation #N vV ->` confirmation lines — the same text this app's own
      Escalation.ps1 already prints on every write) must have a matching `escalation_history` row
      at least at the version the transcript shows. A gap here means: something the transcript
      shows as touched isn't reflected in escalation_history at that version — Claude reviews and
      adds the missing update (researcher's own instruction: "add additional entries").
  (b) governance/config/doc drift — reports which of GOVERNANCE.md/CLAUDE.md/USER-GUIDE.md changed
      in the session's git diff window. Whether chat content that SHOULD have updated governance/
      config actually did, and whether superseded text is properly marked, is NOT mechanically
      checkable (no chat-transcript-to-decision mapping exists) — left as a flagged judgement call
      for Claude to make reading the transcript, per escalation #1875's own design.
  (c) BUILD.md coverage — any `iba/app/**` file changed in the session's git diff window (excluding
      report/doc output) with no corresponding change to `iba/app/BUILD.md` itself is a gap
      (governance.build_md_on_code_change).

Read-only against iba.db + the filesystem (git, the session's own JSONL transcript under the user
profile). Always persists a report (governance.reports_must_persist). Never escalates for a
`gaps-found` condition — mapped via `cfg_on_fail` to `report-continue` (non-blocking), per the
researcher's explicit instruction that remediation must not create an additional approval cycle.
"""

from __future__ import annotations

import datetime
import json
import os
import pathlib
import re
import subprocess

from .base import Ctx, Outcome, ok, fail
from ..lib import reportkit

_RAISED_RE = re.compile(r"raised[^#\n]{0,4}#(\d+)\. Update with")
_UPDATED_RE = re.compile(r"escalation #(\d+) v(\d+) ->")

_DOC_WATCH = ("iba/app/GOVERNANCE.md", "CLAUDE.md", "iba/app/USER-GUIDE.md")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _repo_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent.parent.parent.parent


def _session_state() -> dict | None:
    state_path = _repo_root() / ".claude" / ".session-boundary-state.json"
    if not state_path.exists():
        return None
    try:
        return json.loads(state_path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _transcript_path(session_id: str) -> pathlib.Path | None:
    home = pathlib.Path(os.path.expanduser("~"))
    matches = list(home.glob(f".claude/projects/*/{session_id}.jsonl"))
    return matches[0] if matches else None


def _scan_transcript(path: pathlib.Path) -> dict[int, int | None]:
    """{escalation_id: highest version this session's own CLI output shows, or 1 if only a bare
    'raised' confirmation was seen (no version-bearing Update yet this session)}."""
    touched: dict[int, int | None] = {}
    with path.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            for m in _RAISED_RE.finditer(line):
                eid = int(m.group(1))
                touched.setdefault(eid, touched.get(eid) or 1)
            for m in _UPDATED_RE.finditer(line):
                eid, ver = int(m.group(1)), int(m.group(2))
                touched[eid] = max(touched.get(eid) or 0, ver)
    return touched


def _commit_before(iso_ts: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-list", "-1", f"--before={iso_ts}", "HEAD"],
            cwd=_repo_root(), capture_output=True, text=True, timeout=15)
        return out.stdout.strip() or None
    except Exception:
        return None


def _git_changed_files(base_commit: str) -> list[str]:
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", base_commit, "HEAD"],
            cwd=_repo_root(), capture_output=True, text=True, timeout=15)
        tracked = [l.strip() for l in out.stdout.splitlines() if l.strip()]
        out2 = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=_repo_root(), capture_output=True, text=True, timeout=15)
        untracked = [l[3:].strip() for l in out2.stdout.splitlines() if l.strip()]
        return sorted(set(tracked) | set(untracked))
    except Exception:
        return []


def _write_report(ctx: Ctx, findings: dict) -> pathlib.Path:
    path = pathlib.Path(ctx.cfg.required_setting("session_close.report_path"))
    intro = [
        f"> Generated {_now()} by `session.close`. Detection only (escalation #1875) — "
        f"remediation is performed separately by Claude via `.claude/commands/session-close.md`, "
        f"reading this report plus the session's own transcript.",
        "",
        f"- session_id: `{findings.get('session_id')}`",
        f"- session started: {findings.get('session_start')}",
        f"- transcript found: {findings.get('transcript_found')}",
        f"- escalation-update gaps: **{len(findings.get('escalation_gaps', []))}**",
        f"- BUILD.md gaps: **{len(findings.get('build_gaps', []))}**",
    ]

    esc_lines: list[str] = []
    if findings.get("escalation_touched"):
        esc_lines.append("Escalations touched this session (id, highest version seen in "
                         "transcript vs. live `escalation_history`):")
        for eid, ver in findings["escalation_touched"]:
            esc_lines.append(f"- #{eid}: transcript v{ver if ver is not None else '?'}")
    else:
        esc_lines.append("No escalation touched this session (per transcript scan).")
    if findings.get("escalation_gaps"):
        esc_lines.append("")
        esc_lines.append("**GAPS** — touched in transcript, `escalation_history` behind it. Per "
                         "the researcher's instruction (2026-09-24), add the missing entries — "
                         "capture researcher update verbatim, design debates, design decisions, "
                         "and anything skipped/postponed/ignored, not just a summary:")
        for g in findings["escalation_gaps"]:
            esc_lines.append(f"- #{g['id']}: transcript shows v{g['transcript_version']}, live "
                             f"`escalation_history` is at v{g['live_version']}")

    gov_lines = [
        f"Files changed this session under governance/doc scope: "
        f"{', '.join(findings.get('governance_files_changed', [])) or '(none)'}.",
        "",
        "Whether chat content that SHOULD have updated governance/config actually did, and "
        "whether any now-superseded text is properly marked superseded/retired, is a judgement "
        "call for Claude to make reading the actual session transcript — not mechanically checked "
        "here (no chat-content-to-decision mapping exists to check against). If the session's own "
        "SESSION-LOG 'decisions made' section names a decision with no matching change among the "
        "files above, that is the signal to look at.",
    ]

    build_lines: list[str] = []
    if findings.get("build_gaps"):
        build_lines.append("**GAPS** — `iba/app/**` files changed this session with no "
                           "`iba/app/BUILD.md` entry added (governance.build_md_on_code_change):")
        for f in findings["build_gaps"]:
            build_lines.append(f"- {f}")
    else:
        build_lines.append("No BUILD.md gap detected — either no `iba/app/**` code changed this "
                           "session, or `BUILD.md` was updated alongside it.")

    sections = {
        "summary": [f"{len(findings.get('escalation_gaps', []))} escalation-update gap(s), "
                    f"{len(findings.get('build_gaps', []))} BUILD.md gap(s)."],
        "escalation_gaps": esc_lines,
        "governance_gaps": gov_lines,
        "build_gaps": build_lines,
    }
    L = reportkit.render_scaffold(ctx.db.conn, "session.close", sections, intro=intro)
    return reportkit.write_report(ctx.db.conn, "session.close", path, L)


def check(ctx: Ctx) -> Outcome:
    db = ctx.db
    state = _session_state()
    findings: dict = {
        "session_id": state.get("session_id") if state else None,
        "session_start": state.get("at") if state else None,
        "transcript_found": False,
        "escalation_touched": [],
        "escalation_gaps": [],
        "build_gaps": [],
        "governance_files_changed": [],
    }

    if not state or not state.get("session_id"):
        findings["error"] = ("no .claude/.session-boundary-state.json / session_id — cannot "
                             "locate this session's transcript")
        report_path = _write_report(ctx, findings)
        return fail("gaps-found", f"session id unavailable — checks skipped, report {report_path}",
                   escalation_gap_count=0, build_gap_count=0)

    session_id = state["session_id"]
    tpath = _transcript_path(session_id)
    if tpath:
        findings["transcript_found"] = True
        touched = _scan_transcript(tpath)
        findings["escalation_touched"] = sorted(touched.items())
        for eid, ver in touched.items():
            rows = db.rows(
                "SELECT version FROM escalation_history WHERE escalation_id=? "
                "ORDER BY version DESC LIMIT 1", (eid,))
            live_version = rows[0]["version"] if rows else 0
            if ver is not None and live_version < ver:
                findings["escalation_gaps"].append(
                    {"id": eid, "transcript_version": ver, "live_version": live_version})
    else:
        findings["error"] = f"transcript file not found for session_id={session_id}"

    session_start = state.get("at")
    base_commit = _commit_before(session_start) if session_start else None
    changed = _git_changed_files(base_commit) if base_commit else []
    findings["changed_files"] = changed
    code_changed = [f for f in changed
                    if f.startswith("iba/app/") and not f.startswith("iba/app/reports/")
                    and not f.endswith(".md") and not f.endswith(".db")]
    build_md_changed = "iba/app/BUILD.md" in changed
    findings["governance_files_changed"] = [f for f in _DOC_WATCH if f in changed]

    if code_changed and not build_md_changed:
        findings["build_gaps"] = code_changed

    report_path = _write_report(ctx, findings)

    gap_count = len(findings["escalation_gaps"]) + len(findings["build_gaps"])
    if gap_count == 0:
        return ok(f"session-close clean: 0 gaps — report written to {report_path}",
                 escalation_gap_count=0, build_gap_count=0)
    return fail("gaps-found",
               f"{len(findings['escalation_gaps'])} escalation-update gap(s), "
               f"{len(findings['build_gaps'])} BUILD.md gap(s) — report {report_path}",
               escalation_gap_count=len(findings["escalation_gaps"]),
               build_gap_count=len(findings["build_gaps"]))
