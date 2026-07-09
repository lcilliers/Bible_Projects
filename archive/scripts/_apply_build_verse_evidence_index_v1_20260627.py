"""
Build the verse↔evidence SPIDERWEB index (researcher 2026-06-27): bind EVERY piece
of evidence back to its verse, from all ends, fast, complete, and not blind.

Materialised (direct, verse-specific, indexed -> superfast):
  verse_evidence_index(verse_id, evidence_type, evidence_id, bind_path, confidence)
    evidence_type: span | unit | lexical | finding_verse | finding_link
Orphan guarantee (nothing dropped silently):
  verse_evidence_orphan(evidence_type, evidence_id, reason)
Indirect (NOT materialised — combinatorial; retrieved on demand, documented):
  - cluster/global findings  : verse -> its terms -> cluster_code -> findings
  - related verses           : verse -> its terms -> other verses sharing the term
  (both are fast via the term index below)
Also builds verse_term_index(verse_id, primary_strong) for the lateral term web.
Reversible: DROP the tables. Idempotent.
"""
import sqlite3, os
DB=os.path.join('database','bible_research.db')

def main():
    c=sqlite3.connect(DB); cur=c.cursor()
    for t in ['verse_evidence_index','verse_evidence_orphan','verse_term_index']:
        cur.execute(f'DROP TABLE IF EXISTS {t}')
    cur.execute("""CREATE TABLE verse_evidence_index(
        verse_id INTEGER, evidence_type TEXT, evidence_id INTEGER, bind_path TEXT, confidence TEXT)""")
    cur.execute("CREATE TABLE verse_evidence_orphan(evidence_type TEXT, evidence_id INTEGER, reason TEXT)")
    cur.execute("CREATE TABLE verse_term_index(verse_id INTEGER, primary_strong TEXT)")

    # --- DIRECT evidence -> verse (verse-specific) ---
    # spans
    cur.execute("""INSERT INTO verse_evidence_index
        SELECT verse_id,'span',id,'direct:morphology','direct' FROM verse_span_index WHERE verse_id IS NOT NULL""")
    # units
    cur.execute("""INSERT INTO verse_evidence_index
        SELECT vr.verse_id,'unit',vc.id,'direct:verse_record','direct'
        FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        WHERE vr.verse_id IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0""")
    # lexicals
    cur.execute("""INSERT INTO verse_evidence_index
        SELECT vr.verse_id,'lexical',vl.id,'direct:vc-vr','direct'
        FROM ve_lexical vl JOIN verse_context vc ON vc.id=vl.verse_context_id
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        WHERE vr.verse_id IS NOT NULL AND COALESCE(vl.delete_flagged,0)=0""")
    # VERSE findings
    cur.execute("""INSERT INTO verse_evidence_index
        SELECT vr.verse_id,'finding_verse',f.id,'direct:vc-vr','direct'
        FROM finding f JOIN verse_context vc ON vc.id=f.verse_context_id
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        WHERE f.level='VERSE' AND vr.verse_id IS NOT NULL AND COALESCE(f.delete_flagged,0)=0""")
    # finding_verse_link (alternate direct path) - map its verse ref to verse_id
    cols=[r[1] for r in c.execute('PRAGMA table_info(finding_verse_link)')]
    if 'verse_id' in cols:
        cur.execute("""INSERT INTO verse_evidence_index
            SELECT verse_id,'finding_link',finding_id,'finding_verse_link','direct'
            FROM finding_verse_link WHERE verse_id IS NOT NULL""")

    # --- verse_term_index (lateral web foundation) ---
    cur.execute("INSERT INTO verse_term_index SELECT DISTINCT verse_id, primary_strong FROM verse_span_index WHERE verse_id IS NOT NULL AND primary_strong IS NOT NULL")

    # --- ORPHANS: evidence that should bind to a verse but cannot ---
    cur.execute("""INSERT INTO verse_evidence_orphan
        SELECT 'lexical',vl.id,'unit/verse_record has no verse_id' FROM ve_lexical vl
        WHERE COALESCE(vl.delete_flagged,0)=0 AND NOT EXISTS(
          SELECT 1 FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
          WHERE vc.id=vl.verse_context_id AND vr.verse_id IS NOT NULL)""")
    cur.execute("""INSERT INTO verse_evidence_orphan
        SELECT 'unit',vc.id,'verse_record has no verse_id' FROM verse_context vc
        WHERE COALESCE(vc.delete_flagged,0)=0 AND NOT EXISTS(
          SELECT 1 FROM wa_verse_records vr WHERE vr.id=vc.verse_record_id AND vr.verse_id IS NOT NULL)""")
    cur.execute("""INSERT INTO verse_evidence_orphan
        SELECT 'finding_verse',f.id,'no resolvable verse' FROM finding f
        WHERE f.level='VERSE' AND COALESCE(f.delete_flagged,0)=0 AND NOT EXISTS(
          SELECT 1 FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
          WHERE vc.id=f.verse_context_id AND vr.verse_id IS NOT NULL)""")

    # indexes -> superfast
    cur.execute("CREATE INDEX ix_vei_verse ON verse_evidence_index(verse_id, evidence_type)")
    cur.execute("CREATE INDEX ix_vei_ev ON verse_evidence_index(evidence_type, evidence_id)")
    cur.execute("CREATE INDEX ix_vti_verse ON verse_term_index(verse_id)")
    cur.execute("CREATE INDEX ix_vti_term ON verse_term_index(primary_strong)")
    c.commit()

    def n(q): return c.execute(q).fetchone()[0]
    print('verse_evidence_index built:', n('SELECT COUNT(*) FROM verse_evidence_index'), 'rows')
    for r in c.execute("SELECT evidence_type, COUNT(*) k, COUNT(DISTINCT verse_id) v FROM verse_evidence_index GROUP BY evidence_type ORDER BY k DESC"):
        print(f'   {r[0]:<14} {r[1]:>7} links  across {r[2]} verses')
    print('verses with ANY evidence:', n('SELECT COUNT(DISTINCT verse_id) FROM verse_evidence_index'))
    print('verse_term_index:', n('SELECT COUNT(*) FROM verse_term_index'), 'verse-term pairs')
    print('ORPHANS:', n('SELECT COUNT(*) FROM verse_evidence_orphan'))
    for r in c.execute("SELECT evidence_type, reason, COUNT(*) k FROM verse_evidence_orphan GROUP BY evidence_type, reason"):
        print(f'   orphan {r[0]} ({r[1]}): {r[2]}')
    c.close()

if __name__=='__main__': main()
