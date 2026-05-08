"""build_obs_catalogue_tiered_extract.py — read-only.

Extract the 189 tiered observation prompts (T0..T7) from
`wa_obs_question_catalogue` into a markdown file.

Output:
  Workflow/Catalogue/wa-obs-catalogue-tiered-v{N}-{YYYYMMDD}.md

Structure: tier → component → numbered questions (prompt_seq).
Read-only: never modifies the database.
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
OUT_DIR = os.path.join("Workflow", "Catalogue")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def next_version(out_dir: str, base_name: str) -> str:
    pat = re.compile(
        r"^" + re.escape(base_name) + r"-v(\d+)-\d{8}\.md$"
    )
    max_v = 0
    if os.path.isdir(out_dir):
        for f in os.listdir(out_dir):
            m = pat.match(f)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def get_schema_version(conn) -> str:
    r = conn.execute(
        "SELECT version_code FROM schema_version "
        "ORDER BY id DESC LIMIT 1"
    ).fetchone()
    return r[0] if r else "?"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--version", default="auto",
        help="vN override; default 'auto' = scan dir for highest vN, bump",
    )
    args = ap.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)
    base = "wa-obs-catalogue-tiered"
    version = (
        next_version(OUT_DIR, base)
        if args.version == "auto" else args.version
    )
    date = datetime.now().strftime("%Y%m%d")
    out_path = os.path.join(OUT_DIR, f"{base}-{version}-{date}.md")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    schema = get_schema_version(conn)

    rows = conn.execute("""
        SELECT obs_id, question_code, tier, component_code,
               component_title, prompt_seq, question_text, scope, status
          FROM wa_obs_question_catalogue
         WHERE tier IS NOT NULL
           AND COALESCE(deleted,0) = 0
         ORDER BY tier, component_code, prompt_seq, obs_id
    """).fetchall()

    by_tier = defaultdict(lambda: defaultdict(list))
    component_titles = {}
    for r in rows:
        by_tier[r["tier"]][r["component_code"]].append(dict(r))
        component_titles[r["component_code"]] = r["component_title"] or ""

    tier_titles = {
        "T0": "Divine Image and Created Design",
        "T1": "Definition",
        "T2": "Constitutional Location and Boundaries",
        "T3": "The Inner Faculties",
        "T4": "Relational Interfaces",
        "T5": "Formative and Developmental Dimension",
        "T6": "Structural Relationships with Other Characteristics",
        "T7": "Evidential and Methodological Foundation",
    }

    # ---- Build markdown
    L = []
    def add(s=""): L.append(s)

    total = sum(len(qs) for comps in by_tier.values() for qs in comps.values())
    add("# WA Observation Catalogue — Tiered Prompts (T0–T7)")
    add()
    add(f"**Generated:** {now_iso()}  ")
    add(f"**Schema:** `{schema}`  ")
    add(f"**Source table:** `wa_obs_question_catalogue` "
        f"(tier IS NOT NULL AND deleted=0)  ")
    add(f"**Total prompts:** {total}  ")
    add()
    add("---")
    add()
    add("## Summary")
    add()
    add("| Tier | Title | Components | Prompts |")
    add("|---|---|---:|---:|")
    for tier in sorted(by_tier.keys()):
        n_comp = len(by_tier[tier])
        n_q = sum(len(qs) for qs in by_tier[tier].values())
        add(f"| `{tier}` | {tier_titles.get(tier, '')} | {n_comp} | {n_q} |")
    add(f"| **Total** | | "
        f"**{sum(len(c) for c in by_tier.values())}** | "
        f"**{total}** |")
    add()
    add("---")
    add()

    for tier in sorted(by_tier.keys()):
        title = tier_titles.get(tier, "")
        n_q = sum(len(qs) for qs in by_tier[tier].values())
        add(f"## {tier} — {title}")
        add()
        add(f"_{len(by_tier[tier])} components, {n_q} prompts._")
        add()

        # Sort components numerically (T2.1, T2.2, ..., T2.10)
        def comp_sort_key(code):
            parts = code.split(".")
            try:
                return (parts[0], int(parts[1]))
            except (IndexError, ValueError):
                return (code,)

        for comp_code in sorted(by_tier[tier].keys(), key=comp_sort_key):
            qs = by_tier[tier][comp_code]
            comp_title = component_titles.get(comp_code, "")
            add(f"### {comp_code} — {comp_title}")
            add()
            for q in qs:
                code = q["question_code"] or f"obs_{q['obs_id']}"
                seq = q["prompt_seq"]
                text = (q["question_text"] or "").strip()
                add(f"{seq}. **`{code}`** — {text}")
            add()

        add("---")
        add()

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"Wrote: {out_path}")
    print(f"Tiers: {len(by_tier)}  Components: "
          f"{sum(len(c) for c in by_tier.values())}  "
          f"Prompts: {total}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
