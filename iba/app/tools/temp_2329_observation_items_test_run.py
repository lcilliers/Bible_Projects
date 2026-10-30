"""temp_2329_observation_items_test_run.py -- escalation #2329 test plan (build v3), on a COPY of the live iba.db (never the live DB): the nine
observation items, one observation per item, the nuance pointers, the verse-text and grounds checks, the per-verse timing. Real data
(Judg 13:6, its existing observations) and synthetic bad input. Spec: outputs/escalation/2329-observation-structure-worked-example-v3-20261030.md.
Usage: python iba/app/tools/temp_2329_observation_items_test_run.py <scratch dir>. Prints PASS/FAIL per case."""
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
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402
from iba.app.handlers import reading as hr  # noqa: E402
from iba.app.lib import reading as rd  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2329v3run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", ROOT / "iba/app/db/iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
MIG = ROOT / "iba/app/migration/analysis_phase_1_2329_v3_20261030.py"
MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(MIG), "--db", str(DB), *a],
                                                                 capture_output=True, text=True, env=env))
      for a in (["--dry-run"], [], [])]
c0 = sqlite3.connect(DB)
c0.execute("UPDATE cfg_setting SET value=? WHERE key='reading.output_dir'", (json.dumps(str(S / "reading")),))
c0.commit()
c0.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:1200]}"), flush=True)


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


# ── M: the migration and the config ─────────────────────────────────────────────────────────────────
FRESH = not mo[0].startswith("already applied")          # False once the live database holds the migration
case("M1", "migration: dry run lists the writes, apply writes, a second run is refused (once the source holds it: every run is refused)",
     (mo[0].startswith("DRY RUN") and "cfg_setting insert" in mo[0] and "applied" in mo[1] if FRESH else mo[0].startswith("already applied"))
     and mo[2].startswith("already applied"), mo)
items = orec.items_setting(cfg)
keys = orec.item_keys(cfg)
case("M2", "config: nine items (item 8 in two forms), each with kinds and bases; modes and flag types held",
     sorted({i["no"] for i in items["items"]}) == list(range(1, 10)) and len(keys) == 10
     and items["modes"] == ["done", "foreseen", "commanded", "negated", "reported"] and items["flag_types"] == ["data-quality", "discovery"]
     and all(i["kinds"] and i["bases"] for i in items["items"]), items)
parts_spec = json.loads(q("SELECT value FROM cfg_setting WHERE key='reading.observation_parts'")[0][0])
rules = orec.rules(cfg)
case("M3", "config: before, after and the typed party are gone from observation_parts; the old completeness rules are gone",
     not any(k in parts_spec for k in ("parts", "party_form", "flag_types"))
     and not any(k in rules for k in ("parts_never_absent", "primary_operation", "chain", "party")), (parts_spec.keys(), rules.keys()))
nu = json.loads(q("SELECT value FROM cfg_setting WHERE key='reading.nuance_pointers'")[0][0])
rule_codes = {r_[0].split(" ")[0] for r_ in q("SELECT rule_key FROM cfg_method_rule WHERE active=1")}
cites = {c.strip() for n in nu for c in n["rule"].split(",") if c.strip().startswith(("RG-", "RW-", "RS-"))}
case("M4", "nuance pointers: every row has nuance, item, form, basis, rule and verse; the item is one of the nine; every rule cited exists",
     len(nu) >= 15 and all(set(n) == {"nuance", "item", "form", "basis", "rule", "verse"} and n["item"] in keys for n in nu)
     and cites <= rule_codes, (cites - rule_codes, [n for n in nu if n["item"] not in keys]))
case("M5", "RS-10 is in, RS-08 and RW-02 restated without the old parts, the change is logged",
     len(q("SELECT 1 FROM cfg_method_rule WHERE rule_key LIKE 'RS-10%' AND active=1")) == 1
     and "before" not in q("SELECT rule_text FROM cfg_method_rule WHERE rule_key LIKE 'RS-08%'")[0][0]
     and "primary operation" not in q("SELECT rule_text FROM cfg_method_rule WHERE rule_key LIKE 'RW-02%'")[0][0]
     and q("SELECT count(*) FROM cfg_change_detail WHERE run_id='DEVMODE-2329-OBSERVATION-ITEMS-20261030'")[0][0] >= 6)

