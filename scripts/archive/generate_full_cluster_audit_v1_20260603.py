"""generate_full_cluster_audit_v1_20260603.py  (READ-ONLY)

Sweep every *started* cluster (status != 'Not started') through the proven
read-only auditor `audit_cluster()` from audit_cluster_v1_20260601.py, and write
ONE consolidated, today-dated programme audit report.

Does NOT touch the per-cluster `wa-cluster-{CODE}-audit-*.md` files (those are the
genuine 06-01/06-02 artefacts). Reuses the audit logic; only orchestrates + renders.

Output: Workflow/Programme/Program_reports/wa-programme-cluster-audit-20260603.md
Filing per docs/file-organisation-rules.md §3.10 (programme report).
"""
from __future__ import annotations

import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# reuse the proven, read-only audit engine
from importlib import import_module
_aud = import_module("audit_cluster_v1_20260601")
audit_cluster = _aud.audit_cluster
render_dispositions = _aud.render_dispositions

DB = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Workflow", "Programme", "Program_reports")
OUT = os.path.join(OUT_DIR, "wa-programme-cluster-audit-v3-20260603.md")


def main() -> int:
    c = sqlite3.connect(DB, timeout=30)
    c.row_factory = sqlite3.Row
    clusters = c.execute(
        "SELECT cluster_code, short_name, status FROM cluster "
        "WHERE status IS NOT NULL AND TRIM(status) <> '' AND status <> 'Not started' "
        "ORDER BY status, cluster_code"
    ).fetchall()

    L = [
        "# Programme Cluster Audit — all started clusters",
        "",
        "**Generated:** 2026-06-03 — **v3** (read-only re-run AFTER M10b/M10c remediation + "
        "citation-extractor sweep across all 19). Engine: `scripts/audit_cluster_v1_20260601.py`. "
        "Spec: `Workflow/methodology/wa-cluster-audit-aspect-spec-v1-20260601.md`.",
        "",
        "> Supersedes v2. Cumulative since v1: FLAG rescue (126→539), cluster_link (D2 cleared), "
        "orphan set-aside (30+72), M10c + M10b A7 dispositions, citation extractor re-run on all "
        "started clusters (B6/B7). Remaining FAILs = fresh COMMENT_EVALUATION (A6/A7) + B1a/B1b "
        "backfill + M11/M38 re-analysis. See the apply-logs in research/investigations/.",
        "",
        "GATE failure ⇒ not validly Analysis Complete. STRUCT = structural completeness. "
        "INFO/REVIEW = advisory. INCR = re-submit/clear work.",
        "",
        f"**Scope:** {len(clusters)} started clusters.",
        "",
    ]

    summ = []      # (code, name, status, verdict, gate_fails, struct_fails, review, d1, d2)
    worklist = []
    for cl in clusters:
        code = cl["cluster_code"]
        verdict, R = audit_cluster(c, code)
        gate_fails = [r for r in R if r["sev"] == "GATE" and r["status"] == "FAIL"]
        struct_fails = [r for r in R if r["sev"] == "STRUCT" and r["status"] == "FAIL"]
        review_items = [r for r in R if r["sev"] == "INFO" and r["status"] == "REVIEW"]
        d1 = next((r for r in R if r["id"] == "D1"), None)
        d2 = next((r for r in R if r["id"] == "D2"), None)
        summ.append((code, cl["short_name"], cl["status"], verdict, len(gate_fails),
                     len(struct_fails), len(review_items),
                     d1["count"] if d1 else 0, d2["count"] if d2 else 0))

        parts = []
        if gate_fails:
            parts.append(f"**{len(gate_fails)} GATE-blocking** ({', '.join(r['id'] for r in gate_fails)})")
        if struct_fails:
            parts.append(f"{len(struct_fails)} structural ({', '.join(r['id'] for r in struct_fails)})")
        if review_items:
            parts.append(f"{len(review_items)} advisory-review ({', '.join(r['id'] for r in review_items)})")
        outstanding = "**nothing outstanding**" if not parts else "; ".join(parts)

        L += [f"## {code} {cl['short_name']} — verdict **{verdict}**", "",
              f"- **Cluster status (DB):** `{cl['status']}`",
              f"- **Outstanding:** {outstanding}", "",
              "| ID | Aspect | Sec | Sev | Status | Count | Detail |",
              "|---|---|---|---|---|--:|---|"]
        for r in R:
            det = "<br>".join(str(x).replace("|", "\\|") for x in r["detail"])
            L.append(f"| {r['id']} | {r['name']} | {r['section']} | {r['sev']} | "
                     f"{r['status']} | {r['count']} | {det} |")
        L.append("")
        L += render_dispositions(code)

        for r in gate_fails:
            verb = "CLEAR" if r["id"] in ("A4", "A5", "A6", "A7", "A8") else "RE-SUBMIT"
            worklist.append((code, verb, f"{r['id']} {r['name']} ({r['count']})"))
        for r in R:
            if r["sev"] == "STRUCT" and r["status"] == "FAIL":
                worklist.append((code, "RE-SUBMIT", f"{r['id']} {r['name']} ({r['count']})"))
            if r["sev"] == "INFO" and r["status"] == "REVIEW":
                worklist.append((code, "REVIEW", f"{r['id']} {r['name']} ({r['count']})"))
            if r["sev"] == "INCR" and isinstance(r["count"], int) and r["count"] > 0:
                worklist.append((code, "RE-SUBMIT" if r["id"] == "D1" else "ADOPT",
                                 f"{r['id']} {r['name']} ({r['count']})"))

    # cross-cluster summary
    L += ["---", "", "## Cross-cluster summary", "",
          "| Cluster | Name | DB status | Verdict | GATE | STRUCT | REVIEW | New terms (D1) | Unalloc ptrs (D2) |",
          "|---|---|---|---|--:|--:|--:|--:|--:|"]
    for code, name, status, v, gf, sf, ri, t, p in summ:
        L.append(f"| {code} | {name} | {status} | {v} | {gf} | {sf} | {ri} | {t} | {p} |")
    npass = sum(1 for s in summ if s[3] == "PASS")
    nfail = len(summ) - npass
    L += ["", f"**PASS {npass} · FAIL {nfail}** of {len(summ)} started clusters.", "",
          "## Consolidated worklist (re-submit / clear / adopt / review)", "",
          "| Cluster | Action | Item |", "|---|---|---|"]
    for code, verb, item in worklist:
        L.append(f"| {code} | {verb} | {item} |")
    if not worklist:
        L.append("| — | — | (nothing outstanding) |")
    L.append("")
    L.append("---")
    L.append("*Read-only. Generated by `scripts/generate_full_cluster_audit_v1_20260603.py` "
             "(reuses `audit_cluster_v1_20260601.audit_cluster`).*")

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"audited {len(summ)} started clusters | PASS {npass} FAIL {nfail} | worklist {len(worklist)}")
    for code, name, status, v, gf, sf, ri, t, p in summ:
        print(f"  {code:5} {v:5} gate={gf} struct={sf} review={ri} status='{status}'")
    print("report:", OUT)
    c.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
