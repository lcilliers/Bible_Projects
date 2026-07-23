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
"""

from __future__ import annotations

import datetime
import json
import sys

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
        "state": "raised", "answer": None, "answered_at": None, "raised_at": _now()})


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
    db.update("escalation", {"id": esc["id"]}, state="answered",
              answer=decision, answered_at=_now())
    new_status = "approved" if decision == "yes" else "rejected"
    wr = db.rows("SELECT id, word FROM word_registry WHERE lower(word)=lower(?) AND deleted=0",
                 (esc["word"],))
    if wr:
        db.update("word_registry", {"id": wr[0]["id"]}, status=new_status)
        word = wr[0]["word"]      # report the canonical stored form
    return f"escalation {esc['id']} answered {decision!r}; {word!r} status -> {new_status}"


# ── run-scoped (general — no word, three-way answer) ─────────────────────────
RUN_ANSWERS = ("approve", "reject", "revise")


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
        "state": "raised", "answer": None, "answered_at": None, "raised_at": _now()})
    return run_id


def answer_for_run(cfg: Cfg, db: Db, run_id: str, decision: str, comment: str | None = None) -> str:
    """Record the researcher's decision on a run-scoped (word-less) escalation.
    decision: 'approve' | 'reject' | 'revise' (revise carries feedback, not a rejection).
    No word_registry side-effect — the caller (e.g. configmaint.propose) acts on the
    answer itself the next time the step runs."""
    if decision not in RUN_ANSWERS:
        return f"invalid decision {decision!r} — must be one of {RUN_ANSWERS}"
    rows = pending_for_run(db, run_id)
    if not rows:
        return f"no pending escalation for run {run_id!r}"
    esc = rows[0]
    _grant(cfg, "escalation")
    db.update("escalation", {"id": esc["id"]}, state="answered",
              answer=decision, comment=comment, answered_at=_now())
    return f"escalation {esc['id']} (run {run_id!r}, step {esc['at_step']!r}) answered {decision!r}" + (
        f" — {comment!r}" if comment else "")


def main() -> int:
    cfg = Cfg()
    db = Db(cfg)
    if len(sys.argv) >= 2 and sys.argv[1] == "list":
        rows = db.rows("SELECT id, run_id, word, at_step, state, question FROM escalation "
                       "WHERE state='raised' ORDER BY id")
        if not rows:
            print("no open escalations")
        for r in rows:
            label = f"[{r['word']}]" if r["word"] else f"(run {r['run_id']})"
            print(f"  #{r['id']} {label} at {r['at_step']} — {r['question']}")
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
    else:
        print("usage: python -m iba.app.escalation list"
              " | answer <word> <yes|no>"
              " | answer-run <run_id> <approve|reject|revise> [comment...]"
              " | raise <question...>")
    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
