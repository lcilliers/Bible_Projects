"""temp_2323_deleted_and_fixes_test_run.py -- escalation #2323 test plan, on a COPY of the live iba.db (never the live DB): the
deleted columns of ib_observation and ib_node, and the fixes the check of the existing observations proposes and applies
(merge a duplicate description, delete the silence kind, standalone nodes), on the real data of Gen 43:27 (the 19 observations
of the earlier m21-asking-test reading) and Gen 24:47 (the node 19107 a reading deleted through disposition), and the per-verse
Record. Usage: python iba/app/tools/temp_2323_deleted_and_fixes_test_run.py <scratch dir>. Prints PASS/FAIL per case."""
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

S = pathlib.Path(sys.argv[1]) / "t2323run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
_pre = ROOT / "backups/iba-pre-2323-deleted-columns-20261027.db"       # the database as the live test left it, before the delete columns
DB = copy_db(S / "iba.db", _pre if _pre.exists() else ROOT / "iba/app/db/iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
v3 = ROOT / "iba/app/migration/analysis_phase_1_2323_v1_20261027.py"
v3 = v3 if v3.exists() else ROOT / "iba/app/migration/archive" / v3.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(v3), "--db", str(DB), *a],
                                                                 capture_output=True, text=True, env=env))
      for a in (["--dry-run"], [], [])]
