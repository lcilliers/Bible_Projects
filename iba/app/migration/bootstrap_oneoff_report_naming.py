"""bootstrap_oneoff_report_naming.py — ONE-OFF: Phase 2 of
PLAN-reports-config-governance-v1-20260722.md §5 — the 3 `governance.oneoff_*` settings
`lib/reportkit.oneoff_path()` reads. One-off ("investigatory") reports don't recur, so they don't
get a `cfg_step`/`cfg_report` row (there's no step to key off) — but their folder/naming/format
still comes from config, not a literal string a future migration/investigation script hardcodes.

    python -m iba.app.migration.bootstrap_oneoff_report_naming
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _setting(conn, key, value, use, module, report):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting VALUES (?,?,?,?)", (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")
    else:
        report.append(f"cfg_setting {key!r} already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    settings = [
        ("governance.oneoff_report_dir", json.dumps("iba/app/reports/"),
         "folder for one-off/investigatory reports — read by lib/reportkit.oneoff_path()"),
        ("governance.oneoff_report_naming_pattern", json.dumps("{topic}-{YYYYMMDD}.{format}"),
         "filename pattern for one-off reports ({topic}/{YYYYMMDD}/{format} substituted) — "
         "same-day collisions get -v2/-v3/... appended by oneoff_path() itself, per the "
         "Bible-study side's docs/file-organisation-rules.md §2.3 convention"),
        ("governance.oneoff_report_format", json.dumps("md"),
         "default file extension for one-off reports"),
    ]
    for key, value, use in settings:
        _setting(conn, key, value, use, "governance", report)

    conn.commit()
    conn.close()

    print("oneoff-report-naming bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
