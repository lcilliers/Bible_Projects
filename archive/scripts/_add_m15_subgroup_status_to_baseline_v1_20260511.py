"""_add_m15_subgroup_status_to_baseline_v1_20260511.py — read+write JSON.

Layer the cleanup-workflow fields onto the v3 baseline:

  - current.subgroup_label, current.subgroup_description
        (from cluster_subgroup.core_description for the current sg)
  - new_subgroup = { code, label, description }
        (derived from new_vcg.source_subgroup letter, looking up the same
         cluster_subgroup row by 'M15-' + uppercase letter; BOUNDARY
         handled specially)
  - review_status (one of: 'No change' | 'Ready with changes' |
                           'For Review' | 'For research')

Default review_status logic (researcher/AI may override later):
  - 'For research' — no new_vcg AND no meaning; OR duplicate-vr row; OR
                     status in {P, UT}; OR no current group_id
  - 'For Review'  — has new_vcg but with conflict flags:
                     - sub-group fallback match (verse in another sg's v2)
                     - multi-candidate match
                     - verse_annotation present (AI breadcrumb)
                     - meaning vcg_mismatch flag
  - 'Ready with changes' — has new_vcg, subgroup-aligned, no conflict flags
  - 'No change'   — never auto-assigned (manual override only)

Reads:  m15-baseline-verses-v3-20260511.json
Writes: m15-baseline-verses-v4-20260511.json
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
BASELINE_IN = os.path.join(M15_DIR, "m15-baseline-verses-v3-20260511.json")
BASELINE_OUT = os.path.join(M15_DIR, "m15-baseline-verses-v4-20260511.json")
DB_PATH = os.path.join("database", "bible_research.db")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # Sub-group metadata
    print("Loading M15 sub-group metadata...")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    sg_by_code: dict[str, dict] = {}
    for r in conn.execute("""
        SELECT subgroup_code, label, core_description
          FROM cluster_subgroup
         WHERE cluster_code='M15' AND COALESCE(delete_flagged,0)=0
    """):
        sg_by_code[r["subgroup_code"]] = {
            "code": r["subgroup_code"],
            "label": r["label"],
            "description": r["core_description"],
        }
    conn.close()
    print(f"  {len(sg_by_code)} sub-groups loaded")

    # Letter → full code map (from v2 source_subgroup letters)
    letter_to_code = {
        "a": "M15-A", "b": "M15-B", "c": "M15-C", "d": "M15-D",
        "e": "M15-E", "f": "M15-F", "g": "M15-G",
        "boundary": "M15-BOUNDARY",
    }
    # cluster_subgroup uses 'BOUNDARY' not 'M15-BOUNDARY' (per earlier query)
    if "M15-BOUNDARY" not in sg_by_code and "BOUNDARY" in sg_by_code:
        sg_by_code["M15-BOUNDARY"] = sg_by_code["BOUNDARY"]

    print(f"Loading baseline: {BASELINE_IN}")
    with open(BASELINE_IN, "r", encoding="utf-8") as f:
        baseline = json.load(f)
    print(f"  rows: {len(baseline['verses'])}")

    duplicate_vr_ids = set(baseline["metadata"].get("duplicate_vr_ids", []))

    counts = {"No change": 0, "Ready with changes": 0,
              "For Review": 0, "For research": 0}

    for v in baseline["verses"]:
        cur = v.get("current", {}) or {}

        # 1. Current sub-group description
        cur_sg_code = cur.get("subgroup_code")
        cur_sg_meta = sg_by_code.get(cur_sg_code) if cur_sg_code else None
        if cur_sg_meta:
            cur["subgroup_label"] = cur_sg_meta["label"]
            cur["subgroup_description"] = cur_sg_meta["description"]
        else:
            cur["subgroup_label"] = None
            cur["subgroup_description"] = None
        v["current"] = cur

        # 2. New sub-group (from new_vcg.source_subgroup if present)
        new_sg_meta = None
        nv = v.get("new_vcg")
        if nv:
            letter = nv.get("source_subgroup")
            if letter:
                new_sg_code = letter_to_code.get(letter)
                new_sg_meta = sg_by_code.get(new_sg_code)
        if new_sg_meta:
            v["new_subgroup"] = {
                "code": new_sg_meta["code"],
                "label": new_sg_meta["label"],
                "description": new_sg_meta["description"],
            }
        else:
            v["new_subgroup"] = None

        # 3. Compute default review_status
        has_meaning = "meaning" in v
        has_new_vcg = nv is not None
        is_dup_vr = v["vr_id"] in duplicate_vr_ids
        status_now = cur.get("status")
        no_current_group = cur.get("group_id") is None

        if (not has_new_vcg and not has_meaning) or is_dup_vr \
                or status_now in ("P", "UT") or no_current_group:
            review = "For research"
        elif has_new_vcg:
            flags = []
            if nv.get("match_type") == "subgroup_fallback":
                flags.append("subgroup_fallback")
            if nv.get("candidates_seen", 0) > 1:
                flags.append("multi_candidate")
            if nv.get("verse_annotation"):
                flags.append("ai_annotation")
            if v.get("meaning", {}).get("vcg_mismatch"):
                flags.append("meaning_vcg_mismatch")
            if flags:
                review = "For Review"
                v["review_flags"] = flags
            else:
                review = "Ready with changes"
        else:
            # has_meaning but no new_vcg
            review = "For research"

        v["review_status"] = review
        counts[review] += 1

    # Update metadata
    baseline["metadata"]["schema_version"] = "baseline-v4"
    baseline["metadata"]["generated_at"] = now_iso()
    baseline["metadata"]["status_workflow"] = {
        "values": ["No change", "Ready with changes", "For Review", "For research"],
        "default_distribution": counts,
        "notes": (
            "Auto-assigned defaults: 'No change' is never auto-assigned "
            "(manual override only — set when researcher/AI confirms the "
            "verse is correctly placed with no edits needed). "
            "'Ready with changes' = has new_vcg, sub-group-aligned, no "
            "conflict flags. 'For Review' = has new_vcg but carries flags "
            "(subgroup_fallback / multi_candidate / ai_annotation / "
            "meaning_vcg_mismatch). 'For research' = missing new_vcg or "
            "meaning, or duplicate vr_id, or status P/UT, or no current "
            "group_id."
        ),
    }

    with open(BASELINE_OUT, "w", encoding="utf-8") as f:
        json.dump(baseline, f, ensure_ascii=False, indent=2)
    print()
    print("Default review_status distribution:")
    for k, v in counts.items():
        print(f"  {k:25s} {v}")
    print(f"  written: {BASELINE_OUT}")
    print(f"  size: {os.path.getsize(BASELINE_OUT):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
