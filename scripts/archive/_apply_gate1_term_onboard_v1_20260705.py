#!/usr/bin/env python
"""
*** RETIRED 2026-07-12 (researcher direction). DO NOT USE. ***
This tool hand-writes mti_terms, bypassing the integrated `audit_word` method. Term and
verse additions MUST go through audit_word only — see wa-term-add-update-AUTHORITATIVE-
pipeline-v1 (2026-07-12 amendment). Use _run_gate1_onboard_batch_v1 (audit_word path)
instead. Runtime-guarded off; kept only for provenance.

_apply_gate1_term_onboard_v1_20260705.py — onboard Gate-1-recovered inner-being terms into mti_terms.

These content-strongs surfaced from the verse_span_index span-orphan scan (Genesis+Exodus+Leviticus)
but were NEVER registered as terms (absent from mti_terms, or delete-only). Registering them here means
they are captured for EVERY book going forward — the durable fix that closes the gate-1 gap at source.

Idempotent: skips a strong already present as a live (non-delete) mti_terms row.
Read-only unless --live.
"""
import argparse, os, sqlite3, datetime

# strong -> cluster_code (assignment reviewed against cluster short_names)
ASSIGN = {
 'H0157':'M05',  # ahev LOVE
 'H0079':'M34',  # avaq wrestle (struggle/perseverance)
 'H5319':'M34',  # naphtulim wrestlings
 'H1350':'M38',  # gaal redeem (salvation)
 'H3467':'M38',  # yasha save
 'H2670':'M38',  # chophshi free/liberty
 'H5087':'M21',  # nadar vow
 'H5088':'M21',  # neder vow
 'H7307':'M47',  # ruach spirit (constitution seat)
 'H7911':'M41',  # shakhach forget (remembrance-neg)
 'H5382':'M41',  # nashah forget
 'H5358':'M02',  # naqam avenge (anger/retribution)
 'H5678':'M02',  # evrah fury
 'H0014':'M29',  # avah be willing (desire)
 'H6973':'M06',  # quts loathe (hate)
 'H0833':'M39',  # ashar call-blessed (blessing)
 'H3905':'M27',  # lachats oppress (evil/harm)
 'H3906':'M27',  # lachats oppression
 'H3238':'M27',  # yanah oppress
 'H7810':'M27',  # shochad bribe (corruption)
 'H2449':'M15',  # chakham be wise
 'H7309':'M33',  # revachah relief/respite (peace)
 'H7891':'M22',  # shir sing (praise)
 'H0034':'M24',  # evyon needy (weakness/affliction)
 'H1800':'M24',  # dal poor
 'H3490':'M24',  # yatom orphan
 'H0490':'M24',  # almanah widow
}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live',action='store_true')
    ap.add_argument('--db',default=os.path.join('database','bible_research.db'))
    ap.add_argument('--i-know-this-is-retired',action='store_true',
                    help=argparse.SUPPRESS)
    a=ap.parse_args()
    # RETIRED 2026-07-12 (researcher direction): this script hand-writes mti_terms,
    # bypassing the integrated audit_word method. Term/verse additions MUST go through
    # audit_word only (see wa-term-add-update-AUTHORITATIVE-pipeline-v1, 2026-07-12
    # amendment). Use _run_gate1_onboard_batch_v1 (audit_word path) instead.
    if not a.__dict__.get('i_know_this_is_retired'):
        import sys
        sys.exit("RETIRED: this tool bypasses audit_word. Onboard terms via "
                 "_run_gate1_onboard_batch_v1 (audit_word). See "
                 "wa-term-add-update-AUTHORITATIVE-pipeline-v1 (2026-07-12).")
    conn=sqlite3.connect(a.db); conn.row_factory=sqlite3.Row; c=conn.cursor()
    now=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    ins=skip=0
    for s,cl in ASSIGN.items():
        live=c.execute("SELECT COUNT(*) n FROM mti_terms WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0 AND COALESCE(status,'') NOT IN ('delete','candidate_delete','excluded')",(s,)).fetchone()['n']
        if live: print(f"  skip {s} (already live)"); skip+=1; continue
        lx=c.execute("SELECT transliteration,gloss,language FROM lexicon WHERE strong=?",(s,)).fetchone()
        tl=lx['transliteration'] if lx else None; gl=lx['gloss'] if lx else None; lang=lx['language'] if lx else 'Hebrew'
        print(f"  INSERT {s} {tl or '':<14} -> {cl}  {gl}")
        if a.live:
            c.execute("""INSERT INTO mti_terms
              (strongs_number,transliteration,gloss,language,status,cluster_code,vc_status,md_version,
               anchor_note,extraction_date,last_changed,strongs_reconciled,delete_flagged)
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
              (s,tl,gl,lang,'extracted',cl,'not_done',1,
               'Gate-1 recovery 2026-07-05: span-orphan inner-being term, not previously registered',
               now,now,1,0))
        ins+=1
    if a.live: conn.commit(); print(f"\nLIVE: {ins} inserted, {skip} skipped.")
    else: print(f"\nDRY-RUN: would insert {ins}, skip {skip}. Re-run with --live.")
    conn.close()

if __name__=='__main__': main()
