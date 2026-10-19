"""apply_flesh_body_complex_2163_v1_20261018.py — ONE-OFF migration, escalation #2163 (for #2162).

Brings the T-coded flesh/body terms into the flesh word complex: re-codes them to M47 in
`cluster_strong` and links them to registry word 150 `flesh` in `word_strong`, from the spec
`iba/docs/flesh-body-complex-spec-2163-v*-20261018.json`. Researcher, chat 2026-10-18 (verbatim):
"the body words should be clustered in with the flesh cluster, and be part of the flesh word
complex.  the word-registry has a range of associated terms associated with a word." Then: "In this
case all the T-code terms related to flesh need to be re-assigned to M47. All the verses, raw data
tables, span, lexical analysis must be brought in line."

Governance basis (not re-derived): `cluster_strong` and `word_strong` are data tables with
`writer='migration'` grants (as `apply_m47_reallocation_1880_v1_20260928.py` and
`add_healing_word_strong_20260810.py`). Soft-delete-and-insert; never an edit in place, never a
hard delete. Idempotent: every op checks live state first.

This script writes the links only. The verses, spans and lexical rows are brought in line after it
by the app's own steps, not here:
  1. `python -m iba.app.run new-word --step strong.reconcile --param Word=flesh ...` — reconciles
     every code of `flesh`; a backfill code now in M47 with a word link is promoted
     (lib.strongreconcile._promote: full STEP concordance via raw.verses_one, origin -> word,
     verse_lexical built for the fetched verses).
  2. `VerseLexical.ps1 -Book <b> -Chapters <lo-hi> -Step lexical.build` over the chapters this
     script prints (the #1719 stale-role refresh).
  3. `Spine-Check.ps1`.

    python -m iba.app.migration.apply_flesh_body_complex_2163_v1_20261018 --spec iba/docs/flesh-body-complex-spec-2163-v1-20261018.json --dry-run
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
_SOURCE = "researcher-ruling-2163-20261018"


def _live_cluster(conn, strong, code):
    return conn.execute(
        "SELECT * FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
        (strong, code)).fetchone()


def _live_link(conn, word_id, strong):
    return conn.execute(
        "SELECT * FROM word_strong WHERE word_id=? AND strong=? AND deleted=0",
        (word_id, strong)).fetchone()


def apply(conn, spec, dry_run):
    report, touched = [], set()
    word_id, esc = spec["word_id"], spec["escalation"]
    why = f"escalation #{esc} (for #{spec['for']}): {spec['ruling']}"
    for item in spec["items"]:
        s = item["strong"]
        if not conn.execute("SELECT 1 FROM strong WHERE strongNumber=? AND deleted=0",
                            (s,)).fetchone():
            report.append(f"{s}: NO live strong row -- skipped")
            continue
        for o in item["ops"]:
            if o["op"] == "move":
                src, dst = _live_cluster(conn, s, o["from"]), _live_cluster(conn, s, o["to"])
                if not src and dst:
                    report.append(f"{s}: already at {o['to']} -- no-op")
                    continue
                if not src:
                    report.append(f"{s}: NO live {o['from']} row -- skipped")
                    continue
                if not dry_run:
                    conn.execute("UPDATE cluster_strong SET deleted=1 WHERE id=?", (src["id"],))
                    if not dst:
                        conn.execute(
                            "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, "
                            "deleted, confidence, operation, alt_clusters, review_flag, rationale) "
                            "VALUES (?, ?, ?, datetime('now'), 0, 'high', 0, NULL, 0, ?)",
                            (s, o["to"], _SOURCE,
                             f"relocated {o['from']}->{o['to']} 2026-10-18, {why}"))
                touched.add(s)
                report.append(f"{s}: cluster {o['from']} -> {o['to']}")
            elif o["op"] == "link":
                if _live_link(conn, word_id, s):
                    report.append(f"{s}: already linked to word {word_id} -- no-op")
                    continue
                if not dry_run:
                    conn.execute("INSERT INTO word_strong (word_id, strong, deleted) VALUES (?, ?, 0)",
                                 (word_id, s))
                touched.add(s)
                report.append(f"{s}: link to word {word_id} '{spec['word']}'")
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
    ap.add_argument("--scope-only", action="store_true",
                    help="print the lexical.build chapter scope for every spec code, write nothing")
    args = ap.parse_args()

    spec = json.loads((_REPO_ROOT / args.spec).read_text(encoding="utf-8"))
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    if args.scope_only:
        touched = {i["strong"] for i in spec["items"]}
        report = []
    else:
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
