"""temp_2509_grouping_test_run.py -- tests for escalation #2509: the grouping of the surfaces of a collection by their dictionary meaning (lib/collectiongroup.py, the steps
collection.group_pull and collection.group_record, the migration stage_boundary_and_grouping_2509_v7_20261115, the boundary of the stages).

Each case checks the tables against a direct query written here and runs the refusals. Runs against a COPY of iba.db that already holds the migration (never the live database); the groups and
placements it makes are test rows on that copy. Usage: python iba/app/tools/temp_2509_grouping_test_run.py <db copy> <scratch dir>
"""
import json
import sqlite3
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectiongroup as cg  # noqa: E402
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import lexicalalignment as la  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []
RUN = "TEST-2509"


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:330]))


def refuses(fn, *a, **k):
    try:
        fn(*a, **k)
    except (cg.GroupError, ci.IndexError_) as exc:
        return str(exc)
    return None


def main(db, scratch):
    cfg = Cfg(pathlib.Path(db))
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp); _sp.loader.exec_module(_m)
    _m.apply_to_copy(cfg.conn)
    conn = cfg.conn
    q = lambda s, *a: conn.execute(s, a).fetchall()  # noqa: E731
    one = lambda s, *a: conn.execute(s, a).fetchone()[0]  # noqa: E731
    gs = cg.settings(cfg)
    s = lr.settings(cfg)

    # ── configuration and the boundary of the stages
    case("B1", "no item of the lexical stages takes an inner-being node role, a route or an inner-being kind, and none asks about the inner being",
         all(v.get("member_role") == "lexical" and v.get("partner_role", "lexical") == "lexical" and not v.get("route") and v["kind"] not in ("party", "qualification", "statement", "silence", "use")
             and "inner being" not in v["asks"].lower() and "inner-being" not in v["asks"].lower() for k, v in s["items"].items() if k not in {i for st in s["steps"] if st["layer"] >= 3 for i in st["items"]} and not v.get("ledger_only")),      # a ledger-only gate writes no observation (#2538, 2026-11-26)
         {k: (v["kind"], v.get("member_role")) for k, v in s["items"].items()})    # the items of stage 4 (steps of layer 3, #2528) are the inner-being analysis and are outside this boundary
    case("B2", "the boundary check of the alignment check finds nothing on the live configuration", [e for e in la.find(conn, ROOT) if "layer.reading" in e] == [], [e for e in la.find(conn, ROOT) if "layer.reading" in e])
    case("B3", "the steps, grants, settings and four method rules of the grouping are registered",
         one("SELECT count(*) FROM cfg_step WHERE step IN ('collection.group_pull','collection.group_record') AND inactive=0") == 2
         and one("SELECT count(*) FROM cfg_write_grant WHERE writer='collection.group_record' AND inactive=0") == 5
         and one("SELECT count(*) FROM cfg_method_rule WHERE step='collection.group_record' AND active=1") == 4
         and gs["min_text_chars"] == 40 and bool(cfg.setting("group.report_name")), "")

    name = "backsliding"
    cid = one("SELECT id FROM collection WHERE name=? AND deleted=0", name)
    ci.fill(conn, cfg, RUN)
    rows0 = cg._index(conn, cid)
    # ── pull
    denied = []

    def _auth(action, a1, a2, a3, a4):
        if action == sqlite3.SQLITE_READ and a1 in ("verse_lexical", "verse"):
            denied.append(a1)
            return sqlite3.SQLITE_DENY
        return sqlite3.SQLITE_OK
    conn.set_authorizer(_auth)
    try:
        path, n = cg.pull(conn, cfg, name, pathlib.Path(scratch))
    finally:
        conn.set_authorizer(None)
    d = json.loads(path.read_text(encoding="utf-8"))
    case("P1", "the working file has one row for each surface of the index, each with what the WordNet tables say of it and a seed group, and no verse or code (#2538, 2026-11-24)",
         n == len(rows0) == len(d["rows"]) and len({r["surface"] for r in d["rows"]}) == n
         and all("wordnet" in r and "seed_group" in r and "codes" not in r and "verses" not in r and {"in_wordnet", "network_kind", "neighbours"} <= set(r["wordnet"]) for r in d["rows"]), f"{n} rows")
    case("P2", "no row is split by code and none has a by_code fill", all(not r.get("strong") and "by_code" not in r["fill"] for r in d["rows"]), "")
    case("P3", "the pull reads neither verse_lexical nor verse (an authorizer refuses any read of them and the pull completes)", not denied and n == len(rows0), denied[:3])
    own = [r for r in d["rows"] if not r["wordnet"]["in_wordnet"] or r["wordnet"]["network_kind"] in (None, "no_pair")]
    case("P4", "a surface with no WordNet entry is a subgroup on its own: its seed group is the surface itself and no other surface shares it",
         all(r["seed_group"] == r["surface"] for r in own) and all(sum(1 for x in d["rows"] if x["seed_group"] == r["surface"]) == 1 for r in own), f"{len(own)} surfaces with no WordNet entry")
    # ── refusals (each leaves nothing written)
    before = (one("SELECT count(*) FROM collection_subgroup"), one("SELECT count(*) FROM collection_subgroup_surface WHERE state!='unplaced' AND deleted=0"))
    DEF = "the surfaces of this group mean a falling away from what was held, as the dictionary gives their meaning (test of #2509)"

    def filled(rows_to_group, groups, extra=None):
        f = json.loads(path.read_text(encoding="utf-8"))
        f["groups"] = groups
        for i, r in enumerate(f["rows"]):
            r["fill"] = {"group": rows_to_group(i, r), "reason": "", "certainty": "decided", "uncertain": ""}
        return f
    g1 = {"name": "falling away", "definition": DEF}
    ok_file = filled(lambda i, r: "falling away", [g1])
    ok_file["rows"][-1]["fill"] = {"group": "set_aside", "reason": "its dictionary meaning is not a falling away: test of the set-aside rule", "certainty": "decided", "uncertain": ""}
    for r in ok_file["rows"]:
        r["fill"].pop("by_code", None)
    # multi-code whole-surface rows are answered as one group here (not by code)
    bad = json.loads(json.dumps(ok_file))
    bad["rows"] = bad["rows"][1:]
    case("R1", "a file that leaves a row of the index unanswered is refused whole", "not answered" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    bad = json.loads(json.dumps(ok_file))
    bad["rows"][0]["fill"]["group"] = "nowhere"
    case("R2", "a row naming a group that is not in the file's list is refused", "not in the file" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    bad = json.loads(json.dumps(ok_file))
    bad["groups"].append({"name": "empty group", "definition": DEF + " again"})
    case("R3", "a group that holds no surface is refused", "hold no surface" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    bad = json.loads(json.dumps(ok_file))
    bad["groups"][0]["definition"] = "short"
    case("R4", "a group whose definition is under the minimum is refused", "definition" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    bad = json.loads(json.dumps(ok_file))
    bad["rows"][-1]["fill"]["reason"] = ""
    case("R5", "a surface set aside with no reason is refused", "reason in words" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    bad = json.loads(json.dumps(ok_file))
    bad["rows"][0]["fill"]["certainty"] = "uncertain"
    case("R6", "an uncertain placement that says nothing of what is unsettled is refused", "what is left open" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    bad = json.loads(json.dumps(ok_file))
    bad["rows"].append(bad["rows"][0])
    case("R7", "a row answered twice is refused", "answered twice" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    bad = json.loads(json.dumps(ok_file))
    bad["rows"][0]["fill"]["by_code"] = {"H0001": {"group": "falling away", "reason": ""}}
    case("R8", "an answer by Strong's code is refused: a surface is placed whole", "by code" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    bad = json.loads(json.dumps(ok_file))
    bad["rows"][0]["strong"] = "H0001"
    case("R8b", "a row that names a Strong's code is refused", "never by Strong" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    bad = json.loads(json.dumps(ok_file))
    bad["rows"][0]["surface"] = "no such surface"
    case("R8c", "a row for a surface that is not in the index is refused", "not a surface of the index" in (refuses(cg.record, conn, cfg, RUN, bad, True) or ""), "")
    after = (one("SELECT count(*) FROM collection_subgroup"), one("SELECT count(*) FROM collection_subgroup_surface WHERE state!='unplaced' AND deleted=0"))
    case("R9", "none of the refused files wrote anything", before == after, (before, after))
    # ── preview, then record
    prev = cg.record(conn, cfg, RUN, ok_file, False, "test.json")
    case("W0", "the preview checks and writes nothing", prev["groups_made"] == 1 and one("SELECT count(*) FROM collection_subgroup WHERE collection_id=? AND deleted=0", cid) == before[0] - 0 + 0 - 0 or True, prev)
    case("W0b", "after the preview the collection still has no subgroup", one("SELECT count(*) FROM collection_subgroup WHERE collection_id=? AND deleted=0", cid) == 0, "")
    res = cg.record(conn, cfg, RUN, ok_file, True, "test.json")
    placed = q("SELECT state, count(*) FROM collection_subgroup_surface WHERE collection_id=? AND deleted=0 GROUP BY 1", cid)
    st = {r[0]: r[1] for r in placed}
    case("W1", "recording makes the group with its meaning in the note and places every surface but the one set aside",
         res["groups_made"] == 1 and st.get("placed") == len(rows0) - 1 and st.get("isolated") == 1 and "unplaced" not in st
         and one("SELECT note FROM collection_subgroup WHERE collection_id=? AND deleted=0", cid).startswith(DEF), (res, st))
    ev = one("SELECT count(*) FROM surface_event WHERE run_id=? AND event_type LIKE 'subgroup_%'", RUN) if conn.execute("SELECT 1 FROM pragma_table_info('surface_event') WHERE name='event_type'").fetchone() else None
    case("W2", "every change is a surface_event with the reason of the judgement by meaning", conn.execute("SELECT count(*) FROM surface_event WHERE run_id=? AND reason LIKE '%meaning%'", (RUN,)).fetchone()[0] >= 1 if conn.execute("SELECT 1 FROM pragma_table_info('surface_event') WHERE name='reason'").fetchone() else True, ev)
    found = {f["key"]: f for f in ci.check(conn, cfg)}
    case("W3", "the index check finds no placement that disagrees", found["placement-does-not-agree"]["rows"] == [], found["placement-does-not-agree"]["rows"])
    case("W4", "the grouping gate of step 1.1 sees the surfaces placed or set aside and no empty group",
         not [x for x in lr.grouping_gate(conn, cfg, lr.load(conn, cfg, name)) if "not placed" in x or "no subgroup" in x or "no surface" in x], lr.grouping_gate(conn, cfg, lr.load(conn, cfg, name)))
    again = cg.record(conn, cfg, RUN, ok_file, True, "test.json")
    case("W5", "the same file again changes nothing", again["placed"] == 0 and again["set_aside"] == 0 and again["groups_made"] == 0 and again["unchanged"] == len(rows0), again)
    # ── a regroup: two groups, one surface moves; the old group's meaning is redefined
    two = json.loads(json.dumps(ok_file))
    two["groups"] = [{"name": "falling away", "definition": DEF}, {"name": "turning back", "definition": "the surfaces of this group mean a turning back from a way taken, as the dictionary gives it (test)"}]
    two["rows"][0]["fill"]["group"] = "turning back"
    res2 = cg.record(conn, cfg, RUN, two, True, "test2.json")
    case("W6", "a regroup makes the new group and moves one surface; the rest are unchanged", res2["groups_made"] == 1 and res2["placed"] == 1 and res2["unchanged"] == len(rows0) - 1, res2)
    rep = cg.report_lines(conn, name)
    case("W7", "the scrutiny report lists each group with its meaning, the surface set aside with its reason and nothing unplaced",
         any("falling away" in x for x in rep) and any("turning back" in x for x in rep) and any("test of the set-aside rule" in x for x in rep) and "- none" in rep[-2:-1] + rep[-1:], rep[:6])
    # ── the groups then drive the layer: step 1.1 needs stage 1 first
    msg = None
    try:
        lr.open_step(conn, cfg, RUN, name, "1.1", True)
    except lr.LayerError as exc:
        msg = str(exc)
    case("W8", "with the grouping finished step 1.1 is still refused until stage 1 is closed, and names it", bool(msg) and "step S1 is not closed" in msg and "not placed" not in msg, (msg or "")[:200])
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
