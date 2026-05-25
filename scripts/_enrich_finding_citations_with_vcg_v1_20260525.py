"""Derive VCG citations from existing verse citations in finding_citation.

For each finding_citation row of citation_type='verse', look up which
verse_context_group(s) in the target cluster contain that verse, and insert
one finding_citation row per distinct (source_id, vcg_code) of
citation_type='vcg'.

Dedup rule: if a finding cites multiple verses that all live in the same
VCG, emit a single 'vcg' row (with position = min position of the
contributing verse citations).

Join chain:
  finding_citation.citation_value  (e.g. 'Psa 51:4')
    -> wa_verse_records.reference
    -> verse_context.verse_record_id
    -> verse_context_group.id (filtered to {cluster}%)
    -> verse_context_group.group_code (e.g. 'M10-D-VCG-02')

Active filters: delete_flagged=0 on verse_context and verse_context_group.

Idempotent: deletes existing finding_citation rows of citation_type='vcg'
whose source_id belongs to a cluster_finding/cluster_observation row in
the target cluster, then re-inserts.
"""
from __future__ import annotations
import argparse, io, sqlite3, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch_source_ids(conn: sqlite3.Connection, cluster: str) -> tuple[list[int], list[int]]:
    fids = [r[0] for r in conn.execute(
        "SELECT id FROM cluster_finding "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (cluster,),
    ).fetchall()]
    oids = [r[0] for r in conn.execute(
        "SELECT id FROM cluster_observation "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (cluster,),
    ).fetchall()]
    return fids, oids


def delete_existing_vcg(conn: sqlite3.Connection, source_table: str, source_ids: list[int]) -> int:
    if not source_ids:
        return 0
    n = 0
    chunk = 900
    for i in range(0, len(source_ids), chunk):
        ids = source_ids[i:i + chunk]
        placeholders = ",".join(["?"] * len(ids))
        cur = conn.execute(
            f"DELETE FROM finding_citation "
            f"WHERE citation_type='vcg' AND source_table=? AND source_id IN ({placeholders})",
            (source_table, *ids),
        )
        n += cur.rowcount
    return n


def derive_vcg_rows(conn: sqlite3.Connection, cluster: str) -> list[tuple[str, int, str, int]]:
    """Return deduped (source_table, source_id, vcg_code, min_position) tuples."""
    cluster_prefix = f"{cluster}-"  # e.g. 'M10-'
    rows = conn.execute(
        """
        SELECT fc.source_table  AS source_table,
               fc.source_id     AS source_id,
               vcg.group_code   AS vcg_code,
               MIN(fc.position) AS min_position,
               COUNT(*)         AS n_contrib_verses
        FROM finding_citation fc
        JOIN wa_verse_records vr ON vr.reference = fc.citation_value
        JOIN verse_context vc    ON vc.verse_record_id = vr.id
        JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE fc.citation_type = 'verse'
          AND vcg.group_code LIKE ?
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND COALESCE(vcg.delete_flagged, 0) = 0
        GROUP BY fc.source_table, fc.source_id, vcg.group_code
        """,
        (cluster_prefix + "%",),
    ).fetchall()
    return [(r["source_table"], r["source_id"], r["vcg_code"], r["min_position"]) for r in rows]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", default="M10")
    ap.add_argument("--live", action="store_true", help="Apply (default: dry-run)")
    args = ap.parse_args()
    cluster = args.cluster.strip()
    dry = not args.live

    print(f"=== finding_citation VCG enrichment — cluster={cluster} "
          f"mode={'DRY-RUN' if dry else 'LIVE'} ===")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    fids, oids = fetch_source_ids(conn, cluster)
    print(f"cluster_finding (active):    {len(fids)}")
    print(f"cluster_observation (active): {len(oids)}")
    print()

    derived = derive_vcg_rows(conn, cluster)
    print(f"derived VCG citations (post-dedup): {len(derived)}")
    print()

    # Reporting
    per_table = Counter()
    per_vcg = Counter()
    sources_with_vcg = set()
    for st, sid, vcg, _pos in derived:
        per_table[st] += 1
        per_vcg[vcg] += 1
        sources_with_vcg.add((st, sid))

    print("Per source-table:")
    for st in ("cluster_finding", "cluster_observation"):
        print(f"  {st:25s}: {per_table[st]} vcg rows")
    print()

    print(f"Distinct source rows with >=1 VCG tag:   {len(sources_with_vcg)}")
    n_total_sources = len(fids) + len(oids)
    print(f"Distinct source rows (total active):     {n_total_sources}")
    coverage_pct = (len(sources_with_vcg) / n_total_sources * 100) if n_total_sources else 0
    print(f"VCG-tag coverage: {coverage_pct:.1f}%")
    print()

    print(f"Distinct VCGs referenced: {len(per_vcg)}")
    print()
    print("Top 15 most-referenced VCGs:")
    for k, v in per_vcg.most_common(15):
        print(f"  {k:20s}  {v} findings")
    print()

    # Fanout: VCGs per source row
    fanout = Counter()
    by_source: dict[tuple[str, int], int] = defaultdict(int)
    for st, sid, vcg, _pos in derived:
        by_source[(st, sid)] += 1
    for n in by_source.values():
        fanout[n] += 1
    print("VCG fanout per source row:")
    for n in sorted(fanout.keys()):
        print(f"  {n:2d} VCGs: {fanout[n]} source rows")
    print()

    if dry:
        print("[DRY-RUN — no writes]")
        conn.close()
        return 0

    # LIVE
    print("--- Wiping existing VCG citations for affected sources ---")
    cur = conn.cursor()
    cur.execute("BEGIN")
    try:
        n_del_f = delete_existing_vcg(conn, "cluster_finding", fids)
        n_del_o = delete_existing_vcg(conn, "cluster_observation", oids)
        print(f"  deleted cluster_finding vcg rows:     {n_del_f}")
        print(f"  deleted cluster_observation vcg rows: {n_del_o}")

        ins_sql = (
            "INSERT INTO finding_citation "
            "(source_table, source_id, citation_type, citation_value, position, "
            "delete_flagged, created_at) "
            "VALUES (?, ?, 'vcg', ?, ?, 0, ?)"
        )
        batch = []
        BATCH_SIZE = 500
        n_ins = 0
        for st, sid, vcg, pos in derived:
            batch.append((st, sid, vcg, pos, NOW))
            if len(batch) >= BATCH_SIZE:
                cur.executemany(ins_sql, batch)
                n_ins += len(batch)
                batch.clear()
        if batch:
            cur.executemany(ins_sql, batch)
            n_ins += len(batch)

        conn.commit()
        print(f"  inserted: {n_ins}")
        print("COMMITTED")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        post = conn.execute(
            "SELECT citation_type, COUNT(*) FROM finding_citation GROUP BY citation_type"
        ).fetchall()
        print()
        print("--- Post-state: finding_citation by type ---")
        for r in post:
            print(f"  {r[0]:11s}: {r[1]}")
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
