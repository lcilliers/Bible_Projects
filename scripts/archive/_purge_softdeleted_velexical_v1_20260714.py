#!/usr/bin/env python
"""Hard-purge ANCIENT soft-deleted ve_lexical rows to reclaim DB space (v1, 2026-07-14).

Context (Proverbs retrospective): the DB has grown to ~800 MB, carrying ~174k soft-deleted
`ve_lexical` rows (the reread supersedes old rows via soft-delete). Space is reclaimable.

⚠ TENSION with the method: the re-read principle is 'never hard-delete — soft-delete-and-
rebuild; rows preserved as the G8 *before*'. So this tool is **deliberate, opt-in, and
conservative**: dry-run by default; --live requires an explicit age cutoff (older-than) so
that RECENT before-states are kept; it refuses to run --live unless a fresh DB snapshot
exists; and it prints the G8-before caveat. Only purge before-states the researcher judges
no longer needed for a delta.

Usage:
  python scripts/_purge_softdeleted_velexical_v1_20260714.py                  # dry-run report
  python scripts/_purge_softdeleted_velexical_v1_20260714.py --older-than 60   # dry-run, cutoff 60d
  python scripts/_purge_softdeleted_velexical_v1_20260714.py --older-than 60 --live [--vacuum]
"""
import sqlite3, os, sys, glob, argparse

DB = os.path.join('database', 'bible_research.db')
BK = 'backups'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--older-than', type=int, help='purge soft-deleted rows whose created_at is older than N days (REQUIRED for --live)')
    ap.add_argument('--live', action='store_true', help='actually hard-delete (else dry-run)')
    ap.add_argument('--vacuum', action='store_true', help='VACUUM after purge to reclaim file space (slow, rewrites the DB)')
    a = ap.parse_args()

    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    one = lambda s, *ar: c.execute(s, ar).fetchone()[0]

    total_soft = one("SELECT COUNT(*) FROM ve_lexical WHERE delete_flagged=1")
    total_active = one("SELECT COUNT(*) FROM ve_lexical WHERE COALESCE(delete_flagged,0)=0")
    print(f"# ve_lexical soft-delete purge | active={total_active} soft-deleted={total_soft}")

    cutoff_clause, params, desc = "delete_flagged=1", (), "ALL soft-deleted (no cutoff)"
    if a.older_than is not None:
        cutoff_clause = "delete_flagged=1 AND created_at < datetime('now', ?)"
        params = (f'-{a.older_than} days',)
        desc = f"soft-deleted older than {a.older_than} days"
    n = one(f"SELECT COUNT(*) FROM ve_lexical WHERE {cutoff_clause}", *params)
    print(f"  candidate for purge ({desc}): {n}")
    # age distribution of soft-deletes (transparency)
    for r in c.execute("""SELECT source_provenance, COUNT(*) n, MIN(created_at) oldest, MAX(created_at) newest
                          FROM ve_lexical WHERE delete_flagged=1 GROUP BY source_provenance ORDER BY n DESC LIMIT 8"""):
        print(f"    {(r['source_provenance'] or '(null)'):<32} {r['n']:>7}  {str(r['oldest'])[:10]}..{str(r['newest'])[:10]}")

    if not a.live:
        print("\n[dry-run] no writes. To purge: add --older-than N and --live (a fresh backups/ snapshot is required).")
        c.close(); return

    # --live guards
    if a.older_than is None:
        sys.exit("REFUSED: --live requires --older-than N (never purge recent before-states wholesale).")
    snaps = glob.glob(os.path.join(BK, '*.db'))
    if not snaps:
        sys.exit("REFUSED: no DB snapshot in backups/ — take one before a destructive purge.")
    newest = max(snaps, key=os.path.getmtime)
    print(f"\n⚠ G8-BEFORE CAVEAT: this HARD-deletes {n} soft-deleted rows ({desc}) — those before-states "
          f"are gone (no longer available for a G8 delta). Newest snapshot: {os.path.basename(newest)}")
    cur = c.execute(f"DELETE FROM ve_lexical WHERE {cutoff_clause}", params)
    c.commit()
    print(f"purged {cur.rowcount} rows. active now = {one('SELECT COUNT(*) FROM ve_lexical WHERE COALESCE(delete_flagged,0)=0')}")
    if a.vacuum:
        print("VACUUM (rewriting DB to reclaim file space)...")
        c.execute("VACUUM"); print("VACUUM done.")
    c.close()

if __name__ == '__main__':
    main()
