"""temp_2538_gates_test_run.py -- the test plan of the sweep (B4) and the evidence validation (B5) as the gates of step 2.1 (escalation #2538; lib/readcommands.py; B:46).

Two copies of iba.db, never the live database:
  <before copy>  a subgroup through 1.2 with 2.1 not open (iba-test-2538-reasoning-through-1.2.db: the named snapshot with every #2538 migration, the words, senses and enrichment test runs
                 for "reasoning"): the order of the gates against the 2.1 rows
  <live copy>    a copy of live with gates_2538_v1_20261126.py applied: "reasoning" read through 2.1 live, with 29 unmarked observations of the replaced group on its scope; the real sweep
                 (Claude's reading, recorded below by observation id) and the evidence validation's package and record
The end-to-end close of the gate (every evidence observation read) is shown by logging the reads on the copy directly (case G22, marked as scaffolding): the reading itself is the
researcher-approved live run, not a test.

Usage: python iba/app/tools/temp_2538_gates_test_run.py <before copy> <live copy> <sweep reading json>
"""
import json
import pathlib
import sys
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import layerloop as ll  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import readcommands as rc  # noqa: E402
from iba.app.lib import scanguard as sg  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
results = []
NAME, SUB = "thought", "reasoning"


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
    return {t: conn.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in ("ib_observation", "ib_node", "ib_observation_change", "collection_layer_item")}


