"""temp_2228_reading_test_run.py -- test plan for escalation #2228, the reading process (design
outputs/escalation/2228-reading-process-design-v2-20261023.md). Run on a copy of iba.db made with lib/dbsnapshot.copy_db
with the migration applied to the copy; the narrative folder, the learning4comfort inbox and the output folders are
redirected to the scratch directory. Expected values by plain SQL on the copy.

Usage: python iba/app/tools/temp_2228_reading_test_run.py <scratch dir>
"""
import json
import os
import pathlib
import shutil
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import reading as rd  # noqa: E402
from iba.app.lib import versemeta  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2228r"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT)}
mig = ROOT / "iba/app/migration/reading_process_2228_v1_20261023.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(mig), "--db", str(DB)],
                                                                 capture_output=True, text=True, env=env)) for _ in range(2)]
live = sqlite3.connect(ROOT / "iba/app/db/iba.db")
src = ROOT / json.loads(live.execute("SELECT value FROM cfg_setting WHERE key='narrative.copy_source_dir'").fetchone()[0])
chap = S / "chapters"
chap.mkdir()
for (f,) in live.execute("SELECT current_file FROM narrative_chapter WHERE inactive=0 AND current_file IS NOT NULL"):
    shutil.copy2(src / f, chap / f)
INBOX = S / "inbox"
c = sqlite3.connect(DB)
for key, val in (("narrative.copy_source_dir", str(chap)), ("narrative.learning4comfort_inbox_dir", str(INBOX)),
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


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/").replace("\n", " ")[:500]))
    print(f"{cid} {'PASS' if passed else 'FAIL'}" + ("" if passed else f"  {str(evidence)[:700]}"), flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(step, **params):
    params.setdefault("By", "Claude")
    return getattr(hr, step)(Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None,
                                 params=params, step_id=f"reading.{step}"))


def gapfile(label="t-fear"):
    return S / "reading" / label / f"{label}-gaps.json"


LABEL, ESC = "t-fear", 2172
# ── R0 migration ─────────────────────────────────────────────────────────────────────────────────
strands = [tuple(x) for x in q("SELECT code, state FROM reading_strand")]
steps_live = q("SELECT step FROM cfg_step WHERE work_package='strand-reading' AND inactive=0")
gates = [tuple(x) for x in q("SELECT check_kind, active FROM cfg_escalation_requirement WHERE check_kind IN "
                              "('strand_account_clean', 'readings_published') ORDER BY check_kind, action")]
case("R0", "migration applied, then nothing to do; strands superseded, strand steps retired, the reading gate on, the "
     "strand gate off", "applied" in mo[0] and "0 cfg write(s)" in mo[1] and all(s[1] == "superseded" for s in strands)
     and not steps_live and gates == [("readings_published", 1)] * 2 + [("strand_account_clean", 0)] * 2,
     f"{mo}; strands {strands}; live strand steps {steps_live}; gates {gates}")
types = rd.gap_types(cfg)
case("R0b", "gap types: enum and setting agree, 5 recording and 2 synergy types", len(types) == 7 and
     sum(1 for t in types.values() if t["phase"] == "recording") == 5, list(types))

# ── R1 Open refusals ─────────────────────────────────────────────────────────────────────────────
scope = {"Verse": "Mar 6:49; Mar 6:50; Psa 36:4"}
ref = {
    "R1a label not lowercase-hyphenated": dict(Label="T Fear", Escalation=str(ESC), Home="M01", **scope),
    "R1b escalation completed": dict(Label=LABEL, Escalation="2236", Home="M01", **scope),
    "R1c home not a cluster": dict(Label=LABEL, Escalation=str(ESC), Home="X99", **scope),
    "R1d scope above 2,500 not reviewed": dict(Label=LABEL, Escalation=str(ESC), Home="M01", Strong="H3068G"),
    "R1e no -By": dict(Label=LABEL, Escalation=str(ESC), Home="M01", By=None, **scope),
}
for cid, params in ref.items():
    o = run("open", **params)
    case(cid.split()[0], f"Open refused: {cid.split(' ', 1)[1]}", o.condition == "refused"
         and not q("SELECT 1 FROM reading"), o.message[:200])

# ── R2 Open ──────────────────────────────────────────────────────────────────────────────────────
o = run("open", Label=LABEL, Escalation=str(ESC), Home="M01", **scope)
r = q("SELECT * FROM reading WHERE label=?", LABEL)
nv = q("SELECT count(*) FROM reading_verse WHERE reading_id=?", r[0]["id"])[0][0] if r else 0
g = json.loads(gapfile().read_text(encoding="utf-8")) if gapfile().is_file() else {"sections": {}}
secs = g["sections"]
oi = [it["item"] for it in secs.get("open_item", {}).get("items", [])]
hu = [(it["verse"], it["strong"]) for it in secs.get("hit_unread", {}).get("items", [])]
case("R2", "Open: the reading and its 3 verses kept; the gap JSON has the 5 recording sections, each with its guide; "
     "OT-11.1 matched; the Psa 36:4 hit unread", o.condition == "ok" and r and r[0]["state"] == "open" and nv == 3
     and set(secs) == {k for k, t in types.items() if t["phase"] == "recording"}
     and all(secs[k]["guide"] == types[k]["guide"] for k in secs) and "OT-11.1" in oi and ("Psa 36:4", "H2803I") in hu
     and (S / "reading" / LABEL / f"{LABEL}-collation.json").is_file(),
     f"{o.message[:300]}; open items {oi}; unread {hu}")
o = run("open", Label=LABEL, Escalation=str(ESC), Home="M01", **scope)
case("R3", "Open refused: the label exists", o.condition == "refused" and "already exists" in o.message, o.message[:120])

# ── R4 Check before any record ───────────────────────────────────────────────────────────────────
o = run("check", Label=LABEL)
case("R4", "Check at gate 1 refused while items have no record; still open", o.condition == "refused" and "no record" in
     o.message and q("SELECT state FROM reading WHERE label=?", LABEL)[0][0] == "open", o.message[:200])


# ── R5 Record refusals ───────────────────────────────────────────────────────────────────────────
def fill(bad=None):
    d = json.loads(gapfile().read_text(encoding="utf-8"))
    for sec, s in d["sections"].items():
        for it in s["items"]:
            if sec in ("not_read", "read_in_files_only") and it["verse"] == "Mar 6:49":
                it["record"] = {"new": {"text": "Seeing him on the sea, \"they thought it was a ghost, and cried out\": "
                                        "the mind names what it cannot place, and fear follows the naming",
                                        "meaning": "the thought (dokeo) comes before the cry; the fear rests on a "
                                        "reading of what is seen", "basis": "read",
                                        "verses": [{"verse": "Mar 6:49", "strong": "G1380"}]}}
            elif sec == "open_item":
                it["record"] = {"new": {"response": "read with Mar 6:50: the troubling stands with fear and is "
                                                    "answered by his word"}}
            elif sec == "hit_unread":
                it["record"] = {"new": {"face": "A. Planning evil on his bed", "parties": "the wicked, alone"}}
            else:
                it["record"] = {"reason": "not needed for this test reading: the word is not read here"}
    d["new_items"] = [{"thread": "OT-11", "origin": "1958", "anchor": "verse:Mar 6:50", "verse": "Mar 6:50",
                       "read_for": "the 'Take heart' words beside tarasso: courage given as the answer to trouble",
                       "why": "found in the test reading of #2228: the word of courage stands with the troubling",
                       "comes_back_when": "when M19 Trust and refuge is read"}]
    if bad:
        bad(d)
    p = S / "fill.json"
    p.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    return p


def bad_quote(d):
    for s in d["sections"].values():
        for it in s["items"]:
            if (it.get("record") or {}).get("new", {}).get("text"):
                it["record"]["new"]["text"] = "He said to them: \"the sea is calm and you are safe now, children.\""


def bad_table(d):
    d["sections"]["hit_unread"]["items"][0]["record"] = {"table": "reading_strand_hit", "id": 999999999}


def bad_two(d):
    d["sections"]["hit_unread"]["items"][0]["record"] = {"reason": "a reason of length", "table": "x", "id": 1}


def bad_meaning(d):
    for it in d["sections"]["meaning_missing"]["items"][:1]:
        it["record"] = {"new": {"text": "x"}}


def other(d):
    d["reading_id"] = 999


before = q("SELECT count(*) FROM ib_observation")[0][0]
for cid, fn, word in (("R5a", bad_quote, "quotation"), ("R5b", bad_table, "does not exist"),
                      ("R5c", bad_two, "record is one of"), ("R5d", bad_meaning, "no new row"), ("R5e", other, "not t-fear")):
    if cid == "R5d" and not secs.get("meaning_missing", {}).get("items"):
        case(cid, "Record refused: a new row for meaning_missing (no such item in this scope: not exercised)", True, "skipped")
        continue
    o = run("record", Label=LABEL, File=str(fill(fn)))
    case(cid, f"Record refused, nothing written: {fn.__name__}", o.condition == "refused" and word in o.message
         and q("SELECT count(*) FROM ib_observation")[0][0] == before, o.message[:240])

# ── R6 Record ────────────────────────────────────────────────────────────────────────────────────
o = run("record", Label=LABEL, File=str(fill()))
d = json.loads((S / "fill.json").read_text(encoding="utf-8"))
recs = [it["record"] for s in d["sections"].values() for it in s["items"]]
new_obs = [x["id"] for x in recs if x.get("table") == "ib_observation"]
ob = q("SELECT stage, cluster_code, status FROM ib_observation WHERE id=?", new_obs[0]) if new_obs else []
resp = [x["id"] for x in recs if x.get("table") == "escalation_thread_item_response"]
rk = q("SELECT kind FROM escalation_thread_item_response WHERE id=?", resp[0]) if resp else []
hit = q("SELECT face FROM reading_strand_hit h JOIN verse v ON v.id=h.verse_id WHERE v.reference='Psa 36:4' AND "
        "h.strong='H2803I'")
added = d["new_items"][0].get("added")
case("R6", "Record: a new observation (home M01, strand-reading stage), a 'touched' response on OT-11.1, the hit's face, "
     "a new open item through the open-item tool (D-b); ids written back into the file",
     o.condition == "ok" and ob and ob[0]["cluster_code"] == "M01" and ob[0]["stage"] == "strand-reading"
     and rk and rk[0][0] == "touched" and hit and hit[0][0] and added and added.startswith("OT-11.")
     and all(x.get("id") or x.get("reason") for x in recs), f"{o.message[:300]}; obs {ob and dict(ob[0])}")
o = run("record", Label=LABEL, File=str(S / "fill.json"))
case("R7", "Record again with nothing new refused", o.condition == "refused" and "nothing to record" in o.message, o.message[:120])

# ── R8 gate 1 ────────────────────────────────────────────────────────────────────────────────────
shutil.copy2(S / "fill.json", gapfile())
st_before = dict(q("SELECT v.reference, m.status FROM verse_meta m JOIN verse v ON v.id=m.verse_id WHERE v.reference IN "
                   "('Mar 6:50', 'Psa 36:4')"))
o = run("check", Label=LABEL)
st = dict(q("SELECT v.reference, m.status FROM verse_meta m JOIN verse v ON v.id=m.verse_id WHERE v.reference IN "
            "('Mar 6:50', 'Psa 36:4')"))
case("R8", "Check: gate 1 passed, recorded; the scope's verses analysed (or kept citated)",
     o.condition == "ok" and q("SELECT state FROM reading WHERE label=?", LABEL)[0][0] == "recorded"
     and all(v in ("analysed", "citated", "exclude") for v in st.values()), f"{o.message}; {st_before} -> {st}")
try:
    versemeta.run_set_status(cfg, ["Gen 1:1"], "analysed")
    ok9 = False
except ValueError as exc:
    ok9 = "gate 1" in str(exc)
case("R9", "D-c: 'analysed' cannot be set by hand", ok9, "run_set_status refused")

# ── R10-R11 synergy ──────────────────────────────────────────────────────────────────────────────
o = run("synergy", Label=LABEL)
r = q("SELECT * FROM reading WHERE label=?", LABEL)[0]
syn = json.loads((ROOT / r["synergy_file"]).read_text(encoding="utf-8")) if r["synergy_file"] else {}
case("R10", "Synergy: built from the tables -- the new observation, OT-11.1 and the new item listed; built_at matches",
     o.condition == "ok" and syn.get("built_at") == r["synergy_built_at"]
     and new_obs[0] in [x["observation"] for x in syn.get("observations", [])]
     and {"OT-11.1", added} <= {x["item"] for x in syn.get("open_items", [])}, o.message[:300])
syn_path = S / "reading" / LABEL / f"{LABEL}-synergy.json"
o = run("check", Label=LABEL)
case("R11", "Check at gate 2 refused before Apply (the new observation not carried, OT-11.1 open)",
     o.condition == "refused" and f"observation {new_obs[0]}" in o.message and "OT-11.1" in o.message, o.message[:300])

# ── R12 Apply refusals ───────────────────────────────────────────────────────────────────────────
s2 = json.loads(syn_path.read_text(encoding="utf-8"))
s2["built_at"] = "2026-01-01T00:00:00Z"
(S / "stale.json").write_text(json.dumps(s2), encoding="utf-8")
o = run("apply", Label=LABEL, File=str(S / "stale.json"))
case("R12a", "Apply refused: a synergy JSON not built from this reading's tables", o.condition == "refused"
     and "not the synergy JSON" in o.message, o.message[:200])
s3 = json.loads(syn_path.read_text(encoding="utf-8"))
s3["open_items"][0]["settle"] = {"as": "superseded", "by": "something else"}
(S / "bad-sup.json").write_text(json.dumps(s3), encoding="utf-8")
o = run("apply", Label=LABEL, File=str(S / "bad-sup.json"))
case("R12b", "Apply refused: superseded without naming the carrier", o.condition == "refused" and "OT-nn.n or #nnnn"
     in o.message, o.message[:200])

# ── R13 Apply ────────────────────────────────────────────────────────────────────────────────────
blk = q("SELECT s.heading, ch.chapter_no FROM narrative_section s JOIN narrative_chapter ch ON ch.id=s.chapter_id AND "
        "ch.inactive=0 WHERE s.last_version IS NULL AND s.level>0 AND s.block_text IS NOT NULL ORDER BY ch.reading_order, "
        "s.ordinal LIMIT 1")[0]
s4 = json.loads(syn_path.read_text(encoding="utf-8"))
s4["new_claims"] = [{"key": "n1", "text": "Fear is met by presence: the troubled are told who is with them before the "
                     "storm is stilled.", "beyond_text": "the order (word before calm) is read, not stated",
                     "verdict": "New", "sources": ["Mar 6:49"], "observations": [new_obs[0]],
                     "tell": [{"chapter": blk["chapter_no"], "section": blk["heading"], "kind": "in full"}]}]
for x in s4["observations"]:
    if x["observation"] == new_obs[0]:
        x["claim"] = "n1"
    elif not x["carried_by"]:
        x["disposition"] = {"as": "silent", "reason": "test reading: the earlier draft is not carried here"}
for x in s4["claims"]:
    if x["status"] == "current" and not x["told_in"]:
        x["hold"] = "test reading: held"
for x in s4["open_items"]:
    if x["item"] == "OT-11.1":
        x["settle"] = {"as": "forward", "new_item": {
            "thread": "OT-11", "origin": "1958", "anchor": "verse:Mat 14:26", "verse": "Mat 14:26; Joh 14:27",
            "read_for": "tarasso where the reading did not reach: the disciples terrified, and peace given",
            "why": "carried forward from OT-11.1 by the test reading of #2228 (gate 2)",
            "comes_back_when": "when M03 Grief and lament is read"}}
    else:
        x["settle"] = {"as": "closed", "answer": "answered by the test reading: n1 told in the first block"}
(S / "apply.json").write_text(json.dumps(s4, ensure_ascii=False), encoding="utf-8")
o = run("apply", Label=LABEL, File=str(S / "apply.json"))
cl = q("SELECT c.claim_ref, c.in_narrative FROM narrative_claim c JOIN narrative_claim_source cs ON cs.claim_id=c.id "
       "WHERE cs.observation_id=?", new_obs[0])
it111 = q("SELECT i.status FROM escalation_thread_item i JOIN escalation e ON e.id=i.escalation_id WHERE e.alias='OT-11' "
          "AND i.item_no=1")
r = q("SELECT * FROM reading WHERE label=?", LABEL)[0]
case("R13", "Apply: new claim on the observation, told in a block; OT-11.1 carried forward (superseded); chapter recorded",
     o.condition == "ok" and cl and cl[0][1] == 1 and it111 and it111[0][0] == "superseded"
     and str(blk["chapter_no"]) in json.loads(r["chapters"] or "[]"), o.message[:400])
o = run("check", Label=LABEL)
case("R14", "Check: gate 2 passed, synergised", o.condition == "ok" and
     q("SELECT state FROM reading WHERE label=?", LABEL)[0][0] == "synergised", o.message[:400])

# ── R15-R17 gate 3 and the close gate ────────────────────────────────────────────────────────────
gm = rd.gate_message(conn, ESC)
case("R15", "the anchoring escalation cannot close while the reading is not published", gm and LABEL in gm, gm)
o = run("publish", Label=LABEL)
chs = json.loads(q("SELECT chapters FROM reading WHERE label=?", LABEL)[0][0])
same = []
for no in chs:
    f = q("SELECT current_file FROM narrative_chapter WHERE chapter_no=?", str(no))[0][0]
    same.append((chap / f).read_bytes() == (INBOX / f).read_bytes())
case("R16", "Publish: the touched chapters in the inbox byte-identical; published; the escalation's gate clear",
     o.condition == "ok" and q("SELECT state FROM reading WHERE label=?", LABEL)[0][0] == "published" and same
     and all(same) and rd.gate_message(conn, ESC) is None, o.message[:300])
o = hr.account(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-account", word="", word_id=None,
                   params={"Label": LABEL}, step_id="reading.account"))
