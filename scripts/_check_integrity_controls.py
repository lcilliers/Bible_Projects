"""_check_integrity_controls.py (2026-06-28) — DB integrity anchor for the term-orphan build (READ-ONLY).

Two modes:
  snapshot : capture control totals + invariant counts -> a json under outputs/integrity/
  compare  : diff two snapshots -> show EXACTLY what changed (expected deltas vs contamination)

Usage:
  python scripts/_check_integrity_controls.py --snapshot --label pre-perek
  python scripts/_check_integrity_controls.py --snapshot --label post-perek
  python scripts/_check_integrity_controls.py --compare pre-perek post-perek

Control totals = row counts per key table/segment (the "anchors").
Invariants = counts that MUST be 0 (FK orphans, duplicate owners, dangling links). Any non-zero = integrity breach.
"""
import argparse, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB=os.path.join("database","bible_research.db")
OUT=os.path.join("outputs","integrity"); os.makedirs(OUT, exist_ok=True)

TOTALS={
 "mti_active":"SELECT COUNT(*) FROM mti_terms WHERE status NOT IN ('delete','candidate_delete','excluded') OR status IS NULL",
 "mti_all":"SELECT COUNT(*) FROM mti_terms",
 "inv_owner":"SELECT COUNT(*) FROM wa_term_inventory WHERE term_owner_type='OWNER' AND (delete_flagged=0 OR delete_flagged IS NULL)",
 "inv_xref":"SELECT COUNT(*) FROM wa_term_inventory WHERE term_owner_type='XREF' AND (delete_flagged=0 OR delete_flagged IS NULL)",
 "verse_records_active":"SELECT COUNT(*) FROM wa_verse_records WHERE delete_flagged=0 OR delete_flagged IS NULL",
 "verse_context_active":"SELECT COUNT(*) FROM verse_context WHERE delete_flagged=0 OR delete_flagged IS NULL",
 "ve_lexical":"SELECT COUNT(*) FROM ve_lexical WHERE delete_flagged=0 OR delete_flagged IS NULL",
 "verse_canon":"SELECT COUNT(*) FROM verse",
 "verse_span_index":"SELECT COUNT(*) FROM verse_span_index",
 "verse_coverage(segregated)":"SELECT COUNT(*) FROM verse_coverage_morphology",
 "word_registry":"SELECT COUNT(*) FROM word_registry",
}
# per-cluster member counts (so we see exactly which cluster grew)
CLUSTER="SELECT cluster_code, COUNT(*) FROM mti_terms WHERE cluster_code IS NOT NULL GROUP BY cluster_code"
# INVARIANTS — must all be 0
INV={
 "dup_owner_strong":"SELECT COUNT(*) FROM (SELECT strongs_number FROM wa_term_inventory WHERE term_owner_type='OWNER' AND (delete_flagged=0 OR delete_flagged IS NULL) GROUP BY strongs_number HAVING COUNT(*)>1)",
 "vr_orphan_term_inv":"SELECT COUNT(*) FROM wa_verse_records vr LEFT JOIN wa_term_inventory ti ON vr.term_inv_id=ti.id WHERE vr.term_inv_id IS NOT NULL AND ti.id IS NULL",
 "vr_orphan_book":"SELECT COUNT(*) FROM wa_verse_records vr LEFT JOIN books b ON vr.book_id=b.id WHERE vr.book_id IS NOT NULL AND b.id IS NULL",
 "vc_orphan_mti":"SELECT COUNT(*) FROM verse_context vc LEFT JOIN mti_terms m ON vc.mti_term_id=m.id WHERE vc.mti_term_id IS NOT NULL AND m.id IS NULL",
 "vc_orphan_vrec":"SELECT COUNT(*) FROM verse_context vc LEFT JOIN wa_verse_records vr ON vc.verse_record_id=vr.id WHERE vc.verse_record_id IS NOT NULL AND vr.id IS NULL",
 "velex_orphan_vc":"SELECT COUNT(*) FROM ve_lexical x LEFT JOIN verse_context vc ON x.verse_context_id=vc.id WHERE vc.id IS NULL",
}

def capture():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    snap={"totals":{}, "clusters":{}, "invariants":{}}
    for k,q in TOTALS.items():
        try: snap["totals"][k]=c.execute(q).fetchone()[0]
        except Exception as e: snap["totals"][k]=f"ERR {e}"
    for r in c.execute(CLUSTER): snap["clusters"][r[0]]=r[1]
    for k,q in INV.items():
        try: snap["invariants"][k]=c.execute(q).fetchone()[0]
        except Exception as e: snap["invariants"][k]=f"ERR {e}"
    return snap

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--snapshot",action="store_true"); ap.add_argument("--label")
    ap.add_argument("--compare",nargs=2,metavar=("PRE","POST"))
    a=ap.parse_args()
    if a.snapshot:
        snap=capture(); p=os.path.join(OUT,f"snap-{a.label}.json")
        json.dump(snap,open(p,"w"),indent=2)
        bad={k:v for k,v in snap["invariants"].items() if v}
        print(f"snapshot '{a.label}' -> {p}")
        print("  invariants:", "ALL CLEAN (0)" if not bad else f"⚠ BREACH {bad}")
    elif a.compare:
        pre=json.load(open(os.path.join(OUT,f"snap-{a.compare[0]}.json")))
        post=json.load(open(os.path.join(OUT,f"snap-{a.compare[1]}.json")))
        print(f"=== DELTA {a.compare[0]} -> {a.compare[1]} ===")
        print("TOTALS (changed only):")
        for k in pre["totals"]:
            d=post["totals"].get(k,0)-pre["totals"][k] if isinstance(pre["totals"][k],int) else "?"
            if d: print(f"   {k:<28} {pre['totals'][k]:>8} -> {post['totals'][k]:<8} ({'+' if isinstance(d,int) and d>0 else ''}{d})")
        print("CLUSTERS (changed only):")
        for k in set(list(pre["clusters"])+list(post["clusters"])):
            d=post["clusters"].get(k,0)-pre["clusters"].get(k,0)
            if d: print(f"   {k:<6} {pre['clusters'].get(k,0):>5} -> {post['clusters'].get(k,0):<5} ({'+' if d>0 else ''}{d})")
        print("INVARIANTS (post):")
        bad={k:v for k,v in post["invariants"].items() if v}
        print("   ALL CLEAN (0)" if not bad else f"   ⚠ BREACH {bad}")
    else: ap.print_help()

if __name__=="__main__": main()
