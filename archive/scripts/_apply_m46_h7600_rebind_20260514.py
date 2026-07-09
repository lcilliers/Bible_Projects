"""Follow-up to WA-M46-cc-instructions RD-01: H7600 sha.a.nan → M46.

Researcher-authorised 2026-05-14. Single TERM_REBIND.

Pre-state:
  mti=413 H7600 sha.a.nan currently in M19 Trust (Not started, 0 sub-groups).
  10 wa_verse_records, 9 verse_context rows (1 UT — Isa 33:20), 2 VCGs:
    413-001 — Complacent ease/self-secure (8 verses incl. Amos 6:1) — fits M46
    413-002 — Divinely intended secure quietness (Isa 32:18) — Phase 6 reconciliation will decide

Mechanism: UPDATE mti_terms.cluster_code. All term-keyed data travels.
"""
from __future__ import annotations
import argparse, os, shutil, sqlite3, sys
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
MTI_ID = 413
EXPECTED_STRONGS = "H7600"
FROM_CLUSTER = "M19"
TO_CLUSTER = "M46"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    ts = now_iso()

    print("=" * 72)
    print(f"  H7600 sha.a.nan rebind: M19 → M46 (RD-01 resolution)")
    print(f"  Mode: {'LIVE' if args.live else 'DRY-RUN'}")
    print("=" * 72)

    r = conn.execute(
        "SELECT id, strongs_number, transliteration, cluster_code, vc_status "
        "FROM mti_terms WHERE id=? AND COALESCE(delete_flagged,0)=0",
        (MTI_ID,)
    ).fetchone()
    if not r:
        print(f"  ✗ mti={MTI_ID} NOT FOUND")
        return 1
    if r["strongs_number"] != EXPECTED_STRONGS or r["cluster_code"] != FROM_CLUSTER:
        print(f"  ✗ pre-state mismatch: strongs={r['strongs_number']} cluster={r['cluster_code']}")
        return 1
    print(f"\n  ✓ Pre-state: mti={r['id']} {r['strongs_number']} '{r['transliteration']}' "
          f"in {r['cluster_code']} (vc_status={r['vc_status']})")

    # Counts that will travel with the term
    n_vr = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE mti_term_id=? "
                        "AND COALESCE(delete_flagged,0)=0", (MTI_ID,)).fetchone()[0]
    n_vc = conn.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? "
                        "AND COALESCE(delete_flagged,0)=0", (MTI_ID,)).fetchone()[0]
    n_vcg = conn.execute("SELECT COUNT(*) FROM verse_context_group "
                         "WHERE group_code LIKE '413-%' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f"  Term-keyed data travelling: vr={n_vr} vc={n_vc} vcg={n_vcg}")

    if not args.live:
        print("\n[DRY-RUN] no changes. Re-run with --live.")
        return 0

    # Backup
    os.makedirs(BACKUP_DIR, exist_ok=True)
    bp = os.path.join(BACKUP_DIR,
                      f"bible_research_pre_m46_h7600_rebind_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db")
    shutil.copy2(DB, bp)
    print(f"\nBackup: {bp}\n")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        cur.execute(
            "UPDATE mti_terms SET cluster_code=?, last_changed=? WHERE id=?",
            (TO_CLUSTER, ts, MTI_ID)
        )
        if cur.rowcount != 1:
            raise RuntimeError(f"UPDATE affected {cur.rowcount} rows (expected 1)")
        # FK check
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {fkv[:3]}")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"ROLLED BACK: {e}")
        return 1

    # Verify
    r = conn.execute("SELECT cluster_code FROM mti_terms WHERE id=?", (MTI_ID,)).fetchone()
    print(f"  ✓ Post-state: mti={MTI_ID} cluster_code={r['cluster_code']!r}")

    n_m46 = conn.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M46' "
                         "AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    n_m19 = conn.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M19' "
                         "AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f"  M46 active terms: {n_m46}")
    print(f"  M19 active terms: {n_m19}")

    conn.close()
    print(f"\n[LIVE] H7600 sha.a.nan rebind applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
