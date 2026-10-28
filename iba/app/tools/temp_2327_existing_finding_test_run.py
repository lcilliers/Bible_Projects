"""temp_2327_existing_finding_test_run.py -- escalation #2327 test plan, on a COPY of the live iba.db (never the live DB or the live reading
file): a finding that names an existing observation (RW-03 / RO11: one finding, many nodes) gains the nodes of a second verse, including a
party and a link observation, whose route and kind come from the live observation. Real case: Judg 1:14, which repeats Jos 15:18 word for
word, in reading m21-asking (four findings naming observations 20725 to 20728). Synthetic bad inputs: a different route, a different kind
and a new description on an existing finding are refused. Usage: python iba/app/tools/temp_2327_existing_finding_test_run.py <scratch dir>.
Prints PASS/FAIL per case."""
import copy
import json
import pathlib
import shutil
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402
from iba.app.handlers import reading as hr  # noqa: E402

LABEL = "m21-asking"
S = pathlib.Path(sys.argv[1]) / "t2327run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
SHEET = ROOT / "backups/m21-asking-judg-1-14-failed-record-20261028.json"       # the reading's JSON as the failed Record left it
if not SHEET.exists():
    shutil.copy(ROOT / "outputs/reading" / LABEL / f"{LABEL}.json", SHEET)
LIVE = ROOT / "backups/iba-pre-2327-existing-finding-20261028.db"                  # the live database before the fix (backup API)
if not LIVE.exists():
    copy_db(LIVE, ROOT / "iba/app/db/iba.db")
DB = copy_db(S / "iba.db", LIVE)
for _m in ("analysis_phase_1_2320_v4_20261028.py",):               # the rules the build reads from config (settings the older copy lacks)
    _p = ROOT / "iba/app/migration" / _m
    _p = _p if _p.exists() else ROOT / "iba/app/migration/archive" / _m
    subprocess.run([sys.executable, str(_p), "--db", str(DB)], capture_output=True, text=True, check=True,
                   env={**__import__("os").environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"})
JSON = S / "reading" / LABEL / f"{LABEL}.json"
JSON.parent.mkdir(parents=True)
shutil.copy(SHEET, JSON)
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='reading.output_dir'", (json.dumps(str(S / "reading")),))
c.execute("UPDATE reading SET gap_file=?, observe_file=? WHERE label=?", (str(JSON), str(JSON), LABEL))      # the copy never writes the live file
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:900]}"), flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(step, **params):
    params.setdefault("By", "Claude")
    return getattr(hr, step)(Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None,
                                 params={k: v for k, v in params.items() if v is not None}, step_id=f"reading.{step}"))


def load():
    return json.loads(JSON.read_text(encoding="utf-8"))


def put(d):
    JSON.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


d0 = load()
v0 = next(v for v in d0["verses"] if v["status"] == "in_hand")
fnd = v0["sheet"]["findings"]
ids = [f["existing"] for f in fnd]
case("E0", "the failed sheet names four existing observations (two statements, a link and a party with route B)",
     len(fnd) == 4 and {f["kind"] for f in fnd} == {"statement", "link", "party"} and all(isinstance(i, int) for i in ids),
     [(f["key"], f["kind"], f.get("existing")) for f in fnd])
before_obs = {r["id"]: tuple(r) for r in q("SELECT id, tag, route, obs_text, parts FROM ib_observation WHERE id IN (%s)" % ",".join(map(str, ids)))}
n_obs = q("SELECT count(*) FROM ib_observation")[0][0]
n_nodes = {i: q("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", i)[0][0] for i in ids}
verse_ref = v0["osis"]
# ── B: synthetic bad inputs, each refused with nothing written ─────────────────────────────────────
for cid, desc, mut in [
        ("B1", "an existing party finding given a different route than the live observation's is refused",
         lambda f: f.update(route="A") if f["kind"] == "party" else None),
        ("B2", "an existing finding given a different kind than the live observation's is refused",
         lambda f: f.update(kind="face") if f["key"] == "s1" else None),
        ("B3", "an existing finding given a new description is refused (a changed description is a new finding)",
         lambda f: f.update(text="a changed description of the finding") if f["key"] == "s1" else None)]:
    d = copy.deepcopy(d0)
    vv = next(v for v in d["verses"] if v["status"] == "in_hand")
    for f in vv["sheet"]["findings"]:
        mut(f)
    put(d)
    r = None
    try:
        r = run("record", Label=LABEL)
        msg, cond = r.message, r.condition
    except Exception as exc:                                  # a refusal is raised
        msg, cond = str(exc), "refused"
    case(cid, desc, cond == "refused" and "takes nodes only" in msg
         and q("SELECT count(*) FROM ib_observation")[0][0] == n_obs
         and all(q("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", i)[0][0] == n_nodes[i] for i in ids), msg[:300])
# ── R: the real sheet ─────────────────────────────────────────────────────────────────────────────
put(d0)
r = run("record", Label=LABEL)
case("R1", "the real sheet is recorded: the existing findings gain the nodes of the second verse (it was refused before #2327)",
     r.condition == "ok", r.message[:500])
after_obs = {r_["id"]: tuple(r_) for r_ in q("SELECT id, tag, route, obs_text, parts FROM ib_observation WHERE id IN (%s)" % ",".join(map(str, ids)))}
case("R2", "no observation was created and the four are unchanged (text, kind, route, parts)",
     q("SELECT count(*) FROM ib_observation")[0][0] == n_obs and before_obs == after_obs)
gained = {i: q("SELECT count(*) FROM ib_node WHERE observation_id=? AND verse_reference=? AND deleted=0", i, verse_ref.replace(" ", ".").replace(":", "."))[0][0] for i in ids}
case("R3", "each of the four now holds more nodes than before", all(q("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", i)[0][0] > n_nodes[i] for i in ids),
     (gained, n_nodes))
case("R4", "no two nodes of an observation share a seq",
     all(q("SELECT count(*) FROM (SELECT seq FROM ib_node WHERE observation_id=? GROUP BY seq HAVING count(*)>1)", i)[0][0] == 0 for i in ids))
d1 = load()
case("R5", "the verse is done and its sheet is gone", next(v for v in d1["verses"] if v["osis"] == v0["osis"])["status"] == "done")
print(f"\n{sum(res)} of {len(res)} cases pass")
