"""temp_2312_surface_observe_test_run.py -- escalation #2312 test, on a COPY of iba.db (never the live DB): steps 1 to 3
(Open, the pull in 0.GAP pre, Observe) on the surface. Usage: python iba/app/tools/temp_2312_surface_observe_test_run.py
<scratch dir>. Prints PASS/FAIL per case."""
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
from iba.app.lib import reading as rd  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2312"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
mig = ROOT / "iba/app/migration/surface_observe_2312_v1_20261027.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(mig), "--db", str(DB), *a],
                                                                 capture_output=True, text=True, env=env))
      for a in (["--dry-run"], [], [])]
c = sqlite3.connect(DB)
for key, val in (("reading.output_dir", str(S / "reading")), ("open_item.output_dir", str(S / "open-items"))):
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val), key))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
from iba.app.handlers import reading as hr  # noqa: E402
res = []


def case(cid, desc, ok, ev=""):
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:700]}"), flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(step, **params):
    params.setdefault("By", "Claude")
    return getattr(hr, step)(Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None,
                                 params={k: v for k, v in params.items() if v is not None}, step_id=f"reading.{step}"))


# ── M: the migration ─────────────────────────────────────────────────────────────────────────────
case("M1", "dry run writes nothing; apply writes; a second run is refused",
     mo[0].startswith("DRY RUN") and "write(s) applied" in mo[1] and mo[2].startswith("already applied"), mo)
def setting(k):
    v = cfg.required_setting(k)
    return json.loads(v) if isinstance(v, str) else v


fw = setting("reading.focus_words")
rq = setting("reading.surface_requirements")
case("M2", "focus_words restated (keep_tags T5, T6), surface_requirements present, RS-01 and RS-02 on reading.observe",
     fw["keep_tags"] == ["T5", "T6"] and rq["kinds"] == ["face", "term"]
     and len(q("SELECT 1 FROM cfg_method_rule WHERE step='reading.observe' AND rule_key LIKE 'RS-0%' AND active=1")) == 2, fw)

# ── pick a small scope in M18 whose home passes the surface-map check ─────────────────────────────
verses = q("""SELECT v.id, v.reference, v.osisId, count(*) n FROM verse v JOIN verse_lexical vl ON vl.verse_id=v.id AND vl.deleted=0
 WHERE v.id IN (SELECT vl2.verse_id FROM verse_lexical vl2 JOIN cluster_strong cs ON cs.strong=vl2.strong AND cs.cluster_code='M18'
   AND cs.deleted=0 WHERE vl2.deleted=0) GROUP BY v.id HAVING n BETWEEN 5 AND 12 ORDER BY v.id LIMIT 3""")
refs = [v["reference"] for v in verses]
vid = verses[0]["id"]

# ── S: the surfaces of a verse ────────────────────────────────────────────────────────────────────
st = rd.surfaces_state(cfg, conn, vid)
rows = q("SELECT id, strong, morph_code, testament FROM verse_lexical WHERE verse_id=? AND deleted=0", vid)
occ = {s["occurrence"] for s in st}
case("S1", "every surface in focus is an occurrence of the verse, once", len(occ) == len(st) and occ <= {r["id"] for r in rows},
     (len(st), len(rows)))
m_coded = [r for r in rows if any(x.startswith("M") for x in orec.word_clusters(conn, r["strong"]))]
case("S2", "content words beyond the M-coded ones are in focus; the verse's function words are left out",
     len(st) > len(m_coded) and len(st) < len(rows) + 1, (len(st), len(m_coded), len(rows)))
case("S3", "a surface with nothing recorded lacks role, face and term", any(set(s["missing"]) == {"role", "face", "term"} for s in st),
     [s["missing"] for s in st][:5])
real = q("""SELECT n.verse_lexical_id, o.tag FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.status<>'withdrawn'
 JOIN verse_lexical vl ON vl.id=n.verse_lexical_id WHERE vl.verse_id=? AND o.tag IN ('face','term','silence')""", vid)
