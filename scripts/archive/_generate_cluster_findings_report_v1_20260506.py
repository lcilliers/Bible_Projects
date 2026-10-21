"""_generate_cluster_findings_report_v1_20260506.py — read-only.

Render cluster_finding rows for a given M-cluster as a structured report.

Layout:
  §1 Coverage summary (per sub-group + cluster level)
  §2 Cluster-level findings (cluster_subgroup_id IS NULL)
  §3 Findings per sub-group, organised by tier → component → prompt
  §4 Gap rows requiring CC follow-up

Companion to wa-cluster-{code}-grouped-v{N}-{date}.md (which renders
verses by sub-group/group). The findings report renders the catalogue-
prompt analytical layer.
"""
from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
SESSIONS_DIR = os.path.join("Sessions", "Session_Clusters")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def next_version(out_dir, base):
    pat = re.compile(r"^" + re.escape(base) + r"-v(\d+)-\d{8}\.md$")
    max_v = 0
    if os.path.isdir(out_dir):
        for f in os.listdir(out_dir):
            m = pat.match(f)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def sanitise(s):
    if not s:
        return ""
    s = str(s).replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
    while "  " in s:
        s = s.replace("  ", " ")
    return s.strip().replace("|", "\\|")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--version", default="auto")
    ap.add_argument(
        "--include-stubs", action="store_true",
        help="Include stub findings ('not separately addressed' cells)",
    )
    args = ap.parse_args()

    date = datetime.now().strftime("%Y%m%d")
    dest_dir = os.path.join(SESSIONS_DIR, args.m_cluster)
    os.makedirs(dest_dir, exist_ok=True)
    base = f"wa-cluster-{args.m_cluster}-findings"
    version = (
        next_version(dest_dir, base)
        if args.version == "auto" else args.version
    )
    out_path = os.path.join(dest_dir, f"{base}-{version}-{date}.md")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code=?", (args.m_cluster,)
    ).fetchone()
    if not cluster:
        print(f"ERROR: cluster {args.m_cluster} not found")
        return 1

    subgroups = [dict(r) for r in conn.execute("""
        SELECT id, subgroup_code, label, core_description, sort_order
          FROM cluster_subgroup
         WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
         ORDER BY sort_order
    """, (args.m_cluster,)).fetchall()]
    sg_by_id = {sg["id"]: sg for sg in subgroups}

    # Load all findings + prompt context
    rows = [dict(r) for r in conn.execute("""
        SELECT cf.id, cf.obs_id, cf.cluster_subgroup_id, cf.finding_status,
               cf.finding_text, cf.source_file,
               oqc.question_code, oqc.tier, oqc.component_code,
               oqc.component_title, oqc.prompt_seq, oqc.question_text
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue oqc ON oqc.obs_id=cf.obs_id
         WHERE cf.cluster_code=? AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY oqc.tier, oqc.component_code, oqc.prompt_seq, oqc.obs_id,
                  cf.cluster_subgroup_id
    """, (args.m_cluster,)).fetchall()]

    L = []

    def add(s=""):
        L.append(s)

    add(f"# {args.m_cluster} {cluster['description']} — findings report")
    add()
    add(f"**Generated:** {now_iso()}  ")
    add(f"**Cluster:** `{args.m_cluster}` "
        f"(bucket={cluster['bucket']}, status={cluster['status']}, "
        f"version={cluster['version']})  ")
    add(f"**Source:** `database/bible_research.db` table `cluster_finding`  ")
    add(f"**Catalogue:** 189 tier prompts (T0–T7), full coverage map.  ")
    add()
    add("---")
    add()

    # § 1. Coverage summary
    add("## §1. Coverage summary")
    add()
    add("Counts of `cluster_finding` rows by scope and status. "
        "**E** (evidenced) = `finding` status with verbatim text from the "
        "consolidated findings document. **S** (silent) = explicit `S` "
        "marker in the source. **G** (gap) = explicit `G` marker — flagged "
        "for CC database query. **C** (cluster synthesis) = `[CLUSTER]` "
        "paragraph in the source. **N/A** = sub-group not separately "
        "addressed in the source (see cluster-level finding for the prompt).")
    add()
    add("| Scope | Total | E (evidenced) | S (silent) | G (gap) | "
        "C (synthesis) | N/A (stub) |")
    add("|---|---:|---:|---:|---:|---:|---:|")

    def status_counts(scope_filter):
        d = defaultdict(int)
        d["total"] = 0
        for r in rows:
            if not scope_filter(r):
                continue
            d["total"] += 1
            text = r["finding_text"] or ""
            if text.startswith("[Sub-group not"):
                d["na"] += 1
                continue
            if r["finding_status"] == "finding":
                d["E"] += 1
            elif r["finding_status"] == "silent":
                d["S"] += 1
            elif r["finding_status"] == "gap":
                d["G"] += 1
            elif r["finding_status"] == "cluster_synthesis":
                d["C"] += 1
        return d

    for sg in subgroups:
        d = status_counts(lambda r, sg=sg: r["cluster_subgroup_id"] == sg["id"])
        add(f"| `{sg['subgroup_code']}` ({sanitise(sg['label'])}) | "
            f"{d['total']} | {d['E']} | {d['S']} | {d['G']} | "
            f"{d['C']} | {d['na']} |")
    d_cluster = status_counts(lambda r: r["cluster_subgroup_id"] is None)
    add(f"| **CLUSTER** (cluster-level) | {d_cluster['total']} | "
        f"{d_cluster['E']} | {d_cluster['S']} | {d_cluster['G']} | "
        f"{d_cluster['C']} | {d_cluster['na']} |")
    d_total = status_counts(lambda r: True)
    add(f"| **TOTAL** | {d_total['total']} | {d_total['E']} | "
        f"{d_total['S']} | {d_total['G']} | {d_total['C']} | "
        f"{d_total['na']} |")
    add()
    add("---")
    add()

    # § 2. Cluster-level findings
    add("## §2. Cluster-level findings")
    add()
    add("Findings authored at cluster scope (`cluster_subgroup_id IS NULL`).")
    add()

    cluster_rows = [r for r in rows if r["cluster_subgroup_id"] is None]
    cluster_real = [
        r for r in cluster_rows
        if not (r["finding_text"] or "").startswith("[Sub-group not")
    ]
    if not cluster_real:
        add("(none populated)")
        add()
    else:
        # Group by tier
        by_tier = defaultdict(list)
        for r in cluster_real:
            by_tier[r["tier"]].append(r)
        for tier in sorted(by_tier.keys()):
            add(f"### {tier}")
            add()
            for r in by_tier[tier]:
                add(f"**{r['question_code']}** "
                    f"`[{r['finding_status']}]` "
                    f"{sanitise(r['question_text'])}")
                add()
                add(r["finding_text"])
                add()
        add("---")
        add()

    # § 3. Findings per sub-group
    add("## §3. Findings per sub-group")
    add()
    add("All catalogue-prompt findings recorded against each sub-group, "
        "ordered by tier → component → prompt sequence.")
    add()

    for sg_idx, sg in enumerate(subgroups, 1):
        sg_rows = [
            r for r in rows if r["cluster_subgroup_id"] == sg["id"]
        ]
        # Filter: include stubs only if --include-stubs
        if not args.include_stubs:
            sg_rows = [
                r for r in sg_rows
                if not (r["finding_text"] or "").startswith(
                    "[Sub-group not"
                )
            ]
        if not sg_rows:
            add(f"### §3.{sg_idx} `{sg['subgroup_code']}` — "
                f"{sanitise(sg['label'])}")
            add()
            add("(no findings recorded for this sub-group)")
            add()
            continue

        add(f"### §3.{sg_idx} `{sg['subgroup_code']}` — "
            f"{sanitise(sg['label'])}")
        add()
        add(f"_{sanitise(sg['core_description'])}_")
        add()
        add(f"**Findings recorded:** {len(sg_rows)}")
        add()

        # Group by tier and component
        by_tc = defaultdict(lambda: defaultdict(list))
        for r in sg_rows:
            by_tc[r["tier"]][r["component_code"]].append(r)

        for tier in sorted(by_tc.keys()):
            comps = by_tc[tier]
            add(f"#### {tier}")
            add()
            comp_keys = sorted(comps.keys(), key=lambda c: (
                c.split(".")[0],
                int(c.split(".")[1]) if "." in c and c.split(".")[1].isdigit()
                else 0,
            ))
            for cc in comp_keys:
                comp_rows = comps[cc]
                comp_title = comp_rows[0]["component_title"] or ""
                add(f"_{cc} — {sanitise(comp_title)}_")
                add()
                for r in comp_rows:
                    add(f"**{r['question_code']}** "
                        f"`[{r['finding_status']}]` "
                        f"{sanitise(r['question_text'])}")
                    add()
                    add(r["finding_text"])
                    add()
        add("---")
        add()

    # § 4. Gap rows
    gap_rows = [r for r in rows if r["finding_status"] == "gap"]
    add("## §4. Gap rows requiring follow-up")
    add()
    if not gap_rows:
        add("(none)")
        add()
    else:
        add(f"_{len(gap_rows)} gap rows flagged in the consolidated "
            f"findings — requiring CC database queries or further "
            f"investigation._")
        add()
        add("| Prompt | Scope | Question | Excerpt |")
        add("|---|---|---|---|")
        for r in gap_rows:
            sg_id = r["cluster_subgroup_id"]
            scope = (
                sg_by_id[sg_id]["subgroup_code"] if sg_id else "CLUSTER"
            )
            text = (r["finding_text"] or "")[:120]
            add(f"| {r['question_code']} | `{scope}` | "
                f"{sanitise(r['question_text'])} | "
                f"{sanitise(text)}... |")
        add()

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"Wrote: {out_path}")
    print(f"Cluster-level findings populated: {len(cluster_real)}")
    print(f"Gap rows: {len(gap_rows)}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
