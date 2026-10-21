"""temp_2193_test_plan_run.py -- runs the #2193 test plan for iba/app/lib/dbsnapshot.py copy_db and
snapshot, and writes the per-case results to the escalation's results file. Temporary: archived
once its results are on #2193.

Usage:  python iba/app/tools/temp_2193_test_plan_run.py SCRATCH_DIR
"""
import os
import pathlib
import shutil
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import dbsnapshot  # noqa: E402
from iba.app.lib.cfg import DB_PATH  # noqa: E402

OUT = ROOT / "outputs/escalation/2193-copy-db-test-results-v1-20261021.md"
results = []


def one(path, sql):
    conn = sqlite3.connect(path)
    try:
        return conn.execute(sql).fetchone()[0]
    finally:
        conn.close()


def case(name, expected, actual, ok):
    results.append((name, expected, actual, "pass" if ok else "FAIL"))


def main(scratch: pathlib.Path) -> int:
    scratch.mkdir(parents=True, exist_ok=True)
    for f in scratch.glob("t2193-*"):
        f.unlink()

    # 1. synthetic: a committed row still in the WAL
    src = scratch / "t2193-wal.db"
    w = sqlite3.connect(src)
    w.execute("PRAGMA journal_mode=WAL")
    w.execute("PRAGMA wal_autocheckpoint=0")
    w.execute("CREATE TABLE t (x)")
    w.commit()
    w.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    w.execute("INSERT INTO t VALUES (1)")
    w.commit()                                   # committed, but only in t2193-wal.db-wal
    plain = scratch / "t2193-plain.db"
    shutil.copy2(src, plain)
    n_plain = one(plain, "SELECT count(*) FROM t")
    backed = dbsnapshot.copy_db(scratch / "t2193-backup.db", src)
    n_backed = one(backed, "SELECT count(*) FROM t")
    w.close()
    case("WAL row: plain file copy", "0 rows (misses the WAL write)", f"{n_plain} rows", n_plain == 0)
    case("WAL row: copy_db", "1 row", f"{n_backed} rows", n_backed == 1)

    # 2. refuses to overwrite
    try:
        dbsnapshot.copy_db(backed, src)
        case("copy_db onto an existing file", "FileExistsError", "no error", False)
    except FileExistsError:
        case("copy_db onto an existing file", "FileExistsError", "FileExistsError", True)

    # 3. real: live iba.db
    real = dbsnapshot.copy_db(scratch / "t2193-real.db")
    live = sqlite3.connect(f"file:{DB_PATH.as_posix()}?mode=ro", uri=True)
    copy = sqlite3.connect(real)
    tables = [r[0] for r in live.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
    diff = [t for t in tables if live.execute(f'SELECT count(*) FROM "{t}"').fetchone()
            != copy.execute(f'SELECT count(*) FROM "{t}"').fetchone()]
    integrity = copy.execute("PRAGMA quick_check").fetchone()[0]
    live.close()
    copy.close()
    case("live iba.db: row counts, every table", f"{len(tables)} tables equal",
         f"{len(tables) - len(diff)} equal, differ: {diff or 'none'}", not diff)
    case("live iba.db copy: quick_check", "ok", integrity, integrity == "ok")

    # 4. snapshot() writes through copy_db (snapshot dir pointed at scratch)
    keep_dir = dbsnapshot.SNAPSHOT_DIR
    dbsnapshot.SNAPSHOT_DIR = scratch / "t2193-snapshots"
    try:
        snap = dbsnapshot.snapshot("t2193", keep=5)
        ok = snap is not None and snap.exists() and one(snap, "PRAGMA quick_check") == "ok"
        case("snapshot()", "a snapshot that passes quick_check", str(snap.name if snap else None), ok)
        os.environ["IBA_NO_SNAPSHOT"] = "1"
        skipped = dbsnapshot.snapshot("t2193-skip", keep=5)
        case("snapshot() with IBA_NO_SNAPSHOT=1", "None", str(skipped), skipped is None)
    finally:
        os.environ.pop("IBA_NO_SNAPSHOT", None)
        shutil.rmtree(dbsnapshot.SNAPSHOT_DIR, ignore_errors=True)
        dbsnapshot.SNAPSHOT_DIR = keep_dir

    # 5. CLI --copy-to
    cli_dest = scratch / "t2193-cli.db"
    r = subprocess.run([sys.executable, "-m", "iba.app.lib.dbsnapshot", "--copy-to", str(cli_dest)],
                       cwd=ROOT, capture_output=True, text=True)
    case("CLI --copy-to", "exit 0, file written", f"exit {r.returncode}, exists={cli_dest.exists()}",
         r.returncode == 0 and cli_dest.exists())

    for f in scratch.glob("t2193-*"):
        if f.is_file():
            f.unlink()

    lines = ["# #2193 test results: dbsnapshot.copy_db and snapshot", "",
             "Run by `iba/app/tools/temp_2193_test_plan_run.py` on 2026-10-21, against "
             "`iba/app/lib/dbsnapshot.py` as changed under #2193.", "",
             "| case | expected | actual | result |", "|---|---|---|---|"]
    lines += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in results]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf8")
    print("\n".join(lines))
    return 0 if all(r[3] == "pass" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(pathlib.Path(sys.argv[1])))
