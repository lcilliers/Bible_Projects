"""_merge_m15a_anchors_v1_20260511.py — read+write JSON.

Pull anchor verses from wa-m15a-vcg-groups-v2-20260511.json (one per VCG)
and merge into:
  (a) the main baseline (v8 → v9): mark the anchor verse on each VCG
      row by setting `new_vcg.is_anchor=true` and storing the rationale
  (b) the DB-staging JSON: populate `anchor_proposed` per VCG so the
      staging is now directive-ready (cluster instruction §9 hard gate
      now satisfied)

Reads:
  - Sessions/Session_Clusters/M15/wa-m15a-vcg-groups-v2-20260511.json
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v8-20260511.json
  - Sessions/Session_Clusters/M15/m15-vcg-db-staging-M15A-v1-20260511.json

Writes:
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v9-20260511.json
  - Sessions/Session_Clusters/M15/m15-vcg-db-staging-M15A-v2-20260511.json
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
ANCHORS_IN = os.path.join(M15_DIR, "wa-m15a-vcg-groups-v2-20260511.json")
MAIN_IN = os.path.join(M15_DIR, "m15-baseline-verses-v8-20260511.json")
STAGING_IN = os.path.join(M15_DIR, "m15-vcg-db-staging-M15A-v1-20260511.json")
MAIN_OUT = os.path.join(M15_DIR, "m15-baseline-verses-v9-20260511.json")
STAGING_OUT = os.path.join(M15_DIR,
                           "m15-vcg-db-staging-M15A-v2-20260511.json")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    with open(ANCHORS_IN, "r", encoding="utf-8") as f:
        anchors_doc = json.load(f)

    # Build anchor lookup: vcg_code → anchor dict
    anchors_by_vcg: dict[str, dict] = {}
    for grp in anchors_doc["verse_context_groups"]:
        code = grp["code"]
        if "anchor_verse" in grp:
            anchors_by_vcg[code] = grp["anchor_verse"]
    print(f"Anchors found: {len(anchors_by_vcg)} across {len(anchors_doc['verse_context_groups'])} VCGs")
    for code, a in sorted(anchors_by_vcg.items()):
        print(f"  {code} → vr_id {a['vr_id']} {a['reference']}  ({a['strongs']} {a['translit']})")

    # --- Update main baseline ---
    with open(MAIN_IN, "r", encoding="utf-8") as f:
        main = json.load(f)
    anchor_vr_ids = {a["vr_id"]: (code, a)
                     for code, a in anchors_by_vcg.items()}
    marked = 0
    for v in main["verses"]:
        nv = v.get("new_vcg")
        if not nv:
            continue
        # Default — explicitly mark non-anchors so it's visible in the JSON
        if "is_anchor" not in nv:
            nv["is_anchor"] = False
        if v["vr_id"] in anchor_vr_ids:
            code, a = anchor_vr_ids[v["vr_id"]]
            # Sanity check — anchor should belong to the VCG it's listed under
            if nv.get("code") == code:
                nv["is_anchor"] = True
                nv["anchor_rationale"] = a.get("anchor_rationale")
                marked += 1
            else:
                print(f"  [WARN] vr_id {v['vr_id']} listed as anchor for {code} "
                      f"but its new_vcg.code is {nv.get('code')!r}; not marking")

    main["metadata"]["schema_version"] = "baseline-v9"
    main["metadata"]["generated_at"] = now_iso()
    main["metadata"]["m15a_anchors_merge"] = {
        "source": "Sessions/Session_Clusters/M15/wa-m15a-vcg-groups-v2-20260511.json",
        "applied_at": now_iso(),
        "anchors_recorded": marked,
    }
    with open(MAIN_OUT, "w", encoding="utf-8") as f:
        json.dump(main, f, ensure_ascii=False, indent=2)
    print()
    print(f"Main: marked {marked} anchor row(s) (expected {len(anchors_by_vcg)})")
    print(f"  written: {MAIN_OUT}")
    print(f"  size: {os.path.getsize(MAIN_OUT):,} bytes")

    # --- Update DB staging ---
    with open(STAGING_IN, "r", encoding="utf-8") as f:
        staging = json.load(f)
    updated = 0
    for block in staging.get("vcg_creations", []):
        a = anchors_by_vcg.get(block["code"])
        if a:
            block["anchor_proposed"] = {
                "vr_id": a["vr_id"],
                "reference": a["reference"],
                "strongs": a["strongs"],
                "translit": a["translit"],
                "anchor_rationale": a.get("anchor_rationale"),
            }
            updated += 1
        else:
            print(f"  [WARN] no anchor for VCG {block['code']}")
    staging["metadata"]["generated_at"] = now_iso()
    staging["metadata"]["anchor_status"] = (
        f"Designated. {updated}/{len(staging['vcg_creations'])} VCGs have an "
        f"anchor_proposed (cluster instruction §9 hard-gate satisfied for M15-A)."
    )
    staging["metadata"]["anchor_source"] = (
        "Sessions/Session_Clusters/M15/wa-m15a-vcg-groups-v2-20260511.json"
    )
    with open(STAGING_OUT, "w", encoding="utf-8") as f:
        json.dump(staging, f, ensure_ascii=False, indent=2)
    print()
    print(f"DB-staging: anchored {updated}/{len(staging['vcg_creations'])} VCGs")
    print(f"  written: {STAGING_OUT}")
    print(f"  size: {os.path.getsize(STAGING_OUT):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
