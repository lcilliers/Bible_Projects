"""_apply_m26_dir003_v1_20260510.py — DB-modifying.

Apply DIR-M26-20260510-003 (M26-A2 VSG restructure) under the
post-M47 m:n vcg ↔ term schema.

Source directive:
  Sessions/Session_Clusters/M26/wa-cluster-M26-dir-003-A2-vsg-restructure-v1-20260510.md

Operations (single transaction, foreign_keys=ON):

  Phase 2 (8 vcgs):
    - UPDATE context_description for each renamed vcg
    - Clear is_anchor=1 on this vcg's M26-A2 vc rows
    - Set is_anchor=1 on the new anchor vr_id's M26-A2 vc row

  Phase 3 (17 NEW vcgs, cluster-prefixed codes M26-A2-001..017):
    - INSERT verse_context_group with new code + description
    - INSERT vcg_term row(s) for each linked term (1..4 per NEW)
    - UPDATE vc.group_id for the listed vr_ids (to point at new vcg)
      — only acts on the M26-A2 vc row of each listed vr_id
    - Set is_anchor=1 on the named anchor vr_id

  Phase 4a (54 verses): UPDATE vc.cluster_subgroup_id = M26-BOUNDARY
    for the listed vr_ids' M26-A2 vc rows.

  Phase 4b (1 verse): UPDATE vc.cluster_subgroup_id = M26-A1 for
    vr_id 96020's M26-A2 vc row.

  Phase 4c: vr_id 169420 reassigned to NEW-01 (handled by adding it
    to NEW-01's source list).

Phase 1 (conceptual — no separate ops): the 5 vcgs flagged in the
directive (3193-002, 942-002, 942-004, 911-003, 950-003) end up with
no M26-A2 verses as a consequence of Phase 2/3/4 moves. Verified
post-execution.

NO API calls. ~3 sec wall time. No cost.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

# ══════════════════════════════════════════════════════════════════════
#  Phase 2 — Rename 8 existing vcgs (description + anchor reset)
# ══════════════════════════════════════════════════════════════════════
PHASE2_VCGS = [
    {
        "code": "911-001", "anchor_vr": 25210,
        "description": (
            "Term names righteousness as a personal inner possession — "
            "held fast, carried in the heart, expressed in the whole "
            "manner of life. The person's righteousness is their own, "
            "concerns themselves (Job 35:8), and does not reproach them "
            "(Job 27:6). It is evidenced in walking before God in "
            "faithfulness and uprightness of heart (1Ki 3:6), in walking "
            "and speaking rightly and despising bribes (Isa 33:15), and "
            "in doing righteousness consistently at all times (Psa "
            "106:3). Inner and outer correspondence is the defining "
            "quality."
        ),
    },
    {
        "code": "911-002", "anchor_vr": 169247,
        "description": (
            "Term names righteousness as a personal moral standing that "
            "God sees and rewards — the inner condition of the person "
            "that God assesses, vindicates, and repays according to "
            "faithfulness."
        ),
    },
    {
        "code": "942-001", "anchor_vr": 96028,
        "description": (
            "Term names the person's righteousness as a personal moral "
            "standing before God — the inner condition appealed to in "
            "prayer, claimed before divine judgment, and rewarded by "
            "God when genuine. The person stands in righteousness "
            "before God as an established inner reality they can "
            "invoke and be assessed by."
        ),
    },
    {
        "code": "942-003", "anchor_vr": 28324,
        "description": (
            "Term names righteousness as an inner orientation actively "
            "pursued — seeking the Lord and righteousness together "
            "(Isa 51:1), commanded alongside humility and doing God's "
            "commands (Zep 2:3). Active seeking is the defining posture."
        ),
    },
    {
        "code": "950-001", "anchor_vr": 28760,
        "description": (
            "Term names righteousness received through faith — credited "
            "and counted by God to the person who trusts. The Abraham "
            "pattern: belief counted as righteousness, received not "
            "earned, grounded in trust not works. The standing is "
            "conferred through faith and sealed by it."
        ),
    },
    {
        "code": "950-002", "anchor_vr": 93734,
        "description": (
            "Term names righteousness as a practiced, lived orientation "
            "— ongoing conduct before God expressed in active service, "
            "progressive sanctification, and formable through scripture "
            "and discipline. Not a one-time standing but a daily "
            "life-direction."
        ),
    },
    {
        "code": "3246-002", "anchor_vr": 169484,
        "description": (
            "Term names the righteous person as the direct object of "
            "God's relational attention — seen, tested, known, loved, "
            "upheld, delivered, and heard. God's engagement with the "
            "righteous person is personal and active: he does not "
            "withdraw his eyes (Job 36:7), his ears are open to their "
            "cry (Psa 34:15), and he will never permit them to be "
            "moved (Psa 55:22). The righteous person's standing is "
            "real and God responds to it specifically."
        ),
    },
    {
        "code": "3246-003", "anchor_vr": 169482,
        "description": (
            "Term names the characteristic inner response of the "
            "righteous person toward God — gladness, exultation, "
            "praise, thanksgiving, and joy when justice is enacted. "
            "These are not incidental emotions but the natural "
            "orientation of the righteous inner being toward God. "
            "Joy is fitting for the righteous (Psa 33:1); it arises "
            "from the person's own relationship with God and from "
            "witnessing divine justice."
        ),
    },
]

# ══════════════════════════════════════════════════════════════════════
#  Phase 3 — Create 17 NEW vcgs (code = M26-A2-NNN, multi-term via vcg_term)
# ══════════════════════════════════════════════════════════════════════
# Each NEW: code, terms (Strong's list), description, anchor_vr,
# source_vr_ids (the vr_ids whose M26-A2 vc rows get reassigned here).
PHASE3_NEW_VCGS = [
    {
        "code": "M26-A2-001", "terms": ["H6666", "H6662"],
        "anchor_vr": 169282,
        "description": (
            "Term names righteousness as a governing quality whose "
            "presence produces measurable life outcomes — deliverance "
            "from death, stability of the way, sure reward, honour, and "
            "enduring legacy. Righteousness is not described here as "
            "an inner disposition to be cultivated but as a quality "
            "already operative whose consequences are stated. "
            "Contrasted consistently with wickedness whose outcomes are "
            "death and captivity."
        ),
        "source_vr_ids": [
            # from former 911-001
            169278, 169281, 169282, 169283, 169279, 169280, 169287,
            169290, 169289, 169291, 169301, 169302,
            # from former 3246-001
            169409, 169413, 169414, 169403, 169408, 169421, 169422,
            169415, 169416, 169417, 169419, 169430, 169431, 169432,
            169433, 169436, 169440, 169442, 169450, 169453, 169459,
            169491, 169492, 169406, 169435, 169458, 169507, 169379,
            169506, 169447, 169393, 169488, 169426,
            # Phase 4c addendum: 169420 (Pro 11:31, 3246-002)
            169420,
        ],
    },
    {
        "code": "M26-A2-002", "terms": ["H6666", "H6662", "H6664G"],
        "anchor_vr": 169271,
        "description": (
            "Term names righteousness as a dynamic personal standing "
            "that must be maintained and can be forfeited. The "
            "righteous person who turns from righteousness and does "
            "injustice loses the standing and dies; none of their prior "
            "righteous deeds are remembered (Eze 33:13). The wicked "
            "person who turns and does what is just and right receives "
            "life. Righteousness here is non-transferable and "
            "non-accumulative — assessed at the point of turning, not "
            "across a lifetime. This is the OT's most developed "
            "treatment of the inner mechanics of righteousness."
        ),
        "source_vr_ids": [
            # from former 911-001
            169269, 169268, 169261, 169263, 169265, 169266, 169267,
            169270, 169271, 169272, 169273, 169274, 169275,
            # from former 911-002
            169259, 169260, 169262, 169264,
            # from former 3246-001
            169357, 169349, 169350, 169351, 169359, 169360, 169361,
            169352, 169456,
            # from former 942-001
            95981,
        ],
    },
    {
        "code": "M26-A2-003", "terms": ["H6666", "G1343", "H6664G", "H6662"],
        "anchor_vr": 25201,
        "description": (
            "Term names the failure, distortion, or counterfeit form of "
            "righteousness — righteous deeds that are polluted and "
            "cannot stand before God; swearing by God's name but not in "
            "righteousness; seeking God in outward form while absent "
            "inwardly; righteousness that does not profit; "
            "self-assessed righteousness producing contempt; "
            "law-righteousness that is rubbish compared to God's; "
            "outward appearance concealing inner lawlessness. Together "
            "these verses define what genuine righteousness is by "
            "showing what it is not."
        ),
        "source_vr_ids": [
            # from former 911-001 — Isaiah absence cluster
            25201, 25181, 25182, 25192, 25185,
            # from former 911-002
            25191,
            # from former 950-001 — law-righteousness impossible
            28734, 28735,
            # from former 950-002 — NT counterfeit cluster
            93740, 93735, 93743, 93745,
            # from former 942-001
            28327,
            # from former 3246-001
            169394,
        ],
    },
    {
        "code": "M26-A2-004", "terms": ["H6666"],
        "anchor_vr": 25179,
        "description": (
            "Term names the condition of being far from or lacking "
            "righteousness — the human person or community described "
            "as distant from the righteous state, hoping for it but "
            "not possessing it. Stubbornness of heart is named as the "
            "inner cause of the distance (Isa 46:12); the absence is "
            "experienced as darkness and the failure of justice "
            "(Isa 59:9). An OT parallel to the NT declaration of "
            "universal absence (Rom 3:10), but expressed as a "
            "particular condition rather than a universal category."
        ),
        "source_vr_ids": [25179, 25196],
    },
    {
        "code": "M26-A2-005", "terms": ["H6664G"],
        "anchor_vr": 28326,
        "description": (
            "Term names righteousness as already known and carried in "
            "the heart as law. The person addressed is defined by this "
            "knowing: righteousness is not something they are seeking "
            "but something they already are and have. The internalised "
            "state produces courage in the face of reproach. Distinct "
            "from righteousness as active pursuit (942-003) and from "
            "righteousness as outward expression (942-001)."
        ),
        "source_vr_ids": [28326],
    },
    {
        "code": "M26-A2-006", "terms": ["G1343", "G1342"],
        "anchor_vr": 93739,
        "description": (
            "Term names righteousness as the object of active inner "
            "longing and deliberate pursuit — hungered for, thirsted "
            "for, fled toward. The righteous person is defined by the "
            "direction of inner desire. The degree of righteousness "
            "matters (exceeding the scribes and Pharisees). Pursuit is "
            "commanded, implying the state is not yet fully arrived at "
            "but is the defining goal of the inner person."
        ),
        "source_vr_ids": [
            93739, 93738, 93722, 93723,  # from 950-002
            93812,  # Rom 1:17, G1342 dikaios — from 3193-002
        ],
    },
    {
        "code": "M26-A2-007", "terms": ["G1343"],
        "anchor_vr": 93742,
        "description": (
            "Term names righteousness as a fruit — something that "
            "grows, is harvested, and can increase. The righteous "
            "person is characterised by what their righteousness "
            "produces outwardly. The fruit comes through Jesus Christ "
            "and can be multiplied by God."
        ),
        "source_vr_ids": [28730, 28729, 93742],
    },
    {
        "code": "M26-A2-008", "terms": ["G1343"],
        "anchor_vr": 28731,
        "description": (
            "Term names righteousness as a defining quality of the new "
            "self in Christ — the new creation is constituted in true "
            "righteousness and holiness (Eph 4:24), and righteousness "
            "is worn as a breastplate (Eph 6:14). These verses describe "
            "righteousness not as something to be pursued but as "
            "something already constitutive of the new identity in "
            "Christ."
        ),
        "source_vr_ids": [28731, 28733],
    },
    {
        "code": "M26-A2-009", "terms": ["H6664G"],
        "anchor_vr": 28338,
        "description": (
            "Term names righteousness as something worn — it clothes "
            "and covers the whole person, like a robe and turban. The "
            "imagery conveys total coverage: righteousness is not one "
            "quality among others but the defining garment of the "
            "person's whole presence. The inner state finds its most "
            "complete expression as an enveloping identity."
        ),
        "source_vr_ids": [28338],
    },
    {
        "code": "M26-A2-010", "terms": ["H6662"],
        "anchor_vr": 169441,
        "description": (
            "Term names the righteous person as the target of "
            "systemic and personal injustice — their cause subverted "
            "by bribes, their right denied by corrupt judges, their "
            "standing falsely condemned. The righteousness is real and "
            "legitimate; the violation is the perversion of what "
            "should vindicate them. God names such perversion as an "
            "abomination (Pro 17:15)."
        ),
        "source_vr_ids": [
            169346, 169341, 169342, 169441, 169445, 169455, 169383,
            169378, 169371, 169444,
        ],
    },
    {
        "code": "M26-A2-011", "terms": ["H6662"],
        "anchor_vr": 169402,
        "description": (
            "Term names righteousness as a governing inner orientation "
            "expressed through speech — the mouth, tongue, and lips of "
            "the righteous produce life, wisdom, and what is fitting "
            "and true. Speech is deliberate rather than reactive; the "
            "heart ponders before answering (Pro 15:28). Falsehood is "
            "hated as an inner aversion (Pro 13:5)."
        ),
        "source_vr_ids": [
            169402, 169404, 169405, 169411, 169412, 169438, 169493,
            169434,
        ],
    },
    {
        "code": "M26-A2-012", "terms": ["H6662"],
        "anchor_vr": 169451,
        "description": (
            "Term names righteousness as an inner orientation that "
            "extends outward toward others — guiding the neighbour, "
            "giving without withholding, caring for animals, returning "
            "good for evil. The righteous person's inner state reaches "
            "toward the needs of others beyond social obligation."
        ),
        "source_vr_ids": [169423, 169427, 169451, 169490, 169332, 169467],
    },
    {
        "code": "M26-A2-013", "terms": ["H6662"],
        "anchor_vr": 169428,
        "description": (
            "Term names righteousness as a state whose inner "
            "foundation produces lasting stability — rootedness that "
            "is never moved, establishment that survives catastrophe, "
            "resilience that rises after falling. The righteous person "
            "is not protected from difficulty (falls seven times, Pro "
            "24:16) but is not finally overthrown by it."
        ),
        "source_vr_ids": [
            169428, 169424, 169407, 169410, 169468, 169454, 169391,
            169457, 169418, 169508, 169437,
        ],
    },
    {
        "code": "M26-A2-014", "terms": ["H6662"],
        "anchor_vr": 169369,
        "description": (
            "Term names righteousness as a state defined by its "
            "orientation toward God — walking with God (Gen 6:9), "
            "living by faith (Hab 2:4), serving God as the defining "
            "mark of the righteous (Mal 3:18), entering through the "
            "gate of the Lord (Psa 118:20), and faithfully keeping "
            "God's statutes (Eze 18:9). The righteous person's state "
            "cannot be separated from this relational grounding."
        ),
        "source_vr_ids": [169369, 169373, 169399, 169471, 169353, 169390],
    },
    {
        "code": "M26-A2-015", "terms": ["H6662"],
        "anchor_vr": 169462,
        "description": (
            "Term names a recognisable community of righteous persons "
            "— a congregation (Psa 1:5), a generation (Psa 14:5), a "
            "register (Psa 69:28), and a trusted circle whose rebuke "
            "is welcomed (Psa 141:5). The righteous person belongs to "
            "an identifiable group distinct from the wicked, in whose "
            "company God dwells."
        ),
        "source_vr_ids": [169462, 169475, 169503, 169477],
    },
    {
        "code": "M26-A2-016", "terms": ["H6662"],
        "anchor_vr": 169487,
        "description": (
            "Term names the righteous person as a specific target of "
            "hostility — plotted against, watched for death, spoken "
            "against with contempt, sold for silver, afflicted, "
            "deprived of justice, and killed. The opposition is "
            "directed precisely because the person is righteous. The "
            "righteous person's mere existence constitutes a contrast "
            "the wicked cannot ignore."
        ),
        "source_vr_ids": [
            169487, 169494, 169486, 169481, 169372, 169338, 169339,
            169398, 169509, 169473, 169345, 169337, 169330, 169348,
            169385, 169464,
        ],
    },
    {
        "code": "M26-A2-017", "terms": ["H6662"],
        "anchor_vr": 169460,
        "description": (
            "Term names a recognisable life trajectory belonging to "
            "the righteous — a path and way that is level (Isa 26:7), "
            "grows progressively brighter (Pro 4:18), and can be kept "
            "and followed (Pro 2:20). The righteous person's life has "
            "a direction and shape that others can observe and walk in."
        ),
        "source_vr_ids": [169446, 169460, 169377, 169425],
    },
]

# ══════════════════════════════════════════════════════════════════════
#  Phase 4a — 54 vc rows from M26-A2 to M26-BOUNDARY
# ══════════════════════════════════════════════════════════════════════
PHASE4A_TO_BOUNDARY = [
    # from 942-002
    96015, 28328,
    # from 942-004
    95990, 28313, 28316,
    # from 942-003
    96005,
    # from 911-001 — governance/national
    25166, 169249, 169239, 169238, 169245, 25204, 25203, 169292,
    169276, 169286, 25207,
    # from 911-002 — national/institutional
    169255, 169256, 169257, 169258, 169253, 169241, 169244, 25211,
    169298, 169246,
    # from 950-001
    28743,
    # from 950-003
    28772, 28748,
    # from 942-001
    96006, 95985, 28331, 28332, 95980,
    # from 3246-002 — corporate/judicial/rhetorical
    169363, 169364, 169365, 169366, 169367, 169368, 169331, 169334,
    169335, 169356, 169380, 169382,
    # from 3246-003
    169452,
    # from 3246-001 — governance/national
    169336, 169376, 169386, 169354, 169355,
]

# ══════════════════════════════════════════════════════════════════════
#  Phase 4b — 1 vc row from M26-A2 to M26-A1
# ══════════════════════════════════════════════════════════════════════
PHASE4B_TO_A1 = [
    96020,  # Psa 45:7, H6664G — messianic king
]

# Phase 1 verification: 5 vcgs that should have NO M26-A2 verses post-apply
PHASE1_DROPPED_VCGS = [
    "3193-002", "942-002", "942-004", "911-003", "950-003",
]

# Phase 2 cross-vcg moves — verses transferred from one existing vcg to
# another existing vcg (the directive's "Add to group from 950-003"
# instructions). These reassign vc.group_id; cluster_subgroup_id stays.
PHASE2_CROSS_VCG_MOVES = [
    # 950-003 verses absorbed into 950-001 (Abraham faith pattern)
    {"from": "950-003", "to": "950-001", "vr_ids": [28771, 28737]},
    # 950-003 verse absorbed into 950-002 (practiced lived orientation)
    {"from": "950-003", "to": "950-002", "vr_ids": [28745]},
]

# 950-003 is dissolved — soft-delete the vcg row after all verses are
# reassigned. Other Phase 1 vcgs (3193-002, 942-002, 942-004, 911-003)
# retain their non-M26-A2 verses and stay active.
PHASE1_VCGS_TO_SOFT_DELETE = ["950-003"]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    path = os.path.join(BACKUP_DIR,
                        f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, path)
    return path


def get_subgroup_ids(conn) -> dict:
    return {r[0]: r[1] for r in conn.execute(
        "SELECT subgroup_code, id FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0"
    )}


def get_vcg_ids_by_code(conn, codes: list[str]) -> dict:
    if not codes:
        return {}
    ph = ",".join("?" * len(codes))
    return {r[0]: r[1] for r in conn.execute(
        f"SELECT group_code, id FROM verse_context_group "
        f" WHERE group_code IN ({ph}) "
        f"   AND COALESCE(delete_flagged,0)=0",
        codes,
    )}


def get_term_ids_by_strong(conn, strongs: list[str]) -> dict:
    if not strongs:
        return {}
    ph = ",".join("?" * len(strongs))
    return {r[0]: r[1] for r in conn.execute(
        f"SELECT strongs_number, id FROM mti_terms "
        f" WHERE strongs_number IN ({ph}) "
        f"   AND cluster_code='M26' "
        f"   AND COALESCE(delete_flagged,0)=0",
        strongs,
    )}


def preflight(conn):
    msgs = []
    ok = True
    sg = get_subgroup_ids(conn)
    for c in ("M26-A1", "M26-A2", "M26-BOUNDARY"):
        if c not in sg:
            msgs.append(f"[ERR] sub-group {c} not found")
            ok = False

    # All Phase 2 vcgs exist
    p2_codes = [v["code"] for v in PHASE2_VCGS]
    p2_ids = get_vcg_ids_by_code(conn, p2_codes)
    missing = [c for c in p2_codes if c not in p2_ids]
    if missing:
        msgs.append(f"[ERR] Phase 2 vcgs missing: {missing}")
        ok = False
    else:
        msgs.append(f"[ok] all {len(p2_codes)} Phase 2 vcgs present")

    # NEW codes must NOT exist (idempotency)
    new_codes = [v["code"] for v in PHASE3_NEW_VCGS]
    existing_new = get_vcg_ids_by_code(conn, new_codes)
    if existing_new:
        msgs.append(f"[ERR] NEW vcg codes already exist (re-run on "
                    f"applied DB?): {sorted(existing_new.keys())}")
        ok = False
    else:
        msgs.append(f"[ok] all {len(new_codes)} NEW vcg codes available")

    # All NEW terms resolve
    all_strongs = sorted(set(s for v in PHASE3_NEW_VCGS for s in v["terms"]))
    term_ids = get_term_ids_by_strong(conn, all_strongs)
    missing_terms = [s for s in all_strongs if s not in term_ids]
    if missing_terms:
        msgs.append(f"[ERR] terms not found in M26: {missing_terms}")
        ok = False
    else:
        msgs.append(f"[ok] all {len(all_strongs)} NEW vcg terms resolve")

    # Sample-check: all source vr_ids in Phase 3 + Phase 4 exist
    all_vrs: set[int] = set()
    for v in PHASE3_NEW_VCGS:
        all_vrs.update(v["source_vr_ids"])
        all_vrs.add(v["anchor_vr"])
    all_vrs.update(PHASE4A_TO_BOUNDARY)
    all_vrs.update(PHASE4B_TO_A1)
    for v in PHASE2_VCGS:
        all_vrs.add(v["anchor_vr"])

    ph_vrs = ",".join("?" * len(all_vrs))
    found = {r[0] for r in conn.execute(
        f"SELECT id FROM wa_verse_records WHERE id IN ({ph_vrs})",
        list(all_vrs),
    )}
    missing_vrs = sorted(all_vrs - found)
    if missing_vrs:
        msgs.append(f"[ERR] {len(missing_vrs)} vr_ids not in "
                    f"wa_verse_records: {missing_vrs[:10]}...")
        ok = False
    else:
        msgs.append(f"[ok] all {len(all_vrs)} referenced vr_ids exist")

    # M26-A2 currently has X verses (record for delta)
    n_a2 = conn.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        " WHERE vc.cluster_subgroup_id=? "
        "   AND COALESCE(vc.delete_flagged,0)=0",
        (sg.get("M26-A2", -1),),
    ).fetchone()[0]
    msgs.append(f"  M26-A2 active vc rows pre-apply: {n_a2}")

    return ok, msgs, sg, p2_ids, term_ids


def run_apply(conn, sg, p2_ids, term_ids):
    cur = conn.cursor()
    counts = defaultdict(int)
    ts = now_iso()
    sg_a1 = sg["M26-A1"]
    sg_a2 = sg["M26-A2"]
    sg_b = sg["M26-BOUNDARY"]

    # ─── Phase 2 — rename 8 vcgs + reset anchors ────────────────────
    print()
    print("Phase 2 — Rename 8 vcgs + reset anchors")
    print("-" * 72)
    for v in PHASE2_VCGS:
        vcg_id = p2_ids[v["code"]]
        # Update description
        cur.execute(
            "UPDATE verse_context_group SET context_description=? "
            " WHERE id=?",
            (v["description"], vcg_id),
        )
        # Clear is_anchor=1 on this vcg's M26-A2 vc rows
        rc_clear = cur.execute(
            "UPDATE verse_context "
            "   SET is_anchor=0 "
            " WHERE group_id=? "
            "   AND cluster_subgroup_id=? "
            "   AND is_anchor=1 "
            "   AND COALESCE(delete_flagged,0)=0",
            (vcg_id, sg_a2),
        ).rowcount
        # Set is_anchor=1 on the new anchor's M26-A2 vc row in this vcg
        rc_set = cur.execute(
            "UPDATE verse_context "
            "   SET is_anchor=1 "
            " WHERE verse_record_id=? "
            "   AND group_id=? "
            "   AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (v["anchor_vr"], vcg_id, sg_a2),
        ).rowcount
        counts["phase2_descriptions"] += 1
        counts["phase2_anchors_cleared"] += rc_clear
        counts["phase2_anchors_set"] += rc_set
        print(f"  {v['code']:<10} description updated · "
              f"anchors cleared={rc_clear} · anchor set={rc_set} "
              f"(vr_id={v['anchor_vr']})")

    # ─── Phase 2b — cross-vcg moves (e.g. 950-003 dissolution) ─────
    print()
    print("Phase 2b — Cross-vcg verse moves (e.g. 950-003 dissolution)")
    print("-" * 72)
    cross_codes = sorted(set(
        m["from"] for m in PHASE2_CROSS_VCG_MOVES
    ) | set(m["to"] for m in PHASE2_CROSS_VCG_MOVES))
    cross_ids = get_vcg_ids_by_code(conn, cross_codes)
    for m in PHASE2_CROSS_VCG_MOVES:
        from_id = cross_ids[m["from"]]
        to_id = cross_ids[m["to"]]
        ph = ",".join("?" * len(m["vr_ids"]))
        # Force is_anchor=0 on moved rows — the destination vcg's
        # anchor was already set in Phase 2 above; an incoming row
        # carrying is_anchor=1 from the source vcg would create a
        # second anchor in the destination, violating the
        # one-anchor-per-vcg rule.
        rc = cur.execute(
            f"UPDATE verse_context "
            f"   SET group_id=?, is_anchor=0 "
            f" WHERE verse_record_id IN ({ph}) "
            f"   AND group_id=? "
            f"   AND cluster_subgroup_id=? "
            f"   AND COALESCE(delete_flagged,0)=0",
            (to_id, *m["vr_ids"], from_id, sg_a2),
        ).rowcount
        counts["phase2b_cross_vcg_moves"] += rc
        print(f"  {m['from']} → {m['to']}: {rc} vc rows "
              f"(vr_ids={m['vr_ids']})")

    # ─── Phase 3 — INSERT 17 NEW vcgs + multi-term links + reassign vcs ─
    print()
    print("Phase 3 — Create 17 NEW vcgs + reassign verses")
    print("-" * 72)
    new_vcg_ids: dict[str, int] = {}
    for v in PHASE3_NEW_VCGS:
        # INSERT vcg
        cur.execute(
            "INSERT INTO verse_context_group "
            "  (group_code, context_description, "
            "   notes, delete_flagged, vertical_pass_flag) "
            "VALUES (?, ?, NULL, 0, 0)",
            (v["code"], v["description"]),
        )
        new_id = cur.lastrowid
        new_vcg_ids[v["code"]] = new_id
        counts["phase3_new_vcgs"] += 1

        # INSERT vcg_term rows for each linked term
        for s in v["terms"]:
            cur.execute(
                "INSERT INTO vcg_term "
                "  (vcg_id, mti_term_id, placement_note, delete_flagged, "
                "   created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, ?, ?)",
                (new_id, term_ids[s],
                 f"DIR-003 NEW vcg for {s}", ts, ts),
            )
            counts["phase3_vcg_term_links"] += 1

        # Reassign vc rows: UPDATE vc.group_id where vc.verse_record_id
        # IN source list AND vc.cluster_subgroup_id = M26-A2
        ph = ",".join("?" * len(v["source_vr_ids"]))
        rc = cur.execute(
            f"UPDATE verse_context "
            f"   SET group_id=? "
            f" WHERE verse_record_id IN ({ph}) "
            f"   AND cluster_subgroup_id=? "
            f"   AND COALESCE(delete_flagged,0)=0",
            (new_id, *v["source_vr_ids"], sg_a2),
        ).rowcount
        counts["phase3_vc_reassigned"] += rc

        # Set is_anchor=1 on the anchor vr_id's vc row in this NEW vcg
        rc_a = cur.execute(
            "UPDATE verse_context "
            "   SET is_anchor=1 "
            " WHERE verse_record_id=? "
            "   AND group_id=? "
            "   AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (v["anchor_vr"], new_id, sg_a2),
        ).rowcount
        counts["phase3_anchors_set"] += rc_a
        print(f"  {v['code']:<14} (id={new_id}) terms={len(v['terms'])} "
              f"vc reassigned={rc} anchor_set={rc_a}")

    # ─── Phase 4a — Move 54 vc rows to M26-BOUNDARY ─────────────────
    print()
    print("Phase 4a — Move 54 vc rows M26-A2 → M26-BOUNDARY")
    print("-" * 72)
    ph = ",".join("?" * len(PHASE4A_TO_BOUNDARY))
    rc = cur.execute(
        f"UPDATE verse_context "
        f"   SET cluster_subgroup_id=? "
        f" WHERE verse_record_id IN ({ph}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND COALESCE(delete_flagged,0)=0",
        (sg_b, *PHASE4A_TO_BOUNDARY, sg_a2),
    ).rowcount
    counts["phase4a_vc_to_boundary"] = rc
    print(f"  vc rows moved: {rc} (expected {len(PHASE4A_TO_BOUNDARY)})")

    # ─── Phase 4b — Move 1 vc row to M26-A1 ─────────────────────────
    print()
    print("Phase 4b — Move 1 vc row M26-A2 → M26-A1")
    print("-" * 72)
    ph = ",".join("?" * len(PHASE4B_TO_A1))
    rc = cur.execute(
        f"UPDATE verse_context "
        f"   SET cluster_subgroup_id=? "
        f" WHERE verse_record_id IN ({ph}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND COALESCE(delete_flagged,0)=0",
        (sg_a1, *PHASE4B_TO_A1, sg_a2),
    ).rowcount
    counts["phase4b_vc_to_a1"] = rc
    print(f"  vc rows moved: {rc} (expected 1)")

    # 4b also needs vcg_term link: H6664G needs to be linked to M26-A1
    # already is (per the M26-A apply). Check by querying — no action
    # needed if already linked.
    # The vc row now points at vcg=942-002 (or wherever it was) which
    # already links H6664G to M26-A1 via mti_term_subgroup. Good.

    # ─── Phase 1 — soft-delete dissolved vcgs ───────────────────────
    # 950-003 is dissolved per the directive — its verses moved out via
    # Phase 2b (to 950-001 / 950-002) and Phase 4a (to BOUNDARY). The
    # row is now empty and can be soft-deleted to satisfy H5.
    print()
    print("Phase 1 — Soft-delete dissolved vcgs")
    print("-" * 72)
    for code in PHASE1_VCGS_TO_SOFT_DELETE:
        rc = cur.execute(
            "UPDATE verse_context_group "
            "   SET delete_flagged=1, "
            "       notes=COALESCE(notes || ' | ', '') || ? "
            " WHERE group_code=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (f"DIR-003 dissolution: verses moved to 950-001/950-002 "
             f"and BOUNDARY", code),
        ).rowcount
        counts["phase1_vcgs_soft_deleted"] += rc
        print(f"  {code} soft-deleted: {rc} row")

    return counts, new_vcg_ids


def verify(conn, sg, p2_ids, new_vcg_ids):
    invariants: dict = {}

    # I-1: Phase 1 — 5 dropped vcgs should have 0 M26-A2 verses
    sg_a2 = sg["M26-A2"]
    dropped = {}
    for code in PHASE1_DROPPED_VCGS:
        r = conn.execute(
            "SELECT id FROM verse_context_group WHERE group_code=? "
            " AND COALESCE(delete_flagged,0)=0",
            (code,),
        ).fetchone()
        if not r:
            dropped[code] = "(vcg missing — N/A)"
            continue
        vcg_id = r[0]
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE group_id=? AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (vcg_id, sg_a2),
        ).fetchone()[0]
        dropped[code] = n
    invariants["I-1: Phase 1 dropped vcgs M26-A2 verse counts (expect 0)"] \
        = dropped

    # I-2: Phase 2 anchors set correctly (one per vcg in M26-A2)
    p2_anchors = {}
    for v in PHASE2_VCGS:
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE group_id=? AND cluster_subgroup_id=? "
            "   AND is_anchor=1 AND COALESCE(delete_flagged,0)=0",
            (p2_ids[v["code"]], sg_a2),
        ).fetchone()[0]
        p2_anchors[v["code"]] = n
    invariants["I-2: Phase 2 anchors per vcg in M26-A2 (expect 1)"] = (
        p2_anchors
    )

    # I-3: Phase 3 NEW vcgs — verse counts per NEW
    p3_counts = {}
    for v in PHASE3_NEW_VCGS:
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE group_id=? AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (new_vcg_ids[v["code"]], sg_a2),
        ).fetchone()[0]
        expected = len(v["source_vr_ids"])
        p3_counts[v["code"]] = f"{n} (expected ≤{expected})"
    invariants["I-3: Phase 3 NEW vcg verse counts in M26-A2"] = p3_counts

    # I-4: Sub-group totals
    for code in ("M26-A1", "M26-A2", "M26-BOUNDARY"):
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (sg[code],),
        ).fetchone()[0]
        invariants[f"I-4: active vc rows in {code}"] = n

    # I-5: Any M26-A2 vc rows still without a group_id? (post-apply)
    n = conn.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        " WHERE vc.cluster_subgroup_id=? "
        "   AND vc.group_id IS NULL "
        "   AND COALESCE(vc.delete_flagged,0)=0 "
        "   AND mt.cluster_code='M26'",
        (sg_a2,),
    ).fetchone()[0]
    invariants["I-5: M26-A2 active vc rows without group_id"] = n

    # I-6: For each Phase 2 vcg, the post-apply M26-A2 verse count
    # should equal len(retain_list) + (any cross-vcg adds). Surface
    # any "stragglers" — vc rows still in the vcg that aren't in the
    # retain list (would indicate the directive's reassign-list is
    # incomplete; e.g. 169443 in 3246-003 which the directive flags as
    # 'reassigned in Phase 3' but doesn't list anywhere).
    p2_retain = {
        "911-001":  {25210, 25212, 25167, 25174, 169240, 169297},
        "911-002":  {169247, 169248, 169243},
        "942-001":  {96028, 96007, 96009, 96010, 95994, 28342, 28344,
                     28340},
        "942-003":  {28324, 96041},
        "950-001":  {28759, 28760, 28762, 28756, 28757, 28758, 28763,
                     28736, 28740, 93731, 28771, 28737},  # +ADD from 950-003
        "950-002":  {93734, 93726, 28766, 93724, 28741, 28739, 28745},
        "3246-002": {169370, 169463, 169496, 169465, 169484, 169485,
                     169489, 169495, 169498, 169500, 169480, 169396,
                     169388, 169439},
        "3246-003": {169392, 169482, 169483, 169497, 169499, 169501,
                     169502, 169510, 169511, 169470, 169476, 169478,
                     169449},
    }
    stragglers: dict = {}
    for v in PHASE2_VCGS:
        code = v["code"]
        retain = p2_retain[code]
        rows = conn.execute(
            "SELECT verse_record_id FROM verse_context "
            " WHERE group_id=? AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (p2_ids[code], sg_a2),
        ).fetchall()
        actual = {r[0] for r in rows}
        extra = sorted(actual - retain)
        if extra:
            stragglers[code] = extra
    invariants["I-6: Phase 2 vcgs — non-retained vr_ids still present "
               "(directive omissions)"] = stragglers or "(none)"

    return invariants


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2
    if args.dry_run and args.live:
        print("ERROR: --dry-run and --live are mutually exclusive",
              file=sys.stderr)
        return 2

    print("=" * 72)
    print("DIR-M26-20260510-003 apply (M26-A2 VSG restructure)")
    print(f"  Mode: {'DRY-RUN (rollback)' if args.dry_run else 'LIVE (commit)'}")
    print(f"  DB:   {DB_PATH}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    print("PRE-FLIGHT")
    print("-" * 72)
    ok, msgs, sg, p2_ids, term_ids = preflight(conn)
    for m in msgs:
        print(m)
    print()
    if not ok:
        print("Pre-flight failed — exiting without changes.")
        return 1

    if args.live:
        print("Taking pre-apply backup...")
        b = take_backup("m26_dir003")
        print(f"  Backup saved: {b}")
        print()

    try:
        conn.execute("BEGIN")
        counts, new_vcg_ids = run_apply(conn, sg, p2_ids, term_ids)
        print()
        print("FOREIGN-KEY CHECK")
        print("-" * 72)
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            print(f"  [ERR] {len(fkv)} FK violations")
            for v in fkv[:10]:
                print(f"    {dict(zip(['table','rowid','parent','fkid'], v))}")
            raise RuntimeError(f"foreign_key_check failed: {len(fkv)}")
        print("  [ok] zero violations")
        print()
        print("VERIFICATION")
        print("-" * 72)
        invariants = verify(conn, sg, p2_ids, new_vcg_ids)
        for k, v in invariants.items():
            print(f"  {k}: {v}")
        print()
        if args.dry_run:
            conn.execute("ROLLBACK")
            print("DRY-RUN: changes rolled back.")
        else:
            conn.execute("COMMIT")
            print("LIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {type(e).__name__}: {e}")
        raise

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:35s} {v}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
