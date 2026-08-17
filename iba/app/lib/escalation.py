"""escalation.py — util.escalation. The only sanctioned researcher interaction.

**Reset 2026-08-16** (researcher's "iba table review" + `export.cfg_settings shortcomings.csv`,
confirmed in `Workflow/Chat_responses/response-tablereviewresponse v1`; full context
`outputs/markdown/iba-table-review-response-v1-20260816.md`). Column shape changed:
`word`->`source` (now required), `question`->`short_description`, `preset`->`context`,
`answer`->`next_action` (expanded: approve|reject|revise|hold|noted); new columns `resolution`
(what was actually done — nothing previously recorded this), `related_activity`,
`next_action_assigned_to` (Claude|Researcher), `answered_by` (Claude|Researcher, required by
convention whenever a row reaches a terminal state). `state` expanded: raised|re-assign|on-hold|
closed|withdraw|completed. Own rule table `cfg_escalation` (duplicate-suppression,
source-classification, module-blocking [not yet wired], resolution-precedence, chat-routing).
Migration: `iba/app/migration/escalation_reset_v1_20260816.py`.

**Explicit recalibration, same source**: configmaint.propose-style approve/reject/revise gating is
NOT the default path for every escalation — "not all escalations goes through propose / approved,
lots of it would raise, schedule, notify" (researcher, 2026-08-16). Use `raise_manual` +
`resolution`/`next_action='noted'` freely for items that just need recording, not a decision gate.

The principle (from the design docs): the app tries to resolve; if it cannot, it
PAUSES the run, asks the researcher, and RESUMES at the same point when answered —
a pause, not a fork. State is durable (in the DB), so a pause survives the process:
the run stops, and resume is a fresh invocation that reads the answer.

    raise_(...)         record a pause (a step names the question + context details)
    pending_for_word    the open escalation for a word, if any
    answer_for_word     the researcher's decision (approve/reject); also advances word status

Word-scoped functions above are the original (registry.create) shape — unchanged in spirit.
RUN-scoped functions below are the general shape for anything that isn't about a word
(e.g. a configuration_maintenance proposal), added 2026-07-21 per the researcher's rule
that every escalation must offer three outcomes, not yes/no:

    pending_for_run     the open escalation for a run, if any
    answered_for_run     the answered escalation for a run at a step, if any
    answer_for_run       approve | reject | revise | hold | noted (+ optional comment/resolution)

CLI (module path: iba.app.lib.escalation, invoked as `python -m iba.app.lib.escalation`):
    python -m iba.app.lib.escalation list
    python -m iba.app.lib.escalation answer <word> <approve|reject> [--by=Claude|Researcher]
    python -m iba.app.lib.escalation answer-run <run_id> <approve|reject|revise|hold|noted>
        [--by=Claude|Researcher] [--resolution=...] [comment words...]
    python -m iba.app.lib.escalation raise <question...>
        [--source=claude|researcher] [--assigned-to=Claude|Researcher] [--type=task|...]
        [--related-activity=...] [--reference-doc=...]  (required together — see
        cfg_escalation.document_reference_grouping; omit both for a standalone item)

Added 2026-07-23 for the researcher's backlog-of-work-for-Claude workflow — a manual escalation
doubles as a work instruction, not only a design decision awaiting approval. Run-scoped/manual only
(same boundary as answer-run vs. answer):
    python -m iba.app.lib.escalation edit <run_id> <new question...>     -- replace the wording
    python -m iba.app.lib.escalation pause <run_id> [comment...]         -- set aside, out of the active queue
    python -m iba.app.lib.escalation resume <run_id>                    -- back into the active queue
    python -m iba.app.lib.escalation retract <run_id> [comment...]      -- withdraw, not a decision
    python -m iba.app.lib.escalation reassign <run_id> <Claude|Researcher> [comment...]
                                                                          -- bounce to the other party
"""

from __future__ import annotations

import datetime
import json
import pathlib
import sys

from . import reportkit
from .cfg import Cfg
from .db import Db

_OPEN_STATES = ("raised", "re-assign", "on-hold", "in-progress")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _grant(cfg: Cfg, table: str):
    if table not in cfg.may_write("escalation"):
        raise PermissionError(f"write-grant violation: 'escalation' may not write {table!r}")


