"""escalation.py — util.escalation. The authoritative record of open items in the project: errors,
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
  - D14: new `from_id` column (immutable, set only at Raise) -- which item this one was spawned
    from. `cfg_escalation_requirement` enforces it (when set) references a real row, isn't
    self-referential, and is paired with `related_activity`.
  - D25: two-stage approval is now an AUTHORITY check, not an identity check -- `approved` is
    refused only if the caller differs from whoever `ready_for_approval` assigned the item to (the
    old same-party refusal wrongly blocked legitimate self-authorisation).
  - D26: `update()` refuses to attach `comment`/`context`/`tried` while the resulting state would
    still be `raised` -- work has to be explicitly moved off `raised` first
    (`cfg_escalation_requirement`, `check_kind='not_raised_with_content'`).
  - D27 (config only, `cfg_escalation_transition`): `ready_for_approval` now has its own explicit
    transition row, rather than relying on the incidental `assignee_changed` rule.
  - D3: the crash-wrapper (`main()`) now sets `from_id` to whatever item a failing `update`/
    `history` command was operating on.
  - `cfg_escalation_requirement` gained a `check_kind` column (`field_required` — the pre-existing
    implicit behaviour, now named — plus `not_raised_with_content`/`exists`/`not_self`).

CLI (module path: iba.app.lib.escalation, invoked as `python -m iba.app.lib.escalation`):
    python -m iba.app.lib.escalation list
    python -m iba.app.lib.escalation answer-run <run_id> <approve|reject|revise|hold|noted>
        --by=Claude|Researcher [--resolution=...] [comment words...]
    python -m iba.app.lib.escalation raise <question...>
        --originator=Claude|Researcher [--source=claude|researcher] [--assigned-to=Claude|Researcher]
        [--type=task|...] [--related-activity=...] --comment=...
        --resolution-kind=decision_required|self_correctable
    python -m iba.app.lib.escalation resolve-self-correctable <id> --originator=Claude
        --resolution=... — closes a self_correctable item. No AnswerRun, no decision vocabulary
        (escalation #798/#799): Claude fixes it, states the resolution, done.
    python -m iba.app.lib.escalation escalate-to-decision <id> --originator=Claude --tried=...
        — converts a self_correctable item to decision_required when a fix attempt reveals a real
        decision is needed (`tried`'s original purpose). Does not change `type`.
    python -m iba.app.lib.escalation update <id> --originator=Claude|Researcher
        [--next-action=...] [--assigned-to=...] [--state=on-hold|in-progress|closed|withdraw|supersede]
        [--resolution=...] [--related-activity=...] [--tried=...] [--from-id=...]
        [comment/context words...]
    python -m iba.app.lib.escalation correction <id> --originator=Claude|Researcher
        [--short-description=...] [--next-action=...] [--assigned-to=...] [--state=...]
        [--resolution=...] [--related-activity=...] [--tried=...] [--from-id=...]
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

# from_id sentinel (escalation #773, researcher's decision): "checked, no discoverable spawn
# parent" -- deliberately non-falsy (bool(-1) is True in Python, unlike 0) so it is genuinely
# distinguishable from NULL/unset everywhere from_id is read: _find_dangling/_find_cycles/
# _find_mismatched_pairing/the paired-requirement 'from_id_set' test/the downward-chain walk. No
# real escalation id is negative, so it can never collide with a genuine reference.
_NO_PARENT_SENTINEL = -1

# every business column on `escalation` / `escalation_history` (id/version/escalation_id excluded
# -- those are structural, not part of a snapshot's business content)
_ENVELOPE_COLS = ("state", "next_action", "next_action_assigned_to", "originator", "answered_at",
                 "resolution_kind")
_APPEND_COLS = ("comment", "context")            # escalation: cumulative. history: raw increment.
# from_id (D14): the item this one builds on -- MUTABLE, settable on Raise or Update alike
# (escalation #6 v5, researcher, 2026-08-20: "not immutable-after-raise -- researcher confirmed it
# can be re-pointed/corrected later, which also lets legacy messy chains ... be retrofitted after
# the fact"; register v7's D14 recorded this in full -- 4 cfg_escalation_requirement rows,
# action='raise'/'update' on each -- before the v9 consolidation pass silently thinned that detail
# out and the code (this session, same day) was built from the thinner text without checking back.
# Corrected 2026-08-21, escalation #763.). A REPLACE column like resolution/related_activity, not
# an immutable structural fact.
_REPLACE_COLS = ("resolution", "related_activity", "tried", "short_description", "from_id")
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
    """`values` (register v9 D14/D26) -- some conditions need to look at what the caller is
    actually supplying this transaction, not just who they are / what action they're taking."""
    if condition_key == "always":
        return True
    if condition_key == "claude_revising":
        return originator == "Claude" and checked_action == "revise"
    if condition_key == "from_id_set":                        # D14
        return bool(values.get("from_id"))
    if condition_key == "has_content":                         # D26
        return bool(values.get("comment") or values.get("context") or values.get("tried"))
    raise ValueError(f"unknown cfg_escalation_requirement.condition_key {condition_key!r}")


