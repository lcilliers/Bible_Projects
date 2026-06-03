"""Step (b): pointers routed to the in-progress clusters, not yet linked to a finding.

Read-only. For clusters with status 'Analysis - In Progress', find pointers whose
cluster_link includes that cluster (exact token match) and which are NOT yet
adopted/linked to a finding, and NOT already set aside.

"Linked to a finding already":
  - findings : wa_finding_catalogue_links (tier-question) OR status in
               (routed_cluster, set_aside_non_evidenced, superseded, folded)
               OR session_c_chapter OR related_finding_id
  - flags    : resolved=1 OR cited in wa_prose_section_citations.cited_sd_pointer_id

Output: research/investigations/inprogress-cluster-pointers-20260601.md
"""
import os
import sqlite3
from collections import defaultdict

DB = "database/bible_research.db"
OUT = "research/investigations/inprogress-cluster-pointers-20260601.md"
FLAG_CODES = ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER")
LINKED_STATUSES = ("routed_cluster", "set_aside_non_evidenced", "superseded", "folded", "resolved_sd", "routed_sd")


def tokens(cl):
    return {t.strip() for t in (cl or "").split(",") if t.strip()}


def main():
    c = sqlite3.connect(DB, timeout=20); c.row_factory = sqlite3.Row
    cur = c.cursor()

    inprog = [r["cluster_code"] for r in cur.execute("SELECT cluster_code FROM cluster WHERE status='Analysis - In Progress' ORDER BY cluster_code")]
    inprog_set = set(inprog)

    cat = {r["finding_id"] for r in cur.execute("SELECT DISTINCT finding_id FROM wa_finding_catalogue_links WHERE COALESCE(delete_flagged,0)=0")}
    cited = {r["cited_sd_pointer_id"] for r in cur.execute("SELECT DISTINCT cited_sd_pointer_id FROM wa_prose_section_citations WHERE cited_sd_pointer_id IS NOT NULL")}

    # findings allocated to an in-progress cluster
    f_alloc = defaultdict(list)   # cluster -> [(id, linked?, ...)]
    f_review = defaultdict(list)
    for r in cur.execute("SELECT id, finding_type ft, status, cluster_link cl, finding, session_c_chapter scc, related_finding_id rfi FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0 AND cluster_link IS NOT NULL"):
        toks = tokens(r["cl"]) & inprog_set
        if not toks:
            continue
        linked = (r["id"] in cat) or (r["status"] in LINKED_STATUSES) or bool(r["scc"]) or (r["rfi"] is not None)
        for cl in toks:
            f_alloc[cl].append(r["id"])
            if not linked:
                f_review[cl].append(r)

    # flags allocated to an in-progress cluster
    fl_alloc = defaultdict(list)
    fl_review = defaultdict(list)
    ph = ",".join("?" * len(FLAG_CODES))
    for r in cur.execute(f"SELECT id, flag_code fc, flag_label flb, description d, cluster_link cl, COALESCE(resolved,0) res FROM wa_session_research_flags WHERE flag_code IN ({ph}) AND cluster_link IS NOT NULL", FLAG_CODES):
        toks = tokens(r["cl"]) & inprog_set
        if not toks:
            continue
        linked = bool(r["res"]) or (r["id"] in cited)
        for cl in toks:
            fl_alloc[cl].append(r["id"])
            if not linked:
                fl_review[cl].append(r)

    L = ["# In-progress clusters — allocated pointers not yet linked to a finding (step b)", "",
         "**Generated:** 2026-06-01 (read-only). Pointers routed (cluster_link, exact token) to a cluster whose status is 'Analysis - In Progress', not yet adopted/linked to a finding, not set aside.", "",
         f"In-progress clusters ({len(inprog)}): {', '.join(inprog)}", "",
         "## Per-cluster summary", "",
         "| cluster | findings allocated | findings NOT yet linked | flags allocated | flags NOT yet linked |",
         "|---|--:|--:|--:|--:|"]
    tot = [0, 0, 0, 0]
    for cl in inprog:
        a, b = len(f_alloc[cl]), len(f_review[cl]); d, e = len(fl_alloc[cl]), len(fl_review[cl])
        tot[0] += a; tot[1] += b; tot[2] += d; tot[3] += e
        L.append(f"| {cl} | {a} | {b} | {d} | {e} |")
    L.append(f"| **TOTAL (rows; pointers in N clusters counted N×)** | {tot[0]} | {tot[1]} | {tot[2]} | {tot[3]} |")

    # distinct review pointers
    df = len({r['id'] for lst in f_review.values() for r in lst})
    dfl = len({r['id'] for lst in fl_review.values() for r in lst})
    L += ["", f"Distinct pointers needing review: **{df} findings + {dfl} flags**.", ""]

    L += ["## Not-yet-linked, per cluster", ""]
    for cl in inprog:
        if not f_review[cl] and not fl_review[cl]:
            continue
        L.append(f"### {cl} — {len(f_review[cl])} findings, {len(fl_review[cl])} flags")
        if f_review[cl]:
            L += ["", "| finding id | type | status | text |", "|---|---|---|---|"]
            for r in sorted(f_review[cl], key=lambda r: len(r["finding"] or ""))[:60]:
                t = (r["finding"] or "").replace("|", "/").replace("\n", " ")
                L.append(f"| {r['id']} | {r['ft']} | {r['status']} | {(t[:120]+'…') if len(t)>121 else t} |")
            if len(f_review[cl]) > 60:
                L.append(f"| … | | | _({len(f_review[cl])-60} more)_ |")
        if fl_review[cl]:
            L += ["", "| flag id | code | text |", "|---|---|---|"]
            for r in sorted(fl_review[cl], key=lambda r: len((r["flb"] or "")+(r["d"] or "")))[:40]:
                t = ((r["flb"] or "")+" — "+(r["d"] or "")).replace("|", "/").replace("\n", " ")
                L.append(f"| {r['id']} | {r['fc']} | {(t[:120]+'…') if len(t)>121 else t} |")
        L.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"in-progress clusters: {len(inprog)}")
    print(f"distinct review pointers: {df} findings + {dfl} flags")
    print(f"alloc totals (row-counted): findings {tot[0]} (review {tot[1]}), flags {tot[2]} (review {tot[3]})")
    print("wrote:", OUT)
    c.close()


if __name__ == "__main__":
    main()
