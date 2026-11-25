"""temp_2505_layers_test_run.py -- tests for escalations #2505 and #2507 (stage 1, the lexical analysis, step S1, is run in place of the earlier synthetic catch-up): the layered reading of a collection (lib/layerreading.py, lib/collectionindex.py subgroup_for and refresh_nodes,
the node writers, the migration layers_2505_v1_20261115, the config it registers).

Each case checks the tables against a direct query written here, not against the library's own lists, and runs the refusals. Runs against a COPY of iba.db that already holds the
migration (never the live database); the groups, observations and ledger rows it makes are test rows on that copy. The lexical gate (step S1) is satisfied on the small test collection by running
stage 1 on the copy; on the real thought collection the gate is tested as it stands.

Usage: python iba/app/tools/temp_2505_layers_test_run.py <db copy> <scratch dir>
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib import buildvalidate as bv  # noqa: E402
from iba.app.lib import collectionvalidate as cvalid  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import validationactions as va  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []
RUN = "TEST-2505"


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:330]))


def refuses(fn, *a, **k):
    try:
        fn(*a, **k)
    except (lr.LayerError, ci.IndexError_) as exc:
        return str(exc)
    return None


def one_finding(r, text, basis="stated"):
    """The fill of a multi row (a sense, a finding): one finding holding every occurrence the row shows, named by verse reference."""
    return {"disposition": "observed", "senses": [{"kind": r["kind"], "obs_text": f"{r['evidence'][0]['reference']}: {text}", "basis": basis, "occurrences": [e["reference"] for e in r["evidence"]]}]}


def main(db, scratch):
    cfg = Cfg(pathlib.Path(db))
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp); _sp.loader.exec_module(_m)
    _m.apply_to_copy(cfg.conn)
    conn = cfg.conn
    q = lambda s, *a: conn.execute(s, a).fetchall()  # noqa: E731
    one = lambda s, *a: conn.execute(s, a).fetchone()[0]  # noqa: E731
    s = lr.settings(cfg)

    # ── configuration
    case("C1", "layer.reading is registered with 4 steps (S1, 1.1, 1.2, 2.1) and 8 items (group-relation removed from 2.1: by verse, #2538); stages lexical, layer-1 and layer-2; the kinds are enum values; 1.1 needs S1",
         len([x for x in s["steps"] if x["layer"] <= 2]) == 4 and len([k for k in s["items"] if k not in ("subgroup-analysis", "collection-gathering", "interworking", "old-observation")]) == 8 and s["stages"]["0"] == "lexical" and [x for x in s["steps"] if x["key"] == "1.1"][0]["needs"] == ["S1"] and one("SELECT count(*) FROM cfg_enum WHERE name='ib_observation.stage' AND value IN ('layer-1','layer-2','lexical')") == 3 and one("SELECT count(*) FROM cfg_enum WHERE name='observation_role' AND value='lexical'") == 1
         and one("SELECT count(*) FROM cfg_enum WHERE name='ib_observation.tag' AND value IN ('group','enrichment','pairing','relation')") == 4, f"steps {[x['key'] for x in s['steps']]}")
    case("C2", "every item kind is an ib_observation.tag value and every step's items are defined",
         all(v["kind"] in {r[0] for r in q("SELECT value FROM cfg_enum WHERE name='ib_observation.tag'")} for v in s["items"].values() if not v.get("ledger_only"))
         and all(i in s["items"] for st in s["steps"] for i in st["items"]), "")
    case("C3", "ib_node.subgroup_id and the ledger table exist and are registered in cfg_column",
         any(r[1] == "subgroup_id" for r in q("PRAGMA table_info(ib_node)")) and one("SELECT count(*) FROM cfg_column WHERE table_name='collection_layer_item' AND inactive=0") == 15
         and one("SELECT count(*) FROM cfg_column WHERE table_name='ib_node' AND name='subgroup_id' AND inactive=0") == 1, "")
    case("C4", "five steps registered with a routed condition; B:119/B:120 reworded; RO13 inactive; three new rules active",
         one("SELECT count(*) FROM cfg_step WHERE step LIKE 'collection.layer_%' OR step='collection.node_groups'") == 5
         and one("SELECT count(*) FROM cfg_on_fail WHERE step LIKE 'collection.layer_%' OR step='collection.node_groups'") == 5
         and "collection of that surface" in one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=119") and "collection's verses" in one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=120")
         and one("SELECT active FROM cfg_method_rule WHERE id=201") == 0
         and one("SELECT count(*) FROM cfg_behaviour_rule WHERE active=1 AND rule_key IN ('collection-reading-runs-in-layers','lexical-and-claims-readings-are-separate','layer-aspects-are-ledgered-and-never-left-open')") == 3, "")

    # ── gates on real data
    msg = refuses(lr.open_step, conn, cfg, RUN, "thought", "3.1", True)
    case("G1", "the real collection thought: LayerOpen 3.1 is refused (the steps it needs are not closed)", bool(msg) and "cannot be opened" in msg, (msg or "")[:300])
    case("G2", "an unknown step and an unknown collection are refused",
         bool(refuses(lr.open_step, conn, cfg, RUN, "thought", "9.9", True)) and bool(refuses(lr.open_step, conn, cfg, RUN, "nosuchword", "1.1", True)), "")

    # ── the small test collection: backsliding
    name = "backsliding"
    cid = one("SELECT id FROM collection WHERE name=? AND deleted=0", name)
    ci.fill(conn, cfg, RUN)
    surf = [r[0] for r in q("SELECT t.surface FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.collection_id=? AND i.deleted=0 ORDER BY t.surface", cid)]
    L = lr.load(conn, cfg, name)
    occ = L["d"]["occurrences"]
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "S1", True)
    case("G3", "the test collection with nothing placed: S1 is refused, naming the surfaces not placed", bool(msg) and "not placed" in msg, (msg or "")[:300])
    # ── the grouping comes first (#2538): S1 is read after it, inside the subgroup of each surface
    ci.make_group(conn, RUN, name, "alpha", "test group (#2505 test)")
    ci.make_group(conn, RUN, name, "beta", "test group (#2505 test)")
    half = len(surf) // 2
    ci.place(conn, RUN, name, "alpha", surf[:half], None, "test placement (#2505 test)")
    ci.place(conn, RUN, name, "beta", surf[half:-1], None, "test placement (#2505 test)")
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "S1", True)
    case("G6", "one surface still unplaced: S1 is refused", bool(msg) and "1 surfaces are not placed" in msg, (msg or "")[:200])
    ci.place(conn, RUN, name, None, [surf[-1]], None, "test isolation: no inner-being role (#2505 test)", isolate=True)
    # ── stage 1, the lexical analysis (step S1): opened after the grouping; one row for each content word (RG-22)
    words_all = sorted({lr.word_subject(o) for o in occ})
    func = {w for w in words_all if all(lr._is_function(cfg, o) for o in occ if lr.word_subject(o) == w)}
    words = [w for w in words_all if w not in func]
    s1a = lr.open_step(conn, cfg, RUN, name, "S1")
    s1b = lr.open_step(conn, cfg, RUN, name, "S1")
    rows_s1 = q("SELECT item, subgroup_id, subject, state FROM collection_layer_item WHERE collection_id=? AND step='S1' AND state!='retired' AND item='word-sense'", cid)
    n_old = one("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND step='S1' AND state!='retired' AND item='old-observation'", cid)
    case("S1", "opening S1 makes one word-sense row for each content word (surface and lettered code), none for a function-word-only word (RG-22), each in the subgroup of its surface; opening again changes nothing",
         s1a["add"] == len(words) + n_old and len(words) == len(rows_s1) and s1b["add"] == 0 and all(x[0] == "word-sense" and x[3] == "open" for x in rows_s1) and any(x[1] > 0 for x in rows_s1) and {x[2] for x in rows_s1} == set(words)
         and not ({x[2] for x in rows_s1} & func), f"{len(words)} content words, {len(func)} function-only; {s1a}")

    def settle_scope():     # test setup: the older observations of the collection are kept as evidence, so a record meets no unanswered older observation (#2538)
        for oid_ in sorted(cvalid.scope(conn, cid)["union"]):
            o_ = conn.execute("SELECT stage, nature FROM ib_observation WHERE id=?", (oid_,)).fetchone()
            if o_[0] not in bv.build_stages(lr.settings(cfg)) and o_[1] is None:
                va.set_nature(cfg, conn, oid_, "evidence", "test setup: an older observation kept as evidence", RUN, "Claude")
                orec.log(conn, oid_, None, "build_answer", None, "keep", "test setup: kept as evidence", None, RUN, "Claude")
            for nid_, in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND disposition_note IS NULL AND "
                                      "(strong IS NULL OR verse_reference IS NULL OR surface IS NULL OR morph_code IS NULL OR role IS NULL OR verse_lexical_id IS NULL OR collection_id IS NULL)", (oid_,)).fetchall():
                va.note_node(conn, nid_, "test setup: a node of an older observation whose data gives no more", RUN, "Claude")
    settle_scope()
    _record = lr.record
    lr.record = lambda *a, **k: (settle_scope(), _record(*a, **k))[1]     # the observations the test itself makes are kept before each record
    pS, nS = lr.pull(conn, cfg, name, "S1", pathlib.Path(scratch))
    dS = json.loads(pS.read_text(encoding="utf-8"))
    r0 = dS["rows"][0]
    case("S2", "the S1 working file holds each occurrence with its full verse and structural facts, the lexicon of the code, the prompts, the existing observations and a senses fill",
         nS == len(words) and r0["evidence"] and "morph" in r0["evidence"][0] and "verse" in r0["evidence"][0] and "lexicon" in r0 and r0["prompts"] and "existing_observations" in r0
         and "senses" in r0["fill"], r0["word"])
    rows_ = dS["rows"]
    multi = [r for r in rows_ if len(r["evidence"]) >= 2]
    bad = json.loads(pS.read_text(encoding="utf-8"))
    br = bad["rows"]
    br[0]["fill"].update({"disposition": "observed", "senses": []})
    br[1]["fill"].update({"disposition": "observed", "senses": [{"kind": "term", "obs_text": "a long enough text that names no verse of the word at all, test of the rule", "basis": "stated",
                                                                  "occurrences": [br[1]["evidence"][0]["reference"]]}]})
    vtext = (br[2]["evidence"][0]["verse"] or "").split()
    br[2]["fill"].update({"disposition": "observed", "senses": [{"kind": "term", "obs_text": f"In {br[2]['evidence'][0]['reference']} the verse reads: " + " ".join(vtext[:14]), "basis": "stated",
                                                                  "occurrences": [br[2]["evidence"][0]["reference"]]}]})
    br[3]["fill"].update({"disposition": "observed", "senses": [{"kind": "term", "obs_text": "In Nowhere 9:9 the word stands in a sense that no verse of this collection shows, test.", "basis": "stated",
                                                                  "occurrences": ["Nowhere 9:9"]}]})
    mr = [r for r in br[4:] if len(r["evidence"]) >= 2]
    if mr:
        mr[0]["fill"].update({"disposition": "observed", "senses": [{"kind": "term", "obs_text": f"In {mr[0]['evidence'][0]['reference']} the word stands in its first sense, test of coverage by senses.",
                                                                      "basis": "stated", "occurrences": [mr[0]["evidence"][0]["reference"]]}]})
    before = (one("SELECT count(*) FROM ib_observation"), one("SELECT count(*) FROM ib_node"))
    msg = refuses(lr.record, conn, cfg, RUN, bad, True)
    after = (one("SELECT count(*) FROM ib_observation"), one("SELECT count(*) FROM ib_node"))
    case("S3", "no senses, a text naming no verse, a text restating the verse, an occurrence that is not one of the word, and senses leaving an occurrence out are each refused, the whole file, nothing written",
         bool(msg) and "answered by senses" in msg and "tied to its verses" in msg and "restates the verse" in msg and "is not an occurrence" in msg and (not mr or "in no sense" in msg) and before == after,
         "missing: " + str([k for k in ("answered by senses", "tied to its verses", "restates the verse", "is not an occurrence", "in no sense") if k not in (msg or "")]) + " :: " + (msg or "")[-250:])
    hold = [r for r in rows_ if len(r["evidence"]) == 1][0]
    # an existing term observation of another stage, adopted by the row of one single-occurrence word (RS-04), and an inner-being one that is refused
    ho = hold["evidence"][0]
    aid = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, basis, meaning_source, status, run_id, created_at) VALUES (NULL,'prior-capture','term',?,'read','verse-text','draft',?,'2026-11-15T00:00:00Z')",
                       (f"Test existing observation of {ho['reference']} for adoption by the lexical analysis (#2507 test).", RUN)).lastrowid
    conn.execute("INSERT INTO ib_node (observation_id, strong, verse_reference, surface, morph_code, source_stage, seq, role, created_at, verse_lexical_id, collection_id) VALUES (?,?,?,?,?,'prior-capture',1,NULL,'2026-11-15T00:00:00Z',?,?)",
                 (aid, ho["strong"], ho["reference"], ho["surface"], ho["morph"], ho["occurrence"], cid))
    inner = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, basis, meaning_source, status, run_id, created_at) VALUES (NULL,'engagement','term',?,'read','verse-text','draft',?,'2026-11-15T00:00:00Z')",
                         (f"Test inner-being observation of {ho['reference']} that must not be adopted as lexical (#2507 test).", RUN)).lastrowid
    conn.execute("INSERT INTO ib_node (observation_id, strong, verse_reference, surface, morph_code, source_stage, seq, role, created_at, verse_lexical_id, collection_id) VALUES (?,?,?,?,?,'engagement',1,'characteristic','2026-11-15T00:00:00Z',?,?)",
                 (inner, ho["strong"], ho["reference"], ho["surface"], ho["morph"], ho["occurrence"], cid))
    ci.refresh_nodes(conn, RUN, collection_id=cid)     # the nodes the test made carry the group of their surface, as the build writes it
    ad_bad = {"collection": name, "step": "S1", "rows": [{"ledger_id": hold["ledger_id"], "fill": {"disposition": "adopt", "observation_id": inner, "reason": "an inner-being finding offered as adopted, test"}}]}
    case("S3b", "an observation whose nodes carry an inner-being role is refused as an adoption", "inner-being finding" in (refuses(lr.record, conn, cfg, RUN, ad_bad, True) or ""), "")
    # a read observation names its grounds in the words of the verse (RS-08); the grounds must be words of the verse; a quotation is the ESV's wording; the text may not restate the verse
    row1 = [r for r in rows_ if len(r["evidence"]) == 1 and r["ledger_id"] != hold["ledger_id"]][0]
    ref1, vtxt1 = row1["evidence"][0]["reference"], row1["evidence"][0]["verse"]
    base_sense = {"kind": "term", "occurrences": [ref1], "obs_text": f"In {ref1} the word {row1['word']} stands in the sense the verse gives it; test observation of the grounds rule, #2507."}
    r_nog = {"collection": name, "step": "S1", "rows": [{"ledger_id": row1["ledger_id"], "fill": {"disposition": "observed", "senses": [dict(base_sense, basis="read")]}}]}
    r_bad = {"collection": name, "step": "S1", "rows": [{"ledger_id": row1["ledger_id"], "fill": {"disposition": "observed", "senses": [dict(base_sense, basis="read", grounds="words that are not in this verse at all")]}}]}
    r_ok = {"collection": name, "step": "S1", "rows": [{"ledger_id": row1["ledger_id"], "fill": {"disposition": "observed", "senses": [dict(base_sense, basis="read", grounds=vtxt1[:14])]}}]}
    case("S3c", "a read observation with no grounds, or grounds that are not words of its verse, is refused; with grounds from the verse it is accepted",
         "names its grounds" in (refuses(lr.record, conn, cfg, RUN, r_nog, True) or "") and "are not words of the verses" in (refuses(lr.record, conn, cfg, RUN, r_bad, True) or "")
         and refuses(lr.record, conn, cfg, RUN, r_ok, False) is None, "")
    good = json.loads(pS.read_text(encoding="utf-8"))
    gr = []
    for r in good["rows"]:
        refs = [e["reference"] for e in r["evidence"]]
        if r["ledger_id"] == hold["ledger_id"]:
            r["fill"].update({"disposition": "adopt", "observation_id": aid, "reason": "the existing term observation already states the word in its verse (test of adoption, #2507)"})
        elif len(refs) >= 2:
            r["fill"].update({"disposition": "observed", "senses": [
                {"kind": "face", "obs_text": f"In {refs[0]} the word {r['word']} ({r['strong']}) departs from the sense it has in the other verses; test face observation of #2507.", "basis": "stated", "occurrences": [refs[0]]},
                {"kind": "term", "obs_text": f"In {', '.join(refs[1:])} the word {r['word']} ({r['strong']}) stands in the sense the verses give it; test observation of #2507, tied to its verses.", "basis": "stated",
                 "occurrences": refs[1:]}]})
        else:
            r["fill"].update({"disposition": "observed", "senses": [{"kind": "term", "obs_text": f"In {refs[0]} the word {r['word']} ({r['strong']}) stands in the sense the verse gives it; test observation of #2507, tied to its verse.",
                                                                      "basis": "stated", "occurrences": refs}]})
        gr.append(r)
    prevS = lr.record(conn, cfg, RUN, good, False)
    case("S4", "the S1 preview checks and writes nothing", prevS["observed"] >= 1 and one(f"SELECT count(*) FROM ib_observation WHERE stage='lexical' AND deleted=0 AND id IN (SELECT observation_id FROM ib_node WHERE collection_id={cid})") == 0, prevS)
    resS = lr.record(conn, cfg, RUN, good, True)
    obsS = q(f"SELECT id, tag, window, meaning_source, parts FROM ib_observation WHERE stage='lexical' AND deleted=0 AND id IN (SELECT observation_id FROM ib_node WHERE collection_id={cid})")
    nodS = q("SELECT n.observation_id, count(*), count(n.collection_id), sum(n.role='lexical'), count(n.subgroup_id) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='lexical' AND n.deleted=0 AND n.collection_id=%d GROUP BY 1" % cid)
    case("S5", "S1 observations are stage lexical, kind term or face, window meaning, the three lexicon sources, nodes with role lexical and a collection and the group of the surface; the adopted one is kept in place",
         len(obsS) == resS["observed"] and resS.get("adopted") == 1 and all(o[1] in ("term", "face") and o[2] == "meaning" and "strong_meaning_tree" in o[3] for o in obsS)
         and all(x[1] == x[2] == x[3] for x in nodS), f"{resS}; {len(obsS)} observations")
    an = q("SELECT role, collection_id FROM ib_node WHERE observation_id=? AND deleted=0", aid)
    case("S6", "the adopted observation keeps its stage and gains the role lexical on its node", one("SELECT stage FROM ib_observation WHERE id=?", aid) == "prior-capture" and an[0][0] == "lexical", [tuple(x) for x in an])
    case("S7", "a word with several occurrences is covered by its senses: a face observation of one occurrence and a term observation of the rest, each with only its own nodes",
         all(sum(q("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", o[0])[0][0] for o in obsS if json.loads(o[4])["word"] == r["subject"]) == len(r["evidence"])
             for r in gr if len(r["evidence"]) >= 2) and any(o[1] == "face" for o in obsS) == bool(multi), f"{len(multi)} words with several occurrences")
    repS = lr.check(conn, cfg, RUN, name)
    case("S8", "LayerCheck validates the S1 rows and closes stage 1; the gate reports it", repS["steps"]["S1"]["closed"] and repS["lexical"]["closed"] and lr.step_closed(conn, cid, "S1"), repS["steps"]["S1"]["failed"][:2])
    victim = q("SELECT n.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='lexical' AND o.tag='term' AND n.deleted=0 AND n.collection_id=%d LIMIT 1" % cid)[0][0]
    conn.execute("UPDATE ib_node SET deleted=1 WHERE id=?", (victim,))
    repS = lr.check(conn, cfg, RUN, name)
    case("S9", "a node removed from a word observation: the row fails (the senses no longer cover its occurrences) and stage 1 is no longer closed", not repS["steps"]["S1"]["closed"] and len(repS["steps"]["S1"]["failed"]) == 1, repS["steps"]["S1"]["failed"])
    conn.execute("UPDATE ib_node SET deleted=0 WHERE id=?", (victim,))
    repS = lr.check(conn, cfg, RUN, name)
    case("S10", "the node restored: stage 1 closes again", repS["steps"]["S1"]["closed"], "")
    L = lr.load(conn, cfg, name)
    gate = lr.lexical_status(conn, cfg, L)
    case("G4", "with stage 1 closed the lexical gate passes", gate["closed"], gate)
    oid = obsS[0][0]
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "1.1", True)
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "1.2", True)
    case("G7", "step 1.2 cannot open before 1.1 is closed", bool(msg) and "step 1.1 is not closed" in msg, (msg or "")[:200])

    # ── the group on the node, from placement
    got = q("SELECT count(*), count(n.subgroup_id) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='lexical' AND n.deleted=0 AND lower(trim(n.surface)) IN (%s)" % ",".join("?" * half), *surf[:half])
    case("N1", "placing surfaces set subgroup_id on their existing nodes (placement refresh)", got[0][0] == got[0][1] and got[0][0] > 0, f"{got[0][1]} of {got[0][0]} nodes of the alpha surfaces carry a group")
    iso_nodes = q("SELECT count(n.subgroup_id) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='lexical' AND n.deleted=0 AND lower(trim(n.surface))=?", surf[-1])
    case("N2", "an isolated surface's nodes carry no group", iso_nodes[0][0] == 0, iso_nodes)

    # ── open 1.1
    r1 = lr.open_step(conn, cfg, RUN, name, "1.1")
    r2 = lr.open_step(conn, cfg, RUN, name, "1.1")
    rows = q("SELECT item, subgroup_id, state FROM collection_layer_item WHERE collection_id=? AND step='1.1'", cid)
    case("O1", "opening 1.1 makes one group-definition row for each of the 2 groups; opening again changes nothing", r1["add"] == 2 and r2["add"] == 0 and len(rows) == 2 and all(x[2] == "open" for x in rows), f"{r1} then {r2}")

    # ── pull
    path, n = lr.pull(conn, cfg, name, "1.1", pathlib.Path(scratch))
    data = json.loads(path.read_text(encoding="utf-8"))
    case("P1", "the working file holds the 2 open rows, each with the evidence and an empty fill", n == 2 and all(r["fill"]["senses"][0]["obs_text"] == "" and r["evidence"] for r in data["rows"]), f"{path.name}")
    # ── record refusals (each leaves nothing written)
    before = (one("SELECT count(*) FROM ib_observation"), one("SELECT count(*) FROM ib_node"))
    bad = json.loads(path.read_text(encoding="utf-8"))
    bad["rows"][0]["fill"].update({"disposition": "none", "reason": "no reason"})
    bad["rows"][1]["fill"].update({"disposition": "observed", "senses": [{"kind": bad["rows"][1]["kind"], "obs_text": "too short", "basis": "invented", "occurrences": [e["reference"] for e in bad["rows"][1]["evidence"]]}]})
    msg = refuses(lr.record, conn, cfg, RUN, bad, True)
    after = (one("SELECT count(*) FROM ib_observation"), one("SELECT count(*) FROM ib_node"))
    case("R1", "a file with none on a group definition, a short text and a bad basis is refused whole, nothing written",
         bool(msg) and "cannot be recorded as none" in msg and "under" in msg and "basis must be one of" in msg and before == after, (msg or "")[:300])
    bad = {"collection": name, "step": "1.1", "rows": [{"ledger_id": 999999, "fill": {"disposition": "observed"}}]}
    case("R2", "an unknown ledger row is refused", "not a ledger row" in (refuses(lr.record, conn, cfg, RUN, bad, True) or ""), "")
    # ── record preview, then record
    good = json.loads(path.read_text(encoding="utf-8"))
    for r in good["rows"]:
        r["fill"].update(one_finding(r, f"The surfaces of the group {r['group']} turn away, which is a movement of the inner being from what it held; test observation of #2505."))
    prev = lr.record(conn, cfg, RUN, good, False)
    case("R3", "the preview checks and writes nothing", prev["observed"] == 2 and one(f"SELECT count(*) FROM ib_observation WHERE stage='layer-1' AND id IN (SELECT observation_id FROM ib_node WHERE collection_id={cid})") == 0, prev)
    res = lr.record(conn, cfg, RUN, good, True)
    obs = q(f"SELECT id, stage, tag, parts FROM ib_observation WHERE stage='layer-1' AND id IN (SELECT observation_id FROM ib_node WHERE collection_id={cid})")
    nodes = q("SELECT n.observation_id, count(*), count(n.subgroup_id), count(n.collection_id), sum(n.role IS NULL) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.stage='layer-1' AND n.collection_id=? AND n.traced_observation_id IS NULL GROUP BY 1", cid)     # the word nodes (the traced nodes name the word observations a sense covers)
    Lg = lr.load(conn, cfg, name)
    want = {g: len([o for o in Lg["d"]["occurrences"] if o["group"] == g]) for g in Lg["groups"]}
    case("R4", "2 observations of stage layer-1 and kind group; each has exactly the occurrences of its group as nodes, each with a role, a collection and the group",
         res["observed"] == 2 and len(obs) == 2 and all(o[2] == "group" for o in obs) and sorted(x[1] for x in nodes) == sorted(want.values())
         and all(x[1] == x[2] == x[3] and not x[4] for x in nodes), f"{res}; nodes {nodes}; want {want}")
    case("R5", "the ledger rows are observed with their observation and not yet validated",
         one("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND step='1.1' AND state='observed' AND observation_id IS NOT NULL AND validated=0", cid) == 2, "")
    # ── check
    rep = lr.check(conn, cfg, RUN, name)
    case("K1", "LayerCheck validates both rows and closes step 1.1; later steps have no rows",
         rep["steps"]["1.1"]["closed"] and rep["steps"]["1.1"]["validated"] == 2 and not rep["steps"]["1.2"]["rows"] and one(f"SELECT count(*) FROM collection_layer_item WHERE step='1.1' AND validated=1 AND collection_id={cid}") == 2, rep["steps"]["1.1"])
    case("R6", "the same file again is refused once the rows are validated", "validated; only an open or an unvalidated row" in (refuses(lr.record, conn, cfg, RUN, good, True) or ""), "")
    # tamper: delete one node of one observation -> the check fails that row
    victim = q("SELECT id, observation_id FROM ib_node WHERE observation_id=? LIMIT 1", obs[0][0])[0]
    conn.execute("UPDATE ib_node SET deleted=1 WHERE id=?", (victim[0],))
    rep = lr.check(conn, cfg, RUN, name)
    case("K2", "a node removed from a layer observation: the row fails with the number missing, validated is cleared, the step is not closed",
         not rep["steps"]["1.1"]["closed"] and len(rep["steps"]["1.1"]["failed"]) == 1 and "1 in no sense" in rep["steps"]["1.1"]["failed"][0]
         and one(f"SELECT count(*) FROM collection_layer_item WHERE step='1.1' AND validated=1 AND collection_id={cid}") == 1, rep["steps"]["1.1"]["failed"])
    msg = refuses(lr.open_step, conn, cfg, RUN, name, "1.2", True)
    case("K3", "with 1.1 not closed, step 1.2 stays refused", bool(msg) and "step 1.1 is not closed" in msg, (msg or "")[:160])
    # re-record the failed row: it is unvalidated, so it can be recorded again; the old observation is withdrawn
    p2, _ = lr.pull(conn, cfg, name, "1.1", pathlib.Path(scratch))
    again = json.loads(p2.read_text(encoding="utf-8"))
    case("K4", "the pull after a failure holds just the failed row", len(again["rows"]) == 1, [r["group"] for r in again["rows"]])
    again["rows"][0]["fill"].update(one_finding(again["rows"][0], "The surfaces of this group turn away from what the inner being held; test re-recording of #2505."))
    res = lr.record(conn, cfg, RUN, again, True)
    rep = lr.check(conn, cfg, RUN, name)
    case("K5", "re-recorded: the earlier observation is withdrawn, the new one validates, step 1.1 closes",
         res["withdrawn"] == 1 and rep["steps"]["1.1"]["closed"] and one(f"SELECT count(*) FROM ib_observation WHERE stage='layer-1' AND deleted=0 AND id IN (SELECT observation_id FROM ib_node WHERE collection_id={cid})") == 2 and one(f"SELECT count(*) FROM ib_observation WHERE stage='layer-1' AND id IN (SELECT observation_id FROM ib_node WHERE collection_id={cid})") == 3, res)
    # ── 1.2
    r = lr.open_step(conn, cfg, RUN, name, "1.2")
    p3, n3 = lr.pull(conn, cfg, name, "1.2", pathlib.Path(scratch))
    enr = json.loads(p3.read_text(encoding="utf-8"))
    for row in enr["rows"]:
        row["fill"].update(one_finding(row, f"The Strong's codes of {row['group']} ({', '.join(row['strong_codes'])}) define it as a turning away; test enrichment of #2505."))
    res = lr.record(conn, cfg, RUN, enr, True)
    rep = lr.check(conn, cfg, RUN, name)
    case("E1", "1.2 opens once 1.1 is closed; the enrichment observations carry a node for every Strong's code of the group; step 1.2 closes",
         r["add"] == 2 and res["observed"] == 2 and rep["steps"]["1.2"]["closed"], f"{r}; {res}")
    # ── 2.1
    r = lr.open_step(conn, cfg, RUN, name, "2.1")
    rows2 = q("SELECT item, count(*) FROM collection_layer_item WHERE collection_id=? AND step='2.1' GROUP BY item", cid)
    L2 = lr.load(conn, cfg, name, pairs=True)
    want2 = lr.derive(conn, cfg, L2, "2.1")
    case("L1", "2.1 opens after 1.2 is closed; the ledger rows equal the aspects the data demands", r["demanded"] == len(want2) and sum(x[1] for x in rows2) == len(want2), f"{rows2}")
    if want2:
        p4, n4 = lr.pull(conn, cfg, name, "2.1", pathlib.Path(scratch))
        d4 = json.loads(p4.read_text(encoding="utf-8"))
        g4 = sorted({x["group"] for x in d4["rows"]})[0]
        pg, ng = lr.pull(conn, cfg, name, "2.1", pathlib.Path(scratch), subgroup=g4)
        dg = json.loads(pg.read_text(encoding="utf-8"))
        case("L0", "the 2.1 pull for one subgroup names it and carries the unmarked list and an empty delete_unmarked; the pull of the whole collection carries none",
             dg.get("subgroup") == g4 and isinstance(dg.get("unmarked"), list) and dg.get("delete_unmarked") == [] and all(x["group"] == g4 for x in dg["rows"]) and "unmarked" not in d4, f"{ng} rows; d4 keys {sorted(d4)}; groups {sorted({x['group'] for x in dg['rows']})}; keys {sorted(dg)}; g4 {g4}; subgroup {dg.get(chr(115)+chr(117)+chr(98)+chr(103)+chr(114)+chr(111)+chr(117)+chr(112))}")
        for row in d4["rows"]:
            it = s["items"][row["item"]]
            if it["none_allowed"]:
                row["fill"].update({"disposition": "none", "reason": "test: nothing to observe for this aspect (#2505 test)"})
            else:
                row["fill"].update(one_finding(row, "test observation text of at least forty characters (#2505)"))
        ent = [x for x in d4["rows"] if x["item"] == "entity"]
        msg_route = refuses(lr.record, conn, cfg, RUN, {"collection": name, "step": "2.1", "rows": [
            {"ledger_id": ent[0]["ledger_id"], "fill": {"disposition": "observed", "obs_text": "x" * 60, "basis": "stated", "route": "A"}}]}, True) if ent else None
        res = lr.record(conn, cfg, RUN, d4, True)
        rep = lr.check(conn, cfg, RUN, name)
        case("L2", "every 2.1 row answered as none (with reason) validates; step 2.1 closes", rep["steps"]["2.1"]["closed"] and res["none"] == len(d4["rows"]), rep["steps"]["2.1"])
        case("L3", "an entity row given an inner-being route is refused: the lexical stages take no route", True if not ent else "takes no route" in (msg_route or ""), "no entity aspect in this collection" if not ent else (msg_route or "")[:160])
    else:
        case("L2", "no 2.1 aspects demanded for this collection (no pairing reaches the thresholds)", True, "")
    # ── a placement change after the observations exist
    ci.make_group(conn, RUN, name, "gamma", "test group (#2505 test)")
    moved = surf[0]
    ci.place(conn, RUN, name, "gamma", [moved], None, "test move (#2505 test)")
    ng = q("SELECT count(*), count(subgroup_id) FROM ib_node WHERE deleted=0 AND lower(trim(surface))=? AND collection_id=?", moved, cid)
    gid = one("SELECT id FROM collection_subgroup WHERE collection_id=? AND name='gamma'", cid)
    case("M1", "moving a surface to another group moves the group on all of its nodes", one("SELECT count(*) FROM ib_node WHERE deleted=0 AND lower(trim(surface))=? AND collection_id=? AND subgroup_id=?", moved, cid, gid) == ng[0][0] > 0, tuple(ng[0]))
    rep = lr.check(conn, cfg, RUN, name)
    case("M2", "the moved surface makes the earlier layer rows fail or the step reopen (the data demands a new group row), not stay validated",
         not rep["steps"]["1.1"]["closed"] and (rep["steps"]["1.1"]["failed"] or rep["steps"]["1.1"]["not_in_ledger"]), f"failed {rep['steps']['1.1']['failed'][:2]} missing {rep['steps']['1.1']['not_in_ledger'][:2]}")
    # ── node refresh and the index check
    dry = ci.refresh_nodes(conn, RUN, dry=True, collection_id=cid)
    case("M3", "NodeGroups preview on the copy: every node agrees with the index", dry["changed"] == 0, dry)
    conn.execute("UPDATE ib_node SET subgroup_id=NULL WHERE lower(trim(surface))=? AND collection_id=?", (surf[1], cid))
    found = {f["key"]: f for f in ci.check(conn, cfg)}
    case("M4", "the index check names nodes whose group differs from the index", found["node-group-does-not-agree"]["rows"] != [], found["node-group-does-not-agree"]["rows"])
    fixed = ci.refresh_nodes(conn, RUN)
    case("M5", "the refresh repairs them and keeps each change with its reason", fixed["changed"] > 0 and ci.refresh_nodes(conn, RUN, dry=True)["changed"] == 0
         and one("SELECT count(*) FROM ib_observation_change WHERE column_name='subgroup_id' AND run_id=?", RUN) >= fixed["changed"], fixed)
    # ── writers fill the group on new nodes
    case("W1", "the shared node writer helper returns the group of a placed surface and None for no collection", orec._group_of(conn, cid, moved, None) == gid and orec._group_of(conn, None, moved, None) is None, "")
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
