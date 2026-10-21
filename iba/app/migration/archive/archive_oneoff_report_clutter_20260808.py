"""archive_oneoff_report_clutter_20260808.py — ONE-OFF, idempotent: sweeps `governance.
oneoff_report_dir` for every report lineage currently sitting with more than one live version
(the `oneoff_path()` archiving gap, BUILD.md §83) and archives every version except the newest.

**Why a script, not `configmaint.propose`.** This is a filesystem operation (moving files), not a
`cfg_*` row change — nothing here goes through the write-grant/propose machinery at all, same as
`archive_before_write`/`_archive_prior_versions` themselves (`lib/reportkit.py`) never have.

**Why now.** `oneoff_path()` versioned every one-off report correctly but never archived a
superseded version — every reconciliation report, `hib.set`-by-type report, debate report, and
verse-span extract accumulated its whole lineage flat in the live folder since before the
2026-08-05 `write_report` archiving fix (which never touched this separate code path). Fixed at
the source in the same session (`lib/reportkit.py:oneoff_path`) — this script is the one-time
retroactive cleanup for everything that already accumulated before the fix landed.

**Reuses the exact same grouping/archiving logic `oneoff_path()` itself now uses**
(`reportkit.archive_oneoff_clutter`) — one place this rule lives, never a second hand-written copy
of it.

    python -m iba.app.migration.archive_oneoff_report_clutter_20260808
"""

from __future__ import annotations

import pathlib
import sqlite3
import sys

from ..lib import reportkit
from ..lib.cfg import DB_PATH


def run(conn: sqlite3.Connection, app_root: pathlib.Path) -> list[str]:
    row = conn.execute(
        "SELECT value FROM cfg_setting WHERE key='governance.oneoff_report_dir' AND inactive=0"
    ).fetchone()
    if not row:
        return ["governance.oneoff_report_dir not set -- nothing to sweep"]
    import json
    out_dir_setting = json.loads(row[0])
    # "iba/app/reports/" is relative to the REPO ROOT (same resolution oneoff_path() itself
    # relies on) -- app_root here is already iba/app, so its own parent.parent is the repo root.
    out_dir_path = pathlib.Path(out_dir_setting)
    out_dir = out_dir_path if out_dir_path.is_absolute() else app_root.parent.parent / out_dir_path

    archived = reportkit.archive_oneoff_clutter(out_dir)
    if not archived:
        return [f"{out_dir}: no report lineage had more than one live version -- nothing to sweep"]
    report = [f"{out_dir}: {len(archived)} file(s) archived (kept the newest version of each "
             f"lineage live):"]
    report += [f"  - {name}" for name in sorted(archived)]
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    app_root = pathlib.Path(__file__).resolve().parent.parent
    report = run(conn, app_root)
    conn.close()
    print("One-off report clutter sweep (BUILD.md §83):")
    for line in report:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
