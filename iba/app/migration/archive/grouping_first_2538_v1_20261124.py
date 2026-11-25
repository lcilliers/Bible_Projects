"""grouping_first_2538_v1_20261124.py -- escalation #2538 (researcher, 2026-11-24, chat: the S1 data pull and the subgroup loop).

The grouping now comes first and is made from the surfaces and WordNet, with no verse read; the words (step S1) and then 1.1, 1.2, 2.1 and 3.1 are done subgroup by subgroup (-Subgroup).
Config only; the code is lib/collectiongroup.py (pull), lib/layerreading.py (open_step, pull, step_closed with a subgroup), lib/buildvalidate.py (closing_gate with a subgroup).
  layer.reading   step S1 gains after_grouping (opened only once the grouping is finished); node_required_from_layer subgroup_id 0 (a word node carries its subgroup from the words on)
  group.reading   asks: the grouping is made from the surfaces and WordNet, no verse is read, a surface WordNet does not hold is a subgroup on its own
All writes through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/grouping_first_2538_v1_20261124.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2538-GROUPING-FIRST-20261124"
MODULE = "grouping_first_2538_v1_20261124"
ASKS = ("Place each surface, whole, in the subgroup of its meaning. The file gives, for each surface, its base and what the WordNet tables say of it (its network group and its pairs with the other "
        "surfaces of the collection) and a seed grouping; no verse is read at this step. Start from the seed (surfaces of one word family stay together unless their forms differ in meaning) and "
        "amend it by meaning. A surface that WordNet does not hold (a phrase, or a surface with no pair) is a subgroup on its own and still goes through the subgroup analysis. Name each subgroup "
        "for the kind of meaning its surfaces share and define it in a sentence. Membership of the collection is settled: set a surface aside only where it is plainly not a member in meaning, "
        "with the reason, and the change procedure moves it out. A surface is never split by Strong's code. Mark a placement that is open as uncertain and say what is unsettled. Nothing here "
        "judges what a word does for the inner being: a concept (a behaviour) comes into play only in stage 4.")


def plan(conn):
    one = lambda q, *a: conn.execute(q, a).fetchone()  # noqa: E731
    ops = []
    cur = json.loads(one("SELECT value FROM cfg_setting WHERE key='layer.reading'")[0])
    new = json.loads(json.dumps(cur))
    for st in new["steps"]:
        if st["key"] == "S1":
            st["after_grouping"] = True
    new["node_required_from_layer"]["subgroup_id"] = 0
    if new != cur:
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(new, ensure_ascii=False)}))
    g = json.loads(one("SELECT value FROM cfg_setting WHERE key='group.reading'")[0])
    if g.get("asks") != ASKS:
        g2 = dict(g, asks=ASKS)
        g2.pop("sample_verses", None)
        g2.pop("max_codes_shown", None)
        g2.pop("verse_chars", None)
        g2["max_neighbours"] = 12
        ops.append(("cfg_setting", "update", {"key": "group.reading"}, {"value": json.dumps(g2, ensure_ascii=False)}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose": f"ONE-OFF migration -- escalation #2538: the grouping first, from WordNet; S1 after the grouping; run_id {RUN_ID}.",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
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
            print(" ", t, op, where)
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-grouping-first-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT gf")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE gf")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO gf")
        conn.execute("RELEASE gf")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
