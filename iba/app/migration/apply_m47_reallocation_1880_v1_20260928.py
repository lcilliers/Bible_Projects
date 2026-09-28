"""apply_m47_reallocation_1880_v1_20260928.py — ONE-OFF migration, escalation #1880.

Applies the M47 re-allocation register (`research/investigations/M47-reallocation-register-v*-
20260928.md`) from its machine-readable twin `iba/docs/m47-cluster-reallocation-spec-v*-
20260928.json`. Researcher instruction, verbatim, 2026-09-28: "1 - yes draft the list; 2 - if you
have access, then apply it, as long as you follow governance and the configs 3 - yes, anything
identified in the M47 work and the batches that flags a re-allocation should be included."

Governance basis (not re-derived): `cluster`/`cluster_strong` are `category='data'` tables with
`writer='migration'` grants, not `configmaint.propose` territory (same basis as
`apply_1598_cluster_batch.py`). Row convention follows `reclassify_g0627_to_t3_v1_20260917.py`:
soft-delete-and-insert, never edit a live `cluster_strong` row in place, never hard-delete.

**Only items with `"approved": true` are applied.** An unapproved item is reported and skipped.
Escalation #1880 is `decision_required`, so approval is the Researcher's alone
(cfg_escalation_requirement 'decision_required_approval_requires_researcher').

Ops (per spec `op_semantics`):
  add              insert live (strong, cluster_code) if absent
  move             soft-delete live (strong, from); insert (strong, to) if absent
  remove           soft-delete live (strong, cluster_code)
  set_alt          soft-delete live (strong, cluster_code) and reinsert it with alt_clusters set
  set_review_flag  soft-delete live (strong, cluster_code) and reinsert it with review_flag=1
  none             nothing

Idempotent: every op checks live state first; re-running is a no-op on applied rows.

After a live run, `verse_lexical.role` is stale for the touched strongs (#1719 gate) — rebuild the
chapters this script prints with `VerseLexical.ps1 -Book <b> -Chapters <lo-hi> -Step lexical.build`.

    python -m iba.app.migration.apply_m47_reallocation_1880_v1_20260928 --spec iba/docs/m47-cluster-reallocation-spec-v2-20260928.json --dry-run
"""

from __future__ import annotations

import argparse
import collections
import datetime
import json
import pathlib
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
_SOURCE = "researcher-ruling-1880-20260928"
_CONF = {"clear": "high", "weak": "medium", "proposed": "medium", "by-design": "high"}


def _live(conn, strong, code):
    return conn.execute(
        "SELECT * FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
        (strong, code)).fetchone()


def _insert(conn, strong, code, confidence, rationale, alt=None, review_flag=0):
    conn.execute(
        "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
        "confidence, operation, alt_clusters, review_flag, rationale) "
        "VALUES (?, ?, ?, datetime('now'), 0, ?, 0, ?, ?, ?)",
        (strong, code, _SOURCE, confidence, alt, review_flag, rationale))


def _soft_delete(conn, row_id):
    conn.execute("UPDATE cluster_strong SET deleted=1 WHERE id=?", (row_id,))


