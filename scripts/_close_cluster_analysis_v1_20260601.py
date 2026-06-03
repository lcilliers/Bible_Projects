"""Closure routine (F14 skeleton): reset cluster status ONLY on a clean audit.

Uses the auditor (audit_cluster_v1_20260601.audit_cluster) as the predicate.
If the cluster has ZERO GATE failures, flip cluster.status to 'Analysis Complete'.
Otherwise refuse and print the GATE failures. Read-only unless --apply.

  python scripts/_close_cluster_analysis_v1_20260601.py --cluster M10c [--apply]
"""
import argparse, importlib.util, sqlite3, os
DB="database/bible_research.db"
spec=importlib.util.spec_from_file_location("auditor","scripts/audit_cluster_v1_20260601.py")
aud=importlib.util.module_from_spec(spec); spec.loader.exec_module(aud)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--cluster",required=True); ap.add_argument("--apply",action="store_true"); a=ap.parse_args()
    c=aud.conn()
    verdict,R=aud.audit_cluster(c,a.cluster)
    gate_fail=[r for r in R if r["sev"]=="GATE" and r["status"]=="FAIL"]
    print(f"{a.cluster}: verdict={verdict} | GATE fails={len(gate_fail)}")
    for r in gate_fail:
        print(f"  FAIL {r['id']} {r['name']} ({r['count']})")
    if gate_fail:
        print("REFUSE: cluster not clean; status unchanged."); c.close(); return
    cur=a_status=c.execute("SELECT status FROM cluster WHERE cluster_code=?",(a.cluster,)).fetchone()[0]
    print(f"  current status: {a_status}")
    if not a.apply:
        print("DRY-RUN: would flip status -> 'Analysis Complete'"); c.close(); return
    c.execute("UPDATE cluster SET status='Analysis Complete', last_updated_date=datetime('now') WHERE cluster_code=?",(a.cluster,)); c.commit()
    print("APPLIED: status -> 'Analysis Complete'"); c.close()
if __name__=="__main__": main()
