"""
_apply_fix_8_mti_mismatches_percase_20260701.py

Per-case resolution of the 8 verse_context/verse_record mti mismatches (OT-DBR-009 symptoms).
Each mismatched verse_context has a sibling; handled by case:

 DELETE (soft) the wrong verse_context + its ve_lexical — wrong term is a phantom (not in verse)
   or a same-group duplicate of an active correct sibling:
     9312  Isa 53:9  (H8267 sheqer phantom; mirmah H4820 is the real term, active sibling 9183)
     9317  Job 31:1  (H8267 sheqer phantom; berith H1285 is the real term, active sibling 8613)
     63732 Isa 2:22  (H2803H dup; correct H2803J sibling 31715 active)
     63733 Isa 29:17 (H2803H dup; correct H2803J sibling 31717 active)

 RE-GROUND (fix mti to the correct sub-entry) — chashab IS in the verse; correct sibling is
   soft-deleted/empty and the active lexical sits on the wrong sub-label; no collision (diff group):
     31638 Psa 40:17 -> 3334 (H2803I)
     31639 Psa 41:7  -> 3334 (H2803I)
     31640 Psa 52:2  -> 3334 (H2803I)

 HOLD (no action, flagged) — covenant (H1285) IS in the verse but has no own verse_record;
   deleting would lose coverage. Needs a covenant-onboarding decision:
     8612  2Ch 21:7

Safe: backs up; dry-run default; verifies. Soft-deletes reversible.
Usage: python scripts/_apply_fix_8_mti_mismatches_percase_20260701.py [--live]
"""
import sqlite3, sys, os, shutil
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
DELETES=[9312,9317,63732,63733]
REGROUND=[(31638,3334),(31639,3334),(31640,3334)]
HOLD=[8612]

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    # collision check for regrounds
    for vcid,newmti in REGROUND:
        r=cur.execute("SELECT verse_record_id,group_id,cluster_subgroup_id FROM verse_context WHERE id=?",(vcid,)).fetchone()
        clash=cur.execute("""SELECT id FROM verse_context WHERE verse_record_id=? AND mti_term_id=?
            AND IFNULL(group_id,-1)=IFNULL(?,-1) AND IFNULL(cluster_subgroup_id,-1)=IFNULL(?,-1) AND id<>?""",
            (r['verse_record_id'],newmti,r['group_id'],r['cluster_subgroup_id'],vcid)).fetchone()
        print('reground vc=%d -> mti %d : %s'%(vcid,newmti,'COLLISION!' if clash else 'ok'))
    ndel_lex=cur.execute("SELECT COUNT(*) FROM ve_lexical WHERE verse_context_id IN (%s) AND delete_flagged=0"%','.join('?'*len(DELETES)),DELETES).fetchone()[0]
    print('deletes: %d verse_contexts + %d ve_lexical rows soft-deleted'%(len(DELETES),ndel_lex))
    print('regrounds: %d ; hold (no action): %s'%(len(REGROUND),HOLD))
    if not LIVE:
        print('\nDRY-RUN. Re-run with --live to apply.'); return
    os.makedirs('backups',exist_ok=True)
    bak=os.path.join('backups',f'bible_research.pre-mismatch8.{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.db')
    shutil.copy2(DB,bak); print('\nBackup:',bak)
    for vcid in DELETES:
        cur.execute("UPDATE verse_context SET delete_flagged=1 WHERE id=?",(vcid,))
        cur.execute("UPDATE ve_lexical SET delete_flagged=1 WHERE verse_context_id=?",(vcid,))
    for vcid,newmti in REGROUND:
        cur.execute("UPDATE verse_context SET mti_term_id=? WHERE id=?",(newmti,vcid))
    conn.commit()
    remaining=cur.execute("""SELECT COUNT(DISTINCT vc.id) FROM ve_lexical vl JOIN verse_context vc ON vl.verse_context_id=vc.id
       JOIN wa_verse_records w ON vc.verse_record_id=w.id
       WHERE vl.delete_flagged=0 AND COALESCE(vc.delete_flagged,0)=0 AND vc.mti_term_id IS NOT w.mti_term_id""").fetchone()[0]
    print('done. remaining active mismatches: %d (expected 1 = the held 2Ch 21:7)'%remaining)

if __name__=='__main__': main()
