"""_assess_keyword_corpus_report.py — READ-ONLY. Directional assessment of the corpus-wide keyword
allocation (reads the P1 map CSV). Answers: how big is the vocabulary, how is it distributed, how much is
generic vs discriminating, how much residual noise, and do clusters get distinct signatures? NO DB writes.

Usage:  python scripts/_assess_keyword_corpus_report.py --map research/investigations/<file>.csv --out <file>.md
"""
import argparse, csv, os, sys
from collections import defaultdict, Counter
sys.stdout.reconfigure(encoding="utf-8")

# low-content / generic glue words that survive the P1 filters — a residual-noise gauge
GLUE = set("""make made making cause caused act acts become became give given giving put set come came go went
goes take took taken bring brought do done keep kept turn turned thing things one great good away upon let
hold held bear born fall fell stand stood rise call called place way time day man people land hand""".split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
    kw_freq = Counter()                 # keyword -> # terms carrying it
    kw_clusters = defaultdict(set)      # keyword -> set of clusters
    cl_kw = defaultdict(Counter)        # cluster -> keyword -> count
    cl_name = {}
    n_terms = 0; n_zero = 0
    with open(a.map, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            n_terms += 1
            cc = row["cluster"]; cl_name[cc] = row["cluster_name"]
            kws = [k.strip() for k in row["keywords"].split(";") if k.strip()]
            if not kws: n_zero += 1
            for k in kws:
                kw_freq[k] += 1; kw_clusters[k].add(cc); cl_kw[cc][k] += 1

    vocab = len(kw_freq); total = sum(kw_freq.values())
    hapax = sum(1 for k, n in kw_freq.items() if n == 1)
    # genericness histogram
    spread = Counter()
    for k, cs in kw_clusters.items():
        n = len(cs)
        b = "1" if n == 1 else "2-3" if n <= 3 else "4-9" if n <= 9 else "10-19" if n <= 19 else "20+"
        spread[b] += 1
    glue_in_top = [k for k, _ in kw_freq.most_common(50) if k in GLUE]

    L = ["# Keyword corpus — directional assessment", ""]
    L.append("> READ-ONLY (`scripts/_assess_keyword_corpus_report.py`) over the preliminary P1 map. A "
             "general read on vocabulary size, distribution, generic-vs-discriminating, residual noise, and "
             "per-cluster signature strength. No DB writes.")
    L.append("")
    L.append("## Scale")
    L.append(f"- **{n_terms} terms · {total} allocations · {vocab} distinct keywords** "
             f"({total/n_terms:.1f} avg/term).")
    L.append(f"- **Hapax: {hapax} ({100*hapax/vocab:.0f}%)** of the vocabulary appears on only one term "
             f"(the long tail).")
    L.append(f"- Terms with **zero** keywords: {n_zero}.")
    L.append("")
    L.append("## Genericness — in how many clusters does each keyword appear?")
    L.append(""); L.append("| spread | # keywords | reading |"); L.append("|---|---|---|")
    rd = {"1": "**cluster-signature** (discriminating)", "2-3": "near-signature",
          "4-9": "shared theme", "10-19": "generic", "20+": "**near-universal** (low value)"}
    for b in ("1", "2-3", "4-9", "10-19", "20+"):
        L.append(f"| {b} clusters | {spread.get(b,0)} | {rd[b]} |")
    L.append("")
    L.append("## Most frequent keywords (the backbone vocabulary)")
    L.append(""); L.append("| keyword | # terms | # clusters |"); L.append("|---|---|---|")
    for k, n in kw_freq.most_common(35):
        flag = " ⚠glue" if k in GLUE else ""
        L.append(f"| {k}{flag} | {n} | {len(kw_clusters[k])} |")
    L.append("")
    L.append(f"**Residual noise gauge:** {len(glue_in_top)} of the top-50 keywords are low-content glue "
             f"words ({', '.join(glue_in_top) or 'none'}).")
    L.append("")
    L.append("## Per-cluster signature strength")
    L.append(""); L.append("| Cluster | distinct kw | unique-to-cluster | % unique | top signature keywords |")
    L.append("|---|---|---|---|---|")
    codes = sorted(cl_kw, key=lambda x: (int("".join(ch for ch in x[1:] if ch.isdigit()) or 0), x))
    for cc in codes:
        kws = cl_kw[cc]
        uniq = [k for k in kws if len(kw_clusters[k]) == 1]
        sig = sorted(uniq, key=lambda k: -kws[k])[:6]
        L.append(f"| {cc} ({cl_name[cc]}) | {len(kws)} | {len(uniq)} | {100*len(uniq)/len(kws):.0f}% | "
                 f"{', '.join(sig) or '—'} |")
    L.append("")
    # directional verdict
    pct_sig = 100 * spread.get("1", 0) / vocab
    pct_generic = 100 * (spread.get("10-19", 0) + spread.get("20+", 0)) / vocab
    L.append("## Directional verdict")
    L.append(f"- **{pct_sig:.0f}%** of the vocabulary is cluster-signature (1 cluster); only "
             f"**{pct_generic:.0f}%** is generic (10+ clusters) → the keyword layer **does discriminate**.")
    L.append(f"- Residual glue in the top band ({len(glue_in_top)}/50) is the main quality drag → the "
             "source-clean would lift signal, but the layer is **directionally usable now**.")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{n_terms} terms, {vocab} distinct kw, hapax {100*hapax/vocab:.0f}%, "
          f"signature {pct_sig:.0f}%, generic {pct_generic:.0f}%, glue-in-top {len(glue_in_top)}; wrote {a.out}")


if __name__ == "__main__":
    main()
