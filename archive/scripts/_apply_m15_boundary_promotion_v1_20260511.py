"""_apply_m15_boundary_promotion_v1_20260511.py — read+write JSON only.

Bulk-update rule: for verses currently in BOUNDARY whose new_vcg has a
sub-group-letter prefix (VCG-A-NN .. VCG-G-NN), set new_subgroup to
M15-<letter>. Pulls the canonical label + description from
cluster_subgroup so the new_subgroup block stays in sync.

Reads:  m15-baseline-verses-v4-20260511.json
Writes: m15-baseline-verses-v5-20260511.json

Also recomputes review_status (most should remain 'Ready with changes';
the SG change is now visible in the new_subgroup block).
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
BASELINE_IN = os.path.join(M15_DIR, "m15-baseline-verses-v4-20260511.json")
BASELINE_OUT = os.path.join(M15_DIR, "m15-baseline-verses-v5-20260511.json")
DB_PATH = os.path.join("database", "bible_research.db")

VCG_LETTER_RE = re.compile(r"^VCG-([A-Z])-\d+$")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # Sub-group metadata
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

    with open(BASELINE_IN, "r", encoding="utf-8") as f:
        baseline = json.load(f)

    promotions: list[tuple[int, str, str, str]] = []  # (vr_id, ref, from_sg, to_sg)
    for v in baseline["verses"]:
        cur_sg = (v.get("current") or {}).get("subgroup_code")
        if cur_sg != "BOUNDARY":
            continue
        nv = v.get("new_vcg") or {}
        code = nv.get("code")
        if not code:
            continue
        m = VCG_LETTER_RE.match(code)
        if not m:
            continue
        letter = m.group(1)
        if letter not in ("A", "B", "C", "D", "E", "F", "G"):
            continue
        target_code = f"M15-{letter}"
        target = sg_by_code.get(target_code)
        if not target:
            print(f"[WARN] sub-group {target_code} not in cluster_subgroup; skipping")
            continue
        old_new_sg = v.get("new_subgroup")
        old_target = (old_new_sg or {}).get("code")
        v["new_subgroup"] = {
            "code": target["code"],
            "label": target["label"],
            "description": target["description"],
        }
        promotions.append((v["vr_id"], v["reference"],
                           old_target or "(none)", target["code"]))
        # The promotion makes the new SG different from current SG; status
        # stays 'Ready with changes' (it's a sub-group change, not a flag).
        # Re-evaluate only if it was something else.
        if v.get("review_status") not in ("Ready with changes", "For Review", "For research", "No change"):
            v["review_status"] = "Ready with changes"

    # Update metadata
    baseline["metadata"]["schema_version"] = "baseline-v5"
    baseline["metadata"]["generated_at"] = now_iso()
    baseline["metadata"]["boundary_promotion"] = {
        "rule": ("Verses currently in BOUNDARY whose new_vcg.code matches "
                 "^VCG-([A-G])-NN$ are promoted: new_subgroup.code = M15-<letter>."),
        "applied_at": now_iso(),
        "promotions_applied": len(promotions),
    }

    with open(BASELINE_OUT, "w", encoding="utf-8") as f:
        json.dump(baseline, f, ensure_ascii=False, indent=2)

    # Summary
    from collections import Counter
    by_target = Counter(t for _, _, _, t in promotions)
    print(f"Promotions applied: {len(promotions)}")
    for target, n in sorted(by_target.items()):
        print(f"  → {target}: {n}")
    print(f"Written: {BASELINE_OUT}")
    print(f"Size: {os.path.getsize(BASELINE_OUT):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
