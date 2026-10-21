#!/usr/bin/env python
"""Claude Code PreToolUse hook (Bash, PowerShell, Edit, Write): puts the rules of an operation in
front of Claude before its first use in a session (#2209).

An operation is a PS tool (with its -Action or -Step), a command family (git commit/push, a
migration run, a database query) or a file written (its repo-relative path). The rules linked to it
come from cfg_rule_scope; a PS tool also brings the method rules (cfg_method_rule) of its work
package's steps, and its usage lines from iba/app/USER-GUIDE.md. Rules with scope 'general' are not
shown here: the start routine delivers them.

The first time a call touches a rule (or a tool usage) not yet shown in this session, the call is
refused once and the reason carries the full text from the database. The same call, re-issued,
passes. What was shown is kept in .claude/.rules-shown.json for the current session only.

An internal error (no database, a locked database) allows the call and is logged to
.claude/.rules-at-point-of-use.log, so a broken check never blocks all work. IBA_RULES_DB overrides
the database path (tests only).
"""
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

PS_RX = re.compile(r"([\w.-]+\.ps1)\b", re.IGNORECASE)
ACTION_RX = re.compile(r"-(Action|Step)\s+[\"']?([\w.-]+)", re.IGNORECASE)
MIGRATION_RX = re.compile(r"iba[/\\]app[/\\]migration[/\\][\w.-]+\.py")
SQL_RX = re.compile(r"\bsqlite3\b|\.db\b")
# only a command counts, not text that mentions one (a heredoc body, a commit message): each is
# matched at the start of a line or command segment
SEG_SPLIT_RX = re.compile(r"\n|;|&&|\|\||\|")
PS_START_RX = re.compile(r"^(?:&\s*)?[\"']?\.?[\\/]?[\w\\/.-]*\.ps1\b|^(?:pwsh|powershell)(?:\.exe)?\s.*-File\s",
                         re.IGNORECASE)
GIT_START_RX = re.compile(r"^(?:cd\s+\S+\s*)?git\s+(?:-C\s+\S+\s+)?(commit|push)\b")
PY_START_RX = re.compile(r"^(?:\$env:\S+\s*)?(?:python3?|py)(?:\.exe)?\s", re.IGNORECASE)


def _allow() -> None:
    print(json.dumps({}))


def _deny(reason: str) -> None:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "deny",
        "permissionDecisionReason": reason}}))


def _log(root: Path, msg: str) -> None:
    try:
        with open(root / ".claude" / ".rules-at-point-of-use.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now(timezone.utc).isoformat()} {msg}\n")
    except OSError:
        pass


def _glob_rx(glob: str) -> re.Pattern:
    out, i = "", 0
    while i < len(glob):
        if glob.startswith("**/", i):
            out, i = out + "(?:.*/)?", i + 3
        elif glob.startswith("**", i):
            out, i = out + ".*", i + 2
        elif glob[i] == "*":
            out, i = out + "[^/]*", i + 1
        else:
            out, i = out + re.escape(glob[i]), i + 1
    return re.compile(out + r"\Z", re.IGNORECASE)


def operations(tool: str, tin: dict, root: Path) -> list[tuple[str, str]]:
    """[(kind, value)]: ('ps', 'X.ps1') and ('ps', 'X.ps1 -Action Y'), ('command', 'git' |
    'migration' | 'sqlite'), ('path', 'repo/relative/path')."""
    ops = []
    if tool in ("Bash", "PowerShell"):
        cmd = tin.get("command", "")
        for seg in (s.strip() for s in SEG_SPLIT_RX.split(cmd)):
            if PS_START_RX.match(seg):
                m = PS_RX.search(seg)
                script = m.group(1)
                ops.append(("ps", script))
                a = ACTION_RX.search(seg, m.end())
                if a:
                    ops.append(("ps", f"{script} -{a.group(1).capitalize()} {a.group(2)}"))
            elif GIT_START_RX.match(seg):
                ops.append(("command", "git"))
            elif PY_START_RX.match(seg):
                if MIGRATION_RX.search(seg):
                    ops.append(("command", "migration"))
                elif SQL_RX.search(seg):
                    ops.append(("command", "sqlite"))
        ops = list(dict.fromkeys(ops))
    elif tool in ("Edit", "Write"):
        p = tin.get("file_path", "")
        try:
            rel = Path(p).resolve().relative_to(root.resolve()).as_posix()
        except (ValueError, OSError):
            return []
        ops.append(("path", rel))
    return ops


