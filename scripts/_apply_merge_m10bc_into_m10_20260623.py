"""
Merge M10b + M10c into M10 (researcher decision 2026-06-23): the three-way split
was an artificial linear-partition; they are one sin operation. Collapse to a
single M10 cluster with a single 1-32 characteristic namespace.

- characteristic: M10b seq1-6 -> M10 seq23-28; M10c seq1-4 -> M10 seq29-32 (M10 1-22 unchanged)
- cluster_code M10b/M10c -> M10 in: mti_terms, finding, cluster_finding,
  cluster_observation, cluster_subgroup, wa_session_b_findings.cluster_link
- cluster rows M10b/M10c: retire (delete_flagged=1 + status note)
- subgroup_code strings (M10b-A ...) left as-is (unique, functional; cosmetic only)

Read-only by default; --live applies after a snapshot. Prints the old->new crosswalk.
"""
import sqlite3, os, shutil, sys

DB = os.path.join('database','bible_research.db')

def main():
    live = '--live' in sys.argv
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row

    # crosswalk from characteristic table (by id, seq order)
    chars = list(conn.execute(
        "SELECT id, cluster_code, char_seq, short_name FROM characteristic "
        "WHERE cluster_code IN ('M10b','M10c') ORDER BY cluster_code, char_seq"))
    plan = []  # (id, old_label, new_seq, name)
    for r in chars:
        old = f"{r['cluster_code']} #{r['char_seq']}"
        new_seq = (22 + r['char_seq']) if r['cluster_code'] == 'M10b' else (28 + r['char_seq'])
        plan.append((r['id'], old, new_seq, r['short_name']))

    print('=== CROSSWALK (old -> new global #, single M10 namespace) ===')
    for cid, old, new_seq, name in plan:
        print(f"  {old:9} -> M10 #{new_seq:<2}  (char id {cid})  {name}")

    print('\n=== cluster_code retags M10b/M10c -> M10 ===')
    for t, col in [('mti_terms','cluster_code'),('finding','cluster_code'),
                   ('cluster_finding','cluster_code'),('cluster_observation','cluster_code'),
                   ('cluster_subgroup','cluster_code'),('wa_session_b_findings','cluster_link')]:
        n = conn.execute(f"SELECT count(*) FROM \"{t}\" WHERE \"{col}\" IN ('M10b','M10c')").fetchone()[0]
        print(f"  {t}.{col}: {n}")
    print('  cluster: retire M10b, M10c rows (delete_flagged=1)')

    if not live:
        print('\n(dry-run — pass --live to apply)')
        return

    snap = os.path.join('backups','bible_research_pre-merge-m10bc_20260623.db')
    os.makedirs('backups', exist_ok=True); shutil.copy2(DB, snap)
    print(f'\nSnapshot: {snap}')

    cur = conn.cursor()
    # 1. characteristic re-seq + retag
    for cid, old, new_seq, name in plan:
        cur.execute("UPDATE characteristic SET cluster_code='M10', char_seq=?, "
                    "last_updated_date=strftime('%Y-%m-%dT%H:%M:%SZ','now') WHERE id=?", (new_seq, cid))
    # 2. retag cluster_code in dependent tables
    for t, col in [('mti_terms','cluster_code'),('finding','cluster_code'),
                   ('cluster_finding','cluster_code'),('cluster_observation','cluster_code'),
                   ('cluster_subgroup','cluster_code'),('wa_session_b_findings','cluster_link')]:
        cur.execute(f"UPDATE \"{t}\" SET \"{col}\"='M10' WHERE \"{col}\" IN ('M10b','M10c')")
    # 3. retire the cluster rows (cluster table has no delete_flagged; use status)
    cur.execute("UPDATE cluster SET status='Merged into M10 (2026-06-23)', "
                "last_updated_date=strftime('%Y-%m-%dT%H:%M:%SZ','now') "
                "WHERE cluster_code IN ('M10b','M10c')")
    conn.commit()
    print('Applied.')

    # 4. verify: no M10b/M10c left in any cluster_code/link column
    print('\n=== verification: residual M10b/M10c ===')
    resid = 0
    for t, col in [('cluster','cluster_code'),('mti_terms','cluster_code'),('finding','cluster_code'),
                   ('cluster_finding','cluster_code'),('cluster_observation','cluster_code'),
                   ('cluster_subgroup','cluster_code'),('characteristic','cluster_code'),
                   ('wa_session_b_findings','cluster_link')]:
        n = conn.execute(f"SELECT count(*) FROM \"{t}\" WHERE \"{col}\" IN ('M10b','M10c') AND "
                         f"(\"{col}\"!='M10')").fetchone()[0]
        # cluster table rows still hold code M10b/M10c but are delete_flagged - report separately
        if t == 'cluster':
            act = conn.execute("SELECT count(*) FROM cluster WHERE cluster_code IN ('M10b','M10c') AND status NOT LIKE 'Merged into M10%'").fetchone()[0]
            print(f"  cluster: {act} non-retired M10b/M10c rows (expect 0; retired rows retain code as provenance)")
            continue
        print(f"  {t}.{col}: {n} (expect 0)"); resid += n
    # characteristic namespace check
    seqs = [r[0] for r in conn.execute("SELECT char_seq FROM characteristic WHERE cluster_code='M10' AND delete_flagged=0 ORDER BY char_seq")]
    print(f"\n  M10 characteristic seqs now: {min(seqs)}..{max(seqs)} count={len(seqs)} unique={len(set(seqs))==len(seqs)}")
    print('  RESIDUAL TOTAL:', resid, '(0 = clean)')

if __name__ == '__main__':
    main()
