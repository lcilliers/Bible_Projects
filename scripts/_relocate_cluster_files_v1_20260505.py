"""_relocate_cluster_files_v1_20260505.py — file move.

Reorganises per-cluster working files out of Workflow/ (methodology) into
Sessions/Session_Clusters/MXX/ (analytical output/input).

Plan:
  - For each of the 47 clusters (M01..M46, T2, FLAG), create folder
    Sessions/Session_Clusters/{cluster_code}/
  - Move per-cluster files into the corresponding folder:
    * Workflow/Clusters/per-cluster/wa-cluster-{cluster}-* → Sessions/...
    * outputs/markdown/wa-cluster-{cluster}-* (case-insensitive) → Sessions/...
  - Keep in Workflow/Clusters/ ONLY:
    * wa-cluster-catalogue-v*-*.{md,json}  (cluster identity catalogue)
    * wa-cluster-overview-v*-*.{md,json}   (programme-level navigator)

Idempotent: skips files that have already been moved.
"""
from __future__ import annotations

import os
import re
import shutil
import sqlite3
import sys

DB_PATH = os.path.join("database", "bible_research.db")
SRC_WORKFLOW = os.path.join("Workflow", "Clusters", "per-cluster")
SRC_OUTPUTS = os.path.join("outputs", "markdown")
DEST_BASE = os.path.join("Sessions", "Session_Clusters")


def list_cluster_codes(conn):
    return [r[0] for r in conn.execute(
        "SELECT cluster_code FROM cluster ORDER BY cluster_code"
    ).fetchall()]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    cluster_codes = list_cluster_codes(conn)
    conn.close()
    print(f"Cluster codes ({len(cluster_codes)}): "
          f"{', '.join(cluster_codes[:5])}…")

    # 1. Create destination folders
    os.makedirs(DEST_BASE, exist_ok=True)
    for code in cluster_codes:
        os.makedirs(os.path.join(DEST_BASE, code), exist_ok=True)

    # 2. Build a regex matching cluster code in filenames (case-insensitive)
    code_to_re = {
        code: re.compile(rf"wa-cluster-{re.escape(code)}-",
                         re.IGNORECASE)
        for code in cluster_codes
    }

    moved = 0
    skipped = 0

    def relocate(src_dir):
        nonlocal moved, skipped
        if not os.path.isdir(src_dir):
            return
        for name in sorted(os.listdir(src_dir)):
            full = os.path.join(src_dir, name)
            if not os.path.isfile(full):
                continue
            target_code = None
            for code, rx in code_to_re.items():
                if rx.match(name):
                    target_code = code
                    break
            if not target_code:
                continue
            dst = os.path.join(DEST_BASE, target_code, name)
            if os.path.exists(dst):
                # already there — remove src to keep clean
                os.remove(full)
                skipped += 1
                continue
            shutil.move(full, dst)
            moved += 1
            print(f"  moved [{target_code}]  {name}")

    print("\n--- Relocating from Workflow/Clusters/per-cluster/ ---")
    relocate(SRC_WORKFLOW)
    print("\n--- Relocating from outputs/markdown/ (cluster-specific) ---")
    relocate(SRC_OUTPUTS)

    # Special case: outputs/markdown/wa-cluster-c17-coverage-* — legacy
    # C-cluster coverage report. Place under a Sessions/Session_Clusters/
    # legacy-c-clusters/ subfolder so it's archived but accessible.
    legacy_dir = os.path.join(DEST_BASE, "legacy_c_clusters")
    os.makedirs(legacy_dir, exist_ok=True)
    if os.path.isdir(SRC_OUTPUTS):
        for name in os.listdir(SRC_OUTPUTS):
            if re.match(r"wa-cluster-c\d+-", name, re.IGNORECASE):
                src = os.path.join(SRC_OUTPUTS, name)
                dst = os.path.join(legacy_dir, name)
                if os.path.exists(dst):
                    os.remove(src)
                    skipped += 1
                else:
                    shutil.move(src, dst)
                    moved += 1
                    print(f"  moved [legacy-C]  {name}")

    # 3. Remove now-empty per-cluster sub-folder under Workflow/
    if os.path.isdir(SRC_WORKFLOW):
        try:
            os.rmdir(SRC_WORKFLOW)
            print(f"\nRemoved empty: {SRC_WORKFLOW}")
        except OSError:
            print(f"\nKept non-empty: {SRC_WORKFLOW}")

    print(f"\nTotal moved: {moved}")
    print(f"Total skipped (already present): {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
