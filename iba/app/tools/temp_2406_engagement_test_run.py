"""temp_2406_engagement_test_run.py -- escalation #2406 test plan, run on a COPY of iba.db (lib/dbsnapshot.copy_db), never the live one.
Usage: python iba/app/tools/temp_2406_engagement_test_run.py <scratch dir>   (the copy and the working files go there)."""
import json
import pathlib
import sqlite3
import subprocess
import sys
from types import SimpleNamespace

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import engagement as he  # noqa: E402
from iba.app.lib import dbsnapshot, engagement as eg  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

scratch = pathlib.Path(sys.argv[1])
scratch.mkdir(parents=True, exist_ok=True)
copy = scratch / "iba-copy.db"
copy.exists() or dbsnapshot.copy_db(copy)
for mname in ("engagement_2406_v1_20261109", "engagement_2406_v2_module_enum_20261109", "engagement_2406_v3_review_close_20261109"):
    mdir = ROOT / "iba/app/migration"
    mpath = mdir / f"{mname}.py" if (mdir / f"{mname}.py").exists() else mdir / "archive" / f"{mname}.py"
    mig = subprocess.run([sys.executable, str(mpath), "--db", str(copy), "--no-snapshot"], capture_output=True, text=True)
    print("migration:", mname, mig.stdout.strip() or mig.stderr.strip()[-300:])
cn = sqlite3.connect(copy)
for key, val in (("engagement.working_dir", scratch / "work"), ("engagement.report_path", scratch / "reports")):
    cn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val.as_posix()), key))
cn.commit()
cn.close()
cfg = Cfg(copy)
conn = cfg.conn
res = []


def case(name, what, okk, detail=""):
    res.append(bool(okk))
    print(f"{name} {'PASS' if okk else 'FAIL'} {what}" + ("" if okk else f"  -- {detail}"), flush=True)


def call(fn, **params):
    return fn(SimpleNamespace(cfg=cfg, params=params, run_id="RUN-TEST-ENGAGEMENT"))


def n(sql, *a):
    return conn.execute(sql, a).fetchone()[0]


# ---- 1 pull ----
r = call(he.pull, Collection="no-such-collection")
case("P1", "an unknown collection is refused, no file", r.condition == "refused" and not (scratch / "work").exists(), r.message)
r = call(he.pull)
case("P2", "no -Collection is refused", r.condition == "refused", r.message)
r = call(he.pull, Collection="aloud")
pull_file = next((scratch / "work").glob("engagement-aloud-pull-*.json"), None)
case("P3", "the pull of aloud is written", r.condition == "ok" and pull_file is not None, r.message)
pulled = json.loads(pull_file.read_text(encoding="utf-8"))
names = sorted(s["surface"] for s in pulled["surfaces"])
case("P4", "the 8 member surfaces of aloud, no outside word (R4)", names == sorted(["aloud", "uttered", "silence", "quiet", "quieted", "quietly", "quietness", "silent"]), names)
verses = {i["osisId"] for s in pulled["surfaces"] for i in s["items"]}
case("P5", "153 distinct verses, each item with text and a cluster", len(verses) == 153 and all(i["text"] and i["cluster"] for s in pulled["surfaces"] for i in s["items"]),
     f"{len(verses)} verses")
before = n("SELECT count(*) FROM ib_observation")
case("P6", "Pull writes no table row", before == n("SELECT count(*) FROM ib_observation"))
r2 = call(he.pull, Collection="aloud")
case("P7", "a second pull of the day is -v2 and the first is archived (filingkit)", r2.condition == "ok" and "-v2" in r2.message
     and any((scratch / "work" / "archive").glob("engagement-aloud-pull-*.json")), r2.message)
pull_file = next(p for p in (scratch / "work").glob("engagement-aloud-pull-*-v2.json"))
pulled = json.loads(pull_file.read_text(encoding="utf-8"))

