"""surface_maps_fix_2361_v1_20261106.py -- escalation #2361, stage 6: the retirement of surface_base.status and surface_base.run left their cfg_on_fail
rows (refused, halted) pointing at steps that are no longer in a work package, which configmaint.validate reports as 3 coherence errors. They are set
inactive with the steps, through configmaint.apply_logged(). Idempotent.

Usage:
    python iba/app/migration/surface_maps_fix_2361_v1_20261106.py [--db PATH]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-SURFACE-MAPS-FIX-20261106"
STEPS = ["surface_base.status", "surface_base.run"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    rows = conn.execute("SELECT step, condition FROM cfg_on_fail WHERE step IN (?,?) AND inactive=0", STEPS).fetchall()
    grants = conn.execute("SELECT writer, table_name FROM cfg_write_grant WHERE writer IN (?,?) AND inactive=0", STEPS).fetchall()
    for step, cond in rows:
        apply_logged(conn, RUN_ID, "cfg_on_fail", "update", {"step": step, "condition": cond}, {"inactive": 1})
    for w, t in grants:
        apply_logged(conn, RUN_ID, "cfg_write_grant", "update", {"writer": w, "table_name": t, "database": "iba"}, {"inactive": 1})
    conn.commit()
    print(f"applied (run {RUN_ID}): {len(rows)} on_fail row(s) and {len(grants)} grant(s) set inactive" if rows or grants else "already applied: nothing changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
