"""temp_2538_validation_actions_test_run.py -- escalation #2538 test plan (B:29, B:46) for iba/app/lib/validationactions.py, on a COPY of the
live iba.db (never the live DB). Each case states what is expected before the run; the result is PASS or FAIL.
Usage: python iba/app/tools/temp_2538_validation_actions_test_run.py <scratch dir>"""
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import validationactions as va  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
S = pathlib.Path(sys.argv[1]) / "t2538run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", ROOT / "iba/app/db/iba.db")
cfg = Cfg(DB)
conn = cfg.conn
RUN, WHO = "TEST-2538", "Claude"
res = []


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


# T1 install_nature: expected True then False; column and the two enum values exist
case("T1a", "install_nature adds the column and enum the first time", va.install_nature(conn) is True)
case("T1b", "install_nature is idempotent", va.install_nature(conn) is False)
conn.commit()
cfg = Cfg(DB)
conn = cfg.conn
case("T1c", "cfg.enum returns evidence and inner_being", sorted(cfg.enum(va.NATURE_ENUM)) == ["evidence", "inner_being"], cfg.enum(va.NATURE_ENUM))

# T2 set_nature: set, repeat, invalid, clear
case("T2a", "set_nature evidence on #22296 returns True and is logged once", va.set_nature(cfg, conn, 22296, "evidence", "the term observation states the sense of the word: evidence", RUN, WHO) and nlog(22296, "nature") == 1)
case("T2b", "setting the same value again changes nothing", va.set_nature(cfg, conn, 22296, "evidence", "the term observation states the sense of the word: evidence", RUN, WHO) is False and nlog(22296, "nature") == 1)
case("T2c", "a value outside the enum is refused", refused(va.set_nature, cfg, conn, 22296, "claim", "not a marker of the validation", RUN, WHO) is not None)
case("T2d", "clearing sets NULL and is logged", va.set_nature(cfg, conn, 22296, None, "cleared for the test of the clear path", RUN, WHO) and q("SELECT nature FROM ib_observation WHERE id=22296")[0][0] is None)

# T3 annotate a deleted observation
dead = q("SELECT id FROM ib_observation WHERE deleted=1 AND stage='verse-reading' ORDER BY id LIMIT 1")[0][0]
note = "Deleted before delete records were kept; the reason was not recorded. Confirmed by the researcher on 2026-11-22 to stay deleted. A trace that points here is handled by the validation."
case("T3a", f"annotate reaches deleted observation {dead}", va.annotate(conn, dead, note, RUN, WHO) and q("SELECT revisit_note, deleted FROM ib_observation WHERE id=?", dead)[0][0] == note)
case("T3b", "the same note again changes nothing", va.annotate(conn, dead, note, RUN, WHO) is False)
case("T3c", "a missing observation is refused", refused(va.annotate, conn, 999999999, note, RUN, WHO) is not None)
case("T3d", "modify_observation still refuses a deleted observation (no widening)", refused(orec.modify_observation, cfg, conn, dead, {"obs_text": "x" * 20}, "a test of the refusal", None, RUN, WHO) is not None)

# T4 deferral
va.defer(conn, 5793, 156, "the seek sense of H1875 is judged by the search collection", RUN, WHO)
case("T4a", "a deferral to collection 156 is listed for it", any(d["observation"] == 5793 for d in va.deferrals_to(conn, 156)))
case("T4b", "a deferral to a collection that does not exist is refused", refused(va.defer, conn, 5793, 999999, "no such collection to defer to", RUN, WHO) is not None)
va.defer(conn, 5793, 78, "a second owner for the test: the intend collection reads the plan words", RUN, WHO)
case("T4c", "an observation deferred to two collections is listed for both", any(d["observation"] == 5793 for d in va.deferrals_to(conn, 156)) and any(d["observation"] == 5793 for d in va.deferrals_to(conn, 78)))
va.close_deferral(conn, 5793, 156, "the search collection's validation closed the finding", RUN, WHO)
case("T4d", "a closed deferral leaves one list and stays on the other", all(d["observation"] != 5793 for d in va.deferrals_to(conn, 156)) and any(d["observation"] == 5793 for d in va.deferrals_to(conn, 78)))
case("T4e", "a deferral without its finding in words is refused", refused(va.defer, conn, 5793, 156, "short", RUN, WHO) is not None)

