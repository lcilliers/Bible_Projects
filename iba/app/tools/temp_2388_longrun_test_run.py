"""temp_2388_longrun_test_run.py -- tests for escalation #2388: the progress control (lib/longrun.py), its handlers (handlers/longrun.py) and the
collection batch driver's failure reading and plan (tools/collection_batch_run.py). Nothing here touches the live collections: the progress files go to a
scratch folder, the one real launch is a dummy job that only writes its progress file, and the plan is read-only.

Usage: python iba/app/tools/temp_2388_longrun_test_run.py <scratch dir>
As a child (the dummy job): python -m iba.app.tools.temp_2388_longrun_test_run --job test-dummy --run
"""
import json
import pathlib
import shutil
import sys
import time
import types

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import longrun as lr  # noqa: E402

if "--run" in sys.argv:  # the dummy job a launch test starts
    with lr.Job("test-dummy", 2) as j:
        for _ in range(2):
            time.sleep(1)
            j.step_done(1.0)
        j.prog["state"] = "finished"
    sys.exit(0)

from iba.app.handlers import longrun as H  # noqa: E402
from iba.app.tools import collection_batch_run as D  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


S = pathlib.Path(sys.argv[1]) / "t2388longrun"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
real_dir = lr.DIR
lr.DIR = S
ctx = lambda **p: types.SimpleNamespace(params=p, run_id="TEST-RUN")  # noqa: E731

# --- lib
case("L1", "summary of a job never started says so", "not been started" in lr.summary("job-a"), lr.summary("job-a"))
with lr.Job("job-a", 3) as j:
    p0 = lr.read("job-a")
    case("L2", "a started job writes a running progress file with its pid", p0["state"] == "running" and p0["pid"] > 0 and p0["left"] == 3, p0["state"])
    j.step_done(10.0)
    j.step_done(20.0, ok_=False, error="boom")
    j.step_done(0, skipped=True)
    p1 = lr.read("job-a")
    case("L3", "done, failed, skipped and left are counted; the mean and last problem show", (p1["done"], p1["failed"], p1["skipped"], p1["left"]) == (1, 1, 1, 0)
         and p1["mean_secs_last_20"] == 10.0 and p1["last_error"] == "boom", p1)
    try:
        lr.Job("job-a", 1).__enter__()
        case("L4", "a second start of a running job is refused", False, "no error")
    except RuntimeError as exc:
        case("L4", "a second start of a running job is refused", "is running" in str(exc), exc)
    case("L5", "alive is true while the file moves", lr.alive(lr.read("job-a")), "")
    j.prog["state"] = "finished"
p2 = lr.read("job-a")
case("L6", "leaving the block records the final state and not running", p2["state"] == "finished" and p2["current"] is None and not lr.alive(p2), p2["state"])
old = dict(p2, state="running", updated_epoch=time.time() - 600)
case("L7", "a live state whose file has not moved for 10 minutes is not alive", not lr.alive(old), "")
lr.paths("job-b")["progress"].write_text(json.dumps(dict(old, job="job-b")), encoding="utf-8")
case("L8", "summary says NOT running and how to resume", "NOT running" in lr.summary("job-b") and "resume" in lr.summary("job-b"), lr.summary("job-b").splitlines()[0])
lr.paths("job-c")["stop"].write_text("stop")
with lr.Job("job-c", 1) as jc:
    case("L9", "a stop flag left from an earlier run is cleared at start", not jc.stop_asked(), "")
    lr.paths("job-c")["stop"].write_text("stop")
    case("L10", "a stop flag written while running is seen", jc.stop_asked(), "")
    jc.prog["state"] = "stopped"

# --- handlers (the job table is patched for the tests)
for k in ("job-a", "job-d", "test-dummy"):
    H.JOBS[k] = "iba.app.tools.temp_2388_longrun_test_run"
r = H.progress(ctx(Job="nope"))
case("H1", "an unknown job is refused", r.condition == "refused", r.message)
r = H.start(ctx(Job="test-dummy", Limit="x"))
case("H2", "a bad -Limit is refused and nothing starts", r.condition == "refused" and "whole number" in r.message, r.message)
r = H.progress(ctx(Job="job-a"))
case("H3", "Progress returns the summary", r.condition == "ok" and "job-a: finished" in r.message, r.message.splitlines()[0])
r = H.stop(ctx(Job="job-a"))
case("H4", "Stop on a job that is not running writes no flag", r.condition == "ok" and "nothing to stop" in r.message and not lr.paths("job-a")["stop"].exists(), r.message)
with lr.Job("job-d", 1) as jd:
    r = H.stop(ctx(Job="job-d"))
    case("H5", "Stop on a running job writes the flag the job sees", "stop asked" in r.message and jd.stop_asked(), r.message)
    r = H.start(ctx(Job="job-d"))
    case("H6", "Start on a running job is refused", r.condition == "refused" and "is running" in r.message, r.message)
    jd.prog["state"] = "stopped"
r = H.plan(ctx(Job="nope"))
case("H7", "Plan of an unknown job is refused", r.condition == "refused", r.message)

# the launch: the dummy job runs in its own process through Windows' process service and writes into the real folder
lr.DIR = real_dir
for f in real_dir.glob("test-dummy*"):
    f.unlink()
r = H.start(ctx(Job="test-dummy"))
case("H8", "Start launches the job detached and returns its process id", r.condition == "ok" and r.counts.get("pid", 0) > 0, r.message)
state, pr = None, None
for _ in range(30):
    time.sleep(1)
    pr = lr.read("test-dummy")
    state = pr and pr["state"]
    if state == "finished":
        break
case("H9", "the detached job ran to the end and wrote done 2 of 2", bool(pr) and state == "finished" and pr["done"] == 2 and pr["total"] == 2, pr and (pr["state"], pr["done"]))
for f in real_dir.glob("test-dummy*"):
    f.unlink(missing_ok=True)
lr.DIR = S

# --- driver
with open(S / "log.txt", "w", encoding="utf-8") as log:
    rc, last = D.ps("Seed", log, Word="zzznotaword")
case("D1", "a refusal that exits 0 is read as a failure", rc != 0, (rc, last))
with open(S / "log.txt", "w", encoding="utf-8") as log:
    rc, last = D.ps("Status", log)
case("D2", "a read-only action that works is read as success", rc == 0, (rc, last))
plan = D.build_plan()
seeds = [p["seed"] for p in plan if p["seed"]]
case("D3", "the plan has sub-groups and unique seeds", len(plan) > 100 and len(seeds) == len(set(seeds)), (len(plan), len(seeds)))
case("D4", "has_collection is true for a word that has one and false for a nonsense word", D.has_collection("supplication") and not D.has_collection("zzznotaword"), "")

lr.DIR = real_dir
fails = [r for r in results if r[2] == "FAIL"]
print("| case | what | result | evidence |\n|---|---|---|---|")
for r in results:
    print("| " + " | ".join(r) + " |")
print("\nALL PASS" if not fails else f"\n{len(fails)} FAIL", len(results))
