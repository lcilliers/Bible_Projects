"""M11 Phase C apply (v3_0 first test).

Consolidated single-transaction apply per `wa-sessionb-cluster-instruction-v3_0-20260527.md` §7.

Operations:
  C.1  Term transfers + BOUNDARY designation
       — M11: 15/15 STAYS; 0 transfers, 0 BOUNDARY. Cross-register flags (3 terms)
         recorded as cluster_observation entries (no DB column for cross_register_target
         on wa_term_inventory).
  C.2  Sub-group create + verse routing
       — INSERT 5 cluster_subgroup rows (M11-A..E)
       — UPDATE verse_context.cluster_subgroup_id for 288 verses from mapping JSON
  C.3  Inherited-VCG soft-delete
       — M11's 26 inherited VCGs were already delete_flagged=1 in bulk pass.
         Confirm + UPDATE verse_context.group_id=NULL where it points at them
         (cleanup before C.4 reassigns).
  C.4  VCG create + verse routing + anchor
       — INSERT 43 verse_context_group rows (new group_code = {sg}-VCG-{NN})
       — INSERT vcg_term rows (one per distinct mti_term_id per VCG)
       — UPDATE verse_context.group_id to new VCG ids
       — Reset is_anchor=0 for M11 verses; SET is_anchor=1 for the 43 anchor vc_ids
  C.5  Characteristic load (silent, 1:1 default)
       — INSERT 5 characteristic rows (one per substantive sub-group)
       — INSERT 5 characteristic_subgroup links (1:1, is_partial=0)
  C.6  Seed cluster_observation rows (6 from B.2 design + per-term cross-register flag notes)
  C.7  Update cluster.status to 'Structurally Ready'

Single transaction; all-or-nothing.
"""
from __future__ import annotations
import argparse, io, json, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CLUSTER = "M11"
SOURCE = "v3_0 Phase C apply 2026-05-27 — first test cluster"

MAPPING_FILE = REPO / "Sessions" / "Session_Clusters" / "M11" / "WA-M11-subgroup-mapping-v1-20260527.json"
VCG_JSON = REPO / "Sessions" / "Session_Clusters" / "M11" / "WA-M11-vcg-creation-v1-20260527.json"

# Sub-group definitions (label + core_description from B.2 design)
SUBGROUPS = [
    {
        "subgroup_code": "M11-A",
        "label": "Atonement",
        "core_description": (
            "The priestly/sacrificial mechanism by which sin and defilement are covered, removed, or borne — "
            "the inner-being state of mediation that effects sin-release. Includes both the action-state of "
            "the mediator (bearing, covering, propitiating) and the resulting state of the one atoned-for "
            "(cleansed, brought to standing). kip.per (atonement) is the central OT verb; G0863I afiēmi-permit "
            "carries the NT atoning surrender in Mat 27:50 and Joh 18:8."
        ),
        "sort_order": 1,
    },
    {
        "subgroup_code": "M11-B",
        "label": "Divine forgiveness",
        "core_description": (
            "The sovereign divine act of releasing sin's guilt — the inner-being state of being pardoned and "
            "the corresponding divine disposition of pardoning. sa.lach is the primary OT divine-forgiveness "
            "verb; sal.lach and se.li.chah name forgiveness as divine character attribute; G0863H afiēmi-forgive "
            "is the central NT divine-forgiveness verb. The kip.per → sa.lach internal arc (M11-A → M11-B) is "
            "the canonical Levitical mechanism-to-outcome pair."
        ),
        "sort_order": 2,
    },
    {
        "subgroup_code": "M11-C",
        "label": "Release (broader sense)",
        "core_description": (
            "The act and state of releasing — from sin's record, debt, obligation, bondage, possession, or "
            "relationship. Broader than divine forgiveness; this register names the act of letting go itself. "
            "Carries afesis, afiēmi-leave (G0863G, majority register M30/M29 volitional-detachment), "
            "afiēmi-permit (G0863I, majority register M29 permission/volition), and exaleifō. Cross-register "
            "verses are isolated at the VCG level per Phase 3 design notes."
        ),
        "sort_order": 3,
    },
    {
        "subgroup_code": "M11-D",
        "label": "Repentance and turning",
        "core_description": (
            "The inner human act of turning from sin toward God — the contrite movement that opens the way for "
            "forgiveness and reconciliation. Also covers divine relenting (na.cham) where God turns from a "
            "planned judgment, often in response to intercession or human turning. The characteristic is the "
            "inner act of turning itself, in both human and divine senses. Includes the marginal H5749A ud "
            "structural-opposite verdict from Phase 3 §6.3.2."
        ),
        "sort_order": 4,
    },
    {
        "subgroup_code": "M11-E",
        "label": "Reconciliation",
        "core_description": (
            "The relational restoration outcome — the inner-being state of being brought back into right "
            "relationship, and the act that effects it. Distinct from atonement (the mechanism) and forgiveness "
            "(the act of pardon); reconciliation names the relational outcome and the inner-being state of "
            "being-at-peace / restored-to-standing. Includes interpersonal and cosmic reconciliation (Christ "
            "as initiator)."
        ),
        "sort_order": 5,
    },
]

