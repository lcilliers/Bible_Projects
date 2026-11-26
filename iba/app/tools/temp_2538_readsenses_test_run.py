"""temp_2538_readsenses_test_run.py -- the test plan of ReadSenses / RecordSenses (escalation #2538; lib/readcommands.py; B:46).

Runs on a COPY of iba.db, never the live database. The copy must hold the subgroup through S1 and 1.1 not yet open: for thought, the copy that temp_2538_readwords_test_run.py has run on
(the named snapshot iba-20261125T123416Z-pre-2538-findings-apply.db with the #2538 migrations applied: findings, layernext_verb, readwords, senses).
The real answer (case S12 on) is the 1.1 reading of the same subgroup recorded in the live database (read-only): each live sense by its occurrences, turned into the B1 observations of the
copy it carries; the older observations answered as live answered them.

Usage: python iba/app/tools/temp_2538_readsenses_test_run.py <db copy> [collection] [subgroup] [other subgroup]
"""
import json
import pathlib
import sqlite3
import sys
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import readcommands as rc  # noqa: E402
from iba.app.lib import scanguard as sg  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.handlers.collectionbuild import _answer_of  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
results = []


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


def main(db, name="thought", sub="meditating and pondering", other="reasoning"):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    t_all = time.monotonic()
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    q = lambda s_, *a: conn.execute(s_, a).fetchall()  # noqa: E731
    out = pathlib.Path(tempfile.mkdtemp(prefix="readsenses-"))
    st = rc.settings(cfg)
    rt, lim = st["senses"], st["limits"]
    s = lr.settings(cfg)
    cid, gid, gname = rc._subgroup(conn, name, sub)

    ins = rc.instruction(conn, rt)
    case("S1", "the instruction carries what, read, write, and the text of every rule it keeps, read live from cfg_method_rule",
         len(ins["keep"]) == len(rt["rules"]) and all(k["text"] for k in ins["keep"]) and bool(ins["read"]) and bool(ins["write"]), [k["rule"] for k in ins["keep"]])
    case("S2", "an unknown subgroup is refused", bool(refused(lambda: rc.read_senses(conn, cfg, "TEST-RS", name, "no such subgroup", out))), "")
    m = refused(lambda: rc.read_senses(conn, cfg, "TEST-RS", name, other, out))
    case("S3", "ReadSenses for a subgroup not through S1 is refused (the order gate or the step's needs)", bool(m), m)
    conn.rollback()

    s1_rows = q("SELECT id FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='S1' AND item='word-sense' AND deleted=0 AND state!='retired'", cid, gid)
    b1_db = set()
    for (lid,) in s1_rows:
        b1_db |= {x[0] for x in q("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", f"layer:{lid}:", f"layer:{lid};")}
    before = q("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.1' AND deleted=0 AND item='group-definition'", cid, gid)[0][0]
    r = rc.read_senses(conn, cfg, "TEST-RS", name, gname, out)
    pkg = json.loads(r["path"].read_text(encoding="utf-8"))
    conn.commit()
    row = rc._word_rows(conn, cid, gid, "1.1", "group-definition")
    case("S4", "ReadSenses opens 1.1 for the subgroup (its group-definition row is made) and writes a package", before == 0 and len(row) == 1 and r["path"].exists(),
         f"rows before {before}, after {len(row)}, opened {r['opened']}")
    got = [x["observation"] for x in pkg["readings"]]
    case("S5", "the package carries every B1 observation of the subgroup once (equal to the observations of its S1 rows)", len(got) == len(set(got)) and set(got) == b1_db,
         f"package {len(got)}, S1 rows' observations {len(b1_db)}")
    occ_pkg = [o["occurrence"] for x in pkg["readings"] for o in x["occurrences"]] + [o["occurrence"] for o in pkg["occurrences_in_no_reading"]]
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    occ_db = {o["vl_id"] for o, _ in lr.expected_nodes(L, "group-definition", gid, row[0][5])}
    loose = {o["occurrence"] for o in pkg["occurrences_in_no_reading"]}
    held = {o["occurrence"] for x in pkg["readings"] for o in x["occurrences"]}
    case("S6", "every occurrence of the subgroup is in a reading or listed as in no reading, never both", set(occ_pkg) == occ_db and not (loose & held),
         f"{len(occ_db)} occurrences, {len(held)} held by readings, {len(loose)} in no reading: {[o['word'] for o in pkg['occurrences_in_no_reading']]}")
    codes_db = {o["strong"] for o, _ in lr.expected_nodes(L, "group-definition", gid, row[0][5]) if o["strong"]}
    case("S7", "every code of the subgroup has its sense head and meaning range, the range within lexicon_chars",
         set(pkg["codes"]) == codes_db and all(len(c["meaning_range"] or "") <= rt["lexicon_chars"] for c in pkg["codes"].values()), f"{len(pkg['codes'])} codes")
    stamped = q("SELECT pulled_at FROM collection_layer_item WHERE id=?", row[0][0])[0][0]
    case("S8", "the row is stamped pulled_at; the package is within its size and time limits", bool(stamped) and r["chars"] <= rt["package_max_chars"] and r["seconds"] <= lim["read_max_seconds"],
         f"{r['chars']} chars (limit {rt['package_max_chars']}), {r['seconds']} s")
    shown = {o["observation"] for o in pkg["older"]}
    led = {int(x[0]) for x in q("SELECT subject FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.1' AND item='old-observation' AND state='open' AND deleted=0", cid, gid)}
    case("S9", "every older observation carried open to 1.1 for the subgroup is shown, once, with its text (RW-09)",
         led <= shown and len(pkg["older"]) == len(shown) and all(o["text"] for o in pkg["older"]), f"shown {len(shown)}, open in the ledger at 1.1 {len(led)}, shown and not in the ledger {sorted(shown - led)[:6]}")

    # ── the real answer: the live 1.1 senses of the subgroup, by occurrence, as carries of the copy's B1 observations
    live = sqlite3.connect(f"file:{LIVE.as_posix()}?mode=ro", uri=True)
    lcid = live.execute("SELECT id FROM collection WHERE name=? AND deleted=0", (name,)).fetchone()[0]
    lgid = live.execute("SELECT id FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND lower(name)=?", (lcid, gname.lower())).fetchone()[0]
    llid = [x[0] for x in live.execute("SELECT id FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.1' AND item='group-definition' AND deleted=0 AND state='observed'", (lcid, lgid))]
    held_by = {x["observation"]: {o["occurrence"] for o in x["occurrences"]} for x in pkg["readings"]}
    senses, used = [], set()
    for lid in llid:
        for oid, tag, text, basis, parts in live.execute("SELECT id, tag, obs_text, basis, parts FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};")):
            vls = {x[0] for x in live.execute("SELECT verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IS NOT NULL", (oid,))}
            carries = sorted(b for b, h in held_by.items() if h and h <= vls and b not in used)
            used |= set(carries)
            rest = sorted(vls - set().union(*(held_by[b] for b in carries)) if carries else vls)
            senses.append({"kind": tag, "obs_text": text, "basis": basis, "grounds": (json.loads(parts) if parts else {}).get("grounds") or "", "carries": carries, "occurrences": rest})
    old_ans, missing = [], []
    for o in pkg["older"]:
        ch = {k: (v, rs) for k, v, rs in live.execute("SELECT column_name, new_value, reason FROM ib_observation_change WHERE observation_id=? AND node_id IS NULL AND column_name IN ('build_answer','carried_to') ORDER BY id", (o["observation"],))}
        nat = (live.execute("SELECT nature FROM ib_observation WHERE id=?", (o["observation"],)).fetchone() or [None])[0]
        if "build_answer" in ch:
            act, rs = ch["build_answer"]
            a = {"observation": o["observation"], "action": act, "reason": rs}
            if act == "keep":
                a["nature"] = nat
            elif act == "consume":
                a.update({"carriers": ["this"], "mapping": rs})
        elif "carried_to" in ch and ch["carried_to"][0] != "1.1":
            a = {"observation": o["observation"], "action": "carry", "to": ch["carried_to"][0], "reason": ch["carried_to"][1]}
        else:
            missing.append(o["observation"])
            continue
        old_ans.append(a)
    answer = {"command": "ReadSenses", "collection": name, "subgroup": gname, "ledger_id": row[0][0], "senses": senses, "older": old_ans}
    have = bool(senses) and not missing
    case("S10", "a real answer exists: the live senses of the subgroup and the live answers to its older observations", have,
         f"{len(senses)} senses carrying {len(used)} of {len(held_by)} B1 observations, {sum(len(x['occurrences']) for x in senses)} occurrences named; older answers {len(old_ans)}/{len(pkg['older'])}, missing {missing[:5]}")

    c0 = counts(conn)
    first = senses[0] if senses else {}
    some_b1 = next(iter(held_by), None)
    bad = [("S11", "an answer whose command is not ReadSenses", {**answer, "command": "ReadWords"}),
           ("S11b", "an answer naming the ledger row of another subgroup or step", {**answer, "ledger_id": -1}),
           ("S11c", "an answer whose sense carries an observation that is not a B1 observation of the subgroup", {**answer, "senses": [{**first, "carries": first.get("carries", []) + [-5]}] + senses[1:]}),
           ("S11d", "an answer carrying one B1 observation in two senses", {**answer, "senses": senses + [{**first, "obs_text": first.get("obs_text", "") + " (again)", "carries": [some_b1], "occurrences": []}]}),
           ("S11e", "an answer in which a B1 observation is carried by no sense", {**answer, "senses": [{**x, "carries": [b for b in x["carries"] if b != some_b1], "occurrences": [v for v in x["occurrences"] if v not in held_by.get(some_b1, set())]} for x in senses]}),
           ("S11f", "an answer whose read grounds are not words of the codes' lexicon", {**answer, "senses": [{**first, "basis": "read", "grounds": "zz nothing in any lexicon zz"}] + senses[1:]}),
           ("S11g", "an answer that leaves the older observations unanswered (RW-13)", {**answer, "older": []} if pkg["older"] else None)]
    for cid_, desc, data in bad:
        if data is None:
            case(cid_, desc + " is refused whole, nothing written", None, "no older observation shown")
            continue
        if not have and cid_ not in ("S11", "S11b"):
            case(cid_, desc + " is refused whole, nothing written", None, "no real answer")
            continue
        m = refused(lambda: rc.record_senses(conn, cfg, "TEST-RS", data, keep=True))
        case(cid_, desc + " is refused whole, nothing written", bool(m) and counts(conn) == c0, m or "")
        conn.rollback()

    whole = {**pkg, "answer": answer}
    case("S12", "the record takes the whole package with its answer filled, as it takes the bare answer", _answer_of(whole) is answer and _answer_of(answer) is answer, "")
    if have:
        p = rc.record_senses(conn, cfg, "TEST-RS", answer, keep=False)
        case("S13", "-Check previews the real answer: everything checked, nothing kept", bool(p.get("preview")) and counts(conn) == c0, p)
        conn.rollback()
        w = rc.record_senses(conn, cfg, "TEST-RS", answer, keep=True)
        conn.commit()
        c1 = counts(conn)
        lid = row[0][0]
        obs = q("SELECT id, nature, tag FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", f"layer:{lid}:", f"layer:{lid};")
        case("S14", "RecordSenses writes the real answer: the row validated, one group observation for each sense, each marked evidence at creation",
             w["validated"] and len(obs) == len(senses) and all(o[1] == "evidence" and o[2] == "group" for o in obs), f"{w}; {len(obs)} observations")
        traced = {}
        for o in obs:
            traced[o[0]] = {x[0] for x in q("SELECT traced_observation_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NOT NULL", o[0])}
        all_traced = set().union(*traced.values()) if traced else set()
        case("S15", "every sense traces to the B1 observations it carries, and together the senses trace every B1 observation of the subgroup",
             all(traced.values()) and all_traced >= set(held_by), f"traced {len(all_traced & set(held_by))} of {len(held_by)} B1 observations")
        old_open = q("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.1' AND item='old-observation' AND state='open' AND deleted=0", cid, gid)[0][0]
        case("S16", "no older observation of 1.1 is left open for the subgroup, and the next command named is ReadEnrichment", old_open == 0 and "ReadEnrichment" in w["next"], f"open {old_open}; {w['next']}")
        m = refused(lambda: rc.read_senses(conn, cfg, "TEST-RS", name, gname, out))
        case("S17", "ReadSenses on a subgroup whose senses are read and validated is refused, naming the next command", bool(m) and "ReadEnrichment" in (m or ""), m)
        case("S18", "the real answer recorded again is refused (the row is validated)", bool(refused(lambda: rc.record_senses(conn, cfg, "TEST-RS", answer, keep=True))) and counts(conn) == c1, "")
        conn.rollback()
    else:
        for c_ in ("S13", "S14", "S15", "S16", "S17", "S18"):
            case(c_, "needs the real answer", None, "")

    scans = []
    for sql, args in [("SELECT observation_id, verse_lexical_id FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND observation_id IN (?,?)", (1, 2)),
                      ("SELECT id, tag, obs_text, basis, parts FROM ib_observation WHERE deleted=0 AND id IN (?,?)", (1, 2)),
                      ("SELECT head FROM strong_sense WHERE strong=? AND deleted=0", ("H1897",)),
                      ("SELECT sense_code, sense_text FROM strong_meaning_tree WHERE strong_variant=? AND deleted=0 ORDER BY sort", ("H1897",))]:
        scans += sg.full_scans(conn, cfg, sql, args)
    case("S19", "no lookup of the read scans a large table (query plans)", not scans, scans)
    case("S20", "the whole test ran in under a minute", time.monotonic() - t_all < 60, f"{time.monotonic() - t_all:.1f} s")

    print("\n| case | what | result | evidence |\n|---|---|---|---|")
    for r_ in results:
        print(f"| {r_[0]} | {r_[1]} | {r_[2]} | {r_[3]} |")
    print(f"\n{sum(1 for r_ in results if r_[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r_[2] != "FAIL" for r_ in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
