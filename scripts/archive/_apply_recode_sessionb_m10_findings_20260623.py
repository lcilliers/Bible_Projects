"""
Recode mis-migrated session_b CLUSTER-level findings off M10 to their correct
home clusters (registry-home basis). Per researcher direction 2026-06-23 (§6 of
wa-m10-family-logical-units-framework).

Basis: each finding is registry-scoped (reg:N in source_legacy_ref). Its correct
home = that registry's dominant live M-cluster (mti_terms.cluster_code, excluding
the T2/FLAG reference buckets). Only unambiguous cases are recoded; the rest are
left on M10 and reported for researcher decision.

Read-only by default. Pass --live to apply (snapshots the DB first).
"""
import sqlite3, os, shutil, sys

DB = os.path.join('database', 'bible_research.db')

# finding_id -> (target_cluster, registry_word, note)
RECODE = {
    129:  ('M31', 'faith',     'reg 59 faith -> M31 (dominant term-owner; Faith/Belief/Unbelief)'),
    821:  ('M24', 'contrition','reg 30 contrition -> M24 (all 6 terms M24; Weakness/Vulnerability/Suffering)'),
    840:  ('M24', 'contrition','reg 30 contrition -> M24'),
    1772: ('M24', 'contrition','reg 30 contrition -> M24'),
    1450: ('M05', 'mercy',     'reg 111 mercy -> M05 (dominant 8; Love/Compassion/Kindness)'),
    2229: ('M44', 'covenant',  'reg 34 covenant -> M44 (dominant non-T2; Relational Disposition)'),
    2230: ('M44', 'covenant',  'reg 34 covenant -> M44'),
    2351: ('M44', 'covenant',  'reg 34 covenant -> M44'),
    2371: ('M44', 'covenant',  'reg 34 covenant -> M44'),
}

# left on M10 deliberately — no clean home; researcher to decide
FLAGGED = {
    167:  'reg 206 vulnerability: terms owned T2(11)/M15(1) -> no clean M-home; candidate M24 (name match) or M07 (shame)',
    1098: 'reg 67 goodness: 3-way tie M04/M05/M39 -> unclear',
    1129: 'reg 67 goodness: 3-way tie M04/M05/M39 -> unclear',
}

def main():
    live = '--live' in sys.argv
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row

    print('=== PLANNED RECODES (off M10) ===')
    for fid, (tgt, word, note) in RECODE.items():
        row = conn.execute('SELECT id, cluster_code FROM finding WHERE id=? AND delete_flagged=0', (fid,)).fetchone()
        if not row:
            print(f'  #{fid}: NOT FOUND (skip)'); continue
        cur = row['cluster_code']
        print(f'  #{fid}: {cur} -> {tgt}   [{note}]' + ('' if cur == 'M10' else f'  (WARN current={cur})'))

    print('\n=== LEFT ON M10 (flagged for researcher) ===')
    for fid, note in FLAGGED.items():
        print(f'  #{fid}: {note}')

    if not live:
        print('\n(dry-run — pass --live to apply)')
        return

    # snapshot
    snap = os.path.join('backups', 'bible_research_pre-recode-sessionb-m10_20260623.db')
    os.makedirs('backups', exist_ok=True)
    shutil.copy2(DB, snap)
    print(f'\nSnapshot: {snap}')

    n = 0
    for fid, (tgt, word, note) in RECODE.items():
        cur = conn.execute('UPDATE finding SET cluster_code=?, last_updated_date=strftime("%Y-%m-%dT%H:%M:%SZ","now") '
                           'WHERE id=? AND delete_flagged=0', (tgt, fid))
        n += cur.rowcount
    conn.commit()
    print(f'Recoded {n} findings off M10.')

    # verify
    rem = conn.execute("SELECT count(*) FROM finding WHERE level='CLUSTER' AND delete_flagged=0 AND cluster_code='M10'").fetchone()[0]
    print(f"M10 CLUSTER-level findings remaining: {rem} (expect 3 flagged: 167,1098,1129)")
    for fid, (tgt, *_ ) in RECODE.items():
        cc = conn.execute('SELECT cluster_code FROM finding WHERE id=?', (fid,)).fetchone()[0]
        assert cc == tgt, f'#{fid} -> {cc} != {tgt}'
    print('Verification OK.')

if __name__ == '__main__':
    main()
