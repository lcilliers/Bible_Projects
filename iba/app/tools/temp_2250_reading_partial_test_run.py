"""temp_2250_reading_partial_test_run.py -- tests for escalation #2250 option A: at gate 2 a matched open item
whose target reaches past the reading may be settled as `touched` (read in part) and stays open
(outputs/escalation/2250-gate2-partial-items-review-v1-20261023.md). The harness of
iba/app/tools/temp_2228_reading_test_run.py (the #2228 migration is live, so it is not re-applied): a copy of iba.db
made with lib/dbsnapshot.copy_db, the narrative folder, the inbox and the output folders redirected to the scratch
directory. The live database is not written.

Usage: python iba/app/tools/temp_2250_reading_partial_test_run.py <scratch dir>
"""
import json
import pathlib
import shutil
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import reading as rd  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2250"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
live = sqlite3.connect(ROOT / "iba/app/db/iba.db")
src = ROOT / json.loads(live.execute("SELECT value FROM cfg_setting WHERE key='narrative.copy_source_dir'").fetchone()[0])
chap = S / "chapters"
chap.mkdir()
for (f,) in live.execute("SELECT current_file FROM narrative_chapter WHERE inactive=0 AND current_file IS NOT NULL"):
    shutil.copy2(src / f, chap / f)
c = sqlite3.connect(DB)
for key, val in (("narrative.copy_source_dir", str(chap)), ("narrative.learning4comfort_inbox_dir", str(S / "inbox")),
                 ("narrative.claim_register_path", str(S / "out/register.md")),
                 ("narrative.claim_changes_path", str(S / "out/changes.md")),
                 ("narrative.citation_index_path", str(S / "out/citations.md")),
                 ("reading.output_dir", str(S / "reading")), ("open_item.output_dir", str(S / "open-items"))):
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val), key))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
from iba.app.handlers import reading as hr  # noqa: E402
results = []
LABEL, ESC = "t-part", 2172


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/").replace("\n", " ")[:500]))
    print(f"{cid} {'PASS' if passed else 'FAIL'}" + ("" if passed else f"  {str(evidence)[:700]}"), flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(step, **params):
    params.setdefault("By", "Claude")
    return getattr(hr, step)(Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None,
                                 params=params, step_id=f"reading.{step}"))


def item_status(ref):
    alias, no = ref.rsplit(".", 1)
    return q("SELECT i.status FROM escalation_thread_item i JOIN escalation e ON e.id=i.escalation_id WHERE e.alias=? "
             "AND i.item_no=?", alias, int(no))[0][0]


# ── set-up: Open, Record, gate 1, Synergy on the #2228 test scope ────────────────────────────────
o = run("open", Label=LABEL, Escalation=str(ESC), Home="M01", Verse="Mar 6:49; Mar 6:50; Psa 36:4")
gapfile = S / "reading" / LABEL / f"{LABEL}-gaps.json"
d = json.loads(gapfile.read_text(encoding="utf-8"))
for sec, s in d["sections"].items():
    for it in s["items"]:
        if sec in ("not_read", "read_in_files_only") and it["verse"] == "Mar 6:49":
            it["record"] = {"new": {"text": "Seeing him on the sea, \"they thought it was a ghost, and cried out\": the "
                                    "mind names what it cannot place, and fear follows the naming",
                                    "meaning": "the thought comes before the cry", "basis": "read",
                                    "verses": [{"verse": "Mar 6:49", "strong": "G1380"}]}}
        elif sec == "open_item":
            it["record"] = {"new": {"response": "read with Mar 6:50: the troubling is answered by his word"}}
        elif sec == "hit_unread":
            it["record"] = {"new": {"face": "A. Planning evil on his bed", "parties": "the wicked, alone"}}
        else:
            it["record"] = {"reason": "not needed for this test reading: the word is not read here"}
d["new_items"] = [{"thread": "OT-11", "origin": "1958", "anchor": "verse:Mar 6:50", "verse": "Mar 6:50",
                   "read_for": "the 'Take heart' words beside tarasso: courage given as the answer to trouble",
                   "why": "found in the test reading of #2250: the word of courage stands with the troubling",
                   "comes_back_when": "when M19 Trust and refuge is read"}]
fill = S / "fill.json"
fill.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
o1 = run("record", Label=LABEL, File=str(fill))
shutil.copy2(fill, gapfile)
d = json.loads(fill.read_text(encoding="utf-8"))
added = d["new_items"][0].get("added")
new_obs = [it["record"]["id"] for s in d["sections"].values() for it in s["items"]
           if (it.get("record") or {}).get("table") == "ib_observation"]
