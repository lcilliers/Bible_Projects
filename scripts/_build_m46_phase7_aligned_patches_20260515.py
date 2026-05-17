"""Build M46 Phase 7 aligned patches (v2 VCREVISE + v3 VCNEW).

Source: WA-M46-patch-phase7-routing-v1-20260515.json (AI's reading-grounded patch).
Output:
  - WA-M46-patch-phase7-routing-v2-20260515.json (VCREVISE, applier format)
  - WA-M46-patch-phase7-newverses-v3-20260515.json (VCNEW, 2 sha.men adj inserts)

Alignment per outputs/markdown/m46-phase7-patch-alignment-v1-20260515.md.

Read-only against DB; only writes the two JSON files.
"""
import json
import sqlite3
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
SRC = REPO / "Sessions" / "Session_Clusters" / "M46" / "WA-M46-patch-phase7-routing-v1-20260515.json"
OUT_V2 = REPO / "Sessions" / "Session_Clusters" / "M46" / "WA-M46-patch-phase7-routing-v2-20260515.json"
OUT_V3 = REPO / "Sessions" / "Session_Clusters" / "M46" / "WA-M46-patch-phase7-newverses-v3-20260515.json"

SUBGROUP_MAP = {"M46-A": 45, "M46-B": 46, "M46-C": 47, "M46-D": 48}