def word_source(word: str) -> str:
    return f"new-word: {word}"


def _terminal_state_for(next_action: str, is_manual: bool = False) -> str:
    """Which `state` a decision resolves to — NOT uniformly 'completed'. Found live 2026-08-16
    (researcher, reviewing USER-GUIDE.md §4.2's staleness, asked directly whether hold/noted were
    actually wired into the app, not just documented): every `answer_for_run`/`answer_for_word`
    dispatcher-tied consumer (registry.create + 7 more handlers — candidate/cluster/configmaint/
    lexicon/narrative/passage/reports, all checked live) only branches on `decision == "approve"`/
    `"reject"`, with a fallback that treats ANYTHING else — including `hold`/`noted` — exactly like
    a rejection ('needs-revision'). Since every prior version of this function hardcoded
    `state='completed'` regardless of `next_action`, answering a real run-scoped escalation with
    `hold` or `noted` was silently mishandled as if it meant 'revise', which is not what either
    word means. Fixed here, not just documented: `approve`/`reject`/`revise` are the only three
    decision values any handler actually understands — those close to `'completed'`. `hold`
    resolves to `'on-hold'` (genuinely kept open — the underlying paused run correctly stays
    paused, not misread as a decision it wasn't). `noted` resolves to `'closed'` (acknowledged/
    dismissed, distinct from a real decision — also excluded from `answered_for_run`'s
    `state='completed'` filter, for the same reason).

    `is_manual` + the `'in-progress'` branch — added 2026-08-17, escalations #673/#674. Researcher,
    reviewing #653/#657: *"how can escalation 653 and 657 be completed, it is still in progress...
    I am not sure this is working properly."* Root cause was this exact function: `approve`/
    `revise` landing on `'completed'` unconditionally conflates "the decision is final" with "the
    task is finished" — true for a same-turn dispatcher-tied decision (`configmaint.propose`
    applies its change in the very call that resolves it), false for a MANUAL task-type escalation
    approving ongoing work. Restricted to `is_manual` ONLY — a real dispatcher-tied escalation's
    `answered_for_run`/resume-on-'completed' machinery (7 handlers, load-bearing) is UNCHANGED, or
    `configmaint.propose -RunId <id>`'s own apply-on-resume flow would break the moment this
    landed. For a MANUAL item, `approve`/`revise` now land on `'in-progress'` — "go do it", not
    "already done" — closed out for real via `complete_run()`/`Escalation.ps1 -Action Complete`,
    not by re-answering with AnswerRun."""
    if next_action == "hold":
        return "on-hold"
    if next_action == "noted":
        return "closed"
    if is_manual and next_action in ("approve", "revise"):
        return "in-progress"
    return "completed"


def _check_state(db: Db, state: str) -> str:
    """Validate a state value against cfg_enum 'escalation_state' — a real, live lookup (not a
    hardcoded Python set) so a change to the DB's enum membership is something this code actually
    responds to, per the researcher's 2026-07-23 correction (escalation #305)."""
    valid = db.cfg.enum("escalation_state")
    if state not in valid:
        raise ValueError(f"{state!r} is not a member of cfg_enum 'escalation_state' ({valid!r})")
    return state


def _check_type(db: Db, etype: str) -> str:
    """Same discipline as _check_state, for cfg_enum 'escalation_type' (task|run_error|issue|
    notice|config as of the 2026-08-16 reset)."""
    valid = db.cfg.enum("escalation_type")
    if etype not in valid:
        raise ValueError(f"{etype!r} is not a member of cfg_enum 'escalation_type' ({valid!r})")
    return etype


def _check_next_action(db: Db, next_action: str | None) -> str | None:
    if next_action is None:
        return None
    valid = db.cfg.enum("escalation_next_action")
    if next_action not in valid:
        raise ValueError(f"{next_action!r} is not a member of cfg_enum 'escalation_next_action' "
                         f"({valid!r})")
    return next_action


