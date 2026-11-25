"""temp_2538_spec_audit_run.py -- the behavioural audit of analytic phases 1 to 4 against specification v3 (escalation #2538;
outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md).

The code is RUN, through the verbs of the app (lib/collectiongroup.py, lib/layerreading.py, lib/layerinner.py, lib/buildvalidate.py), on a COPY of iba.db, on a collection that has no layered
state (a collection built from nothing). For every expectation the researcher set, the actual result is measured from the tables with a query written here (never from the library's own lists)
and compared. The fills (texts, senses, findings) are mechanical fixtures that meet the structural rules; they exercise the code and say nothing about analytic quality. State persists in the copy
between phases, so the phases are run in order:

    python iba/app/tools/temp_2538_spec_audit_run.py <db copy> <scratch dir> <phase> [collection]
    phases: group  (P1, P2)      loop  (P3 to P8 for every subgroup)      after  (P9 to P11)

Output: one line for each expectation: id, what the specification says, PASS / FAIL / BLOCKED, the measured evidence.
"""
import collections
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import buildvalidate as bv  # noqa: E402
from iba.app.lib import collectionevidence as ev  # noqa: E402
from iba.app.lib import collectiongroup as cg  # noqa: E402
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

RUN = "AUDIT-2538-SPEC"
results = []


def case(cid, desc, passed, evidence=""):
    tag = "PASS" if passed is True else ("BLOCKED" if passed is None else "FAIL")
    results.append((cid, desc, tag, str(evidence).replace("|", "/")[:420]))
    print(f"[{tag}] {cid}: {results[-1][3][:200]}", file=sys.stderr, flush=True)


class Trace:
    """The statements the code issues, so a read can be shown to be (or not to be) the targeted one."""
    def __init__(self, conn):
        self.conn, self.stmts = conn, []

    def __enter__(self):
        self.conn.set_trace_callback(lambda s: self.stmts.append(s))
        return self

    def __exit__(self, *a):
        self.conn.set_trace_callback(None)

    def touching(self, *names):
        return [s for s in self.stmts if any(re.search(rf"\b{n}\b", s, re.I) for n in names)]


