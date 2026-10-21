"""_assess_cluster_profiles.py — READ-ONLY. Per-cluster L1 profile correlated to the co-occurrence matrix:
verses · cross-cluster% (angle 1) · S3 multi-same-cluster · S4 qualifier-verses (angle 2) · top qualifiers
reaching the cluster. Pairs with the cross-cluster matrix to explain each cluster's exposure. NO DB writes.

Usage:  python scripts/_assess_cluster_profiles.py --out <file>.md
"""
import argparse, os, sqlite3, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"])
            for r in c.execute("SELECT cluster_code, short_name FROM cluster")}
    clus, t2info = {}, {}
    for r in c.execute("SELECT id, cluster_code, transliteration FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 "
                       "AND cluster_code IS NOT NULL AND cluster_code NOT IN ('FLAG')"):
        if r["cluster_code"] == "T2":
            t2info[r["id"]] = r["transliteration"] or str(r["id"])
        else:
            clus[r["id"]] = r["cluster_code"]

    ref_cl = defaultdict(lambda: defaultdict(int))   # ref -> cluster -> #distinct terms
    ref_t2 = defaultdict(set)                          # ref -> set of T2 ids
    for r in c.execute("SELECT reference, mti_term_id FROM wa_verse_records "
                       "WHERE COALESCE(delete_flagged,0)=0 AND reference IS NOT NULL AND mti_term_id IS NOT NULL"):
        mid = r["mti_term_id"]; ref = r["reference"]
        if mid in clus:
            ref_cl[ref][clus[mid]] += 1
        elif mid in t2info:
            ref_t2[ref].add(mid)

    verses = defaultdict(int); s5 = defaultdict(int); s3 = defaultdict(int); s4 = defaultdict(int)
    qreach = defaultdict(lambda: defaultdict(int))    # cluster -> t2id -> count
    for ref, cc_counts in ref_cl.items():
        ncl = len(cc_counts); t2s = ref_t2.get(ref, set())
        for cc, n in cc_counts.items():
            verses[cc] += 1
            if ncl >= 2: s5[cc] += 1
            if n >= 2: s3[cc] += 1
            if t2s:
                s4[cc] += 1
                for t in t2s:
                    qreach[cc][t] += 1

    codes = sorted(verses, key=lambda x: (int("".join(ch for ch in x[1:] if ch.isdigit()) or 0), x))
    L = ["# Per-cluster L1 profile — qualifier + scenario (roll-up angles 2 & 4)", ""]
    L.append("> READ-ONLY (`scripts/_assess_cluster_profiles.py`). Correlates to the co-occurrence matrix "
             "(angle 1). **S5** = cross-cluster verses · **S3** = verses with ≥2 of the cluster's own terms · "
             "**S4** = verses where a T2 qualifier co-occurs. No DB writes.")
    L.append("")
    L.append("| Cluster | verses | S5 cross % | S3 multi-same % | S4 qualifier % | top qualifiers (verses) |")
    L.append("|---|---|---|---|---|---|")
    for cc in codes:
        v = verses[cc]
        tq = sorted(qreach[cc].items(), key=lambda x: -x[1])[:4]
        tqs = ", ".join(f"{t2info.get(t,t)} {n}" for t, n in tq)
        L.append(f"| {cc} ({name.get(cc,cc)}) | {v} | {100*s5[cc]/v:.0f}% | {100*s3[cc]/v:.0f}% | "
                 f"{100*s4[cc]/v:.0f}% | {tqs} |")
    L.append("")
    # qualifier reach overall: top T2 by #clusters reached
    t2_clusters = defaultdict(set)
    for cc, d in qreach.items():
        for t in d:
            t2_clusters[t].add(cc)
    L.append("## Top qualifiers by cluster-reach (angle 2)")
    L.append(""); L.append("| Qualifier (T2) | clusters reached | total qualifier-verses |")
    L.append("|---|---|---|")
    tot_qv = defaultdict(int)
    for cc, d in qreach.items():
        for t, n in d.items():
            tot_qv[t] += n
    for t in sorted(t2_clusters, key=lambda x: (-len(t2_clusters[x]), -tot_qv[x]))[:20]:
        L.append(f"| {t2info.get(t,t)} | {len(t2_clusters[t])} | {tot_qv[t]} |")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(codes)} clusters profiled; wrote {a.out}")


if __name__ == "__main__":
    main()
