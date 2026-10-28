"""analysis_phase_1_2323_v1_20261027.py -- escalation #2323: the soft delete of observations and nodes.

Researcher, chat 2026-10-27 (verbatim): "I also not neither observations nor nodes have a deleted collumn" and "fix the delete columns
on both tables and also ensure that the code deals with fixing errors during checking of the observations."

Until now a reading deleted an observation by `status='withdrawn'` and a node by `disposition='withdrawn'`. For a node that is
wrong: `disposition` is also how the claims step ended the node (told, claim, held, data, context, withdrawn), so a node deleted by a
reading looked like one withdrawn by the claims. The project's soft delete is a `deleted` column (40 tables carry it). This adds it:
- ib_observation.deleted and ib_node.deleted (INTEGER NOT NULL DEFAULT 0, cfg_column + ALTER), and backfills them: every
  observation with status 'withdrawn' (4,953) and every node with disposition 'withdrawn' is deleted=1;
- a node deleted by a reading before this column existed (its ib_observation_change row: column disposition, new value withdrawn,
  with a reading) is moved to the column: deleted=1 and disposition set back to empty, each kept in ib_observation_change;
- cfg_setting reading.verse_loop: the action `merge` (a duplicate description merged into the observation that is kept);
- cfg_method_rule RS-04 restated.
The readers and writers are in iba/app/lib (observationrecord.py, reading.py and the other modules that read live observations).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2323_v1_20261027.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2323-DELETED-COLUMNS-20261027"
MODULE = "analysis_phase_1_2323_v1_20261027"
SRC = "#2323 (researcher, chat 2026-10-27)"
FILLED = "iba/app/lib/observationrecord.py (soft_delete_observation, delete_node, merge_observation); iba/app/lib/recordingpass.py; iba/app/lib/strandreading.py"
OBS_USE = ("soft delete (#2323): 1 when the observation is deleted. The reading sets it with its reason in ib_observation_change; "
           "status 'withdrawn' is kept equal for the readers that still look at status. Never a physical delete")
NODE_USE = ("soft delete (#2323): 1 when the node is deleted: by a reading, or by the claims step (disposition withdrawn). "
            "disposition is the claims ending of a node (told, claim, held, data, context, withdrawn) and is not a delete by a reading. "
            "Never a physical delete")
RS04 = ("When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse and "
        "accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), "
        "soft deleted (the `deleted` column; observation withdrawn, or the node deleted, with the reason) or, for a duplicate "
        "description, merged into the observation that is kept (its nodes move to it; the duplicate is soft deleted). The check "
        "lists the errors it finds with a proposed fix; the reading confirms each fix. Nothing is physically deleted.")


class Refused(Exception):
    pass


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    for table, use in (("ib_observation", OBS_USE), ("ib_node", NODE_USE)):
        if not one("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name='deleted'", table):
            o = one("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE database='iba' AND table_name=?", table)[0]
            ops.append(("cfg_column", "insert", {}, {
                "database": "iba", "table_name": table, "name": "deleted", "ordinal": o, "type": "INTEGER", "is_pk": 0,
                "notnull": 1, "is_unique": 0, "dflt": "0", "fk": None, "use": use, "expectation": "0 or 1", "source": SRC,
                "filled_by": FILLED, "inactive": 0}))
    loop = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.verse_loop'")[0])
    if "merge" not in loop["existing_actions"]:
        loop["existing_actions"] = list(loop["existing_actions"]) + ["merge"]
        ops.append(("cfg_setting", "update", {"key": "reading.verse_loop"}, {"value": json.dumps(loop)}))
    row = one("SELECT id FROM cfg_method_rule WHERE rule_key LIKE 'RS-04 %' AND active=1")
    if row:
        ops.append(("cfg_method_rule", "update", {"id": row[0]}, {"rule_text": RS04, "source_doc": SRC}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2323: the deleted columns of ib_observation and ib_node; run_id "
                       f"{RUN_ID}. inactive=1 once applied."}))
    return ops


def data_moves(conn) -> dict:
    """The data written outside cfg_*: the backfill and the move of the nodes a reading deleted through disposition."""
    cols_o = {r[1] for r in conn.execute("PRAGMA table_info(ib_observation)")}
    cols_n = {r[1] for r in conn.execute("PRAGMA table_info(ib_node)")}
    moved = [r[0] for r in conn.execute(
        "SELECT DISTINCT c.node_id FROM ib_observation_change c JOIN ib_node n ON n.id=c.node_id WHERE c.column_name='disposition' "
        "AND c.new_value='withdrawn' AND c.reading_id IS NOT NULL AND n.disposition='withdrawn'")]
    return {"add_obs": "deleted" not in cols_o, "add_node": "deleted" not in cols_n, "moved": moved}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    ops = plan(conn)
    dm = data_moves(conn)
    summary = ", ".join(f"{t} {op}" for t, op, _, _ in ops)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} cfg write(s): {summary}; add deleted to ib_observation: {dm['add_obs']}, to ib_node: "
              f"{dm['add_node']}; nodes a reading deleted through disposition, to move: {dm['moved']}")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if dm["add_obs"]:
            conn.execute('ALTER TABLE ib_observation ADD COLUMN "deleted" INTEGER NOT NULL DEFAULT 0')
        if dm["add_node"]:
            conn.execute('ALTER TABLE ib_node ADD COLUMN "deleted" INTEGER NOT NULL DEFAULT 0')
        n_obs = conn.execute("UPDATE ib_observation SET deleted=1 WHERE status='withdrawn' AND deleted=0").rowcount
        n_node = conn.execute("UPDATE ib_node SET deleted=1 WHERE disposition='withdrawn' AND deleted=0").rowcount
        for nid in dm["moved"]:
            n = conn.execute("SELECT observation_id FROM ib_node WHERE id=?", (nid,)).fetchone()
            ch = conn.execute("SELECT reading_id, run_id FROM ib_observation_change WHERE node_id=? AND column_name='disposition' "
                              "AND new_value='withdrawn' ORDER BY id DESC LIMIT 1", (nid,)).fetchone()
            conn.execute("UPDATE ib_node SET disposition=NULL WHERE id=?", (nid,))
            for col, old, new in (("disposition", "withdrawn", None), ("deleted", "0", "1")):
                conn.execute("INSERT INTO ib_observation_change (observation_id, node_id, column_name, old_value, new_value, reason, "
                             "reading_id, run_id, created_by) VALUES (?,?,?,?,?,?,?,?,?)",
                             (n["observation_id"], nid, col, old, new,
                              "moved to the deleted column (#2323): a reading's delete is not a claims disposition",
                              ch["reading_id"], RUN_ID, "migration"))
    print(f"{len(ops)} cfg write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {summary}; deleted backfilled: "
          f"{n_obs} observation(s), {n_node} node(s); moved to the column: {dm['moved']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
