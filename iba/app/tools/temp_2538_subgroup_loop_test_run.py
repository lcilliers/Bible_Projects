"""temp_2538_subgroup_loop_test_run.py -- tests for the loop over the subgroups (escalation #2538, researcher 2026-11-24: each subgroup in isolation).

The words (S1), then 1.1, 1.2, 2.1 and 3.1 are opened, pulled and answered for one subgroup at a time: -Subgroup on LayerOpen and LayerPull, the needs of a step judged for the
subgroup, the evidence gate of 3.1 judged for the subgroup. Runs against a COPY of iba.db that holds the migrations (never the live database); the small collection backsliding is split
in two subgroups on the copy.

Usage: python iba/app/tools/temp_2538_subgroup_loop_test_run.py <db copy> <scratch dir>
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import buildvalidate as bv  # noqa: E402
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib import collectionvalidate as cvalid  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import validationactions as va  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []
RUN = "TEST-2538-LOOP"


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
    cfg = Cfg(pathlib.Path(db))
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp); _sp.loader.exec_module(_m)
    _m.apply_to_copy(cfg.conn)
    conn = cfg.conn
    sc = pathlib.Path(scratch)
    name = "backsliding"
    cid = conn.execute("SELECT id FROM collection WHERE name=? AND deleted=0", (name,)).fetchone()[0]
    try:
        ci.fill(conn, cfg, RUN)
        s = lr.settings(cfg)
        case("C1", "step S1 is opened only after the grouping (after_grouping) and node subgroup_id is required from layer 0",
             any(x["key"] == "S1" and x.get("after_grouping") for x in s["steps"]) and s["node_required_from_layer"]["subgroup_id"] == 0, "")
        msg = refuses(lr.open_step, conn, cfg, RUN, name, "S1", True)
        case("C2", "S1 before the grouping is refused, naming the surfaces not placed", bool(msg) and "not placed" in msg, (msg or "")[:200])

        def settle_scope():
            for oid_ in sorted(cvalid.scope(conn, cid)["union"]):
                o_ = conn.execute("SELECT stage, nature FROM ib_observation WHERE id=?", (oid_,)).fetchone()
                if o_[0] not in bv.build_stages(s) and o_[1] is None:
                    va.set_nature(cfg, conn, oid_, "evidence", "test setup: an older observation kept as evidence", RUN, "Claude")
                    orec.log(conn, oid_, None, "build_answer", None, "keep", "test setup: kept as evidence", None, RUN, "Claude")
                for nid_, in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND disposition_note IS NULL AND "
                                          "(strong IS NULL OR verse_reference IS NULL OR surface IS NULL OR morph_code IS NULL OR role IS NULL OR verse_lexical_id IS NULL OR collection_id IS NULL)", (oid_,)).fetchall():
                    va.note_node(conn, nid_, "test setup: a node of an older observation whose data gives no more", RUN, "Claude")
        surf = [r[0] for r in conn.execute("SELECT t.surface FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.collection_id=? AND i.deleted=0 ORDER BY t.surface", (cid,))]
        ci.make_group(conn, RUN, name, "alpha", "test group (#2538 loop test)")
        ci.make_group(conn, RUN, name, "beta", "test group (#2538 loop test)")
        half = len(surf) // 2
        ci.place(conn, RUN, name, "alpha", surf[:half], None, "test placement (#2538 loop test)")
        ci.place(conn, RUN, name, "beta", surf[half:], None, "test placement (#2538 loop test)")
        L = lr.load(conn, cfg, name)
        ga = [g["id"] for g in L["groups"].values() if g["name"] == "alpha"][0]
        gb = [g["id"] for g in L["groups"].values() if g["name"] == "beta"][0]
        msg = refuses(lr.open_step, conn, cfg, RUN, name, "S1", True, "nope")
        case("C3", "an unknown subgroup is refused, naming the live ones", bool(msg) and "alpha" in msg and "beta" in msg, (msg or "")[:160])

        r = lr.open_step(conn, cfg, RUN, name, "S1", subgroup="alpha")
        rows = conn.execute("SELECT subgroup_id, count(*) FROM collection_layer_item WHERE collection_id=? AND step='S1' AND deleted=0 AND state!='retired' GROUP BY 1", (cid,)).fetchall()
        case("C4", "opening S1 for alpha adds the words of alpha only, each row carrying the subgroup of its surface", r["add"] > 0 and {x[0] for x in rows} == {ga}, rows)
        before = conn.execute("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND step='S1' AND deleted=0", (cid,)).fetchone()[0]
        before_pull = conn.execute("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND step='S1' AND deleted=0 AND item!='old-observation'", (cid,)).fetchone()[0]     # the pull's rows: the words (the old observations are listed in its head)
        lr.open_step(conn, cfg, RUN, name, "S1", subgroup="alpha")
        case("C5", "opening it again changes nothing", conn.execute("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND step='S1' AND deleted=0", (cid,)).fetchone()[0] == before, "")
        p, n = lr.pull(conn, cfg, name, "S1", sc, subgroup="alpha")
        d = json.loads(p.read_text(encoding="utf-8"))
        case("C6", "the pull for alpha holds the open rows of alpha and the rows of beta are not there", n == len(d["rows"]) == before_pull, f"{n} rows")
        msg = refuses(lr.pull, conn, cfg, name, "S1", sc, "beta")
        case("C7", "a pull for beta, whose S1 was not opened, has no open row and says so", bool(msg) and "no open row" in msg, (msg or "")[:160])
        msg = refuses(lr.open_step, conn, cfg, RUN, name, "1.1", True, "alpha")
        case("C8", "1.1 for alpha is refused while the words of alpha are not answered", bool(msg) and "step S1 is not closed" in msg, (msg or "")[:200])
        for r_ in d["rows"]:
            refs = [e["reference"] for e in r_["evidence"]]
            r_["fill"].update({"disposition": "observed", "senses": [{"kind": "term", "obs_text": f"In {', '.join(refs)} the word {r_['word']} ({r_['strong']}) stands in the sense the verses give it; test setup of #2538.",
                                                                      "basis": "stated", "occurrences": refs}]})
        settle_scope()
        d_ = lr.record(conn, cfg, RUN, d, True)
        lr.check(conn, cfg, RUN, name)
        case("C9", "once the words of alpha are answered and checked, S1 is closed for alpha and not for beta", lr.step_closed(conn, cid, "S1", ga) and not lr.step_closed(conn, cid, "S1", gb), d_)
        o = lr.open_step(conn, cfg, RUN, name, "1.1", subgroup="alpha")
        case("C10", "1.1 then opens for alpha although beta has no word read", o["add"] == 1, o)
        # a 1.1 row answered by an observation older than the S1 reading is stale; LayerOpen reopens it, and not a row answered after it
        old_obs = conn.execute("SELECT id FROM ib_observation WHERE deleted=0 AND created_at < (SELECT min(o2.created_at) FROM collection_layer_item i JOIN ib_observation o2 ON o2.id=i.observation_id "
                               "WHERE i.collection_id=? AND i.step='S1' AND i.subgroup_id=?) ORDER BY id LIMIT 1", (cid, ga)).fetchone()
        r11 = conn.execute("SELECT id FROM collection_layer_item WHERE collection_id=? AND step='1.1' AND subgroup_id=? AND deleted=0", (cid, ga)).fetchone()
        s_ = conn.execute("SELECT i.observation_id FROM collection_layer_item i JOIN ib_observation o ON o.id=i.observation_id WHERE i.collection_id=? AND i.step='S1' AND i.subgroup_id=? AND i.state='observed' ORDER BY o.created_at DESC LIMIT 1", (cid, ga)).fetchone()
        conn.execute("UPDATE collection_layer_item SET state='observed', observation_id=?, validated=1 WHERE id=?", (old_obs[0], r11[0]))
        o25 = lr.open_step(conn, cfg, RUN, name, "1.1", subgroup="alpha")
        st25 = conn.execute("SELECT state, validated FROM collection_layer_item WHERE id=?", (r11[0],)).fetchone()
        conn.execute("UPDATE collection_layer_item SET state='observed', observation_id=?, validated=1 WHERE id=?", (s_[0], r11[0]))
        o25b = lr.open_step(conn, cfg, RUN, name, "1.1", subgroup="alpha")
        case("C25", "a 1.1 row answered before the S1 reading was recorded is reopened by LayerOpen; one answered after it is left", o25["revive"] == 1 and tuple(st25) == ("open", 0) and o25b["revive"] == 0, (o25, o25b))
        # a whole-collection S1 row (subgroup 0) of a word the subgroup reads is retired and its observation withdrawn when the subgroup's S1 is opened again
        subj = conn.execute("SELECT subject FROM collection_layer_item WHERE collection_id=? AND step='S1' AND subgroup_id=? AND state!='retired' LIMIT 1", (cid, ga)).fetchone()[0]
        lg = conn.execute("INSERT INTO collection_layer_item (collection_id, step, item, subgroup_id, subject, state, observation_id, validated, run_id, created_by) VALUES (?,?,?,?,?,?,?,1,?,?)",
                          (cid, "S1", "word-sense", 0, subj, "observed", old_obs[0], RUN, "test")).lastrowid
        o26 = lr.open_step(conn, cfg, RUN, name, "S1", subgroup="alpha")
        st26 = conn.execute("SELECT state FROM collection_layer_item WHERE id=?", (lg,)).fetchone()[0]
        dl26 = conn.execute("SELECT deleted FROM ib_observation WHERE id=?", (old_obs[0],)).fetchone()[0]
        case("C26", "a whole-collection S1 row of a word the subgroup now reads is retired by LayerOpen and its observation withdrawn", o26["legacy"] == 1 and st26 == "retired" and dl26 == 1, o26)
        msg = refuses(lr.open_step, conn, cfg, RUN, name, "1.1", True, "beta")
        case("C11", "1.1 for beta is still refused (by the loop order while alpha is further through its loop, or by the S1 gate)", bool(msg) and ("step S1 is not closed" in msg or "one subgroup at a time" in msg), (msg or "")[:160])
        g_alpha = bv.closing_gate(conn, cfg, cid, "evidence", ga)
        g_all = bv.closing_gate(conn, cfg, cid, "evidence")
        case("C12", "the evidence gate of a subgroup is no longer than the gate of the collection", len(g_alpha) <= len(g_all), (g_alpha[:1], g_all[:1]))
        # the WordNet control of step 2.1: checked against a direct query written here
        L2 = lr.load(conn, cfg, name, pairs=True)
        wn = lr.wordnet_control(conn, L2, ga)
        ct = lr.control_for(L2, ga, wn)
        mine = {r[1] for r in L2["index"] if r[4] == ga and r[5] == "placed"}
        direct = 0
        for a_, b_ in conn.execute("SELECT term_a_id, term_b_id FROM surface_relation WHERE deleted=0"):
            for x, y in ((a_, b_), (b_, a_)):
                if x in mine and y not in mine:
                    direct += len(conn.execute("SELECT DISTINCT c.name FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 AND c.status='confirmed' AND c.id!=? AND l.term_id=?", (cid, y)).fetchall())
        case("C13", "the WordNet control counts the same pairs as a direct query (a surface of the subgroup related to a member of another collection)", sum(v["pairs"] for v in wn.values()) == direct, f"{direct} pairs")
        case("C14", "the control sets are disjoint and complete: both, wordnet_only and verse_only; both and wordnet_only make the WordNet collections; both and verse_only the verse ones",
             set(ct["both"]) | set(ct["wordnet_only"]) == set(wn) and set(ct["both"]) | set(ct["verse_only"]) == set(ct["verse_pairings"])
             and not (set(ct["both"]) & set(ct["wordnet_only"])) and not (set(ct["both"]) & set(ct["verse_only"])), {k: len(v) for k, v in ct.items() if isinstance(v, list)})
        # backsliding has no WordNet pair to another collection, so the same comparison is made on thought, whose subgroups have many
        Lt = lr.load(conn, cfg, "thought", pairs=True)
        tcid = Lt["cid"]
        bad, total = [], 0
        for gid_, g_ in list(Lt["groups"].items())[:4]:
            wn_ = lr.wordnet_control(conn, Lt, gid_)
            mine_ = {r[1] for r in Lt["index"] if r[4] == gid_ and r[5] == "placed"}
            d_ = 0
            for a_, b_ in conn.execute("SELECT term_a_id, term_b_id FROM surface_relation WHERE deleted=0"):
                for x, y in ((a_, b_), (b_, a_)):
                    if x in mine_ and y not in mine_:
                        d_ += len(conn.execute("SELECT DISTINCT c.name FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 AND c.status='confirmed' AND c.id!=? AND l.term_id=?", (tcid, y)).fetchall())
            total += d_
            if sum(v["pairs"] for v in wn_.values()) != d_:
                bad.append((g_["name"], sum(v["pairs"] for v in wn_.values()), d_))
        case("C15", "on thought the WordNet control counts the same pairs as a direct query for four subgroups, and there are pairs to count", not bad and total > 0, bad or f"{total} pairs")
        # the sweep of the unmarked observations (step 2.1, one subgroup), on thought whose subgroups hold older observations
        gt = None
        for gid_, g_ in Lt["groups"].items():
            um = lr.unmarked_of(conn, cfg, s, Lt, gid_)
            if len(um) >= 2:
                gt, cand = gid_, um
                break
        case("C16", "the unmarked observations of a subgroup are older, live, have no marker and sit on its occurrences", gt is not None and all(v["nature"] is None for v in cand.values()), f"{len(cand) if gt else 0} candidates")
        vls = {o["vl_id"] for o in Lt["d"]["occurrences"] if o["group"] == gt}
        on = {r[0] for r in conn.execute(f"SELECT DISTINCT observation_id FROM ib_node WHERE deleted=0 AND verse_lexical_id IN ({','.join('?' * len(vls))})", list(vls))}
        case("C17", "every candidate holds a live node on an occurrence of the subgroup", set(cand) <= on, "")
        outsider = conn.execute("SELECT id FROM ib_observation WHERE deleted=0 AND nature IS NOT NULL LIMIT 1").fetchone()[0]
        probs = bv.sweep(cfg, conn, [{"observation": outsider, "reason": "an observation that is not in the list of candidates"}], cand, RUN)
        probs2 = bv.sweep(cfg, conn, [{"observation": next(iter(cand)), "reason": "short"}], cand, RUN)
        case("C18", "a name outside the candidates and a short reason are each refused", len(probs) == 1 and "not in the unmarked" in probs[0] and len(probs2) == 1 and "20 characters" in probs2[0], (probs, probs2))
        conn.execute("SAVEPOINT sweep_t")
        done = None
        for oid_ in [k for k, v in cand.items() if not v['elsewhere']]:
            p_ = bv.sweep(cfg, conn, [{"observation": oid_, "reason": "test: states nothing of the verse and nothing of the inner being, so it contributes nothing"}], cand, RUN)
            if not p_:
                done = oid_
                break
        row = conn.execute("SELECT deleted, nature FROM ib_observation WHERE id=?", (done,)).fetchone() if done else None
        logged = conn.execute("SELECT count(*) FROM ib_observation_change WHERE observation_id=? AND column_name='build_answer' AND run_id=?", (done, RUN)).fetchone()[0] if done else 0
        after = lr.unmarked_of(conn, cfg, s, Lt, gt)
        case("C19", "a candidate deleted by the sweep is soft-deleted, still unmarked, answered in the log, and no longer a candidate", bool(done) and tuple(row) == (1, None) and logged == 1 and done not in after, (done, row, logged))
        conn.execute("ROLLBACK TO sweep_t")
        conn.execute("RELEASE sweep_t")
        d_ = {"collection": "thought", "step": "2.1", "rows": [], "delete_unmarked": [{"observation": done or 0, "reason": "test reason that is long enough to pass"}]}
        msg = refuses(lr.record, conn, cfg, RUN, d_, False)
        case("C20", "delete_unmarked in a file that names no subgroup is refused", bool(msg) and "names no subgroup" in msg, (msg or "")[:200])
        shared = [k for k, v in cand.items() if v["elsewhere"]]
        if not shared:   # look through the other subgroups of thought for a candidate that has nodes elsewhere
            for gid2 in Lt["groups"]:
                um2 = lr.unmarked_of(conn, cfg, s, Lt, gid2)
                shared = [k for k, v in um2.items() if v["elsewhere"]]
                if shared:
                    cand2 = um2
                    break
        else:
            cand2 = cand
        pr = bv.sweep(cfg, conn, [{"observation": shared[0], "reason": "test: states nothing of the verse and nothing of the inner being"}], cand2, RUN) if shared else []
        case("C21", "an observation that also holds nodes outside the subgroup is shown with the count and refused for deletion", bool(shared) and len(pr) == 1 and "outside this subgroup" in pr[0], (pr or "no shared candidate found")[:1])
        # the record of a file with delete_unmarked and a subgroup, as a preview: written, counted, then rolled back
        gname = Lt["groups"][gt]["name"]
        d2 = {"collection": "thought", "step": "2.1", "subgroup": gname, "rows": [], "delete_unmarked": [{"observation": done, "reason": "test: states nothing of the verse and nothing of the inner being"}]}
        res = lr.record(conn, cfg, RUN, d2, False)
        live = conn.execute("SELECT deleted FROM ib_observation WHERE id=?", (done,)).fetchone()[0]
        case("C22", "the record of a 2.1 file for one subgroup carries delete_unmarked through; the preview deletes nothing", res.get("deleted_unmarked") == 1 and live == 0, res)
        d3 = {"collection": "thought", "step": "2.1", "subgroup": gname, "rows": [], "delete_unmarked": [{"observation": outsider, "reason": "an observation that is not in the list of candidates"}]}
        msg = refuses(lr.record, conn, cfg, RUN, d3, True)
        case("C23", "the record refuses the whole file for a name outside the candidates", bool(msg) and "not in the unmarked" in msg, (msg or "")[:160])
        # config behind the code: the one plain message in place of a KeyError
        real = cfg.setting
        cfg.setting = lambda k, *a, **kw: None if k == "layer.scan" else real(k, *a, **kw)
        try:
            msg = refuses(lr.settings, cfg)
        finally:
            cfg.setting = real
        case("C24", "config behind the code is named plainly with the migration to apply", bool(msg) and "ahead of the config" in msg and "validation_in_build" in msg, (msg or "")[:200])
    finally:
        conn.rollback()
    print("| case | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    print(f"\n{sum(1 for r in results if r[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r[2] == "PASS" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
