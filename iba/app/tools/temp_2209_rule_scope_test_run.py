"""temp_2209_rule_scope_test_run.py -- test plan for escalation #2209 part (a): cfg_rule_scope (the
migration), cfgquality.find_rule_scope_gaps and the hook .claude/hooks/rules_at_point_of_use.py. Run on
a copy of iba.db made with lib/dbsnapshot.copy_db; the hook runs against the copy (IBA_RULES_DB) with
a scratch project folder, so no live DB, live state file or live report is written.

Usage: python iba/app/tools/temp_2209_rule_scope_test_run.py <scratch dir>
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
from iba.app.lib import dbsnapshot, cfgquality  # noqa: E402

scratch = pathlib.Path(sys.argv[1])
if scratch.exists():
    shutil.rmtree(scratch)
scratch.mkdir(parents=True)
APP = ROOT / "iba" / "app"
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/").replace("\n", " ")[:400]))


copy = dbsnapshot.copy_db(scratch / "iba.db")
# T1-T2: the migration ran on live before this run (archived scripts are gated, #2200); the copy
# carries its record. T1 drops the table on the copy to check the missing-table case.
conn = sqlite3.connect(copy)
logged = conn.execute("SELECT count(*) FROM cfg_change_detail WHERE run_id='DEVMODE-2209-RULE-SCOPE-20261021'").fetchone()[0]
case("T2", "migration's audited writes are on record (229) and the table exists",
     logged == 229 and conn.execute("SELECT 1 FROM sqlite_master WHERE name='cfg_rule_scope'").fetchone(), logged)
conn.execute("ALTER TABLE cfg_rule_scope RENAME TO cfg_rule_scope_t1")
case("T1", "with the table missing the check reports it",
     cfgquality.find_rule_scope_gaps(conn, APP) == ["cfg_rule_scope is missing (#2209)"],
     cfgquality.find_rule_scope_gaps(conn, APP))
conn.execute("ALTER TABLE cfg_rule_scope_t1 RENAME TO cfg_rule_scope")
conn.commit()
conn.close()

conn = sqlite3.connect(copy)
gaps = cfgquality.find_rule_scope_gaps(conn, APP)
n_links = conn.execute("SELECT count(*) FROM cfg_rule_scope").fetchone()[0]
n_gen = conn.execute("SELECT count(DISTINCT rule_ref) FROM cfg_rule_scope WHERE scope_kind='general'").fetchone()[0]
n_m_off = conn.execute("SELECT count(*) FROM cfg_method_rule m JOIN cfg_step s ON s.step=m.step "
                       "WHERE m.active=1 AND s.inactive=1").fetchone()[0]
case("T3", "after the migration: no gaps; method rules on retired steps deactivated",
     gaps == [] and n_m_off == 0, f"{n_links} links, {n_gen} general rules; gaps={gaps}")

# T4 synthetic gaps, each kind
conn.execute("UPDATE cfg_rule_scope SET inactive=1 WHERE rule_ref='B:63'")
conn.execute("INSERT INTO cfg_rule_scope (rule_ref, scope_kind, scope_value) VALUES ('B:9999','general','*')")
conn.execute("INSERT INTO cfg_rule_scope (rule_ref, scope_kind, scope_value) VALUES ('B:26','ps','Nope.ps1')")
conn.execute("UPDATE cfg_method_rule SET active=1 WHERE id=49")
g4 = cfgquality.find_rule_scope_gaps(conn, APP)
want = ["rule B:63 has no cfg_rule_scope link", "cfg_rule_scope links B:9999, which is missing or inactive",
        "names PS script Nope.ps1", "method rule 49"]
case("T4", "synthetic: unlinked rule, link to missing rule, unknown PS script, method rule on retired step",
     all(any(w in g for g in g4) for w in want) and len(g4) == 4, g4)
conn.rollback()
conn.close()

# ── hook, against the copy ──
proj = scratch / "proj"
(proj / ".claude").mkdir(parents=True)
(proj / "iba" / "app").mkdir(parents=True)
shutil.copy(APP / "USER-GUIDE.md", proj / "iba" / "app" / "USER-GUIDE.md")
hook = ROOT / ".claude" / "hooks" / "rules_at_point_of_use.py"
env = {**os.environ, "IBA_RULES_DB": str(copy)}


def run(tool, tin, session="S1", e=None):
    p = subprocess.run([sys.executable, str(hook)], input=json.dumps(
        {"cwd": str(proj), "session_id": session, "tool_name": tool, "tool_input": tin}),
        capture_output=True, text=True, env=e or env)
    out = json.loads(p.stdout or "{}")
    hs = out.get("hookSpecificOutput", {})
    return hs.get("permissionDecision", "allow"), hs.get("permissionDecisionReason", "")


upd = {"command": ".\\iba\\app\\ps\\Escalation.ps1 -Action Update -Id 5 -AnsweredBy Claude"}
d, r = run("PowerShell", upd)
case("H1", "first Escalation Update: refused with its rules (63, 45, escalation 13) and only the Update usage",
     d == "deny" and "B:63" in r and "B:45" in r and "E:13" in r and "-Action Update" in r and "B:19" not in r
     and "How to run Escalation.ps1 (" not in r and "-Action Raise" not in r,
     f"{d}; {len(r)} chars; refs: {sorted(set(l.split(' ')[1] for l in r.splitlines() if l.startswith('- ')))}")
d, _ = run("PowerShell", upd)
case("H2", "the same call re-issued passes", d == "allow", d)
d, r = run("PowerShell", {"command": ".\\iba\\app\\ps\\Escalation.ps1 -Action Raise -Question x"})
case("H3", "a new action of the same tool: only its usage is new, so refused once with the usage",
     d == "deny" and "-Action Raise" in r and "B:63" not in r, f"{d}; {r[:200]}")
d, r = run("Write", {"file_path": str(proj / "_analytics" / "Clusters" / "M02 - anger-wrath" / "x.md")})
case("H4", "a write under _analytics/Clusters: refused with the study and filing rules",
     d == "deny" and "B:69" in r and "G:report.cluster_folder_naming_convention" in r and "B:56" in r,
     f"{d}; {len(r)} chars")
d, r = run("Edit", {"file_path": str(proj / "iba" / "app" / "lib" / "x.py")})
case("H5", "an edit under iba/app: refused with the build rules (BUILD.md, USER-GUIDE, test plan)",
     d == "deny" and "G:governance.build_md_on_code_change" in r and "B:42" in r and "B:46" in r, f"{d}; {len(r)} chars")
d, r = run("Bash", {"command": "git commit -m x && git push"})
d2, _ = run("Bash", {"command": "git commit -m y"})
case("H6", "git commit: refused once with rule 26, then passes", d == "deny" and "B:26" in r and d2 == "allow",
     f"{d} -> {d2}")
d, _ = run("Bash", {"command": "ls -la"})
case("H7", "a call with no governed operation passes", d == "allow", d)
d, r = run("PowerShell", upd, session="S2")
case("H8", "a new session shows the rules again", d == "deny" and "B:63" in r, d)
d, _ = run("PowerShell", upd, session="S3", e={**os.environ, "IBA_RULES_DB": str(scratch / "missing.db")})
case("H9", "no database: the call passes (a broken check never blocks)", d == "allow", d)
d, r = run("Bash", {"command": "python -c \"import sqlite3; sqlite3.connect('iba/app/db/iba.db')\""}, session="S4")
case("H10", "a database query: refused once with the database rules (11, 13, 61, 67)",
     d == "deny" and all(f"B:{n}" in r for n in (11, 13, 61, 67)), d)
d, r = run("PowerShell", {"command": ".\\iba\\app\\ps\\ClusterSubgroup.ps1 -Step Reading"}, session="S5")
case("H11", "a PS tool brings the method rules of its steps", d == "deny" and "M:" in r,
     f"{d}; {sum(1 for l in r.splitlines() if l.startswith('- M:'))} method rules")
d, _ = run("Write", {"file_path": "C:/Windows/Temp/x.txt"}, session="S6")
case("H12", "a write outside the project passes", d == "allow", d)

heredoc = ("cat >> iba/app/BUILD.md <<'EOF'\nIt finds a PS script with -Action, git\ncommit/push, a migration.\n"
           "See Escalation.ps1 -Action Update and python iba/app/migration/x.py and iba.db.\nEOF")
d, r = run("Bash", {"command": heredoc}, session="S7")
case("H13", "text that only mentions git, a PS tool, a migration or a database (a heredoc body) passes",
     d == "allow", f"{d}; {r[:150]}")
d, r = run("Bash", {"command": "cd /c/Bible_study_projects && git commit -q -m x"}, session="S8")
case("H14", "git after cd ... && is a command: refused once", d == "deny" and "B:26" in r, d)
ps_here = "$c = @'\nResearcher said: git commit later\n'@\n.\\iba\\app\\ps\\Escalation.ps1 -Action Update -Id 1 -Comment $c"
d, r = run("PowerShell", {"command": ps_here}, session="S9")
case("H15", "a PS call after a here-string is found with its action; the here-string text is not",
     d == "deny" and "-Action Update" in r and "B:26" not in r, f"{d}; refs B:63={'B:63' in r}")
d, r = run("Bash", {"command": "python iba/app/migration/x_v1_20261021.py --db y.db"}, session="S10")
case("H16", "a migration run: refused once with the migration rules (75, 62)",
     d == "deny" and "B:75" in r and "B:62" in r and "B:11" not in r, d)

out = scratch / "results.md"
out.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" +
               "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in results) + "\n", encoding="utf-8")
print(out.read_text(encoding="utf-8"))
print(f"{sum(r[2] == 'PASS' for r in results)}/{len(results)} pass")
