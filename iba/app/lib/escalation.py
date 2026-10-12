"""escalation.py — util.escalation.

**D14/D15 RETIRED 2026-08-27, escalation #909.** `from_id` and `related_activity` are both gone —
not deprecated, not unenforced, removed: neither column exists on `escalation`/
`escalation_history` any more, and every check/report section built on them (the pairing
requirement, `_link_graph`/cycle/dangling/mismatched-pairing/missing-link/incoherent-link, the
list report's group-by, the history report's relationship-walk) is deleted, not merely
unreachable. The researcher's own instruction named both columns together, not just the graph
mechanism on top of one of them — a half-measure (keep the free-text field, drop only the
enforcement) would have been exactly the "smoke and mirrors" the instruction explicitly rejected.
Researcher, verbatim, after two live audits this session found the mechanism was unreliable and
never actually used
(`iba/app/reports/related-activity-summary-mockup-20260826.md`,
`iba/app/reports/from-id-data-quality-audit-20260826.md`, on top of escalation #768's own 10-round
closure, `GOVERNANCE.md` §56): *"the related-activity and fromid columns in the table is
unreliable, and does not serve a purpose, and is very confusing and distracting in the history
report. I dont think you can solve the problem, and I dont think it is worth it, because you in
any case are not using it. so scrap it."* Full removal record: `GOVERNANCE.md` §57.

util.escalation. The authoritative record of open items in the project: errors,
issues, and building tasks. NOT a run-logging mechanism — a standard operational routine (run
through an already-approved app PS script) is logged by the engine (`run.state`/`resume_point`/
`outcome`) and escalates only on genuine error. A DEVELOPMENT/DESIGN control — anything that
changes the app's own behaviour, above all a `configmaint.propose` config write — keeps a real,
gated approval here.

**Full rebuild, 2026-08-20** (full design: `iba/docs/escalation-rebuild-design-v1-20260820.md`).
The redesign that preceded this (2026-08-19/20, `escalation-redesign-plan-v3-20260819.md`) fixed
the loss-of-history bug (#715) correctly but shipped with no config representation for any of its
own validate/complete rules, and its `escalation_history` rows stored full cumulative snapshots
instead of per-version deltas — both found, in one session, alongside a chain of smaller defects
(a title-shape violation, ≥39 originator misattributions from a silent default, two `cfg_escalation`
rows naming a function that no longer existed). Researcher: *"the system is not ready for
production ... export the data ... delete all the records ... go back and do a proper design and
implementation."* Both tables were exported (`iba/app/db/archive/escalation{,_history}-export-
20260820.json`) and emptied before this rewrite.

**What actually changed** (§1 of the design doc has the full before/after table):
  - `escalation_history`'s content fields (`comment`/`context`/`resolution`/`tried`/
    `short_description`/`related_activity`) are now TRUE DELTAS — `NULL` unless this transaction
    actually set them. `escalation`'s own fields are unchanged: still the cumulative/current state.
  - State-derivation is now a config-driven rule engine (`cfg_escalation_transition`), evaluated
    in priority order, not a hardcoded `if`/`elif` chain — see `_evaluate_transition()`.
  - Field-requirement rules are config-driven too (`cfg_escalation_requirement`) — see
    `_check_requirements()`.
  - `originator` has NO default anywhere, in this file or in `Escalation.ps1` — every caller must
    say who they are. The old `"Researcher"` default was the actual root cause of the
    misattribution bug.
  - Two-stage approval (`ready_for_approval` → `approved`) now checks the two parties differ.
  - `escalation_next_action` (the old merged cfg_enum) is retired; the dispatcher and manual
    shapes each validate against their own group (`escalation_next_action_dispatcher` /
    `_manual`), closing the vocabulary-leak gap the merged enum had.

**Two shapes, deliberately not unified** (unchanged from the prior redesign, still correct):
  - **dispatcher-tied** (`run_id` set) — a real pipeline pause. `raise_()` / `pending_for_run()` /
    `answered_for_run()` / `answer_for_run()`.
  - **manual** (`run_id` is `MANUAL-...`) — the researcher/Claude backlog workflow. `raise_new()` /
    `update()`.

Both write through the SAME snapshot mechanism (`_snapshot()`), so both get real (now correctly
delta-shaped) history for free.

**Register v9 build, 2026-08-21** (`iba/docs/escalation-design-plan-v5-20260821.md` +
`iba/docs/escalation-design-decision-register-v9-20260821.md`, both narrated D1-D28):
  - D12: `raise_new()` now special-cases `type='notice'` at creation (`state='closed'`,
    `next_action=None`, no review/decision cycle) -- every other type still defaults
    `state='raised'`/`next_action='review'`.
  - D14 (RETIRED 2026-08-27, escalation #909 -- see the banner at the top of this docstring):
    was a `from_id` column + `related_activity` pairing check. Removed entirely, not just
    unenforced -- see the retirement note below.
  - D25: two-stage approval is now an AUTHORITY check, not an identity check -- `approved` is
    refused only if the caller differs from whoever `ready_for_approval` assigned the item to (the
    old same-party refusal wrongly blocked legitimate self-authorisation).
  - D26: `update()` refuses to attach `comment`/`context`/`tried` while the resulting state would
    still be `raised` -- work has to be explicitly moved off `raised` first
    (`cfg_escalation_requirement`, `check_kind='not_raised_with_content'`).
  - D27 (config only, `cfg_escalation_transition`): `ready_for_approval` now has its own explicit
    transition row, rather than relying on the incidental `assignee_changed` rule.
  - `cfg_escalation_requirement` gained a `check_kind` column (`field_required` — the pre-existing
    implicit behaviour, now named — plus `not_raised_with_content` (`exists`/`not_self` were D14's
    own, retired with it, escalation #909)).

CLI (module path: iba.app.lib.escalation, invoked as `python -m iba.app.lib.escalation`):
    python -m iba.app.lib.escalation list
    python -m iba.app.lib.escalation answer-run <run_id> <approve|reject|revise|hold|noted>
        --by=Claude|Researcher [--resolution=...] [comment words...]
    python -m iba.app.lib.escalation raise <question...>
        --originator=Claude|Researcher [--source=claude|researcher] [--assigned-to=Claude|Researcher]
        [--type=task|...] --comment=...
        --resolution-kind=decision_required|self_correctable
        [--needs-followup=1] — set when finishing this item needs a further Claude action AFTER
        approval (escalation #1075): approved then routes back to Claude, not straight to completed.
    python -m iba.app.lib.escalation resolve-self-correctable <id> --originator=Claude
        --resolution=... — closes a self_correctable item. No AnswerRun, no decision vocabulary
        (escalation #798/#799): Claude fixes it, states the resolution, done.
    python -m iba.app.lib.escalation escalate-to-decision <id> --originator=Claude --tried=...
        — converts a self_correctable item to decision_required when a fix attempt reveals a real
        decision is needed (`tried`'s original purpose). Does not change `type`.
    python -m iba.app.lib.escalation update <id> --originator=Claude|Researcher
        [--next-action=...] [--assigned-to=...] [--state=on-hold|in-progress|closed|withdraw|supersede]
        [--resolution=...] [--tried=...]
        [--needs-followup=1|0] — set/clear the followup flag (escalation #1075); omit to carry the
        item's current value forward unchanged.
        [comment/context words...]
    python -m iba.app.lib.escalation correction <id> --originator=Claude|Researcher
        [--short-description=...] [--next-action=...] [--assigned-to=...] [--state=...]
        [--resolution=...] [--tried=...]
        [comment/context words...]
        — ★ ERROR CORRECTION ONLY (escalation #774) — a copy of Update that works on ANY item state
        (closed/completed included, unlike Update) and can touch short_description (which Update
        never exposes). Not a workflow action: state/next_action are taken exactly as given, never
        auto-derived, and carry forward unchanged if omitted. Use Update for every ordinary change;
        use Correction only to fix something already recorded wrong.

`--originator`/`--by` are now REQUIRED on every write verb — no default, see above.

**Threads, escalation #2000 (2026-10-12)** -- the open threads register carried in this table as
type='thread' (alias OT-nn). Design: `_analytics/cross-cluster-web/open-threads-table-proposal-v3-
20261012.md`; rules T0-T9 in config (see the THREADS section below). Child tables
`escalation_thread_item` (current status only) and `escalation_thread_item_response` (every
response, each completion included). New verbs: `match` (T1) and `thread-check` (T5); `raise`
gains --state (T2, manual raise only -- `raise_()` keeps 'raised'), --comes-back-when and
repeatable --item; `update` gains --item/--response-kind/--respond/--via/--file and --add-item;
every <id> also takes the alias. Reports (dispatched through run.py): `write_thread_report`
(-Action Thread) and `write_thread_register` (-Action Export -Type thread).
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

_OPEN_STATES = ("raised", "re-assigned", "on-hold", "in-progress")
_TERMINAL_STATES = ("completed", "closed", "withdraw", "supersede")
_THREAD_OPEN_STATES = ("on-hold", "in-progress")    # a thread never sits at raised (T2)

# every business column on `escalation` / `escalation_history` (id/version/escalation_id excluded
# -- those are structural, not part of a snapshot's business content)
# D14/D15 RETIRED 2026-08-27 (escalation #909): from_id and related_activity both removed from
# these tuples (and from the tables themselves) -- see the module docstring's retirement banner.
# escalation #2000 (2026-10-12): `alias` (OT-nn, threads only) is immutable like type/raised_at;
# `comes_back_when` is a replace column like tried/resolution.
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
    """Returns an error message if `short_description` violates the title-shape spec (escalation
    #759 -- 'a short description of item, like a title', <=60 chars, no embedded clause-stitching)
    -- else None."""
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
    """cfg_status_flow lookup for entity='escalation' -- same pattern handlers/registry.py uses
    for entity='word'. `fallback` is only hit if the row is somehow missing post-rebuild (defensive,
    should not happen -- every key used below has a seeded row, see migration/
    rebuild_escalation_rules_config_20260820.py)."""
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
    """The fixed, small vocabulary cfg_escalation_transition.condition_key draws from -- see
    escalation-rebuild-design-v1-20260820.md sec2.4. A new condition needs a code change here
    (a new named boolean); which RULE consumes it, in what priority, with what resulting status,
    is config from that point on.

    `thread` (escalation #2000) is None for every non-thread item, so the two thread conditions
    are always false for them (so is thread_reassigned, #2000 D1). For a thread it carries: items_changed (an item added, closed or
    reopened this call, or the state of the work an 'escalation' item references changed),
    closed_some (an item closed this call), open_remaining (open items after this call) and
    referenced (an open 'escalation' item points at a task/issue at state in-progress)."""
    if condition_key == "always":
        return True
    if condition_key == "thread_items_changed_and_referenced":          # T3/T5
        return bool(thread and thread["items_changed"] and thread["referenced"])
    if condition_key == "thread_items_changed_partly_closed":           # T6, partial completion
        return bool(thread and thread["closed_some"] and thread["open_remaining"]
                    and not thread["referenced"])
    if condition_key == "has_resolution":
        return bool(has_resolution)
    if condition_key == "thread_items_all_settled":           # #2000 lifecycle: the last open
        return bool(thread and thread["items_changed"]         # item settled this call -> the
                    and thread["all_settled"]                  # thread completes. Never on
                    and next_action != "reject")               # reject: withdraw/supersede of a
                                                                # thread settles its items itself
    if condition_key == "thread_reassigned":                  # escalation #2000 D1 (researcher:
        return bool(thread is not None and assignee_changed)   # "go with option a"): reassigning a
                                                                # thread keeps its state -- it never
                                                                # lands on re-assigned, outside the
                                                                # thread open states
    if condition_key == "assignee_changed":
        return bool(assignee_changed)
    if condition_key == "explicit_state_given":               # found live 2026-08-21 (#762): an
        return bool(has_explicit_state)                        # explicit -State must outrank the
                                                                # assignee_changed inference, not
                                                                # lose to it -- see priority 6 below
    if condition_key == "needs_followup":                      # escalation #1075, 2026-08-30: an
        return bool(needs_followup)                            # 'approved' item still flagged
                                                                # needs_claude_followup routes back
                                                                # to Claude, not straight to
                                                                # completed -- checked ahead of the
                                                                # plain has_resolution rule.
    if condition_key == "followup_cleared_was_approved":
        # Researcher, 2026-08-31, found live: clearing needs_claude_followup (Claude reporting the
        # approved write is actually applied) never reached completed on its own -- the priority
        # 1/2 'approved' rules above only fire when the CALLER re-supplies -NextAction approved
        # THIS call, which a bare -NeedsFollowup 0 call never does, so it fell through to the
        # generic reassignment rule (priority 7) instead, landing on re-assigned for an unrelated
        # reason. And since decision_required_approval_requires_researcher (this same session)
        # now blocks Claude from ever re-supplying -NextAction approved itself, there was no path
        # to completed left at all except the researcher re-running the whole approve handshake a
        # second time, for a decision already made -- friction with no control value. This
        # recognises "already approved, resolution on file, follow-up now done" as itself
        # sufficient: no NEW decision is being made, just the existing one finishing.
        return not needs_followup and has_resolution and cur_next_action == "approved"
    raise ValueError(f"unknown cfg_escalation_transition.condition_key {condition_key!r}")


def _evaluate_transition(db: Db, shape: str, next_action: str | None, *, has_resolution: bool,
                         assignee_changed: bool, explicit_state: str | None,
                         cur_state: str, needs_followup: bool = False,
                         cur_next_action: str | None = None, thread: dict | None = None) -> str:
    """Reads cfg_escalation_transition for `shape`, in priority order, first match wins -- replaces
    the old hardcoded if/elif chain. `resulting_status_key` of `__explicit__` means the reject
    branch: state comes from the caller's own choice, validated here (withdraw|supersede only).
    `__unchanged__` means no rule truly fires: state carries forward (or the caller's -State).

    D-fix 2026-08-21 (#762): the caller's own explicit -State must outrank an INFERRED
    assignee_changed result -- `-AssignedTo Researcher -State on-hold` was silently landing on
    `re-assigned` (assignee_changed's rule fired first, matching next_action=None the same way the
    catch-all does, but at an earlier priority) with no way to combine an explicit state with a
    reassignment. cfg_escalation_transition priority 6 (condition_key='explicit_state_given') now
    sits ahead of assignee_changed (shifted to 7) for exactly this."""
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
    if condition_key == "thread_superseding":                  # #2000 lifecycle: a thread
        return values.get("type") == "thread" and values.get("state") == "supersede"
    raise ValueError(f"unknown cfg_escalation_requirement.condition_key {condition_key!r}")


def _check_requirements(db: Db, action: str, *, originator: str, checked_action: str | None,
                        values: dict, self_id: int | None = None) -> None:
    """Raises ValueError on the first unmet requirement. `values` = the field->value the caller is
    actually supplying this transaction (already-merged where relevant, e.g. resolution). `check_kind`
    (register v9 D25/D26 -- column added alongside these rules, previously only 'field_required'
    existed implicitly) selects which comparison runs. `self_id` is the item's own id (None at
    Raise -- the new id does not exist yet)."""
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
            # escalation #851, 2026-08-26: the D25 authority check alone is vacuous when no prior
            # ready_for_approval transition exists at all -- exactly how #865 was self-approved, and
            # would still be true of 'noted' even after D25 was extended to cover it. This makes the
            # SEQUENCE itself required for decision_required items, not just an opportunistic
            # comparison against whichever prior transition happens to exist.
            #
            # TIGHTENED 2026-08-31, researcher direct correction: the original check (renamed from
            # requires_PRIOR_ready_for_approval_if_decision_required) only checked that a
            # ready_for_approval transition existed SOMEWHERE in escalation_history, ever -- not
            # that it's where the item currently sits. So `ready_for_approval -> revise ->
            # in-progress -> approved` would have passed: a ready_for_approval happened once, long
            # ago, satisfying the old check, even though the item had since moved away from it.
            # Researcher, verbatim: "approval should not be able to be in any other state that
            # ready for approval" (decision_required only -- explicitly excluded self_correctable,
            # which never uses this vocabulary anyway). Now checks the item's CURRENT next_action
            # directly, not history.
            if self_id is not None:
                row = db.rows("SELECT resolution_kind, next_action FROM escalation WHERE id=?",
                              (self_id,))
                if (row and row[0]["resolution_kind"] == "decision_required"
                        and row[0]["next_action"] != "ready_for_approval"):
                    raise ValueError(r["message"])
        elif kind == "actor_must_be_assignee":
            # researcher, 2026-08-31 morning: "the code should have a blocker that the party
            # processing an item (answered_by) must be the assigned_to." Built same day, wired
            # into update()/resolve_self_correctable()/escalate_to_decision() via
            # cfg_escalation_requirement rows (action IN those three, check_kind=this).
            #
            # WALKED BACK same day, evening, researcher's own words: "the objective of
            # actor_must_be_assignee is to prevent you to do what you like. but I also see that it
            # is now preventing you from acting on a chat, and requires me to put all notes through
            # the difficult to use escalation excel tool. so the two objectives works against each
            # other... escalation activities are now consuming 80% of time spent on the project...
            # My conclusion is just drop this requirement." Live evidence that surfaced it:
            # `iba/docs/escalation-operational-friction-review-v1-20260831.md` Defect 2 -- #1338/
            # #1339 (Claude blocked from leaving a clarifying comment on an item held by
            # Researcher) and #1341 (Researcher blocked from giving feedback on an item held by
            # Claude) -- the guard controlled who may say ANYTHING about an item, not just who
            # does the substantive work, and hit both parties in ordinary back-and-forth.
            #
            # Disabled by deactivating the three cfg_escalation_requirement rows (rowid 17/18/19,
            # active=0) rather than deleting them or this code branch -- reversible without a
            # redeploy if ever wanted back in a narrower form. This branch is now practically dead
            # (no active row references check_kind='actor_must_be_assignee') but left in place so
            # re-activating is a one-row UPDATE, not a rebuild. The SEPARATE, narrower D25 check --
            # whoever `ready_for_approval` assigned an item to is the only one who may `approved`/
            # `noted` it (hardcoded in update(), search "authority check, not identity -- D25") --
            # is NOT touched by this reversal; that one gates an actual decision, this one gated
            # everything.
            if self_id is not None:
                row = db.rows("SELECT next_action_assigned_to FROM escalation WHERE id=?", (self_id,))
                cur_assignee = row[0]["next_action_assigned_to"] if row else None
                if cur_assignee and originator != cur_assignee:
                    raise ValueError(
                        f"escalation #{self_id} is currently assigned to {cur_assignee!r} -- only "
                        f"{cur_assignee} may act on it (got originator={originator!r}). "
                        f"{cur_assignee} must process it first (even just to reassign it onward).")
        elif kind == "decision_required_approval_requires_researcher":
            # researcher, 2026-08-31: "the only way for you to get me to approve anything is to
            # set the item to ready_for_approval... When I process the approval step, that
            # implicitly is my approval." Closes the loophole D25 alone leaves open: D25 only
            # checks that the approver matches whoever 'ready_for_approval' assigned it to -- if
            # Claude assigns ready_for_approval to ITSELF (a legitimate self-authorisation for
            # self_correctable-shaped work), D25 passes even though the item is decision_required,
            # which structurally must never be Claude's call. Independent of assignment history.
            if self_id is not None:
                row = db.rows("SELECT resolution_kind FROM escalation WHERE id=?", (self_id,))
                if (row and row[0]["resolution_kind"] == "decision_required"
                        and originator != "Researcher"):
                    raise ValueError(r["message"])
        elif kind == "ready_for_approval_not_assignable_to_claude":
            # researcher, 2026-08-31: "you may want to build in another overall control that
            # ready for approval for tasks and issue can not be assigned to claude, because you do
            # not have authority to self approve these types." Belt-and-suspenders alongside
            # decision_required_approval_requires_researcher above -- that one catches Claude
            # setting approved/noted on a self-assigned item; this one stops the self-assignment
            # from ever landing at ready_for_approval in the first place, for type in
            # ('task','issue') regardless of resolution_kind (a self_correctable item never
            # reaches ready_for_approval at all -- it closes via resolve_self_correctable() -- so
            # scoping by type rather than resolution_kind changes nothing in practice, and matches
            # the researcher's own words exactly). Real example this was written against: escalation
            # #1315, set ready_for_approval but left assigned_to=Claude by Claude's own mistake.
            if self_id is not None and values.get("next_action_assigned_to") == "Claude":
                row = db.rows("SELECT type FROM escalation WHERE id=?", (self_id,))
                if row and row[0]["type"] in ("task", "issue"):
                    raise ValueError(r["message"])
        elif kind == "reassign_to_researcher_requires_ready_for_approval":
            # researcher, 2026-09-03: caught Claude bare-reassigning 4 decision_required items
            # (#1373/#1316/#1366/#1375) back to the researcher -- next_action left at 'review',
            # only next_action_assigned_to touched -- after already doing complete, real work on
            # each. Verbatim: "why did you pass [them] back to me. the expectation is that you do
            # a ready for approval... and assign it to me... It is not the first time we get into
            # this loop and it must stop now with a proper fix in the configs." cfg_behaviour_rule
            # 63's own two-branch design (progress-via-ready_for_approval OR bounce-with-a-comment
            # when genuinely unsure) left exactly this judgement call open, and it kept getting
            # made wrong. This closes it structurally, no judgement call left: handing a
            # decision_required item from Claude to the Researcher must set
            # next_action=ready_for_approval in the SAME call -- there is no third, bare-handoff
            # option any more, including "I'm stuck, please advise" (state that as the resolution
            # text on a ready_for_approval call; the researcher's reply -- approved/reject/revise --
            # already covers "yes"/"no"/"reconsider this way" without a separate bare-review path).
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
            # escalation #2000 T4 (researcher, round 1: "I am ok if threads are assigned as
            # self-correctable"): every thread is raised self_correctable.
            if field_val != "self_correctable":
                raise ValueError(r["message"])
        elif kind == "no_open_thread_items":
            # escalation #2000 T6: a thread reaches completed/closed only when every item is
            # closed. `field` is 'state' -- the state this call would land on. Items written
            # earlier in the same call (a last item closed together with approved) are already
            # visible here: same connection, same transaction.
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
    """New item, version 1. Every field is 'set' at creation -- no delta/envelope split needed,
    v1's history row IS the full row (matches escalation itself)."""
    _grant_both(cfg)
    row = {"version": 1, **{k: fields.get(k) for k in _COLS}}
    new_id = db.write("escalation", row)
    db.write("escalation_history", {"escalation_id": new_id, "version": 1,
                                    **{k: fields.get(k) for k in _COLS}})
    return new_id


def _snapshot(cfg: Cfg, db: Db, escalation_id: int, deltas: dict, envelope: dict,
              originator: str) -> dict:
    """`deltas` = exactly what the caller is setting THIS transaction for append/replace columns
    (raw, un-merged increments -- None/absent means untouched). `envelope` = state/next_action/
    next_action_assigned_to already resolved by the caller. Writes escalation_history with deltas
    AS GIVEN (NULL where not supplied this version) plus envelope always populated -- a true
    per-version delta, not a cumulative snapshot (escalation-rebuild-design-v1 sec1/sec3). Writes
    `escalation` with append-cols merged onto the running cumulative text and replace-cols taking
    the new value or carrying forward -- `escalation` stays the full current-state materialisation
    it always was."""
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
    """D25: who a past transaction ASSIGNED the item to when it set `next_action` -- distinct from
    `_last_next_action_originator` (who DID it). Used to answer 'ready_for_approval assigned this to
    whom' for the authority check."""
    rows = db.rows(
        "SELECT next_action_assigned_to FROM escalation_history WHERE escalation_id=? AND "
        "next_action=? ORDER BY version DESC LIMIT 1", (escalation_id, next_action))
    return rows[0]["next_action_assigned_to"] if rows else None


# ── THREADS (type='thread', escalation #2000) ────────────────────────────────────────────────────
# The open threads register carried in the escalation table. Design: _analytics/cross-cluster-web/
# open-threads-table-proposal-v3-20261012.md (rounds 1-6). Rules T0-T9 live in config:
# cfg_escalation (thread_check_before_work, raise_state_choice, thread_completion, 4 amended),
# cfg_escalation_transition (priority 0, the two thread_* condition keys),
# cfg_escalation_requirement (thread_type rows), cfg_behaviour_rule
# open-threads-carried-as-escalations. A thread's items (escalation_thread_item) hold current status
# only; every response, including each completion, is an escalation_thread_item_response row.

def resolve_id(db: Db, ref) -> int:
    """An escalation id from `ref`: 2000, '2000', '#2000', or a thread alias 'OT-16' (any case).
    Escalation.ps1 -Id accepts the alias anywhere an id is taken (proposal sec5)."""
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
    """An item of `thread` from `ref` (proposal sec3.4): 'OT-16.1' (alias must be this thread's),
    '1' (the item number), 'kind:value', or the value alone (unique within the thread)."""
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


_SETTLE_KINDS = ("closed", "withdrawn", "superseded")   # #2000 lifecycle: response kinds
                                                         # that settle an item (its status = kind)
_SUCCESSOR_RE = re.compile(r"\bOT-\d+(?:\.\d+)?\b|#\d+")


def _respond(cfg: Cfg, db: Db, item: dict, kind: str, text: str, *, via: int | None, by: str,
             files: list | None, at: str) -> None:
    """One response row (ruling 7: every individual completion is recorded in the response table).
    A settling kind -- closed, withdrawn, superseded (#2000 lifecycle) -- needs an open item and
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
    """#2000 lifecycle (G4): no thread ends with an open item. Withdraw -> each open item is
    withdrawn with the thread's reason. Supersede -> each open item is added to the successor
    thread (an existing item of the same kind:value is reused, reopened if settled) and recorded
    superseded here, naming its new reference. Returns summary lines for the history comment.
    `succ_lines`, when given, receives what happened on the successor -- each item added,
    reopened or already open there -- for the successor's own history (G5-a, test plan v5)."""
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
    """T5 (round 2, 'in-progress only'): an open 'escalation' item points at a task or issue that
    is itself at state in-progress."""
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
    """#2000 lifecycle: the resolution written when a thread completes because its last item was
    settled -- each item with how it was settled, from its latest response."""
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
    update(): the two priority-0 thread rows, else unchanged. Writes one history version carrying
    `summary` (ruling 8: notes on a thread land in history). Returns the new state, or None when
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
    item '#ref_id') into line -- T6: when the task or issue reaches a terminal state its item
    closes, with a note of what it settled (round 2: it may close without resolving its threads);
    T3/T5: a thread follows the in-progress state of the work that references it."""
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
        if ref["state"] in _TERMINAL_STATES:
            # #2000 lifecycle (G2): the item takes the task's own ending -- a withdrawn or
            # superseded task does not read as work done.
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
        if target["state"] not in _OPEN_STATES:
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
    """T5, run at session start (.claude/commands/start-project.md step 4B): every open thread
    referenced by a task or issue is brought into line with that work -- moved to in-progress when
    the work is in-progress, its item closed when the work has reached a terminal state."""
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
    """Dispatcher-tied short_description still respects the title-shape spec, but this path fires
    from inside a crash/pause handler (run.py:172-200) -- raising here would mask the real crash.
    Sanitise instead of reject, never lose data: the untouched original survives in
    preset['full_message'] whenever sanitising actually changes anything."""
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

    `resolution_kind` (escalation #798/#799): every real call site now supplies one explicitly
    (crash/report-stop pass `self_correctable` -- "pure coding logic", researcher 2026-08-22;
    pause-continue passes through whatever the handler's own `escalate()` call decided). The
    `None` fallback below (-> `decision_required`, the conservative "we don't know, ask" default)
    exists only as the same sanitise-don't-crash safety net this function already follows
    elsewhere -- never intended to be the normal path. If `decision_required` and `etype` isn't
    `notice`, `type` is forced to `issue` (same rule as `raise_new()`).

    Escalation #790 (2026-08-22, researcher: "Proceed to fix this bug"): this shape used to leave
    `comment`/`originator` unset (NULL), even though `cfg_escalation_requirement` states `comment`
    is required "always" at Raise, with no carve-out for the dispatcher shape -- #787 was the live
    example. Fixed by ALWAYS populating both, not by calling `_check_requirements()` (which
    raises on failure): this function already fires from inside crash/pause handling
    (`run.py`), where the module's own long-standing rule for `_sanitise_dispatcher_title` applies
    equally -- "raising here would mask the real crash. Sanitise instead of reject, never lose
    data." `comment` reuses `tried` (every real call site already passes a real, non-empty
    explanation there -- the same content a comment is meant to hold, e.g. "ran the full
    validation report -- {out}"); `originator` is 'Claude' (every current call site is invoked by
    Claude Code, and 'Claude'/'Researcher' are the only two values `cfg_enum
    escalation_assignee` allows -- there is no third 'system' option).
    `next_action` is `'review'` (researcher, 2026-08-22: "it just does not have a next-action and
    the state should be review" -- correcting an earlier, wrong version of this docstring, which
    reasoned `next_action` had to be a member of `cfg_enum escalation_next_action_dispatcher`
    (approve/reject/revise/hold/noted) and left it `None` on that basis. That enum is only ever
    consulted by `_check_next_action_dispatcher()`, which fires solely inside `answer_for_run()`
    -- it validates the ANSWER decision, never the value a freshly-raised item starts at.
    `raise_new()` (the manual shape) already sets its own initial `next_action = "review"` as a
    bare literal, with no enum check at all at creation -- `'review'` here does exactly the same,
    for the same reason: it means "this needs a decision", not "the decision is X".

    `title` (escalation #1326, 2026-08-31): a caller-supplied, already title-shaped
    short_description -- used directly, `question` then stays free to be the real, longer
    REPRESENTATIVE description a caller like `configmaint.propose` needs, without either being
    forced through the lossy word-slicing `_sanitise_dispatcher_title()` otherwise applies. Found
    live: every `configmaint.propose` escalation's short_description was a mid-word-truncated
    fragment of its `-Question`, because that single field had to serve as both the representative
    description AND the title -- `-Question` was never actually validated as (or intended to be) a
    title. Omitted (the crash-handler call site in `run.py`'s `except Exception` never has a
    pre-built title to give), the old sanitise-by-truncation behaviour is unchanged -- that
    fallback stays deliberately lossy-but-safe because it fires from inside exception handling,
    where raising here would mask the real crash (see `_sanitise_dispatcher_title`'s own
    docstring). A caller-supplied title is assumed pre-validated (the two live call sites --
    `configmaint.propose`, `handlers/base.py:escalate()`'s docstring -- both point back to
    `_title_shape_error` at the source, where a bad title fails loudly as its own clear crash
    rather than being silently swallowed here); still guarded defensively rather than trusted
    blindly, since a badly-shaped title reaching this deep should never itself become a second,
    confusing failure on top of whatever the original escalation was about."""
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
    """`run_id` accepts either the full dispatcher run_id string, or (as a convenience) the short
    escalation id, e.g. '796' -- researcher-reported UX gap, escalation #795 v4 (2026-08-22): the
    researcher tried the short numeric id instead of the long generated string and got 'no pending
    escalation for run 796'; the long string is error-prone to copy correctly. Short-id resolution
    still requires the row to actually be dispatcher-tied (run_id IS NOT NULL) so a manual-shaped
    item can never be answered through this path just by guessing its id."""
    if run_id.isdigit():
        return db.rows(
            "SELECT * FROM escalation WHERE id=? AND run_id IS NOT NULL AND state='raised' "
            "ORDER BY id DESC LIMIT 1", (int(run_id),))
    return db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND state='raised' "
        "ORDER BY id DESC LIMIT 1", (run_id,))


def answered_for_run(db: Db, run_id: str, at_step: str):
    """The latest ANSWERED escalation for a run at a step, or None -- a real decision
    (approve/approved/reject/revise) recorded in `next_action`, regardless of `state`. `hold`/
    `noted` deliberately never match (their own `next_action` values aren't in this list).

    Fixed 2026-08-31 (escalation #1328, researcher's own live suspicion, confirmed by
    reproduction): this used to require `state='completed'` -- correct before escalation #1075/
    #1301 existed, wrong since. A `needs_claude_followup` item's `approved` deliberately resolves
    to `state='re-assigned'`, NOT `completed` (cfg_escalation_transition priority 1, "routes back
    to Claude instead of completed") -- meaning the OLD query could never find a
    `configmaint.propose` approval at all, because `propose()` always sets `needs_followup=True`.
    Reproduced live: re-running an approved #1309 with the researcher's real 'approved' decision
    already on file still fell all the way through to demanding a fresh decision, because this
    query's `state='completed'` filter excluded the very row that held the answer. Every
    `configmaint.propose` approval before this fix was silently subject to the same gap -- caught
    only where independently re-verified against the live DB (escalations #1238-1256's own
    history notes exactly this), never by the escalation's own terminal state, because there
    never was one to reach."""
    rows = db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND at_step=? AND "
        "next_action IN ('approve','approved','reject','revise') "
        "ORDER BY id DESC LIMIT 1", (run_id, at_step))
    return rows[0] if rows else None