H7600_ADDITIONS = [
    {"ref": "Isa 32:9",  "subgroup": "M46-A", "group_id": 1861,
     "basis": "Complacent ease of Jerusalem's women — same 413-001 register as Amo 6:1 / Zec 1:15 already in patch; CC extrapolation from AI's pattern."},
    {"ref": "Isa 32:11", "subgroup": "M46-A", "group_id": 1861,
     "basis": "Same pericope as Isa 32:9 — complacent ease warning. CC extrapolation."},
    {"ref": "Isa 32:18", "subgroup": "M46-D", "group_id": 1862,
     "basis": "Per AI's note: 413-002 'divine secure quietness' face routes to M46-D + VCG 1862. Existing is_anchor=1 preserved."},
    {"ref": "Isa 37:29", "subgroup": "M46-A", "group_id": 1861,
     "basis": "Sennacherib's complacent boasting — 413-001 register. CC extrapolation."},
]


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    src = json.loads(SRC.read_text(encoding="utf-8"))
    src_ops = src["operations"]
    src_meta = src["_patch_meta"]

    distinct_mti = sorted({o["mti_id"] for o in src_ops})

    md_versions = {}
    for mti in distinct_mti:
        r = conn.execute("SELECT md_version FROM mti_terms WHERE id=?", (mti,)).fetchone()
        md_versions[mti] = r["md_version"]

    v2_ops = []
    v3_ops = []
    realignments = []
    next_op_seq = 1

    for o in src_ops:
        ref = o["reference"]
        mti = o["mti_id"]
        patch_vr = o["vr_id"]
        target_sg_code = o["set_cluster_subgroup"]
        target_gid = o["set_group_id"]
        is_anchor = o.get("set_is_anchor", 0)
        basis = o["routing_basis"]

        # Resolve the canonical verse_record_id
        vc_at_patch_vr = conn.execute(
            "SELECT id FROM verse_context WHERE verse_record_id=? AND mti_term_id=?",
            (patch_vr, mti)
        ).fetchone()

        if vc_at_patch_vr:
            canonical_vr_id = patch_vr
            vr_status = "exact"
        else:
            # Look up by reference + mti
            canonical_vr = conn.execute(
                "SELECT id FROM wa_verse_records WHERE reference=? AND mti_term_id=? "
                "AND COALESCE(delete_flagged,0)=0 ORDER BY id LIMIT 1",
                (ref, mti)
            ).fetchone()
            if canonical_vr:
                canonical_vr_id = canonical_vr["id"]
                # Confirm the vc row exists at the canonical vr_id
                vc_at_canonical = conn.execute(
                    "SELECT id FROM verse_context WHERE verse_record_id=? AND mti_term_id=?",
                    (canonical_vr_id, mti)
                ).fetchone()
                if vc_at_canonical:
                    vr_status = "recovered"
                    realignments.append({"ref": ref, "mti": mti, "patch_vr": patch_vr, "canonical_vr": canonical_vr_id})
                else:
                    # Genuinely orphan — needs VCNEW
                    vr_status = "vcnew"
            else:
                vr_status = "no_wa_verse_records"

        sg_id = SUBGROUP_MAP[target_sg_code]

        if vr_status in ("exact", "recovered"):
            set_dict = {"group_id": target_gid, "cluster_subgroup_id": sg_id}
            if is_anchor == 1:
                set_dict["is_anchor"] = 1
            v2_ops.append({
                "op_id": f"OP-{next_op_seq:03d}",
                "table": "verse_context",
                "operation": "update",
                "match": {"verse_record_id": canonical_vr_id, "mti_term_id": mti, "delete_flagged": 0},
                "set": set_dict,
                "_reference": ref,
                "_routing_basis": basis,
                "_vr_status": vr_status,
            })
            next_op_seq += 1
        elif vr_status == "vcnew":
            # Sha.men adj orphans (Neh 9:25, Neh 9:35)
            v3_ops.append({
                "op_id": f"OP-{len(v3_ops)+1:03d}",
                "table": "verse_context",
                "operation": "insert",
                "record": {
                    "verse_record_id": canonical_vr_id,
                    "mti_term_id": mti,
                    "group_id": target_gid,
                    "cluster_subgroup_id": sg_id,
                    "is_relevant": 1,
                    "is_anchor": is_anchor,
                    "is_related": 0,
                    "delete_flagged": 0,
                    "vertical_pass_flag": 0,
                },
                "_reference": ref,
                "_routing_basis": basis,
            })
        else:
            print(f"  WARNING: skipped op for {ref} mti={mti} — no wa_verse_records entry found", file=sys.stderr)

    # Add 4 H7600 ops
    for add in H7600_ADDITIONS:
        ref = add["ref"]
        vr = conn.execute(
            "SELECT id FROM wa_verse_records WHERE reference=? AND mti_term_id=413 "
            "AND COALESCE(delete_flagged,0)=0 ORDER BY id LIMIT 1",
            (ref,)
        ).fetchone()
        if not vr:
            print(f"  WARNING: H7600 addition {ref} — no wa_verse_records entry", file=sys.stderr)
            continue
        canonical_vr_id = vr["id"]
        vc = conn.execute(
            "SELECT is_anchor FROM verse_context WHERE verse_record_id=? AND mti_term_id=413",
            (canonical_vr_id,)
        ).fetchone()
        if not vc:
            print(f"  WARNING: H7600 addition {ref} — no verse_context row at canonical vr", file=sys.stderr)
            continue
        sg_id = SUBGROUP_MAP[add["subgroup"]]
        set_dict = {"group_id": add["group_id"], "cluster_subgroup_id": sg_id}
        # Preserve existing anchor where applicable (Isa 32:18)
        v2_ops.append({
            "op_id": f"OP-{next_op_seq:03d}",
            "table": "verse_context",
            "operation": "update",
            "match": {"verse_record_id": canonical_vr_id, "mti_term_id": 413, "delete_flagged": 0},
            "set": set_dict,
            "_reference": ref,
            "_routing_basis": add["basis"],
            "_vr_status": "added_by_cc",
        })
        next_op_seq += 1

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    v2_meta = {
        "patch_id": "WA-M46-patch-phase7-routing-v2-20260515",
        "patch_type": "VCREVISE",
        "cluster_code": "M46",
        "source_report": src_meta["source_report"],
        "governing_instruction": "wa-sessionb-cluster-instruction-v1_13-20260514.md",
        "supersedes": src_meta["patch_id"],
        "date": now,
        "description": (
            "Phase 7 verse routing for M46. CC-aligned from AI v1 patch "
            "(WA-M46-patch-phase7-routing-v1-20260515.json). Eight technical "
            "defects in v1 were corrected without disturbing the reading-"
            "grounded routing decisions. See "
            "outputs/markdown/m46-phase7-patch-alignment-v1-20260515.md and "
            "Sessions/Session_Clusters/M46/WA-M46-cc-response-to-phase7-patch-v1-20260515.md "
            "for the full audit trail."
        ),
        "terms_covered": distinct_mti,
        "input_versions": {str(k): v for k, v in md_versions.items()},
        "op_count": len(v2_ops),
        "cc_alignment_notes": {
            "anchor_strategy": "Existing anchors preserved except where AI explicitly designated 7 new anchor ops (per AI's _patch_meta.description: 'Anchors set where designated'). set_is_anchor field omitted from non-anchor ops.",
            "vr_id_corrections": f"{len(realignments)} ops had vr_id corrected via (reference, mti_term_id) lookup. Original AI patch used verse_context.id values where verse_record_id was expected.",
            "h7600_additions": "4 H7600 sha.a.nan verses added per AI's instruction in v1 notes (CC to identify 413-002 verses) and pattern extrapolation: Isa 32:9, Isa 32:11, Isa 37:29 -> M46-A gid=1861; Isa 32:18 -> M46-D gid=1862.",
            "orphan_inserts_split": "2 truly-orphan ops (Neh 9:25, Neh 9:35 for sha.men adj mti=4695) split into companion VCNEW patch WA-M46-patch-phase7-newverses-v3-20260515.json.",
            "subgroup_code_resolution": "AI's 'M46-A'..'M46-D' translated to integer cluster_subgroup_id: 45/46/47/48.",
            "liparos_term_move": "Term G3045 liparos moved from M46-A to M46-B via mti_term_subgroup UPDATE before patch apply (separate inline operation, not part of this patch). Required because AI's reading routes Rev 18:14 to M46-B.",
            "anchor_preservation_for_isa_32_18": "Isa 32:18 H7600 retained is_anchor=1 (existing) — patch op does not modify is_anchor.",
            "hon_retargeting_applied": "4 hon (H1952 mti=7010) ops retarget Psa 112:3 / Psa 119:14 / Pro 11:4 / Pro 28:22 from group_id=2933 to specific content-aligned VCGs (3711/3716/3717/2957). AI's generic 'preserve existing group_id' note overridden by reading-grounded explicit ops.",
        },
        "ai_input_intent_summary": src_meta,
    }

    v3_meta = {
        "patch_id": "WA-M46-patch-phase7-newverses-v3-20260515",
        "patch_type": "VCNEW",
        "cluster_code": "M46",
        "source_report": src_meta["source_report"],
        "governing_instruction": "wa-sessionb-cluster-instruction-v1_13-20260514.md",
        "companion_to": "WA-M46-patch-phase7-routing-v2-20260515",
        "date": now,
        "description": (
            "VCNEW inserts for 2 sha.men adj verses not previously in verse_context. "
            "Companion to WA-M46-patch-phase7-routing-v2-20260515 (VCREVISE)."
        ),
        "terms_covered": [4695],
        "input_versions": {"4695": md_versions[4695]},
        "op_count": len(v3_ops),
        "ai_input_intent_summary": {
            "from_patch": src_meta["patch_id"],
            "ops_split_out": [{"ref": o["_reference"], "vr_id": o["record"]["verse_record_id"]} for o in v3_ops],
        },
    }

    OUT_V2.write_text(json.dumps({"_patch_meta": v2_meta, "operations": v2_ops}, indent=2, ensure_ascii=False), encoding="utf-8")
    OUT_V3.write_text(json.dumps({"_patch_meta": v3_meta, "operations": v3_ops}, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"v2 ops: {len(v2_ops)}  (target: 206)")
    print(f"v3 ops: {len(v3_ops)}  (target: 2)")
    print(f"vr_id corrections applied: {len(realignments)}")
    print(f"Wrote: {OUT_V2.relative_to(REPO)}")
    print(f"Wrote: {OUT_V3.relative_to(REPO)}")


if __name__ == "__main__":
    main()
