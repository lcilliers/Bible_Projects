"""
_apply_file_chapter_lexical_prose_v1_20260702.py

REUSABLE Phase-2 endpoint for poetic (chapter-driven) books: file a whole-chapter inner-being
reading into the prose tables under type 'lexical_prose_chapter' (one per book+chapter).
Parameter-driven (no editing): --book, --chapter, --story=PATH, --heading.

- creates prose_section_type 'lexical_prose_chapter' if absent.
- inserts one prose_section (registry_id NULL — a chapter is not a single registry word;
  book/chapter/verses/characteristics recorded in metadata_json; cluster_code left NULL = multi-characteristic).
- version-aware: supersedes any prior active chapter reading for the same book+chapter.

Safe: backup, dry-run default, verify.
Usage:
  python scripts/_apply_file_chapter_lexical_prose_v1_20260702.py --book=Psa --chapter=1 \
      --story=verse-analysis/_reports/wa-psalm1-inner-being-reading-20260702.md \
      --heading="Psalm 1 - inner-being reading" [--live]
"""
import sqlite3, os, sys, shutil, json
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db')
def arg(n,d=None):
    for a in sys.argv[1:]:
        if a.startswith('--%s='%n): return a.split('=',1)[1]
    return d
LIVE='--live' in sys.argv
BOOK=arg('book'); CHAP=int(arg('chapter')); STORY=arg('story'); HEADING=arg('heading') or ('%s %d - inner-being reading'%(BOOK,CHAP))
TYPE_CODE='lexical_prose_chapter'; NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def main():
    if not (BOOK and CHAP and STORY): print("need --book --chapter --story"); return
    body=open(STORY,encoding='utf-8').read(); wc=len(body.split())
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    bid=cur.execute("SELECT DISTINCT book_id FROM verse WHERE reference LIKE ?||' %' LIMIT 1",(BOOK,)).fetchone()
    verses=[r['reference'] for r in cur.execute("SELECT reference FROM verse WHERE book_id=? AND chapter=? ORDER BY verse_num",(bid['book_id'],CHAP)).fetchall()] if bid else []
    # characteristics present (sanity-checked role) for this chapter
    chars=cur.execute("""SELECT DISTINCT si.primary_strong, mt.cluster_code, mt.gloss FROM ve_lexical role
        JOIN verse_span_index si ON role.verse_span_id=si.id JOIN verse v ON si.verse_id=v.id
        LEFT JOIN wa_verse_records w ON w.verse_id=v.id AND (w.term_id=si.primary_strong OR w.term_id=substr(si.primary_strong,1,5))
        LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id
        WHERE v.book_id=? AND v.chapter=? AND role.ve_label='role' AND role.value='characteristic'
          AND role.source_provenance='lexical-model-2026' AND COALESCE(role.delete_flagged,0)=0""",(bid['book_id'],CHAP)).fetchall()
    charlist=sorted({(r['primary_strong'] or '', r['cluster_code'] or '') for r in chars})
    t=cur.execute("SELECT id FROM prose_section_type WHERE code=?",(TYPE_CODE,)).fetchone(); tid=t['id'] if t else None
    prev=cur.execute("""SELECT id,version FROM prose_section WHERE section_type_id=? AND json_extract(metadata_json,'$.book')=? AND json_extract(metadata_json,'$.chapter')=?
        AND COALESCE(delete_flagged,0)=0 ORDER BY version DESC LIMIT 1""",(tid,BOOK,CHAP)).fetchone() if tid else None
    new_ver=(prev['version']+1) if prev and prev['version'] else 1
    meta=json.dumps({'book':BOOK,'chapter':CHAP,'verses':verses,'source':'lexical-model-2026',
                     'characteristics':['%s/%s'%(s,c) for s,c in charlist],'story_file':STORY,
                     'method':'wa-poetic-chapter-method-and-psalm1-plan-v1-20260702','phase':'2-chapter-reading'})
    print("=== PLAN ===")
    print(" type '%s' exists:"%TYPE_CODE, bool(tid), "verses:", len(verses), "characteristics:", charlist)
    print(" prior chapter reading:", dict(prev) if prev else None, "-> version", new_ver, "| body words:", wc)
    if not LIVE:
        print("\nDRY-RUN. Re-run with --live."); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-chapprose.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    if not tid:
        msort=cur.execute("SELECT COALESCE(MAX(sort_order),200)+1 s FROM prose_section_type").fetchone()['s']
        cur.execute("""INSERT INTO prose_section_type (code,label,source_stage,chapter_no,description,sort_order,delete_flagged,created_at)
            VALUES (?,?,?,?,?,?,0,?)""",(TYPE_CODE,'Lexical Prose (chapter reading)','verse-analysis',1,
            'Whole-chapter inner-being reading for poetic books (Psalms/Proverbs), built from lexical-model-2026 Phase-1 lexicals. Multi-characteristic. One per book+chapter.',msort,NOW))
        tid=cur.lastrowid
    cur.execute("""INSERT INTO prose_section
        (registry_id,section_type_id,heading,body,word_count,status,version,supersedes_id,author,created_at,metadata_json,source_file,delete_flagged)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,0)""",
        (None,tid,HEADING,body,wc,'approved',new_ver,prev['id'] if prev else None,'claude_code',NOW,meta,STORY))
    nid=cur.lastrowid
    if prev: cur.execute("UPDATE prose_section SET superseded_by_id=?, delete_flagged=1 WHERE id=?",(nid,prev['id']))
    conn.commit()
    r=cur.execute("SELECT id,heading,version,status,word_count,section_type_id FROM prose_section WHERE id=?",(nid,)).fetchone()
    print("wrote prose_section:", dict(r))

if __name__=='__main__': main()
