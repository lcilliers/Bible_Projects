"""_assess_shared_forms.py — READ-ONLY. Shared-form / homonym index: transliterations whose terms are
assigned across >=2 characteristic clusters. Explains part of the co-occurrence fabric — the same lexical
form (homonym or shared root) doing work in several clusters. NO DB writes.

Usage:  python scripts/_assess_shared_forms.py --out <file>.md
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
    form = defaultdict(list)   # translit -> [(strongs, cluster)]
    for r in c.execute("SELECT strongs_number, transliteration, cluster_code FROM mti_terms "
                       "WHERE COALESCE(delete_flagged,0)=0 AND cluster_code NOT IN ('T2','FLAG') "
                       "AND cluster_code IS NOT NULL AND transliteration IS NOT NULL"):
        form[r["transliteration"]].append((r["strongs_number"], r["cluster_code"]))

    multi = {f: v for f, v in form.items() if len({cc for _s, cc in v}) >= 2}
    L = ["# Shared-form / homonym index (roll-up angle 3)", ""]
    L.append("> READ-ONLY (`scripts/_assess_shared_forms.py`). Transliterated forms whose terms are assigned "
             "across ≥2 characteristic clusters — homonyms or shared roots that span the cluster boundary. "
             "Part of why the co-occurrence fabric (angle 1) is so dense. No DB writes.")
    L.append("")
    L.append(f"**{len(multi)} forms span ≥2 clusters** (of {len(form)} distinct forms).")
    L.append("")
    L.append("| Form | clusters | Strong's (by cluster) |")
    L.append("|---|---|---|")
    for f in sorted(multi, key=lambda x: (-len({cc for _s, cc in multi[x]}), x)):
        v = multi[f]
        ccs = sorted({cc for _s, cc in v}, key=lambda x: (int("".join(ch for ch in x[1:] if ch.isdigit()) or 0), x))
        detail = "; ".join(f"{s}→{cc}" for s, cc in sorted(v, key=lambda x: x[1]))
        L.append(f"| {f} | {', '.join(name.get(cc,cc) for cc in ccs)} | {detail} |")
    L.append("")
    # cluster-pair counts from shared forms
    pairc = defaultdict(int)
    from itertools import combinations
    for f, v in multi.items():
        ccs = sorted({cc for _s, cc in v})
        for ci, cj in combinations(ccs, 2):
            pairc[(ci, cj)] += 1
    L.append("## Cluster pairs most linked by shared forms")
    L.append(""); L.append("| Cluster A | Cluster B | shared forms |"); L.append("|---|---|---|")
    for (ci, cj), n in sorted(pairc.items(), key=lambda x: -x[1])[:25]:
        L.append(f"| {name.get(ci,ci)} | {name.get(cj,cj)} | {n} |")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(multi)} multi-cluster forms; wrote {a.out}")


if __name__ == "__main__":
    main()
