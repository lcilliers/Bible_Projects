"""temp_2538_validation_apply_1chr28_9.py -- escalation #2538: the actions of plan v9 section 8 applied to the 55 observations of 1Chr.28.9 on a COPY
of the live iba.db (never the live DB), through iba/app/lib/validationactions.py. Every step is tried on its own; a refusal is reported,
not hidden. Usage: python iba/app/tools/temp_2538_validation_apply_1chr28_9.py <scratch dir> [<db path to keep>]
Prints one line per step (OK or REFUSED with the reason) and the counts at the end."""
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import validationactions as va  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
S = pathlib.Path(sys.argv[1]) / "t2538apply"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db", ROOT / "iba/app/db/iba.db")
RUN, WHO = "PILOT-2538-1CHR-28-9-APPLY", "Claude"

# every top-level action that succeeds is recorded as a line of a sheet for Collection-Build.ps1 -Action ValidateRecord; a created observation is
# named "@new<k>" in the later actions that use it (the k-th create_observation of the sheet)
import inspect  # noqa: E402
SHEET, CREATED, DEPTH = [], {}, [0]
ID_PARAMS = {"oid", "old_id", "target", "to_obs", "serves", "traces", "carriers", "carried_by"}


def _sub(k, v):
    if k in ID_PARAMS:
        return [CREATED.get(x, x) for x in v] if isinstance(v, (list, tuple)) else CREATED.get(v, v)
    return v


def _wrap(name):
    fn, sig = getattr(va, name), inspect.signature(getattr(va, name))

    def w(*a, **k):
        top = DEPTH[0] == 0
        DEPTH[0] += 1
        try:
            out = fn(*a, **k)
        finally:
            DEPTH[0] -= 1
        if top:
            b = sig.bind(*a, **k)
            b.apply_defaults()
            line = {"action": name}
            for n, v in b.arguments.items():
                if n in ("cfg", "conn", "run_id", "who"):
                    continue
                if sig.parameters[n].kind is inspect.Parameter.VAR_KEYWORD:
                    line.update(v)                       # extra keyword parameters (restate's more): flattened, none when empty
                else:
                    line[n] = _sub(n, v)
            SHEET.append(line)
            if name == "create_observation":
                CREATED[out["observation"]] = f"@new{len(CREATED) + 1}"
        return out
    return w


for _n in ("set_nature", "defer", "close_deferral", "annotate", "complete_node", "note_node", "restate", "add_trace", "create_observation", "add_word_node", "move_node",
           "drop_node", "drop_unrelated_node", "consume", "delete_neither", "mark_self_evidencing"):
    setattr(va, _n, _wrap(_n))
conn0 = Cfg(DB).conn
va.install_nature(conn0)
conn0.commit()
cfg = Cfg(DB)
conn = cfg.conn
q = lambda s, *a: conn.execute(s, a).fetchall()
LOG = []


def step(name, fn):
    try:
        r = fn()
        LOG.append((name, "OK", r))
        print(f"OK       {name}" + (f"  {r}" if r not in (None, True, False, []) else ""), flush=True)
        return r
    except orec.Refused as e:
        LOG.append((name, "REFUSED", str(e)))
        print(f"REFUSED  {name}  -- {str(e)[:600]}", flush=True)
    except Exception as e:  # a bug in this script: shown, not hidden
        LOG.append((name, "ERROR", repr(e)))
        print(f"ERROR    {name}  -- {e!r}", flush=True)


IDS = [r[0] for r in q("SELECT DISTINCT o.id FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id AND n.deleted=0 "
                       "WHERE o.deleted=0 AND n.verse_reference='1Chr.28.9' ORDER BY o.id")]
assert len(IDS) == 55, len(IDS)

# ── 1. the marker (from the reading of the pilot) ───────────────────────────────────────────────────────────
EV = [5793, 5797, 7091, 7317, 12412, 16318, 17012, 17057, 17167, 17270, 19508, 22296, 22306, 22313, 22332, 22342, 22344, 22346, 22360,
      22361, 22369, 22413, 22431, 22438, 22445, 22608, 22622, 22623, 22631]
