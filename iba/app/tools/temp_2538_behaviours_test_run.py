"""temp_2538_behaviours_test_run.py -- escalation #2538: step 3.2 as a read command (ReadBehaviours / RecordBehaviours) and the sweep that closes 3.1 (SweepSuperseded).

Researcher 2026-11-26: "step 3.2 is a fundamental part of the collection process and must be codified"; "step 3.1 is incomplete. it did not sweep the observations that are
not valid, and removed them"; "the approach and observation results for 3.2 looks good."

Runs on a COPY of iba.db (dbsnapshot.copy_db of live into <scratch dir>), never the live database, on the collection thought:
  S1  behaviours_2538_v1_20261126.py applies on the copy; a second run writes nothing; the file is not archived from a copy
  S2  the steps, grants and IB-08 are registered; the coherence check finds no analytic guide gap (every step has its read command or a deferral)
  S3  before the sweep: ReadBehaviours refuses naming SweepSuperseded, and LayerNext names SweepSuperseded
  S4  the sweep refuses while a current subgroup is not through 3.1 (one 3.1 row unvalidated on the copy), and writes nothing
  S5  SweepSuperseded -Check counts and writes nothing; the run retires every live row of a deleted subgroup and removes the observations under it, each logged; a second run finds none
  S6  ReadBehaviours after the sweep: it takes up exactly the 3.1 findings of the current subgroups, and its instruction keeps IB-08
  S7  RecordBehaviours refuses a whole answer that leaves a finding neither gathered nor declared, and writes nothing
  S9  after the sweep and the record every row of S1 to 3.2 still validates (a not_used declaration of a removed observation is set aside, layerinner.check_row)
  S8  RecordBehaviours records an answer (the file given, else one behaviour gathering every finding): -Check writes nothing; the run validates the 3.2 row; LayerNext moves past 3.2
Usage: python iba/app/tools/temp_2538_behaviours_test_run.py <scratch dir> [answer file]. Prints PASS/FAIL per case.
"""
import json
import os
import pathlib
import subprocess
import sys
import time

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import cfgquality, layerloop, layerreading as lr, readcommands as rc  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = ROOT / "iba/app/migration/behaviours_2538_v1_20261126.py"
MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name
COLL = "thought"
RESULTS = []


def case(code, what, ok, detail=""):
    RESULTS.append((code, what, bool(ok), detail))
    print(f"| {code} | {what} | {'PASS' if ok else 'FAIL'} | {str(detail)[:400]} |")


def count_live(conn):
    return conn.execute("SELECT count(*) FROM ib_observation WHERE deleted=0").fetchone()[0]


def current_31(conn, cid):
    ids = set()
    for (lid,) in conn.execute("SELECT c.id FROM collection_layer_item c JOIN collection_subgroup s ON s.id=c.subgroup_id WHERE c.collection_id=? AND c.step='3.1' AND c.deleted=0 "
                               "AND c.state!='retired' AND s.deleted=0", (cid,)):
        ids |= {r[0] for r in conn.execute("SELECT id FROM ib_observation WHERE stable_key>=? AND stable_key<? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};"))}
    return ids


def one_behaviour(conn, lid, ids, drop=None):
    occ = sorted({conn.execute("SELECT verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IS NOT NULL "
                               "ORDER BY verse_lexical_id LIMIT 1", (i,)).fetchone()[0] for i in ids})
    keep = [i for i in sorted(ids) if i != drop]
    return {"command": "ReadBehaviours", "collection": COLL, "ledger_id": lid, "disposition": "observed", "reason": "",
            "findings": [{"key": "b1", "kind": "statement", "basis": "read", "text": "A test behaviour that gathers the findings of the collection.",
                          "parts": {"item": "flag", "flag_type": "discovery", "grounds": "the test gathers every 3.1 finding"},
                          "nodes": [{"traced": i} for i in keep] + [{"occurrence": v, "role": "characteristic"} for v in occ], "read_back": []}],
            "not_gathered": {}, "older": [], "existing": []}


