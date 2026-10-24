"""temp_2273_reading_phases_test_run.py -- test plan for escalations #2273 (B1) and #2274 (B2), one change set
(design outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md sec 5). Run on a copy
of iba.db made with lib/dbsnapshot.copy_db with the migration applied to the copy; the narrative folder, the
learning4comfort inbox and the output folders are redirected to the scratch directory. Expected values by plain SQL
on the copy. The trial reading is three verses (RG-19), one with a qualifier: Jon 1:10 "exceedingly afraid".

Usage: python iba/app/tools/temp_2273_reading_phases_test_run.py <scratch dir> [<source db>]
       (the source defaults to the live iba.db; once the migration is live, give the pre-run snapshot so the
       migration is tested from scratch)
"""
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
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2273"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", *sys.argv[2:3])
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
mig = ROOT / "iba/app/migration/reading_phases_2273_v1_20261024.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(mig), "--db", str(DB)],
                                                                 capture_output=True, text=True, env=env)) for _ in range(2)]
live = sqlite3.connect(f"file:{(ROOT / 'iba/app/db/iba.db').as_posix()}?mode=ro", uri=True)
src = ROOT / json.loads(live.execute("SELECT value FROM cfg_setting WHERE key='narrative.copy_source_dir'").fetchone()[0])
chap = S / "chapters"
chap.mkdir()
for (f,) in live.execute("SELECT current_file FROM narrative_chapter WHERE inactive=0 AND current_file IS NOT NULL"):
    shutil.copy2(src / f, chap / f)
INBOX = S / "inbox"
c = sqlite3.connect(DB)
for key, val in (("narrative.copy_source_dir", str(chap)), ("narrative.learning4comfort_inbox_dir", str(INBOX)),
                 ("narrative.claim_register_path", str(S / "out/register.md")),
                 ("narrative.claim_changes_path", str(S / "out/changes.md")),
                 ("narrative.citation_index_path", str(S / "out/citations.md")),
                 ("reading.output_dir", str(S / "reading")), ("open_item.output_dir", str(S / "open-items"))):
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val), key))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
from iba.app.handlers import reading as hr  # noqa: E402
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/").replace("\n", " ")[:500]))
    print(f"{cid} {'PASS' if passed else 'FAIL'}" + ("" if passed else f"  {str(evidence)[:900]}"), flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(step, **params):
    params.setdefault("By", "Claude")
    params = {k: v for k, v in params.items() if v is not None}
    return getattr(hr, step)(Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None,
                                 params=params, step_id=f"reading.{step}"))


def state():
    return q("SELECT state FROM reading WHERE label=?", LABEL)[0][0]


def n_reading_obs():
    return q("SELECT count(*) FROM ib_observation WHERE stage='reading'")[0][0]


LABEL, ESC = "t-fear-sea", 2273
OBJ = "how fear turns at sea when the sailors learn whom the storm answers to"
scope = {"Verse": "Jon 1:10; Jon 1:16; Psa 56:3"}

# ── M migration ──────────────────────────────────────────────────────────────────────────────────
cols = {t: {r[1] for r in q(f"PRAGMA table_info({t})")} for t in ("ib_observation", "ib_node", "reading")}
case("M1", "Migration applied on the copy, and a second run writes nothing (idempotent)",
     "applied (run" in mo[0] and mo[1].startswith("0 cfg write(s)"), mo)
case("M2", "Schema: ib_observation.route; ib_node role, reading_id, disposition, disposition_note; the reading's new "
     "columns; ib_observation_change", {"route"} <= cols["ib_observation"]
     and {"role", "reading_id", "disposition", "disposition_note"} <= cols["ib_node"]
     and {"objective", "gathered_at", "observe_file", "observe_built_at", "observed_at", "narrate_file", "narrated_at"}
     <= cols["reading"] and q("SELECT 1 FROM sqlite_master WHERE name='ib_observation_change'"), cols)
