"""stage_2538_v1_20261126.py -- escalation #2538 (researcher 2026-11-26: "I agree, the layer must be part of it. not sure if it belongs on the observation or the node.
(probably the observation).").

Each step of stage 4 writes its own stage on the observation, so that an observation says which step wrote it:
  cfg_enum         ib_observation.stage: layer-3.1, layer-3.2, layer-3.3
  cfg_setting      layer.reading stages: "3.1", "3.2", "3.3" (read by layerreading.stage_of; the layer's own "3" stays for the history)
  cfg_method_rule  IB-05 and IB-06 name the stage of the step
  ib_observation   every live observation written under a 3.1, 3.2 or 3.3 ledger row relabelled from layer-3 to the stage of its step, through
                   observationrecord.restage_observation (each change kept with its reason)
  cfg_utility      this migration's own row
Config through configmaint.apply_logged; the observations through observationrecord. Named snapshot before a live apply; after the live apply the file archives itself.
Idempotent. Usage: python iba/app/migration/stage_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2538-STAGE-20261126"
MODULE = "stage_2538_v1_20261126"
STAGES = {"3.1": "layer-3.1", "3.2": "layer-3.2", "3.3": "layer-3.3"}
ENUM = [("layer-3.1", 16), ("layer-3.2", 17), ("layer-3.3", 18)]
REASON = ('the stage names the step that wrote the observation (researcher 2026-11-26, #2538: "the layer must be part of it ... (probably the observation)"); '
          'relabelled from layer-3 by the step of its ledger row')
IB05_OLD, IB05_NEW = "(any stage but lexical, layer-1, layer-2 and layer-3)", "(any stage but those of the build: lexical, layer-1, layer-2, layer-3.1 to layer-3.3, and layer-3 before 2026-11-26)"
IB06_OLD, IB06_NEW = "at least one live observation of stage layer-3 with its stable_key on the row", "at least one live observation of the stage of its step (layer-3.1, layer-3.2 or layer-3.3) with its stable_key on the row"


def plan(conn):
    ops = []
    have = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name='ib_observation.stage'")}
    for v, o in ENUM:
        if v not in have:
            ops.append(("cfg_enum", "insert", {}, {"name": "ib_observation.stage", "value": v, "ordinal": o, "inactive": 0}))
    lay = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.reading'").fetchone()[0])
    if any(lay["stages"].get(k) != v for k, v in STAGES.items()):
        lay["stages"] = {**lay["stages"], **STAGES}
        ops.append(("cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(lay, ensure_ascii=False)}))
    for key, old, new in (("IB-05 earlier-observations-are-shown-not-demanded", IB05_OLD, IB05_NEW), ("IB-06 stage-4-check-rederives-from-the-tables", IB06_OLD, IB06_NEW)):
        text = conn.execute("SELECT rule_text FROM cfg_method_rule WHERE rule_key=?", (key,)).fetchone()[0]
        if old in text:
            ops.append(("cfg_method_rule", "update", {"rule_key": key}, {"rule_text": text.replace(old, new)}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2538: a stage per stage-4 step (layer-3.1, layer-3.2, layer-3.3) and the observations relabelled",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def relabel(conn):
    """[(observation id, new stage)] for the live observations of stage layer-3 written under a live or retired 3.1, 3.2 or 3.3 row (the stable key range of the row)."""
    out = []
    for lid, step in conn.execute("SELECT id, step FROM collection_layer_item WHERE step IN ('3.1','3.2','3.3')").fetchall():
        for (oid,) in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0 AND stage='layer-3'", (f"layer:{lid}:", f"layer:{lid};")):
            out.append((oid, STAGES[step]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    live = pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    todo = relabel(conn)
    if a.dry_run or (not ops and not todo):
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s), {len(todo)} observation(s) to relabel")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: set_[k] for k in list(set_)[:3]})
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-stage-apply', named=True)}")
    from iba.app.lib import observationrecord as orec
    try:
        conn.execute("SAVEPOINT rel")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        n = sum(1 for oid, st in todo if orec.restage_observation(cfg, conn, oid, st, REASON, None, RUN_ID, "Claude"))      # cfg.enum reads the enum just written
        conn.execute("RELEASE rel")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rel")
        conn.execute("RELEASE rel")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s), {n} observation(s) relabelled")
    if live:
        new = archive_migration(conn, RUN_ID, __file__)
        conn.commit()
        print(f"archived: {new}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