# ── U: check_item_parts, unit ───────────────────────────────────────────────────────────────────────
G = "the awe is placed directly before the refusals in the report"


def cp(parts, kind, basis="stated", route=None):
    e = []
    orec.check_item_parts(cfg, parts, kind, basis, route, "t", e)
    return e


case("U1", "a meaning item as a face passes", cp({"item": "meaning"}, "face") == [])
case("U2", "bad input: no item / unknown item / not an object", all(cp(p_, "face") for p_ in ({}, {"item": "colour"}, "meaning", None)))
case("U3", "bad input: the item written as a kind it does not allow is refused and names the kinds",
     any("['face']" in x for x in cp({"item": "meaning"}, "statement")), cp({"item": "meaning"}, "statement"))
case("U4", "bad input: a basis the item does not allow is refused (meaning is stated only)",
     any("basis" in x for x in cp({"item": "meaning", "grounds": G}, "face", "read")))
case("U5", "a read observation without grounds is refused; with grounds it passes",
     any("grounds" in x for x in cp({"item": "operation", "mode": "done"}, "statement", "read"))
     and cp({"item": "operation", "mode": "done", "grounds": G}, "statement", "read") == [])
case("U6", "bad input: the operation without a mode, or a mode outside the list",
     any("mode" in x for x in cp({"item": "operation"}, "statement")) and any("mode" in x for x in cp({"item": "operation", "mode": "maybe"}, "statement")))
case("U7", "all five modes pass", all(cp({"item": "operation", "mode": m_}, "statement") == [] for m_ in items["modes"]))
case("U8", "polarity item: needs refusal or pursuit",
     any("polarity" in x for x in cp({"item": "polarity"}, "statement")) and cp({"item": "polarity", "polarity": "refusal"}, "statement") == [])
case("U9", "flag item: needs a flag type",
     any("flag_type" in x for x in cp({"item": "flag"}, "statement")) and cp({"item": "flag", "flag_type": "discovery"}, "statement") == [])
case("U10", "party item: a party finding carries its route",
     any("route" in x for x in cp({"item": "party"}, "party")) and cp({"item": "party"}, "party", route="A") == [])
case("U11", "bad input: the old twelve-part form and the typed party are refused",
     bool(cp({"item": "meaning", "sense": "x", "before": "y", "party": {"text": "z", "acts": "human", "acted_on": "human"}}, "face")))
verse_text = "Then the woman came and told her husband, A man of God came to me, and his appearance was like the appearance of the angel of God"
case("U12", "verse text: a run of more than seven words is found; a short phrase is not",
     orec.copies_verse(cfg, ["his appearance was like the appearance of the angel of God"], verse_text)
     and orec.copies_verse(cfg, ["the appearance of the angel of God sets the standing"], verse_text) is None,
     orec.copies_verse(cfg, ["his appearance was like the appearance of the angel of God"], verse_text))

# ── E: Judg 13:6 end to end ─────────────────────────────────────────────────────────────────────────
L = "t2329-v3"
r = run("open", Label=L, Escalation="2329", Objective="the asking words in their verses (a test of the observation items)",
        Subgroup="M21_asking", Verse="Judg 13:6")
case("E1", "Open: Judg 13:6 indexed", r.condition == "ok", r.message)
r = run("observe", Label=L, Count=1)
d = idx(L)
v = d["verses"][0]
sh = v["sheet"]
case("E2", "Observe: the sheet carries the nine items, the nuance pointers, items_absent per surface, and the item rules in `how`; in_hand_at is stamped",
     r.condition == "ok" and len(sh["items"]) == 10 and len(sh["nuances"]) == len(nu) and all("items_absent" in g for g in sh["surfaces"])
     and "RS-10" in sh["how"] and "twelve" not in sh["how"] and "`before`" not in sh["how"] and v.get("in_hand_at"), (r.message, sh["how"][:300]))
ex = sh["existing"]
case("E3", "real data: every existing observation on Judg 13:6 (the old form) is flagged as not an item",
     ex and all(any(f["code"] == "parts_not_an_item" for f in e["flags"]) for e in ex), [(e["observation"], [f["code"] for f in e["flags"]]) for e in ex])