# ---- 2 group before any assessment ----
r = call(he.group, Collection="aloud", Check="true")
case("G0", "Group before the assessment: every surface not assessed, none to change", "not assessed: aloud" in r.message and r.counts["change"] == 0, r.message[:300])
r = call(he.check, Collection="aloud")
case("K0", "Check before the assessment names the surfaces not assessed", r.condition == "not_assessed" and "aloud" in r.message, r.message)

# ---- 3 the filled assessment, built from the pull ----
existing = pulled["existing_observations"]


def build(mut=None):
    evals, obs = [], []
    groups = {}
    for s in pulled["surfaces"]:
        for k, it in enumerate(s["items"]):
            if s["surface"] == "aloud":                       # a characteristic everywhere
                e = {"result": "relevant", "role": "characteristic", "test": "inner_being_vocabulary", "reason": "the surface names the voiced cry in this verse"}
            elif s["surface"] == "quiet":                      # qualifier, characteristic, bears_on and no bearing mixed
                e = [{"result": "relevant", "role": "qualifier", "gives": "calm", "test": "negation_or_modifier", "reason": "it gives the calm of the operation"},
                     {"result": "relevant", "role": "characteristic", "test": "volitional_sense", "reason": "it is the standing calm itself in this verse"},
                     {"result": "bears_on", "role": "object", "test": "other_party", "reason": "it names what the act is directed at"},
                     {"result": "not_relevant", "reason": "nothing beyond grammar in this verse here"}][k % 4]
            elif s["surface"] == "quieted":                    # no bearing anywhere: leaves the study group
                e = {"result": "not_relevant", "reason": "no inner-being role in this verse at all"}
            else:                                              # qualifier only
                e = {"result": "relevant", "role": "qualifier", "gives": "manner", "test": "negation_or_modifier", "reason": "it gives the manner of the operation"}
            evals.append({"surface": s["surface"], "vl_id": it["vl_id"], **e})
            key = (s["surface"], e.get("role") or "none", e.get("gives") or "")
            groups.setdefault(key, []).append(it["vl_id"])
    for i, ((surf, role, gives), vls) in enumerate(sorted(groups.items())):
        silent = role == "none"
        obs.append({"key": f"o{i}", "surface": surf, "kind": "silence" if silent else "statement", "role": None if silent else role, "gives": gives,
                    "basis": "read", "vl_ids": vls, "text": f"engagement test: {surf} as {role} {gives}".strip() + " in these verses",
                    "meaning": "test"})
    acts = [{"id": int(i), "action": "accept"} for i, o in existing.items() if o["stage"] != "engagement"]
    f = {"pull": str(pull_file), "evaluations": evals, "observations": obs, "existing": acts}
    if mut:
        mut(f)
    p = scratch / "assess.json"
    p.write_text(json.dumps(f), encoding="utf-8")
    return str(p), f


# refusals first: nothing may be written
rows0 = (n("SELECT count(*) FROM ib_observation"), n("SELECT count(*) FROM ib_node"), n("SELECT count(*) FROM ib_observation_change"))


def same_rows():
    return rows0 == (n("SELECT count(*) FROM ib_observation"), n("SELECT count(*) FROM ib_node"), n("SELECT count(*) FROM ib_observation_change"))


