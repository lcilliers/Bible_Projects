"""escalation.py -- util.escalation: the record of open items in the project (errors, issues,
building tasks, threads). Not a run log: a standard routine is logged by the engine (run state,
resume point, outcome) and escalates only on a genuine error. A development or design control,
above all a configmaint.propose config write, keeps a gated approval here.

Two shapes, both writing through `_snapshot()`:
  - dispatcher-tied (`run_id` set): a real pipeline pause. `raise_()`, `pending_for_run()`,
    `answered_for_run()`, `answer_for_run()`.
  - manual (`run_id` MANUAL-...): the researcher/Claude backlog. `raise_new()`, `update()`,
    `correction()`, `resolve_self_correctable()`, `escalate_to_decision()`.
`escalation` holds each item's current state; `escalation_history` holds one row per version, its
content fields set only where that version changed them.

State derivation is config (`cfg_escalation_transition`, `_evaluate_transition()`), and so are the
field requirements (`cfg_escalation_requirement`, `_check_requirements()`). `originator` has no
default anywhere: every caller says who it is.

Threads (type='thread', alias OT-nn, #2000): items in `escalation_thread_item` (current status),
every response in `escalation_thread_item_response`; rules T0-T9 in config (THREADS section).

CLI (`python -m iba.app.lib.escalation`; `--originator`/`--by` required on every write verb):
    list
    answer-run <run_id> <approve|reject|revise|hold|noted> --by=... [--resolution=...] [comment...]
    raise <question...> --originator=... --comment=... --resolution-kind=decision_required|self_correctable
        [--source=...] [--assigned-to=...] [--type=...] [--state=...] [--comes-back-when=...]
        [--item=kind:value ...] [--needs-followup=1]   (approved then routes back to Claude, #1075)
    resolve-self-correctable <id> --originator=Claude --resolution=...
    escalate-to-decision <id> --originator=Claude --tried=...
    update <id> --originator=... [--next-action=...] [--assigned-to=...] [--state=...]
        [--resolution=...] [--tried=...] [--needs-followup=1|0] [thread flags] [comment words...]
    correction <id> --originator=... [--short-description=...] [--state=...] [...]
        error correction only (#774): any state, nothing auto-derived.
    match | thread-check                              (threads, T1 / T5)
Every <id> also takes a thread alias.
"""

from __future__ import annotations

import datetime
import json
import pathlib
import re
import sqlite3
import sys
import time

from . import reportkit
from .cfg import Cfg
from .db import Db

# State groups live in config (cfg_enum escalation_state_open / _parked / _terminal, #2173): open
# is what is being worked; every "not yet closed" check uses open + parked (live_states).
_STATE_GROUP_ENUM = {"open": "escalation_state_open", "parked": "escalation_state_parked",
                     "terminal": "escalation_state_terminal"}
_STATE_GROUP_SQL = {   # literal names, so configmaint's orphan check sees each group's reader
    "open": "SELECT value FROM cfg_enum WHERE name='escalation_state_open' AND inactive=0 ORDER BY ordinal",
    "parked": "SELECT value FROM cfg_enum WHERE name='escalation_state_parked' AND inactive=0 ORDER BY ordinal",
    "terminal": "SELECT value FROM cfg_enum WHERE name='escalation_state_terminal' AND inactive=0 ORDER BY ordinal",
}
_THREAD_OPEN_STATES = ("on-hold", "in-progress")    # a thread never sits at raised (T2)


def state_group(db, group: str) -> tuple[str, ...]:
    """The states in one group ('open' | 'parked' | 'terminal'), from cfg_enum. `db` is a Db or a
    sqlite3 connection. Missing config is an error, never a silent default."""
    conn = getattr(db, "conn", db)
    rows = conn.execute(_STATE_GROUP_SQL[group]).fetchall()
    if not rows:
        raise RuntimeError(f"cfg_enum {_STATE_GROUP_ENUM[group]!r} has no active values -- the "
                           f"escalation state groups are config (#2173 G1)")
    return tuple(r[0] for r in rows)


def live_states(db) -> tuple[str, ...]:
    """Not yet closed: open + parked."""
    return state_group(db, "open") + state_group(db, "parked")

# every business column on `escalation` / `escalation_history` (id/version/escalation_id are
# structural). `alias` (threads) is immutable like type/raised_at.
_ENVELOPE_COLS = ("state", "next_action", "next_action_assigned_to", "originator", "answered_at",
                 "resolution_kind", "needs_claude_followup")
_APPEND_COLS = ("comment", "context")            # escalation: cumulative. history: raw increment.
_REPLACE_COLS = ("resolution", "tried", "short_description", "comes_back_when")
_IMMUTABLE_COLS = ("run_id", "source", "at_step", "type", "raised_at", "alias")
_COLS = _ENVELOPE_COLS + _APPEND_COLS + _REPLACE_COLS + _IMMUTABLE_COLS


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _grant(cfg: Cfg, table: str):
    if table not in cfg.may_write("escalation"):
        raise PermissionError(f"write-grant violation: 'escalation' may not write {table!r}")


def word_source(word: str) -> str:
    return f"new-word: {word}"


def _check_state(db: Db, state: str) -> str:
    valid = db.cfg.enum("escalation_state")
    if state not in valid:
        raise ValueError(f"{state!r} is not a member of cfg_enum 'escalation_state' ({valid!r})")
    return state


def _check_type(db: Db, etype: str) -> str:
    valid = db.cfg.enum("escalation_type")
    if etype not in valid:
        raise ValueError(f"{etype!r} is not a member of cfg_enum 'escalation_type' ({valid!r})")
    return etype


def _check_resolution_kind(db: Db, value: str) -> str:
    """decision_required | self_correctable (cfg_enum resolution_kind) -- escalation #798/#799,
    cfg_behaviour_rule 'decision-points-are-terminal-not-inline'."""
    valid = db.cfg.enum("resolution_kind")
    if value not in valid:
        raise ValueError(f"{value!r} is not a member of cfg_enum 'resolution_kind' ({valid!r})")
    return value


def _check_next_action_manual(db: Db, next_action: str | None) -> str | None:
    if next_action is None:
        return None
    valid = db.cfg.enum("escalation_next_action_manual")
    if next_action not in valid:
        raise ValueError(f"{next_action!r} is not a member of cfg_enum "
                         f"'escalation_next_action_manual' ({valid!r})")
    return next_action


def _check_next_action_dispatcher(db: Db, decision: str) -> str:
    valid = db.cfg.enum("escalation_next_action_dispatcher")
    if decision not in valid:
        raise ValueError(f"{decision!r} is not a member of cfg_enum "
                         f"'escalation_next_action_dispatcher' ({valid!r})")
    return decision


def _check_assignee(db: Db, who: str | None, required: bool = True) -> str | None:
    if who is None:
        if required:
            raise ValueError("originator is required — must be 'Claude' or 'Researcher'. No "
                             "default (escalation rebuild 2026-08-20): a silent 'Researcher' "
                             "default previously misattributed >=39 history rows in one session.")
        return None
    normalised = who.strip().capitalize()
    valid = db.cfg.enum("escalation_assignee")
    if normalised not in valid:
        raise ValueError(f"{who!r} is not a member of cfg_enum 'escalation_assignee' ({valid!r})")
    return normalised


_TITLE_MAX_CHARS = 60


def _title_shape_error(short_description: str) -> str | None:
    """Returns an error message if `short_description` breaks the title shape (#759: a title,
    <=60 chars, no clause-stitching), else None."""
    if "\n" in short_description:
        return "short_description must be a single line (a title) -- it contains a newline."
    if len(short_description) > _TITLE_MAX_CHARS:
        return (f"short_description is {len(short_description)} chars, over the "
                f"{_TITLE_MAX_CHARS}-char title limit. It must read like a title/subject naming "
                f"the topic -- move the detail into context (background needed to understand/"
                f"decide) or comment (what needs to be done, or the error).")
    if "--" in short_description:
        return ("short_description contains '--' -- that's a clause connector, a reliable sign "
                "this is a compressed sentence, not a title. Rephrase as a noun phrase naming the "
                "topic; move the detail into context/comment.")
    return None


def _status_for(db: Db, set_by_substr: str, fallback: str) -> str:
    """cfg_status_flow lookup for entity='escalation'. `fallback` only covers a missing row."""
    for r in db.conn.execute(
            "SELECT status FROM cfg_status_flow WHERE entity='escalation' AND set_by LIKE ?",
            (f"%{set_by_substr}%",)):
        return r["status"]
    return fallback


# ── the config-driven state-derivation rule engine ───────────────────────────────────────────────
def _condition_true(condition_key: str, *, next_action: str | None, has_resolution: bool,
                    assignee_changed: bool, has_explicit_state: bool = False,
                    needs_followup: bool = False, cur_next_action: str | None = None,
                    thread: dict | None = None) -> bool:
    """The fixed vocabulary cfg_escalation_transition.condition_key draws from. A new condition
    needs a code change here; which rule consumes it, in what priority, with what result, is config.

    `thread` is None for every non-thread item, so the thread conditions are false for them. For
    a thread it carries: items_changed (an item added, closed or reopened this call, or the state
    of the work an 'escalation' item references changed), closed_some, open_remaining, all_settled
    and referenced (an open 'escalation' item points at a task/issue at state in-progress)."""
    if condition_key == "always":
        return True
    if condition_key == "thread_items_changed_and_referenced":          # T3/T5
        return bool(thread and thread["items_changed"] and thread["referenced"])
    if condition_key == "thread_items_changed_partly_closed":           # T6, partial completion
        return bool(thread and thread["closed_some"] and thread["open_remaining"]
                    and not thread["referenced"])
    if condition_key == "has_resolution":
        return bool(has_resolution)
    if condition_key == "thread_items_all_settled":           # last open item settled: the
        return bool(thread and thread["items_changed"]         # thread completes; never on
                    and thread["all_settled"]                  # reject (withdraw/supersede
                    and next_action != "reject")               # settles its items itself)
    if condition_key == "thread_reassigned":                  # reassigning a thread keeps its
        return bool(thread is not None and assignee_changed)   # state (#2000 D1)
    if condition_key == "assignee_changed":
        return bool(assignee_changed)
    if condition_key == "explicit_state_given":               # an explicit -State outranks
        return bool(has_explicit_state)                        # assignee_changed (#762)
    if condition_key == "needs_followup":                      # approved but flagged: back to
        return bool(needs_followup)                            # Claude, not completed (#1075)
    if condition_key == "followup_cleared_was_approved":
        # Approved, resolution on file, follow-up now cleared: completed, without a second approval.
        return not needs_followup and has_resolution and cur_next_action == "approved"
    raise ValueError(f"unknown cfg_escalation_transition.condition_key {condition_key!r}")


def _evaluate_transition(db: Db, shape: str, next_action: str | None, *, has_resolution: bool,
                         assignee_changed: bool, explicit_state: str | None,
                         cur_state: str, needs_followup: bool = False,
                         cur_next_action: str | None = None, thread: dict | None = None) -> str:
    """Reads cfg_escalation_transition for `shape`, in priority order, first match wins.
    `resulting_status_key` `__explicit__` is the reject branch: the caller's own state, validated
    here (withdraw|supersede only). `__unchanged__` carries the state forward (or the caller's
    -State). The caller's explicit -State outranks an inferred assignee_changed result (#762)."""
    rows = db.rows(
        "SELECT priority, next_action, condition_key, resulting_status_key FROM "
        "cfg_escalation_transition WHERE shape=? AND active=1 ORDER BY priority", (shape,))
    if not rows:
        raise ValueError(f"cfg_escalation_transition has no active rows for shape={shape!r} -- "
                         f"run migration/rebuild_escalation_rules_config_20260820")
    for r in rows:
        if r["next_action"] is not None and r["next_action"] != next_action:
            continue
        if not _condition_true(r["condition_key"], next_action=next_action,
                               has_resolution=has_resolution, assignee_changed=assignee_changed,
                               has_explicit_state=explicit_state is not None,
                               needs_followup=needs_followup, cur_next_action=cur_next_action,
                               thread=thread):
            continue
        key = r["resulting_status_key"]
        if key == "__explicit__":
            if explicit_state not in ("withdraw", "supersede"):
                raise ValueError("next_action='reject' requires state='withdraw' or 'supersede', "
                                 "chosen explicitly by the caller")
            return explicit_state
        if key == "__unchanged__":
            return explicit_state or cur_state
        return _status_for(db, key, cur_state)
    raise ValueError(f"no cfg_escalation_transition rule matched shape={shape!r} "
                     f"next_action={next_action!r} -- the priority-last 'always' rule should have "
                     f"caught this; check the seed data")


