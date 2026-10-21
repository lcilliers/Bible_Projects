"""init.py — the app bootstrap. Prepare the environment; report ready.

The startup sequence, idempotent:
  1. validate the config seeds (cfgcheck) — refuse to start on incoherent config
  2. load the config into the DB if it is not already there (or --reload to reseed)
  3. build the data tables from the config if they are missing (or --reset to rebuild)
  4. pre-flight STEP — up AND answering with the tagged module
  5. how the last session ended (S6, escalation #2173): uncommitted work, a missing close
  6. deliver the rules in full: every governance.* setting, active behaviour rule and active
     escalation rule (#305; #2173 P2 A) — the input to the session compliance file
  7. print the status

A check that passes is silent; only a problem is printed, and problems come first (#2173).

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
from .lib import cfgload, compliance, db as dbmod, sessionwindow


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
    problems: list[str] = []          # printed first; a passing check prints nothing (P0)

    # 1-2. config
    if a.reload or not _config_loaded():
        try:
            _, counts = cfgload.load()
        except cfgload.ConfigRejected as e:
            print(f"  ✗ {e}", file=sys.stderr)
            return 1
        problems.append(f"config was (re)loaded from the seeds ({sum(counts.values())} rows in "
                        f"{len(counts)} cfg_* tables) — confirm this was intended")
    cfg = Cfg()

    # 3. data tables
    if a.reset or not _data_tables_exist(cfg):
        dbmod.build(reset_data=a.reset)
        problems.append(f"data tables {'rebuilt' if a.reset else 'created'} "
                        f"({len(cfg.tables())} tables)")

    # 3b. database-path integrity (escalation #723/#727): Cfg.database_path() is the consumer of
    # database.*.path; a configured path that does not exist is path drift.
    for db_name in cfg.enum("project_database"):
        try:
            p = cfg.database_path(db_name)
        except KeyError as e:
            print(f"  ✗ database_path({db_name!r}): {e}", file=sys.stderr)
            return 1
        if not p.exists():
            problems.append(f"database.{db_name}.path is {p}, which does not exist")

    # 4. STEP pre-flight. step.required_for_runs is the config's call (governance.rules_must_be_
    # config_driven); the known-answer probe proves STEP answers, not just that its port is open
    # (start-project step 2's port probe only launches it, #2173 S5).
    from .lib.stepapi import Step, StepUnavailable
    step_required = cfg.setting("step.required_for_runs", True)
    try:
        Step(cfg).up()
        step_ok = True
    except StepUnavailable as e:
        problems.append(f"STEP not ready: {e} — "
                        + ("runs will refuse to start without it" if step_required
                           else "step.required_for_runs=false, runs may proceed"))
        step_ok = False

    # 5. how the last session ended (S6)
    try:
        problems += [f"last session: {x}" for x in sessionwindow.last_close_findings(cfg)]
    except Exception as exc:                      # never hide why the check did not run
        problems.append(f"last-session check could not run: {type(exc).__name__}: {exc}")

    if problems:
        print("\n  NEEDS ACTION:")
        for x in problems:
            print(f"  ! {x}")

    # 6. the rules, in full, from the DB (#305; #2173 P2 A). The session compliance file
    # (Compliance.ps1 -Action Template, then -Action Check -Phase Start) restates each one.
    print("\n  RULES (comply with every one this session; restate each in the compliance file):")
    for line in compliance.deliver_lines(cfg.conn):
        print(line)
    cfg.close()

    if not step_ok and step_required:
        # STEP is required for runs when step.required_for_runs is set
        print("\nNOT READY — STEP is required (step.required_for_runs) and not reachable. "
              "Start STEP, then re-run.")
        return 1
    print("\nREADY." if step_ok else
          "\nREADY (config + DB) — STEP not reachable, step.required_for_runs=false.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
