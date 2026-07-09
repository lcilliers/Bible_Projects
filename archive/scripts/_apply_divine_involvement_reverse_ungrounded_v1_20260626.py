"""
Reverse out UNGROUNDED divine-involvement rows per the verse-bounded rule
(researcher 2026-06-26, rule a): a value with no basis in THE VERSE is an error,
even if true from context. Divine-involvement role asserted on a verse with NO
divine name in it = error -> soft-delete (reversible).

Conservative: a row is KEPT if the verse contains ANY divine name/title under a
GENEROUS set (incl. ambiguous kurios/pater/Jesus/Christ/Holy/adon) so we only
reverse the unambiguous errors. Rows grounded only by an ambiguous title survive
here and are left for the role-clarity pass (rule b). UNRESOLVED rows are untouched
(they assert no role). Only value != 'UNRESOLVED' rows are eligible for reversal.

  --dry-run : counts + sample, no write
  --live    : backup DB -> backups/, snapshot -> ve_lexical_divinv_pre_reverse_20260626, soft-delete
"""
import sqlite3, os, re, argparse, shutil
from collections import Counter

DB=os.path.join('database','bible_research.db')
BACKUP=os.path.join('backups','bible_research_pre-divinv-reverse_20260626.db')
SNAP='ve_lexical_divinv_pre_reverse_20260626'
# GENEROUS divine set (keep-if-present): OT names + NT theos/kurios/pater/Christ/Jesus/holy + adon
DIV={'H3068','H3069','H0430','H0410','H0433','H0136','H3050','H5945','H7706','H0113',
     'G2316','G2962','G3962','G5547','G2424','G0040'}

def canon(s):
    m=re.match(r'^([HG])(\d+)([A-Z]?)$',(s or '').strip().upper())
    return f'{m.group(1)}{int(m.group(2)):04d}' if m else None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live',action='store_true'); ap.add_argument('--dry-run',action='store_true')
    a=ap.parse_args(); live=a.live and not a.dry_run
    if live: print('backing up DB ->', BACKUP); shutil.copy2(DB, BACKUP)
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    div_verses=set()
    for r in c.execute('SELECT verse_id, strongs FROM verse_morphology WHERE strongs IS NOT NULL'):
        for tok in (r['strongs'] or '').split():
            if canon(tok) in DIV: div_verses.add(r['verse_id']); break
    rows=c.execute("""
      SELECT vl.id, vl.value val, vr.verse_id vid, vr.reference ref, vr.verse_text txt, m.transliteration tr
      FROM ve_lexical vl JOIN verse_context vc ON vc.id=vl.verse_context_id
      JOIN wa_verse_records vr ON vr.id=vc.verse_record_id JOIN mti_terms m ON m.id=vc.mti_term_id
      WHERE vl.ve_label='divine-involvement' AND COALESCE(vl.delete_flagged,0)=0
        AND vl.value!='UNRESOLVED' AND vr.verse_id IS NOT NULL""").fetchall()
    ungrounded=[r for r in rows if r['vid'] not in div_verses]
    print(f'resolved divine-involvement rows: {len(rows)}')
    print(f'UNGROUNDED (no divine name in verse, generous set) -> REVERSE: {len(ungrounded)}')
    print(f'  by value: {dict(Counter(r["val"] for r in ungrounded).most_common())}')
    print('  sample:')
    for r in ungrounded[:6]:
        print(f"    [{r['val']}] {r['ref']} ({r['tr']}): {(r['txt'] or '').strip().replace(chr(10),' ')[:90]}")
    if not live:
        print('dry-run (no write).'); c.close(); return
    ids=[r['id'] for r in ungrounded]
    cur=c.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {SNAP}")
    cur.execute(f"CREATE TABLE {SNAP} AS SELECT * FROM ve_lexical WHERE id IN (%s)"%','.join('?'*len(ids)) if ids else f"CREATE TABLE {SNAP} AS SELECT * FROM ve_lexical WHERE 0", ids)
    CH=900
    for i in range(0,len(ids),CH):
        ch=ids[i:i+CH]
        cur.execute("UPDATE ve_lexical SET delete_flagged=1, notes=COALESCE(notes,'')||' | reversed 2026-06-26: ungrounded (no divine name in verse) per verse-bounded rule' WHERE id IN (%s)"%','.join('?'*len(ch)), ch)
    c.commit()
    left=c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_label='divine-involvement' AND COALESCE(delete_flagged,0)=0 AND value!='UNRESOLVED'").fetchone()[0]
    print(f'LIVE: snapshot {SNAP} ({len(ids)} rows); soft-deleted {len(ids)}. resolved divine-involvement remaining: {left}')
    c.close()

if __name__=='__main__': main()