def answered_baseline_for_step(db: Db, at_step: str, current_counts: dict):
    """The most recent APPROVED escalation for `at_step`, ACROSS every run (not just this one),
    if its recorded `context` preset counts already cover `current_counts` component-wise --
    or None if no such row exists, parsing fails, or the current counts exceed what was approved.

    Built 2026-09-15, escalation #1707 (researcher, verbatim, on that item's own comment: "this
    report is as expected. Can be signed off. This situation should no longer create an exception
    everytime it runs"). `answered_for_run()` above only recognises an answer given to THIS SAME
    run_id -- a plain read-only DB-wide check like `cluster.validate`/`spine.check` gets a fresh
    run_id every invocation, so a researcher's 'approved' on one run's findings could never be
    recognised by any LATER run, however unchanged the underlying backlog -- exactly the repeated-
    escalation-on-a-known-situation defect this closes. Deliberately narrow and fail-safe: only
    `next_action IN ('approve','approved')` counts as durable acknowledgment (a `reject`/`revise`
    means the researcher wants it acted on, never silently re-absorbed); every key in
    `current_counts` must be present in the stored preset AND <= its stored value, or this returns
    None (escalate again) rather than guess. A genuine INCREASE in any count still escalates fresh,
    exactly as before -- this only suppresses re-raising the SAME already-acknowledged situation,
    never masks growth."""
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


