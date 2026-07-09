"""M38 Salvation — Phase C structural apply.

Consolidated single-transaction apply per wa-sessionb-cluster-instruction-v3_0-20260527 §7.

Operations:
  C.1  Term verdicts — all 13 STAYS; cross-register flags seeded as observations.
  C.2  Sub-group create + verse routing (7 sub-groups; 310 IB verses).
  C.3  Inherited-VCG soft-delete + null out old group_id refs.
  C.4  VCG create + verse routing + anchors (45 new VCGs).
  C.5  Characteristic load (1:1 default; 7 characteristic rows).
  C.6  Seed cluster_observation rows (cross-register flags + B.2 design notes).
  C.7  Cluster status flip → 'Structurally Ready'.

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
CLUSTER = "M38"
SOURCE = "v3_0 Phase C apply 2026-05-28 — M38 first sub-group/VCG creation"

B2_MAPPING_FILE = REPO / "Sessions" / "Session_Clusters" / "M38" / "WA-M38-subgroup-mapping-v2-20260528.json"
VCG_JSON_FILE   = REPO / "Sessions" / "Session_Clusters" / "M38" / "WA-M38-vcg-creation-v2-20260528.json"
B1_DEBATE_FILE  = REPO / "Sessions" / "Session_Clusters" / "M38" / "WA-M38-constitution-debate-v1-20260528.json"

# Sub-group definitions copied from B.2 mapping JSON _meta block (canonical)
SUBGROUPS = [
    {"subgroup_code": "M38-A", "label": "Eschatological salvation received by faith",
     "core_description":
         "This sub-group captures the inner-being state of the person who has received or is receiving "
         "eschatological/spiritual salvation — rescue from sin, condemnation, and future judgment for the kingdom. "
         "The dominant inner-being content is faith exercised as the reception point, the will turning toward Christ, "
         "the receiving of righteousness as gift, and the resulting state of being saved/justified/eternally "
         "secured. Includes the Greek salvation-vocabulary (sōzō, sōtēr, soteria) where the meaning is "
         "eschatological/spiritual, the dōrea/dōrēma gift-of-salvation register (Rom 5:15-17), and verses where "
         "salvation is named as God's power received through faith (Rom 1:16, Eph 2:8 register). "
         "The largest sub-group at 39% of cluster — sits at the §6.2.7 distribution gate.",
     "sort_order": 1},
    {"subgroup_code": "M38-B", "label": "Physical rescue from mortal danger",
     "core_description":
         "This sub-group represents the inner-being state characterised by terror, panic, urgent faith-cry, and "
         "despair-then-relief when salvation means rescue from drowning, illness, mortal danger, or political "
         "violence. Distinct from M38-A by the absence of eschatological content — the rescue is physical, "
         "and the inner-being content is the fear-faith dynamic in the moment of mortal threat (Mat 8:25 "
         "'Save us, we perish'; Mat 14:30 Peter sinking; Act 27:20 storm despair). Per researcher direction "
         "(BOUNDARY resolution on sōzō homonymic_polysemic) these verses are held distinct from M38-A.",
     "sort_order": 2},
    {"subgroup_code": "M38-C", "label": "Healing wholeness through faith exercised",
     "core_description":
         "This sub-group captures the inner-being characteristic of the person whose faith activates "
         "holistic rescue — physical healing that carries an explicit spiritual register, where the healing "
         "and the saving are inseparable (Mar 5:34, Mat 9:21-22 'your faith has saved you'). The inner faculty "
         "engaged is faith as the activating mechanism, with wholeness sought and received bridging the "
         "physical and the spiritual. Per researcher direction (sōzō sense-split) held distinct from M38-A "
         "and M38-B.",
     "sort_order": 3},
    {"subgroup_code": "M38-D", "label": "Conscience cleansed through atonement received",
     "core_description":
         "This sub-group names the inner-being state of the person who stands at the receiving end of "
         "atonement — guilt removed, wrath averted, conscience cleansed, sin covered (Lev 4:20 priestly "
         "atonement effects forgiveness; 1Jo 2:2 Christ as propitiation; Rom 3:25 propitiation received by "
         "faith). The Greek propitiation vocabulary (hilaskomai, hilasmos, hilastērios, hileōs) integrates "
         "with the Hebrew ka.phar atoned-state verses. Cross-register with M02 Anger (wrath-averted as "
         "structural opposite) and M05 Love (1Jo 4:10 love as source of propitiation).",
     "sort_order": 4},
    {"subgroup_code": "M38-E", "label": "Priestly mediation machinery of atonement",
     "core_description":
         "This sub-group holds ka.phar Register B — the instrumental and procedural register of the atonement "
         "system where the priest acts on behalf of others rather than the atoned-for person's inner-being state. "
         "The inner-being content here is the mediator's solidarity-burden (Aaron commanded to offer atonement "
         "for himself first, Lev 9:7), the high priest's solitary intercession (Lev 16:17), the procedural "
         "ordination and Day of Atonement mechanics. Per researcher direction (ka.phar BOUNDARY resolution) "
         "held distinct from M38-D's atoned-state inner-being.",
     "sort_order": 5},
    {"subgroup_code": "M38-F", "label": "Salvation anticipated and hope sustained",
     "core_description":
         "This sub-group captures the distinctive inner-being posture of waiting, longing, and hope-sustained-"
         "toward-salvation — the soul that has not yet received but actively waits in expectant trust "
         "(Gen 49:18 'I wait for your salvation'; Isa 25:9 'we have waited for him'; Heb 9:28 awaiting Christ's "
         "appearing). An emergent characteristic that surfaced from the keyword analytics rather than from the "
         "working cluster characteristic statement — hope sustained as the inner-being content distinct from "
         "salvation-already-received (M38-A). Cross-register with M18 Hope (eschatological orientation).",
     "sort_order": 6},
    {"subgroup_code": "M38-G", "label": "Ransomed identity gratitude and memory",
     "core_description":
         "This sub-group captures the inner-being characteristic of the person who has been ransomed — "
         "delivered by God's covenantal initiative from slavery, oppression, the pit, or Sheol — and the "
         "consequent inner-being states of gratitude, formative memory, and identity grounded in being the "
         "ransomed people. Dominated by pa.dah (Hebrew) with cross-register flags to M37 Calling (covenantal "
         "election), M41 Remembrance (formative memory of past ransom), and M04 Joy (sustained rejoicing of "
         "the ransomed at Isa 35:10, 51:11).",
     "sort_order": 7},
]


def main(live: bool) -> int:
    print(f"=== M38 Phase C apply — mode={'LIVE' if live else 'DRY-RUN'} ===")

    b2 = json.loads(B2_MAPPING_FILE.read_text(encoding="utf-8"))
    # Flatten to {vc_id: sg_code}
    mapping: dict[int, str] = {}
    for sg in b2["subgroups"]:
        for vc_id in sg["verses"]:
            mapping[int(vc_id)] = sg["subgroup_code"]

    vcg_outer = json.loads(VCG_JSON_FILE.read_text(encoding="utf-8"))
    # vcg_outer is {"_meta": {...}, "subgroups": {"M38-A": {"vcgs": [...]}, ...}}
    vcg_data = vcg_outer["subgroups"]

    debate = json.loads(B1_DEBATE_FILE.read_text(encoding="utf-8"))

    conn = sqlite3.connect(DB, timeout=120.0)
    conn.execute("PRAGMA busy_timeout = 120000")
    conn.row_factory = sqlite3.Row

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
        print("ABORT: cluster_subgroup rows already exist for M38. Phase C must run from clean state.")
        return 1
    if n_existing_char > 0:
        print("ABORT: characteristic rows already exist for M38. Phase C must run from clean state.")
        return 1
    if n_ib != len(mapping):
        print(f"ABORT: IB verse count {n_ib} != mapping size {len(mapping)}")
        return 1

    # VCG sanity
    n_vcg = 0
    total_vcg_verses = 0
    for sg_code, sg_payload in vcg_data.items():
        for vcg in sg_payload["vcgs"]:
            n_vcg += 1
            total_vcg_verses += len(vcg["verses"])
    print(f"  VCG count: {n_vcg}")
    print(f"  VCG total verses (incl. declared duals): {total_vcg_verses}")

    if not live:
        print("\n[DRY-RUN — no writes]")
        print("Would execute Ops C.1..C.7 in single transaction.")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        # ── C.1 — term verdicts ────────────────────────────────────────────────────────────────────
        print("\nC.1: All 13 STAYS; no transfers; no BOUNDARY (resolved). Cross-register flags → C.6 observations.")

        # ── C.2 — sub-group create + verse routing ────────────────────────────────────────────────
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
        print(f"C.2: Inserted {len(sg_id_by_code)} cluster_subgroup rows")

        n_updates_sg = 0
        for vc_id, sg_code in mapping.items():
            cur.execute(
                "UPDATE verse_context SET cluster_subgroup_id=? WHERE id=?",
                (sg_id_by_code[sg_code], vc_id),
            )
            n_updates_sg += cur.rowcount
        print(f"C.2: Updated verse_context.cluster_subgroup_id on {n_updates_sg} rows")

        # ── C.3 — inherited VCG soft-delete + null out old group_id refs ─────────────────────────
        # Soft-delete any active verse_context_group rows referenced by M38 vc rows
        rows_to_softdel = cur.execute("""
            SELECT DISTINCT vc.group_id FROM verse_context vc
            JOIN mti_terms m ON m.id = vc.mti_term_id
            WHERE m.cluster_code=? AND vc.group_id IS NOT NULL
              AND COALESCE(vc.delete_flagged,0)=0 AND COALESCE(m.delete_flagged,0)=0
        """, (CLUSTER,)).fetchall()
        inherited_group_ids = [r[0] for r in rows_to_softdel]
        n_softdel = 0
        for gid in inherited_group_ids:
            cur.execute(
                "UPDATE verse_context_group SET delete_flagged=1 WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (gid,)
            )
            n_softdel += cur.rowcount
            # Also soft-delete vcg_term links for this group
            cur.execute(
                "UPDATE vcg_term SET delete_flagged=1, last_updated_date=? WHERE vcg_id=? AND COALESCE(delete_flagged,0)=0",
                (NOW, gid)
            )
        print(f"C.3: Soft-deleted {n_softdel} inherited verse_context_group rows ({len(inherited_group_ids)} distinct group_ids)")

        # Null out the group_id refs on M38 vc rows
        cur.execute("""
            UPDATE verse_context SET group_id=NULL
            WHERE mti_term_id IN (SELECT id FROM mti_terms WHERE cluster_code=?)
              AND group_id IS NOT NULL
              AND COALESCE(delete_flagged,0)=0
        """, (CLUSTER,))
        print(f"C.3: Cleared verse_context.group_id on {cur.rowcount} M38 rows")

        # ── C.4 — new VCG create + verse routing + anchors ────────────────────────────────────────
        cur.execute("""
            UPDATE verse_context SET is_anchor=0
            WHERE mti_term_id IN (SELECT id FROM mti_terms WHERE cluster_code=?)
              AND COALESCE(delete_flagged,0)=0 AND is_anchor=1
        """, (CLUSTER,))
        print(f"C.4: Reset is_anchor=0 on {cur.rowcount} prior-anchor M38 rows")

        vcg_id_by_code: dict[str, int] = {}
        n_vcg_insert = 0
        n_vcg_term_insert = 0
        n_vc_group_update = 0
        n_anchor_set = 0

        for sg_code in sorted(vcg_data.keys()):
            vcgs = vcg_data[sg_code]["vcgs"]
            for vcg in vcgs:
                vcg_code = vcg["provisional_code"]
                cur.execute(
                    """INSERT INTO verse_context_group
                       (group_code, context_description, delete_flagged, vertical_pass_flag)
                       VALUES (?, ?, 0, 0)""",
                    (vcg_code, vcg.get("context_description", "")),
                )
                new_id = cur.lastrowid
                vcg_id_by_code[vcg_code] = new_id
                n_vcg_insert += 1

                # Distinct mti_term_ids for this VCG → vcg_term rows
                if vcg["verses"]:
                    ph = ",".join("?" * len(vcg["verses"]))
                    term_ids = [r[0] for r in cur.execute(
                        f"SELECT DISTINCT mti_term_id FROM verse_context WHERE id IN ({ph})",
                        vcg["verses"]
                    ).fetchall()]
                    for tid in term_ids:
                        cur.execute(
                            """INSERT INTO vcg_term (vcg_id, mti_term_id, delete_flagged, created_at, last_updated_date)
                               VALUES (?, ?, 0, ?, ?)""",
                            (new_id, tid, NOW, NOW),
                        )
                        n_vcg_term_insert += 1

                # UPDATE verse_context.group_id for each member (primary assignment)
                for vc_id in vcg["verses"]:
                    cur.execute("UPDATE verse_context SET group_id=? WHERE id=?", (new_id, vc_id))
                    n_vc_group_update += cur.rowcount

                # is_anchor=1 for anchor vc_id
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

        # ── C.6 — seed cluster_observation rows from B.1 cross-register flags + B.2 notes ─────────
        observations = []
        # B.1 cross-register flags (from verdicts)
        for v in debate.get("verdicts", []):
            if v.get("cross_register_flag"):
                observations.append({
                    "source_phase": "B.1",
                    "title": f"{v['strongs']} {v['transliteration']} cross-register flag",
                    "description": v["cross_register_flag"],
                    "target_phase": "D",
                    "source_file": "WA-M38-constitution-debate-v1-20260528.md",
                })
        # B.2 notes
        b2_notes = [
            {
                "source_phase": "B.2",
                "title": "M38 cluster is multi-characteristic under v3_0",
                "description": (
                    "M38 is multi-characteristic — 7 distinct characteristics (eschatological salvation, "
                    "physical rescue, healing-spiritual wholeness, atoned conscience, priestly mediation, "
                    "salvation anticipated, ransomed identity). The three semantic registers from the "
                    "constitution report (salvation/atonement/gift) integrated into seven sub-groups via the "
                    "researcher-directed BOUNDARY resolutions on sōzō (sense-split) and ka.phar (register-split)."
                ),
                "target_phase": "D",
                "source_file": "WA-M38-subgroup-design-v1-20260528.md",
            },
            {
                "source_phase": "B.2",
                "title": "M38-A approaches the 40% distribution gate (39.0%)",
                "description": (
                    "M38-A (Eschatological salvation received by faith) holds 121/310 = 39.0% of cluster verses, "
                    "right against the §6.2.7 hard gate. Future revision may volume-split this sub-group along "
                    "an axis such as NT-faith vs OT-prefigurement, christological vs general, or salvation-by-"
                    "grace vs salvation-by-confession-and-calling. Phase D analytical findings will inform whether "
                    "this volume-split is needed."
                ),
                "target_phase": "D",
                "source_file": "WA-M38-subgroup-design-v1-20260528.md",
            },
            {
                "source_phase": "B.2",
                "title": "Emergent characteristic — Salvation anticipated and hope sustained (M38-F)",
                "description": (
                    "M38-F was not part of the working cluster characteristic statement; it emerged from the "
                    "Pass A keyword analytics — particularly the 'hope sustained' (25 hits) and 'eschatological' "
                    "(93 hits) keyword pattern across ye.shu.ah (Gen 49:18, Isa 25:9) and NT soteria/sōtēr in "
                    "their anticipation-of-coming-salvation register. This is the 'expect the unexpected' "
                    "discipline yielding a substantive characteristic the cluster name did not predict."
                ),
                "target_phase": "D",
                "source_file": "WA-M38-subgroup-design-v1-20260528.md",
            },
            {
                "source_phase": "B.2",
                "title": "sōzō sense-split honoured at sub-group level",
                "description": (
                    "Researcher direction (BOUNDARY resolution) required sōzō's three discriminable senses to "
                    "operate distinctly. The B.2 design placed eschatological in M38-A (68v), physical rescue in "
                    "M38-B (12v), and healing-spiritual in M38-C (12v). Phase D should examine whether the sense "
                    "boundaries hold under analytical scrutiny — particularly whether physical-rescue M38-B "
                    "carries enough salvation-relevant inner content to remain in M38 or should transfer to a "
                    "non-salvation rescue/danger cluster (no such cluster currently named in the programme)."
                ),
                "target_phase": "D",
                "source_file": "WA-M38-subgroup-design-v1-20260528.md",
            },
            {
                "source_phase": "B.2",
                "title": "ka.phar dual-register honoured at sub-group level",
                "description": (
                    "Researcher direction (BOUNDARY resolution) required ka.phar's two distinct registers to "
                    "operate separately. M38-D holds the atoned-state inner-being (33 ka.phar + 6 Greek "
                    "propitiation verses; conscience cleansed, guilt removed, forgiven). M38-E holds the "
                    "priestly-mediation machinery (44 ka.phar verses; what the priest does on behalf of others). "
                    "Phase D T6 should articulate the structural relationship between M38-D (effect) and M38-E "
                    "(mechanism). Session D synthesis may revisit the OT/NT change to atonement-as-inner-being "
                    "given Christ's once-for-all priestly mediation."
                ),
                "target_phase": "D",
                "source_file": "WA-M38-subgroup-design-v1-20260528.md",
            },
            {
                "source_phase": "B.2",
                "title": "OT/NT atonement transformation — Session D question",
                "description": (
                    "Researcher direction (2026-05-28): the OT-to-NT transformation in cleansing/atonement/role "
                    "of sacrifice and its bearing on inner being is to be addressed in Session D, not in M38's "
                    "individual cluster analysis. The current M38-D/E split (atoned-state vs priestly mediation) "
                    "serves that future synthesis adequately. M11 Repentance was the previous cluster where "
                    "atonement was analysed in a different context (the kip.per/sa.lach Levitical pair, NT "
                    "afiēmi); cross-cluster Session D should integrate M11's findings with M38's."
                ),
                "target_phase": "Session_D",
                "source_file": "researcher direction 2026-05-28",
            },
        ]
        observations.extend(b2_notes)

        n_obs = 0
        for o in observations:
            cur.execute(
                """INSERT INTO cluster_observation
                   (cluster_code, source_phase, observation_type, target_phase,
                    title, description, status, raised_date,
                    source_file, delete_flagged, created_at, last_updated_date)
                   VALUES (?, ?, ?, ?, ?, ?, 'open', ?, ?, 0, ?, ?)""",
                (CLUSTER, o["source_phase"], "design-note", o["target_phase"],
                 o["title"], o["description"], NOW, o["source_file"], NOW, NOW),
            )
            n_obs += 1
        print(f"C.6: Inserted {n_obs} cluster_observation rows ({len(b2_notes)} B.2 notes + {n_obs - len(b2_notes)} B.1 cross-register flags)")

        # ── C.7 — cluster status flip ────────────────────────────────────────────────────────────
        cur.execute(
            "UPDATE cluster SET status=?, last_updated_date=? WHERE cluster_code=?",
            ("Structurally Ready", NOW, CLUSTER),
        )
        print(f"C.7: cluster.status → 'Structurally Ready' (rows={cur.rowcount})")

        # ── Post-checks ──────────────────────────────────────────────────────────────────────────
        print("\n=== Post-checks ===")
        n_sg = cur.execute("SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]
        n_char = cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]
        n_csg = cur.execute("""
            SELECT COUNT(*) FROM characteristic_subgroup csg
            JOIN characteristic ch ON ch.id=csg.characteristic_id
            WHERE ch.cluster_code=? AND COALESCE(csg.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        n_new_vcg = cur.execute("""
            SELECT COUNT(*) FROM verse_context_group vcg
            WHERE vcg.id IN (
                SELECT DISTINCT group_id FROM verse_context vc
                JOIN mti_terms m ON m.id=vc.mti_term_id
                WHERE m.cluster_code=? AND vc.group_id IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0
            ) AND COALESCE(vcg.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        n_assigned = cur.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms m ON m.id = vc.mti_term_id
            WHERE m.cluster_code=? AND vc.is_relevant=1
              AND vc.cluster_subgroup_id IS NOT NULL AND vc.group_id IS NOT NULL
              AND COALESCE(vc.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        n_anchors = cur.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms m ON m.id = vc.mti_term_id
            WHERE m.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        n_status = cur.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()[0]

        print(f"  cluster_subgroup rows: {n_sg} (expected 7)")
        print(f"  characteristic rows: {n_char} (expected 7)")
        print(f"  characteristic_subgroup rows: {n_csg} (expected 7)")
        print(f"  Active VCG rows for cluster: {n_new_vcg} (expected 45)")
        print(f"  IB verses fully assigned (sg + group): {n_assigned} (expected {n_ib})")
        print(f"  Anchor rows: {n_anchors} (expected 45)")
        print(f"  cluster.status: {n_status}")

        ok = (n_sg == 7 and n_char == 7 and n_csg == 7 and n_new_vcg == 45
              and n_assigned == n_ib and n_anchors == 45 and n_status == "Structurally Ready")
        if not ok:
            print("\nABORT: post-check mismatch — rolling back.")
            conn.rollback()
            return 2

        conn.commit()
        print("\nCOMMITTED.")
        return 0

    except Exception as e:
        print(f"ERROR: {e}")
        conn.rollback()
        raise


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
