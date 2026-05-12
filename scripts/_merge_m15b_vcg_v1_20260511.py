"""_merge_m15b_vcg_v1_20260511.py — read+write JSON.

Load M15-B VCG assignments from wa-m15b-vcg-groups-v1-20260511.json:
  - 7 VCGs (M15-B-VCG01..07) with anchors already inline
  - 307 verses assigned to VCGs
  - 7 verses NOT in the file (derived as set-aside by exclusion)
  - 0 reroutes

Merge into main baseline (v9 → v10) and emit DB-staging JSON for M15-B.

Reads:
  - m15-baseline-verses-v9-20260511.json
  - wa-m15b-vcg-groups-v1-20260511.json

Writes:
  - m15-baseline-verses-v10-20260511.json
  - m15-vcg-db-staging-M15B-v1-20260511.json
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
MAIN_IN = os.path.join(M15_DIR, "m15-baseline-verses-v9-20260511.json")
VCG_IN = os.path.join(M15_DIR, "wa-m15b-vcg-groups-v1-20260511.json")
MAIN_OUT = os.path.join(M15_DIR, "m15-baseline-verses-v10-20260511.json")
STAGING_OUT = os.path.join(M15_DIR,
                           "m15-vcg-db-staging-M15B-v1-20260511.json")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    with open(MAIN_IN, "r", encoding="utf-8") as f:
        main = json.load(f)
    with open(VCG_IN, "r", encoding="utf-8") as f:
        vcg_input = json.load(f)

    md_in = vcg_input["metadata"]
    print(f"Main baseline rows: {len(main['verses'])}")
    print(f"M15-B VCG input: total_in_subgroup={md_in['total_verses_in_subgroup']}, "
          f"vcgs={md_in['vcg_count']}, in_vcgs={md_in['total_verses_in_vcgs']}, "
          f"setasides={md_in['setaside_count']}")

    # Build per-vr_id assignment lookup from the input file (VCGs only)
    by_vr: dict[int, dict] = {}
    vcg_meta: dict[str, dict] = {}
    for grp in vcg_input["verse_context_groups"]:
        code = grp["code"]
        verses = grp.get("verses", [])
        terms_used: set[str] = set()
        for v in verses:
            terms_used.add(v["strongs"])
            by_vr[v["vr_id"]] = {
                "code": code,
                "label": grp.get("label"),
                "context_description": grp.get("context_description"),
                "assignment_note": v.get("assignment_note"),
            }
        anchor = grp.get("anchor_verse")
        vcg_meta[code] = {
            "code": code,
            "label": grp.get("label"),
            "context_description": grp.get("context_description"),
            "verse_count_in_input": len(verses),
            "terms_used": sorted(terms_used),
            "anchor": anchor,
        }
        if anchor:
            # Add the anchor's vr_id if not already in verses list (some
            # formats list the anchor separately from the verses array).
            avid = anchor.get("vr_id")
            if avid is not None and avid not in by_vr:
                by_vr[avid] = {
                    "code": code,
                    "label": grp.get("label"),
                    "context_description": grp.get("context_description"),
                    "assignment_note": anchor.get("anchor_rationale"),
                }

    print(f"  Loaded {len(by_vr)} vr_id assignments across {len(vcg_meta)} VCGs")

    # Identify all M15-B verses in main baseline (effective sub-group)
    m15b_verses = [
        v for v in main["verses"]
        if (((v.get("new_subgroup") or {}).get("code") == "M15-B")
            or ((v.get("current") or {}).get("subgroup_code") == "M15-B"
                and not (v.get("new_subgroup") or {}).get("code")))
    ]
    print(f"  Main baseline effective M15-B verses: {len(m15b_verses)}")

    # Apply assignments
    counters = Counter()
    setaside_vrs: list[dict] = []
    unmatched: list[int] = []
    for v in m15b_verses:
        a = by_vr.get(v["vr_id"])
        # Wipe old new_vcg context to keep new state authoritative
        v.pop("vcg_comparison", None)
        v.pop("review_flags", None)
        if a:
            counters["vcg"] += 1
            v["new_vcg"] = {
                "code": a["code"],
                "label": a["label"],
                "context_description": a["context_description"],
                "assignment_note": a.get("assignment_note"),
                "source_file": "wa-m15b-vcg-groups-v1-20260511.json",
                "source_version": "M15-B-vcg-groups-v1",
                "is_anchor": False,  # filled below
            }
            v.pop("proposed_set_aside", None)
        else:
            # Not in any VCG → set-aside by exclusion
            counters["setaside"] += 1
            setaside_vrs.append({
                "vr_id": v["vr_id"],
                "reference": v["reference"],
                "strongs": v["term"]["strongs"],
                "translit": v["term"]["translit"],
                "mti_term_id": v["term"]["mti_id"],
                "verse_text": v.get("verse_text"),
                "meaning": (v.get("meaning") or {}).get("text"),
                "assignment_note": "Set aside (derived by exclusion from M15-B-VCG01..07)",
            })
            v.pop("new_vcg", None)
            v["proposed_set_aside"] = {
                "reason": "no_inner_being_phenomenon",
                "context_description": (
                    "M15-B verse not assigned to any of the 7 derived VCGs; "
                    "set aside by exclusion. Per-verse rationale not "
                    "provided in source file."
                ),
                "assignment_note": "Derived by exclusion from M15-B-VCG01..07",
                "source_file": "wa-m15b-vcg-groups-v1-20260511.json",
                "_derivation": "verses_not_in_any_vcg",
            }

    # Mark anchors
    anchor_count = 0
    for code, m in vcg_meta.items():
        a = m.get("anchor")
        if not a:
            continue
        avid = a.get("vr_id")
        v = next((v for v in main["verses"] if v["vr_id"] == avid), None)
        if v and (v.get("new_vcg") or {}).get("code") == code:
            v["new_vcg"]["is_anchor"] = True
            v["new_vcg"]["anchor_rationale"] = a.get("anchor_rationale")
            anchor_count += 1

    # Recompute review_status
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
            review = "Ready with changes"
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
    main["metadata"]["schema_version"] = "baseline-v10"
    main["metadata"]["generated_at"] = now_iso()
    main["metadata"]["m15b_vcg_merge"] = {
        "source": "Sessions/Session_Clusters/M15/wa-m15b-vcg-groups-v1-20260511.json",
        "applied_at": now_iso(),
        "vcgs_recorded": len(vcg_meta),
        "anchors_marked": anchor_count,
        "verses_assigned_to_vcg": counters["vcg"],
        "verses_proposed_set_aside": counters["setaside"],
        "setaside_derivation": "by_exclusion_from_VCGs",
    }
    main["metadata"]["status_workflow"]["default_distribution"] = dict(status_counts)

    with open(MAIN_OUT, "w", encoding="utf-8") as f:
        json.dump(main, f, ensure_ascii=False, indent=2)
    print()
    print("Merge into main:")
    print(f"  VCG assignments: {counters['vcg']}")
    print(f"  Set-aside (derived): {counters['setaside']}")
    print(f"  Anchors marked: {anchor_count}/{len(vcg_meta)}")
    print()
    print("review_status — new distribution:")
    for k, n in status_counts.items():
        print(f"  {k:25s} {n}")
    print(f"Main written: {MAIN_OUT}")
    print(f"  size: {os.path.getsize(MAIN_OUT):,} bytes")

    # ----- DB staging -----
    print()
    print("Building DB-staging JSON...")
    vcg_blocks = []
    for code, m in vcg_meta.items():
        if not code.startswith("M15-B-VCG"):
            continue
        verses_in_vcg = []
        for vid, a in by_vr.items():
            if a["code"] != code:
                continue
            v = next((v for v in main["verses"] if v["vr_id"] == vid), None)
            if not v:
                continue
            verses_in_vcg.append({
                "vr_id": vid,
                "reference": v["reference"],
                "strongs": v["term"]["strongs"],
                "mti_term_id": v["term"]["mti_id"],
                "assignment_note": a.get("assignment_note"),
            })
        mti_term_ids = sorted({v["mti_term_id"] for v in verses_in_vcg
                               if v["mti_term_id"] is not None})
        anchor = m.get("anchor")
        anchor_proposed = None
        if anchor:
            anchor_proposed = {
                "vr_id": anchor.get("vr_id"),
                "reference": anchor.get("reference"),
                "strongs": anchor.get("strongs"),
                "translit": anchor.get("translit"),
                "anchor_rationale": anchor.get("anchor_rationale"),
            }
        vcg_blocks.append({
            "code": code,
            "label": m["label"],
            "context_description": m["context_description"],
            "cluster_subgroup_code": "M15-B",
            "mti_term_ids": mti_term_ids,
            "verse_count": len(verses_in_vcg),
            "verses": verses_in_vcg,
            "anchor_proposed": anchor_proposed,
        })

    setaside_block = {
        "reason_code": "no_inner_being_phenomenon",
        "context_description": (
            "M15-B verses not assigned to any of the 7 VCGs in "
            "wa-m15b-vcg-groups-v1-20260511.json. Set aside by exclusion; "
            "per-verse rationale not provided in source file."
        ),
        "verse_count": len(setaside_vrs),
        "verses": setaside_vrs,
        "_derivation_note": (
            "Source file omits the set-aside list (only 7 VCGs published). "
            "Derived by exclusion from the M15-B effective verse set."
        ),
    }
    reroute_block = {
        "target_subgroup_code": None,
        "verse_count": 0,
        "verses": [],
    }

    staging = {
        "metadata": {
            "cluster_code": "M15",
            "cluster_subgroup_code": "M15-B",
            "source_input": "wa-m15b-vcg-groups-v1-20260511.json",
            "generated_at": now_iso(),
            "purpose": (
                "DB-load staging for M15-B VCG cleanup. Two operations "
                "for a future directive: (1) create 7 new VCGs in "
                "verse_context_group + vcg_term link rows; assign 307 "
                "verses via verse_context.group_id; mark 7 anchors. "
                "(2) Apply set-aside reason to 7 verses derived by "
                "exclusion. No reroutes for M15-B."
            ),
            "totals": {
                "vcgs_to_create": len(vcg_blocks),
                "verses_to_assign_to_vcgs": sum(b["verse_count"] for b in vcg_blocks),
                "verses_to_set_aside": setaside_block["verse_count"],
                "verses_to_reroute": 0,
                "sum_check": (
                    sum(b["verse_count"] for b in vcg_blocks)
                    + setaside_block["verse_count"]
                ),
            },
            "anchor_status": (
                f"Designated. {sum(1 for b in vcg_blocks if b['anchor_proposed'])}/"
                f"{len(vcg_blocks)} VCGs have anchor_proposed."
            ),
        },
        "vcg_creations": vcg_blocks,
        "setasides": setaside_block,
        "reroutes": reroute_block,
    }

    with open(STAGING_OUT, "w", encoding="utf-8") as f:
        json.dump(staging, f, ensure_ascii=False, indent=2)
    print(f"DB-staging written: {STAGING_OUT}")
    print(f"  size: {os.path.getsize(STAGING_OUT):,} bytes")
    print(f"  vcgs={len(vcg_blocks)}  "
          f"verses_in_vcgs={sum(b['verse_count'] for b in vcg_blocks)}  "
          f"setasides={setaside_block['verse_count']}  "
          f"sum={staging['metadata']['totals']['sum_check']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
