"""escalation.py — util.escalation. The only sanctioned researcher interaction.

The principle (from the design docs): the app tries to resolve; if it cannot, it
PAUSES the run, asks the researcher, and RESUMES at the same point when answered —
a pause, not a fork. State is durable (in the DB), so a pause survives the process:
the run stops, and resume is a fresh invocation that reads the answer.

    raise_(...)         record a pause (a step names the question + preset details)
    pending_for_word    the open escalation for a word, if any
    answer_for_word     the researcher's decision (yes/no); also advances the word's status

Word-scoped functions above are the original (registry.create) shape — unchanged.
RUN-scoped functions below are the general shape for anything that isn't about a word
(e.g. a configuration_maintenance proposal), added 2026-07-21 per the researcher's rule
that every escalation must offer three outcomes, not yes/no:

    pending_for_run     the open escalation for a run, if any
    answered_for_run     the answered escalation for a run at a step, if any
    answer_for_run       approve | reject | revise (+ optional comment) — no word side-effect

CLI (the researcher's side, VS-Code terminal per O6). Note the module path — this file lives
at iba/app/lib/escalation.py, so it's invoked via iba.app.lib.escalation, not iba.app.escalation
(a stale path was in this docstring and registry.py's before 2026-07-21; corrected here):
    python -m iba.app.lib.escalation list
    python -m iba.app.lib.escalation answer <word> <yes|no>
    python -m iba.app.lib.escalation answer-run <run_id> <approve|reject|revise> [comment...]
    python -m iba.app.lib.escalation raise <question...>

Added 2026-07-23 for the researcher's backlog-of-work-for-Claude workflow — a manual escalation
doubles as a work instruction, not only a design decision awaiting approval. Run-scoped/manual only
(same boundary as answer-run vs. answer):
    python -m iba.app.lib.escalation edit <run_id> <new question...>     -- replace the wording
    python -m iba.app.lib.escalation pause <run_id> [comment...]         -- set aside, out of the active queue
    python -m iba.app.lib.escalation resume <run_id>                    -- back into the active queue
    python -m iba.app.lib.escalation retract <run_id> [comment...]      -- withdraw, not a decision
"""

from __future__ import annotations

import datetime
import json
import pathlib
import sys

from . import reportkit
from .cfg import Cfg
from .db import Db


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _grant(cfg: Cfg, table: str):
    if table not in cfg.may_write("escalation"):
        raise PermissionError(f"write-grant violation: 'escalation' may not write {table!r}")


def raise_(db: Db, run_id: str, word: str, at_step: str, question: str,
           preset: dict, tried: str, etype: str = "prompted") -> int:
    """Record a pause. Written under the dispatcher's grant (caller passes an open db)."""
    return db.write("escalation", {
        "run_id": run_id, "word": word, "at_step": at_step, "type": etype,
        "question": question, "preset": json.dumps(preset), "tried": tried,
        "state": _check_state(db, "raised"), "answer": None, "answered_at": None,
        "raised_at": _now()})


def pending_for_word(db: Db, word: str):
    """The latest un-answered escalation for a word, or None. Case-insensitive on word."""
    return db.rows(
        "SELECT * FROM escalation WHERE lower(word)=lower(?) AND state='raised' "
        "ORDER BY id DESC LIMIT 1", (word,))
    # returns a list; caller takes [0]


def answered_for_word(db: Db, word: str, at_step: str):
    """The latest ANSWERED escalation for a word at a step, or None. Case-insensitive."""
    rows = db.rows(
        "SELECT * FROM escalation WHERE lower(word)=lower(?) AND at_step=? AND state='answered' "
        "ORDER BY id DESC LIMIT 1", (word, at_step))
    return rows[0] if rows else None