IB = [7303, 7319, 7320, 12413, 12431, 17271, 19501, 20019, 20216, 20455, 20489, 20498, 20549, 21752, 21757, 22524, 22525, 22594, 22604, 22606]
NEITHER = [19613, 19915, 20029, 20345, 20414, 20427]
assert sorted(EV + IB + NEITHER) == IDS, sorted(set(IDS) ^ set(EV + IB + NEITHER))
for oid in EV:
    step(f"nature evidence #{oid}", lambda oid=oid: va.set_nature(cfg, conn, oid, "evidence", "read against the base data: the observation states what the data are or show", RUN, WHO))
for oid in IB:
    step(f"nature inner_being #{oid}", lambda oid=oid: va.set_nature(cfg, conn, oid, "inner_being", "read against the base data: the observation states how something works in the inner being", RUN, WHO))

# ── 2. node roles completed (each role by what the finding is about) ───────────────────────────────────────────
CHAR = {5793: {"H1875"}, 5797: {"H1875"}, 7091: {"H1875"}, 7303: {"H1875"}, 7317: {"H1875"}, 7319: {"H1875"}, 7320: {"H1875"},
        12412: {"H3336"}, 12413: {"H3336"}, 12431: {"H7454", "H8312", "H4284", "G1761", "G1261", "G1270"}}
for oid, chars in CHAR.items():
    for nid, st, sf in q("SELECT id, strong, surface FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND role IS NULL", oid):
        role = "characteristic" if st in chars else "qualifier"
        step(f"role #{oid} node {nid} {sf} {st} -> {role}", lambda nid=nid, role=role: va.complete_node(
            cfg, conn, nid, role, None, "the role is what the word is in the finding the observation states (characteristic: the word the finding is about; qualifier: the word beside it)", RUN, WHO))

# ── 3. the six that are neither: comment first, then deleted (researcher 2026-11-22) ──────────────────────────────
WHY = {19613: "a statement about election, not about a word or the inner being; it points at a section of the earlier document.",
       19915: "a table row of the earlier document with no study content of its own.",
       20029: "an outline line of the earlier document that lists verses and states no finding.",
       20345: "a review-table row of the earlier document with no study content of its own.",
       20414: "a review-table row of the earlier document that cites its section numbers and states no finding of its own.",
       20427: "a working note of the earlier document (nothing woven, waits for the researcher) with no finding."}
for oid in NEITHER:
    step(f"delete neither #{oid}", lambda oid=oid: va.delete_neither(cfg, conn, oid, WHY[oid] + " Ruled deleted by the researcher on 2026-11-22.", RUN, WHO))

# ── 4. evidence that earns its place (plan v9 section 4) ─────────────────────────────────────────────────────────
def spec(text, nodes):
    return {"kind": "statement", "basis": "stated", "parts": {"item": "circumstance"}, "text": text, "nodes": nodes}


T = {"Ps.139.2": (1266422, "H7454", 1266420, "H0995"), "Ps.139.23": (1249981, "H8312", 1249978, "H3045"), "1Chr.28.9": (1193138, "H4284", 1193134, "H0995"),
     "Isa.66.18": (1308866, "H4284", None, None), "Ps.94.11": (1266797, "H4284", 1266796, "H3045"), "1Cor.3.20": (1483839, "G1261", 1483838, "G1097"),
     "Luke.5.22": (1439973, "G1261", 1439971, "G1921"), "Luke.6.8": (1434988, "G1261", 1434986, "G1492I"), "Luke.11.17": (1435976, "G1270", 1435974, "G6063"),
     "Matt.9.4": (1410604, "G1761", 1410602, "G1492H"), "Matt.12.25": (1410756, "G1761", 1410754, "G6063"), "Heb.4.12": (1504175, "G1761", 1504174, "G2924")}
e1_nodes = []
for ref, (to, ts, vo, vs) in T.items():
    e1_nodes.append({"occurrence": to, "strong": ts, "role": "object"})
    if vo:
        e1_nodes.append({"occurrence": vo, "strong": vs, "role": "characteristic", "supports": to})
