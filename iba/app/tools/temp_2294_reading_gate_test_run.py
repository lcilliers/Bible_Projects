"""temp_2294_reading_gate_test_run.py -- the test of escalation #2294 (#2286 U4, decision G-a): stale and unallocated
pairs found, retired, counted by cluster.validate, and refused by reading.open. Runs on a copy of iba.db made with
lib/dbsnapshot.copy_db, with the migration applied to the copy and every output redirected to the scratch directory.
The mappings here are synthetic: they test the gate, not a mapping. No API call is made.

Usage: python iba/app/tools/temp_2294_reading_gate_test_run.py <scratch dir>
"""
import copy
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
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import surfacemap as sm  # noqa: E402
from iba.app.lib import cfgquality as q  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2294"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
mig = ROOT / "iba/app/migration/reading_gate_2294_v1_20261025.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(mig), "--db", str(DB)],
                                                                 capture_output=True, text=True, env=env)) for _ in range(2)]
c = sqlite3.connect(DB)
for key, val in (("cluster.surface_map.output_dir", str(S / "out")), ("cluster.quality_report_path", str(S / "cv.md")),
                 ("reading.output_dir", str(S / "reading")), ("verse_scope.output_dir", str(S / "scope"))):
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val), key))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
from iba.app.handlers import surfacemap as hs  # noqa: E402
from iba.app.handlers import reading as hr  # noqa: E402
from iba.app.handlers import cluster as hc  # noqa: E402
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/").replace("\n", " ")[:600]))
    print(f"{cid} {'PASS' if passed else 'FAIL'}" + ("" if passed else f"  {str(evidence)[:900]}"), flush=True)


def ctx(step_id, **params):
    return Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step_id}", word="", word_id=None,
               params={k: v for k, v in params.items() if v is not None}, step_id=step_id)


def open_reading(label, home, verse):
    return hr.open(ctx("reading.open", Label=label, Escalation="2294", Home=home, Verse=verse, By="Claude",
                       Objective="test of the reading gate on the surface mapping (#2294)"))


def mapfile(cluster, parts=("head", "tail")):
    o = hs.pairs(ctx("cluster.surface_pairs", Cluster=cluster))
    d = json.loads(pathlib.Path(o.counts["path"]).read_text(encoding="utf-8"))
    code = f"{cluster}_t1"
    if not any(g["kind"] != "anomaly" and g["code"] not in (sm.anomaly_code(cluster),) for g in d["groups"]):
        d["groups"].append({"code": code, "label": "test group", "description": "synthetic", "kind": "group",
                            "anchor": None})
    target = next(g["code"] for g in d["groups"] if g.get("kind") != "anomaly")
    for a in d["allocations"]:
        if a["part"] in parts and not a["group"] and a["surface"]:
            a["group"], a["reason"] = target, "test allocation"
    p = S / f"{cluster}-{'-'.join(parts)}.json"
    p.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    return hs.apply(ctx("cluster.surface_apply", Cluster=cluster, File=str(p)))


def ov(cluster):
    return next(m for m in sm.overview(conn) if m["cluster"] == cluster)


case("G1", "migration on the copy, and a second run writes nothing", "write(s) applied" in mo[0] and "0 write(s)" in mo[1],
     mo)
t = time.time()
o = sm.overview(conn)
secs = round(time.time() - t, 2)
case("G2", "overview: 80 M clusters, none allocated, none stale, in seconds (B:71)",
     len(o) == 80 and sum(m["allocated"] for m in o) == 0 and sum(m["stale"] for m in o) == 0 and secs < 5,
     f"{len(o)} clusters, {secs} s")
r = open_reading("t-gate-m18", "M18", "Psa 37:4")
case("G3", "reading.open refuses an unmapped M home cluster (M18), naming the counts and the next step",
     r.condition == "refused" and "unallocated" in r.message and "Surface-Map.ps1" in r.message, r.message[:300])
case("G4", "the gate passes a T home cluster (rule is for M clusters)", sm.reading_refusal(conn, "T3") is None, "")
o = mapfile("M18", parts=("head",))
r = open_reading("t-gate-m18b", "M18", "Psa 37:4")
case("G5", "M18 with only its head allocated: still refused (tail unallocated); overview shows it partly mapped",
     o.condition == "ok" and r.condition == "refused" and ov("M18")["allocated"] and ov("M18")["unallocated"],
     (o.message, r.message[:200], ov("M18")))
