"""escalation_reset_v1_20260816.py — ONE-OFF: the escalation-system reset instructed by the
researcher's "iba table review" (2026-08-16) + `export.cfg_settings shortcomings.csv`, confirmed
in the researcher's follow-up response (`Workflow/Chat_responses/response-tablereviewresponse v1`).

Full context: `outputs/markdown/iba-table-review-response-v1-20260816.md`.

**What this does, in order:**

1. Retrofits the `escalation` table (634 live rows) to the new shape:
   - renames: `word`->`source` (now NOT NULL), `question`->`short_description`,
     `preset`->`context`, `answer`->`next_action`
   - adds: `resolution`, `related_activity`, `next_action_assigned_to`, `answered_by`
   - backfills every renamed/added column from the OLD data (mapping documented inline in
     `_retrofit_escalation()` below — not a blind copy)
   Same method as `migration/retrofit_debate_lexicon_tables.py` (SQLite has no
   `ALTER TABLE ... RENAME COLUMN` + `ADD CONSTRAINT` in one step for this shape of change; build
   `escalation__retrofit` from config-driven DDL via `lib.db.table_ddl()`, copy+transform, verify,
   swap) — but with an explicit column-mapping INSERT, not the generic shared-name copy, because
   this migration renames columns (the generic helper only handles pure additions).
2. Creates `cfg_escalation` — a new rule table for the escalation utility's own control rules
   (duplicate-suppression, source-classification, module-blocking, resolution-precedence, chat-
   routing), same shape/registration convention as `cfg_method_rule`
   (`migration/build_method_rule_table.py`).
3. Updates `cfg_enum`: `escalation_type` (old 4 values -> inactive, new 5:
   task|run_error|issue|notice|config), `escalation_state` (old 4 -> inactive, new 6: raised|
   re-assign|on-hold|closed|withdraw|completed), `escalation_answer` (old 3 -> inactive, replaced
   by new group `escalation_next_action`: approve|reject|revise|hold|noted), new group
   `escalation_assignee`: Claude|Researcher.
4. Registers `escalation`'s new/renamed columns and `cfg_escalation` in `cfg_table`/`cfg_column`
   (`governance.tables`/`governance.table_columns`, applied in the same unit of work — see step 5).
5. Writes the governance/escalation `cfg_setting` rows that are fully worded in the CSV (not the
   blank stubs — those are the researcher's own explicit design-delegation to Claude, applied here
   with the wording confirmed in the chat response) — see `SETTINGS` below.
6. Adds the 3 `cfg_utility` rows missing per escalation #643 (`clusterassign`, `clusterreport`,
   `strongreconcile`).

**What this does NOT do** (deferred, tracked as new escalations by the caller script that runs
after this one — `escalation_reset_v1_20260816_backlog.py`):
- wiring the module-blocking rule into `run.py`'s dispatcher (the rule is recorded in
  `cfg_escalation`; `enforced_by` says "not yet wired")
- the `governance.oneoff_report_dir` relocation (researcher flagged this as "think through", not
  settled — a filing decision, not a mechanical config apply)
- `governance.startup` and the bare/duplicate `naming.` CSV rows (genuinely no content given)
- the project-wide config-driven-rule sweep, `cfg_work_package` registration-check verification,
  the `configmaint.propose` crash (escalation #579)

    python -m iba.app.migration.escalation_reset_v1_20260816
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import Cfg
from ..lib.db import table_ddl

DB_PATH = "iba/app/db/iba.db"

# ── 1. escalation table: cfg_column changes (renames + new columns) ─────────────────────────────

_RENAMES = {
    "word": ("source", 1,
             "the source of the escalation -- 'new-word: <word>' for a word-registration decision, "
             "the generating module name for a code-raised finding, or 'claude'/'researcher' for a "
             "manually-raised item. Required."),
    "question": ("short_description", 0, "the short description of what's being escalated"),
    "preset": ("context", 0, "the context that lets it be answered (JSON)"),
    "answer": ("next_action", 0, "the decision/next action taken: approve | reject | revise | hold | noted"),
}

_NEW_COLUMNS = [
    # (name, ordinal, type, notnull, use, expectation, filled_by)
    ("resolution", 13, "TEXT", 0,
     "what was actually done to resolve the item -- a short description or reference. NOT the "
     "decision itself (see next_action) -- records the outcome, which nothing previously captured.",
     None, "escalation.answer_for_run / manual close"),
    ("related_activity", 14, "TEXT", 0,
     "the process, module, or activity this row relates to -- defaults to at_step for code-raised "
     "rows; set explicitly for manual/task items", None, "escalation.raise / escalation.raise_manual"),
    ("next_action_assigned_to", 15, "TEXT", 0,
     "who should act on this next -- Claude or Researcher", "enum.escalation_assignee",
     "escalation.raise / re-assignment"),
    ("answered_by", 16, "TEXT", 0,
     "who recorded the decision/resolution -- Claude or Researcher. Required BY CONVENTION whenever "
     "a row reaches a terminal state (completed/closed/withdraw) -- enforced in escalation.py's "
     "answer/retract functions, not a DB-level NOT NULL (a raised/on-hold row has none yet).",
     "enum.escalation_assignee", "escalation.answer_for_run / answer_for_word / retract_run"),
]

_TYPE_UPDATE = ("task | run_error | issue | notice | config", "enum.escalation_type")
_STATE_UPDATE = ("raised | re-assign | on-hold | closed | withdraw | completed", "enum.escalation_state")

# ── 2. cfg_escalation ─────────────────────────────────────────────────────────────────────────

CFG_ESCALATION_DDL = """
    CREATE TABLE cfg_escalation (
        id           INTEGER PRIMARY KEY,
        rule_key     TEXT NOT NULL UNIQUE,
        rule_text    TEXT NOT NULL,
        enforced_by  TEXT,
        active       INTEGER NOT NULL DEFAULT 1
    )"""

CFG_ESCALATION_COLUMNS = [
    ("cfg_escalation", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("cfg_escalation", "rule_key", 1, "TEXT", 0, 1, 1, None, None,
     "short slug, unique -- e.g. 'duplicate_suppression'", None, None, None),
    ("cfg_escalation", "rule_text", 2, "TEXT", 0, 1, 0, None, None,
     "the rule's own exact wording -- the operational source of truth", None, None, None),
    ("cfg_escalation", "enforced_by", 3, "TEXT", 0, 0, 0, None, None,
     "code location that mechanically checks this rule, if any -- NULL/'not yet wired' if it "
     "is process discipline, not yet a SQL/code-checkable condition", None, None, None),
    ("cfg_escalation", "active", 4, "INTEGER", 0, 1, 0, "1", None,
     "supersede by setting 0 and inserting a new row, rather than editing/deleting -- history kept",
     None, None, None),
]

CFG_ESCALATION_RULES = [
    ("source_classification",
     "The source of an escalation is one of: code-generated (a validation/quality check -- value "
     "= the generating module name), raised-by-Claude, or raised-by-Researcher. A code-generated "
     "row's source column must include the module as the source.",
     "escalation.raise_ / escalation.raise_manual (source parameter)"),
    ("duplicate_suppression",
     "A duplicate of the same issue in the same state must not be raised again.",
     "escalation.open_duplicate"),
    ("module_blocking",
     "Running a module registered in cfg_utility (or a step registered in cfg_step) is blocked "
     "while it has an unresolved escalation against it (state is one of raised, re-assign).",
     "not yet wired -- scheduled as a task escalation, see the reset's backlog pass"),
    ("resolution_precedence",
     "Escalation resolution takes precedence over any other activity; open items with "
     "next_action_assigned_to='Claude' must be addressed before other work.",
     "session practice (Claude Code) -- not mechanically enforced"),
    ("chat_routing",
     "Chat discussions must be actioned through escalations -- the next action to work on arrives "
     "from an escalation, and the actions/steps identified are recorded in escalations, optionally "
     "by reference to a planning document that carries a whole package of tasks.",
     "session practice (Claude Code) -- not mechanically enforced"),
]

CFG_ESCALATION_TABLE_ROW = (
    "cfg_escalation",
    "One row per discrete, nameable rule governing the escalation utility itself -- config, not "
    "prose (researcher, 2026-08-16 iba-table-review reset). Parallel to cfg_method_rule but scoped "
    "to escalation.py, not the debate pipeline.",
    "cfg_escalation",
)

# ── 3. cfg_enum ───────────────────────────────────────────────────────────────────────────────

NEW_ESCALATION_TYPE = ["task", "run_error", "issue", "notice", "config"]
NEW_ESCALATION_STATE = ["raised", "re-assign", "on-hold", "closed", "withdraw", "completed"]
NEW_ESCALATION_NEXT_ACTION = ["approve", "reject", "revise", "hold", "noted"]
NEW_ESCALATION_ASSIGNEE = ["Claude", "Researcher"]

# ── 5. governance/escalation cfg_setting rows -- fully worded in the CSV (not the blank stubs) ──

SETTINGS_INSERT = [
    # key, value(JSON string), module
    ("governance.escalation.scope",
     '"all open items, discovery of anomalies, clarifications and other forms of escalation must '
     'be recorded in escalation using escalation rules"', "governance"),
    ("governance.utility.config",
     '"each utility must have its own config table in the cfg_* series to control all aspects of '
     'the utility"', "governance"),
    ("governance.module.config",
     '"each operating module must have a config table (or tables) in the cfg_* series to control '
     'all aspects of the module\'s operation"', "governance"),
    ("governance.scope_project",
     '"the config\'s scope is the entire project, with all of its parts, not a sub-section of the '
     'project"', "governance"),
    ("governance.project_databases",
     '"bible_research.db (aka research_db) lives in database/; iba.db lives in iba/app/db/ -- both '
     'paths are project-root-relative"', "governance"),
    ("governance.tables",
     '"each table in the project must be listed in cfg_table with a proper use text. This applies '
     'to all databases. Tables no longer in use must be set as inactive."', "governance"),
    ("governance.table_columns",
     '"each column in each table in the project must be listed in cfg_column with a proper use '
     'text. This applies to all databases and all tables. Updating a column in any routine must '
     'validate the use of the column against this config. Deviation from the rules must be '
     'escalated."', "governance"),
    ("governance.scope_iba_app",
     '"IBA App is the central process control mechanism for all operations in the entire project"',
     "governance"),
    ("governance.scope_research_db",
     '"The research_db (bible_research.db) is the home for prose and findings with all the related '
     'enabling tables."', "governance"),
    ("governance.scope_iba_db",
     '"The iba_db is the home for all project process control and base data, including all related '
     'tables from STEP through Strongs, verses, meaning, and lexicals. It is now primary for all '
     'processes and base data; a few analysis tables (debate/passage control) are expected to '
     'migrate back to research_db."', "governance"),
    ("governance.project_change_rule",
     '"Any change of operations, methodologies or approach must channel through the IBA App. Any '
     'operation defined in the past that is not in the IBA app must be migrated to the app."',
     "governance"),
    ("governance.project_lookups_and_naming_convensions",
     '"Project-specific naming in lookups, stages, and terms with specific meaning must be defined '
     'in cfg_enum (see cfg_setting naming.*). Terminology must be checked whenever an operation is '
     'executed to ensure it is used in accordance with its definition; a missing definition must be '
     'escalated."', "governance"),
    ("governance.config_control",
     '"every configuration entry in any cfg_* table is controlled by the cfg.configmaint rules"',
     "governance"),
    ("governance.confmaint_configs",
     '"all the rules that govern the maintenance operations of the configs are set in cfg_* under '
     'the configmaint module"', "governance"),
    ("governance.primary_responsibility",
     '"Claude is responsible for the coding of, and maintenance of the integrity to ensure that all '
     'project operations are coded, controlled and maintained in the IBA application. This includes '
     'back-filling operations currently outside the application."', "governance"),
    ("governance.project_operations",
     '"A project operation is any activity to perform research, development, exploration, '
     'investigation, or running scripts related to achieving the project objectives."', "governance"),
    ("governance.User_Guide_scope",
     '"The user guide must reflect the latest state of all the tools and details on the use of the '
     'tools, geared towards user interaction for the entire project."', "governance"),
    ("governance.scripts_and_routines",
     '"All scripts and routines must belong to a module, utility, library, or be a temporary '
     'script. Temporary scripts must be prefixed with temp_."', "governance"),
    ("governance.redundancy_archiving",
     '"One-off reports, scripts, or other artifacts no longer in use or relevant must be archived '
     'on a daily basis."', "governance"),
    ("governance.programme_stages",
     '"The research programme has three main stages: Base_data (STEP through lexical); Analysis '
     '(deriving understanding of the inner being); Publishing (essays and output for the results). '
     'Previously referred to as Session A (base data), Session B/D (analytics), Session C '
     '(publishing) -- methodologies and processes have changed materially over time across all '
     'three."', "governance"),
    ("escalation.control_objectives",
     '"the escalation table manages all open items, irrespective of source or reason -- AI or '
     'researcher raise the escalation when discovered or raised, using the escalation module"',
     "escalation"),
    ("escalation.control_process",
     '"escalations are raised, processed, and completed using the escalation utility module"',
     "escalation"),
]

# updates to EXISTING live rows (already-live settings the CSV revises with additional wording)
SETTINGS_UPDATE = [
    ("governance.governance_md_on_rule_change",
     '"any governance/process rule change must be set in cfg_* first (via configmaint.propose), '
     'then GOVERNANCE.md updated to reflect it in the same unit of work -- GOVERNANCE.md documents '
     'the config, it never holds a rule the config does not, and the config should hold a record of '
     'every change or new rule set via the chat."'),
    ("governance.rules_must_be_config_driven",
     '"no operational or process rule may exist only in GOVERNANCE.md, BUILD.md, USER-GUIDE.md, or '
     'memory without a referenced cfg_* row recording it as the evidence that the configuration '
     'control is in operation. Any deviation discovered requires escalation. On a new instruction, '
     'the first thing to establish is that the rules governing the instruction are fully captured '
     'and interpreted correctly in the configs -- if not, it requires escalation."'),
]

# ── 6. missing cfg_utility rows (escalation #643) ────────────────────────────────────────────

MISSING_UTILITIES = [
    ("clusterassign", "iba/app/lib/clusterassign.py", "cluster.assign -- allocates strongs to M-code clusters"),
    ("clusterreport", "iba/app/lib/clusterreport.py", "report.cluster -- cluster content/quality report"),
    ("strongreconcile", "iba/app/lib/strongreconcile.py", "strong reconciliation utility"),
]


def _retrofit_escalation(conn: sqlite3.Connection, cfg: Cfg) -> str:
    tmp = "escalation__retrofit"
    conn.execute(f'DROP TABLE IF EXISTS "{tmp}"')
    create_sql, _idx = table_ddl(cfg, "escalation", name=tmp)
    conn.execute(create_sql)

    # explicit mapping -- NOT a shared-name copy, because this migration renames columns.
    conn.execute(f"""
        INSERT INTO "{tmp}" (
            id, run_id, source, at_step, type, short_description, context, tried, state,
            next_action, answered_at, raised_at, comment, resolution, related_activity,
            next_action_assigned_to, answered_by
        )
        SELECT
            id, run_id,
            CASE
                WHEN word IS NOT NULL AND word<>'' THEN 'new-word: ' || word
                WHEN run_id LIKE 'MANUAL-%' THEN 'claude'
                WHEN instr(at_step, '.') > 0 THEN substr(at_step, 1, instr(at_step, '.') - 1)
                ELSE 'code'
            END,
            at_step,
            CASE
                WHEN type IN ('crash', 'report-stop') THEN 'run_error'
                WHEN type = 'interactive' THEN 'task'
                WHEN type = 'prompted' AND at_step LIKE 'configmaint.propose%' THEN 'config'
                WHEN type = 'prompted' AND at_step LIKE '%.validate' THEN 'issue'
                WHEN type = 'prompted' AND word IS NOT NULL AND word<>'' THEN 'task'
                WHEN type = 'prompted' AND at_step IN ('candidate.curate', 'candidate.load') THEN 'issue'
                ELSE 'issue'
            END,
            question, preset, tried,
            CASE state
                WHEN 'raised' THEN 'raised'
                WHEN 'answered' THEN 'completed'
                WHEN 'retracted' THEN 'withdraw'
                WHEN 'paused' THEN 'on-hold'
                ELSE state
            END,
            CASE answer WHEN 'yes' THEN 'approve' WHEN 'no' THEN 'reject' ELSE answer END,
            answered_at, raised_at, comment,
            NULL,
            at_step,
            'Researcher',
            CASE WHEN state IN ('answered', 'retracted') THEN 'Researcher' ELSE NULL END
        FROM "escalation"
    """)

    before = conn.execute('SELECT COUNT(*) FROM "escalation"').fetchone()[0]
    after = conn.execute(f'SELECT COUNT(*) FROM "{tmp}"').fetchone()[0]
    if before != after:
        raise RuntimeError(f"escalation: row count mismatch after copy ({before} -> {after})")

    fk_problems = conn.execute(f'PRAGMA foreign_key_check("{tmp}")').fetchall()
    orphan_notes = []
    if fk_problems:
        # PRAGMA foreign_keys enforcement is OFF app-wide at runtime (lib/db.py Db docstring), so
        # this FK was never actually checked before -- these are PRE-EXISTING orphaned run_ids the
        # retrofit surfaces for the first time, not something this migration created. Two classes:
        rowids = [p[1] for p in fk_problems]
        placeholders = ",".join("?" * len(rowids))
        rows = conn.execute(
            f'SELECT id, run_id, state FROM "{tmp}" WHERE id IN ({placeholders})', rowids
        ).fetchall()
        manual = [r for r in rows if r["run_id"].startswith("MANUAL-")]
        genuine = [r for r in rows if not r["run_id"].startswith("MANUAL-")]
        if manual:
            print(f"  escalation: {len(manual)} FK violation(s) on synthetic MANUAL- run_ids -- "
                  f"documented by design (escalation.raise_manual's own docstring: no `run` row is "
                  f"ever created for these). Accepted, not gated.")
        if genuine:
            ids = ", ".join(f"#{r['id']} ({r['run_id']}, state={r['state']})" for r in genuine)
            note = (f"escalation: {len(genuine)} GENUINE orphaned run_id(s), not MANUAL- and not "
                    f"previously documented as by-design: {ids}. Pre-existing data condition, "
                    f"surfaced by this migration's FK check (never run before -- PRAGMA "
                    f"foreign_keys is OFF app-wide). Not fixed here (out of this migration's "
                    f"scope); one of these (#579) is the same run_id as the known configmaint."
                    f"propose crash escalation. Raising a new escalation for this once the reset "
                    f"is live.")
            print(f"  {note}")
            orphan_notes.append(note)

    conn.execute('DROP TABLE "escalation"')
    conn.execute(f'ALTER TABLE "{tmp}" RENAME TO "escalation"')
    summary = (f"escalation: {after} rows retrofitted "
               f"({len(fk_problems)} pre-existing run_id orphan(s) surfaced, see above)"
               if fk_problems else f"escalation: {after} rows retrofitted, FK-check clean")
    return summary, orphan_notes


def _update_escalation_cfg_column(conn: sqlite3.Connection) -> None:
    for old_name, (new_name, notnull, use) in _RENAMES.items():
        conn.execute(
            'UPDATE cfg_column SET name=?, "notnull"=?, "use"=? WHERE table_name=? AND name=?',
            (new_name, notnull, use, "escalation", old_name))
    for name, ordinal, ctype, notnull, use, expectation, filled_by in _NEW_COLUMNS:
        exists = conn.execute(
            "SELECT 1 FROM cfg_column WHERE table_name=? AND name=?", ("escalation", name)
        ).fetchone()
        if not exists:
            conn.execute(
                'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", '
                'is_unique, dflt, fk, "use", expectation, source, filled_by) '
                "VALUES (?,?,?,?,0,?,0,NULL,NULL,?,?,NULL,?)",
                ("escalation", name, ordinal, ctype, notnull, use, expectation, filled_by))
    use, expectation = _TYPE_UPDATE
    conn.execute('UPDATE cfg_column SET "use"=?, expectation=? WHERE table_name=? AND name=?',
                (use, expectation, "escalation", "type"))
    use, expectation = _STATE_UPDATE
    conn.execute('UPDATE cfg_column SET "use"=?, expectation=? WHERE table_name=? AND name=?',
                (use, expectation, "escalation", "state"))


def _create_cfg_escalation(conn: sqlite3.Connection) -> bool:
    exists = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='cfg_escalation'").fetchone()
    if exists:
        return False
    conn.execute(CFG_ESCALATION_DDL)
    conn.execute("INSERT INTO cfg_table (name, grain, \"use\") VALUES (?,?,?)",
                (CFG_ESCALATION_TABLE_ROW[0], CFG_ESCALATION_TABLE_ROW[2], CFG_ESCALATION_TABLE_ROW[1]))
    conn.executemany(
        'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", is_unique, '
        "dflt, fk, \"use\", expectation, source, filled_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        CFG_ESCALATION_COLUMNS)
    conn.executemany(
        "INSERT INTO cfg_escalation (rule_key, rule_text, enforced_by) VALUES (?,?,?)",
        CFG_ESCALATION_RULES)
    return True


def _upsert_enum(conn: sqlite3.Connection, name: str, value: str, ordinal: int) -> None:
    """INSERT OR IGNORE silently no-ops when (name, value) already exists (the PK) -- wrong here
    whenever a value is SHARED between an old and new set (e.g. escalation_state's 'raised' is
    valid in both): a prior blanket `inactive=1` sweep would leave that row stuck inactive since
    the insert never fires to reactivate it. Found live 2026-08-16 (escalation.raise_manual failed
    immediately post-migration: 'raised' not a member of escalation_state). Upsert instead."""
    conn.execute(
        "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0) "
        "ON CONFLICT(name, value) DO UPDATE SET ordinal=excluded.ordinal, inactive=0",
        (name, value, ordinal))


def _update_enums(conn: sqlite3.Connection) -> None:
    conn.execute("UPDATE cfg_enum SET inactive=1 WHERE name='escalation_type'")
    for ordinal, value in enumerate(NEW_ESCALATION_TYPE):
        _upsert_enum(conn, "escalation_type", value, ordinal)
    conn.execute("UPDATE cfg_enum SET inactive=1 WHERE name='escalation_state'")
    for ordinal, value in enumerate(NEW_ESCALATION_STATE):
        _upsert_enum(conn, "escalation_state", value, ordinal)
    conn.execute("UPDATE cfg_enum SET inactive=1 WHERE name='escalation_answer'")
    for ordinal, value in enumerate(NEW_ESCALATION_NEXT_ACTION):
        _upsert_enum(conn, "escalation_next_action", value, ordinal)
    for ordinal, value in enumerate(NEW_ESCALATION_ASSIGNEE):
        conn.execute("INSERT OR IGNORE INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                    ("escalation_assignee", value, ordinal))


def _write_settings(conn: sqlite3.Connection) -> tuple[int, int]:
    inserted = 0
    for key, value, module in SETTINGS_INSERT:
        exists = conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone()
        if exists:
            continue
        conn.execute("INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,NULL,?,0)",
                    (key, value, module))
        inserted += 1
    updated = 0
    for key, value in SETTINGS_UPDATE:
        cur = conn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (value, key))
        updated += cur.rowcount
    return inserted, updated


def _add_missing_utilities(conn: sqlite3.Connection) -> int:
    n = 0
    for module, path, purpose in MISSING_UTILITIES:
        exists = conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone()
        if exists:
            continue
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive) VALUES (?,?,?,0)",
            (module, path, purpose))
        n += 1
    return n


def run() -> None:
    cfg = Cfg(DB_PATH)
    conn = cfg.conn
    conn.row_factory = sqlite3.Row

    conn.execute("BEGIN")
    try:
        _update_escalation_cfg_column(conn)
        result, orphan_notes = _retrofit_escalation(conn, cfg)
        created = _create_cfg_escalation(conn)
        _update_enums(conn)
        n_settings, n_updated = _write_settings(conn)
        n_util = _add_missing_utilities(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise

    from ..lib.db import build_data_tables
    build_data_tables(cfg, conn)
    conn.commit()

    print(result)
    print(f"cfg_escalation created: {created} (5 rules seeded)")
    print("cfg_enum updated: escalation_type, escalation_state, escalation_next_action, "
          "escalation_assignee")
    print(f"cfg_setting: {n_settings} new row(s) inserted, {len(SETTINGS_UPDATE)} existing row(s) "
          f"revised")
    print(f"cfg_utility: {n_util} missing row(s) added (escalation #643)")
    cfg.close()


if __name__ == "__main__":
    run()
