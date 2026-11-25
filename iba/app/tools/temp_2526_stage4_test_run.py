"""temp_2526_stage4_test_run.py -- tests for stage 4 of the study, the inner-being analysis, built on the stage 3 observations (escalation #2528 / #2526; design
outputs/escalation/2528-stage-4-design-v2-20261121.md; lib/layerinner.py, the dispatch in lib/layerreading.py, the migration stage4_observation_led_2526_v1_20261121).

Each case checks the tables against a direct query written here, not against the library's own lists, and runs the refusals. Runs against a COPY of iba.db that already holds the migration (never
the live database): a small test collection (backsliding) is taken through stages 1 to 3 on the copy, then steps 3.1 to 3.3 are run; the observations and ledger rows it makes are test rows.

Usage: python iba/app/tools/temp_2526_stage4_test_run.py <db copy> <scratch dir>
"""
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import buildvalidate as bv  # noqa: E402
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib import collectionvalidate as cvalid  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import validationactions as va  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import lexicalalignment as la  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []
RUN = "TEST-2526-S4"


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:330]))
    print(f"[{results[-1][2]}] {cid}: {results[-1][3][:160]}", file=sys.stderr, flush=True)


def refuses(fn, *a, **k):
    try:
        fn(*a, **k)
    except (lr.LayerError, ci.IndexError_) as exc:
        return str(exc)
    return None


