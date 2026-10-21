"""_check_softdelete_integrity.py — H5 (2026-06-15): the standing soft-delete integrity check, and the
H1/H2 reconcile vehicle. Read-only by default; --fix applies the reconciliations via engine.softdelete
(the one shared cascade path).

Invariants asserted (all should be 0):
  - active wa_verse_records with NULL mti_term_id in a NON-excluded registry   (missing link)
  - mti_terms with status='delete' but delete_flagged=0                        (status<->flag inconsistency)
  - active downstream rows under an Excluded registry                          (missing exclusion cascade)

  python scripts/_check_softdelete_integrity.py            # report only
  python scripts/_check_softdelete_integrity.py --fix      # H1 excluded-cascade + H2 status reconcile, then re-check
"""
import argparse, os, sqlite3, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding="utf-8")
from engine.softdelete import integrity_violations, reconcile_delete_flags, cascade_delete_registry
DB = os.path.join("database", "bible_research.db")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="apply H1 (excluded cascade) + H2 (status reconcile)")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=120)
    conn.row_factory = sqlite3.Row

    v = integrity_violations(conn)
    print("soft-delete integrity:")
    for k, n in v.items():
        print(f"  {'OK ' if n == 0 else 'XX '} {k}: {n}")

    if a.fix and any(v.values()):
        print("\n--fix:")
        n2, anomalies = reconcile_delete_flags(conn)    # H2 (safe subset only)
        print(f"  H2 reconcile_delete_flags: {n2} safe status='delete' term(s) cascaded")
        if anomalies:
            print(f"  H2 ANOMALIES (delete-marked but in an ACTIVE cluster — left for review): {len(anomalies)}")
            print(f"     mti_term ids: {anomalies}")
        exc = [r[0] for r in conn.execute("SELECT id FROM word_registry WHERE phase1_status='Excluded'")]
        tot = 0
        for rid in exc:                                  # H1
            out = cascade_delete_registry(conn, rid)
            tot += sum(out.values())
        print(f"  H1 excluded-registry cascade: {tot} downstream row(s) soft-deleted")
        conn.commit()
        v2 = integrity_violations(conn)
        print("\nafter fix:")
        for k, n in v2.items():
            print(f"  {'OK ' if n == 0 else 'XX '} {k}: {n}")


if __name__ == "__main__":
    main()
