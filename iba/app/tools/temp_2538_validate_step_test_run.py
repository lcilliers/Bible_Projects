"""temp_2538_validate_step_test_run.py -- escalation #2538 test plan (B:29, B:46) for the registered validation: the migration, ValidatePull, ValidateRecord,
ValidateCheck (handlers of collection-build) and lib/collectionvalidate.py, on a COPY of the live iba.db (never the live DB). The expectations are stated
before the run. Usage: python iba/app/tools/temp_2538_validate_step_test_run.py <scratch dir> <sheet.json> <applied copy of the pilot (reference state)>"""
import json
import os
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
from iba.app.lib import collectionvalidate as cv  # noqa: E402
from iba.app.handlers import collectionbuild as hc  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
S = pathlib.Path(sys.argv[1]) / "t2538step"
SHEET = pathlib.Path(sys.argv[2])
REF = pathlib.Path(sys.argv[3])
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", ROOT / "iba/app/db/iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
MIG = ROOT / "iba/app/migration/validation_2538_v1_20261122.py"
if not MIG.exists():
    MIG = ROOT / "iba/app/migration/archive/validation_2538_v1_20261122.py"
res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:700]}"), flush=True)


def mig(*a):
    r = subprocess.run([sys.executable, str(MIG), "--db", str(DB), *a], capture_output=True, text=True, env=env)
    return (r.stdout + r.stderr).strip()


# V1 the migration: 30 cfg writes planned; applied; a second run changes nothing
d = mig("--dry-run")
case("V1a", "the dry run plans 30 cfg writes and the column", d.startswith("DRY RUN: 30 cfg write(s); ib_observation.nature to add: True"), d[:200])
a = mig("--no-snapshot")
case("V1b", "the migration applies 30 cfg writes and adds the column", a.startswith("applied") and "30 cfg write(s)" in a and "added: True" in a, a)
b = mig("--no-snapshot")
case("V1c", "a second run changes nothing", b.startswith("already applied"), b)
raw = sqlite3.connect(DB)
case("V1d", "the column, three steps, the setting, the enum and the new rule exist", all([
    any(r[1] == "nature" for r in raw.execute("PRAGMA table_info(ib_observation)")),
    raw.execute("SELECT count(*) FROM cfg_step WHERE step LIKE 'collection.validate_%'").fetchone()[0] == 3,
    raw.execute("SELECT count(*) FROM cfg_setting WHERE key LIKE 'validate.%'").fetchone()[0] == 3,
    raw.execute("SELECT count(*) FROM cfg_enum WHERE name='ib_observation.nature'").fetchone()[0] == 2,
    raw.execute("SELECT count(*) FROM cfg_behaviour_rule WHERE rule_key='collection-validation-follows-stage-4'").fetchone()[0] == 1,
    raw.execute("SELECT count(*) FROM cfg_method_rule WHERE rule_key LIKE 'VA-0%' OR rule_key LIKE 'IB-07%'").fetchone()[0] == 7]))
case("V1e", "B:132 and B:133 gained their sentence once", all("collection-validation-follows-stage-4" in raw.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=?", (i,)).fetchone()[0] for i in (132, 133)))
case("V1f", "every cfg write is in cfg_change_detail under the run", raw.execute("SELECT count(*) FROM cfg_change_detail WHERE run_id='DEVMODE-2538-VALIDATION-20261122'").fetchone()[0] >= 30)
for k, v in (("surfaces.exports_root", str(S / "exports")), ("layer.working_dir", str(S / "work")), ("governance.oneoff_report_archive_dir", str(S / "archive"))):
    raw.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(v), k))      # the test writes its files in the scratch dir, never the live folders
raw.commit()
raw.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
q = lambda sql, *a: conn.execute(sql, a).fetchall()


