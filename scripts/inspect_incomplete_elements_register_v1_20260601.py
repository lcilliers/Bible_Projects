"""Incomplete-elements register per cluster (read-only).

Three streams: (a) new terms to cluster (FLAG-classification cluster assignments),
(b) unallocated pointers (step-b logic), (c) unresolved boundaries
(BOUNDARY_DECISION_PENDING, cluster named in description). Annotated by cluster
status so differential-pass need (in-progress) vs fold-into-full (not started) is clear.

Output: research/investigations/incomplete-elements-register-20260601.md
"""
import json
import os
import re
import sqlite3
from collections import defaultdict, Counter

DB = "database/bible_research.db"
JSONF = "Workflow/Clusters/wa-flag-cluster-classification-v1_0-20260601.json"
OUT = "research/investigations/incomplete-elements-register-20260601.md"
FLAG_CODES = ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER")
LINKED_STATUSES = ("routed_cluster", "set_aside_non_evidenced", "superseded", "folded", "resolved_sd", "routed_sd")


def toks(cl):
    return {t.strip() for t in (cl or "").split(",") if t.strip()}


def main():
    c = sqlite3.connect(DB, timeout=20); c.row_factory = sqlite3.Row
    status = {r["cluster_code"]: r["status"] for r in c.execute("SELECT cluster_code, status FROM cluster")}

    # (a) new terms per cluster (from the classification cluster-dispositions)
    new_terms = defaultdict(list)
    with open(JSONF, encoding="utf-8") as f:
        for r in json.load(f)["classifications"]:
            if r["disposition"] == "cluster" and r["target_clusters"]:
                new_terms[r["target_clusters"][0]].append(r["strongs"])

    # (b) unallocated pointers per cluster (step-b logic)
    cat = {r["finding_id"] for r in c.execute("SELECT DISTINCT finding_id FROM wa_finding_catalogue_links WHERE COALESCE(delete_flagged,0)=0")}
    cited = {r["cited_sd_pointer_id"] for r in c.execute("SELECT DISTINCT cited_sd_pointer_id FROM wa_prose_section_citations WHERE cited_sd_pointer_id IS NOT NULL")}
    pf = defaultdict(int); pfl = defaultdict(int)
    for r in c.execute("SELECT id, cluster_link cl, status, session_c_chapter scc, related_finding_id rfi FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0 AND cluster_link IS NOT NULL"):
        if (r["id"] in cat) or (r["status"] in LINKED_STATUSES) or r["scc"] or (r["rfi"] is not None):
            continue
        for cl in toks(r["cl"]):
            pf[cl] += 1
    ph = ",".join("?" * len(FLAG_CODES))
    for r in c.execute(f"SELECT id, cluster_link cl, COALESCE(resolved,0) res FROM wa_session_research_flags WHERE flag_code IN ({ph}) AND cluster_link IS NOT NULL", FLAG_CODES):
        if r["res"] or (r["id"] in cited):
            continue
        for cl in toks(r["cl"]):
            pfl[cl] += 1

    # (c) unresolved boundaries per cluster
    bound = defaultdict(int)
    for r in c.execute("SELECT description d FROM wa_session_research_flags WHERE flag_code='BOUNDARY_DECISION_PENDING' AND COALESCE(resolved,0)=0"):
        m = re.match(r"\s*(M\d+[a-z]?)\b", r["d"] or "")
        bound[m.group(1) if m else "(unparsed)"] += 1

    allc = sorted(set(new_terms) | set(pf) | set(pfl) | set(bound), key=lambda x: (x not in status, x))

    L = ["# Incomplete-elements register (post-FLAG-triage)", "",
         "**Generated:** 2026-06-01 (read-only). Per cluster: (a) new terms to cluster (FLAG classification), (b) unallocated pointers (findings+flags), (c) unresolved boundaries. Status flags whether a **differential pass** is needed (Analysis - In Progress) or it folds into a not-yet-started full run.", "",
         "| cluster | status | (a) new terms | (b) ptr findings | (b) ptr flags | (c) boundaries | differential? |",
         "|---|---|--:|--:|--:|--:|---|"]
    tot = Counter()
    for cl in allc:
        st = status.get(cl, "(no cluster row)")
        a, bf, bfl, cc = len(new_terms.get(cl, [])), pf.get(cl, 0), pfl.get(cl, 0), bound.get(cl, 0)
        tot["a"] += a; tot["bf"] += bf; tot["bfl"] += bfl; tot["c"] += cc
        diff = "DIFFERENTIAL" if st == "Analysis - In Progress" else ("fold into full" if st == "Not started" else st)
        L.append(f"| {cl} | {st} | {a} | {bf} | {bfl} | {cc} | {diff} |")
    L.append(f"| **TOTAL** | | {tot['a']} | {tot['bf']} | {tot['bfl']} | {tot['c']} | |")

    L += ["", "## New terms per cluster (a) — the FLAG-assigned strongs", ""]
    for cl in sorted(new_terms):
        L.append(f"- **{cl}** ({status.get(cl,'?')}): {', '.join(sorted(new_terms[cl]))}")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"clusters with any incomplete element: {len(allc)}")
    print(f"totals: new_terms={tot['a']} ptr_findings={tot['bf']} ptr_flags={tot['bfl']} boundaries={tot['c']}")
    print("wrote:", OUT)
    c.close()


if __name__ == "__main__":
    main()
