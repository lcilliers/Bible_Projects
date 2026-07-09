"""_apply_m26_dir005_v1_20260510.py — DB-modifying.

Apply DIR-M26-20260510-005 (M26-A1 VSG restructure) under the
post-DIR-004 v14 state.

Source directive:
  Sessions/Session_Clusters/M26/wa-cluster-M26-dir-005-A1-vsg-restructure-v1-20260510.md

Operations (single transaction, foreign_keys=ON):

  Phase 2  — INSERT 7 NEW vcgs (codes M26-A1-001..007) for G1..G7
  Phase 3  — UPDATE descriptions on 3 retained vcgs
              (942-002, 911-003, 3193-002)
  Phase 4  — UPDATE vc.group_id for ~150 M26-A1 vc rows
              (per the per-source tables in the directive)
              + clear is_anchor on M26-A1 vcg-rows touched
              + set is_anchor=1 on each NEW vcg's anchor vr_id
  Phase 4b — Auto-absorb: add vcg_term rows for any (vcg, term) pair
              referenced by the new vc routings but not yet in vcg_term
  Phase 5  — Soft-delete globally-empty vcgs post-moves

NO API calls. ~3 sec wall time.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

# ══════════════════════════════════════════════════════════════════════
#  Phase 2 — 7 NEW vcgs G1..G7
# ══════════════════════════════════════════════════════════════════════
NEW_VCGS = [
    {
        "key": "G1", "code": "M26-A1-001", "anchor_vr": 169479,
        "description": (
            "Term declares God's righteousness as a foundational, "
            "permanent attribute of his nature — not situational, not "
            "responsive to circumstances, not capable of violation. It "
            "is affirmed across all his ways and all his works (Psa "
            "145:17), endures forever (Psa 111:3), reaches to the high "
            "heavens (Psa 71:19), and will never be dismayed (Isa "
            "51:6). It is the structural basis of his throne (Psa "
            "89:14, 97:2), and paired consistently with faithfulness, "
            "holiness, and mercy. The closest the text comes to "
            "defining it is by exclusion: he does no injustice (Zep 3:5)."
        ),
    },
    {
        "key": "G2", "code": "M26-A1-002", "anchor_vr": 96035,
        "description": (
            "Term names God's righteousness as expressed through his "
            "judicial acts — judgments that conform to what is right "
            "rather than to preference or power. God judges the world "
            "with righteousness (Psa 9:8), his throne gives righteous "
            "judgment (Psa 9:4), the heavens declare it (Psa 50:6), and "
            "his judgments are named just in their most severe "
            "eschatological expressions (Rev 15:3–19:2). Christ's "
            "judgment is just because it aligns with the Father's will "
            "(Joh 5:30). God's righteous rules are expressions of this "
            "judicial character (Psa 119:7, 75, 106)."
        ),
    },
    {
        "key": "G3", "code": "M26-A1-003", "anchor_vr": 169401,
        "description": (
            "Term names God's righteousness as the quality that makes "
            "him reliable and faithful to his covenant people — keeping "
            "promises (Neh 9:8), betrothing in righteousness and "
            "justice (Hos 2:19), extending his righteousness across "
            "generations to those who fear him (Psa 103:17). His "
            "righteous promise is longed for (Psa 119:123); his "
            "testimonies are appointed in righteousness and "
            "faithfulness (Psa 119:138). The covenant bond itself is "
            "characterised by righteousness: 'I will be their God, in "
            "faithfulness and in righteousness' (Zec 8:8). He practices "
            "steadfast love, justice, and righteousness in the earth "
            "(Jer 9:24)."
        ),
    },
    {
        "key": "G4", "code": "M26-A1-004", "anchor_vr": 169310,
        "description": (
            "Term names God's righteousness as the basis on which he "
            "acts to save, deliver, vindicate, and redeem — the quality "
            "that makes him reliably and confidently appealable. The "
            "psalmists invoke it repeatedly as the ground of petition: "
            "'In your righteousness deliver me' (Psa 31:1, 71:2, "
            "143:1, 143:11). God's saving acts are expressions of his "
            "righteousness (1Sa 12:7). Righteousness and salvation "
            "travel inseparably (Isa 45:8, 46:13, 51:5). In the NT, "
            "God's righteousness is the basis on which he forgives "
            "(1Jo 1:9), and the ground of the cross — where he is "
            "simultaneously just and the justifier (Rom 3:26). God "
            "gives his righteousness to his people as gift and "
            "vindication (Psa 24:5, Isa 54:17)."
        ),
    },
    {
        "key": "G5", "code": "M26-A1-005", "anchor_vr": 28744,
        "description": (
            "Term names God's righteousness as something that must be "
            "declared, proclaimed, and made known — it is not "
            "self-evident but requires witness. The psalmist's tongue "
            "speaks of it all day (Psa 35:28, 71:24, 145:7), future "
            "generations shall proclaim it (Psa 22:31), the heavens "
            "declare it (Psa 50:6, 97:6). God's righteous word goes "
            "out and does not return (Isa 45:23). In the NT it is "
            "revealed through the gospel (Rom 1:17), manifested apart "
            "from law (Rom 3:21), and its glory exceeds the ministry "
            "of condemnation (2Cor 3:9). The Spirit convicts the world "
            "concerning it (Joh 16:8). The proclamation of God's "
            "righteousness is a sustained act of the covenant "
            "community across all time."
        ),
    },
    {
        "key": "G6", "code": "M26-A1-006", "anchor_vr": 25164,
        "description": (
            "Term names God's righteousness as the standard that "
            "exposes human unrighteousness by contrast — when God's "
            "righteousness is affirmed, human guilt and shame are "
            "simultaneously revealed. The pattern recurs throughout "
            "Scripture: 'you are righteous; we have acted wickedly' "
            "(Neh 9:33), 'you are just; we are before you in guilt' "
            "(Ezr 9:15), 'The Lord is in the right; I have rebelled "
            "against his word' (Lam 1:18), 'to you belongs "
            "righteousness, but to us open shame' (Dan 9:7). Human "
            "anger cannot produce God's righteousness (Jam 1:20); "
            "human self-established righteousness fails to submit to "
            "it (Rom 10:3)."
        ),
    },
    {
        "key": "G7", "code": "M26-A1-007", "anchor_vr": 169384,
        "description": (
            "Term names righteousness as the defining quality of the "
            "coming Messianic figure — the Righteous One, the "
            "righteous Branch, the righteous Servant. The Servant's "
            "righteousness enables him to make many accounted "
            "righteous (Isa 53:11); the Branch is named 'The Lord is "
            "our righteousness' (Jer 23:6, 33:16); the Messianic king "
            "is 'righteous and having salvation' (Zec 9:9); Christ's "
            "love of righteousness grounds his anointing (Psa 45:7, "
            "Heb 1:9). In the NT these figures are identified as "
            "Jesus, who is the Holy and Righteous One (Act 3:14), "
            "whose coming was betrayed (Act 7:52), who died 'the "
            "righteous for the unrighteous' (1Pe 3:18), and who is "
            "called as advocate 'Jesus Christ the righteous' (1Jo "
            "2:1). God's righteousness does not remain external — it "
            "becomes incarnate in the Messiah and through him is "
            "given to his people."
        ),
    },
]

# ══════════════════════════════════════════════════════════════════════
#  Phase 4 — Per-source verse assignments. Each (vr_id, target_key)
#  causes vc.group_id update for the M26-A1 vc row.
# ══════════════════════════════════════════════════════════════════════
ASSIGNMENTS: list[tuple[int, str]] = [
    # Ungrouped (13)
    (169343, "G1"), (169469, "G1"), (169472, "G1"), (169479, "G1"),
    (169340, "G1"), (169513, "G1"),
    (169504, "G2"), (169474, "G2"),
    (96018, "G5"),
    (169333, "G6"), (169400, "G6"),
    (57129, "G7"), (57130, "G7"),
    # group-1426 / 950-003 dissolved (6)
    (93733, "G5"), (93732, "G7"), (93728, "G2"),
    (28746, "G6"), (28723, "G4"), (28725, "G5"),
    # 911-002 (2)
    (169309, "G4"), (25189, "G4"),
    # 942-004 (4)
    (28343, "G1"), (96020, "G7"), (28311, "G7"), (28312, "G7"),
    # 942-001 (4)
    (96027, "G5"), (96012, "G4"), (96014, "G5"), (28334, "G2"),
    # 3246-001 (4)
    (169375, "G7"), (169384, "G7"), (169389, "G7"), (169512, "G7"),
    # 950-002 (4)
    (93736, "G7"), (93741, "G1"), (28738, "G7"), (93730, "G6"),
    # 942-003 (5)
    (96011, "G4"), (96003, "G2"), (96004, "G2"), (95993, "G2"),
    (95995, "G3"),
    # 3193-001 (12)
    (93802, "G7"), (93786, "G7"), (93776, "G2"), (93764, "G7"),
    (93766, "G7"), (93762, "G7"), (93758, "G2"), (93759, "G2"),
    (93760, "G2"), (93752, "G7"), (93746, "G4"), (93747, "G7"),
    # 3193-002 (2 move; 4 remain)
    (93815, "G7"), (93775, "G1"),
    # 911-001 (9)
    (169254, "G3"), (169328, "G2"), (25169, "G4"), (25183, "G1"),
    (25202, "G7"), (25175, "G4"), (25205, "G7"), (25206, "G7"),
    (169329, "G3"),
    # 950-001 (9)
    (28744, "G5"), (28755, "G6"), (28751, "G5"), (28752, "G4"),
    (28753, "G4"), (28754, "G4"), (28761, "G4"), (28764, "G1"),
    (28770, "G1"),
    # 3246-002 (9)
    (169347, "G6"), (169362, "G6"), (169401, "G3"), (169395, "G1"),
    (169466, "G1"), (169448, "G2"), (169381, "G1"), (169387, "G1"),
    (169397, "G6"),
    # 942-002 (25)
    (28341, "G5"), (96016, "G4"), (96034, "G2"), (96035, "G2"),
    (96021, "G5"), (96022, "G2"), (96026, "G4"), (96031, "G3"),
    (96032, "G3"), (96033, "G1"), (96037, "G2"), (96038, "G1"),
    (96039, "G5"), (96040, "G2"), (95996, "G3"), (95997, "G1"),
    (28317, "G4"), (28320, "G3"), (28319, "G1"), (28323, "G4"),
    (28321, "G4"), (28322, "G1"), (28325, "G4"), (28337, "G1"),
    (28308, "G3"),
    # 911-003 (45 listed in directive table)
    (169242, "G5"), (25213, "G1"), (169315, "G4"), (169308, "G4"),
    (169310, "G4"), (169311, "G3"), (169313, "G1"), (169312, "G4"),
    (169314, "G5"), (169316, "G4"), (169321, "G4"), (169318, "G5"),
    (169319, "G5"), (169320, "G5"), (169322, "G5"), (169323, "G7"),
    (169325, "G5"), (169326, "G4"), (169327, "G5"), (169296, "G7"),
    (169295, "G3"), (169300, "G1"), (169304, "G4"), (169303, "G1"),
    (169305, "G4"), (169306, "G4"), (169307, "G5"), (25171, "G2"),
    (25178, "G4"), (25176, "G5"), (25177, "G1"), (25180, "G4"),
    (25186, "G1"), (25187, "G1"), (25194, "G4"), (25195, "G4"),
    (25198, "G4"), (25199, "G4"), (25200, "G5"), (25209, "G3"),
    (25164, "G6"), (169277, "G4"), (25217, "G5"), (25218, "G4"),
    (25216, "G7"),
]

# ══════════════════════════════════════════════════════════════════════
#  Phase 3 — 3 retained vcgs with description updates
# ══════════════════════════════════════════════════════════════════════
PHASE3_DESCRIPTIONS = [
    {
        "code": "942-002",
        "description": (
            "Term names God's righteousness as his foundational divine "
            "attribute — the eternal quality that is the basis of his "
            "throne, proclaimed by the heavens, expressed in his "
            "righteous right hand, and active in his covenant calling "
            "and commissioning. His righteous word goes out and does "
            "not return empty. All his judgments are rooted in this "
            "attribute. The term consistently associates God's "
            "righteousness with his acts, but the attribute precedes "
            "and grounds them all."
        ),
    },
    {
        "code": "911-003",
        "description": (
            "Term names God's righteousness as the object of appeal, "
            "praise, and proclamation by his people — the quality they "
            "invoke when seeking deliverance, declare when praising "
            "him, and remember across generations. It is vast (reaches "
            "the high heavens), eternal (endures forever), and active "
            "(draws near with salvation). God's righteousness is not "
            "only what he is but what he does for his people — the "
            "quality from which saving acts consistently flow."
        ),
    },
    {
        "code": "3193-002",
        "description": (
            "Term names God and Christ as just and righteous — "
            "addressing the Father directly as 'righteous Father' "
            "(Joh 17:25), affirming God's judgments as just in their "
            "most severe expressions (Rev 15:3, 16:5, 16:7, 19:2). The "
            "VSG captures direct divine address and the eschatological "
            "declaration of God's justice as final judge."
        ),
    },
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR,
                     f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, p)
    return p


def preflight(conn):
    msgs = []
    ok = True
    sg = {r[0]: r[1] for r in conn.execute(
        "SELECT subgroup_code, id FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0"
    )}
    if "M26-A1" not in sg:
        msgs.append("[ERR] M26-A1 missing")
        return False, msgs, sg, {}, {}, set()

    new_codes = [v["code"] for v in NEW_VCGS]
    existing_new = list(conn.execute(
        f"SELECT group_code FROM verse_context_group "
        f" WHERE group_code IN ({','.join('?' * len(new_codes))}) "
        f"   AND COALESCE(delete_flagged,0)=0",
        new_codes,
    ))
    if existing_new:
        msgs.append(f"[ERR] NEW codes already exist: "
                    f"{[r[0] for r in existing_new]}")
        ok = False
    else:
        msgs.append(f"[ok] all {len(new_codes)} NEW vcg codes available")

    p3_codes = [d["code"] for d in PHASE3_DESCRIPTIONS]
    p3_ids = {r[0]: r[1] for r in conn.execute(
        f"SELECT group_code, id FROM verse_context_group "
        f" WHERE group_code IN ({','.join('?' * len(p3_codes))}) "
        f"   AND COALESCE(delete_flagged,0)=0",
        p3_codes,
    )}
    missing_p3 = [c for c in p3_codes if c not in p3_ids]
    if missing_p3:
        msgs.append(f"[ERR] Phase 3 vcgs missing: {missing_p3}")
        ok = False
    else:
        msgs.append(f"[ok] all {len(p3_codes)} Phase 3 retained vcgs "
                    f"present")

    # Each ASSIGNMENT vr_id must have an active M26-A1 vc row
    vr_ids = sorted({v for v, _ in ASSIGNMENTS})
    ph = ",".join("?" * len(vr_ids))
    found = {r[0] for r in conn.execute(
        f"SELECT verse_record_id FROM verse_context "
        f" WHERE verse_record_id IN ({ph}) "
        f"   AND cluster_subgroup_id=? "
        f"   AND COALESCE(delete_flagged,0)=0",
        (*vr_ids, sg["M26-A1"]),
    )}
    missing_vr = sorted(set(vr_ids) - found)
    if missing_vr:
        msgs.append(f"[ERR] {len(missing_vr)} ASSIGNMENT vr_ids have no "
                    f"active M26-A1 vc row: {missing_vr[:10]}...")
        ok = False
    else:
        msgs.append(f"[ok] all {len(vr_ids)} ASSIGNMENT vr_ids resolve "
                    f"to active M26-A1 vc rows")

    # Anchors: each NEW vcg's anchor_vr must be in the assignments for
    # that key (otherwise we can't set is_anchor=1 — the anchor isn't
    # in the vcg)
    anchor_check = []
    for v in NEW_VCGS:
        if (v["anchor_vr"], v["key"]) not in [(x, y) for x, y in
                                              ASSIGNMENTS]:
            anchor_check.append(f"{v['key']} anchor_vr={v['anchor_vr']}")
    if anchor_check:
        msgs.append(f"[ERR] NEW anchor vr_ids not in their assignment "
                    f"list: {anchor_check}")
        ok = False
    else:
        msgs.append(f"[ok] all 7 NEW anchor vr_ids appear in their "
                    f"assignment lists")

    n_a1 = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
        (sg["M26-A1"],),
    ).fetchone()[0]
    msgs.append(f"  M26-A1 active vc rows pre-apply: {n_a1}")

    # Detect duplicate vr_id assignments (same vr_id → multiple targets)
    seen: dict = {}
    dups: list = []
    for v, k in ASSIGNMENTS:
        if v in seen and seen[v] != k:
            dups.append((v, seen[v], k))
        seen[v] = k
    if dups:
        msgs.append(f"[WARN] duplicate ASSIGNMENT vr_ids with different "
                    f"targets: {dups}")

    return ok, msgs, sg, p3_ids, set(), set(vr_ids)


def run_apply(conn, sg, p3_ids):
    cur = conn.cursor()
    counts = defaultdict(int)
    ts = now_iso()
    sg_a1 = sg["M26-A1"]

    # ─── Phase 2 — INSERT 7 NEW vcgs ────────────────────────────────
    print()
    print("Phase 2 — INSERT 7 NEW vcgs (G1..G7)")
    print("-" * 72)
    new_ids: dict[str, int] = {}  # key (G1..G7) → vcg.id
    for v in NEW_VCGS:
        cur.execute(
            "INSERT INTO verse_context_group "
            "  (group_code, context_description, notes, "
            "   delete_flagged, vertical_pass_flag) "
            "VALUES (?, ?, NULL, 0, 0)",
            (v["code"], v["description"]),
        )
        new_id = cur.lastrowid
        new_ids[v["key"]] = new_id
        counts["phase2_new_vcgs"] += 1
        print(f"  {v['key']} → {v['code']:<14} (id={new_id})")

    # ─── Phase 3 — Update descriptions on retained vcgs ─────────────
    print()
    print("Phase 3 — Update descriptions on 3 retained vcgs")
    print("-" * 72)
    for d in PHASE3_DESCRIPTIONS:
        rc = cur.execute(
            "UPDATE verse_context_group "
            "   SET context_description=? "
            " WHERE id=?",
            (d["description"], p3_ids[d["code"]]),
        ).rowcount
        counts["phase3_descriptions"] += rc
        print(f"  {d['code']} description updated ({rc} row)")

    # ─── Phase 4 — Verse assignments ─────────────────────────────────
    print()
    print("Phase 4 — Verse assignments + anchor setting")
    print("-" * 72)
    for vr_id, key in ASSIGNMENTS:
        rc = cur.execute(
            "UPDATE verse_context "
            "   SET group_id=?, is_anchor=0 "
            " WHERE verse_record_id=? "
            "   AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (new_ids[key], vr_id, sg_a1),
        ).rowcount
        counts["phase4_vc_reassigned"] += rc
    print(f"  vc.group_id moves: {counts['phase4_vc_reassigned']} "
          f"(expected {len(ASSIGNMENTS)})")

    # Set anchors
    for v in NEW_VCGS:
        rc = cur.execute(
            "UPDATE verse_context "
            "   SET is_anchor=1 "
            " WHERE verse_record_id=? "
            "   AND group_id=? "
            "   AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (v["anchor_vr"], new_ids[v["key"]], sg_a1),
        ).rowcount
        counts["phase4_anchors_set"] += rc
        print(f"  {v['key']} anchor set on vr_id {v['anchor_vr']}: "
              f"{rc} row")

    # ─── Phase 4b — Auto-absorb vcg_term for new placements ─────────
    print()
    print("Phase 4b — Auto-absorb vcg_term rows")
    print("-" * 72)
    rc = cur.execute(
        "INSERT OR IGNORE INTO vcg_term "
        "  (vcg_id, mti_term_id, placement_note, delete_flagged, "
        "   created_at, last_updated_date) "
        "SELECT DISTINCT vc.group_id, vc.mti_term_id, "
        "       'DIR-005 absorb cross-term placement', 0, ?, ? "
        "  FROM verse_context vc "
        "  JOIN verse_context_group vcg ON vcg.id=vc.group_id "
        "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        " WHERE mt.cluster_code='M26' "
        "   AND COALESCE(vc.delete_flagged,0)=0 "
        "   AND COALESCE(vcg.delete_flagged,0)=0 "
        "   AND NOT EXISTS ("
        "       SELECT 1 FROM vcg_term vt "
        "        WHERE vt.vcg_id=vc.group_id "
        "          AND vt.mti_term_id=vc.mti_term_id "
        "          AND COALESCE(vt.delete_flagged,0)=0"
        "   )",
        (ts, ts),
    ).rowcount
    counts["phase4b_vcg_term_absorbed"] = rc
    print(f"  vcg_term rows absorbed: {rc}")

    # ─── Phase 5 — Soft-delete globally-empty vcgs ──────────────────
    print()
    print("Phase 5 — Soft-delete globally-empty vcgs")
    print("-" * 72)
    candidates = [
        "911-002", "942-004", "942-001", "3246-001", "950-002",
        "942-003", "3193-001", "911-001", "950-001", "3246-002",
        "942-002",
    ]
    for code in candidates:
        r = conn.execute(
            "SELECT id FROM verse_context_group "
            " WHERE group_code=? AND COALESCE(delete_flagged,0)=0",
            (code,),
        ).fetchone()
        if not r:
            print(f"  {code:<10} already soft-deleted (skip)")
            continue
        n_active = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE group_id=? AND COALESCE(delete_flagged,0)=0",
            (r[0],),
        ).fetchone()[0]
        if n_active == 0:
            cur.execute(
                "UPDATE verse_context_group "
                "   SET delete_flagged=1, "
                "       notes=COALESCE(notes || ' | ', '') || ? "
                " WHERE id=?",
                (f"DIR-005 dissolution: empty after Phase 4 reassignments",
                 r[0]),
            )
            counts["phase5_vcgs_soft_deleted"] += 1
            print(f"  {code:<10} soft-deleted (0 active vc rows)")
        else:
            print(f"  {code:<10} kept active ({n_active} active vc rows "
                  f"in other sub-groups)")

    return counts, new_ids


def verify(conn, sg, p3_ids, new_ids):
    invariants = {}
    sg_a1 = sg["M26-A1"]

    # I-1: 7 NEW vcg verse counts
    counts: dict[str, int] = {}
    for key, vcg_id in new_ids.items():
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE group_id=? AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (vcg_id, sg_a1),
        ).fetchone()[0]
        counts[key] = n
    invariants["I-1: NEW vcg verse counts in M26-A1"] = counts

    # I-2: One anchor per NEW vcg
    anchors: dict[str, int] = {}
    for key, vcg_id in new_ids.items():
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE group_id=? AND cluster_subgroup_id=? "
            "   AND is_anchor=1 AND COALESCE(delete_flagged,0)=0",
            (vcg_id, sg_a1),
        ).fetchone()[0]
        anchors[key] = n
    invariants["I-2: anchors per NEW vcg in M26-A1 (expect 1)"] = anchors

    # I-3: Sub-group totals
    for code in ("M26-A1", "M26-A2", "M26-BOUNDARY"):
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
            (sg[code],),
        ).fetchone()[0]
        invariants[f"I-3: active vc rows in {code}"] = n

    # I-4: M26-A1 verses still without group_id (should be 0 ideally)
    n = conn.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        " WHERE vc.cluster_subgroup_id=? "
        "   AND vc.group_id IS NULL "
        "   AND COALESCE(vc.delete_flagged,0)=0 "
        "   AND mt.cluster_code='M26'",
        (sg_a1,),
    ).fetchone()[0]
    invariants["I-4: M26-A1 active vc rows without group_id"] = n

    # I-5: M26-A1 vc rows still pointing at soft-deleted vcgs (H3 source)
    n = conn.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "  JOIN verse_context_group vcg ON vcg.id=vc.group_id "
        " WHERE vc.cluster_subgroup_id=? "
        "   AND COALESCE(vc.delete_flagged,0)=0 "
        "   AND vcg.delete_flagged=1",
        (sg_a1,),
    ).fetchone()[0]
    invariants["I-5: M26-A1 vc rows pointing at soft-deleted vcgs"] = n

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
    print("DIR-M26-20260510-005 apply (M26-A1 VSG restructure)")
    print(f"  Mode: {'DRY-RUN (rollback)' if args.dry_run else 'LIVE (commit)'}")
    print(f"  DB:   {DB_PATH}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    print("PRE-FLIGHT")
    print("-" * 72)
    ok, msgs, sg, p3_ids, _, _ = preflight(conn)
    for m in msgs:
        print(m)
    print()
    if not ok:
        print("Pre-flight failed — exiting.")
        return 1

    if args.live:
        print("Taking pre-apply backup...")
        b = take_backup("m26_dir005")
        print(f"  Backup saved: {b}")
        print()

    try:
        conn.execute("BEGIN")
        counts, new_ids = run_apply(conn, sg, p3_ids)
        print()
        print("FOREIGN-KEY CHECK")
        print("-" * 72)
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            print(f"  [ERR] {len(fkv)} FK violations")
            raise RuntimeError(f"foreign_key_check failed: {len(fkv)}")
        print("  [ok] zero violations")
        print()
        print("VERIFICATION")
        print("-" * 72)
        invariants = verify(conn, sg, p3_ids, new_ids)
        for k, v in invariants.items():
            print(f"  {k}: {v}")
        print()
        if args.dry_run:
            conn.execute("ROLLBACK")
            print("DRY-RUN: rolled back.")
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
