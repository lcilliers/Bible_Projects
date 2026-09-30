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


_CALL_MARKER = "Session-Close.ps1"
_TAIL_BYTES = 200_000


def _transcripts_dir() -> pathlib.Path:
    """This project's transcript folder: Claude Code names it after the project path with every
    non-alphanumeric character replaced by '-' (C:\\Bible_study_projects -> C--Bible-study-projects)."""
    mangled = re.sub(r"[^A-Za-z0-9]", "-", str(_repo_root()))
    return pathlib.Path(os.path.expanduser("~")) / ".claude" / "projects" / mangled


def _tail_contains(path: pathlib.Path, marker: str) -> bool:
    try:
        with path.open("rb") as fh:
            fh.seek(0, os.SEEK_END)
            fh.seek(max(0, fh.tell() - _TAIL_BYTES))
            return marker.encode("utf-8") in fh.read()
    except Exception:
        return False


def _identify_session() -> tuple[str | None, pathlib.Path | None, str]:
    """(session_id, transcript_path, method) for the session this close is RUNNING IN (escalation
    #1894 option A, 2026-09-30). Never reads the shared .session-boundary-state.json: that file
    is overwritten by whichever session in this folder started or resumed last, which made closes
    v18-v20 scan another session. Order:
      1. CLAUDE_CODE_SESSION_ID, which Claude Code sets for the commands it runs;
      2. else the most recently written transcript whose recent content contains the running
         Session-Close.ps1 call.
    No match -> (None, None, reason). There is no fallback to any other session."""
    tdir = _transcripts_dir()
    env_id = os.environ.get("CLAUDE_CODE_SESSION_ID")
    if env_id:
        path = tdir / f"{env_id}.jsonl"
        if path.exists():
            return env_id, path, "CLAUDE_CODE_SESSION_ID"
        return None, None, (f"CLAUDE_CODE_SESSION_ID={env_id} but no transcript at {path}")
    if not tdir.is_dir():
        return None, None, f"transcript folder not found: {tdir}"
    for path in sorted(tdir.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True):
        if _tail_contains(path, _CALL_MARKER):
            return path.stem, path, f"most recent transcript containing the {_CALL_MARKER} call"
    return None, None, (f"no CLAUDE_CODE_SESSION_ID and no transcript in {tdir} contains the "
                        f"running {_CALL_MARKER} call")


def _session_record(session_id: str) -> dict | None:
    """This session's own boundary record, written by .claude/hooks/session_boundary_track.py."""
    path = _repo_root() / ".claude" / "session-boundary" / f"{session_id}.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


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
        f"- session_id: `{findings.get('session_id')}` (identified by: "
        f"{findings.get('session_id_method')})",
        f"- session started: {findings.get('session_start')}",
        f"- transcript found: {findings.get('transcript_found')}",
        *([f"- **problem:** {findings['error']}"] if findings.get("error") else []),
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
    session_id, tpath, method = _identify_session()
    record = _session_record(session_id) if session_id else None
    findings: dict = {
        "session_id": session_id,
        "session_id_method": method,
        "session_start": (record.get("first_seen_at") or record.get("at")) if record else None,
        "transcript_found": False,
        "escalation_touched": [],
        "escalation_gaps": [],
        "build_gaps": [],
        "governance_files_changed": [],
    }

    if not session_id:
        findings["error"] = f"cannot identify the session this close is running in: {method}"
        report_path = _write_report(ctx, findings)
        return fail("gaps-found", f"session id unavailable — checks skipped, report {report_path}",
                   escalation_gap_count=0, build_gap_count=0)

    if not record:
        findings["error"] = (f"no per-session boundary record .claude/session-boundary/"
                             f"{session_id}.json (session started before #1894's hook change, "
                             f"or the SessionStart hook did not fire) — git diff window skipped")
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
    session_start = findings["session_start"]
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