def open_duplicate(db: Db, at_step: str, stable_key: str):
    """Two real bugs found and fixed live 2026-08-29 (a `configmaint.validate` re-run pile-up --
    #1008/#1011/#1015/#1016/#1017/#1038/#1039, seven near-identical "cfg_* is structurally
    coherent" notices in one session, the exact class this function's own call site comment says
    it exists to prevent):

    1. Matched against `short_description`, which `_sanitise_dispatcher_title` truncates to
       `_TITLE_MAX_CHARS` (60) chars -- but `configmaint.validate`'s own lead-in text ("cfg_* is
       structurally coherent, but has findings needing your judgement: ") is already ~74 chars, so
       `short_description` NEVER contains any of the variable finding-summary text `stable_key`
       actually is. The `LIKE` could never match, structurally, regardless of whether the
       underlying finding-set had genuinely changed or not. Fixed: match against `context`
       instead, which holds the un-truncated `json.dumps(preset)` (via `escalate()`) -- `preset`
       includes `full_message`, which DOES contain `stable_key` verbatim.
    2. Matched only `state='raised'` -- but the researcher's own documented workaround for this
       exact class of noise (#1008: "I am leaving it here so the system will not duplicate the
       same error") moves the anchor escalation to `state='in-progress'`, which this query could
       never see. Fixed: reuse the module's own shared `_OPEN_STATES` (raised/re-assigned/
       on-hold/in-progress) -- the same "still open, not yet closed" definition `write_list_report`
       already uses -- rather than the narrower literal this function invented independently."""
    ph = ",".join("?" * len(_OPEN_STATES))
    rows = db.rows(
        f"SELECT * FROM escalation WHERE at_step=? AND state IN ({ph}) AND context LIKE ? "
        f"ORDER BY id DESC LIMIT 1", (at_step, *_OPEN_STATES, f"%{stable_key}%"))
    return rows[0] if rows else None


