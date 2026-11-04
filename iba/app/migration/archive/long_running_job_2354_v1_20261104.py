"""long_running_job_2354_v1_20261104.py -- escalation #2354 (researcher, chat 2026-11-04: "the stoppage occured because
claude on the desktop went to sleep ... the problem is on your side - you ran an extended session in a way that does
not ensure that it would continue running even after the claude close it session"; "update configs to ensure that you
will not miss this important detail when you create the next long running batch").

The surface-judging cycle (about 17 hours) was started in a Claude terminal tab. The tab and its child processes sit in
the app's job object and ended when the app slept and closed its session, 6 hours into the night, with the run row
left at 'running'. This adds the behaviour rule long-running-job-starts-outside-the-session (general scope link) so
the start routine delivers it, and registers itself. The writes go through configmaint.apply_logged(). Idempotent.
One transaction.

Usage:
    python iba/app/migration/long_running_job_2354_v1_20261104.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2354-LONG-RUNNING-JOB-20261104"
MODULE = "long_running_job_2354_v1_20261104"
RULE_KEY = "long-running-job-starts-outside-the-session"
RULE_TEXT = (
    "A job that will run longer than a few minutes (a cycle, a batch, a loop over a list) is started so that it does "
    "not depend on the Claude session or the Claude app. It is never started in a Claude terminal tab, from the "
    "Bash or PowerShell tool as a child process, or in a window opened from them: all of these sit in the app's job "
    "object and end when the app sleeps, restarts or closes its session. It is started through Windows' own process "
    "service (Invoke-CimMethod -ClassName Win32_Process -MethodName Create, parent WmiPrvSE), with its output "
    "written to a log file under Logs/, and the start is checked before it is reported: the process is not in a job "
    "object and the job's own progress is moving. The tool that runs the job gives a way to see its progress, to "
    "stop it and to resume it without repeating work. Windows sleep ends any job; the closing message says how the job was launched, where its log is, how to check, "
    "stop and resume it, and that sleep ends it.")
RULE_SOURCE = (
    "Researcher, chat 2026-11-04 (verbatim, #2354): \"I can confirm that the stoppage occured because claude on the "
    "desktop went to sleep, not because the vm had any issue. So the problem is on your side - you ran an extended "
    "session in a way that does not ensure that it would continue running even after the claude close it session\"; "
    "\"would you be so kind to update configs to ensure that you will not miss this important detail when you create "
    "the next long running batch.\"")
RULE_ENFORCED = ("Context-delivered at session start (rule 81); the procedure is iba/app/USER-GUIDE.md section 8.8 "
                 "(Running a long job). Not hook-enforced: no hook sees how a job was started.")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    row = conn.execute("SELECT id FROM cfg_behaviour_rule WHERE rule_key=?", (RULE_KEY,)).fetchone()
    rid = row[0] if row else conn.execute("SELECT MAX(id) FROM cfg_behaviour_rule").fetchone()[0] + 1
    if row is None:
        ops.append(("cfg_behaviour_rule", "insert", {}, {
            "id": rid, "class": "development", "rule_key": RULE_KEY, "rule_text": RULE_TEXT, "source": RULE_SOURCE,
            "enforced_by": RULE_ENFORCED, "added_at": "2026-11-04T00:00:00Z", "active": 1,
            "enforcement_status": "context_delivered", "deliver_when": "always"}))
    if not has("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='general'", f"B:{rid}"):
        ops.append(("cfg_rule_scope", "insert", {}, {
            "id": conn.execute("SELECT MAX(id) FROM cfg_rule_scope").fetchone()[0] + 1, "rule_ref": f"B:{rid}",
            "scope_kind": "general", "scope_value": "general", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2354: the rule that a long-running job is started outside "
                       f"the Claude session; run_id {RUN_ID}.",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
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
            print(f"  {t} {op} {set_.get('rule_key') or set_.get('rule_ref') or set_.get('module')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT long_job")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE long_job")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO long_job")
        conn.execute("RELEASE long_job")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
