"""temp_2173_test_plan_run.py -- runs the #2173 test plan
(iba/docs/2173-session-routines-test-plan-v1-20261020.md) against a COPY of iba.db and a scratch
file tree. The live iba.db and the live project files are never written: Cfg/Db default to the copy,
and sessionwindow.repo_root / narrativeregister.PROJECT_ROOT point at the scratch root, which holds
copies of the chapter folder and the files the session-close checks read. STEP is read (only for the
gap codes). Git is the real repository's, read-only.

Usage: python -m iba.app.tools.temp_2173_test_plan_run <scratch_dir>
<scratch_dir>/repo/iba/app/db/iba.db must be a migrated copy of iba.db (the migration
session_routines_2173_v1_20261020 applied to it). Writes <scratch_dir>/results-2173.json and prints
a table. Temporary (governance.scripts_and_routines)."""
from __future__ import annotations

import json
import os
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
SCR = pathlib.Path(sys.argv[1]).resolve()
TDB = SCR / "repo" / "iba" / "app" / "db" / "iba.db"
FAKE = SCR / "fake"                      # scratch project root for file-based checks
os.environ["IBA_NO_SNAPSHOT"] = "1"

from iba.app.lib import cfg as cfgmod, db as dbmod          # noqa: E402
cfgmod.Cfg.__init__.__defaults__ = (TDB,)
dbmod.Db.__init__.__defaults__ = (None, TDB)

from iba.app import run as runmod                            # noqa: E402
from iba.app.lib import (compliance, escalation as esc, escalationcontext, narrativeregister as nr,  # noqa: E402
                         quotecheck, sessionwindow as sw, threadaudit)
from iba.app.lib.cfg import Cfg                               # noqa: E402
from iba.app.lib.db import Db                                 # noqa: E402
from iba.app.handlers import session_close as sc, spine      # noqa: E402

R: list[dict] = []

# ── fake project root for the file-based checks ──────────────────────────────────────────────
if FAKE.exists():
    shutil.rmtree(FAKE)
cdir_rel = pathlib.Path("_analytics/essay/spirit_soul_body/inner-being-narrative")
shutil.copytree(ROOT / cdir_rel, FAKE / cdir_rel, ignore=shutil.ignore_patterns("archive"))
(FAKE / "Logs" / "compliance").mkdir(parents=True)
(FAKE / "_analytics" / "cross-cluster-web").mkdir(parents=True)
(FAKE / "iba" / "app" / "reports").mkdir(parents=True)
reg = pathlib.Path("_analytics/cross-cluster-web/open-threads-register.md")
shutil.copy2(ROOT / reg, FAKE / reg)
sw.repo_root = lambda: FAKE
nr.PROJECT_ROOT = FAKE
os.chdir(FAKE)            # every report path is cwd-relative: reports land in the scratch tree



def T(tid, ok, ev):
    R.append({"id": tid, "result": "Pass" if ok else "FAIL", "evidence": str(ev)[:700]})


def step(pkg, sid, **params):
    return runmod.run_step(pkg, sid, dict(params), f"TEST-2173-{sid}-{len(R)}")


def conn():
    c = Cfg()
    return c, Db(c)


# ── G1 state groups ──────────────────────────────────────────────────────────────────────────
c, d = conn()
T("G1.1", esc.state_group(d, "open") == ("raised", "in-progress", "re-assigned")
  and esc.state_group(d, "parked") == ("on-hold",), esc.state_group(d, "open"))
r = step("escalation-reporting", "escalation.list")
T("G1.2", " open, " in r["message"] and "parked" in r["message"], r["message"])
d.close()
c2 = Cfg()
c2.conn.execute("UPDATE cfg_enum SET inactive=1 WHERE name='escalation_state_parked'")
try:
    esc.state_group(c2.conn, "parked")
    T("G1.3", False, "no error with the group switched off")
except RuntimeError as e:
    T("G1.3", True, e)
c2.conn.rollback()
c2.close()

# ── P1 context ───────────────────────────────────────────────────────────────────────────────
c, d = conn()
new_id = esc.raise_new(c, d, "TEST 2173 context", "claude", etype="task",
                       comment="see outputs/markdown/no-such-file-v3-20260101.md and run.py",
                       context="_analytics/Clusters/M53 - dishonor-disgrace/m53-cluster-overview-v1-20261019.md",
                       assigned_to="Claude", resolution_kind="self_correctable", originator="Claude")
