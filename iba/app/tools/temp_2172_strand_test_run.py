"""TEMPORARY (#2172 test plan, iba/docs/2172-strand-reading-test-plan-v1-20261022.md). Run:
    python iba/app/tools/temp_2172_strand_test_run.py <scratch folder>
against a dbsnapshot copy of iba.db in the scratch folder; live iba.db and live files are never written.
#2172 build steps 2-5 test: Strand-Reading (lib and handlers) and the close gate, on a dbsnapshot copy.
The word family is real (its hits come from verse_lexical); every reading in the JSON files is made up."""
import json
import pathlib
import shutil
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(r"C:\Bible_study_projects")
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import narrativeregister as nr  # noqa: E402
from iba.app.lib import strandreading as sr  # noqa: E402
from iba.app.lib import escalation as esc  # noqa: E402
from iba.app.handlers import strandreading as hs  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t4"
if S.exists():
    shutil.rmtree(S)
S.mkdir()
DB = copy_db(S / "iba.db")
print("copy of the live database (migrations already applied)")
live = sqlite3.connect(ROOT / "iba/app/db/iba.db")
src = ROOT / json.loads(live.execute("SELECT value FROM cfg_setting WHERE key='narrative.copy_source_dir'").fetchone()[0])
chap = S / "chapters"
chap.mkdir()
for (f,) in live.execute("SELECT current_file FROM narrative_chapter WHERE inactive=0 AND current_file IS NOT NULL"):
    shutil.copy2(src / f, chap / f)
c = sqlite3.connect(DB)
for key, val in (("narrative.copy_source_dir", str(chap)), ("narrative.claim_register_path", str(S / "out/register.md")),
                 ("narrative.claim_changes_path", str(S / "out/changes.md")),
                 ("narrative.citation_index_path", str(S / "out/citations.md")),
                 ("strand_reading.output_dir", str(S / "strands"))):
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val), key))
c.commit()
has_items = c.execute("SELECT 1 FROM sqlite_master WHERE name='reading_strand_item'").fetchone()
c.close()
if not has_items:      # #2219 under test before it is live: its migration applied to the copy
    subprocess.run([sys.executable, str(ROOT / "iba/app/migration/strand_items_2219_v1_20261022.py"), "--db", str(DB)],
                   check=True, capture_output=True)

cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg)
results = []
WORD = "G0022"            # a small real word family whose verses the narrative cites
CODE = "test-strand"
ESC = 2172


def W(step):
    return nr.Writer(conn, f"strand_reading.{step}", "Claude")    # an open item's raiser is Claude|Researcher (#2219)


def count(sql, *a):
    return conn.execute(sql, a).fetchone()[0]


def snap():
    return tuple(count(f"SELECT COUNT(*) FROM {t}") for t in (
        "ib_observation", "ib_node", "narrative_claim", "narrative_claim_telling", "narrative_claim_source",
        "narrative_update")) + (count("SELECT COUNT(*) FROM reading_strand_hit WHERE face IS NOT NULL OR reason IS NOT NULL"),)


def case(name, fn, refused=None, check=None):
    before = snap()
    try:
        out = fn()
        good = refused is None and (check is None or check(out))
        detail = str(out)[:260]
    except nr.Refused as exc:
        same = snap() == before
        good = refused is not None and refused in str(exc) and same
        detail = f"Refused{' (nothing written)' if same else ' BUT ROWS WRITTEN'}: {str(exc)[:240]}"
    results.append((name, "PASS" if good else "FAIL", detail.replace("\n", " ")))


def jf(name, obj):
    p = S / f"{name}.json"
    p.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
    return str(p)


def P(**kw):
    return {"Strand": CODE, **kw}


# Define
case("define: new strand needs title, cluster, escalation", lambda: sr.define(cfg, W("define"), P(Strongs=WORD)), "needs")
case("define: a code not in verse_lexical refused", lambda: sr.define(cfg, W("define"), P(
    Strongs="H9999Z", Title="t", Cluster="M01", Escalation="2172")), "no live verse_lexical")