e1_nodes.append({"occurrence": 1193130, "strong": "H1875", "role": "characteristic"})
E1 = spec("God is the one who discerns, knows or understands thoughts in Ps 139:2 ('you discern my thoughts'), Ps 94:11 and 1Cor 3:20 ('knows the thoughts'), "
          "Isa 66:18 ('I know their works and their thoughts') and 1Chr 28:9, where the Lord 'searches all hearts' and 'understands every plan and thought'. "
          "In Ps 139:23 God is asked to know the speaker's thoughts. Jesus is the one who perceives or knows their thoughts in Luke 5:22, 6:8 and 11:17 and in Matt 9:4 and 12:25. "
          "In Heb 4:12 the word of God discerns 'the thoughts and intentions' of the heart.", e1_nodes)
e1 = step("create evidence E1 (who knows thoughts)", lambda: va.create_observation(
    cfg, conn, E1, "evidence", "states who is the subject of knowing, discerning or understanding thoughts in each verse, with Ps 139:23 as a petition and Heb 4:12 as the word of God; the nodes hold the words, not who does what to what", RUN, WHO, serves=[12431]))
E2 = spec("In Jer 29:13 ('You will seek me and find me') and Isa 55:6 ('Seek the Lord while he may be found') the seeking comes before the finding, and in 1Chr 28:9 the finding is conditional: 'If you seek him, he will be found by you'. "
          "Isa 65:1 gives the finding to 'those who did not seek me'.",
          [{"occurrence": 1340033, "strong": "H1245", "role": "characteristic"}, {"occurrence": 1340034, "strong": "H4672", "role": "qualifier", "supports": 1340033},
           {"occurrence": 1303056, "strong": "H1875", "role": "characteristic"}, {"occurrence": 1303058, "strong": "H4672", "role": "qualifier", "supports": 1303056},
           {"occurrence": 1193140, "strong": "H1875", "role": "characteristic"}, {"occurrence": 1193141, "strong": "H4672", "role": "qualifier", "supports": 1193140},
           {"occurrence": 1302385, "strong": "H1245", "role": "characteristic"}, {"occurrence": 1302382, "strong": "H4672", "role": "qualifier", "supports": 1302385}])
e2 = step("create evidence E2 (seek before find)", lambda: va.create_observation(
    cfg, conn, E2, "evidence", "states the order of seeking and finding in three verses, 1Chr 28:9 as a condition, and Isa 65:1 as the finding given without seeking: the clause type is in no node", RUN, WHO, serves=[7319, 7303]))
E3 = spec("Deut 31:21 states a knowing ahead: 'I know what they are inclined to do even today, before I have brought them into the land'; 'inclined' is H3336, the code of 'plan' in 1Chr 28:9.",
          [{"occurrence": q("SELECT verse_lexical_id FROM ib_node WHERE id=16651")[0][0], "strong": "H3336", "role": "characteristic"},
           {"occurrence": 1193137, "strong": "H3336", "role": "characteristic"}])
e3 = step("create evidence E3 (knowing ahead)", lambda: va.create_observation(
    cfg, conn, E3, "evidence", "states the timing of the knowing (before the people are brought into the land) and ties inclined to H3336, which no node holds", RUN, WHO, serves=[12413]))

