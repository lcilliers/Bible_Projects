"""escalation_redesign_v1_20260819_ROLLBACK.py — ONE-OFF: reverts escalation_redesign_v1_20260819
in full. Run live 2026-08-19, same day, after the redesign migration surfaced a real gap not
covered by any of the three plan review rounds: `run.py`'s DISPATCHER-TIED pauses (configmaint.
propose, candidate.validate, etc.) correlate to one specific pipeline execution via `run_id`, which
the new schema dropped entirely, and 7+ handlers branch on `next_action=='approve'`, a value the
new vocabulary removed (split into ready_for_approval/approved). Both only apply to the
dispatcher-tied use case, never discussed across the three review rounds (which scoped entirely to
the MANUAL/researcher-workflow case) -- not safe to guess a reconciliation on live infrastructure.

Restores: `escalation` (the original 722-row table, renamed back from `escalations_old`),
drops `escalation_history` and the new empty `escalation`, reverts cfg_table/cfg_column/cfg_index/
cfg_unique/cfg_enum, clears the sqlite_sequence override. The 4 carryover rows (735-738) lived only
in the dropped new `escalation` table, so no separate cleanup needed for those.

    python -m iba.app.migration.escalation_redesign_v1_20260819_ROLLBACK
"""
from __future__ import annotations
import sqlite3
from ..lib.cfg import Cfg

DB_PATH = "iba/app/db/iba.db"


def run() -> None:
    cfg = Cfg(DB_PATH)
    conn = cfg.conn
    conn.execute("BEGIN")
    try:
        conn.execute("DROP TABLE IF EXISTS escalation_history")
        conn.execute("DROP TABLE IF EXISTS escalation")
        conn.execute("ALTER TABLE escalations_old RENAME TO escalation")

        conn.execute("DELETE FROM cfg_table WHERE database='iba' AND name IN ('escalation_history','escalation')")
        conn.execute(
            "UPDATE cfg_table SET name='escalation', inactive=0, "
            "\"use\"='One row per researcher interaction -- the pause. A pause, not a fork: the "
            "run resumes at resume_point when answered.' "
            "WHERE database='iba' AND name='escalations_old'")
        conn.execute("DELETE FROM cfg_column WHERE database='iba' AND table_name='escalation'")
        conn.execute(
            "UPDATE cfg_column SET table_name='escalation' WHERE database='iba' AND table_name='escalations_old'")
        conn.execute("DELETE FROM cfg_column WHERE database='iba' AND table_name='escalation_history'")
        conn.execute("UPDATE cfg_index SET table_name='escalation' WHERE table_name='escalations_old'")
        conn.execute("DELETE FROM cfg_index WHERE table_name='escalation_history'")
        conn.execute(
            "UPDATE cfg_unique SET table_name='escalation' WHERE database='iba' AND table_name='escalations_old'")
        conn.execute("DELETE FROM cfg_unique WHERE database='iba' AND table_name='escalation_history'")

        conn.execute("UPDATE cfg_enum SET inactive=0 WHERE name='escalation_state' AND value='re-assign'")
        conn.execute(
            "DELETE FROM cfg_enum WHERE name='escalation_state' AND value IN ('supersede','re-assigned')")
        conn.execute(
            "UPDATE cfg_enum SET inactive=0 WHERE name='escalation_next_action' AND value IN ('approve','hold')")
        conn.execute(
            "DELETE FROM cfg_enum WHERE name='escalation_next_action' AND value IN "
            "('ready_for_approval','approved','review')")
        # reject/revise/noted were shared between old and new -- left active, correctly, either way

        conn.execute("DELETE FROM sqlite_sequence WHERE name='escalation'")
        n = conn.execute("SELECT COUNT(*) FROM escalation").fetchone()[0]
        conn.commit()
        print(f"  ROLLED BACK. escalation restored: {n} rows (should be 722).")
    except Exception:
        conn.rollback()
        print("  Rollback itself failed and was rolled back -- state unchanged from before this ran.")
        raise
    finally:
        cfg.close()


if __name__ == "__main__":
    run()
