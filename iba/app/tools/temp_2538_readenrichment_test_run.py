"""temp_2538_readenrichment_test_run.py -- the test plan of ReadEnrichment / RecordEnrichment (escalation #2538; lib/readcommands.py; B:46).

Runs on a COPY of iba.db, never the live database. The copy must hold the subgroup through 1.1 with 1.2 not yet open: for thought, the named snapshot
iba-20261125T123416Z-pre-2538-findings-apply.db with the #2538 migrations applied (findings, layernext_verb, readwords, senses, enrichment), then
temp_2538_readwords_test_run.py and temp_2538_readsenses_test_run.py run on it for the same subgroup. The default subgroup is "reasoning", the one subgroup of thought with a
1.2 reading recorded live.
The real answer (case E10 on) is the live 1.2 reading of the subgroup (read-only): each live enrichment matched to the copy's sense that holds the same occurrences; the older
observations answered as live answered them.

Usage: python iba/app/tools/temp_2538_readenrichment_test_run.py <db copy> [collection] [subgroup] [other subgroup]
"""
import json
import pathlib
import sqlite3
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



def _whole_words(g: str) -> str:
    """Live grounds as an answer would give them now: a last word cut short when the reading was written (observation 22919: '... the content o') is dropped; the
    grounds check compares whole words since BUILD.md 589."""
    if g and not g.rstrip().endswith((".", ",", ";", ":", ")", "'", '"')) and len(g.split()) > 3:
        last = g.split()[-1]
        if len(last) <= 2:
            return g.rsplit(" ", 1)[0]
    return g

