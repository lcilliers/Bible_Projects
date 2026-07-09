"""_apply_m15_logos_subgroup_v1_20260511.py — read+write JSON only.

Define a new sub-group M15-H for G3056 logos and assign every G3056 verse
to it (via new_subgroup). The DB is NOT modified — this is a proposal
captured in the JSON. A directive will be authored later to land it in DB.

Reads:  m15-baseline-verses-v6-20260511.json
Writes: m15-baseline-verses-v7-20260511.json
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
IN_PATH = os.path.join(M15_DIR, "m15-baseline-verses-v6-20260511.json")
OUT_PATH = os.path.join(M15_DIR, "m15-baseline-verses-v7-20260511.json")

# New sub-group spec — these are draft values; the researcher will refine
# the label / description when the directive is authored.
NEW_SG = {
    "code": "M15-H",
    "label": "Logos — the word as inner-being engagement",
    "description": (
        "Verses where the term logos (G3056) names the word as it enters, "
        "dwells in, addresses, or shapes the inner being — the inner "
        "engagement of the spoken or written word with conscience, mind, "
        "heart, and orientation toward God. Held as a distinct sub-group "
        "in M15 because logos sits across the wisdom/understanding/"
        "knowledge cluster without fitting any single existing sub-group "
        "and warrants its own analytical frame."
    ),
    "proposed_at": "2026-05-11",
    "proposed_by": "researcher direction (auto-mode session 2026-05-11)",
    "db_state": "not-yet-applied — sub-group does not exist in cluster_subgroup",
}

TARGET_STRONGS = "G3056"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    with open(IN_PATH, "r", encoding="utf-8") as f:
        d = json.load(f)

    # Collect G3056 verses
    g3056 = [v for v in d["verses"] if v["term"]["strongs"] == TARGET_STRONGS]
    print(f"G3056 logos verses found: {len(g3056)}")
    cur_sg = Counter((v.get("current") or {}).get("subgroup_code") for v in g3056)
    prev_new_sg = Counter((v.get("new_subgroup") or {}).get("code") for v in g3056)
    print(f"  by current sub-group: {dict(cur_sg)}")
    print(f"  by previous new_subgroup proposal: {dict(prev_new_sg)}")

    # Update each row's new_subgroup
    transitions = Counter()
    for v in g3056:
        prev = (v.get("new_subgroup") or {}).get("code")
        transitions[prev] += 1
        v["new_subgroup"] = {
            "code": NEW_SG["code"],
            "label": NEW_SG["label"],
            "description": NEW_SG["description"],
            "_origin": "manual_assignment_2026-05-11_logos_subgroup",
            "_prior_new_subgroup_code": prev,
        }

    # Recompute review_status (preserve manual 'No change' overrides)
    duplicate_vr_ids = set(d["metadata"].get("duplicate_vr_ids", []))
    counts = Counter()
    for v in d["verses"]:
        cur = v.get("current") or {}
        nv = v.get("new_vcg")
        has_meaning = bool((v.get("meaning") or {}).get("text"))
        has_new_vcg = nv is not None
        is_dup_vr = v["vr_id"] in duplicate_vr_ids
        status_now = cur.get("status")
        no_current_group = cur.get("group_id") is None

        if v.get("review_status") == "No change":
            review = "No change"
            v["review_flags"] = v.get("review_flags") or []
        elif (not has_new_vcg and not has_meaning) or is_dup_vr \
                or status_now in ("P", "UT") or no_current_group:
            review = "For research"
            v.pop("review_flags", None)
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
                v.pop("review_flags", None)
        else:
            review = "For research"
            v.pop("review_flags", None)
        v["review_status"] = review
        counts[review] += 1

    # Metadata bump
    d["metadata"]["schema_version"] = "baseline-v7"
    d["metadata"]["generated_at"] = now_iso()
    d["metadata"]["new_subgroup_proposed"] = NEW_SG
    d["metadata"]["new_subgroup_assignment"] = {
        "target_strongs": TARGET_STRONGS,
        "new_subgroup_code": NEW_SG["code"],
        "rows_updated": len(g3056),
        "previous_new_subgroup_distribution": dict(transitions),
    }
    d["metadata"]["status_workflow"]["default_distribution"] = dict(counts)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

    print()
    print(f"Assigned {len(g3056)} G3056 verses to new_subgroup={NEW_SG['code']!r}")
    print(f"  prior new_subgroup distribution before reassign: {dict(transitions)}")
    print()
    print(f"review_status — new distribution:")
    for k, n in counts.items():
        print(f"  {k:25s} {n}")
    print()
    print(f"Written: {OUT_PATH}")
    print(f"Size: {os.path.getsize(OUT_PATH):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
