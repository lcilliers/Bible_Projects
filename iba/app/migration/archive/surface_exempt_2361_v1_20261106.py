"""surface_exempt_2361_v1_20261106.py -- escalation #2361, stage 2: marks the two new handler modules config_exempt.

handlers/surfacestructure.py and handlers/surfacegroup.py are thin adapters: every setting is read by the lib modules they call
(lib/surfacestructure.read_settings, lib/surfacegroup.read_settings, through Cfg.setting), so the handlers themselves have no Cfg call site.
That is the legitimate zero configmaint.validate asks to be confirmed. Through configmaint.apply_logged(). Idempotent.

Usage:
    python iba/app/migration/surface_exempt_2361_v1_20261106.py [--db PATH]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-SURFACE-EXEMPT-20261106"
REASONS = {
    "handlers_surfacestructure": "thin adapter: every setting is read in lib/surfacestructure.py (read_settings, through Cfg.setting)",
    "handlers_surfacegroup": "thin adapter: every setting is read in lib/surfacegroup.py (read_settings, through Cfg.setting)",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    n = 0
    for module, reason in REASONS.items():
        row = conn.execute("SELECT config_exempt FROM cfg_utility WHERE module=?", (module,)).fetchone()
        if row is None:
            print(f"REFUSED: cfg_utility {module} not found")
            return 2
        if not row[0]:
            apply_logged(conn, RUN_ID, "cfg_utility", "update", {"module": module}, {"config_exempt": 1, "config_exempt_reason": reason})
            n += 1
    conn.commit()
    print(f"applied (run {RUN_ID}): {n} utility row(s) marked config_exempt" if n else "already applied: nothing changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
