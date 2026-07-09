"""Assign newly-extracted 'wealth' terms (registry 215) to cluster M46.

Per WA-M46-cc-instructions action group 5: after Session A extraction,
all new mti_terms rows under registry 'wealth' (no=215) are assigned to M46.

10 terms: G4145, G4146, G4147, G4148, G4149, G4433, G4434, H6223, H6238, H6239.
"""
import sqlite3, sys, os, shutil
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = "database/bible_research.db"
REGISTRY_ID = 215
TARGET_CLUSTER = "M46"
EXPECTED_TERMS = ["G4145","G4146","G4147","G4148","G4149","G4433","G4434","H6223","H6238","H6239"]


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Find new terms attached to registry 215
    rows = list(conn.execute(
        "SELECT id, strongs_number, transliteration, gloss, cluster_code "
        "FROM mti_terms WHERE owning_registry_fk=? AND COALESCE(delete_flagged,0)=0 "
        "ORDER BY strongs_number",
        (REGISTRY_ID,)
    ))
    print(f"=== Registry {REGISTRY_ID} (wealth) terms: {len(rows)} ===")
    for r in rows:
        print(f"  mti={r['id']:<6} {r['strongs_number']:<8} {r['transliteration']:<14} "
              f"'{(r['gloss'] or '')[:30]}' cluster={r['cluster_code']}")

    expected_set = set(EXPECTED_TERMS)
    found_set = set(r["strongs_number"] for r in rows)
    if expected_set != found_set:
        missing = expected_set - found_set
        extra = found_set - expected_set
        print(f"  [ERR] expected vs found mismatch. missing={missing}  extra={extra}")
        return 1

    # All cluster_code should be NULL (unassigned) before we set them
    needs_update = [r for r in rows if r["cluster_code"] != TARGET_CLUSTER]
    print(f"\n  Terms needing M46 assignment: {len(needs_update)}/{len(rows)}")

    if not args.live:
        print("\n[DRY-RUN] would set cluster_code='M46' on these terms.")
        return 0

    # Backup
    bp = f"backups/bible_research_pre_m46_wealth_assign_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
    os.makedirs("backups", exist_ok=True)
    shutil.copy2(DB, bp)
    print(f"\nBackup: {bp}\n")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        for r in needs_update:
            cur.execute(
                "UPDATE mti_terms SET cluster_code=?, last_changed=? WHERE id=?",
                (TARGET_CLUSTER, ts, r["id"])
            )
            if cur.rowcount != 1:
                raise RuntimeError(f"mti={r['id']} UPDATE affected {cur.rowcount}")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"ROLLED BACK: {e}")
        return 1

    print(f"  ✓ {len(needs_update)} terms assigned to {TARGET_CLUSTER}")

    # Verify
    n_m46 = conn.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M46' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"\n  M46 active terms: {n_m46}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