def _check_assignee(db: Db, who: str | None, required: bool = True) -> str | None:
    """Normalises case (Claude|Researcher) and validates against cfg_enum 'escalation_assignee'."""
    if who is None:
        if required:
            raise ValueError("answered_by is required — must be 'Claude' or 'Researcher'")
        return None
    normalised = who.strip().capitalize()
    valid = db.cfg.enum("escalation_assignee")
    if normalised not in valid:
        raise ValueError(f"{who!r} is not a member of cfg_enum 'escalation_assignee' ({valid!r})")
    return normalised


def raise_(db: Db, run_id: str, word: str, at_step: str, question: str,
           preset: dict, tried: str, etype: str = "task", assigned_to: str = "Researcher") -> int:
    """Record a pause (word-scoped — the original registry.create shape). Written under the
    dispatcher's grant (caller passes an open db). `source` is derived from `word` per the
    source-classification rule in cfg_escalation ('new-word: <word>')."""
    return db.write("escalation", {
        "run_id": run_id, "source": word_source(word), "at_step": at_step,
        "type": _check_type(db, etype), "short_description": question, "context": json.dumps(preset),
        "tried": tried, "state": _check_state(db, "raised"), "next_action": None, "answered_at": None,
        "raised_at": _now(), "resolution": None, "related_activity": at_step,
        "next_action_assigned_to": _check_assignee(db, assigned_to), "answered_by": None})


def pending_for_word(db: Db, word: str):
    """The latest un-answered escalation for a word, or None. Case-insensitive on word."""
    return db.rows(
        "SELECT * FROM escalation WHERE lower(source)=lower(?) AND state='raised' "
        "ORDER BY id DESC LIMIT 1", (word_source(word),))
    # returns a list; caller takes [0]


def answered_for_word(db: Db, word: str, at_step: str):
    """The latest COMPLETED escalation for a word at a step, or None. Case-insensitive."""
    rows = db.rows(
        "SELECT * FROM escalation WHERE lower(source)=lower(?) AND at_step=? AND state='completed' "
        "ORDER BY id DESC LIMIT 1", (word_source(word), at_step))
    return rows[0] if rows else None


def answer_for_word(cfg: Cfg, db: Db, word: str, decision: str, answered_by: str = "Researcher",
                    resolution: str | None = None) -> str:
    """Record the researcher's answer and advance the word's status accordingly.
    decision: 'approve'/'yes' -> approved, 'reject'/'no' -> rejected (yes/no accepted as aliases
    for backward compatibility with the pre-reset CLI). Case-insensitive on word.

    Deliberately restricted to approve/reject ONLY — unlike answer_for_run, `hold`/`noted`/`revise`
    have no sensible word_registry.status to map to (that enum is proposed|approved|rejected, no
    'on hold' or 'needs revision' state for a word). Found live 2026-08-16: before this check, ANY
    decision that wasn't literally 'approve' fell into `new_status = ... else 'rejected'` — meaning
    answering with `hold` would have wrongly REJECTED the word. Fixed at the source, not patched
    around."""
    rows = pending_for_word(db, word)
    if not rows:
        return f"no pending escalation for {word!r}"
    esc = rows[0]
    normalised = {"yes": "approve", "no": "reject"}.get(decision.lower(), decision.lower())
    if normalised not in ("approve", "reject"):
        return (f"{decision!r} is not valid for a word-scoped escalation — must be "
                f"'approve'/'reject' (word_registry.status has no meaning for hold/noted/revise)")
    _check_next_action(db, normalised)
    who = _check_assignee(db, answered_by)
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]},
              state=_check_state(db, _terminal_state_for(normalised)),
              next_action=normalised, resolution=resolution, answered_by=who, answered_at=_now())
    new_status = "approved" if normalised == "approve" else "rejected"
    wr = db.rows("SELECT id, word FROM word_registry WHERE lower(word)=lower(?) AND deleted=0",
                 (esc["source"].removeprefix("new-word: "),))
    if wr:
        db.update("word_registry", {"id": wr[0]["id"]}, status=new_status)
        word = wr[0]["word"]      # report the canonical stored form
    return f"escalation {esc['id']} answered {normalised!r}; {word!r} status -> {new_status}"


