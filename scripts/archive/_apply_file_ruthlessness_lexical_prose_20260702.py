"""
_apply_file_ruthlessness_lexical_prose_20260702.py

Pipeline endpoint: file the accepted ruthlessness first-tier story into the prose tables
as the LEXICAL PROSE for ruthlessness (source = lexical-model-2026 only).

- Creates prose_section_type 'lexical_prose' if absent (the new-model single-term story convention).
- Inserts one prose_section: registry_id=216 (Ruthlessness), cluster_code M06, body = the accepted story.
- Version-aware: if a lexical_prose row already exists for this registry, supersede it (version+1,
  supersedes_id link, mark old superseded_by_id) rather than overwrite.
- Verse citations live INLINE in the story (act->impact->source cited); the finding-centric
  wa_prose_section_citations table does not fit lexical prose, so the verse list + span provenance
  are recorded in metadata_json.

Safe: backup, dry-run default, verify. Usage: python scripts/_apply_file_ruthlessness_lexical_prose_20260702.py [--live]
"""
import sqlite3, os, sys, shutil, json
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
REG=216; CC='M06'; TYPE_CODE='lexical_prose'
STORY=os.path.join('verse-analysis','_reports','wa-ruthlessness-story-refined-20260702.md')
VERSES=['Exo 1:13','Exo 1:14','Lev 25:43','Lev 25:46','Lev 25:53','Eze 34:4']

def main():
    body=open(STORY,encoding='utf-8').read()
    wc=len(body.split())
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    # section type
    t=cur.execute("SELECT id FROM prose_section_type WHERE code=?",(TYPE_CODE,)).fetchone()
    tid=t['id'] if t else None
    # existing lexical_prose for this registry (active)
    prev=None
    if tid:
        prev=cur.execute("""SELECT id,version FROM prose_section WHERE registry_id=? AND section_type_id=?
            AND COALESCE(delete_flagged,0)=0 ORDER BY version DESC LIMIT 1""",(REG,tid)).fetchone()
    new_ver=(prev['version']+1) if prev and prev['version'] else 1
    meta=json.dumps({'term':'H6531','cluster_code':CC,'source':'lexical-model-2026',
                     'verses':VERSES,'roles':'characteristic (6 spans)','story_file':STORY,
                     'method':'wa-verse-analysis-method-v1-20260702','tier':'first-tier'})
    print("=== PLAN ===")
    print(" section_type 'lexical_prose' exists:", bool(tid), "(id=%s)"%tid)
    print(" prior lexical_prose for reg %d:"%REG, dict(prev) if prev else None, "-> new version", new_ver)
    print(" body words:", wc)
    if not LIVE:
        print("\nDRY-RUN. Re-run with --live."); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-lexprose.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    if not tid:
        msort=cur.execute("SELECT COALESCE(MAX(sort_order),200)+1 s FROM prose_section_type").fetchone()['s']
        cur.execute("""INSERT INTO prose_section_type (code,label,source_stage,chapter_no,description,sort_order,delete_flagged,created_at)
            VALUES (?,?,?,?,?,?,0,?)""",(TYPE_CODE,'Lexical Prose (single-term story)','verse-analysis',1,
            'The accepted single-term first-tier story built from lexical-model-2026 ve-records only (method v1-20260702). One per owner term.',msort,NOW))
        tid=cur.lastrowid
    cur.execute("""INSERT INTO prose_section
        (registry_id,section_type_id,heading,body,word_count,status,version,supersedes_id,author,created_at,metadata_json,source_file,delete_flagged,cluster_code)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,0,?)""",
        (REG,tid,'Ruthlessness — lexical prose',body,wc,'approved',new_ver,prev['id'] if prev else None,
         'claude_code',NOW,meta,STORY,CC))
    nid=cur.lastrowid
    if prev:
        cur.execute("UPDATE prose_section SET superseded_by_id=?, delete_flagged=1 WHERE id=?",(nid,prev['id']))
    conn.commit()
    print("wrote prose_section id=%d (type_id=%d, version=%d)."%(nid,tid,new_ver))
    # verify
    r=cur.execute("SELECT id,heading,version,status,word_count,cluster_code FROM prose_section WHERE id=?",(nid,)).fetchone()
    print("verify:", dict(r))

if __name__=='__main__': main()