def main(db, name="thought", sub="reasoning", other="meditating and pondering"):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    t_all = time.monotonic()
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    q = lambda s_, *a: conn.execute(s_, a).fetchall()  # noqa: E731
    out = pathlib.Path(tempfile.mkdtemp(prefix="readenrichment-"))
    st = rc.settings(cfg)
    rt, lim = st["enrichment"], st["limits"]
    if not ts.in_loop(conn, cfg, name):      # live is past this step: the copy is put back to it (temp_2538_test_state, BUILD.md 597)
        print(ts.back_to(conn, cfg, name, sub, '1.2'), file=sys.stderr)
    cid, gid, gname = rc._subgroup(conn, name, sub)

    ins = rc.instruction(conn, rt)
    case("E1", "the instruction carries what, read, write, and the text of every rule it keeps, read live from cfg_method_rule",
         len(ins["keep"]) == len(rt["rules"]) and all(k["text"] for k in ins["keep"]) and bool(ins["read"]) and bool(ins["write"]), [k["rule"] for k in ins["keep"]])
    case("E2", "an unknown subgroup is refused", bool(refused(lambda: rc.read_enrichment(conn, cfg, "TEST-RE", name, "no such subgroup", out))), "")
    m = refused(lambda: rc.read_enrichment(conn, cfg, "TEST-RE", name, other, out))
    case("E3", "ReadEnrichment for another subgroup is refused while this one is further through its loop, or that one is not through 1.1", bool(m), m)
    conn.rollback()

    l11 = [x[0] for x in q("SELECT id FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.1' AND item='group-definition' AND deleted=0 AND state!='retired'", cid, gid)]
    senses_db = set()
    for lid in l11:
        senses_db |= {x[0] for x in q("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", f"layer:{lid}:", f"layer:{lid};")}
    before = q("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.2' AND deleted=0 AND item='strong-enrichment' AND state!='retired'", cid, gid)[0][0]
    r = rc.read_enrichment(conn, cfg, "TEST-RE", name, gname, out)
    pkg = json.loads(r["path"].read_text(encoding="utf-8"))
    conn.commit()
    row = rc._word_rows(conn, cid, gid, "1.2", "strong-enrichment")
    case("E4", "ReadEnrichment opens 1.2 for the subgroup (its strong-enrichment row is made) and writes a package", before == 0 and len(row) == 1 and r["path"].exists(),
         f"rows before {before}, after {len(row)}, opened {r['opened']}")
    got = [x["sense"] for x in pkg["senses"]]
    case("E5", "the package carries every 1.1 sense of the subgroup once (equal to the observations of its 1.1 row)", len(got) == len(set(got)) and set(got) == senses_db,
         f"package {len(got)}, 1.1 observations {len(senses_db)}")
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    exp = lr.expected_nodes(L, "strong-enrichment", gid, row[0][5])
    codes_db = {o["strong"] for o, _ in exp if o["strong"]}
    case("E6", "every code of the subgroup has its lexicon (the three sources and related), each source within lexicon_chars",
         set(pkg["codes"]) == codes_db and all(len(c.get(k) or "") <= rt["lexicon_chars"] for c in pkg["codes"].values() for k in ("meaning_range", "lsj", "mounce"))
         and all("lsj" in c and "mounce" in c and "related" in c for c in pkg["codes"].values()), f"{len(pkg['codes'])} codes")
    case("E7", "every occurrence of the subgroup is held by a sense or listed as in no sense",
         {len(exp)} == {sum(len(x["occurrences"]) for x in pkg["senses"]) + len(pkg["occurrences_in_no_sense"])}, f"{len(exp)} occurrences; in no sense {len(pkg['occurrences_in_no_sense'])}")
    stamped = q("SELECT pulled_at FROM collection_layer_item WHERE id=?", row[0][0])[0][0]
    case("E8", "the row is stamped pulled_at; the package is within its size and time limits", bool(stamped) and r["chars"] <= rt["package_max_chars"] and r["seconds"] <= lim["read_max_seconds"],
         f"{r['chars']} chars (limit {rt['package_max_chars']}), {r['seconds']} s")
    shown = {o["observation"] for o in pkg["older"]}
    led = {int(x[0]) for x in q("SELECT subject FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.2' AND item='old-observation' AND state='open' AND deleted=0", cid, gid)}
    case("E9", "every older observation carried open to 1.2 for the subgroup is shown, once, with its text (RW-09)",
         led <= shown and len(pkg["older"]) == len(shown) and all(o["text"] for o in pkg["older"]), f"shown {len(shown)}, open in the ledger at 1.2 {len(led)}")

    # ── the real answer: the live 1.2 reading of the subgroup, each enrichment matched to the copy's sense by the occurrences it holds
    held = {}
    for x in pkg["senses"]:
        held[x["sense"]] = {v for (v,) in q("SELECT verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IS NOT NULL", x["sense"])}
    live = sqlite3.connect(f"file:{LIVE.as_posix()}?mode=ro", uri=True)
    lcid = live.execute("SELECT id FROM collection WHERE name=? AND deleted=0", (name,)).fetchone()[0]
    lgid = live.execute("SELECT id FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND lower(name)=?", (lcid, gname.lower())).fetchone()[0]
    llid = [x[0] for x in live.execute("SELECT id FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.2' AND item='strong-enrichment' AND deleted=0 AND state='observed'", (lcid, lgid))]
    enrich, unmatched = [], 0
    for lid in llid:
        for oid, tag, text, basis, parts in live.execute("SELECT id, tag, obs_text, basis, parts FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};")):
            vls = {x[0] for x in live.execute("SELECT verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IS NOT NULL", (oid,))}
            match = [sid for sid, h in held.items() if h == vls]
            if len(match) != 1:
                unmatched += 1
                continue
            enrich.append({"sense": match[0], "kind": tag, "obs_text": text, "basis": basis, "grounds": _whole_words((json.loads(parts) if parts else {}).get("grounds") or "")})
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
        elif "carried_to" in ch and ch["carried_to"][0] not in ("1.1", "1.2"):
            a = {"observation": o["observation"], "action": "carry", "to": ch["carried_to"][0], "reason": ch["carried_to"][1]}
        else:
            missing.append(o["observation"])
            continue
        old_ans.append(a)
    answer = {"command": "ReadEnrichment", "collection": name, "subgroup": gname, "ledger_id": row[0][0], "enrichments": enrich, "older": old_ans}
    have = bool(enrich) and {e["sense"] for e in enrich} == set(held) and not unmatched and not missing
    case("E10", "a real answer exists: one live enrichment for each sense of the copy, and the live answers to the older observations", have,
         f"{len(enrich)} enrichments for {len(held)} senses, {unmatched} live enrichment(s) unmatched; older answers {len(old_ans)}/{len(pkg['older'])}, missing {missing[:5]}")

    c0 = counts(conn)
    first = enrich[0] if enrich else {}
    bad = [("E11", "an answer whose command is not ReadEnrichment", {**answer, "command": "ReadSenses"}),
           ("E11b", "an answer naming the ledger row of another subgroup or step", {**answer, "ledger_id": -1}),
           ("E11c", "an answer naming a sense that is not a 1.1 sense of the subgroup", {**answer, "enrichments": enrich + [{**first, "sense": -5}]}),
           ("E11d", "an answer enriching one sense twice", {**answer, "enrichments": enrich + [{**first, "obs_text": first.get("obs_text", "") + " (again)"}]}),
           ("E11e", "an answer that leaves a sense without its enrichment", {**answer, "enrichments": enrich[1:]}),
           ("E11f", "an answer whose read grounds are not words of the codes' lexicon", {**answer, "enrichments": [{**first, "basis": "read", "grounds": "zz nothing in any lexicon zz"}] + enrich[1:]}),
           ("E11g", "an answer that leaves the older observations unanswered (RW-13)", {**answer, "older": []} if pkg["older"] else None)]
    for cid_, desc, data in bad:
        if data is None:
            case(cid_, desc + " is refused whole, nothing written", None, "no older observation shown")
            continue
        if not have and cid_ not in ("E11", "E11b"):
            case(cid_, desc + " is refused whole, nothing written", None, "no real answer")
            continue
        m = refused(lambda: rc.record_enrichment(conn, cfg, "TEST-RE", data, keep=True))
        case(cid_, desc + " is refused whole, nothing written", bool(m) and counts(conn) == c0, m or "")
        conn.rollback()

    if have:
        p = rc.record_enrichment(conn, cfg, "TEST-RE", answer, keep=False)
        case("E12", "-Check previews the real answer: everything checked, nothing kept", bool(p.get("preview")) and counts(conn) == c0, p)
        conn.rollback()
        w = rc.record_enrichment(conn, cfg, "TEST-RE", answer, keep=True)
        conn.commit()
        c1 = counts(conn)
        lid = row[0][0]
        obs = q("SELECT id, nature, tag FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", f"layer:{lid}:", f"layer:{lid};")
        case("E13", "RecordEnrichment writes the real answer: the row validated, one enrichment observation for each sense, each marked evidence at creation",
             w["validated"] and len(obs) == len(held) and all(o[1] == "evidence" and o[2] == "enrichment" for o in obs), f"{w}; {len(obs)} observations")
        traced = set()
        for o in obs:
            traced |= {x[0] for x in q("SELECT traced_observation_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NOT NULL", o[0])}
        nodes_codes = {x[0] for x in q(f"SELECT DISTINCT strong FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND observation_id IN ({','.join('?' * len(obs))})", *[o[0] for o in obs])} if obs else set()
        case("E14", "the enrichments trace every sense of the subgroup, and every code of the subgroup has a node", traced >= set(held) and codes_db <= nodes_codes,
             f"traced {len(traced & set(held))} of {len(held)} senses; codes without a node {sorted(codes_db - nodes_codes)[:5]}")
        old_open = q("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.2' AND item='old-observation' AND state='open' AND deleted=0", cid, gid)[0][0]
        case("E15", "no older observation of 1.2 is left open for the subgroup, and the next command named is ReadStructure", old_open == 0 and "ReadStructure" in w["next"], f"open {old_open}; {w['next']}")
        m = refused(lambda: rc.read_enrichment(conn, cfg, "TEST-RE", name, gname, out))
        case("E16", "ReadEnrichment on a subgroup whose enrichment is read and validated is refused, naming the next command", bool(m) and "ReadStructure" in (m or ""), m)
        case("E17", "the real answer recorded again is refused (the row is validated)", bool(refused(lambda: rc.record_enrichment(conn, cfg, "TEST-RE", answer, keep=True))) and counts(conn) == c1, "")
        conn.rollback()
    else:
        for c_ in ("E12", "E13", "E14", "E15", "E16", "E17"):
            case(c_, "needs the real answer", None, "")

    scans = []
    for sql, args in [("SELECT lsj, mounce FROM strong_lexicon WHERE strong=? AND deleted=0", ("G1256",)),
                      ("SELECT related_strong, related_form, related_gloss FROM strong_related WHERE strong=? AND deleted=0 LIMIT 12", ("G1256",)),
                      ("SELECT observation_id, verse_lexical_id FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND observation_id IN (?,?)", (1, 2))]:
        scans += sg.full_scans(conn, cfg, sql, args)
    case("E18", "no lookup of the read scans a large table (query plans)", not scans, scans)
    case("E19", "the whole test ran in under a minute", time.monotonic() - t_all < 60, f"{time.monotonic() - t_all:.1f} s")

    print("\n| case | what | result | evidence |\n|---|---|---|---|")
    for r_ in results:
        print(f"| {r_[0]} | {r_[1]} | {r_[2]} | {r_[3]} |")
    print(f"\n{sum(1 for r_ in results if r_[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r_[2] != "FAIL" for r_ in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