def answer_for_run(cfg: Cfg, db: Db, run_id: str, decision: str, comment: str | None = None,
                   *, answered_by: str, resolution: str | None = None) -> str:
    """Record the decision on a run-scoped (dispatcher-tied) escalation. `answered_by` is required,
    no default (escalation-rebuild-design-v1 sec6).

    escalation #795 (researcher, 2026-08-22) -- BOTH `resolution_kind` values now refuse this
    path, checked and confirmed live as real gaps before either guard existed, not assumed:

    - `decision_required` (checked live 2026-08-22, escalation #820: a flat 'approve' via AnswerRun
      silently succeeded on a decision_required item -- researcher's own words, "it should not be
      possible"). Mirrors `update()`'s own carve-out the OTHER way: `update()` refuses a
      dispatcher-tied item UNLESS `resolution_kind='decision_required'`; this refuses one IF
      `resolution_kind='decision_required'` -- together, a decision_required item is answerable
      ONLY through Update's richer vocabulary (ready_for_approval -> approved, -State on-hold,
      next_action=reject/revise/noted).
    - `self_correctable` (this was always the APPROVED spec -- proposal
      `escalation-decision-vs-defect-axis-proposal-v4-20260822.md` §6: "No approve/reject/revise/
      hold/noted vocabulary. AnswerRun is never invoked" -- and its own §11 Stage 2 test named this
      exact check by name: "confirm the second [a self_correctable item] has no reachable AnswerRun
      path (attempting it should refuse, citing resolution_kind)". #799's Stage 2 build never
      actually implemented or tested this specific line of its own approved spec -- found live
      2026-08-22 re-checking #795, escalation #822, the same way #820 was found: a flat 'approve'
      succeeded with no refusal at all. A self_correctable item is closed ONLY via
      `resolve_self_correctable()` / converted via `escalate_to_decision()`, never AnswerRun.

    Net effect: `AnswerRun`'s flat approve/reject/revise/hold/noted vocabulary is now unreachable
    for EVERY item raised under the resolution_kind regime (i.e. every item raised since #799,
    resolution_kind being required at Raise) -- both branches refuse. This is a real, deliberate
    consequence of the approved design, not a partial/temporary state: `decision_required` runs
    terminate and never resume the same run_id (a fresh run is the test, per §5), and
    `self_correctable` items never carried decision vocabulary to begin with (per §6) -- neither
    kind ever had a genuine use for AnswerRun's original 'answer and resume' semantics. See
    `cfg_behaviour_rule` (class=development,
    rule_key='decision-required-answered-via-update-not-answerrun') -- text covers both halves."""
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
    """Raise -- a new MANUAL item. `originator` is required, no default. `comment`/
    `short_description` requirements come from cfg_escalation_requirement (action='raise').

    `resolution_kind` (escalation #798/#799): `decision_required` or `self_correctable`, required
    at Raise (`cfg_escalation_requirement`).

    **No longer forces `type` to `issue` under `decision_required` -- removed 2026-08-26, escalation
    #872.** Until this fix, any `decision_required` raise silently overwrote whatever `etype` was
    passed (unless it was `notice`) with `issue`, regardless of caller intent -- never a config rule
    (no `cfg_escalation_requirement`/`cfg_escalation_transition` row implemented it, just a bare
    Python `if`), and the researcher's own explicit instruction on #872 was 'Task and notes as types
    are a requirement' -- `task` must be settable and respected under `decision_required`, not
    coerced. Whatever `etype` is passed (or defaults to) is now used as-is, checked only for cfg_enum
    membership.

    D12 (register v9, type-keyed Raise defaults): only `notice` is special -- it closes on arrival
    (`state='closed'`, `next_action=NULL`), never entering the review/decision machinery. Every
    other type (`task`/`issue`/`run_error`/`config`/`note`) defaults identically: `state='raised'`,
    `next_action='review'`.

    `needs_followup` (escalation #1075, 2026-08-30): set when finishing this item will require a
    further action from Claude AFTER the researcher approves it (a config apply, a build step) --
    consumed by cfg_escalation_transition so `approved` routes back to Claude instead of straight to
    `completed`. Defaults False -- most items need nothing further.

    escalation #2000 (2026-10-12):
    - `state` (T2, cfg_escalation raise_state_choice): a manual Raise may land at any member of
      cfg_enum escalation_raise_state (raised / on-hold / in-progress); default 'raised'. Offered
      here only -- the code path `raise_()` keeps 'raised', so module_blocking still fires.
    - type 'thread': `items` (kind, value, note) are required (T7), resolution_kind must be
      self_correctable (T4), the alias OT-nn is assigned automatically, the state defaults to
      on-hold and may not be 'raised', and next_action is left empty (a thread is not waiting on
      review). `comes_back_when` holds the thread's whole 'comes back when' text."""
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
    """Update -- every subsequent change to a MANUAL item. `originator` is required, no default.
    Two-stage approval separation of duties: the party that sets `approved` must differ from the
    party that most recently set `ready_for_approval` on this item.

    `needs_followup` (escalation #1075): None (the default) carries the item's current flag
    forward unchanged -- pass True/False to set or clear it, normally done at the
    `ready_for_approval` call (flag it there) and cleared once Claude actually finishes the real
    follow-up work, before the final `noted` that closes the item out.

    Dispatcher-tied carve-out (escalation #798/#799): a dispatcher-tied item is still refused
    UNLESS `resolution_kind='decision_required'`, in which case it's handled exactly like a
    manual item from here on -- `decision_required` always uses the manual ready_for_approval/
    approved vocabulary, regardless of which shape raised it (`cfg_behaviour_rule
    'decision-points-are-terminal-not-inline'`). A dispatcher-tied `self_correctable` item still
    has no `Update`/`AnswerRun` path at all -- see `resolve_self_correctable()`/
    `escalate_to_decision()` instead.

    Threads (escalation #2000, proposal sec3.3): `item_refs` + `response_kind` + `respond` (+ `via`,
    `files`) record one response per named item, all sharing one `via`; `closed` closes the item,
    `reopened` opens it again, and `forward` needs at least one `add_items` entry (the forward mark
    becomes a matchable item). `add_items` alone adds items. Each such Update also writes a
    one-line summary into the thread's history (ruling 8). The thread's state then follows the
    priority-0 cfg_escalation_transition rows (T3/T5, T6); completed/closed is refused while any
    item is open (T6). After any change to a task or issue, every thread referencing it is brought
    into line (`_sync_threads_for`).

    Thread lifecycle (#2000, researcher 2026-10-12: "the rest you need to control ... all
    interaction must go to history"): `withdrawn`/`superseded` settle an item like `closed`; when
    an item change leaves none open, the thread completes with a generated resolution. A thread
    withdrawn (`-NextAction reject -State withdraw`) withdraws its open items; superseded
    (`-State supersede`) needs `superseded_by` (OT-nn) and moves each open item there, recording
    it superseded. Each item response is written in full into the thread's history comment."""
    cur = _current(db, escalation_id)
    if not cur["run_id"].startswith("MANUAL-") and cur["resolution_kind"] != "decision_required":
        return (f"escalation #{escalation_id} is dispatcher-tied (run_id {cur['run_id']!r}), not "
               f"manual -- answer it via AnswerRun, not Update")
    if cur["state"] not in _OPEN_STATES:
        return f"escalation #{escalation_id} is not open (state={cur['state']!r})"

    who = _check_assignee(db, originator)
    checked_action = _check_next_action_manual(db, next_action)
    new_resolution = resolution if resolution is not None else cur["resolution"]
    # Hoisted above its one prior use site (envelope construction, below) so the
    # 'ready_for_approval' guard can see what the assignment WOULD become this call, not just
    # what it currently is.
    resolved_assignee = _check_assignee(db, next_action_assigned_to, required=False) or cur["next_action_assigned_to"]
    # Also hoisted above its later use (was computed just before _evaluate_transition, below) so
    # the forced-reassignment rule right after this can see it.
    resolved_needs_followup = (int(needs_followup) if needs_followup is not None
                               else cur["needs_claude_followup"])

    # researcher, 2026-08-31: "approval... will progress to approved, with Claude as assignee...
    # when claude completes the work, claude must be able to set the item to completed." An
    # approval that still needs follow-up work must hand the item BACK to Claude -- not leave it
    # sitting with whoever approved it (normally the Researcher) because nobody remembered to pass
    # -AssignedTo Claude explicitly. Forced, not merely defaulted: this overrides even an explicit
    # -AssignedTo on this specific call, because the flag's whole meaning is "this isn't done,
    # Claude has to act next" -- there is no legitimate reason to approve-with-followup and assign
    # it anywhere else.
    if checked_action == "approved" and resolved_needs_followup:
        resolved_assignee = "Claude"

    # D25 (register v9, corrects a shipped defect): approval is an AUTHORITY check, not an identity
    # check. The party ready_for_approval assigned the item to is who may approve -- Claude assigning
    # to itself is a legitimate, visible self-authorisation for items Claude holds authority over;
    # assigning to the researcher means only the researcher may approve. Same-party is fine when
    # that party holds the authority; what's refused is approving something assigned to someone else.
    #
    # Extended to 'noted' -- escalation #851, 2026-08-26. noted and approved both reach state=closed
    # (cfg_escalation_transition priorities 1/4) but only approved had this check; a decision_required
    # item could be closed via noted with zero authority check, something approved on the same item
    # would correctly have refused. Only for decision_required items -- self_correctable items close
    # via resolve_self_correctable() (its own, separate, no-approval-needed path by design, per
    # cfg_behaviour_rule 'decision-points-are-terminal-not-inline'); a self_correctable item reaching
    # 'noted' via plain Update is unaffected by this check.
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

    # ── thread items and responses (escalation #2000) -- written before the state is derived, in
    # the same transaction, so the transition rows and the T6 check see this call's changes.
    is_thread = cur["type"] == "thread"
    thread_facts, item_summary = None, []
    succ_lines: list[str] = []          # G5-a: what a supersede did on the successor thread
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
        if checked_action == "reject":                          # #2000 lifecycle (G4)
            item_summary += _settle_thread_on_reject(cfg, db, cur, state, superseded_by,
                                                     reason=comment, who=who, at=now,
                                                     succ_lines=succ_lines)
        changed = bool(add_items) or response_kind in _SETTLE_KINDS + ("reopened",)
        thread_facts = _thread_facts(db, escalation_id, items_changed=changed,
                                     closed_some=response_kind in _SETTLE_KINDS)
        if item_summary:
            # all interaction to history (#2000 lifecycle, G5): the response itself, in full
            line = (f"{cur['alias'] or '#' + str(escalation_id)}: " + "; ".join(item_summary)
                    + (f" (via #{via_id})" if via_id else ""))
            if respond:
                line += f" -- {response_kind} by {who}: {respond}"
                if files:
                    line += f" [files: {', '.join(files)}]"
            comment = f"{comment}\n{line}" if comment else line

    assignee_changed = bool(next_action_assigned_to) and next_action_assigned_to != cur["next_action_assigned_to"]
    # resolved_needs_followup now computed earlier, above -- the forced-reassignment rule needs it
    # before this point.
    new_state = _evaluate_transition(db, "manual", checked_action, has_resolution=bool(new_resolution),
                                     assignee_changed=assignee_changed, explicit_state=state,
                                     cur_state=cur["state"], needs_followup=bool(resolved_needs_followup),
                                     cur_next_action=cur["next_action"], thread=thread_facts)

    if (is_thread and new_state == "completed" and thread_facts and thread_facts["all_settled"]
            and not new_resolution):                        # #2000 lifecycle: last item settled
        resolution = new_resolution = _thread_completion_resolution(db, cur)

    # D26 (register v9): work cannot land on a `raised` item -- comment/context/tried content
    # requires the state to actually move first (e.g. -State in-progress), mechanically enforced
    # here via cfg_escalation_requirement (action='update', check_kind='not_raised_with_content').
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
    # researcher, 2026-08-31: the old message showed only state (e.g. "-> state='re-assigned'"),
    # leaving next_action invisible -- ambiguous, since 're-assigned' alone doesn't say WHAT it was
    # re-assigned by (approved? a plain reassignment?). Show both.
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
    """Correction — escalation #774 v2, researcher verbatim: "create a copy of update transaction
    as Correction and allow the Correction transaction to update any column in any state... ensure
    that this is update in the documentation and that correction is stated as only to be used for
    error correction."

    ★ ERROR CORRECTION ONLY — not a normal workflow action. Use Update for every ordinary change
    (comments, decisions, reassignment, state changes); use Correction only to fix something
    already recorded wrong (a bad title, a typo in a resolution). Correction does
    NOT advance an item through its lifecycle — state/next_action are taken EXACTLY as given, never
    auto-derived via cfg_escalation_transition, and default to the item's CURRENT values (carried
    forward unchanged) when omitted, which is the normal case: most corrections touch content, not
    workflow.

    Differs from `update()` in exactly the two ways the researcher asked for, nothing more:
    1. No `_OPEN_STATES` gate — works on closed/completed/withdraw/supersede items, which `update()`
       structurally refuses (escalation #774's own finding).
    2. `short_description` is a real parameter — `update()` has none at all (escalation #10's
       finding; `_REPLACE_COLS` already lists it as an eligible delta column, nothing before this
       ever wired it through). Still subject to the same title-shape spec as Raise (#759's
       guardrail) — a Correction cannot write an over-length/dashed/multi-line title either.

    Deliberately NOT copied from `update()`: the D25 same-approval-authority check and the D26
    raised-state content guard — both are workflow-transition safeguards, not data-integrity ones,
    and a correction has to be able to fix ANY state (including a `raised` item with a wrong
    title) without being routed through the two-stage approval machinery.

    **No `MANUAL-` restriction — removed 2026-08-26, escalation #867.** A `run_id.startswith
    ('MANUAL-')` gate was added at some point after #774 and was never actually part of the
    original spec quoted above, which says "any column in any state" — no carve-out for
    dispatcher-tied items. Found live when it blocked correcting #865/#866 (both dispatcher-tied,
    wrongly recorded `completed`/`approved` after an invalid transition), the exact class of repair
    Correction exists for. Researcher, #867 v2, verbatim: "the correction action was intended to be
    able override the controls and to reset a escalation. It should be handled with care but must
    be available." Handling-with-care is the CLI's own yellow ERROR-CORRECTION-ONLY warning at the
    point of use (`Escalation.ps1`), not a code-level restriction on which items qualify."""
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
    synced = _sync_threads_for(cfg, db, escalation_id, who=who)       # escalation #2000
    return (f"escalation #{escalation_id} v{merged['version']} CORRECTED -> "
           f"state={resolved_state!r}, next_action={resolved_next_action!r}, "
           f"assigned_to={resolved_assigned_to!r}"
           + ("\n  threads: " + "; ".join(synced) if synced else ""))


