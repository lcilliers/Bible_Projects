"""temp_2206_reading_waste_test_run.py -- test plan for escalation #2206 (options 1, 2a, 3, 4, 5 and
the BUILD.md sec 42 fix), run on a copy of iba.db made with lib/dbsnapshot.copy_db. Never touches the
live DB or live report files: CONFIG-REPORT generation is replaced by a scratch path, and the list
report and the hook run against the copy.

Usage: python iba/app/tools/temp_2206_reading_waste_test_run.py <scratch dir>
"""
import json
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import dbsnapshot, compliance, cfgquality, escalation as esc  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.handlers import configmaint  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

scratch = pathlib.Path(sys.argv[1])
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")))


# ── fixtures: a project tree holding the copy (the hook resolves iba/app/db/iba.db under cwd) ──
proj = scratch / "proj"
if proj.exists():
    shutil.rmtree(proj)
(proj / "iba" / "app" / "db").mkdir(parents=True)
(proj / ".claude").mkdir()
copy = dbsnapshot.copy_db(proj / "iba" / "app" / "db" / "iba.db")
# validate opens research_db relative to the copy's project root (valuequality._conn_for)
dbsnapshot.copy_db(proj / "database" / "bible_research.db", ROOT / "database" / "bible_research.db")

# T1 migration: applied to live before this run (archived scripts are gated, #2200, so it is not
# re-run); the copy carries its audited writes
import sqlite3 as _s
_c = _s.connect(copy)
logged = _c.execute("SELECT table_name, op FROM cfg_change_detail WHERE run_id="
                    "'DEVMODE-2206-READING-WASTE-20261021' ORDER BY id").fetchall()
has = _c.execute("SELECT 1 FROM cfg_setting WHERE key='compliance.value_settings' AND inactive=0").fetchone()
_c.close()
case("T1", "migration's 2 writes are in cfg_change_detail and the setting is live",
     logged == [("cfg_setting", "insert"), ("cfg_utility", "insert")] and has, f"{logged}")

cfg = Cfg(copy)
db = Db(cfg, copy)
conn = cfg.conn

# T2 option 3: the 7 value settings are left out; the 2 unread ones stay
ids = {r["id"] for r in compliance.rules(conn, "developer")}
vals = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='compliance.value_settings'").fetchone()[0])
g = sorted(i for i in ids if i.startswith("G:"))
case("T2", "compliance.rules leaves out the 7 value settings, keeps scripts_ps_dir",
     not any(f"G:{v}" in ids for v in vals) and "G:governance.scripts_ps_dir" in ids,
     f"{len(g)} governance rows delivered; excluded {len(vals)}")
# T3 synthetic: with the setting inactive, all governance settings come back
conn.execute("UPDATE cfg_setting SET inactive=1 WHERE key='compliance.value_settings'")
g_all = [r for r in compliance.rules(conn, "developer") if r["id"].startswith("G:")]
conn.execute("UPDATE cfg_setting SET inactive=0 WHERE key='compliance.value_settings'")
case("T3", "no value_settings row: every governance setting delivered (fails open to reading)",
     len(g_all) == len(g) + len(vals), f"{len(g_all)} = {len(g)} + {len(vals)}")

# T4 option 2a: no context_delivered rule is listed
un = cfgquality.find_unenforced_behaviour_rules(conn)
case("T4", "unenforced list holds no context_delivered rule",
     un and not any("context_delivered" in u for u in un), f"{len(un)} listed: " + "; ".join(un))

# T5 acknowledged_findings reads the old-format approved item (full lists in context)
tried = configmaint._ADVISORY_TRIED[:40]
base_id, ack = esc.acknowledged_findings(db, "configmaint.validate", tried)
case("T5", "baseline found from the latest approved advisory escalation (old format)",
     base_id is not None and sum(len(v) for v in ack.values()) > 0,
     f"#{base_id}, {sum(len(v) for v in ack.values())} fingerprints in {len(ack)} categories")

