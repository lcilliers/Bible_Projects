"""add_elevation_candidate_question_v1_20260922.py — ONE-OFF migration, escalation #1836,
researcher instruction verbatim: "sometimes a word is in T2 or T3, and they really should be a
M-code. although this is rare, is there any way that question can be added for any T2 or T3 word
that should flag it elevation to a cluster status." Answered "YES, APPROVED, BUILD this" the same
turn.

Registers `M0.8.1` in `wa_obs_question_catalogue`: a new, per-occurrence Stage 1 question scoped to
words that carry a T2/T3 role but NO M-code at all in the same verse (a word carrying both a T-code
and an M-code already IS an M-code characteristic -- excluded, nothing to flag). Rare by design
(most T2/T3 words are genuinely supporting roles, per the researcher's own framing) -- landing place
is the new `elevation-candidate` tag (`taggingguidance.py`), filterable corpus-wide without a
separate review-queue mechanism.

Idempotent (checks live `question_code` before writing) -- a second run is a no-op.

    python -m iba.app.migration.add_elevation_candidate_question_v1_20260922
"""
from __future__ import annotations

import datetime
import sqlite3

from ..lib.cfg import DB_PATH

_QUESTION_TEXT = (
    "In this verse, this word is tagged T2 or T3 (a role word, not currently its own M-code "
    "characteristic) -- does its role here suggest it names a distinct inner-being characteristic "
    "in its own right, warranting elevation to its own M-code, rather than remaining a supporting "
    "role tag? Record the reason if yes; record none if it genuinely functions as a supporting "
    "role (manner, operation-word, qualifier) and not as its own characteristic.")

_REVIEW_NOTE = (
    "New 2026-09-22, escalation #1836: researcher direct instruction -- \"sometimes a word is in "
    "T2 or T3, and they really should be a M-code... is there any way that question can be added "
    "for any T2 or T3 word that should flag it elevation to a cluster status.\" Population: every "
    "T2/T3-tagged word present in the verse that carries NO M-code role at all (a word carrying "
    "both a T-code and an M-code simultaneously is already an M-code characteristic -- excluded). "
    "Answered per occurrence (rare event expected -- most T2/T3 words are correctly supporting "
    "roles, per the researcher's own framing 'although this is rare'). Landing place: tag "
    "'elevation-candidate' (taggingguidance.py) makes every yes-answer filterable corpus-wide "
    "without a separate review-queue mechanism.")


def run(dry_run: bool = True) -> None:
    conn = sqlite3.connect(DB_PATH("iba"))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    existing = cur.execute(
        "SELECT obs_id FROM wa_obs_question_catalogue WHERE question_code='M0.8.1'").fetchone()
    if existing:
        print(f"M0.8.1 already exists (obs_id={existing['obs_id']}) -- no-op.")
        conn.close()
        return

    today = datetime.date.today().isoformat()
    print("Will insert M0.8.1 into wa_obs_question_catalogue.")
    if dry_run:
        print("DRY RUN -- no write. Re-run with --live to apply.")
        conn.close()
        return

    cur.execute("""
        INSERT INTO wa_obs_question_catalogue
        (question_code, section, question_text, scope, status, deleted, date_added,
         catalogue_version, review_note, tier, component_code, component_title, prompt_seq,
         source, last_modified, dimension, window)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, ("M0.8.1", "M0", _QUESTION_TEXT, "Verse-context", "active", 0, today,
          "v9-elevation-flag-20260922", _REVIEW_NOTE, "M0", "M0.8",
          "T2/T3 Elevation Candidacy", 1, "escalation #1836, researcher instruction 2026-09-22",
          today, "M0", "action-impact"))
    conn.commit()
    print(f"Inserted M0.8.1, obs_id={cur.lastrowid}.")
    conn.close()


if __name__ == "__main__":
    import sys
    run(dry_run="--live" not in sys.argv)