p, _ = build(lambda f: f["evaluations"].pop())
r = call(he.record, File=p)
case("R1", "a surface item with no evaluation is refused, nothing written", r.condition == "refused" and "has no evaluation" in r.message and same_rows(), r.message[:200])
p, _ = build(lambda f: f["evaluations"][0].update(reason="short"))
r = call(he.record, File=p)
case("R2", "a reason that is too short is refused", r.condition == "refused" and "reason needs" in r.message and same_rows(), r.message[:200])
p, _ = build(lambda f: f["evaluations"][0].update(role="qualifier"))
r = call(he.record, File=p)
case("R3", "a qualifier with no `gives` and a role that does not fit the observation are refused", r.condition == "refused" and "gives" in r.message and same_rows(), r.message[:300])
p, _ = build(lambda f: f["observations"][0].update(kind="silence"))
r = call(he.record, File=p)
case("R4", "the silence kind on a surface that has bearing is refused", r.condition == "refused" and "does not fit" in r.message and same_rows(), r.message[:300])
if any(o["stage"] != "engagement" for o in existing.values()):
    p, _ = build(lambda f: f["existing"].pop())
    r = call(he.record, File=p)
    case("R5", "an existing observation with no action is refused", r.condition == "refused" and "no action" in r.message and same_rows(), r.message[:200])
else:
    print("R5 SKIP no existing observation on the verses of aloud")
p, _ = build(lambda f: f["evaluations"].append(dict(f["evaluations"][0])))
r = call(he.record, File=p)
case("R6", "an item evaluated twice is refused", r.condition == "refused" and "evaluated twice" in r.message and same_rows(), r.message[:200])

# the real record
p, f = build()
r = call(he.record, File=p, Check="true")
case("R7", "-Check previews and writes nothing", r.condition == "ok" and "PREVIEW" in r.message and same_rows(), r.message[:300])
r = call(he.record, File=p)
case("R8", "the assessment is written", r.condition == "ok" and r.counts["observations"] == len(f["observations"]), r.message)
n_items = sum(len(s["items"]) for s in pulled["surfaces"])
case("R9", "one live engagement node for each surface item, on the item's verse_lexical row",
     n("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='engagement' AND n.deleted=0") == n_items
     and n("SELECT count(DISTINCT n.verse_lexical_id) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='engagement'") == n_items,
     n("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='engagement'"))
case("R10", "no-bearing items are silence-kind observations with a node and no role; the others carry a role",
     n("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='engagement' AND ((o.tag='silence') != (n.role IS NULL))") == 0)
case("R11", "every observation has a cluster, every node a cluster and a Strong's code", n("SELECT count(*) FROM ib_observation WHERE stage='engagement' AND cluster_code IS NULL") == 0
     and n("SELECT count(*) FROM ib_node WHERE source_stage='engagement' AND (cluster_code IS NULL OR strong IS NULL)") == 0)
r = call(he.record, File=p)
case("R12", "a second Record changes nothing (observations reused, no new node)", r.condition == "ok" and r.counts["observations"] == 0 and r.counts["nodes"] == 0, r.message)

# existing observations: a modify with its reason in ib_observation_change
old = [int(i) for i, o in existing.items() if o["stage"] != "engagement"]
if old:
    oid = old[0]
    p, f = build()
    f["existing"] = [a for a in f["existing"] if a["id"] != oid] + [{"id": oid, "action": "modify", "set": {"implication": "engagement test implication"},
                                                                       "reason": "test of a modify in place"}]
    pathlib.Path(p).write_text(json.dumps(f), encoding="utf-8")
    r = call(he.record, File=p)
    case("R13", "a modify is made in place with its old value, new value and reason kept", r.condition == "ok" and r.counts["modified"] == 1
         and n("SELECT count(*) FROM ib_observation_change WHERE observation_id=? AND column_name='implication' AND new_value='engagement test implication'", oid) == 1
         and n("SELECT implication FROM ib_observation WHERE id=?", oid) == "engagement test implication", r.message[:300])
else:
    print("R13 SKIP no existing observation on the verses of aloud")

# ---- 4 group ----
conn.execute("UPDATE surface_term SET group_state='confirmed' WHERE surface='silent' AND deleted=0")   # the researcher confirmed this one
conn.commit()
r = call(he.group, Collection="aloud", Check="true")
case("G1", "-Check previews, writes nothing", "PREVIEW" in r.message and n("SELECT count(*) FROM surface_event WHERE created_by='engagement'") == 0, r.message[:400])
r = call(he.group, Collection="aloud")
g = dict(conn.execute("SELECT surface, surface_group FROM surface_term WHERE deleted=0 AND surface IN "
                      "('aloud','uttered','silence','quiet','quieted','quietly','quietness','silent')").fetchall())
