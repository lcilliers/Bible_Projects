"""TEMPORARY (#2219 test plan, section 9 of iba/docs/2172-strand-reading-test-plan-v1-20261022.md). Run:
    python iba/app/tools/temp_2219_strand_items_test_run.py <scratch folder>
against a dbsnapshot copy of iba.db in the scratch folder; live iba.db and live files are never written.
#2219 option A: open items matched by Context and answered before close, raised by Record, Map and
Derive on the strand's own thread. The word family is real; every reading and item is made up."""
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

S = pathlib.Path(sys.argv[1]) / "t5"
if S.exists():
    shutil.rmtree(S)
S.mkdir()
DB = copy_db(S / "iba.db")
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='strand_reading.output_dir'", (json.dumps(str(S / "strands")),))
c.commit()
has_items = c.execute("SELECT 1 FROM sqlite_master WHERE name='reading_strand_item'").fetchone()
c.close()
if not has_items:
    subprocess.run([sys.executable, str(ROOT / "iba/app/migration/strand_items_2219_v1_20261022.py"), "--db", str(DB)],
                   check=True, capture_output=True)
print(f"copy of the live database; #2219 migration {'live' if has_items else 'applied to the copy'}")

cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg)
results = []
WORD, CODE, ESC = "G0022", "items-strand", 2219


def W(step):
    return nr.Writer(conn, f"strand_reading.{step}", "Claude")


def count(sql, *a):
    return conn.execute(sql, a).fetchone()[0]


def jf(name, obj):
    p = S / f"{name}.json"
    p.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
    return str(p)


def P(**kw):
    return {"Strand": CODE, **kw}


def res(name, good, detail=""):
    results.append((name, "PASS" if good else "FAIL", str(detail)[:260].replace("\n", " ")))


def refused(name, fn, text):
    before = (count("SELECT COUNT(*) FROM escalation_thread_item"), count("SELECT COUNT(*) FROM reading_strand_item"),
              count("SELECT COUNT(*) FROM ib_observation"))
    try:
        fn()
        res(name, False, "not refused")
    except nr.Refused as exc:
        after = (count("SELECT COUNT(*) FROM escalation_thread_item"), count("SELECT COUNT(*) FROM reading_strand_item"),
                 count("SELECT COUNT(*) FROM ib_observation"))
        res(name, text in str(exc) and before == after, f"{'nothing written' if before == after else 'ROWS WRITTEN'}: {exc}")


def unanswered(sid):
    return sr.account_gaps(conn, sid)["open items matched and not answered"]


def gate_refuses():
    try:
        esc._check_requirements(db, "update", originator="Claude", checked_action=None,
                                values={"state": "completed", "type": "issue"}, self_id=ESC)
        return None
    except ValueError as exc:
        return str(exc)


# A. the shared matcher (Escalation.ps1 Match and Context)
lines = esc.match_threads(cfg, db, clusters=["T3"])
res("A1 match: a T cluster item is found (T3, OT-108.13)", any("OT-108" in x and "T3" in x for x in lines), lines[:1])
lines = esc.match_threads(cfg, db, clusters=["M64"])
res("A2 match: an M cluster item is found as before (M64, OT-108.3)", any("OT-108" in x and "M64" in x for x in lines),
    lines[:1])

# B. Context records the matched items
sr.define(cfg, W("define"), P(Strongs=WORD, Title="Items test strand", Cluster="M01", Escalation=str(ESC)))
s = sr.strand(conn, CODE)
sr.refresh_hits(conn, W("context"), s)
h0 = conn.execute("SELECT v.reference, v.osisId, h.verse_id FROM reading_strand_hit h JOIN verse v ON v.id=h.verse_id "
                  "WHERE h.strand_id=? ORDER BY v.id LIMIT 1", (s["id"],)).fetchone()
chapter = h0["reference"].rsplit(":", 1)[0]
word_clusters = [r[0] for r in conn.execute("SELECT cluster_code FROM cluster_strong WHERE strong=? AND "
                                             "COALESCE(deleted,0)=0 AND cluster_code<>'M01'", (WORD,))]
other = word_clusters[0] if word_clusters else None
items = [("strong", "G22", "base code, unpadded"), ("verse", chapter, "a chapter holding a hit"),
         ("strand", CODE, "the strand by its code"), ("strong", "G9999", "not the strand's"),
         ("verse", "Gen 1:1", "not a hit")] + ([("cluster", other, "a cluster the word sits in")] if other else [])