def main(before, livecopy, reading):
    for p in (before, livecopy):
        if pathlib.Path(p).resolve() == LIVE.resolve():
            sys.exit("refused: this test runs on copies, never the live database")
    t_all = time.monotonic()
    out = pathlib.Path(tempfile.mkdtemp(prefix="gates-"))

    # ── the order of the gates (before copy) ──
    cfg = Cfg(pathlib.Path(before))
    conn = cfg.conn
    st = rc.settings(cfg)
    for k in ("sweep", "evidence"):
        ins = rc.instruction(conn, st[k])
        case(f"G1{'a' if k == 'sweep' else 'b'}", f"the {k} instruction carries its rules, read live", len(ins["keep"]) == len(st[k]["rules"]) and all(x["text"] for x in ins["keep"]), [x["rule"] for x in ins["keep"]])
    cid, gid, gname = rc._subgroup(conn, NAME, SUB)
    rc.read_structure(conn, cfg, "TEST-G", NAME, gname, out)
    conn.commit()
    gates = {r[3]: r for r in lr._rows(conn, cid, "2.1") if r[4] == gid and r[3] in rc.GATE_ITEMS}
    case("G2", "opening 2.1 for the subgroup makes one sweep row and one evidence-validation row, open", set(gates) == set(rc.GATE_ITEMS) and all(r[6] == "open" for r in gates.values()), {k: v[6] for k, v in gates.items()})
    m = refused(lambda: rc.read_sweep(conn, cfg, "TEST-G", NAME, gname, out))
    case("G3", "ReadSweep is refused while a 2.1 row of the subgroup is not answered and validated, naming ReadStructure", bool(m) and "ReadStructure" in (m or ""), m)
    m = refused(lambda: rc.read_evidence(conn, cfg, "TEST-G", NAME, gname, out))
    case("G4", "ReadEvidence is refused before the sweep, naming ReadSweep", bool(m) and "ReadSweep" in (m or ""), m)
    conn.rollback()
    m = refused(lambda: lr.record(conn, cfg, "TEST-G", {"collection": NAME, "step": "2.1", "subgroup": gname, "rows": [{"ledger_id": gates["sweep"][0], "fill": {"disposition": "observed"}}]}, False))
    case("G5", "a gate row is refused in a LayerRecord working file (it is answered by its own command)", bool(m) and "own command" in (m or ""), m)
    conn.rollback()
    pulled = lr.pull(conn, cfg, NAME, "2.1", out, subgroup=gname)
    items_pulled = {x["item"] for x in json.loads(pulled[0].read_text(encoding="utf-8"))["rows"]}
    case("G6", "LayerPull leaves the gate rows out", not (items_pulled & set(rc.GATE_ITEMS)), sorted(items_pulled))
    conn.rollback()
    n = ll.next_action(conn, cfg, NAME)
    case("G7", "LayerNext names the read command of the next open item (ReadStructure while 2.1 rows are open)", n["step"] == "2.1" and "ReadStructure" in " ".join(n["commands"]), n["commands"][:1])
    conn.close()

    # ── the sweep and the evidence validation on the live reading (live copy) ──
    cfg = Cfg(pathlib.Path(livecopy))
    conn = cfg.conn
    s = lr.settings(cfg)
    cid, gid, gname = rc._subgroup(conn, NAME, SUB)
    n = ll.next_action(conn, cfg, NAME)
    case("G8", "on the live reading, with 2.1 rows all validated, LayerNext names ReadSweep", "ReadSweep" in " ".join(n["commands"]), n["commands"][:1])
    r = rc.read_sweep(conn, cfg, "TEST-G", NAME, gname, out)
    conn.commit()
    pkg = json.loads(r["path"].read_text(encoding="utf-8"))
    L = lr.load(conn, cfg, NAME, pairs=False, subgroup=gname)
    unmarked = {o for o, v in rc.evidence_scope(conn, cfg, L, cid, gid)["obs"].items() if v["nature"] is None}
    shown = {o["observation"] for o in pkg["older"]}
    case("G9", "the sweep package holds every unmarked observation of the subgroup's scope, once (equal to the evidence scope's unmarked)", shown == unmarked and len(shown) == len(pkg["older"]),
         f"{len(shown)} shown, {len(unmarked)} unmarked in scope, {r['chars']} chars, {r['seconds']} s")
    rd = json.loads(pathlib.Path(reading).read_text(encoding="utf-8"))
    ans = {**pkg["answer"], "older": [{"observation": o["observation"], **rd[str(o["observation"])]} for o in pkg["answer"]["older"] if str(o["observation"]) in rd]}
    have = len(ans["older"]) == len(pkg["older"])
    case("G10", "a real answer exists for every observation of the sweep (Claude's reading)", have, f"{len(ans['older'])} of {len(pkg['older'])}")
    c0 = counts(conn)
    first = ans["older"][0] if ans["older"] else {}
    bad = [("G11", "an answer whose command is not ReadSweep", {**ans, "command": "ReadEvidence"}),
           ("G11b", "an answer that leaves an unmarked observation unanswered", {**ans, "older": ans["older"][1:]}),
           ("G11c", "an answer with an action the sweep does not take", {**ans, "older": [{**first, "action": "carry", "to": "3.1"}] + ans["older"][1:]}),
           ("G11d", "an answer with a reason under 20 characters", {**ans, "older": [{**first, "reason": "old"}] + ans["older"][1:]}),
           ("G11e", "an answer naming an observation that is not a candidate", {**ans, "older": ans["older"] + [{"observation": -7, "action": "keep", "nature": "evidence", "reason": "a reason long enough to pass"}]}),
           ("G11f", "an answer consuming into carriers that do not hold its occurrences (VA-03)", {**ans, "older": [{**a, "carriers": [a["carriers"][0]] if a.get("carriers") else a.get("carriers")} if a.get("observation") == 22433 else a for a in ans["older"]]})]
    for cid_, desc, data in bad:
        if not have and cid_ not in ("G11",):
            case(cid_, desc + " is refused whole, nothing written", None, "no real answer")
            continue
        m = refused(lambda: rc.record_sweep(conn, cfg, "TEST-G", data, keep=True))
        case(cid_, desc + " is refused whole, nothing written", bool(m) and counts(conn) == c0, m or "")
        conn.rollback()
    if have:
        p = rc.record_sweep(conn, cfg, "TEST-G", ans, keep=False)
        case("G12", "-Check previews the sweep: everything run, nothing kept", bool(p.get("preview")) and counts(conn) == c0, p)
        w = rc.record_sweep(conn, cfg, "TEST-G", ans, keep=True)
        conn.commit()
        left = rc.sweep_candidates(conn, cfg, s, L, cid, gid)
        acts = {}
        for a in ans["older"]:
            acts[a["action"]] = acts.get(a["action"], 0) + 1
        case("G13", "RecordSweep writes the sweep: nothing unmarked is left, the sweep row is validated, the next command is ReadEvidence",
             w["validated"] and not left and "ReadEvidence" in w["next"], f"{acts}; {w}")
        gone = [a["observation"] for a in ans["older"] if a["action"] in ("consume", "merge", "delete_neither")
                if conn.execute("SELECT deleted FROM ib_observation WHERE id=?", (a["observation"],)).fetchone()[0] != 1]
        case("G14", "every consumed observation is deleted, its consumption logged", not gone, gone[:5])
        m = refused(lambda: rc.read_sweep(conn, cfg, "TEST-G", NAME, gname, out))
        case("G15", "ReadSweep after the sweep has nothing to read and names ReadEvidence", bool(m) and "ReadEvidence" in (m or ""), m)
        conn.commit()

        re_ = rc.read_evidence(conn, cfg, "TEST-G", NAME, gname, out)
        conn.commit()
        ek = json.loads(re_["path"].read_text(encoding="utf-8"))
        steps = [x["step"] for x in ek["observations"]]
        order = ["S1", "1.1", "1.2", "2.1"]
        case("G16", "ReadEvidence: the code checks pass after the sweep; the package holds at most batch_observations, in the order of the steps, within its size",
             ek["code_checks"]["passes"] and len(steps) <= st["evidence"]["batch_observations"] and re_["chars"] <= st["evidence"]["package_max_chars"]
             and steps == sorted(steps, key=lambda x: order.index(x) if x in order else 9), f"{len(steps)} observations, {ek['batch']}, {re_['chars']} chars")
        case("G17", "every observation of the package carries its verses, and the verses are given once with their text",
             all(x["verses"] for x in ek["observations"]) and len({v["reference"] for v in ek["verses"]}) == len(ek["verses"]) and all(v["text"] for v in ek["verses"]), f"{len(ek['verses'])} verses")
        o1 = ek["observations"][0]["observation"]
        c1 = counts(conn)
        good = {"command": "ReadEvidence", "collection": NAME, "subgroup": gname, "observations": [{"observation": o1, "verdict": "true", "why": "test of the record's checks only, on a copy; the reading itself is the live run"}]}
        bad = [("G18", "an answer naming an observation that is not an evidence observation of the subgroup", {**good, "observations": [{**good["observations"][0], "observation": -3}]}),
               ("G18b", "a verdict that is neither true nor repair", {**good, "observations": [{**good["observations"][0], "verdict": "maybe"}]}),
               ("G18c", "a repair with no action", {**good, "observations": [{**good["observations"][0], "verdict": "repair"}]}),
               ("G18d", "a true verdict with an action", {**good, "observations": [{**good["observations"][0], "actions": [{"action": "annotate", "oid": o1, "note": "a note of ten or more"}]}]}),
               ("G18e", "a why under 20 characters", {**good, "observations": [{**good["observations"][0], "why": "true"}]}),
               ("G18f", "a repair whose action the validation refuses", {**good, "observations": [{**good["observations"][0], "verdict": "repair", "actions": [{"action": "restate", "oid": o1}]}]})]
        for cid_, desc, data in bad:
            m = refused(lambda: rc.record_evidence(conn, cfg, "TEST-G", data, keep=True))
            case(cid_, desc + " is refused whole, nothing written", bool(m) and counts(conn) == c1, m or "")
            conn.rollback()
        p = rc.record_evidence(conn, cfg, "TEST-G", {**good, "observations": [{**good["observations"][0], "verdict": "repair",
                                                                                 "actions": [{"action": "annotate", "oid": o1, "note": "test note on a copy, a repair test"}]}]}, keep=False)
        case("G19", "-Check previews a repair through the validation actions: run, nothing kept", bool(p.get("preview")) and p["actions"] == 1 and counts(conn) == c1, p)
        w = rc.record_evidence(conn, cfg, "TEST-G", good, keep=True)
        conn.commit()
        read_ = rc.evidence_read(conn, cfg, [o1])
        case("G20", "RecordEvidence logs the observation read; the gate stays open while others are unread", o1 in read_ and not w["validated"] and w["left"] > 0, w)
        r2 = rc.read_evidence(conn, cfg, "TEST-G", NAME, gname, out)
        k2 = json.loads(r2["path"].read_text(encoding="utf-8"))
        case("G21", "the next ReadEvidence leaves the read observation out", o1 not in {x["observation"] for x in k2["observations"]}, k2["batch"])
        conn.rollback()
        # scaffolding on the copy: the remaining reads logged directly, to show the gate closing end to end (the real reading is the live run)
        from iba.app.lib import observationrecord as orec
        sc = rc.evidence_scope(conn, cfg, L, cid, gid)
        for oid, v in sc["obs"].items():
            if v["nature"] == "evidence" and oid not in rc.evidence_read(conn, cfg, [oid]):
                orec.log(conn, oid, None, "evidence_read", None, "true", "scaffolding of the test on a copy: read logged directly", None, "TEST-G", "Claude")
        conn.commit()
        m = refused(lambda: rc.read_evidence(conn, cfg, "TEST-G", NAME, gname, out))
        conn.commit()
        ev = rc._gate_row(conn, cid, gid, rc.EVIDENCE_ITEM)
        n = ll.next_action(conn, cfg, NAME)
        p_ = {g["name"]: g for g in ll.progress(conn, cfg, NAME)["subgroups"]}[gname]
        case("G22", "(scaffolding) with every evidence observation read, ReadEvidence answers the gate, it validates, 2.1 closes and LayerNext moves to 3.1",
             bool(ev[9]) and p_["steps"]["2.1"] == "closed" and n["step"] == "3.1", f"{m}; 2.1={p_['steps']['2.1']}; next {n['step']}")
    else:
        for c_ in ("G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20", "G21", "G22"):
            case(c_, "needs the real sweep", None, "")

    scans = []
    for sql, args in [("SELECT DISTINCT observation_id FROM ib_observation_change WHERE column_name='evidence_read' AND observation_id IN (?,?)", (1, 2)),
                      ("SELECT DISTINCT n.observation_id FROM ib_node n WHERE n.deleted=0 AND n.traced_observation_id IS NULL AND n.verse_lexical_id IN (?,?)", (1, 2)),
                      ("SELECT id, verse_id FROM verse_lexical WHERE id IN (?,?)", (1, 2))]:
        scans += sg.full_scans(conn, cfg, sql, args)
    case("G23", "no lookup of the gates scans a large table (query plans)", not scans, scans)
    case("G24", "the whole test ran in under a minute", time.monotonic() - t_all < 60, f"{time.monotonic() - t_all:.1f} s")
    print("\n| case | what | result | evidence |\n|---|---|---|---|")
    for r_ in results:
        print(f"| {r_[0]} | {r_[1]} | {r_[2]} | {r_[3]} |")
    print(f"\n{sum(1 for r_ in results if r_[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r_[2] != "FAIL" for r_ in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