o = mapfile("M67")
r = open_reading("t-gate-m67", "M67", "Pro 6:6")
case("G6", "M67 fully allocated: the gate passes and the reading opens",
     o.condition == "ok" and sm.reading_refusal(conn, "M67") is None and r.condition == "ok",
     (o.message, r.condition, r.message[:300]))
cv = hc.validate(ctx("cluster.validate"))
case("G7", "cluster.validate: M18 partly mapped is a finding (escalates), with the mapping in its report",
     cv.escalation is not None and "partly mapped" in cv.message and "Surface mapping" in (S / "cv.md").read_text(
         encoding="utf-8"), cv.message[:300])
moved = conn.execute("SELECT strong FROM surface_subgroup WHERE cluster_code='M67' AND deleted=0 LIMIT 1").fetchone()[0]
n_pairs = conn.execute("SELECT count(*) FROM surface_subgroup WHERE cluster_code='M67' AND strong=? AND deleted=0",
                       (moved,)).fetchone()[0]
conn.execute("UPDATE cluster_strong SET deleted=1 WHERE cluster_code='M67' AND strong=?", (moved,))
conn.commit()
st = sm.stale(conn, "M67")
r = open_reading("t-gate-m67b", "M67", "Pro 6:9")
case("G8", f"a code leaving M67 ({moved}) makes its {n_pairs} pair(s) stale and the gate refuses",
     len(st) == n_pairs and all(s["why"] == "the code is no longer in the cluster" for s in st) and
     r.condition == "refused" and "stale" in r.message, (len(st), r.message[:200]))
ck = hs.check(ctx("cluster.surface_check", Cluster="M67"))
case("G9", "Check lists the stale pairs", ck.counts.get("stale") == n_pairs and "Stale pairs" in pathlib.Path(
    ck.counts["path"]).read_text(encoding="utf-8"), ck.message[:200])
o = mapfile("M67")
left = conn.execute("SELECT count(*), sum(reason LIKE 'stale: %') FROM surface_subgroup WHERE cluster_code='M67' AND "
                    "strong=? AND deleted=1", (moved,)).fetchone()
case("G10", "Apply retires the stale pairs (soft delete, reason kept), and the gate passes again",
     o.counts.get("stale_retired") == n_pairs and tuple(left) == (n_pairs, n_pairs) and not sm.stale(conn, "M67") and
     sm.reading_refusal(conn, "M67") is None, (o.message, tuple(left)))
conn.execute("UPDATE surface_subgroup SET surface='zzz-no-such-surface' WHERE id=(SELECT min(id) FROM surface_subgroup "
             "WHERE cluster_code='M67' AND deleted=0)")
conn.commit()
st = sm.stale(conn, "M67")
case("G11", "a surface that no longer occurs is stale too, with its reason",
     len(st) == 1 and st[0]["why"] == "the surface no longer occurs for the code", st)
live = sqlite3.connect(f"file:{(ROOT / 'iba/app/db/iba.db').as_posix()}?mode=ro", uri=True)
live.row_factory = sqlite3.Row
AP = ROOT / "iba/app"
checks = {"scope_gaps": lambda x: q.find_rule_scope_gaps(x, AP), "hedge": q.find_hedge_phrases_in_active_config,
          "orphan": lambda x: q.find_orphan_configs(x, AP), "grant_writers": q.find_unknown_write_grant_writers,
          "no_ps": q.find_steps_without_ps_script, "report_rows": q.find_missing_cfg_report_rows}
new = {k: [x for x in fn(conn) if x not in fn(live)] for k, fn in checks.items()}
sec = conn.execute("SELECT heading FROM cfg_report_section WHERE step='cluster.validate' AND "
                   "section_key='surface_mapping'").fetchone()
case("G12", "registry: the report section exists; validate checks on the copy show no new finding",
     sec is not None and not any(new.values()), (sec and sec[0], new))

out = S / "results.md"
out.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" +
               "\n".join(f"| {a} | {b} | {r_} | {e} |" for a, b, r_, e in results) + "\n", encoding="utf-8")
print(f"{sum(r_[2] == 'PASS' for r_ in results)} of {len(results)} pass -> {out}")
