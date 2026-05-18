"""Build the M04 special-case patch covering the 4 orphan vcs.

Researcher-approved 2026-05-18:
- Case A — Dan 1:10 (vc=23405, H1524A gil): SET-ASIDE + raise M01_INGEST_CANDIDATE flag
- Case B — Psa 81:2 (vc=28388, H5273A na.im): SET-ASIDE with §4.5.1 reason
- Case C — 2Sa 23:1 (vc=28385, H5273A na.im): RESTORE vr + leave vc in M04-J for Pass A
- Case D — Ezr 6:16 (vc=23418, H2304 ched.vah): RESTORE vr + reassign to M04-B; INSERT mti_term_subgroup link

Output: Sessions/Patches/wa-cluster-M04-repair-special-cases-v1-{date}.json
"""
from __future__ import annotations
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
NOW_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUT = Path(f"Sessions/Patches/wa-cluster-M04-repair-special-cases-v1-{TODAY}.json")


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Confirm M04-B id (89)
    m04b = conn.execute("SELECT id FROM cluster_subgroup WHERE cluster_code='M04' AND subgroup_code='M04-B'").fetchone()
    assert m04b and m04b["id"] == 89, f"unexpected M04-B id: {m04b}"

    # Confirm H2304 ched.vah (mti=356) has no active link to M04-B
    existing = conn.execute(
        "SELECT id, delete_flagged FROM mti_term_subgroup WHERE mti_term_id=356 AND cluster_subgroup_id=89"
    ).fetchone()
    if existing and not existing["delete_flagged"]:
        raise RuntimeError(f"Unexpected: H2304 already has active mti_term_subgroup to M04-B (id={existing['id']})")
    # If a deleted link exists we'd need different handling; verified by recon that none exists.

    operations = []

    # --- Case A: Dan 1:10 SET-ASIDE + research flag ---
    operations.append({
        "op_id": "OP-00001",
        "operation": "update",
        "table": "verse_context",
        "match": {"id": 23405},
        "set": {
            "is_relevant": 0,
            "is_anchor": 0,
            "cluster_subgroup_id": None,
            "group_id": None,
            "set_aside_reason": (
                "gil reference at Dan 1:10 — verse describes Daniel's fear of the king "
                "('I fear my lord the king, who has appointed your food and your drink'), "
                "not joy/rejoicing. STEP surfaced gil but no inner-joy sense is evidenced "
                "in the verse content. Verse semantically belongs to fear register (M01) "
                "but no fear-cluster term currently has an entry at Dan 1:10 — would "
                "need M01 ingest pass to add one. Set-aside per v2_5 §4.5.1; flagged for "
                "M01 ingest review via M01_INGEST_CANDIDATE research flag."
            ),
            "notes": f"[audit-fix v2_5 special-case 2026-05-18] Case A — Dan 1:10 disposition per researcher approval. Was orphan vc (vr=11725 deleted).",
        },
        "description": "M04 special-case A — Dan 1:10 H1524A gil → SET-ASIDE (verse describes fear, not joy; flagged for M01)",
    })

    operations.append({
        "op_id": "OP-00002",
        "operation": "insert",
        "table": "wa_session_research_flags",
        "values": {
            "registry_id": 61,  # fear registry (M01 target)
            "cross_registry_id": 97,  # joy registry (source — gil's home)
            "flag_code": "M01_INGEST_CANDIDATE",
            "flag_label": "M01 Fear cluster — verse-ingest candidate",
            "strongs_reference": None,
            "priority": "advisory",
            "session_target": "M01-ingest",
            "description": (
                "Dan 1:10 — Daniel-chief-eunuchs scene; verse explicitly says 'I fear my lord the king' "
                "in English. No M01 (Fear cluster) term currently extracted at this verse — only "
                "H1524A gil (M04 joy) was surfaced by STEP, but gil has no inner-joy sense here. "
                "Consider adding an appropriate fear-term anchor (ya.re, pa.chad, or similar) when "
                "next M01 ingest pass runs. Raised from M04 audit-fix 2026-05-18 (researcher direction)."
            ),
            "session_raised": "session_20260518",
            "raised_date": NOW_UTC,
            "resolved": 0,
        },
        "description": "Raise M01_INGEST_CANDIDATE flag for Dan 1:10 (registry=fear/61, cross=joy/97)",
    })

    # --- Case B: Psa 81:2 SET-ASIDE ---
    operations.append({
        "op_id": "OP-00003",
        "operation": "update",
        "table": "verse_context",
        "match": {"id": 28388},
        "set": {
            "is_relevant": 0,
            "is_anchor": 0,
            "cluster_subgroup_id": None,
            "group_id": None,
            "set_aside_reason": (
                "na.im at Psa 81:2 is used as a descriptive adjective of a musical instrument "
                "('the sweet lyre with the harp'), not inner-being content — outside M04 "
                "inner-being scope. The verse-level joy register sits in the surrounding "
                "'sing aloud / raise a song / sound the tambourine' context (carried by other "
                "Hebrew verbs of praise), but na.im itself here is the instrument-quality "
                "adjective applied to the lyre. Set-aside per v2_5 §4.5.1."
            ),
            "notes": "[audit-fix v2_5 special-case 2026-05-18] Case B — Psa 81:2 disposition per researcher approval. Was orphan vc (vr=4368 deleted, kept deleted).",
        },
        "description": "M04 special-case B — Psa 81:2 H5273A na.im → SET-ASIDE (instrument-quality adjective, not inner state)",
    })

    # --- Case C: 2Sa 23:1 RESTORE vr (vc stays in M04-J for Pass A pickup) ---
    operations.append({
        "op_id": "OP-00004",
        "operation": "update",
        "table": "wa_verse_records",
        "match": {"id": 4364},
        "set": {
            "delete_flagged": 0,
        },
        "description": "M04 special-case C — restore vr=4364 (2Sa 23:1) so vc=28385 has a live underlying verse_record",
    })

    # vc=28385 stays as-is (is_relevant=1, M04-J, no analysis_note). Pass A will pick it up next.
    operations.append({
        "op_id": "OP-00005",
        "operation": "update",
        "table": "verse_context",
        "match": {"id": 28385},
        "set": {
            "notes": "[audit-fix v2_5 special-case 2026-05-18] Case C — orphan vr=4364 restored; Pass A meaning to be authored next.",
        },
        "description": "M04 special-case C — annotate vc=28385 with audit note (Pass A authoring pending)",
    })

    # --- Case D: Ezr 6:16 RESTORE vr + REASSIGN sub-group + INSERT mti_term_subgroup ---
    operations.append({
        "op_id": "OP-00006",
        "operation": "update",
        "table": "wa_verse_records",
        "match": {"id": 11626},
        "set": {
            "delete_flagged": 0,
        },
        "description": "M04 special-case D — restore vr=11626 (Ezr 6:16) so vc=23418 has a live underlying verse_record",
    })

    operations.append({
        "op_id": "OP-00007",
        "operation": "insert",
        "table": "mti_term_subgroup",
        "values": {
            "mti_term_id": 356,
            "cluster_subgroup_id": 89,  # M04-B
            "placement_note": "[primary, audit-fix v2_5 2026-05-18] H2304 ched.vah Ezr 6:16 corporate temple-dedication joy; assigned to M04-B Communal/Festive Rejoicing per researcher direction.",
            "delete_flagged": 0,
            "created_at": NOW_UTC,
            "last_updated_date": NOW_UTC,
        },
        "description": "M04 special-case D — INSERT mti_term_subgroup link for H2304 ched.vah → M04-B (no prior link existed)",
    })

    operations.append({
        "op_id": "OP-00008",
        "operation": "update",
        "table": "verse_context",
        "match": {"id": 23418},
        "set": {
            "cluster_subgroup_id": 89,  # M04-B
            "group_id": None,  # VCG to be re-assigned in step 5 of cascade
            "is_anchor": 0,
            "notes": "[audit-fix v2_5 special-case 2026-05-18] Case D — re-assigned from M04-C (NT Joy) to M04-B (Communal/Festive Rejoicing). Underlying vr=11626 restored. Pass A meaning + VCG assignment pending.",
        },
        "description": "M04 special-case D — Ezr 6:16 H2304 ched.vah → re-assign to M04-B; clear group_id (VCG TBD)",
    })

    patch = {
        "_patch_meta": {
            "patch_id": f"PATCH-{TODAY}-M04-REPAIR-SPECIAL-CASES-V1",
            "registry_id": None,
            "produced_date": TODAY,
            "produced_by": "scripts/_build_m04_special_cases_patch_20260518.py",
            "patch_type": "REPAIR",
            "cluster_code": "M04",
            "session_b_status": None,
            "governing_instruction": "wa-sessionb-cluster-instruction-v2_5-20260518 §17.5 (audit-fix) + §18.2 (verse-level dispositions)",
            "description": (
                "Four special-case orphan vc dispositions per researcher approval 2026-05-18:\n"
                "  A) Dan 1:10 H1524A gil → SET-ASIDE + raise M01_INGEST_CANDIDATE research flag\n"
                "  B) Psa 81:2 H5273A na.im → SET-ASIDE (instrument-quality adjective)\n"
                "  C) 2Sa 23:1 H5273A na.im → restore vr=4364; keep in M04-J; Pass A pending\n"
                "  D) Ezr 6:16 H2304 ched.vah → restore vr=11626; reassign to M04-B; "
                "INSERT mti_term_subgroup link; Pass A + VCG assignment pending"
            ),
        },
        "_patch_summary": {
            "total_operations": len(operations),
            "set_aside_count": 2,
            "vr_restore_count": 2,
            "subgroup_reassign_count": 1,
            "mti_term_subgroup_insert_count": 1,
            "research_flag_insert_count": 1,
            "produced_at_utc": NOW_UTC,
        },
        "operations": operations,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(patch, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Patch written: {OUT}")
    print(f"Operations: {len(operations)}")
    conn.close()


if __name__ == "__main__":
    main()
