"""surface_judge_tool_2354_v1_20261102.py -- escalation #2354 (researcher, chat 2026-11-02: the list to group is the
distinct surface of surface_subgroup; "a) behaviours b) states c) beings d) other"; "it is definitively in a or b or
c, else it falls in d"; "you can register it as a tool").

Registers the tool iba/app/ps/Surface-Judge.ps1: work package surface-judge with two steps (status, run), the
'refused' condition of each, and the cfg_utility rows of the script, its handler module, its library and this
script (inactive, at its archive path). The steps write no table, so there is no write grant. Adds the value
`other` to the enums surface_pair_verdict.surface_group and surface_subgroup.surface_group (the first split's
residue) and brings the `use` text of their cfg_column rows to say so. Adds the cfg_setting rows
surface_judge.groups (the four groups of the first split) and surface_judge.word_prompt (the question put to the
server). cfg_* writes go through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/surface_judge_tool_2354_v1_20261102.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2354-SURFACE-JUDGE-TOOL-20261102"
MODULE = "surface_judge_tool_2354_v1_20261102"
WP = "surface-judge"
H = "iba.app.handlers.surfacejudge"
STEPS = [
    ("surface_judge.status", f"{H}:status", "how far a batch file has got against the list of surfaces (read-only); "
     "-Batch -- see lib/surfacejudge.py (escalation #2354)"),
    ("surface_judge.run", f"{H}:run", "judge the surfaces not yet judged, appending one JSON line per surface to the "
     "batch file; -Batch, -Limit; resumable; writes no table -- see lib/surfacejudge.py (escalation #2354)"),
]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
UTILITIES = [
    ("surfacejudge", "iba/app/lib/surfacejudge.py", 0, "surfacejudge.py -- the first split of the concept surfaces "
     "into behaviour, state, being or other by the Ollama server, one call per surface (escalation #2354).", 0, None),
    ("handlers_surfacejudge", "iba/app/handlers/surfacejudge.py", 0, "handlers/surfacejudge.py -- the run.py handlers "
     "for work package surface-judge (Surface-Judge.ps1, escalation #2354).", 0, None),
    ("Surface-Judge.ps1", "iba/app/ps/Surface-Judge.ps1", 0, "PS entry point for the first split of the concept "
     "surfaces (escalation #2354): Status, Run; dispatches through run.py, work package surface-judge.", 1,
     "thin wrapper; config is read by the handlers through run.py"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2354: registers the "
     f"surface-judge tool and the value other; run_id {RUN_ID}.", 1, "one-off migration script -- writes cfg_* rows "
     "through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]
ENUMS = ["surface_pair_verdict.surface_group", "surface_subgroup.surface_group"]
GROUPS = ["behaviour", "inner_being_state", "being", "other"]
GROUPS_USE = ("the groups of the first split of the concept surfaces (#2354): behaviour, inner_being_state, being, "
              "or other. The model answers one of them; the surface goes to the first three only when it definitely "
              "belongs there, otherwise to other, which the researcher cleans up in a later pass")
PROMPT = """You classify one English word or phrase as the ESV Bible uses it, for a study of how Scripture describes the human inner being.
English: "{surface}"

Answer with exactly one group:
- behaviour: something a person does or undergoes, inwardly or outwardly (an act, feeling, thought, speech, choice)
- inner_being_state: a standing condition or characteristic of a person's inner being (righteous, wicked, wise, proud)
- being: an entity: a person, God, a spirit, an angel, or a part of a person such as the heart or the soul
- other: everything else

Give behaviour, inner_being_state or being only when the English definitely belongs there as the Bible uses it. If it does not definitely belong in one of those three, or you cannot tell, answer other. Words that only describe, locate or link something (pronouns, prepositions, adverbs, conjunctions, articles, numerals, degree words) and words with no bearing on a person's inner being are other.
Answer JSON only: {"group":"...","reason":null}
"reason" only for other, under 10 words (else null)."""
PROMPT_USE = ("the question put to the server for each surface in the first split (#2354); {surface} is replaced by "
              "the English string; the answer is JSON with group and reason")
OTHER_USE = (" The value other is the first split's residue: everything not definitely a behaviour, a state or a "
             "being; the researcher cleans it up in a later pass (#2354).")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for enum in ENUMS:
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value='other'", enum):
            top = conn.execute("SELECT MAX(ordinal) FROM cfg_enum WHERE name=?", (enum,)).fetchone()[0]
            ops.append(("cfg_enum", "insert", {}, {"name": enum, "value": "other", "ordinal": top + 1, "inactive": 0}))
        table, col = enum.split(".")
        row = conn.execute("SELECT use FROM cfg_column WHERE database='iba' AND table_name=? AND name=?",
                           (table, col)).fetchone()
        if row is not None and OTHER_USE not in row[0]:
            ops.append(("cfg_column", "update", {"database": "iba", "table_name": table, "name": col},
                        {"use": row[0] + OTHER_USE}))
    for key, value, use in (("surface_judge.groups", json.dumps(GROUPS), GROUPS_USE),
                            ("surface_judge.word_prompt", json.dumps(PROMPT), PROMPT_USE)):
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": value, "use": use,
                                                      "module": "surface_judge", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {
            "name": WP, "ps_script": "iba/app/ps/Surface-Judge.ps1", "runs_over": "none", "chained": 0,
            "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for i, (step, handler, does) in enumerate(STEPS):
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {
                "work_package": WP, "ordinal": i, "step": step, "handler": handler, "scope": "none",
                "does": does, "inactive": 0, "kind": "utility"}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {
                "step": step, "condition": "refused", "path": "report-continue", "resolver": None,
                "message": REFUSED, "route": "terminal", "inactive": 0}))
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
            print(f"  {t} {op} {set_.get('step') or set_.get('module') or set_.get('key') or set_.get('value') or where.get('name')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT surface_judge_reg")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE surface_judge_reg")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_judge_reg")
        conn.execute("RELEASE surface_judge_reg")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
