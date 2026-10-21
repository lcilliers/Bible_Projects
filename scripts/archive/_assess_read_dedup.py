"""_assess_read_dedup.py — READ-ONLY. Estimates how much the (expensive) read layer would DUPLICATE across
verses, by signature on the existing mechanical findings. Many read fields depend only on (term, sense) — not
the individual verse — so those can be read ONCE per signature and applied to all member verses. Reports the
dedup ratio at three signature levels. NO DB writes.

Signatures (coarse → fine):
  S1 term            — fields that depend only on the term (e.g. base faculty / origin / nature)
  S2 term + sense    — fields that depend on the term's applied sense (the shade)
  S3 term + sense + co-occurring-cluster-set — fields that also depend on the relational context

Usage:  python scripts/_assess_read_dedup.py --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
MRE = re.compile(r"\((M\w+)\)")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"]) for r in c.execute("SELECT cluster_code, short_name FROM cluster")}
    tl = {r["id"]: r["transliteration"] for r in c.execute("SELECT id, transliteration FROM mti_terms")}

    sense, cooc, mid_of = {}, {}, {}
    for r in c.execute("SELECT f.verse_context_id vc, f.mti_term_id mid, l.question_id q, f.finding_value v "
                       "FROM finding f JOIN finding_question_link l ON l.finding_id=f.id "
                       "WHERE f.provenance='l2_mechanical' AND f.level='VERSE' AND l.question_id IN (395,369)"):
        mid_of[r["vc"]] = r["mid"]
        if r["q"] == 395: sense[r["vc"]] = r["v"]
        else: cooc[r["vc"]] = r["v"]

    vcs = list(mid_of)
    S1, S2, S3 = Counter(), Counter(), Counter()
    for vc in vcs:
        mid = mid_of[vc]; sv = (sense.get(vc) or "")[:60]
        ccs = frozenset(MRE.findall(cooc.get(vc) or ""))
        S1[mid] += 1
        S2[(mid, sv)] += 1
        S3[(mid, sv, ccs)] += 1
    n = len(vcs)

    def stat(sig):
        d = len(sig); dup = n - d
        return d, 100 * dup / n if n else 0

    d1, p1 = stat(S1); d2, p2 = stat(S2); d3, p3 = stat(S3)
    L = ["# Read-layer dedup estimate (from mechanical findings)", ""]
    L.append("> READ-ONLY (`scripts/_assess_read_dedup.py`). How much the read would duplicate: distinct "
             "signatures vs total term-in-verses. Read once per signature → apply to all members.")
    L.append("")
    L.append(f"**{n} term-in-verses total.**")
    L.append("")
    L.append("| signature | distinct | reads saved | dedup % | read-once cost |")
    L.append("|---|---|---|---|---|")
    L.append(f"| **S1 term only** | {d1} | {n-d1} | **{p1:.0f}%** | {d1} reads |")
    L.append(f"| **S2 term + sense** | {d2} | {n-d2} | **{p2:.0f}%** | {d2} reads |")
    L.append(f"| **S3 term + sense + co-occur-clusters** | {d3} | {n-d3} | **{p3:.0f}%** | {d3} reads |")
    L.append("")
    L.append("**Reading:** term/sense-invariant read fields (faculty · origin · base nature) → read once per "
             f"**S2 ({d2})**, applied to all {n} verses = **{p2:.0f}% saved**. Context fields "
             "(attributed-to-God · produces · response · direction) → S3-grained ({0}) or per-verse, but "
             "near-dups still cluster.".format(d3))
    L.append("")
    L.append("## Biggest duplicate groups (term + sense) — read once, applies to N verses")
    L.append(""); L.append("| term | verses | sample sense |"); L.append("|---|---|---|")
    for (mid, sv), cnt in S2.most_common(20):
        L.append(f"| {tl.get(mid, mid)} | {cnt} | {sv[:48]} |")
    L.append("")
    # how many verses sit in singleton signatures (genuinely unique → must read individually)
    sing2 = sum(1 for k, v in S2.items() if v == 1)
    sing3 = sum(1 for k, v in S3.items() if v == 1)
    L.append(f"_Singletons (must read individually): S2 = {sing2} ({100*sing2/n:.0f}% of verses unique by "
             f"term+sense); S3 = {sing3} ({100*sing3/n:.0f}%)._")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{n} term-verses; S1 {d1} ({p1:.0f}% dedup); S2 {d2} ({p2:.0f}%); S3 {d3} ({p3:.0f}%); wrote {a.out}")


if __name__ == "__main__":
    main()
