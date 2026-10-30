"""temp_2331_reopen_test_run.py -- escalation #2331 test plan, on a COPY of the live iba.db and a COPY of the m21-asking scope JSON
(never the live ones): the Reopen step. Usage: python iba/app/tools/temp_2331_reopen_test_run.py <scratch dir>. Prints PASS/FAIL."""
import json
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import reading as rd  # noqa: E402
from iba.app.lib import narrativeregister as nr  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2331run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", ROOT / "iba/app/db/iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
MIG = ROOT / "iba/app/migration/reading_reopen_2331_v1_20261030.py"
MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(MIG), "--db", str(DB), *a],
                                                                 capture_output=True, text=True, env=env))
      for a in (["--dry-run"], [], [])]
cfg = Cfg(DB)
conn = cfg.conn
res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:900]}"), flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


case("T1", "migration: dry run, apply, second run refused",
     mo[0].startswith("DRY RUN") and "cfg_step insert" in mo[0] and "applied" in mo[1] and mo[2].startswith("already applied"), mo)
case("T2", "config: step reading.reopen and rule RS-09 present, change logged",
     q("SELECT count(*) FROM cfg_step WHERE step='reading.reopen' AND inactive=0")[0][0] == 1
     and q("SELECT count(*) FROM cfg_method_rule WHERE rule_key LIKE 'RS-09%'")[0][0] == 1
     and q("SELECT count(*) FROM cfg_change_detail WHERE run_id='DEVMODE-2331-READING-REOPEN-20261030'")[0][0] >= 3)

# the scope JSON, copied: the copied reading row points at the copy; the root is the scratch dir
live = ROOT / q("SELECT gap_file FROM reading WHERE label='m21-asking'")[0][0]
copy = S / "scope.json"
shutil.copy(live, copy)
conn.execute("UPDATE reading SET gap_file=? WHERE label='m21-asking'", ("scope.json",))
conn.commit()
before = json.loads(copy.read_text(encoding="utf-8"))
done = [v for v in before["verses"] if v["status"] == "done"]
w = nr.Writer(conn, "reading.reopen", "Claude")
REASON = "a reason that is long enough"


def run(**p):
    try:
        return "OK", rd.reopen(cfg, w, {"Label": "m21-asking", **p}, "TEST-2331", S)
    except nr.Refused as e:
        return "REFUSED", str(e)


def obs_count():
    return conn.execute("SELECT count(*) FROM ib_observation").fetchone()[0]


case("T3", f"precondition: the copy holds done verses ({len(done)})", len(done) >= 3, len(done))
obs0 = obs_count()
k, m = run(Verse=done[0]["verse"])
case("T4", "bad input: no reason is refused", k == "REFUSED" and "-Note" in m, m)
k, m = run(Note=REASON)
case("T5", "bad input: no verse is refused", k == "REFUSED" and "-Verse" in m, m)
k, m = run(Note="short", Verse=done[0]["verse"])
case("T6", "bad input: a too-short reason is refused", k == "REFUSED", m)
k, m = run(Note=REASON, Verse="Gen 1:1")
case("T7", "bad input: a verse outside the scope is refused", k == "REFUSED", m)
case("T8", "refusals changed nothing in the JSON", json.loads(copy.read_text(encoding="utf-8")) == before)
k, m = run(Note=REASON, Verse=done[0]["verse"])
after = json.loads(copy.read_text(encoding="utf-8"))
v0 = next(v for v in after["verses"] if v["verse_id"] == done[0]["verse_id"])
case("T9", "a done verse goes to waiting, its reason and previous result kept, `result` gone",
     k == "OK" and v0["status"] == "waiting" and "result" not in v0 and v0["reopened"][0]["reason"] == REASON
     and v0["reopened"][0]["previous_result"] == done[0]["result"] and v0["reopened"][0]["by"] == "Claude", (k, m, v0))
case("T10", "counts.done falls by one; the other verses are untouched",
     after["counts"]["done"] == before["counts"]["done"] - 1
     and all(a == b for a, b in zip(after["verses"], before["verses"]) if a["verse_id"] != v0["verse_id"]))
case("T11", "no observation row added or removed", obs_count() == obs0, (obs_count(), obs0))
k, m = run(Note=REASON, Verse=done[0]["verse"])
case("T12", "bad input: a verse already waiting is not re-opened", k == "REFUSED" and "not done" in m, m)
k, m = run(Note=REASON, Verse="; ".join(v["verse"] for v in done[1:3]))
case("T13", "two named verses re-open together", k == "OK" and "2 verse(s)" in m, m)
k, m = run(Note=REASON, Verse=done[1]["verse"])
case("T14", "bad input: a re-opened verse named again (now waiting) is refused", k == "REFUSED", m)
o = rd.observe(cfg, nr.Writer(conn, "reading.observe", "Claude"), {"Label": "m21-asking", "Verse": done[0]["verse"]}, "TEST-2331", S)
after2 = json.loads(copy.read_text(encoding="utf-8"))
v0 = next(v for v in after2["verses"] if v["verse_id"] == done[0]["verse_id"])
case("T15", "Observe puts the re-opened verse in hand with a sheet that holds its existing observations",
     v0["status"] == "in_hand" and v0["sheet"]["existing"] and v0["reopened"], o)
conn.execute("UPDATE reading SET state='observed' WHERE label='m21-asking'")
k, m = run(Note=REASON, Verse=done[3]["verse"])
case("T16", "bad input: a reading that is not open is refused", k == "REFUSED", m)
print(f"{sum(res)} of {len(res)} passed")
sys.exit(0 if all(res) else 1)
