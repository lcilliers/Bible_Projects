"""temp_2361_manifest_test_run.py -- tests for escalation #2361 stage 1c: manifest.rebuild updates file_manifest BY PATH and keeps the
analytic columns (module, run_id, sha256, analytic_status, migrated_from) of a file that is still there; register_analytic sets them.
Part A uses an in-memory table and synthetic scan entries; part B runs the real rebuild on a copy of iba.db made with
lib/dbsnapshot.copy_db (the scan reads the real project tree, read-only).

Usage: python iba/app/tools/temp_2361_manifest_test_run.py <scratch dir>
"""
import pathlib
import shutil
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import manifest  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


def entry(path, size=10, cur="current"):
    return {"path": path, "category": "other", "file_type": "x", "currency": cur, "archived": 0, "registry": None, "word": None,
            "cluster": None, "vcb_batch": None, "version": None, "date": None, "ext": ".md", "size_bytes": size,
            "modified_at": "2026-11-06T00:00:00Z"}


# ---- part A: the rules, on an in-memory table ------------------------------------------------------------------------------
c = sqlite3.connect(":memory:")
c.execute("""CREATE TABLE file_manifest (path TEXT PRIMARY KEY, category TEXT NOT NULL, file_type TEXT NOT NULL, currency TEXT NOT NULL,
  archived INTEGER NOT NULL DEFAULT 0, registry INTEGER, word TEXT, cluster TEXT, vcb_batch INTEGER, version TEXT, date TEXT, ext TEXT,
  size_bytes INTEGER NOT NULL, modified_at TEXT NOT NULL, scanned_at TEXT NOT NULL, module TEXT, run_id TEXT, sha256 TEXT,
  analytic_status TEXT, migrated_from TEXT)""")
r = manifest.apply_entries(c, [entry("a/keep.json", 10), entry("a/gone.json", 5)], "T1")
case("A1", "first scan adds every path", r == {"added": 2, "removed": 0, "kept": 0}, r)
ok_ = manifest.register_analytic(c, "a/keep.json", module="collection", run_id="R1", sha256="abc", analytic_status="live", migrated_from="old/keep.json")
case("A2", "register_analytic sets the five columns and says so", ok_ is True and c.execute(
    "SELECT module, run_id, sha256, analytic_status, migrated_from FROM file_manifest WHERE path='a/keep.json'").fetchone() == ("collection", "R1", "abc", "live", "old/keep.json"), ok_)
case("A3", "register_analytic on a path not in the manifest returns False", manifest.register_analytic(
    c, "no/such.json", module="group", run_id="R", sha256="x", analytic_status="live") is False, "")
r = manifest.apply_entries(c, [entry("a/keep.json", 99), entry("a/new.json", 1)], "T2")
row = c.execute("SELECT size_bytes, scanned_at, module, run_id, sha256, analytic_status, migrated_from FROM file_manifest WHERE path='a/keep.json'").fetchone()
case("A4", "a rebuild updates the scanned columns of a kept path and leaves the analytic columns alone",
     row == (99, "T2", "collection", "R1", "abc", "live", "old/keep.json"), row)
case("A5", "a new path is added, a path no longer on disk is removed", r == {"added": 1, "removed": 1, "kept": 1} and
     c.execute("SELECT count(*) FROM file_manifest WHERE path='a/gone.json'").fetchone()[0] == 0, r)
case("A6", "a new path has empty analytic columns", c.execute(
    "SELECT module, run_id, sha256, analytic_status, migrated_from FROM file_manifest WHERE path='a/new.json'").fetchone() == (None,) * 5, "")
r2 = manifest.apply_entries(c, [entry("a/keep.json", 99), entry("a/new.json", 1)], "T3")
case("A7", "the same scan again changes nothing but the scan time", r2 == {"added": 0, "removed": 0, "kept": 2}, r2)
r3 = manifest.apply_entries(c, [entry("a/moved.json", 99), entry("a/new.json", 1)], "T4")
case("A8", "a moved file is a new path: the old row, with its analytic columns, goes, and the new one starts empty",
     r3 == {"added": 1, "removed": 1, "kept": 1} and c.execute("SELECT module FROM file_manifest WHERE path='a/moved.json'").fetchone() == (None,), r3)
case("A9", "the scanned-column list and the analytic-column list do not overlap", not set(manifest._SCAN_COLS) & set(manifest.ANALYTIC_COLS), "")
c.close()

# ---- part B: the real rebuild on a copy -------------------------------------------------------------------------------------
S = pathlib.Path(sys.argv[1]) / "t2361"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
cfg = Cfg(DB)
live = sqlite3.connect(DB)
cnt0 = live.execute("SELECT count(*) FROM file_manifest").fetchone()[0]
sample = live.execute("SELECT path FROM file_manifest WHERE archived=0 AND path LIKE 'iba/app/lib/%' ORDER BY path LIMIT 1").fetchone()[0]
manifest.register_analytic(live, sample, module="collection", run_id="TEST", sha256="deadbeef", analytic_status="regenerable", migrated_from="x/y")
live.commit()
live.close()
summary = manifest.rebuild(cfg)
live = sqlite3.connect(DB)
row = live.execute("SELECT module, run_id, sha256, analytic_status, migrated_from FROM file_manifest WHERE path=?", (sample,)).fetchone()
case("B1", "real rebuild: the registered columns of a file that is still there survive", row == ("collection", "TEST", "deadbeef", "regenerable", "x/y"), row)
n = live.execute("SELECT count(*) FROM file_manifest").fetchone()[0]
case("B2", "real rebuild: the table equals the scan", n == summary["total"], f"{n} rows, scan {summary['total']}")
case("B3", "real rebuild: the summary counts what changed", summary["added"] + summary["kept"] == summary["total"] and summary["removed"] >= 0, {k: summary[k] for k in ("added", "removed", "kept")})
summary2 = manifest.rebuild(cfg)
case("B4", "a second real rebuild adds and removes nothing", summary2["added"] == 0 and summary2["removed"] == 0, {k: summary2[k] for k in ("added", "removed", "kept")})
live.close()

width = max(len(r[0]) for r in results)
fails = [r for r in results if r[2] == "FAIL"]
for cid, desc, res, ev in results:
    print(f"{cid:<{width}}  {res}  {desc}  [{ev}]")
print(f"\n{len(results) - len(fails)} of {len(results)} pass")
sys.exit(1 if fails else 0)
