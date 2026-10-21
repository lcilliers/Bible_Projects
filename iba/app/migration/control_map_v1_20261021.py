"""control_map_v1_20261021.py -- escalation #2180 (option A of the #2179 review; an element of the
IBA app reset, #2177): the control map, held in config.

Researcher, 2026-10-21, verbatim (approving #2179): "proceed with A, then B and D. History that
are replaced with a new or changed version, in every file or document or table must be handled in
such a way that it is not read every time and is only kept for deliberate read to assess a
historic status. ... There should be no instance of the same rule in multiple documents. I am not
sure that Claude, Build, and Governance must all be maintained - they should either have simple
pointers (or serve distinct separate purposes that are not duplications)."

Builds:
  - cfg_control_home: one row per kind of control content -> its ONE home, who reads it and when,
    and where its replaced versions go (kept out of the routine read path). Registered in
    cfg_table / cfg_column / cfg_table_purpose / cfg_write_grant, with two cfg_enum sets
    (control_home_type, control_read_when).
  - cfg_behaviour_rule 3 (single-authority-pointer-not-copy): names cfg_control_home as the map
    of homes; source gains the researcher's 2026-10-21 words.
  - cfg_report_section: section 15 of CONFIG-REPORT.md shows the map (lib/cfgreport.py).
  - cfg_setting governance.procedural_document_taxonomy: retired (inactive=1); the map replaces
    its four-way taxonomy, which was never applied (its own text says so).

Every cfg_* row write goes through configmaint.apply_logged() (Developer Mode removes propose's
gate, never the audit). The CREATE TABLE is DDL. Idempotent: an existing row is skipped. One
transaction.

Usage:
    python iba/app/migration/control_map_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2180-CONTROL-MAP-20261021"
FILLED_BY = "migration/control_map_v1_20261021.py"
SRC = "escalation #2180 (#2179 option A), researcher 2026-10-21"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

DDL = """CREATE TABLE IF NOT EXISTS cfg_control_home (
    kind          TEXT PRIMARY KEY,
    description   TEXT NOT NULL,
    home_type     TEXT NOT NULL,
    home          TEXT NOT NULL,
    read_when     TEXT NOT NULL,
    history_home  TEXT NOT NULL,
    source        TEXT NOT NULL,
    added_at      TEXT NOT NULL,
    inactive      INTEGER NOT NULL DEFAULT 0
)"""

COLUMNS = [
    ("kind", "TEXT", 1, 1, "the kind of control content (e.g. behaviour_rule, tool_usage) -- one row each"),
    ("description", "TEXT", 0, 1, "what content of this kind is, and what its home holds and does not hold"),
    ("home_type", "TEXT", 0, 1, "cfg_enum control_home_type: cfg_table, db_table, document, folder or harness"),
    ("home", "TEXT", 0, 1, "the ONE place content of this kind lives; every other place names it, never restates it"),
    ("read_when", "TEXT", 0, 1, "cfg_enum control_read_when: when the home is read (always, session_start, when_invoked, when_needed, history_only)"),
    ("history_home", "TEXT", 0, 1, "where a replaced or changed version of this content goes: out of the routine read path, kept for deliberate reading of a past state"),
    ("source", "TEXT", 0, 1, "the ruling or escalation the row comes from"),
    ("added_at", "TEXT", 0, 1, "when the row was added (ISO-8601 UTC)"),
    ("inactive", "INTEGER", 0, 1, "0=active, 1=retired (kept as history)"),
]

EXPECT = {"home_type": "enum.control_home_type", "read_when": "enum.control_read_when"}

ENUMS = {
    "control_home_type": ["cfg_table", "db_table", "document", "folder", "harness"],
    "control_read_when": ["always", "session_start", "when_invoked", "when_needed", "history_only"],
}

# kind, home_type, home, read_when, history_home, description
ROWS = [
    ("session_entry", "document", "CLAUDE.md", "always", "git history of CLAUDE.md",
     "What the Claude Code harness loads into every conversation. Holds only: what the project is, "
     "how a session starts (/start-project or /developer-mode), and pointers to this map, CHARTER.md "
     "and USER-GUIDE.md. No rule text, no study or work state, no history (#2181)."),
    ("objective", "document", "iba/app/CHARTER.md", "when_needed", "git history of CHARTER.md",
     "What the IBA app is for, in the researcher's words. Changed only on the researcher's direct "
     "instruction."),
    ("behaviour_rule", "cfg_table", "cfg_behaviour_rule", "session_start",
     "cfg_change_detail (prior row state); retired rows inactive=1",
     "How Claude and the app must act: every operational, process, interaction, filing and "
     "study-method rule. A rule exists here once; every other place names it by rule_key and does "
     "not restate it (rule 3)."),
    ("escalation_rule", "cfg_table",
     "cfg_escalation, with cfg_escalation_requirement, cfg_escalation_transition, cfg_status_flow",
     "session_start", "cfg_change_detail (prior row state); retired rows inactive",
     "How escalations are raised, moved and closed."),
    ("setting", "cfg_table", "cfg_setting", "when_needed",
     "cfg_change_detail (prior row state); retired rows inactive=1",
     "Named values the code and routines read: paths, thresholds, governance settings."),
    ("enum", "cfg_table", "cfg_enum", "when_needed", "cfg_change_detail; retired members inactive=1",
     "The allowed values of every controlled field."),
    ("schema", "cfg_table", "cfg_table, cfg_column, cfg_table_purpose, cfg_unique, cfg_index",
     "when_needed", "cfg_change_detail; retired rows inactive=1",
     "What each table and column is, holds and is for."),
    ("app_procedure", "cfg_table",
     "cfg_work_package, cfg_step, cfg_utility, cfg_on_fail, cfg_write_grant, cfg_report",
     "when_needed", "cfg_change_detail; retired rows inactive",
     "What the app runs, in what order, what happens on failure, and who may write what."),
    ("session_procedure", "document",
     ".claude/commands/ (start-project.md, session-close.md, developer-mode.md, exit-developer-mode.md)",
     "when_invoked", "git history of .claude/commands/",
     "The order of calls of each session routine. Names rules by key; holds no rule text."),
    ("harness_control", "harness", ".claude/settings.json and .claude/hooks/", "always",
     "git history of .claude/",
     "Hooks, permissions and the statusline that the Claude Code harness enforces. "
     ".claude/settings.local.json and the user-level ~/.claude/settings.json hold no project rule."),
    ("mechanism", "document", "iba/app/GOVERNANCE.md", "when_needed", "iba/app/BUILD.md",
     "How the config governs the code, as it is now: the config store, the change path, the two "
     "modes, what is enforced and what is not. Current state only; names rules by key; no dated "
     "history (history goes to BUILD.md)."),
    ("tool_usage", "document", "iba/app/USER-GUIDE.md", "when_needed", "git history of USER-GUIDE.md",
     "How to run each tool, as it is now. Current state only."),
    ("change_history", "document", "iba/app/BUILD.md", "history_only",
     "BUILD.md is itself history; with cfg_change_detail, escalation_history and git",
     "The dated record of what changed in the app (code, config, control documents) and why. Read "
     "only deliberately, to assess a past state; never the source for how things are now."),
    ("open_item", "db_table", "escalation", "session_start", "escalation_history",
     "Every open item, task, issue, decision or thread (rule 40). No other task ledger."),
    ("researcher_ruling", "db_table",
     "escalation_history (the comment on the escalation the ruling answers)", "when_needed",
     "escalation_history is itself history",
     "The researcher's decisions, verbatim. A rule that results goes to its cfg row, with the "
     "ruling in that row's source."),
    ("study_state", "db_table",
     "escalation (strand escalations and type=thread items), narrative_chapter, the narrative claim "
     "register tables", "when_needed", "escalation_history; the register's change records",
     "Where the study stands: strands, what is read, woven, held or forwarded, the chapters and "
     "their claims. Not held in CLAUDE.md or memory."),
    ("study_method", "folder",
     "Workflow/Instructions/ -- one live file per subject, named by a cfg_setting path",
     "when_needed", "Workflow/Instructions/archive/",
     "How study work is done (reading, weaving, writing). Rules drawn from a method file live in "
     "cfg_behaviour_rule; the file explains, it does not restate."),
    ("claude_memory", "harness", "Claude Code project memory (~/.claude/projects/C--Bible-study-projects/memory/)",
     "always", "the memory folder's archive files",
     "Only what config cannot hold (who the researcher is; pointers). Never a rule held in config "
     "(#2184 settles the contents)."),
    ("generated_report", "folder", "the path a *.report_path cfg_setting names", "when_needed",
     "the report folder's archive/",
     "Output a tool writes. Never edited by hand and never a source; regenerated, not maintained."),
    ("escalation_deliverable", "folder", "outputs/escalation/ ({id}- prefix)", "when_needed",
     "outputs/escalation/archive/",
     "An authored document produced for one escalation's work (rules 60, 64)."),
    ("engineering_note", "folder", "iba/docs/", "when_needed", "iba/docs/archive/",
     "Engineering or design notes not tied to one escalation (rule 60)."),
    ("session_record", "folder", "Logs/ (governance.session_log_dir)", "history_only",
     "Logs/ is itself history", "One log per session: what the session did and decided."),
    ("study_output", "folder",
     "_analytics/ (cluster folders per report.cluster_folder_naming_convention; narrative chapters "
     "in _analytics/essay/spirit_soul_body/inner-being-narrative/)", "when_needed",
     "each folder's archive/", "The study's working files and the narrative itself."),
]

PURPOSE = ("The control map: for each kind of control content, its ONE home, when that home is read, "
           "and where replaced versions go so they are not read routinely.")
SUCCESS = ("Every control file, table and folder in the project is the home of a row here or is "
           "history; no rule or setting is held in two homes; every always-read home holds only its "
           "row's content.")

RULE3_ADD = (" The home of each kind of content is cfg_control_home (the control map, escalation "
             "#2180): content lives in its kind's home only.")
RULE3_SRC_ADD = (" | 2026-10-21 (escalation #2180), researcher verbatim: \"There should be no instance "
                 "of the same rule in multiple documents.\"")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if a.dry_run:
        print(f"DRY RUN -- would create cfg_control_home with {len(ROWS)} rows")
        return 0
    n = 0
    with conn:
        conn.execute(DDL)
        have = lambda sql, p: conn.execute(sql, p).fetchone() is not None  # noqa: E731
        if not have("SELECT 1 FROM cfg_table WHERE database='iba' AND name='cfg_control_home'", ()):
            apply_logged(conn, RUN_ID, "cfg_table", "insert", {}, {
                "database": "iba", "name": "cfg_control_home",
                "grain": "one row per kind of control content",
                "use": PURPOSE + " Escalation #2180.", "inactive": 0, "category": "rule"}); n += 1
        for i, (col, typ, pk, nn, use) in enumerate(COLUMNS):
            if not have("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='cfg_control_home' "
                        "AND name=?", (col,)):
                apply_logged(conn, RUN_ID, "cfg_column", "insert", {}, {
                    "database": "iba", "table_name": "cfg_control_home", "name": col, "ordinal": i,
                    "type": typ, "is_pk": pk, "notnull": nn, "is_unique": 0, "use": use,
                    "expectation": EXPECT.get(col),
                    "filled_by": FILLED_BY, "inactive": 0}); n += 1
        for kind, text in (("purpose", PURPOSE), ("success", SUCCESS)):
            if not have("SELECT 1 FROM cfg_table_purpose WHERE table_name='cfg_control_home' AND kind=?",
                        (kind,)):
                apply_logged(conn, RUN_ID, "cfg_table_purpose", "insert", {},
                             {"table_name": "cfg_control_home", "kind": kind, "text": text}); n += 1
        if not have("SELECT 1 FROM cfg_write_grant WHERE writer='configmaint.propose' AND "
                    "table_name='cfg_control_home'", ()):
            apply_logged(conn, RUN_ID, "cfg_write_grant", "insert", {}, {
                "writer": "configmaint.propose", "table_name": "cfg_control_home", "database": "iba",
                "inactive": 0}); n += 1
        for name, values in ENUMS.items():
            for i, v in enumerate(values):
                if not have("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, v)):
                    apply_logged(conn, RUN_ID, "cfg_enum", "insert", {},
                                 {"name": name, "value": v, "ordinal": i, "inactive": 0}); n += 1
        for kind, htype, home, rw, hist, desc in ROWS:
            if not have("SELECT 1 FROM cfg_control_home WHERE kind=?", (kind,)):
                apply_logged(conn, RUN_ID, "cfg_control_home", "insert", {}, {
                    "kind": kind, "description": desc, "home_type": htype, "home": home,
                    "read_when": rw, "history_home": hist, "source": SRC, "added_at": NOW,
                    "inactive": 0}); n += 1
        if not have("SELECT 1 FROM cfg_report_section WHERE step='configmaint.report' AND "
                    "section_key='control_map'", ()):
            apply_logged(conn, RUN_ID, "cfg_report_section", "insert", {}, {
                "step": "configmaint.report", "ordinal": 15, "section_key": "control_map",
                "heading": "## 15. Control map — one home per kind of control",
                "toc_label": "15. Control map — one home per kind of control",
                "include": 1, "inactive": 0}); n += 1
        r3 = conn.execute("SELECT rule_text, source FROM cfg_behaviour_rule WHERE id=3").fetchone()
        if r3 and "cfg_control_home" not in r3[0]:
            apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": 3},
                         {"rule_text": r3[0] + RULE3_ADD, "source": (r3[1] or "") + RULE3_SRC_ADD}); n += 1
        t = conn.execute("SELECT inactive FROM cfg_setting WHERE key='governance.procedural_document_taxonomy'").fetchone()
        if t and t[0] == 0:
            apply_logged(conn, RUN_ID, "cfg_setting", "update",
                         {"key": "governance.procedural_document_taxonomy"}, {"inactive": 1}); n += 1
    print(f"{n} audited cfg_* write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