# T5 complete_node
case("T5a", "role completed on node 6951 (seek, role empty)", va.complete_node(cfg, conn, 6951, "characteristic", None, "the word is the characteristic the observation is about", RUN, WHO) == ["role"] and q("SELECT role FROM ib_node WHERE id=6951")[0][0] == "characteristic")
case("T5b", "a role outside reading.node_roles is refused", refused(va.complete_node, cfg, conn, 6951, "claim", None, "not a role at all in the config", RUN, WHO) is not None)
case("T5c", "a collection the surface does not belong to is refused (surface 'seek' is not in collection 1)", refused(va.complete_node, cfg, conn, 6951, None, 1, "the wrong collection on purpose", RUN, WHO) is not None)

# T6 restate
case("T6a", "restate without the check named is refused", refused(va.restate, cfg, conn, 7319, "In Jer 29:13, Isa 55:6 and 1Chr 28:9 the seeking is stated before the finding.", "", "reason given in words", RUN, WHO) is not None)
txt = "In Jer 29:13, Isa 55:6 and 1Chr 28:9 the seeking is stated before the finding; Isa 65:1 gives the finding to those who did not seek."
case("T6b", "restate with the check named changes obs_text and logs reason with the check", va.restate(cfg, conn, 7319, txt, "the three verses and Isa.65.1 read against the verse table", "the word 'invariably' is untrue", RUN, WHO) == ["obs_text"] and "checked:" in q("SELECT reason FROM ib_observation_change WHERE observation_id=7319 AND column_name='obs_text' ORDER BY id DESC LIMIT 1")[0][0])

# T7 add_trace
va.set_nature(cfg, conn, 22342, "evidence", "pairing statement: evidence about word positions", RUN, WHO)
va.set_nature(cfg, conn, 12431, "inner_being", "thoughts open to God: a building block", RUN, WHO)
case("T7a", "a trace to an observation not marked evidence is refused", refused(va.add_trace, conn, 12431, 22306, "target is not marked", RUN, WHO) is not None)
nid = va.add_trace(conn, 12431, 22342, "the evidence for the inner-being observation", RUN, WHO)
case("T7b", "a trace to marked evidence is written", nid is not None and q("SELECT traced_observation_id FROM ib_node WHERE id=?", nid)[0][0] == 22342)
case("T7c", "the same trace again returns None", va.add_trace(conn, 12431, 22342, "the same trace again", RUN, WHO) is None)
case("T7d", "a trace to itself is refused", refused(va.add_trace, conn, 12431, 12431, "a self trace", RUN, WHO) is not None)
case("T7e", "a trace to a deleted observation is refused", refused(va.add_trace, conn, 12431, dead, "a dead target", RUN, WHO) is not None)

# T8 create_evidence (draft E3 of the pilot): two occurrences, one finding
occ_inclined = q("SELECT verse_lexical_id FROM ib_node WHERE id=16651")[0][0]
occ_plan = q("SELECT verse_lexical_id FROM ib_node WHERE id=16652")[0][0]
spec = {"kind": "statement", "basis": "stated", "parts": {"item": "circumstance"},
        "text": "Deut 31:21 states a knowing ahead: 'I know what they are inclined to do even today, before I have brought them into the land'; the word inclined is H3336, the code of plan in 1Chr 28:9.",
        "nodes": [{"occurrence": occ_inclined, "strong": "H3336", "role": "characteristic"},
                  {"occurrence": occ_plan, "strong": "H3336", "role": "characteristic"}]}
case("T8a", "create_evidence without a stated contribution is refused", refused(va.create_evidence, cfg, conn, spec, [12413], "", RUN, WHO) is not None)
va.set_nature(cfg, conn, 12413, "inner_being", "God knows the inclination: a building block", RUN, WHO)
out = va.create_evidence(cfg, conn, spec, [12413], "states the timing of the knowing (before) and ties it to H3336, which no node holds", RUN, WHO)
ev = out["observation"]
case("T8b", "the new observation is live, marked evidence, with 2 word nodes", q("SELECT nature, deleted FROM ib_observation WHERE id=?", ev)[0][:] == ("evidence", 0) and len(out["nodes"]) == 2, out)
case("T8c", "12413 now traces to it", ev in va._live_traces(conn, 12413))
case("T8d", "the same text again is refused as already live", refused(va.create_evidence, cfg, conn, spec, [], "states the timing of the knowing and ties it to H3336 again", RUN, WHO) is not None)