def _check_requirements(db: Db, action: str, *, originator: str, checked_action: str | None,
                        values: dict, self_id: int | None = None) -> None:
    """Raises ValueError on the first unmet requirement. `values` = the field->value the caller is
    actually supplying this transaction (already-merged where relevant, e.g. resolution). `check_kind`
    (register v9 D14/D25/D26 -- column added alongside these rules, previously only 'field_required'
    existed implicitly) selects which comparison runs; `self_id` is the item's own id, needed by
    `not_self` (D14) -- None at Raise (the new id does not exist yet, so self-reference is moot)."""
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
        elif kind == "exists":                                 # D14
            if (field_val and field_val != _NO_PARENT_SENTINEL
                    and not db.rows("SELECT 1 FROM escalation WHERE id=?", (field_val,))):
                raise ValueError(r["message"])
        elif kind == "not_self":                               # D14
            if field_val and self_id is not None and field_val == self_id:
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
    `comment`/`originator`/`from_id` unset (NULL), even though `cfg_escalation_requirement` states
    `comment` is required "always" at Raise, with no carve-out for the dispatcher shape, and D14's
    -1 no-parent sentinel (escalation #773) was never applied here either -- #787 was the live
    example. Fixed by ALWAYS populating all three, not by calling `_check_requirements()` (which
    raises on failure): this function already fires from inside crash/pause handling
    (`run.py`), where the module's own long-standing rule for `_sanitise_dispatcher_title` applies
    equally -- "raising here would mask the real crash. Sanitise instead of reject, never lose
    data." `comment` reuses `tried` (every real call site already passes a real, non-empty
    explanation there -- the same content a comment is meant to hold, e.g. "ran the full
    validation report -- {out}"); `originator` is 'Claude' (every current call site is invoked by
    Claude Code, and 'Claude'/'Researcher' are the only two values `cfg_enum
    escalation_assignee` allows -- there is no third 'system' option); `from_id` is the sentinel.
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
        "resolution": None, "related_activity": at_step, "from_id": _NO_PARENT_SENTINEL,
        "next_action_assigned_to": _check_assignee(db, assigned_to), "originator": "Claude"}
    return _create(db.cfg, db, **fields)


def pending_for_run(db: Db, run_id: str):
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
    rows = db.rows(
        "SELECT * FROM escalation WHERE at_step=? AND state='raised' AND short_description LIKE ? "
        "ORDER BY id DESC LIMIT 1", (at_step, f"%{stable_key}%"))
    return rows[0] if rows else None


