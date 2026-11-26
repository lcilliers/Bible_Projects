"""temp_2618_encode_test_run.py -- escalations #2618 and #2576: the session's hand repairs encoded into the packages.

Runs on a COPY of iba.db (dbsnapshot.copy_db of live into <scratch dir>), never the live database:
  E1  encode_2618_v1_20261126.py applies on the copy; a second run writes nothing (idempotent); the file is not archived from a copy
  E2  the step collection.release_dead_traces is registered with its two write grants, and rule B:137 with its scope row
  E3  ReleaseDeadTraces through its handler: -Check counts and writes nothing; the run drops every dead trace, each logged; a second run finds none
  E4  the 3.1 instruction keeps B:72 (the meaning of the routes) beside its method rules, and RG-06 names it
  E5  no cfg_utility row names a file that does not exist (cfgquality.find_utility_paths_missing)
  E6  the grounds check compares words: each grounds refused this session for a typographic quote or punctuation passes; a word not in the verse still fails
  E7  ReadEvidence releases the dead traces of its scope before its checks (code read)
Usage: python iba/app/tools/temp_2618_encode_test_run.py <scratch dir>. Prints PASS/FAIL per case.
"""
import inspect
import os
import pathlib
import subprocess
import sys
import time

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import cfgquality, layerreading as lr, readcommands as rc  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = ROOT / "iba/app/migration/encode_2618_v1_20261126.py"
MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name
RESULTS = []


def case(code, what, ok, detail=""):
    RESULTS.append((code, what, bool(ok), detail))
    print(f"| {code} | {what} | {'PASS' if ok else 'FAIL'} | {detail} |")


def main(scratch):
    t0 = time.monotonic()
    S = pathlib.Path(scratch) / "t2618enc"
    S.mkdir(parents=True, exist_ok=True)
    for f in S.glob("iba.db*"):
        f.unlink()
    db = copy_db(S / "iba.db", LIVE)
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1", "IBA_NO_SNAPSHOT": "1"}
    r1 = subprocess.run([sys.executable, str(MIG), "--db", str(db), "--no-snapshot"], capture_output=True, text=True, env=env)
    r2 = subprocess.run([sys.executable, str(MIG), "--db", str(db), "--no-snapshot"], capture_output=True, text=True, env=env)
    case("E1", "the migration applies on the copy, a second run writes nothing, the file is not archived from a copy",
         "applied" in r1.stdout and "already applied: 0" in r2.stdout and MIG.exists(), (r1.stdout + r1.stderr).strip()[-160:] + " / " + r2.stdout.strip())
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    grants = conn.execute("SELECT count(*) FROM cfg_write_grant WHERE writer='collection.release_dead_traces'").fetchone()[0]
    rule = conn.execute("SELECT count(*) FROM cfg_behaviour_rule WHERE id=137 AND rule_key='core-methods-absorb-every-intervention' AND active=1").fetchone()[0]
    scope = conn.execute("SELECT count(*) FROM cfg_rule_scope WHERE rule_ref='B:137'").fetchone()[0]
    step = conn.execute("SELECT handler FROM cfg_step WHERE step='collection.release_dead_traces'").fetchone()
    case("E2", "the step, its two write grants, rule B:137 and its scope row are registered", step and grants == 2 and rule == 1 and scope == 1, f"step {step}, grants {grants}")

    from iba.app.handlers import collectionbuild as cb
    from iba.app.handlers.base import Ctx

    class P(dict):
        pass
    before = conn.execute("SELECT count(*) FROM ib_node n JOIN ib_observation t ON t.id=n.traced_observation_id JOIN ib_observation o ON o.id=n.observation_id "
                          "WHERE n.deleted=0 AND t.deleted=1 AND o.deleted=0").fetchone()[0]
    ctx = Ctx.__new__(Ctx)
    ctx.cfg, ctx.run_id, ctx.params = cfg, "T2618ENC", {"Check": True}
    o1 = cb.release_dead_traces(ctx)
    mid = conn.execute("SELECT count(*) FROM ib_node n JOIN ib_observation t ON t.id=n.traced_observation_id JOIN ib_observation o ON o.id=n.observation_id "
                       "WHERE n.deleted=0 AND t.deleted=1 AND o.deleted=0").fetchone()[0]
    ctx.params = {}
    os.environ["IBA_NO_SNAPSHOT"] = "1"
    o2 = cb.release_dead_traces(ctx)
    after = conn.execute("SELECT count(*) FROM ib_node n JOIN ib_observation t ON t.id=n.traced_observation_id JOIN ib_observation o ON o.id=n.observation_id "
                         "WHERE n.deleted=0 AND t.deleted=1 AND o.deleted=0").fetchone()[0]
    logged = conn.execute("SELECT count(*) FROM ib_observation_change WHERE run_id='T2618ENC' AND column_name='deleted' AND reason LIKE 'traced observation % is deleted%'").fetchone()[0]
    ctx.params = {}
    o3 = cb.release_dead_traces(ctx)
    case("E3", "-Check writes nothing; the run drops every dead trace, each logged; a second run finds none",
         before == mid and after == 0 and logged == before and "nothing to release" in str(getattr(o3, "message", o3)),
         f"before {before}, after check {mid}, after {after}, logged {logged}")

    ins = rc.instruction(conn, rc.settings(cfg)["elements"])
    keys = [k["rule"] for k in ins["keep"]]
    rg06 = next((k["text"] for k in ins["keep"] if k["rule"].startswith("RG-06")), "")
    case("E4", "the 3.1 instruction keeps B:72 and RG-06 names it", any(k.startswith("B:72 ") for k in keys) and "cfg_behaviour_rule 72" in rg06, [k for k in keys if k.startswith("B:")])

    miss = cfgquality.find_utility_paths_missing(conn, ROOT)
    case("E5", "no cfg_utility row names a file that does not exist", not miss, miss[:2])

    pairs = [("do not care about anyone's opinion", "we know that you are true and do not care about anyone’s opinion."),
             ("He answered, For the sake of forty", "He answered, “ For the sake of forty I will not do it.”"),
             ("to set one's mind on", "to think, regard, hold an opinion; to set one’s mind on; to have"),
             ("A rich man's wealth is his strong city", "A rich man’s wealth is his strong city, and like a high wall"),
             ("When I thought, My foot slips, your steadfast love", "When I thought, “ My foot slips,” your steadfast love, O Lord, held me up.")]
    good = all(lr._words(g) in lr._words(v) for g, v in pairs)
    bad = lr._words("care about any") in lr._words(pairs[0][1]) or lr._words("a word not there") in lr._words(pairs[0][1])
    case("E6", "grounds with typographic quotes or punctuation pass; a part-word or absent words still fail", good and not bad)

    src = inspect.getsource(rc.read_evidence)
    case("E7", "ReadEvidence releases the dead traces of its scope before its checks",
         src.index("release_dead_traces") < src.index("evidence_check(conn"))
    conn.rollback()
    n_ok = sum(1 for r in RESULTS if r[2])
    print(f"\n{n_ok} of {len(RESULTS)} pass ({round(time.monotonic() - t0, 1)} s)")
    return 0 if n_ok == len(RESULTS) else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python iba/app/tools/temp_2618_encode_test_run.py <scratch dir>")
    sys.exit(main(sys.argv[1]))
