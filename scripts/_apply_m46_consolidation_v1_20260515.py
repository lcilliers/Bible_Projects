"""Apply WA-M46-patch-consolidation-v1-20260515.json — 5-section consolidation.

Sections (briefing-confirmed):
  A: 18 vcg_term INSERTs (resolves H3 cross-term contamination)
  B: 20 mti_term_subgroup INSERTs (resolves H4 orphaned routing)
  C: 1 verse_context_group CREATE + vcg_term link + verse_context UPDATE for liparos (resolves H7)
  D: 4 verse_context INSERTs (resolves 4 of 7 UT verses)
  E: 13 verse_context UPDATEs (resolves 7 P-status verses, with duplicate vc_id encoding handled)

All 5 sections execute in a single transaction. Backup taken before apply.

CC alignment decisions applied:
  - Section A: skip the liparos→VCG 3709 (7581-001) op because Section C makes it redundant.
    The H3 violation for vc.id=64258 (Rev 18:14 liparos in 7581-001) is resolved instead by
    Section C re-routing that verse to a new dedicated VCG (4702-001). Per AI's note:
    "liparos added to 7581-001 (to be reversed by Section C)". Net effect: same.
    Section A applies 17 ops, not 18.
  - Section E: dedup ops by canonical (verse_record_id, mti_term_id) — AI submitted some ops
    twice (once with correct vr_id, once with vc_id-as-vr_id). 13 ops dedup to 7 unique targets.
  - All UPDATEs include delete_flagged=0 in WHERE to avoid touching soft-deleted duplicate rows
    (the pattern that caused OP-179 to fail on Patch v2 earlier today).

Usage: python scripts/_apply_m46_consolidation_v1_20260515.py [--dry-run]
"""
import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
BACKUP_DIR = REPO / "backups"
PATCH = REPO / "Sessions" / "Session_Clusters" / "M46" / "WA-M46-patch-consolidation-v1-20260515.json"
ARCHIVE_DIR = REPO / "archive" / "patches"