OCC = {"woman": ("H0802G", 1101798), "man": ("H0376G", 1101805), "appearance": ("H4758", 1101812), "angel": ("H4397H", 1101818),
       "very": ("H3966", 1101821), "awesome": ("H3372H", 1101822), "not1": ("H3808", 1101823), "ask": ("H7592", 1101824),
       "not2": ("H3808", 1101826), "tell": ("H5046", 1101827), "name": ("H8034", 1101831)}
REL = {"H4758": "relevant", "H3372H": "relevant", "H7592": "relevant", "H5046": "relevant", "H3966": "relevant", "H3808": "relevant",
       "H4397H": "bears_on", "H0376G": "bears_on", "H0802G": "bears_on", "H8034": "bears_on"}
CHARS = ["appearance", "awesome", "ask", "tell"]
ROUTES = sorted(cfg.enum("observation_route"))
ROUTE, ROUTE2 = ROUTES[0], ROUTES[-1]


def node(name, role):
    strong, occ = OCC[name]
    return {"strong": strong, "occurrence": occ, "role": role, **({"cluster": "T2"} if strong == "H8034" else {})}


def F(key, kind, text, parts, nodes, basis="stated", **kw):
    return {"key": key, "kind": kind, "text": text, "basis": basis, "parts": parts, "nodes": nodes, **kw}


def good_findings():
    return [
        F("m1", "face", "Appearance here is what was seen of him, the sight of the man as the woman describes it.", {"item": "meaning"}, [node("appearance", "characteristic")]),
        F("m2", "face", "Awesome here describes what was seen and carries the sense of inspiring awe or reverence.", {"item": "meaning"}, [node("awesome", "characteristic")]),
        F("m3", "face", "The verb is the one of enquiring, to put a question to someone.", {"item": "meaning"}, [node("ask", "characteristic")]),
        F("m4", "face", "The verb is to tell or report, to make something known to someone.", {"item": "meaning"}, [node("tell", "characteristic")]),
        F("r1", "qualification", "Very raises the awe to a high degree.", {"item": "role"}, [node("very", "qualifier"), node("awesome", "characteristic")]),
        F("p1", "statement", "The negation makes the asking a refusal: she records that she did not enquire.", {"item": "polarity", "polarity": "refusal"},
          [node("not1", "qualifier"), node("ask", "characteristic")]),
        F("p2", "statement", "The negation makes the telling a refusal on his side: he did not make it known.", {"item": "polarity", "polarity": "refusal"},
          [node("not2", "qualifier"), node("tell", "characteristic")]),
        F("o1", "statement", "His appearance is set beside the appearance of the angel.", {"item": "object"}, [node("appearance", "characteristic"), node("angel", "object")]),
        F("o2", "statement", "What was not told is his name.", {"item": "object"}, [node("tell", "characteristic"), node("name", "object")]),
        F("a1", "statement", "She did not enquire of him about his origin.", {"item": "operation", "mode": "negated"},
          [node("ask", "characteristic"), node("woman", "relational_target"), node("man", "relational_target")]),
        F("a2", "statement", "He did not tell her who he was.", {"item": "operation", "mode": "negated"}, [node("tell", "characteristic")]),
        F("a3", "statement", "His look carries his standing for the woman, who calls him a man of God as she tells it.",
          {"item": "operation", "mode": "done", "grounds": "the likeness to the angel and the words man of God stand in one sentence"},
          [node("appearance", "characteristic")], basis="read"),
        F("t1", "party", "The woman did not ask; the man was not asked; he did not tell and she was not told.", {"item": "party"},
          [node("ask", "characteristic"), node("tell", "characteristic")], route=ROUTE),
        F("c1", "statement", "All of it is said in her report to her husband.", {"item": "circumstance"}, [node(n_, "characteristic") for n_ in CHARS]),
        F("k1", "link", "In her report the appearance, the awe, the not-asking and the not-telling are stated in that order.", {"item": "chain"},
          [node(n_, "characteristic") for n_ in CHARS], route=ROUTE),
        F("k2", "link", "The awe of the appearance and the restraint in asking and telling belong together.",
          {"item": "chain", "grounds": G}, [node(n_, "characteristic") for n_ in CHARS], basis="read", route=ROUTE2),
        F("g1", "statement", "These readings are not settled by the verse; the claims process tests them against other verses.",
          {"item": "flag", "flag_type": "discovery"}, [node(n_, "characteristic") for n_ in ("appearance", "ask", "tell")]),
    ]