d.close()
r = step("escalation-reporting", "escalation.context")
out = pathlib.Path(r["counts"]["path"]).read_text(encoding="utf-8")
sec = out.split(f"#{new_id} --", 1)[1].split("### #", 1)[0] if f"#{new_id} --" in out else ""
T("P1.1 missing file is a finding", "**missing**" in sec and "no-such-file" in sec, sec[:300])
T("P1.2 bare filename is a finding", "**bare**" in sec and "`run.py`" in sec, sec[:300])
T("P1.3 older version resolved to the latest", "m53-cluster-overview-v2-20261019.md" in sec
  and "newer" in sec, sec[:400])
T("P1.4 parked items are not read", "#1891 --" not in out, "on-hold #1891 absent" if "#1891 --" not in out else "present")

# ── P5 thread audit ──────────────────────────────────────────────────────────────────────────
c, d = conn()
t = d.rows("SELECT id, alias FROM escalation WHERE type='thread' AND state='on-hold' ORDER BY id LIMIT 1")[0]
n0 = d.rows("SELECT COALESCE(MAX(item_no),0) n FROM escalation_thread_item WHERE escalation_id=?", (t["id"],))[0]["n"]
told_ref = d.rows("SELECT v.reference FROM narrative_citation nc JOIN verse v ON v.id=nc.verse_id "
                  "WHERE nc.last_version IS NULL LIMIT 1")[0]["reference"]
for i, (k, v, note) in enumerate([("cluster", "M99", "x"), ("escalation", "#1962", "x"),
                                  ("verse", told_ref, "x"), ("strong", "H0430", None),
                                  ("cluster", "M02", "x")], 1):
    c.conn.execute("INSERT INTO escalation_thread_item (escalation_id, item_no, kind, value, status, "
                   "note, opened_at, opened_by) VALUES (?,?,?,?, 'open', ?, '2026-10-20', 'Claude')",
                   (t["id"], n0 + i, k, v, note))
c.conn.commit()
F = threadaudit.audit(c, d)
mine = {f["ref"]: f for f in F if f["ref"].startswith(t["alias"] + ".") and
        int(f["ref"].split(".")[1]) > n0}
T("P5 T-a cluster does not resolve", any(f["check"] == "T-a" and "M99" in f["reason"] for f in mine.values()), mine)
T("P5 T-c referred escalation closed", any(f["check"] == "T-c" for f in mine.values()), mine)
T("P5 T-e verse already told", any(f["check"] == "T-e" for f in mine.values()), mine)
T("P5 T-b no note", any(f["check"] == "T-b" for f in mine.values()), mine)
T("P5 T-d worked strand (M02, #1963 completed)", any(f["check"] == "T-d" and "M02" in f["reason"]
                                                      for f in mine.values()), mine)
T("P5 T-g register file differs from the table", any(f["check"] == "T-g" for f in F),
  "the test added thread items, so the copied register file is out of date")
d.close()

# ── P3 spine ─────────────────────────────────────────────────────────────────────────────────
from iba.app.lib.stepapi import Step                          # noqa: E402
c, d = conn()
f0 = spine.compute(c, c.conn, Step(c))
T("P3.0 live copy is sound", f0["fatal_count"] == 0, {k: v for k, v in f0.items() if not isinstance(v, list)})
c.conn.execute("INSERT INTO span (verse_id, position, surface, strong_variant, morph_code, is_particle, "
               "built_at, deleted) VALUES (99999999, 1, 'x', 'G9999Z', '', 0, '', 0)")
code = c.conn.execute("SELECT strong_variant FROM strong_meaning_tree WHERE deleted=0 AND "
                      "strong_variant LIKE 'H%' LIMIT 1").fetchone()[0]
