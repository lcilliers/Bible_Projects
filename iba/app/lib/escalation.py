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
    python -m iba.app.lib.escalation resolve-self-correctable <id> --originator=Claude
        --resolution=... — closes a self_correctable item. No AnswerRun, no decision vocabulary
        (escalation #798/#799): Claude fixes it, states the resolution, done.
    python -m iba.app.lib.escalation escalate-to-decision <id> --originator=Claude --tried=...
        — converts a self_correctable item to decision_required when a fix attempt reveals a real
        decision is needed (`tried`'s original purpose). Does not change `type`.
    python -m iba.app.lib.escalation update <id> --originator=Claude|Researcher
        [--next-action=...] [--assigned-to=...] [--state=on-hold|in-progress|closed|withdraw|supersede]
        [--resolution=...] [--tried=...]
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
"""

from __future__ import annotations

import datetime
import json
import pathlib
import sys

from . import reportkit
from .cfg import Cfg
from .db import Db

_OPEN_STATES = ("raised", "re-assigned", "on-hold", "in-progress")

# every business column on `escalation` / `escalation_history` (id/version/escalation_id excluded
# -- those are structural, not part of a snapshot's business content)
# D14/D15 RETIRED 2026-08-27 (escalation #909): from_id and related_activity both removed from
# these tuples (and from the tables themselves) -- see the module docstring's retirement banner.
_ENVELOPE_COLS = ("state", "next_action", "next_action_assigned_to", "originator", "answered_at",
                 "resolution_kind")
_APPEND_COLS = ("comment", "context")            # escalation: cumulative. history: raw increment.
_REPLACE_COLS = ("resolution", "tried", "short_description")
_IMMUTABLE_COLS = ("run_id", "source", "at_step", "type", "raised_at")
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
                    assignee_changed: bool, has_explicit_state: bool = False) -> bool:
    """The fixed, small vocabulary cfg_escalation_transition.condition_key draws from -- see
    escalation-rebuild-design-v1-20260820.md sec2.4. A new condition needs a code change here
    (a new named boolean); which RULE consumes it, in what priority, with what resulting status,
    is config from that point on."""
    if condition_key == "always":
        return True
    if condition_key == "has_resolution":
        return bool(has_resolution)
    if condition_key == "assignee_changed":
        return bool(assignee_changed)
    if condition_key == "explicit_state_given":               # found live 2026-08-21 (#762): an
        return bool(has_explicit_state)                        # explicit -State must outrank the
                                                                # assignee_changed inference, not
                                                                # lose to it -- see priority 6 below
    raise ValueError(f"unknown cfg_escalation_transition.condition_key {condition_key!r}")


def _evaluate_transition(db: Db, shape: str, next_action: str | None, *, has_resolution: bool,
                         assignee_changed: bool, explicit_state: str | None,
                         cur_state: str) -> str:
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
                               has_explicit_state=explicit_state is not None):
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
        elif kind == "requires_prior_ready_for_approval_if_decision_required":
            # escalation #851, 2026-08-26: the D25 authority check alone is vacuous when no prior
            # ready_for_approval transition exists at all -- exactly how #865 was self-approved, and
            # would still be true of 'noted' even after D25 was extended to cover it. This makes the
            # SEQUENCE itself required for decision_required items, not just an opportunistic
            # comparison against whichever prior transition happens to exist.
            if self_id is not None:
                row = db.rows("SELECT resolution_kind FROM escalation WHERE id=?", (self_id,))
                if row and row[0]["resolution_kind"] == "decision_required":
                    has_rfa = db.rows(
                        "SELECT 1 FROM escalation_history WHERE escalation_id=? AND "
                        "next_action='ready_for_approval'", (self_id,))
                    if not has_rfa:
                        raise ValueError(r["message"])
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
          resolution_kind: str | None = None) -> int:
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
    for the same reason: it means "this needs a decision", not "the decision is X"."""
    now = _now()
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
        "resolution": None,
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
    """The latest COMPLETED escalation for a run at a step, or None. `hold`/`noted` deliberately
    never resolve to `state='completed'`, so they never match here."""
    rows = db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND at_step=? AND state='completed' "
        "ORDER BY id DESC LIMIT 1", (run_id, at_step))
    return rows[0] if rows else None


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
                                "resolution_kind": esc_row["resolution_kind"]},
                       originator=who)
    return (f"escalation {esc_row['id']} (run {run_id!r}, step {esc_row['at_step']!r}) answered "
           f"{decision!r} -> {new_state}" + (f" — {comment!r}" if comment else ""))


