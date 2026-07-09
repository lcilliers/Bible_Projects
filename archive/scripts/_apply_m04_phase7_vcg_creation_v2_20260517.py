"""Apply M04 Phase 7 v2 — VCG creation, vcg_term links, verse routing, anchor designation.

Reads AI's Phase 7 v2 design:
  Sessions/Session_Clusters/M04/files phase 7/WA-M04-vcg-creation-v2-20260517.json

Per §10.9 pre-apply validation (already passed):
  - 1138 vc_ids in JSON = 1138 active is_relevant M04 vc rows in DB ✓
  - 0 phantoms / 0 gaps / 0 cross-sub-group leaks / 0 anchor issues / 0 cross-VCG dups
  - Per-sub-group sums all match DB

Operations (single transaction):
  Op A: INSERT 30 verse_context_group rows
  Op B: INSERT vcg_term rows (one per (VCG, term) pair from member verses)
  Op C: UPDATE verse_context.group_id for each is_relevant verse (primary VCG)
  Op D: Reset all M04 is_anchor=0; set is_anchor=1 per VCG anchor designation
  Op D.1: R4 fallback — provisional per-term anchors for terms whose verses
          don't include an AI-designated anchor

Directive: DIR-20260517-008
"""
from __future__ import annotations
import argparse, json, re, shutil, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
M04 = REPO / "Sessions" / "Session_Clusters" / "M04"
CREATION_JSON = M04 / "files phase 7" / "WA-M04-vcg-creation-v2-20260517.json"
DIRECTIVE = "DIR-20260517-008"
CLUSTER = "M04"
SG_ORDER = ["M04-A", "M04-B", "M04-C", "M04-D", "M04-E", "M04-F",
            "M04-G", "M04-H", "M04-I", "M04-J", "M04-BOUNDARY"]