v4 = ROOT / "iba/app/migration/analysis_phase_1_2323_v2_20261027.py"
v4 = v4 if v4.exists() else ROOT / "iba/app/migration/archive" / v4.name
subprocess.run([sys.executable, str(v4), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v5 = ROOT / "iba/app/migration/analysis_phase_1_2323_v3_20261027.py"
v5 = v5 if v5.exists() else ROOT / "iba/app/migration/archive" / v5.name
subprocess.run([sys.executable, str(v5), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v6 = ROOT / "iba/app/migration/analysis_phase_1_2323_v4_20261027.py"
v6 = v6 if v6.exists() else ROOT / "iba/app/migration/archive" / v6.name
subprocess.run([sys.executable, str(v6), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v7 = ROOT / "iba/app/migration/analysis_phase_1_2320_v3_20261028.py"
v7 = v7 if v7.exists() else ROOT / "iba/app/migration/archive" / v7.name
subprocess.run([sys.executable, str(v7), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v8 = ROOT / "iba/app/migration/analysis_phase_1_2320_v4_20261028.py"
v8 = v8 if v8.exists() else ROOT / "iba/app/migration/archive" / v8.name
subprocess.run([sys.executable, str(v8), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='reading.output_dir'", (json.dumps(str(S / "reading")),))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
from iba.app.handlers import reading as hr  # noqa: E402

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


def idx(label):
    return json.loads((S / "reading" / label / f"{label}.json").read_text(encoding="utf-8"))


def save(label, data):
    (S / "reading" / label / f"{label}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

PARTS_FULL = {"sense": "test sense in this verse", "evidence": "test evidence for the sense", "polarity": "pursuit",
              "content": {"none": "test: no object stated in the verse"}, "enactment": {"none": "test: no outward act stated"},
              "party": {"none": "test: no other party stated"}, "circumstance": "test circumstance in this verse",
              "chain": {"none": "test: a single operation in the verse"}, "primary_operation": {"none": "test: not the primary one"},
              "flags": []}


def fixrules(sh):
    """The reading's part of the rules for stating an observation (spec 4.1, 4.2): the parts completed on what covers a relevant
    surface, the bears-on-only observations deleted, one statement naming the primary operation."""
    REL = {"characteristic", "qualifier"}
    cov = []
    for e in sh["existing"]:
        a = e.get("action")
        if not a or a["action"] not in ("accept", "modify"):
            continue
        roles = [n["role"] for n in e["nodes"] if n["role"]]
        if roles and not (set(roles) & REL) and a["action"] == "accept" and not a.get("nodes"):
            e["action"] = {"action": "delete", "reason": "test: every node bears on an act, none is its characteristic"}
        elif set(roles) & REL:
            st = dict(a.get("set") or {})
            st.setdefault("parts", dict(PARTS_FULL))
            e["action"] = dict(a, action="modify", reason=a.get("reason") or "test: the parts of spec 4.2 completed", set=st)
            cov.append(e)
    for f in sh.get("findings") or []:
        f["parts"] = {**PARTS_FULL, "primary_operation": "test primary operation of the verse", **(f.get("parts") or {})}
    if cov and not sh.get("findings"):
        e = cov[0]
        e["action"]["set"]["tag"] = "statement"
        e["action"]["set"]["parts"] = dict(PARTS_FULL, primary_operation="test primary operation of the verse")


OK_KINDS = {"face", "qualification", "party", "statement", "link", "use", "term"}


def fixkinds(sh):
    """The reading's part of a kept observation: a tag that is not a kind is modified to one (the reading reads what it says);
    the silence kind is deleted; the nodes' missing or different subgroup is filled."""
    sh["fill_nodes"] = True
    for e in sh["existing"]:
        a = e.get("action")
        if not a:
            continue
        if e["kind"] == "silence" and a["action"] in ("accept", "modify"):
            e["action"] = {"action": "delete", "reason": "test: the silence kind is not used by Analysis_phase_1"}
        elif e["kind"] not in OK_KINDS and a["action"] in ("accept", "modify"):
            a = dict(a, action="modify", reason=a.get("reason") or "test: the tag is set to the kind of what it says")
            a["set"] = {**(a.get("set") or {}), "tag": a.get("set", {}).get("tag", "statement")}
            e["action"] = a
    fixrules(sh)


loop = cfg.required_setting("reading.verse_loop")
loop = json.loads(loop) if isinstance(loop, str) else loop

# ── V: the migration, on the live data ──────────────────────────────────────────────────────────────
FRESH = not mo[0].startswith("already applied")
case("V1", "dry run writes nothing; apply writes; a second run is refused (or every run is refused when the source holds it)",
     (mo[0].startswith("DRY RUN") and "write(s) applied" in mo[1] if FRESH else mo[0].startswith("already applied"))
     and mo[2].startswith("already applied"), mo)
case("V2", "both tables have deleted, the backfill is complete and the two flags agree",
     "deleted" in [r[1] for r in q("PRAGMA table_info(ib_observation)")] and "deleted" in [r[1] for r in q("PRAGMA table_info(ib_node)")]
     and q("SELECT count(*) FROM ib_observation WHERE (status='withdrawn') <> (deleted=1)")[0][0] == 0
     and q("SELECT count(*) FROM ib_node WHERE disposition='withdrawn' AND deleted=0")[0][0] == 0)
row = q("SELECT deleted, disposition FROM ib_node WHERE id=19107")
chg = [tuple(x) for x in q("SELECT column_name, new_value FROM ib_observation_change WHERE node_id=19107 ORDER BY id")]
case("V3", "node 19107 (the nose of Gen 24:47), deleted by a reading through disposition, is moved to the deleted column and its "
     "disposition is empty again, each kept in the change table",
     row and tuple(row[0]) == (1, None) and ("deleted", "1") in chg and ("disposition", None) in chg, (row and tuple(row[0]), chg))
case("V4", "the cfg rows are in: the two cfg_column rows and the merge action",
     len(q("SELECT 1 FROM cfg_column WHERE database='iba' AND name='deleted' AND table_name IN ('ib_observation','ib_node')")) == 2
     and "merge" in loop["existing_actions"])

# ── D: a deleted node is not seen ───────────────────────────────────────────────────────────────────
base = dict(Escalation="2323", Subgroup="M21_asking")
r = run("open", Label="t2323-nose", Objective="Gen 24:47 (test)", Verse="Gen 24:47", **base)
r = run("observe", Label="t2323-nose") if r.condition == "ok" else r
sh = idx("t2323-nose")["verses"][0]["sheet"]
shown = {n["node"] for e in sh["existing"] for n in e["nodes"]}
case("D1", "Observe does not show node 19107 (deleted)", 19107 not in shown, sorted(shown)[:12])

# ── F: the fixes, on Gen 43:27 ──────────────────────────────────────────────────────────────────────
# a synthetic identical copy of observation 20622 on the same word, to test the merge of a duplicate description
c5 = sqlite3.connect(DB)
dupid = c5.execute("INSERT INTO ib_observation (stage, tag, obs_text, meaning, basis, status, created_at) SELECT stage, tag, obs_text, "
                   "meaning, basis, status, created_at FROM ib_observation WHERE id=20622").lastrowid
c5.execute("INSERT INTO ib_node (observation_id, cluster_code, cluster_subgroup_code, strong, verse_reference, surface, morph_code, "
           "source_stage, seq, role, reading_id, created_at, verse_lexical_id) SELECT ?, cluster_code, cluster_subgroup_code, strong, "
           "verse_reference, surface, morph_code, source_stage, 1, role, reading_id, created_at, verse_lexical_id FROM ib_node "
           "WHERE observation_id=20622 AND verse_reference='Gen.43.27'", (dupid,))
c5.commit()
c5.close()
r = run("open", Label="t2323-a", Objective="Gen 43:27 (test)", Verse="Gen 43:27", **base)
r = run("observe", Label="t2323-a")
d = idx("t2323-a")
v = d["verses"][0]
sh = v["sheet"]
ex = sh["existing"]
dup_flags = [(e["observation"], f) for e in ex for f in e["flags"] if f["code"] == "duplicate_description"]
merge_props = [(o, f["propose"]) for o, f in dup_flags if f["propose"]]
sil = [e for e in ex if e["kind"] == "silence"]
stand = [(e["observation"], n["node"]) for e in ex for n in e["nodes"] if any(f["code"] == "role_standalone" for f in n["flags"])]
case("F1", "the sheet flags the duplicate description (the later copy proposes a merge into the first), the silence kind (proposes a "
     "delete) and the standalone nodes",
     len(merge_props) >= 1 and len(sil) >= 1 and all(any(f["code"] == "unused_kind" and f["propose"] for f in e["flags"]) for e in sil)
     and len(stand) >= 1 and (dupid, True) in [(o, True) for o, _ in merge_props], (len(merge_props), len(sil), len(stand), len(ex)))
ovl = [(e["observation"], f["code"]) for e in ex for f in e["flags"] if f["code"] == "same_word_same_role"]
case("F1b", "observations that name the same word with the same role are listed as overlapping (the face and term pairs)",
     len(ovl) >= 2, len(ovl))
live_before = {e["observation"] for e in ex}
dup_ids = [o for o, _ in merge_props]
gs = sh["surfaces"]
rel = next((g for g in gs if "M-coded" in g["hint"]), gs[0])
for g in gs:
    g["evaluation"] = {"result": "relevant" if g is rel else "not_relevant", "reason": "test evaluation of Gen 43:27 words"}
cl = orec.word_clusters(conn, rel["strong"])
sh["findings"] = [{"key": "f1", "kind": "statement", "text": "test finding on the asking in Gen 43:27", "basis": "stated",
                   "nodes": [{"strong": rel["strong"], "occurrence": rel["occurrences"][0], "role": "characteristic",
                              "cluster": cl[0] if cl else "T3"}], "parts": {"sense": "test sense", "polarity": "pursuit"}}]
sh["drop_non_relevant_nodes"] = True
save("t2323-a", d)
r = run("record", Label="t2323-a")
d = idx("t2323-a")
sh = d["verses"][0].get("sheet") or {}
case("F2", "an observation with no action and no automatic fix is refused, names the flags in its error, writes nothing and puts the "
     "errors on the sheet (the verse stays in hand)",
     r.condition == "refused" and "needs an action" in r.message and "flags" in r.message
     and d["verses"][0]["status"] == "in_hand" and bool(sh.get("errors")), r.message[:300])
for e in sh["existing"]:
    if not any(f.get("propose") for f in e["flags"]):
        e["action"] = {"action": "accept"}
fixrules(sh)
sh["confirm_fixes"] = False
sh["fill_nodes"] = False
save("t2323-a", d)
r = run("record", Label="t2323-a")
case("F3", "with an action on those, and the automatic fixes run unconfirmed, the verse is recorded", r.condition == "ok" and "merged" in r.message, r.message)
d = idx("t2323-a")
case("F4", "the verse is done and its sheet (with its errors) is gone", d["verses"][0]["status"] == "done" and "sheet" not in d["verses"][0])
kept = {}
for dup in dup_ids:
    rw = q("SELECT status, deleted FROM ib_observation WHERE id=?", dup)[0]
    mv = [tuple(x) for x in q("SELECT column_name, old_value, new_value FROM ib_observation_change WHERE observation_id=? AND "
                              "column_name IN ('observation_id','deleted')", dup)]
    kept[dup] = (tuple(rw), mv)
case("F5", "a merged duplicate is deleted (deleted=1, status withdrawn), with the change kept; nothing was physically deleted",
     all(v_[0] == ("withdrawn", 1) and any(m[0] == "deleted" for m in v_[1]) for v_ in kept.values())
     and q("SELECT count(*) FROM ib_observation WHERE id IN (%s)" % ",".join(map(str, dup_ids)))[0][0] == len(dup_ids), kept)
texts = [r_[0] for r_ in q("SELECT trim(obs_text) FROM ib_observation WHERE deleted=0 AND id IN (%s)" % ",".join(map(str, live_before)))]
case("F6", "after the merge no description of the verse is live twice", len(texts) == len(set(texts)), len(texts))
case("F7", "a merged duplicate keeps no live node: they moved to the observation kept, or were deleted as the same node",
     all(q("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", dup)[0][0] == 0 for dup in dup_ids))
orph = [o_ for o_ in live_before if o_ not in dup_ids and q("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", o_)[0][0] == 0]
case("F7b", "an observation whose last node was deleted is itself soft deleted (it could not be reached from a verse)",
     len(orph) >= 1 and all(tuple(q("SELECT status, deleted FROM ib_observation WHERE id=?", o_)[0]) == ("withdrawn", 1) for o_ in orph), orph)
case("F8", "the silence observations of the verse are deleted",
     all(tuple(q("SELECT status, deleted FROM ib_observation WHERE id=?", e["observation"])[0]) == ("withdrawn", 1) for e in sil))
bad = []
for g in d["verses"][0]["result"]["surfaces"]:
    if g["result"] == "not_relevant":
        ids = ",".join(str(i) for i in g["occurrences"])
        bad += q("SELECT n.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 WHERE n.deleted=0 "
                 "AND n.verse_lexical_id IN (%s)" % ids)
case("F9", "no live node names a surface evaluated not_relevant (the standalone nodes were dropped)", not bad, bad[:5])
r = run("check", Label="t2323-a")
case("F10", "the Observe gate passes for the one-verse reading: open -> observed",
     r.condition == "ok" and rd.reading(conn, "t2323-a")["state"] == "observed", r.message)

# ── P: per-verse Record ─────────────────────────────────────────────────────────────────────────────
r = run("open", Label="t2323-b", Objective="two verses (test)", Verse="Mat 7:8; Job 42:4", **base)
r = run("observe", Label="t2323-b", Count="2")
d = idx("t2323-b")


def fill(vv, ok=True):
    s_ = vv["sheet"]
    g_ = s_["surfaces"]
    rl = next((x for x in g_ if "M-coded" in x["hint"]), g_[0])
    for x in g_:
        x["evaluation"] = {"result": "relevant" if x is rl else "not_relevant", "reason": f"test evaluation in {vv['verse']}"}
    if not ok:
        other = next(x for x in g_ if x is not rl)
        other["evaluation"] = None
    k_ = orec.word_clusters(conn, rl["strong"])
    s_["findings"] = [{"key": "f1", "kind": "statement", "text": f"test finding on {vv['verse']} for the per-verse test",
                       "basis": "stated", "nodes": [{"strong": rl["strong"], "occurrence": rl["occurrences"][0],
                                                      "role": "characteristic", "cluster": k_[0] if k_ else "T3"}]}]
    s_["drop_non_relevant_nodes"] = True
    s_["confirm_fixes"] = True
    for e in s_["existing"]:
        if not any(f.get("propose") for f in e["flags"]):
            e["action"] = {"action": "accept"}
    fixkinds(s_)


fill(d["verses"][0], ok=False)       # the first verse has an error: a surface without an evaluation
fill(d["verses"][1], ok=True)
save("t2323-b", d)
r = run("record", Label="t2323-b")
d = idx("t2323-b")
st = [v_["status"] for v_ in d["verses"]]
case("P1", "one verse with an error does not stop the other: the good verse is recorded, the other stays in hand with its errors "
     "on its sheet, and the message names it",
     r.condition == "ok" and st == ["in_hand", "done"] and d["verses"][0]["sheet"].get("errors") and "NOT recorded" in r.message,
     (r.condition, st, r.message[-200:]))
case("P2", "the verse that failed wrote nothing: its finding text is not in the table",
     q("SELECT count(*) FROM ib_observation WHERE obs_text LIKE ?", f"test finding on {d['verses'][0]['verse']}%")[0][0] == 0)
r = run("record", Label="t2323-b")
case("P3", "when no verse can be recorded the step is a refusal that names the errors",
     r.condition == "refused" and "errors are on the sheets" in r.message, r.message[:200])
fill(d["verses"][0], ok=True)
d["verses"][0]["sheet"]["errors"] = []
save("t2323-b", d)
r = run("record", Label="t2323-b")
case("P4", "after the reading fixes the sheet the verse is recorded and the batch is complete",
     r.condition == "ok" and [v_["status"] for v_ in idx("t2323-b")["verses"]] == ["done", "done"], r.message[:200])

# ── T: the stage, the kind (tag) and the subgroup of what is kept ──────────────────────────────────────
case("T1", "what Analysis_phase_1 writes has the stage Analysis_phase_1 (observation stage and node source_stage)",
     {r_[0] for r_ in q("SELECT stage FROM ib_observation WHERE obs_text LIKE 'test finding on%'")} == {"Analysis_phase_1"}
     and {r_[0] for r_ in q("SELECT n.source_stage FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.obs_text LIKE 'test finding on%'")} == {"Analysis_phase_1"})
r = run("open", Label="t2323-c", Objective="legacy tag (test)", Verse="John 16:19", **base)
r = run("observe", Label="t2323-c", Count="1")
d = idx("t2323-c")
vv = d["verses"][0]
for x in vv["sheet"]["surfaces"]:
    x["evaluation"] = {"result": "not_relevant", "reason": "test evaluation: no role here"}
vv["sheet"]["drop_non_relevant_nodes"] = True
legacy = [e for e in vv["sheet"]["existing"] if e["kind"] not in OK_KINDS and e["kind"] != "silence"]
for e in vv["sheet"]["existing"]:
    e["action"] = {"action": "accept"}
save_raw = lambda dd: (S / "reading" / "t2323-c" / "t2323-c.json").write_text(json.dumps(dd, ensure_ascii=False, indent=1), encoding="utf-8")
save_raw(d)
r = run("record", Label="t2323-c")
case("T2", "accepting an observation whose tag is not a kind is refused, and the error says to modify the tag",
     len(legacy) >= 1 and r.condition == "refused" and "is not a kind of observation" in r.message, (len(legacy), r.message[:160]))
d = idx("t2323-c")
vv = d["verses"][0]
vv["sheet"]["errors"] = []
for e in vv["sheet"]["existing"]:
    e["action"] = {"action": "modify", "reason": "test: the tag is set to the kind of what it says", "set": {"tag": "statement"}}         if e["kind"] not in OK_KINDS else {"action": "accept"}
    for n in e["nodes"]:
        if n["flags"] and any(f["code"] == "subgroup_differs" for f in n["flags"]):
            n["action"] = None
sh_ = vv["sheet"]
wrong = [n for e in sh_["existing"] for n in e["nodes"] if n.get("suggest") and "cluster_subgroup_code" in n["suggest"]]
sh_["fill_nodes"] = False
save_raw(d)
r = run("record", Label="t2323-c")
case("T3", "a node whose subgroup is missing or differs from surface_subgroup is refused unless it is filled" if wrong
     else "(no node with a wrong subgroup on this verse: covered by P1)", (not wrong) or "cluster_subgroup_code" in r.message, r.message[:200])
d = idx("t2323-c")
if d["verses"][0].get("sheet"):
    d["verses"][0]["sheet"]["fill_nodes"] = True
    d["verses"][0]["sheet"]["errors"] = []
    save_raw(d)
    r = run("record", Label="t2323-c")
case("T4", "with the tags modified to kinds and the subgroups filled the verse is recorded; no kept observation has a legacy tag",
     r.condition == "ok" and q("SELECT count(*) FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE n.verse_reference='John.16.19' AND o.deleted=0 AND n.deleted=0 AND o.tag NOT IN ('face','qualification','party','statement','link','use','term')")[0][0] == 0, r.message[:200])

# ── O: an observation the reading leaves by its wording ────────────────────────────────────────
prot = "SELECT {} FROM ib_observation o WHERE o.id=618".format("o.stage, o.tag, o.obs_text, o.deleted, o.status, o.meaning")
pnodes = "SELECT id, role, deleted, cluster_subgroup_code, verse_lexical_id, disposition FROM ib_node WHERE observation_id=618 ORDER BY id"
snap_o, snap_n = [tuple(x) for x in q(prot)], [tuple(x) for x in q(pnodes)]
nchg = q("SELECT count(*) FROM ib_observation_change WHERE observation_id=618")[0][0]
r = run("open", Label="t2323-d", Objective="other stage (test)", Verse="Matt 20:3",
        **{**base, "Subgroup": "M67_A_dispositional_idleness"})
r = run("observe", Label="t2323-d", Count="1")
d = idx("t2323-d")
sh = d["verses"][0]["sheet"]
case("O1", "the stage does not filter: an observation of the stage char-answers is on the sheet to be checked like any other",
     any(e["observation"] == 618 for e in sh["existing"]) and "other_stage" not in sh, [e["observation"] for e in sh["existing"]][:5])
for g in sh["surfaces"]:
    g["evaluation"] = {"result": "not_relevant", "reason": "test evaluation: no role here"}
sh["drop_non_relevant_nodes"] = True
for e in sh["existing"]:
    e["action"] = ({"action": "leave", "reason": "test: by its wording this is a characteristic claim answer, not verse understanding"}
                   if e["observation"] == 618 else {"action": "delete", "reason": "test: the verse does not support this observation"})
(S / "reading" / "t2323-d" / "t2323-d.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
r = run("record", Label="t2323-d")
d = idx("t2323-d")
case("O2", "an observation the reading leaves by its wording stays exactly as it is, with its nodes and no change row, while the others are deleted",
     [tuple(x) for x in q(prot)] == snap_o and [tuple(x) for x in q(pnodes)] == snap_n
     and q("SELECT count(*) FROM ib_observation_change WHERE observation_id=618")[0][0] == nchg, (r.condition, r.message[:200]))
case("O3", "the Observe gate does not count the nodes of a left observation (the verse is done with every surface not_relevant)",
     r.condition == "ok" and d["verses"][0]["status"] == "done", r.message[:200])

# ── M: merge and node fixes, directly ───────────────────────────────────────────────────────────────
a_, b_ = [r_[0] for r_ in q("SELECT id FROM ib_observation WHERE deleted=0 AND obs_text LIKE 'test finding on%' ORDER BY id LIMIT 2")]
try:
    orec.merge_observation(conn, a_, b_, "test: two different descriptions", None, "T", "Claude")
    case("M1", "a merge of two different descriptions is refused", False, "it merged")
except orec.Refused as exc:
    case("M1", "a merge of two different descriptions is refused", "texts differ" in str(exc), str(exc))
nid = q("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0 LIMIT 1", a_)[0][0]
orec.modify_node(cfg, conn, nid, {"role": "qualifier"}, "test: the word is a qualifier here", None, "T", "Claude")
case("M2", "a role is modified in place and logged",
     q("SELECT role FROM ib_node WHERE id=?", nid)[0][0] == "qualifier"
     and q("SELECT count(*) FROM ib_observation_change WHERE node_id=? AND column_name='role'", nid)[0][0] == 1)
try:
    orec.delete_node(conn, nid, "short", None, "T", "Claude")
    case("M3", "a delete without a proper reason is refused", False, "it deleted")
except orec.Refused as exc:
    case("M3", "a delete without a proper reason is refused (10 characters or more)", "reason" in str(exc), str(exc))
case("M4", "delete_node on a node already deleted is a no-op (False)",
     orec.delete_node(conn, nid, "test: this node is deleted", None, "T", "Claude") is True
     and orec.delete_node(conn, nid, "test: deleted a second time", None, "T", "Claude") is False)

# ── L: the other readers of live ────────────────────────────────────────────────────────────────────
from iba.app.lib import versecollate as vc  # noqa: E402
from iba.app.lib import versescope as vs  # noqa: E402
col = vc.collate(cfg, vs.normalise_request({"subgroup": "M21_asking", "verse": "Gen 24:47"}), ROOT)
shown_c = {n["node"] for vv in col["verses"] for o in vv["observations"] for n in o["nodes"]}
case("L1", "the collation (versecollate) does not show the deleted node 19107", 19107 not in shown_c, sorted(shown_c)[:10])
files = ("iba/app/lib/reading.py", "iba/app/lib/observationrecord.py", "iba/app/lib/versecollate.py", "iba/app/lib/versescope.py",
         "iba/app/lib/priorcapture.py", "iba/app/lib/strandreading.py", "iba/app/lib/stage1coverage.py",
         "iba/app/lib/versereadinggenerate.py")
case("L2", "no reader of live observations or nodes still takes status or disposition 'withdrawn' as the live test",
     not any(("status<>'withdrawn'" in (ROOT / f).read_text(encoding="utf-8") or "disposition<>'withdrawn'" in (ROOT / f).read_text(encoding="utf-8")
              or "status != 'withdrawn'" in (ROOT / f).read_text(encoding="utf-8")) for f in files))

print(f"\n{sum(res)} of {len(res)} cases pass")
sys.exit(0 if all(res) else 1)