def run(fn, **params):
    return fn(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-VALIDATE", word="", word_id=None, params=params, step_id="collection.validate"))


# V2 ValidatePull on thought: 1,180 in scope, all unmarked, 1,212 word nodes missing a column (the pilot's counts), no table written
chg0 = q("SELECT count(*) FROM ib_observation_change")[0][0]
o = run(hc.validate_pull, Collection="thought")
case("V2a", "ValidatePull reports 1,180 in scope and writes no table", "1180 observations in scope" in o.message and q("SELECT count(*) FROM ib_observation_change")[0][0] == chg0, o.message[:300])
pl = cv.pull(conn, cfg, cv.collection_id(conn, "thought"))
nm, nn_ = len(pl["findings"].get("word_missing", [])), len(pl["findings"].get("word_missing_noted", []))
case("V2b", "all 1,180 are unmarked and 1,212 word nodes lack a required column (unexplained plus explained in disposition_note)", "1180 not marked" in o.message and nm + nn_ == 1212, (o.message[:300], nm, nn_))
case("V2c", "the report and the working file exist; the working file holds 1,180 observations", (S / "work" / "validate-thought.json").exists() and len(json.loads((S / "work" / "validate-thought.json").read_text(encoding="utf-8"))["observations"]) == 1180)

# V3 ValidateRecord: -Check previews (nothing kept); a bad sheet refuses whole; the real record equals the reference state
state0 = (q("SELECT count(*) FROM ib_observation_change")[0][0], q("SELECT count(*) FROM ib_observation WHERE deleted=1")[0][0], q("SELECT count(*) FROM ib_observation")[0][0])
o = run(hc.validate_record, File=str(SHEET), Check="true")
state1 = (q("SELECT count(*) FROM ib_observation_change")[0][0], q("SELECT count(*) FROM ib_observation WHERE deleted=1")[0][0], q("SELECT count(*) FROM ib_observation")[0][0])
case("V3a", "-Check runs the 221 actions and keeps nothing", o.message.startswith("PREVIEW") and "221 actions" in o.message and state0 == state1, (o.message[:300], state0, state1))
data = json.loads(SHEET.read_text(encoding="utf-8"))
bad = dict(data, actions=data["actions"][:5] + [{"action": "set_nature", "oid": 22296, "nature": "claim", "reason": "an invalid marker at the end of the sheet"}])
bp = S / "bad.json"
bp.write_text(json.dumps(bad), encoding="utf-8")
o = run(hc.validate_record, File=str(bp))
state2 = (q("SELECT count(*) FROM ib_observation_change")[0][0], q("SELECT count(*) FROM ib_observation WHERE deleted=1")[0][0], q("SELECT count(*) FROM ib_observation")[0][0])
case("V3b", "a sheet with one refused action is refused whole and nothing of its first five actions is kept", o.condition == "refused" and state2 == state0, (o.condition, o.message[:300], state2))
for label, acts, frag in (("unknown action", [{"action": "erase_everything"}], "not an action"),
                          ("unknown parameter", [{"action": "set_nature", "oid": 1, "nature": "evidence", "reason": "a reason of enough words", "wat": 1}], "unknown parameter"),
                          ("missing parameter", [{"action": "set_nature", "oid": 1}], "missing parameter"),
                          ("unresolved reference", [{"action": "add_trace", "oid": 12431, "target": "@new9", "reason": "a trace to an observation that was never created"}], "no earlier create")):
    p = S / "x.json"
    p.write_text(json.dumps({"collection": "thought", "actions": acts}), encoding="utf-8")
    o = run(hc.validate_record, File=str(p))
    case("V3c", f"{label} is refused with its reason", o.condition == "refused" and frag in o.message, o.message[:300])
o = run(hc.validate_record, File=str(SHEET))
case("V3d", "the real record writes 221 actions", (not o.message.startswith("PREVIEW")) and "221 actions" in o.message, o.message[:300])

# V4 the state after the record equals the pilot's reference state on the 55 and the 4 created observations
ref = sqlite3.connect(f"file:{REF.as_posix()}?mode=ro", uri=True)
ids = [r[0] for r in ref.execute("SELECT DISTINCT observation_id FROM ib_observation_change WHERE run_id='PILOT-2538-1CHR-28-9-APPLY' AND column_name IN ('nature','created') AND node_id IS NULL")]


def sig(c):
    out = {}
    for i in ids:
        o_ = tuple(c.execute("SELECT deleted, nature, obs_text FROM ib_observation WHERE id=?", (i,)).fetchone())
        tr = sorted(r[0] for r in c.execute("SELECT traced_observation_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NOT NULL", (i,)))
        nn = c.execute("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", (i,)).fetchone()[0]
        df = sorted(r[0] for r in c.execute("SELECT new_value FROM ib_observation_change WHERE observation_id=? AND column_name='deferred_to'", (i,)))
        out[i] = (o_, tr, nn, df)
    return out


sa, sb = sig(ref), sig(conn)
diff = [i for i in ids if sa[i] != sb[i]]
case("V4a", f"the {len(ids)} observations match the reference state (deleted, marker, text, traces, node count, deferrals)", not diff, diff[:6])
case("V4b", "50 of the compared observations are live (46 of the 55 plus the 4 created: 22669 to 22672)", sum(1 for i in ids if sb[i][0][0] == 0) == 50 and {22669, 22670, 22671, 22672} <= set(ids), sum(1 for i in ids if sb[i][0][0] == 0))
case("V4c", "the 26 deleted observations carry the note", q("SELECT count(*) FROM ib_observation WHERE deleted=1 AND revisit_note LIKE 'Deleted before delete records were kept%'")[0][0] == 26)

# V5 ValidateCheck on thought after the record: the evidence layer does not pass (the rest of the scope is unmarked); the inner-being layer is not judged
o = run(hc.validate_check, Collection="thought")
case("V5a", "ValidateCheck: evidence layer does not pass, inner-being not judged, report written", "evidence layer does not pass" in o.message and "not judged" in o.message and any((S / "exports").glob("validate-check-thought*.md")), o.message[:300])

# V6 the two-layer check on a small synthetic database with known defects
m = sqlite3.connect(":memory:")
m.row_factory = sqlite3.Row
m.executescript("""
create table collection(id integer primary key, name text, deleted int default 0);
create table collection_layer_item(collection_id int, step text, item text, subject text, deleted int default 0);
create table ib_observation(id integer primary key, stage text, tag text, obs_text text, strong text, nature text, deleted int default 0);
create table ib_node(id integer primary key, observation_id int, verse_reference text, verse_lexical_id int, surface text, strong text, morph_code text, role text,
  collection_id int, subgroup_id int, traced_observation_id int, disposition_note text, deleted int default 0);
create table ib_observation_change(id integer primary key, observation_id int, node_id int, column_name text, old_value text, new_value text, reason text, reading_id int, run_id text, created_at text, created_by text);
insert into collection values (1,'t',0),(2,'u',0);
insert into collection_layer_item values (1,'S1','word-lexical','think|G1',0);
insert into ib_observation values (1,'lexical','term','ev one','G1','evidence',0),(2,'layer-3','statement','ib traced','G1','inner_being',0),(3,'layer-3','statement','ib none','G1','inner_being',0);
insert into ib_node values (1,1,'V.1',10,'think','G1','m','lexical',1,5,null,null,0),(2,2,'V.1',11,'think','G1','m','characteristic',1,5,null,null,0),(3,2,null,null,null,null,null,null,null,null,1,null,0),
 (4,3,'V.1',12,'think','G1','m','characteristic',1,5,null,null,0);
""")


class FakeCfg:
    def required_setting(self, k):
        return {"word_columns": ["verse_reference", "verse_lexical_id", "surface", "strong", "morph_code", "role", "collection_id"], "actions": []}


g = cv.check(m, FakeCfg(), 1)
case("V6a", "all marked, no gap on the evidence layer: it passes", g["evidence_passes"], g["open_evidence"])
case("V6b", "the inner-being observation with no trace is open (3), the traced one is not", g["ib_open"] == [3] and not g["inner_being_passes"], (g["ib_open"], g["lines"]))
m.execute("INSERT INTO ib_observation_change(observation_id, column_name, new_value, reason) VALUES (3,'deferred_to','2','the collection u will trace it to its evidence')")
g = cv.check(m, FakeCfg(), 1)
case("V6c", "a deferral to a named collection makes it deferred, and the layer passes", g["ib_open"] == [] and g["ib_deferred"] == [3] and g["inner_being_passes"], (g["ib_open"], g["ib_deferred"]))
g2 = cv.check(m, FakeCfg(), 2)
case("V6d", "collection u lists the deferral addressed to it", len(g2["incoming"]) == 1 and g2["incoming"][0]["observation"] == 3, g2["incoming"])
m.execute("INSERT INTO ib_observation VALUES (4,'layer-2','pairing','unmarked one','G1',NULL,0)")
m.execute("INSERT INTO ib_node VALUES (5,4,'V.1',13,'think','G1','m','characteristic',1,5,null,null,0)")
g = cv.check(m, FakeCfg(), 1)
case("V6e", "an unmarked observation fails the evidence layer and the inner-being layer is not judged", not g["evidence_passes"] and not g["inner_being_passes"] and "not judged" in "\n".join(g["lines"]), g["lines"])
m.execute("UPDATE ib_node SET role=NULL WHERE id=5")
m.execute("UPDATE ib_observation SET nature='evidence' WHERE id=4")
g = cv.check(m, FakeCfg(), 1)
case("V6f", "a word node missing a column with no reason fails; with its reason in disposition_note it is accepted", not g["evidence_passes"], g["open_evidence"])
m.execute("UPDATE ib_node SET disposition_note='the data cannot give a role here' WHERE id=5")
g = cv.check(m, FakeCfg(), 1)
case("V6g", "...and passes once the reason is recorded", g["evidence_passes"], g["open_evidence"])

print(f"\n{sum(res)}/{len(res)} PASS")
sys.exit(0 if all(res) else 1)
