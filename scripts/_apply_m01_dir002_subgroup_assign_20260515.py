"""Apply DIR-20260515-002 — M01 Phase 4 sub-group assignment.

Source: Sessions/Session_Clusters/M01/wa-cluster-M01-dir-001-subgroup-assign-v1-20260515.md

Operations (all in one transaction):
  1. INSERT 9 cluster_subgroup rows (M01-A..M01-H, M01-BOUNDARY)
  2. INSERT 86 mti_term_subgroup rows (82 primary + 4 secondary cross-listings)
  3. UPDATE cluster.status M01: 'Data - In Progress' → 'Analysis - In Progress'

Schema note: directive references `mti_terms.cluster_subgroup_id`. That column
does not exist on mti_terms — the cluster-to-subgroup mapping is held entirely
in the m:n table `mti_term_subgroup`. CC uses the m:n table per schema reality
(same precedent as DIR-20260515-001).

Cross-listed terms (per directive Outcome §2 — listed under two sub-groups):
  - H2865 cha.tat (703):  primary M01-D + secondary M01-A
  - H2730 cha.red (310):  primary M01-A + secondary M01-E
  - G5156 tromos (308):   primary M01-E + secondary M01-A
  - H6206 a.rats (306):   primary M01-A + secondary M01-E

Usage: python scripts/_apply_m01_dir002_subgroup_assign_20260515.py [--dry-run]
"""
import shutil
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
BACKUP_DIR = REPO / "backups"
DIRECTIVE = "DIR-20260515-002 (wa-cluster-M01-dir-001-subgroup-assign-v1-20260515)"

# Sub-group definitions — order is execution order; sort_order set 1..9
SUBGROUPS = [
    ("M01-A", "Reverential Fear / Fear of God",
     "The fear of the Lord as the proper inner orientation — reverential awe before divine majesty, the beginning of wisdom, the ground of covenant obedience and worship. God is the object; wisdom, holiness, and faithful conduct are the outcomes."),
    ("M01-B", "Threatening / Creaturely Fear",
     "The alarm-response to perceived danger — fear of enemies, threatening powers, circumstances, and death. Includes the divine 'do not fear' reassurance commands, whose meaning requires the threatening fear to be identified."),
    ("M01-C", "Terror and Dread",
     "Overwhelming, acute terror — externally imposed, comprehensive, often divinely sent. The inner being not merely afraid but engulfed, overwhelmed, and shattered. The most intense end of the fear spectrum."),
    ("M01-D", "Dismay and Alarm",
     "The destabilising, paralysing form of fear — the inner collapse of composure under threat; the overwhelmed and immobilised inner person, unable to act."),
    ("M01-E", "Trembling and Shuddering",
     "The somatic-inner expression of fear, dread, and awe — trembling and shuddering as the felt inner-bodily manifestation across the full fear spectrum. Names what fear looks like as it moves through the body-inner interface."),
    ("M01-F", "Anxiety",
     "Chronic, anticipatory inner-being agitation — accumulated apprehensive thoughts, worried restlessness, the inner person dwelling on feared possibilities. Temporal structure is forward-looking and sustained, not immediate-response."),
    ("M01-G", "Awe and Wonder",
     "Overwhelmed astonishment before the extraordinary — the wonder-fear response to divine action, miraculous presence, or the unexpected. Astonishment is the primary element; fear is secondary and derivative."),
    ("M01-H", "Timidity and Cowardice",
     "The dispositional form of fear — the settled inner orientation of fearfulness that impairs faith and action. Cowardice as a moral inner condition: the person characterised by chronic fearfulness rather than trust."),
    ("M01-BOUNDARY", "Boundary",
     "Terms held in BOUNDARY pending programme-level cluster reassignment decision. Current content: perplexity/bewilderment terms (cognitive disorientation — being at a loss before the inexplicable). Distinct from fear; no current cluster home."),
]