def _resolve_run_id(db: Db, ident: str) -> str:
    """Accept either the real `run_id` string, or the bare `escalation.id` shown as the `#`
    column in `escalation-list.md` — found 2026-07-30 when a researcher typed `-RunId 384`
    (the `#` the list report shows first, the natural thing to reference) and got "no pending
    escalation for run '384'": the report's own primary-looking column and the CLI's expected
    identifier are two different columns of the same row (`run_id` only appears buried inside
    the `scope` column, e.g. `` run `RUN-20260730_050949_853-CONFIGMAINT` ``). A real `run_id`
    always carries a non-digit prefix (`RUN-`/`MANUAL-`), so digits-only input is unambiguous
    and safe to resolve via `id`; anything else is returned unchanged, exactly as before."""
    if ident.isdigit():
        rows = db.rows("SELECT run_id FROM escalation WHERE id=?", (int(ident),))
        if rows:
            return rows[0]["run_id"]
    return ident


# ── run-scoped (general — no word, five-way next_action) ─────────────────────────
def pending_for_run(db: Db, run_id: str):
    """The latest un-answered escalation for a run, or None."""
    return db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND state='raised' "
        "ORDER BY id DESC LIMIT 1", (run_id,))
    # returns a list; caller takes [0]


def answered_for_run(db: Db, run_id: str, at_step: str):
    """The latest COMPLETED escalation for a run at a step, or None."""
    rows = db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND at_step=? AND state='completed' "
        "ORDER BY id DESC LIMIT 1", (run_id, at_step))
    return rows[0] if rows else None


def open_duplicate(db: Db, at_step: str, stable_key: str):
    """The already-OPEN (raised, unanswered) escalation for this step whose short_description
    CONTAINS `stable_key`, from any prior run_id, or None. Found 2026-08-06: a re-run of a
    self-computing advisory check (configmaint.validate — same live findings, freshly re-derived
    each call) got a brand new run_id every time, so `run.py`'s own within-run dedup
    (`answered_for_run`/the pause-continue idempotency guard) never caught it — every re-run raised
    its own duplicate escalation for the SAME still-open finding, 15+ near-identical rows piling up
    in one day. Now also the codified rule `cfg_escalation.duplicate_suppression`.

    **Matches on a substring, not the full text, on purpose** — a real bug in the first cut of
    this fix, caught immediately by actually running it twice: `configmaint.validate`'s own
    question text embeds `report_path`, which is itself freshly versioned every call
    (`CONFIG-REPORT-v28...` -> `-v29...`), so an exact-text match never matched even when the
    underlying findings were byte-for-byte identical. `stable_key` must be the caller's own
    STABLE summary (counts/labels only, no versioned path) — the caller finds it as a substring of
    the stored `short_description`, not compares the whole thing.

    Deliberately scoped to steps like `configmaint.validate`/`passage.validate`/`candidate.
    validate` (an advisory check that re-computes the same facts on every call, so an identical
    summary really does mean an identical situation) — NOT used generically in `run.py`'s own
    dispatcher, because `configmaint.propose`'s auto-generated text ("insert on cfg_write_grant —
    approve?") is deliberately generic and shared across genuinely DIFFERENT proposals
    distinguished only by their `Set` payload; a text-match dedup there would wrongly suppress
    real, distinct decisions."""
    rows = db.rows(
        "SELECT * FROM escalation WHERE at_step=? AND state='raised' AND short_description LIKE ? "
        "ORDER BY id DESC LIMIT 1", (at_step, f"%{stable_key}%"))
    return rows[0] if rows else None