# Legacy (vr, mti) duplicates among M04 is_relevant active rows.
# Three pairs of cha.phets (H2654A) vc rows share the same (verse_record_id, mti_term_id)
# tuple. Both rows in each pair are is_relevant=1 and route to the same sub-group VCG.
# Under v2_4 single-VCG primary routing, both can't UPDATE to the same group_id
# (UNIQUE (vr, mti, group_id, cluster_subgroup_id)). Keep the lower vc_id; soft-delete
# the higher. Same pattern as M03's Hab 1:3 a.mal handling.
LEGACY_DUP_SOFT_DELETES: dict[int, str] = {
    9456: ("Isa 65:12 cha.phets H2654A — legacy (vr,mti) duplicate. Sibling vc=9412 "
           "retained for VCG routing. Soft-deleted in M04 Phase 7 v2 reconciliation."),
    9457: ("Mal 2:17 cha.phets H2654A — legacy (vr,mti) duplicate. Sibling vc=9420 "
           "retained. Soft-deleted in M04 Phase 7 v2 reconciliation."),
    9428: ("Psa 112:1 cha.phets H2654A — legacy (vr,mti) duplicate. Sibling vc=9400 "
           "retained. Soft-deleted in M04 Phase 7 v2 reconciliation."),
}


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def main():
    dry_run = "--live" not in sys.argv

    log(f"M04 Phase 7 v2 — directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        backup_dir = REPO / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_dir / f"bible_research_backup_{ts}_{DIRECTIVE}.db"
        shutil.copy2(DB, backup_path)
        log(f"Backup: {backup_path.name}")

    creation = json.loads(CREATION_JSON.read_text(encoding="utf-8"))

    # Flatten VCGs into a dict: code → {description, verses, anchor, sg_code}
    vcgs: dict[str, dict] = {}
    for sg in SG_ORDER:
        for vcg in creation.get(sg, {}).get("vcgs", []):
            code = vcg["provisional_code"]
            vcgs[code] = {
                "code": code,
                "sg_code": sg,
                "description": vcg["description"],
                "verses": set(vcg.get("verses", [])),
                "anchor_vc_id": vcg.get("anchor_vc_id"),
            }
    log(f"VCGs loaded: {len(vcgs)}")
    log(f"Total verse memberships: {sum(len(v['verses']) for v in vcgs.values())}")

    # Drop legacy-dup vc_ids that will be soft-deleted (their siblings remain in member lists)
    if LEGACY_DUP_SOFT_DELETES:
        legacy_set = set(LEGACY_DUP_SOFT_DELETES)
        removed = 0
        for vcg in vcgs.values():
            before = len(vcg["verses"])
            vcg["verses"] -= legacy_set
            removed += before - len(vcg["verses"])
        log(f"Legacy (vr,mti) dup vc_ids removed from member lists: {removed}")

    # Build per-vc primary VCG mapping (no duplicates per §10.9 validation)
    primary_vcg: dict[int, str] = {}
    for sg in SG_ORDER:
        for code, vcg in sorted(vcgs.items()):
            if vcg["sg_code"] != sg:
                continue
            for vc in vcg["verses"]:
                primary_vcg[vc] = code  # last-write-wins; validation confirms no dups

    log(f"Distinct vc_ids routed (primary): {len(primary_vcg)}")

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    counts = {
        "vcg_inserts": 0, "vcg_term_inserts": 0, "vc_group_updates": 0,
        "vc_anchor_sets": 0, "vc_anchor_resets": 0, "warns": 0,
        "provisional_anchors": 0,
    }

    try:
        conn.execute("BEGIN")

        # Preflight
        st = conn.execute(
            "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
        ).fetchone()
        if not st or st["status"] != "Analysis - In Progress":
            raise RuntimeError(
                f"cluster.status {CLUSTER} expected 'Analysis - In Progress', "
                f"got {st and st['status']!r}"
            )
        log(f"  cluster.status {CLUSTER} = {st['status']} ✓")

        sg_id_map = {
            r["subgroup_code"]: r["id"]
            for r in conn.execute(
                "SELECT id, subgroup_code FROM cluster_subgroup "
                "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
                (CLUSTER,)
            )
        }
        log(f"  sub-group ids resolved: {len(sg_id_map)}")

        # ===== Op 0 — Soft-delete legacy (vr,mti) duplicate vc rows =====
        if LEGACY_DUP_SOFT_DELETES:
            log(f"\n=== Op 0 — Soft-delete legacy duplicate vc rows ===")
            for vc_id, reason in LEGACY_DUP_SOFT_DELETES.items():
                rc = conn.execute(
                    "UPDATE verse_context SET delete_flagged=1, "
                    "notes=COALESCE(notes,'')||? "
                    "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                    (f" | {DIRECTIVE} legacy-dup soft-delete: {reason}", vc_id)
                ).rowcount
                log(f"  vc={vc_id}: soft-deleted (rowcount={rc})")
                if rc != 1:
                    raise RuntimeError(f"Op 0 soft-delete vc={vc_id} affected {rc} rows; expected 1")

        # ===== Op A — INSERT verse_context_group =====
        log(f"\n=== Op A — INSERT verse_context_group ===")
        vcg_db_id: dict[str, int] = {}
        for code in sorted(vcgs.keys()):
            vcg = vcgs[code]
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

        # ===== Op B — INSERT vcg_term =====
        log(f"\n=== Op B — INSERT vcg_term ===")
        vcg_terms: dict[str, set[int]] = defaultdict(set)
        for vc, code in primary_vcg.items():
            r = conn.execute(
                "SELECT mti_term_id FROM verse_context WHERE id=?", (vc,)
            ).fetchone()
            if r:
                vcg_terms[code].add(r["mti_term_id"])

        for code, mti_set in vcg_terms.items():
            for mti in sorted(mti_set):
                conn.execute(
                    """INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note,
                                              delete_flagged, created_at, last_updated_date)
                       VALUES (?, ?, ?, 0, ?, ?)""",
                    (vcg_db_id[code], mti,
                     f"{DIRECTIVE}: derived from VCG member verses", now, now)
                )
                counts["vcg_term_inserts"] += 1
        log(f"  INSERTed {counts['vcg_term_inserts']} vcg_term rows")

        # ===== Op C — UPDATE verse_context.group_id =====
        log(f"\n=== Op C — UPDATE verse_context.group_id ===")
        for vc, code in primary_vcg.items():
            gid = vcg_db_id[code]
            rc = conn.execute(
                "UPDATE verse_context SET group_id=? "
                "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (gid, vc)
            ).rowcount
            if rc == 1:
                counts["vc_group_updates"] += 1
        log(f"  UPDATEd {counts['vc_group_updates']} verse_context.group_id values")

        # ===== Op D — Anchor reset + designation =====
        log(f"\n=== Op D — Anchor reset + designation ===")
        rc_reset = conn.execute("""
            UPDATE verse_context SET is_anchor=0
            WHERE id IN (
              SELECT vc.id FROM verse_context vc
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
              WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
              AND vc.is_anchor=1
            )
        """, (CLUSTER,)).rowcount
        counts["vc_anchor_resets"] = rc_reset
        log(f"  Reset {rc_reset} prior {CLUSTER} anchors")

        for code in sorted(vcgs.keys()):
            anc = vcgs[code].get("anchor_vc_id")
            if not anc:
                log(f"  WARN: VCG {code} has no anchor_vc_id; skipping")
                counts["warns"] += 1
                continue
            rc = conn.execute(
                "UPDATE verse_context SET is_anchor=1 "
                "WHERE id=? AND COALESCE(delete_flagged,0)=0", (anc,)
            ).rowcount
            if rc == 1:
                counts["vc_anchor_sets"] += 1
            else:
                log(f"  WARN: anchor designation for {code} (vc={anc}) affected {rc} rows")
                counts["warns"] += 1
        log(f"  Set {counts['vc_anchor_sets']} VCG-anchor designations")

        # ===== Op D.1 — R4 provisional anchors =====
        log(f"\n=== Op D.1 — R4 provisional anchors ===")
        provisional_targets = list(conn.execute("""
            SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration
            FROM mti_terms mt
            WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
              AND mt.status IN ('extracted','extracted_thin')
              AND EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id
                            AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0)
              AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id
                                AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0)
        """, (CLUSTER,)))
        for r in provisional_targets:
            first = conn.execute("""
                SELECT vc.id FROM verse_context vc
                JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                WHERE vc.mti_term_id=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
                ORDER BY vr.book_id, vr.chapter, vr.verse_num, vc.id
                LIMIT 1
            """, (r["mti_id"],)).fetchone()
            if first:
                note = (
                    f" | {DIRECTIVE} provisional anchor (R4 fallback): "
                    f"term {r['strongs_number']} {r['transliteration']} had no AI-designated "
                    f"anchor; first canonical-order is_relevant verse promoted."
                )
                conn.execute(
                    "UPDATE verse_context SET is_anchor=1, "
                    "notes=COALESCE(notes,'')||? "
                    "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                    (note, first["id"])
                )
                counts["provisional_anchors"] += 1
        log(f"  Set {counts['provisional_anchors']} provisional per-term anchors")

        # ===== Post-checks =====
        log(f"\n=== Post-checks ===")
        h2 = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
            WHERE mt.cluster_code=? AND vc.is_relevant=1 AND vc.group_id IS NULL
              AND COALESCE(vc.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        h3 = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id=vc.mti_term_id
            JOIN verse_context_group vcg ON vcg.id=vc.group_id
                 AND COALESCE(vcg.delete_flagged,0)=0
            LEFT JOIN vcg_term vt ON vt.vcg_id=vcg.id AND vt.mti_term_id=vc.mti_term_id
                 AND COALESCE(vt.delete_flagged,0)=0
            WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
              AND vc.is_relevant=1
              AND vt.id IS NULL
        """, (CLUSTER,)).fetchone()[0]
        r4_fail = conn.execute("""
            SELECT COUNT(DISTINCT mt.id) FROM mti_terms mt
            WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
              AND mt.status IN ('extracted','extracted_thin')
              AND EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id
                            AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0)
              AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id=mt.id
                                AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0)
        """, (CLUSTER,)).fetchone()[0]

        log(f"  H2 (is_relevant=1 without group_id): {h2} ({'✓' if h2==0 else '✗'})")
        log(f"  H3 (vc mti not in vcg term set): {h3} ({'✓' if h3==0 else '✗'})")
        log(f"  R4 failures (terms with is_relevant verses but no anchor): {r4_fail} "
            f"({'✓' if r4_fail==0 else '✗'})")
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