# ── 5. restatements, each checked against the base data ────────────────────────────────────────────────────────
vt = lambda ref: q("SELECT text FROM verse WHERE osisId=? AND deleted=0", ref)[0][0].lower()
assert "knew all this" in vt("Dan.5.22") and "mind is stayed on you" in vt("Isa.26.3") and "perfect peace" in vt("Isa.26.3")
RS = {
 5797: ("In 1Chr 28:9 the codes M15, M36, M12, M47, M64, M06, M30, M18 and M34 stand in the verse with H1875 (M83), which occurs twice: as 'searches' and as 'seek'.",
        "each code read on the words of 1Chr.28.9 in verse_lexical (know, understands M15; serve M36; whole M12; heart, hearts, mind M47; plan M64; thought M06; forsake, off M30; willing M18; forever M34; searches, seek M83); M59 is on no word of the verse"),
 7317: ("Adjacent characteristics appear beside seeking: 'heart/mind' (M47) in 1Chr 22:19, 2Chr 15:12 and Ps 119:2; 'trust' (M19) and 'forsake' (M30, the opposite) in Ps 9:10; and 'forsake' (M30) in 1Chr 28:9. The verses are those the observation holds as nodes.",
         "M47 on a word of 1Chr.22.19, 2Chr.15.12, Ps.119.2; M19 and M30 on words of Ps.9.10; M30 on forsake in 1Chr.28.9, read in verse_lexical; the unquantified 'notable frequency' and the two cited verses with no node are taken out"),
 7319: ("In Jer 29:13, Isa 55:6 and 1Chr 28:9 the seeking is stated before the finding, and in 1Chr 28:9 the finding is conditional: 'If you seek him, he will be found by you'.",
         "the three verses read in the verse table; 'invariably, never the reverse' is taken out because Isa 65:1 gives the finding to those who did not seek"),
 12413: ("God knows the inclination before the act: 'I know what they are inclined to do even today, before I have brought them into the land' (Deut 31:21); the Lord 'understands every plan' (1Chr 28:9).",
         "Deut 31:21 and 1Chr 28:9 read in the verse table; 'before it acts' is stated by Deut 31:21, not by 1Chr 28:9"),
 12431: ("The thoughts of people are open to God and to Jesus: God discerns, knows and understands them (Ps 139:2; 1Chr 28:9; Isa 66:18), Jesus perceives them (Luke 5:22; Matt 9:4), and the word of God discerns them (Heb 4:12); the speaker of Ps 139:23 asks God to know his thoughts.",
         "each verse read in the verse table for its subject and verb; Ps 139:23 is a petition and the subject of Heb 4:12 is the word of God"),
 17167: ("God's rejection of the one who forsakes him: 'if you forsake him, he will cast you off forever' (1Ch 28:9).",
         "1Chr.28.9 read in the verse table; the title promised a non-rejection the verse does not state"),
 20216: ("Knowing is not enough. Belshazzar 'knew all this' and did not humble his heart (Dan 5:22); God 'understands every plan' (1Chr 28:9).",
         "Dan 5:22 and 1Chr 28:9 read in the verse table; the references to 'the plan set' and 'the will set' and the claim that knowing does not move the will go beyond the two verses and are taken out"),
 20549: ("The inclination, searched and stayed: in 1Chr 28:9 the Lord 'searches all hearts' and understands 'every plan'; in Isa 26:3 the mind 'stayed' on God is kept in 'perfect peace'. What the inclination rests on decides its peace (Isa 26:3).",
         "1Chr 28:9 and Isa 26:3 read in the verse table; 'kept forever toward you' is 1Chr 29:18, and in 1Chr 28:9 'forever' is the casting off"),
}
for oid, (txt, chk) in RS.items():
    step(f"restate #{oid}", lambda oid=oid, txt=txt, chk=chk: va.restate(cfg, conn, oid, txt, chk, "the wording did not match the base data as it stood", RUN, WHO))


def outline(oid, pattern, replacement=""):
    o = q("SELECT obs_text FROM ib_observation WHERE id=? AND deleted=0", oid)
    if not o:
        raise orec.Refused(f"{oid} not live")
    new = re.sub(pattern, replacement, o[0][0], count=1).strip()
    return va.restate(cfg, conn, oid, new, f"compared with the old wording character by character: only the numbering of the earlier document ({pattern}) is taken out", "the outline number of the earlier document is not part of the finding", RUN, WHO)


# #17270 keeps its number until the heart collection splits it (its text holds renderings in double quotes that are not ESV quotations)
for oid, pat in ((16318, r"^4\.1 "), (17057, r"^2\.2 "), (17271, r"^3\.1 "), (20019, r"^3\.9 ")):
    step(f"outline strip #{oid}", lambda oid=oid, pat=pat: outline(oid, pat))
step("strip [*soul*] gloss #16318", lambda: outline(16318, r"\s*\[\*soul\*\]"))
# #17012 quotes 1Ch 28:9 as 'willing [delighting] soul [nephesh]': the ESV reads 'willing mind' (the word is nephesh)
t = q("SELECT obs_text FROM ib_observation WHERE id=17012")[0][0]
t = re.sub(r"^1\.4 ", "", t).replace(" [H1]", "")
bad = '"serve him with a whole heart and with a willing [delighting] soul [*nephesh*]" (1Ch 28:9)'
assert bad in t
t = t.replace(bad, '"serve him with a whole heart and with a willing mind" (1Ch 28:9, where the word rendered mind is nephesh, soul)')
step("restate #17012 (the 1Ch 28:9 quotation made the ESV's, the document marks out)", lambda: va.restate(
    cfg, conn, 17012, t, "1Chr.28.9 read in the verse table: the ESV has 'a willing mind', and the word is H5315G nephesh; the editorial brackets, the document mark [H1] and the outline number are taken out", "the quotation was not the ESV's wording", RUN, WHO))

