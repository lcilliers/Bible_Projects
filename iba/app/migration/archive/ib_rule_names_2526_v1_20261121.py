"""ib_rule_names_2526_v1_20261121.py -- escalation #2526 / #2528: three IB rule keys named the verse-first design (every-occurrence-carries-a-node, each-characteristic-has-each-item,
earlier-observations-are-checked-first) although their text was rewritten to the observation-led design. The keys are renamed to say what the rules now say. apply_logged; idempotent.

Usage: python iba/app/migration/ib_rule_names_2526_v1_20261121.py [--db PATH]. After a live run, move this file to iba/app/migration/archive/ (rule 96).
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2526-IB-RULE-NAMES-20261121"
NAMES = {"IB-02": "IB-02 stage-4-starts-from-the-observations", "IB-04": "IB-04 nothing-is-lost-on-the-way-to-stage-5", "IB-05": "IB-05 earlier-observations-are-shown-not-demanded"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        for k, new in NAMES.items():
            r = conn.execute("SELECT id, rule_key FROM cfg_method_rule WHERE rule_key LIKE ?", (k + " %",)).fetchone()
            if r is None:
                raise SystemExit(f"{k} not found")
            if r[1] != new:
                apply_logged(conn, RUN_ID, "cfg_method_rule", "update", {"id": r[0]}, {"rule_key": new})
                n += 1
    print(f"{n} cfg write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