case("define: new strand", lambda: sr.define(cfg, W("define"), P(Strongs=WORD, Title="Test strand", Cluster="M01",
                                                                 Escalation=str(ESC))))
case("define: a word added again is not doubled", lambda: sr.define(cfg, W("define"), P(Strongs=WORD)),
     check=lambda o: "0 word(s) added" in o)
s = sr.strand(conn, CODE)

# 1 Context (through the handler: it writes the report)
ctx = Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-CONTEXT", word="", word_id=None,
          params=P(By="Claude"), step_id="strand_reading.context")
out = hs.context(ctx)
n_occ = count("SELECT COUNT(*) FROM (SELECT DISTINCT verse_id, strong FROM verse_lexical WHERE strong=? AND deleted=0)", WORD)
hits = conn.execute("SELECT h.*, v.osisId, v.reference FROM reading_strand_hit h JOIN verse v ON v.id=h.verse_id WHERE "
                    "h.strand_id=? ORDER BY h.id", (s["id"],)).fetchall()
results.append(("context: one hit per live occurrence", "PASS" if out.condition == "ok" and len(hits) == n_occ else "FAIL",
                f"{len(hits)} hits / {n_occ} occurrences; {out.message[:160]}"))
results.append(("context: report written", "PASS" if out.counts.get("path") and pathlib.Path(out.counts["path"]).is_file()
                else "FAIL", str(out.counts.get("path"))))
out2 = hs.context(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-CONTEXT2", word="", word_id=None, params=P(By="Claude"),
                      step_id="strand_reading.context"))
results.append(("context: a second run adds no hit", "PASS" if count("SELECT COUNT(*) FROM reading_strand_hit WHERE strand_id=?",
                                                                       s["id"]) == n_occ else "FAIL", ""))
results.append(("context: without -By refused", "PASS" if hs.context(Ctx(db=db, cfg=cfg, step=None, run_id="x", word="",
               word_id=None, params=P(), step_id="strand_reading.context")).condition == "refused" else "FAIL", ""))

# 2 Record
h0, h1 = hits[0], hits[1]
v0 = conn.execute("SELECT text FROM verse WHERE id=?", (h0["verse_id"],)).fetchone()[0]
q = " ".join(v0.split()[:5])
good_obs = {"key": "o1", "text": f'A test observation on "{q}".', "setting": "test setting", "meaning": "test meaning",
            "implication": "test implication", "basis": "read", "parties": "test parties",
            "verses": [{"verse": h0["osisId"], "strong": WORD}]}
case("record: a hit with a face and a reason refused", lambda: sr.record(cfg, W("record"), P(File=jf("r1", {
    "observations": [good_obs], "hits": [{"verse": h0["osisId"], "strong": WORD, "face": "A", "reason": "x"}]})), "RUN-T"),
    "one of them")
case("record: a hit not in the strand refused", lambda: sr.record(cfg, W("record"), P(File=jf("r2", {
    "hits": [{"verse": "Gen.1.22", "strong": WORD, "face": "A"}]})), "RUN-T"), "is not a hit")
case("record: a verse where the strong does not occur refused", lambda: sr.record(cfg, W("record"), P(File=jf("r3", {
    "observations": [{**good_obs, "verses": [{"verse": "Gen.1.22", "strong": WORD}]}]})), "RUN-T"), "no matching live")
case("record: no basis refused", lambda: sr.record(cfg, W("record"), P(File=jf("r4", {
    "observations": [{**good_obs, "basis": None}]})), "RUN-T"), "basis must be")
case("record: a quotation not in the text refused", lambda: sr.record(cfg, W("record"), P(File=jf("r5", {
    "observations": [{**good_obs, "meaning": 'it says "the lantern of brass and wool shines"'}]})), "RUN-T"),
    "not found in the ESV text")
case("record: observation and two hits", lambda: sr.record(cfg, W("record"), P(File=jf("r6", {
    "observations": [good_obs], "hits": [{"verse": h0["osisId"], "strong": WORD, "face": "A. A test face",
                                          "parties": "p", "observation": "o1"},
                                         {"verse": h1["reference"] or h1["osisId"], "strong": WORD,
                                          "reason": "another sense of the word"}]})), "RUN-TEST-R6"))