t = q("SELECT obs_text FROM ib_observation WHERE id=22623")[0][0]
t2 = t.replace("'Do' is the partner in ten:", "'Do' is the partner in nine verses (ten words, two of them in Num 33:56):").replace(
    "'service' is 2 words after in Joh 16:2", "'serve' is 12 words before in 1Ch 28:9, 'service' is 2 words after in Joh 16:2")
assert t2 != t and "12 words before in 1Ch 28:9" in t2
step("restate #22623 (count and the omitted serve)", lambda: va.restate(
    cfg, conn, 22623, t2, "the verses listed with 'do' counted (nine) against the layer-2 statement #22361; serve is word 6 and thought word 18 in verse_lexical, so 12 before", "the count did not match the verses it names and 1Chr.28.9 serve was dropped though its node is held", RUN, WHO))

# ── 6. the inner-being observation split off #5797; its trace ─────────────────────────────────────────────────────
S5797 = spec("In 1Chr 28:9 the verb darash stands twice: the Lord searches all hearts, and the one addressed is to seek him; the searching of the heart by God and the seeking of God by a person are set in one verse.",
             [{"occurrence": 1193130, "strong": "H1875", "role": "characteristic"}, {"occurrence": 1193140, "strong": "H1875", "role": "characteristic"},
              {"occurrence": 1193133, "strong": "H3824", "role": "object"}])
step("create inner being from #5797 (mirrored darash)", lambda: va.create_observation(
    cfg, conn, S5797, "inner_being", "the 'relational spine' sentence split off the evidence row #5797: the two uses of one verb as God searching the heart and a person seeking God", RUN, WHO, traces=[5797]))

# ── 7. consumptions (verified by the function before anything changes) ────────────────────────────────────────────
step("consume #7320 into #7319", lambda: va.consume(
    cfg, conn, 7320, [7319], "#7320 says the finding in 1Chr 28:9 is conditioned on the seeking ('If you seek him, he will be found'); #7319 as restated states the same condition; 'covenantal' is not in the verse and is not carried", RUN, WHO))
step("consume #22524 into #22604", lambda: va.consume(
    cfg, conn, 22524, [22604], "#22524 says the heart or mind stands with the thought in ten verses and the verses place it there; #22604 says the same of the supposition with the same ten verses and adds the Isa 10:7 contrast", RUN, WHO))
step("consume #22525 into #22608", lambda: va.consume(
    cfg, conn, 22525, [22608], "#22525 says knowing stands with the thought in thirteen verses, held, lacking or known by another; #22608 says the same of the supposition with the same verses and gives the ties", RUN, WHO))

