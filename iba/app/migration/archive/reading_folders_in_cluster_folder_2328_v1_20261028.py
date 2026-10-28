"""reading_folders_in_cluster_folder_2328_v1_20261028.py -- escalation #2328: a reading is filed in its home cluster's folder.

Researcher, chat 2026-10-28 (verbatim): "the code test failed. the code does not read the correct folder for the filing of the json because
the code does not read the configs."

The filing convention (cfg_setting report.cluster_folder_naming_convention) files ALL output relating to a cluster in
_analytics/Clusters/{cluster_code} - {short_name slug}/. The reading code read one setting, reading.output_dir = outputs/reading, and
filed every reading there. This migration:
- sets cfg_setting reading.output_dir to _analytics/Clusters/{cluster_folder}: the code (lib/reading.py out_dir, with
  lib/filingkit.py cluster_folder_name) resolves {cluster_folder} from the reading's home cluster by the convention;
- restates the study_output entry of cfg_control_home (the readings are in their cluster's folder; the "until build B7" wording goes);
- moves every existing reading folder from outputs/reading/<label>/ to <home cluster folder>/<label>/ and points the reading row's
  gap_file, observe_file, synergy_file and narrate_file at the new place. Every move is written to
  outputs/escalation/2328-reading-folder-moves-v1-20261028.tsv (the way back). Nothing is deleted: a file is moved whole, and the old
  folder is removed only when it is empty.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/reading_folders_in_cluster_folder_2328_v1_20261028.py [--db PATH] [--root PATH] [--dry-run]
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib import filingkit  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2328-READING-FOLDERS-20261028"
MODULE = "reading_folders_in_cluster_folder_2328_v1_20261028"
PATTERN = "_analytics/Clusters/{cluster_folder}"
CONTROL_HOME = ("_analytics/ (cluster folders per report.cluster_folder_naming_convention, each reading in its home cluster's folder "
                "under <label>/ by reading.output_dir; the exported narrative chapters in "
                "_analytics/essay/spirit_soul_body/inner-being-narrative/)")
FILE_COLS = ("gap_file", "observe_file", "synergy_file", "narrate_file")


def plan(conn, root: pathlib.Path):
    """[(reading row, old folder, new folder)] for every reading whose folder is not yet its home cluster's."""
    out = []
    for r in conn.execute("SELECT * FROM reading ORDER BY id").fetchall():
        old = (root / (r["gap_file"] or "")).parent
        new = root / "_analytics/Clusters" / filingkit.cluster_folder_name(conn, r["home_cluster"]) / r["label"]
        if old != new:
            out.append((r, old, new))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    root = pathlib.Path(a.root)
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    moves = plan(conn, root)
    clash = [str(new) for _, old, new in moves if new.exists() and any(new.iterdir())]
    if clash:
        print("REFUSED: the target folder already holds files: " + "; ".join(clash))
        return 1
    n_files = sum(sum(1 for f in old.rglob("*") if f.is_file()) for _, old, _ in moves if old.is_dir())
    if a.dry_run:
        print(f"DRY RUN -- {len(moves)} reading folder(s), {n_files} file(s) to move: "
              + "; ".join(f"{r['label']} -> {new.relative_to(root).as_posix()}" for r, _, new in moves) + "; nothing written")
        return 0
    lines = ["label\told_path\tnew_path"]
    with conn:
        for r, old, new in moves:
            new.mkdir(parents=True, exist_ok=True)
            if old.is_dir():
                for f in sorted(old.rglob("*")):
                    if f.is_file():
                        dest = new / f.relative_to(old)
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(f), str(dest))
                        lines.append(f"{r['label']}\t{f.relative_to(root).as_posix()}\t{dest.relative_to(root).as_posix()}")
            for sub in sorted((p for p in old.rglob("*") if p.is_dir()), reverse=True):
                if not any(sub.iterdir()):
                    sub.rmdir()
            if old.is_dir() and not any(old.iterdir()):
                old.rmdir()
            sets, args = [], []
            for col in FILE_COLS:
                if r[col]:
                    old_rel = pathlib.PurePosixPath(r[col])
                    sets.append(f"{col}=?")
                    args.append(str(pathlib.PurePosixPath(new.relative_to(root).as_posix()) / old_rel.name))
            if sets:
                conn.execute(f"UPDATE reading SET {', '.join(sets)} WHERE id=?", args + [r["id"]])
        apply_logged(conn, RUN_ID, "cfg_setting", "update", {"key": "reading.output_dir"}, {"value": '"' + PATTERN + '"'})
        apply_logged(conn, RUN_ID, "cfg_control_home", "update", {"kind": "study_output"}, {"home": CONTROL_HOME})
        if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {
                "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
                "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                        "as the other Developer Mode migrations",
                "purpose": f"ONE-OFF migration -- escalation #2328: readings filed in their home cluster's folder; run_id {RUN_ID}. "
                           f"inactive=1 once applied."})
    record = (root / "outputs/escalation/2328-reading-folder-moves-v1-20261028.tsv") if a.db == DEFAULT_DB \
        else pathlib.Path(a.db).with_suffix(".folder-moves.tsv")
    record.parent.mkdir(parents=True, exist_ok=True)
    record.write_text(chr(10).join(lines) + chr(10), encoding="utf-8")
    print(f"{len(moves)} reading folder(s), {len(lines) - 1} file(s) moved; reading.output_dir is {PATTERN}; record {record}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