tags = set(cfg.enum("ib_observation.tag"))
guide = cfg.required_setting("ib_observation.tag_guidance")
guide = json.loads(guide) if isinstance(guide, str) else guide
kinds = ["face", "qualification", "party", "statement", "link", "use", "term", "silence"]
case("M3", "The eight kinds are tag values, each with its tag guidance", set(kinds) <= tags and all(k in guide for k in kinds),
     sorted(set(kinds) - tags))
steps = [tuple(x) for x in q("SELECT ordinal, step FROM cfg_step WHERE work_package='reading' AND inactive=0 ORDER BY ordinal")]
case("M4", "Ten steps in order: open, gather, observe, record, check, synergy, apply, narrate, publish, account",
     [s for _, s in steps] == [f"reading.{x}" for x in ("open", "gather", "observe", "record", "check", "synergy", "apply",
                                                         "narrate", "publish", "account")], steps)
rules = dict(q("SELECT step, count(*) FROM cfg_method_rule WHERE active=1 AND step LIKE 'reading.%' GROUP BY step"))
rg04 = q("SELECT rule_text FROM cfg_method_rule WHERE rule_key LIKE 'RG-04 %' AND active=1")[0][0]
case("M5", "Rules moved: 39 on reading.observe, 16 on reading.narrate, none left on record or apply; RG-04 restated "
     "(qualifiers evaluated for value, examples not a list)", rules.get("reading.observe") == 39
     and rules.get("reading.narrate") == 16 and not rules.get("reading.record") and not rules.get("reading.apply")
     and "evaluated for its value" in rg04 and "not a list" in rg04, rules)
gt = rd.gap_types(cfg)
case("M6", "Gap types by phase: 7 pre, 3 observe, 2 post, 2 narrate; reading_state 'recorded' retired",
     sorted(t["phase"] for t in gt.values()).count("pre") == 7 and [t["phase"] for t in gt.values()].count("observe") == 3
     and [t["phase"] for t in gt.values()].count("post") == 2 and [t["phase"] for t in gt.values()].count("narrate") == 2
     and "recorded" not in cfg.enum("reading_state") and "narrated" in cfg.enum("reading_state"),
     {k: t["phase"] for k, t in gt.items()})
prompts = json.loads(cfg.required_setting("reading.observe_prompts")) if isinstance(
    cfg.required_setting("reading.observe_prompts"), str) else cfg.required_setting("reading.observe_prompts")
codes = [c2 for v in prompts.values() for c2 in v]
known = {r[0] for r in q("SELECT question_code FROM wa_obs_question_catalogue WHERE deleted=0")}
case("M7", "The 53 one-verse catalogue questions are prompts, each once, each a live catalogue row",
     len(codes) == 53 and len(set(codes)) == 53 and set(codes) <= known, len(codes))
old = [tuple(x) for x in q("SELECT label, state FROM reading ORDER BY id")]
o = hr.account(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-account", word="", word_id=None,
                   params={"Label": "m64-choose"}, step_id="reading.account"))
case("M8", "The four readings published before #2273 are untouched, and their Account renders",
     old == [("m64-choose", "published"), ("m64-willing", "published"), ("m64-plan", "published"),
             ("m64-dedicate", "published")] and o.condition == "ok", (old, o.message[:200]))

# ── O Open ───────────────────────────────────────────────────────────────────────────────────────
o = run("open", Label=LABEL, Escalation=str(ESC), Home="M01", **scope)
case("O1", "Open refused with no objective", o.condition == "refused" and "Objective" in o.message
     and not q("SELECT 1 FROM reading WHERE label=?", LABEL), o.message[:200])
o = run("open", Label=LABEL, Escalation=str(ESC), Home="M01", Objective="fear", **scope)
case("O2", "Open refused with an objective that says nothing (under 10 characters)", o.condition == "refused"
     and not q("SELECT 1 FROM reading WHERE label=?", LABEL), o.message[:200])