# Each tuple = (mti_id, strongs, [(subgroup_code, role, note)])
# role: "primary" or "secondary"
ASSIGNMENTS = [
    # M01-A primaries
    (269, "H3374", [("M01-A", "primary", "definitive fear-of-God noun")]),
    (298, "H3372G", [("M01-A", "primary", "primary A; VCG-003 content verse-routed to B in Phase 6")]),
    (1682, "H3372H", [("M01-A", "primary", "to fear: revere")]),
    (1681, "H3373", [("M01-A", "primary", "God-fearing person")]),
    (266, "G5401", [("M01-A", "primary", "primary A; VCG-003 verse-routed to B")]),
    (292, "G5399", [("M01-A", "primary", "primary A; VCG-003 verse-routed to B")]),
    (291, "H6342", [("M01-A", "primary", "primary A (VCG-002); VCG-001 verse-routed to B")]),
    (829, "H6343", [("M01-A", "primary", "primary A (VCG-001 Fear of Isaac); VCGs-002,003,004 verse-routed to B/C")]),
    (263, "H6345", [("M01-A", "primary", "reverential fear of God owed but absent")]),
    (290, "H1481C", [("M01-A", "primary", "primary A (VCG-001); VCG-002 verse-routed to B")]),
    (270, "H4172A", [("M01-A", "primary", "primary A (VCG-002); VCG-001 verse-routed to C")]),
    (271, "H4172B", [("M01-A", "primary", "primary A (VCG-002); VCG-001 verse-routed to C")]),
    (272, "H4035", [("M01-A", "primary", "fears as divine-judgment instrument — fear-of-God register")]),
    (704, "G6015", [("M01-A", "primary", "reverent awe for worship")]),
    (1713, "H7578", [("M01-A", "primary", "trembling of reverential awe/deference")]),
    # Cross-listed: primary A + secondary E
    (310, "H2730", [("M01-A", "primary", "primary A (VCG-001: trembling at word of God)"),
                    ("M01-E", "secondary", "cross-listed in E: trembling vocabulary")]),
    (306, "H6206", [("M01-A", "primary", "primary A (VCG-002: holy reverence); VCG-001 verse-routed to B"),
                    ("M01-E", "secondary", "cross-listed in E: trembling vocabulary")]),

    # M01-B primaries (13)
    (257, "G1719", [("M01-B", "primary", "afraid before divine/threatening presence")]),
    (296, "H3025", [("M01-B", "primary", "fearful dread before what may befall")]),
    (276, "H3016", [("M01-B", "primary", "inner condition of fear before powerful enemy")]),
    (286, "H4032", [("M01-B", "primary", "comprehensive inner terror of being surrounded")]),
    (273, "H4034", [("M01-B", "primary", "inner fears that oppress the person")]),
    (297, "H7297", [("M01-B", "primary", "fear commanded against in divine reassurance")]),
    (267, "G4423", [("M01-B", "primary", "inner condition of fear before what is frightening")]),
    (1690, "G4422", [("M01-B", "primary", "inner fear-response to alarming events")]),
    (1692, "G4426", [("M01-B", "primary", "inner intimidation by hostile opposition")]),
    (274, "G5398", [("M01-B", "primary", "divine judgment/presence as terror-inducing quality")]),
    (283, "G1630", [("M01-B", "primary", "overwhelming inner terror before divine presence")]),
    (294, "H1763", [("M01-B", "primary", "commanded reverence / inner terror before visions/powers")]),
    (1734, "H2119B", [("M01-B", "primary", "dread-filled trembling before God/power")]),

    # M01-C primaries (17)
    (284, "H0367", [("M01-C", "primary", "")]),
    (1156, "H1091", [("M01-C", "primary", "")]),
    (1154, "H1205", [("M01-C", "primary", "")]),
    (1152, "H4288", [("M01-C", "primary", "")]),
    (1151, "H2851", [("M01-C", "primary", "")]),
    (1155, "H2847", [("M01-C", "primary", "")]),
    (1723, "H2844A", [("M01-C", "primary", "")]),
    (1729, "H2849", [("M01-C", "primary", "")]),
    (1730, "H2866", [("M01-C", "primary", "")]),
    (1720, "H8606", [("M01-C", "primary", "")]),
    (1776, "H4637", [("M01-C", "primary", "")]),
    (1777, "H6178", [("M01-C", "primary", "")]),
    (1722, "H0366", [("M01-C", "primary", "")]),
    (1157, "H2283", [("M01-C", "primary", "")]),
    (1162, "H2189", [("M01-C", "primary", "")]),
    (1161, "H8047G", [("M01-C", "primary", "")]),
    (162, "H4712", [("M01-C", "primary", "")]),

    # M01-D primaries (5) — H2865 cross-listed
    (92, "H0926", [("M01-D", "primary", "")]),
    (5187, "H0927", [("M01-D", "primary", "")]),
    (703, "H2865", [("M01-D", "primary", "primary D"),
                    ("M01-A", "secondary", "VCG-003 (reverential awe) verse-routed to A in Phase 6")]),
    (1732, "H8541", [("M01-D", "primary", "")]),
    (152, "H3735", [("M01-D", "primary", "")]),

    # M01-E primaries (17 unique)
    (305, "H2729", [("M01-E", "primary", "")]),
    (309, "H2731", [("M01-E", "primary", "")]),
    (1554, "H7264", [("M01-E", "primary", "")]),
    (1576, "H7268", [("M01-E", "primary", "")]),
    (1577, "H7269", [("M01-E", "primary", "")]),
    (1793, "H7460", [("M01-E", "primary", "")]),
    (1792, "H7461A", [("M01-E", "primary", "")]),
    (311, "H7461B", [("M01-E", "primary", "")]),
    (1744, "H8175A", [("M01-E", "primary", "")]),
    (1746, "H8178A", [("M01-E", "primary", "")]),
    (282, "H6427", [("M01-E", "primary", "")]),
    (1719, "H6426", [("M01-E", "primary", "")]),
    (1158, "H2113", [("M01-E", "primary", "")]),
    (279, "H7374", [("M01-E", "primary", "")]),
    (1733, "H8429", [("M01-E", "primary", "")]),
    (308, "G5156", [("M01-E", "primary", "primary E"),
                    ("M01-A", "secondary", "VCG-002 (trembling reverential service) verse-routed to A")]),
    (307, "G1790", [("M01-E", "primary", "")]),

    # M01-F (3)
    (107, "H1674", [("M01-F", "primary", "")]),
    (349, "H8312", [("M01-F", "primary", "")]),
    (2, "G0085", [("M01-F", "primary", "")]),

    # M01-G (4)
    (16, "G1568", [("M01-G", "primary", "")]),
    (5126, "G1569", [("M01-G", "primary", "")]),
    (1245, "G2285", [("M01-G", "primary", "")]),
    (289, "H8539", [("M01-G", "primary", "")]),

    # M01-H (3)
    (288, "G1167", [("M01-H", "primary", "")]),
    (261, "G1168", [("M01-H", "primary", "")]),
    (1701, "G1169", [("M01-H", "primary", "")]),

    # M01-BOUNDARY (3)
    (4481, "G1280", [("M01-BOUNDARY", "primary", "perplexity/bewilderment — held for cluster reassignment")]),
    (4482, "G0639", [("M01-BOUNDARY", "primary", "perplexity/bewilderment — held for cluster reassignment")]),
    (4483, "H7672", [("M01-BOUNDARY", "primary", "perplexity/bewilderment — held for cluster reassignment")]),
]


