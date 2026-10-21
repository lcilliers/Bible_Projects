"""temp_2186_control_file_check_test_run.py -- test plan for #2186 (SC15, control files), against a
COPY of iba.db (argv[1]) holding the #2186 settings. One-off; archived when #2186 closes.

Synthetic cases (a temporary project root with its own CLAUDE.md, CHARTER.md, GOVERNANCE.md and
.claude/commands/):
  S1 a clean set: no finding (apart from the real memory folder, filtered out)
  S2 a path that does not resolve
  S3 a pointer into archive/ without the history word; S4 the same line with it: no finding
  S5 struck-through text; S6 a 'Superseded 2026-..' note; S7 the same inside a code fence is
     still history text, but a fenced path is not checked
  S8 CLAUDE.md over the size limit
  S9 a missing control file
Real case:
  R1 the live control files -- printed for the record
"""
import json
import pathlib
import shutil
import sqlite3
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import cfgquality  # noqa: E402

c = sqlite3.connect(sys.argv[1])
res = []


def T(name, cond, detail=""):
    res.append((name, bool(cond), detail))


def run(root):
    return [(k, t) for k, t in cfgquality.find_control_file_problems(c, root) if not k.startswith("SC15:memory/")]


tmp = pathlib.Path(tempfile.mkdtemp())
(tmp / "iba/app").mkdir(parents=True)
(tmp / ".claude/commands").mkdir(parents=True)
(tmp / "archive/docs").mkdir(parents=True)
(tmp / "archive/docs/old.md").write_text("x", encoding="utf-8")
(tmp / "iba/app/BUILD.md").write_text("x", encoding="utf-8")
base = {"CLAUDE.md": "See [`iba/app/CHARTER.md`](iba/app/CHARTER.md).\n",
        "iba/app/CHARTER.md": "Objective.\n", "iba/app/GOVERNANCE.md": "See [BUILD.md](BUILD.md).\n",
        ".claude/commands/start-project.md": "Run `iba/app/GOVERNANCE.md`.\n"}


def write(over=None, drop=None):
    for rel, txt in {**base, **(over or {})}.items():
        p = tmp / rel
        if drop == rel:
            if p.exists():
                p.unlink()
            continue
        p.write_text(txt, encoding="utf-8")


write(); T("S1 clean set: no finding", not run(tmp), str(run(tmp))[:120])
write({"CLAUDE.md": base["CLAUDE.md"] + "Also `docs/missing-file.md`.\n"})
T("S2 unresolved path", any("does not resolve" in t for _, t in run(tmp)))
write({"CLAUDE.md": base["CLAUDE.md"] + "Old copy: `archive/docs/old.md`.\n"})
T("S3 archive pointer without the history word", any("archive" in t and "without" in t for _, t in run(tmp)))
write({"CLAUDE.md": base["CLAUDE.md"] + "Old copy (history): `archive/docs/old.md`.\n"})
T("S4 archive pointer marked as history: no finding", not run(tmp), str(run(tmp))[:120])
write({"iba/app/GOVERNANCE.md": "~~old~~ new\n"})
T("S5 struck-through text", any("history text" in t for _, t in run(tmp)))
write({"iba/app/GOVERNANCE.md": "Superseded 2026-10-01 by X.\n"})
T("S6 dated superseded note", any("history text" in t for _, t in run(tmp)))
write({".claude/commands/start-project.md": "```\n`nowhere/at-all.md`\n```\n"})
T("S7 a fenced path is not checked", not run(tmp), str(run(tmp))[:120])
limit = json.loads(c.execute("SELECT value FROM cfg_setting WHERE key='session_close.always_read_max_bytes'").fetchone()[0])
write({"CLAUDE.md": base["CLAUDE.md"] + ("x" * (limit + 1))})
T("S8 CLAUDE.md over the size limit", any(k.endswith(":size") for k, _ in run(tmp)))
write(drop="iba/app/CHARTER.md")
T("S9 missing control file", any(k.endswith(":missing") for k, _ in run(tmp)))
shutil.rmtree(tmp)

real = cfgquality.find_control_file_problems(c, ROOT)
for name, okv, d in res:
    print(("PASS " if okv else "FAIL ") + name + (f"  -- {d}" if d and not okv else ""))
print(f"{sum(o for _, o, _ in res)}/{len(res)} passed")
print(f"R1 live control files: {len(cfgquality.control_files(c, ROOT))} files, {len(real)} finding(s)")
for k, t in real:
    print("   ", t)
