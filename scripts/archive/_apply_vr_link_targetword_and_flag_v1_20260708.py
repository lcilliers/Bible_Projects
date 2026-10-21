"""Second-pass verse-record link repair for the multi-span (ambiguous) OT residual.

After the deterministic 1-span repair, the leftover multi-span records (term repeats in the verse)
are resolved here ONLY where `target_word` matches exactly one span's surface. The rest are marked
`analysis_marker='SPAN_UNRESOLVED'` so the reading step resolves them (no guessing).

Read-only unless --live. Backup before writing.
"""
import sqlite3, os, sys, shutil, datetime
DB='database/bible_research.db'; LIVE='--live' in sys.argv
def base(s): return s[:-1] if (s and len(s)>1 and s[-1].isalpha() and s[0] in 'HG') else s

def main():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
    ot=[r['id'] for r in cur.execute("SELECT id FROM books WHERE testament='OT'")]
    ins=','.join('?'*len(ot))
    rows=cur.execute("SELECT id,reference,term_id,target_word,analysis_marker FROM wa_verse_records WHERE book_id IN (%s) AND COALESCE(delete_flagged,0)=0 AND verse_span_id IS NULL"%ins, ot).fetchall()
    if LIVE:
        NOW=datetime.datetime.now(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')
        bp='backups/bible_research.pre-vrtw-%s.db'%NOW; os.makedirs('backups',exist_ok=True); shutil.copy2(DB,bp); print('backup:',bp)
    linked=flagged=0
    for r in rows:
        v=cur.execute('SELECT id FROM verse WHERE reference=?',(r['reference'],)).fetchone()
        if not v: continue
        spans=cur.execute('SELECT id,surface FROM verse_span_index WHERE verse_id=? AND (primary_strong=? OR substr(primary_strong,1,5)=?) ORDER BY word_index',(v['id'],r['term_id'],base(r['term_id']))).fetchall()
        if len(spans)<2: continue  # 1-span handled elsewhere; 0-span is a data issue
        tw=(r['target_word'] or '').strip().lower()
        match=[s for s in spans if tw and (s['surface'] or '').strip().lower()==tw]
        if len(match)==1:
            if LIVE: cur.execute('UPDATE wa_verse_records SET verse_span_id=? WHERE id=?',(match[0]['id'],r['id']))
            linked+=1
        else:
            if r['analysis_marker']!='SPAN_UNRESOLVED':
                if LIVE: cur.execute("UPDATE wa_verse_records SET analysis_marker='SPAN_UNRESOLVED' WHERE id=?",(r['id'],))
                flagged+=1
    if LIVE: c.commit()
    print('multi-span residual processed: linked via target_word=%d | flagged SPAN_UNRESOLVED=%d'%(linked,flagged))
    if not LIVE: print('DRY-RUN — re-run with --live.')

if __name__=='__main__': main()
