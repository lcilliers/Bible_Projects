"""_transform_m15_phase2_patch_v1_20260508.py — read-only transformer.

Produces a canonical-format sibling of:
  Sessions/Session_Clusters/M15/files phase 2/
  wa-cluster-M15-patch-vcrevise-utreview-v1-20260508.json

Three corrections vs the original:
  1. operation 'upsert' -> 'insert' (UT cases; 323 ops) or 'update'
     (rows that already exist; 3 ops). Decided per-op by checking the DB
     for an existing (mti_term_id, verse_record_id) row.
  2. Field 'context_description' (not on verse_context) -> 'analysis_note'
     (per M05 SA-description precedent).
  3. Insert ops include the full record (group_id=NULL, is_anchor=0,
     is_related=0, delete_flagged=0) so the inserted row is well-formed.

Original patch retained for audit. Output sibling written to the same
folder with '-canonical-' tag.
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
SRC = ("Sessions/Session_Clusters/M15/files phase 2/"
       "wa-cluster-M15-patch-vcrevise-utreview-v1-20260508.json")
DEST = ("Sessions/Session_Clusters/M15/files phase 2/"
        "wa-cluster-M15-patch-vcrevise-utreview-canonical-v1-20260508.json")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    with open(SRC, encoding="utf-8") as f:
        patch = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    new_ops = []
    n_insert = 0
    n_update = 0
    for op in patch["operations"]:
        match = op["match"]
        set_vals = dict(op["set"])
        op_id = op["op_id"]

        # Map context_description -> analysis_note
        analysis_note = set_vals.pop("context_description", None)
        if analysis_note is not None:
            set_vals["analysis_note"] = analysis_note

        mti_id = match["mti_term_id"]
        vr_id = match["verse_record_id"]

        # Decide insert vs update by current DB state
        existing = cur.execute(
            "SELECT id FROM verse_context "
            " WHERE mti_term_id=? AND verse_record_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (mti_id, vr_id),
        ).fetchone()

        if existing is None:
            # INSERT — full record
            record = {
                "verse_record_id": vr_id,
                "mti_term_id": mti_id,
                "group_id": None,
                "is_anchor": 0,
                "is_relevant": set_vals.get("is_relevant", 0),
                "is_related": 0,
                "set_aside_reason": set_vals.get("set_aside_reason"),
                "analysis_note": set_vals.get("analysis_note"),
                "delete_flagged": 0,
            }
            new_ops.append({
                "op_id": op_id,
                "operation": "insert",
                "table": "verse_context",
                "record": record,
            })
            n_insert += 1
        else:
            # UPDATE — same match + set as canonical update form
            new_ops.append({
                "op_id": op_id,
                "operation": "update",
                "table": "verse_context",
                "match": {
                    "mti_term_id": mti_id,
                    "verse_record_id": vr_id,
                },
                "set": set_vals,
            })
            n_update += 1

    # ── R4 safety pass ──────────────────────────────────────────────────
    # The patch creates new is_relevant=1 vc rows. R4 (programme integrity
    # rule) requires every term with relevant verses to have at least one
    # anchor. For terms with NO existing anchor and at least one new
    # is_relevant=1 insert in this patch, mark the first such insert as
    # is_anchor=1 (provisional — Phase 6 group-verse mapping revisits).
    from collections import defaultdict

    # Per-term: pre-patch anchor count, list of new-relevant op indices
    per_term: dict[int, dict] = defaultdict(
        lambda: {"pre_anc": 0, "rel_op_idx": []}
    )
    for tid in {(o.get("record") or o.get("match") or {}).get("mti_term_id")
                for o in new_ops if (o.get("record") or o.get("match"))}:
        if tid is None:
            continue
        r = cur.execute(
            "SELECT SUM(is_anchor) AS anc FROM verse_context "
            " WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0",
            (tid,),
        ).fetchone()
        per_term[tid]["pre_anc"] = r["anc"] or 0

    for i, op in enumerate(new_ops):
        if op["operation"] != "insert":
            continue
        rec = op["record"]
        if rec.get("is_relevant") == 1:
            per_term[rec["mti_term_id"]]["rel_op_idx"].append(i)

    r4_provisional_anchors = []
    for tid, d in per_term.items():
        if d["pre_anc"] == 0 and d["rel_op_idx"]:
            # Set is_anchor=1 on the first is_relevant=1 insert for this term
            first_idx = d["rel_op_idx"][0]
            new_ops[first_idx]["record"]["is_anchor"] = 1
            r4_provisional_anchors.append(
                (tid, new_ops[first_idx]["record"]["verse_record_id"])
            )

    if r4_provisional_anchors:
        print(f"R4 provisional anchors set on "
              f"{len(r4_provisional_anchors)} term(s):")
        for tid, vr in r4_provisional_anchors:
            print(f"  mti={tid} vr={vr}")

    # Recompute terms_covered + input_versions from actual operations
    referenced_terms = set()
    for op in new_ops:
        rec = op.get("record") or op.get("match") or {}
        if "mti_term_id" in rec:
            referenced_terms.add(rec["mti_term_id"])

    # Get current md_version per term so the version gate (A-03) is satisfied
    input_versions = {}
    for tid in referenced_terms:
        r = cur.execute(
            "SELECT md_version FROM mti_terms WHERE id=?", (tid,)
        ).fetchone()
        input_versions[str(tid)] = int(r["md_version"]) if r else 1

    # Build canonical patch envelope
    new_meta = dict(patch["_patch_meta"])
    new_meta["patch_id"] = "PATCH-20260508-M15-VCREVISE-UTREVIEW-CANONICAL-V1"
    new_meta["supersedes"] = (
        "PATCH-20260508-M15-VCREVISE-UTREVIEW-V1 (format errors: "
        "operation='upsert' not supported by applicator; field "
        "'context_description' not on verse_context table — moved to "
        "'analysis_note'; terms_covered list out of sync with operations)"
    )
    new_meta["correction_note"] = (
        f"Canonical-format rewrite. {n_insert} insert ops (UT cases) "
        f"+ {n_update} update ops (existing rows). "
        "context_description -> analysis_note. terms_covered + "
        "input_versions recomputed from actual operations. "
        f"R4 integrity: {len(r4_provisional_anchors)} provisional "
        "anchor(s) set on terms with no pre-existing anchor "
        f"({', '.join(str(t) for t,_ in r4_provisional_anchors)}); "
        "Phase 6 mapping revisits these. "
        "Verified against DB as of generation time."
    )
    new_meta["terms_covered"] = sorted(referenced_terms)
    new_meta["input_versions"] = input_versions
    new_meta["operations_count"] = len(new_ops)

    new_patch = {
        "_patch_meta": new_meta,
        "operations": new_ops,
    }

    with open(DEST, "w", encoding="utf-8") as f:
        json.dump(new_patch, f, indent=2, ensure_ascii=False)

    print(f"Wrote: {DEST}")
    print(f"  insert ops: {n_insert}")
    print(f"  update ops: {n_update}")
    print(f"  total:      {n_insert + n_update}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