# ── resolution_kind transactions (escalation #798/#799) ─────────────────────────────────────────
def resolve_self_correctable(cfg: Cfg, db: Db, escalation_id: int, resolution: str,
                             *, originator: str) -> str:
    """Closes a `self_correctable` escalation. No `approve`/`reject`/`revise`/`hold`/`noted`
    vocabulary and no `AnswerRun` involvement -- `cfg_behaviour_rule
    'decision-points-are-terminal-not-inline'`: a researcher never fixes code, so there is no
    decision for them to make here. Claude fixes it, states what was wrong and what changed
    (`resolution`, required), and this closes the item directly."""
    cur = _current(db, escalation_id)
    if cur["resolution_kind"] != "self_correctable":
        raise ValueError(f"escalation #{escalation_id} is not self_correctable "
                        f"(resolution_kind={cur['resolution_kind']!r}) -- use Update/AnswerRun "
                        f"instead, or escalate_to_decision() if it turned out to need one")
    if not resolution:
        raise ValueError("resolution is required -- state what was wrong and what changed")
    who = _check_assignee(db, originator)
    # values (escalation #2000): type + the state this lands on, so the T6 row
    # (no_open_thread_items, condition thread_type) can refuse a thread with open items.
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
    """Converts an existing `self_correctable` escalation to `decision_required` -- the mechanism
    named in `cfg_behaviour_rule 'decision-points-are-terminal-not-inline'`: a self-correction
    attempt that reveals a genuine new decision is needed, not just an execution slip (this is
    `tried`'s original purpose: what was attempted before escalating further). Does NOT change
    `type` -- immutable, same as `run_id`/`source`/`at_step`/`raised_at`; the item keeps whatever
    type it was raised with, only `resolution_kind`/`state`/`next_action` change. `tried` is
    required and non-empty."""
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
    synced = _sync_threads_for(cfg, db, escalation_id, who=who)       # escalation #2000
    return (f"escalation #{escalation_id} v{merged['version']} converted to decision_required "
           f"(state={new_state!r})" + ("\n  threads: " + "; ".join(synced) if synced else ""))


