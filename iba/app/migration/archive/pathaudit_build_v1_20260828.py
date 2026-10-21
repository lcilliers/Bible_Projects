"""pathaudit_build_v1_20260828.py — ONE-OFF, idempotent: registers `path-audit`/`pathaudit.scan` —
the project-wide hardcoded-location-literal scan (escalation #971/#976). Researcher, 2026-08-28:
"we are now in the real meat of sorting out locations that does not go through config, so applying
to [every] script, and pushing it into a utility (with all the governance around it) is relevant
now." See `iba/app/lib/pathaudit.py`'s own docstring for method and honest limits.

Same idempotent-bootstrap pattern as `folder_purpose_build_v1_20260828.py`/
`bootstrap_file_manifest.py` — schema-adjacent registration for a NEW module, not a
`configmaint.propose` call.

    python -m iba.app.migration.pathaudit_build_v1_20260828
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


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


def _utility(conn, module, file_path, purpose, report):
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
        conn.execute("INSERT INTO cfg_utility (module, file_path, purpose, inactive) "
                    "VALUES (?,?,?,0)", (module, file_path, purpose))
        report.append(f"cfg_utility {module!r} added")
    else:
        report.append(f"cfg_utility {module!r} already present")


def _work_package(conn, name, ps_script, report):
    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (name,)).fetchone():
        conn.execute("INSERT INTO cfg_work_package (name, ps_script, runs_over, chained) "
                    "VALUES (?,?,'none',0)", (name, ps_script))
        report.append(f"cfg_work_package {name!r} added")
    else:
        report.append(f"cfg_work_package {name!r} already present")


def _step(conn, wp, ordinal, step, handler, does, kind, report):
    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (wp, step)).fetchone():
        conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, inactive, "
            "kind) VALUES (?,?,?,?,?,?,0,?)", (wp, ordinal, step, handler, "none", does, kind))
        report.append(f"cfg_step {step!r} added (kind={kind})")
    else:
        report.append(f"cfg_step {step!r} already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _enum(conn, "config_module", "pathaudit", report)

    _setting(conn, "pathaudit.report_path", '"outputs/configs/path-audit.md"',
            "where pathaudit.scan writes its full findings report", "pathaudit", report)

    _utility(conn, "pathaudit", "iba/app/lib/pathaudit.py",
            "pathaudit.py -- project-wide scan for hardcoded folder/file-path string literals not "
            "backed by a live cfg accessor. Escalation #971/#976, the automated successor to the "
            "one-off #648 sweep for the location subset specifically.", report)

    _work_package(conn, "path-audit", "iba/app/ps/PathAudit.ps1", report)
    _step(conn, "path-audit", 0, "pathaudit.scan",
         "iba.app.handlers.pathaudit:path_audit_scan",
         "Project-wide scan (every .py file except cfg_utility.inactive=1 ones) for a string "
         "literal that looks like a project-relative path under a live top-level folder, with no "
         "live cfg accessor on the same line -- ADVISORY, needs a look per finding, not an "
         "auto-fix.", "utility", report)

    if not conn.execute("SELECT 1 FROM cfg_report WHERE step='pathaudit.scan'").fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir) VALUES "
            "('pathaudit.scan','Project-wide hardcoded-location-literal scan',1,NULL,'md','stable',"
            "'archive')")
        report.append("cfg_report 'pathaudit.scan' added")
    else:
        report.append("cfg_report 'pathaudit.scan' already present")

    for ordinal, key, heading in ((0, "summary", "## Summary"), (1, "findings", "## Findings")):
        if not conn.execute(
                "SELECT 1 FROM cfg_report_section WHERE step='pathaudit.scan' AND section_key=?",
                (key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, toc_label, "
                "include) VALUES ('pathaudit.scan',?,?,?,?,1)",
                (ordinal, key, heading, heading.lstrip("# ").strip()))
            report.append(f"cfg_report_section (pathaudit.scan, {key}) added")
        else:
            report.append(f"cfg_report_section (pathaudit.scan, {key}) already present")

    conn.commit()
    conn.close()

    print("pathaudit build bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
