"""fullpaths_2528_v1_20261121.py -- escalation #2528: the files named in the stage 4 rule texts are given as full repo-relative paths (the compliance start check reads a short path as a missing file;
escalation rule 7 asks for the full path). Behaviour rule 132 (lib/layerinner.py) and method rule IB-05 (lib/verseevidence.py). apply_logged; idempotent.

Usage: python iba/app/migration/fullpaths_2528_v1_20261121.py [--db PATH]
After a live run, move this file to iba/app/migration/archive/ (rule 96).
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2528-FULL-PATHS-20261121"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        for table, where, col, old, new in (
                ("cfg_behaviour_rule", {"id": 132}, "rule_text", "(lib/layerinner.py; rules IB-01 to IB-06)", "(iba/app/lib/layerinner.py; rules IB-01 to IB-06)"),
                ("cfg_method_rule", {"rule_key": "IB-05 earlier-observations-are-checked-first"}, "rule_text", "come from lib/verseevidence.py", "come from iba/app/lib/verseevidence.py")):
            wsql = " AND ".join(f'"{k}"=?' for k in where)
            cur = conn.execute(f'SELECT {col} FROM {table} WHERE {wsql}', list(where.values())).fetchone()[0]
            if old in cur:
                apply_logged(conn, RUN_ID, table, "update", where, {col: cur.replace(old, new)})
                n += 1
    print(f"{n} cfg write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
