"""M03 characteristic backfill (test cluster for pre-v2_6 characteristic retrofit).

Per researcher direction 2026-05-27: 10 pre-v2_6 closed clusters lack
`characteristic` rows (M01, M02, M03, M05, M06, M15, M20, M26, M39, M46).
This script does the M03 retrofit as a clean-test pattern that will scale
to the others.

M03's sub-group descriptions (Phase 5 design under v2_x) explicitly name
"the unifying characteristic" of each sub-group. Mapping is therefore 1:1:
sub-group LABEL → characteristic SHORT_NAME; core_description → definition.
BOUNDARY sub-group is structural-holding (not a characteristic).

Operations (single transaction):
- Op A: INSERT 7 characteristic rows (char_seq 1-7)
- Op B: INSERT 7 characteristic_subgroup links (1:1, is_partial=0)
- Op C: UPDATE cluster_finding.characteristic_id for findings scoped to
        a substantive M03 sub-group (joined via characteristic_subgroup)
"""
from __future__ import annotations
import argparse, io, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CLUSTER = "M03"
SOURCE = "Pre-v2_6 characteristic backfill 2026-05-27 — derived 1:1 from cluster_subgroup label + core_description"


# (char_seq, short_name, subgroup_code, definition)
# Definitions taken directly from each sub-group's core_description.
CHARACTERISTICS = [
    (1, "Weeping and tears", "M03-A",
     "The somatic and visible expression of grief through weeping and tears. The inner state overflows outward "
     "into the body — tears drench the bed, exhaust the eyes, flow continuously on the face, or are so abundant "
     "the prophet longs for a fountain to sustain them. Tears function as recognised evidence of inner grief: "
     "God sees them, hears the sound of them, and records them. Weeping is communal as well as personal, "
     "penitential as well as bereavement-driven. The characteristic names the act, sound, or substance of "
     "weeping and tears as the primary inner-grief indicator."),
    (2, "Mourning and lamentation", "M03-B",
     "The act and condition of mourning — the outward form that grief takes in its social, ritual, communal, "
     "and personal expression. Mourning is the structured or habitual pattern of grief: mourning periods, "
     "mourning garments, lament cries, communal wailing. Includes both personal mourning for the dead and "
     "national disaster, and divinely commanded or withheld mourning that marks the God-people relationship. "
     "Mourning is what God himself addresses and reverses: the mourner is the target of divine consolation, "
     "and mourning is what eschatological joy displaces. The characteristic names mourning as the human act "
     "and state of grief given outward, socially recognised form."),
    (3, "Sorrow and inner grief", "M03-C",
     "Grief as a settled inner emotional condition — the state of the person who is sorrowful, grieved, or "
     "weighted with sorrow in the soul and heart. Grief is located in the inner person directly: Jesus's soul "
     "is very sorrowful, even to death; sorrow is lodged in the heart all day long; grief is so deep the soul "
     "melts away. The distinguishing feature is the inner-state character of the grief — the sorrow is felt, "
     "located in the heart or soul, and experienced as an inner condition rather than primarily expressed "
     "outward. This register includes grief that is morally motivated, grief at relational loss, grief that "
     "coexists with joy, and godly grief that produces repentance."),
    (4, "Anguish and distress", "M03-D",
     "Grief's most intense, overwhelming form — anguish as a pressing, constricting, crushing inner state. "
     "Distress is a force that presses in on the inner person, grips the soul and spirit, and drives the "
     "sufferer to cry out to God for deliverance. The two largest corpora in the cluster — tsa.rah (62 verses) "
     "and tsar (28 verses) — both consistently show distress as the inner-being crisis driving prayer and from "
     "which God delivers. The Greek anguish vocabulary supplements this: sunochē (heart-seated anguish), "
     "odunaō (anguish at relational loss and afterlife), odunē (heart-located unceasing sorrow). The "
     "characteristic names anguish as the most acute and pressing form of inner suffering."),
    (5, "Groaning and sighing", "M03-E",
     "The involuntary or deliberate vocal and bodily expression of grief through groaning, sighing, and "
     "travail-like utterance. Groaning and sighing are the deep inner pressure of grief or suffering finding "
     "their outward voice — often rising to God as a cry or appeal. Israel groans under slavery and their cry "
     "rises to God covenantally. The Spirit intercedes with groanings too deep for words within the believer's "
     "spirit. All creation groans together in birth-pain anguish oriented toward redemption. The travail "
     "vocabulary belongs here: ōdinō names the consuming, involuntary anguish of labour used metaphorically "
     "for apostolic inner travail. The characteristic names grief expressed as the groan, sigh, or travail-cry."),
    (6, "Pain and inner ache", "M03-F",
     "Grief at the level of pain — the ache, wound, and soreness of the inner person. Suffering felt as pain "
     "in body and soul simultaneously, often persistent and inescapable. The servant is a man of sorrows, "
     "deeply familiar with grief, bearing the people's sorrows as a burden. Unceasing pain erodes trust in "
     "the divine relationship. The heart can ache beneath outward laughter. The birth-pangs vocabulary of "
     "che.vel-B uses labour-pain imagery consistently as a metaphor for acute, involuntary seizure of inner "
     "anguish. The characteristic names pain as the primary phenomenological quality of grief — what grief "
     "feels like from within."),
    (7, "Bitterness of soul", "M03-G",
     "The specific inner quality of bitterness that arises from grief, suffering, loss, and divine dealings — "
     "the soul's experience of something that has become harsh, sharp, and without sweetness. Bitterness is an "
     "intensification or colouring of grief: God fills the inner being with bitterness to saturation, leaving "
     "no room for relief; bitterness is located in the heart as a private inner experience no outsider can "
     "share; a foolish son inflicts sharp bitter pain on his mother through his failure; harshness produces "
     "bitterness in another person's spirit. This is bitterness-of-soul rather than anger-bitterness, arising "
     "from grief, loss, suffering, and divine dealings — what grief tastes like when it is at its sharpest."),
]


