"""
_apply_fix_verse_context_mti_mismatch_20260701.py

Fix verse_context rows whose mti_term_id disagrees with the morph-authoritative
wa_verse_records.mti_term_id (the term actually at the verse). In all found cases the
verse_context points to a wrong homonym/base entry while wa_verse_records matches the
term_id (source of truth = morph/term_id). Align verse_context.mti_term_id to the
verse_record's value.

Scope: ve_lexical-bearing verse_contexts where vc.mti_term_id != wa_verse_records.mti_term_id
(found 8: 2Ch 21:7, Isa 53:9, Job 31:1, Psa 40:17, 41:7, 52:2, Isa 2:22, 29:17).

Safe: ve_lexical keys on verse_context_id, so no lexical relinking. Backs up first; verifies.
Usage: python scripts/_apply_fix_verse_context_mti_mismatch_20260701.py [--live]
"""
import sqlite3, sys, os, shutil
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv

FIND=("SELECT vc.id vcid, w.reference, w.term_id, vc.mti_term_id vc_mti, w.mti_term_id wvr_mti "
      "FROM ve_lexical vl JOIN verse_context vc ON vl.verse_context_id=vc.id "
      "JOIN wa_verse_records w ON vc.verse_record_id=w.id "
      "WHERE vl.delete_flagged=0 AND vc.mti_term_id IS NOT w.mti_term_id GROUP BY vc.id")

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    rows=cur.execute(FIND).fetchall()
    print('Mismatched ve_lexical-bearing verse_contexts: %d' % len(rows))
    for r in rows:
        s=lambda m: (cur.execute('SELECT strongs_number FROM mti_terms WHERE id=?',(m,)).fetchone() or {'strongs_number':'?'})['strongs_number']
        print('  vc=%d %-10s term=%s  vc_mti=%s(%s) -> wvr_mti=%s(%s)' % (
            r['vcid'], r['reference'], r['term_id'], r['vc_mti'], s(r['vc_mti']), r['wvr_mti'], s(r['wvr_mti'])))
    if not LIVE:
        print('\nDRY-RUN. Re-run with --live to apply.'); return
    os.makedirs('backups',exist_ok=True)
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    bak=os.path.join('backups',f'bible_research.pre-vc-mti-fix.{stamp}.db'); shutil.copy2(DB,bak)
    print('\nBackup:', bak)
    cur.executemany('UPDATE verse_context SET mti_term_id=? WHERE id=?', [(r['wvr_mti'], r['vcid']) for r in rows])
    conn.commit()
    remaining=cur.execute('SELECT COUNT(*) FROM ('+FIND+')').fetchone()[0]
    print('Applied %d fixes. Remaining mismatches: %d (expected 0)' % (len(rows), remaining))

if __name__=='__main__': main()
