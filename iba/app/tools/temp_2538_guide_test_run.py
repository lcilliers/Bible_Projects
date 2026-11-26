"""temp_2538_guide_test_run.py -- escalation #2538: the analytic process described as one path of methods in USER-GUIDE.md 8.20, checked by config.

Runs on a COPY of iba.db (dbsnapshot.copy_db of live into <scratch dir>), never the live database:
  G1  guide_2538_v1_20261126.py applies on the copy; a second run writes nothing; the file is not archived from a copy
  G2  cfgquality.find_analytic_guide_gaps finds nothing on the guide as it stands
  G3  a read command added to layer.read_types that the section does not name is found, with its Record half
  G4  a guide naming a section that does not exist is found; a read_types with no guide is found
  G5  LayerNext's read-command lookup and the 3.1 instruction still read layer.read_types with the guide in it
  G6  configmaint.validate runs the check (code read)
Usage: python iba/app/tools/temp_2538_guide_test_run.py <scratch dir>. Prints PASS/FAIL per case.
"""
import inspect
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
from iba.app.lib import cfgquality, readcommands as rc  # noqa: E402
from iba.app.handlers import configmaint  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = ROOT / "iba/app/migration/guide_2538_v1_20261126.py"
MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name
RESULTS = []


def case(code, what, ok, detail=""):
    RESULTS.append((code, what, bool(ok), detail))
    print(f"| {code} | {what} | {'PASS' if ok else 'FAIL'} | {detail} |")


def set_types(conn, types):
    conn.execute("UPDATE cfg_setting SET value=? WHERE key='layer.read_types'", (json.dumps(types),))


def main(scratch):
    t0 = time.monotonic()
    S = pathlib.Path(scratch) / "t2538guide"
    S.mkdir(parents=True, exist_ok=True)
    for f in S.glob("iba.db*"):
        f.unlink()
    db = copy_db(S / "iba.db", LIVE)
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1", "IBA_NO_SNAPSHOT": "1"}
    r1 = subprocess.run([sys.executable, str(MIG), "--db", str(db), "--no-snapshot"], capture_output=True, text=True, env=env)
    r2 = subprocess.run([sys.executable, str(MIG), "--db", str(db), "--no-snapshot"], capture_output=True, text=True, env=env)
    case("G1", "the migration applies on the copy, a second run writes nothing, not archived from a copy",
         "applied" in r1.stdout and "already applied: 0" in r2.stdout and MIG.exists(), (r1.stdout + r1.stderr).strip()[-160:] + " / " + r2.stdout.strip())
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    naming = lambda g_: [x for x in g_ if "does not name" in x or "no section" in x or "no `guide`" in x]      # the step coverage (#2538 3.2) is tested in temp_2538_behaviours
    gaps = naming(cfgquality.find_analytic_guide_gaps(conn, ROOT))
    case("G2", "the guide as it stands names every method of the path", not gaps, gaps[:3])
    types = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    set_types(conn, {**types, "probe": {"step": "3.2", "command": "ReadProbe", "items": ["collection-gathering"], "rules": []}})
    g3 = naming(cfgquality.find_analytic_guide_gaps(conn, ROOT))
    case("G3", "a read command the section does not name is found, with its Record half",
         len(g3) == 2 and "`ReadProbe`" in g3[0] and "`RecordProbe`" in g3[1], g3)
    set_types(conn, {**types, "guide": {**types["guide"], "section": "99.9"}})
    g4a = cfgquality.find_analytic_guide_gaps(conn, ROOT)
    set_types(conn, {k: v for k, v in types.items() if k != "guide"})
    g4b = cfgquality.find_analytic_guide_gaps(conn, ROOT)
    case("G4", "a missing section and a missing guide are each found", len(g4a) == 1 and "99.9" in g4a[0] and len(g4b) == 1 and "no `guide`" in g4b[0], g4a + g4b)
    set_types(conn, types)
    from iba.app.lib import layerloop
    v = json.loads(cfg.setting("layer.read_types")) if isinstance(cfg.setting("layer.read_types"), str) else cfg.setting("layer.read_types")
    by_item = {i: t["command"] for t in v.values() if isinstance(t, dict) and t.get("command") for i in t.get("items", [])}
    ins = rc.instruction(conn, rc.settings(cfg)["elements"])
    case("G5", "LayerNext's lookup and the 3.1 instruction read read_types with the guide in it",
         by_item.get("subgroup-analysis") == "ReadElements" and "guide" not in by_item.values() and ins["keep"]
         and "isinstance(t, dict) and t.get(\"command\")" in inspect.getsource(layerloop._read_commands), len(ins["keep"]))
    case("G6", "configmaint.validate runs the check", "find_analytic_guide_gaps" in inspect.getsource(configmaint.validate))
    conn.rollback()
    n_ok = sum(1 for r in RESULTS if r[2])
    print(f"\n{n_ok} of {len(RESULTS)} pass ({round(time.monotonic() - t0, 1)} s)")
    return 0 if n_ok == len(RESULTS) else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python iba/app/tools/temp_2538_guide_test_run.py <scratch dir>")
    sys.exit(main(sys.argv[1]))
