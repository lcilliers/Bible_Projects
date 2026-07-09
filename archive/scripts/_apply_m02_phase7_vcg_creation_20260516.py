"""Apply M02 Phase 7 — VCG creation, vcg_term links, verse routing, anchor designation.

Reads AI's Phase 7 design + the 39 missing-verse assignments:
  - Sessions/Session_Clusters/M02/WA-M02-vcg-creation-v1-20260516.json
  - Sessions/Session_Clusters/M02/WA-M02-vcg-missing-verse-assignments-v1-20260516.json

Operations (single transaction):
  Op A: INSERT 26 verse_context_group rows
  Op B: INSERT vcg_term rows (one per (VCG, term) pair derived from member verses)
  Op C: UPDATE verse_context.group_id for each is_relevant verse (primary VCG)
        + record dual-memberships in verse_context.notes
  Op D: Reset all M02 anchors to is_anchor=0; set is_anchor=1 for each VCG's designated anchor
  Op D.1: R4 fallback — provisional per-term anchors for terms whose verses don't include
          an AI-designated anchor

No Op E set-asides (AI flagged 0 candidates per WA-M02-phase7-cross-routing-flags-v1-20260516.md §2).
No duplicate soft-deletes (M02 has no known duplicate vc rows).

Phantom vc_id filtering:
  vc=64718, 64660, 285 — exist but is_relevant=0 (AI mistakenly routed set-aside rows)
  vc=356, 399 — don't exist in verse_context at all (AI typos)
These are dropped from each VCG's verse list before processing.
"""
from __future__ import annotations
import argparse, json, sqlite3, sys, shutil
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
BACKUP_DIR = REPO / "backups"
M02 = REPO / "Sessions" / "Session_Clusters" / "M02"
CREATION_JSON = M02 / "WA-M02-vcg-creation-v1-20260516.json"
ASSIGN_JSON = M02 / "WA-M02-vcg-missing-verse-assignments-v1-20260516.json"
DIRECTIVE = "DIR-20260516-010 (wa-cluster-M02-dir-003-vcg-create-v1-20260516)"

