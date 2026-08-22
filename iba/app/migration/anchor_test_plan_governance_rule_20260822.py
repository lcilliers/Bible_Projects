"""anchor_test_plan_governance_rule_20260822.py — ONE-OFF, idempotent. Researcher instruction
2026-08-22 (verbatim), prompted directly by escalation #795's two self-found build gaps (approved
spec had a named test that #799's own build never ran, twice):

"I think we got to the stage where we need to have a re-usable test pack for all development tasks.
we already included a governance config that development goes through plan/propose/design - in
detail - approve - the build per the plan - approve. each module or utility in future must have a
test plan. the test plan must include testing all the different interations, params options of each
of the module/utility intended functionality. this test plan must be updated to include modifying
the testing plan for each functional component after a change. the test plan must then run through
after the design, and the results of the test must be included in the resolution of the build. this
instruction must be anchored in governance now. however, the test plan method will be introduced
case by case as further development takes place, rather than trying to develop test plans for all
modules."

Anchors the RULE now, in two places (both read by something real, not just written and forgotten):

  (a) `cfg_behaviour_rule` (class=development, rule_key='test-plan-per-module-utility') — full
      text + rationale, same shape as the existing `decision-points-are-terminal-not-inline` row it
      extends. Checked for coherence by `configmaint.validate`.
  (b) `cfg_setting` (module=governance, key='governance.module_utility_test_plan') — the compact
      form, because `cfg_behaviour_rule` rows are NOT re-surfaced every session (only `configmaint.
      validate` reads them for coherence) while `governance.*` cfg_setting rows ARE explicitly
      printed at every `Start-Iba.ps1` run (`init.py`'s own comment: "its only real usage is being
      surfaced here... otherwise it's a rule that exists only as an unread database row") — the
      researcher's "anchored in governance now" needs the row that's actually read every session,
      not only the row that's internally coherence-checked.

Deliberately does NOT: build a `cfg_test_plan` table, a template, or any test-plan artifact for any
existing module — the researcher was explicit that rollout is case-by-case, starting the next time a
module/utility is designed or changed, not a retrofit now.

    python -m iba.app.migration.anchor_test_plan_governance_rule_20260822
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_MIGRATION_FILE = "iba/app/migration/anchor_test_plan_governance_rule_20260822.py"

_RULE_TEXT = (
    "Each module or utility, from now on (case-by-case as it comes up in development, NOT "
    "retrofitted to existing modules), must have a test plan. The test plan covers every "
    "meaningfully different interaction, parameter, and option combination of that module/"
    "utility's intended functionality -- not a single happy-path example. The test plan is a "
    "living artifact: when a functional component changes, the test plan for that component is "
    "updated in the same unit of work, before the change is considered complete -- the same "
    "'same unit of work' discipline governance.build_md_on_code_change already applies to "
    "BUILD.md. The test plan is RUN after the design is approved and the build (per the approved "
    "plan) is complete -- a required stage inside the existing plan/propose/design (in detail) -> "
    "approve -> build per the plan -> approve cycle, not a separate optional step. The test "
    "results are included IN the build's escalation resolution when requesting final approval -- "
    "not just claimed as 'tested live' in prose without the actual per-case results shown, and "
    "not omitted. Origin: escalation #795, where the approved proposal's own named Stage 2 test "
    "('self_correctable has no reachable AnswerRun path') was written into the design document but "
    "never actually run before the build was reported complete -- twice, once for each half of the "
    "same function. A written-but-unexecuted test is indistinguishable from no test at all."
)

_RULE_SOURCE = (
    "researcher, 2026-08-22, verbatim: \"I think we got to the stage where we need to have a "
    "re-usable test pack for all development tasks... each module or utility in future must have "
    "a test plan. the test plan must include testing all the different interations, params "
    "options of each of the module/utility intended functionality. this test plan must be updated "
    "to include modifying the testing plan for each functional component after a change. the test "
    "plan must then run through after the design, and the results of the test must be included in "
    "the resolution of the build... however, the test plan method will be introduced case by case "
    "as further development takes place, rather than trying to develop test plans for all "
    "modules.\""
)

_RULE_ENFORCED_BY = (
    "No automated check yet -- deliberately, per the researcher's case-by-case rollout instruction "
    "(building a configmaint.validate check now, before any real test plan exists to check against, "
    "would be exactly the 'machinery-heavy design' simple-steps-not-engineered-designs warns "
    "against). Practical enforcement today is manual: the next module/utility design proposal "
    "should name its test plan as part of the design, and the build's resolution should carry the "
    "test plan's actual results. A configmaint.validate check (e.g. 'every active cfg_utility/"
    "cfg_work_package has an associated test plan reference') is a natural candidate to add once "
    "the first real test plan exists and its storage convention (table vs doc) is chosen against "
    "that real case -- not designed speculatively here."
)

_GOVERNANCE_VALUE = (
    "\"From now on, case-by-case as development happens (not retrofitted): every module/utility "
    "design must include a test plan covering all its meaningful interaction/parameter/option "
    "combinations; the test plan is kept current (updated in the same unit of work whenever the "
    "functional component changes); it is RUN after the approved design is built, as a required "
    "stage of the existing plan/propose/design -> approve -> build -> approve cycle; and its actual "
    "results are included in the build's escalation resolution, not just asserted. Full rationale "
    "and origin: cfg_behaviour_rule (development/test-plan-per-module-utility).\""
)

_GOVERNANCE_USE = (
    "Read explicitly every session by init.py's governance-rules printout (Start-Iba.ps1) -- the "
    "only real enforcement a process rule like this has. Applies project-wide, not IBA-only, same "
    "as governance.operational_behaviour_control."
)


def _behaviour_rule(conn, report: list[str]) -> None:
    class_, rule_key = "development", "test-plan-per-module-utility"
    if conn.execute(
            "SELECT 1 FROM cfg_behaviour_rule WHERE class=? AND rule_key=?",
            (class_, rule_key)).fetchone():
        report.append(f"cfg_behaviour_rule ({class_}/{rule_key}) already present")
        return
    conn.execute(
        "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, enforced_by, "
        "added_at, active) VALUES (?,?,?,?,?,datetime('now'),1)",
        (class_, rule_key, _RULE_TEXT, _RULE_SOURCE, _RULE_ENFORCED_BY))
    report.append(f"cfg_behaviour_rule ({class_}/{rule_key}) added")


def _governance_setting(conn, report: list[str]) -> None:
    key = "governance.module_utility_test_plan"
    if conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        report.append(f"cfg_setting {key!r} already present")
        return
    conn.execute(
        "INSERT INTO cfg_setting (key, value, \"use\", module, inactive) VALUES (?,?,?,?,0)",
        (key, _GOVERNANCE_VALUE, _GOVERNANCE_USE, "governance"))
    report.append(f"cfg_setting {key!r} added")


def _utility(conn, report: list[str]) -> None:
    if not conn.execute(
            "SELECT 1 FROM cfg_utility WHERE file_path=?", (_MIGRATION_FILE,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
            "config_exempt_reason, crash_escalation_reviewed) VALUES (?,?,?,0,1,?,0)",
            ("anchor_test_plan_governance_rule", _MIGRATION_FILE,
             "Anchors the researcher's 2026-08-22 test-plan-per-module/utility instruction in "
             "governance (cfg_behaviour_rule + governance.* cfg_setting), escalation #795.",
             "one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same "
             "class as cfgload.py"))
        report.append(f"cfg_utility {_MIGRATION_FILE!r} registered")
    else:
        report.append(f"cfg_utility {_MIGRATION_FILE!r} already registered")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []
    _behaviour_rule(conn, report)
    _governance_setting(conn, report)
    _utility(conn, report)
    conn.commit()
    conn.close()
    print("anchor_test_plan_governance_rule_20260822:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