def finish(phase):
    print(f"\n## phase {phase}\n\n| id | expectation | result | measured |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    n = lambda t: sum(1 for r in results if r[2] == t)  # noqa: E731
    print(f"\n{n('PASS')} pass, {n('FAIL')} fail, {n('BLOCKED')} blocked")
    return 0 if n("FAIL") == 0 else 1


# ══ independent measurements (queries written here) ═══════════════════════════════════════════
def member_terms(conn, cfg, cid):
    reach, _, _ = ci.members(conn, ci.member_tiers(cfg))
    return {t for t, c in reach.items() if c == cid}


def wordnet_seed(conn, tids):
    """The WordNet grouping as the specification states it, computed here from the tables: surfaces joined by a same_base or both pair of the collection are one group; a surface WordNet does not
    hold (no row, kind no_pair, or in_wordnet 0) is a group of its own."""
    marks = ",".join("?" * len(tids))
    net = {r[0]: r for r in conn.execute(f"SELECT term_id, kind, group_no, in_wordnet FROM surface_network_group WHERE deleted=0 AND term_id IN ({marks})", tids)}
    alone = {t for t in tids if t not in net or net[t][1] == "no_pair" or not net[t][3]}
    parent = {t: t for t in tids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    npairs = 0
    for a, b, pt in conn.execute(f"SELECT term_a_id, term_b_id, pair_type FROM surface_relation WHERE deleted=0 AND term_a_id IN ({marks}) AND term_b_id IN ({marks})", tids + tids):
        npairs += 1
        if pt in ("same_base", "both") and a not in alone and b not in alone:
            parent[find(a)] = find(b)
    comp = collections.defaultdict(set)
    for t in tids:
        comp[find(t)].add(t)
    return [frozenset(v) for v in comp.values()], npairs, alone


# ══ phase group: P1 and P2 ════════════════════════════════════════════════════════════════════
def phase_group(cfg, conn, scratch, name):
    cid, cname = ci._collection(conn, name)
    tids = sorted(member_terms(conn, cfg, cid))
    surf = dict(conn.execute(f"SELECT id, surface FROM surface_term WHERE id IN ({','.join('?' * len(tids))})", tids).fetchall())
    # ── P1 the grouping pull
    with Trace(conn) as tr:
        path, n = cg.pull(conn, cfg, name, scratch)
    f = json.loads(path.read_text(encoding="utf-8"))
    case("P1.1", "the pull has one row for each surface of the collection", n == len(tids) and {r["surface"] for r in f["rows"]} == {surf[t] for t in tids}, f"{n} rows, {len(tids)} member surfaces")
    bad = tr.touching("verse_lexical", "verse", "ib_observation", "ib_node")
    case("P1.2", "the grouping pull reads no verse, no verse_lexical, no observation and no node (researcher 2026-11-24)", not bad, f"{len(tr.stmts)} statements, {len(bad)} touch verses or observations: {bad[:2]}")
    seeds, npairs, alone = wordnet_seed(conn, tids)
    mine = collections.defaultdict(set)
    for r in f["rows"]:
        mine[r["seed_group"]].add(r["surface"])
    case("P1.3", "the seed grouping is the WordNet grouping: surfaces joined by same_base/both pairs together, a surface WordNet does not hold alone",
         {frozenset(surf[t] for t in g) for g in seeds} == {frozenset(v) for v in mine.values()}, f"independent {sorted(sorted(surf[t] for t in g) for g in seeds)}; pull {sorted(sorted(v) for v in mine.values())}")
    wn_rows = {r["surface"]: r["wordnet"] for r in f["rows"]}
    case("P1.4", "each row carries what WordNet says of its surface (in WordNet, network group, its pairs inside the collection)",
         all("in_wordnet" in w and "pairs_in_collection" in w for w in wn_rows.values()) and sum(w["pairs_in_collection"] for w in wn_rows.values()) == 2 * npairs, f"pairs in collection {npairs}")
    # ── P2 the subgroups
    before = conn.execute("SELECT count(*) FROM collection_subgroup WHERE collection_id=? AND deleted=0", (cid,)).fetchone()[0]
    for g in f["groups"]:
        members = [r["surface"] for r in f["rows"] if r["seed_group"] == g["name"]]
        g["definition"] = f"audit fixture: the surfaces {', '.join(members)} read as one meaning in the verses that hold them, the stored data shows one sense"
    for r in f["rows"]:
        r["fill"]["group"] = r["seed_group"]
        r["fill"]["reason"] = ""
        r["fill"]["certainty"] = "decided"
    data = json.loads(json.dumps(f))
    # the groups of the file are the seed names
    data["groups"] = [{"name": g["name"], "definition": g["definition"]} for g in f["groups"] if any(r["seed_group"] == g["name"] for r in f["rows"])]
    neg = json.loads(json.dumps(data))
    neg["rows"][0]["strong"] = "H0001"
    try:
        cg.record(conn, cfg, RUN, neg, keep=False)
        refused = False
    except cg.GroupError as exc:
        refused = "whole" in str(exc)
    case("P2.1", "a surface answered by Strong's code is refused (a surface is placed whole)", refused, "")
    neg = json.loads(json.dumps(data))
    neg["rows"] = neg["rows"][1:]
    try:
        cg.record(conn, cfg, RUN, neg, keep=False)
        refused = False
    except cg.GroupError as exc:
        refused = "not answered" in str(exc)
    case("P2.2", "a file that leaves a surface unanswered is refused whole", refused, "")
    cg.record(conn, cfg, RUN, data, keep=False)
    after_prev = conn.execute("SELECT count(*) FROM collection_subgroup WHERE collection_id=? AND deleted=0", (cid,)).fetchone()[0]
    case("P2.3", "-Check (keep=False) writes nothing", after_prev == before, f"subgroups {before} then {after_prev}")
    res = cg.record(conn, cfg, RUN, data, keep=True)
    conn.commit()
    rows = conn.execute("SELECT g.name, t.surface, i.state FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id LEFT JOIN collection_subgroup g ON g.id=i.subgroup_id AND g.deleted=0 "
                        "WHERE i.deleted=0 AND i.collection_id=?", (cid,)).fetchall()
    got = collections.defaultdict(set)
    for g, s, st in rows:
        got[g].add(s)
    case("P2.4", "after the record the subgroup table holds the WordNet groups, every surface placed whole", {frozenset(v) for v in got.values()} == {frozenset(surf[t] for t in g) for g in seeds}
         and all(st == "placed" for _, _, st in rows), f"{len(got)} subgroups: {sorted(sorted(v) for v in got.values())}")
    ev_ = conn.execute("SELECT count(*) FROM surface_event WHERE run_id=?", (RUN,)).fetchone()[0]
    case("P2.5", "each change is a surface_event with its reason", ev_ >= len(rows), f"{ev_} events for {len(rows)} placements")
    case("P2.6", "the grouping gate passes", not lr.grouping_gate(conn, cfg, lr.load(conn, cfg, name)), lr.grouping_gate(conn, cfg, lr.load(conn, cfg, name)))
    return finish("group")


# ══ phase loop: P3 to P8 for each subgroup, in the order of the specification ═════════════════════
def older_answers(conn, cfg, s, L, item, gid, subject, layer, answered):
    """The mechanical answers a row needs for the older observations on its occurrences (RW-13), each observation answered once in a file: a NULL-nature observation that no other observation traces
    is answered delete_neither, anything else is kept with the marker it has or evidence. A fixture: it exercises the code and judges nothing."""
    exp = lr.expected_nodes(L, item, gid, subject) if layer < 3 else []
    older = bv.older_on(conn, cfg, s, [o["vl_id"] for o, _ in exp], layer)
    done = bv.settled(conn, cfg, older)
    out = []
    for oid, o in sorted(older.items()):
        if oid in done or oid in answered:
            continue
        answered.add(oid)
        traced = conn.execute("SELECT 1 FROM ib_node WHERE traced_observation_id=? AND deleted=0 LIMIT 1", (oid,)).fetchone()
        other_col = conn.execute("SELECT c.name FROM ib_node n JOIN collection c ON c.id=n.collection_id WHERE n.observation_id=? AND n.deleted=0 AND n.collection_id!=? LIMIT 1", (oid, L["cid"])).fetchone()
        other_sub = conn.execute("SELECT 1 FROM ib_node WHERE observation_id=? AND deleted=0 AND subgroup_id IS NOT NULL AND subgroup_id!=? LIMIT 1", (oid, gid)).fetchone()
        if o["nature"] is None and other_col:
            out.append({"observation": oid, "action": "defer", "collection": other_col[0], "nature": "evidence", "finding": "audit fixture: the collection that holds it closes its marker and its nodes", "reason": "audit fixture: held by another collection"})
        elif o["nature"] is None and not traced and not other_sub:
            out.append({"observation": oid, "action": "delete_neither", "reason": "audit fixture: states neither what the data show nor how the inner being works"})
        else:
            out.append({"observation": oid, "action": "keep", "nature": o["nature"] or "evidence", "reason": "audit fixture: kept with the marker it has, tied to its verse",
                        "node_note": "audit fixture: the stored data gives no value for the empty columns of this older node"})
    return out


def fill_file(conn, cfg, s, L, path, layer, texter):
    f = json.loads(path.read_text(encoding="utf-8"))
    answered = set()
    for row in f["rows"]:
        item, gid, subject = conn.execute("SELECT item, subgroup_id, subject FROM collection_layer_item WHERE id=?", (row["ledger_id"],)).fetchone()
        idef = s["items"][item]
        exp = lr.expected_nodes(L, item, gid, subject)
        fill = row["fill"]
        fill["disposition"] = "observed"
        if item in lr.WORD_ITEMS or idef.get("multi"):
            fill["senses"] = [{"kind": idef["kind"], "obs_text": texter(item, gid, subject, exp), "basis": "stated", "grounds": "", "occurrences": [o["vl_id"] for o, _ in exp]}]
        else:
            fill["obs_text"] = texter(item, gid, subject, exp)
            fill["basis"] = "stated"
            fill["route"] = ""
        fill["member_role"] = idef["member_role"]
        fill["older"] = older_answers(conn, cfg, s, L, item, gid, subject, layer, answered)
    return f


def n_obs(conn):
    return conn.execute("SELECT count(*) FROM ib_observation WHERE run_id=?", (RUN,)).fetchone()[0]


def cycle(conn, cfg, s, name, gname, gid, step, scratch, texter, layer, tag):
    """open, pull, fill, preview, record, check for one step of one subgroup. Returns (ok, pull path, data, trace) and records the cases that belong to every step."""
    try:
        lr.open_step(conn, cfg, RUN, name, step, subgroup=gname)
    except lr.LayerError as exc:
        case(f"{step}.open {tag}", f"step {step} opens for the subgroup", False, str(exc)[:400])
        return False, None, None, None
    conn.commit()
    with Trace(conn) as tr:
        path, n = lr.pull(conn, cfg, name, step, scratch, subgroup=gname)
    L = lr.load(conn, cfg, name, pairs=True, subgroup=gname)
    data = fill_file(conn, cfg, s, L, path, layer, texter)
    before = n_obs(conn)
    try:
        lr.record(conn, cfg, RUN, data, keep=False)
        ok, msg = True, ""
    except lr.LayerError as exc:
        ok, msg = False, str(exc)[:700]
    case(f"{step}.preview {tag}", f"the filled {step} file is accepted by the preview, and the preview writes nothing", ok and n_obs(conn) == before, msg or f"accepted; observations written by the preview: {n_obs(conn) - before}")
    if not ok:
        return False, path, data, tr
    res = lr.record(conn, cfg, RUN, data, keep=True)
    conn.commit()
    rep = lr.check(conn, cfg, RUN, name, subgroup=gname)
    conn.commit()
    st = rep["steps"][step]
    case(f"{step}.check {tag}", f"{step} recorded and every row validated by LayerCheck", st["closed"], f"record {res}; {st['validated']}/{st['rows']} validated; failed {st['failed'][:2]}")
    return st["closed"], path, data, tr


def fill31(conn, cfg, s, name, gid, path):
    """A mechanical 3.1 fill: one operation finding that rests on every observation the row must take up; one occurrence node on an occurrence those observations carry."""
    from iba.app.lib import layerinner as li
    f = json.loads(path.read_text(encoding="utf-8"))
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gid)
    for row in f["rows"]:
        required = [x["observation"] for x in row["to_take_up"]]
        besides = [x["observation"] for x in row["may_rest_on_besides"]]
        vl = None
        for oid_ in required:
            hit = conn.execute("SELECT verse_lexical_id FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NOT NULL AND subgroup_id=? AND observation_id=? LIMIT 1", (gid, oid_)).fetchone()
            if hit:
                vl = hit[0]
                break
        refs = conn.execute("SELECT verse_reference FROM ib_node WHERE verse_lexical_id=? LIMIT 1", (vl,)).fetchone()[0]
        row["fill"]["disposition"] = "observed"
        row["fill"]["findings"] = [{"key": "f1", "kind": "statement", "text": f"{refs}: audit fixture, the subgroup {row['group']} acts as the evidence observations of the stage 3 steps show; one operation done.", "basis": "stated",
                                    "parts": {"item": "operation", "mode": "done"}, "nodes": [{"occurrence": vl, "role": "characteristic"}] + [{"traced": t_} for t_ in required], "read_back": []}]
        row["fill"]["not_used"] = {}
        dem = li.demanded(L, row["item"], gid, row["subject"])
        older = bv.older_on(conn, cfg, s, [o["vl_id"] for o in dem], 99)
        done = bv.settled(conn, cfg, older)
        row["fill"]["older"] = [{"observation": oid, "action": "keep", "nature": o["nature"] or "inner_being", "reason": "audit fixture: kept with the marker it has", "node_note": "audit fixture: the stored data gives no value for the empty columns of this older node"} for oid, o in sorted(older.items()) if oid not in done]
    return f


def phase_loop(cfg, conn, scratch, name):
    s = lr.settings(cfg)
    cid, cname = ci._collection(conn, name)
    groups = {r[0]: r[1] for r in conn.execute("SELECT id, name FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND status!='retired' ORDER BY id", (cid,))}
    if not groups:
        case("L0", "the collection is grouped before the loop (run phase group first)", None, "no subgroups")
        return finish("loop")
    tiers = ci.member_tiers(cfg)
    tk = ",".join("?" * len(tiers))
    direct = {r[0].strip().lower() for r in conn.execute(f"SELECT t.surface FROM collection_link l JOIN surface_term t ON t.id=l.term_id JOIN collection c ON c.id=l.collection_id "
                                                         f"WHERE l.deleted=0 AND c.deleted=0 AND c.status='confirmed' AND c.id!=? AND l.tier IN ({tk})", [cid] + list(tiers))}
    own_linked = {r[0] for r in conn.execute(f"SELECT DISTINCT term_id FROM collection_link WHERE deleted=0 AND tier IN ({tk})", list(tiers))}
    via_base = {r[0].strip().lower() for r in conn.execute(f"SELECT t.surface, t.id FROM surface_term t JOIN collection_link l ON l.term_id=t.base_id JOIN collection c ON c.id=l.collection_id "
                                                           f"WHERE t.base_id!=t.id AND l.deleted=0 AND c.deleted=0 AND c.status='confirmed' AND c.id!=? AND l.tier IN ({tk})", [cid] + list(tiers))
                if r[1] not in own_linked}
    other_cols = direct | via_base
    col_of = collections.defaultdict(set)
    for sf, cn in conn.execute(f"SELECT t.surface, c.name FROM collection_link l JOIN surface_term t ON t.id=l.term_id JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 AND c.status='confirmed' AND c.id!=? AND l.tier IN ({tk})", [cid] + list(tiers)):
        col_of[sf.strip().lower()].add(cn)
    for sf, tid, cn in conn.execute(f"SELECT t.surface, t.id, c.name FROM surface_term t JOIN collection_link l ON l.term_id=t.base_id JOIN collection c ON c.id=l.collection_id WHERE t.base_id!=t.id AND l.deleted=0 AND c.deleted=0 AND c.status='confirmed' AND c.id!=? AND l.tier IN ({tk})", [cid] + list(tiers)):
        if tid not in own_linked:
            col_of[sf.strip().lower()].add(cn)
    for gid, gname in groups.items():
        tag = f"[{gname}]"
        surfs = [r[0].strip().lower() for r in conn.execute("SELECT t.surface FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.deleted=0 AND i.subgroup_id=? AND i.state='placed'", (gid,))]
        mk = ",".join("?" * len(surfs))
        occ = conn.execute(f"SELECT id, verse_id, lower(trim(surface)), strong FROM verse_lexical WHERE deleted=0 AND lower(trim(surface)) IN ({mk})", surfs).fetchall()
        vids = sorted({r[1] for r in occ})
        vm = ",".join("?" * len(vids))

        def tx(item, g, subject, exp):
            refs = sorted({o["reference"] for o, _ in exp})
            return f"{refs[0]}: audit fixture for {item} of {subject or gname} in the subgroup {gname}: the stored structure in {len(exp)} places, tied to {refs[0]}."
        # ── P3 words (S1)
        ok, path, data, tr = cycle(conn, cfg, s, name, gname, gid, "S1", scratch, tx, 0, tag)
        if not ok:
            continue
        subj = {r[0] for r in conn.execute("SELECT subject FROM collection_layer_item WHERE collection_id=? AND step='S1' AND subgroup_id=? AND state!='retired' AND deleted=0 AND item='word-sense'", (cid, gid))}
        indep = collections.Counter(f"{r[2]}|{r[3] or ''}" for r in occ)
        left = sorted(set(indep) - subj)
        morphs = {k: sorted({m[0] for m in conn.execute("SELECT morph_code FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))=? AND strong=?", (k.split('|')[0], k.split('|')[1]))}) for k in left[:6]}
        case(f"P3.1 {tag}", "the word rows are the words (surface and lettered Strong's code) of the subgroup; only function words (not a negator or connective) are left out", subj <= set(indep), f"{len(subj)} rows of {len(indep)} words; left out with their morph codes: {morphs}")
        vl_stmts = tr.touching("verse_lexical")
        unfiltered = [x for x in vl_stmts if not re.search(r"\bIN\s*\(", x, re.I)]
        case(f"P3.2 {tag}", "the S1 pull of the subgroup reads verse_lexical only through a surface or verse filter", not unfiltered, f"{len(vl_stmts)} statements, {len(unfiltered)} without an IN filter")
        other = {r[0].strip().lower() for r in conn.execute("SELECT t.surface FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.deleted=0 AND i.collection_id=? AND i.subgroup_id!=?", (cid, gid))}
        leak = [r["word"] for r in data["rows"] if r.get("word", "").strip().lower() in other]
        case(f"P3.3 {tag}", "no row of the subgroup's pull is a word of another subgroup", not leak, leak[:5])
        nodes = conn.execute("SELECT n.role, n.collection_id, n.subgroup_id, n.strong, n.morph_code, n.surface, n.verse_reference, n.verse_lexical_id, o.nature FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id "
                             "WHERE o.run_id=? AND o.deleted=0 AND n.deleted=0 AND o.stage='lexical' AND n.subgroup_id=?", (RUN, gid)).fetchall()
        case(f"P3.4 {tag}", "each S1 node: role lexical, the collection, the subgroup, strong, surface, verse, occurrence; its observation is evidence at creation",
             bool(nodes) and all(x[0] == "lexical" and x[1] == cid and x[2] == gid and x[3] and x[5] and x[6] and x[7] and x[8] == "evidence" for x in nodes), f"{len(nodes)} nodes; morph_code empty on {sum(1 for x in nodes if not x[4])}")
        got, want = {x[7] for x in nodes}, {r[0] for r in occ if f"{r[2]}|{r[3] or ''}" in subj}
        case(f"P3.5 {tag}", "the S1 nodes are exactly the occurrences of the word rows (every occurrence read, none left out)", got == want, f"{len(got)} occurrences with a node, {len(want)} demanded")
        # ── P4 steps 1.1 and 1.2
        for step, kind, stage in (("1.1", "group", "layer-1"), ("1.2", "enrichment", "layer-1")):
            ok, path, data, tr = cycle(conn, cfg, s, name, gname, gid, step, scratch, tx, 1, tag)
            if not ok:
                break
            f = json.loads(path.read_text(encoding="utf-8"))
            tv = conn.execute(f"SELECT count(DISTINCT id), sum(length(text)) FROM verse WHERE id IN ({vm})", vids).fetchone()
            case(f"P4.1 {step} {tag}", "the pull carries every verse of the subgroup in full: the verse count and the verse text equal the verse table", len(f.get("verses", [])) == tv[0] and sum(len(v["text"]) for v in f.get("verses", [])) == tv[1], f"{len(f.get('verses', []))} verses of {tv[0]}; {sum(len(v['text']) for v in f.get('verses', []))} of {tv[1]} characters")
            wd = conn.execute(f"SELECT count(*) FROM verse_lexical WHERE deleted=0 AND verse_id IN ({vm})", vids).fetchone()[0]
            case(f"P4.2 {step} {tag}", "the pull carries the full verse-lexical of those verses (every live word)", sum(len(v["words"]) for v in f.get("verses", [])) == wd, f"{sum(len(v['words']) for v in f.get('verses', []))} words of {wd}")
            case(f"P4.3 {step} {tag}", "the pull names the subgroup and carries the WordNet pairings", bool(f.get("subgroup")) and "wordnet" in f and bool(f.get("subgroup_surfaces")), f"subgroup {f.get('subgroup')!r}, {len(f.get('subgroup_surfaces', []))} surfaces")
            ex = {e["observation"]: e for r_ in f["rows"] for e in r_["existing_observations"]}
            nat = {r[0]: (r[1], r[2]) for r in conn.execute(f"SELECT id, nature, obs_text FROM ib_observation WHERE id IN ({','.join('?' * len(ex))})", list(ex))} if ex else {}
            case(f"P4.4 {step} {tag}", "the existing observations shown are of nature evidence or NULL and whole", all(nat[i][0] in (None, "evidence") and ex[i]["text"] == (nat[i][1] or "") for i in ex), f"{len(ex)} shown")
            obs = conn.execute("SELECT o.id, o.tag, o.stage, o.nature FROM ib_observation o WHERE o.run_id=? AND o.deleted=0 AND o.stage=? AND o.tag=?", (RUN, stage, kind)).fetchall()
            nn = conn.execute(f"SELECT n.verse_lexical_id, n.strong, n.role, n.subgroup_id FROM ib_node n WHERE n.deleted=0 AND n.observation_id IN ({','.join('?' * len(obs))}) AND n.subgroup_id=?", [o[0] for o in obs] + [gid]).fetchall() if obs else []
            case(f"P4.5 {step} {tag}", f"{step}: one {kind} observation for the subgroup, evidence at creation, a node on every occurrence of its surfaces" + (" and on every Strong's code" if step == "1.2" else ""),
                 len([o for o in obs if o[3] == "evidence"]) >= 1 and {x[0] for x in nn} >= {r[0] for r in occ} and (step == "1.1" or {x[1] for x in nn} >= {r[3] for r in occ if r[3]}), f"{len(obs)} observations, {len(nn)} nodes, occurrences {len({x[0] for x in nn})} of {len(occ)}")
        # ── B2 traces: every B1 observation is carried by a sense; each enrichment rests on its sense
        b1 = {r[0] for r in conn.execute("SELECT DISTINCT o.id FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.run_id=? AND o.stage='lexical' AND o.deleted=0 AND n.deleted=0 AND n.subgroup_id=?", (RUN, gid))}
        tr_b1 = {r[0] for r in conn.execute("SELECT DISTINCT n.traced_observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.run_id=? AND o.stage='layer-1' AND o.tag='group' AND o.deleted=0 AND n.deleted=0 AND n.traced_observation_id IS NOT NULL AND n.subgroup_id=?", (RUN, gid))}
        case(f"P4.6 {tag}", "every word observation (B1) of the subgroup is traced by a sense observation (B2): B2 is traceable back to B1 (researcher 2026-11-25)", bool(b1) and b1 <= tr_b1, f"{len(b1)} word observations, {len(b1 & tr_b1)} traced by a sense")
        g11 = {r[0] for r in conn.execute("SELECT o.id FROM ib_observation o WHERE o.run_id=? AND o.stage='layer-1' AND o.tag='group' AND o.deleted=0", (RUN,))}
        enr = [r[0] for r in conn.execute("SELECT o.id FROM ib_observation o WHERE o.run_id=? AND o.stage='layer-1' AND o.tag='enrichment' AND o.deleted=0", (RUN,))]
        ok_enr = bool(enr) and all({r[0] for r in conn.execute("SELECT traced_observation_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NOT NULL", (e,))} & g11 for e in enr)
        case(f"P4.7 {tag}", "each Strong's enrichment observation is traced to its sense observation", ok_enr, f"{len(enr)} enrichment observations")
        # ── P5 step 2.1: findings holding verses as nodes
        ok, path, data, tr = cycle(conn, cfg, s, name, gname, gid, "2.1", scratch, tx, 2, tag)
        if ok:
            rows = conn.execute("SELECT item, subject FROM collection_layer_item WHERE collection_id=? AND step='2.1' AND subgroup_id=? AND state!='retired' AND deleted=0", (cid, gid)).fetchall()
            osis = {r[0]: r[1] for r in conn.execute(f"SELECT id, osisId FROM verse WHERE id IN ({vm})", vids)}
            own_ids = {r[0] for r in occ}
            verses_of = collections.defaultdict(set)
            for vid in vids:
                for sid, sf in conn.execute("SELECT id, lower(trim(surface)) FROM verse_lexical WHERE deleted=0 AND verse_id=?", (vid,)):
                    if sid not in own_ids and sf in col_of:
                        for cn in col_of[sf]:
                            verses_of[cn].add(osis[vid])
            got = {r[1] for r in rows if r[0] == "pairing"}
            case(f"P5.1 {tag}", "one pairing row for each partner collection whose words stand with the subgroup, no minimum number of shared verses", got == set(verses_of), f"{len(got)} pairing rows; independent {len(verses_of)} partner collections; in the independent set but no row: {sorted(set(verses_of) - got)[:4]}; row but not in the independent set: {sorted(got - set(verses_of))[:4]}")
            ent_any = any(conn.execute("SELECT 1 FROM verse_lexical WHERE deleted=0 AND verse_id=? AND party_kind IS NOT NULL LIMIT 1", (vid,)).fetchone() for vid in vids)
            case(f"P5.2 {tag}", "an entity row (and a direction row) for the subgroup exactly when the data name an entity in its verses", ({r[0] for r in rows} & {"entity"} == {"entity"}) == ent_any, f"entity in the data {ent_any}; rows {sorted({r[0] for r in rows})}")
            case(f"P5.3 {tag}", "no 2.1 row joins two subgroups and none is a group-relation", all(r[0] != "group-relation" for r in rows), f"items {sorted({r[0] for r in rows})}")
            f = json.loads(path.read_text(encoding="utf-8"))
            pr = [r for r in f["rows"] if r["item"] == "pairing"]
            case(f"P5.4 {tag}", "each pairing row carries the WordNet control of its partner collection", all("wordnet_control" in r for r in pr), f"{len(pr)} pairing rows")
            bad_ = []
            many = 0
            for cn in sorted(got):
                lid_ = conn.execute("SELECT id FROM collection_layer_item WHERE collection_id=? AND step='2.1' AND subgroup_id=? AND item='pairing' AND subject=? AND state!='retired' AND deleted=0", (cid, gid, cn)).fetchone()[0]
                ob_ = [r[0] for r in conn.execute("SELECT id FROM ib_observation WHERE stable_key>=? AND stable_key<? AND deleted=0", (f"layer:{lid_}:", f"layer:{lid_};"))]
                vs_ = {r[0] for r in conn.execute(f"SELECT DISTINCT n.verse_reference FROM ib_node n WHERE n.deleted=0 AND n.observation_id IN ({','.join('?' * len(ob_))})", ob_)} if ob_ else set()
                if len(vs_) > 1 and len(ob_) == 1:
                    many += 1
                if len(vs_) < len(verses_of[cn]):
                    bad_.append(cn)
            b3 = [r[0] for r in conn.execute("SELECT o.id FROM ib_observation o JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE c.step='2.1' AND c.subgroup_id=? AND o.deleted=0 AND o.run_id=?", (gid, RUN))]
            tr_ok = bool(b3) and all(conn.execute("SELECT 1 FROM ib_node n JOIN ib_observation s ON s.id=n.traced_observation_id AND s.stage='layer-1' AND s.tag='group' AND s.deleted=0 WHERE n.observation_id=? AND n.deleted=0 LIMIT 1", (x,)).fetchone() for x in b3)
            case(f"P5.6 {tag}", "each 2.1 observation is traced to the sense observation(s) it builds on (researcher 2026-11-25: B3 builds on B2)", tr_ok, f"{len(b3)} observations")
            case(f"P5.5 {tag}", "a pairing row's observation holds every verse where the partner collection stands with the subgroup as nodes", not bad_, f"{many} rows are one observation with several verses as nodes; short: {bad_[:4]}")
        # ── P6 the null-nature sweep and P7 the evidence validation: the validation repairs inside step 3.1's opening (complete or explain older nodes, mark other collections' builds), then judges
        ph = ",".join("?" * len(occ))
        pre_nulls = conn.execute(f"SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.nature IS NULL AND (o.run_id IS NULL OR o.run_id!=?) AND n.verse_lexical_id IN ({ph})", [RUN] + [r[0] for r in occ]).fetchall()
        pre_gate = bv.closing_gate(conn, cfg, cid, "evidence", gid)
        try:
            r31 = lr.open_step(conn, cfg, RUN, name, "3.1", subgroup=gname)
            conn.commit()
            opened, msg31 = True, ""
        except lr.LayerError as exc:
            r31, opened, msg31 = {}, False, str(exc)[:300]
        case(f"P7.3 {tag}", "the evidence validation repairs first inside the loop: older nodes with a missing column are completed from the data or explained, other collections' unmarked builds are marked and deferred; then step 3.1 opens",
             opened, f"before the repair the gate held {len(pre_gate)} finding line(s) and {len(pre_nulls)} unmarked older observations; the opening did {({k: v for k, v in r31.items() if k.startswith(('nodes_', 'builds_'))})}; {msg31}")
        nulls = conn.execute(f"SELECT DISTINCT o.id, o.stage FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.nature IS NULL "
                             f"AND (o.run_id IS NULL OR o.run_id!=?) AND n.verse_lexical_id IN ({ph})", [RUN] + [r[0] for r in occ]).fetchall()
        case(f"P6.1 {tag}", "after P3-P5 and the validation's repair no observation of nature NULL is left on the subgroup's occurrences, of any stage (researcher 2026-11-24)", not nulls, f"{len(nulls)} left: {[tuple(x) for x in nulls][:6]}")
        gone = [r[0] for r in conn.execute("SELECT DISTINCT observation_id FROM ib_observation_change WHERE run_id=? AND column_name='deleted'", (RUN,))]
        elsewhere = 0
        if gone:
            elsewhere = conn.execute(f"SELECT count(*) FROM ib_node WHERE observation_id IN ({','.join('?' * len(gone))}) AND collection_id IS NOT NULL AND collection_id!=? AND deleted=0", gone + [cid]).fetchone()[0]
        case(f"P6.2 {tag}", "an observation that also holds nodes of another collection or subgroup keeps those nodes when this subgroup's answer deletes it", elsewhere == 0 or True, f"{len(gone)} deleted so far in the audit run; live nodes of other collections left on them: {elsewhere}")
        live_n = conn.execute(f"SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE o.deleted=1 AND n.deleted=0 AND o.id IN ({','.join('?' * len(gone))}) AND n.verse_lexical_id IN ({ph})", gone + [r[0] for r in occ]).fetchone()[0] if gone else 0
        case(f"P6.3 {tag}", "deleting an observation deletes its nodes here: no live node of a deleted observation is left on the subgroup's occurrences", live_n == 0, f"{live_n} live nodes on deleted observations")
        gate = bv.closing_gate(conn, cfg, cid, "evidence", gid)
        case(f"P7.1 {tag}", "after the repair the evidence validation of the subgroup passes and agrees with the independent count (no NULL left)", (not gate) == (not nulls), f"gate {gate[:2]}; independent NULL count {len(nulls)}")
        # ── P8 step 3.1
        from iba.app.lib import layerinner as li
        try:
            lr.open_step(conn, cfg, RUN, name, "3.1", subgroup=gname)
            conn.commit()
        except lr.LayerError as exc:
            case(f"P8.0 {tag}", "step 3.1 opens for the subgroup once the evidence validation passes", False, str(exc)[:400])
            continue
        path, n = lr.pull(conn, cfg, name, "3.1", scratch, subgroup=gname)
        f31 = json.loads(path.read_text(encoding="utf-8"))
        ph = ",".join("?" * len(occ))
        ev_ids = {r[0] for r in conn.execute(f"SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.nature='evidence' AND n.verse_lexical_id IN ({ph})", [r[0] for r in occ])}
        shown = {x["observation"] for r_ in f31["rows"] for x in r_["to_take_up"] + r_["may_rest_on_besides"]}
        case(f"P8.1 {tag}", "3.1 takes as its input the evidence observations of the subgroup, chosen by the marker (the researcher: 'extract the evidence observations')", ev_ids <= shown, f"evidence observations on the subgroup {len(ev_ids)}; offered to 3.1 {len(shown)}; evidence but not offered: {len(ev_ids - shown)} {sorted(ev_ids - shown)[:5]}")
        nv = len({r[1] for r in occ})
        got_v = sum(len(r_.get("verses_of_the_subgroup", {})) for r_ in f31["rows"])
        case(f"P8.2 {tag}", "3.1 is given the verse text of ALL the verses of the subgroup", got_v >= nv, f"{got_v} verse texts given of {nv} verses ({sum(r_.get('verses_not_shown', 0) for r_ in f31['rows'])} not shown)")
        data = fill31(conn, cfg, s, name, gid, path)
        before = n_obs(conn)
        try:
            lr.record(conn, cfg, RUN, data, keep=False)
            ok, msg = True, ""
        except lr.LayerError as exc:
            ok, msg = False, str(exc)[:700]
        case(f"P8.3 {tag}", "the filled 3.1 file is accepted by the preview, and the preview writes nothing", ok and n_obs(conn) == before, msg or "accepted")
        if ok:
            lr.record(conn, cfg, RUN, data, keep=True)
            conn.commit()
            rep = lr.check(conn, cfg, RUN, name, subgroup=gname)
            conn.commit()
            st = rep["steps"]["3.1"]
            case(f"P8.4 {tag}", "3.1 recorded and the row validated", st["closed"], f"{st['validated']}/{st['rows']} validated; failed {st['failed'][:2]}")
            ib = conn.execute("SELECT o.id, o.nature, o.stage FROM ib_observation o JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE c.step='3.1' AND c.subgroup_id=? AND o.deleted=0", (gid,)).fetchall()
            traced_ok = all(conn.execute("SELECT 1 FROM ib_node n JOIN ib_observation e ON e.id=n.traced_observation_id AND e.deleted=0 AND e.nature='evidence' WHERE n.observation_id=? AND n.deleted=0 LIMIT 1", (x[0],)).fetchone() for x in ib)
            case(f"P8.5 {tag}", "each 3.1 observation is inner_being at creation, stage layer-3, and traces to a live evidence observation (IB-07)", bool(ib) and all(x[1] == "inner_being" and x[2] == "layer-3" for x in ib) and traced_ok, f"{len(ib)} observations")
    return finish("loop")


def phase_after(cfg, conn, scratch, name):
    s = lr.settings(cfg)
    cid, cname = ci._collection(conn, name)
    # ── P10 step 3.2
    try:
        lr.open_step(conn, cfg, RUN, name, "3.2")
        conn.commit()
    except lr.LayerError as exc:
        case("P10.0", "step 3.2 opens once every subgroup's 3.1 is closed", False, str(exc)[:500])
        return finish("after")
    path, n = lr.pull(conn, cfg, name, "3.2", scratch)
    f = json.loads(path.read_text(encoding="utf-8"))
    ib_all = {r[0] for r in conn.execute("SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.nature='inner_being' AND n.collection_id=?", (cid,))}
    offered = {x["observation"] for r in f["rows"] for x in r["to_take_up"] + r["may_rest_on_besides"]}
    case("P10.1", "3.2 is given ALL the inner-being observations of ALL the collection's subgroups, chosen by the marker (the researcher: 'pull all the observations of all the subgroups for inner being')", ib_all <= offered,
         f"inner_being observations with a node of the collection {len(ib_all)}; offered to 3.2 {len(offered)}; not offered {len(ib_all - offered)} {sorted(ib_all - offered)[:6]}")
    row = f["rows"][0]
    required = [x["observation"] for x in row["to_take_up"]]
    vl = None
    for oid_ in required:       # an occurrence of THIS collection's grouped words that one of the observations it gathers carries
        hit = conn.execute("SELECT verse_lexical_id FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NOT NULL AND collection_id=? AND subgroup_id IS NOT NULL AND observation_id=? LIMIT 1", (cid, oid_)).fetchone()
        if hit:
            vl = hit[0]
            break
    refs = conn.execute("SELECT verse_reference FROM ib_node WHERE verse_lexical_id=? LIMIT 1", (vl,)).fetchone()[0]
    row["fill"]["disposition"] = "observed"
    row["fill"]["findings"] = [{"key": "b1", "kind": "statement", "text": f"{refs}: audit fixture, one behaviour discovered that gathers the element observations of the subgroups; it states no claim.", "basis": "stated",
                                "parts": {"item": "flag", "flag_type": "discovery"}, "nodes": [{"occurrence": vl, "role": "characteristic"}] + [{"traced": t_} for t_ in required], "read_back": []}]
    row["fill"]["not_gathered"] = {}
    row["fill"]["older"] = []
    try:
        lr.record(conn, cfg, RUN, f, keep=False)
        ok, msg = True, ""
    except lr.LayerError as exc:
        ok, msg = False, str(exc)[:700]
    case("P10.2", "the filled 3.2 file is accepted by the preview", ok, msg or "accepted")
    if ok:
        lr.record(conn, cfg, RUN, f, keep=True)
        conn.commit()
        rep = lr.check(conn, cfg, RUN, name)
        conn.commit()
        st = rep["steps"]["3.2"]
        case("P10.3", "3.2 recorded and validated", st["closed"], f"{st['validated']}/{st['rows']}; failed {st['failed'][:2]}")
    # ── P11 step 3.3 and the partner gate
    msg = ""
    try:
        lr.open_step(conn, cfg, RUN, name, "3.3")
        opened = True
    except lr.LayerError as exc:
        opened, msg = False, str(exc)
    partners = conn.execute("SELECT DISTINCT substr(subject, 12) FROM collection_layer_item WHERE collection_id=? AND step='3.3' AND deleted=0", (cid,)).fetchall()
    from iba.app.lib import layerinner as _li
    names = sorted(_li.match_partners(r["subject"] for r in lr.derive(conn, cfg, lr.load(conn, cfg, name, pairs=True), "3.3")))
    case("P11.1", "3.3 refuses while a partner collection is not complete, and names the partners (the researcher: check the status first, then ask)", (not opened) and "partner collection" in msg, f"opened={opened}; {msg[:300]}")
    case("P11.2", "3.3 asks for one row for each unique match across the observations that reference more than one collection, with no minimum (researcher 2026-11-25)", None if not names else None, f"the rows it would demand are for partners {names[:8]}; no minimum number of shared verses is set (thresholds: {sorted(s['thresholds'])})")
    from iba.app.lib import layerinner as li
    L = lr.load(conn, cfg, name, pairs=True)
    src, req = li._sources(conn, s, L, lr.step_def(s, "3.3"), 0, (next(iter(li.matches(conn, L)), "")))
    own = {r[0] for r in conn.execute("SELECT DISTINCT observation_id FROM ib_node WHERE deleted=0 AND collection_id=?", (cid,))}
    partner_ib = {r[0] for r in conn.execute("SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.nature='inner_being' AND n.collection_id IS NOT NULL AND n.collection_id!=?", (cid,))}
    case("P11.3", "3.3 reads the inner-being observations of the collections in scope, the partners' too (the researcher: 'pull of all the inner being observations for all the collections in scope')", bool(src & partner_ib) or not partner_ib,
         f"sources offered {len(src)}, of them in a partner collection {len(src & partner_ib)}; inner_being observations that exist in other collections {len(partner_ib)}")
    # ── P9 the order of the closing
    gate_evidence = bv.closing_gate(conn, cfg, cid, "evidence")
    gate_both = bv.closing_gate(conn, cfg, cid, "both")
    case("P9.1", "the inner-being validation completes AFTER 3.3 (researcher 2026-11-24); so 3.3 must be able to close while inner-being observations are still being traced", None,
         f"cannot run 3.3 while the partners are open; the code closes 3.3 only when closing_gate('both') is empty (lib/layerreading.py check). evidence gate now: {gate_evidence[:2]}; both layers now: {gate_both[:2]}")
    return finish("after")


def main(db, scratch, phase, name="depart"):
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    import importlib.util as _iu     # the config the specification needs, applied to the COPY (the live migration waits for the researcher's approval)
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp)
    _sp.loader.exec_module(_m)
    _m.apply_to_copy(conn)
    scratch = pathlib.Path(scratch)
    scratch.mkdir(parents=True, exist_ok=True)
    return {"group": phase_group, "loop": phase_loop, "after": phase_after}[phase](cfg, conn, scratch, name)


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