o = conn.execute("SELECT * FROM ib_observation WHERE run_id='RUN-TEST-R6'").fetchone()
results.append(("record: observation row with its parts", "PASS" if o and o["stage"] == "strand-reading" and
                o["tag"] == "key-statement" and o["meaning"] == "test meaning" and o["basis"] == "read" and
                o["status"] == "draft" else "FAIL", dict(o) if o else "-"))
results.append(("record: grounded in ib_node", "PASS" if o and count(
    "SELECT COUNT(*) FROM ib_node WHERE observation_id=? AND verse_reference=? AND strong=?", o["id"], h0["osisId"], WORD) == 1
    else "FAIL", ""))
results.append(("record: hits faced / reasoned, linked", "PASS" if count(
    "SELECT COUNT(*) FROM reading_strand_hit WHERE id=? AND face='A. A test face' AND observation_id=?", h0["id"], o["id"]) == 1
    and count("SELECT COUNT(*) FROM reading_strand_hit WHERE id=? AND reason IS NOT NULL", h1["id"]) == 1 else "FAIL", ""))
results.append(("record: read verses analysed", "PASS" if count(
    "SELECT COUNT(*) FROM verse_meta WHERE verse_id IN (?,?) AND status IN ('analysed','citated')", h0["verse_id"],
    h1["verse_id"]) == len({h0["verse_id"], h1["verse_id"]}) else "FAIL", ""))
case("record: supersedes withdraws the earlier row", lambda: sr.record(cfg, W("record"), P(File=jf("r7", {
    "observations": [{**good_obs, "key": "o2", "text": "A corrected test observation.", "supersedes": o["id"]}]})),
    "RUN-TEST-R7"), check=lambda _: count("SELECT COUNT(*) FROM ib_observation WHERE id=? AND status='withdrawn'", o["id"]) == 1)
o2 = conn.execute("SELECT * FROM ib_observation WHERE run_id='RUN-TEST-R7'").fetchone()

# 7 Account and the gate, with gaps open
gaps = sr.account_gaps(conn, s["id"])
results.append(("account: unread hits and undisposed observations counted", "PASS" if
                len(gaps["hits with no face or reason"]) == n_occ - 2 and gaps["observations with no disposition"] ==
                [f"observation {o2['id']}"] else "FAIL", {k: len(v) for k, v in gaps.items()}))


def gate():
    esc._check_requirements(db, "update", originator="Claude", checked_action=None,
                            values={"state": "completed", "type": "task"}, self_id=ESC)
    return "passes"


try:
    gate()
    results.append(("gate: close refused while gaps are open", "FAIL", "it passed"))
except ValueError as exc:
    results.append(("gate: close refused while gaps are open", "PASS" if "strand test-strand" in str(exc) else "FAIL",
                    str(exc)[:200]))

# 3 Gather
lines, console = sr.gather(cfg, P())
related = sr.related_blocks(conn, s["id"])
results.append(("gather: related blocks listed", "PASS" if related and console.startswith(CODE) else "FAIL", console))
b_ids = sorted(related)
blocks = [conn.execute("SELECT s.*, ch.chapter_no, ps.heading parent FROM narrative_section s JOIN narrative_chapter ch "
                       "ON ch.id=s.chapter_id LEFT JOIN narrative_section ps ON ps.id=s.parent_section_id WHERE s.id=?",
                       (b,)).fetchone() for b in b_ids]


def spec(b):
    dup = count("SELECT COUNT(*) FROM narrative_section WHERE chapter_id=? AND heading=? AND last_version IS NULL",
                b["chapter_id"], b["heading"])
    return f"{b['parent']} > {b['heading']}" if dup > 1 else b["heading"]


def told(b):
    return [{"claim": r[0], "kind": r[1], "part": r[2] or ("test part" if r[1] == "in part" else None)}
            for r in conn.execute("SELECT c.claim_ref, t.kind, t.part_told FROM narrative_claim_telling t JOIN narrative_claim "
                                  "c ON c.id=t.claim_id WHERE t.section_id=? AND t.status='current'", (b["id"],))]