tid = esc.raise_new(cfg, db, "Test thread for strand items", "test", "thread", comment="test",
                    resolution_kind="self_correctable", originator="Claude", comes_back_when="test", items=items)
talias = esc._current(db, tid)["alias"]
# a response made before the item is matched does not answer it
esc.update(cfg, db, tid, item_refs=["1"], response_kind="note", respond="an earlier note", originator="Claude")
conn.execute("UPDATE escalation_thread_item_response SET responded_at='2020-01-01T00:00:00Z' WHERE escalation_id=?",
             (tid,))
out = hs.context(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-C1", word="", word_id=None, params=P(By="Claude"),
                     step_id="strand_reading.context"))
mine = conn.execute("SELECT i.kind, i.value FROM reading_strand_item ri JOIN escalation_thread_item i ON i.id=ri.item_id "
                    "WHERE ri.strand_id=? AND ri.source='matched' AND i.escalation_id=?", (s["id"], tid)).fetchall()
want = {("strong", "G22"), ("verse", chapter), ("strand", CODE)} | ({("cluster", other)} if other else set())
res(f"B1 context: matches by base code, chapter, strand code{', the word cluster ' + other if other else ''}; "
    f"not the others", {(r[0], r[1]) for r in mine} == want, [tuple(r) for r in mine])
n_all = count("SELECT COUNT(*) FROM reading_strand_item WHERE strand_id=?", s["id"])
out = hs.context(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-C2", word="", word_id=None, params=P(By="Claude"),
                     step_id="strand_reading.context"))      # its report is the live one (the first is archived)
res("B2 context: a second run records nothing again", count("SELECT COUNT(*) FROM reading_strand_item WHERE strand_id=?",
                                                            s["id"]) == n_all, n_all)
rep = pathlib.Path(out.counts.get("path") or "")
text = rep.read_text(encoding="utf-8") if rep.is_file() else ""
res("B3 context report: the items to answer, each 'not yet'", "## Open items to answer" in text and
    f"{talias}.1 strong:G22" in text and "**not yet**" in text, out.message)

# C. answering, and the gate
un = unanswered(s["id"])
res("C1 account: every matched item unanswered, the earlier note not counted", f"{talias}.1" in un and len(un) == n_all, un[:6])
g = gate_refuses()
res("C2 gate: close refused while matched items are unanswered", g is not None and "open items matched and not answered"
    in (g or ""), g)
esc.update(cfg, db, tid, item_refs=["1"], response_kind="touched", respond="taken into account", via=ESC,
           originator="Claude")
un2 = unanswered(s["id"])
res("C3 a touched response answers that item only", f"{talias}.1" not in un2 and len(un2) == n_all - 1, un2[:6])
for r in [r for r in sr.strand_items(conn, s["id"]) if r["source"] == "matched" and not r["answer"]]:
    t = conn.execute("SELECT escalation_id FROM escalation_thread_item WHERE id=?", (r["item_id"],)).fetchone()[0]
    esc.update(cfg, db, t, item_refs=[str(r["item_no"])], response_kind="closed" if t == tid else "note",
               respond="test answer", via=ESC, originator="Claude")
res("C4 every matched item answered: no item gap", unanswered(s["id"]) == [], unanswered(s["id"]))
g = gate_refuses()
res("C5 gate: the item gap no longer named (hits are still unread)", g is not None and "open items" not in
    (sr.gate_message(conn, ESC) or "") and "hits with no face" in (sr.gate_message(conn, ESC) or ""), sr.gate_message(conn, ESC))

# D. raising new items
refused("D1 record: an item that is not kind:value refused, nothing written", lambda: sr.record(cfg, W("record"), P(
    File=jf("r1", {"items": ["foo:bar :: x"]})), "RUN-T"), "needs kind:value")
refused("D2 record: a good item with a bad hit refused, no thread raised", lambda: sr.record(cfg, W("record"), P(
    File=jf("r2", {"items": ["verse:Rom 7:15 :: test open"], "hits": [{"verse": "Gen.1.22", "strong": WORD,
                                                                        "face": "A"}]})), "RUN-T"), "is not a hit")
m = sr.record(cfg, W("record"), P(File=jf("r3", {"items": ["verse:Rom 7:15 :: test open"]})), "RUN-TEST-R3")
s = sr.strand(conn, CODE)
st1 = s["thread_id"]
it = conn.execute("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND kind='verse' AND value='Rom 7:15'",
                  (st1 or 0,)).fetchone()
