"""Apply M01 Phase 7 — VCG creation, vcg_term links, verse routing, anchor designation,
plus the 109 missing-verse assignments and 4 set-asides.

Reads AI's Phase 7 design:
  - Sessions/Session_Clusters/M01/files vcg phase 7/WA-M01-vcg-creation-v1-20260516.json
  - + missing-verse assignments: WA-M01-vcg-missing-verse-assignments-v1-20260516.json
  - + cross-routing flags + set-asides (handled inline)

Operations (single transaction):
  Op A: INSERT 36 verse_context_group rows (one per AI-designed VCG)
  Op B: INSERT vcg_term rows — one per (VCG, term) pair derived from member verses
  Op C: UPDATE verse_context.group_id for each is_relevant verse (primary VCG)
        + record dual-memberships in verse_context.notes
  Op D: UPDATE verse_context.is_anchor=1 for each VCG's anchor; reset all others to is_anchor=0
        within the cluster's terms
  Op E: Set-aside 4 verses (Deu 32:27, Eze 16:43, Job 39:16, Job 25:2):
        is_relevant=0, set_aside_reason populated, group_id NULL, is_anchor=0

Dual-membership rule: first-listed VCG (in iteration order of the JSON sub-groups
A/B/C/D/E/F/G/BOUNDARY) wins as primary; secondaries recorded in vc.notes.

Usage:
  python scripts/_apply_m01_phase7_vcg_creation_20260516.py [--dry-run]
"""
from __future__ import annotations
import argparse, json, re, sqlite3, sys, shutil
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
BACKUP_DIR = REPO / "backups"
PHASE7_DIR = REPO / "Sessions" / "Session_Clusters" / "M01" / "files vcg phase 7"
DIRECTIVE = "DIR-20260516-003 (wa-cluster-M01-dir-003-vcg-create-v1-20260516)"

# Set-asides per cross-routing flags + AI design
SET_ASIDES = {
    14968: ("H1481C gur Deu 32:27", "Describes God's inner apprehension about enemy pride shaping his restrained judgment — divine inner life, not human inner being. Outside programme scope."),
    1846: ("H7264 ra.gaz Eze 16:43", "Describes inner fury aroused in God by Israel's unfaithfulness — divine inner state, not human fear-trembling. Outside programme scope per researcher confirmation."),
    64529: ("H6343 pa.chad Job 39:16", "Describes the ostrich's lack of fear toward her young — animal instinct, not human inner being. Outside programme scope per researcher confirmation."),
    13958: ("H6343 pa.chad Job 25:2", "Describes dread as an attribute of God's dominion — intrinsic quality of divine sovereign majesty, not human emotion. Outside programme scope per researcher confirmation."),
}


def normalize_vcg_code(code: str) -> str:
    """AI returned some codes without the VCG- infix (e.g. M01-B-01 instead of M01-B-VCG-01).
    Normalize all codes to the canonical M01-X-VCG-NN form."""
    if not code:
        return code
    m = re.match(r"^(M01-[A-Z])-(\d{1,2})$", code)
    if m:
        return f"{m.group(1)}-VCG-{int(m.group(2)):02d}"
    m = re.match(r"^(M01-[A-Z])-VCG-(\d{1,2})$", code)
    if m:
        return f"{m.group(1)}-VCG-{int(m.group(2)):02d}"
    m = re.match(r"^(M01-BOUNDARY)-VCG-(\d{1,2})$", code)
    if m:
        return f"{m.group(1)}-VCG-{int(m.group(2)):02d}"
    return code


