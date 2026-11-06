"""surface_hygiene_2361_v1_20261106.py -- escalation #2361, stage 6: registers lib/surfacehygiene.py (the working-file and junk rules of the surface cycle,
checked by configmaint.validate and shown in the config report as "Surface cycle hygiene"). Through configmaint.apply_logged(). Idempotent.

Usage:
    python iba/app/migration/surface_hygiene_2361_v1_20261106.py [--db PATH]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-SURFACE-HYGIENE-20261106"
MODULE = "surface_hygiene_2361_v1_20261106"
ROWS = [
    ("surfacehygiene", "iba/app/lib/surfacehygiene.py", 0, "surfacehygiene.py -- the working-file and junk rules of the surface cycle (surfaces.junk_rules, working_files_root, "
     "exports_root, discarded_root), checked: a live junk surface, a stray analytic file (escalation #2361).", 0, None),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2361 stage 6: registers surfacehygiene; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    n = 0
    for module, path, inactive, purpose, exempt, reason in ROWS:
        if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone() is None:
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive,
                                                                  "config_exempt": exempt, "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                                                                  "crash_escalation_note": None})
            n += 1
    conn.commit()
    print(f"applied (run {RUN_ID}): {n} utility row(s)" if n else "already applied: nothing changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
