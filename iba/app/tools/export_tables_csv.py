"""export_tables_csv.py — dump every DATA table of a project database to CSV, one file per table:
every column, every row, verbatim. Excludes cfg_* tables (configmaint.report owns those). The
previous same-named file is archived before writing (`reportkit.archive_before_write`).

    python -m iba.app.tools.export_tables_csv                       # -> iba/app/reports/export/*.csv
    python -m iba.app.tools.export_tables_csv --out some/dir
    python -m iba.app.tools.export_tables_csv --table candidate_seed lemma_inventory
    python -m iba.app.tools.export_tables_csv --database bible_research --table wa_obs_question_catalogue

`--database` selects the database through `cfg.database_path(name)`; `--table` filtering applies in
either.
"""

from __future__ import annotations

import argparse
import csv
import pathlib
import sqlite3
import sys

from ..lib import reportkit
from ..lib.cfg import DB_PATH

DEFAULT_OUT = pathlib.Path(__file__).resolve().parent.parent / "reports" / "export"


def _tables(conn: sqlite3.Connection) -> list[str]:
    return [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' "
        "AND name NOT LIKE 'cfg_%' ORDER BY name")]


def export(out_dir: pathlib.Path, only: list[str] | None,
           db_path: pathlib.Path | str | None = None) -> list[tuple[str, int]]:
    conn = sqlite3.connect(db_path or DB_PATH)
    conn.row_factory = sqlite3.Row
    out_dir.mkdir(parents=True, exist_ok=True)
    tables = [t for t in (only or _tables(conn)) if not t.startswith("cfg_")]
    results = []
    for t in tables:
        cols = [d[0] for d in conn.execute(f'SELECT * FROM "{t}" LIMIT 0').description]
        rows = conn.execute(f'SELECT * FROM "{t}"').fetchall()
        path = out_dir / f"{t}.csv"
        reportkit.archive_before_write(path)
        # utf-8-sig: Hebrew/Greek (accentedUnicode) and Excel need the BOM to render correctly
        with path.open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(cols)
            for r in rows:
                w.writerow([r[c] for c in cols])
        results.append((t, len(rows)))
    conn.close()
    return results


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=pathlib.Path, default=DEFAULT_OUT)
    ap.add_argument("--table", nargs="*", help="export only these tables (default: every table)")
    ap.add_argument("--database", help="registered project database name (default: iba) -- "
                                        "see cfg_enum 'project_database'")
    a = ap.parse_args()
    db_path = None
    if a.database and a.database != "iba":
        from ..lib.cfg import Cfg
        db_path = Cfg().database_path(a.database)
    results = export(a.out, a.table, db_path)
    print(f"exported {len(results)} table(s) to {a.out}")
    for t, n in results:
        print(f"  {t:24} {n} row(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