if real:
    hit = real[0]
    s = next((s for s in st if s["occurrence"] == hit["verse_lexical_id"]), None)
    case("S4", "an existing live face/term/silence node on an occurrence counts for it",
         s is None or hit["tag"] in s["has"] or hit["tag"] == "silence", (hit["tag"], s and s["has"]))
else:
    case("S4", "an existing node counts (no face/term/silence node on this verse; covered by S5)", True)

# synthetic: a face finding with a node that names no occurrence id: counts by verse, Strong, surface when unique
uniq = None
for s in st:
    same = [r for r in q("SELECT id FROM verse_lexical WHERE verse_id=? AND strong=? AND surface=? AND deleted=0", vid,
                         s["strong"], s["surface"])]
    if len(same) == 1:
        uniq = s
        break
cl = orec.word_clusters(conn, uniq["strong"])[0]
osis = verses[0]["osisId"]


def put(kind, strong, surface, role, vlid, cluster):
    plan = [{"existing": None, "key": "k", "kind": kind, "text": f"test {kind} {surface}", "basis": "stated",
             "nodes": [{"strong": strong, "cluster": cluster, "role": role, "question": None, "traced": None, "at": "t",
                        "verse_reference": osis, "surface": surface, "morph_code": None, "verse_lexical_id": vlid}]}]
    orec.write(conn, plan, None, "TEST-2312")
    conn.commit()


put("face", uniq["strong"], uniq["surface"], "characteristic", None, cl)
s = next(x for x in rd.surfaces_state(cfg, conn, vid) if x["occurrence"] == uniq["occurrence"])
case("S5", "a node with no occurrence id but a unique verse+Strong+surface counts: face and role no longer missing",
     "face" not in s["missing"] and "role" not in s["missing"] and "term" in s["missing"], s["missing"])
# a node that names the Strong only, where the Strong occurs twice in the verse, is set aside
dup = q("""SELECT strong FROM verse_lexical WHERE verse_id=? AND deleted=0 GROUP BY strong HAVING count(*)>1 LIMIT 1""", vid)
if dup:
    d = dup[0]["strong"]
    put("term", d, None, "standalone", None, orec.word_clusters(conn, d)[0])
    sd = [x for x in rd.surfaces_state(cfg, conn, vid) if x["strong"] == d]
    case("S6", "a node naming a Strong that occurs twice, with no surface, counts for neither occurrence",
         all("term" in x["missing"] for x in sd), [x["missing"] for x in sd])
else:
    case("S6", "no repeated Strong in this verse (the set-aside rule is read from the code, not run)", True)
# the occurrence-id route
put("silence", uniq["strong"], uniq["surface"], "standalone", uniq["occurrence"], cl)
s = next(x for x in rd.surfaces_state(cfg, conn, vid) if x["occurrence"] == uniq["occurrence"])
case("S7", "a silence finding on the occurrence stands in for face and term", s["missing"] == [], s["missing"])

# ── O: Open, the pull, Observe ────────────────────────────────────────────────────────────────────
LABEL, ESC = "t-surface", 2312
o = run("open", Label=LABEL, Escalation=str(ESC), Home="M18", Objective="surfaces of three verses with a desire word", Verse="; ".join(refs))
case("O1", "Open on three verses", o.condition == "ok", o.message[:400])
col = json.loads((S / "reading" / LABEL / f"{LABEL}-collation.json").read_text(encoding="utf-8"))
v0 = next(v for v in col["verses"] if v["verse_id"] == vid)
case("O2", "the scope JSON holds every surface occurrence with its clusters and subgroups",
     len(v0["surfaces"]) == q("SELECT count(*) c FROM verse_lexical WHERE verse_id=? AND deleted=0", vid)[0]["c"]
     and all({"occurrence", "surface", "strong", "clusters", "subgroups"} <= set(x) for x in v0["surfaces"]), v0["surfaces"][:2])
statuses = {o["status"] for v in col["verses"] for o in v["observations"]}
case("O3", "the scope JSON pulls every non-withdrawn observation, with nodes",
     "withdrawn" not in statuses and all("nodes" in o for v in col["verses"] for o in v["observations"]), statuses)