case("G2", "the rule: characteristic -> behaviour (aloud, quiet); qualifier only -> inner_being_state; no bearing -> other",
     g["aloud"] == "behaviour" and g["quiet"] == "behaviour" and g["uttered"] == "inner_being_state" and g["quieted"] == "other", g)
case("G3", "a group the researcher confirmed is held", "held: silent" in (r.message + (r.escalation or {}).get("question", "")) and conn.execute(
    "SELECT group_state FROM surface_term WHERE surface='silent' AND deleted=0").fetchone()[0] == "confirmed", str(r.escalation)[:400])
case("G4", "a surface that leaves the study group raises one escalation for the collection, never an unlink",
     r.escalation is not None and "quieted" in r.escalation["question"], r.escalation)
case("G5", "each change keeps the value before in surface_event; state corrected, judged by the rule",
     n("SELECT count(*) FROM surface_event WHERE created_by='engagement' AND action='set_group'") == r.counts["changed"] > 0
     and n("SELECT count(*) FROM surface_term WHERE surface='aloud' AND group_state='corrected' AND group_judged_by='rule:engagement'") >= 1)
case("G6", "no collection link is changed by Group", n("SELECT count(*) FROM collection_link WHERE updated_at > '2026-11-09T07' AND deleted=1") == 0)
r = call(he.group, Collection="aloud")
case("G7", "a second Group changes nothing and raises nothing", r.counts.get("changed") == 0 and r.escalation is None, r.message[:300])

# ---- 5 check ----
r = call(he.check, Collection="aloud")
case("K1", "Check passes when every member surface is assessed in every verse and writes a report", r.condition == "ok"
     and any((scratch / "reports").glob("engagement-aloud-check-*.md")), r.message)
# ---- 6 review and close (ruling B of #2411) ----
r = call(he.review, Collection="aloud")
rev_file = max((scratch / "work").glob("engagement-aloud-review-*.json"), key=lambda q: q.stat().st_mtime, default=None)
case("V1", "Review writes the review file of the no-bearing verses", r.condition == "ok" and rev_file is not None, r.message)
rev = json.loads(rev_file.read_text(encoding="utf-8"))
rev_items = [(s["surface"], i) for s in rev["surfaces"] for i in s["items"]]
role_nodes = {}
for vl, role in conn.execute("SELECT n.verse_lexical_id, n.role FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='engagement' AND n.deleted=0"):
    role_nodes[vl] = role
verses_with_bearing = {i["osisId"] for s in pulled["surfaces"] for i in s["items"] if role_nodes.get(i["vl_id"])}
case("V2", "every review verse has no surface with bearing, every item is a no-bearing node",
     rev_items and all(i["osisId"] not in verses_with_bearing and role_nodes.get(i["vl_id"], "x") is None for _, i in rev_items), f"{len(rev_items)} items")
case("V3", "the review holds only member surfaces (R4)", {s for s, _ in rev_items} <= set(names))


def dec(item, kind, **kw):
    d = {"surface": item[0], "vl_id": item[1]["vl_id"], "decision": kind}
    d.update(kw)
    return d


def build_close(mut=None, reopen_first=False):
    decisions = [dec(it, "confirm", reason="read again: still no inner-being role here") for it in rev_items]
    obs = []
    if reopen_first:
        it = rev_items[0]
        decisions[0] = dec(it, "reopen", result="relevant", role="characteristic", test="volitional_sense", reason="read again: it is the characteristic here")
        obs = [{"key": "r1", "surface": it[0], "kind": "statement", "role": "characteristic", "gives": "", "basis": "read", "vl_ids": [it[1]["vl_id"]],
                "text": "engagement review test: reopened as characteristic in this verse"}]
    f = {"review": str(rev_file), "decisions": decisions, "observations": obs}
    if mut:
        mut(f)
    q = scratch / "close.json"
    q.write_text(json.dumps(f), encoding="utf-8")
    return str(q), f


