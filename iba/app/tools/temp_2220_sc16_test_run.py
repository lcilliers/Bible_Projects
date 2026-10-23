"""temp_2220_sc16_test_run.py -- test for escalation #2220 decision B: SC16 does not count a designed stop
(session_close.sc16_designed_stops) as a failure; a real error is still counted. On a synthetic transcript, on
the real transcript of the session that raised #2220 (6c511f74, read-only), and on the setting through a copy
of iba.db with the migration applied.

Usage: python iba/app/tools/temp_2220_sc16_test_run.py <scratch dir>
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.handlers import session_close as sc  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2220"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:400]))


DB = copy_db(S / "iba.db")
mig = ROOT / "iba/app/migration/guard_review_sc16_2228_2220_v1_20261023.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
env = {**os.environ, "PYTHONPATH": str(ROOT)}
mo = [subprocess.run([sys.executable, str(mig), "--db", str(DB)], capture_output=True, text=True, env=env).stdout.strip()
      for _ in range(2)]
case("S0", "migration applied (or already), then skipped", ("applied" in mo[0] or "already" in mo[0]) and "already" in mo[1], mo)
stops = Cfg(DB).required_setting("session_close.sc16_designed_stops")
case("S1", "the setting holds the three designed stops", stops == ["COMMIT BLOCKED", "NOT PASSED",
                                                                    "a config change needs researcher approval"], stops)


def call(i, cmd):
    return {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": f"t{i}", "name": "PowerShell",
                                                          "input": {"command": cmd}}]}}


def result(i, text):
    return {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": f"t{i}", "is_error": True,
                                                     "content": text}]}}


lines = [call(1, ".\\iba\\app\\ps\\Session-Close.ps1"), result(1, "Exit code 3\n  COMMIT BLOCKED: 2 open finding(s)"),
         call(2, ".\\iba\\app\\ps\\Session-Close.ps1"), result(2, "Exit code 3\n  COMMIT BLOCKED: 1 open finding(s)"),
         call(3, ".\\iba\\app\\ps\\Config-Maintenance.ps1 -Step Propose"),
         result(3, "Exit code 3\n  configmaint.propose pause-continue a config change needs researcher approval"),
         call(4, ".\\iba\\app\\ps\\Config-Maintenance.ps1 -Step Propose"),
         result(4, "Exit code 3\n  configmaint.propose pause-continue a config change needs researcher approval"),
         call(5, ".\\iba\\app\\ps\\Spine-Check.ps1"), result(5, "Exit code 3\n  spine.check report-stop FATAL: 3 gaps"),
         call(6, ".\\iba\\app\\ps\\Spine-Check.ps1"), result(6, "Exit code 3\n  spine.check report-stop FATAL: 3 gaps")]
t = S / "synthetic.jsonl"
t.write_text("\n".join(json.dumps(x) for x in lines) + "\n", encoding="utf-8")
before = sc._sc16(t)
after = sc._sc16(t, stops)
case("S2", "synthetic: without the markers, three repeated failures; with them, only the real one (Spine-Check)",
     len(before) == 3 and len(after) == 1 and "Spine-Check" in after[0]["text"],
     f"before {[f['key'] for f in before]}; after {[f['key'] for f in after]}")

proj = pathlib.Path.home() / ".claude" / "projects" / "C--Bible-study-projects"
real = sorted(proj.glob("45f739ba*.jsonl")) + sorted(proj.glob("6c511f74*.jsonl"))
if real:
    b, a = sc._sc16(real[0]), sc._sc16(real[0], stops)
    case("S3", f"real transcript {real[0].name[:8]}: the designed stops no longer counted",
         not any("Session-Close" in f["text"] or "Propose" in f["text"] for f in a),
         f"before {[f['text'][:80] for f in b]}; after {[f['text'][:80] for f in a]}")
else:
    case("S3", "real transcript of the session that raised #2220", False, "not found")

L = ["| # | case | result | evidence |", "|---|---|---|---|"] + [f"| {a} | {b} | {r} | {e} |" for a, b, r, e in results]
(S / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
print(f"\n{sum(r[2] == 'PASS' for r in results)}/{len(results)} PASS")