# Cross-register flag terms (from Phase 3 verdicts) → seed as cluster_observation rows
CROSS_REGISTER_FLAGS = [
    {
        "title": "G0863G afiēmi (leave) cross-register flag — M30/M29 primary",
        "description": (
            "G0863G afiēmi (leave sense, 32V) carries M30/M29 (volitional-detachment) as its primary register "
            "for ~22 of 32 verses. M11-relational verses (Mat 5:24, Heb 6:1, Rev 2:4, 1Cor 7:11) sit in "
            "M11-C-VCG-04 (reconciliation-prioritizing); volitional-detachment verses in M11-C-VCG-03 "
            "(discipleship-call leaving); eschatological separation in M11-C-VCG-06; loyalty failure in "
            "M11-C-VCG-05. Phase D T6 will articulate the cross-register relationship."
        ),
        "target_phase": "D",
    },
    {
        "title": "G0863I afiēmi (permit) cross-register flag — M29 primary",
        "description": (
            "G0863I afiēmi (permit sense, 18V) carries M29 (permission/volition) as its primary register for "
            "~16 of 18 verses. Two M11-A atonement-relational verses (Mat 27:50, Joh 18:8) routed to M11-A. "
            "Remaining 16 verses routed to M11-C and split at VCG level (VCG-08 permission granted / "
            "VCG-09 permission withheld). Phase D T6 will articulate."
        ),
        "target_phase": "D",
    },
    {
        "title": "H5749A ud — marginal STAYS structural-opposite",
        "description": (
            "Psa 119:61 — sole IB verse. Phase 3 §6.3.2 verse-level relationship test satisfied by "
            "structural-opposite reading (sustained faithfulness is the obverse of the M11-D turning-from-"
            "abandonment). Marginal STAYS verdict. Routed to M11-D-VCG-09 as a dedicated single-verse VCG. "
            "Phase D T6 reading may confirm or reverse this verdict."
        ),
        "target_phase": "D",
    },
]

# 6 cluster-scope observations from B.2 design §5
B2_OBSERVATIONS = [
    {
        "title": "M11 multi-characteristic framing under v3_0",
        "description": (
            "M11 is multi-characteristic under v3_0 §6.2.2 — 5 distinct characteristics (Atonement, Divine "
            "forgiveness, Release, Repentance and turning, Reconciliation) causally linked but ontologically "
            "distinct. Phase 3's 'one characteristic, three mechanisms' reading re-framed under v3_0 "
            "sub-groups-represent-characteristics."
        ),
        "target_phase": "D",
    },
    {
        "title": "Cross-cluster characteristic-legs (forgive-text scatter)",
        "description": (
            "Only 103 of programme-wide 421 forgive-text verses sit in M11; the other ~246 are anchored to "
            "non-M11 terms in 30+ other clusters (M10 88, M05 19, M38 17, M45 10, M21 7, etc.). Cross-cluster "
            "T6 findings at Phase D should surface this; Session D may need to integrate."
        ),
        "target_phase": "D",
    },
    {
        "title": "kip.per/sa.lach internal arc (M11-A ↔ M11-B canonical pair)",
        "description": (
            "M11 internal arc: kip.per (atonement, M11-A-VCG-02) → sa.lach (forgiveness, M11-B-VCG-05) is the "
            "central OT mechanism-to-outcome pair. Same Levitical verses are evidenced from both sides; the "
            "M11-A and M11-B together form the canonical Levitical atonement/forgiveness arc. Phase D T6 should "
            "articulate this inter-characteristic structural relationship."
        ),
        "target_phase": "D",
    },
    {
        "title": "Christic surrender → cosmic reconciliation arc (M11-A-VCG-10 ↔ M11-E-VCG-01)",
        "description": (
            "The NT atoning death (Christ voluntarily releasing his spirit, Mat 27:50; granting disciples free "
            "passage, Joh 18:8) → cosmic reconciliation (Col 1:20, Eph 2:16, Rom 5:10) is the NT christological "
            "arc of the cluster. Phase D T6 should articulate."
        ),
        "target_phase": "D",
    },
    {
        "title": "Negative pole runs across M11-A, M11-B, M11-C",
        "description": (
            "Atonement denied (M11-A-VCG-08), forgiveness foreclosed (M11-B-VCG-04), and release foreclosed "
            "(M11-C-VCG-02) form the parallel negative pole across three sub-groups. Phase D may synthesize "
            "the M11 limit-condition pattern — the inner state of sealed/unrepentable rejection that closes "
            "the entire restorative arc."
        ),
        "target_phase": "D",
    },
    {
        "title": "M03 cross-register flag for divine grief (na.cham)",
        "description": (
            "M11-D-VCG-04 (Divine grief / sorrow over human failure) carries M03 cross-register — divine grief "
            "is M03 inner content while the relenting movement is M11-D. The cluster's verse evidence shows the "
            "two intertwined in the same lexical occurrences (Gen 6:6/7, 1Sa 15:11/35)."
        ),
        "target_phase": "D",
    },
]