# ── the config-driven field-requirement checker ──────────────────────────────────────────────────
def _requirement_condition_true(condition_key: str, *, originator: str, checked_action: str | None,
                                values: dict) -> bool:
    """`values` -- some conditions need to look at what the caller is actually supplying this
    transaction, not just who they are / what action they're taking."""
    if condition_key == "always":
        return True
    if condition_key == "claude_revising":
        return originator == "Claude" and checked_action == "revise"
    if condition_key == "has_content":                         # D26
        return bool(values.get("comment") or values.get("context") or values.get("tried"))
    if condition_key == "thread_type":                         # escalation #2000 (T4/T6/T7)
        return values.get("type") == "thread"
    if condition_key == "thread_superseding":
        return values.get("type") == "thread" and values.get("state") == "supersede"
    raise ValueError(f"unknown cfg_escalation_requirement.condition_key {condition_key!r}")


def _check_requirements(db: Db, action: str, *, originator: str, checked_action: str | None,
                        values: dict, self_id: int | None = None) -> None:
    """Raises ValueError on the first unmet requirement. `values` = the field->value the caller is
    supplying this transaction (already merged where relevant). `check_kind` selects the
    comparison. `self_id` is the item's own id (None at Raise)."""
    rows = db.rows(
        "SELECT field, condition_key, check_kind, message FROM cfg_escalation_requirement "
        "WHERE action=? AND active=1", (action,))
    for r in rows:
        if not _requirement_condition_true(r["condition_key"], originator=originator,
                                           checked_action=checked_action, values=values):
            continue
        kind = r["check_kind"] or "field_required"
        field_val = values.get(r["field"])
        if kind == "field_required":
            if not field_val:
                raise ValueError(r["message"])
        elif kind == "not_raised_with_content":                # D26
            if field_val == "raised":
                raise ValueError(r["message"])
        elif kind == "requires_current_ready_for_approval_if_decision_required":
            # A decision_required item may be approved only while it sits at ready_for_approval (#851).
            if self_id is not None:
                row = db.rows("SELECT resolution_kind, next_action FROM escalation WHERE id=?",
                              (self_id,))
                if (row and row[0]["resolution_kind"] == "decision_required"
                        and row[0]["next_action"] != "ready_for_approval"):
                    raise ValueError(r["message"])
        elif kind == "actor_must_be_assignee":
            # Inactive: no active cfg_escalation_requirement row uses this check_kind (rows 17-19 set
            # active=0); kept so it can be re-enabled by one row update. The D25 authority
            # check in update() is separate and stays.
            if self_id is not None:
                row = db.rows("SELECT next_action_assigned_to FROM escalation WHERE id=?", (self_id,))
                cur_assignee = row[0]["next_action_assigned_to"] if row else None
                if cur_assignee and originator != cur_assignee:
                    raise ValueError(
                        f"escalation #{self_id} is currently assigned to {cur_assignee!r} -- only "
                        f"{cur_assignee} may act on it (got originator={originator!r}). "
                        f"{cur_assignee} must process it first (even just to reassign it onward).")
        elif kind == "decision_required_approval_requires_researcher":
            # Only the researcher may approve a decision_required item, whoever it was assigned to.
            if self_id is not None:
                row = db.rows("SELECT resolution_kind FROM escalation WHERE id=?", (self_id,))
                if (row and row[0]["resolution_kind"] == "decision_required"
                        and originator != "Researcher"):
                    raise ValueError(r["message"])
        elif kind == "ready_for_approval_not_assignable_to_claude":
            # A task or issue can never be put at ready_for_approval assigned to Claude.
            if self_id is not None and values.get("next_action_assigned_to") == "Claude":
                row = db.rows("SELECT type FROM escalation WHERE id=?", (self_id,))
                if row and row[0]["type"] in ("task", "issue"):
                    raise ValueError(r["message"])
        elif kind == "reassign_to_researcher_requires_ready_for_approval":
            # Claude hands a decision_required item to the researcher only by setting
            # next_action=ready_for_approval in the same call; no bare reassignment (rule 63).
            if self_id is not None:
                row = db.rows("SELECT resolution_kind, next_action_assigned_to FROM escalation "
                              "WHERE id=?", (self_id,))
                if row:
                    cur_assignee = row[0]["next_action_assigned_to"]
                    new_assignee = values.get("next_action_assigned_to")
                    new_next_action = values.get("next_action")
                    if (row[0]["resolution_kind"] == "decision_required" and originator == "Claude"
                            and cur_assignee == "Claude" and new_assignee == "Researcher"
                            and new_next_action != "ready_for_approval"):
                        raise ValueError(r["message"])
        elif kind == "must_be_self_correctable":
            # every thread is raised self_correctable (T4)
            if field_val != "self_correctable":
                raise ValueError(r["message"])
        elif kind == "no_open_thread_items":
            # T6: a thread reaches completed/closed only when every item is closed. `field` is 'state',
            # the state this call would land on; items written earlier in the same call are visible here.
            if self_id is not None and field_val in ("completed", "closed"):
                n_open = db.rows("SELECT COUNT(*) AS n FROM escalation_thread_item WHERE "
                                 "escalation_id=? AND status='open'", (self_id,))[0]["n"]
                if n_open:
                    raise ValueError(f"{r['message']} ({n_open} open item(s) on #{self_id})")
        else:
            raise ValueError(f"unknown cfg_escalation_requirement.check_kind {kind!r}")


# ── the shared core: every write, either shape, goes through this ───────────────────────────────
def _current(db: Db, escalation_id: int) -> dict:
    rows = db.rows("SELECT * FROM escalation WHERE id=?", (escalation_id,))
    if not rows:
        raise ValueError(f"no escalation #{escalation_id}")
    return dict(rows[0])


def _grant_both(cfg: Cfg) -> None:
    _grant(cfg, "escalation")
    _grant(cfg, "escalation_history")


def _create(cfg: Cfg, db: Db, **fields) -> int:
    """New item, version 1: every field is set, so the v1 history row is the full row."""
    _grant_both(cfg)
    row = {"version": 1, **{k: fields.get(k) for k in _COLS}}
    new_id = db.write("escalation", row)
    db.write("escalation_history", {"escalation_id": new_id, "version": 1,
                                    **{k: fields.get(k) for k in _COLS}})
    return new_id


def _snapshot(cfg: Cfg, db: Db, escalation_id: int, deltas: dict, envelope: dict,
              originator: str) -> dict:
    """`deltas` = what the caller sets THIS transaction for append/replace columns (None/absent =
    untouched). `envelope` = state/next_action/next_action_assigned_to, already resolved. The
    history row gets the deltas as given (NULL where not supplied) plus the envelope; `escalation`
    gets append columns merged onto the running text and replace columns updated or carried."""
    _grant_both(cfg)
    cur = _current(db, escalation_id)
    version = cur["version"] + 1
    now = _now()

    hist_row = {c: None for c in _APPEND_COLS + _REPLACE_COLS + _IMMUTABLE_COLS}
    for c in _APPEND_COLS + _REPLACE_COLS:
        if deltas.get(c):
            hist_row[c] = deltas[c]
    hist_row.update(envelope)
    hist_row["originator"] = originator
    hist_row["answered_at"] = now
    db.write("escalation_history", {"escalation_id": escalation_id, "version": version, **hist_row})

    merged = dict(cur)
    for c in _APPEND_COLS:
        if deltas.get(c):
            merged[c] = _append(cur[c], deltas[c])
    for c in _REPLACE_COLS:
        if deltas.get(c) is not None:
            merged[c] = deltas[c]
    merged.update(envelope)
    merged["originator"] = originator
    merged["answered_at"] = now
    merged["version"] = version
    db.update("escalation", {"id": escalation_id}, version=version,
             **{k: merged[k] for k in _COLS})
    return merged


def _append(current: str | None, addition: str | None) -> str | None:
    if not addition:
        return current
    return f"{current}\n{addition}" if current else addition


def _last_next_action_originator(db: Db, escalation_id: int, next_action: str) -> str | None:
    rows = db.rows(
        "SELECT originator FROM escalation_history WHERE escalation_id=? AND next_action=? "
        "ORDER BY version DESC LIMIT 1", (escalation_id, next_action))
    return rows[0]["originator"] if rows else None


def _last_next_action_assigned_to(db: Db, escalation_id: int, next_action: str) -> str | None:
    """Who a past transaction ASSIGNED the item to when it set `next_action` (not who did it).
    Answers 'ready_for_approval assigned this to whom' for the D25 authority check."""
    rows = db.rows(
        "SELECT next_action_assigned_to FROM escalation_history WHERE escalation_id=? AND "
        "next_action=? ORDER BY version DESC LIMIT 1", (escalation_id, next_action))
    return rows[0]["next_action_assigned_to"] if rows else None


# ── THREADS (type='thread', escalation #2000) ────────────────────────────────────────────────────
# The open threads register carried in the escalation table. Rules T0-T9 are config:
# cfg_escalation, cfg_escalation_transition (priority 0, the thread_* condition keys),
# cfg_escalation_requirement (thread_type rows), cfg_behaviour_rule
# open-threads-carried-as-escalations. escalation_thread_item holds current status only; every
# response, each completion included, is an escalation_thread_item_response row.

def resolve_id(db: Db, ref) -> int:
    """An escalation id from `ref`: 2000, '2000', '#2000', or a thread alias 'OT-16' (any case)."""
    s = str(ref).strip()
    if s.startswith("#"):
        s = s[1:]
    if s.isdigit():
        return int(s)
    rows = db.rows("SELECT id FROM escalation WHERE alias=? COLLATE NOCASE", (s,))
    if not rows:
        raise ValueError(f"no escalation with id or alias {ref!r}")
    return rows[0]["id"]


def _next_alias(db: Db) -> str:
    rows = db.rows("SELECT MAX(CAST(substr(alias, 4) AS INTEGER)) AS n FROM escalation "
                   "WHERE alias LIKE 'OT-%'")
    return f"OT-{(rows[0]['n'] or 0) + 1:02d}"


def parse_item_spec(spec: str) -> tuple[str, str, str | None]:
    """'kind:value[:note]' -> (kind, value, note). The value may itself hold a colon (a verse,
    'Rom 7:15-21'), so the note is split off only on ' :: ' -- 'verse:Rom 7:15-21 :: 7 verses'."""
    if ":" not in spec:
        raise ValueError(f"item {spec!r} must be kind:value (e.g. cluster:M72, verse:Rom 7:15)")
    kind, rest = spec.split(":", 1)
    note = None
    if " :: " in rest:
        rest, note = rest.split(" :: ", 1)
    return kind.strip().lower(), rest.strip(), (note.strip() if note else None)


def _thread_items(db: Db, escalation_id: int, status: str | None = None):
    if status:
        return db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND status=? "
                       "ORDER BY item_no", (escalation_id, status))
    return db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? ORDER BY item_no",
                   (escalation_id,))


