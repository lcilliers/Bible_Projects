"""filingkit_build_v1_20260828.py — ONE-OFF, idempotent: registers `filingkit` (`lib/filingkit.py`)
as a `cfg_utility` (escalation #863/#971/#992 — the last piece of #971 Part A, carried forward
from `iba/docs/file-naming-and-location-governance-plan-v1-20260826.md` §2). No new `cfg_setting`s
of its own — `versioned_path()` reads the same `governance.oneoff_*` settings `reportkit.
oneoff_path()` already did, as its fallback defaults.

    python -m iba.app.migration.filingkit_build_v1_20260828
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module='filingkit'").fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive) VALUES (?,?,?,0)",
            ("filingkit", "iba/app/lib/filingkit.py",
             "filingkit.py -- the project-wide filing utility: naming-shape, same-day -v{n} "
             "versioning, archive-before-overwrite, for any writer. Generalises reportkit."
             "oneoff_path(), which now delegates here. Escalation #863/#971/#992. Calls "
             "cfg.setting() directly (governance.oneoff_* fallback defaults) -- not config_exempt, "
             "a real call site."))
        report.append("cfg_utility 'filingkit' added")
    else:
        report.append("cfg_utility 'filingkit' already present")

    conn.commit()
    conn.close()

    print("filingkit build bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