def rules_for(conn, ops) -> list[tuple[str, str, str]]:
    """[(ref, key, text)] linked to the operations, general rules excluded, in ref order."""
    scopes = conn.execute("SELECT rule_ref, scope_kind, scope_value FROM cfg_rule_scope "
                          "WHERE inactive=0 AND scope_kind != 'general'").fetchall()
    refs = set()
    for kind, value in ops:
        for ref, sk, sv in scopes:
            if sk != kind:
                continue
            if kind == "path":
                if _glob_rx(sv).match(value):
                    refs.add(ref)
            elif sv.lower() == value.lower():
                refs.add(ref)
    out = []
    for ref in refs:
        t, _, k = ref.partition(":")
        if t == "B":
            r = conn.execute("SELECT class || '.' || rule_key, rule_text FROM cfg_behaviour_rule "
                             "WHERE id=? AND active=1", (int(k),)).fetchone()
        elif t == "E":
            r = conn.execute("SELECT rule_key, rule_text FROM cfg_escalation WHERE id=? AND active=1",
                             (int(k),)).fetchone()
        else:
            r = conn.execute("SELECT key, value FROM cfg_setting WHERE key=? AND inactive=0",
                             (k,)).fetchone()
        if r:
            out.append((ref, r[0], r[1]))
    # method rules of each PS tool's steps
    for kind, value in ops:
        if kind == "ps" and " " not in value:
            for mid, mkey, mtext in conn.execute(
                    "SELECT m.id, m.rule_key, m.rule_text FROM cfg_method_rule m "
                    "JOIN cfg_step s ON s.step = m.step JOIN cfg_work_package w ON w.name = s.work_package "
                    "WHERE m.active=1 AND COALESCE(s.inactive,0)=0 AND w.ps_script LIKE ? "
                    "ORDER BY m.id", (f"%/{value}",)):
                out.append((f"M:{mid}", mkey, mtext))
    key = lambda r: (r[0][0], int(r[0][2:]) if r[0][2:].isdigit() else 0, r[0])
    return sorted(set(out), key=key)


def usage_for(root: Path, ops) -> list[tuple[str, list[str]]]:
    """[(operation, USER-GUIDE.md lines)] for each PS tool operation: the guide's command lines
    naming the script (and the action, when one is given), with their continuation lines."""
    try:
        guide = (root / "iba" / "app" / "USER-GUIDE.md").read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    out = []
    with_action = {v.split(" ")[0] for k, v in ops if k == "ps" and " " in v}
    for kind, value in ops:
        if kind != "ps" or value in with_action:   # the action's own lines are enough
            continue
        script, _, action = value.partition(" ")
        lines, i = [], 0
        while i < len(guide):
            ln = guide[i]
            if script.lower() in ln.lower() and (not action or action.split()[-1].lower() in ln.lower()):
                lines.append(ln)
                while ln.rstrip().endswith("`") and i + 1 < len(guide):
                    i += 1
                    ln = guide[i]
                    lines.append(ln)
            i += 1
        out.append((value, lines[:20]))
    return out


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    root = Path(payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
    try:
        ops = operations(payload.get("tool_name", ""), payload.get("tool_input") or {}, root)
        if not ops:
            _allow()
            return
        db = os.environ.get("IBA_RULES_DB") or str(root / "iba" / "app" / "db" / "iba.db")
        if not os.path.isfile(db):
            _allow()
            return
        conn = sqlite3.connect(f"file:{Path(db).as_posix()}?mode=ro", uri=True, timeout=2)
        rules = rules_for(conn, ops)
        conn.close()
        usage = [u for u in usage_for(root, ops) if u[1]]
        state_path = root / ".claude" / ".rules-shown.json"
        session = payload.get("session_id", "")
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            state = {}
        if state.get("session_id") != session:
            state = {"session_id": session, "shown": []}
        shown = set(state["shown"])
        new_rules = [r for r in rules if r[0] not in shown]
        new_usage = [u for u in usage if f"usage:{u[0]}" not in shown]
        if not new_rules and not new_usage:
            _allow()
            return
        state["shown"] = sorted(shown | {r[0] for r in new_rules} | {f"usage:{u[0]}" for u in new_usage})
        state_path.write_text(json.dumps(state), encoding="utf-8")
        labels = ", ".join(sorted({v for _, v in ops}))
        parts = [f"Rules for this operation ({labels}), shown once per session before first use "
                 f"(#2209, cfg_rule_scope). Check the call against them, then re-issue it."]
        for op, lines in new_usage:
            parts.append(f"\nHow to run {op} (iba/app/USER-GUIDE.md):\n" + "\n".join(lines))
        if new_rules:
            parts.append("\nRules:")
            parts += [f"- {ref} {k}: {t}" for ref, k, t in new_rules]
        _deny("\n".join(parts))
    except Exception as e:  # a broken check never blocks work
        _log(root, f"error: {e!r}")
        _allow()


if __name__ == "__main__":
    main()
