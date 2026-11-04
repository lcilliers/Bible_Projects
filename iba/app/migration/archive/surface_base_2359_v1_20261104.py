"""surface_base_2359_v1_20261104.py -- escalation #2359 (researcher, chat 2026-11-04: "proceed with asking ollama to
determine the base form of the remaining words ... the rule of similar root meaning must be maintained"; approved
the question and the pilot of 20 words).

Registers the tool iba/app/ps/Surface-Base.ps1: work package surface-base with two steps (status, run), the
'refused' condition of each and the 'halted' condition of run, and the cfg_utility rows of the script, its handler
module, its library and this script (inactive, at its archive path). The steps write no table, so there is no write
grant. Adds the cfg_setting rows surface_judge.base_prompt (the question put to the server), base_relations (the
relations the model may answer), base_form_pattern (the shape of a usable base) and base_input_suffix (the end of the
input file's name beside the batch file). cfg_* writes go through configmaint.apply_logged(). Idempotent. One
transaction.

Usage:
    python iba/app/migration/archive/surface_base_2359_v1_20261104.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2359-SURFACE-BASE-20261104"
MODULE = "surface_base_2359_v1_20261104"
WP = "surface-base"
H = "iba.app.handlers.surfacebase"
STEPS = [
    ("surface_base.status", f"{H}:status", "how far a batch file has got against its input list of words (read-only); "
     "-Batch -- see lib/surfacebase.py (escalation #2359)"),
    ("surface_base.run", f"{H}:run", "ask the Ollama server for the base form of the words not yet answered, appending "
     "one JSON line per word to the batch file; -Batch, -Limit; resumable; writes no table -- see lib/surfacebase.py "
     "(escalation #2359)"),
]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
HALTED = ("halted, the batch file keeps what was answered -- the set number of words in a row got no usable answer "
          "(the server or the ssh tunnel stopped answering); fix the cause and run again with the same -Batch, it "
          "resumes (a usage outcome, not recorded as an escalation)")
ON_FAIL = [("surface_base.status", "refused", REFUSED), ("surface_base.run", "refused", REFUSED),
           ("surface_base.run", "halted", HALTED)]
UTILITIES = [
    ("surfacebase", "iba/app/lib/surfacebase.py", 0, "surfacebase.py -- the base form of a surface word, asked of the "
     "Ollama server, one call per word, keeping the rule of similar root meaning (escalation #2359).", 0, None),
    ("handlers_surfacebase", "iba/app/handlers/surfacebase.py", 0, "handlers/surfacebase.py -- the run.py handlers "
     "for work package surface-base (Surface-Base.ps1, escalation #2359).", 0, None),
    ("Surface-Base.ps1", "iba/app/ps/Surface-Base.ps1", 0, "PS entry point for the base form of a surface word "
     "(escalation #2359): Status, Run; dispatches through run.py, work package surface-base.", 1,
     "thin wrapper; config is read by the handlers through run.py"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2359: registers the "
     f"surface-base tool and its settings; run_id {RUN_ID}.", 1, "one-off migration script -- writes cfg_* rows "
     "through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]
PROMPT = """You give the base form of one English word as the ESV Bible uses it, for a study of how Scripture describes the human inner being.
English: "{surface}"

Give a base word only when the English is an inflected or derived form of it AND the two share the same root meaning.
- Inflected forms count: tense, plural, participle, comparative, including irregular ones (sought: seek; wept: weep; grew: grow).
- Derived forms count only when the core meaning stays the same (wonderful: wonder).
- Not the same root meaning, so give the word itself: an opposite (unfaithful, faithless), a different word that only looks similar (lying is not lye), a word whose meaning has moved away from its base, and a word with no base.
Answer JSON only: {"base":"...","relation":"inflection|derivation|none","reason":null}
"reason" only when relation is none and the word looks derived: under 10 words (else null)."""
SETTINGS = [
    ("surface_judge.base_prompt", json.dumps(PROMPT), "the question put to the server for each word in the base-form "
     "step (#2359); {surface} is replaced by the English word; the answer is JSON with base, relation and reason"),
    ("surface_judge.base_relations", json.dumps(["inflection", "derivation", "none"]), "the relations the model may "
     "answer in the base-form step (#2359): inflection (tense, plural, participle, comparative, irregular forms), "
     "derivation (a suffix or prefix that keeps the core meaning), none (no base of the same root meaning)"),
    ("surface_judge.base_form_pattern", json.dumps("[a-z]+(-[a-z]+)*"), "the shape of a usable base word in the "
     "base-form step (#2359): a regular expression the whole base must match (lower-case letters, hyphens between "
     "parts)"),
    ("surface_judge.base_input_suffix", json.dumps("-input.json"), "the end of the input list's file name in the "
     "base-form step (#2359): the words are in <surface_judge.batch_dir>/<Batch><this suffix> as {\"words\": [...]}"),
]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": value, "use": use,
                                                      "module": "surface_judge", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {
            "name": WP, "ps_script": "iba/app/ps/Surface-Base.ps1", "runs_over": "none", "chained": 0,
            "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for i, (step, handler, does) in enumerate(STEPS):
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {
                "work_package": WP, "ordinal": i, "step": step, "handler": handler, "scope": "none",
                "does": does, "inactive": 0, "kind": "utility"}))
    for step, cond, msg in ON_FAIL:
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, cond):
            ops.append(("cfg_on_fail", "insert", {}, {
                "step": step, "condition": cond, "path": "report-continue", "resolver": None,
                "message": msg, "route": "terminal", "inactive": 0}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {
                "module": module, "file_path": path, "purpose": purpose, "inactive": inactive,
                "config_exempt": exempt, "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                "crash_escalation_note": None}))
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
            print(f"  {t} {op} {set_.get('step') or set_.get('module') or set_.get('key') or set_.get('name') or where.get('name')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT surface_base_reg")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE surface_base_reg")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_base_reg")
        conn.execute("RELEASE surface_base_reg")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