def answer_for_run(cfg: Cfg, db: Db, run_id: str, decision: str, comment: str | None = None,
                   *, answered_by: str, resolution: str | None = None) -> str:
    """Record the decision on a run-scoped (dispatcher-tied) escalation. `answered_by` is required,
    no default (escalation-rebuild-design-v1 sec6)."""
    decision = decision.lower()
    rows = pending_for_run(db, run_id)
    if not rows:
        return f"no pending escalation for run {run_id!r}"
    esc_row = rows[0]
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
             related_activity: str | None = None, assigned_to: str = "Claude",
             from_id: int | None = None, resolution_kind: str | None = None,
             *, originator: str) -> int:
    """Raise -- a new MANUAL item. `originator` is required, no default. `comment`/
    `short_description` requirements come from cfg_escalation_requirement (action='raise'), as does
    the `from_id`/`related_activity` pairing check (D14) when `from_id` is supplied.

    `resolution_kind` (escalation #798/#799): `decision_required` or `self_correctable`, required
    at Raise (`cfg_escalation_requirement`). If `decision_required` and `etype` isn't `notice`
    (which never enters the decision machinery at all), `type` is forced to `issue` regardless of
    what `etype` was passed -- `decision_required` items always use the issue vocabulary
    (`cfg_behaviour_rule 'decision-points-are-terminal-not-inline'`).

    D12 (register v9, type-keyed Raise defaults): only `notice` is special -- it closes on arrival
    (`state='closed'`, `next_action=NULL`), never entering the review/decision machinery. Every
    other type (`task`/`issue`/`run_error`/`config`) defaults identically: `state='raised'`,
    `next_action='review'`."""
    checked_type = _check_type(db, etype)
    checked_kind = _check_resolution_kind(db, resolution_kind) if resolution_kind else None
    if checked_kind == "decision_required" and checked_type != "notice":
        checked_type = "issue"
    _check_requirements(db, "raise", originator=originator or "", checked_action=None,
                        values={"comment": comment, "short_description": short_description,
                               "from_id": from_id, "related_activity": related_activity,
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
        "related_activity": related_activity, "from_id": from_id,
        "resolution_kind": checked_kind,
        "next_action_assigned_to": _check_assignee(db, assigned_to),
        "originator": _check_assignee(db, originator)}
    return _create(cfg, db, **fields)


def update(cfg: Cfg, db: Db, escalation_id: int, *, next_action: str | None = None,
          next_action_assigned_to: str | None = None, comment: str | None = None,
          context: str | None = None, tried: str | None = None, resolution: str | None = None,
          related_activity: str | None = None, state: str | None = None,
          from_id: int | None = None, originator: str) -> str:
    """Update -- every subsequent change to a MANUAL item. `originator` is required, no default.
    Two-stage approval separation of duties: the party that sets `approved` must differ from the
    party that most recently set `ready_for_approval` on this item.

    `from_id` (D14) is settable HERE too, not just at Raise (escalation #6 v5, researcher,
    2026-08-20; corrected 2026-08-21 after being built immutable, escalation #763) -- an existing
    item can be re-pointed/corrected later, letting a messy legacy chain be retrofitted after the
    fact.

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
    if checked_action == "approved":
        rfa_assigned_to = _last_next_action_assigned_to(db, escalation_id, "ready_for_approval")
        if rfa_assigned_to and who != rfa_assigned_to:
            return (f"escalation #{escalation_id}: {who} cannot set 'approved' -- "
                   f"'ready_for_approval' assigned this to {rfa_assigned_to!r}; only "
                   f"{rfa_assigned_to} may approve it (authority check, not identity -- D25).")

    if checked_action == "ready_for_approval":
        _check_requirements(db, "ready_for_approval", originator=who, checked_action=checked_action,
                            values={"resolution": new_resolution})
    if checked_action == "approved":
        _check_requirements(db, "approved", originator=who, checked_action=checked_action,
                            values={"resolution": new_resolution})
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
    # D14 (corrected 2026-08-21, escalation #763): from_id/related_activity checks (exists/
    # not_self/paired) now also apply here, not just at Raise -- same `action='update'` rows,
    # checked in the same call. `related_activity` falls back to the CURRENT value when this call
    # isn't itself changing it, so re-pointing from_id alone on an item that already has a
    # related_activity doesn't wrongly fail the pairing check.
    _check_requirements(db, "update", originator=who, checked_action=checked_action,
                        values={"state": new_state, "comment": comment, "context": context,
                               "tried": tried, "from_id": from_id,
                               "related_activity": related_activity if related_activity is not None
                                                   else cur["related_activity"]},
                        self_id=escalation_id)

    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"comment": comment, "context": context, "tried": tried,
                              "resolution": resolution, "related_activity": related_activity,
                              "from_id": from_id},
                       envelope={
                           "next_action": checked_action if checked_action is not None else cur["next_action"],
                           "next_action_assigned_to": _check_assignee(db, next_action_assigned_to, required=False) or cur["next_action_assigned_to"],
                           "state": _check_state(db, new_state),
                           "resolution_kind": cur["resolution_kind"]},
                       originator=who)
    return f"escalation #{escalation_id} v{merged['version']} -> state={new_state!r}"


def correction(cfg: Cfg, db: Db, escalation_id: int, *, short_description: str | None = None,
              comment: str | None = None, context: str | None = None, tried: str | None = None,
              resolution: str | None = None, related_activity: str | None = None,
              state: str | None = None, next_action: str | None = None,
              next_action_assigned_to: str | None = None, from_id: int | None = None,
              originator: str) -> str:
    """Correction — escalation #774 v2, researcher verbatim: "create a copy of update transaction
    as Correction and allow the Correction transaction to update any column in any state... ensure
    that this is update in the documentation and that correction is stated as only to be used for
    error correction."

    ★ ERROR CORRECTION ONLY — not a normal workflow action. Use Update for every ordinary change
    (comments, decisions, reassignment, state changes); use Correction only to fix something
    already recorded wrong (a wrong from_id, a bad title, a typo in a resolution). Correction does
    NOT advance an item through its lifecycle — state/next_action are taken EXACTLY as given, never
    auto-derived via cfg_escalation_transition, and default to the item's CURRENT values (carried
    forward unchanged) when omitted, which is the normal case: most corrections touch content, not
    workflow.

    Differs from `update()` in exactly the two ways the researcher asked for, nothing more:
    1. No `_OPEN_STATES` gate — works on closed/completed/withdraw/supersede items, which `update()`
       structurally refuses (escalation #774's own finding; 9 of the 10 `from_id` repairs in #767
       needed a one-off migration script for exactly this reason — this replaces that class of
       workaround with a real, sanctioned mechanism).
    2. `short_description` is a real parameter — `update()` has none at all (escalation #10's
       finding; `_REPLACE_COLS` already lists it as an eligible delta column, nothing before this
       ever wired it through). Still subject to the same title-shape spec as Raise (#759's
       guardrail) — a Correction cannot write an over-length/dashed/multi-line title either.

    Deliberately NOT copied from `update()`: the D25 same-approval-authority check and the D26
    raised-state content guard — both are workflow-transition safeguards, not data-integrity ones,
    and a correction has to be able to fix ANY state (including a `raised` item with a wrong
    title) without being routed through the two-stage approval machinery. The `from_id`
    exists/not_self checks (D14) DO still apply — a correction should never introduce a genuinely
    broken reference — but `-1` (escalation #773's sentinel, "checked, no discoverable parent") is
    accepted without an `exists` lookup, since it is deliberately not a real escalation id."""
    cur = _current(db, escalation_id)
    if not cur["run_id"].startswith("MANUAL-"):
        return (f"escalation #{escalation_id} is dispatcher-tied (run_id {cur['run_id']!r}), not "
               f"manual -- Correction only applies to manual items")
    who = _check_assignee(db, originator)

    if from_id is not None and from_id != _NO_PARENT_SENTINEL:
        if from_id == escalation_id:
            raise ValueError(f"from_id cannot equal this item's own id ({escalation_id})")
        if not db.rows("SELECT 1 FROM escalation WHERE id=?", (from_id,)):
            raise ValueError(f"from_id={from_id} does not reference an existing escalation")

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
                              "resolution": resolution, "related_activity": related_activity,
                              "from_id": from_id, "short_description": short_description},
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


# D15 (register v9) -- the report exception categories, over the WHOLE table (not just open items):
# these are referential-integrity concerns about the from_id/related_activity graph, so a stale
# historical broken link is still worth surfacing even once the item itself is closed. Config side
# is D4's cfg_report_section rows; this is the detection logic those sections need.
import re as _re


def _link_graph(db: Db) -> dict[int, dict]:
    return {r["id"]: dict(r) for r in db.rows("SELECT id, from_id, related_activity FROM escalation")}


def _find_cycles(graph: dict[int, dict]) -> list[list[int]]:
    """Following from_id pointers (id -> from_id -> from_id -> ...) should terminate -- from_id is
    meant to be a DAG pointing strictly at an earlier item. A cycle is a data bug."""
    found = []
    for start in graph:
        chain, cur = [start], start
        while True:
            nxt = graph.get(cur, {}).get("from_id")
            if not nxt:
                break
            if nxt in chain:
                found.append(chain + [nxt])
                break
            chain.append(nxt)
            cur = nxt
            if cur not in graph:
                break
    return found


def _find_dangling(graph: dict[int, dict]) -> list[tuple[int, int]]:
    """from_id set but pointing at an id that doesn't exist. Excludes _NO_PARENT_SENTINEL (-1,
    escalation #773) -- a deliberate "checked, no discoverable spawn parent" marker, not a broken
    reference; flagging it here would recreate exactly the noise #773 was raised to avoid."""
    return [(i, r["from_id"]) for i, r in graph.items()
           if r["from_id"] and r["from_id"] != _NO_PARENT_SENTINEL and r["from_id"] not in graph]


def _find_mismatched_pairing(graph: dict[int, dict]) -> list[int]:
    """from_id set but related_activity is not -- the D14 pairing rule, checked defensively over
    ALL rows (replayed/pre-enforcement data may violate it even though new writes can't)."""
    return sorted(i for i, r in graph.items() if r["from_id"] and not r["related_activity"])


def _find_missing_link(graph: dict[int, dict]) -> list[tuple[int, int]]:
    """related_activity's free-text '#NNN' mentions (the same convention write_history_report
    already follows to walk related items) that don't resolve to a real id -- distinct from
    `dangling`, which is the structured from_id column, not this free-text convention."""
    out = []
    for i, r in graph.items():
        for m in _re.findall(r"#(\d+)", r["related_activity"] or ""):
            ref = int(m)
            if ref not in graph:
                out.append((i, ref))
    return out


def _find_incoherent_link(graph: dict[int, dict]) -> list[tuple[int, int]]:
    """Advisory heuristic (D15: no tunable threshold built yet -- only if a dry run shows it's
    needed): A's related_activity names #B, B is a real item, A/B are not in a from_id parent-child
    relationship (legitimately one-directional), and B's own related_activity does NOT name A back
    -- a one-way reference where a mutual one looks intended."""
    out = []
    for i, r in graph.items():
        for m in _re.findall(r"#(\d+)", r["related_activity"] or ""):
            ref = int(m)
            if ref == i or ref not in graph:
                continue
            if r["from_id"] == ref or graph[ref].get("from_id") == i:
                continue
            back = {int(x) for x in _re.findall(r"#(\d+)", graph[ref]["related_activity"] or "")}
            if i not in back:
                out.append((i, ref))
    return out


def write_list_report(cfg: Cfg, db: Db, path: pathlib.Path) -> tuple[pathlib.Path, list]:
    """Open items, grouped by related_activity, WITH full history inline underneath each one --
    the `comment`/`context` columns here are now the true per-version DELTA (blank when that
    version didn't touch the field), not a cumulative gist (escalation-rebuild-design-v1 sec4.2)."""
    ph = ",".join("?" * len(_OPEN_STATES))
    rows = db.rows(f"SELECT * FROM escalation WHERE state IN ({ph}) "
                   f"ORDER BY related_activity, id", _OPEN_STATES)
    n_on_hold = sum(1 for r in rows if r["state"] == "on-hold")
    n_in_progress = sum(1 for r in rows if r["state"] == "in-progress")
    n_active = len(rows) - n_on_hold - n_in_progress
    objectives = cfg.setting("escalation.control_objectives", "")
    process = cfg.setting("escalation.control_process", "")
    L = ["# Open escalations", "",
        f"> {objectives}. {process}.".strip(), "",
        f"> Generated by `Escalation.ps1 -Action List`. {len(rows)} open escalation(s) "
        f"({n_active} active, {n_in_progress} in-progress, {n_on_hold} on-hold), grouped by "
        f"`related_activity`, full history inline (each row = that version's own changes).", ""]
    if not rows:
        L.append("_no open escalations_")
    for r in rows:
        hist = db.rows("SELECT * FROM escalation_history WHERE escalation_id=? ORDER BY version",
                       (r["id"],))
        L.append(f"## #{r['id']} v{r['version']} — {r['state']} — {r['short_description']}")
        L.append(f"type={r['type']} assigned_to={r['next_action_assigned_to']} "
                 f"related_activity={r['related_activity'] or ''}")
        L.append("")
        L.append("| v | state | next_action | originator | changed this version | at |")
        L.append("|---|---|---|---|---|---|")
        for h in hist:
            changed = [c for c in ("comment", "context", "resolution", "tried",
                                   "short_description", "related_activity") if h[c]]
            summary = "; ".join(f"{c}: {_gist(h[c], 50)}" for c in changed) or "_(state/assignee only)_"
            L.append(f"| {h['version']} | {h['state']} | {h['next_action'] or ''} | "
                     f"{h['originator'] or ''} | {summary} | {h['answered_at']} |")
        L.append("")

    # D15 exception sections (cfg_report_section: cycle/dangling/mismatched_pairing/missing_link/
    # incoherent_link) -- over the whole table, see _link_graph's docstring group above.
    graph = _link_graph(db)
    cycles = _find_cycles(graph)
    dangling = _find_dangling(graph)
    mismatched = _find_mismatched_pairing(graph)
    missing = _find_missing_link(graph)
    incoherent = _find_incoherent_link(graph)

    L += ["## Cycle", ""]
    L.append("_none_" if not cycles else "\n".join(
        f"- {' -> '.join(f'#{c}' for c in chain)}" for chain in cycles))
    L += ["", "## Dangling", ""]
    L.append("_none_" if not dangling else "\n".join(
        f"- #{i} from_id={fid} does not exist" for i, fid in dangling))
    L += ["", "## Mismatched pairing", ""]
    L.append("_none_" if not mismatched else "\n".join(
        f"- #{i} has from_id set but no related_activity" for i in mismatched))
    L += ["", "## Missing link", ""]
    L.append("_none_" if not missing else "\n".join(
        f"- #{i} related_activity mentions #{ref}, which does not exist" for i, ref in missing))
    L += ["", "## Incoherent link", ""]
    L.append("_none_" if not incoherent else "\n".join(
        f"- #{i} names #{ref} in related_activity; #{ref} does not name #{i} back "
        f"(advisory heuristic, D15)" for i, ref in incoherent))
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
        "SELECT id, short_description, state, related_activity, resolution, answered_at "
        "FROM escalation WHERE state IN ('completed','closed','withdraw','supersede') "
        "ORDER BY answered_at DESC LIMIT 15")
    L += ["## Recently resolved (last 15)", ""]
    if not resolved:
        L.append("_none yet_")
    else:
        L += ["| # | short_description | state | related activity | resolution | answered |",
             "|---|---|---|---|---|---|"]
        for r in resolved:
            sd = str(r["short_description"]).replace("|", "\\|")
            res = str(r["resolution"]).replace("|", "\\|").replace("\n", " ") if r["resolution"] \
                else "_(see comment -- notice-type items can't carry a separate resolution)_"
            if len(res) > 200:
                res = res[:200] + "… (full text in escalation.resolution, id " + str(r["id"]) + ")"
            L.append(f"| {r['id']} | {sd} | {r['state']} | {r['related_activity']} | {res} | "
                     f"{r['answered_at']} |")

    reportkit.archive_before_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(L).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
    return path, rows


