"""M11 Phase 1 — vc_status advancement (0 UT verses).

Per v2_9 §4. M11 has 0 UT verses (all 288 verse_context rows already classified —
287 is_relevant=1 + 1 is_relevant=0). The legacy `vc_status` field on 14 of the 15
terms is 'to_revise' or 'not_done' from the pre-cluster era. This script advances
those terms to 'vc_completed' to reflect the new methodology's understanding:
under v2_9, vc_status is per-term UT-completion progress; with 0 UT remaining,
all terms are vc_completed by definition.

Operations (single transaction):
- Op A: pre-check — 0 UT (is_relevant IS NULL) verses for any M11 term
- Op B: UPDATE mti_terms SET vc_status='vc_completed' for any M11 term where
        vc_status != 'vc_completed'
"""
from __future__ import annotations
import argparse, io, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CLUSTER = "M11"


def main(live: bool) -> int:
    print(f"=== M11 Phase 1 apply - mode={'LIVE' if live else 'DRY-RUN'} ===")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    n_ut = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code = ? AND vc.is_relevant IS NULL
          AND COALESCE(vc.delete_flagged, 0) = 0
    """, (CLUSTER,)).fetchone()[0]
    print(f"UT verses (is_relevant IS NULL): {n_ut}")
    assert n_ut == 0, f"Expected 0 UT verses for M11; found {n_ut}"

    rows = conn.execute(
        "SELECT id, strongs_number, transliteration, vc_status FROM mti_terms "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        "ORDER BY strongs_number",
        (CLUSTER,)
    ).fetchall()
    print(f"\nM11 terms ({len(rows)}):")
    needs_update = []
    for r in rows:
        flag = "" if r["vc_status"] == "vc_completed" else "  <-- needs update"
        print(f"  mti={r['id']:5d}  {r['strongs_number']:8s}  {r['transliteration']:25s}  vc_status={r['vc_status']!r}{flag}")
        if r["vc_status"] != "vc_completed":
            needs_update.append(r["id"])

    print(f"\n{len(needs_update)} terms need vc_status update -> 'vc_completed'")

    if not live:
        print("\n[DRY-RUN - no writes]")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN")
    try:
        n_updated = 0
        for mti_id in needs_update:
            cur.execute(
                "UPDATE mti_terms SET vc_status='vc_completed', vc_status_updated_at=? "
                "WHERE id=? AND vc_status != 'vc_completed'",
                (NOW, mti_id),
            )
            n_updated += cur.rowcount
        assert n_updated == len(needs_update), f"Expected {len(needs_update)} updates, got {n_updated}"
        conn.commit()
        print(f"\nCOMMITTED at {NOW}")
        print(f"Updated {n_updated} mti_terms rows -> vc_status='vc_completed'")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
