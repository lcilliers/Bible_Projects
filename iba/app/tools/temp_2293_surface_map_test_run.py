"""temp_2293_surface_map_test_run.py -- the test plan of escalation #2293 (#2286 U3; design
outputs/escalation/2293-surface-map-design-v1-20261025.md sec 5). Runs on a copy of iba.db made with
lib/dbsnapshot.copy_db, with the migration applied to the copy and the output folder and API usage log redirected to
the scratch directory. Expected values by plain SQL on the copy. The groups and allocations here are synthetic: they
test the mechanics, not a mapping (the real mapping is the pilot, #2298). Case 7 makes one live API call (M67's tail)
only when given --live.

Usage: python iba/app/tools/temp_2293_surface_map_test_run.py <scratch dir> [--live] [--source <db>]
"""
import argparse
import copy
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
from iba.app.lib import surfacemap as sm  # noqa: E402
from iba.app.lib import cfgquality as q  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("scratch")
ap.add_argument("--live", action="store_true")
ap.add_argument("--source")
ap.add_argument("--reset-mapping", action="store_true",
                help="on the copy only: remove the surface mapping (#2298 bulk run) so the cases start unmapped")
A = ap.parse_args()
S = pathlib.Path(A.scratch) / "t2293"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", *([A.source] if A.source else []))
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
mig = ROOT / "iba/app/migration/surface_map_steps_2293_v1_20261025.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(mig), "--db", str(DB)],
                                                                 capture_output=True, text=True, env=env)) for _ in range(2)]
c = sqlite3.connect(DB)
if A.reset_mapping:
    c.execute("DELETE FROM surface_subgroup")
    c.execute("DELETE FROM cluster_subgroup WHERE source='#2293 cluster.surface_map'")
for key, val in (("cluster.surface_map.output_dir", str(S / "out")), ("lexical.llm_usage_log_path", str(S / "usage.csv"))):
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val), key))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
from iba.app.handlers import surfacemap as h  # noqa: E402
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/").replace("\n", " ")[:600]))
    print(f"{cid} {'PASS' if passed else 'FAIL'}" + ("" if passed else f"  {str(evidence)[:900]}"), flush=True)


def qv(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(step, **params):
    params = {k: v for k, v in params.items() if v is not None}
    return getattr(h, step)(Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None,
                                params=params, step_id=f"cluster.surface_{step}"))


def state(cluster):
    return (qv("SELECT count(*) FROM surface_subgroup WHERE cluster_code=? AND deleted=0", cluster)[0][0],
            qv("SELECT count(*) FROM cluster_subgroup WHERE cluster_code=?", cluster)[0][0])


def direct(cluster):
    return qv("SELECT count(*), sum(n) FROM (SELECT count(*) n FROM verse_lexical l JOIN cluster_strong cs ON "
              "cs.strong=l.strong AND cs.deleted=0 AND cs.cluster_code=? WHERE l.deleted=0 GROUP BY l.strong, "
              "lower(trim(coalesce(l.surface,''))))", cluster)[0]


def fill(data, cluster, groups=(("t1", "group"), ("t2", "qualifier")), part="head"):
    d = copy.deepcopy(data)
    codes = [f"{cluster}_{g}" for g, _ in groups]
    d["groups"] += [{"code": code, "label": f"test group {g}", "description": "synthetic", "kind": k, "anchor": None}
                    for code, (g, k) in zip(codes, groups)]
    i = 0
    for a in d["allocations"]:
        if codes and a["part"] == part and not a["group"] and a["surface"]:
            a["group"], a["reason"] = codes[i % len(codes)], "test allocation"
            i += 1
    return d


def write(d, name):
    p = S / name
    p.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    return str(p)


# ── 0 migration ─────────────────────────────────────────────────────────────────────────────────
case("T0", "migration on the copy, and a second run writes nothing", "write(s) applied" in mo[0] and "0 write(s)" in mo[1],
     mo)

