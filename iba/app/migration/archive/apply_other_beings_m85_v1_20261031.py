"""apply_other_beings_m85_v1_20261031.py -- ONE-OFF migration: the new M85 Other Beings cluster.

Re-codes the angelic (T9) and adversarial (T4) terms to a new M-code M85 in `cluster_strong`, from
the spec `iba/docs/other-beings-m85-spec-v1-20261031.json`. Researcher, chat 2026-10-31: the other-being
terms are elevated from T-codes to M; the divine terms stay in T7; spirit terms are not part of this.
`cluster` and `cluster_strong` are data tables with `writer='migration'` grants. Soft-delete-and-insert,
never an edit in place, never a hard delete. Idempotent. The subgroups and surface pairs follow through
the surface-map script (Pairs, Apply, Tail, Check).

    python -m iba.app.migration.apply_other_beings_m85_v1_20261031 --spec iba/docs/other-beings-m85-spec-v1-20261031.json --dry-run
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
_SOURCE = "researcher-ruling-other-beings-m85-20261031"


def apply(conn, spec, dry_run):
    report = []
    cl = spec["cluster"]
    code = cl["code"]
    why = f"researcher ruling 2026-10-31: {spec['ruling']}"
    if not conn.execute("SELECT 1 FROM cluster WHERE cluster_code=?", (code,)).fetchone():
        if not dry_run:
            conn.execute(
                "INSERT INTO cluster (cluster_code, short_name, description, deleted, status, status_changed_at) "
                "VALUES (?, ?, ?, 0, 't_cluster_assignment_completed', strftime('%Y-%m-%dT%H:%M:%SZ','now'))",
                (code, cl["short_name"], cl["description"]))
        report.append(f"cluster {code} {cl['short_name']}: created")
    for item in spec["items"]:
        s = item["strong"]
        if not conn.execute("SELECT 1 FROM strong WHERE strongNumber=? AND deleted=0", (s,)).fetchone():
            report.append(f"{s}: NO live strong row -- skipped")
            continue
        if conn.execute("SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
                        (s, code)).fetchone():
            report.append(f"{s}: already at {code} -- no-op")
            continue
        for frm in item["from"]:
            src = conn.execute("SELECT id FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
                               (s, frm)).fetchone()
            if src and not dry_run:
                conn.execute("UPDATE cluster_strong SET deleted=1 WHERE id=?", (src[0],))
        if not dry_run:
            conn.execute(
                "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, confidence, "
                "operation, alt_clusters, review_flag, rationale) "
                "VALUES (?, ?, ?, datetime('now'), 0, 'high', 0, NULL, 0, ?)",
                (s, code, _SOURCE, f"relocated {'+'.join(item['from'])}->{code} 2026-10-31 ({item['subgroup']}), {why}"))
        report.append(f"{s}: {'+'.join(item['from'])} -> {code}")
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--db", default=str(DB_PATH))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    spec = json.loads((_REPO_ROOT / args.spec).read_text(encoding="utf-8"))
    conn = sqlite3.connect(args.db)
    report = apply(conn, spec, args.dry_run)
    if args.dry_run:
        conn.rollback()
    else:
        conn.commit()
    print("\n".join(report))
    print(("DRY RUN -- nothing written. " if args.dry_run else "") + f"{len(report)} lines")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