o = run("open", Label=LABEL, Escalation=str(ESC), Home="M01", Objective=OBJ, **scope)
r = q("SELECT * FROM reading WHERE label=?", LABEL)
gapf = S / "reading" / LABEL / f"{LABEL}-gaps.json"
g = json.loads(gapf.read_text(encoding="utf-8")) if gapf.is_file() else {"sections": {}}
pre = {k for k, t in gt.items() if t["phase"] == "pre"}
case("O3", "Open: the reading with its objective and 3 verses; the pre-gap JSON holds the 7 pre sections only (no "
     "not_read)", o.condition == "ok" and r and r[0]["objective"] == OBJ and r[0]["state"] == "open"
     and q("SELECT count(*) FROM reading_verse WHERE reading_id=?", r[0]["id"])[0][0] == 3
     and set(g["sections"]) == pre, o.message[:300])
rid = r[0]["id"]

# ── G pre gate and Gather ────────────────────────────────────────────────────────────────────────
o = run("observe", Label=LABEL)
case("G1", "Observe refused while the reading is open (the pre gate first)", o.condition == "refused"
     and "needs it gathered" in o.message, o.message[:150])
n_items = sum(len(s["items"]) for s in g["sections"].values())
if n_items:
    o = run("check", Label=LABEL)
    case("G2", f"Check at the pre gate refused while {n_items} item(s) have no record", o.condition == "refused"
         and state() == "open", o.message[:200])
    g2 = json.loads(gapf.read_text(encoding="utf-8"))
    first = next(it for s in g2["sections"].values() for it in s["items"])
    first["record"] = {"reason": "short"}
    (S / "bad-gather.json").write_text(json.dumps(g2), encoding="utf-8")
    o = run("gather", Label=LABEL, File=str(S / "bad-gather.json"))
    case("G3", "Gather refused: a reason under 10 characters; nothing written", o.condition == "refused"
         and n_reading_obs() == 0, o.message[:200])
    g3 = json.loads(gapf.read_text(encoding="utf-8"))
    for sec, s in g3["sections"].items():
        for it in s["items"]:
            it["record"] = {"reason": f"test reading of #2273: {sec} is outside what this trial reading reads"}
    gapf.write_text(json.dumps(g3, ensure_ascii=False), encoding="utf-8")
    o = run("gather", Label=LABEL)
    case("G4", "Gather: every pre-gap item recorded with its reason", o.condition == "ok", o.message[:200])
else:
    o = run("gather", Label=LABEL)
    case("G2", "Gather refused when there is nothing to gather (no pre-gap items)", o.condition == "refused"
         and "nothing to gather" in o.message, o.message[:150])
o = run("check", Label=LABEL)
case("G5", "Check: pre gate passed, gathered", o.condition == "ok" and state() == "gathered", o.message[:200])

# ── B Observe ────────────────────────────────────────────────────────────────────────────────────
o = run("observe", Label=LABEL)
obsf = S / "reading" / LABEL / f"{LABEL}-observe.json"
ob = json.loads(obsf.read_text(encoding="utf-8")) if obsf.is_file() else {"verses": []}
jon10 = next((v for v in ob["verses"] if v["verse"] == "Jon 1:10"), {"words": [], "findings_in_focus": []})
w10 = {wd["strong"]: wd for wd in jon10["words"]}
case("B1", "Observe: 3 verses; at Jon 1:10 'exceedingly' (H1419A, T2) is in focus as a qualifier, 'afraid' (H3372G) "
     "as an M-code word, and the function words 'to' (H0413) and the article (H9009) are not; the prompts by kind",
     o.condition == "ok" and len(ob["verses"]) == 3 and "qualifier (T2)" in w10.get("H1419A", {}).get("in_focus_as", [])
     and "M-code" in w10.get("H3372G", {}).get("in_focus_as", []) and "H0413" not in w10 and "H9009" not in w10
     and sum(len(x) for x in ob["prompts"].values()) == 53, (o.message[:200], sorted(w10)))