# ── 1 Pairs on M18 ──────────────────────────────────────────────────────────────────────────────
o = run("pairs", Cluster="M18")
f18 = json.loads(pathlib.Path(o.counts["path"]).read_text(encoding="utf-8"))
n, hits = direct("M18")
heads = [a for a in f18["allocations"] if a["part"] == "head"]
keys = {(a["strong"], a["surface"]) for a in f18["allocations"]}
case("T1a", "Pairs M18: every pair once; pairs and hits equal a direct query",
     o.condition == "ok" and len(keys) == len(f18["allocations"]) == n and f18["counts"]["hits"] == hits,
     f"{o.condition} pairs {len(f18['allocations'])} vs {n}, hits {f18['counts']['hits']} vs {hits}")
acc, cut = 0, None
for i, a in enumerate(f18["allocations"]):
    if acc >= 0.8 * hits:
        cut = i
        break
    acc += a["hits"]
case("T1b", "Pairs M18: head is the pairs up to 80% of the hits (163 expected from the design)",
     len(heads) == cut == 163, f"head {len(heads)}, cut {cut}")
o2 = run("pairs", Cluster="M18")
case("T1c", "Pairs M18 twice on a day: the second file is -v2, the first archived",
     o2.counts["path"].endswith("-v2.json") and not pathlib.Path(o.counts["path"]).exists(), o2.counts["path"])

# ── 2 Pairs on M67 ──────────────────────────────────────────────────────────────────────────────
o = run("pairs", Cluster="M67")
f67 = json.loads(pathlib.Path(o.counts["path"]).read_text(encoding="utf-8"))
inh = [a for a in f67["allocations"] if a["inherited"]]
pre = [a for a in inh if a["group"] == a["inherited"] and a["reason"].startswith(sm.INHERITED)]
blank = [a for a in f67["allocations"] if not a["inherited"]]
case("T2", "Pairs M67: 24 inherited pairs pre-filled with their subgroup, 20 blank",
     len(inh) == len(pre) == 24 and len(blank) == 20 and all(a["group"] is None for a in blank),
     f"inherited {len(inh)}, prefilled {len(pre)}, blank {len(blank)}")

# ── 3 Apply refusals ────────────────────────────────────────────────────────────────────────────
before = state("M18")
good = fill(f18, "M18")
bad = {}
d = copy.deepcopy(good)
next(a for a in d["allocations"] if a["part"] == "head" and a["group"])["group"] = None
bad["a head pair with no group"] = d
d = copy.deepcopy(good)
d["groups"][-1]["kind"] = None
bad["a new group with no kind"] = d
d = copy.deepcopy(good)
d["groups"][-1]["kind"] = "anomaly"
bad["a new group of kind anomaly (made only by the step)"] = d
d = copy.deepcopy(good)
d["allocations"].append({"strong": "H0001", "surface": "father", "group": "M18_t1", "reason": "x", "two_sense": 0})
bad["a pair not in the cluster"] = d
d = copy.deepcopy(good)
next(a for a in d["allocations"] if a["group"])["reason"] = " "
bad["a blank reason"] = d
d = copy.deepcopy(good)
d["groups"][-1]["code"] = "X_bad"
bad["a new code not <cluster>_<slug>"] = d
d = copy.deepcopy(good)
d["cluster"] = "M19"
bad["a file for another cluster"] = d
for i, (label, d) in enumerate(bad.items()):
    o = run("apply", Cluster="M18", File=write(d, f"bad{i}.json"))
    case(f"T3{chr(97 + i)}", f"Apply refuses {label}, nothing written",
         o.condition == "refused" and state("M18") == before, o.message[:300])
fm = fill(f67, "M67", groups=(), part="none")
mv = next(a for a in fm["allocations"] if a["inherited"])
mv["group"] = next(g["code"] for g in fm["groups"] if g["code"] != mv["inherited"])
o = run("apply", Cluster="M67", File=write(fm, "bad-move.json"))
case("T3h", "Apply refuses an inherited pair moved without a 'correction:' reason",
     o.condition == "refused" and "correction" in o.message and state("M67")[0] == 0, o.message[:300])
o = run("apply", Cluster="M18")
case("T3i", "Apply refuses a missing -File", o.condition == "refused", o.message)

