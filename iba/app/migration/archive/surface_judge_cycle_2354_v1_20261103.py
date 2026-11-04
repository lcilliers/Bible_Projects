"""surface_judge_cycle_2354_v1_20261103.py -- escalation #2354 (researcher, chat 2026-11-03: a coded method that
controls the entire cycle so it can run unattended; stop after a period to let the CPUs cool; a method to report
progress while it runs; a method of interrupting and restarting).

Adds the settings of the cycle (surface_judge.cycle_work_minutes, cycle_cooldown_minutes, cycle_halt_wait_minutes,
cycle_max_halts_in_a_row), the steps surface_judge.cycle / progress / stop of the work package surface-judge with
their routed conditions, and the utility rows of this migration and of ssh_tunnel_2354_v1_20261103.py (not
registered when it ran). The writes go through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/surface_judge_cycle_2354_v1_20261103.py [--db PATH]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2354-SURFACE-JUDGE-CYCLE-20261103"
MODULE = "surface_judge_cycle_2354_v1_20261103"
ONE_OFF = "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"

SETTINGS = [
    ("surface_judge.cycle_work_minutes", 60,
     "how long one work period of the surface judging cycle lasts, in minutes (#2354): the cycle judges surfaces for "
     "this long (the ssh tunnel is open), then rests for cycle_cooldown_minutes. A starting value; the researcher "
     "sets it to what lets the server's CPUs cool"),
    ("surface_judge.cycle_cooldown_minutes", 10,
     "how long the surface judging cycle rests between two work periods, in minutes (#2354), so the server's CPUs "
     "cool; 0 means no rest. A starting value, set by the researcher"),
    ("surface_judge.cycle_halt_wait_minutes", 10,
     "how long the surface judging cycle waits before trying again after a work period that ended with the server "
     "or the ssh tunnel not answering, in minutes (#2354)"),
    ("surface_judge.cycle_max_halts_in_a_row", 3,
     "the surface judging cycle ends (state halted, needs attention) after this many work periods in a row that "
     "made no progress because the server or the ssh tunnel did not answer (#2354)"),
]
STEPS = [
    (2, "surface_judge.cycle", "iba.app.handlers.surfacejudge:cycle",
     "judge the whole list unattended in work periods with a cool-down between, retrying after a halt; writes the "
     "batch file and its progress file, no table; -Batch -- see lib/surfacejudge.py run_cycle (escalation #2354)"),
    (3, "surface_judge.progress", "iba.app.handlers.surfacejudge:progress",
     "report a cycle's progress from its progress file (read-only): state, judged per group, failed, left, speed, "
     "estimated finish; -Batch -- see lib/surfacejudge.py (escalation #2354)"),
    (4, "surface_judge.stop", "iba.app.handlers.surfacejudge:stop",
     "ask a running cycle to end after the surface in hand (writes the stop flag beside the batch file); -Batch -- "
     "see lib/surfacejudge.py (escalation #2354)"),
]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
HALTED = ("halted, the batch file keeps what was judged -- the cycle made no progress for the set number of work "
          "periods in a row (the server or the ssh tunnel did not answer); fix the cause and run Cycle again with the "
          "same -Batch, it resumes (a usage outcome, not recorded as an escalation)")
ON_FAIL = [("surface_judge.cycle", "refused", REFUSED), ("surface_judge.cycle", "halted", HALTED),
           ("surface_judge.progress", "refused", REFUSED), ("surface_judge.stop", "refused", REFUSED)]
UTILITIES = [
    ("surface_judge_cycle_2354_v1_20261103", "iba/app/migration/archive/surface_judge_cycle_2354_v1_20261103.py",
     "ONE-OFF migration -- escalation #2354: the surface judging cycle (settings, steps cycle, progress, stop); "
     f"run_id {RUN_ID}."),
    ("ssh_tunnel_2354_v1_20261103", "iba/app/migration/archive/ssh_tunnel_2354_v1_20261103.py",
     "ONE-OFF migration -- escalation #2354: setting ollama.tunnel_local_port (the run opens an ssh tunnel to the "
     "Ollama server); run_id DEVMODE-2354-SSH-TUNNEL-20261103."),
]
PS_PURPOSE = ("PS entry point for the first split of the concept surfaces (escalation #2354): Status, Run, Cycle, "
              "Progress, Stop; dispatches through run.py, work package surface-judge.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    n = 0

    def exists(sql, *a):
        return conn.execute(sql, a).fetchone() is not None

    for key, value, use in SETTINGS:
        if not exists("SELECT 1 FROM cfg_setting WHERE key=?", key):
            apply_logged(conn, RUN_ID, "cfg_setting", "insert", {},
                         {"key": key, "value": json.dumps(value), "use": use, "module": "surface_judge", "inactive": 0})
            n += 1
    for ordinal, step, handler, does in STEPS:
        if not exists("SELECT 1 FROM cfg_step WHERE step=?", step):
            apply_logged(conn, RUN_ID, "cfg_step", "insert", {},
                         {"work_package": "surface-judge", "ordinal": ordinal, "step": step, "handler": handler,
                          "scope": "none", "does": does, "inactive": 0, "kind": "utility"})
            n += 1
    for step, condition, message in ON_FAIL:
        if not exists("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, condition):
            apply_logged(conn, RUN_ID, "cfg_on_fail", "insert", {},
                         {"step": step, "condition": condition, "path": "report-continue", "resolver": None,
                          "message": message, "route": "terminal", "inactive": 0})
            n += 1
    for module, path, purpose in UTILITIES:
        if not exists("SELECT 1 FROM cfg_utility WHERE module=?", module):
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {},
                         {"module": module, "file_path": path, "purpose": purpose, "inactive": 1, "config_exempt": 1,
                          "config_exempt_reason": ONE_OFF, "crash_escalation_reviewed": 0,
                          "crash_escalation_note": None})
            n += 1
    if conn.execute("SELECT purpose FROM cfg_utility WHERE module='Surface-Judge.ps1'").fetchone()[0] != PS_PURPOSE:
        apply_logged(conn, RUN_ID, "cfg_utility", "update", {"module": "Surface-Judge.ps1"}, {"purpose": PS_PURPOSE})
        n += 1
    conn.commit()
    print(f"{n} apply_logged writes ({'already applied' if n == 0 else 'done'}) on {args.db}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