def raise_manual(db: Db, question: str, tried: str | None = None, source: str = "claude",
                 etype: str = "task", assigned_to: str = "Researcher",
                 related_activity: str | None = None, reference_doc: str | None = None) -> str:
    """A researcher- or Claude-initiated item — 'flag this for later, resolve it via the same
    review workflow' — not raised BY a running step. Found 2026-07-22: raise_() always needed a
    run_id/at_step from an in-flight run; there was no way to add a standalone tracked item.
    Uses a synthetic run_id (no 'run' row exists for it — answer_for_run only queries escalation by
    run_id, so this needs no special-casing; documented, by-design FK exception, see
    `escalation_reset_v1_20260816.py`) so it answers via the exact same
    `Escalation.ps1 -Action AnswerRun -RunId <id> -Decision ...` path as every other escalation,
    and shows up in the same open-items list/report.

    `source` per `cfg_escalation.source_classification`: 'claude' or 'researcher' (lowercase, by
    convention — this is a free-text field, not itself enum-validated, so the exact casing here is
    what every future query matches against; keep it lowercase).

    `reference_doc` per `cfg_escalation.document_reference_grouping` — MECHANICALLY ENFORCED, not
    just documented: found 2026-08-16 (the researcher spotted it directly, escalation #653) that
    this rule was written the same session it was first needed and then not actually applied by the
    code raising the very escalations it governs — 14 rows landed with `context='{}'` despite the
    rule existing. `related_activity` alone is not enough to satisfy it; a non-default
    `related_activity` (a real group, not the bare 'manual' default) now REQUIRES a `reference_doc`,
    written into `context` as `{"reference_doc": "..."}`, or this raises rather than writing another
    silently ungrounded row."""
    related = related_activity or "manual"
    if related != "manual" and not reference_doc:
        raise ValueError(
            f"related_activity={related!r} groups this escalation with others, but no "
            f"reference_doc was given — cfg_escalation.document_reference_grouping requires the "
            f"planning document be recorded in `context` for any grouped item (pass "
            f"reference_doc=... or related_activity='manual' for a genuinely standalone item)")
    context = {"reference_doc": reference_doc} if reference_doc else {}
    run_id = f"MANUAL-{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d_%H%M%S_%f')}"
    _grant(db.cfg, "escalation")
    db.write("escalation", {
        "run_id": run_id, "source": source, "at_step": "manual", "type": _check_type(db, etype),
        "short_description": question, "context": json.dumps(context),
        "tried": tried or "researcher/Claude-initiated — no run to resume; a standalone tracked note",
        "state": _check_state(db, "raised"), "next_action": None, "answered_at": None,
        "raised_at": _now(), "resolution": None, "related_activity": related,
        "next_action_assigned_to": _check_assignee(db, assigned_to), "answered_by": None})
    return run_id


def answer_for_run(cfg: Cfg, db: Db, run_id: str, decision: str, comment: str | None = None,
                   answered_by: str = "Researcher", resolution: str | None = None) -> str:
    """Record the decision on a run-scoped (word-less) escalation.
    decision: 'approve' | 'reject' | 'revise' | 'hold' | 'noted' (revise carries feedback, not a
    rejection). No word_registry side-effect — the caller (e.g. configmaint.propose) acts on the
    answer itself the next time the step runs. Valid decisions come from cfg_enum
    'escalation_next_action' (a live lookup, not a hardcoded Python tuple).

    **`hold`/`noted` do NOT resolve to `state='completed'`** (see `_terminal_state_for`) — every
    dispatcher-tied consumer of `answered_for_run` (7 handlers, checked live 2026-08-16) only
    branches on `decision == "approve"`/`"reject"`, with everything else falling into a
    'needs-revision'-shaped fallback. If a real quality-check/config-proposal pause is answered
    `hold` or `noted`, the underlying paused run correctly STAYS PAUSED (visible in the open list as
    on-hold/closed, not silently misread as a rejection) — those two words only fully make sense
    for a MANUAL item with no run to resume. `approve`/`reject`/`revise` are unaffected."""
    run_id = _resolve_run_id(db, run_id)
    decision = decision.lower()
    valid_answers = cfg.enum("escalation_next_action")
    if decision not in valid_answers:
        return f"invalid decision {decision!r} — must be one of {valid_answers!r}"
    rows = pending_for_run(db, run_id)
    if not rows:
        return f"no pending escalation for run {run_id!r}"
    esc = rows[0]
    who = _check_assignee(db, answered_by)
    _grant(cfg, "escalation")
    new_state = _terminal_state_for(decision, is_manual=run_id.startswith("MANUAL-"))
    db.update("escalation", {"id": esc["id"]},
              state=_check_state(db, new_state),
              next_action=decision, comment=comment, resolution=resolution, answered_by=who,
              answered_at=_now())
    note = " — use Escalation.ps1 -Action Complete when the work is actually done" \
        if new_state == "in-progress" else ""
    return (f"escalation {esc['id']} (run {run_id!r}, step {esc['at_step']!r}) answered "
           f"{decision!r} -> {new_state}{note}" + (f" — {comment!r}" if comment else ""))


