"""data_corrections_2541_2542_v1_20261124.py -- the data corrections the researcher approved on #2542 v5 and #2541 v5 (2026-11-24, 'approved').

#2542: `surely` is not of the collection hear (its link and index-fill row set deleted; its group is set separately by Surface-Group Set); the index-fill row of `presence` in offer is
        set deleted. `unworthy` in reward is NOT moved here: its destination is the researcher's to give.
#2541 2.3: lemma_inventory 15848 gloss and strong_sense H6424 head "to envy" -> "to weigh, make level, balance" (the STEP lexicon line, strong_meaning_parsed).
Every write through configmaint.apply_logged (the old values go to cfg_change_detail). A named snapshot is taken before a live apply. Idempotent. One transaction.
Usage: python iba/app/migration/data_corrections_2541_2542_v1_20261124.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2541-2542-DATA-CORRECTIONS-20261124"
NEW_GLOSS = "to weigh, make level, balance"


def plan(conn):
    ops = []
    for table, rid in (("collection_link", 9416), ("collection_subgroup_surface", 1547), ("collection_subgroup_surface", 2864)):
        if conn.execute(f"SELECT deleted FROM {table} WHERE id=?", (rid,)).fetchone()[0] == 0:
            ops.append((table, "update", {"id": rid}, {"deleted": 1}))
    if conn.execute("SELECT gloss FROM lemma_inventory WHERE id=15848").fetchone()[0] != NEW_GLOSS:
        ops.append(("lemma_inventory", "update", {"id": 15848}, {"gloss": NEW_GLOSS}))
    if conn.execute("SELECT head FROM strong_sense WHERE strong='H6424'").fetchone()[0] != NEW_GLOSS:
        ops.append(("strong_sense", "update", {"strong": "H6424"}, {"head": NEW_GLOSS}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where, set_)
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2541-2542-data-corrections', named=True)}")
    try:
        conn.execute("SAVEPOINT dc")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE dc")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO dc")
        conn.execute("RELEASE dc")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
