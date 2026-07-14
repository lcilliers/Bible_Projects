#!/usr/bin/env python
"""Cadence-aware DB snapshot + prune helper (v1, 2026-07-14).

Proverbs retrospective: the per-cycle `cp` of the 0.8 GB DB created ~60 snapshots
(~48 GB churn). Cadence v2 says snapshot every N cycles, not every cycle, and cap the
retained set. This helper does both:
  - only snapshots when the cycle is on-cadence (cycle==1 or cycle % every == 0), unless forced;
  - prunes reread snapshots beyond --keep (newest kept), reclaiming disk.
Only touches files matching the reread-snapshot name pattern in backups/; never db_backups/
or unrelated files.

Usage:
  python scripts/_snapshot_db_v1_20260714.py --tag pre-read-cycle40 --cycle 40 --every 5 --keep 6
  python scripts/_snapshot_db_v1_20260714.py --tag pre-bookclose --force        # always snapshot
  python scripts/_snapshot_db_v1_20260714.py --prune-only --keep 6              # just prune
"""
import os, sys, shutil, glob, argparse, datetime

DB = os.path.join('database', 'bible_research.db')
BK = 'backups'
PATTERN = os.path.join(BK, 'bible_research_reread-*.db')  # only reread snapshots this helper creates

def prune(keep):
    snaps = sorted(glob.glob(PATTERN), key=os.path.getmtime, reverse=True)
    for old in snaps[keep:]:
        try:
            os.remove(old); print(f"  pruned {os.path.basename(old)}")
        except OSError as e:
            print(f"  (could not prune {old}: {e})")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tag', help='snapshot label (e.g. pre-read-cycle40)')
    ap.add_argument('--cycle', type=int, help='current cycle number (for cadence gating)')
    ap.add_argument('--every', type=int, default=5, help='snapshot every N cycles (default 5)')
    ap.add_argument('--keep', type=int, default=6, help='retain newest N reread snapshots (default 6)')
    ap.add_argument('--force', action='store_true', help='snapshot regardless of cadence')
    ap.add_argument('--prune-only', action='store_true')
    a = ap.parse_args()

    if a.prune_only:
        print(f"# prune reread snapshots, keep newest {a.keep}")
        prune(a.keep); return

    if not a.tag:
        sys.exit("give --tag (or --prune-only)")
    on_cadence = a.force or a.cycle is None or a.cycle == 1 or (a.every and a.cycle % a.every == 0)
    if not on_cadence:
        print(f"cycle {a.cycle} off-cadence (every {a.every}) — no snapshot (git commit is the finer-grained safety). "
              f"Use --force to override.")
        return
    date = datetime.date.today().strftime('%Y%m%d')
    dest = os.path.join(BK, f"bible_research_reread-{a.tag}_{date}.db")
    shutil.copy2(DB, dest)
    print(f"snapshot: {dest} ({os.path.getsize(dest)//(1024*1024)} MB)")
    prune(a.keep)

if __name__ == '__main__':
    main()
