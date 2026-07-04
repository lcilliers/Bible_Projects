"""
_apply_file_passage_lexical_prose_v1_20260704.py

REUSABLE Phase-2 endpoint for NARRATIVE (passage-driven) books: file one inner-being
reading per PASSAGE (segment_unit), under type 'lexical_prose_passage'. Sibling of the
chapter-level filer (_apply_file_chapter_lexical_prose) — needed because a narrative
chapter can hold several passages, so filing must key on unit_code, not chapter.

- creates prose_section_type 'lexical_prose_passage' if absent.
- resolves the segment_unit by (book, unit_code, active) to record verse_refs + anchor chapter.
- inserts one prose_section (registry_id NULL); metadata carries book/unit_code/verse_refs/anchor_chapter.
- version-aware: supersedes any prior active reading for the same unit_code.

Safe: backup (self-pruning), dry-run default, verify.
Usage:
  python scripts/_apply_file_passage_lexical_prose_v1_20260704.py --book=Gen --unit-code=GEN-01-creation-good \
      --story=verse-analysis/genesis/readings/wa-gen01-creation-good-20260704.md [--heading="..."] [--live] [--no-backup]
"""
import sqlite3, os, sys, shutil, json, glob
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db')
NO_BACKUP='--no-backup' in sys.argv
LIVE='--live' in sys.argv

def snapshot_db(prune_keep=3):
    if NO_BACKUP:
        print(" [--no-backup: skipping pre-passageprose snapshot]"); return
    dst=os.path.join('backups','bible_research.pre-passageprose.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    shutil.copy2(DB,dst)
    snaps=sorted(glob.glob(os.path.join('backups','bible_research.pre-passageprose.*.db')))
    for old in snaps[:-prune_keep]:
        try: os.remove(old)
        except OSError: pass

def arg(n,d=None):
    for a in sys.argv[1:]:
        if a.startswith('--%s='%n): return a.split('=',1)[1]
    return d

BOOK=arg('book'); UNIT=arg('unit-code'); STORY=arg('story'); HEADING=arg('heading')
TYPE_CODE='lexical_prose_passage'; NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def main():
    if not (BOOK and UNIT and STORY): print("need --book --unit-code --story"); return
    if not os.path.exists(STORY): print("story file not found:", STORY); return
    body=open(STORY,encoding='utf-8').read(); wc=len(body.split())
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    su=cur.execute("""SELECT id, chapter, verse_ref_summary, gist FROM segment_unit
        WHERE book=? AND unit_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY id DESC LIMIT 1""",(BOOK,UNIT)).fetchone()
    if not su: print("no active segment_unit for %s / %s"%(BOOK,UNIT)); return
    verse_refs=[r['reference'] for r in cur.execute("""SELECT v.reference FROM segment_unit_verse suv
        JOIN verse v ON v.id=suv.verse_id WHERE suv.unit_id=? ORDER BY v.chapter, v.verse_num""",(su['id'],)).fetchall()]
    anchor_chapter=su['chapter']
    heading=HEADING or ('%s %s - inner-being reading'%(BOOK,UNIT))
    t=cur.execute("SELECT id FROM prose_section_type WHERE code=?",(TYPE_CODE,)).fetchone(); tid=t['id'] if t else None
    prev=cur.execute("""SELECT id,version FROM prose_section WHERE section_type_id=? AND json_extract(metadata_json,'$.unit_code')=?
        AND COALESCE(delete_flagged,0)=0 ORDER BY version DESC LIMIT 1""",(tid,UNIT)).fetchone() if tid else None
    new_ver=(prev['version']+1) if prev and prev['version'] else 1
    meta=json.dumps({'book':BOOK,'unit_code':UNIT,'segment_unit_id':su['id'],'anchor_chapter':anchor_chapter,
                     'verse_refs':verse_refs,'source':'lexical-model-2026','story_file':STORY,
                     'method':'wa-ot-narrative-inner-being-method-v1-20260704','phase':'2-passage-reading'})
    print("=== PLAN ===")
    print(" type '%s' exists:"%TYPE_CODE, bool(tid), "| unit:", UNIT, "| anchor ch:", anchor_chapter, "| verses:", len(verse_refs))
    print(" prior reading:", dict(prev) if prev else None, "-> version", new_ver, "| body words:", wc)
    if not LIVE:
        print("\nDRY-RUN. Re-run with --live."); return
    snapshot_db()
    if not tid:
        msort=cur.execute("SELECT COALESCE(MAX(sort_order),200)+1 s FROM prose_section_type").fetchone()['s']
        cur.execute("""INSERT INTO prose_section_type (code,label,source_stage,chapter_no,description,sort_order,delete_flagged,created_at)
            VALUES (?,?,?,?,?,?,0,?)""",(TYPE_CODE,'Lexical Prose (passage reading)','verse-analysis',1,
            'Per-passage inner-being reading for narrative books, built from verse-first lexicals over an operation-web passage (segment_unit). Multi-characteristic. One per unit_code.',msort,NOW))
        tid=cur.lastrowid
    cur.execute("""INSERT INTO prose_section
        (registry_id,section_type_id,heading,body,word_count,status,version,supersedes_id,author,created_at,metadata_json,source_file,delete_flagged)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,0)""",
        (None,tid,heading,body,wc,'approved',new_ver,prev['id'] if prev else None,'claude_code',NOW,meta,STORY))
    nid=cur.lastrowid
    if prev: cur.execute("UPDATE prose_section SET superseded_by_id=?, delete_flagged=1 WHERE id=?",(nid,prev['id']))
    conn.commit()
    r=cur.execute("SELECT id,heading,version,status,word_count,section_type_id FROM prose_section WHERE id=?",(nid,)).fetchone()
    print("wrote prose_section:", dict(r))

if __name__=='__main__': main()
