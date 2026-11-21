"""temp_2525_standalone_test_run.py -- escalation #2525 test plan, run on a COPY of iba.db (never the live one).
A no-bearing surface of the engagement step is written with the role standalone (researcher ruling 2026-11-21).
Usage: python iba/app/tools/temp_2525_standalone_test_run.py <scratch dir>"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import dbsnapshot, engagement as eg  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

scratch = pathlib.Path(sys.argv[1])
scratch.mkdir(parents=True, exist_ok=True)
copy = scratch / "iba-copy-2525.db"
copy.exists() or dbsnapshot.copy_db(copy)
mig = str(ROOT / "iba/app/migration/archive/silence_nodes_standalone_2525_v1_20261121.py")
r1 = subprocess.run([sys.executable, "-I", mig, "--db", str(copy)], capture_output=True, text=True)
r2 = subprocess.run([sys.executable, "-I", mig, "--db", str(copy)], capture_output=True, text=True)
cfg = Cfg(copy)
conn = cfg.conn
res = []


def case(name, what, ok, detail=""):
    res.append(bool(ok))
    print(f"{name} {'PASS' if ok else 'FAIL'} {what}" + ("" if ok else f"  -- {detail}"), flush=True)


def n(sql, *a):
    return conn.execute(sql, a).fetchone()[0]


SIL = "o.stage='engagement' AND o.tag='silence' AND o.deleted=0 AND n.deleted=0"
case("M1", "the migration runs, and a rerun writes nothing", "0 cfg write(s), 0 node(s)" in r2.stdout and not r1.stderr.strip(), r1.stdout + r1.stderr[-200:] + r2.stdout)
case("M2", "no live engagement silence node is left with no role",
     n(f"SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE {SIL} AND n.role IS NULL") == 0)
case("M3", "every live engagement silence node is standalone",
     n(f"SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE {SIL} AND n.role<>'standalone'") == 0)
case("M4", "nodes of other stages and kinds with no role were not touched",
     n("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND n.role IS NULL") > 10000)
case("M5", "each of the 2,139 nodes that had no role (counted on the live database before the run) has its reason in ib_observation_change, and none else is logged",
     n("SELECT count(*) FROM ib_observation_change WHERE run_id='DEVMODE-2525-SILENCE-NODES-STANDALONE-20261121' AND column_name='role' AND new_value='standalone' AND old_value IS NULL") == 2139
     and n("SELECT count(*) FROM ib_observation_change WHERE run_id='DEVMODE-2525-SILENCE-NODES-STANDALONE-20261121'") == 2139)
case("M6", "the setting is live", json.loads(n("SELECT value FROM cfg_setting WHERE key='engagement.no_bearing_role' AND inactive=0")) == "standalone")

# ---- the check and the write, on a real surface ----
st = eg.settings(cfg)
surf = "search"
vls = conn.execute("SELECT vl.id, v.osisId, v.reference, vl.strong, vl.morph_code FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
                   "WHERE vl.deleted=0 AND lower(trim(vl.surface))=? ORDER BY vl.id LIMIT 3", (surf,)).fetchall()
items = [{"vl_id": r[0], "osisId": r[1], "reference": r[2], "strong": r[3], "morph_code": r[4]} for r in vls]
pulled = {"surfaces": [{"surface": surf, "items": items}], "existing_observations": {}}
ev = [{"surface": surf, "vl_id": items[0]["vl_id"], "result": "relevant", "role": "characteristic", "test": "inner_being_vocabulary", "reason": "test: the surface is the act here"},
      {"surface": surf, "vl_id": items[1]["vl_id"], "result": "relevant", "role": "qualifier", "gives": "manner", "test": "negation_or_modifier", "reason": "test: it gives the manner"},
      {"surface": surf, "vl_id": items[2]["vl_id"], "result": "not_relevant", "reason": "test: nothing for the inner being here"}]
ob = [{"key": "a", "surface": surf, "kind": "statement", "role": "characteristic", "basis": "read", "vl_ids": [items[0]["vl_id"]], "text": "test 2525: search as the act in this verse", "meaning": "t"},
      {"key": "b", "surface": surf, "kind": "qualification", "role": "qualifier", "gives": "manner", "basis": "read", "vl_ids": [items[1]["vl_id"]], "text": "test 2525: search with manner here", "meaning": "t"},
      {"key": "c", "surface": surf, "kind": "silence", "role": None, "basis": "read", "vl_ids": [items[2]["vl_id"]], "text": "test 2525: search holds nothing in this verse", "meaning": "t"}]
errors = []
plan = eg.check_assessment(conn, cfg, pulled, {"evaluations": ev, "observations": ob, "existing": []}, errors)
roles = {p["key"]: [x["role"] for x in p["nodes"]] for p in plan["plan"]}
case("C1", "the checked plan gives the no-bearing node standalone and the others their roles", not errors and roles == {"a": ["characteristic"], "b": ["qualifier"], "c": ["standalone"]}, (errors, roles))
case("C2", "the no-bearing observation's own role is standalone", [p["role"] for p in plan["plan"] if p["key"] == "c"] == ["standalone"])
ev_bad = [dict(e) for e in ev]
ev_bad[2]["role"] = "qualifier"
errs = []
eg.check_assessment(conn, cfg, pulled, {"evaluations": ev_bad, "observations": ob, "existing": []}, errs)
case("C3", "a no-bearing evaluation that names a role is still refused", any("has no role" in e for e in errs), errs[:2])
done = {"observations": 0, "reused": 0, "nodes": 0, "ids": {}}
eg._write_plan(conn, st, plan["plan"], "RUN-TEST-2525", done)
conn.commit()
rows = conn.execute("SELECT n.verse_lexical_id, n.role FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.run_id='RUN-TEST-2525' ORDER BY n.verse_lexical_id").fetchall()
case("W1", "the nodes are written with characteristic, qualifier and standalone", {r[1] for r in rows} == {"characteristic", "qualifier", "standalone"} and len(rows) == 3, rows)

# ---- the group rule is unchanged by standalone, on real collections ----
rule = st["group_rule"]
agree, checked = 0, 0
for name in ("search", "call", "anger", "godly"):
    pl = eg.group_plan(conn, cfg, name)
    col = eg.collection_row(conn, name)
    for tid, (s, tier) in eg.member_terms(conn, col[0], st["tiers"]).items():
        vl = [r[0] for r in conn.execute("SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))=?", (s,))]
        nodes = eg._live_nodes(conn, st["stage"], s, vl)
        if [v for v in vl if v not in nodes] or not vl:
            continue
        rs = {r for x in nodes.values() for r in x}
        want = rule["characteristic"] if "characteristic" in rs else rule["qualifier"] if "qualifier" in rs else rule["none"]
        got = next((c[4] for c in pl["change"] if c[1] == s), None)
        if got is None:
            got = next((x[2] for x in pl["held"] if x[0] == s), want if s in pl["same"] else None)
        checked += 1
        agree += got == want
case("G1", "group_plan gives the group the rule gives from the roles, standalone counted as no bearing", checked > 20 and agree == checked, f"{agree}/{checked}")

# ---- the no-bearing count and the review ----
members = eg.member_terms(conn, eg.collection_row(conn, "search")[0], st["tiers"])
chk = eg.check_collection(conn, cfg, "search")
expect = n("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='engagement' AND o.deleted=0 AND n.deleted=0 AND n.role='standalone' "
           "AND n.verse_lexical_id IN (SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface)) IN (%s))" % ",".join("?" * len(members)),
           *[m[0] for m in members.values()])
case("K1", "Check counts the standalone nodes as the no-bearing items", chk["no_bearing"] == expect and expect > 0, (chk["no_bearing"], expect))
rv = eg.review_pull(conn, cfg, "search")
n_items = sum(len(s["items"]) for s in rv["surfaces"])
case("V1", "the review lists items, all of them nodes that are standalone", n_items > 0 and all(
    conn.execute("SELECT role FROM ib_node WHERE id=?", (i["node_id"],)).fetchone()[0] == "standalone"
    for s in rv["surfaces"] for i in s["items"][:200]), n_items)
print(f"\n{sum(res)} of {len(res)} cases pass")
sys.exit(0 if all(res) else 1)