PHANTOM_VC_IDS = {64718, 64660, 285, 356, 399}
SG_ORDER = ["M02-A", "M02-B", "M02-C", "M02-D", "M02-E", "M02-F", "M02-BOUNDARY"]


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def main():
    dry_run = "--dry-run" in sys.argv or "--live" not in sys.argv

    log(f"M02 Phase 7 — directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP_DIR / f"bible_research_backup_{ts}_DIR-20260516-010.db"
        shutil.copy2(DB, backup_path)
        log(f"Backup: {backup_path.name}")

    # Load AI's VCG design
    creation = json.loads(CREATION_JSON.read_text(encoding="utf-8"))
    assign_data = json.loads(ASSIGN_JSON.read_text(encoding="utf-8"))
    extra_assignments = {a["vc_id"]: a["vcg"] for a in assign_data["assignments"]}
    log(f"Missing-verse assignments to merge: {len(extra_assignments)}")

    # Build vcg structure: {code: {description, verses, anchor_vc_id, sg_code}}
    vcgs: dict[str, dict] = {}
    for sg, sg_data in creation["subgroup_vcgs"].items():
        for vcg in sg_data.get("vcgs", []):
            code = vcg["provisional_code"]
            if code not in vcgs:
                vcgs[code] = {
                    "code": code,
                    "sg_code": sg,
                    "description": vcg["description"],
                    "verses": set(),
                    "anchor_vc_id": vcg.get("anchor_vc_id"),
                }
            for v in vcg.get("verses", []):
                if v in PHANTOM_VC_IDS:
                    continue
                vcgs[code]["verses"].add(v)

    phantom_filtered = sum(
        1 for sg_data in creation["subgroup_vcgs"].values()
        for vcg in sg_data.get("vcgs", [])
        for v in vcg.get("verses", []) if v in PHANTOM_VC_IDS
    )
    log(f"Phantom vc_ids filtered: {phantom_filtered}")

    # Merge missing-verse assignments
    for vc_id, vcg_code in extra_assignments.items():
        if vcg_code not in vcgs:
            log(f"  WARN: missing-verse assignment vc_id={vc_id} → {vcg_code} (VCG not in design)")
            continue
        vcgs[vcg_code]["verses"].add(vc_id)

    # Build per-vc primary VCG mapping (first-listed wins; iterate sub-groups in canonical order)
    primary_vcg: dict[int, str] = {}
    secondary_vcgs: dict[int, list[str]] = defaultdict(list)
    for sg in SG_ORDER:
        for code, vcg in sorted(vcgs.items()):
            if vcg["sg_code"] != sg:
                continue
            for vc in vcg["verses"]:
                if vc not in primary_vcg:
                    primary_vcg[vc] = code
                else:
                    if code != primary_vcg[vc]:
                        secondary_vcgs[vc].append(code)

    log(f"\nVCGs to create: {len(vcgs)}")
    log(f"Distinct vc_ids routed (primary): {len(primary_vcg)}")
    log(f"Verses with dual-membership: {len(secondary_vcgs)}")

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    counts = {"vcg_inserts": 0, "vcg_term_inserts": 0, "vc_group_updates": 0,
              "vc_anchor_sets": 0, "vc_anchor_resets": 0, "warns": 0,
              "provisional_anchors": 0}

    try:
        conn.execute("BEGIN")

        # ===== Pre-check =====
        # cluster.status must be Analysis - In Progress
        st = conn.execute("SELECT status FROM cluster WHERE cluster_code='M02'").fetchone()
        if not st or st["status"] != "Analysis - In Progress":
            raise RuntimeError(f"cluster.status M02 expected 'Analysis - In Progress', got {st and st['status']!r}")
        log(f"  cluster.status M02 = {st['status']} ✓")

        # Resolve sub-group ids
        sg_id_map = {}
        for r in conn.execute("SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code='M02' AND COALESCE(delete_flagged,0)=0"):
            sg_id_map[r["subgroup_code"]] = r["id"]

        # ===== Op A — INSERT verse_context_group rows =====
        log(f"\n=== Op A — INSERT verse_context_group ===")
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
        log(f"  INSERTed {counts['vcg_inserts']} VCG rows")

        # ===== Op B — INSERT vcg_term rows =====
        log(f"\n=== Op B — INSERT vcg_term ===")
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
        log(f"  INSERTed {counts['vcg_term_inserts']} vcg_term rows")

        # ===== Op C — UPDATE verse_context.group_id (and notes for duals) =====
        log(f"\n=== Op C — UPDATE verse_context.group_id ===")
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
        log(f"  UPDATEd {counts['vc_group_updates']} verse_context.group_id values")

        # ===== Op D — Anchor reset + designation =====
        log(f"\n=== Op D — Anchor designation ===")
        rc_reset = conn.execute("""
            UPDATE verse_context SET is_anchor=0
            WHERE id IN (
              SELECT vc.id FROM verse_context vc
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
              WHERE mt.cluster_code='M02' AND COALESCE(vc.delete_flagged,0)=0
              AND vc.is_anchor=1
            )
        """).rowcount
        counts["vc_anchor_resets"] = rc_reset
        log(f"  Reset {rc_reset} prior M02 anchors")

        for code, vcg in vcgs.items():
            anchor = vcg.get("anchor_vc_id")
            if not anchor:
                continue
            if anchor in PHANTOM_VC_IDS:
                log(f"  WARN: anchor for {code} is phantom vc={anchor}; skipping")
                counts["warns"] += 1
                continue
            rc = conn.execute(
                """UPDATE verse_context SET is_anchor=1
                   WHERE id=? AND COALESCE(delete_flagged,0)=0""",
                (anchor,)
            ).rowcount
            if rc == 1:
                counts["vc_anchor_sets"] += 1
            else:
                log(f"  WARN: anchor designation for {code} (vc={anchor}) affected {rc} rows")
                counts["warns"] += 1
        log(f"  Set {counts['vc_anchor_sets']} VCG-anchor designations")

        # ===== Op D.1 — R4 provisional anchors (per-term fallback) =====
        log(f"\n=== Op D.1 — R4 provisional anchors ===")
        provisional_targets = list(conn.execute("""
            SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration
            FROM mti_terms mt
            WHERE mt.cluster_code='M02' AND COALESCE(mt.delete_flagged,0)=0
              AND mt.status IN ('extracted','extracted_thin')
              AND EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id
                            AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0)
              AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id
                                AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0)
        """))
        for r in provisional_targets:
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
                """, (f" | {DIRECTIVE} provisional anchor (R4 fallback): term {r['strongs_number']} {r['transliteration']} had no AI-designated anchor; first canonical-order is_relevant verse promoted.", first["id"]))
                counts["provisional_anchors"] += 1
        log(f"  Set {counts['provisional_anchors']} provisional per-term anchors")

        # ===== Post-checks =====
        log(f"\n=== Post-checks ===")
        h2 = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
            WHERE mt.cluster_code='M02' AND vc.is_relevant=1 AND vc.group_id IS NULL
              AND COALESCE(vc.delete_flagged,0)=0
        """).fetchone()[0]
        h3 = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id=vc.mti_term_id
            JOIN verse_context_group vcg ON vcg.id=vc.group_id AND COALESCE(vcg.delete_flagged,0)=0
            LEFT JOIN vcg_term vt ON vt.vcg_id=vcg.id AND vt.mti_term_id=vc.mti_term_id AND COALESCE(vt.delete_flagged,0)=0
            WHERE mt.cluster_code='M02' AND COALESCE(vc.delete_flagged,0)=0 AND vt.id IS NULL
        """).fetchone()[0]
        r4_fail = conn.execute("""
            SELECT COUNT(DISTINCT mt.id) FROM mti_terms mt
            WHERE mt.cluster_code='M02' AND COALESCE(mt.delete_flagged,0)=0
              AND mt.status IN ('extracted','extracted_thin')
              AND EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0)
              AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0)
        """).fetchone()[0]

        log(f"  H2 (is_relevant=1 without group_id): {h2} ({'✓' if h2==0 else '✗'})")
        log(f"  H3 (vc mti not in vcg term set): {h3} ({'✓' if h3==0 else '✗'})")
        log(f"  R4 failures: {r4_fail} ({'✓' if r4_fail==0 else '✗'})")
        for k, v in counts.items():
            log(f"  {k}: {v}")

        if h2 > 0 or h3 > 0 or r4_fail > 0:
            raise RuntimeError(f"Health-check failures: H2={h2} H3={h3} R4={r4_fail}")

        if dry_run:
            conn.execute("ROLLBACK")
            log("\nDRY RUN — Rolled back.")
        else:
            conn.execute("COMMIT")
            log("\nCommitted.")
    except Exception as exc:
        try: conn.execute("ROLLBACK")
        except: pass
        log(f"\nERROR: {exc}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
