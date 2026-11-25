"""temp_2538_validation_in_build_test_run.py -- tests for the validation made part of the build (escalation #2538; plan outputs/escalation/2538-validation-in-the-build-plan-v1-20261124.md;
migration validation_in_build_2538_v1_20261124, lib/buildvalidate.py, lib/scanguard.py, lib/collectionvalidate.py, lib/validationactions.py trace_gaps, lib/layerreading.py, lib/layerinner.py).

Each case checks the tables against a direct query written here, not against the library's own lists, and runs the refusals. Runs against a COPY of iba.db that holds both #2538
migrations (never the live database). The test rows are made on one verse_lexical occurrence that no observation has a node on, so nothing real is involved.

Usage: python iba/app/tools/temp_2538_validation_in_build_test_run.py <db copy>
"""
import json
import math
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import buildvalidate as bv  # noqa: E402
from iba.app.lib import collectionvalidate as cv  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import scanguard as sg  # noqa: E402
from iba.app.lib import validationactions as va  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []
RUN = "TEST-2538-BUILD"


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:330]))
    print(f"[{results[-1][2]}] {cid}: {results[-1][3][:160]}", file=sys.stderr, flush=True)


def main(db):
    cfg = Cfg(pathlib.Path(db))
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp); _sp.loader.exec_module(_m)
    _m.apply_to_copy(cfg.conn)
    conn = cfg.conn
    q = lambda s, *a: conn.execute(s, a).fetchall()  # noqa: E731
    one = lambda s, *a: conn.execute(s, a).fetchone()[0]  # noqa: E731
    s = lr.settings(cfg)
    scan = sg.settings(cfg)
    cid = one("SELECT id FROM collection WHERE name='backsliding' AND deleted=0")
    other_cid = one("SELECT id FROM collection WHERE name='thought' AND deleted=0")

    # ── configuration
    case("C1", "layer.scan is set; 3.1 opens on the evidence gate and 3.3 closes on the whole; RW-13 and RW-14 exist; the four indexes exist and are registered in cfg_index",
         scan["max_vm_ops"] > 0 and scan["chunk"] > 0
         and [x.get("open_gate") for x in s["steps"] if x["key"] == "3.1"] == ["evidence"] and [x.get("closing_gate") for x in s["steps"] if x["key"] == "3.3"] == [True]
         and one("SELECT count(*) FROM cfg_method_rule WHERE active=1 AND (rule_key LIKE 'RW-13 %' OR rule_key LIKE 'RW-14 %')") == 2
         and one("SELECT count(*) FROM sqlite_master WHERE type='index' AND name IN ('idx_ib_node_collection','idx_ib_node_strong_surface','idx_ib_observation_stable_key','idx_ib_observation_change_column_value')") == 4
         and one("SELECT count(DISTINCT name) FROM cfg_index WHERE name IN ('idx_ib_node_collection','idx_ib_node_strong_surface','idx_ib_observation_stable_key','idx_ib_observation_change_column_value')") == 4, scan)

    # ── every lookup is pinpointed: the plans, the work budget, the number of statements
    plans = {
        "older_on": "SELECT o.id, o.stage, o.tag, o.nature, o.obs_text, count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.verse_lexical_id IN (1,2,3) AND n.deleted=0 AND o.deleted=0 AND o.stage NOT IN ('a') GROUP BY o.id",
        "settled": "SELECT DISTINCT observation_id FROM ib_observation_change WHERE observation_id IN (1,2,3) AND column_name IN ('build_answer','nature','deferred_to','consumed_by')",
        "scope_texts": "SELECT DISTINCT o.id, o.obs_text FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 WHERE n.collection_id=1 AND n.deleted=0",
        "row_vl_ids": "SELECT DISTINCT verse_lexical_id FROM ib_node WHERE observation_id IN (1,2,3) AND deleted=0 AND verse_lexical_id IS NOT NULL",
        "scope a": "SELECT DISTINCT n.observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 WHERE n.deleted=0 AND n.collection_id=1",
        "scope verses": "SELECT DISTINCT n.observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 WHERE n.deleted=0 AND n.verse_reference IN ('Rom.1.1','Rom.1.2')",
        "scope pairs": "SELECT DISTINCT n.observation_id FROM _vpairs CROSS JOIN ib_node n INDEXED BY idx_ib_node_strong_surface ON n.strong=_vpairs.strong AND n.surface=_vpairs.surface JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 WHERE n.deleted=0",
        "trace_gaps traces": "SELECT n.observation_id, t.id, t.deleted, t.nature FROM ib_node n JOIN ib_observation t ON t.id=n.traced_observation_id WHERE n.observation_id IN (1,2,3) AND n.deleted=0",
        "deferrals": "SELECT c.observation_id FROM ib_observation_change c WHERE c.column_name='deferred_to' AND c.new_value='5'",
        "layer observations of a row": "SELECT id FROM ib_observation WHERE stable_key >= 'layer:5:' AND stable_key < 'layer:5;' AND deleted=0",
    }
    conn.execute("CREATE TEMP TABLE IF NOT EXISTS _vpairs (strong TEXT, surface TEXT)")
    bad = {k: sg.full_scans(conn, cfg, v) for k, v in plans.items()}
    case("P1", "no lookup of the build or the validation scans a table: the query plan of each searches by an index (the temporary table of pairs, scan_ok, is the driving list)",
         not any(bad.values()), {k: v for k, v in bad.items() if v})
    try:
        with sg.budget(conn, cfg, "test scan", max_ops=20000):
            conn.execute("SELECT count(*) FROM ib_node a JOIN ib_node b ON a.surface=b.surface AND a.id<b.id WHERE a.role='characteristic'").fetchall()
        over = None
    except sg.ScanBudgetExceeded as exc:
        over = str(exc)
    with sg.budget(conn, cfg, "test lookup"):
        pin = conn.execute("SELECT count(*) FROM ib_node WHERE collection_id=?", (cid,)).fetchone()[0]
    case("P2", "a statement that walks the table is stopped and named when it passes the work budget, nothing written; a pinpointed lookup runs under the same guard", bool(over) and "test scan" in over and pin >= 0, (over or "")[:200])
    stmts = []
    ids = [r[0] for r in q("SELECT verse_lexical_id FROM ib_node WHERE verse_lexical_id IS NOT NULL LIMIT 2000")]
    conn.set_trace_callback(lambda x: stmts.append(x))
    bv.older_on(conn, cfg, s, ids)
    conn.set_trace_callback(None)
    lookups = [x for x in stmts if "FROM ib_node n JOIN ib_observation o" in x]
    case("P3", "older_on over 2000 occurrences runs one lookup for each chunk, not one for each occurrence", len(lookups) == math.ceil(len(set(ids)) / scan["chunk"]), f"{len(lookups)} lookups for {len(set(ids))} occurrences, chunk {scan['chunk']}")
    sc = cv.scope(conn, other_cid)
    pairs_stmts = []
    conn.set_trace_callback(lambda x: pairs_stmts.append(x))
    cv.scope(conn, other_cid)
    conn.set_trace_callback(None)
    pairs_stmts = [x for x in pairs_stmts if not x.startswith("INSERT INTO _vpairs")]       # the driving rows are inserted in one executemany; the trace shows each row
    case("P4", "the scope of a collection runs a fixed number of statements however many pairs the collection has (the pairs are one join)", len(pairs_stmts) <= 12 and len(sc["union"]) > 0, f"{len(pairs_stmts)} statements, {sc['pairs']} pairs")

    # ── the answers to older observations, on one occurrence no observation has a node on
    V = conn.execute("SELECT v.id, v.strong, x.osisId, v.surface, v.morph_code FROM verse_lexical v JOIN verse x ON x.id=v.verse_id WHERE v.deleted=0 AND v.morph_code IS NOT NULL AND v.morph_code!='' "
                     "AND NOT EXISTS (SELECT 1 FROM ib_node n WHERE n.verse_lexical_id=v.id) LIMIT 1").fetchone()

    def obs(text, stage, nature=None, vl=V[0]):
        o = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, basis, meaning_source, status, run_id, created_at, nature) VALUES (NULL,?,'term',?,'stated','verse-text','draft',?,'2026-11-24T00:00:00Z',?)",
                         (stage, text, RUN, nature)).lastrowid
        conn.execute("INSERT INTO ib_node (observation_id, strong, verse_reference, surface, morph_code, source_stage, seq, role, created_at, verse_lexical_id, collection_id, subgroup_id) VALUES (?,?,?,?,?,?,1,'characteristic','2026-11-24T00:00:00Z',?,?,1)",
                     (o, V[1], V[2], V[3], V[4], stage, vl, cid))
        return o
    new = obs("Test new observation of the build, #2538, states one finding of the occurrence.", "layer-1", "evidence")
    texts = {}
    older = {k: obs(f"Test older observation {k}, #2538, an earlier reading of the occurrence {k}.", "prior-capture") for k in ("none", "keep", "restate", "consume", "neither", "defer", "bad")}
    older["merge"] = obs("Test new observation of the build, #2538, states one finding of the occurrence.", "prior-capture")      # the same description as the new one: a merge is for that
    found = bv.older_on(conn, cfg, s, [V[0]])
    case("B1", "older_on finds the eight older observations on the occurrence and not the build's own", set(found) == set(older.values()) and new not in found, sorted(found))
    p0 = bv.settle_row(conn, cfg, s, cid, [new], [], RUN, texts)
    case("B2", "with no answer the row is refused, naming how many are unanswered", any("8 older live observation(s)" in x and "no answer" in x for x in p0), p0)
    nat = va.natures(cfg)[0]
    ans = [{"observation": older["keep"], "action": "keep", "nature": "evidence", "reason": "test: the older observation stands as evidence of the occurrence"},
           {"observation": older["restate"], "action": "restate", "nature": "evidence", "new_text": "Test older observation restated, #2538, the occurrence reads as the verse gives it.",
            "checked": "the verse text and the stored occurrence were read for this test", "reason": "test: its wording is made specific to the occurrence"},
           {"observation": older["merge"], "action": "merge", "into": new, "reason": "test: the same finding as the new observation, its node moves"},
           {"observation": older["consume"], "action": "consume", "carriers": ["this"], "mapping": "test: the older observation says what the new one says, the one occurrence is carried by the new node"},
           {"observation": older["neither"], "action": "delete_neither", "reason": "test: states nothing of the verse and of the inner being, so it contributes nothing"},
           {"observation": older["defer"], "action": "defer", "collection": "thought", "nature": "inner_being", "finding": "test: the collection thought is to judge the working of this word"},
           {"observation": older["bad"], "action": "keep", "reason": "test: no marker given"}]
    p1 = bv.settle_row(conn, cfg, s, cid, [new], ans, RUN, {})
    case("B3", "a keep with no marker is refused with its reason; the older observation with no answer is still reported", any(str(older["bad"]) in x and "marker" in x for x in p1) and any("no answer" in x and "(for example [%d]" % older["none"] in x for x in p1), p1)
    live = lambda i: one("SELECT deleted FROM ib_observation WHERE id=?", i) == 0  # noqa: E731
    mark = lambda i: one("SELECT nature FROM ib_observation WHERE id=?", i)  # noqa: E731
    logged = lambda i: one("SELECT count(*) FROM ib_observation_change WHERE observation_id=? AND column_name='build_answer'", i)  # noqa: E731
    case("B4", "keep and restate set the marker and are logged; restate holds the new text; defer marks it and records the collection",
         mark(older["keep"]) == "evidence" and logged(older["keep"]) == 1 and mark(older["restate"]) == "evidence" and one("SELECT obs_text FROM ib_observation WHERE id=?", older["restate"]).startswith("Test older observation restated")
         and mark(older["defer"]) == "inner_being" and one("SELECT count(*) FROM ib_observation_change WHERE observation_id=? AND column_name='deferred_to'", older["defer"]) == 1 and logged(older["defer"]) == 1, "")
    case("B5", "merge, consume and delete_neither remove the older observation (soft) and are logged; merge moved its node to the kept observation",
         not live(older["merge"]) and not live(older["consume"]) and not live(older["neither"]) and logged(older["merge"]) == 1
         and one("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", new) >= 1, [(k, live(v)) for k, v in older.items()])
    older_live = bv.older_on(conn, cfg, s, [V[0]])
    done = bv.settled(conn, cfg, list(older.values()))
    left = [k for k, v in older.items() if v in older_live and v not in done]
    case("B6", "answered ones are settled and are not asked again: only the two unanswered remain", sorted(left) == ["bad", "none"] and older["keep"] in done and older["defer"] in done and older["restate"] in done, left)
    p2 = bv.settle_row(conn, cfg, s, cid, [new], [{"observation": older["bad"], "action": "keep", "nature": "evidence", "reason": "test: this one is kept as evidence"},
                                                   {"observation": older["none"], "action": "delete_neither", "reason": "test: states nothing of the verse or the inner being"}], RUN, {})
    case("B7", "with every older observation answered the row passes", p2 == [], p2)
    p3 = bv.settle_row(conn, cfg, s, cid, [new], [{"observation": 999999999, "action": "keep", "nature": "evidence", "reason": "test: not an older observation of this row"}], RUN, {})
    case("B8", "an answer that names an observation which is not an older one on this row is refused", any("999999999" in x for x in p3), p3)

    # ── the text clash (RW-03)
    same = obs("Test new observation of the build, #2538, states one finding of the occurrence.", "layer-1", "evidence", vl=V[0])
    p4 = bv.settle_row(conn, cfg, s, cid, [same], [], RUN, bv.scope_texts(conn, cfg, cid))
    case("B9", "a new observation whose text equals that of a live observation of the collection is refused, the other named", any(f"live observation {new}" in x and "RW-03" in x for x in p4), p4)
    conn.execute("UPDATE ib_observation SET deleted=1 WHERE id=?", (new,))
    p5 = bv.settle_row(conn, cfg, s, cid, [same], [], RUN, bv.scope_texts(conn, cfg, cid))
    case("B10", "once the other is deleted the text is no clash", not any("RW-03" in x for x in p5), p5)

    # ── the check re-derives from the tables
    conn.execute("UPDATE ib_node SET morph_code=NULL, disposition_note=NULL WHERE observation_id=?", (same,))
    r1 = bv.row_problems(conn, cfg, s, cid, [same], 1)
    conn.execute("UPDATE ib_node SET disposition_note='empty at creation, the data gives none -- test' WHERE observation_id=?", (same,))
    stray = obs("Test stray older observation, #2538, appeared after the row was recorded.", "prior-capture")
    r2 = bv.row_problems(conn, cfg, s, cid, [same], 1)
    va.set_nature(cfg, conn, stray, "evidence", "test: judged by a reading afterwards", RUN, "Claude")
    r3 = bv.row_problems(conn, cfg, s, cid, [same], 1)
    case("K1", "the check reports a word node missing a column with no reason, then an older observation nobody judged; when both hold it returns none",
         r1 and "miss a required column" in r1 and r2 and "no answer" in r2 and r3 is None, (r1, r2, r3))

    # ── the gate and the end state
    gate_ev = bv.closing_gate(conn, cfg, other_cid, "evidence")
    case("G1", "the closing gate names what the evidence layer still finds in a collection that is not clean (thought: unmarked observations)", any("unmarked" in x for x in gate_ev), gate_ev[:3])
    conn.rollback()

    ok = sum(1 for r in results if r[2] == "PASS")
    print("| id | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    print(f"\n{ok} of {len(results)} pass")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
