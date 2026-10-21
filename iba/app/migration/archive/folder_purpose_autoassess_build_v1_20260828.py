"""folder_purpose_autoassess_build_v1_20260828.py — ONE-OFF, idempotent: registers Method D
(`folderpurpose.autoassess`) as a real step on the existing `folder-purpose` work package.

Researcher, 2026-08-28: "where the folder_purpose_type can be determined by you, you must fill and
maintain it. the folder_purpose_status status must be assessed by you and filled, only prompting
me if you are unsure." This is the "maintain" half — a re-runnable step, not a one-time script, so
a future `-Action Seed` bringing in new folders gets them assessed the same way without a fresh
ad hoc pass. See `lib/folderpurpose.py:auto_assess()`'s own docstring for the exact rules and their
honest limits (never guesses 'mixed'/'reallocate', or a category-less folder's type).

    python -m iba.app.migration.folder_purpose_autoassess_build_v1_20260828
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package='folder-purpose' AND "
                       "step='folderpurpose.autoassess'").fetchone():
        conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, inactive, "
            "kind) VALUES ('folder-purpose',5,'folderpurpose.autoassess',"
            "'iba.app.handlers.folderpurpose:folder_purpose_autoassess','none',"
            "'Method D -- fills type/status for every row missing either, from Methods A/B''s own "
            "gathered facts only (governed_by_setting, manifest_category/currency, file counts, "
            "mtime). Never guesses mixed/reallocate or a category-less folder''s type -- those "
            "stay for Method C.',0,'utility')")
        report.append("cfg_step 'folderpurpose.autoassess' added")
    else:
        report.append("cfg_step 'folderpurpose.autoassess' already present")

    conn.commit()
    conn.close()

    print("folder_purpose autoassess build bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
