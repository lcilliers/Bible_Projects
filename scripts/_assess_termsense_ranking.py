"""_assess_termsense_ranking.py — READ-ONLY. Reasonability check on the read-dedup: ranks every (term, sense)
group by verse count and flags groups ABOVE a threshold (default 100) as SUSPECT — a single mechanical sense
applying to >100 verses likely hides real sense variation (e.g. ya.da "to know" = cognitive / relational /
experiential collapsed into one Qal branch), so reading-once is unsafe for those. NO DB writes.

Usage:  python scripts/_assess_termsense_ranking.py --threshold 100 --out <file>.md
"""
import argparse, os, sqlite3, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--threshold", type=int, default=100)
    ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    tl = {r["id"]: r["transliteration"] for r in c.execute("SELECT id, transliteration FROM mti_terms")}
    cc = {r["id"]: r["cluster_code"] for r in c.execute("SELECT id, cluster_code FROM mti_terms")}

    grp = Counter(); senses = {}
    for r in c.execute("SELECT f.mti_term_id mid, f.finding_value v, COUNT(DISTINCT f.verse_context_id) n "
                       "FROM finding f JOIN finding_question_link l ON l.finding_id=f.id "
                       "WHERE f.provenance='l2_mechanical' AND f.level='VERSE' AND l.question_id=395 "
                       "GROUP BY f.mti_term_id, f.finding_value"):
        key = (r["mid"], (r["v"] or "")[:50])
        grp[key] += r["n"]; senses[key] = (r["v"] or "")[:55]
    total = sum(grp.values())

    buckets = [("1", 1, 1), ("2-10", 2, 10), ("11-50", 11, 50), ("51-100", 51, 100),
               ("101-200", 101, 200), ("201+", 201, 10**9)]
    bgroups = Counter(); bverses = Counter()
    for k, n in grp.items():
        for label, lo, hi in buckets:
            if lo <= n <= hi:
                bgroups[label] += 1; bverses[label] += n; break

    L = ["# Read-dedup reasonability — (term, sense) group sizes", ""]
    L.append(f"> READ-ONLY (`scripts/_assess_termsense_ranking.py`). Ranks (term, sense) groups; flags "
             f"**>{a.threshold}** as SUSPECT (one mechanical sense over that many verses likely hides sense "
             "variation → reading-once unsafe). No DB writes.")
    L.append("")
    L.append(f"**{len(grp)} (term, sense) groups · {total} term-in-verses.**")
    L.append("")
    L.append("## Size distribution")
    L.append(""); L.append("| group size | groups | verses | % verses |"); L.append("|---|---|---|---|")
    for label, lo, hi in buckets:
        L.append(f"| {label} | {bgroups[label]} | {bverses[label]} | {100*bverses[label]/total:.0f}% |")
    susp_g = sum(bgroups[l] for l in ("101-200", "201+"))
    susp_v = sum(bverses[l] for l in ("101-200", "201+"))
    L.append("")
    L.append(f"**Suspect (> {a.threshold}): {susp_g} groups covering {susp_v} verses "
             f"({100*susp_v/total:.0f}% of all term-in-verses).** Acceptable (≤{a.threshold}): "
             f"{len(grp)-susp_g} groups, {total-susp_v} verses ({100*(total-susp_v)/total:.0f}%).")
    L.append("")
    L.append(f"## SUSPECT groups (> {a.threshold} verses) — ranked")
    L.append(""); L.append("| term | cluster | verses | sense |"); L.append("|---|---|---|---|")
    for k, n in grp.most_common():
        if n <= a.threshold:
            break
        mid = k[0]
        L.append(f"| {tl.get(mid, mid)} | {cc.get(mid,'?')} | {n} | {senses[k]} |")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(grp)} groups; suspect (>{a.threshold}) {susp_g} groups / {susp_v} verses "
          f"({100*susp_v/total:.0f}%); wrote {a.out}")


if __name__ == "__main__":
    main()
