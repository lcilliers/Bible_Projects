"""temp_2538_elements_test_run.py -- the test plan of ReadElements / RecordElements, step 3.1 (escalation #2538; lib/readcommands.py; B:46).

Runs on a COPY of iba.db with elements_2538_v1_20261126.py applied, never the live database. Where every subgroup is through 3.1 (live since 2026-11-26), temp_2538_test_state.back_to first puts
"reasoning" back to 3.1 not yet read on the copy, so the cases test the state they describe whatever the state of live.
The 3.1 reading itself is the researcher-approved live run, not a test. The record is tested with refused answers and with one minimal answer (case X12 on), written here as
scaffolding on the copy: one finding resting on one sense, every other observation declared not used with a test reason, the older inner-being observations kept, the earlier
readings left. It proves the record, the check and the loop moving on; it is not a reading.

Usage: python iba/app/tools/temp_2538_elements_test_run.py <db copy> [collection] [subgroup]
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
from iba.app.lib import layerinner as li  # noqa: E402
from iba.app.lib import layerloop as ll  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import readcommands as rc  # noqa: E402
from iba.app.lib import scanguard as sg  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
results = []
TEST = "test scaffolding on a copy: not a reading"


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


def main(db, name="thought", sub="reasoning"):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    t_all = time.monotonic()
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    out = pathlib.Path(tempfile.mkdtemp(prefix="elements-"))
    st = rc.settings(cfg)
    rt, lim = st["elements"], st["limits"]
    s = lr.settings(cfg)
    cid, gid, gname = rc._subgroup(conn, name, sub)
    if not ts.in_loop(conn, cfg, name):
        print(ts.back_to(conn, cfg, name, gname, "3.1", "TEST-X-STATE"), file=sys.stderr)

    ins = rc.instruction(conn, rt)
    case("X1", "the instruction carries what, read, write, and the text of every rule it keeps, read live", len(ins["keep"]) == len(rt["rules"]) and all(k["text"] for k in ins["keep"]), [k["rule"] for k in ins["keep"]])
    n = ll.next_action(conn, cfg, name)
    case("X2", "LayerNext names ReadElements for the subgroup at 3.1", n["step"] == "3.1" and "ReadElements" in " ".join(n["commands"]), n["commands"][:1])
    r = rc.read_elements(conn, cfg, "TEST-X", name, gname, out)
    conn.commit()
    k = json.loads(r["path"].read_text(encoding="utf-8"))
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    sd = lr.step_def(s, "3.1")
    sources, required = li._sources(conn, s, L, sd, gid, "")
    take = [x["observation"] for x in k["to_take_up"]]
    case("X3", "ReadElements opens 3.1 for the subgroup and its package takes up exactly the observations the recorder demands, the senses first",
         set(take) == required and len(take) == len(set(take)) and {x["observation"] for x in k["may_rest_on_besides"]} == sources - required
         and [x["stage"] for x in k["to_take_up"]][0] == s["stages"]["1"], f"{len(take)} to take up, {len(k['may_rest_on_besides'])} besides, opened {r['opened'] is not None}")
    case("X4", "the package is within its size and time limits, the meaning by code cut to lexicon_chars",
         r["chars"] <= rt["package_max_chars"] and r["seconds"] <= lim["read_max_seconds"] and all(len(v.get("meaning_range") or "") <= rt["lexicon_chars"] for v in k["meaning_by_code"].values()),
         f"{r['chars']} chars, {r['seconds']} s")
    case("X5", "every verse of the subgroup is given once with its text, and every occurrence", len(k["verses"]) == len({o["osis"] for o in k["occurrences"]}) and all(v["text"] for v in k["verses"]),
         f"{len(k['verses'])} verses, {len(k['occurrences'])} occurrences")
    case("X6", "the earlier readings of the scope (inner being of the build stages, not the subgroup's own) are listed for `existing`", all(e["observation"] for e in k["earlier_readings"]),
         f"{len(k['earlier_readings'])} earlier readings, {len(k['older_inner_being'])} older inner-being")

    # the scaffolding answer: one finding resting on a sense, on an occurrence of it that holds an older inner-being observation where there is one (so RW-13 is exercised)
    osis = {o["occurrence"]: o["osis"] for o in k["occurrences"]}
    occ_ids = set(osis)
    older_on = {o["observation"]: {r[0] for r in conn.execute("SELECT verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_lexical_id IS NOT NULL", (o["observation"],))} & occ_ids
                for o in k["older_inner_being"]}
    done = lr.bv.settled(conn, cfg, list(older_on)) | lr.bv.carried_later(conn, list(older_on), "3.1")      # an older observation already answered is not demanded again (RW-13)
    older_on = {o: v for o, v in older_on.items() if o not in done}
    senses = [x["observation"] for x in k["to_take_up"] if x["stage"] == s["stages"]["1"] and x["kind"] == "group"]
    pick = next(((sn, o) for sn in senses for o in sorted(li._covered(conn, [sn]) & occ_ids) if any(o in v for v in older_on.values())), None)
    sense, first_occ = pick if pick else (senses[0], sorted(li._covered(conn, [senses[0]]) & occ_ids)[0])
    cov = [first_occ] + sorted((li._covered(conn, [sense]) & occ_ids) - {first_occ})
    spec = orec.items_setting(cfg)
    mode = spec["modes"][0]
    text_of = {v["reference"]: v["text"] for v in k["verses"]}
    v0 = osis[cov[0]]
    grounds = " ".join(text_of[v0].split()[:3])
    finding = {"key": "t1", "kind": "statement", "text": f"Test finding on a copy: the act of the sense in {v0} is an operation of speech; {TEST}.", "basis": "read",
               "parts": {"item": "operation", "grounds": grounds, "mode": mode}, "nodes": [{"occurrence": cov[0], "role": "characteristic"}, {"traced": sense}]}
    ans = {"command": "ReadElements", "collection": name, "subgroup": gname, "ledger_id": k["answer"]["ledger_id"], "findings": [finding],
           "not_used": {str(o): TEST for o in take if o != sense},
           "older": [{"observation": o, "action": "keep", "nature": "inner_being", "reason": TEST} for o, v in older_on.items() if cov[0] in v],
           "existing": [{"observation": e["observation"], "action": "leave", "reason": TEST} for e in k["earlier_readings"]]}
    c0 = counts(conn)
    bad = [("X7", "an answer whose command is not ReadElements", {**ans, "command": "ReadEvidence"}),
           ("X7b", "an answer naming another ledger row", {**ans, "ledger_id": -1}),
           ("X7c", "an answer that leaves an earlier reading out of `existing`", {**ans, "existing": ans["existing"][1:]} if ans["existing"] else None),
           ("X7d", "a finding resting on an observation the row may not rest on", {**ans, "findings": [{**finding, "nodes": finding["nodes"][:1] + [{"traced": -9}]}]}),
           ("X7e", "a finding with an occurrence outside what it rests on and no read-back", {**ans, "findings": [{**finding, "nodes": finding["nodes"] + [{"occurrence": next(o for o in osis if o not in cov), "role": "standalone"}]}]}),
           ("X7f", "an observation taken up that is neither rested on nor declared not used", {**ans, "not_used": dict(list(ans["not_used"].items())[1:])}),
           ("X7g", "an older inner-being observation on a named occurrence left unanswered (RW-13)", {**ans, "older": ans["older"][1:]} if ans["older"] else None),
           ("X7i", "an answer to an older observation on no occurrence the findings name (shown, not demanded: IB-05)",
            {**ans, "older": ans["older"] + [{"observation": o, "action": "keep", "nature": "inner_being", "reason": TEST} for o, v in older_on.items() if cov[0] not in v][:1]}
            if any(cov[0] not in v for v in older_on.values()) else None),
           ("X7h", "a finding whose item the step does not use", {**ans, "findings": [{**finding, "parts": {**finding["parts"], "item": "meaning"}}]})]
    for cid_, desc, data in bad:
        if data is None:
            case(cid_, desc + " is refused whole, nothing written", None, "nothing of that kind on this subgroup")
            continue
        m = refused(lambda: rc.record_elements(conn, cfg, "TEST-X", data, keep=True))
        case(cid_, desc + " is refused whole, nothing written", bool(m) and counts(conn) == c0, m or "")
        conn.rollback()
    m = refused(lambda: rc.record_elements(conn, cfg, "TEST-X", ans, keep=False))
    case("X8", "(scaffolding) -Check previews the minimal answer: checked whole, nothing kept", m is None and counts(conn) == c0, m or "previewed")
    conn.rollback()
    if m is None:
        w = rc.record_elements(conn, cfg, "TEST-X", ans, keep=True)
        conn.commit()
        row = rc._elements_row(conn, cid, gid)
        obs = conn.execute("SELECT nature, stage FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{row[0]}:", f"layer:{row[0]};")).fetchall()
        case("X9", "(scaffolding) RecordElements writes it: the 3.1 row validated, the finding marked inner_being at stage 4", w["validated"] and obs and all(o[0] == "inner_being" for o in obs), f"{w}; {[tuple(o) for o in obs]}")
        p_ = {g["name"]: g for g in ll.progress(conn, cfg, name)["subgroups"]}[gname]
        n = ll.next_action(conn, cfg, name)
        case("X10", "(scaffolding) the subgroup's loop is complete and LayerNext moves to the next subgroup", p_["complete"] and n.get("subgroup") != gname, f"complete {p_['complete']}; next {n.get('subgroup')} {n.get('step')}")
        m2 = refused(lambda: rc.read_elements(conn, cfg, "TEST-X", name, gname, out))
        case("X11", "ReadElements on a subgroup whose 3.1 is validated is refused, naming LayerNext", bool(m2) and "LayerNext" in (m2 or ""), m2)
    else:
        for c_ in ("X9", "X10", "X11"):
            case(c_, "needs the scaffolding answer", None, "")
    scans = []
    for sql, args in [("SELECT DISTINCT verse_lexical_id FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NOT NULL AND observation_id IN (?,?)", (1, 2)),
                      ("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", ("layer:1:", "layer:1;"))]:
        scans += sg.full_scans(conn, cfg, sql, args)
    case("X12", "no lookup of the read scans a large table (query plans)", not scans, scans)
    case("X13", "the whole test ran in under a minute", time.monotonic() - t_all < 60, f"{time.monotonic() - t_all:.1f} s")
    print("\n| case | what | result | evidence |\n|---|---|---|---|")
    for r_ in results:
        print(f"| {r_[0]} | {r_[1]} | {r_[2]} | {r_[3]} |")
    print(f"\n{sum(1 for r_ in results if r_[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r_[2] != "FAIL" for r_ in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