def _add_item(cfg: Cfg, db: Db, escalation_id: int, kind: str, value: str, note: str | None,
              *, opened_by: int | None, at: str) -> dict:
    _grant(cfg, "escalation_thread_item")
    if kind not in db.cfg.enum("escalation_thread_item_kind"):
        raise ValueError(f"{kind!r} is not a member of cfg_enum 'escalation_thread_item_kind' "
                         f"({db.cfg.enum('escalation_thread_item_kind')!r})")
    if not value:
        raise ValueError("an item needs a value (kind:value)")
    dup = db.rows("SELECT item_no, status FROM escalation_thread_item WHERE escalation_id=? AND "
                  "kind=? AND value=? COLLATE NOCASE", (escalation_id, kind, value))
    if dup:
        raise ValueError(f"item {kind}:{value} already exists on #{escalation_id} as item "
                         f"{dup[0]['item_no']} ({dup[0]['status']}) -- respond to it instead "
                         f"(-ResponseKind reopened if it is closed)")
    n = db.rows("SELECT COALESCE(MAX(item_no), 0) + 1 AS n FROM escalation_thread_item "
                "WHERE escalation_id=?", (escalation_id,))[0]["n"]
    row = {"escalation_id": escalation_id, "item_no": n, "kind": kind, "value": value,
           "status": "open", "note": note, "opened_at": at, "opened_by": opened_by}
    row["id"] = db.write("escalation_thread_item", row)
    return row


def _resolve_item(db: Db, thread: dict, ref: str):
    """An item of `thread` from `ref`: 'OT-16.1' (alias must be this thread's), '1' (the item
    number), 'kind:value', or the value alone (unique within the thread)."""
    s = ref.strip()
    alias = thread["alias"] or ""
    if alias and s.upper().startswith(alias.upper() + "."):
        s = s[len(alias) + 1:]
    elif s.upper().startswith("OT-") and "." in s:
        raise ValueError(f"item {ref!r} does not belong to {alias or '#' + str(thread['id'])}")
    if s.isdigit():
        rows = db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND item_no=?",
                       (thread["id"], int(s)))
    elif ":" in s and s.split(":", 1)[0].lower() in db.cfg.enum("escalation_thread_item_kind"):
        kind, value = s.split(":", 1)
        rows = db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND kind=? "
                       "AND value=? COLLATE NOCASE", (thread["id"], kind.lower(), value.strip()))
    else:
        rows = db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND "
                       "value=? COLLATE NOCASE", (thread["id"], s))
    if len(rows) != 1:
        raise ValueError(f"item {ref!r} on {alias or '#' + str(thread['id'])}: "
                         f"{'not found' if not rows else 'ambiguous -- use the item number'}")
    return dict(rows[0])


_SETTLE_KINDS = ("closed", "withdrawn", "superseded")   # response kinds that settle an item
_SUCCESSOR_RE = re.compile(r"\bOT-\d+(?:\.\d+)?\b|#\d+")


def _respond(cfg: Cfg, db: Db, item: dict, kind: str, text: str, *, via: int | None, by: str,
             files: list | None, at: str) -> None:
    """One response row. A settling kind (closed, withdrawn, superseded) needs an open item and
    sets its status to that kind; 'reopened' opens a settled item again. 'superseded' must name
    what carries the item on (OT-nn, OT-nn.n or #nnnn) in its text."""
    _grant(cfg, "escalation_thread_item_response")
    if kind not in db.cfg.enum("escalation_thread_item_response_kind"):
        raise ValueError(f"{kind!r} is not a member of cfg_enum "
                         f"'escalation_thread_item_response_kind' "
                         f"({db.cfg.enum('escalation_thread_item_response_kind')!r})")
    if not text:
        raise ValueError("a response needs its text (-Respond); a researcher's response is quoted "
                         "verbatim (cfg_escalation 5)")
    statuses = db.cfg.enum("escalation_thread_item_status")   # open/closed/withdrawn/superseded
    if item["status"] not in statuses:
        raise ValueError(f"item {item['item_no']} has status {item['status']!r}, not a member of "
                         f"cfg_enum 'escalation_thread_item_status' ({statuses!r})")
    if kind in _SETTLE_KINDS:
        if item["status"] != "open":
            raise ValueError(f"item {item['item_no']} ({item['kind']}:{item['value']}) is already "
                             f"{item['status']} -- reopen it first")
        if kind == "superseded" and not _SUCCESSOR_RE.search(text):
            raise ValueError("a superseded response names what carries the item on (OT-nn, "
                             "OT-nn.n or #nnnn) in -Respond")
        db.update("escalation_thread_item", {"id": item["id"]}, status=kind)
        item["status"] = kind
    elif kind == "reopened":
        if item["status"] == "open":
            raise ValueError(f"item {item['item_no']} ({item['kind']}:{item['value']}) is already "
                             f"open")
        db.update("escalation_thread_item", {"id": item["id"]}, status="open")
        item["status"] = "open"
    db.write("escalation_thread_item_response", {
        "item_id": item["id"], "escalation_id": item["escalation_id"], "kind": kind, "text": text,
        "via_escalation": via, "responded_by": by, "responded_at": at,
        "files": json.dumps(files, ensure_ascii=False) if files else None})


def _settle_thread_on_reject(cfg: Cfg, db: Db, thread: dict, state: str | None, superseded_by,
                             *, reason: str | None, who: str, at: str,
                             succ_lines: list[str] | None = None) -> list[str]:
    """No thread ends with an open item. Withdraw: each open item is withdrawn with the thread's
    reason. Supersede: each open item is added to the successor thread (an existing item of the
    same kind:value is reused, reopened if settled) and recorded superseded here, naming its new
    reference. Returns summary lines for the history comment; `succ_lines`, when given, receives
    what happened on the successor, for the successor's own history."""
    alias = thread["alias"] or f"#{thread['id']}"
    open_items = [dict(r) for r in _thread_items(db, thread["id"], "open")]
    out = []
    if state == "withdraw":
        for it in open_items:
            _respond(cfg, db, it, "withdrawn", f"{alias} withdrawn: {reason or ''}".strip(),
                     via=None, by=who, files=None, at=at)
            out.append(f"item {it['item_no']} ({it['kind']}:{it['value']}) withdrawn")
        return out
    if state != "supersede":
        return out
    succ = _current(db, resolve_id(db, superseded_by))
    if succ["type"] != "thread" or succ["id"] == thread["id"]:
        raise ValueError(f"-SupersededBy {superseded_by!r} must be another thread")
    if succ["state"] not in _THREAD_OPEN_STATES:
        raise ValueError(f"-SupersededBy {succ['alias']} is {succ['state']!r}; the successor must "
                         f"be open (on-hold or in-progress)")
    for it in open_items:
        carried = f"carried over from {alias}.{it['item_no']} (superseded): {reason or ''}".strip()
        dup = db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND kind=? AND "
                      "value=? COLLATE NOCASE", (succ["id"], it["kind"], it["value"]))
        if dup:
            new = dict(dup[0])
            if new["status"] != "open":
                _respond(cfg, db, new, "reopened", carried, via=thread["id"], by=who, files=None,
                         at=at)
                done = "reopened"
            else:
                done = "already open, kept"
        else:
            new = _add_item(cfg, db, succ["id"], it["kind"], it["value"], it["note"],
                            opened_by=thread["id"], at=at)
            _respond(cfg, db, new, "note", carried, via=thread["id"], by=who, files=None, at=at)
            done = "added"
        ref = f"{succ['alias']}.{new['item_no']}"
        if succ_lines is not None:
            succ_lines.append(f"item {new['item_no']} ({it['kind']}:{it['value']}) {done}, from "
                              f"{alias}.{it['item_no']}")
        _respond(cfg, db, it, "superseded", f"superseded by {ref}: {reason or ''}".strip(),
                 via=succ["id"], by=who, files=None, at=at)
        out.append(f"item {it['item_no']} ({it['kind']}:{it['value']}) superseded by {ref}")
    return out


def _thread_referenced(db: Db, escalation_id: int) -> bool:
    """T5: an open 'escalation' item points at a task or issue that is itself in-progress."""
    for it in _thread_items(db, escalation_id, "open"):
        if it["kind"] != "escalation":
            continue
        try:
            ref_id = resolve_id(db, it["value"])
        except ValueError:
            continue
        rows = db.rows("SELECT state FROM escalation WHERE id=?", (ref_id,))
        if rows and rows[0]["state"] == "in-progress":
            return True
    return False


def _thread_facts(db: Db, escalation_id: int, *, items_changed: bool, closed_some: bool) -> dict:
    n_open = len(_thread_items(db, escalation_id, "open"))
    return {"items_changed": items_changed, "closed_some": closed_some,
            "open_remaining": n_open,
            "all_settled": n_open == 0 and bool(_thread_items(db, escalation_id)),
            "referenced": _thread_referenced(db, escalation_id)}


def _thread_completion_resolution(db: Db, thread: dict) -> str:
    """The resolution written when a thread completes because its last item was settled: each item
    with how it was settled, from its latest response."""
    alias = thread["alias"] or f"#{thread['id']}"
    parts = []
    for it in _thread_items(db, thread["id"]):
        r = _latest_response(db, it["id"])
        via = f" via #{r['via_escalation']}" if r and r["via_escalation"] else ""
        text = (r["text"] or "").replace("\n", " ") if r else ""
        parts.append(f"{alias}.{it['item_no']} {it['kind']}:{it['value']} {it['status']}{via}"
                     + (f": {text[:300]}{'…' if len(text) > 300 else ''}" if text else ""))
    return f"Every item settled ({len(parts)}): " + "; ".join(parts)


def _restate_thread(cfg: Cfg, db: Db, thread_id: int, summary: str, *, who: str,
                    closed_some: bool) -> str | None:
    """Re-derive a thread's state after its items, or the work they reference, changed outside an
    Update of the thread itself (a Match, a referenced task changing state). Same config rows as
    update(). Writes one history version carrying `summary`. Returns the new state, or None when
    the thread is not open."""
    cur = _current(db, thread_id)
    if cur["state"] not in _THREAD_OPEN_STATES:
        return None
    facts = _thread_facts(db, thread_id, items_changed=True, closed_some=closed_some)
    new_state = _evaluate_transition(db, "manual", None, has_resolution=bool(cur["resolution"]),
                                     assignee_changed=False, explicit_state=None,
                                     cur_state=cur["state"],
                                     needs_followup=bool(cur["needs_claude_followup"]),
                                     cur_next_action=cur["next_action"], thread=facts)
    resolution = None
    if new_state == "completed" and facts["all_settled"]:      # #2000 lifecycle: last item settled
        resolution = _thread_completion_resolution(db, cur)
    elif new_state not in _THREAD_OPEN_STATES:
        new_state = cur["state"]
    _snapshot(cfg, db, thread_id, deltas={"comment": summary, "resolution": resolution},
              envelope={"state": _check_state(db, new_state),
                        "next_action": None if resolution else cur["next_action"],
                        "next_action_assigned_to": cur["next_action_assigned_to"],
                        "resolution_kind": cur["resolution_kind"],
                        "needs_claude_followup": cur["needs_claude_followup"]},
              originator=who)
    return new_state


def _sync_threads_for(cfg: Cfg, db: Db, ref_id: int, *, who: str) -> list[str]:
    """After a task or issue changes, bring every thread that references it (an open 'escalation'
    item '#ref_id') into line: T6, at a terminal state its item takes the same ending; T3/T5, a
    thread follows the in-progress state of the work that references it."""
    ref = _current(db, ref_id)
    if ref["type"] == "thread":
        return []
    out = []
    items = db.rows("SELECT i.* FROM escalation_thread_item i JOIN escalation e ON "
                    "e.id=i.escalation_id WHERE i.kind='escalation' AND i.status='open' AND "
                    "i.value=? AND e.type='thread'", (f"#{ref_id}",))
    now = _now()
    for it in items:
        it = dict(it)
        thread = _current(db, it["escalation_id"])
        label = thread["alias"] or f"#{thread['id']}"
        if ref["state"] in state_group(db, "terminal"):
            # the item takes the task's own ending: a withdrawn or superseded task is not work done
            kind = {"withdraw": "withdrawn", "supersede": "superseded"}.get(ref["state"], "closed")
            settled = (ref["resolution"] or ref["comment"] or "").strip().replace("\n", " ")
            text = (f"#{ref_id} reached {ref['state']}"
                    + (f": {settled[:400]}{'…' if len(settled) > 400 else ''}" if settled else ""))
            _respond(cfg, db, it, kind, text, via=ref_id, by=who, files=None, at=now)
            st = _restate_thread(cfg, db, thread["id"],
                                 f"{label}: item {it['item_no']} (#{ref_id}) {kind} by {who} -- "
                                 f"{text} (T6)", who=who, closed_some=True)
        else:
            # T5 moves on-hold -> in-progress only. A thread already in-progress is left alone when
            # its work steps back (no rule moves it; T6 handles completion).
            if not (thread["state"] == "on-hold" and ref["state"] == "in-progress"):
                continue
            st = _restate_thread(cfg, db, thread["id"],
                                 f"{label}: #{ref_id} is now {ref['state']} (T3/T5)", who=who,
                                 closed_some=False)
        if st:
            out.append(f"{label} (#{thread['id']}) -> {st}")
    return out


