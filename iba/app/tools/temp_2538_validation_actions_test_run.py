"""temp_2538_validation_actions_test_run.py -- escalation #2538 test plan (B:29, B:46) for iba/app/lib/validationactions.py, on a COPY of the
live iba.db (never the live DB). Each case states what is expected before the run; the result is PASS or FAIL.

Independent of the state of live (rewritten 2026-11-26, BUILD.md 595; the researcher: "Yes, fix them"): the first version named fixed observation and node ids of
2026-11-22, which the later readings and sweeps deleted. Every case now picks what it needs from the copy by the condition it needs (an unmarked observation with
word nodes, an inner-being observation with no trace, a word node with no role, ...), or builds it on the copy with the library's own functions (the consume pair,
the pending trace). install_nature is tested on an in-memory database that lacks the column, and on the copy, which has it.
Usage: python iba/app/tools/temp_2538_validation_actions_test_run.py <scratch dir>"""
import pathlib
import shutil
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import validationactions as va  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
LIVE = ROOT / "iba/app/db/iba.db"
S = pathlib.Path(sys.argv[1]) / "t2538run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", LIVE)
if pathlib.Path(DB).resolve() == LIVE.resolve():
    sys.exit("refused: this test runs on a copy, never the live database")
cfg = Cfg(DB)
conn = cfg.conn
RUN, WHO = "TEST-2538", "Claude"
res = []
USED: set = set()


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:700]}"), flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def refused(fn, *a, **k):
    try:
        fn(*a, **k)
    except orec.Refused as e:
        return str(e)
    return None


def nlog(oid, col):
    return q("SELECT count(*) FROM ib_observation_change WHERE observation_id=? AND column_name=?", oid, col)[0][0]


WORD = "EXISTS (SELECT 1 FROM ib_node w WHERE w.observation_id=o.id AND w.deleted=0 AND w.verse_lexical_id IS NOT NULL AND w.traced_observation_id IS NULL)"
UNTRACED = "NOT EXISTS (SELECT 1 FROM ib_node t WHERE t.traced_observation_id=o.id AND t.deleted=0)"
NO_TRACE = "NOT EXISTS (SELECT 1 FROM ib_node t WHERE t.observation_id=o.id AND t.deleted=0 AND t.traced_observation_id IS NOT NULL)"


def pick(where, *a, label=""):
    """The first live observation of the copy meeting `where` that no earlier case has taken."""
    for (oid,) in q(f"SELECT o.id FROM ib_observation o WHERE o.deleted=0 AND {where} ORDER BY o.id LIMIT {len(USED) + 1}", *a):      # rowid order: stops at the first match
        if oid not in USED:
            USED.add(oid)
            return oid
    sys.exit(f"the copy holds no observation for {label or where}: the test cannot set its case")


def word_nodes(oid):
    return [r[0] for r in q("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_lexical_id IS NOT NULL AND traced_observation_id IS NULL ORDER BY id", oid)]


# T1 install_nature: on a database without the column it adds the column and the enum; again, nothing; on the copy (installed) nothing
mem = sqlite3.connect(":memory:")
mem.execute("CREATE TABLE ib_observation (id INTEGER PRIMARY KEY)")
mem.execute("CREATE TABLE cfg_enum (name TEXT, value TEXT, ordinal INTEGER, inactive INTEGER)")
case("T1a", "install_nature adds the column and enum on a database without them", va.install_nature(mem) is True and va._has_nature(mem))
case("T1b", "install_nature is idempotent (the same database again, and the copy, which has them)", va.install_nature(mem) is False and va.install_nature(conn) is False)
case("T1c", "cfg.enum returns evidence and inner_being", sorted(cfg.enum(va.NATURE_ENUM)) == ["evidence", "inner_being"], cfg.enum(va.NATURE_ENUM))

