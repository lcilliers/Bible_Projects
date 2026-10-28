"""temp_2320_dispatch_test_run.py -- escalation #2320, the dispatcher path, on a COPY of iba.db (never the live DB): Reading steps
through run.run_step (the gates, cfg_step, cfg_on_fail, the run row), the whole subgroup M21_asking (timing and size), and the
retired Gather step. Usage: python iba/app/tools/temp_2320_dispatch_test_run.py <scratch dir>. Prints PASS/FAIL per case."""
import json
import os
import pathlib
import shutil
import sqlite3
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ["IBA_NO_SNAPSHOT"] = "1"          # the dispatcher must not snapshot the live database
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib import cfg as cfgmod  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2320disp"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
SNAPS = sorted((ROOT / "iba/app/db/snapshots").glob("iba-*pre-2320-analysis-phase-1.db"))
SOURCE = SNAPS[-1] if SNAPS else ROOT / "iba/app/db/iba.db"       # the database as it was before the migration
DB = copy_db(S / "iba.db", SOURCE)
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
mig = ROOT / "iba/app/migration/analysis_phase_1_2320_v1_20261027.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
subprocess.run([sys.executable, str(mig), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v2 = ROOT / "iba/app/migration/analysis_phase_1_2320_v2_20261027.py"
v2 = v2 if v2.exists() else ROOT / "iba/app/migration/archive" / v2.name
subprocess.run([sys.executable, str(v2), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v3 = ROOT / "iba/app/migration/analysis_phase_1_2323_v1_20261027.py"
v3 = v3 if v3.exists() else ROOT / "iba/app/migration/archive" / v3.name
subprocess.run([sys.executable, str(v3), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v4 = ROOT / "iba/app/migration/analysis_phase_1_2323_v2_20261027.py"
v4 = v4 if v4.exists() else ROOT / "iba/app/migration/archive" / v4.name
subprocess.run([sys.executable, str(v4), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v5 = ROOT / "iba/app/migration/analysis_phase_1_2323_v3_20261027.py"
v5 = v5 if v5.exists() else ROOT / "iba/app/migration/archive" / v5.name
subprocess.run([sys.executable, str(v5), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v6 = ROOT / "iba/app/migration/analysis_phase_1_2323_v4_20261027.py"
v6 = v6 if v6.exists() else ROOT / "iba/app/migration/archive" / v6.name
subprocess.run([sys.executable, str(v6), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='reading.output_dir'", (json.dumps(str(S / "reading")),))
c.commit()
c.close()
cfgmod.Cfg.__init__.__defaults__ = (DB,)      # every Cfg() in run_step now opens the copy
from iba.app import run as runmod  # noqa: E402

res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:700]}"), flush=True)


def step(name, **params):
    params.setdefault("By", "Claude")
    return runmod.run_step("reading", f"reading.{name}", {k: v for k, v in params.items() if v is not None},
                           f"RUN-TEST-{name}-{time.time_ns()}")


t0 = time.time()
r = step("open", Label="d-full", Escalation="2320", Objective="the whole asking subgroup (dispatch test)", Subgroup="M21_asking")
t_open = time.time() - t0
d = json.loads((S / "reading" / "d-full" / "d-full.json").read_text(encoding="utf-8"))
case("D1", "Open through the dispatcher, on the whole subgroup M21_asking: ok, path ok", r["condition"] == "ok" and r["path"] == "ok", r)
print(f"   Open on the whole subgroup: {len(d['verses'])} verses in {t_open:.1f}s; the index file is "
      f"{(S / 'reading' / 'd-full' / 'd-full.json').stat().st_size / 1024:.0f} KB", flush=True)
case("D2", "the index file holds only verses, routes and progress (no surfaces, observations or open items)",
     all(set(v) <= {"verse", "osis", "verse_id", "routes", "status"} for v in d["verses"]))
t0 = time.time()
r = step("observe", Label="d-full")
t_obs = time.time() - t0
d = json.loads((S / "reading" / "d-full" / "d-full.json").read_text(encoding="utf-8"))
hand = [v for v in d["verses"] if v["status"] == "in_hand"]
size = (S / "reading" / "d-full" / "d-full.json").stat().st_size
case("D3", "Observe through the dispatcher puts the configured number of verses in hand (reading.verse_loop)",
     r["condition"] == "ok" and len(hand) == 5, r)
print(f"   Observe, 5 verses: {t_obs:.1f}s; the file is now {size / 1024:.0f} KB; "
      f"{sum(len(v['sheet']['existing']) for v in hand)} existing observations and "
      f"{sum(len(v['sheet']['surfaces']) for v in hand)} surfaces in the sheets", flush=True)
r = step("record", Label="d-full")
case("D4", "Record on unfilled sheets is a routed refusal: condition refused, path report-continue (cfg_on_fail), no escalation",
     r["condition"] == "refused" and r["path"] == "report-continue", r)
try:
    step("gather", Label="d-full")
    case("D5", "the retired Gather step is refused by the dispatcher gate", False, "it ran")
except PermissionError as exc:
    case("D5", "the retired Gather step is refused by the dispatcher gate (cfg_step.inactive)", "inactive" in str(exc), str(exc))
r = step("check", Label="d-full")
case("D6", "Check at open with verses waiting is a routed refusal", r["condition"] == "refused" and r["path"] == "report-continue", r)
run_rows = sqlite3.connect(DB).execute("SELECT count(*) FROM run WHERE work_package='reading' AND state='done'").fetchone()[0]
case("D7", "each call closed its run (reading is not chained)", run_rows >= 3, run_rows)
print(f"\n{sum(res)} of {len(res)} cases pass")
sys.exit(0 if all(res) else 1)