# ── matching (T1) ──
import re as _re

_VERSE_RE = _re.compile(r"^\s*(?P<book>\d?\s*[A-Za-z]+)\.?\s+(?P<ch>\d+)"
                        r"(?::(?P<v1>\d+)(?:\s*[-–—]\s*(?P<v2>\d+))?)?\s*$")


def _parse_verse(s: str):
    m = _VERSE_RE.match(s)
    if not m:
        return None
    v1 = int(m["v1"]) if m["v1"] else None
    v2 = int(m["v2"]) if m["v2"] else v1
    return (m["book"].replace(" ", "").lower(), int(m["ch"]), v1, v2)


def _code_parts(code: str, pattern: str):
    m = _re.match(pattern, code.strip(), _re.IGNORECASE)
    return (m.group(1).upper(), (m.group(2) or "").lower()) if m else None


def _code_match(item_value: str, query: str, pattern: str, norm=lambda b: b) -> bool:
    """Exact code, else the same base when either side has no suffix (M10 <-> M10c,
    H7067 <-> H7067G); two different suffixes never match."""
    a, b = _code_parts(item_value, pattern), _code_parts(query, pattern)
    if not a or not b or norm(a[0]) != norm(b[0]):
        return False
    return a[1] == b[1] or not a[1] or not b[1]


def _strong_norm(base: str) -> str:
    return base[0] + base[1:].zfill(4)       # reference_strongs_zero_padded_4digit_in_db


def _verse_match(item_value: str, query: str) -> bool:
    """A verse matches inside a range (either side may be a range), and a whole-chapter item
    ('Rom 8') matches any verse of that chapter."""
    a, b = _parse_verse(item_value), _parse_verse(query)
    if not a or not b or a[0] != b[0] or a[1] != b[1]:
        return False
    if a[2] is None or b[2] is None:
        return True
    return a[2] <= b[3] and b[2] <= a[3]


def match_threads(cfg: Cfg, db: Db, *, clusters=(), strongs=(), verses=(), for_ref=None,
                  who: str | None = None) -> list[str]:
    """T1. Matches clusters / Strong's / verses against the open items of every thread not
    completed. Read-only unless `for_ref` names the task or issue the match is for: then each
    matched thread gains an 'escalation' item '#nnnn' (unless one is already open), and T3/T5
    re-derive its state -- in-progress only if that task or issue is itself in-progress."""
    for_id = resolve_id(db, for_ref) if for_ref is not None else None
    if for_id is not None:
        target = _current(db, for_id)
        if target["type"] == "thread":
            raise ValueError(f"-For must be a task or issue, not a thread (#{for_id})")
        if target["state"] not in live_states(db):
            raise ValueError(f"-For #{for_id} is not open (state={target['state']!r})")
        who = _check_assignee(db, who)
    if not (clusters or strongs or verses):
        raise ValueError("Match needs at least one -Cluster, -Strong or -Verse")
    ph = ",".join("?" * len(_THREAD_OPEN_STATES))
    threads = db.rows(f"SELECT * FROM escalation WHERE type='thread' AND state IN ({ph}) "
                      f"ORDER BY CAST(substr(alias, 4) AS INTEGER)", _THREAD_OPEN_STATES)
    lines, now = [], _now()
    for t in threads:
        hits = []
        for it in _thread_items(db, t["id"], "open"):
            v = it["value"]
            if it["kind"] == "cluster":
                hits += [f"{it['item_no']} {v} ({q})" for q in clusters
                         if _code_match(v, q, r"^(M\d+)([a-z]*)$")]
            elif it["kind"] == "strong":
                hits += [f"{it['item_no']} {v} ({q})" for q in strongs
                         if _code_match(v, q, r"^([HG]\d+)([A-Z]*)$", _strong_norm)]
            elif it["kind"] == "verse":
                hits += [f"{it['item_no']} {v} ({q})" for q in verses if _verse_match(v, q)]
        if not hits:
            continue
        label = f"{t['alias']} · #{t['id']}"
        line = f"{label} [{t['state']}] {t['short_description']} -- items {'; '.join(hits)}"
        if for_id is not None:
            existing = db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND "
                               "kind='escalation' AND value=?", (t["id"], f"#{for_id}"))
            matched = ", ".join(h.split(" (")[0] for h in hits)
            if existing and existing[0]["status"] == "open":
                line += f" -- #{for_id} already referenced (item {existing[0]['item_no']})"
            else:
                if existing:
                    _respond(cfg, db, dict(existing[0]), "reopened",
                             f"matched again by #{for_id}: items {matched}", via=for_id, by=who,
                             files=None, at=now)
                    n = existing[0]["item_no"]
                else:
                    n = _add_item(cfg, db, t["id"], "escalation", f"#{for_id}",
                                  f"matched: items {matched}", opened_by=for_id, at=now)["item_no"]
                st = _restate_thread(cfg, db, t["id"],
                                     f"{t['alias']}: item {n} #{for_id} added -- matched items "
                                     f"{matched} (T1)", who=who, closed_some=False)
                line += f" -- item {t['alias']}.{n} #{for_id} recorded; thread {st}"
        lines.append(line)
    return lines


def thread_check(cfg: Cfg, db: Db, *, who: str) -> list[str]:
    """T5, run at session start: every open thread referenced by a task or issue is brought into
    line with that work -- in-progress when the work is, its item closed when the work is done."""
    who = _check_assignee(db, who)
    refs = db.rows("SELECT DISTINCT i.value FROM escalation_thread_item i JOIN escalation e ON "
                   "e.id=i.escalation_id WHERE i.kind='escalation' AND i.status='open' AND "
                   "e.type='thread' AND e.state IN ('on-hold','in-progress')")
    out = []
    for r in refs:
        try:
            ref_id = resolve_id(db, r["value"])
        except ValueError:
            out.append(f"item value {r['value']!r} names no escalation -- left as is")
            continue
        out += _sync_threads_for(cfg, db, ref_id, who=who)
    return out


# ── DISPATCHER-TIED shape (run_id set) -- vocabulary/semantics unchanged, engine now config-driven
def _sanitise_dispatcher_title(question: str, preset: dict) -> tuple[str, dict]:
    """Dispatcher-tied titles still follow the title shape, but this fires from inside a crash or
    pause handler, where raising would mask the real crash: sanitise instead of reject. The
    original survives in preset['full_message'] whenever sanitising changes anything."""
    if _title_shape_error(question) is None:
        return question, preset
    flat = question.replace("\n", " ").replace("--", "-")
    if len(flat) > _TITLE_MAX_CHARS:
        flat = flat[: _TITLE_MAX_CHARS - 1].rstrip() + "…"
    return flat, {**preset, "full_message": question}


def raise_(db: Db, run_id: str, source: str, at_step: str, question: str,
          preset: dict, tried: str, etype: str = "task", assigned_to: str = "Researcher",
          resolution_kind: str | None = None, needs_followup: bool = False,
          title: str | None = None) -> int:
    """Record a pause -- called by run.py at a real dispatcher pause point.

    `resolution_kind`: every call site passes one (crash/report-stop pass `self_correctable`;
    pause-continue passes the handler's own choice). The `None` fallback (`decision_required`) is
    only a safety net. If `decision_required` and `etype` isn't `notice`, `type` becomes `issue`.

    `comment` and `originator` are always populated (#790) without raising, since this runs inside
    crash handling: `comment` reuses `tried`, `originator` is 'Claude'. `next_action` starts at
    'review', as in raise_new().

    `title`: a caller-supplied, already title-shaped short_description (#1326), so `question` can
    carry the full description. Without it, the title is sanitised from `question`. A supplied title
    is still guarded, since a bad title here must not become a second failure."""
    now = _now()
    if title and _title_shape_error(title) is None:
        short_description = title
        preset = {**preset, "full_message": question}   # the fuller description, always kept
    else:
        short_description, preset = _sanitise_dispatcher_title(question, preset)
    checked_type = _check_type(db, etype)
    try:
        checked_kind = _check_resolution_kind(db, resolution_kind) if resolution_kind else "decision_required"
    except ValueError:
        checked_kind = "decision_required"   # sanitise, never crash the raise itself
    if checked_kind == "decision_required" and checked_type != "notice":
        checked_type = "issue"
    comment = tried or f"dispatcher pause at {at_step}"
    fields = {
        "run_id": run_id, "source": source, "at_step": at_step,
        "type": checked_type, "short_description": short_description,
        "context": json.dumps(preset), "comment": comment,
        "tried": tried, "state": _check_state(db, _status_for(db, "at Raise", "raised")),
        "next_action": "review", "resolution_kind": checked_kind,
        "answered_at": now, "raised_at": now,
        "resolution": None, "needs_claude_followup": 1 if needs_followup else 0,
        "next_action_assigned_to": _check_assignee(db, assigned_to), "originator": "Claude"}
    return _create(db.cfg, db, **fields)


def pending_for_run(db: Db, run_id: str):
    """`run_id` takes the full dispatcher run_id or the short escalation id, e.g. '796' (#795).
    A short id still has to be dispatcher-tied (run_id IS NOT NULL)."""
    if run_id.isdigit():
        return db.rows(
            "SELECT * FROM escalation WHERE id=? AND run_id IS NOT NULL AND state='raised' "
            "ORDER BY id DESC LIMIT 1", (int(run_id),))
    return db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND state='raised' "
        "ORDER BY id DESC LIMIT 1", (run_id,))


def answered_for_run(db: Db, run_id: str, at_step: str):
    """The latest ANSWERED escalation for a run at a step, or None: a real decision (approve/
    approved/reject/revise) in `next_action`, whatever the `state` (#1328: an approved item with
    needs_claude_followup sits at re-assigned, not completed). `hold`/`noted` never match."""
    rows = db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND at_step=? AND "
        "next_action IN ('approve','approved','reject','revise') "
        "ORDER BY id DESC LIMIT 1", (run_id, at_step))
    return rows[0] if rows else None


def answered_baseline_for_step(db: Db, at_step: str, current_counts: dict):
    """The most recent APPROVED escalation for `at_step`, across every run, if its recorded
    `context` preset counts cover `current_counts` component-wise -- else None (#1707). Lets a
    repeated read-only check recognise an already-approved, unchanged situation. Only
    approve/approved counts; every key in `current_counts` must be present and <= its stored
    value, so any increase escalates again."""
    import json
    rows = db.rows(
        "SELECT * FROM escalation WHERE at_step=? AND "
        "next_action IN ('approve','approved') ORDER BY id DESC LIMIT 1", (at_step,))
    if not rows:
        return None
    row = rows[0]
    try:
        preset = json.loads(row["context"] or "{}")
    except (ValueError, TypeError):
        return None
    for key, value in current_counts.items():
        baseline = preset.get(key)
        if not isinstance(baseline, (int, float)) or value > baseline:
            return None
    return row


def finding_fingerprint(item: str) -> str:
    """A short stable key for one finding's text: what an escalation stores instead of the text
    itself (#2206, BUILD.md sec 42)."""
    import hashlib
    return hashlib.sha1(item.encode("utf-8")).hexdigest()[:12]