# ── edit / pause / resume / retract — added 2026-07-23 for the researcher's own backlog-of-
# items-for-Claude workflow (a manual escalation is a work instruction, not only a design decision
# needing approval). Restricted to MANUAL-prefixed run_ids ONLY (not run-scoped-in-general) --
# found while building this: a REAL dispatcher-tied escalation (configmaint.propose, candidate.
# validate, ...) checks `answered_for_run` (state='completed') and run.py's own pause-continue dedup
# checks `state='raised'` to decide whether to raise a duplicate; pausing one of those would flip
# it to `state='on-hold'`, matching NEITHER check, so re-running the underlying command before
# resuming would raise a second escalation row for the same run_id+step, not resume the real one.
# Manual items have no such downstream reader, so this cannot happen to them.
def _manual_only(run_id: str) -> str | None:
    if not run_id.startswith("MANUAL-"):
        return (f"{run_id!r} is not a manual escalation (run_id doesn't start with 'MANUAL-'). "
               f"Edit/Pause/Resume/Retract are restricted to researcher/Claude-raised items only -- "
               f"a real dispatcher-tied escalation must be answered via AnswerRun.")
    return None


def _latest_for_run(db: Db, run_id: str, states: tuple[str, ...]):
    """The latest escalation row for a run in one of `states`, or None."""
    ph = ",".join("?" * len(states))
    rows = db.rows(f"SELECT * FROM escalation WHERE run_id=? AND state IN ({ph}) "
                   f"ORDER BY id DESC LIMIT 1", (run_id, *states))
    return rows[0] if rows else None


def reassign_run(cfg: Cfg, db: Db, run_id: str, new_assignee: str, comment: str | None = None) -> str:
    """Bounce an open MANUAL escalation to the other party (Claude<->Researcher) without treating
    it as a decision. Found live 2026-08-16: `state='re-assign'` was documented (BUILD.md §113,
    GOVERNANCE.md §39) but no code path ever produced it — a dead enum value, same class of gap as
    `document_reference_grouping` before it was wired. `state='re-assign'` — distinct from both
    'raised' (nobody has looked at it yet) and any terminal state (nobody decided anything, it's
    just moved to the other party's queue). Restricted to `MANUAL-`-prefixed run_ids only, same
    boundary as edit/pause/resume/retract — a real dispatcher-tied escalation's
    `next_action_assigned_to` is set by the app itself (the researcher's own approval gate), not
    something either party bounces around."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("raised", "on-hold", "re-assign", "in-progress"))
    if not esc:
        return f"no open escalation for run {run_id!r} to re-assign"
    who = _check_assignee(db, new_assignee)
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "re-assign"),
              next_action_assigned_to=who, comment=comment)
    return (f"escalation {esc['id']} (run {run_id!r}) re-assigned to {who!r}"
           + (f" — {comment!r}" if comment else ""))


def complete_run(cfg: Cfg, db: Db, run_id: str, resolution: str) -> str:
    """Claude marks an `in-progress` MANUAL escalation genuinely done — the actual answer to
    escalations #673/#674 (2026-08-17), replacing the earlier workaround (raising a SEPARATE
    tracker escalation for ongoing work, `BUILD.md` §123) with a real state transition. Restricted
    to MANUAL- run_ids currently `in-progress`, same boundary as edit/pause/resume/retract/
    reassign — a dispatcher-tied escalation's `'completed'` is set by the app itself the moment
    its decision resolves (see `_terminal_state_for`), not something either party marks later."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("in-progress",))
    if not esc:
        return f"no in-progress escalation for run {run_id!r} to complete"
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "completed"),
              resolution=resolution)
    return f"escalation {esc['id']} (run {run_id!r}) marked complete — {resolution!r}"


