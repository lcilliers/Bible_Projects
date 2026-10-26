"""temp_2305_prior_capture_test_run.py -- the test plan of escalation #2305 (design
outputs/escalation/2305-prior-work-capture-design-v2-20261026.md sec 7; method rules CP-01 to CP-08). Runs on a copy of
iba.db made with lib/dbsnapshot.copy_db, the migration applied to the copy and the output folder redirected to the
scratch directory. Fills here are synthetic (they test the mechanics, not a capture): the real captures are the pilot.
Expected values by plain SQL on the copy.

Usage: python iba/app/tools/temp_2305_prior_capture_test_run.py <scratch dir> [--source <db>]
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
from iba.app.lib import cfgquality as q  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("scratch")
ap.add_argument("--source")
A = ap.parse_args()
S = pathlib.Path(A.scratch) / "t2305"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", *([A.source] if A.source else []))
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
mig = ROOT / "iba/app/migration/prior_capture_config_2305_v1_20261026.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(mig), "--db", str(DB)],
                                                                 capture_output=True, text=True, env=env)) for _ in range(2)]
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='prior_capture.output_dir'", (json.dumps(str(S / "out")),))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
from iba.app.handlers import priorcapture as h  # noqa: E402
from iba.app.lib import priorcapture as pc  # noqa: E402
results = []
FEAR, M18 = 8, 86


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/").replace("\n", " ")[:600]))
    print(f"{cid} {'PASS' if passed else 'FAIL'}" + ("" if passed else f"  {str(evidence)[:900]}"), flush=True)


def qv(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(step, **params):
    params = {k: v for k, v in params.items() if v is not None}
    return getattr(h, step)(Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None,
                                params=params, step_id=f"prior_capture.{step}"))


def prep(fid):
    o = run("prepare", File=str(fid))
    return o, (json.loads(pathlib.Path(o.counts["path"]).read_text(encoding="utf-8")) if o.condition == "ok" else None)


def put(d, name):
    p = S / name
    p.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    return str(p)


def state():
    return (qv("SELECT count(*) FROM ib_observation")[0][0], qv("SELECT count(*) FROM ib_node")[0][0],
            qv("SELECT count(*) FROM prior_capture_line")[0][0],
            qv("SELECT count(*) FROM reading_file WHERE capture_status<>'not started'")[0][0])


def base_fill(d, finding=None):
    """Every line a pointer, except line 1 which carries one finding on its first verse (verse-only node)."""
    d = copy.deepcopy(d)
    first = d["lines"][0]
    verse = next(r["verse"] for r in first["refs"] if r["verse"])
    f = finding or {"key": "f1", "kind": "statement", "text": "Synthetic finding about the verse.", "basis": "read",
                    "nodes": [{"verse": verse}]}
    d["findings"] = [f]
    for i, l in enumerate(d["lines"]):
        l["answer"] = {"captured": [f["key"]]} if i == 0 else \
            {"not_an_observation": "pointer with no content", "reason": "synthetic: a pointer"}
    return d


def refused(d, expect, name):
    before = state()
    o = run("record", File=put(d, name))
    return o.condition == "refused" and expect in o.message and state() == before, (o.condition, o.message[:300])


# ── 0 migration ─────────────────────────────────────────────────────────────────────────────────
case("T0", "migration on the copy, and a second run writes nothing",
     "applied" in mo[0] and "0 cfg write(s)" in mo[1], mo)

# ── 1 Prepare ───────────────────────────────────────────────────────────────────────────────────
o, fear = prep(FEAR)
nl = qv("SELECT count(DISTINCT line_no) FROM reading_ref WHERE file_id=? AND deleted=0", FEAR)[0][0]
nv = qv("SELECT count(DISTINCT verse_id) FROM reading_ref WHERE file_id=? AND deleted=0 AND verse_id IS NOT NULL", FEAR)[0][0]
case("T1a", "Prepare (fear ledger, by id): lines and verses equal the index; every line has its text; written to the "
     "redirected folder", o.condition == "ok" and len(fear["lines"]) == nl and fear["counts"]["verses"] == nv and
     all(l["text"] for l in fear["lines"]) and str(S) in o.counts["path"], (o.message, nl, nv))
exp_oct = qv("SELECT count(*) FROM ib_observation WHERE status<>'withdrawn' AND stable_key IS NOT NULL AND "
             "revisit_note LIKE (SELECT '%'||path||'%' FROM reading_file WHERE id=?)", FEAR)[0][0]
case("T1b", "Prepare lists the October ids already recorded for the document (FE-47 is observation 11762)",
     len(fear["october"]) == exp_oct and fear["october"].get("fear:FE-47") == 11762, (len(fear["october"]), exp_oct))
case("T1b2", "Prepare also lists live ids of the same prefix whose revisit_note does not name the file (FE-64 is "
     "observation 11776, held to OT-108.26), kept apart from the document's own", fear["october_same_prefix"].get(
         "fear:FE-64") == 11776 and "fear:FE-64" not in fear["october"], fear["october_same_prefix"].get("fear:FE-64"))
path = qv("SELECT path FROM reading_file WHERE id=?", FEAR)[0][0]
o2 = run("prepare", File=path)
case("T1c", "Prepare by repo-relative path equals Prepare by id", o2.condition == "ok" and o2.counts["lines"] == nl,
     o2.message)
words = [w for ws in fear["verse_words"].values() for w in ws]
case("T1d", "verse_words holds M/T-coded words with clusters, and none without",
     words and all(w["clusters"] and all(x[0] in "MT" for x in w["clusters"]) for w in words), len(words))
o = run("prepare", File="no/such/document.md")
case("T2a", "Prepare refuses a path that is not in the index", o.condition == "refused", o.message)
conn.execute("UPDATE reading_file SET sha256='x' WHERE id=?", (FEAR,))
conn.commit()
o = run("prepare", File=str(FEAR))
conn.execute("UPDATE reading_file SET sha256=? WHERE id=?", (fear["file"]["sha256"], FEAR))
conn.commit()
case("T2b", "Prepare refuses a document changed since the index was built", o.condition == "refused" and
     "changed since" in o.message, o.message)

# ── 3 Record: refusals, each leaves the database as it was ──────────────────────────────────────
o, m18 = prep(M18)
ok_ = o.condition == "ok"
case("T3-prep", "Prepare (M18 reading)", ok_, o.message)
b = base_fill(m18)
v = lambda **kw: {**b["findings"][0], **kw}  # noqa: E731


def mutated(findings=None, lines=None):
    d = copy.deepcopy(b)
    if findings is not None:
        d["findings"] = findings
    if lines is not None:
        d["lines"] = lines(d["lines"])
    return d


tests = [
    ("T3a", "an unanswered line is refused (CP-01)", mutated(lines=lambda ls: [ls[0], {**ls[1], "answer": None}] + ls[2:]), "no answer"),
    ("T3b", "a line missing from the JSON is refused", mutated(lines=lambda ls: ls[:-1]), "differ from the index"),
    ("T3c", "an unknown kind is refused", mutated([v(kind="bogus")]), "kind must be one of"),
    ("T3d", "a bad basis is refused", mutated([v(basis="guess")]), "basis must be one of"),
    ("T3e", "a party finding without a route is refused", mutated([v(kind="party")]), "carries its route"),
    ("T3f", "a route on a statement is refused", mutated([v(route="A")]), "route"),
    ("T3g", "empty text is refused", mutated([v(text=" ")]), "text is required"),
    ("T3h", "a bad disposition is refused", mutated([v(nodes=[{**b["findings"][0]["nodes"][0], "disposition": "W"}])]),
     "disposition must be one of"),
    ("T3i", "a bad role is refused", mutated([v(nodes=[{**b["findings"][0]["nodes"][0], "role": "main"}])]), "role must be"),
    ("T3j", "a finding with no node is refused", mutated([v(nodes=[])]), "at least one node"),
    ("T3k", "a finding no line captured is refused", mutated([v(), {**v(key="f2", text="Another synthetic finding.")}]),
     "no line answers captured"),
    ("T3l", "captured naming an unknown finding is refused", mutated(lines=lambda ls: [{**ls[0], "answer": {"captured": ["zz"]}}] + ls[1:]),
     "not a finding"),
    ("T3m", "already_recorded naming a missing observation is refused",
     mutated(lines=lambda ls: [{**ls[0], "answer": {"captured": ["f1"], "already_recorded": [999999999]}}] + ls[1:]),
     "not live"),
    ("T3n", "a bad not_an_observation class is refused",
     mutated(lines=lambda ls: [ls[0], {**ls[1], "answer": {"not_an_observation": "dull", "reason": "x"}}] + ls[2:]),
     "not_an_observation is one of"),
    ("T3o", "a not_an_observation without a reason is refused",
     mutated(lines=lambda ls: [ls[0], {**ls[1], "answer": {"not_an_observation": "heading"}}] + ls[2:]), "with a reason"),
    ("T3p", "a node's word that is not in the verse is refused",
     mutated([v(nodes=[{"verse": b["findings"][0]["nodes"][0]["verse"], "strong": "H0001", "role": "standalone"}])]),
     "H0001"),
    ("T3q", "a verse that does not exist is refused", mutated([v(nodes=[{"verse": "Zzz 9:9"}])]), "not one verse"),
]
for cid, desc, d, expect in tests:
    passed, ev = refused(d, expect, f"{cid}.json")
    case(cid, desc, passed, ev)
d = copy.deepcopy(b)
d["file"]["sha256"] = "x"
passed, ev = refused(d, "another version", "T3r.json")
case("T3r", "a JSON built from another version of the document is refused", passed, ev)
passed, ev = refused({"kind": "other"}, "not a prior-capture JSON", "T3s.json")
case("T3s", "a file that is not a prior-capture JSON is refused", passed, ev)

# ── 4 Record: success, then the document is done ───────────────────────────────────────────────
before = state()
o = run("record", File=put(b, "base.json"))
nlines = len(m18["lines"])
st = state()
obs = qv("SELECT * FROM ib_observation WHERE stage='prior-capture'")
nd = qv("SELECT * FROM ib_node WHERE source_stage='prior-capture'")
case("T4a", "Record writes the finding, its node, an answer per line and the status",
     o.condition == "ok" and st == (before[0] + 1, before[1] + 1, before[2] + nlines, before[3] + 1) and
     qv("SELECT capture_status FROM reading_file WHERE id=?", M18)[0][0] == "captured", (o.message, before, st))
path18 = qv("SELECT path FROM reading_file WHERE id=?", M18)[0][0]
case("T4b", "the observation: stage prior-capture, status draft, tag, basis, revisit_note names the file and its line",
     len(obs) == 1 and obs[0]["status"] == "draft" and obs[0]["tag"] == "statement" and obs[0]["cluster_code"] is None and
     obs[0]["revisit_note"].startswith(f"Captured from {path18} lines ") and obs[0]["revisit_note"].endswith("(#2305)"),
     dict(obs[0]) if obs else None)
case("T4c", "the verse-only node takes the document's cluster, no word, seq 0, source_stage prior-capture",
     len(nd) == 1 and nd[0]["cluster_code"] == "M18" and nd[0]["strong"] is None and nd[0]["seq"] == 0 and
     nd[0]["verse_reference"] == b["findings"][0]["nodes"][0]["verse"], dict(nd[0]) if nd else None)
rows = qv("SELECT answer, count(*) FROM prior_capture_line WHERE file_id=? GROUP BY 1", M18)
case("T4d", "line answers: one captured, the rest not an observation with class and reason",
     dict(map(tuple, rows)) == {"captured": 1, "not an observation": nlines - 1} and
     qv("SELECT count(*) FROM prior_capture_line WHERE answer='not an observation' AND (reason_class IS NULL OR "
        "reason IS NULL)")[0][0] == 0, [tuple(r) for r in rows])
o = run("prepare", File=str(M18))
case("T4e", "a captured document is not prepared again", o.condition == "refused" and "already captured" in o.message, o.message)
passed, ev = refused(b, "already captured", "T4f.json")
case("T4f", "a captured document is not recorded again", passed, ev)
case("T4g", "the other documents are untouched",
     qv("SELECT count(*) FROM reading_file WHERE capture_status<>'not started'")[0][0] == 1, "")

# ── 5 Word nodes (fear ledger) ──────────────────────────────────────────────────────────────────
verse, w1 = next((vv, ws[0]) for vv, ws in fear["verse_words"].items() if len(ws[0]["clusters"]) == 1 and
                 sum(1 for x in ws if x["strong"] == ws[0]["strong"]) == 1)
fd = copy.deepcopy(fear)
first = fd["lines"][0]
fd["findings"] = [{"key": "w1", "kind": "face", "text": "Synthetic word finding.", "basis": "stated",
                   "nodes": [{"verse": verse, "strong": w1["strong"], "surface": w1["surface"], "role": "characteristic",
                              "disposition": "told", "disposition_note": "touches 10.1"}]}]
for i, l in enumerate(fd["lines"]):
    l["answer"] = {"captured": ["w1"]} if i == 0 else {"already_recorded": [11762]} if i == 1 else \
        {"not_an_observation": "heading", "reason": "synthetic"}
o = run("record", File=put(fd, "word.json"))
n = qv("SELECT * FROM ib_node WHERE source_stage='prior-capture' AND strong=?", w1["strong"])
n = [x for x in n if x["verse_reference"] == verse]
case("T5a", "a word node: occurrence, surface, morph, cluster from the tables; disposition and note kept",
     o.condition == "ok" and len(n) == 1 and n[0]["verse_lexical_id"] == w1["verse_lexical_id"] and
     n[0]["cluster_code"] == w1["clusters"][0] and n[0]["surface"] == w1["surface"] and n[0]["disposition"] == "told" and
     n[0]["disposition_note"] == "touches 10.1", (o.message, [dict(x) for x in n]))
case("T5b", "already_recorded writes an answer row naming the October observation and changes nothing on it",
     qv("SELECT count(*) FROM prior_capture_line WHERE file_id=? AND answer='already recorded' AND observation_id=11762",
        FEAR)[0][0] == 1 and qv("SELECT stage FROM ib_observation WHERE id=11762")[0][0] == "strand-reading", o.message)
case("T5c", "a document of already recorded and passed-over lines plus one finding is captured",
     qv("SELECT capture_status FROM reading_file WHERE id=?", FEAR)[0][0] == "captured", "")

# ── 6 More refusals on real words ───────────────────────────────────────────────────────────────
conn.execute("UPDATE reading_file SET capture_status='not started', capture_run_id=NULL WHERE id=?", (FEAR,))
conn.execute("DELETE FROM prior_capture_line WHERE file_id=?", (FEAR,))
conn.commit()
sk = copy.deepcopy(fd)
sk["findings"][0]["stable_key"] = "fear:FE-47"
passed, ev = refused(sk, "already recorded as observation 11762", "T6a.json")
case("T6a", "a finding whose stable_key is already live is refused (CP-05)", passed, ev)
two_m = [r[0] for r in qv("SELECT strong FROM cluster_strong WHERE deleted=0 AND (cluster_code LIKE 'M%' OR cluster_code "
                          "LIKE 'T%') GROUP BY strong HAVING count(*)>1 AND sum(cluster_code LIKE 'M%')=0")]  # two T, no M
multi = []
for s_ in two_m[:50]:
    multi = qv("SELECT v.osisId, vl.strong FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.strong=? AND "
               "vl.deleted=0 LIMIT 1", s_)
    if multi:
        break
if multi:
    mv = copy.deepcopy(fd)
    mv["findings"][0]["nodes"] = [{"verse": multi[0][0], "strong": multi[0][1], "role": "standalone"}]
    passed, ev = refused(mv, "name the cluster", "T6b.json")
    case("T6b", "a word in two T clusters, with none named and none the document's, is refused", passed, ev)
    mt = qv("SELECT v.osisId, vl.strong FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.strong='G0599' "
            "AND vl.deleted=0 LIMIT 1")
    mv["findings"][0]["nodes"] = [{"verse": mt[0][0], "strong": "G0599", "role": "standalone"}]
    pl = pc.check(cfg, ROOT, mv)
    case("T6b2", "a word in one M and one T cluster takes the M cluster (G0599: T3, M25)",
         pl["plan"][0]["nodes"][0]["cluster"] == "M25", pl["plan"][0]["nodes"][0])
else:
    case("T6b", "a word in more than one cluster is refused until named", False, "no multi-cluster word found")
ud = copy.deepcopy(fd)
ud["findings"][0]["kind"] = "unfitted"
ud["findings"][0]["text"] = "Synthetic unfitted observation."
o = run("record", File=put(ud, "unfitted.json"))
case("T6c", "tag unfitted is accepted and written (Q2)", o.condition == "ok" and qv(
    "SELECT count(*) FROM ib_observation WHERE tag='unfitted' AND stage='prior-capture'")[0][0] == 1, o.message)
conn.execute("UPDATE reading_file SET capture_status='not started', capture_run_id=NULL WHERE id=?", (M18,))
conn.execute("DELETE FROM prior_capture_line WHERE file_id=?", (M18,))
conn.commit()
rt = copy.deepcopy(b)
rt["findings"][0]["text"] = "Synthetic unfitted observation."          # the identical live description (CP-04)
o = run("record", File=put(rt, "reuse.json"))
case("T6d", "an identical live description joins the first observation: no second row, one more node (CP-04)",
     o.condition == "ok" and o.counts["observations_reused"] == 1 and o.counts["observations_new"] == 0 and
     qv("SELECT count(*) FROM ib_observation WHERE obs_text='Synthetic unfitted observation.'")[0][0] == 1 and
     qv("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.obs_text="
        "'Synthetic unfitted observation.'")[0][0] == 2, o.message)
report = pathlib.Path(o.counts["path"]).read_text(encoding="utf-8")
case("T6e", "the run report names the document and its status", path18 in report and "captured" in report, report[:200])

# ── 7 Report ────────────────────────────────────────────────────────────────────────────────────
o = run("report")
case("T7", "Report: documents by status and observations by tag", o.condition == "ok" and "captured 2" in o.message and
     "unfitted" in pathlib.Path(o.counts["path"]).read_text(encoding="utf-8"), o.message)

# ── 8 Registry and validate ─────────────────────────────────────────────────────────────────────
steps = qv("SELECT step, handler FROM cfg_step WHERE work_package='prior-capture' AND inactive=0 ORDER BY ordinal")
grants = qv("SELECT table_name FROM cfg_write_grant WHERE writer='prior_capture.record' AND inactive=0")
case("T8a", "Registry: three steps with handlers, four grants on the record step, the PS script",
     len(steps) == 3 and len(grants) == 4 and qv("SELECT ps_script FROM cfg_work_package WHERE name='prior-capture'")
     [0][0] == "iba/app/ps/Prior-Capture.ps1" and qv("SELECT count(*) FROM cfg_method_rule WHERE "
                                                    "step='prior_capture.record' AND active=1")[0][0] == 10,
     ([tuple(s) for s in steps], [g[0] for g in grants]))
live = sqlite3.connect(f"file:{(ROOT / 'iba/app/db/iba.db').as_posix()}?mode=ro", uri=True)
live.row_factory = sqlite3.Row
AP = ROOT / "iba/app"
checks = {"scope_gaps": lambda x: q.find_rule_scope_gaps(x, AP), "unenforced": q.find_unenforced_behaviour_rules,
          "hedge": q.find_hedge_phrases_in_active_config, "orphan": lambda x: q.find_orphan_configs(x, AP),
          "grant_writers": q.find_unknown_write_grant_writers, "no_ps": q.find_steps_without_ps_script,
          "bypass": lambda x: q.find_ps_scripts_bypassing_runpy(x, AP), "unclassified": q.find_unclassified_active_steps}
new = {}
for k, fn in checks.items():
    lv, cp = fn(live), fn(conn)
    new[k] = [x for x in cp if x not in lv]
mods = {r[0] for r in qv("SELECT value FROM cfg_enum WHERE name='config_module' AND inactive=0")}
bad = [r[0] for r in qv("SELECT key FROM cfg_setting WHERE key LIKE 'prior_capture.%' AND module NOT IN (" +
                       ",".join("?" * len(mods)) + ")", *mods)] if mods else ["no config_module enum"]
case("T8c", "every prior_capture setting names a module in enum config_module (the consistency check)", not bad, bad)
case("T8b", "Validate checks on the copy: no new finding against the live database", not any(new.values()), new)

out = S / "results.md"
out.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" +
               "\n".join(f"| {a} | {b_} | {r_} | {e} |" for a, b_, r_, e in results) + "\n", encoding="utf-8")
print(f"{sum(r_[2] == 'PASS' for r_ in results)} of {len(results)} pass -> {out}")
