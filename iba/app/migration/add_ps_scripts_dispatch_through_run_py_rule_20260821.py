"""One-off migration: escalation #8 -- researcher asked to confirm a governance rule exists that
every active PS script must dispatch through run.py, so the item can close either against the
existing rule or a newly-created one. Checked live against cfg_behaviour_rule and GOVERNANCE.md
directly: no such rule existed anywhere (rule 41, 'every-interactive-module-needs-ps-script', is
the adjacent-but-different rule -- PS script MUST exist, not PS script MUST dispatch through
run.py). Creates it.

Written to be honest against live reality, not a blanket claim: #8 v1's own investigation (this
session) found 8 of 45 PS scripts under iba/app/ps do NOT dispatch through run.py. Two of those
are legitimate, permanent architectural exceptions (named in the rule text); the other 6 are real,
current non-compliance, NOT silently declared fixed by this rule's existence -- tracked forward as
their own escalation (#767) rather than left to vanish when #8 closes.

Same class of migration as bootstrap_behaviour_rules_cycle4_v1_20260818.py -- writes directly into
cfg_behaviour_rule via raw sqlite3, same reasoning already established for that whole file: a
one-off content-seeding script, config_exempt in cfgquality's own utility registry.
"""
import datetime
import pathlib
import sqlite3
import sys

DB_PATH = pathlib.Path(__file__).resolve().parents[1] / "db" / "iba.db"

RULE_TEXT = (
    "Every active PS script under `governance.scripts_ps_dir` (`iba/app/ps/`) that performs a "
    "real project operation dispatches through `run.py` (`python -m iba.app.run <package> --step "
    "<step> --run-id <id>`) -- not a direct call into the underlying Python module. Dispatching "
    "through run.py is what gives an operation a real `run` row, a `run_id`, `cfg_step` "
    "registration, and `module_blocking` protection; a script that calls its module directly "
    "leaves no record anywhere that it ran, when, or with what result -- not a partial record, "
    "none (escalation #8, checked live 2026-08-20: 8 of 45 scripts bypassed run.py this way). "
    "Two named exceptions, both permanent and architectural, not violations: (1) `Start-Iba.ps1` "
    "-- necessarily, since it bootstraps what run.py itself depends on; (2) `Escalation.ps1`'s "
    "`-Action Raise/Update/AnswerRun` -- a deliberate manual front door onto the escalation "
    "system's own backlog workflow, not a pipeline run (its `-Action List/History` DO dispatch "
    "through run.py, work package `escalation-reporting`, fixed this session per D4/D16/D23). Any "
    "other bypass is real non-compliance, not a third exception -- tracked as its own escalation, "
    "not silently accepted."
)

ENFORCED_BY = (
    "not yet mechanically checked -- no configmaint.validate scan exists for 'does this PS script "
    "call run.py'. Known live non-compliance as of 2026-08-21, NOT retroactively fixed by this "
    "rule's creation: Behaviour.ps1, Debate-Run.ps1 (its post-run side-call to "
    "iba.app.tools.build_debate_report specifically), and 5 lowercase-hyphenated one-off scripts "
    "(create-iba-view-template.ps1, create-passage-view-and-export.ps1, "
    "create-passages-by-book-view-and-export.ps1, export-iba-config-tables.ps1, "
    "generate-iba-db-schema-report.ps1) -- tracked at escalation #767."
)


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id FROM cfg_behaviour_rule WHERE rule_key=?",
                ("every-active-ps-script-dispatches-through-run-py",))
    if cur.fetchone():
        print("rule already present -- no-op")
        conn.close()
        return 0
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    cur.execute(
        "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, enforced_by, "
        "added_at, active) VALUES (?,?,?,?,?,?,1)",
        ("development", "every-active-ps-script-dispatches-through-run-py", RULE_TEXT,
         "researcher, 2026-08-21 (escalation #8)", ENFORCED_BY, now))
    conn.commit()
    print(f"inserted rule id={cur.lastrowid}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
