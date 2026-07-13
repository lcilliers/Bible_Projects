"""Isolate duplicate ACTIVE mti_terms rows — one active row per Strong's (OT-DBR-009).

mti_terms is meant to be UNIQUE per Strong's (CLAUDE.md §3). Where >1 active row exists,
keep the CANONICAL row and delete-flag the redundant ones, so historic/orphan stubs are
isolated and cannot interfere with the study (readiness isolation principle §B).

Keeper rule (per Strong's, among active rows):
  rank by (owning_registry_fk IS NOT NULL, status != 'delete', verse_record_count) DESC.
  The top row is the keeper; the rest are delete_flagged. A redundant row is ONLY flagged
  if it has 0 active verse_records (safety: never flag a row that holds data).

Systematic (root fix, not one-off): processes EVERY duplicated Strong's programme-wide.
Read-only unless --live.  Usage:
  python scripts/_apply_mti_dedup_active_duplicates_v1_20260713.py            # dry-run
  python scripts/_apply_mti_dedup_active_duplicates_v1_20260713.py --live
"""
import sqlite3, os, sys, datetime

DB = os.path.join('database', 'bible_research.db')
LIVE = '--live' in sys.argv


def vr_count(c, mti_id):
    return c.execute(
        "SELECT COUNT(*) FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0",
        (mti_id,)).fetchone()[0]


def main():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    dups = [r['strongs_number'] for r in c.execute(
        "SELECT strongs_number FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 "
        "GROUP BY strongs_number HAVING COUNT(*)>1")]
    print(f"{len(dups)} Strong's with >1 active mti row.\n")
    to_flag = []
    skipped = []
    for s in dups:
        rows = [dict(r) for r in c.execute(
            "SELECT id, owning_registry_fk, owning_word, status FROM mti_terms "
            "WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0", (s,))]
        for r in rows:
            r['vr'] = vr_count(c, r['id'])
        rows.sort(key=lambda r: (r['owning_registry_fk'] is not None,
                                 (r['status'] or '') != 'delete', r['vr']), reverse=True)
        keeper, redundant = rows[0], rows[1:]
        for r in redundant:
            if r['vr'] > 0:
                skipped.append((s, r['id'], r['vr']))  # SAFETY: never flag a row with data
            else:
                to_flag.append((s, r['id'], keeper['id']))
        print(f"  {s}: keep id={keeper['id']} (reg={keeper['owning_registry_fk']}, vr={keeper['vr']}) "
              f"| flag {[r['id'] for r in redundant if r['vr']==0]}"
              + (f" | SKIP-has-data {[r['id'] for r in redundant if r['vr']>0]}" if any(r['vr']>0 for r in redundant) else ""))

    print(f"\nto delete-flag: {len(to_flag)} rows | skipped (hold data, need manual reconcile): {len(skipped)}")
    if skipped:
        print("  SKIPPED:", skipped)
    if not LIVE:
        print("\nDRY-RUN. Re-run with --live to apply.")
        return
    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    for s, rid, keep in to_flag:
        c.execute("UPDATE mti_terms SET delete_flagged=1, last_changed=?, "
                  "exclusion_reason=COALESCE(exclusion_reason,'mti-dedup-2026: redundant active duplicate, 0 records, canonical='||?) "
                  "WHERE id=?", (now, str(keep), rid))
    c.commit()
    print(f"\n[LIVE] delete-flagged {len(to_flag)} redundant rows.")
    left = c.execute("SELECT COUNT(*) FROM (SELECT strongs_number FROM mti_terms "
                     "WHERE COALESCE(delete_flagged,0)=0 GROUP BY strongs_number HAVING COUNT(*)>1)").fetchone()[0]
    print(f"Strong's with >1 active row remaining: {left}")


if __name__ == '__main__':
    main()
