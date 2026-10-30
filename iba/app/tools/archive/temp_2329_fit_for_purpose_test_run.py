"""temp_2329_fit_for_purpose_test_run.py -- escalation #2329 test plan, on a COPY of the live iba.db (never the live DB): the before and
after parts, the typed party and the meaning data on the Observe sheet (design
outputs/escalation/2329-phase-1-fit-for-purpose-design-v1-20261030.md). Synthetic bad input and real data (Gen 37:15, Gen 43:27, an NT
verse with G0154). Usage: python iba/app/tools/temp_2329_fit_for_purpose_test_run.py <scratch dir>. Prints PASS/FAIL per case."""
import json
import pathlib
import shutil
import subprocess
import sys
import os

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import reading as rd  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2329run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
_pre = sorted((ROOT / "iba/app/db/snapshots/kept").glob("iba-*-before-migration-analysis-phase-1-2329-v*.db"))   # the database before #2329
DB = copy_db(S / "iba.db", _pre[0] if _pre else ROOT / "iba/app/db/iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
MIG = ROOT / "iba/app/migration/analysis_phase_1_2329_v1_20261030.py"
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


case("T1", "migration: dry run lists the writes, then applies, then refuses a second run",
     mo[0].startswith("DRY RUN") and "cfg_setting update" in mo[0] and "cfg_setting insert" in mo[0]
     and "applied" in mo[1] and mo[2].startswith("already applied"), mo)
spec = json.loads(q("SELECT value FROM cfg_setting WHERE key='reading.observation_parts'")[0][0])
case("T2", "config: before and after are parts (after content and enactment), party_form is held",
     spec["parts"].index("before") == spec["parts"].index("content") + 1
     and spec["parts"].index("after") == spec["parts"].index("enactment") + 1
     and spec["party_form"]["kind_enum"] == "party_kind", spec)
case("T3", "config: the change is in cfg_change_detail under the run id",
     q("SELECT count(*) FROM cfg_change_detail WHERE run_id='DEVMODE-2329-PHASE1-FIT-FOR-PURPOSE-20261030'")[0][0] >= 3)

OK = {"sense": "test sense in this verse", "evidence": "test evidence for the sense", "polarity": "pursuit",
      "content": {"none": "test: no object stated in the verse"}, "before": "test: the prompt before the act is stated",
      "enactment": {"none": "test: no outward act stated"}, "after": "Gen 37:16 -- the answer follows in the next verse",
      "party": {"text": "a man asks Joseph", "acts": "human", "acted_on": "human"},
      "circumstance": "test circumstance in this verse", "chain": {"none": "test: a single operation in the verse"},
      "primary_operation": {"none": "test: not the primary one"}, "flags": []}


def errs(parts):
    e = []
    orec.complete_parts(cfg, parts, "t", e)
    return e


case("T4", "a complete set with a typed party passes", errs(OK) == [], errs(OK))
no_before = {k: v for k, v in OK.items() if k != "before"}
e = errs(no_before)
case("T5", "bad input: no `before` is refused and named", any("'before'" in x for x in e), e)
no_after = {k: v for k, v in OK.items() if k != "after"}
case("T6", "bad input: no `after` is refused and named", any("'after'" in x for x in errs(no_after)), errs(no_after))
case("T7", "`before` and `after` stated absent with a reason pass",
     errs({**OK, "before": {"none": "the verse does not say what led to it"}, "after": {"none": "the verse does not say what follows"}}) == [])
case("T8", "bad input: `before` absent with a too-short reason is refused",
     any("'before'" in x for x in errs({**OK, "before": {"none": "no"}})))
case("T9", "bad input: the party as a bare sentence (the old form) is refused",
     any("party" in x for x in errs({**OK, "party": "a man asks Joseph"})), errs({**OK, "party": "a man asks Joseph"}))
case("T10", "bad input: a party kind outside party_kind is refused",
     any("acted_on" in x for x in errs({**OK, "party": {**OK["party"], "acted_on": "angelic"}})))
case("T11", "bad input: a party missing a key is refused",
     any("party" in x for x in errs({**OK, "party": {"text": "a man asks Joseph", "acts": "human"}})))
case("T12", "a party stated absent with a reason passes",
     errs({**OK, "party": {"none": "the verse names one party only"}}) == [])
e = []
orec.check_parts(cfg, {**OK, "party": {"text": "a man asks Joseph", "acts": "robot", "acted_on": "human"}}, "t", e)
case("T13", "check_parts (a new finding) refuses a bad party kind", any("acts" in x for x in e), e)
e = []
orec.check_parts(cfg, {"sense": "x"}, "t", e)
case("T14", "check_parts still accepts a partial set (completeness is checked at Record)", e == [], e)


# the Observe sheet: real data
def sheet_for(osis):
    v = q("SELECT id, osisId FROM verse WHERE osisId=?", osis)[0]
    return rd._sheets(cfg, conn, [{"verse_id": v[0], "osis": osis, "verse": osis}])[v[0]]


nt = q("SELECT v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0 AND vl.strong LIKE 'G0154%' "
       "ORDER BY v.id LIMIT 1")[0][0]
sh_ot, sh_nt = sheet_for("Gen.37.15"), sheet_for(nt)
ask = [g for g in sh_ot["surfaces"] if g["strong"].startswith("H7592")]
case("T15", "sheet (OT, Gen 37:15): every surface carries meaning; no lexicon for Hebrew",
     all("meaning" in g for g in sh_ot["surfaces"]) and all("lexicon" not in g["meaning"] for g in sh_ot["surfaces"]), sh_ot["surfaces"][0])
if ask:
    g = ask[0]["meaning"]
    n_tree = q("SELECT count(*) FROM strong_meaning_tree WHERE deleted=0 AND strong_variant=?", ask[0]["strong"])[0][0]
    n_rel = q("SELECT count(*) FROM strong_related WHERE deleted=0 AND strong=?", ask[0]["strong"])[0][0]
    case("T16", "sheet: the asking word's meaning equals the tables (tree rows, related words, sense head, STEP gloss)",
         len(g["tree"]) == n_tree > 0 and len(g["related"]) == n_rel and g["sense"] == "to ask" and g["step_gloss"] == "to ask", g)
else:
    case("T16", "Gen 37:15 has an H7592 surface", False, [x["word"] for x in sh_ot["surfaces"]])
gn = [g for g in sh_nt["surfaces"] if g["strong"].startswith("G0154")]
case("T17", f"sheet (NT, {nt}): a Greek surface carries the lexicon columns",
     gn and set(gn[0]["meaning"].get("lexicon", {})) == {"lsj", "mounce"}, gn[0]["meaning"] if gn else sh_nt["surfaces"])
case("T18", "a code with nothing held reads as empty, not as missing",
     all(isinstance(g["meaning"].get("tree"), list) and "related" in g["meaning"] for g in sh_ot["surfaces"] + sh_nt["surfaces"]))
case("T19", "the sheet text names before, after, the party shape and the meaning",
     all(w in sh_ot["how"] for w in ("`before`", "`after`", "acted_on", "party_kind", "`meaning`")))

# real observations: what the sheet says of an existing party observation, and its modify
row = q("SELECT o.id, o.parts FROM ib_observation o WHERE o.deleted=0 AND o.tag='party' AND o.parts IS NOT NULL AND EXISTS "
        "(SELECT 1 FROM ib_node n WHERE n.observation_id=o.id AND n.deleted=0 AND n.verse_reference='Gen.43.27') LIMIT 1")
if not row:
    case("T20", "a recorded party observation on Gen 43:27 exists", False)
else:
    oid, old = row[0]["id"], json.loads(row[0]["parts"])
    sh = sheet_for("Gen.43.27")
    ex = [e_ for e_ in sh["existing"] if e_["observation"] == oid][0]
    case("T20", f"real data: the recorded party observation {oid} is flagged parts_incomplete (before, after, party form)",
         any(f["code"] == "parts_incomplete" and "'before'" in f["text"] for f in ex["flags"]), ex["flags"])
    new = {**old, "before": "the brothers have come into Joseph's house with the present (43:26)",
           "after": "Gen 43:28 -- the brothers answer that their father is well",
           "party": {"text": old["party"] if isinstance(old.get("party"), str) else "Joseph asks the brothers",
                     "acts": "human", "acted_on": "human"}}
    n0 = q("SELECT count(*) FROM ib_observation WHERE deleted=0")[0][0]
    problems = orec.modify_observation(cfg, conn, oid, {"parts": new}, "trial under the new parts (test)", None, "RUN-TEST-2329", "Claude")
    n1 = q("SELECT count(*) FROM ib_observation WHERE deleted=0")[0][0]
    live = json.loads(q("SELECT parts FROM ib_observation WHERE id=?", oid)[0][0])
    chg = q("SELECT count(*) FROM ib_observation_change WHERE observation_id=? AND run_id='RUN-TEST-2329'", oid)[0][0]
    case("T21", "real data: modifying the parts writes them, logs the change with its reason, adds and removes no observation",
         problems == ["parts"] and live["after"].startswith("Gen 43:28") and live["party"]["acts"] == "human" and chg >= 1 and n0 == n1,
         (problems, chg, n0, n1))
    try:
        orec.modify_observation(cfg, conn, oid, {"parts": {**new, "party": {"text": "Joseph asks the brothers", "acts": "robot",
                                                                           "acted_on": "human"}}}, "bad kind (test)", None,
                                "RUN-TEST-2329b", "Claude")
        bad = ""
    except orec.Refused as exc:
        bad = str(exc)
    still = json.loads(q("SELECT parts FROM ib_observation WHERE id=?", oid)[0][0])
    case("T22", "bad input on a modify: a bad party kind is refused and the stored parts are untouched",
         bool(bad) and still["party"]["acts"] == "human", (bad, still["party"]))
    sh2 = sheet_for("Gen.43.27")
    ex2 = [e_ for e_ in sh2["existing"] if e_["observation"] == oid][0]
    case("T23", "after the modify the sheet no longer flags that observation parts_incomplete",
         not any(f["code"] == "parts_incomplete" for f in ex2["flags"]), ex2["flags"])

print(f"\n{sum(res)} of {len(res)} cases pass")
sys.exit(0 if all(res) else 1)
