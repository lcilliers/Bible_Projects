"""surface_judge_preflight_2354_v1_20261103.py -- escalation #2354 (researcher, chat 2026-11-03: a routine that
needs the Ollama server must check the connection first; running 16 surfaces against a server that did not answer,
42 s each, "is really poor coding standards").

Adds the config the server check needs: cfg_setting ollama.connect_timeout_seconds (how long the check waits for
the server before refusing to run) and surface_judge.max_consecutive_failures (the run halts after that many
surfaces in a row with no usable answer), and the routed condition `halted` of the step surface_judge.run. The
writes go through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/surface_judge_preflight_2354_v1_20261103.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2354-SURFACE-JUDGE-PREFLIGHT-20261103"
MODULE = "surface_judge_preflight_2354_v1_20261103"
SETTINGS = [
    ("ollama.connect_timeout_seconds", 10, "ollama",
     "how many seconds the check before a run waits for the Ollama server to answer (and to list its models) before "
     "it refuses to run (#2354); not the time allowed for a model to answer, which is ollama.timeout_seconds"),
    ("surface_judge.max_consecutive_failures", 3, "surface_judge",
     "a run of the surface judging halts after this many surfaces in a row with no usable answer, so a server that "
     "went away part-way is not called once per remaining surface (#2354)"),
]
HALTED = ("halted, the batch file keeps what was judged -- the server stopped answering part-way; the surfaces "
          "without an answer are tried again on the next run (a usage outcome, not recorded as an escalation)")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, value, module, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use,
                                                      "module": module, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_step WHERE step='surface_judge.run'"):
        raise SystemExit("REFUSED, nothing written: step surface_judge.run is not registered (run the #2354 tool "
                         "migration first)")
    if not has("SELECT 1 FROM cfg_on_fail WHERE step='surface_judge.run' AND condition='halted'"):
        ops.append(("cfg_on_fail", "insert", {}, {
            "step": "surface_judge.run", "condition": "halted", "path": "report-continue", "resolver": None,
            "message": HALTED, "route": "terminal", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2354: the server check before a surface judging run; "
                       f"run_id {RUN_ID}.", "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {set_.get('key') or set_.get('condition') or set_.get('module')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT sj_preflight")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE sj_preflight")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO sj_preflight")
        conn.execute("RELEASE sj_preflight")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
