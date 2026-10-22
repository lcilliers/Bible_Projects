"""sessionwindow.py -- the running Claude Code session, its start, its git window and its transcript
(#2173), shared by start-up and close.

Session identity (#1894): CLAUDE_CODE_SESSION_ID, else the newest transcript containing the given
marker; never the shared .session-boundary-state.json. The session start is this session's own
boundary record (.claude/session-boundary/{id}.json, written by the SessionStart hook).
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import subprocess

_TAIL_BYTES = 200_000


GIT_ROOT = pathlib.Path(__file__).resolve().parents[3]     # git always runs in the repository


def repo_root() -> pathlib.Path:
    """Root for project files (the same folder as GIT_ROOT; a test may point it elsewhere)."""
    return GIT_ROOT


def transcripts_dir() -> pathlib.Path:
    """Claude Code names the folder after the project path with every non-alphanumeric character
    replaced by '-' (C:\\Bible_study_projects -> C--Bible-study-projects)."""
    mangled = re.sub(r"[^A-Za-z0-9]", "-", str(GIT_ROOT))
    return pathlib.Path(os.path.expanduser("~")) / ".claude" / "projects" / mangled


def _tail_contains(path: pathlib.Path, marker: str) -> bool:
    try:
        with path.open("rb") as fh:
            fh.seek(0, os.SEEK_END)
            fh.seek(max(0, fh.tell() - _TAIL_BYTES))
            return marker.encode("utf-8") in fh.read()
    except Exception:
        return False


def identify(marker: str) -> tuple[str | None, pathlib.Path | None, str]:
    """(session_id, transcript_path, how). No match -> (None, None, reason); no fallback."""
    tdir = transcripts_dir()
    env_id = os.environ.get("CLAUDE_CODE_SESSION_ID")
    if env_id:
        path = tdir / f"{env_id}.jsonl"
        if path.exists():
            return env_id, path, "CLAUDE_CODE_SESSION_ID"
        return None, None, f"CLAUDE_CODE_SESSION_ID={env_id} but no transcript at {path}"
    if not tdir.is_dir():
        return None, None, f"transcript folder not found: {tdir}"
    for path in sorted(tdir.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True):
        if _tail_contains(path, marker):
            return path.stem, path, f"most recent transcript containing the {marker} call"
    return None, None, f"no CLAUDE_CODE_SESSION_ID and no transcript in {tdir} contains {marker}"


def boundary_record(session_id: str) -> dict | None:
    path = repo_root() / ".claude" / "session-boundary" / f"{session_id}.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def session_start(record: dict | None) -> str | None:
    return (record.get("first_seen_at") or record.get("at")) if record else None


def git(*args: str, timeout: int = 20) -> str:
    out = subprocess.run(["git", *args], cwd=GIT_ROOT, capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=timeout)
    return out.stdout


def commit_before(iso_ts: str) -> str | None:
    try:
        return git("rev-list", "-1", f"--before={iso_ts}", "HEAD").strip() or None
    except Exception:
        return None


def changed_files(base_commit: str) -> list[str]:
    """Committed since base_commit, plus uncommitted and untracked (repo-relative, '/')."""
    try:
        tracked = [l.strip() for l in git("diff", "--name-only", base_commit, "HEAD").splitlines()
                   if l.strip()]
        status = []
        for l in git("status", "--porcelain", "--untracked-files=all").splitlines():
            if not l.strip():
                continue
            p = l[3:].strip()
            if " -> " in p:
                p = p.split(" -> ", 1)[1]
            status.append(p.strip('"'))
        return sorted(set(tracked) | set(status))
    except Exception:
        return []


def diff_added_text(base_commit: str, path: str) -> str:
    """Lines added to `path` since base_commit, committed or not."""
    try:
        d = git("diff", base_commit, "--", path)
    except Exception:
        return ""
    return "\n".join(l[1:] for l in d.splitlines() if l.startswith("+") and not l.startswith("+++"))


def file_at(commit: str, path: str) -> str | None:
    try:
        out = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=GIT_ROOT,
                             capture_output=True, text=True, encoding="utf-8", errors="replace",
                             timeout=20)
        return out.stdout if out.returncode == 0 else None
    except Exception:
        return None


def commit_exists(h: str) -> bool:
    try:
        r = subprocess.run(["git", "cat-file", "-e", f"{h}^{{commit}}"], cwd=GIT_ROOT,
                           capture_output=True, timeout=15)
        return r.returncode == 0
    except Exception:
        return False


_RULES_SHOWN = "Rules for this operation ("   # the point-of-use hook's deliberate refusal (#2209)


def _operation(tool: str, inp: dict) -> str:
    """A short operation key for a tool call: a PS script with its -Action/-Step, a command's first
    word, or the top folder a file is written in."""
    if tool in ("Bash", "PowerShell"):
        cmd = inp.get("command", "")
        m = re.search(r"([\w.-]+\.ps1)\b(?:.*?-(Action|Step)\s+['\"]?([\w.-]+))?", cmd, re.S)
        if m:
            return f"{m.group(1)} -{m.group(2)} {m.group(3)}" if m.group(2) else m.group(1)
        first = re.sub(r"^(?:(?:cd|export)\s+\S+\s*&&\s*|\w+=\S+\s*(?:&&\s*)?)+", "", cmd.strip()).split()
        return f"{tool}: {first[0] if first else ''}"
    if tool in ("Edit", "Write", "Read"):
        p = (inp.get("file_path") or "").replace("\\", "/")
        rel = p.split("Bible_study_projects/", 1)[-1]
        return f"{tool}: {rel.split('/')[0] if '/' in rel else rel}"
    return tool


def failed_calls(transcript: pathlib.Path) -> list[dict]:
    """Claude's tool calls in the session that came back as errors (#2207 part 3): [{at, tool,
    operation, kind, text}]. `kind` is the error's first line with digits blanked, so the same
    mistake made twice has the same kind. The point-of-use hook's rule display is left out: it is a
    deliberate first-use refusal, not a failure."""
    calls, out, seen = {}, [], set()
    with transcript.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get("isSidechain"):
                continue
            content = (e.get("message") or {}).get("content")
            if not isinstance(content, list):
                continue
            for c in content:
                if not isinstance(c, dict):
                    continue
                if c.get("type") == "tool_use":
                    calls[c.get("id")] = (c.get("name") or "", c.get("input") or {})
                elif c.get("type") == "tool_result" and c.get("is_error"):
                    if c.get("tool_use_id") in seen:     # the transcript can hold a result twice
                        continue
                    seen.add(c.get("tool_use_id"))
                    body = c.get("content")
                    if isinstance(body, list):
                        body = "\n".join(x.get("text", "") for x in body if isinstance(x, dict))
                    body = str(body or "")
                    if _RULES_SHOWN in body:
                        continue
                    tool, inp = calls.get(c.get("tool_use_id"), ("", {}))
                    lines = [ln.strip() for ln in body.splitlines() if ln.strip()
                             and not re.fullmatch(r"Exit code \d+", ln.strip())]
                    # a Python traceback is named by its exception line, not its common header
                    exc = [ln for ln in lines if re.match(r"[\w.]+(Error|Exception|Exit)\b", ln)]
                    first = (exc or lines)[-1] if lines and lines[0].startswith("Traceback") else \
                        (lines[0] if lines else "")
                    first = re.sub(r"<[^>]+>", "", first)
                    out.append(dict(at=e.get("timestamp") or "", tool=tool,
                                    operation=_operation(tool, inp),
                                    kind=re.sub(r"\d+", "#", first)[:100], text=first[:200]))
    return out


def user_messages(transcript: pathlib.Path) -> list[dict]:
    """The researcher's own messages in the session: [{uuid, at, text}]. Tool results, hook and
    system text, and Claude Code's command wrappers are not the researcher's words; a slash command
    is kept as its command name and arguments."""
    out = []
    with transcript.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get("type") != "user" or e.get("isMeta") or e.get("isSidechain"):
                continue
            msg = e.get("message") or {}
            content = msg.get("content")
            if isinstance(content, list):
                if any(isinstance(c, dict) and c.get("type") == "tool_result" for c in content):
                    continue
                content = "\n".join(c.get("text", "") for c in content
                                    if isinstance(c, dict) and c.get("type") == "text")
            if not isinstance(content, str):
                continue
            text = content
            cmd = re.search(r"<command-name>(.*?)</command-name>", text, re.S)
            if cmd:
                args = re.search(r"<command-args>(.*?)</command-args>", text, re.S)
                text = (cmd.group(1).strip() + " " + (args.group(1).strip() if args else "")).strip()
            text = re.sub(r"<system-reminder>.*?</system-reminder>", "", text, flags=re.S)
            text = re.sub(r"<(local-command-stdout|command-message|command-args|"
                          r"local-command-caveat)>.*?</\1>", "", text, flags=re.S).strip()
            if not text or text.startswith("Stop hook feedback") or text.startswith("[Request interrupted"):
                continue
            out.append(dict(uuid=e.get("uuid") or "", at=e.get("timestamp") or "", text=text))
    return out


def normalise(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", (text or "").lower())).strip()


def last_close_findings(cfg) -> list[str]:
    """S6 (#2173): how the last session ended, checked at start. A clean end is a tree with
    nothing uncommitted, a newest commit that is a session-close's final commit (its message
    carries session_close.final_commit_marker: the SC13 second commit), and a newest session log
    whose git section names a commit that exists. Each departure is one finding line."""
    out: list[str] = []
    marker = cfg.required_setting("session_close.final_commit_marker")
    status = [l for l in git("status", "--porcelain", "--untracked-files=all").splitlines()
              if l.strip()]
    if status:
        out.append(f"the working tree is not clean: {len(status)} path(s) uncommitted, e.g. "
                   + "; ".join(l[3:] for l in status[:6]))
        logs = [l[3:] for l in status if "SESSION-LOG-" in l]
        if logs:
            out.append("an uncommitted session log: " + "; ".join(logs))
    sep = chr(31)
    log = [l.split(sep) for l in git("log", "-40", f"--format=%h{sep}%ci{sep}%s").splitlines() if l]
    if log and marker.lower() not in log[0][2].lower():
        since = []
        for h, when, subj in log:
            if marker.lower() in subj.lower():
                break
            since.append(f"{h} {when[:16]} {subj[:70]}")
        out.append(f"the last session did not end with a completed session-close (the newest "
                   f"commit is not a '{marker}' commit); commits since the last close: "
                   + " | ".join(since[:8]) + (" ..." if len(since) > 8 else ""))
    ldir = repo_root() / cfg.required_setting("governance.session_log_dir")
    logs = sorted(ldir.glob("SESSION-LOG-*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not logs:
        out.append(f"no session log in {ldir}")
    else:
        text = logs[0].read_text(encoding="utf-8", errors="replace")
        last_head = cfg.required_setting("session_close.log_sections")[-1]
        m = re.search(r"^#{1,6}\s+" + re.escape(last_head) + r".*$", text, re.M | re.I) or \
            re.search(r"^#{1,6}\s+.*\bgit\b.*$", text, re.M | re.I)   # a log older than the headings
        sec = text[m.end():] if m else ""
        hashes = [h for h in re.findall(r"\b[0-9a-f]{7,40}\b", sec) if any(c.isalpha() for c in h)]
        if not any(commit_exists(h) for h in hashes):
            out.append(f"the newest session log ({logs[0].name}) names no existing commit in its "
                       f"'{last_head}' section")
    return out
