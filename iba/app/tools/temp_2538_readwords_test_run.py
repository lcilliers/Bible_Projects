"""temp_2538_readwords_test_run.py -- the test plan of ReadWords / RecordWords (escalation #2538; lib/readcommands.py; B:46).

Runs on a COPY of iba.db, never the live database: the copy must hold the collection grouped and its subgroup not yet read in step S1 (for thought: the named snapshot
iba-20261125T123416Z-pre-2538-findings-apply.db with the two later config migrations of #2560 applied, then iba/app/migration/archive/readwords_2538_v1_20261125.py).
The real answer (case R12 on) is the reading of the same words recorded in the live database (read-only, by word and verse reference), so the recorder is tested on real readings.

Usage: python iba/app/tools/temp_2538_readwords_test_run.py <db copy> [collection] [subgroup] [other subgroup]
"""
import json
import pathlib
import sqlite3
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import temp_2538_test_state as ts  # noqa: E402
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import readcommands as rc  # noqa: E402
from iba.app.lib import scanguard as sg  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
results = []


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed is True else ("BLOCKED" if passed is None else "FAIL"), str(evidence).replace("|", "/")[:330]))
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
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    q = lambda s, *a: conn.execute(s, a).fetchall()  # noqa: E731
    out = pathlib.Path(tempfile.mkdtemp(prefix="readwords-"))
    st = rc.settings(cfg)
    rt, lim = st["words"], st["limits"]
    if not ts.in_loop(conn, cfg, name):      # live is past this step: the copy is put back to it (temp_2538_test_state, BUILD.md 597)
        print(ts.back_to(conn, cfg, name, sub, 'S1'), file=sys.stderr)
        print(ts.back_to(conn, cfg, name, other, 'S1'), file=sys.stderr)
    cid, gid, gname = rc._subgroup(conn, name, sub)

    ins = rc.instruction(conn, rt)
    case("R1", "the instruction carries what, read, write, and the text of every rule it keeps, read live from cfg_method_rule",
         len(ins["keep"]) == len(rt["rules"]) and all(k["text"] for k in ins["keep"]) and bool(ins["read"]) and bool(ins["write"]), [k["rule"] for k in ins["keep"]])
    case("R2", "a read naming a rule that is not active is refused (synthetic)", bool(refused(lambda: rc.instruction(conn, {**rt, "rules": rt["rules"] + ["XX-99"]}))),
         refused(lambda: rc.instruction(conn, {**rt, "rules": ["XX-99"]})))
    case("R3", "an unknown subgroup is refused", bool(refused(lambda: rc.read_words(conn, cfg, "TEST-RW", name, "no such subgroup", out))), "")

    before = q("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='S1' AND deleted=0 AND state!='retired'", cid, gid)[0][0]
    r = rc.read_words(conn, cfg, "TEST-RW", name, gname, out)
    pkg = json.loads(r["path"].read_text(encoding="utf-8"))
    words_all = q("SELECT id, subject FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='S1' AND item='word-sense' AND deleted=0 AND state!='retired'", cid, gid)
    case("R4", "ReadWords opens S1 for a subgroup with no rows (the ledger rows are made) and writes a package", before == 0 and len(words_all) > 0 and r["path"].exists(),
         f"rows before {before}, word rows {len(words_all)}, opened {r['opened']}")
    case("R5", "the package holds at most batch_words words; its words stay within package_max_chars", 0 < r["words"] <= rt["batch_words"] and r["chars"] <= lim["package_max_chars"] + 20000,
         f"{r['words']} words, {r['chars']} chars (with the instruction), {r['seconds']} s")
    ok, ev = True, []
    for w in pkg["words"]:
        n_db = q("SELECT count(*) FROM verse_lexical WHERE strong=? AND surface=? AND deleted=0", w["strong"], w["word"])[0][0]
        ok &= len(w["occurrences"]) == n_db and all(o["verse"] for o in w["occurrences"])
        ev.append(f"{w['word']}/{w['strong']} {len(w['occurrences'])}/{n_db}")
    case("R6", "every word carries every one of its occurrences, each with its verse text (equal to an independent count on verse_lexical)", ok, "; ".join(ev))
    case("R7", "the lexicon in the package is trimmed (no source over 700 characters)",
         all(len(w["lexicon"].get(k) or "") <= 700 for w in pkg["words"] for k in ("lsj", "mounce", "meaning_range")), "")
    ids_ = [w["ledger_id"] for w in pkg["words"]]
    stamped = q(f"SELECT count(*) FROM collection_layer_item WHERE id IN ({','.join('?' * len(ids_))}) AND pulled_at IS NOT NULL", *ids_)[0][0]
    case("R8", "the ledger rows of the package are stamped pulled_at; the answer has one row for each word", stamped == len(ids_) and len(pkg["answer"]["rows"]) == len(ids_), f"stamped {stamped}")
    case("R9", "the read took under read_max_seconds", r["seconds"] <= lim["read_max_seconds"], f"{r['seconds']} s")

    msg = refused(lambda: rc.read_words(conn, cfg, "TEST-RW", name, other, out))
    case("R10", "ReadWords for another subgroup is refused while this one is further through its loop (the order gate)", bool(msg) and gname in (msg or ""), msg)

    seen, packages, overlap = set(ids_), [pkg], False
    while r["left"] and len(packages) < 20:
        r = rc.read_words(conn, cfg, "TEST-RW", name, gname, out)
        p2 = json.loads(r["path"].read_text(encoding="utf-8"))
        ids = {w["ledger_id"] for w in p2["words"]}
        overlap |= bool(ids & seen)
        seen |= ids
        packages.append(p2)
    case("R11", "repeated ReadWords gives the next words; together the packages carry every word once", seen == {w[0] for w in words_all} and not overlap, f"{len(packages)} package(s), {len(seen)} words")
    shown = [o["observation"] for p_ in packages for w in p_["words"] for o in w["older"]]
    ledger_old = {int(x[0]) for x in q("SELECT subject FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='S1' AND item='old-observation' AND state='open' AND deleted=0", cid, gid)}
    case("R11b", "every older observation open in the ledger for the subgroup is shown once, under one word, with its text (RW-09)", len(shown) == len(set(shown)) and set(shown) == ledger_old
         and all(o["text"] for p_ in packages for w in p_["words"] for o in w["older"]), f"shown {len(shown)}, ledger {len(ledger_old)}")
    under = {o["observation"]: w["ledger_id"] for p_ in packages for w in p_["words"] for o in w["older"]}
    conn.commit()

    live = sqlite3.connect(f"file:{LIVE.as_posix()}?mode=ro", uri=True)
    lcid = live.execute("SELECT id FROM collection WHERE name=? AND deleted=0", (name,)).fetchone()[0]
    lgid = live.execute("SELECT id FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND lower(name)=?", (lcid, gname.lower())).fetchone()[0]
    real = {}
    for lid, subj in live.execute("SELECT id, subject FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='S1' AND item='word-sense' AND deleted=0 AND state='observed'", (lcid, lgid)):
        rd = []
        for oid, tag, text, basis, parts in live.execute("SELECT id, tag, obs_text, basis, parts FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};")):
            refs = [x[0] for x in live.execute("SELECT DISTINCT verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IS NOT NULL", (oid,))]
            grounds = (json.loads(parts) if parts else {}).get("grounds") or ""
            rd.append({"kind": tag, "obs_text": text, "basis": basis or "stated", "grounds": grounds, "occurrences": refs})
        real[subj] = rd
    old_ans, missing = {}, []      # the live answers to the older observations at S1, from the change log
    for oid in under:
        ch = {k: (v, rs) for k, v, rs in live.execute("SELECT column_name, new_value, reason FROM ib_observation_change WHERE observation_id=? AND node_id IS NULL AND column_name IN ('build_answer','carried_to') ORDER BY id", (oid,))}
        nat = (live.execute("SELECT nature FROM ib_observation WHERE id=?", (oid,)).fetchone() or [None])[0]
        if "carried_to" in ch:
            a = {"observation": oid, "action": "carry", "to": ch["carried_to"][0], "reason": ch["carried_to"][1]}
        elif "build_answer" in ch:
            act, rs = ch["build_answer"]
            a = {"observation": oid, "action": act, "reason": rs}
            if act == "keep":
                a["nature"] = nat
            elif act == "consume":
                a.update({"carriers": ["this"], "mapping": rs})
        else:
            missing.append(oid)
            continue
        old_ans.setdefault(under[oid], []).append(a)
    answer = {"command": "ReadWords", "collection": name, "subgroup": gname, "rows": [{"ledger_id": i, "readings": real.get(s, []), "older": old_ans.get(i, [])} for i, s in words_all]}
    have_real = all(real.get(s) for _, s in words_all) and not missing
    case("R12", "a real answer exists for every word and every older observation (the live reading of the same words, and the live answers from the change log)", have_real,
         f"words {sum(1 for _, s in words_all if real.get(s))}/{len(words_all)}, older answers {sum(len(v) for v in old_ans.values())}/{len(under)}, missing {missing[:5]}")

    c0 = counts(conn)
    first = answer["rows"][0] if answer["rows"] else {"readings": [{}]}
    bad = [("R13", "an answer whose command is not ReadWords", {**answer, "command": "LayerRecord"}),
           ("R14", "an answer naming a ledger row of another subgroup", {**answer, "rows": answer["rows"] + [{"ledger_id": -1, "readings": []}]}),
           ("R15", "an answer that leaves the occurrences of a word out", {**answer, "rows": [{**first, "readings": [{**first["readings"][0], "occurrences": []}]}] + answer["rows"][1:]}),
           ("R16", "an answer with a text under min_text_chars", {**answer, "rows": [{**first, "readings": [{**x, "obs_text": "too short"} for x in first["readings"]]}] + answer["rows"][1:]}),
           ("R17", "an answer with a kind the item does not take", {**answer, "rows": [{**first, "readings": [{**x, "kind": "pairing"} for x in first["readings"]]}] + answer["rows"][1:]}),
           ("R17b", "an answer that leaves the older observations of the words unanswered (RW-13)", {**answer, "rows": [{**x, "older": []} for x in answer["rows"]]} if under else None)]
    for cid_, desc, data in bad:
        if data is None:
            case(cid_, desc + " is refused whole, nothing written", None, "no older observation in the subgroup")
            continue
        if not have_real and cid_ != "R13":
            case(cid_, desc + " is refused whole, nothing written", None, "no real answer")
            continue
        m = refused(lambda: rc.record_words(conn, cfg, "TEST-RW", data, keep=True))
        case(cid_, desc + " is refused whole, nothing written", bool(m) and counts(conn) == c0, (m or "")[:200])
        conn.rollback()

    if have_real:
        p = rc.record_words(conn, cfg, "TEST-RW", answer, keep=False)
        case("R18", "-Check previews the real answer: everything checked, nothing kept", bool(p.get("preview")) and counts(conn) == c0, p)
        conn.rollback()
        w = rc.record_words(conn, cfg, "TEST-RW", answer, keep=True)
        conn.commit()
        c1 = counts(conn)
        nat = q("SELECT count(*), sum(o.nature='evidence') FROM collection_layer_item l JOIN ib_observation o ON o.stable_key >= 'layer:' || l.id || ':' AND o.stable_key < 'layer:' || l.id || ';' "
                "WHERE l.collection_id=? AND l.subgroup_id=? AND l.step='S1' AND l.item='word-sense' AND l.deleted=0 AND o.deleted=0", cid, gid)[0]
        case("R19", "RecordWords writes the real answer: every word validated, each observation marked evidence at creation",
             w["validated"] == len(words_all) and not w["failed"] and nat[0] == nat[1] and nat[0] > 0, f"{w['observed']} obs, {w['nodes']} nodes, validated {w['validated']}/{len(words_all)}, evidence {nat[1]}/{nat[0]}")
        bad_nodes = q("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id JOIN collection_layer_item l ON o.stable_key >= 'layer:' || l.id || ':' AND o.stable_key < 'layer:' || l.id || ';' "
                      "WHERE l.collection_id=? AND l.subgroup_id=? AND l.step='S1' AND n.deleted=0 AND o.deleted=0 AND n.traced_observation_id IS NULL "
                      "AND (n.verse_lexical_id IS NULL OR n.verse_reference IS NULL OR n.strong IS NULL OR n.surface IS NULL OR n.collection_id IS NULL OR n.subgroup_id IS NULL OR n.role IS NULL)", cid, gid)[0][0]
        case("R20", "no word node of the subgroup's S1 observations misses a required column", bad_nodes == 0, f"{bad_nodes} incomplete")
        old_open = q("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='S1' AND item='old-observation' AND state='open' AND deleted=0", cid, gid)[0][0]
        case("R21", "every older observation of the step is answered with its word (none left open in the ledger), and the next command named is ReadSenses", old_open == 0 and "ReadSenses" in w["next"],
             f"open {old_open}; {w['next']}")
        m = refused(lambda: rc.read_words(conn, cfg, "TEST-RW", name, gname, out))
        case("R22", "ReadWords on a subgroup whose words are all read and validated is refused, naming the next command", bool(m) and "every word" in (m or ""), m)
        case("R23", "the real answer recorded again is refused (its rows are validated)", bool(refused(lambda: rc.record_words(conn, cfg, "TEST-RW", answer, keep=True))) and counts(conn) == c1, "")
        conn.rollback()
    else:
        for c_ in ("R18", "R19", "R20", "R21", "R22", "R23"):
            case(c_, "needs the real answer", None, "")

    scans = []
    for sql, args in [("SELECT id, morph_code FROM verse_lexical WHERE id IN (?,?)", (1, 2)), ("SELECT id, text FROM verse WHERE id IN (?,?)", (1, 2)),
                      ("SELECT head FROM strong_sense WHERE strong=? AND deleted=0", ("H1897",)),
                      ("SELECT sense_code, sense_text FROM strong_meaning_tree WHERE strong_variant=? AND deleted=0 ORDER BY sort", ("H1897",)),
                      ("SELECT lsj, mounce FROM strong_lexicon WHERE strong=? AND deleted=0", ("H1897",)),
                      ("SELECT related_strong FROM strong_related WHERE strong=? AND deleted=0 LIMIT 12", ("H1897",))]:
        scans += sg.full_scans(conn, cfg, sql, args)
    case("R24", "no lookup of the read scans a large table (query plans)", not scans, scans)

    print("\n| case | what | result | evidence |\n|---|---|---|---|")
    for r_ in results:
        print(f"| {r_[0]} | {r_[1]} | {r_[2]} | {r_[3]} |")
    print(f"\n{sum(1 for r_ in results if r_[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r_[2] != "FAIL" for r_ in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