# ── 8. the compound observations ────────────────────────────────────────────────────────────────────────────────
# 20455: claim 1 (1Cor 2:11) stays; claim 2 (God and Jesus know thoughts) is carried by E1 and #12431: nodes dropped when carried, else moved to #12431
if e1:
    E1ID = e1["observation"]
    t = q("SELECT obs_text FROM ib_observation WHERE id=20455")[0][0]
    cut = t.index(" Separately, God searches")
    keep = re.sub(r"^4\. ", "", t[:cut]).strip()
    cav = t[t.index(": *Caveat:*"):].replace('"the things of a person."', "'the things of a person.'")   # the Greek rendering, not an ESV quotation
    step("restate #20455 to its first claim", lambda: va.restate(
        cfg, conn, 20455, keep + cav, "1Cor 2:11 read in the verse table (no one knows a person's thoughts except the spirit of that person); the second claim, that God and Jesus know thoughts, is carried by the evidence observation " + str(E1ID) + " and #12431", "the observation held two findings (one finding per observation)", RUN, WHO))
    for nid, ref, occ in q("SELECT id, verse_reference, verse_lexical_id FROM ib_node WHERE observation_id=20455 AND deleted=0 AND verse_reference<>'1Cor.2.11'"):
        r = step(f"20455 node {nid} {ref}: drop if carried", lambda nid=nid: va.drop_node(conn, nid, [E1ID, 12431], "the second claim of #20455 is carried by the evidence and #12431", RUN, WHO))
        if r is None:
            step(f"20455 node {nid} {ref}: move to #12431", lambda nid=nid: va.move_node(cfg, conn, nid, 12431, "the word belongs to the claim that God and Jesus know thoughts, now #12431", RUN, WHO))
    # 20498: claim 1 consumed; reckons, overrules, turns toward God stay as one finding about the relation
    t = q("SELECT obs_text FROM ib_observation WHERE id=20498")[0][0]
    new = ("The relation between God's thinking and human thinking runs both ways. God reckons (Gen 15:6; Ps 32:2) and overrules: " + t[t.index('"you meant evil'):])
    new = new.replace(".; ", ". ")
    step("restate #20498 to the relation", lambda: va.restate(
        cfg, conn, 20498, new.strip(), "Gen 15:6, Ps 32:2, Gen 50:20, Prov 19:21 and Ps 119:59 read in the verse table; the first claim, that God searches, knows and discerns thoughts, is carried by the evidence " + str(E1ID) + " and #12431", "the observation held four findings; the first is #12431's", RUN, WHO))
    for nid in (68928, 68929, 68930, 68931):
        step(f"20498 node {nid}: drop (carried)", lambda nid=nid: va.drop_node(conn, nid, [E1ID, 12431], "the first claim of #20498 is carried by the evidence and #12431", RUN, WHO))
    step("20498 add node Gen.15.6 counted", lambda: va.add_word_node(cfg, conn, 20498, 997396, "H2803H", "qualifier", "God's reckoning in the text has no node", RUN, WHO))
    step("20498 add node Ps.32.2 counts", lambda: va.add_word_node(cfg, conn, 20498, 1263193, "H2803H", "qualifier", "God's reckoning in the text has no node", RUN, WHO))
    # 20489: claim 6 (fully open to God) carried; the five others deferred to the collections their nodes carry
    t = q("SELECT obs_text FROM ib_observation WHERE id=20489")[0][0]
    cut = t.index("Fully open to God.")
    new = re.sub(r"^9\.2 ", "", t[:cut].rstrip("; ").rstrip()).strip()
    step("restate #20489 without the claim that is carried", lambda: va.restate(
        cfg, conn, 20489, new, "the last claim ('fully open to God') is the meaning of #12431 and the evidence " + str(E1ID) + "; its text and nodes are taken out; the remaining claims are unchanged", "the observation held six findings; the sixth is carried", RUN, WHO))
    CLAIM6 = ("Ps.139.2", "Ps.139.23", "1Chr.28.9", "Isa.66.18", "Heb.4.12", "Luke.5.22", "Luke.6.8", "Luke.11.17", "Matt.9.4", "Matt.12.25")
    for nid, ref, occ, sf in q("SELECT id, verse_reference, verse_lexical_id, surface FROM ib_node WHERE observation_id=20489 AND deleted=0 AND traced_observation_id IS NULL"):
        if ref not in CLAIM6:
            continue
        why = ("the first 'know' of 1Chr 28:9 is Solomon's knowing God, not God's knowing; the word is held by #19501 where it belongs" if ref == "1Chr.28.9" else "the claim is carried by the evidence and #12431")
        carriers = [19501] if ref == "1Chr.28.9" else [E1ID, 12431]
        r = step(f"20489 node {nid} {ref} {sf}: drop (carried)", lambda nid=nid, carriers=carriers, why=why: va.drop_node(conn, nid, carriers, why, RUN, WHO))
        if r is None:   # a 'know' that is not about the thoughts: no carrier holds it and no finding of the observation uses it
            step(f"20489 node {nid} {ref} {sf}: drop (unrelated)", lambda nid=nid, sf=sf, ref=ref: va.drop_unrelated_node(
                conn, nid, f"the word '{sf}' of {ref} is a 'know' of another clause (not of the thoughts) and supports none of the findings left in the observation", RUN, WHO))