res("D3 record: item raised on the strand's own thread, linked as raised", st1 and it and esc._current(db, st1)["type"] ==
    "thread" and count("SELECT COUNT(*) FROM reading_strand_item WHERE strand_id=? AND item_id=? AND source='raised'",
                       s["id"], it["id"]) == 1, m)
m2 = sr.record(cfg, W("record"), P(File=jf("r4", {"items": ["verse:Rom 7:15 :: again"]})), "RUN-TEST-R4")
res("D4 record: the same item again is reused, not doubled", count(
    "SELECT COUNT(*) FROM escalation_thread_item WHERE escalation_id=? AND value='Rom 7:15'", st1) == 1 and
    f"{esc._current(db, st1)['alias']}.{it['item_no']}" in m2, m2)
res("D5 raised items are not gated", unanswered(s["id"]) == [], unanswered(s["id"]))
v0 = conn.execute("SELECT text FROM verse WHERE id=?", (h0["verse_id"],)).fetchone()[0]
sr.record(cfg, W("record"), P(File=jf("r5", {"observations": [
    {"key": "o1", "text": "A test observation.", "meaning": "test meaning", "basis": "read",
     "stable_key": "items-strand:T-01", "note": "October disposition: W",
     "verses": [{"verse": h0["osisId"], "strong": WORD}]}]})), "RUN-TEST-R5")
oid = conn.execute("SELECT id FROM ib_observation WHERE run_id='RUN-TEST-R5'").fetchone()[0]
res("D6a record: stable_key and note kept (#2172 catch-up)", tuple(conn.execute(
    "SELECT stable_key, revisit_note FROM ib_observation WHERE id=?", (oid,)).fetchone()) ==
    ("items-strand:T-01", "October disposition: W"), "")
refused("D6 derive: held with both an item and a new_item refused", lambda: sr.derive(cfg, W("derive"), P(File=jf("d1", {
    "dispositions": [{"observation": oid, "as": "held", "item": "#2172", "new_item": "verse:Rom 7:16 :: x"}]})), "RUN-T"),
    "one of them")
md = sr.derive(cfg, W("derive"), P(File=jf("d2", {"dispositions": [
    {"observation": oid, "as": "held", "new_item": "verse:Rom 7:16 :: held for the redo"}]})), "RUN-TEST-D2")
o = conn.execute("SELECT status, revisit_note FROM ib_observation WHERE id=?", (oid,)).fetchone()
it16 = conn.execute("SELECT item_no FROM escalation_thread_item WHERE escalation_id=? AND value='Rom 7:16'", (st1,)).fetchone()
res("D7 derive: held on a new item -- raised, observation open, note names it", it16 and o["status"] == "open" and
    o["revisit_note"] == f"held: {esc._current(db, st1)['alias']}.{it16[0]}", (md, dict(o)))
esc.update(cfg, db, st1, item_refs=["verse:Rom 7:15"], response_kind="closed", respond="test", originator="Claude")
sr.record(cfg, W("record"), P(File=jf("r6", {"items": ["verse:Rom 7:15 :: found again"]})), "RUN-TEST-R6")
res("D8 a settled item found again is reopened on the same thread", conn.execute(
    "SELECT status FROM escalation_thread_item WHERE escalation_id=? AND value='Rom 7:15'", (st1,)).fetchone()[0] == "open",
    "")
for r in esc._thread_items(db, st1, "open"):
    esc.update(cfg, db, st1, item_refs=[str(r["item_no"])], response_kind="closed", respond="test", originator="Claude")
done = esc._current(db, st1)["state"]
sr.record(cfg, W("record"), P(File=jf("r7", {"items": ["strong:G0022 :: after the thread completed"]})), "RUN-TEST-R7")
st2 = sr.strand(conn, CODE)["thread_id"]
res("D9 once the strand's thread completes, the next item opens a new thread", done == "completed" and st2 and st2 != st1
    and esc._current(db, st2)["state"] in ("on-hold", "in-progress"), (done, st1, st2))

# E. the account
lines, console = sr.account(cfg, P())
body = "\n".join(lines)
res("E1 account: items listed with source and answer", "## Open items" in body and "| matched |" in body and
    "| raised |" in body, console)
res("E2 account console: gated gaps counted, items not among them", console.startswith(f"{CODE}:"), console)

for r in results:
    print(" | ".join(str(x) for x in r))
print(f"\n{sum(r[1] == 'PASS' for r in results)} of {len(results)} pass")
