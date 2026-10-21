"""rebuild_escalation_rules_config_20260820.py — ONE-OFF, researcher-directed full rebuild.

Full design: iba/docs/escalation-rebuild-design-v1-20260820.md. Builds the config layer the
retired escalation.py never had: two new rule tables (cfg_escalation_transition,
cfg_escalation_requirement), the entity='escalation' cfg_status_flow rows (escalation #755 finding
1, previously blocked behind #756 -- that block no longer applies, #756 was wiped with the rest of
the data per the researcher's reset), two split escalation_next_action enum groups (#755 finding
2), corrected cfg_escalation enforced_by claims (#746 concretised), and the 2 orphan cfg_write_grant
rows cleared (#750, #755 finding 4).

Written as a direct migration (schema + seed data), not routed through configmaint.propose --
matching the established precedent for THIS SAME MODULE's last rebuild (escalation_redesign_v1/v2
also wrote cfg_table/cfg_column/cfg_write_grant directly, under direct researcher direction, for
exactly this reason: bootstrapping a new config shape is not the same operation configmaint.propose
exists to gate (changing an already-established one).

    python -m iba.app.migration.rebuild_escalation_rules_config_20260820
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # ── 0. escalation_history: relax NOT NULL on source/type/short_description/raised_at ──────
    # The retired full-snapshot design had every column always populated, so those 4 were validly
    # NOT NULL. The delta design (escalation-rebuild-design-v1 sec3) leaves them NULL on any
    # version after v1 unless that specific transaction changed them -- the old constraint would
    # reject every such row. Table is empty post-reset (verified before this migration runs), so a
    # straight rebuild is safe -- no data to lose or migrate.
    n = conn.execute("SELECT COUNT(*) FROM escalation_history").fetchone()[0]
    if n != 0:
        raise RuntimeError(f"escalation_history has {n} rows -- expected empty (post-reset). "
                           f"Refusing to rebuild its schema over live data.")
    conn.execute("""
        CREATE TABLE escalation_history_new (
          "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
          "escalation_id" INTEGER NOT NULL,
          "version" INTEGER NOT NULL,
          "run_id" TEXT,
          "source" TEXT,
          "at_step" TEXT,
          "type" TEXT,
          "short_description" TEXT,
          "context" TEXT,
          "comment" TEXT,
          "tried" TEXT,
          "state" TEXT NOT NULL,
          "next_action" TEXT,
          "next_action_assigned_to" TEXT,
          "originator" TEXT,
          "resolution" TEXT,
          "related_activity" TEXT,
          "raised_at" TEXT,
          "answered_at" TEXT NOT NULL,
          UNIQUE (escalation_id, version),
          FOREIGN KEY ("escalation_id") REFERENCES "escalation"("id")
        )
    """)
    conn.execute("DROP TABLE escalation_history")
    conn.execute("ALTER TABLE escalation_history_new RENAME TO escalation_history")
    conn.executemany(
        'UPDATE cfg_column SET "notnull"=0 WHERE database=\'iba\' AND table_name=\'escalation_history\' '
        "AND name=?", [("source",), ("type",), ("short_description",), ("raised_at",)])
    conn.execute(
        "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='escalation_history' "
        "AND name='source'",
        ("delta: NULL after v1 unless source is corrected (it normally never changes after "
         "creation) -- was wrongly NOT NULL under the retired full-snapshot design",))
    conn.execute(
        "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='escalation_history' "
        "AND name='type'",
        ("delta: NULL after v1 unless type is corrected -- was wrongly NOT NULL under the retired "
         "full-snapshot design",))
    conn.execute(
        "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='escalation_history' "
        "AND name='short_description'",
        ("delta: NULL after v1 unless the title is explicitly corrected (rare, exceptional) -- "
         "was wrongly NOT NULL under the retired full-snapshot design",))
    conn.execute(
        "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='escalation_history' "
        "AND name='raised_at'",
        ("delta, structural: only ever set at v1 (the item's true creation time; never changes) -- "
         "was wrongly NOT NULL every version under the retired full-snapshot design",))
    conn.execute(
        "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='escalation_history' "
        "AND name='comment'",
        ("delta: the raw increment THIS version added, NULL if this version didn't touch it -- "
         "was wrongly 'full cumulative text' under the retired full-snapshot design (that design "
         "wiped 2026-08-20, researcher: 'the cumulative is only in escalation')",))
    conn.execute(
        "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='escalation_history' "
        "AND name='context'",
        ("delta: the raw increment THIS version added, NULL if this version didn't touch it -- "
         "same correction as comment, above",))
    print("escalation_history: schema rebuilt (source/type/short_description/raised_at now "
         "nullable), cfg_column descriptions corrected to match the delta design")

    # ── 1. new tables ────────────────────────────────────────────────────────────────────────
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cfg_escalation_transition (
            priority INTEGER NOT NULL,
            shape TEXT NOT NULL,
            next_action TEXT,
            condition_key TEXT NOT NULL,
            resulting_status_key TEXT NOT NULL,
            notes TEXT,
            active INTEGER NOT NULL DEFAULT 1
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cfg_escalation_requirement (
            action TEXT NOT NULL,
            field TEXT NOT NULL,
            condition_key TEXT NOT NULL,
            message TEXT NOT NULL,
            active INTEGER NOT NULL DEFAULT 1
        )
    """)

    # ── 2. cfg_table registration ───────────────────────────────────────────────────────────
    conn.execute("DELETE FROM cfg_table WHERE database='iba' AND name IN "
                 "('cfg_escalation_transition','cfg_escalation_requirement')")
    conn.executemany(
        "INSERT INTO cfg_table (database, name, grain, use, inactive) VALUES (?,?,?,?,0)", [
        ("iba", "cfg_escalation_transition", "one row per (shape, priority) state-derivation rule",
         "The escalation state-derivation rule engine, evaluated in priority order per shape -- "
         "replaces the hardcoded if/elif chain _derive_state()/_terminal_state_for() used to be. "
         "Built 2026-08-20 as part of the post-reset rebuild (escalation-rebuild-design-v1)."),
        ("iba", "cfg_escalation_requirement", "one row per (action, field) validation rule",
         "Which fields are required for which escalation action (comment@raise, resolution@"
         "approved, etc), and under what named condition. Built 2026-08-20, same rebuild."),
    ])

    # ── 3. cfg_column registration ──────────────────────────────────────────────────────────
    conn.execute("DELETE FROM cfg_column WHERE database='iba' AND table_name IN "
                 "('cfg_escalation_transition','cfg_escalation_requirement')")
    conn.executemany(
        'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
        "is_unique, dflt, fk, use, expectation, source, filled_by) VALUES "
        "(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [
        ("iba", "cfg_escalation_transition", "priority", 0, "INTEGER", 0, 1, 0, None, None,
         "evaluation order within its shape, ascending, first match wins", None, None, None),
        ("iba", "cfg_escalation_transition", "shape", 1, "TEXT", 0, 1, 0, None, None,
         "'manual' or 'dispatcher' -- which vocabulary/function this rule belongs to",
         "enum.escalation_shape", None, None),
        ("iba", "cfg_escalation_transition", "next_action", 2, "TEXT", 0, 0, 0, None, None,
         "which next_action this rule matches, or NULL to match any", None, None, None),
        ("iba", "cfg_escalation_transition", "condition_key", 3, "TEXT", 0, 1, 0, None, None,
         "named condition the code evaluates (escalation-rebuild-design-v1 sec2.4) -- a fixed "
         "small vocabulary, not a general expression language", None, None, None),
        ("iba", "cfg_escalation_transition", "resulting_status_key", 4, "TEXT", 0, 1, 0, None, None,
         "substring matched against cfg_status_flow.set_by (entity=escalation) to resolve the "
         "target status", None, None, None),
        ("iba", "cfg_escalation_transition", "notes", 5, "TEXT", 0, 0, 0, None, None,
         "why this rule exists / provenance", None, None, None),
        ("iba", "cfg_escalation_transition", "active", 6, "INTEGER", 0, 1, 0, "1", None,
         "inactive rows are skipped during evaluation", None, None, None),

        ("iba", "cfg_escalation_requirement", "action", 0, "TEXT", 0, 1, 0, None, None,
         "'raise', or a next_action value -- which transaction this requirement applies to",
         None, None, None),
        ("iba", "cfg_escalation_requirement", "field", 1, "TEXT", 0, 1, 0, None, None,
         "the escalation column that must be filled in", None, None, None),
        ("iba", "cfg_escalation_requirement", "condition_key", 2, "TEXT", 0, 1, 0, None, None,
         "'always', or a named condition gating when the requirement applies", None, None, None),
        ("iba", "cfg_escalation_requirement", "message", 3, "TEXT", 0, 1, 0, None, None,
         "shown to the caller when the requirement is violated", None, None, None),
        ("iba", "cfg_escalation_requirement", "active", 4, "INTEGER", 0, 1, 0, "1", None,
         "inactive rows are skipped", None, None, None),
    ])

    # ── 4. compound-PK registration (is_pk=0 + cfg_unique, per fix_compound_pk_registration
    #      precedent -- inline PK DDL only supports one column) ────────────────────────────────
    conn.execute("DELETE FROM cfg_unique WHERE database='iba' AND table_name IN "
                 "('cfg_escalation_transition','cfg_escalation_requirement')")
    conn.executemany("INSERT INTO cfg_unique (database, table_name, col) VALUES (?,?,?)", [
        ("iba", "cfg_escalation_transition", "shape"),
        ("iba", "cfg_escalation_transition", "priority"),
        ("iba", "cfg_escalation_requirement", "action"),
        ("iba", "cfg_escalation_requirement", "field"),
    ])

    # ── 5. write-grant so configmaint.propose can reach these tables going forward ────────────
    conn.execute("DELETE FROM cfg_write_grant WHERE table_name IN "
                 "('cfg_escalation_transition','cfg_escalation_requirement')")
    conn.executemany(
        "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) VALUES (?,?,?,0)", [
        ("configmaint.propose", "cfg_escalation_transition", "iba"),
        ("configmaint.propose", "cfg_escalation_requirement", "iba"),
    ])

    # ── 6. cfg_status_flow rows for entity='escalation' (escalation #755 finding 1 -- previously
    #      blocked behind #756, no longer applicable, that item was wiped with the reset) ───────
    conn.execute("DELETE FROM cfg_status_flow WHERE entity='escalation'")
    conn.executemany(
        "INSERT INTO cfg_status_flow (entity, status, set_by, ordinal, inactive) VALUES "
        "(?,?,?,?,0)", [
        ("escalation", "raised", "initial state at Raise (escalation.raise_/raise_new)", 0),
        ("escalation", "in-progress", "either party directly (Update state=in-progress); OR "
         "system: next_action=revise", 1),
        ("escalation", "on-hold", "either party directly (Update state=on-hold); OR "
         "dispatcher-tied answer_for_run decision=hold", 2),
        ("escalation", "re-assigned", "system: next_action_assigned_to changed, no more specific "
         "rule matched (Update)", 3),
        ("escalation", "closed", "either party directly (Update state=closed); OR system: "
         "next_action=noted (manual) or decision=noted (dispatcher-tied)", 4),
        ("escalation", "withdraw", "party's explicit choice at Update: next_action=reject, "
         "state=withdraw", 5),
        ("escalation", "supersede", "party's explicit choice at Update: next_action=reject, "
         "state=supersede", 6),
        ("escalation", "completed", "system: manual next_action=approved+resolution present; "
         "OR: dispatcher-tied default (answer_for_run, decision not hold/noted)", 7),
    ])

    # ── 7. cfg_escalation_transition seed rows -- the actual rule engine ─────────────────────
    conn.execute("DELETE FROM cfg_escalation_transition")
    conn.executemany(
        "INSERT INTO cfg_escalation_transition (priority, shape, next_action, condition_key, "
        "resulting_status_key, notes, active) VALUES (?,?,?,?,?,?,1)", [
        # manual shape, priority order = plan v3 sec3, now data not code
        (1, "manual", "approved", "has_resolution", "next_action=approved",
         "resolution present (this call or a prior one) -> completed"),
        (2, "manual", "reject", "always", "__explicit__",
         "state comes from the caller's own explicit withdraw|supersede choice, not a lookup"),
        (3, "manual", "revise", "always", "next_action=revise", None),
        (4, "manual", "noted", "always", "next_action=noted", None),
        (5, "manual", None, "assignee_changed", "no more specific rule",
         "matches ready_for_approval, and any bare reassignment"),
        (6, "manual", None, "always", "__unchanged__",
         "no rule matched -- state carries forward (or the caller's explicit -State)"),
        # dispatcher shape
        (1, "dispatcher", "hold", "always", "decision=hold", None),
        (2, "dispatcher", "noted", "always", "decision=noted", None),
        (3, "dispatcher", None, "always", "dispatcher-tied default",
         "approve/reject/revise all just complete the pause"),
    ])

    # ── 8. cfg_escalation_requirement seed rows ───────────────────────────────────────────────
    conn.execute("DELETE FROM cfg_escalation_requirement")
    conn.executemany(
        "INSERT INTO cfg_escalation_requirement (action, field, condition_key, message, active) "
        "VALUES (?,?,?,?,1)", [
        ("raise", "comment", "always",
         "comment is required at Raise -- minimum: what the item is about"),
        ("raise", "short_description", "always",
         "short_description must pass the title-shape check (escalation #759)"),
        ("approved", "resolution", "always",
         "next_action='approved' requires resolution to be filled in (plan v3 sec3)"),
        ("reject", "state", "always",
         "next_action='reject' requires state='withdraw' or 'supersede', chosen explicitly"),
        ("revise", "tried", "claude_revising",
         "tried is required when Claude sets next_action=revise on its own item -- describe what "
         "was attempted and why it didn't resolve it"),
    ])

    # ── 8b. escalation_shape enum (referenced by cfg_column's expectation above) ──────────────
    conn.execute("DELETE FROM cfg_enum WHERE name='escalation_shape'")
    conn.executemany("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)", [
        ("escalation_shape", "manual", 0),
        ("escalation_shape", "dispatcher", 1),
    ])

    # ── 9. escalation_next_action split into two shape-scoped groups (#755 finding 2) ────────
    conn.execute("UPDATE cfg_enum SET inactive=1 WHERE name='escalation_next_action'")
    conn.execute("DELETE FROM cfg_enum WHERE name IN "
                 "('escalation_next_action_dispatcher','escalation_next_action_manual')")
    conn.executemany("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)", [
        ("escalation_next_action_dispatcher", "approve", 0),
        ("escalation_next_action_dispatcher", "reject", 1),
        ("escalation_next_action_dispatcher", "revise", 2),
        ("escalation_next_action_dispatcher", "hold", 3),
        ("escalation_next_action_dispatcher", "noted", 4),
        ("escalation_next_action_manual", "ready_for_approval", 0),
        ("escalation_next_action_manual", "approved", 1),
        ("escalation_next_action_manual", "reject", 2),
        ("escalation_next_action_manual", "revise", 3),
        ("escalation_next_action_manual", "noted", 4),
        ("escalation_next_action_manual", "review", 5),
    ])

    # ── 10. cfg_escalation stale enforced_by claims corrected (#746 concretised) ──────────────
    conn.execute(
        "UPDATE cfg_escalation SET enforced_by=? WHERE rule_key='document_reference_grouping'",
        ("not currently enforced -- escalation.raise_manual (the function this used to name) was "
         "removed in the 2026-08-20 redesign and has no replacement check; found stale during "
         "escalation-config-review-v2-20260820.md, corrected during the 2026-08-20 rebuild",))
    conn.execute(
        "UPDATE cfg_escalation SET enforced_by=? WHERE rule_key='source_classification'",
        ("escalation.raise_ (source parameter) for the dispatcher shape; the raise_manual half of "
         "this claim was stale (function removed in the redesign) -- manual-shape raises "
         "(escalation.raise_new) take source as a direct required parameter, no separate "
         "classification logic exists for that shape",))

    # ── 11. cfg_write_grant orphans cleared (#750, #755 finding 4) ───────────────────────────
    conn.execute("UPDATE cfg_write_grant SET inactive=1 WHERE writer='run' AND table_name='escalation'")
    conn.execute("UPDATE cfg_write_grant SET inactive=1 WHERE writer='escalation' AND table_name='word_registry'")

    conn.commit()
    conn.close()
    print("cfg_escalation_transition: 9 rows (6 manual + 3 dispatcher)")
    print("cfg_escalation_requirement: 5 rows")
    print("cfg_status_flow: 8 rows for entity=escalation")
    print("cfg_enum: escalation_next_action retired (inactive), split into _dispatcher (5) + _manual (6)")
    print("cfg_escalation: 2 stale enforced_by claims corrected")
    print("cfg_write_grant: 2 orphan rows retired")


if __name__ == "__main__":
    main()
