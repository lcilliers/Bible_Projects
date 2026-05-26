"""M10c Phase 8.7 — Characteristic mapping load.

Per v2_9 §11B. Per directive wa-cluster-M10c-dir-003-phase8_7-characteristic-map-v1-20260526.md.

M10c Phase 5 produced 5 sub-groups carrying 4 characteristics:

  char_seq=1  Ritual defilement-state  →  M10c-A + M10c-B  (volume-split per §8.6)
  char_seq=2  Moral-inner defilement-state  →  M10c-C
  char_seq=3  Corporate/covenantal defilement  →  M10c-D
  char_seq=4  Defilement by external spiritual agency  →  M10c-E

M10c-A vs M10c-B is the only M:N case: both fully serve characteristic 1
(both are full-fledged ritual-defilement registers — mechanical contact vs
authoritative verdict), split by §8.6 distribution gate (combined 133V/263V
= 50.6% > 40% threshold). is_partial=0 for both because each sub-group
covers a *complete* register of the same characteristic; the split is
mechanism-vs-verdict, not VCG-level register partitioning.

Carry-forward observations capture:
- SPLIT_DESIGN_RATIONALE for char_seq=1 (the §8.6-triggered A/B split)
- INTEGRATION_NOTE for M10c-E (unclean-spirit register cross-cluster signal to M27)
- INTEGRATION_NOTE for M10c-D (idolatry sub-register cross-cluster signal to M10b)

Operations (single transaction):
- Op A: INSERT 4 characteristic rows
- Op B: INSERT 5 characteristic_subgroup rows (1:1 for chars 2/3/4; 1:2 for char 1)
- Op C: INSERT carry-forward cluster_observation rows
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
CLUSTER = "M10c"
DIRECTIVE_ID = "wa-cluster-M10c-dir-003-phase8_7-characteristic-map-v1-20260526"
SOURCE_FILE = "Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-design-v1_0-20260526.md"

CHARACTERISTICS = [
    {
        "char_seq": 1,
        "short_name": "Ritual defilement-state",
        "definition": (
            "The inner-being condition of ritual uncleanness — the state of being unclean as it bears on "
            "sacred participation, communal life, and the conscience. The condition is acquired through "
            "two mechanisms held distinct in the corpus but constituting one inner state: bodily "
            "interaction with a defiling agent (contact, carrying, proximity, fluid transmission), and "
            "authoritative verdict or inherent categorical designation (priestly diagnosis, animals or "
            "objects declared unclean by nature). The inner content includes awareness of contamination "
            "incurred, duty of watchful restraint over bodily action and over discernment, distress at "
            "worship exclusion, conscience formed by purity categories, the social-relational duty not "
            "to transmit one's state to others. Structural opposite: M12 (purity)."
        ),
        "subgroups": [
            ("M10c-A", (
                "M10c-A carries the bodily-contact mechanism — defilement acquired through physical "
                "contact with corpse, discharge, carcass, swarming creature, or unclean fluid. Time-bound; "
                "transmitted by touch, carrying, proximity. Volume: 93V (50V H2930A ta.me verb + 28V "
                "H2931 ta.me adj + 15V H5079 nid.dah). The M10c-A vs M10c-B split is §8.6-volume-driven "
                "(combined ritual register would be 133V/263V = 50.6% > 40% cap)."
            )),
            ("M10c-B", (
                "M10c-B carries the categorical/classificatory mechanism — defilement determined by "
                "authoritative examination/verdict (priestly diagnosis of skin disease) or by inherent "
                "categorical designation (animals declared unclean by nature, materials permanently "
                "defiled). The discernment register: 'distinguish clean from unclean' (Lev 10:10), "
                "'unclean! unclean!' (Lev 13:45), publicly-marked stigma (Lam 4:15). Volume: 40V "
                "(21V H2931 ta.me adj + 15V H2930A ta.me verb + 4V G0169 akathartos). NT akathartos "
                "categorical use (Act 10:14, 1Cor 7:14, 2Cor 6:17) sits here as the discernment "
                "register extended to the new-covenant question of food/persons."
            )),
        ],
    },
    {
        "char_seq": 2,
        "short_name": "Moral-inner defilement-state",
        "definition": (
            "Defilement as the inner condition of moral corruption — conscience, will, and heart corrupted "
            "by desire, habitual sin, and idolatrous attachment. The locus of defilement is the inner "
            "person itself, not external contact. Primary NT register (all five Greek terms) and Hebrew "
            "metaphorical extension (Isa 6:5, Isa 64:6, Hag 2:14 inner-aspect, Job 14:4, Pro 30:12). "
            "Inner content includes: conscience defiled (1Cor 8:7), prior moral-life slavery as the "
            "dominion-of-flesh inner condition (Rom 6:19, Rom 1:24, Eph 4:19), body-and-spirit "
            "purification call (2Cor 7:1), idolater = heart impurity (Eph 5:5), inner moral corruption "
            "causing outer abomination (Tit 1:15-16, 2Pe 2:10-20), constitutional moral uncleanness "
            "(Job 14:4). Structural opposite: M12 (purity/holiness of the inner person)."
        ),
        "subgroups": [
            ("M10c-C", (
                "M10c-C carries the moral-inner register in full. 26V across 6 terms: G0167 akatharsia "
                "(10V), H2931 ta.me adj (6V — Hebrew metaphorical extension to inner condition), G0169 "
                "akathartos (5V — moral-inner uses), G3435 molunō (3V), G3436 molusmos (1V), G3394 "
                "miasmos (1V). Strong cross-register flags inherited from Phase 3: M10 (sin-act produces "
                "defilement-state), M11 (cleansing as response), M29 (desire as vehicle), M08 (pride as "
                "companion), M09 (consecration as opposite). The miasmos verse (2Pe 2:10) and molusmos "
                "verse (2Cor 7:1) co-anchor M10c-C-VCG-03 (body-and-spirit purification register)."
            )),
        ],
    },
    {
        "char_seq": 3,
        "short_name": "Corporate/covenantal defilement",
        "definition": (
            "Defilement extending from persons or community to land, sanctuary, and the divine name "
            "through moral defection. Includes both covenantal-relational defilement (sexual betrayal, "
            "ordeal law, Nazirite violation) and the prophetic corporate register (idolatry defiling "
            "sanctuary and land, persistent unfaithfulness contaminating sacred space). The inner-being "
            "dimension is the corporate will in defection from God, hearts unfaithful in covenant, the "
            "community's inner corruption rendering offerings worthless (Hag 2:14), and the memory of "
            "defilement functioning as the inner mechanism of corporate repentance (Eze 20:43). "
            "Structural opposite: M12 (purity/holiness of sacred space, divine name, covenant relationship)."
        ),
        "subgroups": [
            ("M10c-D", (
                "M10c-D carries the corporate/covenantal register in full. 83V across 3 terms: H2930A "
                "ta.me verb (63V — Eze-heavy + Num/Jer/Hos), H2931 ta.me adj (11V), H5079 nid.dah "
                "(9V — corporate-prophetic uses). Cross-register flags inherited from Phase 3: M10 "
                "(sin act underpinning corporate defilement), M10b (idolatry contexts — heavy "
                "Ezekiel idolatry corpus produces an INTEGRATION_NOTE for Phase 9), M07 (shame-stigma "
                "in Lam 1:17). The covenant-relational and sanctuary/land/name registers are held "
                "together by their shared structural feature: defilement of a sacred relational order."
            )),
        ],
    },
    {
        "char_seq": 4,
        "short_name": "Defilement by external spiritual agency",
        "definition": (
            "The inner-being condition of defilement produced by an unclean spirit inhabiting, controlling, "
            "and corrupting a person from without. The mechanism is external — an unclean spiritual force "
            "enters and dominates the person's inner and bodily life. The result is a defilement-state in "
            "the person: will overridden, faculties suppressed (speech/hearing, Mar 9:25), bodily agency "
            "lost (Luk 8:29), communal access severed. The spirits recognise superior divine authority "
            "(Mar 3:11) and resist expulsion (Act 8:7); restoration is treated as wholeness (Luk 6:18). "
            "Structurally distinct from the bodily-mechanism (chars 1) and moral self-defilement (char 2) "
            "in that the defiling agent is an external spiritual being. Structural opposite: M12 "
            "(purity/wholeness — the restored state after expulsion)."
        ),
        "subgroups": [
            ("M10c-E", (
                "M10c-E carries the external-spiritual-agency register in full. 21V exclusively G0169 "
                "akathartos (the unclean-spirit register of the NT). Recognition-and-expulsion narratives "
                "dominate; authority-over-unclean-spirits commissioning verses constitute a second VCG; "
                "general-affliction/Revelation cosmic register is the third. M27 cross-register flag is "
                "strong (unclean spirits as cosmic-evil agents) — captured by an INTEGRATION_NOTE "
                "carry-forward for Phase 9."
            )),
        ],
    },
]

OBSERVATIONS = [
    {
        "characteristic_seq": 1,
        "subgroup_code": None,
        "observation_type": "SPLIT_DESIGN_RATIONALE",
        "target_phase": "phase_9_findings",
        "title": "Ritual-defilement characteristic volume-split per §8.6 (M10c-A vs M10c-B)",
        "description": (
            "Characteristic 1 (Ritual defilement-state) is carried by two sub-groups — M10c-A "
            "(bodily-contact mechanism, 93V) and M10c-B (categorical/classificatory mechanism, 40V) "
            "— because the combined ritual register (133V) would breach the §8.6 distribution gate "
            "(40% of 263V = 105V cap; 133V = 50.6%). The split-axis is mechanism-vs-verdict, not "
            "characteristic-divergence: both sub-groups express the same inner-being condition (the "
            "state of ritual uncleanness as it bears on sacred participation and conscience), differing "
            "in how the state is acquired. Phase 9 findings on characteristic 1 should treat A and B "
            "as complementary registers of one inner-being faculty rather than two separate "
            "characteristics; T1.1 'characteristic in its inner-being aspect' answers should integrate "
            "both registers; T1.2.1 sub-group structural descriptions distinguish them."
        ),
    },
    {
        "characteristic_seq": 4,
        "subgroup_code": "M10c-E",
        "observation_type": "INTEGRATION_NOTE",
        "target_phase": "phase_9_findings",
        "title": "Unclean-spirit register cross-cluster signal to M27 (cosmic-evil agents)",
        "description": (
            "M10c-E (Defilement by external spiritual agency, 21V — all akathartos NT) carries an M27 "
            "cross-register flag inherited from Phase 3. The unclean spirits are cosmic-evil agents "
            "recognised in NT exorcism narratives; they participate analytically in M27 (Evil) as well "
            "as M10c (Defilement). Phase 9 T6 (Structural Relationships) findings on characteristic 4 "
            "should attend to this register: defilement here is the *result* an external evil agent "
            "produces; in M27 the same verses analyse the *agent's* nature. The two analytical lenses "
            "are complementary, not duplicative."
        ),
    },
    {
        "characteristic_seq": 3,
        "subgroup_code": "M10c-D",
        "observation_type": "INTEGRATION_NOTE",
        "target_phase": "phase_9_findings",
        "title": "Ezekiel idolatry sub-corpus within M10c-D — cross-cluster signal to M10b",
        "description": (
            "M10c-D-VCG-03 (16V — Eze 14:11, 20:7/18/30/31/43, 22:3-4, 23:30, 36:18, 37:23, 43:8 etc.) "
            "and the broader Ezekiel idolatry-defilement corpus within M10c-D carry an M10b "
            "(Wickedness/Evil/Abomination) cross-register flag — these verses analyse the same prophetic "
            "events under two complementary characteristics: idolatry as abomination (M10b register) "
            "and idolatry as defilement of sanctuary/land/name (M10c register). Phase 9 T6 findings on "
            "characteristic 3 should attend to the M10b cross-register relationship; the verses are "
            "primary M10c but their full analytical force is multi-cluster."
        ),
    },
    {
        "characteristic_seq": 2,
        "subgroup_code": "M10c-C",
        "observation_type": "INTEGRATION_NOTE",
        "target_phase": "phase_9_findings",
        "title": "Moral-inner register cross-cluster signals (M10, M11, M29, M08, M09)",
        "description": (
            "M10c-C (Moral-inner defilement-state, 26V) carries the heaviest cluster of cross-register "
            "flags inherited from Phase 3 — M10 (sin-act producing defilement-state, e.g. Rom 1:24, "
            "Rom 6:19, Gal 5:19), M11 (cleansing/repentance as response, e.g. 2Cor 7:1, 1Th 4:7), M29 "
            "(desire as vehicle, miasmos 2Pe 2:10), M08 (pride as companion, miasmos), M09 (consecration "
            "as opposite, molunō Rev 14:4). Phase 9 T6 findings on characteristic 2 should map these "
            "relational pairs explicitly: defilement-state and the sin-act / cleansing-response / "
            "desire-vehicle / consecration-opposite are co-evidenced at the verse level. The "
            "characteristic's analytical centre of gravity is the relational network between defilement "
            "and these neighbouring inner-being faculties."
        ),
    },
]


def main(live: bool) -> int:
    print(f"=== M10c Phase 8.7 apply - mode={'LIVE' if live else 'DRY-RUN'} ===")

    if live:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup = REPO / "backups" / f"bible_research_backup_{ts}_M10c-phase8_7-characteristic-map.db"
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DB, backup)
        print(f"Backup: {backup.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

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
    print(f"M10c sub-groups: {len(sg_by_code)} -> {sorted(sg_by_code.keys())}")
    expected_sgs = {sg for c in CHARACTERISTICS for sg, _ in c["subgroups"]}
    missing = expected_sgs - set(sg_by_code)
    if missing:
        print(f"ERROR: missing sub-groups in DB: {missing}")
        return 1
    print("All characteristic-target sub-groups exist")

    total_links = sum(len(c["subgroups"]) for c in CHARACTERISTICS)
    if not live:
        print(f"\nWould insert: {len(CHARACTERISTICS)} characteristic rows + "
              f"{total_links} characteristic_subgroup rows + "
              f"{len(OBSERVATIONS)} cluster_observation rows")
        for c in CHARACTERISTICS:
            sgs = ", ".join(sg for sg, _ in c["subgroups"])
            print(f"  char_seq={c['char_seq']} -> [{sgs}]: {c['short_name']}")
        print("\n[DRY-RUN - no writes]")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN")
    try:
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

        n_links = 0
        for c in CHARACTERISTICS:
            for sg_code, qnote in c["subgroups"]:
                cur.execute(
                    "INSERT INTO characteristic_subgroup "
                    "(characteristic_id, cluster_subgroup_id, qualifier_note, is_partial, "
                    " delete_flagged, created_at, last_updated_date) "
                    "VALUES (?, ?, ?, 0, 0, ?, ?)",
                    (char_id_by_seq[c["char_seq"]], sg_by_code[sg_code], qnote, NOW, NOW),
                )
                n_links += 1
        print(f"Op B: inserted {n_links} characteristic_subgroup rows "
              f"(1:1 for chars 2/3/4, 1:2 for char 1; all is_partial=0)")

        for o in OBSERVATIONS:
            sg_id = sg_by_code[o["subgroup_code"]] if o.get("subgroup_code") else None
            cur.execute(
                "INSERT INTO cluster_observation "
                "(cluster_code, characteristic_id, cluster_subgroup_id, source_phase, "
                " observation_type, target_phase, title, description, status, "
                " raised_date, source_file, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 'phase_8_7_characteristic_map', ?, ?, ?, ?, 'open', ?, ?, 0, ?, ?)",
                (CLUSTER, char_id_by_seq[o["characteristic_seq"]],
                 sg_id, o["observation_type"], o["target_phase"],
                 o["title"], o["description"], NOW, SOURCE_FILE, NOW, NOW),
            )
        print(f"Op C: inserted {len(OBSERVATIONS)} cluster_observation rows "
              f"(1x SPLIT_DESIGN_RATIONALE + 3x INTEGRATION_NOTE)")

        n_chars = conn.execute(
            "SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
            (CLUSTER,)
        ).fetchone()[0]
        assert n_chars == len(CHARACTERISTICS), f"Post-check fail: {n_chars} characteristic rows"

        n_links_db = conn.execute("""
            SELECT COUNT(*) FROM characteristic_subgroup csg
            JOIN characteristic ch ON ch.id = csg.characteristic_id
            WHERE ch.cluster_code=? AND COALESCE(csg.delete_flagged,0)=0
        """, (CLUSTER,)).fetchone()[0]
        assert n_links_db == n_links, f"Post-check fail: {n_links_db} link rows"

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
        print(f"Post-check: all 5 sub-groups have a characteristic mapping")

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
