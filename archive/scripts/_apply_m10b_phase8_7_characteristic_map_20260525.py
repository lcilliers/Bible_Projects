"""M10b Phase 8.7 — Characteristic mapping load.

Per v2_8 §11B. Per directive wa-cluster-M10b-dir-004-phase8_7-characteristic-map-v1-20260525.md.

M10b Phase 5 produced 6 sub-groups mapping 1:1 to 6 characteristics (the §8.0
default — no volume-splits, no SPLIT_SUBGROUP). Phase 8.7 confirms this by
loading the characteristic rows + characteristic_subgroup links.

Three Phase 7 polysemy notes also load as cluster_observation carry-forwards
for Phase 9 attention (INTEGRATION_NOTE type — VCG-level cross-register signals
already structurally separated at Phase 7).

Operations (single transaction):
- Op A: INSERT 6 characteristic rows (char_seq 1-6, definitions from Phase 5 design)
- Op B: INSERT 6 characteristic_subgroup links (1:1, is_partial=0)
- Op C: INSERT 3 cluster_observation rows (Phase 7 polysemy carry-forwards)
"""
from __future__ import annotations
import argparse, io, shutil, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CLUSTER = "M10b"
DIRECTIVE_ID = "wa-cluster-M10b-dir-004-phase8_7-characteristic-map-v1-20260525"
SOURCE_FILE = "Sessions/Session_Clusters/M10b/WA-M10b-subgroup-design-v1-20260525.md"