def edit_question(cfg: Cfg, db: Db, run_id: str, new_question: str) -> str:
    """Replace a still-open (raised, on-hold, or in-progress) MANUAL escalation's
    short_description. The old wording is preserved in `tried` with a timestamp, not silently
    lost -- the row's history stays readable."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("raised", "on-hold", "re-assign", "in-progress"))
    if not esc:
        return f"no open (raised/on-hold/re-assign/in-progress) escalation for run {run_id!r} to edit"
    _grant(cfg, "escalation")
    old_note = f"[edited {_now()}] was: {esc['short_description']}"
    tried = f"{esc['tried']}\n{old_note}" if esc["tried"] else old_note
    db.update("escalation", {"id": esc["id"]}, short_description=new_question, tried=tried)
    return f"escalation {esc['id']} (run {run_id!r}) question updated"


def pause_run(cfg: Cfg, db: Db, run_id: str, comment: str | None = None) -> str:
    """Set a raised (or re-assigned) MANUAL escalation aside without answering it -- still shown
    in the list, flagged distinctly, until resumed."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("raised", "re-assign", "in-progress"))
    if not esc:
        return f"no raised/re-assign/in-progress escalation for run {run_id!r} to pause"
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "on-hold"), comment=comment)
    return f"escalation {esc['id']} (run {run_id!r}) on-hold" + (f" — {comment!r}" if comment else "")


def resume_run(cfg: Cfg, db: Db, run_id: str) -> str:
    """Bring an on-hold MANUAL escalation back into the active (raised) queue."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("on-hold",))
    if not esc:
        return f"no on-hold escalation for run {run_id!r} to resume"
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "raised"))
    return f"escalation {esc['id']} (run {run_id!r}) resumed — back in the active queue"


def retract_run(cfg: Cfg, db: Db, run_id: str, comment: str | None = None,
                answered_by: str = "Researcher") -> str:
    """Withdraw an open (raised, on-hold, re-assign, or in-progress) MANUAL escalation without it
    counting as a decision -- 'never mind', not 'reviewed and approved/rejected'. Terminal, like
    completed, but distinguishable from it in the record."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("raised", "on-hold", "re-assign", "in-progress"))
    if not esc:
        return f"no open (raised/on-hold/re-assign) escalation for run {run_id!r} to retract"
    who = _check_assignee(db, answered_by)
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "withdraw"), comment=comment,
              answered_by=who, answered_at=_now())
    return f"escalation {esc['id']} (run {run_id!r}) withdrawn" + (f" — {comment!r}" if comment else "")


def write_list_report(cfg: Cfg, db: Db, path: pathlib.Path) -> tuple[pathlib.Path, list]:
    """`Escalation.ps1 -Action List` used to only print to the terminal — never persisted, the
    same standard violation `governance.reports_must_persist` (GOVERNANCE.md §9E) already named
    for every other report in this app. Fixed 2026-07-23: writes a real .md file (archived on
    every regenerate, same convention as every other report) and returns the rows so the caller
    can still print a short terminal pointer, not the full dump."""
    ph = ",".join("?" * len(_OPEN_STATES))
    rows = db.rows(f"SELECT id, run_id, source, at_step, state, short_description, "
                   f"next_action_assigned_to, raised_at FROM escalation "
                   f"WHERE state IN ({ph}) ORDER BY id", _OPEN_STATES)
    n_on_hold = sum(1 for r in rows if r["state"] == "on-hold")
    # in-progress broken out from "active" explicitly (escalation #674) -- "awaiting a decision"
    # (raised/re-assign) and "decided, work under way" (in-progress) are different things to see
    # at a glance, the whole point of the new state.
    n_in_progress = sum(1 for r in rows if r["state"] == "in-progress")
    n_active = len(rows) - n_on_hold - n_in_progress
    L = ["# Open escalations", "",
         f"> Generated by `Escalation.ps1 -Action List`. {len(rows)} open escalation(s) "
         f"({n_active} active, {n_in_progress} in-progress, {n_on_hold} on-hold).", ""]
    if not rows:
        L.append("_no open escalations_")
    else:
        L += ["| # | state | source | at step | assigned to | raised | short description |",
              "|---|---|---|---|---|---|---|"]
        for r in rows:
            q = str(r["short_description"]).replace("|", "\\|").replace("\n", " ")
            state = f"**{r['state']}**" if r["state"] in ("on-hold", "in-progress") else r["state"]
            L.append(f"| {r['id']} | {state} | {r['source']} | {r['at_step']} | "
                     f"{r['next_action_assigned_to'] or ''} | {r['raised_at']} | {q} |")
    reportkit.archive_before_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(L).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
    return path, rows


