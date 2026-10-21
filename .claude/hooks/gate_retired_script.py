#!/usr/bin/env python
"""Claude Code PreToolUse hook (Bash, PowerShell): refuses a command that RUNS a retired script
unless the researcher has approved that script's use (#2200).

Retired: a project file under any `archive/` folder, a file whose `cfg_utility` row is inactive,
or a path that no longer exists live but sits in its folder's `archive/`. A script counts as run
when it follows a Python launcher (`python x.py`, `python -m pkg.mod`), follows `-File`, or is the
first word of a command segment (`.\\x.ps1`, `& "x.ps1"`, also inside `pwsh -Command "..."`).
Reading a retired file (cat, Get-Content, the Read tool) is never blocked.

Approved: an escalation whose text (any version's short_description, context, comment, tried or
resolution) names the script's repo-relative path, with an `approved` version written by the
Researcher, and not withdrawn or superseded. One approval covers that one script.

An internal error (no database, a locked database) allows the command and is logged to
.claude/.gate-retired-script.log, so a broken check never blocks all work. IBA_GATE_DB overrides
the database path (tests only).
"""
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

LAUNCH_RX = re.compile(r"(?:^|[\s;&|(\"'])(?:python3?|py)(?:\.exe)?\s+(.+)", re.IGNORECASE)
FILE_RX = re.compile(r"-File\s+[\"']?([^\"'\s]+\.ps1)", re.IGNORECASE)
SHELL_PREFIX_RX = re.compile(r"^(?:pwsh|powershell)(?:\.exe)?\s+(?:-\w+\s+)*?-Command\s+", re.IGNORECASE)


def _deny(reason: str) -> None:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "deny",
        "permissionDecisionReason": reason}}))


def _python_targets(cmd: str) -> list[tuple[str, str]]:
    """[(kind, value)] for each Python launch: ('path', 'x.py') or ('module', 'pkg.mod')."""
    out = []
    for m in LAUNCH_RX.finditer(cmd):
        tokens = re.split(r"\s+", m.group(1).strip())
        i = 0
        while i < len(tokens):
            t = tokens[i].strip("\"'")
            if t == "-m" and i + 1 < len(tokens):
                out.append(("module", tokens[i + 1].strip("\"'")))
                break
            if t == "-c":
                break
            if t.startswith("-"):
                i += 1
                continue
            if t.lower().endswith(".py"):
                out.append(("path", t))
            break
    return out


def _ps1_targets(cmd: str) -> list[str]:
    found = [m.group(1) for m in FILE_RX.finditer(cmd)]
    for seg in re.split(r"[;\n|]|&&|\|\|", cmd):
        s = seg.strip()
        for _ in range(3):
            s = s.lstrip("&").strip().strip("\"'").strip()
            s2 = SHELL_PREFIX_RX.sub("", s)
            if s2 == s:
                break
            s = s2
        first = s.split()[0].strip("\"'") if s.split() else ""
        if first.lower().endswith(".ps1"):
            found.append(first)
    return found


def _rel(raw: str, root: Path, cwd: Path) -> str | None:
    p = Path(raw.replace("\\", "/"))
    p = p if p.is_absolute() else (cwd / p)
    try:
        return PurePosixPath(p.resolve().relative_to(root.resolve()).as_posix()).as_posix()
    except (ValueError, OSError):
        return None


def _retired(rel: str, root: Path, conn) -> bool:
    if "archive" in PurePosixPath(rel).parts:
        return True
    row = conn.execute("SELECT inactive FROM cfg_utility WHERE file_path=?", (rel,)).fetchone()
    if row is not None and row[0] == 1:
        return True
    p = root / rel
    return not p.exists() and (p.parent / "archive" / p.name).exists()


def _approved(rel: str, conn) -> bool:
    variants = {rel, rel.replace("/", "\\")}
    ids = set()
    for v in variants:
        like = f"%{v}%"
        for (eid,) in conn.execute(
                "SELECT DISTINCT escalation_id FROM escalation_history WHERE "
                "coalesce(short_description,'')||' '||coalesce(context,'')||' '||coalesce(comment,'')"
                "||' '||coalesce(tried,'')||' '||coalesce(resolution,'') LIKE ?", (like,)):
            ids.add(eid)
    for eid in ids:
        state = conn.execute("SELECT state FROM escalation WHERE id=?", (eid,)).fetchone()
        if not state or state[0] in ("withdraw", "supersede"):
            continue
        ok = conn.execute("SELECT 1 FROM escalation_history WHERE escalation_id=? AND "
                          "next_action='approved' AND originator='Researcher'", (eid,)).fetchone()
        if ok:
            return True
    return False


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    root = Path(payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
    cmd = (payload.get("tool_input") or {}).get("command") or ""
    try:
        db = os.environ.get("IBA_GATE_DB") or str(root / "iba" / "app" / "db" / "iba.db")
        conn = sqlite3.connect(f"file:{Path(db).as_posix()}?mode=ro", uri=True, timeout=5)
        refs = []
        for kind, val in _python_targets(cmd):
            if kind == "module":
                refs.append(val.replace(".", "/") + ".py")
            else:
                refs.append(val)
        refs += _ps1_targets(cmd)
        blocked = []
        for raw in refs:
            rel = _rel(raw, root, root)
            if rel and _retired(rel, root, conn) and not _approved(rel, conn):
                blocked.append(rel)
        conn.close()
    except Exception as exc:
        try:
            with open(root / ".claude" / ".gate-retired-script.log", "a", encoding="utf-8") as fh:
                now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                fh.write(json.dumps({"at": now, "error": repr(exc), "command": cmd[:500]}) + "\n")
        except Exception:
            pass
        print(json.dumps({}))
        return
    if blocked:
        _deny("Retired script, not approved for use (#2200): " + ", ".join(sorted(set(blocked)))
              + ". To use it, raise an escalation naming the path and get the researcher's "
                "approval; reading the file is allowed.")
        return
    print(json.dumps({}))


if __name__ == "__main__":
    main()