def main(live: bool) -> int:
    print(f"=== M03 characteristic backfill — mode={'LIVE' if live else 'DRY-RUN'} ===")
    conn = sqlite3.connect(DB, timeout=120.0)
    conn.execute("PRAGMA busy_timeout = 120000")
    conn.row_factory = sqlite3.Row

    # Pre-check: no characteristics already
    n_existing = conn.execute(
        "SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()[0]
    if n_existing:
        print(f"ABORT: {n_existing} characteristic rows already exist for {CLUSTER}")
        return 1

    # Resolve sub-group ids
    sg_id_by_code = {r["subgroup_code"]: r["id"] for r in conn.execute(
        "SELECT subgroup_code, id FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchall()}
    print(f"M03 sub-groups in DB: {len(sg_id_by_code)} -> {sorted(sg_id_by_code.keys())}")
    missing = [c[2] for c in CHARACTERISTICS if c[2] not in sg_id_by_code]
    if missing:
        print(f"ABORT: sub-groups missing in DB: {missing}")
        return 1
    print(f"All 7 characteristic-target sub-groups exist")

    # Plan summary
    print("\nProposed characteristics (1:1 from sub-groups):")
    for seq, short, sg_code, defn in CHARACTERISTICS:
        sg_id = sg_id_by_code[sg_code]
        n_findings = conn.execute(
            "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=? AND cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
            (CLUSTER, sg_id)
        ).fetchone()[0]
        print(f"  char_seq={seq} → {sg_code} ({n_findings} findings to backfill char_id): {short}")

    if not live:
        print("\n[DRY-RUN — no writes]")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        char_id_by_seq = {}
        for seq, short, sg_code, defn in CHARACTERISTICS:
            cur.execute(
                "INSERT INTO characteristic "
                "(cluster_code, char_seq, short_name, definition, source, version, "
                " delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'v1', 0, ?, ?)",
                (CLUSTER, seq, short, defn, SOURCE, NOW, NOW),
            )
            char_id_by_seq[seq] = cur.lastrowid
        print(f"\nOp A: inserted {len(CHARACTERISTICS)} characteristic rows")

        n_csg = 0
        for seq, short, sg_code, defn in CHARACTERISTICS:
            cur.execute(
                "INSERT INTO characteristic_subgroup "
                "(characteristic_id, cluster_subgroup_id, qualifier_note, is_partial, "
                " delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, 0, ?, ?)",
                (char_id_by_seq[seq], sg_id_by_code[sg_code],
                 f"1:1 mapping from M03 sub-group {sg_code} (Pre-v2_6 backfill)", NOW, NOW),
            )
            n_csg += 1
        print(f"Op B: inserted {n_csg} characteristic_subgroup links (1:1, is_partial=0)")

        # Op C: backfill cluster_finding.characteristic_id
        n_updated = 0
        for seq, short, sg_code, defn in CHARACTERISTICS:
            sg_id = sg_id_by_code[sg_code]
            cur.execute(
                "UPDATE cluster_finding SET characteristic_id=?, last_updated_date=? "
                "WHERE cluster_code=? AND cluster_subgroup_id=? AND characteristic_id IS NULL "
                "AND COALESCE(delete_flagged,0)=0",
                (char_id_by_seq[seq], NOW, CLUSTER, sg_id),
            )
            n_updated += cur.rowcount
        print(f"Op C: backfilled {n_updated} cluster_finding.characteristic_id values")

        # Post-checks
        n_chars = conn.execute(
            "SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
            (CLUSTER,)
        ).fetchone()[0]
        assert n_chars == 7
        n_links = conn.execute(
            "SELECT COUNT(*) FROM characteristic_subgroup csg "
            "JOIN characteristic ch ON ch.id=csg.characteristic_id "
            "WHERE ch.cluster_code=? AND COALESCE(csg.delete_flagged,0)=0",
            (CLUSTER,)
        ).fetchone()[0]
        assert n_links == 7
        print(f"\nPost-check: {n_chars} characteristics, {n_links} subgroup links ✓")

        conn.commit()
        print(f"COMMITTED at {NOW}")
    except Exception as e:
        conn.rollback()
        print(f"ROLLED BACK: {e}")
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