# Characteristic definitions (1:1 with sub-groups; from Phase 5 design §1)
CHARACTERISTICS = [
    {
        "char_seq": 1,
        "short_name": "Wickedness as settled person-identity",
        "subgroup_code": "M10b-A",
        "definition": (
            "The wicked person as an inner-being type — the individual whose core moral character is "
            "defined by wickedness. Will corrupted, God actively excluded from the mind (practical "
            "atheism), inner orientation persistently bent toward harm and injustice. Conscience "
            "suppressed or displaced by an inner voice of transgression. Wickedness is not merely a "
            "series of acts but a stable identity and inner condition; divine judgment falls "
            "specifically on this person-type because their inner character warrants it."
        ),
        "qualifier_note": (
            "M10b-A carries the wicked-person evidence in full. Primary terms: ra.sha (179V), "
            "re.sha (9V), mir.sha.at (1V). Includes 1 ro.a verse (1Sa 17:28 — evil in the heart of "
            "a specific accused person). The forensic-verdict sub-corpus within ra.sha (M10b-A-VCG-01, "
            "5V) carries an M10 cross-register flag — ra.sha as legal-status label rather than inner "
            "moral character."
        ),
    },
    {
        "char_seq": 2,
        "short_name": "Evil as constitutional inner nature",
        "subgroup_code": "M10b-B",
        "definition": (
            "Evil as the structural condition of the inner person — not primarily the choice of the "
            "will moment by moment, but the constitutive nature from which corrupt choices flow. The "
            "heart is a treasury of evil that the person draws on; the inner nature is bent toward "
            "corruption as its default output. NT-distinctive analysis: humans constitutionally "
            "incline toward evil, evil thoughts originate in the heart, the heart's evil nature is "
            "the root of all outward moral failure."
        ),
        "qualifier_note": (
            "M10b-B carries the evidence for evil-as-constitutional-nature. Primary terms: ponēros "
            "(63V), kakia (11V), adikia (8V), ponēria (7V), faulos (1V). The cosmic-evil-agent / "
            "evil-one / evil-age sub-corpus within ponēros (M10b-B-VCG-01, 13V) carries an M27 "
            "cross-register flag. Mat 6:34 kakia (M03 trouble register) and Eph 6:12 ponēria (M27 "
            "cosmic-evil) remain in this characteristic as flag-only minorities."
        ),
    },
    {
        "char_seq": 3,
        "short_name": "Abomination — divine revulsion on moral character",
        "subgroup_code": "M10b-C",
        "definition": (
            "The category of evil that violates divine holiness and provokes God's active revulsion "
            "— directed specifically at corrupt moral character and ethical failure rather than "
            "idolatry. Inner-being dimensions: the abominable person's inner state (crooked heart, "
            "proud heart, lying lips, perverted judgment, conscience violated and silenced), and "
            "the divine inner response (revulsion, disgust, hatred, rejection). The three-part "
            "co-occurrence pattern — act defiling + boundary transgressed + divine revulsion — "
            "names the mechanism of abomination."
        ),
        "qualifier_note": (
            "M10b-C carries to.e.vah's moral-character sub-corpus (~70V via passage-driven split: "
            "Proverbs ethical-abomination cluster, conscience-silenced Jer/Eze, idol-folly Isa, "
            "covenant-betrayal Mal), bdelugma's moral verses (4V — Luk 16:15, Rev 17:4/17:5/21:27), "
            "and bdeluktos (1V — Tit 1:16). Distinct from M10b-D (idolatrous abomination) by "
            "register: M10b-C is moral-character, M10b-D is idol-devotion."
        ),
    },
    {
        "char_seq": 4,
        "short_name": "Idolatrous abomination",
        "subgroup_code": "M10b-D",
        "definition": (
            "The specific form of abomination rooted in idolatrous devotion — the will's conformity "
            "to detestable practices, the heart going after idol-objects, worship corrupted through "
            "false devotion. Inner-being dimensions: the heart's defiant attachment to idols, the "
            "soul that actively delights in abominations rather than recoiling, the pride that "
            "converts beautiful gifts into idol-objects, the conscience deadened to the horror of "
            "idolatrous acts."
        ),
        "qualifier_note": (
            "M10b-D carries to.e.vah's idolatry sub-corpus (~72V — Lev boundary-laws, Deuteronomy "
            "warnings, historical reform narratives, Ezra covenant-boundary including Ezr 9:11, "
            "Jeremiah idolatry, Ezekiel idolatry-driving-divine-presence-away), shiq.quts (25V "
            "predominantly idol-objects), and bdelugma's desecration-event verses (2V — Mat 24:15, "
            "Mar 13:14). Strong M27 cross-register flag (idol-object / concrete-abomination); "
            "M10c cross-register flag for the Levitical/Deuteronomic/Ezekiel cultic-defilement "
            "sub-corpora."
        ),
    },
    {
        "char_seq": 5,
        "short_name": "Iniquity as active inner scheming and evil generation",
        "subgroup_code": "M10b-E",
        "definition": (
            "Evil as an ongoing active inner process — devised, cultivated, generated, and enacted "
            "from within. Iniquity is plotted on the bed at night, conceived in the heart, schemed "
            "by the mind, and born into harmful deeds. The evildoer is a person who works iniquity "
            "as a habitual pursuit, exploiting others, lurking with predatory intent. Also "
            "encompasses the evil-deeds register — deeds whose inner origin is wickedness, and "
            "whose quality marks the one who commits them."
        ),
        "qualifier_note": (
            "M10b-E carries a.ven (66V) and ro.a's evil-deeds sub-corpus (13V). The trouble/distress "
            "sub-corpus within a.ven (M10b-E-VCG-01, 7V) carries M03/M27 cross-register flag "
            "(affliction-suffered rather than iniquity-of-the-agent). Neh 2:2 + Ecc 7:3 ro.a (M03 "
            "sadness register) remain as flag-only minorities."
        ),
    },
    {
        "char_seq": 6,
        "short_name": "Evil expressed through speech",
        "subgroup_code": "M10b-F",
        "definition": (
            "The inner character of wickedness expressed through the instrument of speech — the "
            "defiant will that generates contemptuous blasphemy against God even under judgment, "
            "the hostile slander that falsely charges the innocent as evildoers, the deceptive "
            "misrepresentation that inverts moral reality through verbal manipulation. The hardened "
            "will interprets divine judgment as occasion for further defiance."
        ),
        "qualifier_note": (
            "M10b-F carries blasfēmeō (11V — the full corpus including the Rev 16 hardened-will "
            "apocalyptic defiance), kakopoios (5V — the wrongdoer-as-defamed register in 1 Peter), "
            "and atopos (1V — Act 25:5 legal-charge). M06 cross-register flag on blasfēmeō "
            "(contempt / hostile speech)."
        ),
    },
]

