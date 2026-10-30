"""temp_2320_analysis_phase_1_test_run.py -- escalation #2320 test plan, on a COPY of iba.db (never the live DB): Analysis_phase_1
(Open, Observe, Record, the Observe gate) to the specification outputs/escalation/2318-analysis-phase-1-specification-v5-20261030.md.
Usage: python iba/app/tools/temp_2320_analysis_phase_1_test_run.py <scratch dir>. Prints PASS/FAIL per case."""
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

S = pathlib.Path(sys.argv[1]) / "t2320run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
SNAPS = sorted((ROOT / "iba/app/db/snapshots").glob("iba-*pre-2320-analysis-phase-1.db"))
SOURCE = SNAPS[-1] if SNAPS else ROOT / "iba/app/db/iba.db"       # the database before the migration, else the live one (copied)
DB = copy_db(S / "iba.db", SOURCE)
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
mig = ROOT / "iba/app/migration/analysis_phase_1_2320_v1_20261027.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(mig), "--db", str(DB), *a],
                                                                 capture_output=True, text=True, env=env))
      for a in (["--dry-run"], [], [])]
v2 = ROOT / "iba/app/migration/analysis_phase_1_2320_v2_20261027.py"
v2 = v2 if v2.exists() else ROOT / "iba/app/migration/archive" / v2.name
subprocess.run([sys.executable, str(v2), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v3 = ROOT / "iba/app/migration/analysis_phase_1_2323_v1_20261027.py"
v3 = v3 if v3.exists() else ROOT / "iba/app/migration/archive" / v3.name
subprocess.run([sys.executable, str(v3), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
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
v9 = ROOT / "iba/app/migration/analysis_phase_1_2329_v1_20261030.py"      # #2329: before, after, typed party, meaning on the sheet
v9 = v9 if v9.exists() else ROOT / "iba/app/migration/archive" / v9.name
subprocess.run([sys.executable, str(v9), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
v10 = ROOT / "iba/app/migration/analysis_phase_1_2329_v3_20261030.py"      # #2329: the nine observation items
v10 = v10 if v10.exists() else ROOT / "iba/app/migration/archive" / v10.name
subprocess.run([sys.executable, str(v10), "--db", str(DB)], capture_output=True, text=True, env=env, check=True)
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


def counts():
    return tuple(q(f"SELECT count(*) FROM {t}")[0][0] for t in ("ib_observation", "ib_node", "ib_observation_change"))


def idx(label):
    return json.loads((S / "reading" / label / f"{label}.json").read_text(encoding="utf-8"))


def save(label, data):
    for v_ in data.get("verses", []):
        if v_.get("sheet"):
            fixkinds(v_["sheet"])
    (S / "reading" / label / f"{label}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

PARTS_FULL = {"item": "circumstance"}


def fixrules(sh):
    """The reading's part of the rules for stating an observation (spec 4.1, 4.2, RS-10; #2329 v3): what covers a relevant surface is one of
    the nine items; every characteristic has its meaning observation and each other item observed or stated absent; the verse has an
    operation; the bears-on-only observations are deleted. Rebuilt on every call (the findings it adds have the key prefix cx_)."""
    REL = {"characteristic", "qualifier"}
    routes = sorted(cfg.enum("observation_route"))
    sh["findings"] = [f for f in sh.get("findings") or [] if not str(f.get("key", "")).startswith("cx_")]
    occ_g = {i: g for g in sh["surfaces"] for i in g["occurrences"]}
    cover, chars, ops, anyc = {}, {}, [], []

    def mark(g, item):
        if (g.get("evaluation") or {}).get("result") != "relevant":
            return                       # a surface without an inner-being role keeps no node (drop_non_relevant_nodes)
        chars[id(g)] = g
        cover.setdefault(id(g), set()).add(item)
    for e in sh["existing"]:
        a = e.get("action")
        if not a or a["action"] not in ("accept", "modify"):
            continue
        eff = {}
        for n in e["nodes"]:                  # a node's role after the actions the test gives it
            na_ = next((x for x in (a.get("nodes") or []) if x.get("node") == n["node"]), None)
            if na_ and na_.get("action") == "delete":
                continue
            eff[n["node"]] = (na_.get("set") or {}).get("role", n["role"]) if na_ and na_.get("action") == "modify" else n["role"]
        roles = [r_ for r_ in eff.values() if r_]
        if roles and not (set(roles) & REL) and a["action"] == "accept" and not a.get("nodes"):
            e["action"] = {"action": "delete", "reason": "test: every node bears on an act, none is its characteristic"}
        elif roles and not set(roles) <= {"object", "relational_target", "enactment"}:      # it covers (a standalone node covers too)
            st = dict(a.get("set") or {})
            kind = st.get("tag", e["kind"])
            item = {"party": "party", "link": "chain"}.get(kind, "circumstance")
            if kind in ("face", "use", "term", "qualification", "silence"):
                st["tag"], kind = "statement", "statement"
            st["basis"] = "stated"
            if kind == "party" and not e["route"]:
                st["route"] = routes[0]
            st["parts"] = {"item": item}
            e["action"] = dict(a, action="modify", reason=a.get("reason") or "test: the observation is one of the nine items", set=st)
            for n in e["nodes"]:
                g = occ_g.get(n["counts_for"])
                if g is not None and n["node"] in eff:
                    anyc.append((item, g))
                    if eff[n["node"]] == "characteristic":
                        mark(g, item)
    for f in sh["findings"]:
        p = f.get("parts") or {}
        if "item" not in p:
            f["kind"], f["parts"] = "statement", {"item": "polarity", "polarity": p.get("polarity", "pursuit")}
        for nd in f.get("nodes") or []:
            g = occ_g.get(nd.get("occurrence"))
            if g is not None:
                anyc.append((f["parts"]["item"], g))
                if nd.get("role") == "characteristic":
                    mark(g, f["parts"]["item"])
        if f["parts"]["item"] == "operation":
            ops.append(f)
    for item_, g_ in anyc:                 # an observation with a node of any role on a characteristic covers its item for it
        if id(g_) in chars:
            cover[id(g_)].add(item_)
    first = None
    for g in list(chars.values()):
        first = first or g
        cl = orec.word_clusters(conn, g["strong"])
        nd = {"strong": g["strong"], "occurrence": g["occurrences"][0], "role": "characteristic", "cluster": cl[0] if cl else "T12"}
        if "meaning" not in cover[id(g)]:
            sh["findings"].append({"key": f"cx_m{g['occurrences'][0]}", "kind": "face", "basis": "stated", "parts": {"item": "meaning"},
                                   "text": f"test meaning of {g['word']} in {sh['verse']}", "nodes": [dict(nd)]})
            cover[id(g)].add("meaning")
    if first is not None and not ops:
        cl = orec.word_clusters(conn, first["strong"])
        sh["findings"].append({"key": "cx_op", "kind": "statement", "basis": "stated", "parts": {"item": "operation", "mode": "done"},
                               "text": f"test operation of {first['word']} in {sh['verse']}",
                               "nodes": [{"strong": first["strong"], "occurrence": first["occurrences"][0], "role": "characteristic",
                                          "cluster": cl[0] if cl else "T12"}]})
        cover[id(first)].add("operation")
    for g in sh["surfaces"]:
        g["items_absent"] = ({k: "test: the verse shows none for this word" for k in orec.item_keys(cfg) if k not in cover[id(g)]}
                             if id(g) in chars else {})


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


# ── M: the migration ────────────────────────────────────────────────────────────────────────────────
FRESH = not mo[0].startswith("already applied")       # False when the source database already holds the migration
case("M1", "dry run writes nothing; apply writes; a second run is refused (when the source already holds the migration: every "
     "run is refused as already applied)",
     (mo[0].startswith("DRY RUN") and "write(s) applied" in mo[1] if FRESH else mo[0].startswith("already applied"))
     and mo[2].startswith("already applied"), mo)
roles = orec.node_role_groups(cfg)
case("M2", "node roles by result; standalone is not a role of a new node; the parts column exists; gather is retired",
     roles == {"relevant": ["characteristic", "qualifier"], "bears_on": ["object", "relational_target", "enactment"]}
     and "standalone" not in orec.node_roles(cfg)
     and "parts" in [r[1] for r in q("PRAGMA table_info(ib_observation)")] and cfg.step_inactive("reading", "reading.gather"),
     (roles,))
case("M3", "the rules are restated and the new ones are in; the write grant is live",
     len(q("SELECT 1 FROM cfg_method_rule WHERE rule_key LIKE 'RS-0%' AND active=1 AND step IN ('reading.observe','reading.open')")) >= 6
     and q("SELECT inactive FROM cfg_write_grant WHERE writer='reading.record' AND table_name='reading_strand_hit'")[0][0] == 0)

case("M4", "the deleted columns exist on both tables and were backfilled: no withdrawn status or disposition left with deleted=0",
     "deleted" in [r[1] for r in q("PRAGMA table_info(ib_observation)")] and "deleted" in [r[1] for r in q("PRAGMA table_info(ib_node)")]
     and q("SELECT count(*) FROM ib_observation WHERE status='withdrawn' AND deleted=0")[0][0] == 0
     and q("SELECT count(*) FROM ib_node WHERE disposition='withdrawn' AND deleted=0")[0][0] == 0
     and q("SELECT count(*) FROM ib_observation WHERE deleted=1")[0][0] == q("SELECT count(*) FROM ib_observation WHERE status='withdrawn'")[0][0])

# ── O: Open ─────────────────────────────────────────────────────────────────────────────────────────
base = dict(Label="t2320-a", Escalation="2320", Objective="the asking words in their verses (test)", Subgroup="M21_asking",
            Verse="Mat 7:8; Job 42:4; Gen 43:27")
before = counts()
rn = len(q("SELECT 1 FROM reading"))
cases = [("O1", "no subgroup is refused", dict(base, Subgroup=None)),
         ("O2", "two subgroups are refused", dict(base, Subgroup="M21_asking,M21_receiving")),
         ("O3", "-Home is refused", dict(base, Home="M21")),
         ("O4", "another selector is refused", dict(base, Strong="H7592")),
         ("O5", "an unknown subgroup is refused", dict(base, Subgroup="M99_nothing")),
         ("O6", "a bad label is refused", dict(base, Label="Bad Label"))]
qual = q("SELECT subgroup_code FROM cluster_subgroup WHERE kind='qualifier' AND coalesce(delete_flagged,0)=0 LIMIT 1")
if qual:
    cases.append(("O8", "a qualifier group is refused", dict(base, Subgroup=qual[0][0])))
for cid, desc, params in cases:
    r = run("open", **params)
    case(cid, desc, r.condition == "refused", (r.condition, r.message))
case("O9", "every refusal wrote nothing", counts() == before and len(q("SELECT 1 FROM reading")) == rn)
c2 = sqlite3.connect(DB)
c2.execute("UPDATE escalation SET state='withdraw' WHERE id=2301")
c2.commit()
c2.close()
r = run("open", **dict(base, Escalation="2301"))
case("O10", "an escalation at state 'withdraw' is refused (the terminal states come from cfg_enum)",
     r.condition == "refused" and "not an open task or issue" in r.message, r.message)

r = run("open", **base)
case("O11", "Open on one subgroup segmented by -Verse succeeds", r.condition == "ok", r.message)
d = idx("t2320-a")
case("O12", "the JSON indexes the three verses, all waiting, with their routes; no surfaces or observations are copied",
     len(d["verses"]) == 3 and all(v["status"] == "waiting" and v["routes"] for v in d["verses"])
     and all("sheet" not in v for v in d["verses"]), [v["verse"] for v in d["verses"]])
case("O13", "Open wrote the reading (state open, home M21) and no observation or node", counts() == before
     and tuple(q("SELECT state, home_cluster FROM reading WHERE label='t2320-a'")[0]) == ("open", "M21"))
case("O14", "a second Open on the same label is refused", run("open", **base).condition == "refused")
r = run("open", **dict(base, Label="t2320-b", Verse=None, Surface="asked"))
dd = idx("t2320-b") if r.condition == "ok" else {"verses": []}
case("O15", "a segment by -Surface keeps only verses where the subgroup's surface stands", r.condition == "ok" and len(dd["verses"]) > 0, r.message)

# a synthetic existing node on the second verse: no occurrence id, no subgroup (to test fill_nodes)
d0 = idx("t2320-a")
sv = d0["verses"][1]
cand = None
for r_ in q("SELECT id, strong, surface, morph_code FROM verse_lexical WHERE verse_id=? AND deleted=0 AND strong IN "
            "(SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code='M21') ORDER BY position", sv["verse_id"]):
    same = q("SELECT 1 FROM verse_lexical WHERE verse_id=? AND deleted=0 AND strong=? AND lower(trim(surface))=lower(trim(?))",
             sv["verse_id"], r_["strong"], r_["surface"])
    if len(same) == 1 and orec.subgroup_code(conn, "M21", r_["strong"], r_["surface"]):
        cand = r_
        break
SYN = None
if cand:
    c4 = sqlite3.connect(DB)
    oid_ = c4.execute("INSERT INTO ib_observation (stage, tag, obs_text, basis, status, created_at) VALUES "
                      "('prior-capture','statement','synthetic existing observation for the fill test','stated','draft',"
                      "'2026-10-27T00:00:00Z')").lastrowid
    SYN = c4.execute("INSERT INTO ib_node (observation_id, cluster_code, strong, verse_reference, surface, source_stage, seq, "
                     "role, created_at) VALUES (?, 'M21', ?, ?, ?, 'prior-capture', 1, 'characteristic', '2026-10-27T00:00:00Z')",
                     (oid_, cand["strong"], sv["osis"], cand["surface"])).lastrowid
    c4.commit()
    c4.close()

# ── S: Observe ──────────────────────────────────────────────────────────────────────────────────────
r = run("observe", Label="t2320-a", Count="2")
d = idx("t2320-a")
hand = [v for v in d["verses"] if v["status"] == "in_hand"]
case("S1", "Observe puts two verses in hand with a sheet each", r.condition == "ok" and len(hand) == 2 and all(v["sheet"] for v in hand), r.message)
v0 = hand[0]
rows = q("SELECT strong, lower(trim(surface)) s FROM verse_lexical WHERE verse_id=? AND deleted=0", v0["verse_id"])
case("S2", "the sheet holds every surface of the verse once per (Strong, surface), not only the subgroup's",
     len(v0["sheet"]["surfaces"]) == len({(x["strong"], x["s"]) for x in rows})
     and sum(len(g["occurrences"]) for g in v0["sheet"]["surfaces"]) == len(rows), (len(v0["sheet"]["surfaces"]), len(rows)))
ex = {e["observation"] for e in v0["sheet"]["existing"]}
real = {r[0] for r in q("SELECT DISTINCT o.id FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 "
                        "AND n.verse_reference=? AND n.deleted=0", v0["osis"])}
case("S3", "the sheet lists every live observation with a live node on the verse (the query by verse)", ex == real, (len(ex), len(real)))
case("S4", "the sheet carries the text, the passage and the instructions", bool(v0["sheet"]["text"]) and len(v0["sheet"]["passage"]) >= 1
     and "evaluation" in v0["sheet"]["how"])
v0["sheet"]["surfaces"][0]["evaluation"] = {"result": "relevant", "reason": "kept to see that Observe does not rebuild it"}
save("t2320-a", d)
r2 = run("observe", Label="t2320-a", Count="3")
d2 = idx("t2320-a")
case("S5", "a second Observe tops up to three and does not rebuild a sheet in hand",
     len([v for v in d2["verses"] if v["status"] == "in_hand"]) == 3
     and d2["verses"][0]["sheet"]["surfaces"][0]["evaluation"] is not None, r2.message)

# ── R: Record ───────────────────────────────────────────────────────────────────────────────────────
d = idx("t2320-a")
for v in d["verses"]:
    for g in v["sheet"]["surfaces"]:
        g["evaluation"] = None
save("t2320-a", d)
before = counts()
r = run("record", Label="t2320-a")
case("R1", "unfilled sheets are refused: nothing to record", r.condition == "refused", r.message)
v = d["verses"][0]
for g in v["sheet"]["surfaces"][:-1]:
    g["evaluation"] = {"result": "not_relevant", "reason": "grammar in this verse (test evaluation)"}
save("t2320-a", d)
r = run("record", Label="t2320-a")
case("R2", "a surface without an evaluation is refused whole, and nothing is written", r.condition == "refused" and counts() == before, r.message)


def fill_verse(v, mark_rel=1, mark_bear=1):
    """Evaluate every surface: the first M-coded surface(s) relevant, then bears_on, the rest not_relevant; one finding covers them."""
    sh = v["sheet"]
    gs = sh["surfaces"]
    rel = [g for g in gs if "M-coded" in g["hint"]][:mark_rel] or gs[:mark_rel]
    bear = [g for g in gs if g not in rel and "grammar by its morph" not in g["hint"]][:mark_bear]
    for g in gs:
        res = "relevant" if g in rel else "bears_on" if g in bear else "not_relevant"
        g["evaluation"] = {"result": res, "reason": f"{res} in {v['verse']} (test evaluation)"}
    nodes = []
    for g, role in [(g, "characteristic") for g in rel] + [(g, "object") for g in bear]:
        cl = orec.word_clusters(conn, g["strong"])
        nodes.append({"strong": g["strong"], "occurrence": g["occurrences"][0], "role": role, "cluster": cl[0] if cl else "T12"})
    sh["findings"] = [{"key": "f1", "kind": "statement", "text": f"test finding on {v['verse']} {rel[0]['word']}",
                       "basis": "stated", "nodes": nodes,
                       "parts": {"item": "polarity", "polarity": "pursuit"}}]
    sh["drop_non_relevant_nodes"] = True
    for e in sh["existing"]:
        e["action"] = {"action": "accept"}
    return rel, bear


fill_verse(d["verses"][0])
if d["verses"][0]["sheet"]["existing"]:
    d["verses"][0]["sheet"]["existing"][0]["action"] = None
    save("t2320-a", d)
    r = run("record", Label="t2320-a")
    case("R3", "an existing observation without an action is refused, nothing written", r.condition == "refused" and counts() == before, r.message)
    d["verses"][0]["sheet"]["existing"][0]["action"] = {"action": "accept"}
else:
    case("R3", "(no existing observation on the first verse: covered by R13)", True)
d["verses"][0]["sheet"]["findings"][0]["parts"]["polarity"] = "sideways"
save("t2320-a", d)
r = run("record", Label="t2320-a")
case("R4", "a polarity outside refusal/pursuit is refused", r.condition == "refused" and counts() == before, r.message)
d["verses"][0]["sheet"]["findings"][0]["parts"]["polarity"] = "pursuit"
d["verses"][0]["sheet"]["findings"][0]["nodes"][0]["role"] = "standalone"
save("t2320-a", d)
r = run("record", Label="t2320-a")
case("R5", "the role standalone is refused for a new node", r.condition == "refused" and counts() == before, r.message)
d["verses"][0]["sheet"]["findings"][0]["nodes"][0]["role"] = "characteristic"
saved_nodes = d["verses"][0]["sheet"]["findings"][0]["nodes"]
cov = {n["counts_for"] for e in d["verses"][0]["sheet"]["existing"] for n in e["nodes"] if n["counts_for"]}
unc = next((g for g in d["verses"][0]["sheet"]["surfaces"] if g["evaluation"]["result"] == "not_relevant"
            and "grammar by its morph" not in g["hint"] and not (set(g["occurrences"]) & cov)), None)
if unc:
    unc["evaluation"] = {"result": "relevant", "reason": "made relevant to test the coverage (test evaluation)"}
    save("t2320-a", d)
    r = run("record", Label="t2320-a")
    case("R6", "a relevant surface that no live node names is refused", r.condition == "refused" and counts() == before
         and "no live node" in r.message, r.message)
    unc["evaluation"] = {"result": "not_relevant", "reason": "grammar in this verse (test evaluation)"}
else:
    case("R6", "(every candidate surface already has an existing node on this verse)", True)
nr_g = next((g for g in d["verses"][0]["sheet"]["surfaces"] if g["evaluation"]["result"] == "not_relevant"
             and "grammar by its morph" not in g["hint"]), None)
if nr_g:
    extra = {"strong": nr_g["strong"], "occurrence": nr_g["occurrences"][0], "role": "object"}
    cl = orec.word_clusters(conn, nr_g["strong"])
    extra["cluster"] = cl[0] if cl else "T12"
    d["verses"][0]["sheet"]["findings"][0]["nodes"] = saved_nodes + [extra]
    save("t2320-a", d)
    r = run("record", Label="t2320-a")
    case("R7", "a new node on a surface evaluated not_relevant is refused", r.condition == "refused" and counts() == before, r.message)
    d["verses"][0]["sheet"]["findings"][0]["nodes"] = saved_nodes
save("t2320-a", d)
r = run("record", Label="t2320-a")
case("R8", "a fully filled verse is recorded (the other two, unfilled, stay in hand)", r.condition == "ok", r.message)
d = idx("t2320-a")
v0 = d["verses"][0]
case("R9", "the verse is done, its sheet is gone and its evaluations are kept in the JSON",
     v0["status"] == "done" and "sheet" not in v0 and v0["result"]["surfaces"] and all("result" in s for s in v0["result"]["surfaces"]), v0.get("status"))
obs = q("SELECT * FROM ib_observation WHERE obs_text LIKE 'test finding on %' ")
case("R10", "the new finding holds its parts (the item and its polarity) in the observation, not the node",
     len(obs) == 1 and json.loads(obs[0]["parts"]) == {"item": "polarity", "polarity": "pursuit"}, [o["parts"] for o in obs])
nodes = q("SELECT * FROM ib_node WHERE observation_id=?", obs[0]["id"])
case("R11", "its nodes name the occurrence, carry the reading and a role of the right group, and the subgroup where the word has one",
     len(nodes) >= 1 and all(n["verse_lexical_id"] for n in nodes) and all(n["reading_id"] for n in nodes)
     and {n["role"] for n in nodes} <= {"characteristic", "object"}
     and all(n["cluster_subgroup_code"] == orec.subgroup_code(conn, n["cluster_code"], n["strong"], n["surface"]) for n in nodes),
     [(n["role"], n["cluster_subgroup_code"]) for n in nodes])
case("R12", "the other verses in hand were untouched (still in hand with their sheets)",
     [v["status"] for v in d["verses"][1:]] == ["in_hand", "in_hand"] and all(v.get("sheet") for v in d["verses"][1:]))

w1 = d["verses"][1]
sh = w1["sheet"]
case("R13", "the second verse has existing observations to check (the trial rows of the earlier test)", len(sh["existing"]) > 0, len(sh["existing"]))
fill_verse(w1, mark_rel=1, mark_bear=0)
ex = sh["existing"]
if SYN:
    for g_ in sh["surfaces"]:
        if cand and g_["strong"] == cand["strong"] and cand["id"] in g_["occurrences"]:
            g_["evaluation"] = {"result": "relevant", "reason": "relevant: the synthetic node's surface (test evaluation)"}
target = ex[0]
o_before = q("SELECT obs_text, meaning FROM ib_observation WHERE id=?", target["observation"])[0]
nm = target["nodes"][0]
n_before = q("SELECT verse_lexical_id, cluster_subgroup_code, role FROM ib_node WHERE id=?", nm["node"])[0]
target["action"] = {"action": "modify", "reason": "test: wording corrected after reading the verse",
                    "set": {"meaning": "test corrected meaning in this verse", "tag": "statement",
                            "parts": dict(PARTS_FULL)},
                    "nodes": [{"node": nm["node"], "action": "modify", "reason": "test: subgroup completed",
                               "set": {"cluster_subgroup_code": "M21_asking"}}]}
if len(ex) > 1:
    ex[1]["action"] = {"action": "delete", "reason": "test: the verse does not support this observation"}
if len(ex) > 2:
    ex[2]["action"] = {"action": "accept", "nodes": [{"node": ex[2]["nodes"][0]["node"], "action": "delete",
                                                      "reason": "test: this node does not belong on the verse"}]}
sh["fill_nodes"] = True
save("t2320-a", d)
r = run("record", Label="t2320-a")
case("R14", "accept, modify, delete and node actions are recorded", r.condition == "ok", r.message)
o_after = q("SELECT obs_text, meaning FROM ib_observation WHERE id=?", target["observation"])[0]
ch = [tuple(x) for x in q("SELECT column_name, old_value, new_value, reason FROM ib_observation_change WHERE observation_id=? AND node_id IS NULL", target["observation"])]
case("R15", "a modify changes the observation IN PLACE and keeps old value, new value and reason in the change table",
     o_after["meaning"] == "test corrected meaning in this verse" and o_after["obs_text"] == o_before["obs_text"]
     and any(x[0] == "meaning" and x[1] == o_before["meaning"] and x[2] == "test corrected meaning in this verse"
             and "wording corrected" in x[3] for x in ch), ch)
case("R16", "no second observation was created by the modify",
     q("SELECT count(*) FROM ib_observation WHERE obs_text=?", o_before["obs_text"])[0][0] == 1)
nchg = q("SELECT column_name, new_value FROM ib_observation_change WHERE node_id=?", nm["node"])
case("R17", "a node modify is logged (or the node already held the value)", any(x[0] == "cluster_subgroup_code" for x in nchg)
     or n_before["cluster_subgroup_code"] == "M21_asking", [tuple(x) for x in nchg])
if len(ex) > 1:
    case("R18", "a delete withdraws the observation with its reason; nothing is deleted",
         tuple(q("SELECT status, deleted FROM ib_observation WHERE id=?", ex[1]["observation"])[0]) == ("withdrawn", 1)
         and q("SELECT count(*) FROM ib_observation_change WHERE observation_id=? AND column_name='deleted'", ex[1]["observation"])[0][0] == 1)
if len(ex) > 2:
    case("R19", "a node delete sets the node's deleted column with its reason and leaves its disposition alone",
         tuple(q("SELECT deleted, disposition FROM ib_node WHERE id=?", ex[2]["nodes"][0]["node"])[0]) == (1, None)
         and q("SELECT count(*) FROM ib_observation_change WHERE node_id=? AND column_name='deleted' AND new_value='1'",
               ex[2]["nodes"][0]["node"])[0][0] == 1)
syn_entry = next((n for e in ex for n in e["nodes"] if n["node"] == SYN), None) if SYN else None
if syn_entry:
    row = q("SELECT verse_lexical_id, cluster_subgroup_code FROM ib_node WHERE id=?", SYN)[0]
    case("R20", "fill_nodes completes a node that lacked its occurrence and subgroup (#2308 D2)",
         syn_entry["suggest"] and all(row[k] == v for k, v in syn_entry["suggest"].items()) and row["verse_lexical_id"],
         (syn_entry["suggest"], tuple(row)))
else:
    case("R20", "(no synthetic node could be set up on this verse)", False)
case("R21", "drop_non_relevant_nodes withdrew the nodes on not_relevant surfaces: no live node names a not_relevant surface",
     not any(q("SELECT n.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 WHERE n.verse_lexical_id IN (%s) "
               "AND n.deleted=0" % ",".join(str(i) for i in g["occurrences"]))
             for g in sh["surfaces"] if g["evaluation"]["result"] == "not_relevant"))

# ── G: the third verse, then the gate ───────────────────────────────────────────────────────────────
d = idx("t2320-a")
w2 = d["verses"][2]
gr = rd.reading(conn, "t2320-a")
r = run("check", Label="t2320-a")
case("G1", "the Observe gate refuses while a verse is not done", r.condition == "refused" and "not done" in r.message, r.message)
fill_verse(w2, mark_rel=1, mark_bear=0)
save("t2320-a", d)
r = run("record", Label="t2320-a")
case("G2", "the last verse is recorded", r.condition == "ok", r.message)
d = idx("t2320-a")
case("G3", "all verses done; the JSON counts say so", d["counts"]["done"] == 3 and all(v["status"] == "done" for v in d["verses"]))
vv = d["verses"][0]
nr_s = next(s for s in vv["result"]["surfaces"] if s["result"] == "not_relevant")
obs_id = q("SELECT id FROM ib_observation WHERE obs_text LIKE 'test finding on %' LIMIT 1")[0][0]
st = q("SELECT strong, surface FROM verse_lexical WHERE id=?", nr_s["occurrences"][0])[0]
c3 = sqlite3.connect(DB)
c3.execute("INSERT INTO ib_node (observation_id, cluster_code, strong, verse_reference, surface, source_stage, seq, role, reading_id, "
           "verse_lexical_id, created_at) VALUES (?,'T12',?,?,?, 'reading', 99, 'object', ?, ?, '2026-10-27T00:00:00Z')",
           (obs_id, st["strong"], vv["osis"], st["surface"], gr["id"], nr_s["occurrences"][0]))
c3.commit()
nid_t = c3.execute("SELECT max(id) FROM ib_node").fetchone()[0]
c3.close()
r = run("check", Label="t2320-a")
case("G4", "the gate refuses when a live node names a surface evaluated not_relevant (checked from the tables)",
     r.condition == "refused" and "no inner-being role" in r.message, r.message)
c3 = sqlite3.connect(DB)
c3.execute("DELETE FROM ib_node WHERE id=?", (nid_t,))
c3.commit()
c3.close()
r = run("check", Label="t2320-a")
case("G5", "the gate passes: open -> observed", r.condition == "ok" and rd.reading(conn, "t2320-a")["state"] == "observed", r.message)
case("G6", "the verses are marked analysed (verse_meta)",
     q("SELECT count(*) FROM verse_meta WHERE verse_id IN (SELECT verse_id FROM reading_verse WHERE reading_id=?) AND status IN ('analysed','citated')", gr["id"])[0][0] >= 1)

# ── X: the rest ─────────────────────────────────────────────────────────────────────────────────────
case("X1", "Gather is retired: the dispatcher's step gate refuses it", cfg.step_inactive("reading", "reading.gather"))
try:
    lines, msg = rd.account(cfg, {"Label": "t2320-b"}, ROOT)
    case("X2", "Account still renders for a reading at state open, with the Observe gate's gaps", bool(lines) and "gap(s)" in msg, msg)
except Exception as exc:  # noqa: BLE001
    case("X2", "Account still renders for a reading at state open", False, repr(exc))
case("X3", "the claims steps still import and the later functions are present",
     all(hasattr(rd, n) for n in ("synergy", "apply", "narrate", "publish", "gate_post", "gate_narrate")))
case("X4", "the settings the new code names are live (reading.verse_loop, reading.node_roles, reading.observation_parts)",
     all(cfg.setting(k) is not None for k in ("reading.verse_loop", "reading.node_roles", "reading.observation_parts")))

print(f"\n{sum(res)} of {len(res)} cases pass")
sys.exit(0 if all(res) else 1)
