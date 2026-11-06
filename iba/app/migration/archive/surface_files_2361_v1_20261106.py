"""surface_files_2361_v1_20261106.py -- escalation #2361, stage 0 (researcher, chat 2026-11-06: "Apply as proposed").

Moves the surface-cycle working files from outputs/concept-mapping/ to the _analytics/surfaces branch by the mapping table of the
stage 0 sweep (outputs/escalation/2361-stage0-file-mapping-v1-20261106.csv, report 2361-stage0-sweep-v1-20261106.md):
    working_files/<module>/import     import sources, read once by the load and then no input
    working_files/collection/embeddings  the regenerable embedding cache
    exports, exports/documents         inspection workbooks and analysis documents
    discarded                          methods that will not be needed again (moved, not deleted, not registered)
Files already in an archive folder stay where they are. A tracked file moves with `git mv`, an untracked one with a plain move;
the sha256 of every file is checked before and after, a destination that exists with other content refuses the whole run, and every
move is written to Logs/ so it can be reversed (--undo LOG). Registers, through configmaint.apply_logged(): the settings
surfaces.working_files_root, surfaces.exports_root, surfaces.discarded_root, the move of cfg_setting surface_judge.batch_dir to
the new group import folder (the two registered tools Surface-Judge and Surface-Base read their batch files from it; the base
files sit in base/import and are read by the rewritten base module, stage 3), and the migration's own cfg_utility row.
Idempotent. The folders are registered afterwards through FolderPurpose.ps1 and the manifest through Manifest-Rebuild.ps1.

Usage:
    python iba/app/migration/surface_files_2361_v1_20261106.py [--db PATH] [--dry-run]
    python iba/app/migration/surface_files_2361_v1_20261106.py --undo Logs/2361-stage0-moves-<time>.csv
"""
import argparse
import csv
import datetime
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-SURFACE-FILES-20261106"
MODULE = "surface_files_2361_v1_20261106"
MAPPING = ROOT / "outputs" / "escalation" / "2361-stage0-file-mapping-v1-20261106.csv"
NEW_BATCH_DIR = "_analytics/surfaces/working_files/group/import"
SETTINGS = [
    ("surfaces.working_files_root", "_analytics/surfaces/working_files",
     "the one folder under which every working file of the surface cycle is written (#2361): a subfolder per module (group, "
     "structure, base, collection), import/ for the only place a file may be read as an input, embeddings/ for regenerable caches"),
    ("surfaces.exports_root", "_analytics/surfaces/exports",
     "the folder for the results of surface analysis made for inspection (workbooks, reports, analysis documents) (#2361)"),
    ("surfaces.discarded_root", "_analytics/surfaces/discarded",
     "where the files of a method that will not be needed again are kept, moved and never deleted, outside the file registry and "
     "outside every read path (#2361; the researcher, 2026-11-06)"),
]


def sha(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)


def tracked() -> set[str]:
    return set(git("ls-files", "outputs/concept-mapping").stdout.split("\n"))


def plan_moves():
    rows = list(csv.DictReader(open(MAPPING, encoding="utf-8")))
    moves, problems = [], []
    for r in rows:
        if r["class"] == "K" or not r["path after the move"]:
            continue
        src, dst = ROOT / r["path now"], ROOT / r["path after the move"]
        if not src.exists():
            if dst.exists():
                continue  # already moved
            problems.append(f"missing: {r['path now']}")
            continue
        if dst.exists() and sha(dst) != sha(src):
            problems.append(f"destination exists with other content: {r['path after the move']}")
            continue
        moves.append((r["path now"], r["path after the move"], r["class"]))
    return moves, problems


def plan_cfg(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use,
                                                      "module": "surfaces", "inactive": 0}))
    cur = conn.execute("SELECT value FROM cfg_setting WHERE key='surface_judge.batch_dir'").fetchone()
    if cur and json.loads(cur[0]) != NEW_BATCH_DIR:
        ops.append(("cfg_setting", "update", {"key": "surface_judge.batch_dir"}, {"value": json.dumps(NEW_BATCH_DIR)}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "purpose": f"ONE-OFF migration -- escalation #2361 stage 0: moves the surface-cycle working files to the "
                       f"_analytics/surfaces branch by the sweep mapping; run_id {RUN_ID}.",
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def do_move(old: str, new: str, tr: set[str]) -> tuple[str, str]:
    src, dst = ROOT / old, ROOT / new
    before = sha(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    is_tracked = old in tr
    if is_tracked:
        r = git("mv", old, new)
        if r.returncode:
            raise RuntimeError(f"git mv {old}: {r.stderr.strip()}")
    else:
        shutil.move(str(src), str(dst))
    if sha(dst) != before:
        raise RuntimeError(f"checksum differs after the move: {new}")
    return before, "git" if is_tracked else "plain"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--undo", help="a move log (Logs/2361-stage0-moves-*.csv) to reverse")
    a = ap.parse_args()
    if a.undo:
        rows = list(csv.DictReader(open(a.undo, encoding="utf-8")))
        for r in reversed(rows):
            src, dst = ROOT / r["new path"], ROOT / r["old path"]
            dst.parent.mkdir(parents=True, exist_ok=True)
            if r["how"] == "git":
                x = git("mv", r["new path"], r["old path"])
                if x.returncode:
                    raise RuntimeError(x.stderr)
            else:
                shutil.move(str(src), str(dst))
        print(f"undone: {len(rows)} file(s) moved back (the cfg writes are in cfg_change_detail and are not undone here)")
        return 0
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    moves, problems = plan_moves()
    ops = plan_cfg(conn)
    by = {}
    for _, _, c in moves:
        by[c] = by.get(c, 0) + 1
    if problems:
        print("REFUSED, nothing moved:")
        for p in problems:
            print("  " + p)
        return 2
    if a.dry_run:
        print(f"DRY RUN: {len(moves)} file(s) to move {by}; {len(ops)} cfg write(s)")
        for o, n, c in moves[:8]:
            print(f"  [{c}] {o} -> {n}")
        print("  ...")
        return 0
    if not moves and not ops:
        print("already applied: nothing changed")
        return 0
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    log = ROOT / "Logs" / f"2361-stage0-moves-{now}.csv"
    tr = tracked()
    done = []
    try:
        for o, n, c in moves:
            digest, how = do_move(o, n, tr)
            done.append((o, n, c, how, digest))
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.commit()
    except Exception:
        # put back what moved, so the tree and the config agree
        for o, n, c, how, digest in reversed(done):
            if how == "git":
                git("mv", n, o)
            else:
                shutil.move(str(ROOT / n), str(ROOT / o))
        conn.rollback()
        raise
    with open(log, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["old path", "new path", "class", "how", "sha256"])
        w.writerows(done)
    print(f"applied (run {RUN_ID}): {len(done)} file(s) moved {by}; {len(ops)} cfg write(s); move log {log}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