# T2 set_nature: set, repeat, invalid, clear -- on an unmarked observation with word nodes
X = pick(f"o.nature IS NULL AND {WORD} AND {UNTRACED}", label="an unmarked observation")
case("T2a", f"set_nature evidence on #{X} returns True and is logged once", va.set_nature(cfg, conn, X, "evidence", "the term observation states the sense of the word: evidence", RUN, WHO) and nlog(X, "nature") == 1)
case("T2b", "setting the same value again changes nothing", va.set_nature(cfg, conn, X, "evidence", "the term observation states the sense of the word: evidence", RUN, WHO) is False and nlog(X, "nature") == 1)
case("T2c", "a value outside the enum is refused", refused(va.set_nature, cfg, conn, X, "claim", "not a marker of the validation", RUN, WHO) is not None)
case("T2d", "clearing sets NULL and is logged", va.set_nature(cfg, conn, X, None, "cleared for the test of the clear path", RUN, WHO) and q("SELECT nature FROM ib_observation WHERE id=?", X)[0][0] is None)

# T3 annotate a deleted observation
dead = q("SELECT id FROM ib_observation WHERE deleted=1 ORDER BY id LIMIT 1")[0][0]
note = "Deleted before delete records were kept; the reason was not recorded. A trace that points here is handled by the validation (test note on a copy)."
case("T3a", f"annotate reaches deleted observation {dead}", va.annotate(conn, dead, note, RUN, WHO) and q("SELECT revisit_note, deleted FROM ib_observation WHERE id=?", dead)[0][0] == note)
case("T3b", "the same note again changes nothing", va.annotate(conn, dead, note, RUN, WHO) is False)
case("T3c", "a missing observation is refused", refused(va.annotate, conn, 999999999, note, RUN, WHO) is not None)
case("T3d", "modify_observation still refuses a deleted observation (no widening)", refused(orec.modify_observation, cfg, conn, dead, {"obs_text": "x" * 20}, "a test of the refusal", None, RUN, WHO) is not None)

# T4 deferral, to two existing collections
D = pick(f"{WORD}", label="any observation")
c1, c2 = [r[0] for r in q("SELECT id FROM collection WHERE deleted=0 ORDER BY id LIMIT 2")]
va.defer(conn, D, c1, "the sense is judged by the first collection's validation (test)", RUN, WHO)
case("T4a", f"a deferral to collection {c1} is listed for it", any(d["observation"] == D for d in va.deferrals_to(conn, c1)))
case("T4b", "a deferral to a collection that does not exist is refused", refused(va.defer, conn, D, 999999, "no such collection to defer to", RUN, WHO) is not None)
va.defer(conn, D, c2, "a second owner for the test: the second collection reads it as well", RUN, WHO)
case("T4c", "an observation deferred to two collections is listed for both", any(d["observation"] == D for d in va.deferrals_to(conn, c1)) and any(d["observation"] == D for d in va.deferrals_to(conn, c2)))
va.close_deferral(conn, D, c1, "the first collection's validation closed the finding", RUN, WHO)
case("T4d", "a closed deferral leaves one list and stays on the other", all(d["observation"] != D for d in va.deferrals_to(conn, c1)) and any(d["observation"] == D for d in va.deferrals_to(conn, c2)))
case("T4e", "a deferral without its finding in words is refused", refused(va.defer, conn, D, c1, "short", RUN, WHO) is not None)

# T5 complete_node: a live word node with no role
node = q("SELECT n.id, n.surface FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND n.role IS NULL AND n.verse_lexical_id IS NOT NULL "
         "AND n.traced_observation_id IS NULL ORDER BY n.observation_id LIMIT 1")[0]
own = orec.surface_collection_map(conn).get((node[1] or "").strip().lower())
wrong = q("SELECT id FROM collection WHERE deleted=0 AND id IS NOT ? ORDER BY id LIMIT 1", own)[0][0]
case("T5a", f"role completed on node {node[0]} ({node[1]}, role empty)", va.complete_node(cfg, conn, node[0], "characteristic", None, "the word is the characteristic the observation is about", RUN, WHO) == ["role"]
     and q("SELECT role FROM ib_node WHERE id=?", node[0])[0][0] == "characteristic")
