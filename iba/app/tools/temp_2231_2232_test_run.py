"""temp_2231_2232_test_run.py -- tests for escalations #2231 (cfg_table ib_observation use text) and #2232
(file_manifest: an archive/ segment overrides a folder_purpose currency). Run on a copy of iba.db made with
lib/dbsnapshot.copy_db; the manifest rebuild on the copy scans the real project tree read-only.

Usage: python iba/app/tools/temp_2231_2232_test_run.py <scratch dir>
"""
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
from iba.app.lib import manifest  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2231"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:400]))


# #2231
env = {**os.environ, "PYTHONPATH": str(ROOT)}
mig = ROOT / "iba/app/migration/ib_observation_use_2231_v1_20261023.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
o = [subprocess.run([sys.executable, str(mig), "--db", str(DB)], capture_output=True, text=True, env=env).stdout.strip()
     for _ in range(2)]
case("A1", "#2231 migration: applied (or already), then skipped", ("applied" in o[0] or "already" in o[0]) and "already" in o[1], o)
c = sqlite3.connect(DB)
row = c.execute("SELECT grain, use FROM cfg_table WHERE database='iba' AND name='ib_observation'").fetchone()
grants = [r[0] for r in c.execute("SELECT writer FROM cfg_write_grant WHERE table_name='ib_observation' AND inactive=0")]
case("A2", "#2231 iba row: grain set; the use names every live writer step", row[0] == "one row per observation"
     and all(g in row[1] for g in grants), f"grain {row[0]!r}; writers {grants}")
br = c.execute("SELECT inactive, substr(use,1,40) FROM cfg_table WHERE database='bible_research' AND name='ib_observation'").fetchone()
case("A3", "#2231 the bible_research row (inactive) untouched", br[0] == 1 and br[1].startswith("A small transitional"), br)
c.close()

# #2232 synthetic
for path, want in (("a/archive/x.md", True), ("archive/x.md", True), ("a/Archive/x.md", True),
                   ("a/_archive/x.md", False), ("a/archives/x.md", False), ("a/b/x.md", False)):
    case(f"B1 {path}", "in_archive", manifest.in_archive(path) == want, manifest.in_archive(path))

# #2232 real: rebuild on the copy
c = sqlite3.connect(DB)
before = dict(c.execute("SELECT path, archived FROM file_manifest").fetchall())
before_cur = dict(c.execute("SELECT path, currency FROM file_manifest").fetchall())
c.close()
cfg = Cfg(DB)
summary = manifest.rebuild(cfg)
c = sqlite3.connect(DB)
after = dict(c.execute("SELECT path, archived FROM file_manifest").fetchall())
after_cur = dict(c.execute("SELECT path, currency FROM file_manifest").fetchall())
left = c.execute("SELECT count(*) FROM file_manifest WHERE (lower(path) LIKE 'archive/%' OR lower(path) LIKE '%/archive/%') AND archived=0").fetchone()[0]
case("B2", "rebuild: no file under an archive/ segment left unarchived", left == 0, f"{left} left; total {summary['total']}")
under = c.execute("SELECT count(*), sum(currency='current') FROM file_manifest WHERE lower(path) LIKE '%/_archive/%'").fetchone()
case("B3", "files under _archive/ keep their folder_purpose currency (current)", under[0] == under[1], under)
common = set(before) & set(after)
changed = [p for p in common if before_cur[p] != after_cur[p]]
odd = [p for p in changed if not manifest.in_archive(p) or after_cur[p] != "archived"]
case("B4", "every row whose currency changed is under an archive/ segment and is now archived", not odd,
     f"{len(changed)} changed, {len(odd)} otherwise: {odd[:5]}")
case("B5", "the 664 _analytics archive rows found in the discovery are now archived",
     c.execute("SELECT count(*) FROM file_manifest WHERE path LIKE '_analytics/%' AND path LIKE '%/archive/%' AND ext='.md' AND archived=0").fetchone()[0] == 0,
     f"{sum(1 for p in changed if p.startswith('_analytics/'))} _analytics rows changed")

lines = ["| # | case | result | evidence |", "|---|---|---|---|"] + [f"| {a} | {b} | {r} | {e} |" for a, b, r, e in results]
(S / "results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
print(f"\n{sum(r[2] == 'PASS' for r in results)}/{len(results)} PASS")
