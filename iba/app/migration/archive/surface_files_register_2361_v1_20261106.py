"""surface_files_register_2361_v1_20261106.py -- escalation #2361, stage 1c: the file registry of the surface cycle.

manifest.rebuild now updates file_manifest by path and keeps the analytic columns (lib/manifest.py, tested by
iba/app/tools/temp_2361_manifest_test_run.py). This migration fills those columns for the working files that exist:
  - the files moved by surface_files_2361_v1_20261106 (read from its move log): module, run_id of the move, sha256 checked before
    and after the move, analytic_status (regenerable for the embedding cache, live for the rest), migrated_from (the old path)
  - the three import files made for the load (prompts, test cases, models): module, run_id of the load, sha256
The files in _analytics/surfaces/discarded are NOT registered (ruling of 2026-11-06: a discarded method is not registered).
Also corrects the description of step manifest.rebuild (it no longer replaces the table's contents) and gives the migration its write
grant on file_manifest, through configmaint.apply_logged(). Refuses, writing nothing, if a file to register is not yet in the manifest
(run Manifest-Rebuild.ps1 first). Idempotent.

Usage:
    python iba/app/migration/surface_files_register_2361_v1_20261106.py [--db PATH] [--dry-run]
"""
import argparse
import csv
import hashlib
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib import manifest  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-SURFACE-FILES-REGISTER-20261106"
MODULE = "surface_files_register_2361_v1_20261106"
MOVE_RUN = "DEVMODE-2361-SURFACE-FILES-20261106"
LOAD_RUN = "DEVMODE-2361-SURFACE-CYCLE-LOAD-20261106"
MOVE_LOG = ROOT / "Logs" / "2361-stage0-moves-20261106T060216Z.csv"
WF = "_analytics/surfaces/working_files/"
CREATED = ["_analytics/surfaces/working_files/collection/import/prompts-v1-20261106.json",
           "_analytics/surfaces/working_files/collection/import/eval-cases-v1-20261106.json",
           "_analytics/surfaces/working_files/base/import/models-v1-20261106.json"]
FOLDER_MODULE = {"group": "group", "structure": "structure", "base": "ai_base", "collection": "collection"}   # folder -> enum surface_cycle_module
STEP_DOES = ("rescan the whole project tree (filename/path metadata only, no file content) and update file_manifest by path: new "
             "paths added, changed ones updated, paths no longer on disk removed; the analytic columns of a file that is still "
             "there (module, run_id, sha256, analytic_status, migrated_from) are kept; see lib/manifest.py")


def sha(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def module_of(path: str):
    if path.startswith(WF):
        return FOLDER_MODULE.get(path[len(WF):].split("/")[0])
    return None  # exports and documents belong to no single module


def items():
    out = []
    for r in csv.DictReader(open(MOVE_LOG, encoding="utf-8")):
        if r["class"] == "D":
            continue  # discarded: not registered
        new = r["new path"].replace("\\", "/")
        out.append((new, module_of(new), MOVE_RUN, r["sha256"], "regenerable" if r["class"] == "R" else "live", r["old path"].replace("\\", "/")))
    for p in CREATED:
        out.append((p, module_of(p), LOAD_RUN, sha(ROOT / p), "live", None))
    return out


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    cur = conn.execute("SELECT does FROM cfg_step WHERE step='manifest.rebuild'").fetchone()
    if cur and cur[0] != STEP_DOES:
        ops.append(("cfg_step", "update", {"step": "manifest.rebuild"}, {"does": STEP_DOES}))
    if not has("SELECT 1 FROM cfg_write_grant WHERE writer='migration' AND table_name='file_manifest' AND database='iba'"):
        ops.append(("cfg_write_grant", "insert", {}, {"writer": "migration", "table_name": "file_manifest", "database": "iba", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "purpose": f"ONE-OFF migration -- escalation #2361 stage 1c: registers the surface-cycle working files in file_manifest "
                       f"and corrects the step description of manifest.rebuild; run_id {RUN_ID}.",
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    rows = items()
    ops = plan(conn)
    missing = [p for p, *_ in rows if not conn.execute("SELECT 1 FROM file_manifest WHERE path=?", (p,)).fetchone()]
    gone = [p for p, *_ in rows if not (ROOT / p).exists()]
    if missing or gone:
        print("REFUSED, nothing written:")
        for p in missing:
            print("  not in file_manifest (run Manifest-Rebuild.ps1 first): " + p)
        for p in gone:
            print("  not on disk: " + p)
        return 2
    changed = [p for p, m, run, digest, st, old in rows if conn.execute(
        "SELECT module, run_id, sha256, analytic_status, migrated_from FROM file_manifest WHERE path=?", (p,)).fetchone() != (m, run, digest, st, old)]
    if a.dry_run:
        print(f"DRY RUN: {len(rows)} file(s) to register ({len(changed)} to change); {len(ops)} cfg write(s)")
        return 0
    if not changed and not ops:
        print("already applied: nothing changed")
        return 0
    bad = [p for p, m, run, digest, st, old in rows if (ROOT / p).exists() and sha(ROOT / p) != digest]
    if bad:
        print("REFUSED: the checksum differs from the move log for: " + ", ".join(bad[:5]))
        return 2
    try:
        conn.execute("SAVEPOINT register_files")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for p, m, run, digest, st, old in rows:
            if not manifest.register_analytic(conn, p, module=m, run_id=run, sha256=digest, analytic_status=st, migrated_from=old):
                raise RuntimeError(f"could not register {p}")
        conn.execute("RELEASE register_files")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO register_files")
        conn.execute("RELEASE register_files")
        raise
    n = conn.execute("SELECT count(*), sum(analytic_status='regenerable') FROM file_manifest WHERE analytic_status IS NOT NULL").fetchone()
    print(f"applied (run {RUN_ID}): {len(rows)} file(s) registered ({n[0]} in the manifest, {n[1]} regenerable); {len(ops)} cfg write(s); "
          f"discarded files not registered")
    return 0


if __name__ == "__main__":
    sys.exit(main())