case("T5b", "a role outside reading.node_roles is refused", refused(va.complete_node, cfg, conn, node[0], "claim", None, "not a role at all in the config", RUN, WHO) is not None)
case("T5c", f"a collection the surface does not belong to is refused (collection {wrong})", refused(va.complete_node, cfg, conn, node[0], None, wrong, "the wrong collection on purpose", RUN, WHO) is not None)

# T6 restate
R = pick(f"{WORD}", label="any observation")
case("T6a", "restate without the check named is refused", refused(va.restate, cfg, conn, R, "In Jer 29:13, Isa 55:6 and 1Chr 28:9 the seeking is stated before the finding.", "", "reason given in words", RUN, WHO) is not None)
txt = "In Jer 29:13, Isa 55:6 and 1Chr 28:9 the seeking is stated before the finding; Isa 65:1 gives the finding to those who did not seek."
case("T6b", "restate with the check named changes obs_text and logs reason with the check", va.restate(cfg, conn, R, txt, "the three verses and Isa.65.1 read against the verse table", "the earlier wording is untrue (test)", RUN, WHO) == ["obs_text"]
     and "checked:" in q("SELECT reason FROM ib_observation_change WHERE observation_id=? AND column_name='obs_text' ORDER BY id DESC LIMIT 1", R)[0][0])

# T7 add_trace: an evidence fixture, an inner-being holder, an unmarked target
E = pick(f"o.nature IS NULL AND {WORD}", label="an unmarked observation for evidence")
va.set_nature(cfg, conn, E, "evidence", "test fixture: marked evidence", RUN, WHO)
I = pick(f"o.nature='inner_being' AND {WORD}", label="an inner-being observation")
U = pick(f"o.nature IS NULL AND {WORD}", label="an unmarked target")
case("T7a", "a trace to an observation not marked evidence is refused", refused(va.add_trace, conn, I, U, "target is not marked", RUN, WHO) is not None)
nid = va.add_trace(conn, I, E, "the evidence for the inner-being observation", RUN, WHO)
case("T7b", "a trace to marked evidence is written", nid is not None and q("SELECT traced_observation_id FROM ib_node WHERE id=?", nid)[0][0] == E)
case("T7c", "the same trace again returns None", va.add_trace(conn, I, E, "the same trace again", RUN, WHO) is None)
case("T7d", "a trace to itself is refused", refused(va.add_trace, conn, I, I, "a self trace", RUN, WHO) is not None)
case("T7e", "a trace to a deleted observation is refused", refused(va.add_trace, conn, I, dead, "a dead target", RUN, WHO) is not None)

# T8 create_evidence: two occurrences of H1875 in 1Chr 28:9 (base data), one finding, serving the inner-being holder
occ_s, occ_k, occ_h = 1193130, 1193140, 1193133                 # searches, seek, hearts of 1Chr.28.9
spec = {"kind": "statement", "basis": "stated", "parts": {"item": "circumstance"},
        "text": "In 1Chr 28:9 the code H1875 carries both the Lord's searching and the seeking asked of the one addressed (test evidence on a copy).",
        "nodes": [{"occurrence": occ_s, "strong": "H1875", "role": "characteristic"}, {"occurrence": occ_k, "strong": "H1875", "role": "characteristic"}]}
I2 = pick(f"o.nature='inner_being' AND {WORD}", label="a second inner-being observation")
case("T8a", "create_evidence without a stated contribution is refused", refused(va.create_evidence, cfg, conn, spec, [I2], "", RUN, WHO) is not None)
out = va.create_evidence(cfg, conn, spec, [I2], "states that one code carries both acts of the verse, which no node holds", RUN, WHO)
ev = out["observation"]
case("T8b", "the new observation is live, marked evidence, with 2 word nodes", tuple(q("SELECT nature, deleted FROM ib_observation WHERE id=?", ev)[0]) == ("evidence", 0) and len(out["nodes"]) == 2, out)
case("T8c", f"#{I2} now traces to it", ev in va._live_traces(conn, I2))
case("T8d", "the same text again is refused as already live", refused(va.create_evidence, cfg, conn, spec, [], "states that one code carries both acts of the verse again", RUN, WHO) is not None)