def acknowledged_findings(db: Db, at_step: str, tried_prefix: str) -> tuple[int | None, dict]:
    """The findings the researcher last acknowledged for a check step (#2206 option 1): the
    newest escalation raised by `at_step` whose `tried` starts with `tried_prefix` and whose
    next_action is approve/approved. Returns (its id, {finding key: set of fingerprints}), or
    (None, {}). The set is the item's LAST JSON line in `context` (context is cumulative; each
    re-run that changes the findings appends one): a `fingerprints` dict, or for items raised
    before #2206 the finding lists themselves, fingerprinted here."""
    import json
    rows = db.rows(
        "SELECT id, context FROM escalation WHERE at_step=? AND tried LIKE ? AND "
        "next_action IN ('approve','approved') ORDER BY id DESC LIMIT 1",
        (at_step, f"{tried_prefix}%"))
    if not rows:
        return None, {}
    found: dict = {}
    for line in (rows[0]["context"] or "").splitlines():
        if not line.startswith("{"):
            continue
        try:
            found = json.loads(line)
        except ValueError:
            continue
    if "fingerprints" in found:
        return rows[0]["id"], {k: set(v) for k, v in found["fingerprints"].items()}
    return rows[0]["id"], {k: {finding_fingerprint(i) for i in v}
                           for k, v in found.items() if isinstance(v, list)}


def open_duplicate(db: Db, at_step: str, stable_key: str):
    """Matches on `context` (it holds the untruncated preset, whose `full_message` contains
    `stable_key`; short_description is truncated to 60 chars) across every live state."""
    live = live_states(db)
    ph = ",".join("?" * len(live))
    rows = db.rows(
        f"SELECT * FROM escalation WHERE at_step=? AND state IN ({ph}) AND context LIKE ? "
        f"ORDER BY id DESC LIMIT 1", (at_step, *live, f"%{stable_key}%"))
    return rows[0] if rows else None


def open_for_step(db: Db, at_step: str, tried_prefix: str):
    """The newest still-open escalation raised by `at_step` whose `tried` starts with
    `tried_prefix`, whatever its findings (#2108): a re-run with changed counts records them on
    this one instead of raising another."""
    live = live_states(db)
    ph = ",".join("?" * len(live))
    rows = db.rows(
        f"SELECT * FROM escalation WHERE at_step=? AND state IN ({ph}) AND tried LIKE ? "
        f"ORDER BY id DESC LIMIT 1", (at_step, *live, f"{tried_prefix}%"))
    return rows[0] if rows else None


def answer_for_run(cfg: Cfg, db: Db, run_id: str, decision: str, comment: str | None = None,
                   *, answered_by: str, resolution: str | None = None) -> str:
    """Record the decision on a dispatcher-tied escalation. `answered_by` is required.

    Refused for both resolution_kind values (#795): a decision_required item is answered only
    through Update (ready_for_approval -> approved, -State on-hold, reject/revise/noted); a
    self_correctable item closes only through resolve_self_correctable() or converts through
    escalate_to_decision(). cfg_behaviour_rule decision-required-answered-via-update-not-answerrun."""
    decision = decision.lower()
    rows = pending_for_run(db, run_id)
    if not rows:
        return f"no pending escalation for run {run_id!r}"
    esc_row = rows[0]
    if esc_row["resolution_kind"] == "decision_required":
        return (f"escalation #{esc_row['id']} is resolution_kind='decision_required' -- answer it "
               f"via Update (ready_for_approval -> approved, or -State/-NextAction directly), not "
               f"AnswerRun. AnswerRun's flat approve/reject/revise is for self_correctable items "
               f"only (cfg_behaviour_rule 'decision-required-answered-via-update-not-answerrun').")
    if esc_row["resolution_kind"] == "self_correctable":
        return (f"escalation #{esc_row['id']} is resolution_kind='self_correctable' -- close it via "
               f"resolve-self-correctable (or convert it via escalate-to-decision if a fix reveals "
               f"a genuine new judgement call), not AnswerRun. Per the approved spec "
               f"(escalation-decision-vs-defect-axis-proposal-v4-20260822.md §6): self_correctable "
               f"items carry no approve/reject/revise/hold/noted vocabulary at all "
               f"(cfg_behaviour_rule 'decision-required-answered-via-update-not-answerrun').")
    who = _check_assignee(db, answered_by)
    decision = _check_next_action_dispatcher(db, decision)
    new_state = _evaluate_transition(db, "dispatcher", decision, has_resolution=bool(resolution),
                                     assignee_changed=False, explicit_state=None,
                                     cur_state=esc_row["state"])
    merged = _snapshot(cfg, db, esc_row["id"],
                       deltas={"comment": comment, "resolution": resolution},
                       envelope={"state": _check_state(db, new_state), "next_action": decision,
                                "next_action_assigned_to": esc_row["next_action_assigned_to"],
                                "resolution_kind": esc_row["resolution_kind"],
                                "needs_claude_followup": esc_row["needs_claude_followup"]},
                       originator=who)
    return (f"escalation {esc_row['id']} (run {run_id!r}, step {esc_row['at_step']!r}) answered "
           f"{decision!r} -> {new_state}" + (f" — {comment!r}" if comment else ""))


# ── MANUAL shape ──────────────────────────────────────────────────────────────────────────────
def raise_new(cfg: Cfg, db: Db, short_description: str, source: str, etype: str = "task",
             comment: str | None = None, context: str | None = None,
             assigned_to: str = "Claude", resolution_kind: str | None = None,
             needs_followup: bool = False,
             *, originator: str, state: str | None = None,
             comes_back_when: str | None = None,
             items: list[tuple[str, str, str | None]] | None = None) -> int:
    """Raise -- a new MANUAL item. `originator` is required. `comment`/`short_description`
    requirements come from cfg_escalation_requirement (action='raise').

    `resolution_kind`: decision_required or self_correctable, required. `etype` is used as given,
    checked against cfg_enum. Only `notice` is special: it closes on arrival (state='closed',
    next_action=NULL); every other type starts at state='raised', next_action='review'.

    `needs_followup` (#1075): finishing needs a further Claude action after approval, so `approved`
    routes back to Claude instead of to completed. Default False.

    `state` (T2): a manual Raise may land at any cfg_enum escalation_raise_state; default 'raised'.
    type 'thread': `items` (kind, value, note) are required (T7), resolution_kind must be
    self_correctable (T4), the alias OT-nn is assigned, the state defaults to on-hold and may not be
    'raised', and next_action is empty. `comes_back_when` holds the thread's 'comes back when' text."""
    checked_type = _check_type(db, etype)
    checked_kind = _check_resolution_kind(db, resolution_kind) if resolution_kind else None
    is_thread = checked_type == "thread"
    _check_requirements(db, "raise", originator=originator or "", checked_action=None,
                        values={"comment": comment, "short_description": short_description,
                               "resolution_kind": checked_kind, "type": checked_type,
                               "items": items or []})
    if items and not is_thread:
        raise ValueError("-Item is for type thread only")
    title_error = _title_shape_error(short_description)
    if title_error:
        raise ValueError(title_error)
    if state is not None:
        if state not in db.cfg.enum("escalation_raise_state"):
            raise ValueError(f"{state!r} is not a member of cfg_enum 'escalation_raise_state' "
                             f"({db.cfg.enum('escalation_raise_state')!r})")
        if checked_type == "notice":
            raise ValueError("a notice closes on arrival (D12) -- no -State at Raise")
    if is_thread and state == "raised":
        raise ValueError("a thread is raised at on-hold or in-progress, never 'raised' "
                         "(cfg_escalation raise_state_choice)")
    run_id = f"MANUAL-{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d_%H%M%S_%f')}"
    now = _now()
    if checked_type == "notice":
        state, next_action = _check_state(db, "closed"), None
    elif is_thread:
        state, next_action = _check_state(db, state or "on-hold"), None
    else:
        state = _check_state(db, state or _status_for(db, "at Raise", "raised"))
        next_action = "review"
    fields = {
        "run_id": run_id, "source": source, "at_step": "manual", "type": checked_type,
        "short_description": short_description, "context": context, "comment": comment,
        "tried": None, "state": state, "next_action": next_action,
        "answered_at": now, "raised_at": now, "resolution": None,
        "resolution_kind": checked_kind, "needs_claude_followup": int(needs_followup),
        "next_action_assigned_to": _check_assignee(db, assigned_to),
        "originator": _check_assignee(db, originator),
        "alias": _next_alias(db) if is_thread else None,
        "comes_back_when": comes_back_when}
    new_id = _create(cfg, db, **fields)
    for kind, value, note in items or []:
        _add_item(cfg, db, new_id, kind, value, note, opened_by=None, at=now)
    return new_id