# T9 consume: #22524 into #22604 (layer-3 pair, the later traces the earlier)
va.set_nature(cfg, conn, 22604, "inner_being", "heart or mind with the supposition: a building block", RUN, WHO)
tr_before = va._live_traces(conn, 22604)
case("T9a", "premise: #22604 traces #22524", 22524 in tr_before, tr_before)
r = refused(va.consume, cfg, conn, 22524, [22604], "short", RUN, WHO)
case("T9b", "a consumption with a bare mapping is refused", r is not None)
r = refused(va.consume, cfg, conn, 22524, [22524], "the mapping says what the old states and what carries it", RUN, WHO)
case("T9c", "an observation cannot be its own carrier", r is not None)
o_occ = va._occurrences(conn, 22524)
held = va._held_by(conn, list(o_occ), [22604])
if len(held) < len(o_occ):
    case("T9d", "an uncovered occurrence blocks the consumption until named", refused(va.consume, cfg, conn, 22524, [22604], "the heart or mind with the thought, stated again with a contrast in Isa 10:7", RUN, WHO) is not None)
    unc = {i: "the occurrence is a different word of the same verse and is not part of the finding" for i in o_occ if i not in held}
else:
    unc = {}
sources = [t for t in tr_before if t != 22524]
out = va.consume(cfg, conn, 22524, [22604], "#22524 says the heart or mind stands with the thought in ten verses and the verses place it there; #22604 says the same for the supposition and adds the Isa 10:7 contrast", RUN, WHO, unc)
case("T9e", "consume deletes #22524, writes consumed_by, drops the trace to it and gives #22604 its sources",
     q("SELECT deleted FROM ib_observation WHERE id=22524")[0][0] == 1 and nlog(22524, "consumed_by") == 1
     and 22524 not in va._live_traces(conn, 22604) and {22342, 22306} <= set(va._live_traces(conn, 22604)), (out, va._live_traces(conn, 22604)))
case("T9f", "no live trace points at the consumed observation", q("SELECT count(*) FROM ib_node WHERE traced_observation_id=22524 AND deleted=0")[0][0] == 0)

# T10 delete_neither
case("T10a", "an observation marked inner_being is not deleted as neither", refused(va.delete_neither, cfg, conn, 12431, "marked, so not neither in any way", RUN, WHO) is not None)
fh = va.facts_held(conn, 19915)
d = va.delete_neither(cfg, conn, 19915, "a table row of the earlier document with no study content of its own.", RUN, WHO)
row = q("SELECT deleted, revisit_note FROM ib_observation WHERE id=19915")[0]
case("T10b", "#19915 is commented first and deleted; the note names the uncovered count", row[0] == 1 and row[1].startswith("Neither evidence nor inner being") and f"{len(fh['uncovered'])} of {fh['nodes']}" in row[1], row)
case("T10c", "the note was logged before the delete (change ids in order)", q("SELECT min(id) FROM ib_observation_change WHERE observation_id=19915 AND column_name='revisit_note'")[0][0] < q("SELECT min(id) FROM ib_observation_change WHERE observation_id=19915 AND column_name='deleted'")[0][0])
case("T10d", "an observation another traces is not deleted as neither", refused(va.delete_neither, cfg, conn, 22306, "traced by layer-3 so not a candidate here", RUN, WHO) is not None)

# T11 create_observation (inner being on evidence), add_word_node, move_node, drop_node, self-evidencing, trace_gaps
occ_s, occ_k, occ_h = 1193130, 1193140, 1193133                 # searches, seek, hearts of 1Chr.28.9
spec2 = {"kind": "statement", "basis": "stated", "parts": {"item": "circumstance"},
         "text": "In 1Chr 28:9 the verb darash stands twice: the Lord searches all hearts, and the one addressed is to seek him.",
         "nodes": [{"occurrence": occ_s, "strong": "H1875", "role": "characteristic"}, {"occurrence": occ_k, "strong": "H1875", "role": "characteristic"}]}
