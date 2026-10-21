"""bootstrap_cfg_utility.py — ONE-OFF: Phase 4 of PLAN-config-system-remediation-v1-20260729.md.

`cfg_step` (+ the hardcoded `REPORT_STEPS`/`QUALITY_CHECK_REPORT_PATH` lists) covers *steps* —
things `run.py` dispatches to. `iba/app/lib/*.py` utility modules had no equivalent registry at
all, so there was no way to ask "does every utility have the config coverage we'd expect" except by
reading each file by hand — exactly how the 2026-07-29 review found `lib/lexiconparse.py` (six
regexes, a hardcoded tag-set, zero `cfg.setting()` calls) invisible until someone actually opened
it. `cfg_utility` is the registry that makes that visible going forward: one row per `iba/app/
lib/*.py` module, ENUMERATED directly (same discipline every retraction/reactivation migration in
this app already uses — count first, don't assume), not curated by memory.

Schema is DDL (new table), so — same class of exception as `bootstrap_configuration_maintenance.py`/
`bootstrap_inactive_column.py` — this is a direct, documented, idempotent bootstrap, not a
`configmaint.propose` call. `cfg_utility` itself is NOT added to `cfg_table` (that table lists DATA
tables `db.py:build()` constructs from `cfg_column`, not `cfg_*` infrastructure — `cfg_report`/
`cfg_write_grant`/etc. aren't there either; `cfg_change_detail`'s presence is a separate, pre-existing,
known bug, not precedent to repeat — see GOVERNANCE.md §2). `cfg_utility`'s OWN columns ARE
registered in `cfg_column`, matching the precedent every other `cfg_*` infrastructure table already
has there.

    python -m iba.app.migration.bootstrap_cfg_utility
"""

from __future__ import annotations

import ast
import pathlib
import sqlite3
import sys

from ..lib.cfg import DB_PATH

LIB_DIR = pathlib.Path(__file__).resolve().parent.parent / "lib"


def _module_purpose(path: pathlib.Path) -> str:
    """First line of the module's own docstring — truncated, never fabricated."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        doc = ast.get_docstring(tree) or ""
    except (SyntaxError, OSError):
        doc = ""
    first_line = doc.split("\n", 1)[0].strip()
    return first_line[:200] if first_line else "(no module docstring)"


def _discover_modules() -> list[tuple[str, str, str]]:
    """(module, file_path, purpose) for every `iba/app/lib/*.py` except `__init__.py` —
    enumerated from disk, not a curated list, so a new lib module is never silently missed."""
    out = []
    for f in sorted(LIB_DIR.glob("*.py")):
        if f.stem == "__init__":
            continue
        rel = f.relative_to(LIB_DIR.parent.parent.parent).as_posix()
        out.append((f.stem, rel, _module_purpose(f)))
    return out


def _create_table(conn: sqlite3.Connection, report: list[str]) -> None:
    existing = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if "cfg_utility" not in existing:
        conn.execute("""
            CREATE TABLE cfg_utility (
                module     TEXT PRIMARY KEY,
                file_path  TEXT NOT NULL,
                purpose    TEXT,
                inactive   INTEGER NOT NULL DEFAULT 0
            )
        """)
        report.append("table cfg_utility created")
    else:
        report.append("table cfg_utility already present")

    # (name, ordinal, type, is_pk, notnull, dflt, use)
    cfg_column_rows = [
        ("module", 0, "TEXT", 1, 1, None, "the lib module's own name (no .py, no package prefix)"),
        ("file_path", 1, "TEXT", 0, 1, None, "path from the repo root, e.g. iba/app/lib/stepapi.py"),
        ("purpose", 2, "TEXT", 0, 0, None, "first line of the module's own docstring, verbatim"),
        ("inactive", 3, "INTEGER", 0, 1, "0",
         "deactivate this registry row without deleting it (module removed/merged) — same "
         "convention as every other cfg_* table's inactive column"),
    ]
    for name, ordinal, type_, is_pk, notnull, dflt, use in cfg_column_rows:
        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE table_name='cfg_utility' AND name=?",
                (name,)).fetchone():
            conn.execute(
                'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", '
                'is_unique, dflt, fk, use, expectation, source, filled_by) '
                "VALUES ('cfg_utility',?,?,?,?,?,0,?,NULL,?,NULL,NULL,"
                "'migration/bootstrap_cfg_utility.py')",
                (name, ordinal, type_, is_pk, notnull, dflt, use))
            report.append(f"cfg_column row for cfg_utility.{name} added")
        else:
            report.append(f"cfg_column row for cfg_utility.{name} already present")


def _grant(conn: sqlite3.Connection, writer: str, table: str, report: list[str]) -> None:
    existing = conn.execute(
        "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?", (writer, table)).fetchone()
    if not existing:
        conn.execute(
            "INSERT INTO cfg_write_grant (writer, table_name, inactive) VALUES (?,?,0)",
            (writer, table))
        report.append(f"cfg_write_grant ({writer}, {table}) added")
    else:
        report.append(f"cfg_write_grant ({writer}, {table}) already present")


def _seed_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    modules = _discover_modules()
    report.append(f"discovered {len(modules)} lib module(s) on disk")
    for module, file_path, purpose in modules:
        if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
            report.append(f"cfg_utility {module!r} already present")
            continue
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive) VALUES (?,?,?,0)",
            (module, file_path, purpose))
        report.append(f"cfg_utility {module!r} added ({file_path})")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _create_table(conn, report)
    _seed_rows(conn, report)
    _grant(conn, "configmaint.propose", "cfg_utility", report)

    conn.commit()
    conn.close()

    print("cfg_utility bootstrap (PLAN-config-system-remediation-v1-20260729.md Phase 4):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
