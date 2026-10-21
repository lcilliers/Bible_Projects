"""register_prose_set_status_v1_20260827.py — ONE-OFF. Escalation #918 companion build: registers
the new `prose.set_status` step (handler: `handlers/prose.py:set_status`, code: `lib/prosestore.py:
run_set_status`) in `cfg_step`, so `Prose.ps1 -Step SetStatus` runs through the standard
work-package dispatcher like every other prose step. No new table and no `cfg_write_grant` row is
needed -- `set_status` only ever generates a `PROSE` patch file (same as `export_chapter`/
`import_chapter`/`flag_fix_propose`/`flag_fix_apply`); it never writes `prose_section` directly, so
it carries no write grant, matching those four steps exactly (only `prose.flag` -- the module's one
direct-write exception -- holds one).

    python -m iba.app.migration.register_prose_set_status_v1_20260827
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []
    try:
        exists = conn.execute(
            "SELECT 1 FROM cfg_step WHERE work_package='prose' AND step='prose.set_status'"
        ).fetchone()
        if exists:
            report.append("cfg_step 'prose.set_status' already present")
        else:
            conn.execute(
                "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                "inactive, kind) VALUES ('prose', 7, 'prose.set_status', "
                "'iba.app.handlers.prose:set_status', 'none', "
                "'Set/reset prose_section.status directly for one or more -SectionIds, no body "
                "change (escalation #918, 2026-08-27 -- the reviewer''s own set/reset action, "
                "superseding cfg_prose_chapter''s removed chapter-status tracking); writes no DB "
                "row itself, generates a PROSE patch, same as export_chapter/import_chapter/"
                "flag_fix_propose/flag_fix_apply', 0, 'utility')"
            )
            report.append("cfg_step 'prose.set_status' added (ordinal 7)")
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("register_prose_set_status_v1_20260827:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