def main():
    dry_run = "--dry-run" in sys.argv

    # Pre-apply backup (only on live)
    if not dry_run:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP_DIR / f"bible_research_backup_{ts}_DIR-20260515-002.db"
        shutil.copy2(DB, backup_path)
        print(f"[BACKUP] {backup_path.name}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    counts = {"cluster_subgroup_inserts": 0, "mti_term_subgroup_inserts": 0, "cluster_status_updates": 0}

    try:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        # Pre-condition: term count
        n = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M01' "
            "AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        if n != 82:
            raise RuntimeError(f"Pre-condition fail: M01 active term count is {n}, expected 82")

        # Pre-condition: no existing M01 subgroups
        n_sg = conn.execute(
            "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M01' "
            "AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        if n_sg != 0:
            raise RuntimeError(f"Pre-condition fail: {n_sg} M01 subgroups already exist")

        # 1. INSERT 9 cluster_subgroup rows
        sg_id_map: dict[str, int] = {}
        for sort_order, (code, label, desc) in enumerate(SUBGROUPS, start=1):
            cur = conn.execute(
                """INSERT INTO cluster_subgroup
                   (cluster_code, subgroup_code, label, core_description, sort_order,
                    status, version, source, notes, delete_flagged, created_at, last_updated_date)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)""",
                ("M01", code, label, desc, sort_order, "active", "v1",
                 DIRECTIVE, f"Created by {DIRECTIVE}", now, now)
            )
            sg_id_map[code] = cur.lastrowid
            counts["cluster_subgroup_inserts"] += 1

        # 2. INSERT mti_term_subgroup rows
        for mti, strongs, sgs in ASSIGNMENTS:
            for sg_code, role, note in sgs:
                sg_id = sg_id_map[sg_code]
                placement_note = f"{DIRECTIVE} [{role}]"
                if note:
                    placement_note += f": {note}"
                conn.execute(
                    """INSERT INTO mti_term_subgroup
                       (mti_term_id, cluster_subgroup_id, placement_note,
                        delete_flagged, created_at, last_updated_date)
                       VALUES (?, ?, ?, 0, ?, ?)""",
                    (mti, sg_id, placement_note, now, now)
                )
                counts["mti_term_subgroup_inserts"] += 1

        # 3. UPDATE cluster.status
        rc = conn.execute(
            """UPDATE cluster
               SET status='Analysis - In Progress', last_updated_date=?
               WHERE cluster_code='M01' AND status='Data - In Progress'""",
            (now,)
        ).rowcount
        if rc != 1:
            raise RuntimeError(f"Cluster status update affected {rc} rows; expected 1")
        counts["cluster_status_updates"] = rc

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
        print(f"\nERROR: {exc}\nTransaction rolled back.")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