# Phase 7 polysemy carry-forwards (loaded as cluster_observation INTEGRATION_NOTE rows)
OBSERVATIONS = [
    {
        "characteristic_seq": 1,
        "subgroup_code": "M10b-A",
        "observation_type": "INTEGRATION_NOTE",
        "target_phase": "phase_9_findings",
        "title": "ra.sha forensic-verdict register — VCG-level cross-register signal",
        "description": (
            "M10b-A-VCG-01 (5V — Exo 23:7, Deu 25:1, 25:2, 1Ki 8:32, 2Ch 6:23) carries ra.sha as a "
            "legal-status label in forensic/judicial contexts ('the wicked = the legally condemnable') "
            "rather than naming inner moral character. Phase 9 T6 (Structural Relationships) findings "
            "should attend to this M10 (act-of-moral-failure) cross-register relationship. The VCG "
            "is structurally separated from the inner-moral-character VCGs within M10b-A."
        ),
    },
    {
        "characteristic_seq": 2,
        "subgroup_code": "M10b-B",
        "observation_type": "INTEGRATION_NOTE",
        "target_phase": "phase_9_findings",
        "title": "ponēros cosmic-evil-agent sub-corpus — VCG-level cross-register signal",
        "description": (
            "M10b-B-VCG-01 (13V — Mat 13:19, 13:38, Joh 17:15, Eph 6:16, 2Th 3:3, 1Jn 2:13, 2:14, "
            "5:18, 5:19, Gal 1:4, Eph 5:16, 6:13, and Eph 6:12 ponēria) carries the 'evil one' / "
            "'evil age' / cosmic-evil-agent register — supra-personal evil rather than the personal "
            "constitutional-evil register of the remaining ~77 VCG-2/3/4/5/6 verses. Phase 9 T6 "
            "findings should attend to this M27 (idolatry/cosmic-evil/concrete-evil) cross-register "
            "relationship. The VCG is structurally separated within M10b-B."
        ),
    },
    {
        "characteristic_seq": 5,
        "subgroup_code": "M10b-E",
        "observation_type": "INTEGRATION_NOTE",
        "target_phase": "phase_9_findings",
        "title": "a.ven trouble-suffered sub-corpus — VCG-level cross-register signal",
        "description": (
            "M10b-E-VCG-01 (7V) carries a.ven in the trouble/distress/affliction-suffered register — "
            "the harm that befalls the victim rather than the iniquity-scheming of the agent. "
            "Phase 9 T6 findings should attend to the M03 (grief/sorrow) and M27 (calamity/ruin) "
            "cross-register relationships. The VCG is structurally separated from the iniquity-scheming "
            "and evil-deeds VCGs within M10b-E. (The brief estimated ~18V for this sub-corpus; the AI's "
            "per-verse read identified 7 cleaner trouble-register cases.)"
        ),
    },
]