# ── 4 Apply valid ───────────────────────────────────────────────────────────────────────────────
o = run("apply", Cluster="M18", File=write(good, "m18-good.json"))
anom = qv("SELECT count(*) FROM cluster_subgroup WHERE cluster_code='M18' AND kind='anomaly'")[0][0]
rows = [tuple(r) for r in qv("SELECT allocated_by, count(*) FROM surface_subgroup WHERE cluster_code='M18' AND deleted=0 "
                             "GROUP BY 1")]
kinds = dict(qv("SELECT subgroup_code, kind FROM cluster_subgroup WHERE cluster_code='M18'"))
case("T4a", "Apply M18: 2 groups added with their kinds, 163 head pairs as session, one anomaly group",
     o.condition == "ok" and o.counts["groups_added"] == 2 and rows == [("session", 163)] and anom == 1
     and kinds.get("M18_t2") == "qualifier", (o.message, rows, anom, kinds))
o = run("apply", Cluster="M18", File=write(good, "m18-good2.json"))
case("T4b", "Apply the same file again: nothing changes, still one anomaly group",
     o.counts.get("unchanged") == 163 and o.counts.get("inserted") == 0 and o.counts.get("groups_added") == 0 and
     qv("SELECT count(*) FROM cluster_subgroup WHERE cluster_code='M18' AND kind='anomaly'")[0][0] == 1, o.message)
f19 = json.loads(pathlib.Path(run("pairs", Cluster="M19").counts["path"]).read_text(encoding="utf-8"))
o = run("apply", Cluster="M19", File=write(fill(f19, "M19"), "m19.json"))
e = qv("SELECT ss.strong, sg.kind, ss.reason FROM surface_subgroup ss JOIN cluster_subgroup sg ON "
       "sg.id=ss.cluster_subgroup_id WHERE ss.cluster_code='M19' AND ss.surface=''")
case("T4c", "Apply M19: its empty-surface pair (G4100) goes to the anomaly group",
     o.condition == "ok" and len(e) == 1 and e[0][0] == "G4100" and e[0][1] == "anomaly", (o.message, [tuple(x) for x in e]))

# ── 5 Apply M67 (incorporation) ─────────────────────────────────────────────────────────────────
old = [tuple(r) for r in qv("SELECT id, subgroup_code, label, core_description, status, kind FROM cluster_subgroup "
                            "WHERE cluster_code='M67' ORDER BY id")]
fm = copy.deepcopy(f67)
for a in fm["allocations"]:
    if a["part"] == "head" and not a["group"] and a["surface"]:
        a["group"], a["reason"] = "M67_C_earnest_diligence", "test allocation of a missing pair"
mv = next(a for a in fm["allocations"] if a["inherited"] == "M67_A_dispositional_idleness")
mv["group"], mv["reason"] = "M67_B_dereliction_of_duty", "correction: test move of an inherited pair"
o = run("apply", Cluster="M67", File=write(fm, "m67.json"))
by = dict(qv("SELECT allocated_by, count(*) FROM surface_subgroup WHERE cluster_code='M67' AND deleted=0 GROUP BY 1"))
moved = [tuple(r) for r in qv("SELECT allocated_by, reason FROM surface_subgroup WHERE cluster_code='M67' AND strong=? "
                              "AND surface=?", mv["strong"], mv["surface"])]
after = [tuple(r) for r in qv("SELECT id, subgroup_code, label, core_description, status, kind FROM cluster_subgroup "
                              "WHERE cluster_code='M67' AND kind!='anomaly' ORDER BY id")]
heads_missing = sum(1 for a in f67["allocations"] if a["part"] == "head" and not a["inherited"])
case("T5", "Apply M67: 23 inherited, the corrected pair and the missing head pairs as session; old subgroups unchanged",
     o.condition == "ok" and by.get("inherited") == 23 and by.get("session") == 1 + heads_missing
     and moved[0][0] == "session" and after == old, (o.message, by, heads_missing, moved))

