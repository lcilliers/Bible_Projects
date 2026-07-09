"""_render_m15_baseline_to_md_v1_20260511.py — read-only render of v3 JSON.

Produce a structured markdown view of the M15 baseline so the researcher
can evaluate where we are.

Sections:
  1. Metadata + headline numbers
  2. Per sub-group:
     a. New VCGs derived from v2 (code · title · description · verse count)
     b. DB VCGs in this sub-group (code · description · verse count)
     c. DB ↔ New cross-mapping matrix
     d. Side-by-side description pairs for each (DB, NEW) flow
     e. Verses with AI annotations (the cleanup breadcrumbs)
     f. Verses missing meaning AND/OR new_vcg
  3. Global anomaly tables:
     - Multi-candidate matches (verse appears in >1 v2 file)
     - Sub-group fallback matches (verse routed via different sg's v2)
     - DB duplicate-vc rows
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict, Counter
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
BASELINE_IN = os.path.join(M15_DIR, "m15-baseline-verses-v3-20260511.json")
OUT_PATH = os.path.join(M15_DIR, "m15-baseline-render-v1-20260511.md")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    with open(BASELINE_IN, "r", encoding="utf-8") as f:
        data = json.load(f)
    md = data["metadata"]
    verses = data["verses"]

    # Index verses by sub-group
    by_sg: dict[str, list] = defaultdict(list)
    for v in verses:
        sg = (v.get("current") or {}).get("subgroup_code") or "(unrouted)"
        by_sg[sg].append(v)

    out: list[str] = []
    w = out.append

    w(f"# M15 baseline — rendered view")
    w(f"")
    w(f"_Source JSON:_ `{os.path.relpath(BASELINE_IN, ROOT)}`")
    w(f"_Rendered:_ {now_iso()}")
    w(f"")
    w(f"## 1. Headline")
    w(f"")
    w(f"| | |")
    w(f"|---|---|")
    w(f"| Cluster | {md['cluster_code']} (status: `{md['cluster_status']}`, version `{md['cluster_version']}`) |")
    w(f"| Schema version | `{md['schema_version']}` |")
    w(f"| Baseline rows | {md['row_count']} ({md['unique_vr_count']} unique vr_ids) |")
    w(f"| Status distribution | "
      f"G={md['status_counts']['G']}  ·  "
      f"SA={md['status_counts']['SA']}  ·  "
      f"NR={md['status_counts']['NR']}  ·  "
      f"P={md['status_counts']['P']}  ·  "
      f"UT={md['status_counts']['UT']} |")
    w(f"| Duplicate vr_ids (data-integrity issue) | "
      f"{', '.join(map(str, md['duplicate_vr_ids']))} |")
    w(f"")

    if "meaning_layer" in md:
        ml = md["meaning_layer"]
        w(f"### Meaning layer (from v1 verse-meaning tables)")
        w(f"")
        w(f"| | |")
        w(f"|---|---|")
        w(f"| Meaning rows parsed | {ml['meaning_rows_parsed']} |")
        w(f"| Rows with meaning attached | {ml['baseline_rows_with_meaning']} |")
        w(f"| Rows MISSING meaning | {ml['baseline_rows_without_meaning']} |")
        w(f"| Unmatched meaning rows | {ml['meaning_rows_unmatched_to_baseline']} |")
        w(f"| VCG text mismatches (v1 file VCG ≠ DB group_code) | "
          f"{ml['vcg_mismatches_flagged']} |")
        w(f"")

    if "new_vcg_layer" in md:
        nv = md["new_vcg_layer"]
        w(f"### New-VCG layer (from v2 derived-VCG sections)")
        w(f"")
        w(f"| | |")
        w(f"|---|---|")
        w(f"| Ref assignments parsed | {nv['ref_assignments_parsed']} |")
        w(f"| New VCGs defined | {nv['new_vcgs_defined']} |")
        w(f"| Rows with new_vcg attached | {nv['baseline_rows_with_new_vcg']} |")
        w(f"| Rows MISSING new_vcg | {nv['baseline_rows_without_new_vcg']} |")
        w(f"| Matched via sub-group fallback | {nv['matched_via_subgroup_fallback']} |")
        w(f"| Verses with multi-candidates | {nv['verses_with_multiple_candidates']} |")
        w(f"| Verses with inline annotation (AI flags) | {nv['verses_with_annotation']} |")
        w(f"")

    # Sub-group coverage summary
    w(f"## 2. Sub-group coverage at a glance")
    w(f"")
    w(f"| Sub-group | Baseline rows | Meaning | New VCG | DB VCGs used | New VCGs |")
    w(f"|---|---:|---:|---:|---:|---:|")
    for sg in sorted(by_sg):
        rows = by_sg[sg]
        nm = sum(1 for v in rows if "meaning" in v)
        nv_ = sum(1 for v in rows if "new_vcg" in v)
        db_codes = {v["current"].get("group_code") for v in rows
                    if v.get("current", {}).get("group_code")}
        new_codes = {v["new_vcg"]["code"] for v in rows if "new_vcg" in v}
        w(f"| {sg} | {len(rows)} | {nm} | {nv_} | {len(db_codes)} | {len(new_codes)} |")
    w(f"")

    # Per sub-group detail
    w(f"## 3. Per sub-group detail")
    w(f"")
    for sg in sorted(by_sg):
        rows = by_sg[sg]
        w(f"### {sg}")
        w(f"")
        w(f"_{len(rows)} rows_")
        w(f"")

        # 3a. New VCGs derived (with verse counts)
        new_count = Counter()
        new_meta: dict[str, dict] = {}
        for v in rows:
            if "new_vcg" not in v:
                continue
            code = v["new_vcg"]["code"]
            new_count[code] += 1
            if code not in new_meta:
                new_meta[code] = v["new_vcg"]
        if new_meta:
            w(f"#### a. New VCGs derived (from v2)")
            w(f"")
            w(f"| Code | Title | Verses |")
            w(f"|---|---|---:|")
            for code, m in sorted(new_meta.items()):
                title = (m.get("title") or "").replace("|", "\\|")
                w(f"| `{code}` | {title} | {new_count[code]} |")
            w(f"")
            # Descriptions
            w(f"_Descriptions:_")
            w(f"")
            for code, m in sorted(new_meta.items()):
                desc = (m.get("description") or "(no description)").replace("\n", " ")
                w(f"- **{code}** — _{desc}_")
            w(f"")

        # 3b. DB VCGs in this sub-group
        db_count = Counter()
        db_descr: dict[str, str | None] = {}
        for v in rows:
            cur = v.get("current", {})
            code = cur.get("group_code")
            db_count[code] += 1
            if code and code not in db_descr:
                cmp_ = v.get("vcg_comparison", {}).get("db") or {}
                db_descr[code] = cmp_.get("description")
        if db_count:
            w(f"#### b. DB VCGs in this sub-group")
            w(f"")
            w(f"| Code | Description | Verses |")
            w(f"|---|---|---:|")
            for code in sorted(db_count, key=lambda c: (c is None, c)):
                d = (db_descr.get(code) or "(no description)").replace("\n", " ")
                d_short = (d[:140] + "…") if len(d) > 140 else d
                d_short = d_short.replace("|", "\\|")
                label = f"`{code}`" if code else "_(no group)_"
                w(f"| {label} | {d_short} | {db_count[code]} |")
            w(f"")

        # 3c. DB → New cross-mapping
        flow = Counter()
        for v in rows:
            db_code = (v.get("current") or {}).get("group_code") or "(none)"
            new_code = v.get("new_vcg", {}).get("code") if "new_vcg" in v else "(none)"
            flow[(db_code, new_code)] += 1
        if flow:
            w(f"#### c. DB ↔ New cross-mapping")
            w(f"")
            w(f"_How DB VCGs flow into the new derived VCGs. The diagonal "
              f"(or near-diagonal) is alignment; off-diagonal shows movement._")
            w(f"")
            w(f"| DB VCG | New VCG | Verses |")
            w(f"|---|---|---:|")
            for (dbc, newc), n in sorted(flow.items(), key=lambda x: (-x[1], x[0])):
                w(f"| `{dbc}` | `{newc}` | {n} |")
            w(f"")

        # 3d. AI annotations (from verse-level [⚠ ...] notes)
        annot = [v for v in rows
                 if v.get("new_vcg", {}).get("verse_annotation")]
        if annot:
            w(f"#### d. Verses with AI annotations ({len(annot)})")
            w(f"")
            w(f"_AI flagged these inline during v2 authoring — these are explicit cleanup breadcrumbs._")
            w(f"")
            w(f"| Reference | Strongs | DB VCG | New VCG | Annotation |")
            w(f"|---|---|---|---|---|")
            for v in annot[:200]:
                t = v["term"]
                db_code = (v.get("current") or {}).get("group_code") or "(none)"
                new_code = v.get("new_vcg", {}).get("code") or "(none)"
                ann = (v["new_vcg"].get("verse_annotation") or "").replace("|", "\\|")
                w(f"| {v['reference']} | {t['strongs']} {t['translit']} | "
                  f"`{db_code}` | `{new_code}` | {ann} |")
            if len(annot) > 200:
                w(f"\n_({len(annot) - 200} more not shown)_\n")
            w(f"")

        # 3e. Missing rows
        missing = [v for v in rows
                   if "meaning" not in v or "new_vcg" not in v]
        if missing:
            w(f"#### e. Verses missing meaning and/or new_vcg ({len(missing)})")
            w(f"")
            w(f"| Reference | Strongs | DB VCG | Status | Has meaning | Has new_vcg |")
            w(f"|---|---|---|---|:-:|:-:|")
            for v in missing[:200]:
                t = v["term"]
                db_code = (v.get("current") or {}).get("group_code") or "(none)"
                st = v.get("current", {}).get("status") or "?"
                hm = "✓" if "meaning" in v else "—"
                hnv = "✓" if "new_vcg" in v else "—"
                w(f"| {v['reference']} | {t['strongs']} {t['translit']} | "
                  f"`{db_code}` | {st} | {hm} | {hnv} |")
            if len(missing) > 200:
                w(f"\n_({len(missing) - 200} more not shown)_\n")
            w(f"")

        # 3f. Side-by-side comparison for distinct (DB VCG, NEW VCG) flow pairs
        flow_pairs: dict[tuple[str, str], dict] = {}
        for v in rows:
            if "vcg_comparison" not in v or "new_vcg" not in v:
                continue
            cmp_ = v["vcg_comparison"]
            db_code = cmp_["db"]["code"] or "(none)"
            new_code = cmp_["new"]["code"]
            key = (db_code, new_code)
            if key not in flow_pairs:
                flow_pairs[key] = {
                    "db_description": cmp_["db"]["description"],
                    "new_title": cmp_["new"]["title"],
                    "new_description": cmp_["new"]["description"],
                    "sample_ref": v["reference"],
                    "sample_strongs": v["term"]["strongs"],
                    "n": 0,
                }
            flow_pairs[key]["n"] += 1
        if flow_pairs:
            w(f"#### f. Side-by-side text comparison (one pair per DB↔NEW flow)")
            w(f"")
            for (dbc, newc), info in sorted(flow_pairs.items(),
                                            key=lambda x: (-x[1]["n"], x[0])):
                w(f"##### `{dbc}` → `{newc}` ({info['n']} verses)")
                w(f"")
                db_d = (info["db_description"] or "_(no DB description)_").strip()
                new_t = info.get("new_title") or ""
                new_d = (info["new_description"] or "_(no new description)_").strip()
                w(f"- **DB**: {db_d}")
                w(f"- **NEW** ({new_t}): {new_d}")
                w(f"- _Sample verse:_ {info['sample_ref']} ({info['sample_strongs']})")
                w(f"")
        w(f"---")
        w(f"")

    # 4. Global anomalies
    w(f"## 4. Global anomalies")
    w(f"")
    # Multi-candidate
    multi = [v for v in verses
             if v.get("new_vcg", {}).get("candidates_seen", 0) > 1]
    w(f"### 4.1 Multi-candidate new_vcg matches ({len(multi)})")
    w(f"")
    w(f"_Verse appeared in >1 v2 file with different new_vcg codes — likely a sub-group membership disagreement._")
    w(f"")
    if multi:
        w(f"| Reference | Strongs | Chosen new_vcg | DB VCG | Match type |")
        w(f"|---|---|---|---|---|")
        for v in multi[:100]:
            t = v["term"]
            new_code = v["new_vcg"]["code"]
            db_code = (v.get("current") or {}).get("group_code") or "(none)"
            mt = v["new_vcg"].get("match_type", "?")
            w(f"| {v['reference']} | {t['strongs']} {t['translit']} | "
              f"`{new_code}` | `{db_code}` | {mt} |")
        if len(multi) > 100:
            w(f"\n_({len(multi) - 100} more not shown)_\n")
    w(f"")

    # Fallback subgroup
    fb = [v for v in verses
          if v.get("new_vcg", {}).get("match_type") == "subgroup_fallback"]
    w(f"### 4.2 Sub-group fallback matches ({len(fb)})")
    w(f"")
    w(f"_Verse's current sub-group did not contain this reference in v2; matched via another sub-group's v2 file. Strong signal that current DB sub-group assignment may be wrong._")
    w(f"")
    if fb:
        w(f"| Reference | Strongs | Current sg | new_vcg sg | new_vcg code |")
        w(f"|---|---|---|---|---|")
        for v in fb[:100]:
            t = v["term"]
            cur_sg = (v.get("current") or {}).get("subgroup_code") or "?"
            nv = v["new_vcg"]
            w(f"| {v['reference']} | {t['strongs']} {t['translit']} | "
              f"`{cur_sg}` | `M15-{nv['source_subgroup'].upper()}` | `{nv['code']}` |")
        if len(fb) > 100:
            w(f"\n_({len(fb) - 100} more not shown)_\n")
    w(f"")

    # Duplicate vc rows
    dup_ids = md.get("duplicate_vr_ids", [])
    if dup_ids:
        w(f"### 4.3 Duplicate active verse_context rows ({len(dup_ids)} vr_ids)")
        w(f"")
        w(f"_These vr_ids each have 2 active vc rows in the DB — must be resolved before any sub-group cleanup._")
        w(f"")
        w(f"| vr_id | Reference | Strongs | Sub-group | DB VCGs (two of them) |")
        w(f"|---|---|---|---|---|")
        for dup_id in dup_ids:
            entries = [v for v in verses if v["vr_id"] == dup_id]
            if not entries:
                continue
            v = entries[0]
            db_codes = ", ".join(sorted({
                (e.get("current") or {}).get("group_code") or "(none)"
                for e in entries
            }))
            w(f"| {dup_id} | {v['reference']} | "
              f"{v['term']['strongs']} {v['term']['translit']} | "
              f"`{(v.get('current') or {}).get('subgroup_code')}` | "
              f"{db_codes} |")
        w(f"")

    text = "\n".join(out) + "\n"
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Written: {OUT_PATH}")
    print(f"  size: {os.path.getsize(OUT_PATH):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