PLACEMENT_NOTE_PREFIX = "WA-M46-patch-consolidation-v1-20260515: "
SKIPPED_A_OP = {"vcg_id": 3709, "add_mti_id": 4702}  # liparos→7581-001 (reversed by C)


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    dry_run = "--dry-run" in sys.argv
    patch = json.loads(PATCH.read_text(encoding="utf-8"))

    # Pre-apply backup
    if not dry_run:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP_DIR / f"bible_research_backup_{ts}_consolidation-v1.db"
        shutil.copy2(DB, backup_path)
        print(f"[BACKUP] {backup_path.name}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    counts = {
        "A_vcg_term_inserts": 0, "A_skipped": 0,
        "B_subgroup_inserts": 0,
        "C_vcg_created_id": None, "C_vcg_term_link": 0, "C_verse_reroute": 0,
        "D_vc_inserts": 0,
        "E_vc_updates": 0, "E_deduped_skip": 0,
    }

    try:
        ts_now = now()

        # ===== SECTION A =====
        for op in patch["section_A_h3_vcg_term_additions"]:
            if op["vcg_id"] == SKIPPED_A_OP["vcg_id"] and op["add_mti_id"] == SKIPPED_A_OP["add_mti_id"]:
                counts["A_skipped"] += 1
                print(f"  [A skip] liparos→VCG {op['vcg_id']} (7581-001) — handled by Section C")
                continue
            note = PLACEMENT_NOTE_PREFIX + "Section A H3 fix: " + op["basis"]
            conn.execute(
                """INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note, delete_flagged, created_at, last_updated_date)
                   VALUES (?, ?, ?, 0, ?, ?)""",
                (op["vcg_id"], op["add_mti_id"], note, ts_now, ts_now)
            )
            counts["A_vcg_term_inserts"] += 1

        # ===== SECTION B =====
        for op in patch["section_B_h4_secondary_subgroup_links"]:
            note = PLACEMENT_NOTE_PREFIX + "Section B H4 fix (secondary subgroup link): " + op["basis"]
            conn.execute(
                """INSERT INTO mti_term_subgroup (mti_term_id, cluster_subgroup_id, placement_note, delete_flagged, created_at, last_updated_date)
                   VALUES (?, ?, ?, 0, ?, ?)""",
                (op["mti_id"], op["subgroup_id"], note, ts_now, ts_now)
            )
            counts["B_subgroup_inserts"] += 1

        # ===== SECTION C =====
        C_op = patch["section_C_h7_liparos_vcg"]
        # Create new VCG
        cur = conn.execute(
            """INSERT INTO verse_context_group (group_code, context_description, notes, delete_flagged, vertical_pass_flag)
               VALUES (?, ?, ?, 0, 0)""",
            (
                C_op["vcg_code"],
                C_op["description"],
                PLACEMENT_NOTE_PREFIX + "Section C H7 fix: dedicated liparos VCG (resolves Rev 18:14 cross-term routing into ploutos VCG).",
            )
        )
        new_vcg_id = cur.lastrowid
        counts["C_vcg_created_id"] = new_vcg_id
        # Insert vcg_term link
        conn.execute(
            """INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note, delete_flagged, created_at, last_updated_date)
               VALUES (?, ?, ?, 0, ?, ?)""",
            (new_vcg_id, C_op["mti_id"], PLACEMENT_NOTE_PREFIX + "Section C: liparos linked to new dedicated VCG.", ts_now, ts_now)
        )
        counts["C_vcg_term_link"] = 1
        # Reroute Rev 18:14 (vc.id=64258 — note: AI's 'anchor_vr_id' field actually holds the vc_id)
        # Update by vc.id directly (verified canonical row in preflight)
        rc = conn.execute(
            """UPDATE verse_context
               SET group_id=?, is_anchor=?
               WHERE id=64258 AND mti_term_id=? AND COALESCE(delete_flagged,0)=0""",
            (new_vcg_id, C_op["is_anchor"], C_op["mti_id"])
        ).rowcount
        if rc != 1:
            raise RuntimeError(f"C reroute: expected 1 row UPDATEd, got {rc}")
        counts["C_verse_reroute"] = rc

        # ===== SECTION D =====
        for op in patch["section_D_vcnew_ut_verses"]:
            # Resolve canonical verse_record_id (preflight confirmed patch vr_id is correct for section D)
            vr_id = op["vr_id"]
            # Defensive lookup if needed
            vr_check = conn.execute("SELECT 1 FROM wa_verse_records WHERE id=? AND mti_term_id=?", (vr_id, op["mti_id"])).fetchone()
            if not vr_check:
                # Try by reference
                vr_lookup = conn.execute(
                    "SELECT id FROM wa_verse_records WHERE reference=? AND mti_term_id=? AND COALESCE(delete_flagged,0)=0 ORDER BY id LIMIT 1",
                    (op["reference"], op["mti_id"])
                ).fetchone()
                if not vr_lookup:
                    raise RuntimeError(f"D insert: no wa_verse_records for {op['reference']} mti={op['mti_id']}")
                vr_id = vr_lookup["id"]
            conn.execute(
                """INSERT INTO verse_context (verse_record_id, mti_term_id, group_id, cluster_subgroup_id,
                                              is_anchor, is_relevant, is_related, notes, delete_flagged, vertical_pass_flag)
                   VALUES (?, ?, ?, ?, ?, ?, 0, ?, 0, 0)""",
                (vr_id, op["mti_id"], op["group_id"], op["subgroup_id"],
                 op.get("is_anchor", 0), op.get("is_relevant", 1),
                 PLACEMENT_NOTE_PREFIX + "Section D VCNEW: " + op["basis"])
            )
            counts["D_vc_inserts"] += 1

        # ===== SECTION E (dedup) =====
        seen_targets = set()
        for op in patch["section_E_vcrevise_p_verses"]:
            # Resolve canonical vr_id (handle vc_id-as-vr_id encoding)
            patch_vr = op["vr_id"]; mti = op["mti_id"]
            vc_at_patch_vr = conn.execute(
                "SELECT id FROM verse_context WHERE verse_record_id=? AND mti_term_id=? AND COALESCE(delete_flagged,0)=0",
                (patch_vr, mti)
            ).fetchone()
            if vc_at_patch_vr:
                canonical_vr = patch_vr
            else:
                vr_lookup = conn.execute(
                    "SELECT id FROM wa_verse_records WHERE reference=? AND mti_term_id=? AND COALESCE(delete_flagged,0)=0 ORDER BY id LIMIT 1",
                    (op["reference"], mti)
                ).fetchone()
                if not vr_lookup:
                    raise RuntimeError(f"E update: no wa_verse_records for {op['reference']} mti={mti}")
                canonical_vr = vr_lookup["id"]
            key = (canonical_vr, mti)
            if key in seen_targets:
                counts["E_deduped_skip"] += 1
                continue
            seen_targets.add(key)
            rc = conn.execute(
                """UPDATE verse_context
                   SET group_id=?, cluster_subgroup_id=?, is_anchor=?
                   WHERE verse_record_id=? AND mti_term_id=? AND COALESCE(delete_flagged,0)=0""",
                (op["group_id"], op["subgroup_id"], op.get("is_anchor", 0), canonical_vr, mti)
            ).rowcount
            if rc != 1:
                raise RuntimeError(f"E update: expected 1 row for {op['reference']} mti={mti}, got {rc}")
            counts["E_vc_updates"] += 1

        if dry_run:
            conn.rollback()
            print("\n[DRY RUN] Rolled back. No changes committed.")
        else:
            conn.commit()
            print("\nCommitted.")

        for k, v in counts.items():
            print(f"  {k}: {v}")

    except Exception as exc:
        conn.rollback()
        print(f"\nERROR: {exc}\nTransaction rolled back. No changes applied.")
        raise
    finally:
        conn.close()

    # Archive patch file on successful live apply
    if not dry_run:
        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
        dest = ARCHIVE_DIR / PATCH.name
        shutil.move(str(PATCH), str(dest))
        print(f"  Archived: {dest.relative_to(REPO)}")


if __name__ == "__main__":
    main()