# T9 consume: a pair built on the copy -- A (evidence, tracing E) is carried by B (inner being on the same occurrence, tracing A)
specA = {"kind": "statement", "basis": "stated", "parts": {"item": "circumstance"}, "text": "In 1Chr 28:9 the seeking is asked of the one addressed (test fixture A on a copy).",
         "nodes": [{"occurrence": occ_k, "strong": "H1875", "role": "characteristic"}]}
A = va.create_observation(cfg, conn, specA, "evidence", "test fixture A: the seeking asked, for the consume case", RUN, WHO, traces=[E])["observation"]
specB = dict(specA, text="In 1Chr 28:9 the one addressed is asked to seek, and the finding is promised to the seeker (test fixture B on a copy).")
B = va.create_observation(cfg, conn, specB, "inner_being", "test fixture B: the seeking with its promise, carrying A", RUN, WHO, traces=[A])["observation"]
case("T9a", f"premise: #{B} traces #{A}", A in va._live_traces(conn, B))
case("T9b", "a consumption with a bare mapping is refused", refused(va.consume, cfg, conn, A, [B], "short", RUN, WHO) is not None)
case("T9c", "an observation cannot be its own carrier", refused(va.consume, cfg, conn, A, [A], "the mapping says what the old states and what carries it", RUN, WHO) is not None)
o_occ = va._occurrences(conn, A)
held = va._held_by(conn, list(o_occ), [B])
unc = {i: "the occurrence is a different word of the same verse and is not part of the finding" for i in o_occ if i not in held}
out = va.consume(cfg, conn, A, [B], "A says the seeking is asked; B says the same and adds the promise to the seeker, so B carries all of A", RUN, WHO, unc)
case("T9e", "consume deletes A, writes consumed_by, drops the trace to it and gives B the source of A",
     q("SELECT deleted FROM ib_observation WHERE id=?", A)[0][0] == 1 and nlog(A, "consumed_by") == 1 and A not in va._live_traces(conn, B) and E in va._live_traces(conn, B), (out, va._live_traces(conn, B)))
case("T9f", "no live trace points at the consumed observation", q("SELECT count(*) FROM ib_node WHERE traced_observation_id=? AND deleted=0", A)[0][0] == 0)

# T10 delete_neither
case("T10a", "an observation marked inner_being is not deleted as neither", refused(va.delete_neither, cfg, conn, I, "marked, so not neither in any way", RUN, WHO) is not None)
N = pick(f"o.nature IS NULL AND {WORD} AND {UNTRACED}", label="an unmarked untraced observation")
fh = va.facts_held(conn, N)
va.delete_neither(cfg, conn, N, "a table row of the earlier document with no study content of its own.", RUN, WHO)
row = q("SELECT deleted, revisit_note FROM ib_observation WHERE id=?", N)[0]
case("T10b", f"#{N} is commented first and deleted; the note names the uncovered count", row[0] == 1 and row[1].startswith("Neither evidence nor inner being") and f"{len(fh['uncovered'])} of {fh['nodes']}" in row[1], row)
case("T10c", "the note was logged before the delete (this run's change ids in order)", q("SELECT min(id) FROM ib_observation_change WHERE observation_id=? AND column_name='revisit_note' AND run_id=?", N, RUN)[0][0]
     < q("SELECT min(id) FROM ib_observation_change WHERE observation_id=? AND column_name='deleted' AND run_id=?", N, RUN)[0][0])