o2 = run("check", Label=LABEL)
o3 = run("synergy", Label=LABEL)
r = q("SELECT * FROM reading WHERE label=?", LABEL)[0]
syn_path = ROOT / r["synergy_file"]
syn = json.loads(syn_path.read_text(encoding="utf-8"))
items = [x["item"] for x in syn["open_items"]]
vids = rd.verse_ids(conn, r["id"])
past = {ref: rd._reaches_past(cfg, rd._thread_item(conn, ref)[1], vids) for ref in items}
case("P0", "set-up: opened, recorded, gate 1 passed, synergy built; OT-11.1 reaches past the 3 verses, the new item "
     "(Mar 6:50) lies inside", all(x.condition == "ok" for x in (o, o1, o2, o3)) and past.get("OT-11.1") is True
     and past.get(added) is False, f"{[x.message[:80] for x in (o, o1, o2, o3)]}; past {past}")


def synergy_with(settles, extra=None):
    s = json.loads(syn_path.read_text(encoding="utf-8"))
    blk = q("SELECT s.heading, ch.chapter_no FROM narrative_section s JOIN narrative_chapter ch ON ch.id=s.chapter_id "
            "AND ch.inactive=0 WHERE s.last_version IS NULL AND s.level>0 AND s.block_text IS NOT NULL ORDER BY "
            "ch.reading_order, s.ordinal LIMIT 1")[0]
    s["new_claims"] = [{"key": "n1", "text": "Fear is met by presence: the troubled are told who is with them before "
                        "the storm is stilled.", "beyond_text": "the order (word before calm) is read, not stated",
                        "verdict": "New", "sources": ["Mar 6:49"], "observations": [new_obs[0]],
                        "tell": [{"chapter": blk["chapter_no"], "section": blk["heading"], "kind": "in full"}]}]
    for x in s["observations"]:
        if x["observation"] == new_obs[0]:
            x["claim"] = "n1"
        elif not x["carried_by"]:
            x["disposition"] = {"as": "silent", "reason": "test reading: the earlier draft is not carried here"}
    for x in s["claims"]:
        if x["status"] == "current" and not x["told_in"]:
            x["hold"] = "test reading: held"
    for x in s["open_items"]:
        x["settle"] = settles.get(x["item"])
    if extra:
        extra(s)
    p = S / "apply.json"
    p.write_text(json.dumps(s, ensure_ascii=False), encoding="utf-8")
    return p


closed = {"as": "closed", "answer": "answered by the test reading: n1 told in the first block"}
other = {ref: closed for ref in items if ref not in ("OT-11.1", added)}
touched = {"as": "touched", "found": "Mar 6:49-50 read: the troubling is answered by his word before the calm"}

# P1 touched on an item lying wholly inside the reading: refused
o = run("apply", Label=LABEL, File=str(synergy_with({**other, "OT-11.1": touched, added: touched})))
case("P1", "Apply refused: touched on an item whose target lies wholly inside the reading", o.condition == "refused"
     and "wholly inside" in o.message and item_status(added) == "open", o.message[:240])
# P2 touched with no `found`: refused
o = run("apply", Label=LABEL, File=str(synergy_with({**other, "OT-11.1": {"as": "touched"}, added: closed})))
case("P2", "Apply refused: touched with no found", o.condition == "refused" and "touched needs found" in o.message,
     o.message[:240])
# P3 gate 2 refused while an item reaching past is left with no settle
o = run("apply", Label=LABEL, File=str(synergy_with({**other, added: closed})))
o2 = run("check", Label=LABEL)
case("P3", "Apply with OT-11.1 not settled, then Check at gate 2 refused naming OT-11.1",
     o.condition == "ok" and o2.condition == "refused" and "OT-11.1: still open" in o2.message, f"{o.message[:160]} / "
     f"{o2.message[:240]}")
# P4 touched on the item reaching past: applied, the item stays open, gate 2 passes
o = run("apply", Label=LABEL, File=str(synergy_with({"OT-11.1": touched})))
resp = q("SELECT r.kind, r.text FROM escalation_thread_item_response r JOIN escalation_thread_item i ON i.id=r.item_id "
         "JOIN escalation e ON e.id=i.escalation_id WHERE e.alias='OT-11' AND i.item_no=1 ORDER BY r.id DESC LIMIT 1")
o2 = run("check", Label=LABEL)
case("P4", "Apply: OT-11.1 touched (read in part) and still open; gate 2 passed, synergised",
     o.condition == "ok" and resp and resp[0][0] == "touched" and rd.PART_MARK in resp[0][1]
     and item_status("OT-11.1") == "open" and o2.condition == "ok"
     and q("SELECT state FROM reading WHERE label=?", LABEL)[0][0] == "synergised",
     f"{o.message[:200]} / {o2.message[:160]} / {resp and tuple(resp[0])}")

out = ROOT / "outputs/escalation/2250-reading-partial-test-results-v1-20261023.md"
L = ["# 2250 -- reading gate 2, items read in part: test results (v1)", "", f"Run on a copy of iba.db ({DB}).", "",
     f"**{sum(1 for x in results if x[2] == 'PASS')}/{len(results)} passed.**", "",
     "| Case | What | Result | Evidence |", "|---|---|---|---|"] + [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in results]
out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"{sum(1 for x in results if x[2] == 'PASS')}/{len(results)} -> {out}")
