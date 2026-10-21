"""_apply_supersede_old_mechanical.py — WRITES (reversible soft-delete). Supersedes the old l2_mechanical
5-field findings for every verse the verse-read has covered (i.e. any verse_context_id that now has an
l2_meaning paragraph). The verse-read l2_api output is strictly richer (~14 fields incl. the old 5), so the
old mechanical rows are redundant. Soft-delete only (delete_flagged=1), provenance-scoped → fully reversible.
Idempotent: re-runnable after each cluster. Use --undo to restore.

Usage:  python scripts/_apply_supersede_old_mechanical.py [--dry-run] [--undo]
"""
import argparse, sqlite3, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

ap = argparse.ArgumentParser()
ap.add_argument("--dry-run", action="store_true")
ap.add_argument("--undo", action="store_true")
a = ap.parse_args()
c = sqlite3.connect(DB)

if a.undo:
    n = c.execute("""UPDATE finding SET delete_flagged=0 WHERE provenance='l2_mechanical' AND delete_flagged=1
                     AND verse_context_id IN (SELECT DISTINCT verse_context_id FROM finding WHERE provenance='l2_meaning')""").rowcount
    if not a.dry_run:
        c.commit()
    print(f"{'WOULD restore' if a.dry_run else 'restored'} {n} l2_mechanical findings")
    sys.exit(0)

covered = c.execute("SELECT COUNT(DISTINCT verse_context_id) FROM finding WHERE provenance='l2_meaning'").fetchone()[0]
target = c.execute("""SELECT COUNT(*) FROM finding WHERE provenance='l2_mechanical' AND COALESCE(delete_flagged,0)=0
                      AND verse_context_id IN (SELECT DISTINCT verse_context_id FROM finding WHERE provenance='l2_meaning')""").fetchone()[0]
print(f"verse-read-covered verses: {covered} | old l2_mechanical to supersede: {target}")
if not a.dry_run:
    n = c.execute("""UPDATE finding SET delete_flagged=1 WHERE provenance='l2_mechanical' AND COALESCE(delete_flagged,0)=0
                     AND verse_context_id IN (SELECT DISTINCT verse_context_id FROM finding WHERE provenance='l2_meaning')""").rowcount
    c.commit()
    remaining = c.execute("SELECT COUNT(*) FROM finding WHERE provenance='l2_mechanical' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f"superseded {n} | l2_mechanical still active (clusters not yet verse-read): {remaining}")
else:
    print("[dry-run] no writes")