def covered(findings):
    """{characteristic name: set of items observed}, from the findings' nodes."""
    out = {n_: set() for n_ in CHARS}
    for f in findings:
        for nd in f["nodes"]:
            nm = next(k for k, (s_, o_) in OCC.items() if o_ == nd["occurrence"])
            if nm in out and nd["role"] == "characteristic":
                out[nm].add(f["parts"]["item"])
    return out


def fill(findings, drop_absent=(), absent_extra=None):
    """Reset the in-hand sheet of Judg 13:6 and fill it: every existing observation deleted, the findings, every surface evaluated,
    the items not observed stated absent per characteristic."""
    d_ = idx(L)
    s_ = d_["verses"][0]["sheet"]
    s_["errors"] = []
    for e in s_["existing"]:
        e["action"] = {"action": "delete", "reason": "test: the old form of parts is replaced by the nine items"}
    s_["findings"] = findings
    cov = covered(findings)
    for g in s_["surfaces"]:
        g["evaluation"] = {"result": REL.get(g["strong"], "not_relevant"), "reason": "test: evaluated by the tests of the lexical work"}
        g["items_absent"] = {}
        for nm in CHARS:
            if OCC[nm][1] in g["occurrences"]:
                g["items_absent"] = {k_: "test: the verse shows none for this word" for k_ in keys if k_ not in cov[nm] and k_ not in drop_absent}
                g["items_absent"].update(absent_extra or {})
    save(L, d_)


def record_errors():
    r_ = run("record", Label=L)
    return r_, idx(L)["verses"][0].get("sheet", {}).get("errors") or []


fill(good_findings(), drop_absent=("meaning",))
r, errs = record_errors()
case("B0", "baseline: a complete set with every item observed or stated absent is recorded", r.condition == "ok", (r.message, errs))
if r.condition != "ok":
    print(f"\n{sum(res)} of {len(res)} cases pass (stopped: baseline failed)")
    sys.exit(1)
GOOD_RUN = "RUN-TEST-record"
V0 = idx(L)["verses"][0]
by_item = {k_: n_ for k_, n_ in q("SELECT json_extract(parts,'$.item'), count(*) FROM ib_observation WHERE deleted=0 AND run_id=? GROUP BY 1", GOOD_RUN)}
case("G2", "stored: one observation per item, queryable by parts.item; 17 findings in all",
     sum(by_item.values()) == 17 and by_item.get("meaning") == 4 and by_item.get("operation") == 3 and by_item.get("chain") == 2
     and by_item.get("circumstance") == 1 and by_item.get("flag") == 1, by_item)
shared = q("SELECT o.id, count(DISTINCT n.verse_lexical_id) c FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id "
           "WHERE o.run_id=? AND o.deleted=0 AND json_extract(o.parts,'$.item')='circumstance' AND n.role='characteristic' "
           "GROUP BY o.id", GOOD_RUN)
case("G3", "a shared observation (circumstance) is one row with nodes on all four characteristics", shared and shared[0]["c"] == 4, [tuple(x) for x in shared])
read = q("SELECT basis, json_extract(parts,'$.grounds') g FROM ib_observation WHERE run_id=? AND deleted=0 AND basis='read'", GOOD_RUN)
case("G4", "read observations hold their grounds", len(read) == 2 and all(x["g"] for x in read), [tuple(x) for x in read])
mode = q("SELECT json_extract(parts,'$.mode') m, count(*) FROM ib_observation WHERE run_id=? AND deleted=0 AND "
         "json_extract(parts,'$.item')='operation' GROUP BY 1", GOOD_RUN)
case("G5", "the mode of the operations is stored", {x["m"]: x[1] for x in mode} == {"negated": 2, "done": 1}, [tuple(x) for x in mode])
old = q("SELECT count(*) FROM ib_observation WHERE deleted=0 AND id IN (SELECT observation_id FROM ib_node WHERE verse_reference='Judg.13.6' "
        "AND deleted=0) AND run_id<>?", GOOD_RUN)[0][0]
case("G6", "the old observations of the verse were soft deleted with their reason, none physically removed",
     old == 0 and q("SELECT count(*) FROM ib_observation_change WHERE column_name='deleted' AND reason LIKE 'test: the old form%'")[0][0] >= 6)
