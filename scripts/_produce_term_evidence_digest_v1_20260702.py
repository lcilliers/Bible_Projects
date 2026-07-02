"""
_produce_term_evidence_digest_v1_20260702.py  (READ-ONLY)

The COLLATION step of the narrative-synthesis process: for an owner term, assemble the EVIDENCE
DIGEST from all its verse-lexicals (new-model ve_lexical) — the scalable, repeatable input the
synthesis reads to write the narrative ("what does it say about the inner being").

Scales trivially: works for any term and ANY number of verses (5 today, 15 later — same operation).
The narrative is always REGENERATED from the full digest, never patched — so adding verses just
re-runs collate + synthesise over the larger set.

Output: a compact, ordered digest — per verse, the TERM's lexical items + the co-terms in that
verse (context), grouped by passage. This is the synthesis input, not the narrative.

Usage: python scripts/_produce_term_evidence_digest_v1_20260702.py --strong H6531 [--out PATH]
"""
import sqlite3, os, sys, argparse, collections
DB=os.path.join('database','bible_research.db'); PROV='lexical-model-2026'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--strong',required=True); ap.add_argument('--out',default='')
    a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    strong=a.strong
    # all new-model lexical rows for the term's verses (the term + its passage co-terms)
    rows=cur.execute("""
      SELECT v.passage_id pid, (SELECT ref FROM passage WHERE id=v.passage_id) pref,
             v.book_id, v.chapter, v.verse_num, wvr.reference ref, wvr.term_id tid, wvr.target_word tw,
             mt.cluster_code cc, vl.ve_label, vl.value, vl.to_span
      FROM ve_lexical vl JOIN verse_context vc ON vl.verse_context_id=vc.id
      JOIN wa_verse_records wvr ON vc.verse_record_id=wvr.id JOIN verse v ON wvr.verse_id=v.id
      LEFT JOIN mti_terms mt ON wvr.mti_term_id=mt.id
      WHERE vl.source_provenance=? AND vl.delete_flagged=0
        AND v.passage_id IN (SELECT DISTINCT v2.passage_id FROM wa_verse_records w2 JOIN verse v2 ON w2.verse_id=v2.id
                             WHERE w2.term_id LIKE ?||'%' AND COALESCE(w2.delete_flagged,0)=0)
      ORDER BY v.book_id, v.chapter, v.verse_num, wvr.id, vl.ve_nr""", (PROV, strong)).fetchall()
    if not rows:
        print('no new-model lexical for the term/passages. (Has the lexical been written?)'); return
    # organise: passage -> verse -> term -> {label:value}
    D=collections.OrderedDict()
    for r in rows:
        D.setdefault((r['pid'],r['pref']),collections.OrderedDict()).setdefault(r['ref'],collections.OrderedDict()) \
         .setdefault((r['tid'],r['tw'],r['cc']),collections.OrderedDict())[r['ve_label']]=r['value']
    nverse=len({r['ref'] for r in rows}); npass=len({r['pid'] for r in rows}); nterm=len({(r['ref'],r['tid']) for r in rows})
    out=[]
    out.append('# EVIDENCE DIGEST — term %s (synthesis input)'%strong)
    out.append('scope: %d passages, %d verses, %d term-in-verse records | lens: what does it say about the inner being'%(npass,nverse,nterm))
    out.append('(collation is mechanical + scales to any N; the narrative is regenerated from THIS digest, never patched)\n')
    for (pid,pref),verses in D.items():
        out.append('## passage %s'%pref)
        for ref,terms in verses.items():
            out.append(' %s'%ref)
            for (tid,tw,cc),items in terms.items():
                core={k:items[k] for k in items if k not in ('sense','type')}
                is_focus = tid.startswith(strong)
                mark=' <TERM>' if is_focus else ''
                out.append('   %-9s "%s" [%s]%s  %s'%(tid,tw,cc or '-',mark,
                    '  '.join('%s=%s'%(k,v) for k,v in core.items()) or '(sense/type only)'))
        out.append('')
    text='\n'.join(out)
    if a.out:
        open(a.out,'w',encoding='utf-8').write(text); print('digest written:',a.out,'(%d verses)'%nverse)
    else:
        print(text)

if __name__=='__main__': main()
