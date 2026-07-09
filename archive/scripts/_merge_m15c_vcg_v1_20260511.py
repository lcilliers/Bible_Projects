"""_merge_m15c_vcg_v1_20260511.py — read+write JSON.

Load M15-C VCG assignments from wa-m15c-vcg-groups-v1-20260511.json:
  - 12 VCGs (M15-C-VCG01..12) with anchors inline
  - 572 verses assigned to VCGs
  - 4 set-asides (explicit SETASIDE block)
  - 0 reroutes

Merge into main baseline (v10 → v11) + emit DB-staging JSON.

Generic across the input shape (handles explicit SETASIDE and REROUTE-*
pseudo-groups when present; derives set-asides by exclusion only when
the file is silent — not the case here).
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
MAIN_IN = os.path.join(M15_DIR, "m15-baseline-verses-v10-20260511.json")
VCG_IN = os.path.join(M15_DIR, "wa-m15c-vcg-groups-v1-20260511.json")
MAIN_OUT = os.path.join(M15_DIR, "m15-baseline-verses-v11-20260511.json")
STAGING_OUT = os.path.join(M15_DIR,
                           "m15-vcg-db-staging-M15C-v1-20260511.json")
SUBGROUP_CODE = "M15-C"
SOURCE_FILE_BASENAME = "wa-m15c-vcg-groups-v1-20260511.json"


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
    print(f"{SUBGROUP_CODE} VCG input: "
          f"total_in_sg={md_in.get('total_verses_in_subgroup')}, "
          f"vcgs={md_in.get('vcg_count')}, "
          f"in_vcgs={md_in.get('total_verses_in_vcgs')}, "
          f"setasides={md_in.get('setaside_count')}, "
          f"reroutes={md_in.get('reroute_count', 0)}")

    # Per-vr_id assignment lookup
    by_vr: dict[int, dict] = {}
    vcg_meta: dict[str, dict] = {}
    for grp in vcg_input["verse_context_groups"]:
        code = grp["code"]
        verses = grp.get("verses", [])
        terms_used: set[str] = set()
        for v in verses:
            terms_used.add(v["strongs"])
            by_vr[v["vr_id"]] = {
                "category": (
                    "vcg" if code.startswith(f"{SUBGROUP_CODE}-VCG") else
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
                    "category": "vcg",
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
            "terms_used": sorted(terms_used),
            "anchor": anchor,
        }
    print(f"  Loaded {len(by_vr)} vr_id assignments across {len(vcg_meta)} groups")

    # Effective sub-group filter
    effective_sg = [
        v for v in main["verses"]
        if (((v.get("new_subgroup") or {}).get("code") == SUBGROUP_CODE)
            or ((v.get("current") or {}).get("subgroup_code") == SUBGROUP_CODE
                and not (v.get("new_subgroup") or {}).get("code")))
    ]
    print(f"  Main baseline effective {SUBGROUP_CODE} verses: {len(effective_sg)}")

    # Find M15-E target meta for any potential reroutes
    target_sg_meta: dict[str, dict] = {}
    # Apply
    counters = Counter()
    unmatched_vr: list[int] = []
    anchor_count = 0
    for v in effective_sg:
        a = by_vr.get(v["vr_id"])
        v.pop("vcg_comparison", None)
        v.pop("review_flags", None)
        if not a:
            unmatched_vr.append(v["vr_id"])
            continue
        cat = a["category"]
        counters[cat] += 1
        if cat == "vcg":
            v["new_vcg"] = {
                "code": a["code"],
                "label": a["label"],
                "context_description": a["context_description"],
                "assignment_note": a.get("assignment_note"),
                "source_file": SOURCE_FILE_BASENAME,
                "source_version": f"{SUBGROUP_CODE}-vcg-groups-v1",
                "is_anchor": False,
            }
            v.pop("proposed_set_aside", None)
        elif cat == "setaside":
            v.pop("new_vcg", None)
            v["proposed_set_aside"] = {
                "reason": "no_inner_being_phenomenon",
                "context_description": a.get("context_description"),
                "assignment_note": a.get("assignment_note"),
                "source_file": SOURCE_FILE_BASENAME,
            }
        elif cat == "reroute":
            target = a["code"].replace("REROUTE-", "")
            if target not in target_sg_meta:
                target_sg_meta[target] = next(
                    (vv.get("new_subgroup") or vv.get("current") or {}
                     for vv in main["verses"]
                     if ((vv.get("new_subgroup") or {}).get("code") == target
                         or (vv.get("current") or {}).get("subgroup_code") == target)),
                    {})
            tm = target_sg_meta[target]
            v.pop("new_vcg", None)
            v.pop("proposed_set_aside", None)
            v["new_subgroup"] = {
                "code": target,
                "label": tm.get("subgroup_label") or tm.get("label"),
                "description": tm.get("subgroup_description") or tm.get("description"),
                "_origin": f"manual_reroute_2026-05-11_{SUBGROUP_CODE}_input",
                "_prior_new_subgroup_code": SUBGROUP_CODE,
                "_reroute_reason": a.get("context_description"),
                "_reroute_note": a.get("assignment_note"),
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
    main["metadata"]["schema_version"] = "baseline-v11"
    main["metadata"]["generated_at"] = now_iso()
    main["metadata"][f"{SUBGROUP_CODE.lower().replace('-','_')}_vcg_merge"] = {
        "source": f"Sessions/Session_Clusters/M15/{SOURCE_FILE_BASENAME}",
        "applied_at": now_iso(),
        "vcgs_recorded": sum(1 for k in vcg_meta if k.startswith(f"{SUBGROUP_CODE}-VCG")),
        "anchors_marked": anchor_count,
        "verses_assigned_to_vcg": counters["vcg"],
        "verses_proposed_set_aside": counters["setaside"],
        "verses_rerouted": counters["reroute"],
        "verses_unmatched": len(unmatched_vr),
        "unmatched_sample": unmatched_vr[:20] + (["..."] if len(unmatched_vr) > 20 else []),
    }
    main["metadata"]["status_workflow"]["default_distribution"] = dict(status_counts)
    with open(MAIN_OUT, "w", encoding="utf-8") as f:
        json.dump(main, f, ensure_ascii=False, indent=2)
    print()
    print(f"Merge into main:")
    print(f"  VCG assignments:   {counters['vcg']}")
    print(f"  Set-aside:         {counters['setaside']}")
    print(f"  Reroutes:          {counters['reroute']}")
    print(f"  Anchors marked:    {anchor_count}/"
          f"{sum(1 for k in vcg_meta if k.startswith(f'{SUBGROUP_CODE}-VCG'))}")
    if unmatched_vr:
        print(f"  [WARN] unmatched vr_ids in effective sg: {len(unmatched_vr)}")
        print(f"         sample: {unmatched_vr[:10]}")
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
        if not code.startswith(f"{SUBGROUP_CODE}-VCG"):
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
            "cluster_subgroup_code": SUBGROUP_CODE,
            "mti_term_ids": mti_term_ids,
            "verse_count": len(verses_in),
            "verses": verses_in,
            "anchor_proposed": anchor_proposed,
        })

    # SETASIDE — collect from by_vr where category=='setaside'
    sa_verses = []
    sa_context = vcg_meta.get("SETASIDE", {}).get("context_description")
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
        "context_description": sa_context,
        "verse_count": len(sa_verses),
        "verses": sa_verses,
    }
    # No reroutes for M15-C
    reroute_block = {
        "target_subgroup_code": None,
        "verse_count": 0,
        "verses": [],
    }

    staging = {
        "metadata": {
            "cluster_code": "M15",
            "cluster_subgroup_code": SUBGROUP_CODE,
            "source_input": SOURCE_FILE_BASENAME,
            "generated_at": now_iso(),
            "purpose": (
                f"DB-load staging for {SUBGROUP_CODE} VCG cleanup. Two "
                "operations: (1) create new VCGs + assign verses + mark "
                "anchors; (2) set-aside verses with the file's "
                "no_inner_being_phenomenon reason."
            ),
            "totals": {
                "vcgs_to_create": len(vcg_blocks),
                "verses_to_assign_to_vcgs": sum(v["verse_count"] for v in vcg_blocks),
                "verses_to_set_aside": setaside_block["verse_count"],
                "verses_to_reroute": 0,
                "sum_check": (
                    sum(v["verse_count"] for v in vcg_blocks)
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
    print(f"  vcgs={len(vcg_blocks)} "
          f"verses_in_vcgs={sum(b['verse_count'] for b in vcg_blocks)} "
          f"setasides={setaside_block['verse_count']} "
          f"sum={staging['metadata']['totals']['sum_check']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