# ── validate on the copy, CONFIG-REPORT redirected to scratch ──
configmaint.cfgreport.generate = lambda out_path: scratch / "CONFIG-REPORT-test.md"
# this test's own migration is registered at its archive path and moves there only after the live
# run; until then validate reports it as unregistered, so that one known file is filtered here
_unreg = cfgquality.find_unregistered_project_scripts
cfgquality.find_unregistered_project_scripts = lambda c, r: [
    e for e in _unreg(c, r) if "reading_waste_2206_v1_20261021.py" not in e]


def run_validate(run_id):
    ctx = Ctx(db=db, cfg=cfg, step=None, run_id=run_id, word="", word_id=None, params={},
              step_id="configmaint.validate")
    return configmaint.validate(ctx)


# close open advisory items on the copy so T6 starts from the baseline only (as after #2197 closes)
conn.execute("UPDATE escalation SET state='withdraw' WHERE at_step='configmaint.validate' AND "
             "state IN ('raised','in-progress','re-assigned','on-hold')")
o6 = run_validate("TEST-2206-T6")
pre = (o6.escalation or {}).get("preset", {})
size = len(json.dumps(pre))
case("T6", "validate vs baseline: escalates only new findings, preset is counts+fingerprints (no lists)",
     (o6.condition == "ok" and o6.escalation is None) or (o6.escalation is not None and all(isinstance(v, int) for v in pre.get("new", {}).values())
                                and not any(isinstance(v, list) and v and len(v[0]) > 12
                                            for v in pre.get("fingerprints", {}).values())),
     f"condition={o6.condition}; question={(o6.escalation or {}).get('question', o6.message)[:300]}; "
     f"preset {size} bytes")

# T7: acknowledge that run (raise it as run.py would, then approve) -> rerun reports no new findings
if o6.escalation:
    e = o6.escalation
    eid = esc.raise_(db, "TEST-2206-T6", "configmaint", "configmaint.validate", e["question"], e["preset"],
                     e["tried"], resolution_kind="decision_required")
    eid = eid if isinstance(eid, int) else conn.execute("SELECT max(id) FROM escalation").fetchone()[0]
    ctx_len = len(conn.execute("SELECT context FROM escalation WHERE id=?", (eid,)).fetchone()[0])
    conn.execute("UPDATE escalation SET next_action='approved', state='completed' WHERE id=?", (eid,))
    o7 = run_validate("TEST-2206-T7")
    case("T7", "after approval, the same findings are not asked again",
         o7.escalation is None and o7.condition == "ok" and "no new findings" in o7.message,
         f"raised #{eid} context {ctx_len} chars; rerun: {o7.condition}: {o7.message[:200]}")
else:
    case("T7", "after approval, the same findings are not asked again", o6.condition == "ok",
         f"T6 already found nothing new: {o6.message[:200]}")

# T8 synthetic: one new finding appears -> escalated, only it counted as new
orig = cfgquality.find_query_file_convention_violations
cfgquality.find_query_file_convention_violations = lambda root: orig(root) + ["SYNTHETIC new finding for #2206 T8"]
o8 = run_validate("TEST-2206-T8")
cfgquality.find_query_file_convention_violations = orig
new8 = (o8.escalation or {}).get("preset", {}).get("new", {})
case("T8", "a new finding is escalated, and only it counts as new",
     o8.escalation is not None and new8 == {"query_file_convention": 1},
     f"condition={o8.condition}; new={new8}")

# T14: an open advisory item, re-run with identical findings -> matched, no new version
eid14 = esc.raise_(db, "TEST-2206-T14", "configmaint", "configmaint.validate", o8.escalation["question"],
                   o8.escalation["preset"], o8.escalation["tried"], resolution_kind="decision_required")