case("B2", "Observe: every finding already applied to the verse is read into focus (RO2), with its nodes",
     all("nodes" in f for v in ob["verses"] for f in v["findings_in_focus"])
     and q("SELECT count(DISTINCT o.id) FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE "
           "n.verse_reference='Jonah.1.10' AND o.status<>'withdrawn'")[0][0] == len(jon10["findings_in_focus"]),
     len(jon10["findings_in_focus"]))
o = run("check", Label=LABEL)
case("B3", "Check at the observe gate refused while words in focus have no node, item or reason (not_read)",
     o.condition == "refused" and "not_read" in o.message and state() == "gathered", o.message[:200])

# ── W the writer refuses, nothing written ────────────────────────────────────────────────────────
live_text = q("SELECT o.obs_text FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE "
              "n.verse_reference='Jonah.1.10' AND o.status<>'withdrawn' LIMIT 1")[0][0]
node10 = {"verse": "Jon 1:10", "strong": "H3372G", "cluster": "M01", "role": "characteristic"}
bad = {
    "W1 a description already live": [{"key": "x", "kind": "statement", "text": live_text, "basis": "stated",
                                       "nodes": [node10]}],
    "W2 a party finding without its route": [{"key": "x", "kind": "party", "text": "test: the sailors fear before the "
                                              "storm's sender", "basis": "stated", "nodes": [node10]}],
    "W3 a route on a statement": [{"key": "x", "kind": "statement", "text": "test: fear grows in the sailors",
                                   "basis": "stated", "route": "B", "nodes": [node10]}],
    "W4 a qualification without its characteristic": [{"key": "x", "kind": "qualification", "text": "test: exceedingly "
                                                       "raises it", "basis": "stated", "nodes": [
                                                           {"verse": "Jon 1:10", "strong": "H1419A", "role": "qualifier"}]}],
    "W5 a node cluster not among the word's own": [{"key": "x", "kind": "statement", "text": "test: fear grows",
                                                    "basis": "stated", "nodes": [{**node10, "cluster": "M02"}]}],
    "W6 a role outside its enum": [{"key": "x", "kind": "statement", "text": "test: fear grows", "basis": "stated",
                                    "nodes": [{**node10, "role": "main"}]}],
    "W7 a node with no verse on a finding that is not a term": [{"key": "x", "kind": "statement", "text": "test: fear "
                                                                 "grows", "basis": "stated", "nodes": [
                                                                     {"strong": "H3372G", "role": "characteristic"}]}],
    "W8 the same text twice in one file": [{"key": "x", "kind": "statement", "text": "test: fear grows", "basis": "stated",
                                            "nodes": [node10]},
                                           {"key": "y", "kind": "statement", "text": "test: fear grows", "basis": "stated",
                                            "nodes": [node10]}],
    "W9 a kind that is not one of the eight": [{"key": "x", "kind": "key-statement", "text": "test: fear grows",
                                                "basis": "stated", "nodes": [node10]}],
}
for cid, findings in bad.items():
    b = json.loads(obsf.read_text(encoding="utf-8"))
    b["findings"] = findings
    (S / "bad.json").write_text(json.dumps(b, ensure_ascii=False), encoding="utf-8")
    o = run("record", Label=LABEL, File=str(S / "bad.json"))
    case(cid.split()[0], f"Record refused: {cid.split(' ', 1)[1]}; nothing written", o.condition == "refused"
         and n_reading_obs() == 0 and not q("SELECT 1 FROM ib_node WHERE reading_id=?", rid), o.message[:250])
b = json.loads(obsf.read_text(encoding="utf-8"))
b["withdraw"] = [{"observation": q("SELECT id FROM ib_observation WHERE status<>'withdrawn' LIMIT 1")[0][0],
                  "reason": "no"}]
