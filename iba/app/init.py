"""init.py — the app bootstrap. Prepare the environment; report ready.

The startup sequence, idempotent:
  1. validate the config seeds (cfgcheck) — refuse to start on incoherent config
  2. load the config into the DB if it is not already there (or --reload to reseed)
  3. build the data tables from the config if they are missing (or --reset to rebuild)
  4. pre-flight STEP — up AND answering with the tagged module
  5. print the status

Run it before the first run of a session:
    python -m iba.app.init            # prepare + status (idempotent)
    python -m iba.app.init --reload   # reseed the config from the JSON
    python -m iba.app.init --reset    # rebuild the data tables (drops data)
"""

from __future__ import annotations

import argparse
import sqlite3
import sys

from .lib.cfg import Cfg, DB_PATH
from .lib import cfgload, db as dbmod


def _config_loaded() -> bool:
    if not DB_PATH.exists():
        return False
    try:
        c = sqlite3.connect(DB_PATH)
        c.execute("SELECT value FROM cfg_meta WHERE key='config_version'").fetchone()
        c.close()
        return True
    except sqlite3.Error:
        return False


def _data_tables_exist(cfg: Cfg) -> bool:
    c = sqlite3.connect(DB_PATH)
    have = {r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    c.close()
    return set(cfg.tables()).issubset(have)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reload", action="store_true", help="reseed the config from the JSON")
    ap.add_argument("--reset", action="store_true", help="rebuild the data tables (DROPS data)")
    a = ap.parse_args()

    print("IBA app — startup")

    # 1-2. config
    if a.reload or not _config_loaded():
        try:
            _, counts = cfgload.load()
        except cfgload.ConfigRejected as e:
            print(f"  ✗ {e}", file=sys.stderr)
            return 1
        print(f"  ✓ config loaded ({sum(counts.values())} rows in {len(counts)} cfg_* tables)")
    else:
        print("  ✓ config already loaded (use --reload to reseed)")

    cfg = Cfg()
    print(f"    config_version: {cfg.config_version()}")

    # 3. data tables
    if a.reset or not _data_tables_exist(cfg):
        dbmod.build(reset_data=a.reset)
        print(f"  ✓ data tables {'rebuilt' if a.reset else 'created'} ({len(cfg.tables())} tables)")
    else:
        print(f"  ✓ data tables present ({len(cfg.tables())})")

    # 4. STEP pre-flight
    from .lib.stepapi import Step, StepUnavailable
    try:
        Step(cfg).up()
        print(f"  ✓ STEP up and tagged ({cfg.connection('base_url')}, {cfg.connection('version')})")
        step_ok = True
    except StepUnavailable as e:
        print(f"  ⚠ STEP not ready: {e}")
        print(f"    start the local STEP server, then re-run this. Runs will refuse to start without it.")
        step_ok = False

    cfg.close()
    print("\nREADY." if step_ok else "\nREADY (config + DB) — waiting on STEP.")
    print("  first run:  iba\\app\\ps\\New-Word.ps1 -Word <word> -Source \"<why>\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
