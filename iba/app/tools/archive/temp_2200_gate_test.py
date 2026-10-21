"""temp_2200_gate_test.py -- the #2200 test plan for .claude/hooks/gate_retired_script.py, run against a
backup-API copy of iba.db holding test escalations. Writes the per-case results to the escalation's
results file. Temporary: archived once its results are on #2200.

Usage:  python iba/app/tools/temp_2200_gate_test.py SCRATCH_DIR
"""
import json
import os
import pathlib
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import dbsnapshot  # noqa: E402

HOOK = ROOT / ".claude/hooks/gate_retired_script.py"
OUT = ROOT / "outputs/escalation/2200-gate-test-results-v1-20261021.md"
RETIRED = "iba/app/tools/archive/temp_2193_test_plan_run.py"
RETIRED2 = "iba/app/tools/archive/temp_2192_apply.py"
INACTIVE_ROW = "query_db.py"


def run_hook(cmd: str, db: str | None) -> str:
    env = dict(os.environ)
    if db:
        env["IBA_GATE_DB"] = db
    payload = {"cwd": str(ROOT), "tool_name": "Bash", "tool_input": {"command": cmd}}
    r = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(payload), capture_output=True,
                       text=True, env=env, cwd=ROOT)
    out = json.loads(r.stdout or "{}")
    return "deny" if out.get("hookSpecificOutput", {}).get("permissionDecision") == "deny" else "allow"


def add_escalation(conn, eid: int, path: str, originator: str, state: str) -> None:
    over = {"id": eid, "state": state, "context": f"test approval for {path}"}
    cols = [r[1] for r in conn.execute("PRAGMA table_info(escalation)")]
    sel = ",".join("?" if c in over else c for c in cols)
    conn.execute(f"INSERT INTO escalation ({','.join(cols)}) SELECT {sel} FROM escalation "
                 "WHERE id=2200 ORDER BY version DESC LIMIT 1", [over[c] for c in cols if c in over])
    hover = {"escalation_id": eid, "next_action": "approved", "originator": originator,
             "context": f"use {path}"}
    hcols = [r[1] for r in conn.execute("PRAGMA table_info(escalation_history)") if r[1] != "id"]
    hsel = ",".join("?" if c in hover else c for c in hcols)
    conn.execute(f"INSERT INTO escalation_history ({','.join(hcols)}) SELECT {hsel} "
                 "FROM escalation_history WHERE escalation_id=2200 LIMIT 1",
                 [hover[c] for c in hcols if c in hover])


def main(scratch: pathlib.Path) -> int:
    scratch.mkdir(parents=True, exist_ok=True)
    db = scratch / "t2200-gate.db"
    if db.exists():
        db.unlink()
    dbsnapshot.copy_db(db)
    conn = sqlite3.connect(db)
    add_escalation(conn, 990001, RETIRED2, "Researcher", "re-assigned")   # approved by researcher
    add_escalation(conn, 990002, RETIRED, "Claude", "re-assigned")        # "approved" by Claude
    add_escalation(conn, 990003, INACTIVE_ROW, "Researcher", "withdraw")  # approved, then withdrawn
    conn.commit()
    conn.close()
    d = str(db)
    cases = [
        ("run retired .py (python path)", f"python {RETIRED}", d, "deny"),
        ("run retired .py with launcher flags", f"python -I -u {RETIRED}", d, "deny"),
        ("run retired module (python -m)", "python -m iba.app.tools.archive.temp_2193_test_plan_run", d, "deny"),
        ("run retired .py, Windows path", "python iba\\app\\tools\\archive\\temp_2193_test_plan_run.py", d, "deny"),
        ("approval written by Claude does not count", f"python {RETIRED}", d, "deny"),
        ("run retired .py approved by the researcher", f"python {RETIRED2}", d, "allow"),
        ("cfg_utility inactive row", f"python {INACTIVE_ROW}", d, "deny"),
        ("approval on a withdrawn item does not count", f"python {INACTIVE_ROW}", d, "deny"),
        ("retired .ps1 as first word", ".\\iba\\app\\ps\\archive\\Old-Thing.ps1 -X 1", d, "deny"),
        ("retired .ps1 via & call", "& \"iba/app/ps/archive/Old-Thing.ps1\"", d, "deny"),
        ("retired .ps1 inside pwsh -Command", "pwsh -NoProfile -Command \".\\iba\\app\\ps\\archive\\Old-Thing.ps1\"", d, "deny"),
        ("retired .ps1 via -File", "pwsh -NoProfile -File iba/app/ps/archive/Old-Thing.ps1", d, "deny"),
        ("retired .ps1 after another command", "cd x; .\\iba\\app\\ps\\archive\\Old-Thing.ps1", d, "deny"),
        ("read a retired file (cat)", f"cat {RETIRED}", d, "allow"),
        ("read a retired file (Get-Content)", "Get-Content iba\\app\\tools\\archive\\temp_2193_test_plan_run.py", d, "allow"),
        ("grep across archive", "grep -rn foo iba/app/tools/archive", d, "allow"),
        ("active PS script", ".\\iba\\app\\ps\\Escalation.ps1 -Action List", d, "allow"),
        ("active module (python -m)", "python -m iba.app.run escalation-reporting --step x", d, "allow"),
        ("python -c inline code", "python -c \"print(1)\"", d, "allow"),
        ("script outside the project", "python C:/Users/someone/AppData/Local/Temp/x.py", d, "allow"),
        ("no database: allow, logged", f"python {RETIRED}", str(scratch / "missing.db"), "allow"),
    ]
    rows, ok_all = [], True
    for name, cmd, dbp, expect in cases:
        got = run_hook(cmd, dbp)
        ok = got == expect
        ok_all &= ok
        rows.append(f"| {name} | `{cmd.replace('|', '/')}` | {expect} | {got} | {'pass' if ok else 'FAIL'} |")
    real = run_hook(".\\iba\\app\\ps\\Start-Iba.ps1", None)
    rows.append(f"| live DB: Start-Iba.ps1 (not yet registered) | `.\\iba\\app\\ps\\Start-Iba.ps1` | allow | {real} | {'pass' if real == 'allow' else 'FAIL'} |")
    ok_all &= real == "allow"
    lines = ["# #2200 test results: gate_retired_script.py", "",
             "Run by `iba/app/tools/temp_2200_gate_test.py` on 2026-10-21 against a backup-API copy "
             "of iba.db with three test escalations (approved by the researcher; 'approved' by Claude; "
             "approved then withdrawn), plus one case against the live DB.", "",
             "| case | command | expected | actual | result |", "|---|---|---|---|---|"] + rows
    OUT.write_text("\n".join(lines) + "\n", encoding="utf8")
    print("\n".join(lines))
    db.unlink()
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main(pathlib.Path(sys.argv[1])))
