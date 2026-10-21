"""_assess_mti_duplicate_terms.py — READ-ONLY. Re-surfaces OT-DBR-009 (mti_terms duplication) from the
read-dedup angle. Groups mti_terms by BASE Strong's (suffix letter stripped), then within each base computes
pairwise verse-set overlap to find DUPLICATE rows — terms whose active verse set is (near-)contained in a
sibling's. Duplicate rows inflate (term,sense) group counts, the read-dedup %, and the l2 finding count, and
some carry a WRONG sense label (chesed H2617B = 'a reproach, shame' over 169 lovingkindness verses, a 100%
subset of H2617A). Distinguishes genuine sub-entries (disjoint verses) from duplicates (subset verses) by
OVERLAP, never by suffix. NO DB writes.

Usage:  python scripts/_assess_mti_duplicate_terms.py --out <file>.md [--overlap 0.9]
"""
import argparse, os, re, sqlite3, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
SUFFIX = re.compile(r"^([HG]\d+)[A-Z]*$")


def base(sn):
    m = SUFFIX.match(sn or "")
    return m.group(1) if m else sn


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--overlap", type=float, default=0.9,
                    help="fraction of the smaller term's verses inside the larger to call it a duplicate")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()

    # all active verse_context rows per mti_term, with reference set
    refs = defaultdict(set)
    meta = {}
    for r in c.execute("""SELECT vc.mti_term_id mid, vr.reference ref, m.strongs_number sn,
                                 m.transliteration tl, m.cluster_code cc
                          FROM verse_context vc
                          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                          JOIN mti_terms m ON m.id = vc.mti_term_id
                          WHERE COALESCE(vc.delete_flagged,0)=0"""):
        refs[r["mid"]].add(r["ref"])
        meta[r["mid"]] = (r["sn"], r["tl"], r["cc"])

    # sense label per term (T7.1 = q395), most common
    sense = {}
    for r in c.execute("""SELECT f.mti_term_id mid, f.finding_value v, COUNT(*) n
                          FROM finding f JOIN finding_question_link l ON l.finding_id=f.id
                          WHERE f.provenance='l2_mechanical' AND l.question_id=395
                          GROUP BY f.mti_term_id, f.finding_value"""):
        if r["mid"] not in sense:
            sense[r["mid"]] = (r["v"] or "")[:45]

    # group by base Strong's
    bygroup = defaultdict(list)
    for mid, (sn, tl, cc) in meta.items():
        bygroup[base(sn)].append(mid)

    dup_terms = set()           # mid flagged as a duplicate (subset of a larger sibling)
    dup_clusters = []           # (base, keeper, [dups]) for reporting
    for b, mids in bygroup.items():
        if len(mids) < 2:
            continue
        # sort largest verse-set first = canonical keeper candidate
        mids = sorted(mids, key=lambda m: -len(refs[m]))
        keeper = mids[0]
        local_dups = []
        for m in mids[1:]:
            sm = refs[m]
            if not sm:
                continue
            inside = len(sm & refs[keeper]) / len(sm)
            if inside >= a.overlap:
                local_dups.append((m, len(sm), round(inside, 2)))
                dup_terms.add(m)
        if local_dups:
            dup_clusters.append((b, keeper, local_dups))

    # quantify duplicated verse_contexts and findings on the duplicate terms
    dup_vc = sum(1 for r in c.execute(
        "SELECT vc.id, vc.mti_term_id m FROM verse_context vc WHERE COALESCE(vc.delete_flagged,0)=0")
        if r["m"] in dup_terms)
    dup_find = sum(1 for r in c.execute(
        "SELECT f.mti_term_id m FROM finding f WHERE f.provenance='l2_mechanical'")
        if r["m"] in dup_terms)
    tot_find = c.execute("SELECT COUNT(*) FROM finding WHERE provenance='l2_mechanical'").fetchone()[0]

    dup_clusters.sort(key=lambda x: -sum(d[1] for d in x[2]))
    L = ["# mti_terms duplicate-term assessment (OT-DBR-009, dedup angle)", ""]
    L.append("> READ-ONLY (`scripts/_assess_mti_duplicate_terms.py`). Groups mti_terms by base Strong's; "
             f"within each base, flags a sibling as a DUPLICATE when ≥{int(a.overlap*100)}% of its active "
             "verses are contained in the largest sibling. Genuine sub-entries (disjoint verses) are NOT "
             "flagged. No DB writes.")
    L.append("")
    L.append(f"**{len(dup_terms)} duplicate term rows** across **{len(dup_clusters)} base Strong's**.  "
             f"They carry **{dup_vc} duplicated active verse_context rows** and **{dup_find} of {tot_find} "
             f"l2_mechanical findings ({100*dup_find/tot_find:.0f}%)** — all redundant copies.")
    L.append("")
    L.append("## Duplicate clusters — ranked by duplicated verses")
    L.append("")
    L.append("| base | keeper (kept) | sense on keeper | duplicate rows (verses, %inside) |")
    L.append("|---|---|---|---|")
    for b, keeper, dups in dup_clusters[:60]:
        sn, tl, cc = meta[keeper]
        dd = ", ".join(f"{meta[m][0]} ({n}, {int(p*100)}%)" for m, n, p in dups)
        L.append(f"| {b} | {sn} {tl} ({cc}, {len(refs[keeper])}v) | {sense.get(keeper,'?')} | {dd} |")
    L.append("")
    L.append("## Wrong sense labels riding on duplicates (keeper vs duplicate sense)")
    L.append("")
    L.append("| base | keeper sense | duplicate | duplicate sense |")
    L.append("|---|---|---|---|")
    for b, keeper, dups in dup_clusters:
        ks = sense.get(keeper, "")
        for m, n, p in dups:
            ds = sense.get(m, "")
            if ds and ds != ks:
                L.append(f"| {b} | {ks} | {meta[m][0]} | {ds} |")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(dup_terms)} duplicate term rows / {len(dup_clusters)} bases; "
          f"{dup_vc} dup verse_context; {dup_find}/{tot_find} dup findings "
          f"({100*dup_find/tot_find:.0f}%); wrote {a.out}")


if __name__ == "__main__":
    main()
