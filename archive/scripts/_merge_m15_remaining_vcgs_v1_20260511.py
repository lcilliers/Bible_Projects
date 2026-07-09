"""_merge_m15_remaining_vcgs_v1_20260511.py — read+write JSON.

Process the 6 remaining M15 sub-group VCG files in sequence, chaining the
main baseline from v11 → v17 and emitting a DB-staging JSON per sub-group.

Order: D → E → F → G → H → BOUNDARY.

For each: parses VCGs + anchors + SETASIDE block (where present); updates
main baseline new_vcg / proposed_set_aside fields; emits DB staging at
m15-vcg-db-staging-<CODE>-v1-20260511.json.

M15-H is a new sub-group not yet in cluster_subgroup; the merge records
its label/description in the staging metadata so the apply can create it.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
SRC_DIR = os.path.join(M15_DIR, "files json vcg")

# (sub-group code, source file basename, output baseline version)
SEQUENCE = [
    ("M15-D",        "wa-m15d-vcg-groups-v1-20260511.json",          "v12"),
    ("M15-E",        "wa-m15e-vcg-groups-v1-20260511.json",          "v13"),
    ("M15-F",        "wa-m15f-vcg-groups-v1-20260511.json",          "v14"),
    ("M15-G",        "wa-m15g-vcg-groups-v1-20260511.json",          "v15"),
    ("M15-H",        "wa-m15h-vcg-groups-v1-20260511.json",          "v16"),
    ("M15-BOUNDARY", "wa-m15-boundary-vcg-groups-v1-20260511.json",  "v17"),
]
# In the JSON metadata the BOUNDARY file uses "BOUNDARY" as subgroup_code
# (not "M15-BOUNDARY"). DB uses subgroup_code='BOUNDARY' for M15's
# boundary. Map both.
EFFECTIVE_SG_NAME = {"M15-BOUNDARY": "BOUNDARY"}
# VCG code prefix used in each file
VCG_PREFIX = {
    "M15-D": "M15-D-VCG", "M15-E": "M15-E-VCG", "M15-F": "M15-F-VCG",
    "M15-G": "M15-G-VCG", "M15-H": "M15-H-VCG",
    "M15-BOUNDARY": "M15-BOUNDARY-VCG",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def process_one(main, sg_code, src_basename, out_version):
    src_path = os.path.join(SRC_DIR, src_basename)
    eff_sg = EFFECTIVE_SG_NAME.get(sg_code, sg_code)
    vcg_prefix = VCG_PREFIX[sg_code]

    with open(src_path, "r", encoding="utf-8") as f:
        vin = json.load(f)
    md = vin["metadata"]
    print(f"\n--- {sg_code}  (file: {src_basename}, → main {out_version}) ---")
    print(f"  total_in_sg={md.get('total_verses_in_subgroup')}, "
          f"vcgs={md.get('vcg_count')}, in_vcgs={md.get('total_verses_in_vcgs')}, "
          f"setasides={md.get('setaside_count')}, "
          f"reroutes={md.get('reroute_count', 0)}")

    # Build assignment lookup
    by_vr: dict[int, dict] = {}
    vcg_meta: dict[str, dict] = {}
    for grp in vin["verse_context_groups"]:
        code = grp["code"]
        verses = grp.get("verses", [])
        for v in verses:
            by_vr[v["vr_id"]] = {
                "category": (
                    "vcg" if code.startswith(vcg_prefix) else
                    "setaside" if code == "SETASIDE" else
                    "reroute" if code.startswith("REROUTE-") else
                    "other"
                ),
                "code": code,
                "label": grp.get("label"),
                "context_description": grp.get("context_description"),
                "assignment_note": v.get("assignment_note"),
            }
        anchor = grp.get("anchor_verse")
        if anchor:
            avid = anchor.get("vr_id")
            if avid is not None and avid not in by_vr:
                by_vr[avid] = {
                    "category": "vcg" if code.startswith(vcg_prefix)
                                 else "setaside",
                    "code": code,
                    "label": grp.get("label"),
                    "context_description": grp.get("context_description"),
                    "assignment_note": anchor.get("anchor_rationale"),
                }
        vcg_meta[code] = {
            "code": code,
            "label": grp.get("label"),
            "context_description": grp.get("context_description"),
            "verse_count_in_input": len(verses),
            "anchor": anchor,
        }

    # Effective sub-group filter
    effective_sg = [
        v for v in main["verses"]
        if (((v.get("new_subgroup") or {}).get("code") == eff_sg)
            or ((v.get("current") or {}).get("subgroup_code") == eff_sg
                and not (v.get("new_subgroup") or {}).get("code")))
    ]
    # M15-H is a sub-group not yet in cluster_subgroup; verses with
    # new_subgroup.code = "M15-H" set earlier come through.
    print(f"  Main baseline effective {eff_sg} verses: {len(effective_sg)}")

    counters = Counter()
    unmatched = []
    anchor_count = 0
    for v in effective_sg:
        a = by_vr.get(v["vr_id"])
        v.pop("vcg_comparison", None)
        v.pop("review_flags", None)
        if not a:
            unmatched.append(v["vr_id"])
            continue
        cat = a["category"]
        counters[cat] += 1
        if cat == "vcg":
            v["new_vcg"] = {
                "code": a["code"],
                "label": a["label"],
                "context_description": a["context_description"],
                "assignment_note": a.get("assignment_note"),
                "source_file": src_basename,
                "source_version": f"{sg_code}-vcg-groups-v1",
                "is_anchor": False,
            }
            v.pop("proposed_set_aside", None)
        elif cat == "setaside":
            v.pop("new_vcg", None)
            v["proposed_set_aside"] = {
                "reason": "no_inner_being_phenomenon",
                "context_description": a.get("context_description"),
                "assignment_note": a.get("assignment_note"),
                "source_file": src_basename,
            }

    # Mark anchors
    for code, m in vcg_meta.items():
        a = m.get("anchor")
        if not a:
            continue
        avid = a.get("vr_id")
        target = next((v for v in main["verses"] if v["vr_id"] == avid), None)
        if target and (target.get("new_vcg") or {}).get("code") == code:
            target["new_vcg"]["is_anchor"] = True
            target["new_vcg"]["anchor_rationale"] = a.get("anchor_rationale")
            anchor_count += 1

    print(f"  VCG: {counters['vcg']}  SA: {counters['setaside']}  "
          f"RR: {counters['reroute']}  anchors: {anchor_count}  "
          f"unmatched: {len(unmatched)}")

    # Build DB staging
    vcg_blocks = []
    for code, m in vcg_meta.items():
        if not code.startswith(vcg_prefix):
            continue
        verses_in = []
        for vid, a in by_vr.items():
            if a["code"] != code:
                continue
            v = next((vv for vv in main["verses"] if vv["vr_id"] == vid), None)
            if not v:
                continue
            verses_in.append({
                "vr_id": vid,
                "reference": v["reference"],
                "strongs": v["term"]["strongs"],
                "mti_term_id": v["term"]["mti_id"],
                "assignment_note": a.get("assignment_note"),
            })
        mti_term_ids = sorted({v["mti_term_id"] for v in verses_in
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
            "cluster_subgroup_code": eff_sg,
            "mti_term_ids": mti_term_ids,
            "verse_count": len(verses_in),
            "verses": verses_in,
            "anchor_proposed": anchor_proposed,
        })

    sa_verses = []
    for vid, a in by_vr.items():
        if a["category"] != "setaside":
            continue
        v = next((vv for vv in main["verses"] if vv["vr_id"] == vid), None)
        if not v:
            continue
        sa_verses.append({
            "vr_id": vid,
            "reference": v["reference"],
            "strongs": v["term"]["strongs"],
            "mti_term_id": v["term"]["mti_id"],
            "assignment_note": a.get("assignment_note"),
        })
    setaside_block = {
        "reason_code": "no_inner_being_phenomenon",
        "context_description": vcg_meta.get("SETASIDE", {}).get(
            "context_description"),
        "verse_count": len(sa_verses),
        "verses": sa_verses,
    }

    # Sub-group creation flag for M15-H
    needs_sg_create = (sg_code == "M15-H")
    sg_create_info = None
    if needs_sg_create:
        sg_create_info = {
            "code": "M15-H",
            "label": md.get("subgroup_label"),
            "description": md.get("subgroup_description"),
            "cluster_code": "M15",
        }

    staging = {
        "metadata": {
            "cluster_code": "M15",
            "cluster_subgroup_code": eff_sg,
            "source_input": src_basename,
            "generated_at": now_iso(),
            "purpose": f"DB-load staging for {sg_code} VCG cleanup.",
            "needs_subgroup_creation": needs_sg_create,
            "subgroup_to_create": sg_create_info,
            "totals": {
                "vcgs_to_create": len(vcg_blocks),
                "verses_to_assign_to_vcgs": sum(b["verse_count"] for b in vcg_blocks),
                "verses_to_set_aside": setaside_block["verse_count"],
                "sum_check": (sum(b["verse_count"] for b in vcg_blocks)
                              + setaside_block["verse_count"]),
            },
            "anchor_status": (
                f"{sum(1 for b in vcg_blocks if b['anchor_proposed'])}/"
                f"{len(vcg_blocks)} VCGs have anchor_proposed."
            ),
        },
        "vcg_creations": vcg_blocks,
        "setasides": setaside_block,
        "reroutes": {"target_subgroup_code": None, "verse_count": 0, "verses": []},
    }
    sg_key = sg_code if sg_code != "M15-BOUNDARY" else "BOUNDARY"
    staging_path = os.path.join(
        M15_DIR, f"m15-vcg-db-staging-{sg_key}-v1-20260511.json")
    with open(staging_path, "w", encoding="utf-8") as f:
        json.dump(staging, f, ensure_ascii=False, indent=2)
    print(f"  staging written: {staging_path}")
    return counters, len(unmatched)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # Start with v11 (post-M15-C)
    in_path = os.path.join(M15_DIR, "m15-baseline-verses-v11-20260511.json")
    with open(in_path, "r", encoding="utf-8") as f:
        main = json.load(f)

    grand_counters = Counter()
    grand_unmatched = 0
    for sg_code, src_basename, out_version in SEQUENCE:
        cs, um = process_one(main, sg_code, src_basename, out_version)
        for k, v in cs.items():
            grand_counters[k] += v
        grand_unmatched += um

    # Recompute review_status across the board
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

    # Final write — v17
    out_path = os.path.join(M15_DIR, "m15-baseline-verses-v17-20260511.json")
    main["metadata"]["schema_version"] = "baseline-v17"
    main["metadata"]["generated_at"] = now_iso()
    main["metadata"]["m15_remaining_subgroups_merge"] = {
        "applied_at": now_iso(),
        "subgroups_processed": [sg for sg, _, _ in SEQUENCE],
        "grand_counters": dict(grand_counters),
        "grand_unmatched": grand_unmatched,
    }
    main["metadata"]["status_workflow"]["default_distribution"] = dict(status_counts)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(main, f, ensure_ascii=False, indent=2)
    print()
    print("=" * 72)
    print(f"Grand totals: {dict(grand_counters)}, unmatched={grand_unmatched}")
    print()
    print("review_status — final distribution:")
    for k, n in status_counts.items():
        print(f"  {k:25s} {n}")
    print()
    print(f"Final main: {out_path}")
    print(f"  size: {os.path.getsize(out_path):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
