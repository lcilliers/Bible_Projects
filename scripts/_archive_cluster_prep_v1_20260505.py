"""_archive_cluster_prep_v1_20260505.py — file move (read+delete).

Moves cluster-preparation files from outputs/markdown/ into archive/Clusters/.
The DB now holds the cluster table (populated from these files); v6 JSON +
all iterations + experiment outputs are no longer the runtime source of truth
and should not sit in the active workspace.

Files KEPT in outputs/markdown/:
  - wa-cluster-{cXX,mXX}-* — current term-cluster analysis outputs (coverage,
    affinity, orphans, comprehensive reports)
  - wa-fk-audit-and-proposal-* — current architecture proposals
  - wa-db-architecture-decision-* — current architecture proposals
  - wa-m-tables-dependencies-* — current architecture proposals

Files MOVED to archive/Clusters/:
  - wa-term-anchor-* — all v1..v6 anchor iterations + summaries + unassigned
  - wa-meaning-clusters-* — researcher-supplied source files + supplements
  - wa-meaning-only-* — bottom-up clustering experiments
  - wa-cluster-identity-* — initial naming proposals
  - wa-cluster-ecosystem-* + wa-characteristic-model-* — design docs
  - wa-cluster-love-terms-* + wa-crosslang-* — exploratory analysis
  - wa-cluster-status-summary-* — superseded by Workflow/Clusters/catalogue
  - term-cluster-* + term-clusters-* — clustering experiment outputs
  - term-anchor-validate-* — quality assessment
  - term-{semantic,usage,cooccurrence,mounce}-* — vector/bridge experiments

Idempotent: skips files already moved.
"""
from __future__ import annotations

import os
import shutil
import sys

SRC_DIR = os.path.join("outputs", "markdown")
DST_DIR = os.path.join("archive", "Clusters")

PREFIXES_TO_ARCHIVE = (
    "wa-term-anchor-",
    "wa-meaning-clusters-",
    "wa-meaning-only-",
    "wa-cluster-identity-",
    "wa-cluster-ecosystem-",
    "wa-characteristic-model-",
    "wa-cluster-love-terms-",
    "wa-crosslang-",
    "wa-cluster-status-summary-",
    "term-cluster-",
    "term-clusters-",
    "term-anchor-validate-",
    "term-semantic-",
    "term-usage-",
    "term-cooccurrence-",
    "term-mounce-",
)


def main() -> int:
    if not os.path.isdir(SRC_DIR):
        print(f"ERROR: source dir not found: {SRC_DIR}")
        return 1
    os.makedirs(DST_DIR, exist_ok=True)

    moved = []
    skipped = []
    for name in sorted(os.listdir(SRC_DIR)):
        if not any(name.startswith(p) for p in PREFIXES_TO_ARCHIVE):
            continue
        src = os.path.join(SRC_DIR, name)
        dst = os.path.join(DST_DIR, name)
        if not os.path.isfile(src):
            continue
        if os.path.exists(dst):
            print(f"  already in archive: {name}")
            skipped.append(name)
            # Remove the duplicate from source to be safe
            os.remove(src)
            continue
        shutil.move(src, dst)
        moved.append(name)
        print(f"  moved: {name}")

    print()
    print(f"Moved: {len(moved)} files → {DST_DIR}/")
    print(f"Skipped (already archived): {len(skipped)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