def answer_for_word(cfg: Cfg, db: Db, word: str, decision: str) -> str:
    """Record the researcher's answer and advance the word's status accordingly.
    decision: 'yes' -> approved, 'no' -> rejected. Case-insensitive on word."""
    rows = pending_for_word(db, word)
    if not rows:
        return f"no pending escalation for {word!r}"
    esc = rows[0]
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "answered"),
              answer=decision, answered_at=_now())
    new_status = "approved" if decision == "yes" else "rejected"
    wr = db.rows("SELECT id, word FROM word_registry WHERE lower(word)=lower(?) AND deleted=0",
                 (esc["word"],))
    if wr:
        db.update("word_registry", {"id": wr[0]["id"]}, status=new_status)
        word = wr[0]["word"]      # report the canonical stored form
    return f"escalation {esc['id']} answered {decision!r}; {word!r} status -> {new_status}"


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


def _check_state(db: Db, state: str) -> str:
    """Validate a state value against cfg_enum 'escalation_state' — a real, live lookup (not a
    hardcoded Python set) so a change to the DB's enum membership is something this code actually
    responds to, per the researcher's 2026-07-23 correction (escalation #305): a cfg_enum's
    genuine 'usage' is being queried by name at runtime, not just having its group name mentioned
    somewhere in source."""
    valid = db.cfg.enum("escalation_state")
    if state not in valid:
        raise ValueError(f"{state!r} is not a member of cfg_enum 'escalation_state' ({valid!r})")
    return state


# ── run-scoped (general — no word, three-way answer) ─────────────────────────
def pending_for_run(db: Db, run_id: str):
    """The latest un-answered escalation for a run, or None."""
    return db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND state='raised' "
        "ORDER BY id DESC LIMIT 1", (run_id,))
    # returns a list; caller takes [0]


def answered_for_run(db: Db, run_id: str, at_step: str):
    """The latest ANSWERED escalation for a run at a step, or None."""
    rows = db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND at_step=? AND state='answered' "
        "ORDER BY id DESC LIMIT 1", (run_id, at_step))
    return rows[0] if rows else None


def raise_manual(db: Db, question: str, tried: str | None = None) -> tuple[int, str]:
    """A researcher-initiated item — 'flag this for later, resolve it via the same review
    workflow' — not raised BY a running step. Found 2026-07-22: raise_() always needed a run_id/
    at_step from an in-flight run; there was no way for the researcher to add their own tracked
    item. Uses a synthetic run_id (no 'run' row exists for it — answer_for_run only queries
    escalation by run_id, so this needs no special-casing) so it answers via the exact same
    `Escalation.ps1 -Action AnswerRun -RunId <id> -Decision ...` path as every other escalation,
    and shows up in the same open-items list/report."""
    run_id = f"MANUAL-{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d_%H%M%S_%f')}"
    _grant(db.cfg, "escalation")
    db.write("escalation", {
        "run_id": run_id, "word": None, "at_step": "manual", "type": "interactive",
        "question": question, "preset": json.dumps({}),
        "tried": tried or "researcher-initiated — no run to resume; a standalone tracked note",
        "state": _check_state(db, "raised"), "answer": None, "answered_at": None,
        "raised_at": _now()})
    return run_id


def answer_for_run(cfg: Cfg, db: Db, run_id: str, decision: str, comment: str | None = None) -> str:
    """Record the researcher's decision on a run-scoped (word-less) escalation.
    decision: 'approve' | 'reject' | 'revise' (revise carries feedback, not a rejection).
    No word_registry side-effect — the caller (e.g. configmaint.propose) acts on the
    answer itself the next time the step runs.
    Valid decisions come from cfg_enum 'escalation_answer' (a live lookup, not a hardcoded Python
    tuple — see _check_state's docstring for why this matters, same reasoning applies here)."""
    run_id = _resolve_run_id(db, run_id)
    valid_answers = cfg.enum("escalation_answer")
    if decision not in valid_answers:
        return f"invalid decision {decision!r} — must be one of {valid_answers!r}"
    rows = pending_for_run(db, run_id)
    if not rows:
        return f"no pending escalation for run {run_id!r}"
    esc = rows[0]
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "answered"),
              answer=decision, comment=comment, answered_at=_now())
    return f"escalation {esc['id']} (run {run_id!r}, step {esc['at_step']!r}) answered {decision!r}" + (
        f" — {comment!r}" if comment else "")


