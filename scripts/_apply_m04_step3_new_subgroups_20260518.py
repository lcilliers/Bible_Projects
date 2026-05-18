"""M04 retrofit Step 3: create 6 new sub-groups + assign register-family verses.

Researcher-approved 2026-05-18: "I agree with new sub groups, I suggest you add
these and assign the verses."

Creates M04-K through M04-P for register families that v2_5 §1.1 brings into
inner-being scope but M04's original Phase 5 design did not accommodate. The 65
affected verses are currently parked in M04-BOUNDARY; this script PROMOTEs them
to the new substantive sub-groups per v2_5 §18.2.

Operations (one transaction):
1. INSERT 6 cluster_subgroup rows (M04-K through M04-P)
2. INSERT mti_term_subgroup links for each (term, new sub-group) pair
3. UPDATE verse_context.cluster_subgroup_id for the 65 affected verses
4. Update group_id to NULL (VCG to be re-assigned in Step 5)

Writes an applied-report markdown at:
  Sessions/Session_Clusters/M04/WA-M04-step3-new-subgroups-applied-v1-{date}.md
"""
from __future__ import annotations
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
NOW_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SOURCE = "M04-retrofit-step3-20260518"
OUT = Path(f"Sessions/Session_Clusters/M04/WA-M04-step3-new-subgroups-applied-v1-{TODAY}.md")

# ---------------------------------------------------------------------------
# Sub-group design (lifted from Pass A meaning corpus 2026-05-18)
# ---------------------------------------------------------------------------

