"""
_produce_final_extract.py
─────────────────────────
Produce the final registry extract (wa-{nnn}-{word}-final-{date}.json)
per WA-Reference-v5.1 Section 14.1 and WA-SessionB-Extraction-Instruction-v5.2 Section 8.1.

Usage:
  python scripts/_produce_final_extract.py --registry=N
"""

import argparse
import json
import os
import sqlite3
from datetime import datetime, timezone

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "exports")


def produce_final_extract(registry_no: int) -> str:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Registry
    reg = dict(conn.execute(
        """SELECT no, word, phase1_term_count, phase1_verse_count, session_b_status,
                  cluster_assignment, sb_classification, sb_classification_reasoning,
                  carry_forward, source_category
           FROM word_registry WHERE no = ?""",
        (registry_no,),
    ).fetchone())

    if reg["session_b_status"] not in ("Analysis Complete", "Session B Complete"):
        conn.close()
        raise ValueError(
            f"Registry {registry_no} is at '{reg['session_b_status']}' — must be Analysis Complete or Session B Complete"
        )

    # File index
    fi = conn.execute(
        "SELECT id FROM wa_file_index WHERE registry_id = ?", (registry_no,)
    ).fetchone()
    file_id = fi["id"] if fi else None

    # Terms with evidential status + mti_status + verse counts
    # Scope mti_terms join to word_data_ref_fk = file_id to avoid duplicates across registries
    terms_raw = conn.execute(
        """SELECT ti.id as term_inv_id, ti.strongs_number, ti.transliteration, ti.language,
                  ti.evidential_status, ti.retention_note, ti.delete_flagged,
                  m.status as mti_status,
                  (SELECT COUNT(*) FROM wa_verse_records vr
                   WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0) as verse_count
           FROM wa_term_inventory ti
           LEFT JOIN mti_terms m ON m.strongs_number = ti.strongs_number
                                 AND m.word_data_ref_fk = ti.file_id
           WHERE ti.file_id = ? AND ti.delete_flagged = 0
           ORDER BY verse_count DESC""",
        (file_id,),
    ).fetchall()
    terms = [dict(t) for t in terms_raw]

    # Active terms = those with evidential_status set
    active_terms = [t for t in terms if t["evidential_status"] is not None]

    confirmed = [t for t in active_terms if t["evidential_status"] == "confirmed"]
    plausible = [t for t in active_terms if t["evidential_status"] == "plausible"]
    uncertain = [t for t in active_terms if t["evidential_status"] == "uncertain"]

    confirmed_vc = sum(t["verse_count"] for t in confirmed)
    plausible_vc = sum(t["verse_count"] for t in plausible)
    uncertain_vc = sum(t["verse_count"] for t in uncertain)

    # Top 5 dominant terms
    dominant = sorted(active_terms, key=lambda t: t["verse_count"], reverse=True)[:5]

    # Dimensions
    dim_row = conn.execute(
        "SELECT * FROM wa_session_b_dimensions WHERE registry_id = ?", (registry_no,)
    ).fetchone()
    if not dim_row:
        conn.close()
        raise ValueError(f"No dimensional profile found for registry {registry_no}")
    dim = dict(dim_row)

    # Derive dimensional weights from dimension notes and presence
    def _weight(present: int, note: str | None) -> str:
        if not present:
            return "PERIPHERAL"
        if note and any(w in note.lower() for w in ["dominat", "primary", "full range", "majority"]):
            return "PRIMARY"
        if note and any(w in note.lower() for w in ["substantial", "significant", "explicit"]):
            return "SECONDARY"
        return "SECONDARY"

    # Findings
    findings_raw = conn.execute(
        """SELECT finding_id, finding_type, finding, anchor_verses
           FROM wa_session_b_findings WHERE registry_id = ?
           ORDER BY finding_id""",
        (registry_no,),
    ).fetchall()

    conn.close()

    now_date = datetime.now(timezone.utc).strftime("%Y%m%d")
    word = reg["word"]

    final = {
        "meta": {
            "json_template_version": "final_v1.0",
            "json_filename": f"wa-{registry_no}-{word}-final-{now_date}.json",
            "registry_id": registry_no,
            "word": word,
            "cluster_assignment": reg["cluster_assignment"],
            "produced_date": now_date,
            "session_b_instruction_version": "WA-SessionB-Analysis-Instruction-v5",
            "extraction_instruction_version": "WA-SessionB-Extraction-Instruction-v5.2",
        },
        "registry_summary": {
            "word_label": word,
            "dimensions": reg.get("source_category") or "",
            "cluster_assignment": reg["cluster_assignment"],
            "phase1_term_count": reg["phase1_term_count"],
            "phase1_verse_count": reg["phase1_verse_count"],
            "active_term_count": len(active_terms),
            "confirmed_count": len(confirmed),
            "plausible_count": len(plausible),
            "uncertain_count": len(uncertain),
            "session_b_status": reg["session_b_status"],
            "sb_classification": reg["sb_classification"],
            "carry_forward": bool(reg["carry_forward"]),
            "dimensional_profile": {
                "relational_environment": {
                    "weight": _weight(dim["relational_environment"], dim["relational_environment_note"]),
                    "note": dim["relational_environment_note"],
                },
                "spirit_soul_body": {
                    "weight": _weight(dim["spirit_soul_body"], dim["spirit_soul_body_note"]),
                    "note": dim["spirit_soul_body_note"],
                },
                "inner_operations": {
                    "weight": _weight(dim["inner_operations"], dim["inner_operations_note"]),
                    "note": dim["inner_operations_note"],
                },
                "being": {
                    "weight": _weight(dim["being"], dim["being_note"]),
                    "note": dim["being_note"],
                },
            },
            "evidential_weight": {
                "confirmed_verse_count": confirmed_vc,
                "plausible_verse_count": plausible_vc,
                "uncertain_verse_count": uncertain_vc,
                "dominant_terms": [
                    {
                        "strongs_id": t["strongs_number"],
                        "transliteration": t["transliteration"],
                        "verse_count": t["verse_count"],
                        "evidential_status": t["evidential_status"],
                    }
                    for t in dominant
                ],
            },
        },
        "terms": [
            {
                "strongs_id": t["strongs_number"],
                "transliteration": t["transliteration"],
                "language": t["language"],
                "mti_status": t["mti_status"],
                "verse_count": t["verse_count"],
                "evidential_status": t["evidential_status"],
                "retention_note": t["retention_note"],
            }
            for t in active_terms
        ],
        "dimensions": {
            "relational_environment": {
                "present": bool(dim["relational_environment"]),
                "note": dim["relational_environment_note"],
            },
            "spirit_soul_body": {
                "present": bool(dim["spirit_soul_body"]),
                "note": dim["spirit_soul_body_note"],
            },
            "inner_operations": {
                "present": bool(dim["inner_operations"]),
                "note": dim["inner_operations_note"],
            },
            "being": {
                "present": bool(dim["being"]),
                "note": dim["being_note"],
            },
        },
        "inner_being_standing": {
            "classification": reg["sb_classification"],
            "reasoning": reg["sb_classification_reasoning"],
            "carry_forward": bool(reg["carry_forward"]),
        },
        "key_findings": [
            {
                "finding_id": f["finding_id"],
                "finding_type": f["finding_type"],
                "finding": f["finding"],
                "anchor_verses": f["anchor_verses"].split(", ") if f["anchor_verses"] else [],
            }
            for f in findings_raw
        ],
        "session_b_revision_candidates": [],
    }

    # Write
    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-{registry_no}-{word}-final-{now_date}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(final, fh, indent=2, ensure_ascii=False)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"\n{'=' * 60}")
    print(f"  FINAL REGISTRY EXTRACT: {filename}")
    print(f"  Registry: {registry_no}  |  Word: {word}")
    print(f"  Active terms: {len(active_terms)} (confirmed: {len(confirmed)}, plausible: {len(plausible)}, uncertain: {len(uncertain)})")
    print(f"  Verse weight: confirmed={confirmed_vc}, plausible={plausible_vc}, uncertain={uncertain_vc}")
    print(f"  Findings: {len(findings_raw)}  |  Revision candidates: 0")
    print(f"  Classification: {reg['sb_classification']}  |  Carry forward: {reg['carry_forward']}")
    print(f"  File: {out_path}  ({size_kb:.1f} KB)")
    print(f"{'=' * 60}\n")

    print("  Dominant terms:")
    for t in dominant:
        print(f"    {t['strongs_number']} {t['transliteration']} — {t['verse_count']}v, {t['evidential_status']}")

    print(f"\n  Dimensions: RE={'Y' if dim['relational_environment'] else 'N'}, "
          f"SSB={'Y' if dim['spirit_soul_body'] else 'N'}, "
          f"IO={'Y' if dim['inner_operations'] else 'N'}, "
          f"B={'Y' if dim['being'] else 'N'}")

    return out_path


def main():
    parser = argparse.ArgumentParser(description="Produce final registry extract")
    parser.add_argument("--registry", type=int, required=True, help="Registry number")
    args = parser.parse_args()
    produce_final_extract(args.registry)


if __name__ == "__main__":
    main()
