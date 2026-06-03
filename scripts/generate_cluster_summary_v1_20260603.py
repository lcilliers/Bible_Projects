"""generate_cluster_summary_v1_20260603.py

Read-only cluster summary report for the current M-cluster methodology
(schema v3.28.0). For every cluster in the `cluster` table, report status,
version, last-updated date, and live counts: active terms, active findings,
relevant verse-context rows, sub-groups. Plus a programme-wide status rollup.

Output: Workflow/Programme/Program_reports/wa-programme-cluster-summary-{date}.md
        (read-only; no DB writes). Filing per docs/file-organisation-rules.md §3.10.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Workflow", "Programme", "Program_reports")

STATUS_ORDER = [
    "Analysis Completed",
    "Analysis Completed (Terms Added)",
    "Ready for re-analysis",
    "Structurally Ready",
    "Not started",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    clusters = conn.execute(
        """SELECT cluster_code, short_name, gloss, bucket, status, version,
                  last_updated_date, char_structure
           FROM cluster ORDER BY cluster_code"""
    ).fetchall()

    data = []
    for c in clusters:
        code = c["cluster_code"]
        terms = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
            (code,),
        ).fetchone()[0]
        findings = conn.execute(
            "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
            (code,),
        ).fetchone()[0]
        rel_verses = conn.execute(
            """SELECT COUNT(*) FROM verse_context vc
               JOIN mti_terms t ON t.id = vc.mti_term_id
               WHERE t.cluster_code=? AND COALESCE(vc.is_relevant,0)=1
                 AND COALESCE(vc.delete_flagged,0)=0""",
            (code,),
        ).fetchone()[0]
        subgroups = conn.execute(
            "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code=?",
            (code,),
        ).fetchone()[0]
        data.append({"row": c, "terms": terms, "findings": findings,
                     "rel_verses": rel_verses, "subgroups": subgroups})

    total = len(data)
    # status rollup
    rollup: dict[str, int] = {}
    for d in data:
        rollup[d["row"]["status"]] = rollup.get(d["row"]["status"], 0) + 1

    P: list[str] = []
    P.append("# Cluster Summary Report\n")
    P.append(f"**Generated:** {now_iso()} · **Source:** `database/bible_research.db` (schema v3.28.0)")
    P.append(f"**Total clusters:** {total}\n")
    P.append("> DB state = recovered **2026-05-28** snapshot. June 1–2 remediation "
             "(M10b/M38/M08 closures, COMMENT_EVALUATION, M20 advance, dedup-ghost repair) "
             "is **not reflected** here — see `wa-db-recovery-assessment-20260603.md`.\n")

    P.append("## Status rollup\n")
    P.append("| Status | Count |")
    P.append("| --- | ---: |")
    for s in STATUS_ORDER:
        if s in rollup:
            P.append(f"| {s} | {rollup[s]} |")
    for s, n in rollup.items():
        if s not in STATUS_ORDER:
            P.append(f"| {s} | {n} |")
    P.append("")

    # Active / in-flight clusters (everything not "Not started")
    P.append("## Clusters in flight (status ≠ Not started)\n")
    P.append("| Cluster | Name | Status | Ver | Terms | Sub-grps | Findings | Rel. verses | Last updated |")
    P.append("| --- | --- | --- | :-: | ---: | ---: | ---: | ---: | --- |")

    def sort_key(d):
        st = d["row"]["status"]
        idx = STATUS_ORDER.index(st) if st in STATUS_ORDER else 99
        return (idx, d["row"]["cluster_code"])

    active = [d for d in data if d["row"]["status"] != "Not started"]
    for d in sorted(active, key=sort_key):
        r = d["row"]
        upd = (r["last_updated_date"] or "")[:10]
        P.append(
            f"| {r['cluster_code']} | {r['short_name']} | {r['status']} | "
            f"{str(r['version']).replace('vv','v')} | {d['terms']} | {d['subgroups']} | "
            f"{d['findings']} | {d['rel_verses']} | {upd} |"
        )
    P.append("")

    # Not-started clusters (compact)
    not_started = [d for d in data if d["row"]["status"] == "Not started"]
    if not_started:
        P.append(f"## Not started ({len(not_started)})\n")
        P.append("| Cluster | Name | Terms | Rel. verses |")
        P.append("| --- | --- | ---: | ---: |")
        for d in sorted(not_started, key=lambda x: x["row"]["cluster_code"]):
            r = d["row"]
            P.append(f"| {r['cluster_code']} | {r['short_name']} | {d['terms']} | {d['rel_verses']} |")
        P.append("")

    # Programme totals
    tot_terms = sum(d["terms"] for d in data)
    tot_find = sum(d["findings"] for d in data)
    tot_rel = sum(d["rel_verses"] for d in data)
    P.append("## Programme totals\n")
    P.append(f"- Active terms (clustered, not delete-flagged): **{tot_terms:,}**")
    P.append(f"- Active cluster findings: **{tot_find:,}**")
    P.append(f"- Relevant verse-context rows (clustered): **{tot_rel:,}**")
    P.append("")
    P.append("---")
    P.append("*Read-only report. Generated by `scripts/generate_cluster_summary_v1_20260603.py`.*")

    os.makedirs(OUT_DIR, exist_ok=True)
    date = datetime.now(timezone.utc).strftime("%Y%m%d")
    out_path = os.path.join(OUT_DIR, f"wa-programme-cluster-summary-{date}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(P))
    print(f"Wrote {out_path} ({len(P)} lines)")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