K = pick(f"o.nature IS NULL AND {WORD} AND {UNTRACED}", label="an unmarked observation to be traced")
va.add_trace(conn, I2, K, "a carried-over trace for the test (moved)", RUN, WHO, moved=True)
case("T10d", "an observation another traces is not deleted as neither", refused(va.delete_neither, cfg, conn, K, "traced by another, so not a candidate here", RUN, WHO) is not None)

# T11 create_observation (inner being on evidence), add_word_node, move_node, drop_node, self-evidencing, trace_gaps
spec2 = {"kind": "statement", "basis": "stated", "parts": {"item": "circumstance"},
         "text": "In 1Chr 28:9 the verb darash stands twice: the Lord searches all hearts, and the one addressed is to seek him.",
         "nodes": [{"occurrence": occ_s, "strong": "H1875", "role": "characteristic"}, {"occurrence": occ_k, "strong": "H1875", "role": "characteristic"}]}
o2 = va.create_observation(cfg, conn, spec2, "inner_being", "states the mirrored seeking and searching of one verb in one verse", RUN, WHO, traces=[E])
inner = o2["observation"]
case("T11a", "an inner-being observation is created with its trace to marked evidence", q("SELECT nature FROM ib_observation WHERE id=?", inner)[0][0] == "inner_being" and E in va._live_traces(conn, inner))
case("T11b", "trace_gaps finds no gap for it", inner not in va.trace_gaps(conn, [inner])["no_trace"])
case("T11c", "an inner-being observation traced to a non-evidence observation is refused at creation",
     refused(va.create_observation, cfg, conn, dict(spec2, text="In 1Chr 28:9 darash stands twice, as searches and as seek, in one verse."), "inner_being",
             "a second statement to test the refusal of an unmarked trace", RUN, WHO, traces=[U]) is not None)
nn = va.add_word_node(cfg, conn, inner, occ_h, "H3824", "object", "the hearts are what the Lord searches", RUN, WHO)
case("T11d", "a word node is added; the same again returns None", nn is not None and va.add_word_node(cfg, conn, inner, occ_h, "H3824", "object", "the same node again", RUN, WHO) is None)
case("T11e", "move_node refuses an occurrence the target already holds", refused(va.move_node, cfg, conn, nn, inner, "the node is already there", RUN, WHO) is not None)
case("T11f", "drop_node refuses when no carrier holds the occurrence", refused(va.drop_node, conn, nn, [U], "no carrier here", RUN, WHO) is not None)
carrier = pick("EXISTS (SELECT 1 FROM ib_node w WHERE w.observation_id=o.id AND w.deleted=0 AND w.verse_lexical_id=?) AND o.id != ?", occ_h, inner, label="a holder of the hearts occurrence")
case("T11g", "drop_node deletes a node carried by another live observation", va.drop_node(conn, nn, [carrier], f"the hearts occurrence is held by observation {carrier}", RUN, WHO) is True
     and q("SELECT deleted FROM ib_node WHERE id=?", nn)[0][0] == 1)
G = pick(f"o.nature='inner_being' AND {WORD} AND {NO_TRACE} AND NOT EXISTS (SELECT 1 FROM ib_observation_change c WHERE c.observation_id=o.id AND c.column_name='self_evidencing')",
         label="an inner-being observation with no trace")
case("T11h", "an inner-being observation with no trace is a gap", G in va.trace_gaps(conn, [G])["no_trace"])
va.mark_self_evidencing(conn, G, "quotes the verse and holds a word node for each word it relies on (test)", RUN, WHO)
case("T11i", "self-evidencing removes the gap", G not in va.trace_gaps(conn, [G])["no_trace"])

# T12 drop_unrelated_node, note_node, pending in trace_gaps
M = pick("(SELECT count(*) FROM ib_node w WHERE w.observation_id=o.id AND w.deleted=0 AND w.verse_lexical_id IS NOT NULL AND w.traced_observation_id IS NULL) >= 2", label="an observation with two word nodes")
w = word_nodes(M)
case("T12a", "drop_unrelated_node needs the reason in words", refused(va.drop_unrelated_node, conn, w[0], "short", RUN, WHO) is not None)
case("T12b", "an unrelated word node is deleted while others remain", va.drop_unrelated_node(conn, w[0], "the word is of another clause and supports none of the findings of this observation", RUN, WHO) is True)
only = word_nodes(pick(f"(SELECT count(*) FROM ib_node w WHERE w.observation_id=o.id AND w.deleted=0 AND w.verse_lexical_id IS NOT NULL AND w.traced_observation_id IS NULL) = 1",
                       label="an observation with one word node"))