def update(cfg: Cfg, db: Db, escalation_id: int, *, next_action: str | None = None,
          next_action_assigned_to: str | None = None, comment: str | None = None,
          context: str | None = None, tried: str | None = None, resolution: str | None = None,
          state: str | None = None, needs_followup: bool | None = None, originator: str,
          comes_back_when: str | None = None,
          add_items: list[tuple[str, str, str | None]] | None = None,
          item_refs: list[str] | None = None, respond: str | None = None,
          response_kind: str | None = None, via=None, files: list | None = None,
          superseded_by=None) -> str:
    """Update -- every later change to a MANUAL item. `originator` is required.

    `needs_followup`: None carries the current flag forward; True/False sets or clears it.

    A dispatcher-tied item is refused unless it is decision_required, which always uses the manual
    ready_for_approval/approved vocabulary. A dispatcher-tied self_correctable item closes through
    resolve_self_correctable() / escalate_to_decision().

    Threads: `item_refs` + `response_kind` + `respond` (+ `via`, `files`) record one response per
    named item; `closed`/`withdrawn`/`superseded` settle an item, `reopened` opens it, and `forward`
    needs at least one `add_items` entry. `add_items` alone adds items. Each such Update writes the
    responses in full into the thread's history. The thread's state follows the priority-0 transition
    rows; completed/closed is refused while any item is open (T6), and when the last item settles
    the thread completes with a generated resolution. Withdrawing a thread withdraws its open items;
    superseding (`superseded_by` OT-nn) moves them to the successor. After any change to a task or
    issue, every thread referencing it is brought into line (`_sync_threads_for`)."""
    cur = _current(db, escalation_id)
    if not cur["run_id"].startswith("MANUAL-") and cur["resolution_kind"] != "decision_required":
        return (f"escalation #{escalation_id} is dispatcher-tied (run_id {cur['run_id']!r}), not "
               f"manual -- answer it via AnswerRun, not Update")
    if cur["state"] not in live_states(db):
        return f"escalation #{escalation_id} is not open (state={cur['state']!r})"

    who = _check_assignee(db, originator)
    checked_action = _check_next_action_manual(db, next_action)
    new_resolution = resolution if resolution is not None else cur["resolution"]
    resolved_assignee = _check_assignee(db, next_action_assigned_to, required=False) or cur["next_action_assigned_to"]
    resolved_needs_followup = (int(needs_followup) if needs_followup is not None
                               else cur["needs_claude_followup"])

    # An approval that still needs follow-up goes back to Claude, overriding any -AssignedTo.
    if checked_action == "approved" and resolved_needs_followup:
        resolved_assignee = "Claude"

    # D25: approval is an authority check -- only the party ready_for_approval assigned the item to
    # may approve or note a decision_required item (#851 for noted). self_correctable items close
    # through resolve_self_correctable().
    if checked_action in ("approved", "noted") and cur["resolution_kind"] == "decision_required":
        rfa_assigned_to = _last_next_action_assigned_to(db, escalation_id, "ready_for_approval")
        if rfa_assigned_to and who != rfa_assigned_to:
            return (f"escalation #{escalation_id}: {who} cannot set {checked_action!r} -- "
                   f"'ready_for_approval' assigned this to {rfa_assigned_to!r}; only "
                   f"{rfa_assigned_to} may close it (authority check, not identity -- D25).")

    if checked_action == "ready_for_approval":
        _check_requirements(db, "ready_for_approval", originator=who, checked_action=checked_action,
                            values={"resolution": new_resolution,
                                    "next_action_assigned_to": resolved_assignee},
                            self_id=escalation_id)
    if checked_action == "approved":
        _check_requirements(db, "approved", originator=who, checked_action=checked_action,
                            values={"resolution": new_resolution}, self_id=escalation_id)
    if checked_action == "noted":
        _check_requirements(db, "noted", originator=who, checked_action=checked_action,
                            values={}, self_id=escalation_id)
    if checked_action == "reject":
        _check_requirements(db, "reject", originator=who, checked_action=checked_action,
                            values={"state": state, "type": cur["type"],
                                    "superseded_by": superseded_by})
    if checked_action == "revise":
        _check_requirements(db, "revise", originator=who, checked_action=checked_action,
                            values={"tried": tried})

    # thread items and responses: written before the state is derived, in the same transaction,
    # so the transition rows and the T6 check see this call's changes.
    is_thread = cur["type"] == "thread"
    thread_facts, item_summary = None, []
    succ_lines: list[str] = []          # what a supersede did on the successor thread
    if (add_items or item_refs or respond or response_kind or superseded_by) and not is_thread:
        raise ValueError("-Item/-AddItem/-Respond/-ResponseKind/-SupersededBy are for type thread "
                         "only")
    if superseded_by and not (checked_action == "reject" and state == "supersede"):
        raise ValueError("-SupersededBy goes with -NextAction reject -State supersede")
    if is_thread:
        if (item_refs or respond or response_kind) and not (item_refs and respond and response_kind):
            raise ValueError("an item response needs all three: -Item, -ResponseKind and -Respond "
                             "(a response about the whole thread is a plain -Comment)")
        if response_kind == "forward" and not add_items:
            raise ValueError("a forward response adds the forward mark as a new item: give "
                             "-AddItem kind:value (e.g. cluster:M03) with it")
        via_id = resolve_id(db, via) if via is not None else None
        now = _now()
        targets = [_resolve_item(db, cur, r) for r in item_refs or []]
        for it in targets:
            _respond(cfg, db, it, response_kind, respond, via=via_id, by=who, files=files, at=now)
            item_summary.append(f"item {it['item_no']} ({it['kind']}:{it['value']}) "
                                f"{response_kind}")
        for kind, value, note in add_items or []:
            new_item = _add_item(cfg, db, escalation_id, kind, value, note, opened_by=via_id, at=now)
            item_summary.append(f"item {new_item['item_no']} {kind}:{value} added")
        if checked_action == "reject":
            item_summary += _settle_thread_on_reject(cfg, db, cur, state, superseded_by,
                                                     reason=comment, who=who, at=now,
                                                     succ_lines=succ_lines)
        changed = bool(add_items) or response_kind in _SETTLE_KINDS + ("reopened",)
        thread_facts = _thread_facts(db, escalation_id, items_changed=changed,
                                     closed_some=response_kind in _SETTLE_KINDS)
        if item_summary:
            # the response itself, in full, to history
            line = (f"{cur['alias'] or '#' + str(escalation_id)}: " + "; ".join(item_summary)
                    + (f" (via #{via_id})" if via_id else ""))
            if respond:
                line += f" -- {response_kind} by {who}: {respond}"
                if files:
                    line += f" [files: {', '.join(files)}]"
            comment = f"{comment}\n{line}" if comment else line

    assignee_changed = bool(next_action_assigned_to) and next_action_assigned_to != cur["next_action_assigned_to"]
    new_state = _evaluate_transition(db, "manual", checked_action, has_resolution=bool(new_resolution),
                                     assignee_changed=assignee_changed, explicit_state=state,
                                     cur_state=cur["state"], needs_followup=bool(resolved_needs_followup),
                                     cur_next_action=cur["next_action"], thread=thread_facts)

    if (is_thread and new_state == "completed" and thread_facts and thread_facts["all_settled"]
            and not new_resolution):                        # last item settled
        resolution = new_resolution = _thread_completion_resolution(db, cur)

    # D26: comment/context/tried cannot land on a `raised` item (check_kind not_raised_with_content)
    _check_requirements(db, "update", originator=who, checked_action=checked_action,
                        values={"state": new_state, "comment": comment, "context": context,
                               "tried": tried, "next_action": next_action,
                               "next_action_assigned_to": resolved_assignee,
                               "type": cur["type"]},
                        self_id=escalation_id)

    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"comment": comment, "context": context, "tried": tried,
                              "resolution": resolution, "comes_back_when": comes_back_when},
                       envelope={
                           "next_action": checked_action if checked_action is not None else cur["next_action"],
                           "next_action_assigned_to": resolved_assignee,
                           "state": _check_state(db, new_state),
                           "resolution_kind": cur["resolution_kind"],
                           "needs_claude_followup": resolved_needs_followup},
                       originator=who)
    msg = (f"escalation #{escalation_id} v{merged['version']} -> "
           f"state={new_state!r}, next_action={merged['next_action']!r}, "
           f"assigned_to={merged['next_action_assigned_to']!r}")
    if item_summary:
        msg += "\n  " + "; ".join(item_summary)
    if not is_thread:
        synced = _sync_threads_for(cfg, db, escalation_id, who=who)
        if synced:
            msg += "\n  threads: " + "; ".join(synced)
    elif superseded_by:
        succ = _current(db, resolve_id(db, superseded_by))
        st = _restate_thread(cfg, db, succ["id"],
                             f"{succ['alias']}: received the open items of "
                             f"{cur['alias'] or '#' + str(escalation_id)}, superseded by {who}: "
                             f"{comment}"
                             + (f"\n{succ['alias']}: " + "; ".join(succ_lines) if succ_lines
                                else ""), who=who, closed_some=False)
        msg += f"\n  successor {succ['alias']} (#{succ['id']}) -> {st}"
    return msg


def correction(cfg: Cfg, db: Db, escalation_id: int, *, short_description: str | None = None,
              comment: str | None = None, context: str | None = None, tried: str | None = None,
              resolution: str | None = None,
              state: str | None = None, next_action: str | None = None,
              next_action_assigned_to: str | None = None,
              originator: str) -> str:
    """Correction -- ERROR CORRECTION ONLY (#774), never a workflow action: fix something already
    recorded wrong (a bad title, a typo). Works on any item in any state, dispatcher-tied included
    (#867), and can set short_description (still title-shape checked). state/next_action are taken
    exactly as given, never derived, and carry forward when omitted. The D25 authority check and
    the D26 raised-state guard do not apply."""
    cur = _current(db, escalation_id)
    who = _check_assignee(db, originator)

    if short_description is not None:
        title_error = _title_shape_error(short_description)
        if title_error:
            raise ValueError(title_error)

    resolved_state = _check_state(db, state) if state is not None else cur["state"]
    resolved_next_action = (_check_next_action_manual(db, next_action) if next_action is not None
                            else cur["next_action"])
    resolved_assigned_to = (_check_assignee(db, next_action_assigned_to, required=False)
                            or cur["next_action_assigned_to"])

    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"comment": comment, "context": context, "tried": tried,
                              "resolution": resolution, "short_description": short_description},
                       envelope={"state": resolved_state, "next_action": resolved_next_action,
                                "next_action_assigned_to": resolved_assigned_to,
                                "resolution_kind": cur["resolution_kind"],
                                "needs_claude_followup": cur["needs_claude_followup"]},
                       originator=who)
    synced = _sync_threads_for(cfg, db, escalation_id, who=who)
    return (f"escalation #{escalation_id} v{merged['version']} CORRECTED -> "
           f"state={resolved_state!r}, next_action={resolved_next_action!r}, "
           f"assigned_to={resolved_assigned_to!r}"
           + ("\n  threads: " + "; ".join(synced) if synced else ""))


# ── resolution_kind transactions ─────────────────────────────────────────────────────────────
def resolve_self_correctable(cfg: Cfg, db: Db, escalation_id: int, resolution: str,
                             *, originator: str) -> str:
    """Closes a `self_correctable` escalation: Claude states what was wrong and what changed
    (`resolution`, required). No approval vocabulary, no AnswerRun."""
    cur = _current(db, escalation_id)
    if cur["resolution_kind"] != "self_correctable":
        raise ValueError(f"escalation #{escalation_id} is not self_correctable "
                        f"(resolution_kind={cur['resolution_kind']!r}) -- use Update/AnswerRun "
                        f"instead, or escalate_to_decision() if it turned out to need one")
    if not resolution:
        raise ValueError("resolution is required -- state what was wrong and what changed")
    who = _check_assignee(db, originator)
    # type + landing state, so the T6 row can refuse a thread with open items
    _check_requirements(db, "resolve_self_correctable", originator=who, checked_action=None,
                        values={"type": cur["type"], "state": "completed"}, self_id=escalation_id)
    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"resolution": resolution},
                       envelope={"state": _check_state(db, "completed"), "next_action": None,
                                "next_action_assigned_to": cur["next_action_assigned_to"],
                                "resolution_kind": "self_correctable",
                                "needs_claude_followup": cur["needs_claude_followup"]},
                       originator=who)
    msg = f"escalation #{escalation_id} v{merged['version']} resolved (self_correctable) -> completed"
    synced = _sync_threads_for(cfg, db, escalation_id, who=who)
    return msg + ("\n  threads: " + "; ".join(synced) if synced else "")


def escalate_to_decision(cfg: Cfg, db: Db, escalation_id: int, tried: str,
                         *, originator: str) -> str:
    """Converts a `self_correctable` escalation to `decision_required` when a fix attempt shows a
    real decision is needed. `tried` (what was attempted) is required. `type` does not change."""
    cur = _current(db, escalation_id)
    if cur["resolution_kind"] != "self_correctable":
        raise ValueError(f"escalation #{escalation_id} is not self_correctable "
                        f"(resolution_kind={cur['resolution_kind']!r}) -- nothing to convert")
    if not tried:
        raise ValueError("tried is required -- describe what was attempted before converting to "
                        "decision_required")
    who = _check_assignee(db, originator)
    _check_requirements(db, "escalate_to_decision", originator=who, checked_action=None,
                        values={}, self_id=escalation_id)
    new_state = "in-progress" if cur["state"] == "raised" else cur["state"]
    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"tried": tried},
                       envelope={"state": _check_state(db, new_state), "next_action": "review",
                                "next_action_assigned_to": cur["next_action_assigned_to"],
                                "resolution_kind": "decision_required",
                                "needs_claude_followup": cur["needs_claude_followup"]},
                       originator=who)
    synced = _sync_threads_for(cfg, db, escalation_id, who=who)
    return (f"escalation #{escalation_id} v{merged['version']} converted to decision_required "
           f"(state={new_state!r})" + ("\n  threads: " + "; ".join(synced) if synced else ""))


# ── reports ───────────────────────────────────────────────────────────────────────────────────
def _gist(raw, width: int = 80) -> str:
    if not raw:
        return ""
    return str(raw).replace("\n", " ")[:width]