# ── MANUAL shape ──────────────────────────────────────────────────────────────────────────────
def raise_new(cfg: Cfg, db: Db, short_description: str, source: str, etype: str = "task",
             comment: str | None = None, context: str | None = None,
             assigned_to: str = "Claude", resolution_kind: str | None = None,
             *, originator: str) -> int:
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
    `next_action='review'`."""
    checked_type = _check_type(db, etype)
    checked_kind = _check_resolution_kind(db, resolution_kind) if resolution_kind else None
    _check_requirements(db, "raise", originator=originator or "", checked_action=None,
                        values={"comment": comment, "short_description": short_description,
                               "resolution_kind": checked_kind})
    title_error = _title_shape_error(short_description)
    if title_error:
        raise ValueError(title_error)
    run_id = f"MANUAL-{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d_%H%M%S_%f')}"
    now = _now()
    if checked_type == "notice":
        state, next_action = _check_state(db, "closed"), None
    else:
        state, next_action = _check_state(db, _status_for(db, "at Raise", "raised")), "review"
    fields = {
        "run_id": run_id, "source": source, "at_step": "manual", "type": checked_type,
        "short_description": short_description, "context": context, "comment": comment,
        "tried": None, "state": state, "next_action": next_action,
        "answered_at": now, "raised_at": now, "resolution": None,
        "resolution_kind": checked_kind,
        "next_action_assigned_to": _check_assignee(db, assigned_to),
        "originator": _check_assignee(db, originator)}
    return _create(cfg, db, **fields)


def update(cfg: Cfg, db: Db, escalation_id: int, *, next_action: str | None = None,
          next_action_assigned_to: str | None = None, comment: str | None = None,
          context: str | None = None, tried: str | None = None, resolution: str | None = None,
          state: str | None = None, originator: str) -> str:
    """Update -- every subsequent change to a MANUAL item. `originator` is required, no default.
    Two-stage approval separation of duties: the party that sets `approved` must differ from the
    party that most recently set `ready_for_approval` on this item.

    Dispatcher-tied carve-out (escalation #798/#799): a dispatcher-tied item is still refused
    UNLESS `resolution_kind='decision_required'`, in which case it's handled exactly like a
    manual item from here on -- `decision_required` always uses the manual ready_for_approval/
    approved vocabulary, regardless of which shape raised it (`cfg_behaviour_rule
    'decision-points-are-terminal-not-inline'`). A dispatcher-tied `self_correctable` item still
    has no `Update`/`AnswerRun` path at all -- see `resolve_self_correctable()`/
    `escalate_to_decision()` instead."""
    cur = _current(db, escalation_id)
    if not cur["run_id"].startswith("MANUAL-") and cur["resolution_kind"] != "decision_required":
        return (f"escalation #{escalation_id} is dispatcher-tied (run_id {cur['run_id']!r}), not "
               f"manual -- answer it via AnswerRun, not Update")
    if cur["state"] not in _OPEN_STATES:
        return f"escalation #{escalation_id} is not open (state={cur['state']!r})"

    who = _check_assignee(db, originator)
    checked_action = _check_next_action_manual(db, next_action)
    new_resolution = resolution if resolution is not None else cur["resolution"]

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
                            values={"resolution": new_resolution})
    if checked_action == "approved":
        _check_requirements(db, "approved", originator=who, checked_action=checked_action,
                            values={"resolution": new_resolution}, self_id=escalation_id)
    if checked_action == "noted":
        _check_requirements(db, "noted", originator=who, checked_action=checked_action,
                            values={}, self_id=escalation_id)
    if checked_action == "reject":
        _check_requirements(db, "reject", originator=who, checked_action=checked_action,
                            values={"state": state})
    if checked_action == "revise":
        _check_requirements(db, "revise", originator=who, checked_action=checked_action,
                            values={"tried": tried})

    assignee_changed = bool(next_action_assigned_to) and next_action_assigned_to != cur["next_action_assigned_to"]
    new_state = _evaluate_transition(db, "manual", checked_action, has_resolution=bool(new_resolution),
                                     assignee_changed=assignee_changed, explicit_state=state,
                                     cur_state=cur["state"])

    # D26 (register v9): work cannot land on a `raised` item -- comment/context/tried content
    # requires the state to actually move first (e.g. -State in-progress), mechanically enforced
    # here via cfg_escalation_requirement (action='update', check_kind='not_raised_with_content').
    _check_requirements(db, "update", originator=who, checked_action=checked_action,
                        values={"state": new_state, "comment": comment, "context": context,
                               "tried": tried},
                        self_id=escalation_id)

    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"comment": comment, "context": context, "tried": tried,
                              "resolution": resolution},
                       envelope={
                           "next_action": checked_action if checked_action is not None else cur["next_action"],
                           "next_action_assigned_to": _check_assignee(db, next_action_assigned_to, required=False) or cur["next_action_assigned_to"],
                           "state": _check_state(db, new_state),
                           "resolution_kind": cur["resolution_kind"]},
                       originator=who)
    return f"escalation #{escalation_id} v{merged['version']} -> state={new_state!r}"


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
                                "resolution_kind": cur["resolution_kind"]},
                       originator=who)
    return f"escalation #{escalation_id} v{merged['version']} CORRECTED -> state={resolved_state!r}"


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
    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"resolution": resolution},
                       envelope={"state": _check_state(db, "completed"), "next_action": None,
                                "next_action_assigned_to": cur["next_action_assigned_to"],
                                "resolution_kind": "self_correctable"},
                       originator=who)
    return f"escalation #{escalation_id} v{merged['version']} resolved (self_correctable) -> completed"


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
    new_state = "in-progress" if cur["state"] == "raised" else cur["state"]
    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"tried": tried},
                       envelope={"state": _check_state(db, new_state), "next_action": "review",
                                "next_action_assigned_to": cur["next_action_assigned_to"],
                                "resolution_kind": "decision_required"},
                       originator=who)
    return (f"escalation #{escalation_id} v{merged['version']} converted to decision_required "
           f"(state={new_state!r})")


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
    module docstring) -- straight `id` order."""
    ph = ",".join("?" * len(_OPEN_STATES))
    rows = db.rows(f"SELECT * FROM escalation WHERE state IN ({ph}) "
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
                                   "short_description") if h[c]]
            summary = "; ".join(f"{c}: {_gist(h[c], 50)}" for c in changed) or "_(state/assignee only)_"
            L.append(f"| {h['version']} | {h['state']} | {h['next_action'] or ''} | "
                     f"{h['originator'] or ''} | {summary} | {h['answered_at']} |")
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
        "ORDER BY answered_at DESC LIMIT 15")
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