case("R17", "Account written", o.condition == "ok" and "published" in o.message, o.message[:200])

# ── R18 validate ─────────────────────────────────────────────────────────────────────────────────
from iba.app.handlers import configmaint as cm  # noqa: E402
from iba.app.lib import cfgquality  # noqa: E402
for (k, v) in sqlite3.connect(DB).execute("SELECT key, value FROM cfg_setting WHERE key LIKE 'database.%.path' AND inactive=0").fetchall():
    conn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(str(ROOT / json.loads(v))), k))
errs = cm._validate_live(conn) + cfgquality.find_rule_scope_gaps(conn, ROOT / "iba" / "app") + [
    e for e in cfgquality.find_unregistered_project_scripts(conn, ROOT) if "iba/app/migration/" not in e]
case("R18", "configmaint.validate hard checks on the copy (a migration not yet archived set aside)", not errs, errs or "none")

out = ROOT / "outputs/escalation/2228-reading-test-results-v1-20261023.md"
L = ["# 2228 -- reading process test results (v1)", "", f"Run on a copy of iba.db ({DB}).", "",
     f"**{sum(1 for x in results if x[2] == 'PASS')}/{len(results)} passed.**", "",
     "| Case | What | Result | Evidence |", "|---|---|---|---|"] + [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in results]
out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"{sum(1 for x in results if x[2] == 'PASS')}/{len(results)} -> {out}")
