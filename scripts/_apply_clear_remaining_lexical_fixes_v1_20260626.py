"""
Clear the 4 remaining lexical fixes under the verse-bounded rule (researcher
2026-06-26, "verse is king"). All reversible: one DB backup + per-fix snapshot.

  1. origin       -> QUARANTINE. Single value 'received-from-outside', 100% per-term
                    constant, no verse basis (interpretive stamp). delete_flag + note.
  2. object-type  -> REMAP. Merge overlapping {thing, abstract, thing/abstract} into
                    one honest 'impersonal' (object is in the verse, not person/God/being).
                    Keep person/God/spiritual-being/situation/threat. Relabel (no delete).
  3. divine-involv-> RULE (b). The grounded resolved rows assert a ROLE the verse doesn't
                    clearly support; demote value -> 'present' (mention is verse-true),
                    original role preserved in notes + snapshot. UNRESOLVED untouched.
  4. faculty seat -> REVERSE. faculty-verse-inferred-seat (proximity binding, not verse-
                    stated) soft-deleted; seats keep faculty only where the verse names it.

  --dry-run : counts only        --live : backup + snapshot + write
"""
import sqlite3, os, argparse, shutil

DB=os.path.join('database','bible_research.db')
BACKUP=os.path.join('backups','bible_research_pre-remaining-fixes_20260626.db')

def snap(cur, name, where, params=()):
    cur.execute(f"DROP TABLE IF EXISTS {name}")
    cur.execute(f"CREATE TABLE {name} AS SELECT * FROM ve_lexical WHERE {where}", params)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live',action='store_true'); ap.add_argument('--dry-run',action='store_true')
    a=ap.parse_args(); live=a.live and not a.dry_run
    if live: print('backing up DB ->',BACKUP); shutil.copy2(DB,BACKUP)
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()

    n_origin=c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_label='origin' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    n_objtype=c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_label='object-type' AND value IN ('thing','abstract','thing/abstract') AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    n_divrole=c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_label='divine-involvement' AND value!='UNRESOLVED' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    n_seat=c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_label='faculty' AND source_provenance='faculty-verse-inferred-seat-v1-20260626' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f'1. origin to QUARANTINE:                 {n_origin}')
    print(f'2. object-type to MERGE -> impersonal:   {n_objtype}')
    print(f'3. divine-involvement roles -> present:  {n_divrole}')
    print(f'4. faculty seat-inferred to REVERSE:     {n_seat}')
    if not live: print('dry-run (no write).'); c.close(); return

    # 1. origin quarantine
    snap(cur,'ve_lexical_origin_quarantine_20260626',"ve_label='origin' AND COALESCE(delete_flagged,0)=0")
    cur.execute("UPDATE ve_lexical SET delete_flagged=1, notes=COALESCE(notes,'')||' | QUARANTINED 2026-06-26: single-value non-grounded interpretive stamp (verse-bounded rule)' WHERE ve_label='origin' AND COALESCE(delete_flagged,0)=0")
    c.commit()
    # 2. object-type merge
    snap(cur,'ve_lexical_objtype_premap_20260626',"ve_label='object-type' AND value IN ('thing','abstract','thing/abstract') AND COALESCE(delete_flagged,0)=0")
    cur.execute("""UPDATE ve_lexical SET value='impersonal',
        notes=COALESCE(notes,'')||' | remapped 2026-06-26 {'||value||'}->impersonal (taxonomy dedupe)',
        source_provenance=source_provenance||'+remap20260626'
        WHERE ve_label='object-type' AND value IN ('thing','abstract','thing/abstract') AND COALESCE(delete_flagged,0)=0""")
    c.commit()
    # 3. divine-involvement rule (b): demote role -> present
    snap(cur,'ve_lexical_divinv_roles_premap_20260626',"ve_label='divine-involvement' AND value!='UNRESOLVED' AND COALESCE(delete_flagged,0)=0")
    cur.execute("""UPDATE ve_lexical SET
        notes=COALESCE(notes,'')||' | rule-b 2026-06-26: role '||value||' demoted to mention (role not clearly verse-supported)',
        value='present', source_provenance=source_provenance||'+ruleb20260626'
        WHERE ve_label='divine-involvement' AND value!='UNRESOLVED' AND COALESCE(delete_flagged,0)=0""")
    c.commit()
    # 4. faculty seat-inferred reverse
    snap(cur,'ve_lexical_faculty_seat_reverse_20260626',"ve_label='faculty' AND source_provenance='faculty-verse-inferred-seat-v1-20260626' AND COALESCE(delete_flagged,0)=0")
    cur.execute("UPDATE ve_lexical SET delete_flagged=1, notes=COALESCE(notes,'')||' | reversed 2026-06-26 rule-b: seat faculty was proximity-inferred, not verse-stated' WHERE ve_label='faculty' AND source_provenance='faculty-verse-inferred-seat-v1-20260626' AND COALESCE(delete_flagged,0)=0")
    c.commit()

    print('LIVE done. Verify:')
    q1="SELECT COUNT(*) FROM ve_lexical WHERE ve_label='origin' AND COALESCE(delete_flagged,0)=0"
    q2="SELECT value, COUNT(*) n FROM ve_lexical WHERE ve_label='object-type' AND COALESCE(delete_flagged,0)=0 GROUP BY value ORDER BY n DESC"
    q3="SELECT value, COUNT(*) n FROM ve_lexical WHERE ve_label='divine-involvement' AND COALESCE(delete_flagged,0)=0 GROUP BY value ORDER BY n DESC"
    q4="SELECT COUNT(*) FROM ve_lexical WHERE ve_label='faculty' AND COALESCE(delete_flagged,0)=0"
    q5="SELECT COUNT(*) FROM ve_lexical WHERE ve_label='faculty' AND source_provenance='faculty-verse-inferred-seat-v1-20260626' AND COALESCE(delete_flagged,0)=0"
    print('  origin active:', c.execute(q1).fetchone()[0])
    print('  object-type values:', [dict(r) for r in c.execute(q2).fetchall()])
    print('  divine-involvement values:', [dict(r) for r in c.execute(q3).fetchall()])
    print('  faculty active:', c.execute(q4).fetchone()[0], '| seat-inferred remaining:', c.execute(q5).fetchone()[0])
    c.close()

if __name__=='__main__': main()