def main(live: bool) -> int:
    print(f"=== M11 Phase C apply — mode={'LIVE' if live else 'DRY-RUN'} ===")

    mapping = {int(k): v for k, v in json.loads(MAPPING_FILE.read_text(encoding="utf-8")).items()}
    vcg_data = json.loads(VCG_JSON.read_text(encoding="utf-8"))

    conn = sqlite3.connect(DB, timeout=120.0)
    conn.execute("PRAGMA busy_timeout = 120000")
    conn.row_factory = sqlite3.Row

    # Pre-checks
    n_terms = conn.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]
    n_ib = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms m ON m.id = vc.mti_term_id
        WHERE m.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0 AND COALESCE(m.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()[0]
    n_existing_sg = conn.execute("SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]
    n_existing_char = conn.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]

    print(f"  Terms in cluster: {n_terms}")
    print(f"  IB verses (DB): {n_ib}")
    print(f"  IB verses (mapping): {len(mapping)}")
    print(f"  Existing cluster_subgroup rows: {n_existing_sg}")
    print(f"  Existing characteristic rows: {n_existing_char}")

    if n_existing_sg > 0:
        print("ABORT: cluster_subgroup rows already exist for M11. Phase C must run from clean state.")
        return 1
    if n_existing_char > 0:
        print("ABORT: characteristic rows already exist for M11. Phase C must run from clean state.")
        return 1
    if n_ib != len(mapping):
        print(f"ABORT: IB verse count {n_ib} != mapping size {len(mapping)}")
        return 1

    total_vcg_verses = sum(len(v["verses"]) for sg in vcg_data.values() for v in sg.values())
    if total_vcg_verses != n_ib:
        print(f"ABORT: VCG JSON total {total_vcg_verses} != IB total {n_ib}")
        return 1
    print(f"  VCG count: {sum(len(sg) for sg in vcg_data.values())}")
    print(f"  VCG total verses: {total_vcg_verses}")

    if not live:
        print("\n[DRY-RUN — no writes]")
        print("Would execute Ops C.1..C.7 in single transaction.")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        # ── C.1 — term transfers (none) + cross-register flags via observations (later, in C.6) ───
        print("\nC.1: No term transfers (15/15 STAYS). Cross-register flags will seed observations in C.6.")

        # ── C.2 — sub-group create + verse routing ───────────────────────────────────────────────
        sg_id_by_code: dict[str, int] = {}
        for sg in SUBGROUPS:
            cur.execute(
                """INSERT INTO cluster_subgroup
                   (cluster_code, subgroup_code, label, core_description, sort_order, status,
                    version, source, delete_flagged, created_at, last_updated_date)
                   VALUES (?, ?, ?, ?, ?, 'active', 'v1', ?, 0, ?, ?)""",
                (CLUSTER, sg["subgroup_code"], sg["label"], sg["core_description"],
                 sg["sort_order"], SOURCE, NOW, NOW),
            )
            sg_id_by_code[sg["subgroup_code"]] = cur.lastrowid
        print(f"C.2: Inserted {len(sg_id_by_code)} cluster_subgroup rows: {sg_id_by_code}")

        # Update verse_context.cluster_subgroup_id for every IB verse
        n_updates_sg = 0
        for vc_id, sg_code in mapping.items():
            cur.execute(
                "UPDATE verse_context SET cluster_subgroup_id=? WHERE id=?",
                (sg_id_by_code[sg_code], vc_id),
            )
            n_updates_sg += cur.rowcount
        print(f"C.2: Updated verse_context.cluster_subgroup_id on {n_updates_sg} rows")

        # ── C.3 — confirm inherited VCG soft-delete + null out old group_id refs ─────────────────
        n_already_softdel = cur.execute("""
            SELECT COUNT(*) FROM verse_context_group
            WHERE id IN (
                SELECT DISTINCT vc.group_id FROM verse_context vc
                JOIN mti_terms m ON m.id = vc.mti_term_id
                WHERE m.cluster_code=? AND vc.group_id IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0
            )
              AND delete_flagged = 1
        """, (CLUSTER,)).fetchone()[0]
        print(f"C.3: Inherited VCGs already soft-deleted (confirmed): {n_already_softdel}")

        # Clear old group_id references (they point at delete_flagged=1 VCGs)
        cur.execute("""
            UPDATE verse_context SET group_id=NULL
            WHERE mti_term_id IN (SELECT id FROM mti_terms WHERE cluster_code=?)
              AND group_id IS NOT NULL
              AND COALESCE(delete_flagged,0)=0
        """, (CLUSTER,))
        print(f"C.3: Cleared verse_context.group_id on {cur.rowcount} rows (pointed at soft-deleted inherited VCGs)")

        # ── C.4 — new VCG create + verse routing + anchors ────────────────────────────────────────
        # Reset is_anchor=0 for all M11 verses first
        cur.execute("""
            UPDATE verse_context SET is_anchor=0
            WHERE mti_term_id IN (SELECT id FROM mti_terms WHERE cluster_code=?)
              AND COALESCE(delete_flagged,0)=0
              AND is_anchor=1
        """, (CLUSTER,))
        print(f"C.4: Reset is_anchor=0 on {cur.rowcount} prior-anchor rows")

        vcg_id_by_code: dict[str, int] = {}
        n_vcg_insert = 0
        n_vcg_term_insert = 0
        n_vc_group_update = 0
        n_anchor_set = 0

        for sg_code, vcgs in vcg_data.items():
            for vcg_code, vcg in vcgs.items():
                # INSERT new VCG row
                cur.execute(
                    """INSERT INTO verse_context_group
                       (group_code, context_description, delete_flagged, vertical_pass_flag)
                       VALUES (?, ?, 0, 0)""",
                    (vcg_code, vcg["description"]),
                )
                new_vcg_id = cur.lastrowid
                vcg_id_by_code[vcg_code] = new_vcg_id
                n_vcg_insert += 1

                # Distinct mti_term_ids for this VCG → INSERT vcg_term rows
                placeholders = ",".join("?" * len(vcg["verses"]))
                term_ids = [r[0] for r in cur.execute(
                    f"SELECT DISTINCT mti_term_id FROM verse_context WHERE id IN ({placeholders})",
                    vcg["verses"],
                ).fetchall()]
                for tid in term_ids:
                    cur.execute(
                        """INSERT INTO vcg_term (vcg_id, mti_term_id, delete_flagged, created_at, last_updated_date)
                           VALUES (?, ?, 0, ?, ?)""",
                        (new_vcg_id, tid, NOW, NOW),
                    )
                    n_vcg_term_insert += 1

                # UPDATE verse_context.group_id for each member
                for vc_id in vcg["verses"]:
                    cur.execute("UPDATE verse_context SET group_id=? WHERE id=?", (new_vcg_id, vc_id))
                    n_vc_group_update += cur.rowcount

                # SET is_anchor=1 for anchor vc_id
                anchor = vcg.get("anchor_vc_id")
                if anchor is not None:
                    cur.execute("UPDATE verse_context SET is_anchor=1 WHERE id=?", (anchor,))
                    n_anchor_set += cur.rowcount

        print(f"C.4: Inserted {n_vcg_insert} VCG rows; {n_vcg_term_insert} vcg_term links; "
              f"updated {n_vc_group_update} verse_context.group_id; set {n_anchor_set} anchors")

        # ── C.5 — characteristic load (1:1 default) ──────────────────────────────────────────────
        char_id_by_sg: dict[str, int] = {}
        for sg in SUBGROUPS:
            cur.execute(
                """INSERT INTO characteristic
                   (cluster_code, char_seq, short_name, definition, source, version,
                    delete_flagged, created_at, last_updated_date)
                   VALUES (?, ?, ?, ?, ?, 'v1', 0, ?, ?)""",
                (CLUSTER, sg["sort_order"], sg["label"], sg["core_description"], SOURCE, NOW, NOW),
            )
            char_id_by_sg[sg["subgroup_code"]] = cur.lastrowid
        print(f"C.5: Inserted {len(char_id_by_sg)} characteristic rows")

        for sg_code, sg_id in sg_id_by_code.items():
            char_id = char_id_by_sg[sg_code]
            cur.execute(
                """INSERT INTO characteristic_subgroup
                   (characteristic_id, cluster_subgroup_id, qualifier_note, is_partial,
                    delete_flagged, created_at, last_updated_date)
                   VALUES (?, ?, ?, 0, 0, ?, ?)""",
                (char_id, sg_id, f"1:1 mapping for {sg_code} (v3_0 default)", NOW, NOW),
            )
        print(f"C.5: Inserted {len(sg_id_by_code)} characteristic_subgroup links (1:1, is_partial=0)")

        # ── C.6 — seed cluster_observation rows ──────────────────────────────────────────────────
        n_obs = 0
        all_obs = [
            (*B2_OBSERVATIONS, "b.2-design"),
            (*CROSS_REGISTER_FLAGS, "b.1-cross-register"),
        ]
        for obs_list, src_phase in [(B2_OBSERVATIONS, "B.2"), (CROSS_REGISTER_FLAGS, "B.1")]:
            for o in obs_list:
                cur.execute(
                    """INSERT INTO cluster_observation
                       (cluster_code, source_phase, observation_type, target_phase,
                        title, description, status, raised_date,
                        source_file, delete_flagged, created_at, last_updated_date)
                       VALUES (?, ?, ?, ?, ?, ?, 'open', ?, ?, 0, ?, ?)""",
                    (CLUSTER, src_phase, "design-note", o["target_phase"], o["title"],
                     o["description"], NOW,
                     "WA-M11-subgroup-design-v1-20260527.md",
                     NOW, NOW),
                )
                n_obs += 1
        print(f"C.6: Inserted {n_obs} cluster_observation rows")

        # ── C.7 — cluster status flip ────────────────────────────────────────────────────────────
        cur.execute(
            "UPDATE cluster SET status=?, last_updated_date=? WHERE cluster_code=?",
            ("Structurally Ready", NOW, CLUSTER),
        )
        print(f"C.7: cluster.status -> 'Structurally Ready' (rows updated: {cur.rowcount})")

        # Post-checks
        print("\n=== Post-checks ===")
        n_sg = cur.execute("SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]
        n_char = cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]
        n_csg = cur.execute("SELECT COUNT(*) FROM characteristic_subgroup csg JOIN characteristic ch ON ch.id=csg.characteristic_id WHERE ch.cluster_code=? AND COALESCE(csg.delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]
        n_new_vcg = cur.execute("""
            SELECT COUNT(*) FROM verse_context_group vcg
            WHERE vcg.id IN (
                SELECT DISTINCT group_id FROM verse_context vc
                JOIN mti_terms m ON m.id=vc.mti_term_id
                WHERE m.cluster_code=? AND vc.group_id IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0
            )
              AND COALESCE(vcg.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        n_assigned = cur.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms m ON m.id = vc.mti_term_id
            WHERE m.cluster_code=? AND vc.is_relevant=1
              AND vc.cluster_subgroup_id IS NOT NULL
              AND vc.group_id IS NOT NULL
              AND COALESCE(vc.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        n_anchors_now = cur.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms m ON m.id = vc.mti_term_id
            WHERE m.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        n_obs_now = cur.execute("SELECT COUNT(*) FROM cluster_observation WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]
        cluster_status = cur.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()[0]

        print(f"  cluster_subgroup rows: {n_sg}")
        print(f"  characteristic rows: {n_char}")
        print(f"  characteristic_subgroup links: {n_csg}")
        print(f"  new active VCGs for cluster: {n_new_vcg}")
        print(f"  IB verses with both subgroup_id and group_id: {n_assigned}")
        print(f"  is_anchor=1 verses: {n_anchors_now}")
        print(f"  cluster_observation rows: {n_obs_now}")
        print(f"  cluster.status: {cluster_status}")

        assert n_sg == 5, "cluster_subgroup count != 5"
        assert n_char == 5, "characteristic count != 5"
        assert n_csg == 5, "characteristic_subgroup count != 5"
        assert n_new_vcg == 43, f"new VCG count {n_new_vcg} != 43"
        assert n_assigned == 288, f"assigned verses {n_assigned} != 288"
        assert n_anchors_now == 43, f"anchors {n_anchors_now} != 43"
        assert n_obs_now == 9, f"observations {n_obs_now} != 9"
        assert cluster_status == "Structurally Ready"

        conn.commit()
        print(f"\nCOMMITTED at {NOW}")
        return 0

    except Exception as e:
        conn.rollback()
        print(f"ROLLED BACK: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