case("T12c", "the last word node of an observation is not deleted", refused(va.drop_unrelated_node, conn, only[0], "the only word node, so it must stay as the context of the observation", RUN, WHO) is not None)
nd = word_nodes(R)[0]
msg = "the surface belongs to no single collection by the member rule, so the collection stays empty"
case("T12d", "note_node keeps the reason a column stays empty", va.note_node(conn, nd, msg, RUN, WHO) is True and va.note_node(conn, nd, msg, RUN, WHO) is False)
E2 = pick(f"o.nature IS NULL AND {WORD}", label="an unmarked observation for the pending case")
va.set_nature(cfg, conn, E2, "evidence", "test fixture: evidence, cleared below", RUN, WHO)
P = pick(f"o.nature='inner_being' AND {WORD} AND {NO_TRACE}", label="an inner-being observation with no trace, for the pending case")
va.add_trace(conn, P, E2, "the evidence of the pending case", RUN, WHO)
va.set_nature(cfg, conn, E2, None, "the marker withdrawn: the target is not yet marked (test)", RUN, WHO)
case("T12e", "traces to unmarked evidence are pending, not a gap", P in va.trace_gaps(conn, [P])["pending"] and P not in va.trace_gaps(conn, [P])["no_trace"])

# T13 merge and node edits, directly (carried from temp_2323_deleted_and_fixes_test_run.py, retired with the reading steps it drove; BUILD.md 595)
a_, b_ = pick(f"{WORD}", label="a first observation"), pick(f"{WORD}", label="a second observation")
case("T13a", "a merge of two different descriptions is refused", "texts differ" in (refused(orec.merge_observation, conn, a_, b_, "test: two different descriptions", None, RUN, WHO) or ""))
nid2 = word_nodes(a_)[0]
orec.modify_node(cfg, conn, nid2, {"role": "qualifier"}, "test: the word is a qualifier here", None, RUN, WHO)
case("T13b", "a role is modified in place and logged", q("SELECT role FROM ib_node WHERE id=?", nid2)[0][0] == "qualifier"
     and q("SELECT count(*) FROM ib_observation_change WHERE node_id=? AND column_name='role' AND run_id=?", nid2, RUN)[0][0] == 1)
case("T13c", "a node delete without a reason in words is refused (10 characters or more)", "reason" in (refused(orec.delete_node, conn, nid2, "short", None, RUN, WHO) or ""))
case("T13d", "delete_node on a node already deleted is a no-op (False)", orec.delete_node(conn, nid2, "test: this node is deleted", None, RUN, WHO) is True
     and orec.delete_node(conn, nid2, "test: deleted a second time", None, RUN, WHO) is False)
files = [f for f in ("iba/app/lib/reading.py", "iba/app/lib/observationrecord.py", "iba/app/lib/versecollate.py", "iba/app/lib/versescope.py", "iba/app/lib/strandreading.py",
                     "iba/app/lib/layerreading.py", "iba/app/lib/layerinner.py", "iba/app/lib/validationactions.py") if (ROOT / f).exists()]
case("T13e", "no reader of live observations or nodes takes status or disposition 'withdrawn' as the live test (the deleted column is)",
     not any(s_ in (ROOT / f).read_text(encoding="utf-8") for f in files for s_ in ("status<>'withdrawn'", "disposition<>'withdrawn'", "status != 'withdrawn'")), files)

conn.rollback()
print(f"\n{sum(res)}/{len(res)} PASS")
sys.exit(0 if all(res) else 1)