gapf = S / "reading" / LABEL / f"{LABEL}-gaps.json"
g = json.loads(gapf.read_text(encoding="utf-8"))
case("O4", "the pre-gap JSON has no read_in_files_only section", "read_in_files_only" not in g["sections"], list(g["sections"]))
for sec, sc in g["sections"].items():
    for it in sc["items"]:
        it["record"] = {"reason": f"test of #2312: {sec} is outside what this trial reads"}
gapf.write_text(json.dumps(g, ensure_ascii=False), encoding="utf-8")
o = run("gather", Label=LABEL)
case("O5", "Gather records the pre-gap items", o.condition == "ok" or "nothing" in o.message, o.message[:300])
o = run("check", Label=LABEL)
case("O6", "the pre gate passes", o.condition == "ok", o.message[:300])
o = run("observe", Label=LABEL)
case("O7", "Observe builds the observe JSON", o.condition == "ok", o.message[:300])
ob = json.loads((S / "reading" / LABEL / f"{LABEL}-observe.json").read_text(encoding="utf-8"))
ov = ob["verses"][0]
case("O8", "the observe JSON lists only the surfaces still missing something, the open items and the counts",
     "open_items" in ov and ov["surfaces_complete"] >= 1 and all(w["missing"] for w in ov["words"])
     and all("occurrence" in w and "subgroups" in w for w in ov["words"]), {k: ov[k] for k in ("surfaces_in_focus", "surfaces_complete")})
o = run("check", Label=LABEL)
n_gap = sum(len(v["words"]) for v in ob["verses"])
case("O9", f"the Observe gate refuses while {n_gap} surface(s) lack what is asked", o.condition == "refused" and "missing" in o.message, o.message[:300])
# fill one surface with a real finding through Record; the others get a reason
w0 = ov["words"][0]
ob["verses"][0]["words"][0]["record"] = None
ob["findings"] = [{"key": "f1", "kind": "face", "text": f"test face of {w0['surface']}", "meaning": "test", "basis": "stated",
                   "nodes": [{"verse": ov["verse"], "strong": w0["strong"], "surface": w0["surface"],
                              "cluster": w0["clusters"][0], "role": "characteristic"}]},
                  {"key": "f2", "kind": "term", "text": f"test term of {w0['surface']}", "meaning": "test", "basis": "stated",
                   "nodes": [{"verse": ov["verse"], "strong": w0["strong"], "surface": w0["surface"],
                              "cluster": w0["clusters"][0], "role": "characteristic"}]}]
(S / "reading" / LABEL / f"{LABEL}-observe.json").write_text(json.dumps(ob, ensure_ascii=False), encoding="utf-8")
o = run("record", Label=LABEL)
case("O10", "Record writes the face and term findings", o.condition == "ok", o.message[:400])
node = q("SELECT verse_lexical_id FROM ib_node WHERE observation_id IN (SELECT id FROM ib_observation WHERE run_id=?) ", "RUN-TEST-record")
case("O11", "the new nodes carry the surface occurrence id", node and all(n["verse_lexical_id"] == w0["occurrence"] for n in node), [tuple(n) for n in node])
o = run("observe", Label=LABEL)
ob2 = json.loads((S / "reading" / LABEL / f"{LABEL}-observe.json").read_text(encoding="utf-8"))
case("O12", "a second Observe no longer lists the surface just completed (only what is missing is asked)",
     o.condition == "ok" and all(w["occurrence"] != w0["occurrence"] for w in ob2["verses"][0]["words"]), o.message[:200])
for v in ob2["verses"]:
    for w in v["words"]:
        w["record"] = {"reason": "test of #2312: this surface is left unfilled in the trial reading"}
(S / "reading" / LABEL / f"{LABEL}-observe.json").write_text(json.dumps(ob2, ensure_ascii=False), encoding="utf-8")
o = run("check", Label=LABEL)
case("O13", "the Observe gate passes once every missing surface is filled or has a reason", o.condition == "ok", o.message[:400])
print("ALL PASS" if all(res) else f"FAILURES: {res.count(False)} of {len(res)}")