def write_list_report(cfg: Cfg, db: Db, path: pathlib.Path) -> tuple[pathlib.Path, list]:
    """Open items at their latest version only (state, next action, assignee, the latest comment and
    resolution in short); parked items one line each (#2206 option 4). Full history:
    `-Action History -Id n`. Threads get one short section instead: counts by state, then the
    in-progress threads only. `-Action Thread` lists them all."""
    open_s, parked_s = state_group(db, "open"), state_group(db, "parked")
    live = open_s + parked_s
    ph = ",".join("?" * len(live))
    rows = db.rows(f"SELECT * FROM escalation WHERE state IN ({ph}) AND type != 'thread' "
                   f"ORDER BY id", live)
    n_open = sum(1 for r in rows if r["state"] in open_s)
    n_parked = len(rows) - n_open
    objectives = cfg.required_setting("escalation.control_objectives")
    process = cfg.required_setting("escalation.control_process")
    L = ["# Open escalations", "",
        f"> {objectives}. {process}.".strip(), "",
        f"> Generated by `Escalation.ps1 -Action List`. {n_open} open ({', '.join(open_s)}), "
        f"{n_parked} parked ({', '.join(parked_s)}) -- state groups from cfg_enum "
        f"escalation_state_open/_parked (#2173 G1). Latest version only; full history: "
        f"`Escalation.ps1 -Action History -Id <id>`.", ""]
    if not rows:
        L.append("_no open escalations_")
    for r in (r for r in rows if r["state"] in open_s):
        last = db.rows("SELECT comment, answered_at FROM escalation_history WHERE escalation_id=? "
                       "AND version=?", (r["id"], r["version"]))
        L.append(f"## #{r['id']} v{r['version']} — {r['state']} — {r['short_description']}")
        L.append(f"type={r['type']} next_action={r['next_action'] or ''} "
                 f"assigned_to={r['next_action_assigned_to']} at={last[0]['answered_at'] if last else ''}")
        L.append("")
        if last and last[0]["comment"]:
            L.append(f"- latest comment: {_gist(last[0]['comment'], 300)}")
        if r["resolution"]:
            L.append(f"- resolution: {_gist(r['resolution'], 300)}")
        L.append("")
    parked = [r for r in rows if r["state"] not in open_s]
    if parked:
        L += ["## Parked", ""]
        L += [f"- #{r['id']} · {r['state']} · {r['short_description']}" for r in parked]
        L.append("")

    # ── threads ──
    counts = db.rows("SELECT state, COUNT(*) AS n FROM escalation WHERE type='thread' "
                     "GROUP BY state ORDER BY state")
    L += ["## Open threads", ""]
    if not counts:
        L += ["_no threads_", ""]
    else:
        L += ["Counts by state: " + ", ".join(f"{c['state']} {c['n']}" for c in counts)
              + ". Full list: `Escalation.ps1 -Action Thread`.", ""]
        live = db.rows("SELECT * FROM escalation WHERE type='thread' AND state='in-progress' "
                       "ORDER BY CAST(substr(alias, 4) AS INTEGER)")
        if not live:
            L += ["_no thread is in-progress (none is referenced by in-progress work)_", ""]
        else:
            L += ["In-progress (referenced by in-progress work; rule 4 counts these):", "",
                  "| thread | title | open items | referenced by |", "|---|---|---|---|"]
            for t in live:
                its = _thread_items(db, t["id"], "open")
                refs = ", ".join(i["value"] for i in its if i["kind"] == "escalation") or "--"
                L.append(f"| {t['alias']} · #{t['id']} | {t['short_description']} | {len(its)} | "
                         f"{refs} |")
            L.append("")

    # recently resolved items, with their title; closed notices carry their text in `comment`
    resolved = db.rows(
        "SELECT id, short_description, state, resolution, answered_at "
        f"FROM escalation WHERE state IN ({','.join('?' * len(state_group(db, 'terminal')))}) "
        "AND type != 'thread' ORDER BY answered_at DESC LIMIT 15", state_group(db, "terminal"))
    L += ["## Recently resolved (last 15)", ""]
    if not resolved:
        L.append("_none yet_")
    else:
        L += ["| # | short_description | state | resolution | answered |",
             "|---|---|---|---|---|"]
        for r in resolved:
            sd = str(r["short_description"]).replace("|", "\\|")
            res = str(r["resolution"]).replace("|", "\\|").replace("\n", " ") if r["resolution"] \
                else "_(see comment -- notice-type items can't carry a separate resolution)_"
            if len(res) > 200:
                res = res[:200] + "… (full text in escalation.resolution, id " + str(r["id"]) + ")"
            L.append(f"| {r['id']} | {sd} | {r['state']} | {res} | "
                     f"{r['answered_at']} |")

    out = reportkit.write_report(db.conn, "escalation.list", path, L)
    return out, rows


def write_history_report(cfg: Cfg, db: Db, escalation_id: int, path: pathlib.Path) -> pathlib.Path:
    """Deep-history report for one item: every version, envelope fields always, delta fields only
    where that version set them."""
    rows = db.rows("SELECT * FROM escalation WHERE id=?", (escalation_id,))
    if not rows:
        raise ValueError(f"no escalation #{escalation_id}")
    r = rows[0]
    hist = db.rows("SELECT * FROM escalation_history WHERE escalation_id=? ORDER BY version",
                   (escalation_id,))
    L = ["# Escalation deep history", "",
        f"## #{escalation_id} — {r['short_description']}",
        f"type={r['type']} source={r['source']}", ""]
    for h in hist:
        L.append(f"**v{h['version']}** ({h['answered_at']}, {h['originator'] or '?'}) "
                 f"state={h['state']} next_action={h['next_action'] or ''} "
                 f"assigned_to={h['next_action_assigned_to'] or ''}")
        for c in ("short_description", "comment", "context", "resolution", "tried"):
            if h[c]:
                label = c.replace("_", " ")
                L.append(f"> **{label} (set this version):** {h[c]}")
        L.append("")
    # `path`'s stem (id-prefixed by the caller) becomes the versioned {stem}-v{n}-{date}.md name
    return reportkit.write_report(db.conn, "escalation.history", path, L)


def _cell(text) -> str:
    """A markdown table cell: one line, pipes escaped."""
    if text is None:
        return ""
    return str(text).replace("\r", "").replace("\n", "<br>").replace("|", "\\|")


def _raised_in(context) -> str:
    try:
        ctx = json.loads(context) if context else {}
    except (ValueError, TypeError):
        return ""
    return ctx.get("raised_in", "") if isinstance(ctx, dict) else ""


def _latest_response(db: Db, item_id: int):
    rows = db.rows("SELECT * FROM escalation_thread_item_response WHERE item_id=? "
                   "ORDER BY responded_at DESC, id DESC LIMIT 1", (item_id,))
    return rows[0] if rows else None


def _item_line(db: Db, alias: str, it, latest: bool = True) -> str:
    s = f"{alias}.{it['item_no']} {it['kind']} {it['value']}"
    if it["note"]:
        s += f" ({it['note']})"
    s += f" -- {it['status']}"
    r = _latest_response(db, it["id"]) if latest else None
    if r:
        via = f", #{r['via_escalation']}" if r["via_escalation"] else ""
        s += f"; latest: {r['kind']} ({r['responded_at'][:10]}{via}): {r['text']}"
    return s


def write_thread_report(cfg: Cfg, db: Db, path: pathlib.Path, *, state: str | None = None,
                        ident=None) -> tuple[pathlib.Path, list[str]]:
    """`Escalation.ps1 -Action Thread`. Without `ident`: every open thread (on-hold and
    in-progress; `state` narrows to one), each with its open items. With `ident` (an id or OT-nn):
    that thread, every item with its responses in date order. Returns the path and console lines."""
    console: list[str] = []
    if ident is not None:
        t = _current(db, resolve_id(db, ident))
        if t["type"] != "thread":
            raise ValueError(f"#{t['id']} is type {t['type']!r}, not a thread")
        L = [f"# {t['alias']} · #{t['id']} -- {t['short_description']}", "",
             f"state={t['state']} · raised {t['raised_at'][:10]} · raised in: "
             f"{_raised_in(t['context']) or '--'}", "",
             f"**Comes back when:** {t['comes_back_when'] or '--'}", "",
             f"**Thread:** {t['comment'] or ''}", ""]
        if t["resolution"]:
            L += [f"**Resolution:** {t['resolution']}", ""]
        L += ["## Items", ""]
        for it in _thread_items(db, t["id"]):
            L.append(f"### {t['alias']}.{it['item_no']} {it['kind']} {it['value']} -- {it['status']}")
            meta = f"opened {it['opened_at'][:10]}"
            if it["opened_by"]:
                meta += f" under #{it['opened_by']}"
            L += [(f"{it['note']} · " if it["note"] else "") + meta, ""]
            for r in db.rows("SELECT * FROM escalation_thread_item_response WHERE item_id=? "
                             "ORDER BY responded_at, id", (it["id"],)):
                via = f", via #{r['via_escalation']}" if r["via_escalation"] else ""
                L.append(f"- **{r['kind']}** ({r['responded_at'][:10]}, {r['responded_by']}{via}): "
                         f"{r['text']}")
            L.append("")
            console.append(_item_line(db, t["alias"], it))
        if t["tried"]:
            L += ["## History before migration", "", t["tried"], ""]
        console.insert(0, f"{t['alias']} · #{t['id']} [{t['state']}] {t['short_description']}")
        out = reportkit.write_report(db.conn, "escalation.thread",
                                     path.with_name(f"{t['id']}-{path.name}"), L)
        return out, console

    states = (state,) if state else _THREAD_OPEN_STATES
    if state and state not in _THREAD_OPEN_STATES:
        raise ValueError(f"-State for -Action Thread is on-hold or in-progress, not {state!r}")
    ph = ",".join("?" * len(states))
    threads = db.rows(f"SELECT * FROM escalation WHERE type='thread' AND state IN ({ph}) "
                      f"ORDER BY CAST(substr(alias, 4) AS INTEGER)", states)
    L = ["# Open threads", "",
         f"> Generated by `Escalation.ps1 -Action Thread`{' -State ' + state if state else ''}. "
         f"{len(threads)} thread(s). One thread in full: `-Action Thread -Id OT-nn`.", "",
         "| thread | state | title | open items |", "|---|---|---|---|"]
    for t in threads:
        its = _thread_items(db, t["id"], "open")
        shown = "; ".join(f"{t['alias']}.{i['item_no']} {i['kind']}:{i['value']}" for i in its)
        if not its:
            shown = "_none open_"
        L.append(f"| {t['alias']} · #{t['id']} | {t['state']} | {_cell(t['short_description'])} | "
                 f"{_cell(shown)} |")
        console.append(f"{t['alias']:<7} #{t['id']} {t['state']:<11} {t['short_description']} "
                       f"({len(its)} open)")
    out = reportkit.write_report(db.conn, "escalation.thread", path, L)
    return out, console


def write_thread_register(cfg: Cfg, db: Db, path: pathlib.Path) -> tuple[pathlib.Path, int]:
    """Writes render_thread_register() to its path."""
    L, n = render_thread_register(cfg, db)
    out = reportkit.write_report(db.conn, "escalation.thread_export", path, L)
    return out, n


def render_thread_register(cfg: Cfg, db: Db) -> tuple[list[str], int]:
    """`Escalation.ps1 -Action Export -Type thread`: regenerates the open threads register from the
    escalation table -- every thread by OT number, `OT-nn · #id` in the id cell. The thread, raised
    and comes-back-when cells carry the stored text; the status cell is generated: state, each item
    with its latest response, then the register's earlier status text (`tried`)."""
    threads = db.rows("SELECT * FROM escalation WHERE type='thread' "
                      "ORDER BY CAST(substr(alias, 4) AS INTEGER)")
    by_state: dict[str, int] = {}
    for t in threads:
        by_state[t["state"]] = by_state.get(t["state"], 0) + 1
    rule = db.rows("SELECT rule_text FROM cfg_behaviour_rule WHERE "
                   "rule_key='open-threads-carried-as-escalations'")
    L = ["# Open threads register", "",
         "> **Generated** from the escalation table (type=thread) by `Escalation.ps1 -Action "
         "Export -Type thread`. Do not edit by hand: respond through `Escalation.ps1 -Action "
         "Update -Id OT-nn` (escalation #2000). The hand-kept register (2026-10-02 to "
         "2026-10-12) is frozen at `archive/open-threads-register-frozen-20261012.md`.", "",
         "**Set up:** 2026-10-02 (researcher: *\"I approve of the open threads register\"*, "
         "#1935). Carried in the escalation table from 2026-10-12 (#2000).", "",
         "**How it is used** (`cfg_behaviour_rule` open-threads-carried-as-escalations): "
         + (rule[0]["rule_text"] if rule else "--"), "",
         "**Threads:** " + ", ".join(f"{k} {v}" for k, v in sorted(by_state.items()))
         + f" ({len(threads)} in all). Item references are `OT-nn.n`.", "",
         "| id | thread | raised | comes back when | status |", "| --- | --- | --- | --- | --- |"]
    for t in threads:
        parts = [f"**{t['state']}**"]
        if t["resolution"]:
            parts[0] += f": {t['resolution']}"
        parts += [_item_line(db, t["alias"], it) for it in _thread_items(db, t["id"])]
        if t["tried"]:
            parts.append(t["tried"])
        L.append(f"| {t['alias']} · #{t['id']} | {_cell(t['comment'])} | "
                 f"{_cell(_raised_in(t['context']))} | {_cell(t['comes_back_when'])} | "
                 f"{_cell(chr(10).join(parts))} |")
    return L, len(threads)


