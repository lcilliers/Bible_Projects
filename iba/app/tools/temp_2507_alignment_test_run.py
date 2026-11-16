"""temp_2507_alignment_test_run.py -- tests for the stored alignment check of the lexical work (lib/lexicalalignment.py, escalation #2507 D9).

Runs on an in-memory database with the few tables the check reads and a scratch project folder; never on iba.db. Usage: python iba/app/tools/temp_2507_alignment_test_run.py
"""
import json
import pathlib
import sqlite3
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import lexicalalignment as la  # noqa: E402

res = []


def case(cid, desc, ok, ev=""):
    res.append((cid, desc, "PASS" if ok else "FAIL", str(ev)[:200]))


conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE cfg_setting (key TEXT, value TEXT, use TEXT, module TEXT, inactive INTEGER DEFAULT 0);
CREATE TABLE cfg_step (step TEXT, does TEXT, inactive INTEGER DEFAULT 0);
CREATE TABLE cfg_utility (module TEXT, purpose TEXT, inactive INTEGER DEFAULT 0);
CREATE TABLE cfg_method_rule (step TEXT, rule_key TEXT, rule_text TEXT, active INTEGER DEFAULT 1);
CREATE TABLE cfg_behaviour_rule (rule_key TEXT, rule_text TEXT, active INTEGER DEFAULT 1);
CREATE TABLE wa_obs_question_catalogue (question_code TEXT, deleted INTEGER DEFAULT 0, status TEXT DEFAULT 'active');
""")
tmp = pathlib.Path(tempfile.mkdtemp())
(tmp / "iba/app/lib").mkdir(parents=True)
(tmp / "iba/app/lib/archive").mkdir()
(tmp / "iba/app/ps").mkdir(parents=True)
for d in ("USER-GUIDE.md", "GOVERNANCE.md", "CHARTER.md"):
    (tmp / "iba/app" / d).write_text("ok\n", encoding="utf-8")

errs = la.find(conn, tmp)
case("A0", "without the setting the check says so", errs and "alignment.retired_lexical" in errs[0], errs)
conn.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES ('alignment.retired_lexical', ?, 'x', 'lexical')", (json.dumps(["lexical.meaning", "oldgen", "Old.ps1"]),))
case("A1", "a clean state has no finding", la.find(conn, tmp) == [], la.find(conn, tmp))
conn.execute("INSERT INTO cfg_step (step, does) VALUES ('s1', 'runs lexical.meaning over a cluster')")
case("A2", "an active step naming a retired entry without saying it is retired is found", any("cfg_step 's1'" in e for e in la.find(conn, tmp)))
conn.execute("UPDATE cfg_step SET does='lexical.meaning is retired, replaced by stage 1'")
case("A3", "the same text that says it is retired is accepted", la.find(conn, tmp) == [])
conn.execute("INSERT INTO cfg_method_rule (step, rule_key, rule_text, active) VALUES ('x', 'r', 'use oldgen to read', 0)")
case("A4", "an inactive rule is not read", la.find(conn, tmp) == [])
conn.execute("UPDATE cfg_method_rule SET active=1")
case("A5", "an active method rule naming a retired generator is found", any("cfg_method_rule" in e for e in la.find(conn, tmp)))
conn.execute("DELETE FROM cfg_method_rule")
(tmp / "iba/app/USER-GUIDE.md").write_text("run Old.ps1 -X to read\nOld.ps1 is retired (history)\n", encoding="utf-8")
e = la.find(conn, tmp)
case("A6", "a guidance line naming a retired script is found by its line and a line that says retired is not", len(e) == 1 and "USER-GUIDE.md:1" in e[0], e)
(tmp / "iba/app/USER-GUIDE.md").write_text("ok\n", encoding="utf-8")
(tmp / "iba/app/lib/live.py").write_text("from . import oldgen\n", encoding="utf-8")
(tmp / "iba/app/lib/archive/dead.py").write_text("from . import oldgen\n", encoding="utf-8")
e = la.find(conn, tmp)
case("A7", "a live module importing a retired module is found and one in an archive folder is not", len(e) == 1 and "live.py" in e[0], e)
(tmp / "iba/app/lib/live.py").write_text("x = 1\n", encoding="utf-8")
(tmp / "iba/app/ps/Run.ps1").write_text("& Old.ps1 -A\n", encoding="utf-8")
e = la.find(conn, tmp)
case("A8", "a live script running a retired script is found", len(e) == 1 and "Run.ps1" in e[0], e)
(tmp / "iba/app/ps/Run.ps1").write_text("x\n", encoding="utf-8")
conn.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES ('layer.reading', ?, 'x', 'layer')", (json.dumps({"items": {"i1": {"asks": "", "prompts": ["Q1"]}, "i2": {"asks": "ask", "prompts": []}}}),))
conn.execute("INSERT INTO wa_obs_question_catalogue (question_code, deleted, status) VALUES ('Q1', 1, 'active')")
e = la.find(conn, tmp)
case("A9", "an item with no asks and a prompt that is not an active question are found, an item with neither fault is not", len(e) == 2 and any("no `asks`" in x for x in e) and any("'Q1'" in x for x in e), e)
conn.execute("UPDATE wa_obs_question_catalogue SET deleted=0")
conn.execute("UPDATE cfg_setting SET value=? WHERE key='layer.reading'", (json.dumps({"items": {"i1": {"asks": "a", "prompts": ["Q1"]}}}),))
case("A10", "an active catalogue question is accepted", la.find(conn, tmp) == [])
conn.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES ('reading.node_roles', ?, 'x', 'reading')", (json.dumps({"relevant": ["characteristic"], "bears_on": ["object"], "recognised": ["standalone"], "lexical": ["lexical"]}),))
conn.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES ('alignment.inner_being_kinds', ?, 'x', 'lexical')", (json.dumps(["party", "qualification"]),))
conn.execute("UPDATE cfg_setting SET value=? WHERE key='layer.reading'", (json.dumps({"items": {"i1": {"asks": "ask about the inner being", "member_role": "characteristic", "partner_role": "lexical", "kind": "party", "route": True, "prompts": ["Q1"]}}}),))
e = la.find(conn, tmp)
case("A11", "the boundary of the stages: an inner-being role, a route, an inner-being kind and a question about the inner being are each found", len(e) == 4 and any("inner-being role" in x for x in e) and any("route" in x for x in e) and any("inner-being kind" in x for x in e) and any("asks about the inner being" in x for x in e), e)

print("| case | what | result | evidence |\n|---|---|---|---|")
for r in res:
    print("| " + " | ".join(r) + " |")
fails = [r for r in res if r[2] == "FAIL"]
print(f"\n{len(res) - len(fails)} of {len(res)} pass")
sys.exit(1 if fails else 0)