# ── edit / pause / resume / retract — added 2026-07-23 for the researcher's own backlog-of-
# items-for-Claude workflow (a manual escalation is a work instruction, not only a design decision
# needing approval). Restricted to MANUAL-prefixed run_ids ONLY (not run-scoped-in-general) --
# found while building this: a REAL dispatcher-tied escalation (configmaint.propose, candidate.
# validate, ...) checks `answered_for_run` (state='answered') and run.py's own pause-continue dedup
# checks `state='raised'` to decide whether to raise a duplicate; pausing one of those would flip
# it to `state='paused'`, matching NEITHER check, so re-running the underlying command before
# resuming would raise a second escalation row for the same run_id+step, not resume the real one.
# Manual items have no such downstream reader, so this cannot happen to them.
def _manual_only(run_id: str) -> str | None:
    if not run_id.startswith("MANUAL-"):
        return (f"{run_id!r} is not a manual escalation (run_id doesn't start with 'MANUAL-'). "
               f"Edit/Pause/Resume/Retract are restricted to researcher-raised items only -- a "
               f"real dispatcher-tied escalation must be answered via AnswerRun.")
    return None


def _latest_for_run(db: Db, run_id: str, states: tuple[str, ...]):
    """The latest escalation row for a run in one of `states`, or None."""
    ph = ",".join("?" * len(states))
    rows = db.rows(f"SELECT * FROM escalation WHERE run_id=? AND state IN ({ph}) "
                   f"ORDER BY id DESC LIMIT 1", (run_id, *states))
    return rows[0] if rows else None


def edit_question(cfg: Cfg, db: Db, run_id: str, new_question: str) -> str:
    """Replace a still-open (raised or paused) MANUAL escalation's question text. The old wording
    is preserved in `tried` with a timestamp, not silently lost -- the row's history stays readable."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("raised", "paused"))
    if not esc:
        return f"no open (raised/paused) escalation for run {run_id!r} to edit"
    _grant(cfg, "escalation")
    old_note = f"[edited {_now()}] was: {esc['question']}"
    tried = f"{esc['tried']}\n{old_note}" if esc["tried"] else old_note
    db.update("escalation", {"id": esc["id"]}, question=new_question, tried=tried)
    return f"escalation {esc['id']} (run {run_id!r}) question updated"


def pause_run(cfg: Cfg, db: Db, run_id: str, comment: str | None = None) -> str:
    """Set a raised MANUAL escalation aside without answering it -- still shown in the list,
    flagged distinctly, until resumed."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("raised",))
    if not esc:
        return f"no raised escalation for run {run_id!r} to pause"
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "paused"), comment=comment)
    return f"escalation {esc['id']} (run {run_id!r}) paused" + (f" — {comment!r}" if comment else "")