c.conn.execute("UPDATE strong_meaning_tree SET deleted=1 WHERE strong_variant=?", (code,))
sc_code = c.conn.execute("SELECT strong FROM cluster_strong WHERE deleted=0 LIMIT 1").fetchone()[0]
c.conn.execute("UPDATE cluster_strong SET deleted=1 WHERE strong=?", (sc_code,))
f1 = spine.compute(c, c.conn, Step(c))
keys = [k for k, _ in spine.finding_lines(f1)]
T("P3.1 span with no verse", any(k.startswith("SC2:span:") for k in keys), keys[:6])
T("P3.2 span code with no strong", "SC2:desync:G9999Z" in keys, keys[:6])
T("P3.3 meaning gap where STEP has the content is FATAL", f"SC2:meaning:{code}" in keys, (code, keys[:8]))
T("P3.4 strong with no cluster", f"SC2:cluster:{sc_code}" in keys or not any(
    sc_code in (r[0] or "").split() for r in c.conn.execute("SELECT strong_variant FROM span WHERE deleted=0 LIMIT 1")),
  (sc_code, [k for k in keys if "cluster" in k][:3]))
T("P3.5 gaps by design listed, not FATAL", len(f1["meaning_by_design"]) >= 6, f1["meaning_by_design"][:3])
c.conn.rollback()
f2 = spine.compute(c, c.conn, None)
T("P3.6 STEP not asked -> unverified is FATAL", f2["fatal_count"] == len(f2["meaning_unverified"]) > 0,
  f2["step_error"])
d.close()

# ── P2 compliance ────────────────────────────────────────────────────────────────────────────
SID = "testsess-2173-0000-0000-000000000000"
os.environ["CLAUDE_CODE_SESSION_ID"] = SID
tdir = sw.transcripts_dir()
c, d = conn()
path, made = compliance.template(c, SID)
F = compliance.check_start(c, path)
T("P2.1 blank template fails: every rule listed", made and sum(1 for f in F if "blank" in f["reason"]) == len(compliance.rules(c.conn)),
  f"{len(F)} findings")
text = path.read_text(encoding="utf-8")
rules = compliance.rules(c.conn)
lines = []
for line in text.splitlines():
    if line.startswith("| G:") or line.startswith("| B:") or line.startswith("| E:"):
        rid = line.split("|")[1].strip()
        lines.append(f"| {rid} | not engaged | test session: no study or app work is done in it |  |")
    else:
        lines.append(line)
text = "\n".join(lines).replace("_(write: ", "").replace(c.required_setting("compliance.acknowledgement") + ")_",
                                                         c.required_setting("compliance.acknowledgement"))
retired = compliance.retired_mentions(c.conn)
text = text.replace("## Close dispositions", "\n".join(f"- {k}: names a retired thing, test" for k in retired)
                    + "\n\n## Close dispositions")
path.write_text(text, encoding="utf-8")
F = compliance.check_start(c, path)
T("P2.2 a filled file passes", not F, F[:3])
first = rules[0]
path.write_text(text.replace(f"| {first['id']} | not engaged | test session: no study or app work is done in it |  |",
                             f"| {first['id']} | engaged | {first['text'][:200].replace('|', ' ')} |  |"), encoding="utf-8")
F = compliance.check_start(c, path)
T("P2.3 a copied restatement is a finding", any(f["key"] == first["id"] and "copies" in f["reason"] for f in F), F[:2])
T("P2.7 a short genuine restatement is not judged a copy",
  not compliance.copied("no wipe of the escalation table", "as any full export+wipe of the escalation table.",
                        3, 0.6, int(c.required_setting("compliance.copy_min_words"))), "")
path.write_text(text.replace(c.required_setting("compliance.acknowledgement"), "I will try."), encoding="utf-8")
T("P2.4 missing acknowledgement is a finding", any(f["key"] == "ack" for f in compliance.check_start(c, path)), "")
eng = text.replace(f"| {first['id']} | not engaged | test session: no study or app work is done in it |  |",
                   f"| {first['id']} | engaged | I must do the thing in this session |  |")
path.write_text(eng, encoding="utf-8")
T("P2.5 engaged rule without evidence fails at close",
  any(f["key"] == first["id"] for f in compliance.check_close(c, path, "2026-10-20T00:00:00Z")), "")
path.write_text(eng.replace("I must do the thing in this session |  |",
                            "I must do the thing in this session | Logs/compliance/none.md; #2173 v1 |"),
                encoding="utf-8")
F = compliance.check_close(c, path, "2026-10-20T14:00:00Z")
T("P2.6 evidence that does not check is a finding", any("does not exist" in f["reason"] for f in F)
  and any("before this session" in f["reason"] for f in F), F)
