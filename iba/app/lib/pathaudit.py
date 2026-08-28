"""pathaudit.py — project-wide scan for hardcoded folder/file-path string literals that should be
`cfg_setting`/`cfg.module_setting()`-driven instead. The general-case, automated successor to the
one-off manual sweep (escalation #648, 2026-08-17, `iba/app/reports/hardcoded-constants-sweep-
20260817.md`) — that sweep covered every kind of hardcoded constant by hand, once; this covers only
LOCATION literals (the class escalation #971/#976 kept surfacing — `cfg_prose.prose.edit_file_dir`
pointing at a moved folder, the `_analytics/Bible_Books` casing mismatch), automatically, every run.

Researcher, 2026-08-28: *"we are now in the real meat of sorting out locations that does not go
through config, so applying to [every] script, and pushing it into a utility (with all the
governance around it) is relevant now. the only scripts to not include, are scripts that is marked
as inactive."* Scope: every `.py` file project-wide (the same walk `cfgquality.
find_unregistered_project_scripts` already uses), MINUS any file whose `cfg_utility` row is
`inactive=1` — a file with no `cfg_utility` row at all is INCLUDED (it isn't marked inactive; not
registering it is itself `find_unregistered_project_scripts`'s own finding, not a reason to skip it
here too).

**Method, and its honest limits (ADVISORY by construction, not a hard fault):**
1. Tokenize each file; look at every real STRING literal (not a COMMENT — the tokenizer already
   distinguishes them, so a docstring/comment merely *mentioning* a path in prose doesn't fool a
   call-site scan the way it does for `cfgquality._code_only_text`'s docstring problem — but a
   docstring IS itself a STRING token, so it's still a source of possible false positives here).
2. A literal counts as a location candidate if it passes the same plausibility filter
   `folderpurpose.normalize_setting_value` already uses (no spaces, no `{template}` braces,
   reasonable length) AND its first path segment matches a live `folder_purpose.top_level_root`
   value (the actual top-level folders of this project, not a guessed list) — catches both a full
   embedded path (`"outputs/markdown/prose-edits"`) and the `Path("Workflow") / "Programme" / ...`
   construction idiom (a bare `"Workflow"` segment).
3. A literal on the SAME source line as `.setting(` or `.module_setting(` is treated as a
   documented DEFAULT for a live config accessor (the established, compliant pattern — e.g.
   `cfg.setting("governance.oneoff_report_dir", "iba/app/reports/")`) and is NOT flagged.
4. No-space docstrings/comments mentioning a bare path can still false-positive; genuinely
   deliberate hardcodes reviewed and accepted before (e.g. `prosestore.OUT_DIR` et al., "unchanged
   from the original scripts — not flagged by escalation #648") will be flagged again here — this
   is a coarser, blunter net than a human review, by design (automated, every run, catches drift a
   one-off sweep can't) — every finding needs the same researcher judgement any advisory check here
   does, not a silent auto-fix.
"""

from __future__ import annotations

import io
import pathlib
import sqlite3
import tokenize

from . import folderpurpose as fp_mod

# "migration" excluded 2026-08-28, checked live: a migration script's whole JOB is writing a
# literal path VALUE into a cfg_setting/cfg_utility/cfg_step row as part of a one-time DB seed —
# that's not a hardcoded-location violation, it's the migration doing exactly what it should
# (same reasoning bootstrap_file_manifest.py's own docstring gives for schema/DDL being a direct
# bootstrap, not something to route through configmaint.propose). Confirmed on the unfiltered
# first run: 109 of 126 findings (86%) were migration scripts recording their own seed values,
# swamping the 17 real findings elsewhere.
_EXCLUDE_ANYWHERE = {".git", "archive", "__pycache__", ".venv", "venv", "node_modules",
                    "site-packages", "migration"}
_CONFIG_ACCESSOR_MARKERS = (".setting(", ".module_setting(")


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
            # A BARE single-segment literal ("iba", "database", "archive") is only a real path
            # candidate when it's actually an argument to pathlib.Path( — otherwise it's just as
            # likely a plain string being compared/labelled (found live: `if name == "iba":` in
            # cfg.py, nothing to do with a folder at all). Multi-segment literals (containing "/")
            # carry no such ambiguity and are checked regardless.
            col = tok.start[1]
            before = line_text[:col]
            if not before.rstrip().endswith("Path("):
                continue
        # Look back up to 2 lines, not just the literal's own line — a wrapped multi-line call
        # (`ctx.cfg.setting(\n    "key",\n    "default/path")`) puts `.setting(` on an earlier
        # line than its own default-value literal; checked live, this is the majority shape of
        # this exact pattern in this codebase (found scanning iba/app/handlers/*.py, all
        # 2-line-wrapped `ctx.cfg.setting(key, default)` calls the same-line-only check missed).
        window = "\n".join(lines[max(0, line_no - 3):line_no])
        if any(m in window for m in _CONFIG_ACCESSOR_MARKERS):
            continue  # documented default alongside a live cfg accessor — compliant, not flagged
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