def apply(conn, spec, dry_run):
    report, touched = [], set()
    esc = spec.get("escalation")
    for item in spec["items"]:
        ops = [o for o in item["ops"] if o["op"] != "none"]
        if not ops:
            continue
        if not item.get("approved"):
            report.append(f"{item['id']}: not approved -- skipped")
            continue
        conf = _CONF.get(item["strength"], "medium")
        ruling = item.get("researcher_note") or "approved as proposed"
        why = (f"escalation #{esc}, M47 re-allocation register item {item['id']} "
               f"({item['source']}): {item['issue']} Ruling: {ruling}.")
        for o in ops:
            s = o["strong"]
            if o["op"] == "add":
                if _live(conn, s, o["cluster_code"]):
                    report.append(f"{item['id']} {s}: {o['cluster_code']} already live -- no-op")
                    continue
                if not dry_run:
                    _insert(conn, s, o["cluster_code"], conf, "added " + why)
                touched.add(s)
                report.append(f"{item['id']} {s}: add {o['cluster_code']}")
            elif o["op"] == "move":
                src, dst = _live(conn, s, o["from"]), _live(conn, s, o["to"])
                if not src and dst:
                    report.append(f"{item['id']} {s}: already at {o['to']} -- no-op")
                    continue
                if not src:
                    report.append(f"{item['id']} {s}: NO live {o['from']} row -- skipped")
                    continue
                if not dry_run:
                    _soft_delete(conn, src["id"])
                    if not dst:
                        _insert(conn, s, o["to"], conf,
                                f"relocated {o['from']}->{o['to']} 2026-09-28, " + why)
                touched.add(s)
                report.append(f"{item['id']} {s}: {o['from']} -> {o['to']}")
            elif o["op"] == "remove":
                row = _live(conn, s, o["cluster_code"])
                if not row:
                    report.append(f"{item['id']} {s}: {o['cluster_code']} not live -- no-op")
                    continue
                if not dry_run:
                    _soft_delete(conn, row["id"])
                touched.add(s)
                report.append(f"{item['id']} {s}: remove {o['cluster_code']}")
            elif o["op"] in ("set_alt", "set_review_flag"):
                row = _live(conn, s, o["cluster_code"])
                if not row and dry_run:
                    report.append(f"{item['id']} {s}: {o['op']} on {o['cluster_code']} "
                                  f"(row created earlier in this item)")
                    continue
                if not row:
                    report.append(f"{item['id']} {s}: NO live {o['cluster_code']} row -- skipped")
                    continue
                alt = json.dumps(o["alt_clusters"]) if o["op"] == "set_alt" else row["alt_clusters"]
                flag = 1 if o["op"] == "set_review_flag" else row["review_flag"]
                if (alt or None) == (row["alt_clusters"] or None) and flag == row["review_flag"]:
                    report.append(f"{item['id']} {s}: {o['op']} already set -- no-op")
                    continue
                if not dry_run:
                    _soft_delete(conn, row["id"])
                    conn.execute(
                        "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, "
                        "deleted, confidence, operation, alt_clusters, review_flag, rationale) "
                        "VALUES (?, ?, ?, ?, 0, ?, ?, ?, ?, ?)",
                        (s, row["cluster_code"], row["source"], row["created_at"],
                         row["confidence"], row["operation"], alt, flag,
                         (row["rationale"] or "") + f" | {o['op']} 2026-09-28, " + why))
                report.append(f"{item['id']} {s}: {o['op']} on {o['cluster_code']}"
                              + (f" alt={o['alt_clusters']}" if o["op"] == "set_alt" else ""))
    return report, touched


def rebuild_scope(conn, strongs):
    """(book, chapter) pairs whose verses contain a touched strong -- the lexical.build scope."""
    if not strongs:
        return {}
    q = ",".join("?" * len(strongs))
    chapters = collections.defaultdict(set)
    for (osis,) in conn.execute(
            f"SELECT DISTINCT v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
            f"WHERE vl.deleted=0 AND vl.strong IN ({q})", sorted(strongs)):
        b, c, _ = osis.split(".")
        chapters[b].add(int(c))
    return chapters


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--db", default=str(DB_PATH))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--assume-approved", action="store_true",
                    help="dry-run only: preview every item as if approved")
    args = ap.parse_args()
    if args.assume_approved and not args.dry_run:
        print("--assume-approved is only allowed with --dry-run")
        return 2

    spec = json.loads((_REPO_ROOT / args.spec).read_text(encoding="utf-8"))
    if args.assume_approved:
        for it in spec["items"]:
            it["approved"] = True
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    report, touched = apply(conn, spec, args.dry_run)
    if args.dry_run:
        conn.rollback()
    else:
        conn.commit()
    for line in report:
        print(line)
    scope = rebuild_scope(conn, touched)
    nch = sum(len(v) for v in scope.values())
    print(f"\n{'DRY RUN -- nothing written. ' if args.dry_run else ''}"
          f"{len(touched)} strong(s) touched; lexical.build scope: {nch} chapter(s) in "
          f"{len(scope)} book(s)")
    for b in sorted(scope):
        print(f"  {b}: {','.join(str(c) for c in sorted(scope[b]))}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
