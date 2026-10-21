"""rule_delivery_scope_v1_20261021.py -- escalation #2185 (option F of the #2179 review; element of
the IBA app reset, #2177): the start-up print and the compliance restatement are scoped to the
session.

Before: init.py printed every active behaviour rule at every start (about 77 KB with the
governance settings and escalation rules), and the compliance file asked for every one to be
restated -- the study rules while the study is on hold, the code-building rules in a session that
builds nothing. A restatement of a rule that cannot apply is rote, not a reading.

Builds:
  - cfg_behaviour_rule.deliver_when (TEXT NOT NULL DEFAULT 'always'), cfg_enum
    behaviour_rule_deliver_when {always, study_active, developer_mode}, registered in cfg_column
    with an enum expectation (checked by valuequality).
  - cfg_setting behaviour.study_state ('on_hold'), cfg_enum study_state {active, on_hold}: the flag
    lib/compliance reads; governance.study_status keeps the ruling and the reason.
  - deliver_when set per rule: study_active for the study-method rules (class study_method and the
    study rules filed under llm_output, chat, sqlite, documentation); developer_mode for the rules
    that govern building the app's code; the rest stay 'always'.

The code side (lib/compliance.py rules/deliver_lines/template/check_start by mode;
handlers/compliance.py; ps/Compliance.ps1 -Mode) is in the same unit of work. Every cfg_* row write
through configmaint.apply_logged(); the ALTER TABLE is DDL. Idempotent. One transaction.

Usage:
    python iba/app/migration/rule_delivery_scope_v1_20261021.py [--db PATH]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2185-RULE-DELIVERY-SCOPE-20261021"
FILLED_BY = "migration/rule_delivery_scope_v1_20261021.py"

# study rules outside class study_method, by id
STUDY_IDS = [69, 70, 71, 72, 73, 74, 76, 77, 78, 79]
# rules that govern building the app's code (Developer Mode only)
DEV_KEYS = [
    ("llm_output", "sdk-dependency-decision"), ("llm_output", "no-hardcoded-call-params"),
    ("development", "every-interactive-module-needs-ps-script"),
    ("development", "user-guide-updated-same-unit-of-work"),
    ("development", "every-active-ps-script-dispatches-through-run-py"),
    ("development", "test-plan-per-module-utility"),
    ("development", "devmode-config-writes-are-audited"),
    ("development", "developer-mode-scope-and-conduct"),
    ("development", "no-per-item-approval-steps-in-designs"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    one = lambda sql, p=(): conn.execute(sql, p).fetchone()  # noqa: E731
    with conn:
        cols = [r[1] for r in conn.execute("PRAGMA table_info(cfg_behaviour_rule)")]
        if "deliver_when" not in cols:
            conn.execute("ALTER TABLE cfg_behaviour_rule ADD COLUMN deliver_when TEXT NOT NULL "
                         "DEFAULT 'always'")
        if not one("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='cfg_behaviour_rule' "
                   "AND name='deliver_when'"):
            ordinal = one("SELECT MAX(ordinal) FROM cfg_column WHERE database='iba' AND "
                          "table_name='cfg_behaviour_rule'")[0] + 1
            apply_logged(conn, RUN_ID, "cfg_column", "insert", {}, {
                "database": "iba", "table_name": "cfg_behaviour_rule", "name": "deliver_when",
                "ordinal": ordinal, "type": "TEXT", "is_pk": 0, "notnull": 1, "is_unique": 0,
                "dflt": "'always'",
                "use": ("When the rule is delivered at session start and restated in the compliance "
                        "file (lib/compliance.deliver_set): always; study_active (only while "
                        "behaviour.study_state is 'active'); developer_mode (only in a Developer "
                        "Mode session's compliance file). Escalation #2185."),
                "expectation": "enum.behaviour_rule_deliver_when", "filled_by": FILLED_BY,
                "inactive": 0}); n += 1
        for name, values in (("behaviour_rule_deliver_when", ["always", "study_active", "developer_mode"]),
                             ("study_state", ["active", "on_hold"])):
            for i, v in enumerate(values):
                if not one("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, v)):
                    apply_logged(conn, RUN_ID, "cfg_enum", "insert", {},
                                 {"name": name, "value": v, "ordinal": i, "inactive": 0}); n += 1
        if not one("SELECT 1 FROM cfg_setting WHERE key='behaviour.study_state'"):
            apply_logged(conn, RUN_ID, "cfg_setting", "insert", {}, {
                "key": "behaviour.study_state", "value": json.dumps("on_hold"), "module": "behaviour",
                "use": ("The study's state flag (cfg_enum study_state): 'active' delivers the "
                        "study_active rules at start; 'on_hold' withholds them. Set only on the "
                        "researcher's instruction; the ruling and reason are in "
                        "governance.study_status. Escalation #2185."),
                "inactive": 0}); n += 1
        targets = {}
        for (rid,) in conn.execute("SELECT id FROM cfg_behaviour_rule WHERE active=1 AND "
                                   "class='study_method'"):
            targets[rid] = "study_active"
        for rid in STUDY_IDS:
            targets[rid] = "study_active"
        for cls, key in DEV_KEYS:
            r = one("SELECT id FROM cfg_behaviour_rule WHERE class=? AND rule_key=?", (cls, key))
            if r:
                targets[r[0]] = "developer_mode"
        for rid, dw in sorted(targets.items()):
            cur = one("SELECT deliver_when FROM cfg_behaviour_rule WHERE id=?", (rid,))
            if cur and cur[0] != dw:
                apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": rid},
                             {"deliver_when": dw}); n += 1
    print(f"{n} audited cfg_* write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
