"""_merge_m15_clean_slate_v2_meanings_v1_20260511.py — read+write JSON.

Pull verse-level meanings from the user's externally-refreshed clean-slate
v2 file and merge them into the main baseline. The clean-slate v2 has a
meaning for every one of the 1715 rows (the previous main baseline had
286 missing).

Reads:
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v5-20260511.json
  - Sessions/Session_Clusters/M15/wa-m15-clean-slate-v2-20260511.json

Writes:
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v6-20260511.json

Behaviour:
  - Match by vr_id (primary key)
  - For each row, set meaning.text from clean-slate v2
  - Track stats: newly added vs text changed vs unchanged
  - Recompute review_status with the existing logic so transitions are
    visible (verses that were 'For research' for lack of meaning will
    shift up; verses still missing new_vcg may still be 'For research')
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
MAIN_IN = os.path.join(M15_DIR, "m15-baseline-verses-v5-20260511.json")
SLATE_IN = os.path.join(M15_DIR, "wa-m15-clean-slate-v2-20260511.json")
MAIN_OUT = os.path.join(M15_DIR, "m15-baseline-verses-v6-20260511.json")


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
    with open(SLATE_IN, "r", encoding="utf-8") as f:
        slate = json.load(f)
    print(f"Main baseline rows: {len(main['verses'])}")
    print(f"Clean-slate v2 rows: {len(slate['verses'])}")

    # Build slate lookup by vr_id (slate has 1 row per vr_id; main may have
    # 2 rows for the 2 duplicate vr_ids — both get the same updated meaning).
    slate_by_vr: dict[int, str | None] = {}
    for s in slate["verses"]:
        slate_by_vr[s["vr_id"]] = s.get("meaning")

    duplicate_vr_ids = set(main["metadata"].get("duplicate_vr_ids", []))
    src_label = os.path.basename(SLATE_IN)

    # Update meanings on main, track stats
    newly_added = 0
    text_changed = 0
    unchanged = 0
    no_slate_match = 0
    for v in main["verses"]:
        new_text = slate_by_vr.get(v["vr_id"])
        if new_text is None:
            no_slate_match += 1
            continue
        existing = v.get("meaning") or {}
        existing_text = existing.get("text")
        if not existing_text:
            v["meaning"] = {
                "text": new_text,
                "source_file": src_label,
                "source_version": "clean-slate-v2",
            }
            newly_added += 1
        elif existing_text.strip() != new_text.strip():
            v["meaning"] = {
                "text": new_text,
                "source_file": src_label,
                "source_version": "clean-slate-v2",
                "previous_text": existing_text,
                "previous_source_file": existing.get("source_file"),
            }
            text_changed += 1
        else:
            # Existing text matches; keep meta but stamp source as latest
            v["meaning"] = {
                **existing,
                "text": new_text,
                "source_file": src_label,
                "source_version": "clean-slate-v2",
            }
            unchanged += 1

    # Recompute review_status with the existing logic
    new_counts = {"No change": 0, "Ready with changes": 0,
                  "For Review": 0, "For research": 0}
    transitions: dict[tuple[str, str], int] = {}
    for v in main["verses"]:
        cur = v.get("current") or {}
        nv = v.get("new_vcg")
        has_meaning = bool((v.get("meaning") or {}).get("text"))
        has_new_vcg = nv is not None
        is_dup_vr = v["vr_id"] in duplicate_vr_ids
        status_now = cur.get("status")
        no_current_group = cur.get("group_id") is None

        # Preserve manual 'No change' overrides
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
            # has_meaning but no new_vcg — under existing logic this stays
            # 'For research'. The researcher views VCGs as noise; this
            # bucket may need a different status semantic going forward.
            review = "For research"
            v.pop("review_flags", None)

        prev = v.get("review_status", "(unset)")
        if prev != review:
            transitions[(prev, review)] = transitions.get((prev, review), 0) + 1
        v["review_status"] = review
        new_counts[review] += 1

    # Metadata bump
    main["metadata"]["schema_version"] = "baseline-v6"
    main["metadata"]["generated_at"] = now_iso()
    main["metadata"]["meaning_layer"] = {
        "source": os.path.relpath(SLATE_IN, ROOT).replace("\\", "/"),
        "source_version": "clean-slate-v2",
        "files_parsed": [src_label],
        "meaning_rows_parsed": len(slate["verses"]),
        "baseline_rows_with_meaning": sum(
            1 for v in main["verses"]
            if (v.get("meaning") or {}).get("text")),
        "baseline_rows_without_meaning": sum(
            1 for v in main["verses"]
            if not (v.get("meaning") or {}).get("text")),
        "newly_added": newly_added,
        "text_changed": text_changed,
        "unchanged": unchanged,
        "vr_ids_with_no_slate_match": no_slate_match,
    }
    main["metadata"]["status_workflow"]["default_distribution"] = new_counts

    with open(MAIN_OUT, "w", encoding="utf-8") as f:
        json.dump(main, f, ensure_ascii=False, indent=2)

    print()
    print("Meaning merge:")
    print(f"  newly added (was missing):     {newly_added}")
    print(f"  text changed (replaced):        {text_changed}")
    print(f"  unchanged (matched existing):   {unchanged}")
    print(f"  no slate match:                 {no_slate_match}")
    print()
    print("review_status — new distribution:")
    for k, n in new_counts.items():
        print(f"  {k:25s} {n}")
    if transitions:
        print()
        print("Status transitions:")
        for (a, b), n in sorted(transitions.items(), key=lambda x: -x[1]):
            print(f"  {a:22s} → {b:22s} {n}")
    print()
    print(f"Written: {MAIN_OUT}")
    print(f"Size: {os.path.getsize(MAIN_OUT):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