cfgquality.find_query_file_convention_violations = lambda root: orig(root) + ["SYNTHETIC new finding for #2206 T8"]
v_before = conn.execute("SELECT version FROM escalation WHERE id=?", (eid14,)).fetchone()[0]
o14a = run_validate("TEST-2206-T14a")
o14b = run_validate("TEST-2206-T14b")
cfgquality.find_query_file_convention_violations = orig
v_after = conn.execute("SELECT version FROM escalation WHERE id=?", (eid14,)).fetchone()[0]
case("T14", "re-run with unchanged findings while an item is open: matched, no new version",
     "identical" in o14a.message and "identical" in o14b.message and v_after == v_before,
     f"#{eid14} v{v_before} -> v{v_after}; {o14b.message[:120]}")
# T15: findings change while the item is open -> one new version, then identical again
cfgquality.find_query_file_convention_violations = lambda root: orig(root) + [
    "SYNTHETIC new finding for #2206 T8", "SYNTHETIC second finding for #2206 T15"]
o15a = run_validate("TEST-2206-T15a")
o15b = run_validate("TEST-2206-T15b")
cfgquality.find_query_file_convention_violations = orig
v15 = conn.execute("SELECT version FROM escalation WHERE id=?", (eid14,)).fetchone()[0]
case("T15", "findings change while open: recorded once as a new version, the next identical run matches it",
     "recorded on it" in o15a.message and "identical" in o15b.message and v15 == v_after + 1,
     f"#{eid14} v{v_after} -> v{v15}; second run: {o15b.message[:100]}")

# T9 option 4: list report, latest version only, parked one line each
lp, rows = esc.write_list_report(cfg, db, scratch / "escalation-list-test.md")
txt = pathlib.Path(lp).read_text(encoding="utf-8")
open_s = esc.state_group(db, "open")
n_parked = sum(1 for r in rows if r["state"] not in open_s) if rows and isinstance(rows[0], dict) or rows else 0
case("T9", "list report: no per-version history table; parked items one line each",
     "| v | state |" not in txt and "## Parked" in txt,
     f"{len(txt)} bytes (live v185 was 22345); {txt.count(chr(10) + '- #')} parked lines")
db.conn.commit()

# ── T10-T13 option 5: the Stop hook against the copy ──
hook = ROOT / ".claude" / "hooks" / "stop_check_escalation_backlog.py"
state = proj / ".claude" / ".session-boundary-state.json"


def hook_run():
    p = subprocess.run([sys.executable, str(hook)], input=json.dumps({"cwd": str(proj)}),
                       capture_output=True, text=True)
    return json.loads(p.stdout or "{}")


last2177 = conn.execute("SELECT max(answered_at) FROM escalation_history WHERE escalation_id=2177").fetchone()[0]
state.write_text(json.dumps({"at": "2026-10-21T17:12:09Z"}))
r10 = hook_run()
case("T10", "item worked this session (#2177, latest " + last2177 + ") does not block",
     "2177" not in r10.get("reason", ""), r10.get("decision", "no block"))
state.write_text(json.dumps({"at": "2099-01-01T00:00:00Z"}))
r11 = hook_run()
case("T11", "session started after the item's last change: it still blocks",
     "#2177" in r11.get("reason", ""), r11.get("decision", "no block"))
state.unlink()
r12 = hook_run()
case("T12", "no session record: nothing is left out, it blocks",
     "#2177" in r12.get("reason", ""), r12.get("decision", "no block"))
r13 = subprocess.run([sys.executable, str(hook)], input=json.dumps({"stop_hook_active": True}),
                     capture_output=True, text=True).stdout.strip()
case("T13", "retry after a block never blocks again", r13 == "{}", r13)

cfg.close()
out = scratch / "results.md"
out.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" +
               "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in results) + "\n", encoding="utf-8")
print(out.read_text(encoding="utf-8"))
print(f"{sum(r[2] == 'PASS' for r in results)}/{len(results)} pass")
