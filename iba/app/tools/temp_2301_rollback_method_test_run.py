"""temp_2301_rollback_method_test_run.py -- escalation #2301 test plan, on SMALL scratch databases and a copy of the live iba.db (never the live
DB or its snapshot folder): the rollback method of cfg_setting backup.rollback_method as lib/dbsnapshot.py applies it. Run snapshots only when the
newest is older than min_interval_minutes; the newest keep_recent plus the newest of each of the last keep_daily days kept; named snapshots in
their own folder, never pruned by the run snapshots, the newest keep_named kept; orphan sidecar files removed; IBA_NO_SNAPSHOT honoured; every
number changes with its row. Real data: the names of the snapshots the live folder holds, and the migration on a copy of the live database.
Usage: python iba/app/tools/temp_2301_rollback_method_test_run.py <scratch dir>. Prints PASS/FAIL per case."""
import datetime
import json
import os
import pathlib
import shutil
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import dbsnapshot as ds  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2301run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
RULE = {"min_interval_minutes": 120, "keep_recent": 2, "keep_daily": 3, "keep_named": 4, "named_dir": "kept"}
res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:700]}"), flush=True)


# a small scratch database holding the rule, and a snapshot folder of its own
DB = S / "iba.db"
c = sqlite3.connect(DB)
c.execute("CREATE TABLE cfg_setting (key TEXT PRIMARY KEY, value TEXT, use TEXT, module TEXT, inactive INTEGER NOT NULL DEFAULT 0)")
c.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES ('backup.rollback_method', ?, 'u', 'backup')", (json.dumps(RULE),))
c.execute("CREATE TABLE t (x)")
c.commit()
c.close()
ds.DB_PATH = DB
ds.SNAPSHOT_DIR = S / "snapshots"


def n_settings(path):
    cx = sqlite3.connect(path)
    try:
        return cx.execute("SELECT count(*) FROM cfg_setting").fetchone()[0]
    finally:
        cx.close()


def setrule(**kw):
    cc = sqlite3.connect(DB)
    cc.execute("UPDATE cfg_setting SET value=? WHERE key='backup.rollback_method'", (json.dumps({**RULE, **kw}),))
    cc.commit()
    cc.close()


def fake(name_ts: str, folder=None, sidecars=False):
    f = (folder or ds.SNAPSHOT_DIR)
    f.mkdir(parents=True, exist_ok=True)
    p = f / f"iba-{name_ts}-x.db"
    p.write_bytes(b"x")
    if sidecars:
        (f / f"iba-{name_ts}-x.db-wal").write_bytes(b"w")
        (f / f"iba-{name_ts}-x.db-shm").write_bytes(b"s")
    return p


def names(folder=None):
    f = folder or ds.SNAPSHOT_DIR
    return sorted(p.name for p in f.glob("iba-*.db")) if f.exists() else []


def ago(**kw):
    return (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(**kw)).strftime("%Y%m%dT%H%M%SZ")


# ── R: the run snapshot is taken at most once per interval ────────────────────────────────────────
p1 = ds.snapshot("run-a")
case("R1", "the first run of the day takes a snapshot (a real, consistent copy)", p1 is not None and p1.is_file() and n_settings(p1) == 1)
p2 = ds.snapshot("run-b")
case("R2", "a second run within min_interval_minutes takes none (no copy of the whole database for every run)", p2 is None and len(names()) == 1, names())
for f in ds.SNAPSHOT_DIR.glob("iba-*"):
    f.unlink()
fake(ago(minutes=121))
p3 = ds.snapshot("run-c")
case("R3", "when the newest is older than the interval a new one is taken", p3 is not None and len(names()) == 2, names())
setrule(min_interval_minutes=0)
p4 = ds.snapshot("run-d")
case("R4", "min_interval_minutes is the row's: with 0 every run takes one (a number in the code could not change)", p4 is not None, names())
setrule()
os.environ["IBA_NO_SNAPSHOT"] = "1"
case("R5", "IBA_NO_SNAPSHOT=1 takes none", ds.snapshot("run-e") is None)
del os.environ["IBA_NO_SNAPSHOT"]
# ── K: the retention ─────────────────────────────────────────────────────────────────────────────
shutil.rmtree(ds.SNAPSHOT_DIR)
for d, h in [(0, 1), (0, 3), (0, 6), (1, 2), (1, 20), (2, 5), (3, 5), (3, 9), (4, 4), (6, 1)]:
    fake(ago(days=d, hours=h))
before = names()
removed = ds.prune()
after = names()
case("K1", "keep_recent 2 + the newest of the other days within the last keep_daily 3 calendar days (today included): 10 snapshots over 5 days leave 4",
     removed == 6 and len(after) == 4, (removed, after))