# ── 6 Tail preview and cap ──────────────────────────────────────────────────────────────────────
n_tail = len(sm.tail_pairs(conn, "M67", 0.8))
o = run("tail", Cluster="M67")
case("T6a", "Tail preview M67: no call, the pairs and the cost shown, nothing written",
     o.condition == "ok" and o.counts.get("preview") == 1 and o.counts["pairs"] == n_tail and
     not (S / "usage.csv").exists(), o.message)
cap = cfg.required_setting("lexical.llm_max_cost_per_batch")
conn.execute("UPDATE cfg_setting SET value='0.0001' WHERE key='lexical.llm_max_cost_per_batch'")
o = run("tail", Cluster="M67")
conn.execute("UPDATE cfg_setting SET value=? WHERE key='lexical.llm_max_cost_per_batch'", (json.dumps(cap),))
conn.commit()
case("T6b", "Tail refuses a cluster over the cost cap", o.condition == "cost-cap-exceeded", o.message)
o = run("tail", Cluster="M83")
case("T6c", "Tail refuses a cluster whose head is not yet allocated in session (M83 before Apply, B1)",
     o.condition == "refused" and "head pair" in o.message, o.message)
o = run("tail", Cluster="M83")
o = run("tail", Cluster="M20")
case("T6d", "Tail refuses a cluster with no groups yet (M20)", o.condition == "refused" and "no groups" in o.message,
     o.message)

# ── 7 Tail: a bad reply, then live ──────────────────────────────────────────────────────────────
pkg = sm.assemble_tail(cfg, conn, "M67", 0.8)
codes = {g["code"] for g in sm.groups(conn, "M67")}
bads = {"not JSON": "sorry", "a pair missing": json.dumps({"allocations": []}),
        "an unknown group": json.dumps({"allocations": [{"strong": p["strong"], "surface": p["surface"],
                                                         "group": "NOPE", "reason": "x"} for p in pkg["pairs"]]})}
for i, (label, text) in enumerate(bads.items()):
    try:
        sm.parse_tail(text, pkg["pairs"], codes)
        case(f"T7{chr(97 + i)}", f"a reply with {label} is refused", False, "accepted")
    except sm.MapError as exc:
        case(f"T7{chr(97 + i)}", f"a reply with {label} is refused, nothing written", True, str(exc)[:200])
curly = [{"strong": "G0001", "surface": "one’s regret", "gloss": None, "part": "tail"}]
try:
    m = sm.parse_tail(json.dumps({"allocations": [{"strong": "G0001", "surface": "one's  Regret", "group": "X1",
                                                   "reason": "r"}]}), curly, {"X1"})
    case("T7e", "a reply that straightens an apostrophe or changes spacing still names its pair; the exact surface kept "
         "(#2298)", m[0]["surface"] == "one’s regret", m)
except sm.MapError as exc:
    case("T7e", "a reply that straightens an apostrophe still names its pair", False, str(exc))
try:
    m = sm.parse_tail("Looking at each pair in context:\n\n" + json.dumps({"allocations": [{
        "strong": "G0001", "surface": "one’s regret", "group": "X1", "reason": "r"}]}) + "\nDone.", curly, {"X1"})
    case("T7g", "a reply with prose before and after its JSON object is read (#2298)", len(m) == 1, m)
except sm.MapError as exc:
    case("T7g", "a reply with prose before and after its JSON object is read", False, str(exc))
nts = sm._not_this_sense_line([{"code": "M67_x", "kind": "not_this_sense"}])
case("T7f", "the tail instructions name the not_this_sense group when the cluster has one, and keep the anomaly group "
     "for the undecidable (#2298 P1)",
     "M67_x" in nts and sm._not_this_sense_line([{"code": "a", "kind": "group"}]) == "" and
     "never for a rendering whose sense is plainly not the cluster's" in pkg["instructions"], pkg["instructions"][-700:])