# ── reports ───────────────────────────────────────────────────────────────────────────────────
def _gist(raw, width: int = 80) -> str:
    if not raw:
        return ""
    return str(raw).replace("\n", " ")[:width]


# D15 RETIRED 2026-08-27, escalation #909, along with D14 (see module docstring's retirement
# banner) -- the whole from_id/related_activity graph (cycle/dangling/mismatched-pairing/
# missing-link/incoherent-link) and its detection functions (_link_graph/_find_cycles/
# _find_dangling/_find_mismatched_pairing/_find_missing_link/_find_incoherent_link) are removed,
# not just unreachable.


def write_list_report(cfg: Cfg, db: Db, path: pathlib.Path) -> tuple[pathlib.Path, list]:
    """Open items, WITH full history inline underneath each one -- the `comment`/`context` columns
    here are the true per-version DELTA (blank when that version didn't touch the field), not a
    cumulative gist (escalation-rebuild-design-v1 sec4.2).

    No longer grouped by `related_activity` (D14/D15 retired 2026-08-27, escalation #909, see
    module docstring) -- straight `id` order.

    Threads (escalation #2000, proposal sec5, clash C6) are kept out of the per-item body -- 100
    of them would flood it -- and get one short section instead: counts by state, then the
    in-progress threads only (rule 4 counts those alone). `-Action Thread` lists them all."""
    ph = ",".join("?" * len(_OPEN_STATES))
    rows = db.rows(f"SELECT * FROM escalation WHERE state IN ({ph}) AND type != 'thread' "
                   f"ORDER BY id", _OPEN_STATES)
    n_on_hold = sum(1 for r in rows if r["state"] == "on-hold")
    n_in_progress = sum(1 for r in rows if r["state"] == "in-progress")
    n_active = len(rows) - n_on_hold - n_in_progress
    objectives = cfg.required_setting("escalation.control_objectives")
    process = cfg.required_setting("escalation.control_process")
    L = ["# Open escalations", "",
        f"> {objectives}. {process}.".strip(), "",
        f"> Generated by `Escalation.ps1 -Action List`. {len(rows)} open escalation(s) "
        f"({n_active} active, {n_in_progress} in-progress, {n_on_hold} on-hold), full history "
        f"inline (each row = that version's own changes).", ""]
    if not rows:
        L.append("_no open escalations_")
    for r in rows:
        hist = db.rows("SELECT * FROM escalation_history WHERE escalation_id=? ORDER BY version",
                       (r["id"],))
        L.append(f"## #{r['id']} v{r['version']} — {r['state']} — {r['short_description']}")
        L.append(f"type={r['type']} assigned_to={r['next_action_assigned_to']}")
        L.append("")
        L.append("| v | state | next_action | originator | changed this version | at |")
        L.append("|---|---|---|---|---|---|")
        for h in hist:
            changed = [c for c in ("comment", "context", "resolution", "tried",
                                   "short_description", "comes_back_when") if h[c]]
            summary = "; ".join(f"{c}: {_gist(h[c], 50)}" for c in changed) or "_(state/assignee only)_"
            L.append(f"| {h['version']} | {h['state']} | {h['next_action'] or ''} | "
                     f"{h['originator'] or ''} | {summary} | {h['answered_at']} |")
        L.append("")

    # ── threads (escalation #2000) ──
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

    # Found live 2026-08-21 (researcher, reading this exact table): no short_description column at
    # all -- a resolution-text-only row gives no way to tell what the item was ABOUT without going
    # to look it up elsewhere. Fixed: short_description now selected and shown first. Widened the
    # WHERE too -- `resolution IS NOT NULL` silently excluded closed notice-type items whose
    # resolution text was folded into `comment` instead (raise_new() can't set `resolution` on an
    # auto-closed notice) -- those items are just as "recently resolved" as any other; requiring a
    # non-null resolution was accidentally hiding a whole class of legitimately-closed items, not a
    # deliberate filter.
    resolved = db.rows(
        "SELECT id, short_description, state, resolution, answered_at "
        "FROM escalation WHERE state IN ('completed','closed','withdraw','supersede') "
        "AND type != 'thread' ORDER BY answered_at DESC LIMIT 15")
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

    # 2026-08-26 (escalation #857): was manual archive_before_write()+write_text(), bypassing the
    # app-wide report.version_on_regenerate mechanism (BUILD.md sec60) every other report writer
    # goes through -- this report never got versioned/archived-with-history like the rest of the
    # app. Now uses reportkit.write_report() like everything else; return value captured and
    # returned (not the pre-write `path`), per sec60's own fixed 19-site systemic bug.
    out = reportkit.write_report(db.conn, "escalation.list", path, L)
    return out, rows


