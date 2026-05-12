"""_export_m15_baseline_verses_v1_20260511.py — read-only.

Emit the 1713 M15 verse-occurrence baseline as JSON for AI-driven cleanup.

One row per (vr_id, mti_term_id) — i.e. one row per term-occurrence at a
verse location. Carries the term, the verse text, and the current DB
analytical state (verse_context + sub-group + VSG).

Schema deliberately lean so refinement layers can be added later without
restructuring.

Output: Sessions/Session_Clusters/M15/m15-baseline-verses-v1-20260511.json
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_PATH = os.path.join(
    "Sessions", "Session_Clusters", "M15",
    "m15-baseline-verses-v1-20260511.json",
)
CLUSTER_CODE = "M15"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def derive_status(vc_row) -> str:
    """Return G / SA / NR / P / UT for a verse_context state.
    UT = no vc row at all.
    """
    if vc_row is None:
        return "UT"
    if vc_row["set_aside_reason"]:
        return "SA"
    if vc_row["is_relevant"] == 0:
        return "NR"
    if vc_row["group_id"] is not None:
        return "G"
    return "P"


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cluster = conn.execute(
        "SELECT cluster_code, gloss, version, status, last_updated_date "
        "FROM cluster WHERE cluster_code=?", (CLUSTER_CODE,),
    ).fetchone()
    if not cluster:
        print(f"[ERR] no cluster row for {CLUSTER_CODE}")
        return 1

    print(f"Exporting {CLUSTER_CODE} ({cluster['gloss']}) baseline...")

    rows = conn.execute("""
        SELECT
          vr.id              AS vr_id,
          vr.reference       AS reference,
          vr.verse_text      AS verse_text,
          mt.id              AS mti_id,
          mt.strongs_number  AS strongs,
          mt.transliteration AS translit,
          mt.gloss           AS gloss,
          mt.language        AS language,
          vc.id              AS vc_id,
          vc.cluster_subgroup_id AS sg_id,
          cs.subgroup_code   AS subgroup_code,
          vc.group_id        AS group_id,
          vcg.group_code     AS group_code,
          vc.is_anchor       AS is_anchor,
          vc.is_relevant     AS is_relevant,
          vc.set_aside_reason AS set_aside_reason,
          vc.analysis_note   AS analysis_note,
          vc.notes           AS notes
        FROM wa_verse_records vr
        JOIN mti_terms mt ON mt.id = vr.mti_term_id
        LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                    AND vc.mti_term_id = vr.mti_term_id
                                    AND COALESCE(vc.delete_flagged,0) = 0
        LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE mt.cluster_code = ?
          AND COALESCE(vr.delete_flagged,0) = 0
        ORDER BY mt.strongs_number, vr.book_id, vr.chapter, vr.verse_num, vr.id
    """, (CLUSTER_CODE,)).fetchall()

    verses = []
    sg_counter = {}
    status_counter = {"G": 0, "SA": 0, "NR": 0, "P": 0, "UT": 0}
    # Track vr_ids with multiple active vc rows (data integrity issue)
    vr_id_counts: dict[int, int] = {}
    for r in rows:
        vr_id_counts[r["vr_id"]] = vr_id_counts.get(r["vr_id"], 0) + 1
    duplicate_vr_ids = sorted(v for v, n in vr_id_counts.items() if n > 1)

    for r in rows:
        st = derive_status(r)
        status_counter[st] += 1
        sg = r["subgroup_code"] or "(unrouted)"
        sg_counter[sg] = sg_counter.get(sg, 0) + 1
        verses.append({
            "vr_id": r["vr_id"],
            "reference": r["reference"],
            "verse_text": (r["verse_text"] or "").strip(),
            "term": {
                "mti_id": r["mti_id"],
                "strongs": r["strongs"],
                "translit": r["translit"],
                "gloss": r["gloss"],
                "language": r["language"],
            },
            "current": {
                "vc_id": r["vc_id"],
                "subgroup_code": r["subgroup_code"],
                "group_id": r["group_id"],
                "group_code": r["group_code"],
                "status": st,
                "is_anchor": bool(r["is_anchor"]) if r["is_anchor"] is not None else None,
                "is_relevant": bool(r["is_relevant"]) if r["is_relevant"] is not None else None,
                "set_aside_reason": r["set_aside_reason"],
                "analysis_note": r["analysis_note"],
                "notes": r["notes"],
            },
        })

    out = {
        "metadata": {
            "cluster_code": cluster["cluster_code"],
            "cluster_version": cluster["version"],
            "cluster_status": cluster["status"],
            "cluster_last_updated": cluster["last_updated_date"],
            "generated_at": now_iso(),
            "source": "database/bible_research.db",
            "schema_version": "baseline-v1",
            "row_count": len(verses),
            "unique_vr_count": len(vr_id_counts),
            "duplicate_vr_ids": duplicate_vr_ids,
            "natural_key": "(vr_id, vc_id) — one row per active verse_context occurrence",
            "purpose": (
                "Baseline for progressive AI-driven cleanup of verse to "
                "sub-group to VSG assignments. The 'current' object holds "
                "the live DB analytical state; refinement layers should be "
                "added under sibling keys (e.g. 'proposed', 'issues', 'review'). "
                "Two vr_ids have duplicate active verse_context rows — those "
                "are data-integrity issues already on the cleanup list and "
                "are surfaced rather than hidden."
            ),
            "status_codes": {
                "G": "group-assigned (analysed)",
                "SA": "set-aside (with reason)",
                "NR": "not-relevant (is_relevant=0)",
                "P": "pending (relevant, no group yet)",
                "UT": "untouched (no verse_context row)",
            },
            "status_counts": status_counter,
            "subgroup_counts": dict(sorted(sg_counter.items())),
        },
        "verses": verses,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"  rows: {len(verses)}")
    print(f"  status counts: {status_counter}")
    print(f"  sub-group counts: {sg_counter}")
    print(f"  written: {OUT_PATH}")
    print(f"  size: {os.path.getsize(OUT_PATH):,} bytes")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