def _extract_flag(args: list[str], name: str) -> tuple[list[str], str | None]:
    prefix = f"--{name}="
    remaining, value = [], None
    for a in args:
        if a.startswith(prefix):
            value = a[len(prefix):]
        else:
            remaining.append(a)
    return remaining, value


def main() -> int:
    cfg = Cfg()
    db = Db(cfg)
    argv = sys.argv[1:]
    try:
        return _dispatch(cfg, db, argv)
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
        question = " ".join(rest)
        new_id = raise_new(cfg, db, question, source or "claude", etype=etype or "task",
                           comment=comment or question, context=context,
                           assigned_to=assigned_to or "Researcher",
                           resolution_kind=resolution_kind,
                           originator=_require_flag(originator, "originator"))
        print(f"  raised — #{new_id}. Update with: python -m iba.app.lib.escalation update {new_id} ...")
    elif len(argv) >= 2 and argv[0] == "resolve-self-correctable":
        rest, resolution = _extract_flag(argv[2:], "resolution")
        rest, originator = _extract_flag(rest, "originator")
        print("  " + resolve_self_correctable(cfg, db, int(argv[1]),
                                              _require_flag(resolution, "resolution"),
                                              originator=_require_flag(originator, "originator")))
    elif len(argv) >= 2 and argv[0] == "escalate-to-decision":
        rest, tried = _extract_flag(argv[2:], "tried")
        rest, originator = _extract_flag(rest, "originator")
        print("  " + escalate_to_decision(cfg, db, int(argv[1]),
                                          _require_flag(tried, "tried"),
                                          originator=_require_flag(originator, "originator")))
    elif len(argv) >= 2 and argv[0] == "update":
        rest, next_action = _extract_flag(argv[2:], "next-action")
        rest, assigned_to = _extract_flag(rest, "assigned-to")
        rest, state = _extract_flag(rest, "state")
        rest, resolution = _extract_flag(rest, "resolution")
        rest, tried = _extract_flag(rest, "tried")
        rest, originator = _extract_flag(rest, "originator")
        rest, context = _extract_flag(rest, "context")
        comment = " ".join(rest) or None
        print("  " + update(cfg, db, int(argv[1]), next_action=next_action,
                            next_action_assigned_to=assigned_to, comment=comment, context=context,
                            tried=tried, resolution=resolution,
                            state=state,
                            originator=_require_flag(originator, "originator")))
    elif len(argv) >= 2 and argv[0] == "history":
        # id-prefixed stem, 2026-08-26 (escalation #857) -- matches handlers/reports.py's copy
        path = pathlib.Path(cfg.required_setting("escalation.history_report_dir")) / f"{argv[1]}-escalation-history.md"
        out = write_history_report(cfg, db, int(argv[1]), path)
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
        print("  " + correction(cfg, db, int(argv[1]), short_description=short_description,
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
             "[--context=...]"
             " | update <id> --originator=Claude|Researcher [--next-action=...] [--assigned-to=...] "
             "[--state=...] [--resolution=...] [--tried=...] "
             "[--context=...] [comment...]"
             " | correction <id> --originator=Claude|Researcher — ERROR CORRECTION ONLY, works in "
             "any state, unlike update: [--short-description=...] [--next-action=...] "
             "[--assigned-to=...] [--state=...] [--resolution=...] "
             "[--tried=...] [--context=...] [comment...]")
    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
