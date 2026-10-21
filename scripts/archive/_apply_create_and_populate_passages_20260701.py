"""
_apply_create_and_populate_passages_20260701.py

Create the passage layer (verse-level) and auto-populate from the isolable='no' backward
links (the reset adjacency-checker). A passage = a maximal run of consecutive same-chapter
verses each reading-back to its predecessor.

Schema:
  passage(id, ref, anchor_verse_id, book_id, start_chapter, start_verse,
          end_chapter, end_verse, verse_count, source, review_flag, notes, created_at)
  verse.passage_id  -> passage.id   (every member verse points to its passage)

Populate:
  - clean 2-3 verse same-chapter runs         -> source='auto', review_flag=NULL
  - >=4 verse runs                             -> source='auto', review_flag='extended'
  - cross-chapter readbacks (verse 1)          -> source='auto', review_flag='cross-chapter' (singleton, needs manual predecessor)

Safe: backs up; dry-run default; verifies. Reversible (DROP passage + column re-derive).
Usage: python scripts/_apply_create_and_populate_passages_20260701.py [--live]
"""
import sqlite3, sys, os, shutil, collections
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()

    # readback verses (verse-level): any term isolable='no'
    rb=cur.execute("""SELECT DISTINCT v.id vid, v.book_id b, v.chapter ch, v.verse_num vn, v.reference ref
       FROM ve_lexical vl JOIN verse_context vc ON vl.verse_context_id=vc.id
       JOIN wa_verse_records w ON vc.verse_record_id=w.id JOIN verse v ON w.verse_id=v.id
       WHERE vl.ve_label='isolable' AND vl.value='no' AND vl.delete_flagged=0""").fetchall()
    coord2vid={}
    bookname={}
    for r in cur.execute("SELECT id,book_id,chapter,verse_num,reference FROM verse").fetchall():
        coord2vid[(r['book_id'],r['chapter'],r['verse_num'])]=r['id']
        # crude book label from reference prefix
        bookname[r['book_id']]=r['reference'].rsplit(' ',1)[0]

    parent={}
    def find(x):
        parent.setdefault(x,x)
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        ra,rb_=find(a),find(b)
        if ra!=rb_: parent[ra]=rb_
    cross=[]
    for r in rb:
        node=(r['b'],r['ch'],r['vn']); find(node)
        if r['vn']>1: pred=(r['b'],r['ch'],r['vn']-1); find(pred); union(node,pred)
        else: cross.append(node)
    comp=collections.defaultdict(set)
    for n in list(parent.keys()): comp[find(n)].add(n)
    passages=[sorted(s) for s in comp.values() if len(s)>=2]

    # build rows
    rows=[]  # (ref, anchor_vid, book,sch,sv,ech,ev,count,source,flag,notes, member_vids)
    for nodes in passages:
        b=nodes[0][0]; sch,sv=nodes[0][1],nodes[0][2]; ech,ev=nodes[-1][1],nodes[-1][2]
        anchor=coord2vid.get(nodes[0])
        vids=[coord2vid[n] for n in nodes if n in coord2vid]
        ref="%s %d:%d-%d"%(bookname.get(b,'?'),sch,sv,ev)
        flag='extended' if len(nodes)>=4 else None
        rows.append((ref,anchor,b,sch,sv,ech,ev,len(nodes),'auto',flag,None,vids))
    for n in cross:
        anchor=coord2vid.get(n); b,ch,vn=n
        ref="%s %d:%d"%(bookname.get(b,'?'),ch,vn)
        rows.append((ref,anchor,b,ch,vn,ch,vn,1,'auto','cross-chapter','reads with prior chapter; needs manual predecessor',[anchor] if anchor else []))

    nflag=collections.Counter(r[9] for r in rows)
    print('passages to create: %d (multi-verse %d + cross-chapter %d)'%(len(rows),len(passages),len(cross)))
    print('  review_flag: none(auto)=%d extended=%d cross-chapter=%d'%(nflag[None],nflag['extended'],nflag['cross-chapter']))
    if not LIVE:
        print('\nDRY-RUN. Re-run with --live to apply.'); return

    os.makedirs('backups',exist_ok=True)
    bak=os.path.join('backups',f'bible_research.pre-passages.{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.db')
    shutil.copy2(DB,bak); print('\nBackup:',bak)

    cur.execute("""CREATE TABLE IF NOT EXISTS passage (
      id INTEGER PRIMARY KEY, ref TEXT, anchor_verse_id INTEGER,
      book_id INTEGER, start_chapter INTEGER, start_verse INTEGER,
      end_chapter INTEGER, end_verse INTEGER, verse_count INTEGER,
      source TEXT, review_flag TEXT, notes TEXT, created_at TEXT)""")
    cols=[r[1] for r in cur.execute("PRAGMA table_info(verse)").fetchall()]
    if 'passage_id' not in cols:
        cur.execute("ALTER TABLE verse ADD COLUMN passage_id INTEGER")
    inserted=0; linked=0
    for (ref,anchor,b,sch,sv,ech,ev,cnt,src,flag,notes,vids) in rows:
        cur.execute("""INSERT INTO passage (ref,anchor_verse_id,book_id,start_chapter,start_verse,end_chapter,end_verse,verse_count,source,review_flag,notes,created_at)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",(ref,anchor,b,sch,sv,ech,ev,cnt,src,flag,notes,NOW))
        pid=cur.lastrowid; inserted+=1
        for vid in vids:
            cur.execute("UPDATE verse SET passage_id=? WHERE id=?",(pid,vid)); linked+=cur.rowcount
    conn.commit()
    print('passages inserted: %d ; verses linked to a passage: %d'%(inserted,linked))
    print('verify: verse.passage_id populated =', cur.execute("SELECT COUNT(*) FROM verse WHERE passage_id IS NOT NULL").fetchone()[0])

if __name__=='__main__': main()