def _extract_flag(args: list[str], name: str) -> tuple[list[str], str | None]:
    """Pulls a `--name=value` token out of `args` (anywhere in the list); returns
    (remaining_args, value_or_None)."""
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
    if len(argv) >= 1 and argv[0] == "list":
        path = pathlib.Path(cfg.setting("escalation.list_report_path",
                                        "iba/app/reports/escalation-list.md"))
        out, rows = write_list_report(cfg, db, path)
        n_on_hold = sum(1 for r in rows if r["state"] == "on-hold")
        n_in_progress = sum(1 for r in rows if r["state"] == "in-progress")
        n_active = len(rows) - n_on_hold - n_in_progress
        print(f"  {len(rows)} open escalation(s) ({n_active} active, {n_in_progress} in-progress, "
             f"{n_on_hold} on-hold) -> {out}")
    elif len(argv) >= 3 and argv[0] == "answer":
        rest, by = _extract_flag(argv[3:], "by")
        print("  " + answer_for_word(cfg, db, argv[1], argv[2], answered_by=by or "Researcher"))
    elif len(argv) >= 3 and argv[0] == "answer-run":
        rest, by = _extract_flag(argv[3:], "by")
        rest, resolution = _extract_flag(rest, "resolution")
        comment = " ".join(rest) or None
        print("  " + answer_for_run(cfg, db, argv[1], argv[2], comment,
                                    answered_by=by or "Researcher", resolution=resolution))
    elif len(argv) >= 2 and argv[0] == "raise":
        rest, source = _extract_flag(argv[1:], "source")
        rest, assigned_to = _extract_flag(rest, "assigned-to")
        rest, etype = _extract_flag(rest, "type")
        rest, related_activity = _extract_flag(rest, "related-activity")
        rest, reference_doc = _extract_flag(rest, "reference-doc")
        question = " ".join(rest)
        run_id = raise_manual(db, question, source=source or "claude",
                              assigned_to=assigned_to or "Researcher", etype=etype or "task",
                              related_activity=related_activity, reference_doc=reference_doc)
        print(f"  raised — run_id {run_id!r}. Answer with:")
        print(f"    python -m iba.app.lib.escalation answer-run {run_id} <approve|reject|revise|hold|noted>")
    elif len(argv) >= 3 and argv[0] == "complete":
        rest, resolution_flag = _extract_flag(argv[2:], "resolution")
        resolution = resolution_flag or " ".join(rest)
        print("  " + complete_run(cfg, db, argv[1], resolution))
    elif len(argv) >= 3 and argv[0] == "edit":
        question = " ".join(argv[2:])
        print("  " + edit_question(cfg, db, argv[1], question))
    elif len(argv) >= 2 and argv[0] == "pause":
        comment = " ".join(argv[2:]) or None
        print("  " + pause_run(cfg, db, argv[1], comment))
    elif len(argv) >= 2 and argv[0] == "resume":
        print("  " + resume_run(cfg, db, argv[1]))
    elif len(argv) >= 2 and argv[0] == "retract":
        rest, by = _extract_flag(argv[2:], "by")
        comment = " ".join(rest) or None
        print("  " + retract_run(cfg, db, argv[1], comment, answered_by=by or "Researcher"))
    elif len(argv) >= 3 and argv[0] == "reassign":
        comment = " ".join(argv[3:]) or None
        print("  " + reassign_run(cfg, db, argv[1], argv[2], comment))
    else:
        print("usage: python -m iba.app.lib.escalation list"
              " | answer <word> <approve|reject> [--by=Claude|Researcher]"
              " | answer-run <run_id> <approve|reject|revise|hold|noted> [--by=...] [--resolution=...] [comment...]"
              " | raise <question...> [--source=claude|researcher] [--assigned-to=...] [--type=...]"
              " [--related-activity=...] [--reference-doc=...]"
              " | complete <run_id> [--resolution=...] <what was actually done...>"
              " | edit <run_id> <new question...>"
              " | pause <run_id> [comment...]"
              " | resume <run_id>"
              " | retract <run_id> [--by=...] [comment...]"
              " | reassign <run_id> <Claude|Researcher> [comment...]")
    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