if A.live:
    o = run("tail", Cluster="M67", Live="1")
    left = len(sm.tail_pairs(conn, "M67", 0.8))
    api = qv("SELECT count(*), sum(reason IS NULL OR trim(reason)='') FROM surface_subgroup WHERE cluster_code='M67' "
             "AND allocated_by='api' AND deleted=0")[0]
    case("T7d", "Tail live M67: every tail pair placed once, as api, each with a reason; usage logged",
         o.condition == "ok" and left == 0 and api[0] == n_tail and api[1] == 0 and (S / "usage.csv").exists(),
         (o.message, left, tuple(api)))
else:
    case("T7d", "Tail live M67 (needs --live)", False, "not run")

# ── 8 Check ─────────────────────────────────────────────────────────────────────────────────────
o = run("check", Cluster="M67")
r = sm.check(conn, "M67", 0.8, 0.3)
share = round(sum(g["share"] for g in r["groups"]), 3)
case("T8a", "Check M67: report written; shares add to 100% once all pairs are placed; unallocated 0 after Tail",
     o.condition == "ok" and pathlib.Path(o.counts["path"]).exists() and
     (share == 1.0 and o.counts["unallocated"] == 0 if A.live else True), (o.message, share))
o = run("check", Cluster="M18")
r18 = sm.check(conn, "M18", 0.8, 0.3)
over = [g["code"] for g in r18["groups"] if g["over"]]
qual = [g for g in r18["groups"] if g["kind"] == "qualifier"][0]
case("T8b", "Check M18: a group of kind group over 30% is flagged; a qualifier group is never flagged",
     "M18_t1" in over and not qual["over"] and o.counts["over"] == len(over),
     ([(g["code"], g["share"], g["over"]) for g in r18["groups"]], o.message))

# ── 9 Registry and validate ─────────────────────────────────────────────────────────────────────
steps = qv("SELECT step, handler FROM cfg_step WHERE work_package='cluster-surface-map' AND inactive=0 ORDER BY ordinal")
grants = qv("SELECT writer, table_name FROM cfg_write_grant WHERE writer LIKE 'cluster.surface%' AND inactive=0")
case("T9a", "Registry: four steps with handlers, grants for Apply and Tail, the work package's PS script",
     len(steps) == 4 and len(grants) == 4 and qv("SELECT ps_script FROM cfg_work_package WHERE name='cluster-surface-map'")
     [0][0] == "iba/app/ps/Surface-Map.ps1", ([tuple(s) for s in steps], [tuple(g) for g in grants]))
live = sqlite3.connect(f"file:{(ROOT / 'iba/app/db/iba.db').as_posix()}?mode=ro", uri=True)
live.row_factory = sqlite3.Row
AP = ROOT / "iba/app"
checks = {"scope_gaps": lambda x: q.find_rule_scope_gaps(x, AP), "unenforced": q.find_unenforced_behaviour_rules,
          "hedge": q.find_hedge_phrases_in_active_config, "orphan": lambda x: q.find_orphan_configs(x, AP),
          "grant_writers": q.find_unknown_write_grant_writers, "no_ps": q.find_steps_without_ps_script,
          "bypass": lambda x: q.find_ps_scripts_bypassing_runpy(x, AP), "unclassified": q.find_unclassified_active_steps}
new, gone = {}, {}
for k, fn in checks.items():
    lv, cp = fn(live), fn(conn)
    new[k] = [x for x in cp if x not in lv]
    gone[k] = [x for x in lv if x not in cp]
unenf = [x for x in checks["unenforced"](conn) if "#117 " in x or "#118 " in x]
orph = [x for x in checks["orphan"](conn) if "cluster.surface_map" in x]
case("T9b", "Validate checks on the copy: no new finding except B:117 and B:118 now partially_enforced; no "
     "cluster.surface_map setting unread",
     not any(v for k, v in new.items() if k != "unenforced") and
     sorted(new["unenforced"]) == sorted(unenf) and all("partially_enforced" in x for x in unenf) and not orph,
     (new, unenf, orph))

out = S / "results.md"
out.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" +
               "\n".join(f"| {a} | {b} | {r_} | {e} |" for a, b, r_, e in results) + "\n", encoding="utf-8")
print(f"{sum(r_[2] == 'PASS' for r_ in results)} of {len(results)} pass -> {out}")
