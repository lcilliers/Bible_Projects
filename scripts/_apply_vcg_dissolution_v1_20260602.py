"""C1 old-format VCG dissolution handler (per cluster) — mechanical, reusable.

Old-format (pre-2026-05-04, registry-era) verse_context_group rows have numeric-dash
group_codes (GLOB '[0-9]*-[0-9]*'). When a cluster goes through current analysis these
inherited VCGs are silently soft-deleted (v2_9 Phase 8). This handler does that for one
cluster: soft-delete the old-format verse_context_group rows tied to the cluster's terms
(via verse_context.group_id) + their vcg_term rows. verse_context.group_id is NOT touched
(analytical queries filter on vcg.delete_flagged=0). Matches the auditor C1 check.

DEFAULT DRY-RUN. --apply to write.
  python scripts/_apply_vcg_dissolution_v1_20260602.py --cluster M20 [--apply]
"""
import argparse, sqlite3, sys
from datetime import datetime, timezone

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DB = "database/bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    c = sqlite3.connect(DB, timeout=60); c.row_factory = sqlite3.Row
    cur = c.cursor()

    ids = [r["id"] for r in cur.execute("""
        SELECT DISTINCT vcg.id
        FROM verse_context_group vcg
        JOIN verse_context vc ON vc.group_id = vcg.id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code = ? AND COALESCE(mt.delete_flagged,0)=0
          AND COALESCE(vc.delete_flagged,0)=0 AND COALESCE(vcg.delete_flagged,0)=0
          AND vcg.group_code GLOB '[0-9]*-[0-9]*'
    """, (a.cluster,))]
    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: {a.cluster} old-format VCGs to dissolve: {len(ids)}")
    if not ids:
        print("  none."); c.close(); return
    sample = cur.execute(f"SELECT group_code FROM verse_context_group WHERE id IN ({','.join('?'*len(ids))}) LIMIT 6", ids).fetchall()
    print("  sample group_codes:", [r["group_code"] for r in sample])
    if not a.apply:
        c.close(); return

    ph = ",".join("?" * len(ids))
    cur.execute("BEGIN")
    try:
        nt = cur.execute(f"UPDATE vcg_term SET delete_flagged=1 WHERE vcg_id IN ({ph}) AND COALESCE(delete_flagged,0)=0", ids).rowcount
        ng = cur.execute(f"UPDATE verse_context_group SET delete_flagged=1, notes=COALESCE(notes,'')||' [C1 dissolution 2026-06-02: inherited old-format VCG soft-deleted]' WHERE id IN ({ph}) AND COALESCE(delete_flagged,0)=0", ids).rowcount
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: soft-deleted {ng} verse_context_group + {nt} vcg_term rows.")
    c.close()


if __name__ == "__main__":
    main()