def main(live: bool) -> int:
    print(f"=== M10b Phase 8.7 apply — mode={'LIVE' if live else 'DRY-RUN'} ===")

    if live:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup = REPO / "backups" / f"bible_research_backup_{ts}_M10b-phase8_7-characteristic-map.db"
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DB, backup)
        print(f"Backup: {backup.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Pre-checks
    n_existing_chars = conn.execute(
        "SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()[0]
    if n_existing_chars:
        print(f"ERROR: {n_existing_chars} characteristic rows already exist for {CLUSTER}")
        return 1

    sg_by_code = {r["subgroup_code"]: r["id"] for r in conn.execute(
        "SELECT subgroup_code, id FROM cluster_subgroup "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchall()}
    print(f"M10b sub-groups: {len(sg_by_code)}")
    missing = [c["subgroup_code"] for c in CHARACTERISTICS if c["subgroup_code"] not in sg_by_code]
    if missing:
        print(f"ERROR: missing sub-groups in DB: {missing}")
        return 1
    print("All characteristic-target sub-groups exist ✓")

    if not live:
        print(f"\nWould insert: {len(CHARACTERISTICS)} characteristic rows + "
              f"{len(CHARACTERISTICS)} characteristic_subgroup rows + "
              f"{len(OBSERVATIONS)} cluster_observation rows")
        for c in CHARACTERISTICS:
            print(f"  char_seq={c['char_seq']} → {c['subgroup_code']}: {c['short_name']}")
        print("\n[DRY-RUN — no writes]")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN")
    try:
        # Op A: characteristic
        char_id_by_seq: dict[int, int] = {}
        for c in CHARACTERISTICS:
            r = cur.execute(
                "INSERT INTO characteristic "
                "(cluster_code, char_seq, short_name, definition, source, version, "
                " delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'v1', 0, ?, ?)",
                (CLUSTER, c["char_seq"], c["short_name"], c["definition"], DIRECTIVE_ID, NOW, NOW),
            )
            char_id_by_seq[c["char_seq"]] = r.lastrowid
        print(f"Op A: inserted {len(CHARACTERISTICS)} characteristic rows")

        # Op B: characteristic_subgroup
        for c in CHARACTERISTICS:
            cur.execute(
                "INSERT INTO characteristic_subgroup "
                "(characteristic_id, cluster_subgroup_id, qualifier_note, is_partial, "
                " delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, 0, ?, ?)",
                (char_id_by_seq[c["char_seq"]], sg_by_code[c["subgroup_code"]],
                 c["qualifier_note"], NOW, NOW),
            )
        print(f"Op B: inserted {len(CHARACTERISTICS)} characteristic_subgroup rows (all 1:1, is_partial=0)")

        # Op C: cluster_observation carry-forwards
        for o in OBSERVATIONS:
            cur.execute(
                "INSERT INTO cluster_observation "
                "(cluster_code, characteristic_id, cluster_subgroup_id, source_phase, "
                " observation_type, target_phase, title, description, status, "
                " raised_date, source_file, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 'phase_7_vcg_design', ?, ?, ?, ?, 'open', ?, ?, 0, ?, ?)",
                (CLUSTER, char_id_by_seq[o["characteristic_seq"]],
                 sg_by_code[o["subgroup_code"]], o["observation_type"], o["target_phase"],
                 o["title"], o["description"], NOW, SOURCE_FILE, NOW, NOW),
            )
        print(f"Op C: inserted {len(OBSERVATIONS)} cluster_observation rows (INTEGRATION_NOTE → phase_9_findings)")

        # Post-checks
        n_chars = conn.execute(
            "SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
            (CLUSTER,)
        ).fetchone()[0]
        assert n_chars == len(CHARACTERISTICS), f"Post-check fail: {n_chars} characteristic rows"

        n_links = conn.execute("""
            SELECT COUNT(*) FROM characteristic_subgroup csg
            JOIN characteristic ch ON ch.id = csg.characteristic_id
            WHERE ch.cluster_code = ? AND COALESCE(csg.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        assert n_links == len(CHARACTERISTICS), f"Post-check fail: {n_links} link rows"

        # Every active sub-group has ≥1 characteristic link
        unmapped = conn.execute("""
            SELECT cs.subgroup_code FROM cluster_subgroup cs
            WHERE cs.cluster_code=? AND COALESCE(cs.delete_flagged,0)=0
              AND cs.id NOT IN (
                SELECT csg.cluster_subgroup_id FROM characteristic_subgroup csg
                JOIN characteristic ch ON ch.id = csg.characteristic_id
                WHERE ch.cluster_code=? AND COALESCE(csg.delete_flagged,0)=0
              )
        """, (CLUSTER, CLUSTER)).fetchall()
        if unmapped:
            raise RuntimeError(f"Unmapped sub-groups: {[r['subgroup_code'] for r in unmapped]}")
        print(f"Post-check: all 6 sub-groups have a characteristic mapping ✓")

        conn.commit()
        print(f"\nCOMMITTED at {NOW}")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