NEW_SUBGROUPS = [
    {
        "code": "M04-K",
        "label": "Material and Sensory Pleasure: Luxury, Sensory Enjoyment, and Aromatic Sacrifice",
        "core_description": (
            "Pleasantness as a sensory or material register. Includes the inner satisfaction of "
            "refined comfort and dainty living (a.nog, ta.a.nug — pampered ease in Deu 28, Isa 47, "
            "Ecc 2, Pro 19, Song 7); the soothing-aroma metonym for divine reception of correct "
            "worship (ni.cho.ach — Lev 1, 23; Num 15, 28); the wicked man's denied enjoyment "
            "(a.las — Job 20); the seductress's carnal delight (a.las — Pro 7); the disciples' "
            "amazement at Jesus' wealth-and-kingdom teaching (thambeō — Mar 10:24); and tov as "
            "material or sensory goodness (Psa 34 'taste and see'; Pro 22 favor as silver-gold; "
            "Jer 22 wellbeing as flourishing). Inner-being-in-bodily-experience: pleasantness "
            "registered through the senses or material conditions, ranging from righteous "
            "worship-reception to illicit luxury to siege-curse refinement under judgment."
        ),
        "register": "material_sensory",
    },
    {
        "code": "M04-L",
        "label": "Evaluative Goodness: Moral and Relational Appraisal of What is Surpassing",
        "core_description": (
            "Tov used as the inner-being faculty of moral or relational evaluation — the soul's "
            "assessment that something is 'good,' 'better than,' or 'surpassing.' Includes Ruth's "
            "love-for-Naomi appraised as surpassing seven sons (Rut 4:15); God's chesed evaluated "
            "as surpassing life itself (Psa 63:3); the youths' 'good appearance' (Dan 1:4) as an "
            "external-quality appraisal; the people judging Egypt-return as better than Canaan "
            "(Num 14:3); 'good and bad' from God's mouth (Lam 3:38); and similar evaluative-"
            "comparative judgments where the soul names what is surpassing in worth. "
            "Inner-being-as-evaluation: the faculty by which a person appraises moral or "
            "relational worth."
        ),
        "register": "judgment_evaluative",
    },
    {
        "code": "M04-M",
        "label": "Pleasing as Obedience: Inner Orientation Toward What is Acceptable to God",
        "core_description": (
            "What is pleasing, fitting, or acceptable in God's sight — framed as the obedient "
            "soul's directed orientation. arestos verses (Joh 8:29 — Jesus doing what pleases the "
            "Father continually; Act 6:2 procedural acceptable; 1Jo 3:22 pleasing God through "
            "obedience as ground of answered prayer); tov verses where inner obedience-character "
            "is named as the 'good' that surpasses sacrifice (1Sa 15:22) and God's 'good things' "
            "as the obedience-consequence promises (Jos 23:15); ni.cho.ach as the soothing aroma "
            "of correct sacrificial obedience (Lev 1:17 torn bird; Num 15:13 every native's food "
            "offering). Inner-being-as-volitional-orientation toward the divine standard."
        ),
        "register": "obedience_fitting",
    },
    {
        "code": "M04-N",
        "label": "Horizontal Relational Delight: Pleasantness Between Persons (Parental, Neighbour, Captivation)",
        "core_description": (
            "Inner-being pleasantness in the horizontal register — between persons rather than "
            "vertically Godward. Parental delight in children (ta.a.nug — Mic 1:16 'children of "
            "your delight'); the value of a nearby neighbour (tov — Pro 27:10 closer than distant "
            "brother) and its negation in the violent man (Pro 16:29); the world's collective "
            "marvelling-captivation at the beast's apparent resurrection (thaumazō — Rev 13:3, "
            "17:8) as horizontal-attention drawn in awe. Inner-being-in-relationship: pleasantness, "
            "captivation, or wonder directed at persons, ranging from tender attachment to "
            "corrupted captivation."
        ),
        "register": "horizontal_relational",
    },
    {
        "code": "M04-O",
        "label": "Circumstantial Gladness: Good News, Beneficial States, and Refreshing Circumstance",
        "core_description": (
            "Tov used to name circumstantial or situational pleasantness — the goodness of a "
            "circumstance, message, or report registered by the inner being. 'Good man with good "
            "news' (2Sa 18:27); the inner disposition of quiet waiting for salvation as 'good for "
            "the soul' (Lam 3:26); 'good news of happiness' of salvation and peace (Isa 52:7); "
            "the simple meal with love better than the feast with hatred (Pro 15:17); good news "
            "refreshing the bones (Pro 15:30). Inner-being-in-circumstance: the soul's pleasant "
            "response to or recognition of beneficial circumstance."
        ),
        "register": "circumstantial_situational",
    },
    {
        "code": "M04-P",
        "label": "Corrupt and Illicit Delight: Predatory, Lustful, and Misdirected Pleasure",
        "core_description": (
            "Inner-being delight in its corrupt or illicit modes — the morally negative face of "
            "pleasure. Predatory exultation devouring the poor in secret (a.li.tsut — Hab 3:14); "
            "Israel's lust for desirable Assyrian young men (che.med — Eze 23:12); misdirected "
            "sacrificial aroma in illicit worship on high places (ni.cho.ach — Eze 20:28); the "
            "wicked man choosing what is 'not good' as his path (tov as negation — Psa 36:4). "
            "Inner-being-as-disordered-delight: pleasure directed toward objects, persons, or "
            "practices contrary to right order."
        ),
        "register": "corrupt_illicit",
    },
]

# ---------------------------------------------------------------------------
# Register-family scan (replicates audit's keyword logic)
# ---------------------------------------------------------------------------

REGISTER_FAMILY_KEYWORDS = {
    "horizontal_relational": ["parental", "parent", "marital", "spouse", "between people", "neighbour", "neighbor", "horizontal", "human-to-human", "between persons", "interpersonal"],
    "material_sensory": ["luxury", "feast", "sensory", "delicate", "pampered", "refined", "dainty", "material delight", "wealth", "comfort-orientation", "indulgence", "abundance"],
    "corrupt_illicit": ["predatory", "predator", "lustful", "lust", "envy", "covetous", "illicit", "corrupt joy", "seductress", "corrupt delight", "carnal", "wicked man"],
    "circumstantial_situational": ["cheerful heart", "good news", "circumstance", "circumstantial", "situational", "good report"],
    "obedience_fitting": ["pleasing god", "doing what pleases", "obedience", "what is acceptable", "pleases the father"],
    "judgment_evaluative": ["evaluat", "judge as good", "seemed good", "consider good", "consider pleasing"],
}

REGISTER_TO_SUBGROUP = {
    "material_sensory": "M04-K",
    "judgment_evaluative": "M04-L",
    "obedience_fitting": "M04-M",
    "horizontal_relational": "M04-N",
    "circumstantial_situational": "M04-O",
    "corrupt_illicit": "M04-P",
}