def main(db, scratch):
    assert pathlib.Path(db).resolve() != (ROOT / "iba/app/db/iba.db").resolve(), "run against a copy"
    cfg = Cfg(pathlib.Path(db))
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp); _sp.loader.exec_module(_m)
    _m.apply_to_copy(cfg.conn)
    conn = cfg.conn
    q = lambda s, *a: conn.execute(s, a).fetchall()  # noqa: E731
    one = lambda s, *a: conn.execute(s, a).fetchone()[0]  # noqa: E731
    sc = pathlib.Path(scratch)
    s = lr.settings(cfg)

    # ── configuration
    steps3 = [x for x in s["steps"] if x["layer"] == 3]
    items3 = {k: s["items"][k] for k in ("subgroup-analysis", "collection-gathering", "interworking")}
    case("C1", "layer.reading has the three steps of layer 3 with the needs of the design and the three observation-led items; the verse-first items are gone",
         [x["key"] for x in steps3] == ["3.1", "3.2", "3.3"] and [x["items"] for x in steps3] == [["subgroup-analysis"], ["collection-gathering"], ["interworking"]]
         and steps3[0]["needs"] == ["1.1", "1.2", "2.1"] and steps3[1]["needs"] == ["3.1"] and steps3[2]["needs"] == ["3.2"] and "verse-working" not in s["items"] and "subgroup-working" not in s["items"]
        , [x["items"] for x in steps3])
    known = {i["key"] for i in __import__("iba.app.lib.observationrecord", fromlist=["x"]).items_setting(cfg)["items"]}
    case("C2", "the stage 4 items use only items of reading.observation_items, none the meaning; each has asks; 3.2 may use the discovery flag; the interventions are the observation-led prompts",
         all(set(v["uses"]) <= known and "meaning" not in v["uses"] and v["asks"] for v in items3.values()) and "flag" in items3["collection-gathering"]["uses"]
         and any("building blocks" in x or "Record building blocks" in x for x in cfg.setting("layer.interventions")), {k: v["uses"] for k, v in items3.items()})
    case("C3", "the rules IB-01 to IB-06 and IB-07 (#2538) are active and name the observation-led rows; the use text of collection_layer_item.item names the new items",
         one("SELECT count(*) FROM cfg_method_rule WHERE active=1 AND rule_key LIKE 'IB-0%'") == 7 and "subgroup-analysis" in one("SELECT rule_text FROM cfg_method_rule WHERE rule_key LIKE 'IB-01 %'")
         and "subgroup-analysis" in one("SELECT use FROM cfg_column WHERE table_name='collection_layer_item' AND name='item'"), "")
    found = [e for e in la.find(conn, ROOT) if "layer.reading" in e]
    case("C4", "the alignment check finds nothing wrong in layer.reading with the stage 4 items in it", not found, found[:3])

    # ── stages 1 to 3 on the small test collection, then the gates of stage 4
    name = "backsliding"
    cid = one("SELECT id FROM collection WHERE name=? AND deleted=0", name)
    ci.fill(conn, cfg, RUN)
    # the build now demands an answer to every older observation of the scope and an evidence layer that passes before stage 4 opens (#2538): the older observations of this
    # test collection are judged here as the test's own setup, each kept as evidence with its answer logged, and each node missing a column given its reason. The scope grows
    # when the grouping puts the older nodes under the collection, so it is settled again before step 3.1 opens.
    def settle_scope():
        sc_ = cvalid.scope(conn, cid)
        for oid_ in sorted(sc_["union"]):
            o_ = conn.execute("SELECT stage, nature FROM ib_observation WHERE id=?", (oid_,)).fetchone()
            if o_[0] not in bv.build_stages(lr.settings(cfg)) and o_[1] is None:
                va.set_nature(cfg, conn, oid_, "evidence", "test setup: an older observation of the test collection kept as evidence", RUN, "Claude")
                orec.log(conn, oid_, None, "build_answer", None, "keep", "test setup: kept as evidence", None, RUN, "Claude")
            for nid_, in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND disposition_note IS NULL AND "
                                      "(strong IS NULL OR verse_reference IS NULL OR surface IS NULL OR morph_code IS NULL OR role IS NULL OR verse_lexical_id IS NULL OR collection_id IS NULL)", (oid_,)).fetchall():
                va.note_node(conn, nid_, "test setup: a node of an older observation whose data gives no more", RUN, "Claude")
    settle_scope()
    surf = [r[0] for r in q("SELECT t.surface FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.collection_id=? AND i.deleted=0 ORDER BY t.surface", cid)]
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "3.1", True)
    case("G1", "step 3.1 on a collection with nothing done is refused, naming the steps of stage 3 that are not closed", bool(msg) and "step 1.1 is not closed" in msg and "step 2.1 is not closed" in msg, (msg or "")[:300])
    ci.make_group(conn, RUN, name, "alpha", "test group (#2526 test)")
    ci.make_group(conn, RUN, name, "beta", "test group (#2526 test)")
    half = len(surf) // 2
    ci.place(conn, RUN, name, "alpha", surf[:half], None, "test placement (#2526 test)")
    ci.place(conn, RUN, name, "beta", surf[half:-1], None, "test placement (#2526 test)")
    ci.place(conn, RUN, name, None, [surf[-1]], None, "test isolation (#2526 test)", isolate=True)
    # the words are read after the grouping, inside the subgroup of their surface (#2538, 2026-11-24)
    lr.open_step(conn, cfg, RUN, name, "S1")
    pS, _ = lr.pull(conn, cfg, name, "S1", sc)
    dS = json.loads(pS.read_text(encoding="utf-8"))
    for r in dS["rows"]:
        refs = [e["reference"] for e in r["evidence"]]
        r["fill"].update({"disposition": "observed", "senses": [{"kind": "term", "obs_text": f"In {', '.join(refs)} the word {r['word']} ({r['strong']}) stands in the sense the verses give it; test setup of #2526.",
                                                                  "basis": "stated", "occurrences": refs}]})
    lr.record(conn, cfg, RUN, dS, True)
    rS_ = lr.check(conn, cfg, RUN, name)
    if not rS_["steps"]["S1"]["closed"]:
        print("S1 not closed:", rS_["steps"]["S1"]["failed"][:4], file=sys.stderr)
    for stp, mk in (("1.1", lambda r: f"The surfaces of the group {r['group']} turn away, which is a movement of the inner being from what it held; test setup of #2526."),
                    ("1.2", lambda r: f"The Strong's codes of {r['group']} ({', '.join(r['strong_codes'])}) define it as a turning away; test setup of #2526.")):
        lr.open_step(conn, cfg, RUN, name, stp)
        p, _ = lr.pull(conn, cfg, name, stp, sc)
        d = json.loads(p.read_text(encoding="utf-8"))
        for r in d["rows"]:
            r["fill"].update({"disposition": "observed", "senses": [{"kind": r["kind"], "obs_text": f"{r['evidence'][0]['reference']}: " + mk(r), "basis": "stated", "occurrences": [e["reference"] for e in r["evidence"]]}]})     # a sense row: one finding for the whole subgroup here
        lr.record(conn, cfg, RUN, d, True)
        lr.check(conn, cfg, RUN, name)
    lr.open_step(conn, cfg, RUN, name, "2.1")
    if lr.derive(conn, cfg, lr.load(conn, cfg, name, pairs=True), "2.1"):
        p, _ = lr.pull(conn, cfg, name, "2.1", sc)
        d = json.loads(p.read_text(encoding="utf-8"))
        for r in d["rows"]:
            if s["items"][r["item"]]["none_allowed"]:
                r["fill"].update({"disposition": "none", "reason": "test: nothing to observe for this aspect (#2526 test)"})
            else:
                r["fill"].update({"disposition": "observed", "obs_text": "test setup observation text of at least forty characters (#2526)", "basis": "stated"})
        lr.record(conn, cfg, RUN, d, True)
    rep = lr.check(conn, cfg, RUN, name)
    case("G2", "stages 1 to 3 are closed on the test collection (setup)", all(rep["steps"][k]["closed"] for k in ("S1", "1.1", "1.2", "2.1")), {k: rep["steps"][k]["closed"] for k in ("S1", "1.1", "1.2", "2.1")})

    # ── 3.1: the rows come from the stage 3 observations of the subgroups
    L = lr.load(conn, cfg, name)
    gid_of = {g["name"]: g["id"] for g in L["groups"].values()}
    st3 = lambda g: {r[0] for r in q("SELECT DISTINCT o.id FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 AND n.collection_id=? AND n.subgroup_id=? "  # noqa: E731
                                     "AND o.stage IN ('layer-1','layer-2')", cid, g)}
    want = {g for g in gid_of.values() if st3(g)}
    settle_scope()
    r1 = lr.open_step(conn, cfg, RUN, name, "3.1")
    r2 = lr.open_step(conn, cfg, RUN, name, "3.1")
    rows31 = q("SELECT item, subgroup_id, subject, state FROM collection_layer_item WHERE collection_id=? AND step='3.1' AND state!='retired'", cid)
    case("O1", "opening 3.1 makes one subgroup-analysis row for each subgroup with stage 3 observations (equal to an independent query), no row for a verse; opening again changes nothing",
         len(want) >= 1 and r1["add"] == len(want) == len(rows31) and r2["add"] == 0 and {x[1] for x in rows31} == want and all(x[0] == "subgroup-analysis" and x[2] == "" and x[3] == "open" for x in rows31),
         f"{len(want)} rows; {r1}")
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "3.2", True)
    case("O2", "step 3.2 cannot open before 3.1 is closed", bool(msg) and "step 3.1 is not closed" in msg, (msg or "")[:160])

    path, n = lr.pull(conn, cfg, name, "3.1", sc)
    data = json.loads(path.read_text(encoding="utf-8"))
    r0 = data["rows"][0]
    g0 = gid_of[r0["group"]]
    def top_evidence(g):    # by marker (researcher 2026-11-24): the evidence observations with a live word node on the subgroup's occurrences, less the word observations a layer-1 sense already traces
        ev = {r[0] for r in q("SELECT DISTINCT o.id FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 AND n.traced_observation_id IS NULL AND o.nature='evidence' AND n.collection_id=? AND n.subgroup_id=?", cid, g)}
        carried = {r[0] for r in q("SELECT DISTINCT n.traced_observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.stage='layer-1' AND n.traced_observation_id IS NOT NULL")}
        return {x for x in ev if not (x in carried and q("SELECT stage FROM ib_observation WHERE id=?", x)[0][0] == "lexical")}

    case("P1", "the 3.1 file lists, for each row, the evidence observations of the subgroup to take up, chosen by the marker (equal to an independent query), the verses of the subgroup with their text, the uses, the roles, a fill with the traced node and the read-back",
         n == len(want) and {x["observation"] for x in r0["to_take_up"]} == top_evidence(g0) and r0["verses_of_the_subgroup"] and r0["uses"] and "characteristic" in json.dumps(r0["node_roles"]) and "not_used" in r0["fill"]
         and "traced" in json.dumps(r0["fill"]["findings"]) and "read_back" in r0["fill"]["findings"][0] and len(data["reading_rules"]) >= 40, f"{n} rows; {len(r0['to_take_up'])} to take up")
    case("P2", "the 3.1 file has no verse row and no demand for every occurrence: it carries observations and the verses only as base data to read back", "verse-working" not in json.dumps(data["rows"]) and "items_absent" not in json.dumps(data["rows"]), "")

    def covered(ids):
        return {r[0] for r in q("SELECT DISTINCT verse_lexical_id FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NOT NULL AND observation_id IN (%s)" % ",".join(map(str, ids)))} if ids else set()

    def good31(row, extra=None):
        req = [x["observation"] for x in row["to_take_up"]]
        occs = [o["occurrence"] for o in row["occurrences"]]
        cov = sorted(covered(req) & set(occs))[:2]
        f = {"key": "f1", "kind": "statement", "text": f"What the stage 3 observations of {row['group']} show is a turning away from what was held, as the working of the subgroup (ledger {row['ledger_id']}, test of #2526).",
             "basis": "stated", "route": "", "parts": {"item": "operation", "mode": "done"}, "nodes": [{"occurrence": o, "role": "characteristic"} for o in cov] + [{"traced": t} for t in req]}
        row["fill"] = {"disposition": "observed", "findings": [f], "existing": [], "not_used": {}, "reason": ""}
        return row

    def fresh(only_unvalidated=False):
        d = copy.deepcopy(data)
        open_ids = {r[0] for r in q("SELECT id FROM collection_layer_item WHERE collection_id=? AND step='3.1' AND validated=0", cid)}
        d["rows"] = [good31(r) for r in d["rows"] if not only_unvalidated or r["ledger_id"] in open_ids]
        return d

    before = (one("SELECT count(*) FROM ib_observation WHERE stage='layer-3'"), one("SELECT count(*) FROM ib_node WHERE observation_id IN (SELECT id FROM ib_observation WHERE stage='layer-3')"))
    row0 = lambda d: d["rows"][0]  # noqa: E731
    d = fresh()
    row0(d)["fill"]["findings"][0]["nodes"] = [n for n in row0(d)["fill"]["findings"][0]["nodes"] if "traced" not in n]
    m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
    case("R1", "a finding that rests on no observation is refused", "rests on observations" in m, m[:160])
    d = fresh()
    other = [i for i in st3(gid_of["beta" if r0["group"] == "alpha" else "alpha"]) if i not in st3(g0)]
    if other:
        row0(d)["fill"]["findings"][0]["nodes"].append({"traced": other[0]})
        m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
        case("R2", "a finding that rests on an observation of another subgroup is refused", "may rest on" in m, m[:160])
    else:
        case("R2", "a finding that rests on an observation of another subgroup is refused", True, "no observation exclusive to the other subgroup on this data (not exercised)")
    # a narrow source: a stage 1 sense observation of one word; an occurrence of the subgroup outside it needs a read-back
    narrow = q("SELECT o.id, count(n.id) c FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 AND o.stage='lexical' AND n.collection_id=? AND n.subgroup_id=? "
               "GROUP BY o.id ORDER BY c LIMIT 1", cid, g0)
    occs0 = [o["occurrence"] for o in r0["occurrences"]]
    out_occ = None
    if narrow:
        cv = covered([narrow[0][0]])
        out = [o for o in occs0 if o not in cv]
        out_occ = out[0] if out else None
    if out_occ:
        v_out = one("SELECT v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.id=?", out_occ)
        d = fresh()
        f = row0(d)["fill"]["findings"][0]
        f["nodes"] = [{"occurrence": out_occ, "role": "characteristic"}] + [n for n in f["nodes"] if "traced" in n]
        f["nodes"] = [{"occurrence": out_occ, "role": "characteristic"}, {"traced": narrow[0][0]}] + [n for n in f["nodes"] if n.get("traced") not in (None, narrow[0][0])][:0]
        row0(d)["fill"]["not_used"] = {}
        m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
        case("R3", "an occurrence outside the observations the finding rests on, with no read-back, is refused", "outside the observations" in m, m[:200])
        f["read_back"] = [{"verse": "Zzz.9.9", "why": "test: a verse that is not one of this row's"}]
        m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
        case("R4", "a read-back naming a verse that is not a verse of the row is refused", "read_back entry" in m, m[:160])
        f["read_back"] = [{"verse": v_out, "why": "test: the sense observation does not reach this occurrence, the verse is read back"}]
        m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
        case("R5", "with the verse read back and the reason given the occurrence is accepted (what is still refused is the take-up of the other observations, not the occurrence)", "outside the observations" not in m, m[:200])
    else:
        case("R3", "(read-back refusals)", True, "every occurrence of the subgroup lies in one stage 1 observation on this data (not exercised)")
    d = fresh()
    f = row0(d)["fill"]["findings"][0]
    f["nodes"] = [n for n in f["nodes"] if "traced" not in n or n["traced"] != f["nodes"][-1].get("traced")]
    m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
    case("R6", "a stage 3 observation neither rested on nor declared not used is refused, so nothing is lost on the way to stage 5", "neither rested on" in m or len(row0(d)["to_take_up"]) < 2, m[:200])
    d = fresh()
    last = row0(d)["to_take_up"][-1]["observation"]
    row0(d)["fill"]["not_used"] = {str(last): "test: declared not used though a finding rests on it"}
    m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
    case("R7", "an observation both rested on and declared not used is refused", "both rested on" in m, m[:160])
    d = fresh()
    row0(d)["fill"]["findings"][0]["nodes"] = [n for n in row0(d)["fill"]["findings"][0]["nodes"] if n.get("traced") != last]
    row0(d)["fill"]["not_used"] = {str(last): "short"}
    m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
    case("R8", "a not_used with no reason in words is refused", "reason in words" in m, m[:160])
    d = fresh()
    verse_txt = one("SELECT v.text FROM verse v JOIN verse_lexical vl ON vl.verse_id=v.id WHERE vl.id=?", occs0[0])
    row0(d)["fill"]["findings"][0]["text"] = " ".join(verse_txt.split()[:12])
    m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
    case("R9", "a finding that restates the verse is refused", "restates the verse" in m, m[:160])
    d = fresh()
    row0(d)["fill"]["findings"][0]["parts"] = {"item": "meaning"}
    m = refuses(lr.record, conn, cfg, RUN, d, True) or ""
    case("R10", "a finding of an item the row does not use (the meaning) is refused", "parts.item" in m, m[:160])
    after = (one("SELECT count(*) FROM ib_observation WHERE stage='layer-3'"), one("SELECT count(*) FROM ib_node WHERE observation_id IN (SELECT id FROM ib_observation WHERE stage='layer-3')"))
    case("R11", "none of the refused files wrote an observation or a node", before == after, (before, after))

    # ── 3.1: preview, record, check
    prev = lr.record(conn, cfg, RUN, fresh(), False)
    case("W0", "the preview checks and writes nothing", one("SELECT count(*) FROM ib_observation WHERE stage='layer-3'") == before[0] and prev["observed"] >= 1, prev)
    res = lr.record(conn, cfg, RUN, fresh(), True)
    obs = q("SELECT o.id, o.stage, o.stable_key FROM ib_observation o JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE o.deleted=0 AND c.collection_id=? AND c.step='3.1'", cid)
    traced = q("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND n.traced_observation_id IS NOT NULL AND o.stage='layer-3'")[0][0]
    states = [tuple(x) for x in q("SELECT DISTINCT state, validated FROM collection_layer_item WHERE collection_id=? AND step='3.1'", cid)]
    case("W1", "recording writes one observation for each finding with stage layer-3, a stable key on its ledger row, occurrence nodes with a role and traced nodes; each row is observed and not yet validated",
         len(obs) == len(want) and all(o[1] == "layer-3" for o in obs) and traced >= len(want) and states == [("observed", 0)], (len(obs), len(want), traced, states, res))
    rep = lr.check(conn, cfg, RUN, name)
    case("K1", "LayerCheck validates the 3.1 rows and closes the step", rep["steps"]["3.1"]["closed"] and rep["steps"]["3.1"]["validated"] == len(want), rep["steps"]["3.1"])
    # tamper: take away the traced nodes of one observation the first row rests on; the row is no longer valid
    tgt = r0["to_take_up"][0]["observation"]
    lid0 = [x for x in q("SELECT id FROM collection_layer_item WHERE collection_id=? AND step='3.1' AND subgroup_id=?", cid, g0)][0][0]
    mine = [x[0] for x in q("SELECT o.id FROM ib_observation o WHERE o.deleted=0 AND o.stable_key LIKE ?", f"layer:{lid0}:%")]
    conn.execute("UPDATE ib_node SET deleted=1 WHERE observation_id=? AND traced_observation_id IS NOT NULL", (mine[0],))
    rep = lr.check(conn, cfg, RUN, name)
    case("K2", "a finding whose traced nodes were removed fails the check and the step is no longer closed", not rep["steps"]["3.1"]["closed"] and any("rests on no observation" in x for x in rep["steps"]["3.1"]["failed"]), rep["steps"]["3.1"]["failed"][:2])
    lr.record(conn, cfg, RUN, fresh(True), True)    # answering the row again withdraws the damaged observation and writes it again (only the unvalidated row)
    rep = lr.check(conn, cfg, RUN, name)
    case("K3", "answering the row again repairs it, withdrawing the earlier observation with its reason, and the step closes", rep["steps"]["3.1"]["closed"] and one("SELECT count(*) FROM ib_observation WHERE stable_key LIKE ? AND deleted=0", f"layer:{lid0}:%") == 1, rep["steps"]["3.1"])
    if out_occ:
        d = fresh()
        d["rows"] = [r for r in d["rows"] if r["ledger_id"] == lid0]
        row0(d)["fill"]["findings"].append({"key": "f2", "kind": "statement", "basis": "stated", "parts": {"item": "circumstance"},
                                            "text": "The circumstance that this occurrence shows, outside what the sense observation covers, read back from its verse (test of #2526).",
                                            "nodes": [{"occurrence": out_occ, "role": "qualifier"}, {"traced": narrow[0][0]}],
                                            "read_back": [{"verse": v_out, "why": "test: the occurrence is outside the observations and the verse was read back (#2526)"}]})
        for lid_ in [x[0] for x in q("SELECT id FROM collection_layer_item WHERE id=? AND validated=1", lid0)]:
            conn.execute("UPDATE collection_layer_item SET validated=0 WHERE id=?", (lid_,))     # the row is answered again, so it is unvalidated until LayerCheck
        lr.record(conn, cfg, RUN, d, True)
        rep = lr.check(conn, cfg, RUN, name)
        ok_rb = rep["steps"]["3.1"]["closed"]
        conn.execute("UPDATE collection_layer_item SET reason=NULL WHERE id=?", (lid0,))
        rep2 = lr.check(conn, cfg, RUN, name)
        case("K4", "a row with an occurrence outside the observations validates only while its read-back is on the record: with the record removed the check fails it",
             ok_rb and not rep2["steps"]["3.1"]["closed"] and any("read-back" in x or "outside" in x for x in rep2["steps"]["3.1"]["failed"]), rep2["steps"]["3.1"]["failed"][:2])
        lr.record(conn, cfg, RUN, fresh(True), True)
        lr.check(conn, cfg, RUN, name)

    # ── 3.2: the behaviours of the collection
    r32 = lr.open_step(conn, cfg, RUN, name, "3.2")
    rows32 = q("SELECT item, subgroup_id, subject FROM collection_layer_item WHERE collection_id=? AND step='3.2' AND state!='retired'", cid)
    rows32 = [tuple(x) for x in rows32]
    case("O3", "step 3.2 opens after 3.1 closes with one collection-gathering row for the collection", r32["add"] == 1 and rows32 == [("collection-gathering", 0, "")], rows32)
    p32, _ = lr.pull(conn, cfg, name, "3.2", sc)
    d32 = json.loads(p32.read_text(encoding="utf-8"))
    row32 = d32["rows"][0]
    all31 = {r[0] for r in q("SELECT DISTINCT o.id FROM ib_observation o JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE o.deleted=0 AND c.collection_id=? AND c.step='3.1'", cid)}
    case("P3", "the 3.2 file lists every 3.1 observation of the collection to gather (equal to an independent query) and a not_gathered fill", {x["observation"] for x in row32["to_take_up"]} == all31 and "not_gathered" in row32["fill"], f"{len(all31)} observations")

    def good32(d_, with_flag=True, leave_out=None, declare=None):
        d2 = copy.deepcopy(d_)
        row = d2["rows"][0]
        req = [x["observation"] for x in row["to_take_up"]]
        use = [t for t in req if t != leave_out]
        cov = sorted(covered(use) & {o["occurrence"] for o in row["occurrences"]})[:2]
        item = {"item": "flag", "flag_type": "discovery"} if with_flag else {"item": "operation", "mode": "done"}
        row["fill"] = {"disposition": "observed", "findings": [{"key": "b1", "kind": "statement", "basis": "stated", "route": "", "parts": item,
                                                              "text": "A turning away from what was held, gathered from the elements of the subgroups of this collection (ledger test of #2526); it names and gathers and makes no claim.",
                                                              "nodes": [{"occurrence": o, "role": "characteristic"} for o in cov] + [{"traced": t} for t in use]}],
                       "existing": [], "not_gathered": declare or {}, "reason": ""}
        return d2
    m = refuses(lr.record, conn, cfg, RUN, good32(d32, with_flag=False), True) or ""
    case("R12", "a 3.2 row with no behaviour (no discovery flag) is refused", "at least one behaviour" in m, m[:200])
    if len(all31) > 1:
        lo = sorted(all31)[-1]
        m = refuses(lr.record, conn, cfg, RUN, good32(d32, leave_out=lo), True) or ""
        case("R13", "a 3.1 observation neither gathered into a behaviour nor declared not gathered is refused", "neither rested on" in m, m[:200])
        res32 = lr.record(conn, cfg, RUN, good32(d32, leave_out=lo, declare={str(lo): "test: this element belongs to no behaviour of the collection (#2526)"}), True)
    else:
        res32 = lr.record(conn, cfg, RUN, good32(d32), True)
        case("R13", "(not-gathered refusal)", True, "one 3.1 observation only on this data (not exercised)")
    rep = lr.check(conn, cfg, RUN, name)
    flags = q("SELECT count(*) FROM ib_observation o JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE o.deleted=0 AND c.step='3.2' AND c.collection_id=? AND json_extract(o.parts,'$.flag_type')='discovery'", cid)[0][0]
    case("K5", "the behaviour is a discovery flag observation that gathers 3.1 observations by traced nodes; LayerCheck validates the 3.2 row and closes the step", flags == 1 and rep["steps"]["3.2"]["closed"], (res32, rep["steps"]["3.2"]))
    conn.execute("UPDATE collection_layer_item SET validated=0 WHERE id=?", (row32["ledger_id"],))    # answered again: unvalidated until LayerCheck
    lr.record(conn, cfg, RUN, {"collection": name, "step": "3.2", "rows": [{"ledger_id": row32["ledger_id"], "fill": {"disposition": "none", "reason": "test: the collection shows no behaviour of its own (#2526 test)"}}]}, True)
    rep = lr.check(conn, cfg, RUN, name)
    case("K6", "a collection row may be recorded as none with its reason and validates", rep["steps"]["3.2"]["closed"] and [tuple(x) for x in q("SELECT state FROM collection_layer_item WHERE id=?", row32["ledger_id"])] == [("none",)], rep["steps"]["3.2"])
    conn.execute("UPDATE collection_layer_item SET state='open', validated=0, observation_id=NULL WHERE id=?", (row32["ledger_id"],))    # a none row is reopened by the researcher's change; here by hand
    lr.record(conn, cfg, RUN, good32(d32, leave_out=(sorted(all31)[-1] if len(all31) > 1 else None), declare=({str(sorted(all31)[-1]): "test: this element belongs to no behaviour of the collection (#2526)"} if len(all31) > 1 else None)), True)
    lr.check(conn, cfg, RUN, name)

    # ── 3.3: across collections
    L2 = lr.load(conn, cfg, name, pairs=True)
    d33 = lr.derive(conn, cfg, L2, "3.3")
    from iba.app.lib import layerinner as _li
    pn = sorted(_li.match_partners(w["subject"] for w in d33))
    msg33 = refuses(lr.open_step, conn, cfg, RUN, name, "3.3", True) if pn else "partner collection (no partner in this data)"
    case("P33a", "step 3.3 is refused while a partner collection is not complete (its step 3.2 or 3.3 not closed), naming it", bool(msg33) and "partner collection" in msg33 and (not pn or pn[0] in msg33), (msg33 or "")[:200])
    for pname in pn:      # test setup: the partner collections are complete (their step 3.2 closed in the ledger)
        pid = one("SELECT id FROM collection WHERE name=? AND deleted=0", pname)
        conn.execute("INSERT INTO collection_layer_item (collection_id, step, item, subgroup_id, subject, state, validated, reason, run_id, created_by) VALUES (?,?,?,?,?,'none',1,'test setup: the partner is complete (#2538 partner check)',?,?)",
                     (pid, "3.2", "collection-gathering", 0, "", RUN, "test"))
    case("P33b", "with its partners complete the check finds no gap", not bv.partner_gaps(conn, set(pn)), pn)
    r33 = lr.open_step(conn, cfg, RUN, name, "3.3")
    case("O4", "step 3.3 opens after 3.2 closes; its rows are the unique matches across the observations that reference more than one collection (researcher 2026-11-25)",
         r33["demanded"] == len(d33) == r33["add"] and all(x["item"] == "interworking" and x["subject"].startswith("match:") for x in d33), f"{len(d33)} rows demanded: {[x['subject'] for x in d33][:4]}")
    if d33:
        p33, _ = lr.pull(conn, cfg, name, "3.3", sc)
        dd33 = json.loads(p33.read_text(encoding="utf-8"))
        lr.record(conn, cfg, RUN, {"collection": name, "step": "3.3", "rows": [{"ledger_id": r["ledger_id"], "fill": {"disposition": "none", "reason": "test: the shared verses show no working together (#2526 test)"}} for r in dd33["rows"]]}, True)
        rep = lr.check(conn, cfg, RUN, name)
        case("K7", "every 3.3 row answered as none with its reason validates", rep["steps"]["3.3"]["validated"] == len(dd33["rows"]), rep["steps"]["3.3"])
    else:
        case("K7", "no 3.3 aspect is demanded on this small collection (no partner collection reaches the threshold)", True, "")

    # ── nothing of the verse-first design is left in the code or the config
    case("M1", "no verse-first ledger item, rule wording or code name is left: no ledger row of verse-working or subgroup-working, no IB rule mentioning them",
         one("SELECT count(*) FROM collection_layer_item WHERE item IN ('verse-working','subgroup-working')") == 0 and one("SELECT count(*) FROM cfg_method_rule WHERE rule_key LIKE 'IB-0%' AND (rule_text LIKE '%verse-working%' OR rule_text LIKE '%subgroup-working%')") == 0, "")
    conn.commit()
    return 0


if __name__ == "__main__":
    db, scratch = sys.argv[1], sys.argv[2]
    rc = 0
    try:
        main(db, scratch)
    except Exception as exc:
        import traceback
        traceback.print_exc()
        case("X", "the run completed", False, repr(exc)[:300])
        rc = 1
    print("| case | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    fails = [r for r in results if r[2] == "FAIL"]
    print(f"\n{len(results) - len(fails)} of {len(results)} pass")
    sys.exit(1 if fails or rc else 0)
