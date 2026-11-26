"""temp_2538_readstructure_test_run.py -- the test plan of ReadStructure / RecordStructure (escalation #2538; lib/readcommands.py; B:46).

Runs on a COPY of iba.db, never the live database. The copy must hold the subgroup through 1.2 with 2.1 not yet open: for thought, "reasoning", the copy built from the named snapshot
iba-20261125T123416Z-pre-2538-findings-apply.db with every #2538 migration applied (#2568), then temp_2538_readwords, _readsenses and _readenrichment test runs for "reasoning".
No 2.1 reading is recorded live, so the real answer (case T12 on) is Claude's reading of the first package, the three double-meaning rows of "reasoning" (one finding for each surface
with more than one code, specification v5 section 3), written below from the codes and verses of the package and checked against the ESV wording.

Usage: python iba/app/tools/temp_2538_readstructure_test_run.py <db copy> [collection] [subgroup] [other subgroup]
"""
import json
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import temp_2538_test_state as ts  # noqa: E402
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import readcommands as rc  # noqa: E402
from iba.app.lib import scanguard as sg  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
results = []

# Claude's reading of the double-meaning rows of "reasoning" (by surface): text, basis, grounds (words of one of the row's verses)
READING = {
    "reason": ("The surface reason renders eighteen codes. As a noun of the mind it is G3056 in 1Pe 3:15 (an account given), H4486 in Dan 4:34 and Dan 4:36 (understanding "
               "restored) and G2138 in Jam 3:17 (open to persuasion); as a verb it is H3198 in Isa 1:18 (to argue a case together). Elsewhere it is part of a phrase of cause: "
               "H6440I in Gen 41:31, H5921A, H1697M, H3651C, G1223, G5124, G0156, G2596, G0302, G1352, G5484, G1519 and H1961, and H2600 in Job 1:9 for without cause.",
               "read", "let us reason together"),
    "reasoned": ("The surface reasoned carries two codes: G1256 in Act 17:2, Act 17:17, Act 18:4, Act 18:19 and Act 24:25, where Paul discourses with others, and G3049 in "
                 "1Co 13:11, where a child reckons for himself.",
                 "read", "I reasoned like a child"),
    "reasoning": ("The surface reasoning carries two codes: G1261 in Luk 9:47, the reasoning held within the hearts of the disciples, and G1256 in Act 19:8 and Act 19:9, "
                  "where Paul argues with others in the synagogue and the hall of Tyrannus.",
                  "read", "the reasoning of their hearts"),
}


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed is True else ("BLOCKED" if passed is None else "FAIL"), str(evidence).replace("|", "/").replace("\n", " ")[:330]))
    print(f"[{results[-1][2]}] {cid}: {desc[:90]} -- {results[-1][3][:200]}", file=sys.stderr, flush=True)


def refused(fn):
    try:
        fn()
        return None
    except (rc.ReadError, lr.LayerError) as exc:
        return str(exc)


def counts(conn):
    return {t: conn.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in ("ib_observation", "ib_node", "ib_observation_change")}