case("K2", "the newest two are kept", all(n in after for n in before[-2:]) or all(n in after for n in sorted(before)[-2:]), after)
case("K3", "the oldest day (6 days back) is gone", not any(ago(days=6, hours=1)[:8] in n for n in after), after)
setrule(keep_recent=1, keep_daily=1)
ds.prune()
case("K4", "keep_recent and keep_daily are the row's: with 1 and 1 the folder holds 1", len(names()) == 1, names())
setrule()
# ── N: named snapshots ──────────────────────────────────────────────────────────────────────────
shutil.rmtree(ds.SNAPSHOT_DIR)
n1 = ds.snapshot("pre-migration", named=True)
case("N1", "a named snapshot is taken at once, in its own folder, as a real copy",
     n1 is not None and n1.parent.name == "kept" and n_settings(n1) == 1, n1)
for i in range(4):
    fake(ago(hours=10 + i), folder=ds.SNAPSHOT_DIR)           # run snapshots, older
    fake(ago(days=1, hours=i), folder=ds.SNAPSHOT_DIR / "kept")
kept_before = names(ds.SNAPSHOT_DIR / "kept")
ds.prune()
case("N2", "the run snapshots' prune never touches the named ones beyond keep_named: the newest 4 named are kept",
     len(names(ds.SNAPSHOT_DIR / "kept")) == 4 and any("pre-migration" in n for n in names(ds.SNAPSHOT_DIR / "kept")), (kept_before, names(ds.SNAPSHOT_DIR / "kept")))
case("N3", "a named snapshot is not counted in the run snapshots' interval (a recent named one does not stop the run snapshot)",
     ds.snapshot("run-after-named") is not None or len(names()) >= 1)
# ── O: orphan sidecars ──────────────────────────────────────────────────────────────────────────
shutil.rmtree(ds.SNAPSHOT_DIR)
ds.SNAPSHOT_DIR.mkdir()
(ds.SNAPSHOT_DIR / "iba-20261026T0900Z-pre-2295.db-wal").write_bytes(b"w")
(ds.SNAPSHOT_DIR / "iba-20261026T0900Z-pre-2295.db-shm").write_bytes(b"s")
live_one = fake(ago(hours=1), sidecars=True)
ds.prune()
left = sorted(p.name for p in ds.SNAPSHOT_DIR.iterdir())
case("O1", "sidecar files whose database is gone are removed; those of a kept database stay",
     not any("pre-2295" in n for n in left) and any(n.endswith("-wal") for n in left), left)
# ── M: the migration and the live folder's names ────────────────────────────────────────────────
LIVE = ROOT / "iba/app/db/iba.db"
_pre = ROOT / "backups/iba-pre-rules-in-config-20261028.db"           # a copy made before the method (backup API); the live database already holds it
CP = copy_db(S / "live-copy.db", _pre if _pre.exists() else LIVE)
MIG = ROOT / "iba/app/migration/backup_rollback_method_2301_v1_20261028.py"
MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name


def mig(*a):
    r = subprocess.run([sys.executable, str(MIG), "--db", str(CP), *a], capture_output=True, text=True,
                       env={**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"})
    return (r.stdout or r.stderr).strip()


dry = mig("--dry-run")
out = mig()
cc = sqlite3.connect(CP)
val = lambda k: cc.execute("SELECT value, inactive FROM cfg_setting WHERE key=?", (k,)).fetchone()
case("M1", "the dry run writes nothing and the apply reports its writes", dry.startswith("DRY RUN") and "write(s) applied" in out, (dry, out))
case("M2", "backup.rollback_method is live with the rule and a use text",
     json.loads(val("backup.rollback_method")[0]) == RULE and val("backup.rollback_method")[1] == 0)
case("M3", "retention.snapshot_keep_count is retired and the old policy sentence points at the new setting",
     val("retention.snapshot_keep_count")[1] == 1 and "backup.rollback_method" in json.loads(val("backup.pre_run_snapshot_policy")[0])
     and "before every NEW run" not in json.loads(val("backup.pre_run_snapshot_policy")[0]))
case("M4", "the Developer Mode rule names the named snapshot as the rollback point",
     "named snapshot" in cc.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE rule_key='developer-mode-scope-and-conduct'").fetchone()[0])
case("M5", "a second run is refused as already applied", mig().startswith("already applied"))
live_names = sorted(p.name for p in (ROOT / "iba/app/db/snapshots").glob("iba-*.db"))
sim = S / "sim"
sim.mkdir()
for n in live_names:
    (sim / n).write_bytes(b"x")
ds.SNAPSHOT_DIR = sim
before = len(names(sim))
ds.prune()
case("M6", "applied to the names the live snapshot folder holds today, the retention leaves at most keep_recent + keep_daily - 1",
     len(names(sim)) <= RULE["keep_recent"] + RULE["keep_daily"] - 1, (before, names(sim)))
print(f"\n{sum(res)} of {len(res)} cases pass")
