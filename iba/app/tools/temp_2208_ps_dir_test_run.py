"""temp_2208_ps_dir_test_run.py -- test plan for escalation #2208 option (a): lib/cfgquality.py reads
governance.scripts_ps_dir (ps_dir()) at its 5 former literal sites, and the setting joins
compliance.value_settings. Run on a copy of iba.db made with lib/dbsnapshot.copy_db; never touches
the live DB or live report files.

Usage: python iba/app/tools/temp_2208_ps_dir_test_run.py <scratch dir>
"""
import json
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import dbsnapshot, compliance, cfgquality  # noqa: E402

scratch = pathlib.Path(sys.argv[1])
if scratch.exists():
    shutil.rmtree(scratch)
scratch.mkdir(parents=True)
results = []
APP = ROOT / "iba" / "app"


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")))


copy = dbsnapshot.copy_db(scratch / "iba.db")
mig = ROOT / "iba" / "app" / "migration" / "ps_dir_setting_2208_v1_20261021.py"
o1 = subprocess.run([sys.executable, str(mig), "--db", str(copy)], capture_output=True, text=True).stdout
o2 = subprocess.run([sys.executable, str(mig), "--db", str(copy)], capture_output=True, text=True).stdout
case("T1", "migration: 2 audited writes, then skips", "2 write(s)" in o1 and "already" in o2,
     f"{o1.strip()} / {o2.strip()}")

import sqlite3  # noqa: E402
conn = sqlite3.connect(copy)
conn.row_factory = sqlite3.Row
ids = {r["id"] for r in compliance.rules(conn, "developer")}
g = [i for i in ids if i.startswith("G:")]
case("T2", "scripts_ps_dir no longer delivered; scripts_python_dir still delivered",
     "G:governance.scripts_ps_dir" not in ids and "G:governance.scripts_python_dir" in ids,
     f"{len(g)} governance rows delivered")

d = cfgquality.ps_dir(conn, APP)
case("T3", "ps_dir() resolves the setting to the repo's PS folder", d == ROOT / "iba" / "app" / "ps" and d.exists(), d)

real = {
    "escalation_ps_validateset_drift": cfgquality.find_escalation_ps_validateset_drift(conn, APP),
    "folderpurpose_ps_validateset_drift": cfgquality.find_folderpurpose_ps_validateset_drift(conn, APP),
    "ps_worksheet_drift": cfgquality.find_ps_worksheet_drift(conn, APP, ROOT),
    "escalation_worksheet_drift": cfgquality.find_escalation_worksheet_drift(conn, APP, ROOT),
    "ps_scripts_bypassing_runpy": cfgquality.find_ps_scripts_bypassing_runpy(conn, APP),
}
counts = {k: len(v) for k, v in real.items()}
case("T4", "the 5 checks on real data give the counts the last live validate gave (0,0,0,0,2)",
     counts == {"escalation_ps_validateset_drift": 0, "folderpurpose_ps_validateset_drift": 0,
                "ps_worksheet_drift": 0, "escalation_worksheet_drift": 0, "ps_scripts_bypassing_runpy": 2},
     f"{counts}; bypass: {real['ps_scripts_bypassing_runpy']}")

# T5 synthetic: point the setting at a scratch folder holding one bypassing script
fake = scratch / "repo" / "fakeps"
fake.mkdir(parents=True)
(fake / "Bad.ps1").write_text("python -m iba.app.lib.something --go\n", encoding="utf-8")
fake_app = scratch / "repo" / "iba" / "app"
fake_app.mkdir(parents=True)
conn.execute("UPDATE cfg_setting SET value=? WHERE key='governance.scripts_ps_dir'", (json.dumps("fakeps"),))
r5 = cfgquality.find_ps_scripts_bypassing_runpy(conn, fake_app)
case("T5", "the check follows the setting: a bypassing script in the configured folder is found",
     r5 == ["fakeps/Bad.ps1 calls iba.app.(handlers|lib|tools) directly, no iba.app.run dispatch found in the same file"],
     r5)

# T6 synthetic: setting inactive -> a loud KeyError, not a silent empty result
conn.execute("UPDATE cfg_setting SET inactive=1 WHERE key='governance.scripts_ps_dir'")
try:
    cfgquality.find_ps_scripts_bypassing_runpy(conn, APP)
    case("T6", "missing setting fails loudly", False, "no error raised")
except KeyError as e:
    case("T6", "missing setting fails loudly", True, f"KeyError: {e}")
conn.rollback()
conn.close()

out = scratch / "results.md"
out.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" +
               "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in results) + "\n", encoding="utf-8")
print(out.read_text(encoding="utf-8"))
print(f"{sum(r[2] == 'PASS' for r in results)}/{len(results)} pass")
