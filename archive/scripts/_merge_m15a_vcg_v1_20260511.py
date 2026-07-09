"""_merge_m15a_vcg_v1_20260511.py — read+write JSON.

Load the M15-A VCG assignments from wa-m15a-vcg-v1-20260511.json (10 VCGs +
39 set-asides + 5 reroute-to-M15-E) into the main baseline. Also emit a
separate DB-staging JSON that is directive-ready: VCG creations, verse
assignments, set-aside proposals, reroute proposals.

Reads:
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v7-20260511.json (main)
  - Sessions/Session_Clusters/M15/wa-m15a-vcg-v1-20260511.json (M15-A input)

Writes:
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v8-20260511.json (main)
  - Sessions/Session_Clusters/M15/m15-vcg-db-staging-M15A-v1-20260511.json (db-staging)
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
MAIN_IN = os.path.join(M15_DIR, "m15-baseline-verses-v7-20260511.json")
VCG_IN = os.path.join(M15_DIR, "wa-m15a-vcg-v1-20260511.json")
MAIN_OUT = os.path.join(M15_DIR, "m15-baseline-verses-v8-20260511.json")
DB_STAGING_OUT = os.path.join(M15_DIR,
                              "m15-vcg-db-staging-M15A-v1-20260511.json")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # Load
    with open(MAIN_IN, "r", encoding="utf-8") as f:
        main = json.load(f)
    with open(VCG_IN, "r", encoding="utf-8") as f:
        vcg_input = json.load(f)

    print(f"Main baseline rows: {len(main['verses'])}")
    print(f"VCG input metadata: total={vcg_input['metadata']['total_verses']}, "
          f"vcgs={vcg_input['metadata']['vcg_count']}, "
          f"setasides={vcg_input['metadata']['setaside_count']}, "
          f"reroutes={vcg_input['metadata']['reroute_count']}")

    # Build per-vr_id assignment lookup from the input file
    by_vr: dict[int, dict] = {}
    vcg_meta: dict[str, dict] = {}  # code -> {label, context_description, terms_used}
    for grp in vcg_input["verse_context_groups"]:
        code = grp["code"]
        verses = grp.get("verses", [])
        terms_used: set[str] = set()
        for v in verses:
            terms_used.add(v["strongs"])
            by_vr[v["vr_id"]] = {
                "category": (
                    "vcg" if code.startswith("M15-A-VCG") else
                    "setaside" if code == "SETASIDE" else
                    "reroute" if code.startswith("REROUTE-") else
                    "other"
                ),
                "code": code,
                "label": grp.get("label"),
                "context_description": grp.get("context_description"),
                "assignment_note": v.get("assignment_note"),
            }
        vcg_meta[code] = {
            "code": code,
            "label": grp.get("label"),
            "context_description": grp.get("context_description"),
            "verse_count_in_input": len(verses),
            "terms_used": sorted(terms_used),
        }

    print(f"  Loaded assignments for {len(by_vr)} vr_ids "
          f"across {len(vcg_meta)} groups (VCGs + pseudo-groups)")

    # Sanity: count M15-A verses in main baseline
    main_m15a = [v for v in main["verses"]
                 if (v.get("new_subgroup") or {}).get("code") == "M15-A"
                 or ((v.get("current") or {}).get("subgroup_code") == "M15-A"
                     and not (v.get("new_subgroup") or {}).get("code"))]
    # The input file is anchored on the by-subgroup view (which uses
    # effective_subgroup = new if present else current). Match accordingly.
    effective_m15a = [v for v in main["verses"]
                      if ((v.get("new_subgroup") or {}).get("code")
                          or (v.get("current") or {}).get("subgroup_code")) == "M15-A"]
    print(f"  Main baseline effective M15-A verses: {len(effective_m15a)}")

    # Apply assignments to main
    counters = Counter()
    unmatched_main_vr_ids: list[int] = []
    for v in main["verses"]:
        eff_sg = ((v.get("new_subgroup") or {}).get("code")
                  or (v.get("current") or {}).get("subgroup_code"))
        if eff_sg != "M15-A":
            continue
        assignment = by_vr.get(v["vr_id"])
        if not assignment:
            unmatched_main_vr_ids.append(v["vr_id"])
            continue
        cat = assignment["category"]
        counters[cat] += 1
        # Wipe old new_vcg and related comparison; this is the authoritative
        # VCG layer now.
        v.pop("vcg_comparison", None)
        v.pop("review_flags", None)
        if cat == "vcg":
            v["new_vcg"] = {
                "code": assignment["code"],
                "label": assignment["label"],
                "context_description": assignment["context_description"],
                "assignment_note": assignment["assignment_note"],
                "source_file": "wa-m15a-vcg-v1-20260511.json",
                "source_version": "M15-A-vcg-v1",
            }
            # new_subgroup stays M15-A (unchanged for VCG verses)
            v.pop("proposed_set_aside", None)
        elif cat == "setaside":
            v.pop("new_vcg", None)
            v["proposed_set_aside"] = {
                "reason": "no_inner_being_phenomenon",
                "context_description": assignment["context_description"],
                "assignment_note": assignment["assignment_note"],
                "source_file": "wa-m15a-vcg-v1-20260511.json",
            }
            # Keep new_subgroup as M15-A (the verse is still in the cluster,
            # just not grouped). Note this is a proposal to set the
            # verse_context row's set_aside_reason on apply.
        elif cat == "reroute":
            v.pop("new_vcg", None)
            v.pop("proposed_set_aside", None)
            # Reroute to M15-E. Look up M15-E meta from another row.
            m15e_meta = next(
                (vv.get("new_subgroup") or vv.get("current") or {}
                 for vv in main["verses"]
                 if ((vv.get("new_subgroup") or {}).get("code") == "M15-E"
                     or (vv.get("current") or {}).get("subgroup_code") == "M15-E")),
                {})
            v["new_subgroup"] = {
                "code": "M15-E",
                "label": (m15e_meta.get("subgroup_label") or
                          m15e_meta.get("label")),
                "description": (m15e_meta.get("subgroup_description") or
                                m15e_meta.get("description")),
                "_origin": "manual_reroute_2026-05-11_M15A_input",
                "_prior_new_subgroup_code": "M15-A",
                "_reroute_reason": assignment["context_description"],
                "_reroute_note": assignment["assignment_note"],
            }

    # Recompute review_status (preserve manual 'No change' overrides)
    duplicate_vr_ids = set(main["metadata"].get("duplicate_vr_ids", []))
    status_counts = Counter()
    for v in main["verses"]:
        cur = v.get("current") or {}
        nv = v.get("new_vcg")
        has_meaning = bool((v.get("meaning") or {}).get("text"))
        has_new_vcg = nv is not None
        has_set_aside = "proposed_set_aside" in v
        is_dup_vr = v["vr_id"] in duplicate_vr_ids
        status_now = cur.get("status")
        no_current_group = cur.get("group_id") is None

        if v.get("review_status") == "No change":
            review = "No change"
        elif has_set_aside:
            review = "Ready with changes"  # proposed set-aside is a ready change
        elif (not has_new_vcg and not has_meaning) or is_dup_vr \
                or status_now in ("P", "UT") or no_current_group:
            review = "For research"
        elif has_new_vcg:
            review = "Ready with changes"
        else:
            review = "For research"
        v["review_status"] = review
        status_counts[review] += 1

    # Save main
    main["metadata"]["schema_version"] = "baseline-v8"
    main["metadata"]["generated_at"] = now_iso()
    main["metadata"]["m15a_vcg_merge"] = {
        "source": "Sessions/Session_Clusters/M15/wa-m15a-vcg-v1-20260511.json",
        "applied_at": now_iso(),
        "vcgs_recorded": sum(1 for k in vcg_meta if k.startswith("M15-A-VCG")),
        "verses_assigned_to_vcg": counters["vcg"],
        "verses_proposed_set_aside": counters["setaside"],
        "verses_rerouted_to_M15E": counters["reroute"],
        "main_m15a_unmatched_to_input": len(unmatched_main_vr_ids),
        "main_m15a_unmatched_vr_ids": unmatched_main_vr_ids[:20]
            + (["..."] if len(unmatched_main_vr_ids) > 20 else []),
    }
    main["metadata"]["status_workflow"]["default_distribution"] = dict(status_counts)

    with open(MAIN_OUT, "w", encoding="utf-8") as f:
        json.dump(main, f, ensure_ascii=False, indent=2)
    print()
    print("Merge into main baseline:")
    for k, n in counters.items():
        print(f"  {k:15s} {n}")
    if unmatched_main_vr_ids:
        print(f"  [WARN] main M15-A verses with no input assignment: "
              f"{len(unmatched_main_vr_ids)}")
        print(f"         sample: {unmatched_main_vr_ids[:10]}")
    print()
    print("review_status — new distribution:")
    for k, n in status_counts.items():
        print(f"  {k:25s} {n}")
    print(f"Main written: {MAIN_OUT}")
    print(f"  size: {os.path.getsize(MAIN_OUT):,} bytes")

    # ----- DB staging JSON -----
    print()
    print("Building DB-staging JSON...")

    # Per VCG: list verses + terms_used
    vcg_blocks = []
    for code, m in vcg_meta.items():
        if not code.startswith("M15-A-VCG"):
            continue
        verses_in_vcg = [
            {
                "vr_id": vid,
                "reference": next(
                    (vv["reference"] for vv in main["verses"]
                     if vv["vr_id"] == vid), None),
                "strongs": next(
                    (vv["term"]["strongs"] for vv in main["verses"]
                     if vv["vr_id"] == vid), None),
                "mti_term_id": next(
                    (vv["term"]["mti_id"] for vv in main["verses"]
                     if vv["vr_id"] == vid), None),
                "assignment_note": a["assignment_note"],
            }
            for vid, a in by_vr.items()
            if a["code"] == code
        ]
        # Distinct mti_term_ids in this VCG (for the vcg_term link rows)
        mti_term_ids = sorted({
            v["mti_term_id"] for v in verses_in_vcg
            if v["mti_term_id"] is not None
        })
        vcg_blocks.append({
            "code": code,
            "label": m["label"],
            "context_description": m["context_description"],
            "cluster_subgroup_code": "M15-A",
            "mti_term_ids": mti_term_ids,
            "verse_count": len(verses_in_vcg),
            "verses": verses_in_vcg,
            "anchor_proposed": None,  # not provided in source file
        })

    # Set-aside block
    setaside_block = {
        "reason_code": "no_inner_being_phenomenon",
        "context_description": vcg_meta.get("SETASIDE", {}).get(
            "context_description"),
        "verse_count": vcg_meta.get("SETASIDE", {}).get("verse_count_in_input", 0),
        "verses": [
            {
                "vr_id": vid,
                "reference": next(
                    (vv["reference"] for vv in main["verses"]
                     if vv["vr_id"] == vid), None),
                "strongs": next(
                    (vv["term"]["strongs"] for vv in main["verses"]
                     if vv["vr_id"] == vid), None),
                "mti_term_id": next(
                    (vv["term"]["mti_id"] for vv in main["verses"]
                     if vv["vr_id"] == vid), None),
                "assignment_note": a["assignment_note"],
            }
            for vid, a in by_vr.items()
            if a["code"] == "SETASIDE"
        ],
    }

    # Reroute block
    reroute_block = {
        "target_subgroup_code": "M15-E",
        "context_description": vcg_meta.get("REROUTE-M15-E", {}).get(
            "context_description"),
        "verse_count": vcg_meta.get("REROUTE-M15-E", {}).get("verse_count_in_input", 0),
        "verses": [
            {
                "vr_id": vid,
                "reference": next(
                    (vv["reference"] for vv in main["verses"]
                     if vv["vr_id"] == vid), None),
                "strongs": next(
                    (vv["term"]["strongs"] for vv in main["verses"]
                     if vv["vr_id"] == vid), None),
                "mti_term_id": next(
                    (vv["term"]["mti_id"] for vv in main["verses"]
                     if vv["vr_id"] == vid), None),
                "assignment_note": a["assignment_note"],
            }
            for vid, a in by_vr.items()
            if a["code"] == "REROUTE-M15-E"
        ],
    }

    staging = {
        "metadata": {
            "cluster_code": "M15",
            "cluster_subgroup_code": "M15-A",
            "source_input": "wa-m15a-vcg-v1-20260511.json",
            "generated_at": now_iso(),
            "purpose": (
                "DB-load staging for M15-A VCG cleanup. Three operations "
                "for a future directive: (1) create new VCGs in "
                "verse_context_group + vcg_term link rows; assign verses "
                "via verse_context.group_id. (2) Apply set-aside reason "
                "to verses with no inner-being phenomenon. (3) Re-route "
                "5 verses from M15-A to M15-E by updating "
                "verse_context.cluster_subgroup_id (per-verse override "
                "since the term has verses in both sub-groups)."
            ),
            "totals": {
                "vcgs_to_create": len(vcg_blocks),
                "verses_to_assign_to_vcgs": sum(v["verse_count"] for v in vcg_blocks),
                "verses_to_set_aside": setaside_block["verse_count"],
                "verses_to_reroute": reroute_block["verse_count"],
                "sum_check": (
                    sum(v["verse_count"] for v in vcg_blocks)
                    + setaside_block["verse_count"]
                    + reroute_block["verse_count"]
                ),
            },
            "anchor_status": (
                "Not designated in input. The cluster instruction §9 "
                "requires at least one anchor per VCG. Anchor designation "
                "is a follow-up step before this staging can be turned "
                "into a directive."
            ),
        },
        "vcg_creations": vcg_blocks,
        "setasides": setaside_block,
        "reroutes": reroute_block,
    }

    with open(DB_STAGING_OUT, "w", encoding="utf-8") as f:
        json.dump(staging, f, ensure_ascii=False, indent=2)
    print(f"DB-staging written: {DB_STAGING_OUT}")
    print(f"  size: {os.path.getsize(DB_STAGING_OUT):,} bytes")
    print(f"  vcgs={len(vcg_blocks)}  "
          f"verses_in_vcgs={sum(v['verse_count'] for v in vcg_blocks)}  "
          f"setasides={setaside_block['verse_count']}  "
          f"reroutes={reroute_block['verse_count']}  "
          f"sum={staging['metadata']['totals']['sum_check']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