(S / "bad.json").write_text(json.dumps(b, ensure_ascii=False), encoding="utf-8")
o = run("record", Label=LABEL, File=str(S / "bad.json"))
case("W10", "Record refused: a withdrawal without its reason (RW-01); nothing changed", o.condition == "refused"
     and not q("SELECT 1 FROM ib_observation_change"), o.message[:200])
b = json.loads(obsf.read_text(encoding="utf-8"))
b["built_at"] = "2000-01-01T00:00:00Z"
(S / "bad.json").write_text(json.dumps(b, ensure_ascii=False), encoding="utf-8")
o = run("record", Label=LABEL, File=str(S / "bad.json"))
case("W11", "Record refused: a file not built from the tables for this reading (stale built_at)",
     o.condition == "refused" and "run Observe" in o.message, o.message[:200])

# ── R Record ─────────────────────────────────────────────────────────────────────────────────────
ob = json.loads(obsf.read_text(encoding="utf-8"))
mwords = [(v["verse"], wd) for v in ob["verses"] for wd in v["words"] if "M-code" in wd["in_focus_as"]]
existing = jon10["findings_in_focus"][0]["observation"] if jon10["findings_in_focus"] else None
statement = {"key": "s1", "kind": "statement", "text": "test (#2273): fear is turned from the storm to the one who "
             "sends it, once the sailors learn whom they face", "meaning": "the object of the fear changes",
             "basis": "read", "nodes": [{"verse": v, "strong": wd["strong"],
                                         "cluster": next(c2 for c2 in wd["clusters"] if c2.startswith("M")),
                                         "role": "characteristic"} for v, wd in mwords]}
findings = [statement,
            {"key": "q1", "kind": "qualification", "text": "test (#2273): 'exceedingly' gives the fear its grade: the "
             "greatest the sailors know", "basis": "stated", "nodes": [
                 {"verse": "Jon 1:10", "strong": "H1419A", "cluster": "T2", "role": "qualifier"},
                 {"verse": "Jon 1:10", "strong": "H3372G", "cluster": "M01", "role": "characteristic"}]},
            {"key": "p1", "kind": "party", "text": "test (#2273): the sailors fear before the Lord who sent the storm",
             "basis": "stated", "route": "B", "nodes": [{"verse": "Jon 1:10", "strong": "H3372G", "cluster": "M01",
                                                          "role": "characteristic"}]}]
if existing:
    findings.append({"key": "e1", "existing": existing, "nodes": [{"verse": "Jon 1:10", "strong": "H3372G",
                                                                   "cluster": "M01", "role": "characteristic"}]})
covered = {(v, wd["strong"]) for v, wd in mwords} | {("Jon 1:10", "H1419A")}
for v in ob["verses"]:
    for wd in v["words"]:
        if (v["verse"], wd["strong"]) not in covered:
            wd["record"] = {"reason": "test reading of #2273: this word carries nothing the trial reading reads for"}
ob["findings"] = findings
obsf.write_text(json.dumps(ob, ensure_ascii=False), encoding="utf-8")
n_obs_before = q("SELECT count(*) FROM ib_observation")[0][0]
o = run("record", Label=LABEL)
ob = json.loads(obsf.read_text(encoding="utf-8"))
wr = {f["key"]: f.get("written") for f in ob["findings"]}
s1 = wr.get("s1") or {}
case("R1", f"Record: 3 new findings, one statement applied by {len(mwords)} node(s) across the verses (one finding, "
     f"many nodes); ids written back", o.condition == "ok" and q("SELECT count(*) FROM ib_observation")[0][0]
     == n_obs_before + 3 and len(s1.get("nodes") or []) == len(mwords) and all(wr.values()), o.message[:300])
p1 = (wr.get("p1") or {}).get("observation")
qn = q("SELECT n.role, n.cluster_code FROM ib_node n WHERE n.observation_id=? ORDER BY n.seq",
       (wr.get("q1") or {}).get("observation"))