def write_history_report(cfg: Cfg, db: Db, escalation_id: int, path: pathlib.Path) -> pathlib.Path:
    """Deep-history report for one item -- its full history, plus the same for every item its
    related_activity text names or that names it back. Every column shown: envelope fields always,
    delta fields only when this version actually set them (escalation-rebuild-design-v1 sec4.1)."""
    seen: set[int] = set()
    queue = [escalation_id]
    L = ["# Escalation deep history", ""]
    while queue:
        eid = queue.pop(0)
        if eid in seen:
            continue
        seen.add(eid)
        rows = db.rows("SELECT * FROM escalation WHERE id=?", (eid,))
        if not rows:
            continue
        r = rows[0]
        hist = db.rows("SELECT * FROM escalation_history WHERE escalation_id=? ORDER BY version",
                       (eid,))
        L.append(f"## #{eid} — {r['short_description']}")
        L.append(f"type={r['type']} source={r['source']} related_activity={r['related_activity'] or ''} "
                 f"from_id={r['from_id'] or ''}")
        L.append("")
        for h in hist:
            L.append(f"**v{h['version']}** ({h['answered_at']}, {h['originator'] or '?'}) "
                     f"state={h['state']} next_action={h['next_action'] or ''} "
                     f"assigned_to={h['next_action_assigned_to'] or ''}")
            for c in ("short_description", "comment", "context", "resolution", "tried",
                     "related_activity"):
                if h[c]:
                    label = c.replace("_", " ")
                    L.append(f"> **{label} (set this version):** {h[c]}")
            L.append("")
        # D5 item 6 / D4's "downward_chain" section -- items SPAWNED FROM this one (from_id child),
        # distinct from the related_activity-text traversal below (a lateral/named-reference walk).
        children = db.rows("SELECT id FROM escalation WHERE from_id=? ORDER BY id", (eid,))
        if children:
            L.append(f"**downward chain (spawned from #{eid}):** " +
                     ", ".join(f"#{c['id']}" for c in children))
            L.append("")
            queue.extend(c["id"] for c in children)
        if r["from_id"]:
            queue.append(r["from_id"])
        if r["related_activity"]:
            others = db.rows(
                "SELECT id FROM escalation WHERE related_activity LIKE ? AND id != ?",
                (f"%#{eid}%", eid))
            queue.extend(o["id"] for o in others)
            import re
            for m in re.findall(r"#(\d+)", r["related_activity"] or ""):
                queue.append(int(m))
    reportkit.archive_before_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")
    return path


