"""_generate_cluster_catalogue_v1_20260505.py — read-only.

Reads the live `cluster` table from the database and produces a versioned
catalogue (JSON + Markdown) in Workflow/Clusters/.

Output filenames:
  Workflow/Clusters/wa-cluster-catalogue-v{version}-{date}.json
  Workflow/Clusters/wa-cluster-catalogue-v{version}-{date}.md

The catalogue is the human-readable + machine-readable view of the
authoritative cluster table.
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
WF_DIR = os.path.join("Workflow", "Clusters")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default="v1")
    args = ap.parse_args()
    date = datetime.now().strftime("%Y%m%d")
    os.makedirs(WF_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Pull cluster rows + per-cluster term counts
    rows = conn.execute("""
        SELECT c.cluster_code, c.description, c.gloss, c.source, c.bucket,
               c.status, c.version, c.last_updated_date,
               (SELECT COUNT(DISTINCT mt.strongs_number)
                  FROM mti_terms mt
                 WHERE mt.cluster_code = c.cluster_code) AS term_count
          FROM cluster c
         ORDER BY
           CASE c.bucket WHEN 'NAMED' THEN 0 ELSE 1 END,
           c.cluster_code
    """).fetchall()
    conn.close()

    # JSON
    out = {
        "meta": {
            "generated": now_iso(),
            "version": args.version,
            "source": "database/bible_research.db cluster table",
            "valid_status_values": [
                "Not started", "Data - In Progress",
                "Analysis - In Progress", "Analysis Completed", "Published",
            ],
        },
        "clusters": [dict(r) for r in rows],
    }
    out_json = os.path.join(
        WF_DIR, f"wa-cluster-catalogue-{args.version}-{date}.json"
    )
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Wrote: {out_json}")

    # Markdown
    out_md = os.path.join(
        WF_DIR, f"wa-cluster-catalogue-{args.version}-{date}.md"
    )
    lines = []
    lines.append(f"# Cluster catalogue — {args.version}\n")
    lines.append(f"**Generated:** {now_iso()}  ")
    lines.append(f"**Source:** `cluster` table in `database/bible_research.db`  ")
    lines.append(f"**Total clusters:** {len(rows)}\n")
    lines.append("**Valid status values:**")
    lines.append("- `Not started` — no work has begun on this cluster")
    lines.append("- `Data - In Progress` — verse-coverage clearance underway")
    lines.append("- `Analysis - In Progress` — term-level meaning analysis underway")
    lines.append("- `Analysis Completed` — analysis locked, awaiting publication")
    lines.append("- `Published` — analysis released for use in other contexts\n")
    lines.append("---\n")

    # Group by bucket
    by_bucket = {}
    for r in rows:
        by_bucket.setdefault(r["bucket"] or "(none)", []).append(r)

    for bucket in ("NAMED", "SUPPLEMENTARY", "REVIEW"):
        if bucket not in by_bucket:
            continue
        cl = by_bucket[bucket]
        lines.append(f"## {bucket} clusters ({len(cl)})\n")
        lines.append("| Code | Description | Terms | Status | Source | "
                     "Version | Last updated |")
        lines.append("|---|---|---:|---|---|---|---|")
        for r in cl:
            lines.append(
                f"| **{r['cluster_code']}** | {r['description'] or ''} | "
                f"{r['term_count']} | {r['status']} | "
                f"{r['source'] or ''} | {r['version'] or ''} | "
                f"{r['last_updated_date'] or ''} |"
            )
        lines.append("")

    # Per-cluster gloss section
    lines.append("\n## Cluster glosses (term-level vocabulary)\n")
    lines.append("Concatenation of all term glosses currently assigned to "
                 "the cluster (distinct, alphabetical).\n")
    for r in rows:
        gloss = r["gloss"] or ""
        # Truncate if very long for readability; full content in JSON
        if len(gloss) > 800:
            gloss = gloss[:800] + " …"
        lines.append(f"### {r['cluster_code']} — {r['description'] or ''} "
                     f"({r['term_count']} terms)")
        lines.append(f"_status: **{r['status']}** · bucket: {r['bucket']} · "
                     f"version: {r['version']}_")
        lines.append("")
        lines.append(gloss)
        lines.append("")

    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {out_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
