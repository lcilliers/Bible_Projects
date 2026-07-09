"""
QUARANTINE valence (researcher 2026-06-26): valence is an interpretive moral
overlay, not verse evidence (does not track verse grammar; 99% read-API). It was
a clustering driver previously, so it is RETAINED (not deleted) but moved out of
the active verse-grounded lexical and clearly labelled interpretive, so it never
reads as evidence again.

Mechanism: snapshot active valence rows -> ve_lexical_valence_quarantine_20260626;
set delete_flagged=1 (excluded from all active lexical reads, which filter
delete_flagged=0) + a QUARANTINE note. Fully recoverable from the snapshot or by
clearing the flag.

  --dry-run : counts only
  --live    : backup DB + snapshot + quarantine
"""
import sqlite3, os, argparse, shutil

DB=os.path.join('database','bible_research.db')
BACKUP=os.path.join('backups','bible_research_pre-valence-quarantine_20260626.db')
SNAP='ve_lexical_valence_quarantine_20260626'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live',action='store_true'); ap.add_argument('--dry-run',action='store_true')
    a=ap.parse_args(); live=a.live and not a.dry_run
    if live: print('backing up DB ->',BACKUP); shutil.copy2(DB,BACKUP)
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    n=c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_label='valence' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    byprov=c.execute("SELECT source_provenance, COUNT(*) k FROM ve_lexical WHERE ve_label='valence' AND COALESCE(delete_flagged,0)=0 GROUP BY source_provenance").fetchall()
    print(f'active valence rows to quarantine: {n}')
    for r in byprov: print(f'   {r["k"]:>7}  {r["source_provenance"]}')
    if not live: print('dry-run (no write).'); c.close(); return
    cur=c.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {SNAP}")
    cur.execute(f"CREATE TABLE {SNAP} AS SELECT * FROM ve_lexical WHERE ve_label='valence' AND COALESCE(delete_flagged,0)=0")
    cur.execute("""UPDATE ve_lexical
        SET delete_flagged=1,
            notes=COALESCE(notes,'')||' | QUARANTINED 2026-06-26: interpretive moral overlay, not verse evidence (verse-bounded rule); retained not error'
        WHERE ve_label='valence' AND COALESCE(delete_flagged,0)=0""")
    c.commit()
    left=c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_label='valence' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f'LIVE: snapshot {SNAP} ({n} rows); quarantined {n}. active valence remaining: {left}')
    c.close()

if __name__=='__main__': main()