def _extract_flag(args: list[str], name: str) -> tuple[list[str], str | None]:
    prefix = f"--{name}="
    remaining, value = [], None
    for a in args:
        if a.startswith(prefix):
            value = a[len(prefix):]
        else:
            remaining.append(a)
    return remaining, value


def _extract_multi(args: list[str], name: str) -> tuple[list[str], list[str]]:
    """A repeatable --name=value flag (-Item, -AddItem, -Cluster, ...)."""
    prefix = f"--{name}="
    remaining, values = [], []
    for a in args:
        if a.startswith(prefix):
            values.append(a[len(prefix):])
        else:
            remaining.append(a)
    return remaining, values


def _files_arg(raw: list[str]) -> list[str] | None:
    return [f.strip() for f in raw if f.strip()] or None


# A sustained write lock from another process can outlast the 30s busy_timeout (#1708): the CLI
# retries only "database is locked", a few times, before falling through to crash recording.
_LOCK_RETRY_DELAYS = (1.0, 2.0, 4.0)  # seconds


def main() -> int:
    cfg = Cfg()
    db = Db(cfg)
    argv = sys.argv[1:]
    try:
        for attempt, delay in enumerate((0.0,) + _LOCK_RETRY_DELAYS):
            if delay:
                time.sleep(delay)
                db.conn.rollback()  # clear whatever partial state the failed attempt left
            try:
                return _dispatch(cfg, db, argv)
            except sqlite3.OperationalError as exc:
                if "database is locked" not in str(exc) or attempt == len(_LOCK_RETRY_DELAYS):
                    raise
                print(f"[retry] database is locked -- retrying ({attempt + 1}/"
                     f"{len(_LOCK_RETRY_DELAYS)})...", file=sys.stderr)
        raise AssertionError("unreachable")  # loop always returns or re-raises above
    except ValueError as exc:
        # a ValueError is a validation guard rejecting a malformed call: print it and exit non-zero,
        # no escalation. Only unanticipated exceptions (below) are recorded.
        db.conn.rollback()
        db.close()
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        import traceback
        tb = traceback.format_exc()
        db.conn.rollback()
        try:
            title, extra = _sanitise_dispatcher_title(f"escalation CLI crashed: {exc}",
                                                       {"argv": argv, "traceback": tb})
            raise_new(cfg, db, title, "iba.app.lib.escalation",
                     etype="run_error", comment=f"argv={argv!r}\n{tb}",
                     context=json.dumps(extra),
                     assigned_to="Claude",
                     resolution_kind="self_correctable",
                     originator="Claude")
        except Exception as record_exc:
            # never silently discard a failure in the recording path; the original crash still re-raises
            print(f"[WARN] failed to record crash escalation: {record_exc!r}", file=sys.stderr)
        db.close()
        raise


def _require_flag(value: str | None, name: str) -> str:
    if not value:
        raise ValueError(f"--{name}= is required -- no default (escalation rebuild 2026-08-20)")
    return value


def _dispatch(cfg: Cfg, db: Db, argv: list[str]) -> int:
    if len(argv) >= 1 and argv[0] == "list":
        path = pathlib.Path(cfg.required_setting("escalation.list_report_path"))
        out, rows = write_list_report(cfg, db, path)
        n_open = sum(1 for r in rows if r["state"] in state_group(db, "open"))
        print(f"  {n_open} open, {len(rows) - n_open} parked escalation(s) -> {out}")
    elif len(argv) >= 3 and argv[0] == "answer-run":
        rest, by = _extract_flag(argv[3:], "by")
        rest, resolution = _extract_flag(rest, "resolution")
        comment = " ".join(rest) or None
        print("  " + answer_for_run(cfg, db, argv[1], argv[2], comment,
                                    answered_by=_require_flag(by, "by"), resolution=resolution))
    elif len(argv) >= 2 and argv[0] == "raise":
        rest, source = _extract_flag(argv[1:], "source")
        rest, assigned_to = _extract_flag(rest, "assigned-to")
        rest, etype = _extract_flag(rest, "type")
        rest, originator = _extract_flag(rest, "originator")
        rest, comment = _extract_flag(rest, "comment")
        rest, context = _extract_flag(rest, "context")
        rest, resolution_kind = _extract_flag(rest, "resolution-kind")
        rest, needs_followup = _extract_flag(rest, "needs-followup")
        rest, state = _extract_flag(rest, "state")                       # escalation #2000 T2
        rest, comes_back_when = _extract_flag(rest, "comes-back-when")
        rest, item_specs = _extract_multi(rest, "item")
        question = " ".join(rest)
        etype = etype or "task"
        new_id = raise_new(cfg, db, question, source or "claude", etype=etype,
                           comment=comment or question, context=context,
                           assigned_to=assigned_to or ("Claude" if etype == "thread" else "Researcher"),
                           resolution_kind=resolution_kind,
                           needs_followup=needs_followup in ("1", "true"),
                           originator=_require_flag(originator, "originator"),
                           state=state, comes_back_when=comes_back_when,
                           items=[parse_item_spec(s) for s in item_specs] or None)
        alias = _current(db, new_id)["alias"]
        print(f"  raised — #{new_id}{' (' + alias + ')' if alias else ''}. Update with: "
              f"Escalation.ps1 -Action Update -Id {alias or new_id} ...")
    elif len(argv) >= 2 and argv[0] == "resolve-self-correctable":
        rest, resolution = _extract_flag(argv[2:], "resolution")
        rest, originator = _extract_flag(rest, "originator")
        print("  " + resolve_self_correctable(cfg, db, resolve_id(db, argv[1]),
                                              _require_flag(resolution, "resolution"),
                                              originator=_require_flag(originator, "originator")))
    elif len(argv) >= 2 and argv[0] == "escalate-to-decision":
        rest, tried = _extract_flag(argv[2:], "tried")
        rest, originator = _extract_flag(rest, "originator")
        print("  " + escalate_to_decision(cfg, db, resolve_id(db, argv[1]),
                                          _require_flag(tried, "tried"),
                                          originator=_require_flag(originator, "originator")))
    elif len(argv) >= 1 and argv[0] == "match":                          # escalation #2000 T1
        rest, for_ref = _extract_flag(argv[1:], "for")
        rest, originator = _extract_flag(rest, "originator")
        rest, clusters = _extract_multi(rest, "cluster")
        rest, strongs = _extract_multi(rest, "strong")
        rest, verses = _extract_multi(rest, "verse")
        lines = match_threads(cfg, db, clusters=clusters, strongs=strongs, verses=verses,
                              for_ref=for_ref,
                              who=_require_flag(originator, "originator") if for_ref else None)
        print(f"  {len(lines)} thread(s) matched" + (" (read-only: no -For)" if not for_ref else ""))
        for line in lines:
            print("  " + line)
    elif len(argv) >= 1 and argv[0] == "thread-check":                   # escalation #2000 T5
        rest, originator = _extract_flag(argv[1:], "originator")
        lines = thread_check(cfg, db, who=_require_flag(originator, "originator"))
        print(f"  thread check: {len(lines)} thread change(s)")
        for line in lines:
            print("  " + line)
    elif len(argv) >= 2 and argv[0] == "update":
        rest, next_action = _extract_flag(argv[2:], "next-action")
        rest, assigned_to = _extract_flag(rest, "assigned-to")
        rest, state = _extract_flag(rest, "state")
        rest, resolution = _extract_flag(rest, "resolution")
        rest, tried = _extract_flag(rest, "tried")
        rest, originator = _extract_flag(rest, "originator")
        rest, context = _extract_flag(rest, "context")
        rest, needs_followup_raw = _extract_flag(rest, "needs-followup")
        needs_followup = None if needs_followup_raw is None else needs_followup_raw in ("1", "true")
        rest, comes_back_when = _extract_flag(rest, "comes-back-when")   # escalation #2000
        rest, add_specs = _extract_multi(rest, "add-item")
        rest, item_refs = _extract_multi(rest, "item")
        rest, respond = _extract_flag(rest, "respond")
        rest, response_kind = _extract_flag(rest, "response-kind")
        rest, via = _extract_flag(rest, "via")
        rest, files = _extract_multi(rest, "file")
        rest, superseded_by = _extract_flag(rest, "superseded-by")      # #2000 lifecycle
        comment = " ".join(rest) or None
        print("  " + update(cfg, db, resolve_id(db, argv[1]), next_action=next_action,
                            next_action_assigned_to=assigned_to, comment=comment, context=context,
                            tried=tried, resolution=resolution,
                            state=state,
                            needs_followup=needs_followup,
                            originator=_require_flag(originator, "originator"),
                            comes_back_when=comes_back_when,
                            add_items=[parse_item_spec(s) for s in add_specs] or None,
                            item_refs=item_refs or None, respond=respond,
                            response_kind=response_kind, via=via, files=_files_arg(files),
                            superseded_by=superseded_by))
    elif len(argv) >= 2 and argv[0] == "history":
        eid = resolve_id(db, argv[1])
        path = pathlib.Path(cfg.required_setting("escalation.history_report_dir")) / f"{eid}-escalation-history.md"
        out = write_history_report(cfg, db, eid, path)
        print(f"  -> {out}")
    elif len(argv) >= 2 and argv[0] == "correction":
        rest, next_action = _extract_flag(argv[2:], "next-action")
        rest, assigned_to = _extract_flag(rest, "assigned-to")
        rest, state = _extract_flag(rest, "state")
        rest, resolution = _extract_flag(rest, "resolution")
        rest, tried = _extract_flag(rest, "tried")
        rest, originator = _extract_flag(rest, "originator")
        rest, context = _extract_flag(rest, "context")
        rest, short_description = _extract_flag(rest, "short-description")
        comment = " ".join(rest) or None
        print("  " + correction(cfg, db, resolve_id(db, argv[1]), short_description=short_description,
                                next_action=next_action, next_action_assigned_to=assigned_to,
                                comment=comment, context=context, tried=tried,
                                resolution=resolution,
                                state=state,
                                originator=_require_flag(originator, "originator")))
    else:
        print("usage: python -m iba.app.lib.escalation list"
             " | history <id>"
             " | answer-run <run_id> <approve|reject|revise|hold|noted> --by=Claude|Researcher "
             "[--resolution=...] [comment...]"
             " | raise <short_description...> --comment=... --originator=Claude|Researcher "
             "[--source=...] [--assigned-to=...] [--type=...] "
             "[--context=...] [--needs-followup=1]"
             " | update <id> --originator=Claude|Researcher [--next-action=...] [--assigned-to=...] "
             "[--state=...] [--resolution=...] [--tried=...] "
             "[--context=...] [--needs-followup=1|0] [comment...]"
             " | correction <id> --originator=Claude|Researcher — ERROR CORRECTION ONLY, works in "
             "any state, unlike update: [--short-description=...] [--next-action=...] "
             "[--assigned-to=...] [--state=...] [--resolution=...] "
             "[--tried=...] [--context=...] [comment...]"
             " | match [--for=<id|OT-nn>] [--cluster=M10]... [--strong=H5782]... "
             "[--verse='Rom 7:15']... [--originator=... (with --for)]"
             " | thread-check --originator=Claude|Researcher"
             " -- threads (escalation #2000): raise --type=thread --state=on-hold "
             "--comes-back-when=... --item='kind:value[ :: note]'...; update <id|OT-nn> "
             "[--item=OT-16.1 --response-kind=closed --respond=... --via=1998 --file=path...] "
             "[--add-item=kind:value...] [--comes-back-when=...]")
    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