# 20549: 'forever' of 1Chr 28:9 no longer supports the text; the nodes for the words now relied on
step("20549 drop node 'forever' (carried by #17167)", lambda: va.drop_node(conn, 69215, [17167], "in 1Chr 28:9 forever is the casting off, which #17167 carries; it does not support the restated text", RUN, WHO))
step("20549 add node searches", lambda: va.add_word_node(cfg, conn, 20549, 1193130, "H1875", "qualifier", "the restated text relies on the searching", RUN, WHO))
step("20549 add node plan", lambda: va.add_word_node(cfg, conn, 20549, 1193137, "H3336", "characteristic", "the restated text relies on the plan (the inclination)", RUN, WHO))

# ── 9. traces (IB-07) ──────────────────────────────────────────────────────────────────────────────────────────────
step("trace #20019 -> #12412", lambda: va.add_trace(conn, 20019, 12412, "the evidence that H3336 is the plan of 1Chr 28:9, the intention of Gen 6:5 and 8:21 and the frame of Ps 103:14", RUN, WHO))
step("trace #17271 -> #17270", lambda: va.add_trace(conn, 17271, 17270, "the labelled reading rests on the parallels of #17270 and no longer carries a copy of their nodes", RUN, WHO))
for oid, why in ((19501, "quotes the clause of 1Chr 28:9 it relies on and holds a node for each of the eleven words (know, serve, whole, heart, willing, mind, searches, hearts, understands, plan, thought)"),
                 (20549, "quotes 1Chr 28:9 and Isa 26:3 and holds a node for each word it relies on (searches, plan, peace, stayed)"),
                 (20216, "quotes Dan 5:22 and 1Chr 28:9 and holds a node for each word it relies on (heart, knew, heart, understands, plan)"),
                 (20455, "quotes 1Cor 2:11 and holds a node for each word it relies on (knows, spirit, Spirit)"),
                 (20498, "quotes Gen 50:20, Prov 19:21 and Ps 119:59 and holds a node for each word it relies on (counted, counts, meant, evil, purpose, think, ways)")):
    step(f"self-evidencing #{oid}", lambda oid=oid, why=why: va.mark_self_evidencing(conn, oid, why, RUN, WHO))

# ── 10. deferrals to the collections that will touch the observation ───────────────────────────────────────────────
DEF = [(156, [5793, 5797, 7091, 7303, 7317, 7319], "the search collection's validation checks the sense of seek and searches (including the 'base cultic-consultation sense' of #5793 against the meaning tree) and whether these are carried by its own observations"),
       (156, [21752], "restate to the verses held as nodes and trace it to evidence: the favour, mercy, rest and enjoyment verses it names are the search collection's"),
       (156, [21757], "the 78 verses of the other nodes are read by the search collection, which then traces it"),
       (78, [12412, 12413, 20019, 20549], "the intend collection's validation checks whether its observations carry the plan (H3336) findings"),
       (47, [17167, 19508], "the forsake collection's validation checks whether its observations carry the casting off and the condition"),
       (24, [16318, 19501], "the serve collection's validation checks whether its observations carry the serving with the whole heart"),
       (9, [17012], "the desire collection's validation checks whether its observations carry the willing heart and the freewill"),
       (102, [17057, 17270, 17271], "the heart collection's validation splits the parallels (heart, spirit, soul, mind) into one finding each and checks consumption"),
       (184, [20489], "split off the design claim (H2803G, skilled work) into its own observation, with its nodes"),
       (201, [20489], "split off the reckoning claims (H2803H, count) into their own observation, with their nodes"),
       (102, [20489], "split off the inner-speech claims (Ps 10:4, 1Sam 1:13, Rom 2:15) into their own observation"),
       (2, [20489], "split off the claims of the body and emotions (Dan 5:6, Ps 94:19) into their own observation"),
       (78, [20489], "split off the claims of the creaturely and passing (Ps 94:11, Ps 146:4, Eccl 2:22, 4:16) into their own observation")]
for cid, oids, finding in DEF:
    for oid in oids:
        step(f"defer #{oid} to collection {cid}", lambda oid=oid, cid=cid, finding=finding: va.defer(conn, oid, cid, finding, RUN, WHO))