def write_history_report(cfg: Cfg, db: Db, escalation_id: int, path: pathlib.Path) -> pathlib.Path:
    """Deep-history report for one item -- its own full history only. Every column shown: envelope
    fields always, delta fields only when this version actually set them (escalation-rebuild-
    design-v1 sec4.1).

    No longer walks related items (D14/D15 retired 2026-08-27, escalation #909, see module
    docstring) -- this used to queue every escalation `from_id` or `related_activity`'s free-text
    `#NNN` mentions pulled in, transitively. One item's history only, now."""
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
    # 2026-08-26 (escalation #857): same fix as write_list_report above -- was manual
    # archive_before_write()+write_text(), bypassing report.version_on_regenerate (BUILD.md
    # sec60) entirely. Now goes through reportkit.write_report(); `path`'s stem (built by the
    # caller, id-prefixed per the researcher's direct instruction this escalation) becomes the
    # versioned {stem}-v{n}-{date}.md filename automatically -- no separate filename-pattern
    # setting needed, the app-wide mechanism already provides it.
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
    """`Escalation.ps1 -Action Thread` (escalation #2000, ruling 6: "Open threads should be a easy
    query on -action thread only"). Without `ident`: every open thread (on-hold and in-progress;
    `state` narrows to one), each with its open items. With `ident` (an id or OT-nn): that one
    thread, every item with its responses in date order. Returns the written path and short
    console lines."""
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
    """`Escalation.ps1 -Action Export -Type thread` (escalation #2000, proposal sec5): regenerates
    the open threads register at its old path from the escalation table -- every thread, by OT
    number, `OT-nn · #id` in the id cell (decision 3). The thread, raised and comes-back-when cells
    carry the imported text unchanged; the status cell is generated: state, each item with its
    latest response, then the register's own status text from before the migration (`tried`)."""
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
    out = reportkit.write_report(db.conn, "escalation.thread_export", path, L)
    return out, len(threads)


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
    """A repeatable --name=value flag (escalation #2000: -Item, -AddItem, -Cluster, ...)."""
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