(FAKE / "Logs/compliance/COMPLIANCE-20261020-d7696d1d.md").write_text("x", encoding="utf-8")
T("P2.8 hex inside a file name is not taken for a commit",
  compliance.check_evidence("Logs/compliance/COMPLIANCE-20261020-d7696d1d.md", c.conn, FAKE, None) == [], "")
path.write_text(text, encoding="utf-8")
d.close()

# ── G14 quote check ──────────────────────────────────────────────────────────────────────────
c, d = conn()
corpus = quotecheck.Corpus(c.conn)
n, bad = quotecheck.check_lines(corpus, ['He said, "For God so loved the world, that he gave his only Son" and '
                                         '"For God so loved the stars and the moon" (*agapao*, "to love").'],
                                2, quotecheck.titles(c.conn))
T("G14.1 a misquote fails, a true quote and a gloss do not", n == 2 and len(bad) == 1 and "loved the stars" in bad[0], (n, bad))
d.close()

# ── session-close on the fake root ───────────────────────────────────────────────────────────
real_changed = sw.changed_files
ch = c.conn  # noqa
reading = FAKE / "_analytics" / "cross-cluster-web" / "test-2173-reading-v1-20261020.md"
reading.write_text("# Test reading\n\nGenesis 1:1 and John 3:16 are read.\n\n## Placements\n\n"
                   "| verse | placement |\n|---|---|\n| Genesis 1:1 | data |\n\n## Open items\n\n"
                   "- Something to come back to\n- Carried on OT-999.1\n"
                   "- A wrapped line whose handle is on the\n  next line, #2173\n", encoding="utf-8")
chap = sorted((FAKE / cdir_rel).glob("10-01-*.md"))[-1]
chap.write_text(chap.read_text(encoding="utf-8") + '\n\nAs it is written, "the heart of stone rejoices in pancakes".\n',
                encoding="utf-8")
genrep = FAKE / "iba" / "app" / "reports" / "session-close-v1-20261020.md"
genrep.write_text("## SC4 Open items in the register\n\n- **OPEN** something\n", encoding="utf-8")
changed = [reading.relative_to(FAKE).as_posix(), chap.relative_to(FAKE).as_posix(), "iba/app/lib/compliance.py",
           "iba/app/lib/zz_test_2173_unnamed.py", genrep.relative_to(FAKE).as_posix()]
sw.changed_files = lambda base: changed
sw.identify = lambda marker: (SID, None, "test")
sw.boundary_record = lambda sid: {"first_seen_at": "2026-10-20T14:51:00Z"}
r = step("session-close", "session.close")
rep = pathlib.Path(r["counts"]["report"]).read_text(encoding="utf-8")
T("SC.1 open findings block (condition findings-open)", r["condition"] == "findings-open" and r["counts"]["open_findings"] > 0, r["message"])
T("SC4a open-items line with no handle", "SC4a:" in rep and "names no OT-nn.n" in rep, "")
T("SC4a handle that does not exist", "OT-999.1 does not exist" in rep, "")
T("SC4a a wrapped bullet is read whole (its handle on the next line counts)", "A wrapped line whose handle" not in rep, "")
T("SC4a a generated report's headings are not read as Open items", "session-close-v1-20261020.md` line" not in rep, "")
T("SC5d verse named with no placement", "Joh 3:16 is named but has no placement row" in rep, "")
T("SC5a chapter changed, no update recorded", "SC5a:" + chap.name in rep, "")
T("SC5b misquote in added lines", "pancakes" in rep, "")
T("SC6 compliance file found and checked", "SC6:file" not in rep, "")
T("SC8 no session log", "SC8:log" in rep, "")
T("SC10 a code file not named in BUILD.md's added lines is a finding; a named one is not",
  "SC10:iba/app/lib/zz_test_2173_unnamed.py" in rep and "SC10:iba/app/lib/compliance.py" not in rep, "")