case("R2", "The party finding holds its route; the qualification is applied to the qualifier (T2) and the "
     "characteristic (M01); every node holds its role, its own cluster and the reading",
     q("SELECT route FROM ib_observation WHERE id=?", p1)[0][0] == "B"
     and [tuple(x) for x in qn] == [("qualifier", "T2"), ("characteristic", "M01")]
     and not q("SELECT 1 FROM ib_node WHERE reading_id=? AND (role IS NULL OR cluster_code IS NULL)", rid), list(qn))
if existing:
    case("R3", "An existing description takes a node, not a new row", (wr.get("e1") or {}).get("observation") == existing
         and q("SELECT count(*) FROM ib_node WHERE observation_id=? AND reading_id=?", existing, rid)[0][0] == 1,
         wr.get("e1"))
    wid = (wr.get("e1") or {}).get("nodes", [None])[0]
    ob = json.loads(obsf.read_text(encoding="utf-8"))
    ob["withdraw"] = [{"node": wid, "reason": "test (#2273): the earlier finding does not hold for this verse"}]
    obsf.write_text(json.dumps(ob, ensure_ascii=False), encoding="utf-8")
    o = run("record", Label=LABEL)
    ch = q("SELECT column_name, old_value, new_value, reason FROM ib_observation_change WHERE node_id=?", wid)
    case("R4", "A node withdrawn with its reason: disposition withdrawn, the change kept in ib_observation_change",
         o.condition == "ok" and q("SELECT disposition FROM ib_node WHERE id=?", wid)[0][0] == "withdrawn"
         and ch and ch[0]["column_name"] == "disposition" and ch[0]["new_value"] == "withdrawn", [tuple(x) for x in ch])
o = run("check", Label=LABEL)
case("R5", "Check: observe gate passed, observed; the three verses marked analysed", o.condition == "ok"
     and state() == "observed" and q("SELECT count(*) FROM verse_meta m JOIN reading_verse rv ON rv.verse_id=m.verse_id "
                                     "WHERE rv.reading_id=? AND m.status IN ('analysed', 'citated')", rid)[0][0] == 3,
     o.message[:300])

# ── A claims ─────────────────────────────────────────────────────────────────────────────────────
o = run("check", Label=LABEL)
case("A1", "Check at the claims gate refused while the reading's nodes have no disposition (observed_no_claim)",
     o.condition == "refused" and "observed_no_claim" in o.message and state() == "observed", o.message[:200])
o = run("synergy", Label=LABEL)
synf = S / "reading" / LABEL / f"{LABEL}-synergy.json"
sy = json.loads(synf.read_text(encoding="utf-8"))
mine = {f["observation"] for f in sy["findings"]}
case("A2", "Synergy: the reading's findings with this reading's live nodes only (the withdrawn node left out)",
     o.condition == "ok" and {(wr.get(k) or {}).get("observation") for k in ("s1", "q1", "p1")} <= mine
     and all(n["disposition"] != "withdrawn" for f in sy["findings"] for n in f["nodes"]), o.message[:200])
b = json.loads(synf.read_text(encoding="utf-8"))
other = q("SELECT id FROM ib_node WHERE reading_id IS NOT ? LIMIT 1", rid)[0][0]
b["findings"][0]["dispose"] = {"as": "data", "reason": "test reading of #2273", "nodes": [other]}
(S / "bad.json").write_text(json.dumps(b, ensure_ascii=False), encoding="utf-8")
o = run("apply", Label=LABEL, File=str(S / "bad.json"))
case("A3", "Apply refused: a node that is not this reading's", o.condition == "refused"
     and "not this reading's" in o.message, o.message[:200])
b = json.loads(synf.read_text(encoding="utf-8"))
b["findings"][0]["dispose"] = {"as": "context"}
(S / "bad.json").write_text(json.dumps(b, ensure_ascii=False), encoding="utf-8")
o = run("apply", Label=LABEL, File=str(S / "bad.json"))
case("A4", "Apply refused: a disposition without its reason", o.condition == "refused" and "reason" in o.message,
     o.message[:200])
