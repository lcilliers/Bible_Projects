"""prose_output_dirs_build_v1_20260828.py — ONE-OFF, idempotent: registers the 4 new `cfg_prose`
settings `prosestore.py`'s `output_dir()`/`docx_output_dir()`/`search_output_dir()`/
`patch_output_dir()` now read (escalation #971/#976, `iba/app/lib/pathaudit.py`'s scan found the
underlying `OUT_DIR`/`DOCX_OUT_DIR`/`SEARCH_OUT_DIR`/`PATCH_OUT_DIR` hardcoded constants — the same
class of silent-drift risk `prose.edit_file_dir` already demonstrated live). New rows in an existing
module table (`cfg_prose` already exists, escalation #798/#799) — a direct bootstrap, same reasoning
as every other `_setting()`-shaped migration in this codebase, not `configmaint.propose` (that gate
is for changing an EXISTING row's value, not adding a new one tied to a code build).

    python -m iba.app.migration.prose_output_dirs_build_v1_20260828
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _prose_setting(conn, key, value, use, report):
    if not conn.execute("SELECT 1 FROM cfg_prose WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_prose (key, value, use, inactive) VALUES (?,?,?,0)",
                    (key, value, use))
        report.append(f"cfg_prose {key!r} added")
    else:
        report.append(f"cfg_prose {key!r} already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _prose_setting(conn, "prose.output_dir", '"Workflow/Programme/programme_prose"',
                  "where prosestore.run_extract writes its JSON/Markdown extract", report)
    _prose_setting(conn, "prose.docx_output_dir", '"outputs/docx"',
                  "where prosestore.run_extract writes its optional .docx export", report)
    _prose_setting(conn, "prose.search_output_dir", '"outputs/markdown"',
                  "where prosestore.run_search and run_flag_fix_propose write their result files",
                  report)
    _prose_setting(conn, "prose.patch_output_dir", '"Sessions/Patches"',
                  "where prosestore.run_import_chapter/run_flag_fix_apply/run_set_status write the "
                  "PROSE supersede patch they generate", report)

    conn.commit()
    conn.close()

    print("prose output-dirs build bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
