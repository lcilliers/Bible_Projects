"""temp_2538_stage_test_run.py -- escalation #2538: each stage-4 step writes its own stage on the observation (layer-3.1, layer-3.2, layer-3.3).

Researcher 2026-11-26: "I agree, the layer must be part of it. not sure if it belongs on the observation or the node. (probably the observation)."

Runs on a COPY of iba.db (dbsnapshot.copy_db of live into <scratch dir>), never the live database:
  T1  stage_2538_v1_20261126.py applies on the copy; a second run writes nothing; the file is not archived from a copy
  T2  no live observation under a 3.1, 3.2 or 3.3 row keeps the stage layer-3; each holds the stage of its step; each relabel is logged with its reason
  T3  layerreading.stage_of gives layer-3.1 / layer-3.2 / layer-3.3 for the stage-4 steps and the layer's stage for the others
  T4  every live row of 3.1 and 3.2 of thought still validates (LayerCheck, layerinner.check_row compares the step's stage)
  T5  a 3.2 recorded again on the copy writes layer-3.2 (RecordBehaviours with one behaviour gathering every finding)
  T6  restage_observation refuses a stage not in cfg_enum and a deleted observation
Usage: python iba/app/tools/temp_2538_stage_test_run.py <scratch dir>. Prints PASS/FAIL per case.
"""
import os
import pathlib
import subprocess
import sys
import time

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import layerreading as lr, observationrecord as orec, readcommands as rc  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = ROOT / "iba/app/migration/stage_2538_v1_20261126.py"
MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name
STEP_STAGE = {"3.1": "layer-3.1", "3.2": "layer-3.2", "3.3": "layer-3.3"}
RESULTS = []


def case(code, what, ok, detail=""):
    RESULTS.append((code, what, bool(ok), detail))
    print(f"| {code} | {what} | {'PASS' if ok else 'FAIL'} | {str(detail)[:300]} |")


def under_steps(conn):
    out = []
    for lid, step in conn.execute("SELECT id, step FROM collection_layer_item WHERE step IN ('3.1','3.2','3.3')").fetchall():
        out += [(r[0], r[1], step) for r in conn.execute("SELECT id, stage FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};"))]
    return out


def main(scratch):
    t0 = time.monotonic()
    S = pathlib.Path(scratch) / "t2538stage"
    S.mkdir(parents=True, exist_ok=True)
    for f in S.glob("iba.db*"):
        f.unlink()
    db = copy_db(S / "iba.db", LIVE)
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1", "IBA_NO_SNAPSHOT": "1"}
    r1 = subprocess.run([sys.executable, str(MIG), "--db", str(db), "--no-snapshot"], capture_output=True, text=True, env=env)
    r2 = subprocess.run([sys.executable, str(MIG), "--db", str(db), "--no-snapshot"], capture_output=True, text=True, env=env)
    case("T1", "the migration applies on the copy, a second run writes nothing, not archived from a copy",
         ("applied" in r1.stdout or "already applied" in r1.stdout) and "already applied: 0 write(s), 0 observation" in r2.stdout and MIG.exists(), (r1.stdout + r1.stderr).strip()[-200:])
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    obs = under_steps(conn)
    wrong = [o for o in obs if o[1] != STEP_STAGE[o[2]]]
    logged = conn.execute("SELECT count(*) FROM ib_observation_change WHERE run_id='DEVMODE-2538-STAGE-20261126' AND column_name='stage' AND old_value='layer-3'").fetchone()[0]
    case("T2", "every live observation under a 3.1/3.2/3.3 row holds the stage of its step, each relabel logged", obs and not wrong and logged == len(obs),
         f"{len(obs)} observations, {len(wrong)} wrong, {logged} relabels logged")
    s = lr.settings(cfg)
    got = {k: lr.stage_of(s, lr.step_def(s, k)) for k in ("S1", "1.1", "1.2", "2.1", "3.1", "3.2", "3.3")}
    case("T3", "stage_of: the step's own stage at stage 4, the layer's elsewhere",
         got == {"S1": "lexical", "1.1": "layer-1", "1.2": "layer-1", "2.1": "layer-2", "3.1": "layer-3.1", "3.2": "layer-3.2", "3.3": "layer-3.3"}, got)
    rep = lr.check(conn, cfg, "T2538S", "thought")
    failed = {k: v["failed"] for k, v in rep["steps"].items() if v["failed"] and k in ("3.1", "3.2")}
    case("T4", "every live row of 3.1 and 3.2 of thought still validates", not failed and rep["steps"].get("3.2", {}).get("closed"), failed)

    cid, _ = lr.ci._collection(conn, "thought")
    row = rc._behaviours_row(conn, cid)
    conn.execute("UPDATE collection_layer_item SET validated=0 WHERE id=?", (row[0],))     # 3.2 recorded again on the copy
    want = set()
    for (lid,) in conn.execute("SELECT c.id FROM collection_layer_item c JOIN collection_subgroup g ON g.id=c.subgroup_id WHERE c.collection_id=? AND c.step='3.1' AND c.deleted=0 "
                               "AND c.state!='retired' AND g.deleted=0", (cid,)):
        want |= {r[0] for r in conn.execute("SELECT id FROM ib_observation WHERE stable_key>=? AND stable_key<? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};"))}
    occ = sorted({conn.execute("SELECT verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IS NOT NULL "
                               "ORDER BY verse_lexical_id LIMIT 1", (i,)).fetchone()[0] for i in want})
    ans = {"command": "ReadBehaviours", "collection": "thought", "ledger_id": row[0], "disposition": "observed", "reason": "",
           "findings": [{"key": "b1", "kind": "statement", "basis": "read", "text": "A test behaviour that gathers the findings of the collection.",
                         "parts": {"item": "flag", "flag_type": "discovery", "grounds": "the test gathers every 3.1 finding"},
                         "nodes": [{"traced": i} for i in sorted(want)] + [{"occurrence": v, "role": "characteristic"} for v in occ], "read_back": []}],
           "not_gathered": {}, "older": [], "existing": []}
    rr = rc.record_behaviours(conn, cfg, "T2538S", ans, keep=True)
    st = [r[0] for r in conn.execute("SELECT stage FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{row[0]}:", f"layer:{row[0]};"))]
    case("T5", "a 3.2 recorded again writes layer-3.2 and validates", rr.get("validated") and st == ["layer-3.2"], f"{st}, validated {rr.get('validated')}")

    some = obs[0][0]
    errs = []
    for bad in (lambda: orec.restage_observation(cfg, conn, some, "layer-9", "a test of the refusal", None, "T2538S", "Claude"),
                lambda: orec.restage_observation(cfg, conn, conn.execute("SELECT id FROM ib_observation WHERE deleted=1 LIMIT 1").fetchone()[0], "layer-3.1",
                                                 "a test of the refusal", None, "T2538S", "Claude")):
        try:
            bad()
            errs.append("not refused")
        except orec.Refused as exc:
            errs.append(str(exc)[:60])
    case("T6", "restage_observation refuses an unknown stage and a deleted observation", "not refused" not in errs, errs)
    conn.rollback()
    n_ok = sum(1 for r in RESULTS if r[2])
    print(f"\n{n_ok} of {len(RESULTS)} pass ({round(time.monotonic() - t0, 1)} s)")
    return 0 if n_ok == len(RESULTS) else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python iba/app/tools/temp_2538_stage_test_run.py <scratch dir>")
    sys.exit(main(sys.argv[1]))