# 4 Map
vref = h0["reference"] or h0["osisId"]
mapping = {"blocks": [{"chapter": b["chapter_no"], "section": spec(b), "statements": (
    [{"text": "a statement", "claims": told(b)}] if told(b) else []) + [
    {"text": "an unclaimed statement", "item": "test: held for later"}]} for b in blocks]}
mapping["blocks"][0]["statements"].append({"text": "a new statement", "new_claim": {
    "text": "A test claim from the narrative.", "beyond_text": "test", "sources": [vref]}})
case("map: a related block left out refused", lambda: sr.map_blocks(cfg, W("map"), P(File=jf("m1", {
    "blocks": mapping["blocks"][1:]})) if len(blocks) > 1 else (_ for _ in ()).throw(nr.Refused("is related to the strand and not mapped"))),
    "not mapped")
case("map: a statement with no claim, new claim or item refused", lambda: sr.map_blocks(cfg, W("map"), P(File=jf("m2", {
    "blocks": [{**mapping["blocks"][0], "statements": [{"text": "bare"}]}] + mapping["blocks"][1:]}))), "give the statement")
mres = []
case("map: every block mapped", lambda: mres.append(sr.map_blocks(cfg, W("map"), P(File=jf("m3", mapping)))) or mres[-1])
new_ref = conn.execute("SELECT claim_ref FROM narrative_claim WHERE claim_text='A test claim from the narrative.'").fetchone()
results.append(("map: new claim added and told in its block", "PASS" if new_ref and count(
    "SELECT COUNT(*) FROM narrative_claim_telling t JOIN narrative_claim c ON c.id=t.claim_id WHERE c.claim_ref=? AND "
    "t.section_id=? AND t.status='current'", new_ref[0], blocks[0]["id"]) == 1 else "FAIL", new_ref[0] if new_ref else "-"))
raised = conn.execute("SELECT i.kind, i.value, i.note FROM reading_strand_item ri JOIN escalation_thread_item i ON "
                      "i.id=ri.item_id WHERE ri.strand_id=? AND ri.source='raised'", (s["id"],)).fetchall()
results.append(("map: held statements raised as open items on the strand's thread (#2219)", "PASS" if len(raised) ==
                len(blocks) and all(r["kind"] == "chapter" and r["note"] == "test: held for later" for r in raised) and
                conn.execute("SELECT thread_id FROM reading_strand WHERE id=?", (s["id"],)).fetchone()[0] else "FAIL",
                [dict(r) for r in raised[:1]]))

# 5 Derive
other = conn.execute("SELECT id FROM ib_observation WHERE status='draft' AND stage<>'strand-reading' LIMIT 1").fetchone()[0]
case("derive: an observation not the strand's refused", lambda: sr.derive(cfg, W("derive"), P(File=jf("d1", {
    "dispositions": [{"observation": other, "as": "silent", "reason": "x"}]})), "RUN-T"), "not one of the strand's")
case("derive: a new claim with no source refused", lambda: sr.derive(cfg, W("derive"), P(File=jf("d2", {
    "claims": [{"key": "n1", "new": {"text": "t", "beyond_text": "b"}}]})), "RUN-T"), "rests on at least one")
case("derive: held on an item that does not exist refused", lambda: sr.derive(cfg, W("derive"), P(File=jf("d3", {
    "dispositions": [{"observation": o2["id"], "as": "held", "item": "OT-999.9"}]})), "RUN-T"), "does not exist")
case("derive: new claim on the observation, disposed as carried", lambda: sr.derive(cfg, W("derive"), P(File=jf("d4", {
    "claims": [{"key": "n1", "new": {"text": "A derived test claim.", "beyond_text": "test", "observations": [o2["id"]]}},
               {"claim": new_ref[0], "withdraw": "test"}],
    "dispositions": [{"observation": o2["id"], "as": "claim", "claim": "n1"}]})), "RUN-TEST-D4"))
