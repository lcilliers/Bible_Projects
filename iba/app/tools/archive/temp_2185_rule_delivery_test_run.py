"""temp_2185_rule_delivery_test_run.py -- test plan for #2185 (rule delivery scoped by mode and
study state), run against a COPY of iba.db given as argv[1]. One-off; archived when #2185 closes.

Cases:
  T1 standard mode, study on hold: no study_active or developer_mode rule delivered
  T2 developer mode: developer_mode rules delivered; study rules still withheld
  T3 study active (flag set on the copy): study rules delivered in standard mode
  T4 an invalid study_state value raises
  T5 template(mode=developer) writes 'Mode: developer'; parse reads it back
  T6 check_start on a developer file: every developer_mode rule has a row to fill; a standard file
     carrying a row for a developer-only rule reports it as not delivered
  T7 deliver_lines ends with the withheld summary
  T8 config: _validate_live 0 errors; a bad deliver_when value is a value-quality error
"""
import json
import pathlib
import shutil
import sqlite3
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import compliance  # noqa: E402
from iba.app.handlers.configmaint import _validate_live  # noqa: E402

DB = pathlib.Path(sys.argv[1])
results = []


def T(name, cond, detail=""):
    results.append((name, bool(cond), detail))


c = sqlite3.connect(DB)
dw = dict(c.execute("SELECT id, deliver_when FROM cfg_behaviour_rule WHERE active=1").fetchall())
ids = lambda mode: {int(r["id"][2:]) for r in compliance.rules(c, mode) if r["id"].startswith("B:")}  # noqa: E731

std = ids("standard")
T("T1 standard/on_hold: only 'always' rules", all(dw[i] == "always" for i in std),
  f"{len(std)} delivered of {len(dw)}")
dev = ids("developer")
T("T2 developer: developer_mode in, study_active out",
  {i for i in dw if dw[i] == "developer_mode"} <= dev and not any(dw[i] == "study_active" for i in dev),
  f"{len(dev)} delivered")

c.execute("UPDATE cfg_setting SET value=? WHERE key='behaviour.study_state'", (json.dumps("active"),))
act = ids("standard")
T("T3 study active: study rules delivered", {i for i in dw if dw[i] == "study_active"} <= act,
  f"{len(act)} delivered")
c.execute("UPDATE cfg_setting SET value=? WHERE key='behaviour.study_state'", (json.dumps("paused"),))
try:
    compliance.rules(c, "standard"); T("T4 invalid study_state raises", False)
except ValueError as e:
    T("T4 invalid study_state raises", True, str(e)[:80])
c.execute("UPDATE cfg_setting SET value=? WHERE key='behaviour.study_state'", (json.dumps("on_hold"),))


class FakeCfg:
    def __init__(self, conn, d):
        self.conn, self._d = conn, d

    def required_setting(self, k):
        if k == "compliance.dir":
            return str(self._d)
        return json.loads(self.conn.execute("SELECT value FROM cfg_setting WHERE key=?", (k,)).fetchone()[0])

    def enum(self, name):
        return [v for (v,) in self.conn.execute("SELECT value FROM cfg_enum WHERE name=? AND inactive=0 "
                                                "ORDER BY ordinal", (name,))]


tmp = pathlib.Path(tempfile.mkdtemp())
orig_root = compliance.sw.repo_root
compliance.sw.repo_root = lambda: tmp
cfg = FakeCfg(c, "logs")
p, made = compliance.template(cfg, "testdev0-0000", "developer")
f = compliance.parse(p)
T("T5 developer template carries its mode", made and "Mode: developer" in p.read_text(encoding="utf-8")
  and f["mode"] == "developer")
F = compliance.check_start(cfg, p)
blank = {x["key"] for x in F if "blank" in x["reason"]}
need = {f"B:{i}" for i in dw if dw[i] == "developer_mode"}
T("T6a developer file: each developer_mode rule has a row to fill", need <= blank, f"{len(blank)} blank rows")
p2, _ = compliance.template(cfg, "teststd0-0000", "standard")
dev_id = sorted(need)[0]
p2.write_text(p2.read_text(encoding="utf-8").replace("## Conflicts", f"| {dev_id} | engaged | x | |\n\n## Conflicts"),
              encoding="utf-8")
F2 = compliance.check_start(cfg, p2)
T("T6b standard file with a developer-only row: reported as not delivered",
  any(x["key"] == dev_id and "not delivered" in x["reason"] for x in F2))
compliance.sw.repo_root = orig_root
shutil.rmtree(tmp)

lines = compliance.deliver_lines(c, "standard")
T("T7 deliver_lines ends with the withheld summary", "not delivered this session" in lines[-1], lines[-1].strip()[:90])

c.row_factory = sqlite3.Row
T("T8a validate: 0 coherence errors", not _validate_live(c))
c.execute("UPDATE cfg_behaviour_rule SET deliver_when='sometimes' WHERE id=(SELECT MIN(id) FROM cfg_behaviour_rule)")
errs = _validate_live(c)
T("T8b bad deliver_when is a value-quality error", any("deliver_when" in e for e in errs))
c.rollback()

for name, okv, d in results:
    print(("PASS " if okv else "FAIL ") + name + (f"  -- {d}" if d else ""))
print(f"{sum(o for _, o, _ in results)}/{len(results)} passed")
