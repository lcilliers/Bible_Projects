"""lexicalalignment.py -- the stored alignment check of the lexical work (escalation #2507, design v4 decision D9).

A name the study has retired (a step, a script, a generator, a table) must not be described as live by the control homes. This check finds, from the stored rows and the files themselves:
  1. active config rows (steps, utilities, settings, method rules, behaviour rules) that name a retired entry and say nothing of its retirement;
  2. lines of the guidance documents (USER-GUIDE.md, GOVERNANCE.md, CHARTER.md) that name a retired entry and say nothing of its retirement;
  3. a live module (lib, handlers, ps, tools; archive folders excluded) that imports or runs a retired module or script;
  4. the items of cfg_setting layer.reading: no inner-being role, route, kind or question (the boundary of stages 1 to 3, #2509); each has an `asks`, and each prompt it names is an active catalogue question.
The retired names are cfg_setting alignment.retired_lexical; nothing here is a list in code. Read-only; returns hard errors for configmaint.validate.
"""
from __future__ import annotations

import json
import pathlib
import re
import sqlite3

DOCS = ("iba/app/USER-GUIDE.md", "iba/app/GOVERNANCE.md", "iba/app/CHARTER.md")
CODE_DIRS = ("iba/app/lib", "iba/app/handlers", "iba/app/ps", "iba/app/tools")
SAYS_RETIRED = re.compile(r"retire|replaced by|history|archive|no longer|inactive|superseded", re.I)


def _names(conn) -> list[str]:
    r = conn.execute("SELECT value FROM cfg_setting WHERE key='alignment.retired_lexical' AND inactive=0").fetchone()
    return json.loads(r[0]) if r else []


def _rows(conn, sql):
    return conn.execute(sql).fetchall()


def find(conn: sqlite3.Connection, project_root: pathlib.Path) -> list[str]:
    errors: list[str] = []
    names = _names(conn)
    if not names:
        return ["cfg_setting alignment.retired_lexical is missing or empty (the stored alignment check of the lexical work needs the retired names)"]
    pats = {n: re.compile(re.escape(n)) for n in names}

    # 1. active config rows
    sources = (("cfg_step", "SELECT step, coalesce(does,'') FROM cfg_step WHERE inactive=0"),
               ("cfg_utility", "SELECT module, coalesce(purpose,'') FROM cfg_utility WHERE inactive=0"),
               ("cfg_setting", "SELECT key, coalesce(use,'') || ' ' || coalesce(value,'') FROM cfg_setting WHERE inactive=0 AND key NOT LIKE 'alignment.%'"),
               ("cfg_method_rule", "SELECT step || ' ' || rule_key, rule_text FROM cfg_method_rule WHERE active=1"),
               ("cfg_behaviour_rule", "SELECT rule_key, rule_text FROM cfg_behaviour_rule WHERE active=1"))
    for table, sql in sources:
        for key, text in _rows(conn, sql):
            for n, pat in pats.items():
                if pat.search(text or "") and not SAYS_RETIRED.search(text or ""):
                    errors.append(f"{table} {key!r} names the retired {n!r} and says nothing of its retirement")

    # 2. guidance documents, by paragraph (a line)
    for rel in DOCS:
        f = project_root / rel
        if not f.exists():
            continue
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
            for n, pat in pats.items():
                if pat.search(line) and not SAYS_RETIRED.search(line):
                    errors.append(f"{rel}:{i} names the retired {n!r} and says nothing of its retirement")

    # 3. live code importing or running a retired module or script
    modules = [n for n in names if re.fullmatch(r"[a-z0-9_]+", n)]
    scripts = [n for n in names if n.lower().endswith(".ps1")]
    for d in CODE_DIRS:
        root = project_root / d
        if not root.exists():
            continue
        for f in root.rglob("*"):
            if not f.is_file() or "archive" in f.parts or f.suffix not in (".py", ".ps1") or "__pycache__" in f.parts:
                continue
            text = f.read_text(encoding="utf-8", errors="replace")
            for m in modules:
                if re.search(rf"(from\s+\.+\s*{m}\b|from\s+\.+lib\s+import[^\n]*\b{m}\b|import\s+[^\n]*\b{m}\b|\.lib\.{m}\b)", text):
                    errors.append(f"{f.relative_to(project_root).as_posix()} imports the retired module {m!r}")
            for s in scripts:
                if s in text and f.suffix == ".ps1" and f.name != s:
                    errors.append(f"{f.relative_to(project_root).as_posix()} runs the retired script {s!r}")

    # 4a. the boundary of the stages (#2509): the items of stages 1 to 3 are lexical work and carry nothing of the inner being (researcher, 2026-11-15)
    inner_roles, inner_kinds = set(), set()
    r = conn.execute("SELECT value FROM cfg_setting WHERE key='reading.node_roles' AND inactive=0").fetchone()
    if r:
        g = json.loads(r[0])
        inner_roles = set(g.get("relevant", [])) | set(g.get("bears_on", [])) | set(g.get("recognised", []))
    r = conn.execute("SELECT value FROM cfg_setting WHERE key='alignment.inner_being_kinds' AND inactive=0").fetchone()
    if r:
        inner_kinds = set(json.loads(r[0]))
    r = conn.execute("SELECT value FROM cfg_setting WHERE key='layer.reading' AND inactive=0").fetchone()
    if r:
        for key, item in json.loads(r[0]).get("items", {}).items():
            for rk in ("member_role", "partner_role"):
                if item.get(rk) in inner_roles:
                    errors.append(f"layer.reading item {key!r} gives its nodes the inner-being role {item[rk]!r} ({rk}): the lexical stages carry the role lexical")
            if item.get("route"):
                errors.append(f"layer.reading item {key!r} takes a route, which is an inner-being finding")
            bad_kinds = ({item.get("kind")} | set(item.get("kinds", []))) & inner_kinds
            if bad_kinds:
                errors.append(f"layer.reading item {key!r} is written as the inner-being kind {sorted(bad_kinds)}")
            if re.search(r"inner.being", item.get("asks") or "", re.I):
                errors.append(f"layer.reading item {key!r} asks about the inner being: the lexical stages state what the dictionary, the verses and the structure show")

    # 4. the items of the layered reading: each asks, each prompt is an active catalogue question
    r = conn.execute("SELECT value FROM cfg_setting WHERE key='layer.reading' AND inactive=0").fetchone()
    if r:
        lay = json.loads(r[0])
        for key, item in lay.get("items", {}).items():
            if not (item.get("asks") or "").strip():
                errors.append(f"layer.reading item {key!r} has no `asks`")
            for code in item.get("prompts", []):
                ok = conn.execute("SELECT 1 FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0 AND status='active'", (code,)).fetchone()
                if not ok:
                    errors.append(f"layer.reading item {key!r} names the catalogue question {code!r}, which is not an active question")
    return errors
