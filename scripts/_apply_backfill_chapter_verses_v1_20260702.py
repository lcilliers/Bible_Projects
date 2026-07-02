"""
_apply_backfill_chapter_verses_v1_20260702.py

REUSABLE measure-layer backfill for the CHAPTER-driven poetic pipeline.
The `verse` table is term-sparse (only verses some study term touches); chapter-driven reading needs
WHOLE chapters. This ingests the verses of a chapter that are MISSING from the DB:
  verse row (+ genre from the chapter) + verse_morphology (+ raw html) + verse_span_index projection.
Parameter-driven (no edits): --book --chapter [--maxverse N] [--live].

Reuses the M60 measure-layer method (_apply_ingest_verse_morphology.py): STEP getBibleText interlinear
-> parse spans -> verse_morphology; verse_span_index = straight projection (per _apply_build_verse_span_index_table).

Detects chapter length by probing STEP upward until 2 consecutive absent verses (end of chapter).
Only MISSING verses are fetched. Safe: backup, dry-run default, count-verified.
Usage:
  python scripts/_apply_backfill_chapter_verses_v1_20260702.py --book=Psa --chapter=2
  python scripts/_apply_backfill_chapter_verses_v1_20260702.py --book=Psa --chapter=2 --live
"""
import os, re, sqlite3, sys, shutil, argparse
from datetime import datetime, timezone
import requests
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
import morph_util
DB=os.path.join('database','bible_research.db')
SPAN=re.compile(r"<span\s+morph='([^']*)'\s+strong='([^']*)'>([^<]*)</span>", re.I)
BASE=os.getenv("STEP_LOCAL_URL","http://localhost:8989").rstrip("/"); VER=os.getenv("STEP_VERSION","ESV_th")
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def fetch_verse(ref):
    dotted=ref.replace(" ",".").replace(":",".")
    try:
        d=requests.get(f"{BASE}/rest/bible/getBibleText/{VER}/{dotted}",timeout=30).json()
        return d.get("osisId"), d.get("value","")
    except Exception: return None,""
def b(s):
    m=re.match(r"^([HG]\d+)",s or ""); return m.group(1) if m else (s or "")
def person(m):
    m=m or ""
    x=re.search(r"([123])[SP]",m) if "-" in m else re.search(r"[123]",m)
    return int(x.group(1) if "-" in m else x.group(0)) if x else None
def parse_words(html, vid):
    rows=[]
    for i,(morphs,strongs,text) in enumerate(SPAN.findall(html or "")):
        m0=morphs.split()[0] if morphs.split() else ""
        rows.append((vid,i,text.strip(),strongs, b(strongs.split()[0]) if strongs.split() else None,
                     morphs, morph_util.morph_language(m0), morph_util.morph_category(m0),
                     morph_util.morph_stem(m0), person(m0), "STEP", NOW))
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--book",required=True); ap.add_argument("--chapter",type=int,required=True)
    ap.add_argument("--maxverse",type=int,default=200); ap.add_argument("--live",action="store_true")
    a=ap.parse_args()
    conn=sqlite3.connect(DB,timeout=600); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    meta=cur.execute("SELECT MIN(book_id) bid, MIN(testament) tst FROM verse WHERE reference LIKE ?||' %'",(a.book,)).fetchone()
    if not meta or meta['bid'] is None: print("unknown book '%s'"%a.book); return
    bid=meta['bid']; tst=meta['tst']
    genre=cur.execute("SELECT genre FROM verse WHERE book_id=? AND chapter=? AND genre IS NOT NULL LIMIT 1",(bid,a.chapter)).fetchone()
    genre=genre['genre'] if genre else None
    present={r['verse_num'] for r in cur.execute("SELECT verse_num FROM verse WHERE book_id=? AND chapter=?",(bid,a.chapter)).fetchall()}
    print("book_id=%d testament=%s genre=%s | verses already in DB: %s"%(bid,tst,genre,sorted(present)))
    # probe upward: find MISSING verses present in STEP; stop after 2 consecutive absent (chapter end)
    tobuild=[]; consec_absent=0; vn=0
    while vn < a.maxverse and consec_absent < 2:
        vn+=1
        if vn in present:
            consec_absent=0; continue     # exists in DB -> in chapter, not missing
        ref="%s %d:%d"%(a.book,a.chapter,vn)
        osis,html=fetch_verse(ref)
        if html and "morph='" in html:
            consec_absent=0; tobuild.append((vn,ref,osis,html))
        else:
            consec_absent+=1
    print("MISSING verses present in STEP -> to backfill: %s"%[t[0] for t in tobuild])
    for vn,ref,osis,html in tobuild:
        words=parse_words(html,None)
        print("   %-10s %d words  e.g. %s"%(ref,len(words),", ".join(w[2] for w in words[:6])))
    if not tobuild: print("nothing to backfill."); return
    if not a.live:
        print("\nDRY-RUN. Re-run with --live."); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-backfill.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    built=0
    for vn,ref,osis,html in tobuild:
        words=parse_words(html,None)
        vtext=" ".join(w[2] for w in words)
        cur.execute("""INSERT INTO verse (osis_id,reference,book_id,chapter,verse_num,testament,verse_text,created_at,genre)
            VALUES (?,?,?,?,?,?,?,?,?)""",(osis,ref,bid,a.chapter,vn,tst,vtext,NOW,genre))
        vid=cur.lastrowid
        rows=[(vid,)+w[1:] for w in words]
        cur.executemany("""INSERT INTO verse_morphology
            (verse_id,word_index,surface,strongs,primary_strong,morph_code,language,pos,stem,person,source,fetched_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",rows)
        cur.execute("INSERT OR REPLACE INTO verse_morphology_raw (verse_id,html,fetched_at) VALUES (?,?,?)",(vid,html,NOW))
        cur.execute("""INSERT INTO verse_span_index
            (verse_id,reference,word_index,surface,pos,morph_code,stem,language,strongs,primary_strong)
            SELECT vm.verse_id,?,vm.word_index,vm.surface,vm.pos,vm.morph_code,vm.stem,vm.language,vm.strongs,vm.primary_strong
            FROM verse_morphology vm WHERE vm.verse_id=? ORDER BY vm.word_index""",(ref,vid))
        built+=1
    conn.commit()
    print("backfilled %d verses (verse + morphology + span_index). genre=%s. passage_id left NULL (poetic ignores; rebuild passages if needed)."%(built,genre))

if __name__=="__main__": main()