def main(scratch, answer_file=None):
    t0 = time.monotonic()
    S = pathlib.Path(scratch) / "t2538behaviours"
    S.mkdir(parents=True, exist_ok=True)
    for f in S.glob("iba.db*"):
        f.unlink()
    db = copy_db(S / "iba.db", LIVE)
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1", "IBA_NO_SNAPSHOT": "1"}
    r1 = subprocess.run([sys.executable, str(MIG), "--db", str(db), "--no-snapshot"], capture_output=True, text=True, env=env)
    r2 = subprocess.run([sys.executable, str(MIG), "--db", str(db), "--no-snapshot"], capture_output=True, text=True, env=env)
    case("S1", "the migration applies on the copy, a second run writes nothing, not archived from a copy",
         ("applied" in r1.stdout or "already applied" in r1.stdout) and "already applied: 0" in r2.stdout and MIG.exists(), (r1.stdout + r1.stderr).strip()[-200:])
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    steps = {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE step IN ('collection.read_behaviours','collection.record_behaviours','collection.sweep_superseded') AND inactive=0")}
    ib08 = conn.execute("SELECT count(*) FROM cfg_method_rule WHERE rule_key='IB-08 what-a-behaviour-is' AND active=1").fetchone()[0]
    gaps = cfgquality.find_analytic_guide_gaps(conn, ROOT)
    case("S2", "steps, IB-08 registered; no analytic guide gap", len(steps) == 3 and ib08 == 1 and not gaps, gaps[:3] or steps)

    cid, _ = lr.ci._collection(conn, COLL)
    out = pathlib.Path(scratch) / "t2538behaviours" / "packages"
    try:
        rc.read_behaviours(conn, cfg, "T2538B", COLL, out)
        refused = ""
    except rc.ReadError as exc:
        refused = str(exc)
    nxt = layerloop.next_action(conn, cfg, COLL)
    left = lr.superseded(conn, cid)
    case("S3", "before the sweep ReadBehaviours refuses naming SweepSuperseded, and LayerNext names it",
         "SweepSuperseded" in refused and any("SweepSuperseded" in c_ for c_ in nxt["commands"]) and left["rows"], f"{len(left['rows'])} rows, {len(left['observations'])} observations")

    row = conn.execute("SELECT c.id FROM collection_layer_item c JOIN collection_subgroup s ON s.id=c.subgroup_id WHERE c.collection_id=? AND c.step='3.1' AND c.deleted=0 "
                       "AND c.state='observed' AND s.deleted=0 ORDER BY c.id LIMIT 1", (cid,)).fetchone()[0]
    conn.execute("SAVEPOINT s4")
    conn.execute("UPDATE collection_layer_item SET validated=0 WHERE id=?", (row,))
    before = count_live(conn)
    try:
        lr.sweep_superseded(conn, cfg, "T2538B", COLL)
        why = ""
    except lr.LayerError as exc:
        why = str(exc)
    after = count_live(conn)
    conn.execute("ROLLBACK TO s4")
    conn.execute("RELEASE s4")
    case("S4", "the sweep refuses while a current subgroup is not through 3.1, and writes nothing", "waits for every current subgroup" in why and before == after, why[:160])

    n_rows, n_obs = len(left["rows"]), len(left["observations"])
    before = count_live(conn)
    chk = lr.sweep_superseded(conn, cfg, "T2538B", COLL, check=True)
    mid = count_live(conn)
    lr.sweep_superseded(conn, cfg, "T2538B", COLL)
    after = count_live(conn)
    logged = len(set(left["observations"]) & {r[0] for r in conn.execute("SELECT DISTINCT observation_id FROM ib_observation_change WHERE run_id='T2538B' AND column_name='deleted' "
                                                                            "AND reason LIKE '%sweep at the close of 3.1%'")})
    retired = conn.execute("SELECT count(*) FROM collection_layer_item WHERE run_id='T2538B' AND state='retired'").fetchone()[0]
    again = lr.sweep_superseded(conn, cfg, "T2538B", COLL, check=True)
    case("S5", "-Check writes nothing; the sweep retires every row and removes every observation, logged; a second run finds none",
         chk["rows"] == n_rows and mid == before and before - after == n_obs and logged == n_obs and retired == n_rows and again["rows"] == 0 and again["observations"] == 0,
         f"rows {n_rows}, observations {n_obs}, removed {before - after}, logged {logged}, retired {retired}")

    want = current_31(conn, cid)
    res = rc.read_behaviours(conn, cfg, "T2538B", COLL, out)
    pkg = json.loads(pathlib.Path(res["path"]).read_text(encoding="utf-8"))
    got = {x["observation"] for x in pkg["to_take_up"]}
    rules = [k["rule"] for k in pkg["instruction"]["keep"]]
    case("S6", "ReadBehaviours takes up exactly the 3.1 findings of the current subgroups; IB-08 in its instruction",
         got == want and any(r_.startswith("IB-08") for r_ in rules), f"{len(got)} taken up, {len(want)} 3.1 findings, chars {res['chars']}")
    lid = pkg["unit"]["ledger_id"]

    before = count_live(conn)
    bad = one_behaviour(conn, lid, want, drop=sorted(want)[0])
    try:
        rc.record_behaviours(conn, cfg, "T2538B", bad, keep=True)
        why = ""
    except rc.ReadError as exc:
        why = str(exc)
    case("S7", "an answer that leaves a finding neither gathered nor declared is refused whole, nothing written",
         "neither rested on by a finding nor in not_gathered" in why and count_live(conn) == before, why[:200])

    ans = json.loads(pathlib.Path(answer_file).read_text(encoding="utf-8")) if answer_file else one_behaviour(conn, lid, want)
    ans["ledger_id"] = lid
    before = count_live(conn)
    pv = rc.record_behaviours(conn, cfg, "T2538B", ans, keep=False)
    mid = count_live(conn)
    rr = rc.record_behaviours(conn, cfg, "T2538B", ans, keep=True)
    nxt = layerloop.next_action(conn, cfg, COLL)
    rep = lr.check(conn, cfg, "T2538B", COLL)
    failed = {k: v["failed"] for k, v in rep["steps"].items() if v["failed"] and k in ("S1", "1.1", "1.2", "2.1", "3.1", "3.2")}
    case("S9", "after the sweep and the record, every row of S1 to 3.2 of the current subgroups still validates (a declaration of a removed observation is set aside)",
         not failed, failed)
    case("S8", "RecordBehaviours: -Check writes nothing; the run validates the 3.2 row; LayerNext moves past 3.2",
         pv.get("preview") and mid == before and rr.get("validated") and nxt.get("step") != "3.2",
         f"observed {rr.get('observed')}, nodes {rr.get('nodes')}, reason {rr.get('reason')!r}; next {nxt.get('step')} {nxt.get('state')}")
    conn.rollback()
    n_ok = sum(1 for r in RESULTS if r[2])
    print(f"\n{n_ok} of {len(RESULTS)} pass ({round(time.monotonic() - t0, 1)} s)")
    return 0 if n_ok == len(RESULTS) else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python iba/app/tools/temp_2538_behaviours_test_run.py <scratch dir> [answer file]")
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
