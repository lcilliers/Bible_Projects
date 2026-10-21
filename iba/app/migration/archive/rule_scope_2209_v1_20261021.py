"""rule_scope_2209_v1_20261021.py -- escalation #2209 part (a): every rule knows the operations it
governs. Creates cfg_rule_scope (one row per rule-to-operation link), registers it in
cfg_table/cfg_column, adds cfg_enum rule_scope_kind (general, ps, command, path) and links every
active behaviour rule, escalation rule and governance setting that is a rule (not in
compliance.value_settings). Method rules keep their own cfg_method_rule.step link; the method rules
of steps already retired are deactivated (a missed cascade).

The mapping is Claude's classification (inferential, rule 4), for the researcher's review as a whole
(#2209). Registers itself (inactive, at its own archive path) in the same transaction. Every cfg_* row
is written through configmaint.apply_logged(); the CREATE TABLE is the one DDL statement. Idempotent.

Usage:
    python iba/app/migration/rule_scope_2209_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2209-RULE-SCOPE-20261021"
MODULE = "rule_scope_2209_v1_20261021"
FILLED = f"migration/archive/{MODULE}.py"

DDL = """CREATE TABLE cfg_rule_scope (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_ref    TEXT NOT NULL,
    scope_kind  TEXT NOT NULL,
    scope_value TEXT NOT NULL,
    inactive    INTEGER NOT NULL DEFAULT 0,
    UNIQUE(rule_ref, scope_kind, scope_value)
)"""

COLUMNS = [
    ("id", "INTEGER", 1, 1, None, "surrogate key", None),
    ("rule_ref", "TEXT", 0, 1, None, "the rule: B:<cfg_behaviour_rule.id>, E:<cfg_escalation.id> or "
     "G:<cfg_setting.key of a governance rule>", None),
    ("scope_kind", "TEXT", 0, 1, None, "what kind of operation the rule governs: general (all work, "
     "delivered at start), ps (a PS tool), command (git, migration, sqlite), path (a file written)",
     "enum.rule_scope_kind"),
    ("scope_value", "TEXT", 0, 1, None, "the operation: a PS script name with an optional -Action/-Step "
     "(Escalation.ps1 -Action Update), a command family (git, migration, sqlite), a repo-relative path "
     "glob (iba/app/**, **), or * for general", None),
    ("inactive", "INTEGER", 0, 1, "0", "1 = link no longer in force", None),
]

KINDS = ["general", "ps", "command", "path"]

G, P, C, F = "general", "ps", "command", "path"
APP = (F, "iba/app/**")
ANALYTICS = (F, "_analytics/**")
ESSAY = (F, "_analytics/essay/**")
MIG, SQL, GIT = (C, "migration"), (C, "sqlite"), (C, "git")
ANY = (F, "**")
MD = (F, "**/*.md")
GEN = (G, "*")
ESC = (P, "Escalation.ps1")
LEX = (P, "VerseLexical.ps1")
PROSE = (P, "Prose.ps1")

MAP = {
    # governance settings that are rules
    "G:governance.User_Guide_scope": [APP],
    "G:governance.base_data_spine": [(P, "Spine-Check.ps1"), (P, "New-Word.ps1"), (P, "Lexicon-Parse.ps1"),
                                     (P, "Raw-Backfill.ps1"), LEX],
    "G:governance.behaviour_boundary.backup_recovery": [MIG],
    "G:governance.behaviour_boundary.git_commit": [GIT],
    "G:governance.build_md_on_code_change": [APP],
    "G:governance.config_control": [MIG, (P, "Config-Maintenance.ps1")],
    "G:governance.confmaint_configs": [MIG, (P, "Config-Maintenance.ps1")],
    "G:governance.engineering_documentation_folder": [(F, "iba/docs/**"), (F, "outputs/escalation/**")],
    "G:governance.escalation.scope": [GEN],
    "G:governance.governance_md_on_rule_change": [MIG, APP],
    "G:governance.module.config": [APP],
    "G:governance.module_utility_test_plan": [APP],
    "G:governance.new_utility_registration_timing": [(F, "**/*.py"), (F, "**/*.ps1")],
    "G:governance.no_direct_github_publish": [GIT, ESSAY],
    "G:governance.operational_behaviour_control": [MIG],
    "G:governance.past_precedent_investigation_signals_missing_config": [GEN],
    "G:governance.primary_responsibility": [GEN],
    "G:governance.programme_stages": [GEN],
    "G:governance.project_change_rule": [GEN],
    "G:governance.project_databases": [SQL],
    "G:governance.project_lookups_and_naming_convensions": [MIG],
    "G:governance.project_operations": [GEN],
    "G:governance.prose_canonical_authority": [PROSE],
    "G:governance.ps_worksheet_sync_on_change": [(F, "iba/app/ps/**")],
    "G:governance.redundancy_archiving": [(F, "outputs/**")],
    "G:governance.reports_must_persist": [APP],
    "G:governance.rules_must_be_config_driven": [GEN],
    "G:governance.scope_iba_app": [GEN],
    "G:governance.scope_iba_db": [SQL],
    "G:governance.scope_project": [GEN],
    "G:governance.scope_research_db": [SQL],
    "G:governance.scripts_and_routines": [(F, "**/*.py"), (F, "**/*.ps1")],
    "G:governance.scripts_python_dir": [(F, "iba/app/tools/**")],
    "G:governance.session_log_required_content": [(P, "Session-Close.ps1"), (F, "Logs/**")],
    "G:governance.session_log_triggers_commit": [(P, "Session-Close.ps1"), GIT],
    "G:governance.study_status": [GEN],
    "G:governance.table_columns": [MIG],
    "G:governance.tables": [MIG],
    "G:governance.utility.config": [APP],
    "G:governance.verse_gap_by_design": [(P, "Spine-Check.ps1"), (P, "New-Word.ps1")],
    "G:narrative.inner_being_style_guide_path": [ESSAY],
    "G:registry.folder_naming_convention": [(F, "_analytics/registry/**")],
    "G:report.book_folder_naming_convention": [(F, "_analytics/Bible_Books/**")],
    "G:report.cluster_folder_naming_convention": [(F, "_analytics/Clusters/**"),
                                                  (F, "_analytics/cross-cluster-web/**")],
    # behaviour rules
    "B:1": [GEN], "B:2": [GEN], "B:3": [MD], "B:4": [GEN],
    "B:5": [APP], "B:6": [APP], "B:7": [LEX], "B:8": [LEX], "B:9": [LEX], "B:10": [GEN],
    "B:11": [SQL], "B:13": [SQL], "B:14": [(F, "scripts/SQLite/**"), (F, "**/*.sql")],
    "B:16": [GEN], "B:17": [GEN], "B:18": [GEN], "B:19": [GEN], "B:20": [GEN], "B:21": [GEN],
    "B:22": [GEN], "B:23": [GEN], "B:24": [GEN], "B:25": [GEN], "B:26": [GIT], "B:27": [GEN],
    "B:28": [GEN], "B:29": [APP], "B:31": [GEN], "B:32": [MD], "B:33": [MD], "B:34": [GEN],
    "B:36": [GEN], "B:37": [ANALYTICS], "B:38": [APP], "B:39": [APP], "B:40": [GEN],
    "B:41": [APP], "B:42": [APP], "B:43": [(F, "iba/app/ps/**")], "B:44": [GEN],
    "B:45": [(P, "Escalation.ps1 -Action Update"), (P, "Escalation.ps1 -Action AnswerRun"),
             (P, "Escalation.ps1 -Action ResolveSelfCorrectable"),
             (P, "Escalation.ps1 -Action EscalateToDecision")],
    "B:46": [APP], "B:48": [PROSE, MIG], "B:49": [PROSE, MIG], "B:50": [PROSE, MIG],
    "B:51": [SQL, MIG], "B:52": [PROSE], "B:53": [PROSE], "B:55": [PROSE],
    "B:56": [ANY], "B:57": [(F, "outputs/**"), ANALYTICS], "B:58": [(F, "outputs/**"), ANALYTICS],
    "B:59": [ANY], "B:60": [(F, "outputs/**"), (F, "iba/docs/**")], "B:61": [SQL],
    "B:62": [MIG, APP], "B:63": [(P, "Escalation.ps1 -Action Update"), (P, "Escalation.ps1 -Action Correction")],
    "B:64": [(F, "outputs/escalation/**"), (F, "iba/docs/**")], "B:65": [(F, "outputs/**")],
    "B:66": [(P, "Cluster-Assign.ps1"), (P, "ClusterSubgroup.ps1")], "B:67": [SQL], "B:68": [LEX],
    "B:75": [MIG], "B:80": [MD], "B:81": [(P, "Compliance.ps1")], "B:82": [(P, "Session-Close.ps1"), GIT],
    "B:83": [GEN], "B:96": [ANY], "B:97": [GEN], "B:98": [GEN], "B:99": [GEN], "B:100": [GEN],
    "B:101": [GEN], "B:102": [GEN], "B:103": [ANY], "B:104": [MIG], "B:105": [GEN],
    "B:106": [(F, "outputs/escalation/**")], "B:107": [SQL], "B:108": [ANY],
    # study rules (delivered at all only while the study is active)
    "B:69": [ANALYTICS], "B:70": [ANALYTICS, (P, "Cluster-Assign.ps1")], "B:71": [ANALYTICS, SQL],
    "B:72": [ANALYTICS], "B:73": [ANALYTICS], "B:74": [(P, "Escalation.ps1 -Action Thread"), ANALYTICS],
    "B:76": [(P, "Narrative-Register.ps1"), ESSAY], "B:77": [ESSAY, (P, "Narrative-Register.ps1")],
    "B:78": [(P, "Narrative-Register.ps1"), ESSAY], "B:79": [ANALYTICS], "B:84": [ANALYTICS],
    "B:85": [ESSAY, PROSE], "B:86": [ESSAY], "B:87": [ESSAY], "B:88": [ANALYTICS], "B:89": [ANALYTICS],
    "B:90": [ESSAY], "B:91": [ESSAY], "B:92": [ANALYTICS], "B:93": [ANALYTICS], "B:94": [ANALYTICS],
    "B:95": [ANALYTICS, (P, "New-Word.ps1")], "B:109": [ANALYTICS], "B:110": [ANALYTICS],
    "B:111": [ANALYTICS], "B:112": [ESSAY],
    # escalation rules
    "E:1": [ESC], "E:2": [ESC], "E:3": [ESC], "E:4": [GEN], "E:5": [GEN], "E:7": [ESC],
    "E:11": [ESC], "E:12": [ESC], "E:13": [ESC], "E:15": [ESC], "E:16": [ESC], "E:17": [ESC],
    "E:18": [ESC],
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    exists = conn.execute("SELECT 1 FROM sqlite_master WHERE name='cfg_rule_scope'").fetchone()
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_table WHERE name='cfg_rule_scope'").fetchone():
        ops.append(("cfg_table", "insert", {}, {
            "database": "iba", "name": "cfg_rule_scope", "category": "rule", "inactive": 0,
            "grain": "one row per link between a rule and an operation it governs",
            "use": "#2209: which operations each rule governs, so the rules of an operation are put in "
                   "front of Claude when it is used (.claude/hooks/rules_at_point_of_use.py) and "
                   "configmaint.validate can check every rule and every operation is linked"}))
    for i, (name, typ, pk, nn, dflt, use, exp) in enumerate(COLUMNS):
        if not conn.execute("SELECT 1 FROM cfg_column WHERE table_name='cfg_rule_scope' AND name=?",
                            (name,)).fetchone():
            ops.append(("cfg_column", "insert", {}, {
                "database": "iba", "table_name": "cfg_rule_scope", "name": name, "ordinal": i,
                "type": typ, "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": None,
                "use": use, "expectation": exp, "source": None, "filled_by": FILLED, "inactive": 0}))
    for i, k in enumerate(KINDS):
        if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='rule_scope_kind' AND value=?", (k,)).fetchone():
            ops.append(("cfg_enum", "insert", {}, {"name": "rule_scope_kind", "value": k, "ordinal": i,
                                                   "inactive": 0}))
    have = set()
    if exists:
        have = {tuple(r) for r in conn.execute("SELECT rule_ref, scope_kind, scope_value FROM cfg_rule_scope")}
    for ref, scopes in MAP.items():
        for kind, value in scopes:
            if (ref, kind, value) not in have:
                ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": ref, "scope_kind": kind,
                                                             "scope_value": value, "inactive": 0}))
    # method rules of steps already retired (lexical.enrich: BUILD.md, #1753; passage.suggest_boundary:
    # BUILD.md sec 370, #2201): the cascade to their method rules was missed
    for (mid,) in conn.execute(
            "SELECT m.id FROM cfg_method_rule m JOIN cfg_step s ON s.step = m.step "
            "WHERE m.active=1 AND s.inactive=1").fetchall():
        ops.append(("cfg_method_rule", "update", {"id": mid}, {"active": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2209: creates cfg_rule_scope and links every "
                       f"rule to its operations, through configmaint.apply_logged under run_id {RUN_ID}. "
                       f"inactive=1 once applied."}))
    if a.dry_run:
        print(f"DRY RUN -- {'table exists' if exists else 'CREATE TABLE'} + {len(ops)} write(s)")
        return 0
    if exists and not ops:
        print("already applied -- skipped")
        return 0
    with conn:
        if not exists:
            conn.execute(DDL)
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{'CREATE TABLE + ' if not exists else ''}{len(ops)} write(s) applied (run {RUN_ID}, "
          f"logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