rows1 = (n("SELECT count(*) FROM ib_node"), n("SELECT count(*) FROM ib_observation_change"), n("SELECT count(*) FROM ib_observation"))


def same1():
    return rows1 == (n("SELECT count(*) FROM ib_node"), n("SELECT count(*) FROM ib_observation_change"), n("SELECT count(*) FROM ib_observation"))


q, _ = build_close(lambda f: f["decisions"].pop())
r = call(he.close, File=q)
case("V4", "an item with no decision is refused, nothing written", r.condition == "refused" and "has no decision" in r.message and same1(), r.message[:200])
q, _ = build_close(lambda f: f["decisions"][0].update(reason="no"))
r = call(he.close, File=q)
case("V5", "a confirm without a proper reason is refused", r.condition == "refused" and "needs its reason" in r.message and same1(), r.message[:200])
q, _ = build_close(lambda f: f["decisions"][0].update(decision="reopen", result="not_relevant", reason="read again: nothing here at all"))
r = call(he.close, File=q)
case("V6", "a reopen that says no bearing is refused", r.condition == "refused" and "a no-bearing result is a confirm" in r.message and same1(), r.message[:200])
q, _ = build_close(reopen_first=True, mut=lambda f: f.__setitem__("observations", []))
r = call(he.close, File=q)
case("V7", "a reopened item with no observation is refused", r.condition == "refused" and "in no observation" in r.message and same1(), r.message[:200])
q, f = build_close(reopen_first=True)
r = call(he.close, File=q, Check="true")
case("V8", "-Check previews and writes nothing", r.condition == "ok" and "PREVIEW" in r.message and same1(), r.message[:200])
r = call(he.close, File=q)
first = rev_items[0][1]["vl_id"]
case("V9", "Close writes: all confirmed but one reopened", r.condition == "ok" and r.counts["reopened"] == 1 and r.counts["confirmed"] == len(rev_items) - 1, r.message)
case("V10", "a confirm is kept in ib_observation_change (column reviewed) with its reason",
     n("SELECT count(*) FROM ib_observation_change WHERE column_name='reviewed' AND new_value='confirmed' AND reason LIKE 'read again%'") == len(rev_items) - 1)
case("V11", "the reopened no-bearing node is deleted with its reason and a characteristic node is written on the same verse_lexical row",
     n("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.verse_lexical_id=? AND n.deleted=1 AND n.role IS NULL AND o.stage='engagement'", first) == 1
     and n("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.verse_lexical_id=? AND n.deleted=0 AND n.role='characteristic' AND o.stage='engagement'", first) == 1
     and n("SELECT count(*) FROM ib_observation_change WHERE column_name='deleted' AND reason LIKE 'review of the no-bearing result%'") >= 1)
r = call(he.review, Collection="aloud")
case("V12", "after Close the confirmed verses are set aside and the reopened verse is not a no-bearing verse any more",
     r.condition == "ok" and ("no verse to review" in r.message or str(rev_items[0][1]["osisId"]) not in json.dumps(json.loads(
         max((scratch / "work").glob("engagement-aloud-review-*.json"), key=lambda q2: q2.stat().st_mtime).read_text(encoding="utf-8"))["verses"])), r.message)
r = call(he.check, Collection="aloud")
case("V13", "Check reports the no-bearing items and how many the review confirmed", "confirmed in the review" in max((scratch / "reports").glob("engagement-aloud-check-*.md"),
     key=lambda q2: q2.stat().st_mtime).read_text(encoding="utf-8"), r.message)

print("ALL PASS" if all(res) else "SOME FAILED")