def resume_run(cfg: Cfg, db: Db, run_id: str) -> str:
    """Bring a paused MANUAL escalation back into the active (raised) queue."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("paused",))
    if not esc:
        return f"no paused escalation for run {run_id!r} to resume"
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "raised"))
    return f"escalation {esc['id']} (run {run_id!r}) resumed — back in the active queue"


def retract_run(cfg: Cfg, db: Db, run_id: str, comment: str | None = None) -> str:
    """Withdraw an open (raised or paused) MANUAL escalation without it counting as a decision --
    'never mind', not 'reviewed and approved/rejected'. Terminal, like answered, but distinguishable
    from it in the record."""
    run_id = _resolve_run_id(db, run_id)
    if (err := _manual_only(run_id)):
        return err
    esc = _latest_for_run(db, run_id, ("raised", "paused"))
    if not esc:
        return f"no open (raised/paused) escalation for run {run_id!r} to retract"
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state=_check_state(db, "retracted"), comment=comment,
              answered_at=_now())
    return f"escalation {esc['id']} (run {run_id!r}) retracted" + (f" — {comment!r}" if comment else "")


def write_list_report(cfg: Cfg, db: Db, path: pathlib.Path) -> tuple[pathlib.Path, list]:
    """`Escalation.ps1 -Action List` used to only print to the terminal — never persisted, the
    same standard violation `governance.reports_must_persist` (GOVERNANCE.md §9E) already named
    for every other report in this app. Fixed 2026-07-23: writes a real .md file (archived on
    every regenerate, same convention as every other report) and returns the rows so the caller
    can still print a short terminal pointer, not the full dump."""
    rows = db.rows("SELECT id, run_id, word, at_step, state, question, raised_at FROM escalation "
                   "WHERE state IN ('raised', 'paused') ORDER BY id")
    n_paused = sum(1 for r in rows if r["state"] == "paused")
    L = ["# Open escalations", "",
         f"> Generated by `Escalation.ps1 -Action List`. {len(rows)} open escalation(s) "
         f"({len(rows) - n_paused} active, {n_paused} paused).", ""]
    if not rows:
        L.append("_no open escalations_")
    else:
        L += ["| # | state | scope | at step | raised | question |", "|---|---|---|---|---|---|"]
        for r in rows:
            scope = f"word `{r['word']}`" if r["word"] else f"run `{r['run_id']}`"
            q = str(r["question"]).replace("|", "\\|").replace("\n", " ")
            state = "**paused**" if r["state"] == "paused" else r["state"]
            L.append(f"| {r['id']} | {state} | {scope} | {r['at_step']} | {r['raised_at']} | {q} |")
    reportkit.archive_before_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(L).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
    return path, rows


def main() -> int:
    cfg = Cfg()
    db = Db(cfg)
    if len(sys.argv) >= 2 and sys.argv[1] == "list":
        path = pathlib.Path(cfg.setting("escalation.list_report_path",
                                        "iba/app/reports/escalation-list.md"))
        out, rows = write_list_report(cfg, db, path)
        n_paused = sum(1 for r in rows if r["state"] == "paused")
        print(f"  {len(rows)} open escalation(s) ({len(rows) - n_paused} active, "
             f"{n_paused} paused) -> {out}")
    elif len(sys.argv) >= 4 and sys.argv[1] == "answer":
        print("  " + answer_for_word(cfg, db, sys.argv[2], sys.argv[3]))
    elif len(sys.argv) >= 4 and sys.argv[1] == "answer-run":
        comment = " ".join(sys.argv[4:]) or None
        print("  " + answer_for_run(cfg, db, sys.argv[2], sys.argv[3], comment))
    elif len(sys.argv) >= 3 and sys.argv[1] == "raise":
        question = " ".join(sys.argv[2:])
        run_id = raise_manual(db, question)
        print(f"  raised — run_id {run_id!r}. Answer with:")
        print(f"    python -m iba.app.lib.escalation answer-run {run_id} <approve|reject|revise>")
    elif len(sys.argv) >= 4 and sys.argv[1] == "edit":
        question = " ".join(sys.argv[3:])
        print("  " + edit_question(cfg, db, sys.argv[2], question))
    elif len(sys.argv) >= 3 and sys.argv[1] == "pause":
        comment = " ".join(sys.argv[3:]) or None
        print("  " + pause_run(cfg, db, sys.argv[2], comment))
    elif len(sys.argv) >= 3 and sys.argv[1] == "resume":
        print("  " + resume_run(cfg, db, sys.argv[2]))
    elif len(sys.argv) >= 3 and sys.argv[1] == "retract":
        comment = " ".join(sys.argv[3:]) or None
        print("  " + retract_run(cfg, db, sys.argv[2], comment))
    else:
        print("usage: python -m iba.app.escalation list"
              " | answer <word> <yes|no>"
              " | answer-run <run_id> <approve|reject|revise> [comment...]"
              " | raise <question...>"
              " | edit <run_id> <new question...>"
              " | pause <run_id> [comment...]"
              " | resume <run_id>"
              " | retract <run_id> [comment...]")
    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
