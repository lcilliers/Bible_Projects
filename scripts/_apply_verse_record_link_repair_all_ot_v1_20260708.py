"""Verse-record -> verse / master-index link repair, WHOLE OT in one pass.

Same deterministic logic as _apply_verse_record_link_repair_v1_20260707.py (per-book), run over
every OT book. Fixes verse-records left with NULL verse_id / verse_span_id (data already in the DB,
just never linked to the master index). NO new data, NO guessing:
  - verse_id  : set from reference (unambiguous).
  - verse_span_id: set ONLY when exactly ONE master span matches (verse_id + exact strong, else base
    strong). Multi-span (ambiguous) and no-span records are LEFT and reported.

Read-only unless --live. Takes a backup before writing.
"""
import sqlite3, os, sys, shutil, datetime
DB='database/bible_research.db'; LIVE='--live' in sys.argv
def base(s): return s[:-1] if (s and len(s)>1 and s[-1].isalpha() and s[0] in 'HG') else s

def main():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
    ot=[r['id'] for r in cur.execute("SELECT id FROM books WHERE testament='OT'")]
    rows=[dict(r) for r in cur.execute(
        "SELECT id,reference,term_id,verse_id,verse_span_id FROM wa_verse_records "
        "WHERE book_id IN (%s) AND COALESCE(delete_flagged,0)=0 AND (verse_id IS NULL OR verse_span_id IS NULL)"
        % ','.join('?'*len(ot)), ot)]
    print('OT verse-records needing a link:', len(rows))

    if LIVE:
        NOW=datetime.datetime.now(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')
        bp='backups/bible_research.pre-vrlinkrepair-%s.db'%NOW
        os.makedirs('backups',exist_ok=True); shutil.copy2(DB,bp); print('backup:',bp)

    set_vid=set_span=amb=nospan=novref=0
    for r in rows:
        v=cur.execute('SELECT id FROM verse WHERE reference=?',(r['reference'],)).fetchone()
        if not v: novref+=1; continue
        vid=v['id']
        if r['verse_id'] is None:
            if LIVE: cur.execute('UPDATE wa_verse_records SET verse_id=? WHERE id=?',(vid,r['id']))
            set_vid+=1
        if r['verse_span_id'] is None:
            cand=[x['id'] for x in cur.execute('SELECT id FROM verse_span_index WHERE verse_id=? AND primary_strong=? ORDER BY word_index',(vid,r['term_id']))]
            if len(cand)!=1:
                cand=[x['id'] for x in cur.execute('SELECT id FROM verse_span_index WHERE verse_id=? AND substr(primary_strong,1,5)=? ORDER BY word_index',(vid,base(r['term_id'])))]
            if len(cand)==1:
                if LIVE: cur.execute('UPDATE wa_verse_records SET verse_span_id=? WHERE id=?',(cand[0],r['id']))
                set_span+=1
            elif len(cand)>1: amb+=1
            else: nospan+=1
    if LIVE: c.commit()
    print('  verse_id set (passage tracking)        : %d'%set_vid)
    print('  verse_span_id set (master link, 1-span): %d'%set_span)
    print('  LEFT ambiguous (multi-span, SPAN_UNRESOLVED): %d'%amb)
    print('  LEFT no matching span                  : %d'%nospan)
    print('  LEFT reference unresolved              : %d'%novref)
    if not LIVE: print('\nDRY-RUN — re-run with --live.')

if __name__=='__main__': main()
