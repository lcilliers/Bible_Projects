"""
_check_passage_reading_coverage_v1_20260704.py

CHECK-BACK GATE (read-only) for narrative passage readings. Regulates the two
devastating tendencies the researcher named (2026-07-04):
  (1) BIAS / eisegesis  - reading in meaning not on the verse
  (2) THEME-BUILDING    - skipping the detail, jumping to synthesis

Mechanically it cannot judge bias, but it makes DETAIL-SKIPPING visible and forces
the bias self-audit by listing every non-T2 span the reading must have engaged:

  - VERSE coverage: every verse in the passage that carries a non-T2 span, and whether
    the reading references it (by chapter:verse).
  - GLOSS coverage: every distinct non-T2 gloss, and whether the reading mentions it
    (gloss / transliteration / target english word).
  - REPEATED glosses: every gloss occurring >1x in the passage - flagged so the
    'why is THIS one different' distinction can be confirmed (never lumped).

Output is a checklist + an explicit BIAS-AUDIT prompt. Nothing is written.

Usage:
  python scripts/_check_passage_reading_coverage_v1_20260704.py --unit-code=GEN-01-creation-good \
      [--story=PATH]   # defaults to the filed reading's stored source_file / body
"""
import sqlite3, os, sys, re
DB=os.path.join('database','bible_research.db')
def arg(n,d=None):
    for a in sys.argv[1:]:
        if a.startswith('--%s='%n): return a.split('=',1)[1]
    return d
UNIT=arg('unit-code'); STORY=arg('story')

def norm(s): return re.sub(r'[^a-z0-9]',' ',(s or '').lower())

def main():
    if not UNIT: print("need --unit-code"); return
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    su=cur.execute("SELECT id, book FROM segment_unit WHERE unit_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY id DESC LIMIT 1",(UNIT,)).fetchone()
    if not su: print("no active segment_unit for",UNIT); return
    # reading body: explicit --story, else the filed prose_section for this unit
    if STORY and os.path.exists(STORY):
        body=open(STORY,encoding='utf-8').read()
    else:
        ps=cur.execute("SELECT body, source_file FROM prose_section WHERE json_extract(metadata_json,'$.unit_code')=? AND COALESCE(delete_flagged,0)=0 ORDER BY version DESC LIMIT 1",(UNIT,)).fetchone()
        if not ps: print("no filed reading and no --story; nothing to check"); return
        body=ps['body']
    nb=norm(body)
    # the passage's verses (by unit membership) and their non-T2 spans
    vids=[r['verse_id'] for r in cur.execute("SELECT verse_id FROM segment_unit_verse WHERE unit_id=?",(su['id'],)).fetchall()]
    spans=cur.execute("""SELECT w.chapter ch, w.verse_num vn, w.target_word tw, w.transliteration tr, mt.gloss gloss
        FROM wa_verse_records w JOIN mti_terms mt ON w.mti_term_id=mt.id
        WHERE w.verse_id IN (%s) AND COALESCE(w.delete_flagged,0)=0 AND (mt.cluster_code IS NULL OR mt.cluster_code!='T2')
        ORDER BY w.chapter, w.verse_num""" % ','.join('?'*len(vids)), vids).fetchall()
    # per-verse coverage
    verses={}
    for s in spans: verses.setdefault((s['ch'],s['vn']),[]).append(s)
    print("=== CHECK-BACK: %s ===" % UNIT)
    print("passage verses with non-T2 spans: %d | total non-T2 spans: %d" % (len(verses), len(spans)))
    unref=[]
    for (ch,vn) in sorted(verses):
        refpat=re.compile(r'\b%d\s*[:\. ]\s*%d\b'%(ch,vn))
        if not refpat.search(body): unref.append('%d:%d'%(ch,vn))
    print("\n-- VERSE coverage --")
    print("  verses NOT referenced by ch:vn in the reading: %d %s" % (len(unref), unref if unref else '(none)'))
    # per-gloss coverage
    glosses={}
    for s in spans: glosses.setdefault(s['gloss'],[]).append((s['ch'],s['vn'],s['tw'],s['tr']))
    missG=[]
    for g,occ in glosses.items():
        toks=set()
        for w in (g or '').replace(':',' ').split(): toks.add(w)
        for _,_,tw,tr in occ:
            for w in (tw or '').split(): toks.add(w)
            if tr: toks.add(tr.replace('.',''))
        toks={norm(t).strip() for t in toks if t and len(norm(t).strip())>2}
        if not any(t in nb for t in toks): missG.append((g,len(occ)))
    print("\n-- GLOSS coverage --")
    print("  distinct non-T2 glosses: %d | glosses NOT mentioned (gloss/translit/word): %d" % (len(glosses), len(missG)))
    for g,n in missG: print("     MISS: %-28s (%dx)" % (g, n))
    # repeated glosses (distinction guard)
    reps={g:len(o) for g,o in glosses.items() if len(o)>1}
    print("\n-- REPEATED glosses (confirm each occurrence treated DISTINCTLY, never lumped) --")
    for g,n in sorted(reps.items(), key=lambda x:-x[1]):
        occ=', '.join('%d:%d'%(c,v) for c,v,_,_ in glosses[g])
        print("     %2dx  %-26s @ %s" % (n, g, occ))
    # verdict + bias audit prompt
    print("\n-- VERDICT --")
    ok = (not unref) and (not missG)
    print("  detail-skipping signal: %s" % ("CLEAN (every verse & gloss engaged)" if ok else "REVIEW - address the misses above or justify each explicitly"))
    print("\n-- BIAS SELF-AUDIT (answer before filing) --")
    print("  1. Is every finding read OFF a span in THIS passage (stated) or explicitly inferred from one? Any claim with no span anchor = bias, cut it.")
    print("  2. Did I ask 'why is THIS one different' for each repeated gloss above (not lump)?")
    print("  3. Any NT / systematic-theology / expected meaning imported that the verse does not carry? Remove.")
    print("  4. Did I start building a theme before the detail was exhausted? If a tidy generalisation appeared early, re-open the detail.")

if __name__=='__main__': main()