dc = conn.execute("SELECT * FROM narrative_claim WHERE claim_text='A derived test claim.'").fetchone()
results.append(("derive: observation source and status resolved", "PASS" if dc and count(
    "SELECT COUNT(*) FROM narrative_claim_source WHERE claim_id=? AND source_kind='observation' AND observation_id=?",
    dc["id"], o2["id"]) == 1 and count("SELECT COUNT(*) FROM ib_observation WHERE id=? AND status='resolved'", o2["id"]) == 1
    else "FAIL", ""))
results.append(("derive: claim withdrawn", "PASS" if count("SELECT COUNT(*) FROM narrative_claim WHERE claim_ref=? AND "
                                                           "status='withdrawn'", new_ref[0]) == 1 else "FAIL", ""))

# 6 Rewrite: block 0 tells the derived claim and drops the withdrawn one (accounted)
b0 = conn.execute("SELECT * FROM narrative_section WHERE id=?", (blocks[0]["id"],)).fetchone()
tells = [t for t in told(b0) if t["claim"] != new_ref[0]] + [{"claim": dc["claim_ref"], "kind": "in full"}]
case("rewrite: block rewritten, claims accounted, verses citated", lambda: sr.rewrite(cfg, W("rewrite"), P(File=jf("w1", {
    "update": {"update_date": "2026-10-22", "title": "test strand rewrite"},
    "blocks": [{"chapter": blocks[0]["chapter_no"], "section": spec(blocks[0]),
                "text": b0["block_text"].rstrip("\n") + "\n\nA test sentence.\n", "tells": tells,
                "accounts": [{"claim": new_ref[0], "as": "withdrawn"}]}]}))))
u = conn.execute("SELECT * FROM narrative_update WHERE title='test strand rewrite'").fetchone()
results.append(("rewrite: update names the strand and its escalation", "PASS" if u and u["strand"] == CODE and count(
    "SELECT COUNT(*) FROM narrative_update_ref WHERE update_id=? AND kind='escalation' AND value=?", u["id"], str(ESC)) == 1
    else "FAIL", ""))
results.append(("rewrite: cited verses citated", "PASS" if count(
    "SELECT COUNT(*) FROM verse_meta vm JOIN narrative_citation ci ON ci.verse_id=vm.verse_id WHERE ci.section_id=? AND "
    "ci.last_version IS NULL AND vm.status NOT IN ('citated','exclude')", b0["id"]) == 0 else "FAIL", ""))

# read the rest, then the gate passes
rest = conn.execute("SELECT h.*, v.osisId FROM reading_strand_hit h JOIN verse v ON v.id=h.verse_id WHERE h.strand_id=? AND "
                    "h.face IS NULL AND h.reason IS NULL", (s["id"],)).fetchall()
case("record: the remaining hits", lambda: sr.record(cfg, W("record"), P(File=jf("r8", {
    "hits": [{"verse": h["osisId"], "strong": WORD, "face": "B. Another test face"} for h in rest]})), "RUN-TEST-R8"))
for it in [r for r in sr.strand_items(conn, s["id"]) if r["source"] == "matched" and not r["answer"]]:   # #2219
    tid = conn.execute("SELECT escalation_id FROM escalation_thread_item WHERE id=?", (it["item_id"],)).fetchone()[0]
    esc.update(cfg, db, tid, item_refs=[str(it["item_no"])], response_kind="touched",
               respond="test: taken into account", originator="Claude")
try:
    results.append(("gate: close allowed once the account is clean", "PASS" if gate() == "passes" else "FAIL", ""))
except ValueError as exc:
    results.append(("gate: close allowed once the account is clean", "FAIL", str(exc)[:200]))
alines, aconsole = sr.account(cfg, P())
results.append(("account: report, no gated gap", "PASS" if aconsole.startswith(f"{CODE}: 0 gated") else "FAIL", aconsole))
lines, _ = nr.check(cfg, {})
results.append(("register check after the strand: files match, no double or dead tellings", "PASS" if not any(
    k in x for x in lines for k in ("differs from the database", "one per block", "no longer in the narrative",
                                    "heading line")) else "FAIL", ""))

for r in results:
    print(" | ".join(str(x) for x in r))
print(f"\n{sum(r[1] == 'PASS' for r in results)} of {len(results)} pass")
