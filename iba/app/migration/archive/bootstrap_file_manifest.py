"""bootstrap_file_manifest.py — ONE-OFF, idempotent: registers `manifest.rebuild` and
`manifest.search` (the whole-project file manifest — filename/path metadata, ported from the
main-repo `scripts/build_file_manifest.py`) as real dispatcher work packages/steps, per the
researcher's 2026-08-15 instruction that manifest build/update/search must be built into the IBA
App, governed the same way as everything else here.

Two work packages (each independently invokable, matching the `log-retention` / `table-export`
precedent — `bootstrap_retention_table_export_registration.py` — rather than one chained package):

  - `file-manifest-rebuild` / `manifest.rebuild` — full rescan, writes the `file_manifest` table.
  - `file-manifest-search`  / `manifest.search`  — read-only query against it.

Both `kind='utility'` (`GOVERNANCE.md` §27 — this app's own running, not the study's substantive
analytic content) — direct 8-column insert since `cfg_step.kind` is now a mandatory dispatch-gate
column, not the 6-column shape the retention/table-export migration used before that column
existed.

Schema is DDL (new table, same class of exception as `bootstrap_cfg_utility.py`'s new table and
`bootstrap_inactive_column.py`'s new column) — a direct, documented, idempotent bootstrap, not a
`configmaint.propose` call. Every `cfg_setting` value here is a genuine decision the code actually
reads (`manifest.skip_dirs`, `manifest.exclude_exts`, `manifest.report_path`); the classification
logic itself (category/type/currency) is project-naming FACT and stays in `lib/manifest.py` code,
per that module's own docstring.

    python -m iba.app.migration.bootstrap_file_manifest
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_SKIP_DIRS_DEFAULT = [".git", "__pycache__", "venv", ".venv", "env", "node_modules",
                      ".claude", ".idea", ".vscode", ".pytest_cache", ".mypy_cache", ".ruff_cache"]
_EXCLUDE_EXTS_DEFAULT = [".pyc", ".pyo", ".pyd", ".tmp", ".swp", ".lock"]

_DDL = """
CREATE TABLE IF NOT EXISTS file_manifest (
    path         TEXT PRIMARY KEY,
    category     TEXT NOT NULL,
    file_type    TEXT NOT NULL,
    currency     TEXT NOT NULL,
    archived     INTEGER NOT NULL DEFAULT 0,
    registry     INTEGER,
    word         TEXT,
    cluster      TEXT,
    vcb_batch    INTEGER,
    version      TEXT,
    date         TEXT,
    ext          TEXT,
    size_bytes   INTEGER NOT NULL,
    modified_at  TEXT NOT NULL,
    scanned_at   TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_file_manifest_category ON file_manifest(category);
CREATE INDEX IF NOT EXISTS ix_file_manifest_currency ON file_manifest(currency);
CREATE INDEX IF NOT EXISTS ix_file_manifest_registry ON file_manifest(registry);
"""


def _enum(conn, name, value, report):
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES (?,?,?,0)", (name, value, n))
        report.append(f"cfg_enum {name} += {value!r}")
    else:
        report.append(f"cfg_enum {name} already has {value!r}")


def _setting(conn, key, value, use, module, report):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES (?,?,?,?)",
                    (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")
    else:
        report.append(f"cfg_setting {key!r} already present")


def _work_package(conn, name, ps_script, report):
    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (name,)).fetchone():
        conn.execute("INSERT INTO cfg_work_package (name, ps_script, runs_over, chained) "
                    "VALUES (?,?,'none',0)", (name, ps_script))
        report.append(f"cfg_work_package {name!r} added")
    else:
        report.append(f"cfg_work_package {name!r} already present")


def _step(conn, wp, ordinal, step, handler, does, kind, report):
    existing = conn.execute(
        "SELECT handler, kind FROM cfg_step WHERE work_package=? AND step=?", (wp, step)).fetchone()
    if not existing:
        conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, inactive, "
            "kind) VALUES (?,?,?,?,?,?,0,?)", (wp, ordinal, step, handler, "none", does, kind))
        report.append(f"cfg_step {step!r} added (kind={kind})")
    elif existing[0] != handler or existing[1] != kind:
        conn.execute("UPDATE cfg_step SET handler=?, kind=? WHERE work_package=? AND step=?",
                    (handler, kind, wp, step))
        report.append(f"cfg_step {step!r} handler/kind corrected")
    else:
        report.append(f"cfg_step {step!r} already present")


def _utility(conn, module, file_path, purpose, report):
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
        conn.execute("INSERT INTO cfg_utility (module, file_path, purpose, inactive) "
                    "VALUES (?,?,?,0)", (module, file_path, purpose))
        report.append(f"cfg_utility {module!r} added")
    else:
        report.append(f"cfg_utility {module!r} already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    conn.executescript(_DDL)
    report.append("file_manifest table + indexes ensured")

    _enum(conn, "config_module", "manifest", report)

    _work_package(conn, "file-manifest-rebuild", "iba/app/ps/Manifest-Rebuild.ps1", report)
    _step(conn, "file-manifest-rebuild", 0, "manifest.rebuild",
         "iba.app.handlers.reports:manifest_rebuild",
         "full rescan of the whole project tree (filename/path metadata only, no file content) — "
         "replaces file_manifest's contents; see lib/manifest.py", "utility", report)

    _work_package(conn, "file-manifest-search", "iba/app/ps/Manifest-Search.ps1", report)
    _step(conn, "file-manifest-search", 0, "manifest.search",
         "iba.app.handlers.reports:manifest_search",
         "read-only query against file_manifest (field:value or free-text path match); "
         "results persisted via reportkit.oneoff_path, per governance.reports_must_persist",
         "utility", report)

    _setting(conn, "manifest.skip_dirs", json.dumps(_SKIP_DIRS_DEFAULT),
             "directories excluded from a manifest.rebuild scan (VCS/build/cache machinery only — "
             "everything else in the project tree, including every archive/ folder, is indexed)",
             "manifest", report)
    _setting(conn, "manifest.exclude_exts", json.dumps(_EXCLUDE_EXTS_DEFAULT),
             "file extensions excluded from a manifest.rebuild scan (compiled/transient junk only)",
             "manifest", report)
    _setting(conn, "manifest.report_path", json.dumps("iba/app/reports/file-manifest.md"),
             "where manifest.rebuild writes its summary report", "manifest", report)

    _utility(conn, "manifest", "iba/app/lib/manifest.py",
            "manifest.py — the project-wide file manifest (rebuild + search). Filename/path "
            "metadata only; the baseline lib/contentindex.py (round 2) cross-checks file-content "
            "search coverage against.", report)

    # cfg_report / cfg_report_section for manifest.rebuild's persisted summary (render_scaffold
    # requires a cfg_report row keyed by step — manifest.search uses reportkit.oneoff_path instead,
    # which needs none)
    if not conn.execute("SELECT 1 FROM cfg_report WHERE step='manifest.rebuild'").fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir) VALUES "
            "('manifest.rebuild','Project file manifest — rebuild summary',1,NULL,'md','stable',"
            "'archive')")
        report.append("cfg_report 'manifest.rebuild' added")
    else:
        report.append("cfg_report 'manifest.rebuild' already present")

    for ordinal, key, heading in ((0, "summary", "## Summary"),
                                  (1, "by_category", "## By category"),
                                  (2, "by_currency", "## By currency")):
        if not conn.execute(
                "SELECT 1 FROM cfg_report_section WHERE step='manifest.rebuild' AND section_key=?",
                (key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, toc_label, "
                "include) VALUES ('manifest.rebuild',?,?,?,?,1)",
                (ordinal, key, heading, heading.lstrip("# ").strip()))
            report.append(f"cfg_report_section (manifest.rebuild, {key}) added")
        else:
            report.append(f"cfg_report_section (manifest.rebuild, {key}) already present")

    conn.commit()
    conn.close()

    print("file-manifest registration bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