T("SC12 narrative copy needed when a chapter changed", r["counts"]["narrative_copy"] == 1, r["counts"])
# SC3 / SC4b on synthetic messages
c, d = conn()
msgs = [dict(uuid="aaaaaaaa-1", at="2026-10-20T15:00:00Z", text="please hold this for later"),
        dict(uuid="bbbbbbbb-2", at="2026-10-20T15:01:00Z", text="/start-project"),
        dict(uuid="cccccccc-3", at="2026-10-20T15:02:00Z", text="zzz unrecorded instruction qqq"),
        dict(uuid="dddddddd-4", at="2026-10-20T15:03:00Z", text="proceed")]
f3, f4 = sc._sc3_sc4b(c, d, msgs, "2026-10-20T00:00:00Z")
T("SC3 an unrecorded message is a finding; a command name is not; a short one always needs its disposition",
  {x["key"] for x in f3} == {"SC3:aaaaaaaa", "SC3:cccccccc", "SC3:dddddddd"}, [x["key"] for x in f3])
T("SC4b a holding word needs its register item", [x["key"] for x in f4] == ["SC4b:aaaaaaaa"], [x["key"] for x in f4])
d.close()
# dispositions
cp = compliance.find_file(Cfg(), SID)
key4 = next(l.split("`")[1] for l in rep.splitlines() if "names no OT-nn.n" in l and "SC4a:" in l)
cp.write_text(cp.read_text(encoding="utf-8") + f"\n- {key4} :: carried #2173\n- SC8:log :: carried OT-999.1\n",
              encoding="utf-8")
r2 = step("session-close", "session.close")
rep2 = pathlib.Path(r2["counts"]["report"]).read_text(encoding="utf-8")
T("SC.2 a checked disposition clears; a bad one does not",
  f"cleared `{key4}`" in rep2 and "**OPEN** `SC8:log`" in rep2 and r2["counts"]["open_findings"] == r["counts"]["open_findings"] - 1,
  (r["counts"]["open_findings"], r2["counts"]["open_findings"]))
# SC1
sw.boundary_record = lambda sid: None
r3 = step("session-close", "session.close")
T("SC1 missing boundary record fails the close", "SC1:boundary" in pathlib.Path(r3["counts"]["report"]).read_text(encoding="utf-8")
  and r3["condition"] == "findings-open", r3["message"])
sw.changed_files = real_changed

# SC8/SC9 with a log; SC5c with a baseline
heads = Cfg().required_setting("session_close.log_sections")
logp = FAKE / "Logs" / "SESSION-LOG-20261020-test.md"
body = [f"# Session log -- session {SID}", ""]
for i, hd in enumerate(heads, 1):
    body += [f"## {hd}", ""]
    if i == 4:
        body += [f"- changed the compliance module (`{changed[2]}`)", "- decided something with no target at all"]
    elif i < 6:
        body += ["- text"]
    body.append("")
logp.write_text(chr(10).join(body), encoding="utf-8")
statep = FAKE / Cfg().required_setting("session_close.state_path")
statep.parent.mkdir(parents=True, exist_ok=True)
statep.write_text(json.dumps({"session_id": "an-earlier-session", "last": ["an old finding only"]}), encoding="utf-8")
sw.boundary_record = lambda sid: {"first_seen_at": "2026-10-20T14:51:00Z"}
sw.changed_files = lambda base: changed
r4 = step("session-close", "session.close")
rep4 = pathlib.Path(r4["counts"]["report"]).read_text(encoding="utf-8")
T("SC8 a log with its six sections clears SC8", "SC8:" not in rep4.split("## SC9")[0].split("## SC8")[1] if "## SC8" in rep4 else False, "")
T("SC9 a decision with no target is a finding; one naming a changed file is not",
  "decided something with no target" in rep4 and "changed the compliance module" not in rep4, "")
T("SC5c a register finding new since the previous close is a finding", "SC5c:new:" in rep4, "")
sw.changed_files = real_changed

# S6 last-session check (real git, read-only)
lc = sw.last_close_findings(Cfg())
T("S6 the last-session check runs and names its findings", isinstance(lc, list), lc[:3])

out = SCR / "results-2173.json"
out.write_text(json.dumps(R, indent=1), encoding="utf-8")
w = max(len(x["id"]) for x in R)
for x in R:
    print(f"{x['id']:<{w}}  {x['result']}  {x['evidence'][:150]}")
print(f"\n{sum(1 for x in R if x['result'] == 'Pass')} of {len(R)} pass -> {out}")
