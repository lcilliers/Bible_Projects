"""escalation_redesign_v2_20260820.py — ONE-OFF: escalation redesign, corrected retry of
`escalation_redesign_v1_20260819.py` (run, broke live dispatch, rolled back same day —
`BUILD.md` §152). v1's gap: it dropped `run_id` and the dispatcher-tied `approve`/`hold`
vocabulary entirely, on the assumption the whole table was being redesigned around the manual
researcher/Claude workflow. The researcher corrected this 2026-08-20 (`BUILD.md` §153): config
writes (`configmaint.propose`/`validate`) are development/design controls that correctly keep a
real, gated approval; a standard operational routine (`registry.create` and friends) needs no
approval mechanism at all, just an engine log. **Two shapes, two vocabularies, one mechanism** —
see `lib/escalation.py`'s own module docstring for the full split. This migration is v1's schema
plus `run_id` restored and the OLD `approve`/`hold` next_action values kept ACTIVE (not retired) —
everything else (rename-to-`escalations_old`, `escalation_history`, the 4-item carryover) unchanged
from v1's already-researcher-approved shape.

**Prerequisite code already live before this ran**: `lib/escalation.py` rewritten (dispatcher-tied
`raise_`/`answer_for_run`/`answered_for_run`/`pending_for_run` ported to the new schema, unchanged
vocabulary/semantics; new `raise_new`/`update` for the manual shape), `run.py`'s 3 direct writes +
`module_blocking` query updated to match. Verified: all 9 handler call sites of
`answered_for_run()` only ever read `["next_action"]`/`["comment"]` — zero handler changes needed.

**What this does, in order (identical structure to v1, `run_id` added throughout):**

1. Renames the live `escalation` table (723 rows as of 2026-08-20 04:07 — includes the one real
   test escalation `#735` from yesterday's verification) to `escalations_old`, frozen,
   `cfg_table.inactive=1`.
2. Builds `escalation` + `escalation_history` from `cfg_column`/`table_ddl()`, both now carrying
   `run_id` (nullable — set for dispatcher-tied items, `MANUAL-...` for manual ones).
3. Seeds `sqlite_sequence` so new ids continue from 735 (`escalations_old`'s real max).
4. `cfg_enum`: `escalation_state` gains `supersede`/`re-assigned` (same as v1). `escalation_
   next_action` GAINS `ready_for_approval`/`approved`/`review` — `approve`/`hold`/`reject`/`revise`/
   `noted` stay ACTIVE, unchanged (the correction from v1: these are still needed, live, by the
   dispatcher-tied shape).
5. Re-raises the same 4 carryover items (`#650`/`#654`/`#668`/`#725`) as MANUAL- shaped fresh rows,
   unchanged from v1.

    python -m iba.app.migration.escalation_redesign_v2_20260820
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import Cfg
from ..lib.db import table_ddl

DB_PATH = "iba/app/db/iba.db"
OLD_MAX_ID = 735  # confirmed live immediately before this script ran (includes yesterday's #735 test)

# ── new `escalation` columns (id/version auto; the rest per plan v3 §3/§8 + run_id restored) ────
ESCALATION_COLUMNS = [
    # name, ordinal, type, is_pk, notnull, is_unique, dflt, fk, use, expectation, filled_by
    ("id", 0, "INTEGER", 1, 1, 0, None, None,
     "serial PK, 4-digit display; continues from escalations_old's max (735) so ids stay "
     "unambiguous across the cutover", None, None),
    ("version", 1, "INTEGER", 0, 1, 0, "1",
     None, "current version number for this id -- count of its escalation_history rows; the "
     "NNNN-NN display format is id+version, not a stored key", None, "escalation.raise_new/update"),
    ("run_id", 2, "TEXT", 0, 0, 0, None, None,
     "restored 2026-08-20 (v1 dropped it, broke dispatch, rolled back -- BUILD.md §152/§153). Set "
     "for a DISPATCHER-TIED item (a real run.py pause, correlates back to the run being resumed) "
     "or a synthetic MANUAL-<timestamp> for a manual item. NULL for neither.", None,
     "escalation.raise_/raise_new"),
    ("source", 3, "TEXT", 0, 1, 0, None, None,
     "what triggered the item: script name | module | issue area. Immutable after Raise.",
     None, "escalation.raise_new"),
    ("at_step", 4, "TEXT", 0, 0, 0, None, None,
     "pipeline reference, only set if code-generated/run-error. Immutable after Raise.",
     None, "escalation.raise_new"),
    ("type", 5, "TEXT", 0, 1, 0, None, None, "differentiates the kind of item",
     "enum.escalation_type", "escalation.raise_new"),
    ("short_description", 6, "TEXT", 0, 1, 0, None, None,
     "label/title -- what this item is about. IMMUTABLE after Raise (plan v3 §3) -- a wrong title "
     "is corrected by raising a new item with state=supersede on the old one (plan v3 §4), never "
     "edited in place.", None, "escalation.raise_new"),
    ("context", 7, "TEXT", 0, 0, 0, None, None,
     "what must be done or the error message, plus links to external documents. Cumulative: an "
     "Update's input is the increment, appended onto the current value (plan v3 §2).",
     None, "escalation.raise_new/update"),
    ("comment", 8, "TEXT", 0, 0, 0, None, None,
     "additional information for the assigned party. Cumulative, same rule as context.",
     None, "escalation.raise_new/update"),
    ("tried", 9, "TEXT", 0, 0, 0, None, None,
     "the corrective action taken -- REQUIRED when next_action_assigned_to=Claude and a prior "
     "corrective action failed (plan v3 §6/v2 §6).", None, "escalation.update"),
    ("state", 10, "TEXT", 0, 1, 0, None, None,
     "current status -- raised at Raise; mostly logic-derived on Update per the auto-state rules "
     "(plan v3 §3), some values either-party-settable (on-hold/in-progress/closed).",
     "enum.escalation_state", "escalation.raise_new/update"),
    ("next_action", 11, "TEXT", 0, 0, 0, None, None,
     "what's expected of the current reader (incoming) / what the next reader should do (outgoing) "
     "-- TWO vocabularies share this column: dispatcher-tied (approve/reject/revise/hold/noted, "
     "unchanged) and manual (ready_for_approval/approved/reject/revise/noted/review) -- see "
     "lib/escalation.py module docstring, 2026-08-20.", "enum.escalation_next_action",
     "escalation.raise_new/update"),
    ("next_action_assigned_to", 12, "TEXT", 0, 0, 0, None, None, "Claude | Researcher",
     "enum.escalation_assignee", "escalation.raise_new/update"),
    ("originator", 13, "TEXT", 0, 0, 0, None, None,
     "who created the latest escalation_history row -- auto-populated, replaces `answered_by`. "
     "Not caller-supplied.", "enum.escalation_assignee", "escalation.raise_new/update"),
    ("resolution", 14, "TEXT", 0, 0, 0, None, None,
     "what was actually done -- REQUIRED when next_action=approved (validity check, plan v3 §3).",
     None, "escalation.update"),
    ("related_activity", 15, "TEXT", 0, 0, 0, None, None,
     "free-text information field linking this item to any other item(s) that relate to it -- "
     "plain text at this stage, not a structural link table (plan v3 §9.2, decided).", None,
     "escalation.raise_new/update"),
    ("raised_at", 16, "TEXT", 0, 1, 0, None, None, "first creation datetime -- set once, immutable",
     None, "escalation.raise_new"),
    ("answered_at", 17, "TEXT", 0, 0, 0, None, None,
     "mirrors the latest escalation_history row's timestamp", None, "escalation.update"),
]

ESCALATION_TABLE_ROW = (
    "escalation",
    "One row per item, CURRENT STATE ONLY -- the escalation redesign (2026-08-19/20, "
    "escalation-redesign-plan-v3 + BUILD.md §153's engine-vs-escalation split). Redundant with the "
    "latest escalation_history row by construction: every write updates both, in one transaction. "
    "New ids continue from escalations_old's max (735) -- see escalation_history for the full "
    "append-only record.",
    "one row per item, current status",
)

# ── `escalation_history` — full snapshot per version, append-only ───────────────────────────────
HISTORY_COLUMNS = [
    ("id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK, row order = write order", None, None),
    ("escalation_id", 1, "INTEGER", 0, 1, 0, None, "escalation.id",
     "which item this snapshot belongs to", None, "escalation.raise_new/update"),
    ("version", 2, "INTEGER", 0, 1, 0, None, None,
     "this item's version number at the time of this snapshot -- matches escalation.version at "
     "the moment this row was the latest", None, "escalation.raise_new/update"),
    ("run_id", 3, "TEXT", 0, 0, 0, None, None, "snapshot of escalation.run_id (constant per item)",
     None, None),
    ("source", 4, "TEXT", 0, 1, 0, None, None, "snapshot of escalation.source at this version",
     None, None),
    ("at_step", 5, "TEXT", 0, 0, 0, None, None, "snapshot of escalation.at_step at this version",
     None, None),
    ("type", 6, "TEXT", 0, 1, 0, None, None, "snapshot of escalation.type at this version",
     None, None),
    ("short_description", 7, "TEXT", 0, 1, 0, None, None,
     "snapshot of escalation.short_description at this version", None, None),
    ("context", 8, "TEXT", 0, 0, 0, None, None,
     "snapshot of escalation.context (full cumulative text) at this version", None, None),
    ("comment", 9, "TEXT", 0, 0, 0, None, None,
     "snapshot of escalation.comment (full cumulative text) at this version", None, None),
    ("tried", 10, "TEXT", 0, 0, 0, None, None, "snapshot of escalation.tried at this version",
     None, None),
    ("state", 11, "TEXT", 0, 1, 0, None, None, "snapshot of escalation.state at this version",
     None, None),
    ("next_action", 12, "TEXT", 0, 0, 0, None, None,
     "snapshot of escalation.next_action at this version", None, None),
    ("next_action_assigned_to", 13, "TEXT", 0, 0, 0, None, None,
     "snapshot of escalation.next_action_assigned_to at this version", None, None),
    ("originator", 14, "TEXT", 0, 0, 0, None, None,
     "who created THIS specific snapshot -- the real per-update author, never overwritten by a "
     "later row (this is the fix for #715's loss)", None, "escalation.raise_new/update"),
    ("resolution", 15, "TEXT", 0, 0, 0, None, None,
     "snapshot of escalation.resolution at this version", None, None),
    ("related_activity", 16, "TEXT", 0, 0, 0, None, None,
     "snapshot of escalation.related_activity at this version", None, None),
    ("raised_at", 17, "TEXT", 0, 1, 0, None, None, "snapshot of escalation.raised_at (constant)",
     None, None),
    ("answered_at", 18, "TEXT", 0, 1, 0, None, None,
     "THIS row's own write timestamp -- the real per-update datetime", None,
     "escalation.raise_new/update"),
]

HISTORY_TABLE_ROW = (
    "escalation_history",
    "Append-only, one FULL SNAPSHOT row per update to an escalation item, every column's value at "
    "that version -- never updated or deleted once written (escalation-redesign-plan-v3 §2). This "
    "is the fix for the single most critical failure the old design had: escalation #715's "
    "updates being silently overwritten with no trace. `escalation` always mirrors the latest row "
    "here by construction.",
    "one row per update to an item, ever",
)

NEW_ESCALATION_STATE_ADDITIONS = ["supersede", "re-assigned"]
# 2026-08-20 correction: approve/hold/reject/revise/noted are NOT retired -- the dispatcher-tied
# shape still uses them unchanged. Only the 3 genuinely new manual-shape values are added.
NEW_ESCALATION_NEXT_ACTION_ADDITIONS = ["review", "ready_for_approval", "approved"]


def _rename_old_table(conn: sqlite3.Connection) -> int:
    count = conn.execute("SELECT COUNT(*) FROM escalation").fetchone()[0]
    conn.execute("ALTER TABLE escalation RENAME TO escalations_old")
    conn.execute(
        "UPDATE cfg_table SET name='escalations_old', inactive=1, "
        "\"use\"='Historical escalation data, frozen at the 2026-08-20 redesign cutover (v2, "
        "corrected retry of the rolled-back 2026-08-19 v1) -- 723 rows, pre-dates "
        "escalation_history entirely. Read-only reference only, excluded from all new "
        "validation/correction (researcher instruction, 2026-08-19). Superseded by escalation + "
        "escalation_history.' "
        "WHERE database='iba' AND name='escalation'")
    conn.execute(
        "UPDATE cfg_column SET table_name='escalations_old' WHERE database='iba' AND table_name='escalation'")
    conn.execute(
        "UPDATE cfg_index SET table_name='escalations_old' WHERE table_name='escalation'")
    conn.execute(
        "UPDATE cfg_unique SET table_name='escalations_old' WHERE database='iba' AND table_name='escalation'")
    return count


def _register_and_build(conn: sqlite3.Connection, cfg: Cfg) -> None:
    conn.execute("INSERT INTO cfg_table (database, name, grain, \"use\") VALUES ('iba',?,?,?)",
                (ESCALATION_TABLE_ROW[0], ESCALATION_TABLE_ROW[2], ESCALATION_TABLE_ROW[1]))
    conn.execute("INSERT INTO cfg_table (database, name, grain, \"use\") VALUES ('iba',?,?,?)",
                (HISTORY_TABLE_ROW[0], HISTORY_TABLE_ROW[2], HISTORY_TABLE_ROW[1]))
    for name, ordinal, ctype, is_pk, notnull, is_unique, dflt, fk, use, expectation, filled_by in ESCALATION_COLUMNS:
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
            'is_unique, dflt, fk, "use", expectation, source, filled_by) '
            "VALUES ('iba','escalation',?,?,?,?,?,?,?,?,?,?,NULL,?)",
            (name, ordinal, ctype, is_pk, notnull, is_unique, dflt, fk, use, expectation, filled_by))
    for name, ordinal, ctype, is_pk, notnull, is_unique, dflt, fk, use, expectation, filled_by in HISTORY_COLUMNS:
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
            'is_unique, dflt, fk, "use", expectation, source, filled_by) '
            "VALUES ('iba','escalation_history',?,?,?,?,?,?,?,?,?,?,NULL,?)",
            (name, ordinal, ctype, is_pk, notnull, is_unique, dflt, fk, use, expectation, filled_by))
    conn.execute(
        "INSERT INTO cfg_unique (database, table_name, col, ordinal) VALUES "
        "('iba','escalation_history','escalation_id',0), "
        "('iba','escalation_history','version',1)")
    conn.execute(
        "INSERT INTO cfg_index (table_name, name, col, ordinal) VALUES "
        "('escalation_history','idx_escalation_history_escalation_id','escalation_id',0)")

    create_sql, index_sql = table_ddl(cfg, "escalation")
    conn.execute(create_sql)
    for sql in index_sql:
        conn.execute(sql)
    create_sql, index_sql = table_ddl(cfg, "escalation_history")
    conn.execute(create_sql)
    for sql in index_sql:
        conn.execute(sql)


def _seed_sequence(conn: sqlite3.Connection) -> None:
    # The new `escalation` table is empty at this point -- no sqlite_sequence row exists for it
    # yet (SQLite only creates one on an AUTOINCREMENT table's first real insert), so this is
    # always a plain insert here, never an update.
    conn.execute("DELETE FROM sqlite_sequence WHERE name='escalation'")
    conn.execute("INSERT INTO sqlite_sequence (name, seq) VALUES ('escalation', ?)", (OLD_MAX_ID,))


def _upsert_enum(conn: sqlite3.Connection, name: str, value: str, ordinal: int) -> None:
    conn.execute(
        "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0) "
        "ON CONFLICT(name, value) DO UPDATE SET ordinal=excluded.ordinal, inactive=0",
        (name, value, ordinal))


def _update_enums(conn: sqlite3.Connection) -> None:
    conn.execute("UPDATE cfg_enum SET inactive=1 WHERE name='escalation_state' AND value='re-assign'")
    for ordinal, value in enumerate(NEW_ESCALATION_STATE_ADDITIONS, start=7):
        _upsert_enum(conn, "escalation_state", value, ordinal)
    # approve/reject/revise/hold/noted stay ACTIVE, unchanged -- only add the 3 new manual-shape
    # values (correction from v1, which wrongly retired approve/hold).
    for ordinal, value in enumerate(NEW_ESCALATION_NEXT_ACTION_ADDITIONS, start=5):
        _upsert_enum(conn, "escalation_next_action", value, ordinal)


# ── 4 carryover items, verbatim from escalations_old, re-raised fresh ───────────────────────────
CARRYOVER = [
    # old_id, source, type, short_description, context, comment, related_activity, assigned_to
    (650, "researcher", "task",
     "Filing/consolidation decision needed: think through filing between the main project and "
     "IBA -- anything related to the phases should be filed together, not split across branches; "
     "topic-specific reports must not be dumped in the general one-off reports folder. Also "
     "resolves the deferred governance.oneoff_report_dir CSV row.",
     '{"reference_doc": "outputs/markdown/iba-table-review-response-v1-20260816.md"}',
     "Carried over from escalations_old #650 at the 2026-08-19 redesign cutover -- was on-hold, "
     "hold this follow up, dependent on a deeper review of the statement of affairs.",
     "oneoff-report filing / main-project-IBA consolidation -- carried over from escalations_old #650",
     "Researcher"),
    (654, "researcher", "task",
     "Create escalation for moving the debate work currently in IBA (passage/phenomenon/operation/"
     "hib debate-pipeline tables) to research_db -- this work is part of findings, which belongs "
     "in research_db per governance.scope_research_db vs governance.scope_iba_db. GATED: do not "
     "start until the IBA design audit is complete.",
     '{"reference_doc": "Workflow/Chat_responses/Additional configs"}',
     "Carried over from escalations_old #654 at the 2026-08-19 redesign cutover -- was on-hold, "
     "hold until work on analytic phase is restarted.",
     "additional-configs-20260816 -- carried over from escalations_old #654",
     "Claude"),
    (668, "cluster", "issue",
     "Cluster-assignment exceptions: 746 strong(s) carry a non-T2 cluster with no word_registry "
     "link at all; 825 backfill strong(s) have an already-active or already-clustered sibling. "
     "Full detail: iba/app/reports/cluster-assign-v2-20260817.md.",
     '{"no_word": 746, "sibling_conflict": 825, "report_path": "iba/app/reports/cluster-assign-v2-20260817.md"}',
     "Carried over from escalations_old #668 at the 2026-08-19 redesign cutover -- was on-hold: "
     "currently backfill strongs (not T2 and T3) may not linked to words. Analytics will identify "
     "individual backfills that must be pulled into the registry, rather than doing the "
     "outstanding backfill word imports in bulk.",
     "cluster.validate -- carried over from escalations_old #668",
     "Researcher"),
    (725, "researcher", "task",
     "Programme prose chapters 4-6 (Data architecture / Data integrity & governance / Instruction "
     "corpus) are registered cfg_prose_chapter status='not_yet_aligned' -- content likely predates "
     "the 2026-08-15 iba.db/bible_research.db architecture correction. Needs: read each chapter "
     "against live GOVERNANCE.md/CLAUDE.md/the actual DB split, identify what's stale, revise or "
     "supersede. Include the README on project root also.",
     '{"reference_doc": "iba/app/reports/gr-prog-001-prose-canonical-authority-plan-20260818.md"}',
     "Carried over from escalations_old #725 at the 2026-08-19 redesign cutover -- was in-progress, "
     "next_action=approve: I would not be surprised to find discrepancies between what is set in "
     "prose, and what is still lingering and inconsistent in the governance and claude.",
     "gr-prog-001-prose-canonical-authority -- carried over from escalations_old #725",
     "Claude"),
]


def _raise_carryovers(conn: sqlite3.Connection, now: str) -> list[int]:
    new_ids = []
    for old_id, source, etype, short_desc, context, comment, related, assigned_to in CARRYOVER:
        run_id = f"MANUAL-{now.replace('-', '').replace(':', '').rstrip('Z')}_{old_id:04d}"
        cur = conn.execute(
            "INSERT INTO escalation (version, run_id, source, at_step, type, short_description, "
            "context, comment, state, next_action, next_action_assigned_to, originator, "
            "related_activity, raised_at, answered_at) VALUES "
            "(1,?,?,?,?,?,?,?, 'raised','review',?,'Claude',?,?,?)",
            (run_id, source, "manual", etype, short_desc, context, comment, assigned_to, related,
             now, now))
        new_id = cur.lastrowid
        conn.execute(
            "INSERT INTO escalation_history (escalation_id, version, run_id, source, at_step, "
            "type, short_description, context, comment, tried, state, next_action, "
            "next_action_assigned_to, originator, resolution, related_activity, raised_at, "
            "answered_at) SELECT id, version, run_id, source, at_step, type, short_description, "
            "context, comment, tried, state, next_action, next_action_assigned_to, originator, "
            "resolution, related_activity, raised_at, answered_at FROM escalation WHERE id=?",
            (new_id,))
        new_ids.append((old_id, new_id))
    return new_ids


def run() -> None:
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    cfg = Cfg(DB_PATH)          # same connection for both -- table_ddl() reads cfg_column via
    conn = cfg.conn              # cfg.conn, so it must see this script's own uncommitted inserts
    conn.execute("BEGIN")
    try:
        old_count = _rename_old_table(conn)
        print(f"  escalations_old: {old_count} rows preserved, frozen, marked inactive")
        _register_and_build(conn, cfg)
        print("  escalation + escalation_history: created from cfg_column (config-driven DDL)")
        _seed_sequence(conn)
        print(f"  sqlite_sequence: new escalation ids continue from {OLD_MAX_ID + 1}")
        _update_enums(conn)
        print("  cfg_enum: escalation_state += supersede, re-assigned (re-assign deactivated); "
              "escalation_next_action += review, ready_for_approval, approved "
              "(approve/reject/revise/hold/noted stay active, unchanged)")
        pairs = _raise_carryovers(conn, now)
        for old_id, new_id in pairs:
            print(f"  carried over: escalations_old #{old_id} -> new escalation #{new_id}")
        conn.commit()
        print("  COMMITTED.")
    except Exception:
        conn.rollback()
        print("  ROLLED BACK -- no changes applied.")
        raise
    finally:
        cfg.close()


if __name__ == "__main__":
    run()
