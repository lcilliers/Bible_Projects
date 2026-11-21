"""temp_2528_stage4_test_run.py -- tests for escalation #2528: stage 4 of the study, the inner-being analysis, as steps 3.1 to 3.3 of the layered reading
(lib/layerinner.py, the dispatch in lib/layerreading.py, lib/verseevidence.py, observationrecord.write with a stage and a stable key, the boundary check of lib/lexicalalignment.py, and the
configuration migration stage4_config_2528_v1_20261121).

Each case checks the tables against a direct query written here, not against the library's own lists, and runs the refusals. Runs against a COPY of iba.db that already holds the migration
(never the live database): a small test collection (backsliding) is taken through stages 1 to 3 on the copy, then steps 3.1 to 3.3 are run; the observations and ledger rows it makes are test rows.

Usage: python iba/app/tools/temp_2528_stage4_test_run.py <db copy> <scratch dir>
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import lexicalalignment as la  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []
RUN = "TEST-2528"


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:330]))
    print(f"[{results[-1][2]}] {cid}: {results[-1][3][:160]}", file=sys.stderr, flush=True)     # progress while the run is going


def refuses(fn, *a, **k):
    try:
        fn(*a, **k)
    except (lr.LayerError, ci.IndexError_) as exc:
        return str(exc)
    return None


def main(db, scratch):
    assert pathlib.Path(db).resolve() != (ROOT / "iba/app/db/iba.db").resolve(), "run against a copy"
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    q = lambda s, *a: conn.execute(s, a).fetchall()  # noqa: E731
    one = lambda s, *a: conn.execute(s, a).fetchone()[0]  # noqa: E731
    sc = pathlib.Path(scratch)
    s = lr.settings(cfg)

    # ── configuration
    steps3 = [x for x in s["steps"] if x["layer"] == 3]
    case("C1", "layer.reading has 7 steps, the three of layer 3 (3.1, 3.2, 3.3) with the needs the design gives; stage 3 is layer-3, an enum value; 3.3 reads the pairings",
         len(s["steps"]) == 7 and [x["key"] for x in steps3] == ["3.1", "3.2", "3.3"] and steps3[0]["needs"] == ["1.1", "1.2", "2.1"] and steps3[1]["needs"] == ["3.1"] and steps3[2]["needs"] == ["3.2"]
         and steps3[2].get("pairs") and s["stages"]["3"] == "layer-3" and one("SELECT count(*) FROM cfg_enum WHERE name='ib_observation.stage' AND value='layer-3'") == 1, f"{[x['key'] for x in s['steps']]}")
    uses = {k: s["items"][k]["uses"] for k in ("verse-working", "subgroup-working", "interworking")}
    known = {i["key"] for i in orec.items_setting(cfg)["items"]}
    case("C2", "the three stage 4 items use only items of reading.observation_items, none of them the meaning; each has asks; layer.interventions has prompts",
         all(set(u) <= known and "meaning" not in u for u in uses.values()) and all(s["items"][k]["asks"] for k in uses) and len(cfg.setting("layer.interventions")) >= 5, uses)
    case("C3", "six rules IB-01 to IB-06 are active on the layer steps; the use text of collection_layer_item.step names 3.1 to 3.3",
         one("SELECT count(*) FROM cfg_method_rule WHERE active=1 AND rule_key LIKE 'IB-0%'") == 6 and "3.1, 3.2 or 3.3" in one("SELECT use FROM cfg_column WHERE table_name='collection_layer_item' AND name='step'"), "")
    found = [e for e in la.find(conn, ROOT) if "layer.reading" in e]
    case("C4", "the alignment check finds nothing wrong in layer.reading with the stage 4 items in it", not found, found[:3])
    bad = json.loads(one("SELECT value FROM cfg_setting WHERE key='layer.reading'"))
    bad["items"]["verse-working"]["uses"] = ["meaning", "nonsense"]
    old = one("SELECT value FROM cfg_setting WHERE key='layer.reading'")
    conn.execute("UPDATE cfg_setting SET value=? WHERE key='layer.reading'", (json.dumps(bad),))
    bad_found = [e for e in la.find(conn, ROOT) if "layer.reading" in e]
    conn.execute("UPDATE cfg_setting SET value=? WHERE key='layer.reading'", (old,))
    case("C5", "the alignment check finds a stage 4 item that uses the meaning item or an item that does not exist", any("meaning" in e for e in bad_found) and any("nonsense" in e for e in bad_found), bad_found[:2])

    # ── the writer: stage and stable key are optional and the defaults are unchanged
    import inspect
    sig = inspect.signature(orec.write)
    case("C6", "orec.write takes optional stage and stable_key (defaults None: the old reading is unchanged)", sig.parameters["stage"].default is None and sig.parameters["stable_key"].default is None, str(sig))

    # ── stages 1 to 3 on the small test collection (as the 2505 test does), then the gates of stage 4
    name = "backsliding"
    cid = one("SELECT id FROM collection WHERE name=? AND deleted=0", name)
    ci.fill(conn, cfg, RUN)
    surf = [r[0] for r in q("SELECT t.surface FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.collection_id=? AND i.deleted=0 ORDER BY t.surface", cid)]
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "3.1", True)
    case("G1", "step 3.1 on a collection with nothing done is refused, naming the steps of stage 3 that are not closed", bool(msg) and "step 1.1 is not closed" in msg and "step 2.1 is not closed" in msg, (msg or "")[:300])
    lr.open_step(conn, cfg, RUN, name, "S1")
    pS, _ = lr.pull(conn, cfg, name, "S1", sc)
    dS = json.loads(pS.read_text(encoding="utf-8"))
    for r in dS["rows"]:
        refs = [e["reference"] for e in r["evidence"]]
        r["fill"].update({"disposition": "observed", "senses": [{"kind": "term", "obs_text": f"In {', '.join(refs)} the word {r['word']} ({r['strong']}) stands in the sense the verses give it; test setup of #2528.",
                                                                  "basis": "stated", "occurrences": refs}]})
    lr.record(conn, cfg, RUN, dS, True)
    lr.check(conn, cfg, RUN, name)
    ci.make_group(conn, RUN, name, "alpha", "test group (#2528 test)")
    ci.make_group(conn, RUN, name, "beta", "test group (#2528 test)")
    half = len(surf) // 2
    ci.place(conn, RUN, name, "alpha", surf[:half], None, "test placement (#2528 test)")
    ci.place(conn, RUN, name, "beta", surf[half:-1], None, "test placement (#2528 test)")
    ci.place(conn, RUN, name, None, [surf[-1]], None, "test isolation (#2528 test)", isolate=True)
    lr.open_step(conn, cfg, RUN, name, "1.1")
    p, _ = lr.pull(conn, cfg, name, "1.1", sc)
    d = json.loads(p.read_text(encoding="utf-8"))
    for r in d["rows"]:
        r["fill"].update({"disposition": "observed", "obs_text": f"The surfaces of the group {r['group']} turn away, which is a movement of the inner being from what it held; test setup of #2528.", "basis": "stated"})
    lr.record(conn, cfg, RUN, d, True)
    lr.check(conn, cfg, RUN, name)
    lr.open_step(conn, cfg, RUN, name, "1.2")
    p, _ = lr.pull(conn, cfg, name, "1.2", sc)
    d = json.loads(p.read_text(encoding="utf-8"))
    for r in d["rows"]:
        r["fill"].update({"disposition": "observed", "obs_text": f"The Strong's codes of {r['group']} ({', '.join(r['strong_codes'])}) define it as a turning away; test setup of #2528.", "basis": "stated"})
    lr.record(conn, cfg, RUN, d, True)
    lr.check(conn, cfg, RUN, name)
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "3.1", True)
    case("G2", "with 1.1 and 1.2 closed and 2.1 not opened, step 3.1 is still refused and names 2.1", bool(msg) and "step 2.1 is not closed" in msg and "step 1.1 is not closed" not in msg, (msg or "")[:200])
    lr.open_step(conn, cfg, RUN, name, "2.1")
    p, _ = lr.pull(conn, cfg, name, "2.1", sc) if lr.derive(conn, cfg, lr.load(conn, cfg, name, pairs=True), "2.1") else (None, 0)
    if p:
        d = json.loads(p.read_text(encoding="utf-8"))
        for r in d["rows"]:
            if s["items"][r["item"]]["none_allowed"]:
                r["fill"].update({"disposition": "none", "reason": "test: nothing to observe for this aspect (#2528 test)"})
            else:
                r["fill"].update({"disposition": "observed", "obs_text": "test setup observation text of at least forty characters (#2528)", "basis": "stated"})
        lr.record(conn, cfg, RUN, d, True)
    rep = lr.check(conn, cfg, RUN, name)
    case("G3", "stages 1 to 3 are closed on the test collection (setup)", all(rep["steps"][k]["closed"] for k in ("S1", "1.1", "1.2", "2.1")), {k: rep["steps"][k]["closed"] for k in ("S1", "1.1", "1.2", "2.1")})

    # ── 3.1: open
    L = lr.load(conn, cfg, name)
    want = sorted({(o["group"], o["osis"]) for o in L["d"]["occurrences"] if o["group"]})
    direct = q("SELECT DISTINCT i.subgroup_id, v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id JOIN surface_term t ON lower(trim(vl.surface))=t.surface "
               "JOIN collection_subgroup_surface i ON i.term_id=t.id AND i.collection_id=? AND i.deleted=0 AND i.state='placed' WHERE vl.deleted=0 AND (i.strong IS NULL OR i.strong=vl.strong)", cid)
    r1 = lr.open_step(conn, cfg, RUN, name, "3.1")
    r2 = lr.open_step(conn, cfg, RUN, name, "3.1")
    rows31 = q("SELECT item, subgroup_id, subject, state FROM collection_layer_item WHERE collection_id=? AND step='3.1' AND state!='retired'", cid)
    case("O1", "opening 3.1 makes one verse-working row for each subgroup and verse the subgroup has an occurrence in (equal to an independent query); opening again changes nothing",
         r1["add"] == len(want) == len(rows31) and r2["add"] == 0 and {(x[1], x[2]) for x in rows31} == set(want) and set(want) <= {(a, b) for a, b in direct} and all(x[0] == "verse-working" and x[3] == "open" for x in rows31),
         f"{len(want)} rows; independent query gives {len(direct)} pairs; {r1}")
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "3.2", True)
    case("O2", "step 3.2 cannot open before 3.1 is closed", bool(msg) and "step 3.1 is not closed" in msg, (msg or "")[:160])

    # ── 3.1: pull
    path, n = lr.pull(conn, cfg, name, "3.1", sc)
    data = json.loads(path.read_text(encoding="utf-8"))
    r0 = data["rows"][0]
    case("P0", "the working file carries the reading rules (RG, RW, RS) once, from the rules of the retired reading steps", len(data["reading_rules"]) >= 40 and any(x["rule"].startswith("RS-10") for x in data["reading_rules"]), len(data["reading_rules"]))
    case("P1", "the working file holds at most pull_max_rows rows, each with the verse in its passage, the occurrences, the uses, the interventions, the node roles and a fill",
         n == min(s["pull_max_rows"], len(want)) and r0["passage"] and r0["occurrences"] and r0["uses"] and r0["interventions"] and "characteristic" in json.dumps(r0["node_roles"]) and r0["fill"]["findings"]
         and "items_absent" in r0["fill"] and r0["meaning_by_code"] and "earlier_observations" in r0, f"{n} rows; {path.name}")

    def good_fill(row, tag, with_absent=True):
        occs = row["occurrences"]
        c = occs[0]
        nodes = [{"occurrence": o["occurrence"], "role": "characteristic" if k == 0 else "standalone"} for k, o in enumerate(occs)]
        f = {"key": "op", "kind": "statement", "basis": "stated", "parts": {"item": "operation", "mode": "done"}, "nodes": nodes,
             "text": f"Ledger row {row['ledger_id']}: the word {c['surface']} ({c['strong']}) carries out the act the verse states at {c['reference']}; test finding {tag} of the stage 4 reading."}
        absent = {str(c["occurrence"]): {it: "the verse shows none of this item; test of the stated-absent rule" for it in [u["item"] for u in row["uses"]] if it != "operation"}}
        # an earlier observation of the verse is answered (RS-04); the setup leaves each one untouched
        existing = [{"observation": e["observation"], "action": "leave", "reason": "test: an earlier observation the stage 4 reading leaves untouched (#2528 test)"} for e in row.get("earlier_observations", [])]
        return {"disposition": "observed", "findings": [f], "items_absent": absent if with_absent else {}, "existing": existing}

    def filled(rows, tag, coll=None, **kw):
        return {"collection": coll or name, "step": "3.1", "rows": [{"ledger_id": r["ledger_id"], "fill": good_fill(r, tag, **kw)} for r in rows]}

    cnt = lambda: (one("SELECT count(*) FROM ib_observation"), one("SELECT count(*) FROM ib_node"))  # noqa: E731
    before = cnt()
    # refusals: each leaves nothing written
    a = filled(data["rows"][:1], "a")
    a["rows"][0]["fill"]["findings"][0]["text"] = " ".join((q("SELECT text FROM verse WHERE osisId=?", r0["subject"])[0][0]).split()[:12])
    b = filled(data["rows"][:1], "b")
    b["rows"][0]["fill"]["findings"][0]["nodes"].append({"occurrence": 1, "role": "standalone"})
    c = filled(data["rows"][:1], "c")
    c["rows"][0]["fill"]["findings"][0]["parts"] = {"item": "meaning"}
    dd = filled(data["rows"][:1], "d")
    dd["rows"][0]["fill"]["findings"] = []
    e = filled(data["rows"][:1], "e")
    e["rows"][0]["fill"] = {"disposition": "none", "reason": "nothing to say here, test of none on a verse-working row"}
    for tag, f_, key in (("a", a, "restates the verse"), ("b", b, "is not an occurrence this row may name"), ("c", c, "parts.item is one of"), ("d", dd, "answered by findings"), ("e", e, "cannot be recorded as none")):
        m = refuses(lr.record, conn, cfg, RUN, f_, True)
        case(f"R1{tag}", f"refused whole, nothing written: {key}", bool(m) and key in m and cnt() == before, (m or "")[-200:])
    # a row that leaves an occurrence with no node, one with no operation finding, a characteristic missing an item
    g = filled(data["rows"][:1], "g")
    g["rows"][0]["fill"]["findings"][0]["parts"] = {"item": "flag", "flag_type": "discovery"}
    g["rows"][0]["fill"]["findings"][0]["basis"] = "stated"
    g["rows"][0]["fill"]["items_absent"] = {str(r0["occurrences"][0]["occurrence"]): {it: "the verse shows none of this item; test" for it in [u["item"] for u in r0["uses"]] if it != "flag"}}
    m = refuses(lr.record, conn, cfg, RUN, g, True)
    case("R3", "a verse with no observation of the item operation is refused", bool(m) and "operation" in m and cnt() == before, (m or "")[-200:])
    h = filled(data["rows"][:1], "h", with_absent=False)
    m = refuses(lr.record, conn, cfg, RUN, h, True)
    case("R4", "a characteristic with an item neither observed nor stated absent is refused, naming the item", bool(m) and "is a characteristic" in m and cnt() == before, (m or "")[-200:])
    i_ = filled(data["rows"][:1], "i")
    i_["rows"][0]["fill"]["findings"][0]["nodes"][0]["role"] = "lexical"
    m = refuses(lr.record, conn, cfg, RUN, i_, True)
    case("R5", "the stage 1 to 3 role lexical is refused on a stage 4 node", bool(m) and cnt() == before, (m or "")[-200:])

    # preview, then record the whole batch
    ok = filled(data["rows"], "ok")
    prev = lr.record(conn, cfg, RUN, ok, False)
    case("R6", "the preview checks and writes nothing", prev["observed"] == len(data["rows"]) and cnt() == before and one("SELECT count(*) FROM ib_observation WHERE stage='layer-3'") == 0, prev)
    res = lr.record(conn, cfg, RUN, ok, True)
    obs = q("SELECT id, tag, stable_key, parts FROM ib_observation WHERE stage='layer-3' AND deleted=0")
    nodes = q("SELECT n.observation_id, count(*), count(n.collection_id), count(n.subgroup_id), sum(n.role IS NULL), sum(n.source_stage='layer-3') FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='layer-3' GROUP BY 1")
    want_nodes = {r["ledger_id"]: len(r["occurrences"]) for r in data["rows"]}
    got_nodes = {int(o[2].split(":")[1]): next(x[1] for x in nodes if x[0] == o[0]) for o in obs}
    case("R7", "one observation for each row, stage layer-3, kind statement, a stable key tying it to its ledger row; each has a node for every occurrence of its row with a role, a collection and a subgroup",
         res["observed"] == len(data["rows"]) == len(obs) and got_nodes == want_nodes and all(x[1] == x[2] == x[3] and not x[4] and x[1] == x[5] for x in nodes) and all(o[1] == "statement" and json.loads(o[3])["item"] == "operation" for o in obs), f"{res}; nodes {got_nodes}")
    case("R8", "the ledger rows are observed, carry the stated-absent items, and are not yet validated",
         one("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND step='3.1' AND state='observed' AND observation_id IS NOT NULL AND validated=0 AND reason LIKE 'row_state:%'", cid) == len(data["rows"]), "")
    case("R9", "the same file again is not accepted once the rows are recorded and unvalidated rows are re-recordable: it withdraws and writes again (re-record)",
         lr.record(conn, cfg, RUN, ok, False)["withdrawn"] == len(data["rows"]) and one("SELECT count(*) FROM ib_observation WHERE stage='layer-3' AND deleted=0") == len(data["rows"]), "")

    # ── check
    rep = lr.check(conn, cfg, RUN, name)
    st = rep["steps"]["3.1"]
    case("K1", "LayerCheck validates the recorded rows; the step is not closed while rows are open", st["validated"] == len(data["rows"]) and st["open"] == len(want) - len(data["rows"]) and not st["failed"] and (st["closed"] == (len(data["rows"]) == len(want))), {k: st[k] for k in ("rows", "validated", "open")})
    # record the remaining batches until the step is complete
    guard = 0
    while lr.step_closed(conn, cid, "3.1") is False and guard < 6:
        guard += 1
        try:
            pth, nn = lr.pull(conn, cfg, name, "3.1", sc)
        except lr.LayerError:
            break
        dt = json.loads(pth.read_text(encoding="utf-8"))
        lr.record(conn, cfg, RUN, filled(dt["rows"], f"b{guard}"), True)
        lr.check(conn, cfg, RUN, name)
    rep = lr.check(conn, cfg, RUN, name)
    case("K2", "after every row is recorded, step 3.1 closes", rep["steps"]["3.1"]["closed"] and rep["steps"]["3.1"]["validated"] == len(want), rep["steps"]["3.1"]["failed"][:2])
    # tamper: a node removed from a stage 4 observation, the occurrence it carried is no longer carried
    victim = q("SELECT n.id, n.observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='layer-3' AND n.deleted=0 AND n.role='standalone' LIMIT 1")
    if victim:
        conn.execute("UPDATE ib_node SET deleted=1 WHERE id=?", (victim[0][0],))
        rep = lr.check(conn, cfg, RUN, name)
        case("K3", "a node removed from a stage 4 observation: the row fails (an occurrence carries no node), validated is cleared, the step is not closed",
             not rep["steps"]["3.1"]["closed"] and len(rep["steps"]["3.1"]["failed"]) == 1 and "carry no node" in rep["steps"]["3.1"]["failed"][0], rep["steps"]["3.1"]["failed"])
        conn.execute("UPDATE ib_node SET deleted=0 WHERE id=?", (victim[0][0],))
        rep = lr.check(conn, cfg, RUN, name)
        case("K4", "the node restored: step 3.1 closes again", rep["steps"]["3.1"]["closed"], "")
    else:
        case("K3", "no standalone node on this collection to remove (every row has a single occurrence)", True, "")
    # tamper: the operation observation withdrawn
    op1 = q("SELECT o.id FROM ib_observation o WHERE o.stage='layer-3' AND o.deleted=0 LIMIT 1")[0][0]
    conn.execute("UPDATE ib_observation SET deleted=1 WHERE id=?", (op1,))
    rep = lr.check(conn, cfg, RUN, name)
    case("K5", "an observation withdrawn from a stage 4 row: the row fails (its observations are missing) and the step is not closed", not rep["steps"]["3.1"]["closed"] and len(rep["steps"]["3.1"]["failed"]) == 1, rep["steps"]["3.1"]["failed"])
    conn.execute("UPDATE ib_observation SET deleted=0 WHERE id=?", (op1,))
    rep = lr.check(conn, cfg, RUN, name)
    case("K6", "restored: step 3.1 closes again", rep["steps"]["3.1"]["closed"], "")

    # ── an earlier inner-being observation on a verse is shown with its flags and is accepted, modified or deleted with a reason
    ref0 = r0["occurrences"][0]
    old_id = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, basis, parts, meaning_source, status, run_id, created_at) VALUES (NULL,'prior-capture','statement',?,'stated',?,'verse-text','draft',?,'2026-11-15T00:00:00Z')",
                          (f"Test earlier observation at {ref0['reference']} for the stage 4 reading to check (#2528 test).", json.dumps({"item": "operation", "mode": "done"}), RUN)).lastrowid
    conn.execute("INSERT INTO ib_node (observation_id, strong, verse_reference, surface, morph_code, source_stage, seq, role, created_at, verse_lexical_id, collection_id) VALUES (?,?,?,?,?,'prior-capture',1,'characteristic','2026-11-15T00:00:00Z',?,?)",
                 (old_id, ref0["strong"], r0["subject"], ref0["surface"], ref0["morph"], ref0["occurrence"], cid))
    row_id = r0["ledger_id"]
    conn.execute("UPDATE collection_layer_item SET validated=0 WHERE id=?", (row_id,))
    pth, _ = lr.pull(conn, cfg, name, "3.1", sc)
    dt = json.loads(pth.read_text(encoding="utf-8"))
    mine = [r for r in dt["rows"] if r["ledger_id"] == row_id][0]
    shown = [x for x in mine["earlier_observations"] if x["observation"] == old_id]
    case("E1", "the pull shows an earlier inner-being observation of the verse with its nodes and flags", bool(shown) and shown[0]["nodes"] and "flags" in shown[0], shown[0]["flags"] if shown else "not shown")
    fill = good_fill(mine, "earlier")
    one_row = lambda f: {"collection": name, "step": "3.1", "rows": [{"ledger_id": row_id, "fill": f}]}  # noqa: E731
    unanswered = dict(fill, existing=[e for e in fill["existing"] if e["observation"] != old_id])
    m = refuses(lr.record, conn, cfg, RUN, one_row(unanswered), True)
    case("E4", "an earlier observation with a node on the verse that the file does not answer is refused (RS-04: none is passed over)", bool(m) and "needs an action" in m, (m or "")[-200:])
    fill["existing"] = [dict(e, action="delete") if e["observation"] == old_id else e for e in fill["existing"]]
    for e in fill["existing"]:
        if e["observation"] == old_id:
            e.pop("reason")
    m = refuses(lr.record, conn, cfg, RUN, one_row(fill), True)
    case("E2", "an action on an earlier observation needs its reason", bool(m) and "needs its reason" in m, (m or "")[-160:])
    accept = dict(fill, existing=[dict(e, action="accept", reason="the earlier observation states the operation and is kept (test of #2528)") if e["observation"] == old_id else e for e in fill["existing"]])
    lr.record(conn, cfg, RUN, one_row(accept), True)
    kept_note = one("SELECT reason FROM collection_layer_item WHERE id=?", row_id)
    case("E5", "an earlier observation accepted is kept on the row: the ledger names it and the check passes the row", f'"kept": [{old_id}]' in (kept_note or "") and lr.check(conn, cfg, RUN, name)["steps"]["3.1"]["failed"] == [], kept_note)
    fill["existing"] = [dict(e, reason="the finding is replaced by the stage 4 finding of this row (test of #2528)") if e["observation"] == old_id else e for e in fill["existing"]]
    conn.execute("UPDATE collection_layer_item SET validated=0 WHERE id=?", (row_id,))      # the check above validated the row; it is answered again
    lr.record(conn, cfg, RUN, one_row(fill), True)
    case("E3", "the earlier observation is deleted with its reason kept in ib_observation_change and the row is answered again",
         one("SELECT deleted FROM ib_observation WHERE id=?", old_id) == 1 and one("SELECT count(*) FROM ib_observation_change WHERE observation_id=? AND column_name='deleted'", old_id) >= 1, "")
    lr.check(conn, cfg, RUN, name)

    # ── 3.2
    r32 = lr.open_step(conn, cfg, RUN, name, "3.2")
    groups = {g for g, _ in want}
    case("O3", "step 3.2 opens after 3.1 closes with one row for each subgroup that has occurrences", r32["add"] == len(groups) == one("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND step='3.2' AND state!='retired'", cid), r32)
    p32, n32 = lr.pull(conn, cfg, name, "3.2", sc)
    d32 = json.loads(p32.read_text(encoding="utf-8"))
    below = d32["rows"][0]["observations_of_the_steps_below"]
    case("P2", "the 3.2 working file shows the observations of step 3.1 the row may rest on", bool(below), len(below))

    def fill32(row, tag, traced=True):
        occs = row["occurrences"]
        nodes = [{"occurrence": o["occurrence"], "role": "characteristic" if k == 0 else "standalone"} for k, o in enumerate(occs)][:80]
        if traced:
            nodes += [{"traced": b["observation"]} for b in row["observations_of_the_steps_below"][:2]]
        return {"disposition": "observed", "findings": [{"key": "g1", "kind": "statement", "basis": "stated", "parts": {"item": "operation", "mode": "done"}, "nodes": nodes,
                                                         "text": f"Ledger row {row['ledger_id']}: across its verses the group {row['group']} works as one act of turning, which no single verse shows alone; test finding {tag} of step 3.2."}]}

    before = cnt()
    m = refuses(lr.record, conn, cfg, RUN, {"collection": name, "step": "3.2", "rows": [{"ledger_id": d32["rows"][0]["ledger_id"], "fill": fill32(d32["rows"][0], "x", traced=False)}]}, True)
    case("R10", "a 3.2 finding that rests on no observation of the step below is refused", bool(m) and "rests on no observation of the step below" in m and cnt() == before, (m or "")[-200:])
    lr.record(conn, cfg, RUN, {"collection": name, "step": "3.2", "rows": [{"ledger_id": r["ledger_id"], "fill": fill32(r, "y")} for r in d32["rows"]]}, True)
    rep = lr.check(conn, cfg, RUN, name)
    case("K7", "LayerCheck validates the 3.2 rows and closes step 3.2", rep["steps"]["3.2"]["closed"] and rep["steps"]["3.2"]["validated"] == len(groups), rep["steps"]["3.2"]["failed"][:2])
    # ── 3.3
    L2 = lr.load(conn, cfg, name, pairs=True)
    d33 = lr.derive(conn, cfg, L2, "3.3")
    r33 = lr.open_step(conn, cfg, RUN, name, "3.3")
    case("O4", "step 3.3 opens after 3.2 closes; its rows equal the pairs of subgroups and the partner collections that reach the thresholds", r33["demanded"] == len(d33) and r33["add"] == len(d33), f"{len(d33)} rows demanded: {[x['subject'] for x in d33][:4]}")
    if d33:
        p33, _ = lr.pull(conn, cfg, name, "3.3", sc)
        dd33 = json.loads(p33.read_text(encoding="utf-8"))
        lr.record(conn, cfg, RUN, {"collection": name, "step": "3.3", "rows": [{"ledger_id": r["ledger_id"], "fill": {"disposition": "none", "reason": "test: the shared verses show no working together (#2528 test)"}} for r in dd33["rows"]]}, True)
        rep = lr.check(conn, cfg, RUN, name)
        case("K8", "every 3.3 row answered as none with its reason validates", rep["steps"]["3.3"]["validated"] == len(dd33["rows"]), rep["steps"]["3.3"])
    else:
        case("K8", "no 3.3 aspect is demanded on this small collection (no pair of subgroups or partner collection reaches the threshold)", True, "")

    # ── a change of the grouping reopens the rows
    ci.make_group(conn, RUN, name, "gamma", "test group (#2528 test)")
    ci.place(conn, RUN, name, "gamma", [surf[0]], None, "test move (#2528 test)")
    rep = lr.check(conn, cfg, RUN, name)
    r31 = rep["steps"]["3.1"]
    case("M1", "moving a surface to another group makes stage 4 rows fail or missing and step 3.1 is no longer closed", not r31["closed"] and (r31["failed"] or r31["not_in_ledger"]), f"failed {r31['failed'][:1]} missing {r31['not_in_ledger'][:1]}")
    # ── the refusal of an occurrence with no node, on a second small collection with a verse that holds a word twice (one row of several occurrences)
    n2 = "betray"
    c2 = one("SELECT id FROM collection WHERE name=? AND deleted=0", n2)
    surf2 = [r[0] for r in q("SELECT t.surface FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.collection_id=? AND i.deleted=0 ORDER BY t.surface", c2)]
    lr.open_step(conn, cfg, RUN, n2, "S1")
    pS, _ = lr.pull(conn, cfg, n2, "S1", sc)
    dS = json.loads(pS.read_text(encoding="utf-8"))
    for r in dS["rows"]:
        refs = [e["reference"] for e in r["evidence"]]
        r["fill"].update({"disposition": "observed", "senses": [{"kind": "term", "obs_text": f"In {', '.join(refs)} the word {r['word']} ({r['strong']}) stands in the sense the verses give it; second test collection of #2528.",
                                                                  "basis": "stated", "occurrences": refs}]})
    lr.record(conn, cfg, RUN, dS, True)
    lr.check(conn, cfg, RUN, n2)
    ci.make_group(conn, RUN, n2, "alpha", "test group (#2528 test)")
    ci.place(conn, RUN, n2, "alpha", surf2, None, "test placement (#2528 test)")
    for step_, txt in (("1.1", "The surfaces of the group {g} of the second test collection turn away, which is a movement of the inner being from what it held; test setup of #2528."),
                       ("1.2", "The Strong's codes of {g} ({c}) in the second test collection define it as a turning away; test setup of #2528.")):
        lr.open_step(conn, cfg, RUN, n2, step_)
        pp, _ = lr.pull(conn, cfg, n2, step_, sc)
        dd = json.loads(pp.read_text(encoding="utf-8"))
        for r in dd["rows"]:
            r["fill"].update({"disposition": "observed", "obs_text": txt.format(g=r["group"], c=", ".join(r.get("strong_codes") or [])), "basis": "stated"})
        lr.record(conn, cfg, RUN, dd, True)
        lr.check(conn, cfg, RUN, n2)
    lr.open_step(conn, cfg, RUN, n2, "2.1")
    if lr.derive(conn, cfg, lr.load(conn, cfg, n2, pairs=True), "2.1"):
        pp, _ = lr.pull(conn, cfg, n2, "2.1", sc)
        dd = json.loads(pp.read_text(encoding="utf-8"))
        for r in dd["rows"]:
            if s["items"][r["item"]]["none_allowed"]:
                r["fill"].update({"disposition": "none", "reason": "test: nothing to observe for this aspect (#2528 test)"})
            else:
                r["fill"].update({"disposition": "observed", "obs_text": "second test collection setup observation text of at least forty characters (#2528)", "basis": "stated"})
        lr.record(conn, cfg, RUN, dd, True)
    lr.check(conn, cfg, RUN, n2)
    lr.open_step(conn, cfg, RUN, n2, "3.1")
    multi, guard = None, 0
    while multi is None and guard < 8:
        guard += 1
        pp, _ = lr.pull(conn, cfg, n2, "3.1", sc)
        dd = json.loads(pp.read_text(encoding="utf-8"))
        multi = next((r for r in dd["rows"] if len(r["occurrences"]) >= 2), None)
        if multi is None:
            lr.record(conn, cfg, RUN, filled(dd["rows"], f"s{guard}", coll=n2), True)
    if multi is None:
        case("R2", "no row of the second test collection has several occurrences: the refusal could not be exercised", False, "")
    else:
        f2 = filled([multi], "f", coll=n2)
        f2["rows"][0]["fill"]["findings"][0]["nodes"] = f2["rows"][0]["fill"]["findings"][0]["nodes"][:1]
        b4 = cnt()
        m = refuses(lr.record, conn, cfg, RUN, f2, True)
        case("R2", "an occurrence of a row with several occurrences left with no node is refused (every occurrence is read), nothing written", bool(m) and "carry no node" in m and cnt() == b4, f"{len(multi['occurrences'])} occurrences; " + (m or "")[-160:])
        ok2 = filled([multi], "g", coll=n2)
        lr.record(conn, cfg, RUN, ok2, True)
        rep2 = lr.check(conn, cfg, RUN, n2)
        case("R11", "the same row with a node on every occurrence (one characteristic, the others standalone) is recorded and validates",
             rep2["steps"]["3.1"]["failed"] == [] and one("SELECT validated FROM collection_layer_item WHERE id=?", multi["ledger_id"]) == 1, rep2["steps"]["3.1"]["failed"][:2])
    conn.commit()
    return 0


if __name__ == "__main__":
    db, scratch = sys.argv[1], sys.argv[2]
    rc = 0
    try:
        main(db, scratch)
    except Exception as exc:  # report what ran, then the failure
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
