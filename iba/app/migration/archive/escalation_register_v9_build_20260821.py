"""escalation_register_v9_build_20260821.py — ONE-OFF, researcher-directed build of the escalation
design plan v5 + decision register v9 (`iba/docs/escalation-design-plan-v5-20260821.md` +
`iba/docs/escalation-design-decision-register-v9-20260821.md`).

Written as a direct migration (schema + config), not routed through configmaint.propose — same
precedent as this module's prior rebuild (migration/rebuild_escalation_rules_config_20260820.py):
bootstrapping/extending an already-negotiated config shape under direct researcher direction ("proceed
to implement the design plan per the attached and decision register v9") is not the operation
configmaint.propose exists to gate (changing an already-established one via a fresh, ungoverned ask).

Covers (register item -> what this script does):
  D2  — cfg_table.use corrected for escalation/escalation_history (stale text, still described the
        retired full-snapshot design).
  D3  — cfg_utility gains crash_escalation_reviewed/crash_escalation_note columns (the rollout ITSELF
        — one genuine pass over every active module — is a separate script, see
        escalation_crash_review_rollout_20260821.py).
  D4  — full report registration for escalation.list/escalation.history: cfg_work_package,
        cfg_step, cfg_report, cfg_report_section (9 rows), cfg_report_csv_table (the corrected raw
        table dump, not the exception sections).
  D6  — cfg_escalation: standing_items_survive_reset.
  D7  — cfg_utility.escalation.purpose corrected to the full text register v9 gives.
  D14 — escalation.from_id column + cfg_column + cfg_escalation_requirement rows.
  D18 — cfg_escalation: issue_decisions_produce_documentation_tasks.
  D19 — cfg_escalation.chat_routing extended with the verbatim-quote convention.
  D25 — cfg_escalation_requirement: ready_for_approval/resolution (moves the readiness check
        earlier; the code fix itself is in lib/escalation.py).
  D26 — cfg_escalation_requirement: update/state check_kind='not_raised_with_content'; cfg_escalation:
        chat_start_work_moves_to_in_progress.
  D27 — cfg_escalation_transition: ready_for_approval gets its own explicit row; the two generic
        rules after it renumber (5->6, 6->7).

`cfg_escalation_requirement` gains a `check_kind` column here too — previously every row's check was
implicitly "field must be truthy" (now named 'field_required'); the new rules this build adds need
different comparisons (not_raised_with_content/exists/not_self), so the column has to exist first.

**D14 implementation note (a judgement call, not literally 4 rows)**: the register's prose lists
"related_activity paired with from_id / from_id paired with related_activity (both directions
checked)" as if two independent rules. Taken literally, a rule requiring `from_id` whenever
`related_activity` is set would break virtually every existing item — `related_activity` is used
constantly as plain free text with no `from_id` involved at all. The only real-world pairing that
makes sense is one-directional: WHEN `from_id` is set, `related_activity` must be too (naming what
the relationship documents). This script builds that direction plus `exists`/`not_self` (3 rows,
not 4) and documents the reasoning here rather than inventing a 4th rule that would misfire on
ordinary usage. Flagged for the researcher to correct if this reads the intent wrong.

    python -m iba.app.migration.escalation_register_v9_build_20260821
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # ── D14a: from_id column, BOTH escalation (current-state) and escalation_history (it's one of
    #      the immutable columns _create()/_snapshot() write into every history row too) ─────────
    for table, ordinal in (("escalation", 18), ("escalation_history", 18)):
        cols = {r[1] for r in conn.execute(f"PRAGMA table_info({table})")}
        if "from_id" not in cols:
            conn.execute(f"ALTER TABLE {table} ADD COLUMN from_id INTEGER")
            print(f"{table}: from_id column added")
        else:
            print(f"{table}: from_id column already present -- skipped")

        conn.execute("DELETE FROM cfg_column WHERE database='iba' AND table_name=? AND "
                     "name='from_id'", (table,))
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
            "is_unique, dflt, fk, use, expectation, source, filled_by) VALUES "
            "('iba',?,'from_id',?,'INTEGER',0,0,0,NULL,'escalation.id',?,NULL,NULL,"
            "'escalation.raise_new')",
            (table, ordinal,
             ("Set once, at Raise, never changed after (D14, register v9) -- the item this one was "
              "spawned from, e.g. a documentation-task's from_id points back at the issue whose "
              "resolution required it. NULL for an item raised independently. Enforced by "
              "cfg_escalation_requirement: references a real row when set, is not self-referential, "
              "and is paired with related_activity." if table == "escalation" else
              "Structural, like run_id/source/at_step/type/raised_at -- only ever set at v1, never "
              "changes after (D14, register v9)."),))

    # ── D14b: cfg_escalation_requirement gains check_kind ─────────────────────────────────────
    req_cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_escalation_requirement)")}
    if "check_kind" not in req_cols:
        conn.execute("ALTER TABLE cfg_escalation_requirement ADD COLUMN check_kind TEXT NOT NULL "
                     "DEFAULT 'field_required'")
        print("cfg_escalation_requirement: check_kind column added")
    else:
        print("cfg_escalation_requirement: check_kind column already present -- skipped")
    conn.execute("UPDATE cfg_escalation_requirement SET check_kind='field_required' "
                 "WHERE check_kind IS NULL")

    conn.execute("DELETE FROM cfg_column WHERE database='iba' AND "
                 "table_name='cfg_escalation_requirement' AND name='check_kind'")
    conn.execute(
        'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
        "is_unique, dflt, fk, use, expectation, source, filled_by) VALUES "
        "('iba','cfg_escalation_requirement','check_kind',5,'TEXT',0,1,0,'field_required',NULL,?,"
        "'enum.escalation_requirement_check_kind',NULL,NULL)",
        ("which comparison lib/escalation.py._check_requirements runs: 'field_required' (value must "
         "be truthy -- the original, only, implicit behaviour before this column existed), "
         "'not_raised_with_content' (value must NOT be 'raised'), 'exists' (value, if set, must "
         "reference a real escalation id), 'not_self' (value, if set, must not equal the item's own "
         "id). Added 2026-08-21, register v9 D14/D25/D26.",))
    conn.execute("DELETE FROM cfg_enum WHERE name='escalation_requirement_check_kind'")
    conn.executemany("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)", [
        ("escalation_requirement_check_kind", "field_required", 0),
        ("escalation_requirement_check_kind", "not_raised_with_content", 1),
        ("escalation_requirement_check_kind", "exists", 2),
        ("escalation_requirement_check_kind", "not_self", 3),
    ])

    # compound-key documentation widened: (action, field) was the old registered compound unique;
    # check_kind now needs to be part of it too (two rows can share action+field with different
    # check_kind, e.g. raise/from_id/exists and raise/from_id/not_self).
    conn.execute("DELETE FROM cfg_unique WHERE database='iba' AND "
                 "table_name='cfg_escalation_requirement' AND col='check_kind'")
    conn.execute("INSERT INTO cfg_unique (database, table_name, col) VALUES "
                 "('iba','cfg_escalation_requirement','check_kind')")

    # ── D25/D26/D14: new cfg_escalation_requirement rows ──────────────────────────────────────
    new_reqs = [
        ("ready_for_approval", "resolution", "always", "field_required",
         "next_action='ready_for_approval' requires resolution to be filled in -- the readiness "
         "check, re-confirmed at 'approved' (D25)."),
        ("update", "state", "has_content", "not_raised_with_content",
         "an update carrying comment/context/tried cannot leave the item at state='raised' -- move "
         "it off raised first (e.g. -State in-progress) before attaching work (D26)."),
        ("raise", "from_id", "always", "exists",
         "from_id, if set, must reference an existing escalation id (D14)."),
        ("raise", "from_id", "always", "not_self",
         "from_id, if set, must not equal this item's own id (D14, defensive -- moot at Raise since "
         "the new id doesn't exist yet)."),
        ("raise", "related_activity", "from_id_set", "field_required",
         "from_id is set this transaction -- related_activity must be paired with it, naming what "
         "the relationship documents (D14)."),
    ]
    for action, field, condition_key, check_kind, message in new_reqs:
        conn.execute("DELETE FROM cfg_escalation_requirement WHERE action=? AND field=? AND "
                     "check_kind=?", (action, field, check_kind))
        conn.execute(
            "INSERT INTO cfg_escalation_requirement (action, field, condition_key, check_kind, "
            "message, active) VALUES (?,?,?,?,?,1)",
            (action, field, condition_key, check_kind, message))
    print(f"cfg_escalation_requirement: {len(new_reqs)} new row(s) (D14 x3, D25 x1, D26 x1)")

    # ── D27: ready_for_approval transition rule, existing rows renumbered ─────────────────────
    conn.execute("DELETE FROM cfg_escalation_transition WHERE shape='manual'")
    conn.executemany(
        "INSERT INTO cfg_escalation_transition (priority, shape, next_action, condition_key, "
        "resulting_status_key, notes, active) VALUES (?,?,?,?,?,?,1)", [
        (1, "manual", "approved", "has_resolution", "next_action=approved",
         "resolution present (this call or a prior one) -> completed"),
        (2, "manual", "reject", "always", "__explicit__",
         "state comes from the caller's own explicit withdraw|supersede choice, not a lookup"),
        (3, "manual", "revise", "always", "next_action=revise", None),
        (4, "manual", "noted", "always", "next_action=noted", None),
        (5, "manual", "ready_for_approval", "always", "no more specific rule",
         "D27 (register v9): ready_for_approval now resolves explicitly, regardless of whether the "
         "assignee happened to change this call -- was previously relying on priority-5's "
         "assignee_changed condition, which isn't guaranteed true (e.g. re-affirming the same "
         "assignee)."),
        (6, "manual", None, "assignee_changed", "no more specific rule",
         "was priority 5 pre-D27 -- any bare reassignment not otherwise matched"),
        (7, "manual", None, "always", "__unchanged__",
         "was priority 6 pre-D27 -- no rule matched, state carries forward (or the caller's "
         "explicit -State)"),
    ])
    print("cfg_escalation_transition: manual shape rebuilt, 7 rows (D27 -- new priority-5 "
         "ready_for_approval row, old 5/6 renumbered to 6/7)")

    # ── D2: stale cfg_table.use text ──────────────────────────────────────────────────────────
    conn.execute(
        "UPDATE cfg_table SET use=? WHERE database='iba' AND name='escalation'",
        ("One row per item, CURRENT STATE ONLY. NOT redundant with escalation_history -- history "
         "stores true per-version deltas (most fields NULL per row); escalation is the only place "
         "the full current state is materialised. Ids continue from escalations_old's max (735) "
         "once D1's rebuild lands (register v9, escalation-design-decision-register-v9-20260821).",))
    conn.execute(
        "UPDATE cfg_table SET use=? WHERE database='iba' AND name='escalation_history'",
        ("One row per update to an item, ever -- append-only, a TRUE DELTA per version (most fields "
         "NULL per row unless that version's own transaction set them), not a full snapshot. "
         "Envelope fields (state/next_action/next_action_assigned_to/originator/answered_at) always "
         "populated; content fields (comment/context/resolution/tried/short_description/"
         "related_activity) NULL unless touched this version. escalation is the current-state "
         "materialisation of the latest row here, not the reverse.",))
    print("cfg_table: escalation/escalation_history .use corrected (D2)")

    # ── D7: cfg_utility.escalation.purpose ─────────────────────────────────────────────────────
    conn.execute(
        "UPDATE cfg_utility SET purpose=? WHERE module='escalation'",
        ("escalation.py -- util.escalation. The authoritative record of open items in the project: "
         "errors, issues, and building tasks. All runtime errors are reported in it; both Claude and "
         "Researcher record emerging issues, tasks, followups as feedback or to get feedback. It "
         "pauses a running process and allows it to resume at resume_point when answered "
         "(dispatcher-tied), or tracks a backlog item through raise/update (manual). Five types "
         "(task/issue/notice/run_error/config), each a distinct shape of life -- see "
         "USER-GUIDE.md sec4.",))
    print("cfg_utility: escalation.purpose corrected (D7)")

    # ── D6/D18/D19: cfg_escalation rule rows ──────────────────────────────────────────────────
    conn.execute("DELETE FROM cfg_escalation WHERE rule_key='standing_items_survive_reset'")
    conn.execute(
        "INSERT INTO cfg_escalation (rule_key, rule_text, enforced_by, active) VALUES (?,?,?,1)",
        ("standing_items_survive_reset",
         "Any item explicitly marked to stay open until signed off must be re-raised, carrying its "
         "unresolved scope forward, in the SAME unit of work as any full export+wipe of the "
         "escalation table. Before a wipe proceeds, open standing items are checked for and flagged "
         "if found.",
         "session practice -- not mechanically enforced (register v9 D6)."))

    conn.execute("DELETE FROM cfg_escalation WHERE rule_key='issue_decisions_produce_documentation_tasks'")
    conn.execute(
        "INSERT INTO cfg_escalation (rule_key, rule_text, enforced_by, active) VALUES (?,?,?,1)",
        ("issue_decisions_produce_documentation_tasks",
         "When an issue is set to next_action=approved (the terminal value an issue reaches via the "
         "reused manual vocabulary, per D11/D21 -- this rule originally referenced the now-withdrawn "
         "next_action=decided) and its resolution states a new or changed project/governance rule, "
         "or when a task changes user-facing app behaviour, the party closing it out raises a "
         "companion task (from_id pointing back, related_activity naming the document it updates) "
         "to update the owning document -- GOVERNANCE.md for a rule change, USER-GUIDE.md for "
         "user-facing behaviour -- in the same turn, not left to be remembered separately. A code "
         "change's BUILD.md entry remains governed independently "
         "(governance.build_md_on_code_change); this rule covers the documentation obligations that "
         "rule does not.",
         "session practice -- not mechanically enforced (register v9 D18)."))

    conn.execute("DELETE FROM cfg_escalation WHERE rule_key='chat_start_work_moves_to_in_progress'")
    conn.execute(
        "INSERT INTO cfg_escalation (rule_key, rule_text, enforced_by, active) VALUES (?,?,?,1)",
        ("chat_start_work_moves_to_in_progress",
         "The researcher saying 'start work' (or equivalent) on an open item means the next Update "
         "on that item carries -State in-progress, before content (comment/context/tried) is "
         "generated. Session-practice half of D26 -- honestly distinguished from the mechanically-"
         "enforced guard (cfg_escalation_requirement, action=update, check_kind="
         "not_raised_with_content) which refuses the write outright if this is skipped.",
         "cfg_escalation_requirement (action='update', check_kind='not_raised_with_content') "
         "mechanically refuses the write; the 'start work' -> in-progress convention itself is "
         "session practice (register v9 D26)."))
    print("cfg_escalation: 3 new rule row(s) (D6, D18, D26)")

    row = conn.execute("SELECT rule_text FROM cfg_escalation WHERE rule_key='chat_routing'").fetchone()
    extension = (
        "\n\nExtended 2026-08-21: content captured under this rule is recorded with the operative "
        "instruction or correction quoted VERBATIM -- the researcher's or Claude's own exact words "
        "for the substantive instruction/finding, not a paraphrase. Claude's own connective framing "
        "may surround it, clearly distinguishable from the quoted part.")
    if row and "Extended 2026-08-21" not in row["rule_text"]:
        conn.execute("UPDATE cfg_escalation SET rule_text=? WHERE rule_key='chat_routing'",
                     (row["rule_text"] + extension,))
        print("cfg_escalation: chat_routing extended with verbatim-quote convention (D19)")
    else:
        print("cfg_escalation: chat_routing already carries the D19 extension -- skipped")

    # ── D3: cfg_utility crash-escalation control columns (rollout is a separate script) ──────
    util_cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_utility)")}
    if "crash_escalation_reviewed" not in util_cols:
        conn.execute("ALTER TABLE cfg_utility ADD COLUMN crash_escalation_reviewed INTEGER NOT NULL "
                     "DEFAULT 0")
    if "crash_escalation_note" not in util_cols:
        conn.execute("ALTER TABLE cfg_utility ADD COLUMN crash_escalation_note TEXT")
    conn.execute("DELETE FROM cfg_column WHERE database='iba' AND table_name='cfg_utility' AND "
                "name IN ('crash_escalation_reviewed','crash_escalation_note')")
    conn.executemany(
        'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
        "is_unique, dflt, fk, use, expectation, source, filled_by) VALUES "
        "(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [
        ("iba", "cfg_utility", "crash_escalation_reviewed", 6, "INTEGER", 0, 1, 0, "0", None,
         "1 once this module's crash-recovery behaviour (does a mid-write failure roll back "
         "cleanly, does it record itself) has been genuinely reviewed, not bulk-defaulted (D3, "
         "register v9). 0 = not yet reviewed.", None, None, None),
        ("iba", "cfg_utility", "crash_escalation_note", 7, "TEXT", 0, 0, 0, None, None,
         "The genuine finding from that review -- what actually happens if this module's write "
         "crashes mid-transaction. NULL until crash_escalation_reviewed=1.", None, None, None),
    ])
    print("cfg_utility: crash_escalation_reviewed/crash_escalation_note columns added (D3 -- "
         "rollout itself is escalation_crash_review_rollout_20260821.py)")

    # ── D4: report registration ────────────────────────────────────────────────────────────────
    conn.execute("DELETE FROM cfg_work_package WHERE name='escalation-reporting'")
    conn.execute(
        "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, complete_message, "
        "next_step_hint, paused_message, inactive) VALUES "
        "('escalation-reporting','iba/app/ps/Escalation.ps1','none',0,NULL,NULL,NULL,0)")

    conn.execute("DELETE FROM cfg_step WHERE work_package='escalation-reporting'")
    conn.executemany(
        "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, inactive, kind) "
        "VALUES (?,?,?,?,?,?,0,'utility')", [
        ("escalation-reporting", 0, "escalation.list",
         "iba.app.handlers.reports:escalation_list", "none",
         "every open escalation, with full history inline, grouped by related_activity, plus the "
         "D15 exception sections (cycle/dangling/mismatched_pairing/missing_link/incoherent_link) "
         "-- see lib/escalation.py:write_list_report"),
        ("escalation-reporting", 1, "escalation.history",
         "iba.app.handlers.reports:escalation_history", "none",
         "deep history for ONE item (-Id), plus its downward chain (from_id children) and every "
         "related_activity-named item -- see lib/escalation.py:write_history_report"),
    ])

    conn.execute("DELETE FROM cfg_report WHERE step IN ('escalation.list','escalation.history')")
    conn.executemany(
        "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, naming_scheme, "
        "archive_dir, inactive) VALUES (?,?,?,?,?,?,?,0)", [
        ("escalation.list", "Open escalations", 1, None, "md+csv", "stable", "archive"),
        ("escalation.history", "Escalation deep history", 1, None, "md", "stable", "archive"),
    ])

    conn.execute("DELETE FROM cfg_report_section WHERE step IN "
                 "('escalation.list','escalation.history')")
    conn.executemany(
        "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, toc_label, include, "
        "inactive) VALUES (?,?,?,?,?,1,0)", [
        ("escalation.list", 0, "open_items", "# Open escalations", "Open items"),
        ("escalation.list", 1, "cycle", "## Cycle", "Cycle"),
        ("escalation.list", 2, "dangling", "## Dangling", "Dangling"),
        ("escalation.list", 3, "mismatched_pairing", "## Mismatched pairing", "Mismatched pairing"),
        ("escalation.list", 4, "missing_link", "## Missing link", "Missing link"),
        ("escalation.list", 5, "incoherent_link", "## Incoherent link", "Incoherent link"),
        ("escalation.list", 6, "recently_resolved", "## Recently resolved (last 15)",
         "Recently resolved"),
        ("escalation.history", 0, "item_history", "## #<id> — <short_description>", "Item history"),
        ("escalation.history", 1, "downward_chain", "**downward chain (spawned from #<id>)**",
         "Downward chain"),
    ])

    conn.execute("DELETE FROM cfg_report_csv_table WHERE step='escalation.list'")
    conn.execute(
        "INSERT INTO cfg_report_csv_table (step, table_name, join_note, inactive, virtual) VALUES "
        "('escalation.list','escalation',?,0,0)",
        ("raw, unprocessed dump of the escalation table itself -- NOT the exception-category "
         "findings (those are markdown-only report sections, D4 correction from v4's original, "
         "wrong claim that the CSV was the flagged-exception rows).",))
    print("cfg_work_package/cfg_step/cfg_report/cfg_report_section/cfg_report_csv_table: "
         "escalation-reporting registered, 15 rows total (D4, D23, D16)")

    conn.commit()
    conn.close()
    print("\nescalation_register_v9_build_20260821: done.")


if __name__ == "__main__":
    main()