sid = (wr.get("s1") or {}).get("observation")
sy["new_claims"] = [{"key": "n1", "text": "test (#2273): the sailors' fear turns from the storm to the Lord who sent it.",
                     "beyond_text": "the turn is read from the order of the verses", "verdict": "New",
                     "sources": ["Jon 1:10"], "observations": [sid]}]
for f in sy["findings"]:
    f["dispose"] = ({"as": "claim", "claim": "n1"} if f["observation"] == sid else
                    {"as": "data", "reason": "test reading of #2273: kept as data, not for the narrative"})
for c2 in sy["claims"]:
    if c2["status"] == "current" and not c2["rests_on_findings"]:
        c2["edit"] = {"observations": [sid]}
for it in sy["open_items"]:
    it["settle"] = {"as": "closed", "answer": "test reading of #2273 (on a copy): answered"}
(S / "apply.json").write_text(json.dumps(sy, ensure_ascii=False), encoding="utf-8")
o = run("apply", Label=LABEL, File=str(S / "apply.json"))
nd = dict(q("SELECT disposition, count(*) FROM ib_node WHERE reading_id=? GROUP BY disposition", rid))
case("A5", "Apply: a new claim on the statement finding; every node of this reading disposed (claim or data), each "
     "change kept", o.condition == "ok" and nd.get(None) is None and nd.get("claim") == len(mwords)
     and q("SELECT count(*) FROM ib_observation_change WHERE reading_id=? AND column_name='disposition'", rid)[0][0]
     >= sum(v for k, v in nd.items()), (o.message[:250], nd))
o = run("check", Label=LABEL)
gaps_post = o.message
case("A6", "Check: the claims gate passed, synergised; the narrate JSON built", o.condition == "ok"
     and state() == "synergised" and (S / "reading" / LABEL / f"{LABEL}-narrate.json").is_file(), o.message[:400])

# ── N narrate ────────────────────────────────────────────────────────────────────────────────────
narf = S / "reading" / LABEL / f"{LABEL}-narrate.json"
nar = json.loads(narf.read_text(encoding="utf-8")) if narf.is_file() else {"claims": []}
blk = q("SELECT s.heading, ch.chapter_no FROM narrative_section s JOIN narrative_chapter ch ON ch.id=s.chapter_id AND "
        "ch.inactive=0 WHERE s.last_version IS NULL AND s.level>0 AND s.block_text IS NOT NULL ORDER BY ch.reading_order, "
        "s.ordinal LIMIT 1")[0]
n1 = q("SELECT c.claim_ref FROM narrative_claim c JOIN narrative_claim_source cs ON cs.claim_id=c.id WHERE "
       "cs.observation_id=? AND c.claim_text LIKE 'test (#2273)%'", sid)
n1 = n1[0][0] if n1 else None
b = json.loads(json.dumps(nar))
for c2 in b["claims"]:
    if c2["claim"] == n1:
        c2["tell"], c2["hold"] = [{"chapter": blk["chapter_no"], "section": blk["heading"]}], "both"
(S / "bad.json").write_text(json.dumps(b, ensure_ascii=False), encoding="utf-8")
o = run("narrate", Label=LABEL, File=str(S / "bad.json"))
case("N1", "Narrate refused: a claim both told and held", o.condition == "refused" and "stands alone" in o.message,
     o.message[:200])
o = run("publish", Label=LABEL)
case("N2", "Publish refused before the narrate gate", o.condition == "refused" and "needs it narrated" in o.message,
     o.message[:150])
for c2 in nar["claims"]:
    if c2["claim"] == n1:
        c2["tell"] = [{"chapter": blk["chapter_no"], "section": blk["heading"], "kind": "in full"}]
    elif c2["status"] == "current" and not c2["told_in"]:
        c2["hold"] = "test reading of #2273: held"