# ── 11. the 26 deleted observations with no recorded reason: note updated (they stay deleted) ────────────────────────
NOTE = ("Deleted before delete records were kept; the reason was not recorded. Confirmed by the researcher on 2026-11-22 to stay deleted. "
        "A trace that points here is handled by the validation.")
dead = [r[0] for r in q("SELECT DISTINCT o.id FROM ib_observation o JOIN ib_node n ON n.traced_observation_id=o.id AND n.deleted=0 WHERE o.deleted=1 "
                        "AND NOT EXISTS (SELECT 1 FROM ib_observation_change c WHERE c.observation_id=o.id AND c.column_name='deleted')")]
print(f"deleted observations traced by a live node with no recorded delete: {len(dead)} (the researcher named 26)")
for oid in dead:
    step(f"annotate deleted #{oid}", lambda oid=oid: va.annotate(conn, oid, NOTE, RUN, WHO))

# ── 11b. empty collection on a word node: the surface's own collection where it has one (B:130), else the reason ───────────────
for oid in [i for i in IDS if q("SELECT deleted FROM ib_observation WHERE id=?", i)[0][0] == 0]:
    for nid, sf in q("SELECT id, surface FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND collection_id IS NULL", oid):
        own = orec.surface_collection_map(conn).get((sf or "").strip().lower())
        if own:
            step(f"collection #{oid} node {nid} {sf} -> {own}", lambda nid=nid, own=own: va.complete_node(cfg, conn, nid, None, own, "the collection is the one the surface belongs to (B:130)", RUN, WHO))
        else:
            step(f"collection #{oid} node {nid} {sf}: reason", lambda nid=nid, sf=sf: va.note_node(
                conn, nid, f"the surface '{sf}' belongs to no single live collection by the member rule (B:130), so the collection stays empty", RUN, WHO))

conn.commit()

# ── 12. completeness over the 55 and what the actions created ───────────────────────────────────────────────────────
new = [r[0] for r in q("SELECT DISTINCT observation_id FROM ib_observation_change WHERE run_id=? AND column_name='created' AND node_id IS NULL", RUN)]
allids = sorted(set(IDS) | set(new))
live = [i for i in allids if q("SELECT deleted FROM ib_observation WHERE id=?", i)[0][0] == 0]
gaps = va.trace_gaps(conn, live)
print("\n── result ──")
print("observations in the set:", len(IDS), "| created by the actions:", new, "| live now:", len(live))
print("deleted now:", [i for i in allids if i not in live])
from collections import Counter
print("nature of the live set:", Counter(q("SELECT nature FROM ib_observation WHERE id=?", i)[0][0] for i in live))
print("inner-being with no trace to evidence and not self-evidencing:", gaps["no_trace"], "| traced to evidence not yet marked (the marking of its own scope is to come):", gaps["pending"])
print("live traces pointing at a deleted observation:", gaps["dead_trace"])
defd = {i for c in (156, 78, 47, 24, 9, 102, 184, 201, 2) for i in [d["observation"] for d in va.deferrals_to(conn, c)]}
print("of the gaps, deferred to a named collection:", [i for i in gaps["no_trace"] if i in defd], "| open:", [i for i in gaps["no_trace"] if i not in defd])
print("word nodes of the live set missing role:", q("SELECT count(*) FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND role IS NULL AND observation_id IN (%s)" % ",".join(map(str, live)))[0][0])
print("word nodes of the live set missing collection:", q("SELECT count(*) FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND collection_id IS NULL AND observation_id IN (%s)" % ",".join(map(str, live)))[0][0])
print("changes logged by this run:", q("SELECT count(*) FROM ib_observation_change WHERE run_id=?", RUN)[0][0])
print("steps:", Counter(s[1] for s in LOG))
(S / "log.json").write_text(json.dumps(LOG, ensure_ascii=False, indent=1), encoding="utf-8")
(S / "sheet.json").write_text(json.dumps({"collection": "thought", "verse": "1Chr.28.9", "actions": SHEET}, ensure_ascii=False, indent=1), encoding="utf-8")
print("sheet:", len(SHEET), "actions ->", S / "sheet.json")
if len(sys.argv) > 2:
    conn.commit()
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")      # the copy is a plain file: the write-ahead log is folded in first
    shutil.copy(DB, sys.argv[2])
    print("copy kept at", sys.argv[2])