def _extract_flag(args: list[str], name: str) -> tuple[list[str], str | None]:
    prefix = f"--{name}="
    remaining, value = [], None
    for a in args:
        if a.startswith(prefix):
            value = a[len(prefix):]
        else:
            remaining.append(a)
    return remaining, value


def _crash_from_id(argv: list[str]) -> int | None:
    """D3 (register v9): the crash-wrapper's own from_id-awareness -- whatever escalation id the
    failing command was OPERATING ON, if any (`update <id> ...` / `history <id>`). `raise ...` has
    no target yet (the crash means the new row was never created) -- from_id stays None there."""
    if len(argv) >= 2 and argv[0] in ("update", "history"):
        try:
            return int(argv[1])
        except ValueError:
            return None
    return None


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
                     related_activity="escalation-cli-crash", assigned_to="Claude",
                     from_id=_crash_from_id(argv),
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
        path = pathlib.Path(cfg.setting("escalation.list_report_path",
                                        "iba/app/reports/escalation-list.md"))
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
        rest, related_activity = _extract_flag(rest, "related-activity")
        rest, originator = _extract_flag(rest, "originator")
        rest, comment = _extract_flag(rest, "comment")
        rest, context = _extract_flag(rest, "context")
        rest, from_id = _extract_flag(rest, "from-id")
        rest, resolution_kind = _extract_flag(rest, "resolution-kind")
        question = " ".join(rest)
        new_id = raise_new(cfg, db, question, source or "claude", etype=etype or "task",
                           comment=comment or question, context=context,
                           assigned_to=assigned_to or "Researcher",
                           related_activity=related_activity,
                           from_id=int(from_id) if from_id else None,
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
        rest, related_activity = _extract_flag(rest, "related-activity")
        rest, tried = _extract_flag(rest, "tried")
        rest, originator = _extract_flag(rest, "originator")
        rest, context = _extract_flag(rest, "context")
        rest, from_id = _extract_flag(rest, "from-id")
        comment = " ".join(rest) or None
        print("  " + update(cfg, db, int(argv[1]), next_action=next_action,
                            next_action_assigned_to=assigned_to, comment=comment, context=context,
                            tried=tried, resolution=resolution, related_activity=related_activity,
                            state=state, from_id=int(from_id) if from_id else None,
                            originator=_require_flag(originator, "originator")))
    elif len(argv) >= 2 and argv[0] == "history":
        path = pathlib.Path(cfg.setting("escalation.history_report_dir",
                                        "iba/app/reports")) / f"escalation-{argv[1]}-history.md"
        out = write_history_report(cfg, db, int(argv[1]), path)
        print(f"  -> {out}")
    elif len(argv) >= 2 and argv[0] == "correction":
        rest, next_action = _extract_flag(argv[2:], "next-action")
        rest, assigned_to = _extract_flag(rest, "assigned-to")
        rest, state = _extract_flag(rest, "state")
        rest, resolution = _extract_flag(rest, "resolution")
        rest, related_activity = _extract_flag(rest, "related-activity")
        rest, tried = _extract_flag(rest, "tried")
        rest, originator = _extract_flag(rest, "originator")
        rest, context = _extract_flag(rest, "context")
        rest, from_id = _extract_flag(rest, "from-id")
        rest, short_description = _extract_flag(rest, "short-description")
        comment = " ".join(rest) or None
        print("  " + correction(cfg, db, int(argv[1]), short_description=short_description,
                                next_action=next_action, next_action_assigned_to=assigned_to,
                                comment=comment, context=context, tried=tried,
                                resolution=resolution, related_activity=related_activity,
                                state=state, from_id=int(from_id) if from_id else None,
                                originator=_require_flag(originator, "originator")))
    else:
        print("usage: python -m iba.app.lib.escalation list"
             " | history <id>"
             " | answer-run <run_id> <approve|reject|revise|hold|noted> --by=Claude|Researcher "
             "[--resolution=...] [comment...]"
             " | raise <short_description...> --comment=... --originator=Claude|Researcher "
             "[--source=...] [--assigned-to=...] [--type=...] [--related-activity=...] "
             "[--context=...] [--from-id=...]"
             " | update <id> --originator=Claude|Researcher [--next-action=...] [--assigned-to=...] "
             "[--state=...] [--resolution=...] [--related-activity=...] [--tried=...] "
             "[--context=...] [--from-id=...] [comment...]"
             " | correction <id> --originator=Claude|Researcher — ERROR CORRECTION ONLY, works in "
             "any state, unlike update: [--short-description=...] [--next-action=...] "
             "[--assigned-to=...] [--state=...] [--resolution=...] [--related-activity=...] "
             "[--tried=...] [--context=...] [--from-id=...] [comment...]")
    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