narf.write_text(json.dumps(nar, ensure_ascii=False), encoding="utf-8")
o = run("narrate", Label=LABEL)
case("N3", "Narrate: the new claim told in a block; the nodes carried by it marked told, each change kept",
     o.condition == "ok" and q("SELECT in_narrative FROM narrative_claim WHERE claim_ref=?", n1)[0][0] == 1
     and q("SELECT count(*) FROM ib_node WHERE reading_id=? AND disposition='told'", rid)[0][0] == len(mwords)
     and str(blk["chapter_no"]) in json.loads(q("SELECT chapters FROM reading WHERE id=?", rid)[0][0] or "[]"),
     o.message[:300])
o = run("check", Label=LABEL)
case("N4", "Check: the narrate gate passed, narrated", o.condition == "ok" and state() == "narrated", o.message[:400])

# ── U publish, account, close gate ───────────────────────────────────────────────────────────────
gm = rd.gate_message(conn, ESC)
case("U1", "The anchoring escalation cannot close while the reading is not published", gm and LABEL in gm, gm)
o = run("publish", Label=LABEL)
chs = json.loads(q("SELECT chapters FROM reading WHERE label=?", LABEL)[0][0])
same = [(chap / f).read_bytes() == (INBOX / f).read_bytes() for (f,) in
        [q("SELECT current_file FROM narrative_chapter WHERE chapter_no=?", str(no))[0] for no in chs]]
case("U2", "Publish: published; the touched chapters in the inbox byte-identical; the escalation's gate clear",
     o.condition == "ok" and state() == "published" and same and all(same) and rd.gate_message(conn, ESC) is None,
     o.message[:300])
o = hr.account(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-account", word="", word_id=None,
                   params={"Label": LABEL}, step_id="reading.account"))
acc = S / "reading" / LABEL / f"{LABEL}-account.md"
acc = acc if acc.is_file() else next((S / "reading" / LABEL).glob(f"{LABEL}-account*.md"), acc)
case("U3", "Account written, with the objective and the findings applied", o.condition == "ok" and acc.is_file()
     and OBJ in acc.read_text(encoding="utf-8") and "Findings applied by this reading" in acc.read_text(encoding="utf-8"),
     o.message[:200])

# ── V validate ───────────────────────────────────────────────────────────────────────────────────
from iba.app.handlers import configmaint as cm  # noqa: E402
from iba.app.lib import cfgquality  # noqa: E402
for (k, v) in sqlite3.connect(DB).execute("SELECT key, value FROM cfg_setting WHERE key LIKE 'database.%.path' AND inactive=0").fetchall():
    conn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(str(ROOT / json.loads(v))), k))
errs = cm._validate_live(conn) + cfgquality.find_rule_scope_gaps(conn, ROOT / "iba" / "app") + [
    e for e in cfgquality.find_unregistered_project_scripts(conn, ROOT) if "iba/app/migration/" not in e]
case("V1", "configmaint.validate hard checks on the copy (the migration not yet archived set aside)", not errs,
     errs or "none")

out = ROOT / "outputs/escalation/2273-2274-test-results-v1-20261024.md"
L = ["# #2273 and #2274 test results (v1)", "",
     "Design: `outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md` sec 5. Run by "
     "`iba/app/tools/temp_2273_reading_phases_test_run.py` on a copy made with `lib/dbsnapshot.copy_db` of "
     f"`{pathlib.Path(sys.argv[2]).name if sys.argv[2:] else 'iba.db'}`, the migration applied to the copy, the narrative folder, the inbox and the output folders redirected to the scratch "
     "directory. The live database and files are not touched.", "",
     f"**{sum(1 for x in results if x[2] == 'PASS')}/{len(results)} passed.**", "",
     "| Case | What | Result | Evidence |", "|---|---|---|---|"] + [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in results]
out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"{sum(1 for x in results if x[2] == 'PASS')}/{len(results)} -> {out}")
