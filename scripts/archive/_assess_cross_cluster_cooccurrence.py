"""_assess_cross_cluster_cooccurrence.py — READ-ONLY. The cross-cluster co-occurrence matrix: which
characteristic clusters share verses (a reference holding active terms from both), and how heavily. This is
the connective-tissue view for the L1-sweep roll-up. NO DB writes.

A "verse" = a reference. Cluster Ci is present in a reference if any active wa_verse_records row there has a
term with cluster_code = Ci. Two clusters co-occur in a reference if both are present. T2/FLAG excluded.

Usage:  python scripts/_assess_cross_cluster_cooccurrence.py --out <file>.md
"""
import argparse, os, sqlite3, sys
from collections import defaultdict
from itertools import combinations
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=50)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()

    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"])
            for r in c.execute("SELECT cluster_code, short_name FROM cluster")}
    clus = {r["id"]: r["cluster_code"] for r in
            c.execute("SELECT id, cluster_code FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 "
                      "AND cluster_code IS NOT NULL AND cluster_code NOT IN ('T2','FLAG')")}

    # reference -> set of clusters present
    ref_clusters = defaultdict(set)
    for r in c.execute("SELECT reference, mti_term_id FROM wa_verse_records "
                       "WHERE COALESCE(delete_flagged,0)=0 AND reference IS NOT NULL AND mti_term_id IS NOT NULL"):
        cc = clus.get(r["mti_term_id"])
        if cc:
            ref_clusters[r["reference"]].add(cc)

    per_cluster_total = defaultdict(int)        # references containing cluster
    per_cluster_cross = defaultdict(int)        # references where cluster shares with >=1 other
    partners = defaultdict(lambda: defaultdict(int))   # cluster -> partner -> shared refs
    pair = defaultdict(int)                      # frozenset(Ci,Cj) -> shared refs
    n_cross_refs = 0
    for ref, cs in ref_clusters.items():
        for cc in cs:
            per_cluster_total[cc] += 1
        if len(cs) >= 2:
            n_cross_refs += 1
            for cc in cs:
                per_cluster_cross[cc] += 1
            for ci, cj in combinations(sorted(cs), 2):
                pair[(ci, cj)] += 1
                partners[ci][cj] += 1
                partners[cj][ci] += 1

    total_refs = len(ref_clusters)
    codes = sorted(per_cluster_total, key=lambda x: (x[0], int("".join(ch for ch in x[1:] if ch.isdigit()) or 0), x))

    L = ["# Cross-cluster co-occurrence matrix (L1-sweep roll-up · angle 1)", ""]
    L.append("> READ-ONLY (`scripts/_assess_cross_cluster_cooccurrence.py`). A verse (reference) co-occurs "
             "two clusters when it holds active terms from both. T2/FLAG excluded. No DB writes.")
    L.append("")
    L.append(f"**{total_refs} characteristic verses · {n_cross_refs} ({100*n_cross_refs/total_refs:.0f}%) "
             f"are cross-cluster** (hold ≥2 clusters). This is the connective tissue across the 46 clusters.")
    L.append("")
    L.append("## A · Per-cluster cross-cluster exposure")
    L.append("")
    L.append("| Cluster | verses | cross-cluster | % | clusters touched | top partners (shared verses) |")
    L.append("|---|---|---|---|---|---|")
    for cc in codes:
        tot = per_cluster_total[cc]; cr = per_cluster_cross[cc]
        tp = sorted(partners[cc].items(), key=lambda x: -x[1])[:4]
        tps = ", ".join(f"{name.get(p,p)} {n}" for p, n in tp)
        L.append(f"| {cc} ({name.get(cc,cc)}) | {tot} | {cr} | {100*cr/tot:.0f}% | {len(partners[cc])} | {tps} |")
    L.append("")
    L.append(f"## B · Strongest cluster links (top {a.top} pairs by shared verses)")
    L.append("")
    L.append("| Cluster A | Cluster B | shared | % of A | % of B |")
    L.append("|---|---|---|---|---|")
    for (ci, cj), n in sorted(pair.items(), key=lambda x: -x[1])[:a.top]:
        L.append(f"| {ci} ({name.get(ci,ci)}) | {cj} ({name.get(cj,cj)}) | {n} | "
                 f"{100*n/per_cluster_total[ci]:.0f}% | {100*n/per_cluster_total[cj]:.0f}% |")
    L.append("")

    # full matrix → CSV
    csv = a.out.rsplit(".", 1)[0] + "-matrix.csv"
    with open(csv, "w", encoding="utf-8") as f:
        f.write("cluster," + ",".join(codes) + "\n")
        for ci in codes:
            row = [str(pair.get((min(ci, cj), max(ci, cj)), 0)) if ci != cj else str(per_cluster_total[ci])
                   for cj in codes]
            f.write(f"{ci}," + ",".join(row) + "\n")
    L.append(f"_Full 46×46 matrix (diagonal = cluster's own verse count): `{os.path.basename(csv)}`._")

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{total_refs} char verses; {n_cross_refs} cross-cluster ({100*n_cross_refs/total_refs:.0f}%); "
          f"wrote {a.out} + matrix csv")


if __name__ == "__main__":
    main()
