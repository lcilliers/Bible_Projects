"""marker_at_creation_2538_v1_20261124.py -- escalation #2538 (researcher, 2026-11-24: "Marker at creation", then "Approve as proposed"; plan outputs/escalation/2538-marker-at-creation-plan-v1-20261124.md).

The stage 1 to 4 recording writes the marker (ib_observation.nature) and the required node columns when it creates an observation. Config only; the code is lib/layerreading.py and lib/layerinner.py:
  settings   layer.reading gains items.<item>.nature, node_required (the word-node columns required at creation) and node_gap_columns (the columns the data may leave empty, with the reason kept on the node) and
             node_required_from_layer (a column required only from a layer on: the subgroup, once the grouping exists)
  columns    the text of cfg_column ib_observation.nature (set at creation, changed afterwards only by the validation)
  rules      method rule VA-05 states the creation; method rule RW-12 is new
  utilities  this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/marker_at_creation_2538_v1_20261124.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2538-MARKER-AT-CREATION-20261124"
MODULE = "marker_at_creation_2538_v1_20261124"
SOURCE = "escalation #2538 (researcher, 2026-11-24; outputs/escalation/2538-marker-at-creation-plan-v1-20261124.md)"
CODE = "iba/app/lib/layerreading.py (check_natures, settle_nodes, record) and iba/app/lib/layerinner.py (record)"

NATURE = {"word-sense": "evidence", "group-definition": "evidence", "strong-enrichment": "evidence", "pairing": "evidence", "qualifier": "evidence", "entity": "evidence",
          "direction": "evidence", "group-relation": "evidence", "double-meaning": "evidence",
          "subgroup-analysis": "inner_being", "collection-gathering": "inner_being", "interworking": "inner_being"}
NODE_REQUIRED = ["strong", "verse_reference", "surface", "morph_code", "role", "verse_lexical_id", "collection_id", "subgroup_id"]
NODE_GAP_COLUMNS = ["morph_code", "subgroup_id"]
NODE_REQUIRED_FROM_LAYER = {"subgroup_id": 1}      # the grouping (layer 1) comes after the words (layer 0)

OLD_USE = "Set only by the validation (lib/validationactions.py set_nature), each setting kept in ib_observation_change with its reason"
NEW_USE = ("Set at creation by the recording of the layer steps, from the nature of the item in cfg_setting layer.reading (lib/layerreading.py, lib/layerinner.py); "
           "changed afterwards only by the validation (lib/validationactions.py set_nature), each setting kept in ib_observation_change with its reason")
VA05_ADD = (" The marker is set when the observation is created, by the item that is answered (cfg_setting layer.reading items.<item>.nature); a finding file never sets it; "
            "the validation changes it only where the content shows the item's nature does not hold.")
RW12 = ("collection.layer_record", "RW-12 marker-and-node-columns-at-creation",
        "An observation is created with its marker (ib_observation.nature, from the item answered, cfg_setting layer.reading items.<item>.nature; a finding file never sets it) and every word node "
        "with the columns of layer.reading node_required. A column the data cannot give (layer.reading node_gap_columns: an empty morph in the source row, a surface with no placement in the "
        "collection index) is left empty and its reason is kept on the node (disposition_note); any other missing column refuses the whole file and nothing is written. A trace to a deleted "
        "observation is refused (IB-07).")


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    cur = json.loads(one("SELECT value FROM cfg_setting WHERE key='layer.reading'")[0])
    new = json.loads(json.dumps(cur))
    missing = [i for i in NATURE if i not in new["items"]]
    if missing:
        raise SystemExit(f"items not in layer.reading: {missing}")
    extra = [i for i in new["items"] if i not in NATURE]
    if extra:
        raise SystemExit(f"items of layer.reading with no nature decided: {extra}")
    for i, n in NATURE.items():
        new["items"][i]["nature"] = n
    new["node_required"], new["node_gap_columns"], new["node_required_from_layer"] = NODE_REQUIRED, NODE_GAP_COLUMNS, NODE_REQUIRED_FROM_LAYER
    if new != cur:
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(new, ensure_ascii=False)}))
    use = one("SELECT use FROM cfg_column WHERE database='iba' AND table_name='ib_observation' AND name='nature'")[0]
    if OLD_USE in use:
        ops.append(("cfg_column", "update", {"database": "iba", "table_name": "ib_observation", "name": "nature"}, {"use": use.replace(OLD_USE, NEW_USE)}))
    va = one("SELECT id, rule_text FROM cfg_method_rule WHERE rule_key LIKE 'VA-05 %'")
    if VA05_ADD.strip() not in va[1]:
        ops.append(("cfg_method_rule", "update", {"id": va[0]}, {"rule_text": va[1].rstrip() + VA05_ADD}))
    if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", RW12[1]):
        nid = one("SELECT max(id) FROM cfg_method_rule")[0] + 1
        top = one("SELECT max(ordinal) FROM cfg_method_rule WHERE step=?", RW12[0])[0]
        ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": RW12[0], "rule_key": RW12[1], "rule_text": RW12[2], "source_doc": SOURCE, "enforced_by": CODE,
                                                      "ordinal": (top or 0) + 1, "active": 1}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose": f"ONE-OFF migration -- escalation #2538: marker and node columns at creation; run_id {RUN_ID}.",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or "", sorted(set_)[:4])
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-marker-at-creation-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT marker_2538")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE marker_2538")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO marker_2538")
        conn.execute("RELEASE marker_2538")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
