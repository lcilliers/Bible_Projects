"""validation_in_build_2538_v1_20261124.py -- escalation #2538 (researcher, 2026-11-24: the validation is part of the build, every scan is pinpointed, nothing is left in the air; plan
outputs/escalation/2538-validation-in-the-build-plan-v1-20261124.md, approved with its four decisions).

  indexes    ib_node(collection_id), ib_node(strong, surface), ib_observation(stable_key), ib_observation_change(column_name, new_value): each a cfg_index row and the physical index
  settings   layer.scan (the work a statement may use, the chunk, the tables a lookup may scan) and layer.reading (step 3.1 opens only when the evidence validation passes;
             step 3.3 closes only when the whole validation passes; step 2.1 sweeps the unmarked older observations of its subgroup, sweep_unmarked)
  rules      method rules RW-13 (older observations answered at record) and RW-14 (every lookup pinpointed); IB-01, IB-05 and VA-06 amended; the behaviour rule
             collection-validation-follows-stage-4 states the build
  utilities  scanguard, buildvalidate and this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/validation_in_build_2538_v1_20261124.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2538-VALIDATION-IN-BUILD-20261124"
MODULE = "validation_in_build_2538_v1_20261124"
SOURCE = "escalation #2538 (researcher, 2026-11-24; outputs/escalation/2538-validation-in-the-build-plan-v1-20261124.md)"
CODE = "iba/app/lib/buildvalidate.py, iba/app/lib/scanguard.py, iba/app/lib/layerreading.py and iba/app/lib/layerinner.py"

INDEXES = [("ib_node", "idx_ib_node_collection", ["collection_id"]),
           ("ib_node", "idx_ib_node_strong_surface", ["strong", "surface"]),
           ("ib_observation", "idx_ib_observation_stable_key", ["stable_key"]),
           ("ib_observation_change", "idx_ib_observation_change_column_value", ["column_name", "new_value"])]
SCAN = {"max_vm_ops": 1000000, "progress_step": 1000, "chunk": 400, "scan_ok": ["_vpairs"],
        "large_tables": ["ib_node", "ib_observation", "ib_observation_change", "verse_lexical", "span"]}
SCAN_USE = ("the protection against a long scan (#2538, lib/scanguard.py): max_vm_ops is the work one statement of the build's lookups may use before it is stopped, progress_step how often it is "
            "counted, chunk the ids a lookup takes at a time, scan_ok the temporary tables of ids or pairs a statement may scan, large_tables the tables whose scan the tests refuse")

AMEND = {
    "IB-01 ": " Step 3.1 opens only when the evidence validation of the collection passes (lib/collectionvalidate.py check, evidence layer: every observation of the scope marked, none without a live node, "
              "no word node missing a required column without its reason, no trace to a deleted observation, no two of one text), so evidence and inner being are never validated together (VA-06).",
    "IB-05 ": " Every older live observation with a node on an occurrence of the row is answered in fill.older at the record of the row (RW-13); this rule's `existing` actions of stage 4 are unchanged.",
    "VA-06 ": " In the build this gate is: step 3.1 does not open before the evidence layer passes, and step 3.3 does not close before both layers pass (cfg_setting layer.reading open_gate and closing_gate).",
}
RW13 = ("collection.layer_record", "RW-13 older-observations-answered-at-record",
        "Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate "
        "(each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or "
        "defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. "
        "A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's "
        "build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.")
RW14 = ("collection.layer_record", "RW-14 every-lookup-is-pinpointed",
        "A lookup of related data in the build or the validation is by an indexed column and takes a chunk of ids (cfg_setting layer.scan chunk); none runs once for each item of a list, and a "
        "statement that uses more work than layer.scan max_vm_ops is stopped and named, nothing written (lib/scanguard.py). The tests refuse a statement of the build whose query plan scans a table "
        "(layer.scan scan_ok lists the temporary tables a statement may scan).")
BEHAVIOUR_ADD = (" The validation is part of the build: the marker and the node columns are set at creation, an older observation on the occurrences of a row is answered when the row is recorded, "
                 "step 3.1 opens only when the evidence layer passes and step 3.3 closes only when both layers pass (RW-12, RW-13; cfg_setting layer.reading); ValidatePull, ValidateRecord and "
                 "ValidateCheck remain as the audit that must find nothing and for a collection built before this change.")
UTILITIES = [
    ("scanguard", "iba/app/lib/scanguard.py", 0, "scanguard.py -- the protection against a long scan (escalation #2538): a work budget for a statement and the check of a query plan.", 0,
     None),
    ("buildvalidate", "iba/app/lib/buildvalidate.py", 0, "buildvalidate.py -- the validation made part of the build (escalation #2538): the answers to older observations, the text clash, the row tests and the closing gate.", 0,
     None),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2538: the validation in the build; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    for table, name, cols in INDEXES:
        for i, c in enumerate(cols):
            if not one("SELECT 1 FROM cfg_index WHERE table_name=? AND name=? AND col=?", table, name, c):
                ops.append(("cfg_index", "insert", {}, {"table_name": table, "name": name, "col": c, "ordinal": i}))
    if not one("SELECT 1 FROM cfg_setting WHERE key='layer.scan'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "layer.scan", "value": json.dumps(SCAN), "use": SCAN_USE, "module": "layer", "inactive": 0}))
    cur = json.loads(one("SELECT value FROM cfg_setting WHERE key='layer.reading'")[0])
    new = json.loads(json.dumps(cur))
    for st in new["steps"]:
        if st["key"] == "3.1":
            st["open_gate"] = "evidence"
        if st["key"] == "3.3":
            st["closing_gate"] = True
        if st["key"] == "2.1":
            st["sweep_unmarked"] = True     # the loop reviews the unmarked older observations of the subgroup for deletion after this step (delete_unmarked)
    if new != cur:
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(new, ensure_ascii=False)}))
    nid = one("SELECT max(id) FROM cfg_method_rule")[0]
    top = one("SELECT max(ordinal) FROM cfg_method_rule WHERE step='collection.layer_record'")[0] or 0
    for step, key, text in (RW13, RW14):
        if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", key):
            nid += 1
            top += 1
            ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": step, "rule_key": key, "rule_text": text, "source_doc": SOURCE, "enforced_by": CODE, "ordinal": top, "active": 1}))
    for prefix, add in AMEND.items():
        r = one("SELECT id, rule_text FROM cfg_method_rule WHERE rule_key LIKE ?", prefix + "%")
        if add.strip() not in r[1]:
            ops.append(("cfg_method_rule", "update", {"id": r[0]}, {"rule_text": r[1].rstrip() + add}))
    b = one("SELECT id, rule_text FROM cfg_behaviour_rule WHERE rule_key='collection-validation-follows-stage-4'")
    if BEHAVIOUR_ADD.strip() not in b[1]:
        ops.append(("cfg_behaviour_rule", "update", {"id": b[0]}, {"rule_text": b[1].rstrip() + BEHAVIOUR_ADD}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not one("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt, "config_exempt_reason": reason,
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
    missing_ix = [n for _, n, _ in INDEXES if not conn.execute("SELECT 1 FROM sqlite_master WHERE type='index' AND name=?", (n,)).fetchone()]
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); physical index(es) to create: {missing_ix}")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or "", set_.get("name") or set_.get("key") or set_.get("rule_key") or set_.get("module") or "")
        return 0
    if not ops and not missing_ix:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-validation-in-build-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT validation_in_build")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for table, name, cols in INDEXES:
            conn.execute(f"CREATE INDEX IF NOT EXISTS {name} ON {table} ({', '.join(cols)})")
        conn.execute("ANALYZE")
        conn.execute("RELEASE validation_in_build")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO validation_in_build")
        conn.execute("RELEASE validation_in_build")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); indexes {[n for _, n, _ in INDEXES]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
