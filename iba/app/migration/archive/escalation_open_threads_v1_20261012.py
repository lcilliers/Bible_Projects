"""escalation_open_threads_v1_20261012.py -- escalation #2000, build steps 1 and 2: the config
(rules T0 to T9) and the schema that let the escalation table carry the open threads register.

Design: `_analytics/cross-cluster-web/open-threads-table-proposal-v3-20261012.md` (approved,
rounds 1 to 6; researcher, verbatim: "approve the preview, proceed with the build"). Build handoff:
`_analytics/cross-cluster-web/escalation-2000-build-handoff-v1-20261012.md`.

Step 1, config (proposal sec4):
  T0  cfg_enum escalation_type += thread; new enums escalation_thread_item_kind,
      escalation_thread_item_status, escalation_thread_item_response_kind
  T1  cfg_escalation thread_check_before_work (Escalation.ps1 -Action Match)
  T2  cfg_escalation raise_state_choice + cfg_enum escalation_raise_state (manual Raise only)
  T3  cfg_escalation_transition: a thread whose items change while in-progress work references it
      -> in-progress
  T4  cfg_escalation_requirement: a thread is raised self_correctable
  T5  cfg_escalation 4 (resolution_precedence) amended: in-progress threads only
  T6  cfg_escalation thread_completion; cfg_escalation_transition (items partly closed -> on-hold);
      cfg_escalation_requirement no_open_thread_items (new check kind) on update and
      resolve_self_correctable
  T7  cfg_escalation_requirement: a thread needs at least one item
  T8  cfg_behaviour_rule open-threads-carried-as-escalations
  T9  title check unchanged (#759) -- nothing to write
  plus cfg_status_flow set_by keys for T3/T6, cfg_step/cfg_report/cfg_setting for the two new
  report steps (escalation.thread, escalation.thread_export), cfg_write_grant, and
  cfg_table/cfg_column for every new table and column (cfg_behaviour_rule 62).

Step 2, schema (proposal sec3): escalation and escalation_history gain alias (unique where set)
and comes_back_when; new tables escalation_thread_item and escalation_thread_item_response.

Idempotent: every insert is guarded, every ALTER checks the column first. One transaction.

Usage:
    python iba/app/migration/escalation_open_threads_v1_20261012.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
SRC = "escalation #2000, proposal v3 (open-threads-table-proposal-v3-20261012.md)"
FILLED = "iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update"

ENUMS = [
    ("escalation_type", "thread", 6),
    *[("escalation_thread_item_kind", v, i) for i, v in enumerate(
        ["cluster", "strong", "verse", "strand", "chapter", "event", "researcher", "escalation"])],
    ("escalation_thread_item_status", "open", 0),
    ("escalation_thread_item_status", "closed", 1),
    *[("escalation_thread_item_response_kind", v, i) for i, v in enumerate(
        ["touched", "narrowed", "forward", "ruling", "note", "closed", "reopened"])],
    ("escalation_raise_state", "raised", 0),
    ("escalation_raise_state", "on-hold", 1),
    ("escalation_raise_state", "in-progress", 2),
    ("escalation_requirement_check_kind", "no_open_thread_items", 9),
    ("escalation_requirement_check_kind", "must_be_self_correctable", 10),
]

RULE4_TEXT = (
    "Escalation resolution takes precedence over any other activity; open items with "
    "next_action_assigned_to='Claude' must be addressed before other work. For type='thread' "
    "(escalation #2000, rule T5): only threads at state 'in-progress' count -- a thread is "
    "in-progress only while an in-progress task or issue references it (an open 'escalation' "
    "item). An on-hold thread is never 'work first'.")
RULE4_ENFORCED = ("session practice (Claude Code) -- not mechanically enforced. The thread half "
                  "is fed by Escalation.ps1 -Action ThreadCheck at session start "
                  "(.claude/commands/start-project.md step 4B).")

CFG_ESCALATION = [
    ("thread_check_before_work",
     "T1 (escalation #2000; researcher, round 1: 'open threads must be read before commencing with "
     "a task or issue, to determine if any threads relate to the task or issue escalation'). When "
     "a task or issue is raised, and before it is started (moved to in-progress), its clusters, "
     "Strong's numbers and verses are matched against the items of every thread not completed. "
     "Each match adds an 'escalation' item #nnnn to the thread. This is rule 4 redirected.",
     "Escalation.ps1 -Action Match -For nnnn [-Cluster ..] [-Strong ..] [-Verse ..] "
     "(lib/escalation.py match_threads); running the match is session practice."),
    ("raise_state_choice",
     "T2 (escalation #2000; researcher, round 1: 'default to raised, but allow for asigning the "
     "status on create to on-hold or in progress'). A manual Raise defaults to 'raised' and may "
     "choose a state from cfg_enum escalation_raise_state. A thread is raised at on-hold unless "
     "a state is given, and never at 'raised'. Code-raised items (escalation.raise_) always land "
     "at 'raised', so module_blocking (rule 3) still fires on them.",
     "lib/escalation.py raise_new (state parameter checked against cfg_enum "
     "escalation_raise_state); raise_ takes no state parameter."),
    ("thread_completion",
     "T6 (escalation #2000; researcher, round 1: 'completion of a thread is achieved by moving the "
     "thread to approved. Partial completion of a thread will move the thread back to on-hold. al "
     "individual completions are recorded in the additional table'; round 2: a task or issue may "
     "close without resolving its threads). A thread reaches completed or closed only when every "
     "item is closed. Each completion is a 'closed' response row. When a task or issue reaches a "
     "terminal state, its 'escalation' item on each thread closes, and a thread with no in-progress "
     "work left referencing it returns to on-hold.",
     "cfg_escalation_requirement check_kind no_open_thread_items (update, "
     "resolve_self_correctable); cfg_escalation_transition (shape manual, priority 0); "
     "lib/escalation.py _sync_threads_for."),
]

TRANSITIONS = [
    (0, "manual", None, "thread_items_changed_and_referenced", "thread, T3/T5",
     "escalation #2000 T3/T5: a thread whose items change this call (an item added, closed or "
     "reopened, or the state of the task/issue an 'escalation' item references changed) while an "
     "in-progress task or issue references it moves to in-progress. A reference from a raised or "
     "on-hold task waits until that task is started (round 2: 'in-progress only'). Mutually "
     "exclusive with the other priority-0 row."),
    (0, "manual", None, "thread_items_changed_partly_closed", "thread, T6",
     "escalation #2000 T6: items closed this call, other items still open, and no in-progress work "
     "references the thread -> on-hold (partial completion). Mutually exclusive with the other "
     "priority-0 row."),
]

# cfg_behaviour_rule 43: the existing named exception (2) covered Raise/Update/AnswerRun only, yet
# Correction/ResolveSelfCorrectable/EscalateToDecision were already direct calls. #2000 adds two
# more write actions (Match, ThreadCheck) and two report actions (Thread, Export -> run.py).
RULE43_OLD = ("(2) `Escalation.ps1`'s `-Action Raise/Update/AnswerRun` -- a deliberate manual front "
              "door onto the escalation system's own backlog workflow, not a pipeline run (its "
              "`-Action List/History` DO dispatch through run.py, work package "
              "`escalation-reporting`, fixed this session per D4/D16/D23).")
RULE43_NEW = ("(2) `Escalation.ps1`'s write actions (`-Action Raise/Update/AnswerRun/Correction/"
              "ResolveSelfCorrectable/EscalateToDecision/Match/ThreadCheck`) -- a deliberate manual "
              "front door onto the escalation system's own backlog workflow, not a pipeline run "
              "(its report actions `-Action List/History/Thread/Export` DO dispatch through run.py, "
              "work package `escalation-reporting`, per D4/D16/D23 and escalation #2000; "
              "Correction/ResolveSelfCorrectable/EscalateToDecision were already direct calls and "
              "were named here 2026-10-12 under #2000, Match/ThreadCheck added by #2000).")

STATUS_FLOW_APPEND = {
    "in-progress": "; OR system (thread, T3/T5): an open escalation item references in-progress "
                   "work (escalation #2000)",
    "on-hold": "; OR system (thread, T6): items partly closed and no in-progress work references "
               "the thread (escalation #2000)",
}

REQUIREMENTS = [
    ("raise", "items", "thread_type",
     "a thread needs at least one item at Raise (-Item kind:value[:note]) -- rule T7, escalation "
     "#2000", "field_required"),
    ("raise", "resolution_kind", "thread_type",
     "a thread is raised self_correctable (-ResolutionKind SelfCorrectable) -- rule T4, escalation "
     "#2000 (researcher: 'I am ok if threads are assigned as self-correctable')",
     "must_be_self_correctable"),
    ("update", "state", "thread_type",
     "a thread reaches completed or closed only when every item is closed -- rule T6, escalation "
     "#2000. Close the open items (-Item ... -ResponseKind closed) first.",
     "no_open_thread_items"),
    ("resolve_self_correctable", "state", "thread_type",
     "a thread reaches completed only when every item is closed -- rule T6, escalation #2000.",
     "no_open_thread_items"),
]

BEHAVIOUR_RULE = (
    "chat", "open-threads-carried-as-escalations",
    "The open threads register is carried in the escalation table as type='thread' (alias OT-nn), "
    "not edited as a markdown file. A thread is not worked as a task: it moves only when a strand "
    "reaches it (focused capture, #1900). Its items (escalation_thread_item; cluster, Strong's, "
    "verse, strand, chapter, event, researcher, escalation) are what a strand or task is matched "
    "against (Escalation.ps1 -Action Match). Every response to an item -- touched, narrowed, "
    "forward, ruling, note, closed, reopened -- is an escalation_thread_item_response row, recorded "
    "through Escalation.ps1 -Action Update -Id OT-nn -Item ... -ResponseKind ... -Respond ...; a "
    "researcher's response is quoted verbatim. Notes and comments on a thread are Updates, never "
    "edits to the register file (rule T8). New held items and researcher questions are raised as "
    "threads at ledger approval. The file _analytics/cross-cluster-web/open-threads-register.md is "
    "generated (Escalation.ps1 -Action Export -Type thread) and regenerated at session-close.",
    "Researcher, chat 2026-10-12 (#2000), verbatim: \"adopt open register into escalation. propose "
    "the changes in a md.\"; round 1 ruling 8: \"any additional notes, or comments on the thread is "
    "captured through history.\"; round 6: \"approve the preview, proceed with the build\".",
    "Escalation.ps1 (-Type thread, -Action Thread/Match/ThreadCheck/Export); cfg_escalation rows "
    "thread_check_before_work/raise_state_choice/thread_completion; GOVERNANCE.md section for #2000",
    "partially_enforced",
)

STEPS = [
    ("escalation-reporting", 2, "escalation.thread", "iba.app.handlers.reports:escalation_thread",
     "none", "open threads (type=thread): alias, id, title, open items; -State in-progress narrows; "
     "-Id OT-nn shows one thread's items with their responses -- see "
     "lib/escalation.py:write_thread_report", "utility"),
    ("escalation-reporting", 3, "escalation.thread_export",
     "iba.app.handlers.reports:escalation_thread_export", "none",
     "regenerates the open threads register (.md) from the escalation table, OT-nn · #id per row "
     "-- see lib/escalation.py:write_thread_register", "utility"),
]

REPORTS = [
    ("escalation.thread", "Open threads", 1, None, "md", "dated", "archive"),
    ("escalation.thread_export", "Open threads register", 0,
     "Generated from the escalation table (type=thread) by Escalation.ps1 -Action Export -Type "
     "thread. Do not edit by hand: respond through Escalation.ps1 -Action Update.",
     "md", "stable", "archive"),
]

# A wrong -Id/-State on the two id-taking report steps is a usage slip, not a hard error: route it
# to report-continue (no run_error escalation filed), as escalation.py's own CLI already treats a
# ValueError (escalation-operational-friction-review-v1-20260831, Defect 1).
ON_FAIL = [
    ("escalation.thread", "bad-parameter", "report-continue",
     "usage error, not recorded as an escalation -- check -Id (id or OT-nn) and -State "
     "(on-hold|in-progress)", "terminal"),
    ("escalation.history", "bad-parameter", "report-continue",
     "usage error, not recorded as an escalation -- check -Id (id or OT-nn)", "terminal"),
]

SETTINGS = [
    ("escalation.thread_report_path", '"outputs/escalation/escalation-threads.md"',
     "where Escalation.ps1 -Action Thread writes the open threads report (escalation #2000)"),
    ("escalation.thread_register_path", '"_analytics/cross-cluster-web/open-threads-register.md"',
     "the generated open threads register (Escalation.ps1 -Action Export -Type thread; "
     "regenerated at session-close) -- same path as the hand-kept register it replaces "
     "(escalation #2000, decision 3)"),
]

NEW_TABLES = {
    "escalation_thread_item": (
        "One row per item of a thread (type='thread' escalation): what a strand or task is matched "
        "against, and the item's current status only (open/closed). Every response, including each "
        "completion, is a row in escalation_thread_item_response. escalation #2000 (proposal v3 "
        "sec3.2, sec3.4).",
        """CREATE TABLE escalation_thread_item (
            id            INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            escalation_id INTEGER NOT NULL REFERENCES escalation(id),
            item_no       INTEGER NOT NULL,
            kind          TEXT NOT NULL,
            value         TEXT NOT NULL,
            status        TEXT NOT NULL DEFAULT 'open',
            note          TEXT,
            opened_at     TEXT NOT NULL,
            opened_by     INTEGER,
            UNIQUE (escalation_id, item_no)
        )""",
        [
            ("id", "INTEGER", 1, 1, 0, None, None, "surrogate PK"),
            ("escalation_id", "INTEGER", 0, 1, 0, None, "escalation.id", "the thread"),
            ("item_no", "INTEGER", 0, 1, 0, None, None,
             "the item's place in its thread; the reference is {alias}.{item_no}, e.g. OT-16.1. "
             "Never renumbered; a new item takes the next number (proposal sec3.4)"),
            ("kind", "TEXT", 0, 1, 0, None, None,
             "cfg_enum escalation_thread_item_kind: cluster, strong, verse, strand, chapter, event, "
             "researcher, escalation"),
            ("value", "TEXT", 0, 1, 0, None, None,
             "e.g. M72, M10c, H5782, Rom 7:15-21, 10.13, #1993 (kind escalation: the task or issue "
             "that references the thread)"),
            ("status", "TEXT", 0, 1, 0, "'open'", None,
             "cfg_enum escalation_thread_item_status: open or closed -- current state only"),
            ("note", "TEXT", 0, 0, 0, None, None, "what this item asks for, e.g. '7 verses'"),
            ("opened_at", "TEXT", 0, 1, 0, None, None, "when the item was added (ISO-8601 UTC)"),
            ("opened_by", "INTEGER", 0, 0, 0, None, "escalation.id",
             "the task or issue under which the item was added (e.g. a forward under #1998); NULL "
             "when added with the thread itself"),
        ]),
    "escalation_thread_item_response": (
        "One row per response to a thread item: touched, narrowed, forward, ruling, note, closed, "
        "reopened. Nothing is overwritten. escalation #2000 (proposal v3 sec3.3, approved round 5).",
        """CREATE TABLE escalation_thread_item_response (
            id             INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            item_id        INTEGER NOT NULL REFERENCES escalation_thread_item(id),
            escalation_id  INTEGER NOT NULL REFERENCES escalation(id),
            kind           TEXT NOT NULL,
            text           TEXT NOT NULL,
            via_escalation INTEGER,
            responded_by   TEXT NOT NULL,
            responded_at   TEXT NOT NULL,
            files          TEXT
        )""",
        [
            ("id", "INTEGER", 1, 1, 0, None, None, "surrogate PK"),
            ("item_id", "INTEGER", 0, 1, 0, None, "escalation_thread_item.id", "the item answered"),
            ("escalation_id", "INTEGER", 0, 1, 0, None, "escalation.id",
             "the thread (repeated from the item, for easy querying)"),
            ("kind", "TEXT", 0, 1, 0, None, None,
             "cfg_enum escalation_thread_item_response_kind. 'closed' closes the item, 'reopened' "
             "opens it again, 'forward' comes with at least one new item on the same thread"),
            ("text", "TEXT", 0, 1, 0, None, None,
             "the response; a researcher's response is quoted verbatim (cfg_escalation 5)"),
            ("via_escalation", "INTEGER", 0, 0, 0, None, "escalation.id",
             "the task or issue whose work gave the response, e.g. 1998"),
            ("responded_by", "TEXT", 0, 1, 0, None, None, "Claude or Researcher"),
            ("responded_at", "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC"),
            ("files", "TEXT", 0, 0, 0, None, None,
             "JSON list of full repo-relative paths (cfg_escalation 7)"),
        ]),
}

# GOVERNANCE.md §C / §53-area (cfg_unique, cfg_index): a data table's keys and indexes are config
# rows, so lib/db.py:table_ddl() rebuilds the table exactly. Every FK column gets an index named
# idx_{table}_{col} (populate_cfg_index_rows.py convention); neither table has a `deleted` column, so
# no composite (fk, deleted) form. Added 2026-10-12 after the researcher's pre-exit governance check
# found both missing.
CFG_UNIQUE = [("escalation_thread_item", "escalation_id", 0),
              ("escalation_thread_item", "item_no", 1)]
CFG_INDEX = [("escalation_thread_item", "escalation_id"),
             ("escalation_thread_item", "opened_by"),
             ("escalation_thread_item_response", "item_id"),
             ("escalation_thread_item_response", "escalation_id"),
             ("escalation_thread_item_response", "via_escalation")]
LEGACY_INDEX = "idx_escalation_thread_item_response_item"   # first build's hand-named index

NEW_COLUMNS = [
    ("alias", "TEXT",
     "OT-nn for type='thread' (assigned automatically at Raise: the next OT number); NULL for "
     "other types. Unique where set (index idx_escalation_alias). Escalation.ps1 -Id accepts it "
     "anywhere an id is taken. Immutable after Raise. escalation #2000",
     "per-version copy of escalation.alias (set at v1 only -- immutable). escalation #2000"),
    ("comes_back_when", "TEXT",
     "the thread's 'comes back when' text, whole, as a person reads it; the matchable parts are "
     "escalation_thread_item rows. Replace column (Update -ComesBackWhen). escalation #2000",
     "delta: set only on the version that set it. escalation #2000"),
]


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _has_column(cur, table: str, col: str) -> bool:
    return any(r[1] == col for r in cur.execute(f'PRAGMA table_info("{table}")'))


def _has_table(cur, table: str) -> bool:
    return cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
                       (table,)).fetchone() is not None


def _exists(cur, sql: str, params) -> bool:
    return cur.execute(sql, params).fetchone() is not None


def _register_column(cur, table, ordinal, name, ctype, is_pk, notnull, is_unique, dflt, fk, use,
                     report):
    if _exists(cur, "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?",
               (table, name)):
        report.append(f"cfg_column {table}.{name} already present -- skipped")
        return
    cur.execute(
        'INSERT INTO cfg_column (database, table_name, name, ordinal, "type", is_pk, "notnull", '
        'is_unique, dflt, fk, "use", expectation, source, filled_by, inactive) '
        "VALUES ('iba',?,?,?,?,?,?,?,?,?,?,NULL,?,?,0)",
        (table, name, ordinal, ctype, is_pk, notnull, is_unique, dflt, fk, use, SRC, FILLED))
    report.append(f"cfg_column {table}.{name} registered")


def config(cur, report: list[str]) -> None:
    for name, value, ordinal in ENUMS:
        if _exists(cur, "SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)):
            report.append(f"cfg_enum {name}={value} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                        (name, value, ordinal))
            report.append(f"cfg_enum {name}={value} inserted")

    cur.execute("UPDATE cfg_escalation SET rule_text=?, enforced_by=? WHERE id=4 AND "
                "rule_key='resolution_precedence'", (RULE4_TEXT, RULE4_ENFORCED))
    report.append(f"cfg_escalation 4 resolution_precedence amended (T5): {cur.rowcount} row")
    for key, text, enforced in CFG_ESCALATION:
        if _exists(cur, "SELECT 1 FROM cfg_escalation WHERE rule_key=?", (key,)):
            report.append(f"cfg_escalation {key} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_escalation (rule_key, rule_text, enforced_by, active) "
                        "VALUES (?,?,?,1)", (key, text, enforced))
            report.append(f"cfg_escalation {key} inserted (id {cur.lastrowid})")

    for prio, shape, na, cond, key, notes in TRANSITIONS:
        if _exists(cur, "SELECT 1 FROM cfg_escalation_transition WHERE shape=? AND condition_key=?",
                   (shape, cond)):
            cur.execute("UPDATE cfg_escalation_transition SET notes=? WHERE shape=? AND "
                        "condition_key=? AND notes IS NOT ?", (notes, shape, cond, notes))
            report.append(f"cfg_escalation_transition {cond} already present -- notes "
                          f"{'refreshed' if cur.rowcount else 'unchanged'}")
        else:
            cur.execute("INSERT INTO cfg_escalation_transition (priority, shape, next_action, "
                        "condition_key, resulting_status_key, notes, active) VALUES (?,?,?,?,?,?,1)",
                        (prio, shape, na, cond, key, notes))
            report.append(f"cfg_escalation_transition {cond} inserted")
    for status, addition in STATUS_FLOW_APPEND.items():
        row = cur.execute("SELECT set_by FROM cfg_status_flow WHERE entity='escalation' AND status=?",
                          (status,)).fetchone()
        if addition.strip("; ") in row[0]:
            report.append(f"cfg_status_flow {status} already carries the thread key -- skipped")
        else:
            cur.execute("UPDATE cfg_status_flow SET set_by=? WHERE entity='escalation' AND status=?",
                        (row[0] + addition, status))
            report.append(f"cfg_status_flow {status} set_by extended")

    for action, field, cond, msg, kind in REQUIREMENTS:
        if _exists(cur, "SELECT 1 FROM cfg_escalation_requirement WHERE action=? AND field=? AND "
                        "check_kind=? AND condition_key=?", (action, field, kind, cond)):
            report.append(f"cfg_escalation_requirement {action}/{kind} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_escalation_requirement (action, field, condition_key, "
                        "message, active, check_kind) VALUES (?,?,?,?,1,?)",
                        (action, field, cond, msg, kind))
            report.append(f"cfg_escalation_requirement {action}/{kind} inserted")

    cur.execute("UPDATE cfg_behaviour_rule SET rule_text = replace(rule_text, ?, ?) WHERE "
                "rule_key='every-active-ps-script-dispatches-through-run-py' AND instr(rule_text, ?)",
                (RULE43_OLD, RULE43_NEW, RULE43_OLD))
    report.append(f"cfg_behaviour_rule 43 exception (2) widened: {cur.rowcount} row")

    cls, key, text, source, enforced, status = BEHAVIOUR_RULE
    if _exists(cur, "SELECT 1 FROM cfg_behaviour_rule WHERE rule_key=?", (key,)):
        report.append(f"cfg_behaviour_rule {key} already present -- skipped")
    else:
        cur.execute("INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, "
                    "enforced_by, added_at, active, enforcement_status) VALUES (?,?,?,?,?,?,1,?)",
                    (cls, key, text, source, enforced, _now(), status))
        report.append(f"cfg_behaviour_rule {key} inserted (id {cur.lastrowid})")

    for wp, ordinal, step, handler, scope, does, kind in STEPS:
        if _exists(cur, "SELECT 1 FROM cfg_step WHERE work_package=? AND step=?", (wp, step)):
            report.append(f"cfg_step {step} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                        "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                        (wp, ordinal, step, handler, scope, does, kind))
            report.append(f"cfg_step {step} inserted")
    for step, title, toc, footer, kind, naming, archive in REPORTS:
        if _exists(cur, "SELECT 1 FROM cfg_report WHERE step=?", (step,)):
            report.append(f"cfg_report {step} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
                        "naming_scheme, archive_dir, inactive) VALUES (?,?,?,?,?,?,?,0)",
                        (step, title, toc, footer, kind, naming, archive))
            report.append(f"cfg_report {step} inserted")
    for step, cond, path, msg, route in ON_FAIL:
        if _exists(cur, "SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", (step, cond)):
            report.append(f"cfg_on_fail {step}/{cond} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_on_fail (step, condition, path, resolver, message, route, "
                        "inactive) VALUES (?,?,?,NULL,?,?,0)", (step, cond, path, msg, route))
            report.append(f"cfg_on_fail {step}/{cond} inserted")
    for key, value, use in SETTINGS:
        if _exists(cur, "SELECT 1 FROM cfg_setting WHERE key=?", (key,)):
            report.append(f"cfg_setting {key} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_setting (key, value, use, module, inactive) "
                        "VALUES (?,?,?,'escalation',0)", (key, value, use))
            report.append(f"cfg_setting {key} inserted")

    for table in NEW_TABLES:
        if _exists(cur, "SELECT 1 FROM cfg_write_grant WHERE writer='escalation' AND table_name=? "
                        "AND database='iba'", (table,)):
            report.append(f"cfg_write_grant escalation->{table} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                        "VALUES ('escalation',?,'iba',0)", (table,))
            report.append(f"cfg_write_grant escalation->{table} inserted")

    cur.execute("UPDATE cfg_utility SET purpose = purpose || ? WHERE module='escalation' AND "
                "purpose NOT LIKE '%type thread%'",
                (" Type thread (escalation #2000): the open threads register, alias OT-nn, with "
                 "item and response child tables (escalation_thread_item, "
                 "escalation_thread_item_response) -- see USER-GUIDE.md sec4.",))
    report.append(f"cfg_utility escalation purpose extended: {cur.rowcount} row")


def schema(cur, report: list[str]) -> None:
    for table in ("escalation", "escalation_history"):
        base = cur.execute("SELECT COALESCE(MAX(ordinal),0) FROM cfg_column WHERE database='iba' "
                           "AND table_name=?", (table,)).fetchone()[0]
        for n, (col, ctype, use_esc, use_hist) in enumerate(NEW_COLUMNS, start=1):
            if _has_column(cur, table, col):
                report.append(f"{table}.{col} already exists -- skipped")
            else:
                cur.execute(f'ALTER TABLE "{table}" ADD COLUMN "{col}" {ctype}')
                report.append(f"{table}.{col} added")
            _register_column(cur, table, base + n, col, ctype, 0, 0, 1 if (
                table == "escalation" and col == "alias") else 0, None, None,
                use_esc if table == "escalation" else use_hist, report)
    cur.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_escalation_alias ON escalation(alias) '
                'WHERE alias IS NOT NULL')
    report.append("index idx_escalation_alias ensured (unique where set)")

    for table, (use, ddl, cols) in NEW_TABLES.items():
        if _has_table(cur, table):
            report.append(f"table {table} already exists -- skipped")
        else:
            cur.execute(ddl)
            report.append(f"table {table} created")
        if _exists(cur, "SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", (table,)):
            report.append(f"cfg_table {table} already present -- skipped")
        else:
            cur.execute('INSERT INTO cfg_table (database, name, grain, "use", inactive, category) '
                        "VALUES ('iba',?,?,?,0,'data')",
                        (table, "one row per thread item" if table.endswith("item")
                         else "one row per response to a thread item", use))
            report.append(f"cfg_table {table} registered")
        for ordinal, (name, ctype, is_pk, notnull, is_unique, dflt, fk, cuse) in enumerate(cols):
            _register_column(cur, table, ordinal, name, ctype, is_pk, notnull, is_unique, dflt, fk,
                             cuse, report)
    for table, col, ordinal in CFG_UNIQUE:
        if _exists(cur, "SELECT 1 FROM cfg_unique WHERE database='iba' AND table_name=? AND col=?",
                   (table, col)):
            report.append(f"cfg_unique {table}.{col} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_unique (database, table_name, col, ordinal) "
                        "VALUES ('iba',?,?,?)", (table, col, ordinal))
            report.append(f"cfg_unique {table}.{col} inserted")
    cur.execute(f'DROP INDEX IF EXISTS "{LEGACY_INDEX}"')
    for table, col in CFG_INDEX:
        name = f"idx_{table}_{col}"
        if _exists(cur, "SELECT 1 FROM cfg_index WHERE table_name=? AND name=?", (table, name)):
            report.append(f"cfg_index {name} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_index (table_name, name, col, ordinal) VALUES (?,?,?,0)",
                        (table, name, col))
            report.append(f"cfg_index {name} inserted")
        cur.execute(f'CREATE INDEX IF NOT EXISTS "{name}" ON "{table}" ("{col}")')
    report.append(f"live indexes ensured: {len(CFG_INDEX)} (legacy {LEGACY_INDEX} dropped if present)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")
        config(cur, report)
        schema(cur, report)
        if args.dry_run:
            conn.rollback()
            report.append("DRY RUN -- rolled back, nothing written")
        else:
            conn.commit()
            report.append("committed")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