def main(db, name="thought", sub="reasoning", other="meditating and pondering"):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    t_all = time.monotonic()
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    q = lambda s_, *a: conn.execute(s_, a).fetchall()  # noqa: E731
    out = pathlib.Path(tempfile.mkdtemp(prefix="readstructure-"))
    st = rc.settings(cfg)
    rt, lim = st["structure"], st["limits"]
    s = lr.settings(cfg)
    if not ts.in_loop(conn, cfg, name):      # live is past this step: the copy is put back to it (temp_2538_test_state, BUILD.md 597)
        print(ts.back_to(conn, cfg, name, sub, '2.1'), file=sys.stderr)
    cid, gid, gname = rc._subgroup(conn, name, sub)

    ins = rc.instruction(conn, rt)
    case("T1", "the instruction carries what, read, write, and the text of every rule it keeps, read live from cfg_method_rule",
         len(ins["keep"]) == len(rt["rules"]) and all(k["text"] for k in ins["keep"]) and bool(ins["read"]) and bool(ins["write"]), [k["rule"] for k in ins["keep"]])
    case("T2", "an unknown subgroup is refused", bool(refused(lambda: rc.read_structure(conn, cfg, "TEST-RT", name, "no such subgroup", out))), "")
    case("T3", "an unknown -Item is refused", bool(refused(lambda: rc.read_structure(conn, cfg, "TEST-RT", name, gname, out, "nonsense"))), "")
    m = refused(lambda: rc.read_structure(conn, cfg, "TEST-RT", name, other, out))
    case("T4", "ReadStructure for another subgroup is refused (the order gate, or that subgroup not through 1.2)", bool(m), m)
    conn.rollback()

    before = q("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='2.1' AND deleted=0 AND state!='retired'", cid, gid)[0][0]
    r = rc.read_structure(conn, cfg, "TEST-RT", name, gname, out)
    conn.commit()
    pkg = json.loads(r["path"].read_text(encoding="utf-8"))
    rows_db = [x for x in lr._rows(conn, cid, "2.1") if x[4] == gid and x[3] in rc.STRUCTURE_ITEMS and x[6] != "retired"]
    case("T5", "ReadStructure opens 2.1 for the subgroup (its rows are made) and writes the first package: one item, double-meaning first",
         before == 0 and len(rows_db) > 0 and r["item"] == "double-meaning" and {x["item"] for x in pkg["rows"]} == {"double-meaning"}, f"rows before {before}, after {len(rows_db)}, {r}")
    L = lr.load(conn, cfg, name, pairs=True, subgroup=gname)
    ok, ev = True, []
    for x in pkg["rows"]:
        want = {o["vl_id"] for o, _ in lr.expected_nodes(L, x["item"], gid, x["subject"])}
        ok &= {o["occurrence"] for o in x["occurrences"]} == want
        ev.append(f"{x['subject']} {len(x['occurrences'])}/{len(want)}")
    case("T6", "every row carries exactly the occurrences it demands (equal to the recorder's derivation)", ok, "; ".join(ev))
    vrefs = {v["reference"] for v in pkg["verses"]}
    star = all(any(w.startswith("*") for w in v["words"]) for v in pkg["verses"])
    case("T7", "the verses of the package hold every verse of its rows, once, each with its text and its structure lines, a * on the subgroup's words",
         all(set(x["verses"]) <= vrefs for x in pkg["rows"]) and len(vrefs) == len(pkg["verses"]) and all(v["text"] and v["words"] for v in pkg["verses"]) and star, f"{len(vrefs)} verses")
    case("T8", "the subgroup's 1.1 senses are given once", len(pkg["senses"]) > 0 and len({x["sense"] for x in pkg["senses"]}) == len(pkg["senses"]), f"{len(pkg['senses'])} senses")
    stamped = q(f"SELECT count(*) FROM collection_layer_item WHERE id IN ({','.join('?' * len(pkg['rows']))}) AND pulled_at IS NOT NULL", *[x["ledger_id"] for x in pkg["rows"]])[0][0]
    case("T9", "the rows of the package are stamped pulled_at; the package is within its size and time limits",
         stamped == len(pkg["rows"]) and r["chars"] <= rt["package_max_chars"] and r["seconds"] <= lim["read_max_seconds"], f"{r['chars']} chars (limit {rt['package_max_chars']}), {r['seconds']} s")

    seen, packages, overlap, sizes = {x["ledger_id"] for x in pkg["rows"]}, 1, False, [r["chars"]]
    while r["left"] and packages < 20:
        r = rc.read_structure(conn, cfg, "TEST-RT", name, gname, out)
        p2 = json.loads(r["path"].read_text(encoding="utf-8"))
        ids = {x["ledger_id"] for x in p2["rows"]}
        overlap |= bool(ids & seen)
        seen |= ids
        packages += 1
        sizes.append(r["chars"])
    conn.commit()
    case("T10", "repeated ReadStructure gives the next rows, one item at a time; together the packages carry every row once, each within the size limit",
         seen == {x[0] for x in rows_db} and not overlap and max(sizes) <= rt["package_max_chars"], f"{packages} packages, {len(seen)} rows, largest {max(sizes)} chars")
    r_p = rc.read_structure(conn, cfg, "TEST-RT", name, gname, out, "pairing")
    p_p = json.loads(r_p["path"].read_text(encoding="utf-8"))
    case("T11", "-Item pairing gives pairing rows, each with its WordNet control", {x["item"] for x in p_p["rows"]} == {"pairing"} and all("wordnet_control" in x for x in p_p["rows"]),
         f"{r_p['rows']} rows")
    conn.rollback()

    answer = {"command": "ReadStructure", "collection": name, "subgroup": gname, "rows": []}
    for x in pkg["rows"]:
        text, basis, grounds = READING.get(x["subject"], ("", "read", ""))
        answer["rows"].append({"ledger_id": x["ledger_id"], "item": x["item"], "subject": x["subject"], "disposition": "observed",
                               "findings": [{"kind": s["items"][x["item"]]["kind"], "obs_text": text, "basis": basis, "grounds": grounds, "occurrences": [o["occurrence"] for o in x["occurrences"]]}],
                               "reason": "", "older": [{"observation": o["observation"], "action": "keep", "nature": "evidence", "reason": "states the structure of its verse"} for o in x["older"]]})
    have = all(x["subject"] in READING for x in pkg["rows"])
    case("T12", "a real answer exists for the first package (Claude's reading of the double-meaning rows)", have, [x["subject"] for x in pkg["rows"]])

    c0 = counts(conn)
    first = answer["rows"][0]
    f0 = first["findings"][0]
    bad = [("T13", "an answer whose command is not ReadStructure", {**answer, "command": "ReadEnrichment"}),
           ("T13b", "an answer naming a ledger row that is not a 2.1 row of the subgroup", {**answer, "rows": answer["rows"] + [{**first, "ledger_id": -1}]}),
           ("T13c", "an answer with a disposition that is neither observed nor none", {**answer, "rows": [{**first, "disposition": "maybe"}] + answer["rows"][1:]}),
           ("T13d", "an answer recording a row as none without its reason", {**answer, "rows": [{**first, "disposition": "none", "reason": ""}] + answer["rows"][1:]}),
           ("T13e", "an answer whose findings leave an occurrence of the row out", {**answer, "rows": [{**first, "findings": [{**f0, "occurrences": f0["occurrences"][1:]}]}] + answer["rows"][1:]}),
           ("T13f", "an answer whose read grounds are not words of the row's verses", {**answer, "rows": [{**first, "findings": [{**f0, "grounds": "zz not in any verse zz"}]}] + answer["rows"][1:]}),
           ("T13g", "an answer whose text names none of its verses", {**answer, "rows": [{**first, "findings": [{**f0, "obs_text": "This surface carries several codes across the verses where it stands, as the data show."}]}] + answer["rows"][1:]})]
    for cid_, desc, data in bad:
        if not have and cid_ not in ("T13", "T13b"):
            case(cid_, desc + " is refused whole, nothing written", None, "no real answer")
            continue
        m = refused(lambda: rc.record_structure(conn, cfg, "TEST-RT", data, keep=True))
        case(cid_, desc + " is refused whole, nothing written", bool(m) and counts(conn) == c0, m or "")
        conn.rollback()

    if have:
        p = rc.record_structure(conn, cfg, "TEST-RT", answer, keep=False)
        case("T14", "-Check previews the real answer: everything checked, nothing kept", bool(p.get("preview")) and counts(conn) == c0, p)
        conn.rollback()
        w = rc.record_structure(conn, cfg, "TEST-RT", answer, keep=True)
        conn.commit()
        c1 = counts(conn)
        obs = []
        for x in answer["rows"]:
            obs += q("SELECT id, nature, tag FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", f"layer:{x['ledger_id']}:", f"layer:{x['ledger_id']};")
        case("T15", "RecordStructure writes the real answer: every row validated, one face observation for each surface, each marked evidence at creation",
             w["validated"] == len(answer["rows"]) and not w["failed"] and len(obs) == len(answer["rows"]) and all(o[1] == "evidence" and o[2] == "face" for o in obs), f"{w}")
        senses = {x["sense"] for x in pkg["senses"]}
        traced_ok = all({y[0] for y in q("SELECT traced_observation_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NOT NULL", o[0])} & senses for o in obs)
        case("T16", "every finding traces to a 1.1 sense of the subgroup", traced_ok, f"{len(obs)} findings")
        case("T17", "the next command named is ReadStructure while rows of 2.1 are open", "ReadStructure" in w["next"] and w["rows_open"] > 0, f"{w['rows_open']} open; {w['next']}")
        case("T18", "the real answer recorded again is refused (its rows are validated)", bool(refused(lambda: rc.record_structure(conn, cfg, "TEST-RT", answer, keep=True))) and counts(conn) == c1, "")
        conn.rollback()
        m = refused(lambda: rc.read_structure(conn, cfg, "TEST-RT", name, gname, out, "double-meaning"))
        case("T19", "-Item double-meaning, once its rows are validated, is refused and says other items are open", bool(m) and "other items" in (m or ""), m)
        conn.rollback()
    else:
        for c_ in ("T14", "T15", "T16", "T17", "T18", "T19"):
            case(c_, "needs the real answer", None, "")

    scans = []
    for sql, args in [("SELECT id, text FROM verse WHERE id IN (?,?)", (1, 2)),
                      ("SELECT id, pulled_at FROM collection_layer_item WHERE id IN (?,?)", (1, 2)),
                      ("SELECT DISTINCT verse_reference FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_reference IS NOT NULL", (1,))]:
        scans += sg.full_scans(conn, cfg, sql, args)
    case("T20", "no lookup of the read scans a large table (query plans)", not scans, scans)
    case("T21", "the whole test ran in under a minute", time.monotonic() - t_all < 60, f"{time.monotonic() - t_all:.1f} s")

    print("\n| case | what | result | evidence |\n|---|---|---|---|")
    for r_ in results:
        print(f"| {r_[0]} | {r_[1]} | {r_[2]} | {r_[3]} |")
    print(f"\n{sum(1 for r_ in results if r_[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r_[2] != "FAIL" for r_ in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
