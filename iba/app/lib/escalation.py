"""escalation.py — util.escalation. The only sanctioned researcher interaction.

The principle (from the design docs): the app tries to resolve; if it cannot, it
PAUSES the run, asks the researcher, and RESUMES at the same point when answered —
a pause, not a fork. State is durable (in the DB), so a pause survives the process:
the run stops, and resume is a fresh invocation that reads the answer.

    raise_(...)         record a pause (a step names the question + preset details)
    pending_for_word    the open escalation for a word, if any
    answer_for_word     the researcher's decision; also advances the word's status

CLI (the researcher's side, VS-Code terminal per O6):
    python -m iba.app.escalation list
    python -m iba.app.escalation answer <word> <yes|no>
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


def main() -> int:
    cfg = Cfg()
    db = Db(cfg)
    if len(sys.argv) >= 2 and sys.argv[1] == "list":
        rows = db.rows("SELECT id, word, at_step, state, question FROM escalation "
                       "WHERE state='raised' ORDER BY id")
        if not rows:
            print("no open escalations")
        for r in rows:
            print(f"  #{r['id']} [{r['word']}] at {r['at_step']} — {r['question']}")
    elif len(sys.argv) >= 4 and sys.argv[1] == "answer":
        print("  " + answer_for_word(cfg, db, sys.argv[2], sys.argv[3]))
    else:
        print("usage: python -m iba.app.escalation list | answer <word> <yes|no>")
    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
