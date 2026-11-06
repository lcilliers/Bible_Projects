"""ai_client_2361_v1_20261106.py -- escalation #2361, stage 4: registers the AI client, its control steps and the table-driven AI steps.

  config_module  new value `ai`
  settings       ai.allowed_options ["temperature","num_ctx","keep_alive"], ai.retries 1, ai.max_consecutive_failures 3
  work package   ai-control (Ai-Control.ps1): ai.status, ai.prompts, ai.prompt_add, ai.replay, ai.compare
  new steps      surface_base.ask (Surface-Base.ps1 -Action Ask) and group.judge (Surface-Group.ps1 -Action Judge): the AI asked through the
                 client, results in ai_call and the tables, no file
  grants         ai.prompt_add -> cfg_ai_prompt; ai.replay -> ai_call; surface_base.ask -> ai_call, run_batch;
                 group.judge -> ai_call, run_batch, surface_term, surface_event
  on_fail        refused for every new step; halted for the two AI steps
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/ai_client_2361_v1_20261106.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2361-AI-CLIENT-20261106"
MODULE = "ai_client_2361_v1_20261106"
WP = "ai-control"
SETTINGS = [
    ("ai.allowed_options", ["temperature", "num_ctx", "keep_alive"], "the model options a call through the AI client may set (#2361, stage 4): the defaults come "
     "from ollama.temperature, ollama.num_ctx and ollama.keep_alive; a call that sets any other option is refused and writes nothing"),
    ("ai.retries", 1, "how many times the AI client asks again when an attempt fails or the answer is not usable (#2361): 1 means up to two attempts, each its own "
     "ai_call row"),
    ("ai.max_consecutive_failures", 3, "the AI client halts a run after this many questions in a row with no usable answer (#2361, B:124); what was answered is kept"),
]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
HALTED = ("halted, what was answered is kept in ai_call -- the set number of questions in a row got no usable answer (the server or the ssh tunnel stopped answering); "
          "fix the cause and run again, it carries on with the words still waiting (a usage outcome, not recorded as an escalation)")
# (work package, ordinal, step, handler, kind, does)
STEPS = [
    (WP, 0, "ai.status", "iba.app.handlers.ai:status", "utility", "the registers of models and prompts and the calls made by module, step and outcome; -Live asks the server (read-only) -- see lib/aiclient.py (escalation #2361)"),
    (WP, 1, "ai.prompts", "iba.app.handlers.ai:prompts", "utility", "every version of every prompt, or of -Key (read-only) -- see lib/aiclient.py (escalation #2361)"),
    (WP, 2, "ai.prompt_add", "iba.app.handlers.ai:prompt_add", "operations", "a new version of a prompt with its change note; -Activate retires the active version (append-only register) -- see lib/aiclient.py (escalation #2361)"),
    (WP, 3, "ai.replay", "iba.app.handlers.ai:replay", "operations", "send a stored request (-Call) again and say whether the answer is the same; recorded as step replay -- see lib/aiclient.py (escalation #2361)"),
    (WP, 4, "ai.compare", "iba.app.handlers.ai:compare", "utility", "per prompt version and model: answered, refused, failed, seconds, tokens for a step (-Step) (read-only) -- see lib/aiclient.py (escalation #2361)"),
    ("surface-base", 2, "surface_base.ask", "iba.app.handlers.surfacebase:ask", "operations", "ask the AI through the client for the base of the surfaces the resolve module leaves unmatched; one ai_call row per attempt; -Limit, -Retry; no file -- see lib/aiclient.py (escalation #2361)"),
    ("surface-group", 2, "group.judge", "iba.app.handlers.surfacegroup:judge", "operations", "ask the AI through the client for the group of the surfaces not yet judged; the group, reason and model go on the surface_term; -Limit, -Retry; no file -- see lib/aiclient.py (escalation #2361)"),
]
HALT_STEPS = ["surface_base.ask", "group.judge"]
GRANTS = [("ai.prompt_add", "cfg_ai_prompt"), ("ai.replay", "ai_call"), ("surface_base.ask", "ai_call"), ("surface_base.ask", "run_batch"),
          ("group.judge", "ai_call"), ("group.judge", "run_batch"), ("group.judge", "surface_term"), ("group.judge", "surface_event")]
UTILITIES = [
    ("aiclient", "iba/app/lib/aiclient.py", 0, "aiclient.py -- the one route to the AI models on zeta-assist: active model and prompt, options within settings, server "
     "check, halt rule, one ai_call row per attempt (escalation #2361).", 0, None),
    ("handlers_ai", "iba/app/handlers/ai.py", 0, "handlers/ai.py -- the run.py handlers for work package ai-control (Ai-Control.ps1, escalation #2361).", 1,
     "thin adapter: every setting is read in lib/aiclient.py (read_settings, through Cfg.setting)"),
    ("Ai-Control.ps1", "iba/app/ps/Ai-Control.ps1", 0, "PS entry point for the AI control and view (escalation #2361): Status, Prompts, PromptAdd, Replay, Compare; "
     "dispatches through run.py, work package ai-control.", 1, "thin wrapper; config is read by the handlers through run.py"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2361 stage 4: registers the AI client, its control steps and the "
     f"table-driven AI steps; run_id {RUN_ID}.", 1, "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='ai'"):
        nxt = conn.execute("SELECT COALESCE(MAX(ordinal),0)+1 FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "ai", "ordinal": nxt, "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": "ai", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Ai-Control.ps1", "runs_over": "none", "chained": 0,
                                                       "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for wp, ordinal, step, handler, kind, does in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": wp, "ordinal": ordinal, "step": step, "handler": handler, "scope": "none", "does": does,
                                                   "inactive": 0, "kind": kind}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None, "message": REFUSED,
                                                      "route": "terminal", "inactive": 0}))
    for step in HALT_STEPS:
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='halted'", step):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "halted", "path": "report-continue", "resolver": None, "message": HALTED,
                                                      "route": "terminal", "inactive": 0}))
    for w, t in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", w, t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": w, "table_name": t, "database": "iba", "inactive": 0}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2361-ai-client', named=True)}")
    try:
        conn.execute("SAVEPOINT ai_client")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE ai_client")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO ai_client")
        conn.execute("RELEASE ai_client")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
