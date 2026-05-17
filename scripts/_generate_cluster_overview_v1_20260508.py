"""_generate_cluster_overview_v1_20260508.py — read-only.

Programme-wide cluster overview report. One row per cluster, summarising:
  - cluster_code, description, status
  - active term count, OT/NT split
  - sub-group count
  - active verse count (across all cluster terms)
  - anchor count (is_anchor=1 active rows)
  - cluster_finding count by status (synthesis / finding / silent / gap)
  - last_updated_date

Output: Workflow/Clusters/wa-cluster-overview-{date}.md
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Workflow", "Clusters")


def now_compact():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def status_marker(status):
    return {
        "Analysis Completed": "✓",
        "Analysis Completed (Terms Added)": "✓+",
        "Analysis - In Progress": "▶",
        "Data - In Progress": "◐",
        "Not started": "·",
    }.get(status, "?")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    clusters = list(cur.execute(
        "SELECT cluster_code, short_name, description, gloss, status, bucket, "
        "       version, last_updated_date "
        "  FROM cluster ORDER BY cluster_code"
    ))

    # Pre-compute per-cluster aggregates in single passes to avoid per-row SQL
    term_counts = {}
    for r in cur.execute(
        "SELECT cluster_code, language, COUNT(*) AS n "
        "  FROM mti_terms "
        " WHERE COALESCE(delete_flagged,0)=0 AND cluster_code IS NOT NULL "
        " GROUP BY cluster_code, language"
    ):
        term_counts.setdefault(r["cluster_code"], {})[r["language"]] = r["n"]

    sg_counts = {}
    for r in cur.execute(
        "SELECT cluster_code, COUNT(*) AS n "
        "  FROM cluster_subgroup "
        " WHERE COALESCE(delete_flagged,0)=0 "
        " GROUP BY cluster_code"
    ):
        sg_counts[r["cluster_code"]] = r["n"]

    verse_counts = {}
    anchor_counts = {}
    for r in cur.execute(
        # Post-M47: vcg ↔ term is m:n. Use vc.mti_term_id directly to
        # determine the cluster (vc has its own mti_term_id, not derived
        # from the vcg).
        "SELECT mt.cluster_code, "
        "       COUNT(DISTINCT vc.id) AS n_vc, "
        "       SUM(CASE WHEN vc.is_anchor=1 THEN 1 ELSE 0 END) AS n_anchor "
        "  FROM verse_context vc "
        "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        " WHERE COALESCE(vc.delete_flagged,0)=0 "
        "   AND COALESCE(mt.delete_flagged,0)=0 "
        "   AND mt.cluster_code IS NOT NULL "
        " GROUP BY mt.cluster_code"
    ):
        verse_counts[r["cluster_code"]] = r["n_vc"] or 0
        anchor_counts[r["cluster_code"]] = r["n_anchor"] or 0

    finding_counts = {}
    for r in cur.execute(
        "SELECT cluster_code, finding_status, COUNT(*) AS n "
        "  FROM cluster_finding "
        " WHERE COALESCE(delete_flagged,0)=0 "
        " GROUP BY cluster_code, finding_status"
    ):
        finding_counts.setdefault(r["cluster_code"], {})[r["finding_status"]] = r["n"]

    # Build report
    today = now_compact()
    out_path = Path(OUT_DIR) / f"wa-cluster-overview-{today}.md"
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append(f"# Cluster Overview — programme-wide snapshot")
    lines.append("")
    lines.append(f"_Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_  ")
    lines.append(f"_Source: `database/bible_research.db`_")
    lines.append("")

    # Status roll-up
    by_status = {}
    for c in clusters:
        by_status[c["status"]] = by_status.get(c["status"], 0) + 1
    lines.append("## Status roll-up")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")
    for s in ("Analysis Completed", "Analysis - In Progress", "Not started"):
        if s in by_status:
            lines.append(f"| {status_marker(s)} {s} | {by_status[s]} |")
    other = {k: v for k, v in by_status.items()
             if k not in ("Analysis Completed", "Analysis - In Progress", "Not started")}
    for k, v in sorted(other.items()):
        lines.append(f"| {k} | {v} |")
    lines.append(f"| **Total clusters** | **{len(clusters)}** |")
    lines.append("")

    # Programme totals
    total_terms = sum(sum(d.values()) for d in term_counts.values())
    total_verses = sum(verse_counts.values())
    total_anchors = sum(anchor_counts.values())
    total_findings = sum(sum(d.values()) for d in finding_counts.values())
    lines.append("## Programme totals")
    lines.append("")
    lines.append(f"- Active terms (cluster-assigned): **{total_terms:,}**")
    lines.append(f"- Active verses (in cluster groups): **{total_verses:,}**")
    lines.append(f"- Anchor verses set: **{total_anchors:,}**")
    lines.append(f"- `cluster_finding` rows (active): **{total_findings:,}**")
    lines.append("")

    # Per-cluster table
    lines.append("## Per-cluster detail")
    lines.append("")
    lines.append(
        "| | Code | Short | Description | Status | Terms (OT+NT) | Sub-grps | Verses | Anchors | Findings (s/f/g/syn) | Updated |"
    )
    lines.append(
        "|---|---|---|---|---|---:|---:|---:|---:|---|---|"
    )
    for c in clusters:
        code = c["cluster_code"]
        tc = term_counts.get(code, {})
        ot = tc.get("Hebrew", 0)
        nt = tc.get("Greek", 0)
        terms_total = ot + nt
        terms_str = f"{terms_total} ({ot}+{nt})" if terms_total else "—"
        sg = sg_counts.get(code, 0)
        v = verse_counts.get(code, 0)
        a = anchor_counts.get(code, 0)
        fc = finding_counts.get(code, {})
        if fc:
            f_str = (
                f"{fc.get('silent',0)}/{fc.get('finding',0)}/"
                f"{fc.get('gap',0)}/{fc.get('cluster_synthesis',0)}"
            )
            f_total = sum(fc.values())
            f_cell = f"{f_total} ({f_str})"
        else:
            f_cell = "—"
        updated = (c["last_updated_date"] or "")[:10]
        lines.append(
            f"| {status_marker(c['status'])} "
            f"| **{code}** "
            f"| {c['short_name'] or ''} "
            f"| {c['description'] or ''} "
            f"| {c['status']} "
            f"| {terms_str} "
            f"| {sg} "
            f"| {v} "
            f"| {a} "
            f"| {f_cell} "
            f"| {updated} |"
        )
    lines.append("")

    # Per-cluster gloss listing (full term-gloss text for each cluster)
    lines.append("## Cluster glosses (full term-gloss lists)")
    lines.append("")
    lines.append(
        "The full `cluster.gloss` field for each cluster — the complete list of "
        "primary terms (with parenthetical transliterations) covered by the cluster. "
        "Intended as parseable input for downstream processes."
    )
    lines.append("")
    for c in clusters:
        code = c["cluster_code"]
        short = c["short_name"] or ""
        desc = c["description"] or ""
        gloss = (c["gloss"] or "").strip()
        header_tail = f" — {desc}" if desc else ""
        header_short = f" ({short})" if short else ""
        lines.append(f"### {code}{header_tail}{header_short}")
        lines.append("")
        if gloss:
            lines.append(gloss)
        else:
            lines.append("_(no gloss recorded)_")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Footer key
    lines.append("## Notation")
    lines.append("")
    lines.append("- **Status markers:** ✓ completed · ▶ in progress · · not started")
    lines.append("- **Terms (OT+NT):** active mti_terms split by language (Hebrew + Greek)")
    lines.append("- **Verses:** active `verse_context` rows for terms in this cluster")
    lines.append("- **Anchors:** `verse_context.is_anchor=1` rows in cluster groups")
    lines.append("- **Findings (s/f/g/syn):** `silent` / `finding` / `gap` / `cluster_synthesis` row counts; total in parens")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out_path}")
    print(f"Clusters: {len(clusters)}")
    print(f"  Completed:    {by_status.get('Analysis Completed', 0)}")
    print(f"  In progress:  {by_status.get('Analysis - In Progress', 0)}")
    print(f"  Not started:  {by_status.get('Not started', 0)}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