v2 = V0
case("G7", "timing: the verse carries a result with in_hand_at and elapsed_seconds",
     v2["status"] == "done" and v2["result"].get("in_hand_at") and isinstance(v2["result"].get("elapsed_seconds"), int)
     and v2["result"]["elapsed_seconds"] >= 0, v2["result"])
ab = [s_ for s_ in v2["result"]["surfaces"] if s_.get("items_absent")]
case("G8", "the items stated absent are kept in the JSON result per surface", len(ab) == 4 and all(len(s_["items_absent"]) >= 2 for s_ in ab), ab[:1])


gate = rd.gate_observe(cfg, hr.PROJECT_ROOT, q("SELECT * FROM reading WHERE label=?", L)[0])
case("G9", "the Observe gate passes on the recorded verse", gate == [], gate)
run("reopen", Label=L, Verse="Judg 13:6", Note="test: the bad-input cases need the verse in hand again")
run("observe", Label=L, Count=1)


def refused_with(mut, needle, cid, desc, **fk):
    base = [dict(f, nodes=[dict(n_) for n_ in f["nodes"]], parts=dict(f["parts"])) for f in good_findings()]
    fs = mut(base)
    n0 = q("SELECT count(*) FROM ib_observation")[0][0]
    fill(fs, **fk)
    r_, e_ = record_errors()
    n1 = q("SELECT count(*) FROM ib_observation")[0][0]
    case(cid, desc + " (refused, named, nothing written)", r_.condition == "refused" and any(needle in x for x in e_) and n0 == n1,
         (r_.condition, needle, e_[:6], n0, n1))


def alter(key, **chg):
    def m(fs):
        for f in fs:
            if f["key"] == key:
                for k_, v_ in chg.items():
                    if k_ == "parts":
                        f["parts"].update(v_)
                    else:
                        f[k_] = v_
        return fs
    return m


refused_with(lambda fs: [f for f in fs if f["key"] != "m3"], "never absent", "B1", "bad input: a characteristic with no meaning observation", drop_absent=("meaning",))
refused_with(alter("m1", kind="statement"), "kind", "B2", "bad input: the meaning item written as a statement")
refused_with(alter("a3", parts={"grounds": ""}), "grounds", "B3", "bad input: a read observation without grounds")
refused_with(lambda fs: [f for f in fs if f["key"] not in ("a1", "a2", "a3")], "operation", "B4", "bad input: a verse with no operation observation")
refused_with(alter("a1", parts={"mode": None}), "mode", "B5", "bad input: an operation with no mode")
refused_with(alter("p1", parts={"polarity": "maybe"}), "polarity", "B6", "bad input: a polarity outside refusal or pursuit")
refused_with(alter("o1", text="Then the woman came and told her husband that a man of God came to me and his appearance was like the appearance of the angel"),
             "restates the verse text", "B7", "bad input: an observation that restates the verse")
refused_with(alter("m3", nodes=[node("ask", "characteristic"), node("tell", "characteristic")]), "one observation for one characteristic", "B8",
             "bad input: the meaning item (not shared) with nodes on two characteristics")
refused_with(lambda fs: fs, "needs an observation with a node on this word", "B9", "bad input: an item neither observed nor stated absent",
             drop_absent=("meaning", "enactment"))
refused_with(lambda fs: fs, "items_absent is", "B10", "bad input: items_absent with an item that is not one of the nine",
             drop_absent=("meaning",), absent_extra={"colour": "test: not an item at all"})
refused_with(alter("t1", route=None), "route", "B11", "bad input: a party observation without its route")
refused_with(alter("m2", parts={"item": "meaning", "sense": "the old form", "before": "the old form"}), "not among", "B12", "bad input: the old twelve-part form")
refused_with(lambda fs: [f for f in fs if f["key"] != "o2"], "name", "B13",
             "bad input: a bears-on word (name) with no observation of the act holding it", drop_absent=("meaning",))

# the refusals wrote nothing: the set recorded at B0 is unchanged
case("G1", "after the refusals the recorded set is unchanged (17 live findings of the good run)",
     q("SELECT count(*) FROM ib_observation WHERE deleted=0 AND run_id=?", GOOD_RUN)[0][0] == 17)

print(f"\n{sum(res)} of {len(res)} cases pass")
sys.exit(0 if all(res) else 1)
