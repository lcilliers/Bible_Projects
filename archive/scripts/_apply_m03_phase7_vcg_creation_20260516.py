"""Apply M03 Phase 7 — VCG creation, vcg_term links, verse routing, anchor designation.

Reads AI's Phase 7 design:
  Sessions/Session_Clusters/M03/files phase 7/WA-M03-vcg-creation-v1-20260516.json

Per validation report WA-M03-phase7-validation-v1-20260516.md, applies these
reconciliations inline before insert:

  DROP (3): invalid placements
    M03-D-VCG-01 → drop vc_id 1492 (does not exist in DB)
    M03-D-VCG-04 → drop vc_id 65109 (is_relevant=0 set-aside)
    M03-D-VCG-05 → drop vc_id 96 (Rom 1:18 orgē — M02 cluster, not M03)

  ADD (8): missing verses routed via primary
    vc=54599 (Jer 3:21 be.khi)    → M03-A-VCG-02
    vc=18529 (Est 6:12 a.vel)     → M03-B-VCG-01
    vc=29990 (Mic 1:8 sa.phad)    → M03-B-VCG-02
    vc=12781 (Isa 8:22 tsu.qah)   → M03-BOUNDARY-VCG-01
    vc=12782 (Pro 1:27 tsu.qah)   → M03-BOUNDARY-VCG-01
    vc=28984 (Psa 142:2 si.ach)   → M03-BOUNDARY-VCG-01
    vc=91    (Luk 2:48 odunaō)    → M03-D-VCG-05
    vc=1359  (Jon 2:2 tsa.rah)    → M03-D-VCG-01

  ANCHOR fix (1):
    M03-D-VCG-05: add vc_id 144 (2Cor 2:4 sunochē — the anchor itself) to member list

  DUAL-MEMBERSHIP (5 legitimate duals + 2 collapse):
    vc=18501 Neh 1:4 a.val  : collapse (M03-B-VCG-02 listed twice)
    vc=65102 2Sa 24:14 tsar : collapse (M03-D-VCG-03 listed twice)
    vc=29992 Zec 12:12      : primary M03-B-VCG-03, secondary M03-B-VCG-04
    vc=38169 Job 30:31      : primary M03-B-VCG-01, secondary M03-B-VCG-02
    vc=54598 Isa 65:19      : primary M03-A-VCG-05, secondary M03-A-VCG-03
    vc=65106 Job 7:11       : primary M03-D-VCG-02 (its anchor), secondary M03-D-VCG-01
    vc=65175 Zep 1:15       : primary M03-D-VCG-04, secondary M03-D-VCG-01

Operations (single transaction):
  Op A: INSERT 25 verse_context_group rows
  Op B: INSERT vcg_term rows (one per (VCG, term) pair derived from member verses)
  Op C: UPDATE verse_context.group_id for each is_relevant verse (primary VCG)
        + record dual-memberships in verse_context.notes
  Op D: Reset all M03 anchors to is_anchor=0; set is_anchor=1 for each VCG's designated anchor
  Op D.1: R4 fallback — provisional per-term anchors for terms whose verses don't include
          an AI-designated anchor

No Op E set-asides (AI flagged 0 candidates per WA-M03-phase7-cross-routing-flags §2).
No old VCG dissolution (handled in Phase 8).
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
M03 = REPO / "Sessions" / "Session_Clusters" / "M03"
CREATION_JSON = M03 / "files phase 7" / "WA-M03-vcg-creation-v1-20260516.json"
DIRECTIVE = "DIR-20260516-017 (wa-cluster-M03-dir-003-vcg-create-v1-20260516)"
CLUSTER = "M03"

# vc_ids to DROP from any VCG member list before processing
DROP_VC_IDS = {1492, 65109, 96}

# Legacy (vr, mti) duplicate vc rows in M03.
# One historical pattern: same verse + same term appeared twice in vc when an inherited
# VCG distinguished two contexts for the same (verse, term). Both rows have is_relevant=1.
# Under v2_2, every verse routes to one primary VCG — so both rows would UPDATE to the
# same new group_id and violate UNIQUE (verse_record_id, mti_term_id, group_id,
# cluster_subgroup_id). Resolution: keep the row that carries the existing is_anchor=1
# (or 'dual-context' note); soft-delete the other.
LEGACY_DUP_SOFT_DELETES: dict[int, str] = {
    1201: ("Hab 1:3 a.mal — legacy (vr,mti) duplicate. Sibling vc=1186 retains "
           "is_anchor=1 and 'dual-context' note. Soft-deleted in M03 Phase 7 "
           "reconciliation to comply with verse_context UNIQUE constraint under "
           "single-VCG primary routing."),
}

# Missing verses to ADD (vc_id → target VCG provisional_code)
# vc=144 is NOT added here — it already exists in M03-D-VCG-02's member list, and is
# designated as M03-D-VCG-05's anchor. Treated as legitimate dual via DUAL_RESOLUTIONS
# (primary VCG-05 to honour the anchor designation; secondary VCG-02 to preserve AI's
# heart-located placement).
MISSING_ASSIGNMENTS = {
    54599: "M03-A-VCG-02",
    18529: "M03-B-VCG-01",
    29990: "M03-B-VCG-02",
    12781: "M03-BOUNDARY-VCG-01",
    12782: "M03-BOUNDARY-VCG-01",
    28984: "M03-BOUNDARY-VCG-01",
    91:    "M03-D-VCG-05",
    1359:  "M03-D-VCG-01",
}

# Dual-membership resolution: vc_id → (primary_vcg_code, [secondary_vcg_codes])
# Verses listed in 2+ VCGs in the AI design. Order in primary_vcg comes first.
DUAL_RESOLUTIONS = {
    29992: ("M03-B-VCG-03", ["M03-B-VCG-04"]),
    38169: ("M03-B-VCG-01", ["M03-B-VCG-02"]),
    54598: ("M03-A-VCG-05", ["M03-A-VCG-03"]),
    65106: ("M03-D-VCG-02", ["M03-D-VCG-01"]),
    65175: ("M03-D-VCG-04", ["M03-D-VCG-01"]),
    # vc=144 is anchor of VCG-05 (NT anguish) and member of VCG-02 (heart-located).
    # Make VCG-05 primary so the anchor designation is consistent.
    144:   ("M03-D-VCG-05", ["M03-D-VCG-02"]),
    # 18501 and 65102 are intra-VCG duplicates — collapse only (no secondary)
    18501: ("M03-B-VCG-02", []),
    65102: ("M03-D-VCG-03", []),
}

SG_ORDER = ["M03-A","M03-B","M03-C","M03-D","M03-E","M03-F","M03-G","M03-BOUNDARY"]


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def main():
    dry_run = "--live" not in sys.argv

    log(f"M03 Phase 7 — directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP_DIR / f"bible_research_backup_{ts}_DIR-20260516-017.db"
        shutil.copy2(DB, backup_path)
        log(f"Backup: {backup_path.name}")

    creation = json.loads(CREATION_JSON.read_text(encoding="utf-8"))

    # Build VCG structure: {code: {description, verses, anchor_vc_id, sg_code}}
    vcgs: dict[str, dict] = {}
    dropped = 0
    for sg in SG_ORDER:
        sg_block = creation.get(sg, {})
        for vcg in sg_block.get("vcgs", []):
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
                if v in DROP_VC_IDS:
                    dropped += 1
                    continue
                vcgs[code]["verses"].add(v)
    log(f"VCGs loaded: {len(vcgs)}")
    log(f"Invalid vc_ids dropped from member lists: {dropped}")

    # ADD missing verses
    for vc_id, vcg_code in MISSING_ASSIGNMENTS.items():
        if vcg_code not in vcgs:
            raise RuntimeError(f"missing-verse assignment vc_id={vc_id} → {vcg_code} (VCG not in design)")
        vcgs[vcg_code]["verses"].add(vc_id)
    log(f"Missing verses added: {len(MISSING_ASSIGNMENTS)}")

    # Pre-drop legacy duplicates from VCG member lists
    if LEGACY_DUP_SOFT_DELETES:
        legacy_set = set(LEGACY_DUP_SOFT_DELETES)
        for vcg in vcgs.values():
            vcg["verses"] -= legacy_set
        log(f"Legacy (vr,mti) dup vc_ids removed from member lists: {len(legacy_set)}")

    # Build per-vc primary VCG mapping (apply DUAL_RESOLUTIONS first; else first-listed wins)
    primary_vcg: dict[int, str] = {}
    secondary_vcgs: dict[int, list[str]] = defaultdict(list)
    # First: explicit duals
    for vc, (primary, secondaries) in DUAL_RESOLUTIONS.items():
        primary_vcg[vc] = primary
        secondary_vcgs[vc] = list(secondaries)
    # Then: walk sub-groups in canonical order
    for sg in SG_ORDER:
        for code, vcg in sorted(vcgs.items()):
            if vcg["sg_code"] != sg:
                continue
            for vc in vcg["verses"]:
                if vc in primary_vcg:
                    # already resolved by explicit dual rule
                    continue
                primary_vcg[vc] = code

    log(f"Distinct vc_ids routed (primary): {len(primary_vcg)}")
    log(f"Verses with dual-membership: {sum(1 for v in secondary_vcgs.values() if v)}")

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    counts = {
        "vcg_inserts": 0, "vcg_term_inserts": 0, "vc_group_updates": 0,
        "vc_anchor_sets": 0, "vc_anchor_resets": 0, "warns": 0,
        "provisional_anchors": 0,
    }

    try:
        conn.execute("BEGIN")

        st = conn.execute(
            "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
        ).fetchone()
        if not st or st["status"] != "Analysis - In Progress":
            raise RuntimeError(
                f"cluster.status {CLUSTER} expected 'Analysis - In Progress', "
                f"got {st and st['status']!r}"
            )
        log(f"  cluster.status {CLUSTER} = {st['status']} ✓")

        # Sub-group ids
        sg_id_map = {
            r["subgroup_code"]: r["id"]
            for r in conn.execute(
                "SELECT id, subgroup_code FROM cluster_subgroup "
                "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
                (CLUSTER,)
            )
        }
        log(f"  sub-group ids resolved: {len(sg_id_map)}")

        # DB-side validation: every vc in primary_vcg must be is_relevant & M03
        bad = []
        for vc in primary_vcg:
            r = conn.execute(
                "SELECT vc.is_relevant, vc.delete_flagged, mt.cluster_code "
                "FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id "
                "WHERE vc.id=?", (vc,)
            ).fetchone()
            if not r:
                bad.append((vc, "DOES NOT EXIST"))
            elif r["delete_flagged"]:
                bad.append((vc, "delete_flagged"))
            elif r["is_relevant"] != 1:
                bad.append((vc, "is_relevant=0"))
            elif r["cluster_code"] != CLUSTER:
                bad.append((vc, f"cluster_code={r['cluster_code']}"))
        if bad:
            for vc, why in bad[:20]:
                log(f"  REJECT vc={vc}: {why}")
            raise RuntimeError(f"{len(bad)} invalid vc_ids in primary routing — fix before live run")

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

        # ===== Op A — INSERT verse_context_group rows =====
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

        # ===== Op B — INSERT vcg_term rows =====
        log(f"\n=== Op B — INSERT vcg_term ===")
        vcg_terms: dict[str, set[int]] = defaultdict(set)
        for vc, primary_code in primary_vcg.items():
            r = conn.execute(
                "SELECT mti_term_id FROM verse_context WHERE id=?", (vc,)
            ).fetchone()
            if r:
                vcg_terms[primary_code].add(r["mti_term_id"])

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

        # ===== Op C — UPDATE verse_context.group_id (and notes for duals) =====
        log(f"\n=== Op C — UPDATE verse_context.group_id ===")
        for vc, primary_code in primary_vcg.items():
            gid = vcg_db_id[primary_code]
            note_addition = ""
            secs = secondary_vcgs.get(vc, [])
            if secs:
                note_addition = (
                    f" | {DIRECTIVE} dual-membership: "
                    f"primary={primary_code} secondary=[{', '.join(secs)}]"
                )
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
              WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
              AND vc.is_anchor=1
            )
        """, (CLUSTER,)).rowcount
        counts["vc_anchor_resets"] = rc_reset
        log(f"  Reset {rc_reset} prior {CLUSTER} anchors")

        for code in sorted(vcgs.keys()):
            vcg = vcgs[code]
            anchor = vcg.get("anchor_vc_id")
            if not anchor:
                continue
            if anchor in DROP_VC_IDS:
                log(f"  WARN: anchor for {code} is dropped vc={anchor}; skipping")
                counts["warns"] += 1
                continue
            # Verify anchor is a primary member of its VCG (post-dual-resolution)
            if primary_vcg.get(anchor) != code:
                log(f"  WARN: anchor for {code} vc={anchor} primary-routed to "
                    f"{primary_vcg.get(anchor)}; setting is_anchor=1 anyway (VCG-level designation)")
                counts["warns"] += 1
            rc = conn.execute(
                "UPDATE verse_context SET is_anchor=1 "
                "WHERE id=? AND COALESCE(delete_flagged,0)=0", (anchor,)
            ).rowcount
            if rc == 1:
                counts["vc_anchor_sets"] += 1
            else:
                log(f"  WARN: anchor designation for {code} (vc={anchor}) affected {rc} rows")
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
        log(f"  H3 (vc mti not in vcg term set, is_relevant=1): {h3} ({'✓' if h3==0 else '✗'})")
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