va.set_nature(cfg, conn, 5797, "evidence", "the co-occurring codes of the verse: evidence", RUN, WHO)
o2 = va.create_observation(cfg, conn, spec2, "inner_being", "states the mirrored seeking and searching of one verb in one verse, which the evidence row only lists", RUN, WHO, traces=[5797])
inner = o2["observation"]
case("T11a", "an inner-being observation is created with its trace to marked evidence", q("SELECT nature FROM ib_observation WHERE id=?", inner)[0][0] == "inner_being" and 5797 in va._live_traces(conn, inner))
case("T11b", "trace_gaps finds no gap for it", inner not in va.trace_gaps(conn, [inner])["no_trace"])
case("T11c", "an inner-being observation traced to a non-evidence observation is refused at creation", refused(va.create_observation, cfg, conn, dict(spec2, text="In 1Chr 28:9 darash stands twice, as searches and as seek, in one verse."), "inner_being", "a second statement to test the refusal of an unmarked trace", RUN, WHO, traces=[22306]) is not None)
nn = va.add_word_node(cfg, conn, inner, occ_h, "H3824", "object", "the hearts are what the Lord searches", RUN, WHO)
case("T11d", "a word node is added; the same again returns None", nn is not None and va.add_word_node(cfg, conn, inner, occ_h, "H3824", "object", "the same node again", RUN, WHO) is None)
case("T11e", "move_node refuses an occurrence the target already holds", refused(va.move_node, cfg, conn, nn, inner, "the node is already there", RUN, WHO) is not None)
case("T11f", "drop_node refuses when no carrier holds the occurrence", refused(va.drop_node, conn, nn, [22306], "no carrier here", RUN, WHO) is not None)
case("T11g", "drop_node deletes a node carried by another live observation", va.drop_node(conn, nn, [19501], "the hearts occurrence is held by observation 19501", RUN, WHO) is True and q("SELECT deleted FROM ib_node WHERE id=?", nn)[0][0] == 1)
va.set_nature(cfg, conn, 19501, "inner_being", "know and serve with the whole inner being: a building block", RUN, WHO)
case("T11h", "an inner-being observation with no trace is a gap", 19501 in va.trace_gaps(conn, [19501])["no_trace"])
va.mark_self_evidencing(conn, 19501, "quotes the verse and holds a word node for each of the eleven words it relies on", RUN, WHO)
case("T11i", "self-evidencing removes the gap", 19501 not in va.trace_gaps(conn, [19501])["no_trace"])

# T12 drop_unrelated_node, note_node, pending in trace_gaps
w = q("SELECT id FROM ib_node WHERE observation_id=20489 AND deleted=0 AND verse_lexical_id IS NOT NULL ORDER BY id LIMIT 2")
case("T12a", "drop_unrelated_node needs the reason in words", refused(va.drop_unrelated_node, conn, w[0][0], "short", RUN, WHO) is not None)
case("T12b", "an unrelated word node is deleted while others remain", va.drop_unrelated_node(conn, w[0][0], "the word is the 'know' of another clause and supports none of the findings of this observation", RUN, WHO) is True)
only = q("SELECT id FROM ib_node WHERE observation_id=22296 AND deleted=0 AND verse_lexical_id IS NOT NULL")
case("T12c", "the last word node of an observation is not deleted", len(only) != 1 or refused(va.drop_unrelated_node, conn, only[0][0], "the only word node, so it must stay as the context of the observation", RUN, WHO) is not None)
case("T12d", "note_node keeps the reason a column stays empty", va.note_node(conn, 64332, "the surface belongs to no single collection by the member rule, so the collection stays empty", RUN, WHO) is True and va.note_node(conn, 64332, "the surface belongs to no single collection by the member rule, so the collection stays empty", RUN, WHO) is False)
va.set_nature(cfg, conn, 22594, "inner_being", "desire beside the supposition: a building block", RUN, WHO)
case("T12e", "traces to unmarked evidence are pending, not a gap", 22594 in va.trace_gaps(conn, [22594])["pending"] and 22594 not in va.trace_gaps(conn, [22594])["no_trace"])

conn.commit()
print(f"\n{sum(res)}/{len(res)} PASS")
sys.exit(0 if all(res) else 1)