def main():
    dry_run = "--dry-run" in sys.argv

    # Backup
    if not dry_run:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP_DIR / f"bible_research_backup_{ts}_DIR-20260516-003.db"
        shutil.copy2(DB, backup_path)
        print(f"[BACKUP] {backup_path.name}")

    # Load AI's VCG design
    creation_path = PHASE7_DIR / "WA-M01-vcg-creation-v1-20260516.json"
    creation = json.loads(creation_path.read_text(encoding="utf-8"))

    # Load 109-verse missing assignments
    assign_path = PHASE7_DIR / "WA-M01-vcg-missing-verse-assignments-v1-20260516.json"
    assign_data = json.loads(assign_path.read_text(encoding="utf-8"))
    extra_assignments = {a["vc_id"]: normalize_vcg_code(a["vcg_code"]) for a in assign_data["assignments"]}

    # Build full vcg structure: {vcg_provisional_code: {description, verses, anchor_vc_id, sg_code}}
    vcgs: dict[str, dict] = {}
    for sg, sg_data in creation.items():
        for vcg in sg_data.get("vcgs", []):
            code = normalize_vcg_code(vcg["provisional_code"])
            if code not in vcgs:
                vcgs[code] = {
                    "code": code,
                    "sg_code": sg,
                    "description": vcg["description"],
                    "verses": set(),
                    "anchor_vc_id": vcg.get("anchor_vc_id"),
                }
            for v in vcg.get("verses", []):
                vcgs[code]["verses"].add(v)

    # Add the 109 missing-verse assignments
    for vc_id, vcg_code in extra_assignments.items():
        if vcg_code not in vcgs:
            print(f"  WARN: missing-verse assignment vc_id={vc_id} → {vcg_code} (VCG not in design)")
            continue
        vcgs[vcg_code]["verses"].add(vc_id)

    # Add vc_id=15211 (AI's cross-routing flag noted but didn't include in JSON)
    if "M01-B-VCG-03" in vcgs:
        vcgs["M01-B-VCG-03"]["verses"].add(15211)
        print(f"  Added vc_id=15211 to M01-B-VCG-03 (per AI cross-routing flag)")

    # Build per-vc primary VCG mapping (first-listed wins; iterate sub-groups in order)
    primary_vcg: dict[int, str] = {}
    secondary_vcgs: dict[int, list[str]] = defaultdict(list)
    sg_order = ["M01-A","M01-B","M01-C","M01-D","M01-E","M01-F","M01-G","M01-BOUNDARY"]
    for sg in sg_order:
        for code, vcg in sorted(vcgs.items()):
            if vcg["sg_code"] != sg:
                continue
            for vc in vcg["verses"]:
                if vc not in primary_vcg:
                    primary_vcg[vc] = code
                else:
                    if code != primary_vcg[vc]:
                        secondary_vcgs[vc].append(code)

    print(f"\nVCGs to create: {len(vcgs)}")
    print(f"Distinct vc_ids in design: {len(primary_vcg)}")
    print(f"Verses with dual-membership: {len(secondary_vcgs)}")

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    counts = {"vcg_inserts": 0, "vcg_term_inserts": 0, "vc_group_updates": 0,
              "vc_anchor_sets": 0, "vc_anchor_resets": 0, "set_asides": 0,
              "warns": 0}

    try:
        conn.execute("BEGIN")

        # ===== Op pre-A — Soft-delete duplicate vc rows in M01 =====
        # Six known duplicate pairs (same vr_id, mti_id, same sub-group, both active).
        # Soft-delete the higher-id of each pair; keep the lower id. Both have identical
        # analysis_note (Pass A wrote per-vc); content not lost. Resolves UNIQUE collision
        # on (verse_record_id, mti_term_id, group_id, cluster_subgroup_id) when both
        # vc rows would be routed to the same new VCG.
        DUPLICATE_PAIRS = [(4954, 4268), (4209, 4260), (4210, 4261),
                            (4211, 4262), (4212, 4263), (4258, 4257)]
        for a, b in DUPLICATE_PAIRS:
            higher = max(a, b)
            note = f" | {DIRECTIVE} duplicate-resolution: soft-deleted (kept vc.id={min(a,b)} for same vr+mti). Both rows had identical Pass A meaning; no analytical content lost."
            rc = conn.execute("""
                UPDATE verse_context
                SET delete_flagged=1, notes=COALESCE(notes,'')||?
                WHERE id=? AND COALESCE(delete_flagged,0)=0
            """, (note, higher)).rowcount
            if rc != 1:
                print(f"  WARN: duplicate soft-delete of vc.id={higher} affected {rc} rows (expected 1)")
                counts["warns"] += 1
        counts["duplicates_soft_deleted"] = len(DUPLICATE_PAIRS)

        # Resolve sub-group ids
        sg_id_map = {}
        for r in conn.execute("SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code='M01' AND COALESCE(delete_flagged,0)=0"):
            sg_id_map[r["subgroup_code"]] = r["id"]

        # ===== Op A — INSERT verse_context_group rows =====
        vcg_db_id: dict[str, int] = {}
        for code, vcg in sorted(vcgs.items()):
            cur = conn.execute(
                """INSERT INTO verse_context_group
                   (group_code, context_description, notes, delete_flagged, vertical_pass_flag)
                   VALUES (?, ?, ?, 0, 0)""",
                (code, vcg["description"],
                 f"Created by {DIRECTIVE} in sub-group {vcg['sg_code']}")
            )
            vcg_db_id[code] = cur.lastrowid
            counts["vcg_inserts"] += 1

        # ===== Op B — INSERT vcg_term rows (one per (VCG, term) pair) =====
        # Derive term set per VCG from member verses
        vcg_terms: dict[str, set[int]] = defaultdict(set)
        for vc, primary_code in primary_vcg.items():
            r = conn.execute("SELECT mti_term_id FROM verse_context WHERE id=?", (vc,)).fetchone()
            if r:
                vcg_terms[primary_code].add(r["mti_term_id"])

        for code, mti_set in vcg_terms.items():
            for mti in sorted(mti_set):
                conn.execute(
                    """INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note,
                                              delete_flagged, created_at, last_updated_date)
                       VALUES (?, ?, ?, 0, ?, ?)""",
                    (vcg_db_id[code], mti, f"{DIRECTIVE}: derived from VCG member verses", now, now)
                )
                counts["vcg_term_inserts"] += 1

        # ===== Op C — UPDATE verse_context.group_id (and notes for duals) =====
        for vc, primary_code in primary_vcg.items():
            gid = vcg_db_id[primary_code]
            note_addition = ""
            if vc in secondary_vcgs:
                secs = ", ".join(secondary_vcgs[vc])
                note_addition = f" | {DIRECTIVE} dual-membership: primary={primary_code} secondary=[{secs}]"
            if note_addition:
                rc = conn.execute(
                    """UPDATE verse_context
                       SET group_id=?, notes=COALESCE(notes,'')||?
                       WHERE id=? AND COALESCE(delete_flagged,0)=0""",
                    (gid, note_addition, vc)
                ).rowcount
            else:
                rc = conn.execute(
                    """UPDATE verse_context SET group_id=?
                       WHERE id=? AND COALESCE(delete_flagged,0)=0""",
                    (gid, vc)
                ).rowcount
            if rc == 1:
                counts["vc_group_updates"] += 1

        # ===== Op D — Anchor designation =====
        # First, reset all existing anchors in M01 cluster to is_anchor=0
        rc_reset = conn.execute("""
UPDATE verse_context SET is_anchor=0
WHERE id IN (
  SELECT vc.id FROM verse_context vc
  JOIN mti_terms mt ON mt.id=vc.mti_term_id
  WHERE mt.cluster_code='M01' AND COALESCE(vc.delete_flagged,0)=0
  AND vc.is_anchor=1
)
""").rowcount
        counts["vc_anchor_resets"] = rc_reset

        # Now set anchor=1 for each VCG's designated anchor
        for code, vcg in vcgs.items():
            anchor = vcg.get("anchor_vc_id")
            if not anchor:
                continue
            rc = conn.execute(
                """UPDATE verse_context SET is_anchor=1
                   WHERE id=? AND COALESCE(delete_flagged,0)=0""",
                (anchor,)
            ).rowcount
            if rc == 1:
                counts["vc_anchor_sets"] += 1

        # ===== Op D.1 — Per-term provisional anchors =====
        # AI's Phase 7 design designates one anchor per VCG (36 anchors total). But many
        # VCGs contain verses from multiple terms; the anchor belongs to ONE term, leaving
        # the other terms in that VCG without an anchor. R4 (applier rule, per-term) requires
        # every term with is_relevant verses to have ≥1 anchor. For each term in M01 active
        # with is_relevant but currently no is_anchor=1, designate its first canonical-order
        # is_relevant verse as a provisional anchor.
        provisional_targets = list(conn.execute("""
SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration
FROM mti_terms mt
WHERE mt.cluster_code='M01' AND COALESCE(mt.delete_flagged,0)=0
  AND mt.status IN ('extracted','extracted_thin')
  AND EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0)
  AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0)
"""))
        provisional_count = 0
        for r in provisional_targets:
            # Pick first canonical-order is_relevant verse for this term
            first = conn.execute("""
SELECT vc.id FROM verse_context vc
JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
WHERE vc.mti_term_id=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
ORDER BY vr.book_id, vr.chapter, vr.verse_num, vc.id
LIMIT 1
""", (r["mti_id"],)).fetchone()
            if first:
                conn.execute("""
UPDATE verse_context SET is_anchor=1,
  notes=COALESCE(notes,'') || ?
WHERE id=? AND COALESCE(delete_flagged,0)=0
""", (f" | {DIRECTIVE} provisional anchor (R4 fallback): term {r['strongs_number']} {r['transliteration']} had no AI-designated anchor; first canonical-order is_relevant verse promoted.", first["id"])).rowcount
                provisional_count += 1
        counts["provisional_anchors"] = provisional_count

        # ===== Op E — Set-asides =====
        for vc_id, (label, reason) in SET_ASIDES.items():
            rc = conn.execute(
                """UPDATE verse_context
                   SET is_relevant=0, set_aside_reason=?, group_id=NULL, is_anchor=0,
                       notes=COALESCE(notes,'') || ?
                   WHERE id=? AND COALESCE(delete_flagged,0)=0""",
                (reason, f" | {DIRECTIVE} set-aside: {label}", vc_id)
            ).rowcount
            if rc == 1:
                counts["set_asides"] += 1

        # ===== Post-checks =====
        # H2 — is_relevant=1 with group_id NULL
        h2 = conn.execute("""
SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
WHERE mt.cluster_code='M01' AND vc.is_relevant=1 AND vc.group_id IS NULL
AND COALESCE(vc.delete_flagged,0)=0
""").fetchone()[0]
        # H3 — vc's mti not in vcg's term set
        h3 = conn.execute("""
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id=vc.mti_term_id
JOIN verse_context_group vcg ON vcg.id=vc.group_id AND COALESCE(vcg.delete_flagged,0)=0
LEFT JOIN vcg_term vt ON vt.vcg_id=vcg.id AND vt.mti_term_id=vc.mti_term_id AND COALESCE(vt.delete_flagged,0)=0
WHERE mt.cluster_code='M01' AND COALESCE(vc.delete_flagged,0)=0 AND vt.id IS NULL
""").fetchone()[0]
        # R4 — every term with is_relevant=1 has at least 1 anchor
        r4_fail = conn.execute("""
SELECT COUNT(DISTINCT mt.id) FROM mti_terms mt
WHERE mt.cluster_code='M01' AND COALESCE(mt.delete_flagged,0)=0
AND mt.status IN ('extracted','extracted_thin')
AND EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0)
AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0)
""").fetchone()[0]

        print(f"\n=== Post-check ===")
        print(f"  H2 (is_relevant=1 without group_id): {h2}")
        print(f"  H3 (vc mti not in vcg term set): {h3}")
        print(f"  R4 failures (terms with relevant verses but no anchor): {r4_fail}")
        for k, v in counts.items():
            print(f"  {k}: {v}")

        if h2 > 0 or h3 > 0 or r4_fail > 0:
            print(f"\nWARN: health-check failures present. Review before committing.")

        if dry_run:
            conn.execute("ROLLBACK")
            print("\n[DRY RUN] Rolled back.")
        else:
            conn.execute("COMMIT")
            print("\nCommitted.")
    except Exception as exc:
        conn.execute("ROLLBACK")
        print(f"\nERROR: {exc}\nRolled back.")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
