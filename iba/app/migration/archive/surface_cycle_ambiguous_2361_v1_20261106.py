"""surface_cycle_ambiguous_2361_v1_20261106.py -- escalation #2361, a correction to the stage 1b load.

The recorded workbook of 2026-11-04 holds a word with TWO candidate bases as one string in its combined base column (hides: 'hid | hide').
The loader turned each such string into a pseudo-base term. That is wrong: it is not a word, and it hid an open choice. Found by the
structure module's first live run (hides showed no accepted evidence). The correction:
  - the 14 surfaces that point at a pseudo-base get base_id NULL, base_source NULL and the new state base_ambiguous (the structure
    found more than one base and nothing has chosen); the evidence rows are unchanged (accepted 0 for each candidate)
  - one open surface_flag of kind structure_conflict per such surface, naming the candidates
  - the 12 pseudo-base terms are set to soft delete (deleted = 1) with a surface_event mark_deleted
  - the enum value base_ambiguous and the note of surface_term.base_state, through configmaint.apply_logged()
The stage 1b reconciliation reproduced the workbook's own base count (2,481) and so did not see this: the true count of distinct bases
is 2,469 plus the 14 unresolved surfaces. Refuses, writing nothing, unless it finds exactly 12 pseudo-bases and 14 surfaces.
A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/surface_cycle_ambiguous_2361_v1_20261106.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import datetime
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-AMBIGUOUS-BASES-20261106"
MODULE = "surface_cycle_ambiguous_2361_v1_20261106"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CLAUSE = ("base_ambiguous (the structure found more than one candidate base for the surface, for example hid and hide for hides, and nothing "
          "has chosen: base_id is NULL, the candidates are the live surface_derivation rows of the surface, and an open surface_flag "
          "structure_conflict names them)")


def find(conn):
    pseudo = [r[0] for r in conn.execute("SELECT id FROM surface_term WHERE surface LIKE '% | %' AND deleted=0")]
    pts = []
    if pseudo:
        pts = conn.execute(f"SELECT t.id, t.surface, b.surface FROM surface_term t JOIN surface_term b ON b.id=t.base_id "
                           f"WHERE b.id IN ({','.join('?' * len(pseudo))}) AND t.id != b.id AND t.deleted=0", pseudo).fetchall()
    return pseudo, pts


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_enum WHERE name='surface_term.base_state' AND value='base_ambiguous'"):
        nxt = conn.execute("SELECT COALESCE(MAX(ordinal),0)+1 FROM cfg_enum WHERE name='surface_term.base_state'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "surface_term.base_state", "value": "base_ambiguous", "ordinal": nxt, "inactive": 0}))
        old = conn.execute("SELECT use FROM cfg_column WHERE table_name='surface_term' AND name='base_state'").fetchone()[0]
        marker = "confirmed (the researcher confirmed the base)"
        new = old.replace(marker, CLAUSE + "; " + marker) if marker in old else old.rstrip(" .") + "; " + CLAUSE
        ops.append(("cfg_column", "update", {"table_name": "surface_term", "name": "base_state"}, {"use": new}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "purpose": f"ONE-OFF migration -- escalation #2361: corrects the 12 pseudo-base terms of the stage 1b load into the state base_ambiguous "
                       f"with a flag; run_id {RUN_ID}.", "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations", "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    pseudo, pts = find(conn)
    if not pseudo and not ops:
        print("already applied: nothing changed")
        return 0
    if (len(pseudo), len(pts)) != (12, 14) and pseudo:
        print(f"REFUSED, nothing written: found {len(pseudo)} pseudo-base(s) and {len(pts)} surface(s), expected 12 and 14")
        return 2
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); {len(pseudo)} pseudo-base term(s) to soft delete; {len(pts)} surface(s) to set base_ambiguous")
        for p in pts:
            print(f"  {p[1]} -> {p[2]}")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2361-ambiguous', named=True)}")
    try:
        conn.execute("SAVEPOINT ambiguous")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for tid, sf, pb in pts:
            cands = [r[0] for r in conn.execute("SELECT DISTINCT base_word FROM surface_derivation WHERE term_id=? AND method='structure' AND deleted=0 "
                                                "AND kind IN ('inflection','derivation') ORDER BY base_word", (tid,))]
            conn.execute("UPDATE surface_term SET base_id=NULL, base_source=NULL, base_state='base_ambiguous', updated_at=?, run_id=? WHERE id=?", (NOW, RUN_ID, tid))
            conn.execute("INSERT INTO surface_flag (subject_kind, subject_id, kind, note, status, run_id, created_by, load_ref) VALUES "
                         "('surface_term',?, 'structure_conflict', ?, 'open', ?, 'migration', ?)",
                         (tid, f"two candidate bases from the structure ({', '.join(cands) or pb}); the recorded workbook kept them as '{pb}' and nothing chose; "
                               f"to be resolved by the resolve module or the researcher", RUN_ID, "outputs/escalation/2359-surfaces-and-bases-v1-20261104.xlsx#combined base"))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES ('surface_term',?, 'set_base', 'base_id', ?, NULL, 'migration', 'the pseudo-base term is not a word', ?, 'migration')", (tid, pb, RUN_ID))
        for pid in pseudo:
            conn.execute("UPDATE surface_term SET deleted=1, updated_at=?, run_id=? WHERE id=?", (NOW, RUN_ID, pid))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES ('surface_term',?, 'mark_deleted', 'deleted', '0', '1', 'migration', 'a pair of candidate bases held as one string by the recorded workbook, "
                         "not a word', ?, 'migration')", (pid, RUN_ID))
        left = conn.execute("SELECT count(*) FROM surface_term WHERE surface LIKE '% | %' AND deleted=0").fetchone()[0]
        if left:
            raise RuntimeError(f"{left} pseudo-base term(s) still live")
        conn.execute("RELEASE ambiguous")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO ambiguous")
        conn.execute("RELEASE ambiguous")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); {len(pts)} surface(s) set base_ambiguous with a flag; {len(pseudo)} pseudo-base term(s) soft deleted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