# escalation #1708, 2026-09-15: the per-connection 30s busy_timeout (cfg.py:Cfg.__init__, WAL +
# PRAGMA busy_timeout=30000) already retries a lock internally -- but a sustained heavy DB-wide
# sweep in a SEPARATE process (e.g. cluster.validate's own 15,455-strong scan, run concurrently
# this session) held a write lock long enough that even 30s wasn't always enough, and this CLI's
# own crash handler (below) recorded it as a run_error rather than a real defect. Genuinely
# transient, not a logic bug -- a short CLI-level retry on the SPECIFIC "database is locked"
# error is proportionate defense-in-depth for exactly the interactive-researcher-typed-command
# case that crashed here, without masking any other failure (only this one error string retries;
# everything else still falls straight through to the existing crash-recording path unchanged).
_LOCK_RETRY_DELAYS = (1.0, 2.0, 4.0)  # seconds; 3 retries, ~7s total on top of the 30s per-attempt timeout


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
        # escalation-operational-friction-review-v1-20260831, Defect 1: a ValueError here is a
        # deliberate validation guard doing its job (_title_shape_error, _check_assignee,
        # _check_requirements, _require_flag, ... all raise exactly this) -- the CLI correctly
        # rejecting a malformed call, not a system failure. Filing it as a run_error escalation
        # (the old behaviour, shared with the branch below) meant every usage slip -- a title 2
        # chars over the limit, a missing -Resolution -- left a permanent traceback-carrying row
        # that then needed a hand-written "usage error, not a code defect" resolution: seven of
        # those, same day, before this fix (#1319, #1313, #1311, #1317, #1318, #1326, #1328).
        # Clean rejection instead: rollback (unchanged), print the message, exit non-zero, no
        # escalation write -- exactly like a shell command rejecting a bad flag. Only exceptions
        # NOT explicitly raised as validation (the branch below) still auto-file, because those
        # really are unanticipated -- this is how #1307/#1308's real WinError 32 bug and #1330's
        # real answered_for_run bug got caught today, and that stays unchanged.
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
                     resolution_kind="self_correctable",  # "pure coding logic" (researcher,
                     # 2026-08-22) -- same reasoning as run.py's crash/report-stop sites;
                     # escalate_to_decision() converts it if a fix reveals a real decision needed.
                     originator="Claude")
        except Exception as record_exc:
            # escalation #798/#799 SS7 fix: never SILENTLY discard a secondary failure -- the
            # original crash still re-raises unmasked (that guarantee is unchanged), but a failure
            # in the recording path itself must be visible, not invisible. Real risk right now:
            # raise_new() just gained a resolution_kind requirement (this call doesn't supply one
            # -- deliberately, a CLI crash is always decision_required by nature, no code path here
            # to decide otherwise -- but if that ever regresses, this is exactly the failure that
            # would go unnoticed under the old `except Exception: pass`).
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
        print(f"  {len(rows)} open escalation(s) -> {out}")
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
        # id-prefixed stem, 2026-08-26 (escalation #857) -- matches handlers/reports.py's copy
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