def classify_register(note: str) -> str | None:
    note_low = (note or "").lower()
    for family, kws in REGISTER_FAMILY_KEYWORDS.items():
        for kw in kws:
            if kw in note_low:
                return family
    return None


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Get current state
    rows = conn.execute(
        """
        SELECT vc.id AS vc_id, vc.mti_term_id, mt.strongs_number, mt.transliteration,
               vr.reference, vc.analysis_note,
               cs.id AS current_sg_id, cs.subgroup_code AS current_sg_code,
               vr.book_id, vr.chapter, vr.verse_num
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE cs.cluster_code = 'M04' AND cs.subgroup_code = 'M04-BOUNDARY'
          AND vc.is_relevant = 1 AND COALESCE(vc.delete_flagged, 0) = 0
          AND vc.analysis_note IS NOT NULL
        """
    ).fetchall()

    # Classify each
    classified = []
    for r in rows:
        family = classify_register(r["analysis_note"])
        if family:
            classified.append((dict(r), family))

    print(f"Total BOUNDARY verses scanned: {len(rows)}")
    print(f"Classified into register families: {len(classified)}")

    # Determine M04-BOUNDARY sub-group id (need for current_sg verification)
    m04_boundary_id = conn.execute(
        "SELECT id FROM cluster_subgroup WHERE cluster_code='M04' AND subgroup_code='M04-BOUNDARY'"
    ).fetchone()["id"]

    # Determine next sort_order (current M04 max + 1)
    next_sort = conn.execute(
        "SELECT COALESCE(MAX(sort_order), 0) + 1 FROM cluster_subgroup WHERE cluster_code='M04'"
    ).fetchone()[0]

    cur = conn.cursor()
    cur.execute("BEGIN")
    try:
        # 1. INSERT 6 cluster_subgroup rows
        new_subgroup_ids = {}
        for i, sg in enumerate(NEW_SUBGROUPS):
            cur.execute(
                """
                INSERT INTO cluster_subgroup
                  (cluster_code, subgroup_code, label, core_description, sort_order,
                   status, version, source, delete_flagged, created_at, last_updated_date)
                VALUES (?, ?, ?, ?, ?, 'active', 'v1', ?, 0, ?, ?)
                """,
                ("M04", sg["code"], sg["label"], sg["core_description"], next_sort + i,
                 SOURCE, NOW_UTC, NOW_UTC),
            )
            new_subgroup_ids[sg["code"]] = cur.lastrowid
            print(f"  INSERT cluster_subgroup {sg['code']} (id={cur.lastrowid})")

        # 2. INSERT mti_term_subgroup links for each (term, new sub-group) pair.
        #    For each unique (mti_term_id, new_sg_code) combination, INSERT if absent.
        link_inserts = 0
        seen_links = set()
        for verse, family in classified:
            target_sg_code = REGISTER_TO_SUBGROUP[family]
            target_sg_id = new_subgroup_ids[target_sg_code]
            key = (verse["mti_term_id"], target_sg_id)
            if key in seen_links:
                continue
            seen_links.add(key)
            # Check if link already exists (defence)
            existing = cur.execute(
                "SELECT id FROM mti_term_subgroup WHERE mti_term_id=? AND cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
                (verse["mti_term_id"], target_sg_id),
            ).fetchone()
            if existing:
                continue
            cur.execute(
                """
                INSERT INTO mti_term_subgroup
                  (mti_term_id, cluster_subgroup_id, placement_note, delete_flagged, created_at, last_updated_date)
                VALUES (?, ?, ?, 0, ?, ?)
                """,
                (verse["mti_term_id"], target_sg_id,
                 f"[primary/secondary mixed — audit-fix v2_5 Step 3 2026-05-18] Term promoted from M04-BOUNDARY to {target_sg_code} (register: {family}). See applied report.",
                 NOW_UTC, NOW_UTC),
            )
            link_inserts += 1
        print(f"  INSERTed {link_inserts} mti_term_subgroup links")

        # 3. UPDATE verse_context: route verses to new sub-groups; clear group_id (VCG TBD in Step 5)
        updates = 0
        for verse, family in classified:
            target_sg_code = REGISTER_TO_SUBGROUP[family]
            target_sg_id = new_subgroup_ids[target_sg_code]
            cur.execute(
                """
                UPDATE verse_context
                SET cluster_subgroup_id = ?,
                    group_id = NULL,
                    is_anchor = 0,
                    notes = ?
                WHERE id = ? AND COALESCE(delete_flagged, 0) = 0
                """,
                (target_sg_id,
                 f"[audit-fix v2_5 Step 3 2026-05-18] PROMOTED from M04-BOUNDARY to {target_sg_code} ({family} register). VCG to be assigned in Step 5. Pass A meaning preserved in analysis_note.",
                 verse["vc_id"]),
            )
            updates += cur.rowcount
        print(f"  UPDATEd {updates} verse_context rows")

        conn.commit()
        print("\nAll operations committed.")
    except Exception:
        conn.rollback()
        print("ROLLED BACK due to error")
        raise

    # Generate applied-report markdown
    L = []
    L.append("# M04 retrofit Step 3 — new sub-groups + register-family promotions applied")
    L.append("")
    L.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    L.append(f"**Script:** `scripts/_apply_m04_step3_new_subgroups_20260518.py`")
    L.append(f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_5-20260518 §17.5 (audit-fix) + §18.2 PROMOTE-TO-SUBGROUP")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Operations applied")
    L.append("")
    L.append("**1. New cluster_subgroup rows (6):**")
    L.append("")
    L.append("| Code | id | Label |")
    L.append("|---|---:|---|")
    for sg in NEW_SUBGROUPS:
        L.append(f"| {sg['code']} | {new_subgroup_ids[sg['code']]} | {sg['label']} |")
    L.append("")
    L.append(f"**2. New mti_term_subgroup links:** {link_inserts}")
    L.append("")
    L.append(f"**3. verse_context PROMOTE updates:** {updates} (PROMOTED from M04-BOUNDARY)")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Per-sub-group detail")
    L.append("")

    by_sg = defaultdict(list)
    for verse, family in classified:
        by_sg[REGISTER_TO_SUBGROUP[family]].append((verse, family))

    for sg in NEW_SUBGROUPS:
        code = sg["code"]
        verses = by_sg.get(code, [])
        L.append(f"### {code} — {sg['label']} ({len(verses)} verses)")
        L.append("")
        L.append(f"**core_description:** {sg['core_description']}")
        L.append("")
        L.append(f"**Verses promoted:**")
        L.append("")
        L.append("| vc_id | Reference | Term | Pass A meaning (head) |")
        L.append("|---:|---|---|---|")
        for verse, _ in sorted(verses, key=lambda x: (x[0]["book_id"], x[0]["chapter"], x[0]["verse_num"])):
            note_head = (verse["analysis_note"] or "")[:80].replace("|", "\\|")
            L.append(f"| {verse['vc_id']} | {verse['reference']} | {verse['strongs_number']} {verse['transliteration']} | {note_head} |")
        L.append("")
        L.append("---")
        L.append("")

    L.append("## Next step")
    L.append("")
    L.append("Step 4 — Phase 8.5 BOUNDARY resolution on the remaining M04-BOUNDARY verses (post-promotion count ~257). AI task per v2_5 §11A: per-verse disposition (SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP).")
    L.append("")
    L.append("Then Step 5 — VCG design for the 6 new sub-groups (AI task per v2_5 §10).")
    L.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"\nReport written: {OUT}")

    # Sanity counts
    print("\n--- Post-apply M04-BOUNDARY counts ---")
    row = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE cs.cluster_code='M04' AND cs.subgroup_code='M04-BOUNDARY'
          AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """).fetchone()
    print(f"M04-BOUNDARY active relevant verses: {row[0]}")
    for sg in NEW_SUBGROUPS:
        row = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
            WHERE vc.cluster_subgroup_id=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        """, (new_subgroup_ids[sg["code"]],)).fetchone()
        print(f"{sg['code']} active relevant verses: {row[0]}")

    conn.close()


if __name__ == "__main__":
    main()
