#!/usr/bin/env python
"""
_apply_reread_roles_from_velexical_v1_20260709.py

Backfill verse_span_index.role from the re-read ve_lexical (source of truth), for every
span touched by a given provenance. Fixes the gap where early re-read applies wrote
ve_lexical + process_marker but NOT the master role (§7A ledger row 2).

Role derivation (matches the apply / cycle §5-6):
  - a span with an active ve_lexical ve_nr=115 row (provenance) -> role = that value
    (characteristic | qualifier | standalone), role_source_ve_id = that row's id;
  - a span appearing as the OTHER end of a real span-id pair (resolution='span',
    from_span!=to_span) that has NO 115 row of its own -> role='qualifier' (captured qualifier).
  - role_provenance='read-2026', role_set_at=NOW.

Idempotent. Does NOT touch ve_lexical. Dry-run default; --live to write.
Usage:
  python scripts/_apply_reread_roles_from_velexical_v1_20260709.py --prov=reread-psalms-2026 --live
"""
import argparse, sqlite3, os
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db')
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--prov',default='reread-psalms-2026')
    ap.add_argument('--live',action='store_true')
    a=ap.parse_args()
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    prov=a.prov
    # 1. explicit roles: latest active 115 row per span
    role_of={}; srcid={}
    for r in c.execute("""SELECT verse_span_id sid, value, id FROM ve_lexical
                          WHERE ve_nr=115 AND delete_flagged=0 AND source_provenance=? """,(prov,)):
        role_of[r['sid']]=r['value']; srcid[r['sid']]=r['id']
    explicit=len(role_of)
    # 2. derived qualifiers: span-id pair endpoints not already roled
    for r in c.execute("""SELECT from_span, to_span FROM ve_lexical
                          WHERE delete_flagged=0 AND source_provenance=? AND resolution='span'
                            AND from_span IS NOT NULL AND to_span IS NOT NULL AND from_span<>to_span""",(prov,)):
        for ep in (r['from_span'], r['to_span']):
            if ep is not None and ep not in role_of:
                role_of[ep]='qualifier'
    derived=len(role_of)-explicit
    # tally + how many differ from current master
    cur=c.cursor(); changed=0; rc={}
    for sid,rl in role_of.items():
        row=cur.execute("SELECT role, role_provenance FROM verse_span_index WHERE id=?",(sid,)).fetchone()
        if not row: continue
        rc[rl]=rc.get(rl,0)+1
        if row['role']!=rl or row['role_provenance']!='read-2026': changed+=1
    print(f"prov={prov} | spans with explicit 115 role: {explicit} | derived qualifiers: {derived} | total: {len(role_of)}")
    print(f"role tally: {rc} | spans whose master role/provenance would change: {changed}")
    if not a.live:
        print("DRY-RUN. Re-run with --live to write."); return
    for sid,rl in role_of.items():
        cur.execute("""UPDATE verse_span_index SET role=?, role_provenance='read-2026', role_set_at=?, role_source_ve_id=?
                       WHERE id=?""",(rl,NOW,srcid.get(sid),sid))
    c.commit()
    print(f"written. {len(role_of)} spans set to read-2026 roles.")

if __name__=='__main__':
    main()
