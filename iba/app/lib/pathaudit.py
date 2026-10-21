"""pathaudit.py — project-wide scan for hardcoded folder/file-path string literals that should be
config-driven (`cfg.required_setting()` / `cfg.module_setting()`). Scope: every `.py` file
project-wide (the walk `cfgquality.find_unregistered_project_scripts` uses), minus files whose
`cfg_utility` row is `inactive=1`; an unregistered file is included.

Method (ADVISORY: every finding needs a researcher judgement):
1. Tokenize each file and look at every STRING literal (comments are skipped; docstrings are
   strings, so they can still false-positive).
2. A literal is a location candidate if it passes `folderpurpose.normalize_setting_value`'s
   plausibility filter (no spaces, no `{template}` braces, reasonable length) AND its first path
   segment is a live `folder_purpose.top_level_root` -- catching both a full embedded path
   (`"outputs/markdown/prose-edits"`) and the `Path("Workflow") / "Programme" / ...` idiom.
3. No exemption for a literal next to a config accessor: there are no hardcoded literals in current
   code, so a `.setting(key, "literal/path")` call is flagged.
"""

from __future__ import annotations

import io
import pathlib
import sqlite3
import tokenize

from . import folderpurpose as fp_mod

# "migration" excluded: a migration's job is writing literal path values into config rows as a
# one-time seed.
_EXCLUDE_ANYWHERE = {".git", "archive", "__pycache__", ".venv", "venv", "node_modules",
                    "site-packages", "migration"}


def _roots(conn: sqlite3.Connection) -> set[str]:
    return {r[0].lower() for r in conn.execute(
        "SELECT DISTINCT top_level_root FROM folder_purpose") if r[0] and r[0] != "(repo root)"}


def _inactive_paths(conn: sqlite3.Connection) -> set[str]:
    return {r[0] for r in conn.execute("SELECT file_path FROM cfg_utility WHERE inactive=1")}


def _candidate_files(project_root: pathlib.Path, inactive: set[str]) -> list[pathlib.Path]:
    out = []
    for f in sorted(project_root.rglob("*.py")):
        rel = f.relative_to(project_root)
        parts = rel.parts
        if not parts or _EXCLUDE_ANYWHERE & set(parts):
            continue
        if f.stem == "__init__" or f.stem.startswith("temp_"):
            continue
        if rel.as_posix() in inactive:
            continue
        out.append(f)
    return out


def _scan_file(path: pathlib.Path, roots: set[str]) -> list[dict]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError, ValueError, UnicodeDecodeError):
        return []
    lines = text.splitlines()
    findings = []
    for tok in tokens:
        if tok.type != tokenize.STRING:
            continue
        try:
            value = eval(tok.string)  # noqa: S307 — a tokenizer-verified STRING literal, not input
        except Exception:
            continue
        if not isinstance(value, str):
            continue
        norm = fp_mod.normalize_setting_value(f'"{value}"')
        if norm is None:
            continue
        first_seg = norm.split("/", 1)[0]
        if first_seg not in roots:
            continue
        line_no = tok.start[0]
        line_text = lines[line_no - 1] if 0 < line_no <= len(lines) else ""
        if "/" not in norm:
            # a bare single-segment literal ("iba", "archive") is a candidate only as a pathlib.Path(
            # argument; a multi-segment literal (containing "/") is always checked
            col = tok.start[1]
            before = line_text[:col]
            if not before.rstrip().endswith("Path("):
                continue
        findings.append({"line": line_no, "literal": value, "line_text": line_text.strip()})
    return findings


def scan(cfg) -> dict:
    """Full project-wide scan. Returns {"scanned": N, "flagged_files": N, "findings": [...]}
    where each finding is {"file", "line", "literal", "line_text", "registered"}."""
    conn: sqlite3.Connection = cfg.conn
    roots = _roots(conn)
    inactive = _inactive_paths(conn)
    registered = {r[0] for r in conn.execute("SELECT file_path FROM cfg_utility")}
    project_root = fp_mod.PROJECT_ROOT

    all_findings = []
    files = _candidate_files(project_root, inactive)
    for f in files:
        rel = f.relative_to(project_root).as_posix()
        for hit in _scan_file(f, roots):
            all_findings.append({"file": rel, "registered": rel in registered, **hit})

    return {"scanned": len(files), "flagged_files": len({f["file"] for f in all_findings}),
           "findings": all_findings}
