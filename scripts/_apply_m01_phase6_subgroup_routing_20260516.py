"""Apply M01 Phase 6 — sub-group creation, term-to-sub-group placement, verse routing.

Implements AI's WA-M01-subgroup-design-v1-20260516.md mechanically per v2_0 §9:
  Op A: INSERT 8 cluster_subgroup rows (M01-A..M01-G + M01-BOUNDARY)
  Op B: INSERT mti_term_subgroup rows (1 per primary placement; +1 per secondary)
  Op C: UPDATE verse_context.cluster_subgroup_id mechanically per term primary,
        with per-verse overrides applied from AI's §3 cross-listings.

cluster.status stays at 'Analysis - In Progress' (Phase 4 already set; no flip in Phase 6).

Usage: python scripts/_apply_m01_phase6_subgroup_routing_20260516.py [--dry-run]
"""
from __future__ import annotations
import argparse, sqlite3, sys, shutil
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
BACKUP_DIR = REPO / "backups"
DIRECTIVE = "DIR-20260516-002 (wa-cluster-M01-dir-002-subgroup-routing-v1-20260516)"

# ===== Sub-group definitions =====
SUBGROUPS = [
    ("M01-A", "Reverential Fear / Fear of God as Governing Orientation",
     "Fear-of-God as enduring inner orientation rather than reactive event — the constitutive disposition that governs the whole inner life: informing conduct, motivating worship, grounding covenant relationship, forming identity. Rooted across hundreds of verses: fear of God as the root of obedience (Deu 6:2; 10:12), criterion for divine guidance (Psa 25:12; 111:5; 34:7), foundation of wisdom (Pro 1:7; 9:10), restraining force on cruelty and injustice (Lev 19:14; 25:17; 25:43), defining character of the righteous (Job 1:1; Neh 7:2). NT: motivating awe governing obedience to Christ and authorities (Col 3:22; Eph 5:21; 1Pe 1:17; 2:17). Learnable, transmissible, divinely implantable; its absence marks moral blindness."),
    ("M01-B", "Acute Fear and Alarm",
     "Reactive, situational fear — sudden inner state of alarm, dread, or terror triggered by specific threat, unexpected encounter, supernatural appearance, or display of divine/extraordinary power. Episodic character: arises at a moment, overwhelms the inner person, governs the will's immediate response. OT: dread before armies (Num 22:3; Deu 20:1-3), divine theophanies (Exo 34:30; Judg 6:23), inexplicable events (Gen 42:35). NT: disciples at Jesus walking on water, transfiguration, calmed storm, resurrection appearances. Includes social fear: fear of crowds governing rulers' decisions, fear of the Jews suppressing speech. Reactive-and-episodic distinguishes M01-B from A's chronic orientation."),
    ("M01-C", "Terror as Overwhelming Force",
     "Terror characterised as active, assaulting force — something that comes upon the inner person from outside, encircles them, pursues them, or is projected by one power onto another. Distinctive: agency and force of the terror itself. It hunts (bal.la.hah, Job 18:11), encircles (ma.gor, Jer 6:25; 20:10; Lam 2:22), is sent as weapon by God (e.mah, Exo 23:27; chit.tah, Gen 35:5; pa.chad, Deu 2:25), projected by military empires (chit.tit, Eze 32:23-32). Strips identity (bal.la.hah, Job 30:15), paralyses will (chit.tah, Gen 35:5), renders enemies motionless (e.mah, Exo 15:16). The terror is often divine in origin — dread deployed as weapon. Also: awe-inspiring terror-force radiating from powerful entities (Leviathan, war horse, a.yom in Song 6:4)."),
    ("M01-D", "Dismay and Inner Collapse",
     "Sudden dissolution of inner coherence — what happens to the inner person when shock, catastrophe, or overwhelming news shatters composure and disables capacity to function. Collapse: dismayed person cannot answer (ba.hal, Gen 45:3), cannot see (Isa 21:3), cannot speak (cha.tat, Job 32:15), cannot resist (Judg 20:41), cannot act (Jer 17:18). Visible on body: color changes (be.hal, Dan 5:6; 5:9), limbs give way, hands paralysed (cha.tat, Eze 7:27). Can be divinely imposed (ba.hal, Psa 2:5; 90:7; cha.tat, Jer 49:37), natural response to catastrophe, or inner effect of grasping terrible message (Dan 4:19; 7:15). Distinct from acute alarm (M01-B): emphasis is dissolution of inner coherence, not reactive alertness. Dismay is the state after fear has overwhelmed — the shattering, not just the shock."),
    ("M01-E", "Trembling / Fear Made Somatic",
     "Involuntary bodily expression of fear — trembling, shuddering, quivering registering fear in the body. Somatic: body trembles, bones shake, flesh quivers, hair bristles, knees fail as outward sign of inner fear. Involuntary — overcomes the person (cha.rad, Exo 19:16; entromos, Act 7:32; tromos, Mar 16:8). In many meanings, bodily trembling is the only indicator of inner state (Saul 1Sa 28:5; Elihu Job 37:1). Theologically distinctive subset: trembling at God's word as inner posture of solemn reverence (cha.red, Isa 66:2; 66:5; Ezr 9:4; 10:3). Double dimension: physical terror response AND reverential responsiveness to the divine word."),
    ("M01-F", "Anticipatory Dread and Anxiety",
     "Sustained, forward-looking inner burden of dread — fear not triggered by immediate present threat but by what is anticipated, imagined, or foreknown. Chronicity and anticipation: weighs down the heart as ongoing burden (de.a.gah, Pro 12:25), saturates every moment (Eze 12:18-19), unrelenting day and night (pa.chad, Deu 28:66-67), anticipatory anguish preceding and matching the feared event (Job 3:25). Includes fear of death as lifelong enslaving burden (fobos, Heb 2:15), fearful expectation of judgment (foberos, Heb 10:27), conscientious dread of divine accountability shaping pastoral conduct (2Cor 12:20; Gal 4:11)."),
    ("M01-G", "Timidity and Cowardly Shrinking",
     "Fear as inner failure of constitution — cowardly, faithless recoiling presented as moral and spiritual defect. Evaluative: unlike M01-B (natural alarm) or M01-F (burden), timidity here is what the inner person ought not to have — a disposition that should yield to faith and courage. 2Ti 1:7 (deilia): explicitly named as spirit-level disposition God has not implanted, deficiency of inner constitution. Joh 14:27 (deiliaō): commanded not to yield to cowardly shrinking. Rev 21:8 (deilos): cowardice listed with idolatry and murder as vices of the lake of fire — apostasy under pressure. Pro 29:25 (cha.ra.dah): fear of man named as inner trap that ensnares the person. Not simply fear being present — fear evaluated as opposite of faith, trust, inner integrity."),
    ("M01-BOUNDARY", "Boundary — Terms Held for Researcher Decision",
     "Terms with empty meaning corpora (all verses set aside, no Pass A meanings) OR with analytical questions unresolved in Phase 3. Cannot be placed in a substantive sub-group from meaning corpus alone. Held for researcher decision at Phase 12 closure gate. Remain in cluster; verses where any exist route to BOUNDARY. Members: ademoneo, thambos, za.a.vah, ke.ra, mish.bar, a.qah, sha.vats, sar.ap.pim, ta.mah, sham.mah, a.ruts, pa.lats."),
]

# ===== Term placements =====
# (mti_id, primary_subgroup, [secondary_subgroups])  — secondary is added for multi-faceted
# Order: alphabetical by strongs for stability
TERM_PLACEMENTS = [
    # ----- Single-sub-group terms (§4 of AI's design, modulo §3 dual-listings) -----
    # M01-A primaries (with no secondaries beyond what §3 details)
    (270, "M01-A", []),   # H4172A mo.rah
    (271, "M01-A", []),   # H4172B mo.ra
    (273, "M01-F", []),   # H4034 me.go.rah — AI §4 lists as M01-F primary
    (272, "M01-F", []),   # H4035 me.gu.rah — AI §4 lists as M01-F primary
    (263, "M01-A", []),   # H6345 pach.dah
    (704, "M01-A", []),   # G6015 deos
    # M01-B primaries (single-sg)
    (16, "M01-B", []),    # G1568 ekthambeo
    (5126, "M01-B", []),  # G1569 ekthambos
    (283, "M01-B", []),   # G1630 ekfobos
    (257, "M01-B", []),   # G1719 emfobos
    (1690, "M01-B", []),  # G4422 ptoeō
    (267, "M01-B", []),   # G4423 ptoēsis
    (1692, "M01-B", []),  # G4426 pturomai
    (294, "M01-B", []),   # H1763 de.chal
    (1734, "M01-B", []),  # H2119B za.chal
    (297, "M01-B", []),   # H7297 ra.hah
    (107, "M01-F", []),   # H1674 de.a.gah — AI §4 lists primary M01-F (not B as some §3 text says)
    (1733, "M01-B", []),  # H8429 te.vah
    (276, "M01-B", []),   # H3016 ya.gor — §4 lists primary M01-B
    # M01-C primaries (single-sg)
    (1156, "M01-C", []),  # H1091 bal.la.hah
    (1154, "M01-C", []),  # H1205 be.a.tah
    (1157, "M01-C", []),  # H2283 chag.ga
    (1723, "M01-C", []),  # H2844A chat
    (1155, "M01-C", []),  # H2847 chit.tah
    (1729, "M01-C", []),  # H2849 chat.chat
    (1151, "M01-C", []),  # H2851 chit.tit
    (1730, "M01-C", []),  # H2866 cha.tat-terror
    (286, "M01-C", []),   # H4032 ma.gor
    (1152, "M01-C", []),  # H4288 me.chit.tah
    (1776, "M01-C", []),  # H4637 ma.a.ra.tsah
    (1720, "M01-C", []),  # H8606 tiph.le.tset
    (1722, "M01-C", []),  # H0366 a.yom — AI §3 says "No secondary placement needed — all three verses fit C"
    # M01-D primaries (single-sg)
    (5187, "M01-D", []),  # H0927 be.hal
    (703, "M01-D", []),   # H2865 cha.tat (to be dismayed)
    (1158, "M01-D", []),  # H2113 ze.va.ah
    (1732, "M01-D", []),  # H8541 tim.ma.hon
    (279, "M01-D", []),   # H7374 re.tet (panic)
    # M01-E primaries (single-sg)
    (310, "M01-E", []),   # H2730 cha.red
    (307, "M01-E", []),   # G1790 entromos
    (308, "M01-E", []),   # G5156 tromos — §4 lists single M01-E
    (1792, "M01-E", []),  # H7461A ra.ad-noun
    (311, "M01-E", []),   # H7461B re.a.dah
    (1793, "M01-E", []),  # H7460 ra.ad-verb
    (1576, "M01-E", []),  # H7268 rag.gaz
    (1577, "M01-E", []),  # H7269 rog.zah
    (282, "M01-E", []),   # H6427 pal.la.tsut
    (1744, "M01-E", []),  # H8175A sa.ar (verb)
    (1746, "M01-E", []),  # H8178A sa.ar (noun)
    (306, "M01-E", []),   # H6206 a.rats
    (1713, "M01-E", []),  # H7578 re.tet (trembling)
    # M01-F primaries (single-sg)
    (274, "M01-F", []),   # G5398 foberos
    (296, "M01-F", []),   # H3025 ya.gor
    # M01-G primaries (single-sg)
    (288, "M01-G", []),   # G1167 deilia
    (261, "M01-G", []),   # G1168 deiliaō
    (1701, "M01-G", []),  # G1169 deilos

    # ----- Multi-faceted terms (§3 of AI's design) -----
    (292, "M01-A", ["M01-B", "M01-F", "M01-G"]),   # G5399 fobeō
    (266, "M01-A", ["M01-B", "M01-C", "M01-F"]),   # G5401 fobos
    (298, "M01-A", ["M01-B"]),                      # H3372G ya.re-revere
    (1682, "M01-A", ["M01-B"]),                     # H3372H ya.re-revere — AI omitted detail; default same pattern as 298
    (1681, "M01-A", ["M01-B"]),                     # H3373 ya.re-afraid
    (829, "M01-A", ["M01-B", "M01-C", "M01-F"]),    # H6343 pa.chad-noun (split primary; using A as nominal primary)
    (291, "M01-F", ["M01-A", "M01-B"]),             # H6342 pa.chad-verb
    (269, "M01-A", ["M01-C", "M01-F"]),             # H3374 yir.ah
    (305, "M01-E", ["M01-B", "M01-D"]),             # H2729 cha.rad
    (92, "M01-D", ["M01-B"]),                       # H0926 ba.hal
    (309, "M01-E", ["M01-D", "M01-G"]),             # H2731 cha.ra.dah
    (1554, "M01-E", ["M01-D", "M01-B"]),            # H7264 ra.gaz
    (290, "M01-A", ["M01-B"]),                      # H1481C gur
    (284, "M01-C", ["M01-B"]),                      # H0367 e.mah

    # ----- BOUNDARY terms -----
    (2, "M01-BOUNDARY", []),     # G0085 ademoneo
    (1245, "M01-BOUNDARY", []),  # G2285 thambos
    (1162, "M01-BOUNDARY", []),  # H2189 za.a.vah
    (152, "M01-BOUNDARY", []),   # H3735 ke.ra
    (4814, "M01-BOUNDARY", []),  # H4867 mish.bar
    (5157, "M01-BOUNDARY", []),  # H6125 a.qah
    (240, "M01-BOUNDARY", []),   # H7661 sha.vats
    (349, "M01-BOUNDARY", []),   # H8312 sar.ap.pim
    (289, "M01-BOUNDARY", []),   # H8539 ta.mah
    (1161, "M01-BOUNDARY", []),  # H8047G sham.mah
    (1777, "M01-BOUNDARY", []),  # H6178 a.ruts
    (1719, "M01-BOUNDARY", []),  # H6426 pa.lats
]

# ===== Per-verse cross-listings (overrides for term-primary mechanical routing) =====
# {mti_id: {reference: target_subgroup}}
# Used when a multi-faceted term's specific verse routes to a non-primary sub-group.
CROSS_LISTINGS: dict[int, dict[str, str]] = {
    # --- G5399 fobeō (mti=292) — primary A, secondaries B / F / G ---
    292: {ref: sg for ref, sg in [
        ("Mat 1:20","M01-B"),("Mat 2:22","M01-B"),("Mat 10:26","M01-B"),("Mat 10:28","M01-B"),
        ("Mat 10:31","M01-B"),("Mat 14:5","M01-B"),("Mat 14:27","M01-B"),("Mat 14:30","M01-B"),
        ("Mat 17:6","M01-B"),("Mat 17:7","M01-B"),("Mat 21:26","M01-B"),("Mat 21:46","M01-B"),
        ("Mat 25:25","M01-G"),("Mat 27:54","M01-B"),("Mat 28:5","M01-B"),("Mat 28:10","M01-B"),
        ("Mar 4:41","M01-B"),("Mar 5:15","M01-B"),("Mar 5:33","M01-B"),("Mar 5:36","M01-B"),
        ("Mar 6:20","M01-A"),("Mar 6:50","M01-B"),("Mar 9:32","M01-B"),("Mar 10:32","M01-B"),
        ("Mar 11:18","M01-B"),("Mar 11:32","M01-B"),("Mar 12:12","M01-B"),("Mar 16:8","M01-B"),
        ("Luk 1:13","M01-B"),("Luk 1:30","M01-B"),("Luk 2:9","M01-B"),("Luk 2:10","M01-B"),
        ("Luk 5:10","M01-B"),("Luk 8:25","M01-B"),("Luk 8:35","M01-B"),("Luk 8:50","M01-B"),
        ("Luk 9:34","M01-B"),("Luk 9:45","M01-B"),("Luk 12:4","M01-B"),("Luk 12:7","M01-B"),
        ("Luk 12:32","M01-F"),("Luk 18:2","M01-A"),("Luk 18:4","M01-A"),("Luk 19:21","M01-G"),
        ("Luk 20:19","M01-B"),("Luk 22:2","M01-B"),("Luk 23:40","M01-A"),
        ("Joh 6:19","M01-B"),("Joh 6:20","M01-B"),("Joh 9:22","M01-B"),("Joh 12:15","M01-B"),
        ("Joh 19:8","M01-B"),("Act 5:26","M01-B"),("Act 9:26","M01-B"),
        ("2Cor 11:3","M01-F"),("2Cor 12:20","M01-F"),("Gal 2:12","M01-B"),("Gal 4:11","M01-F"),
        ("Heb 4:1","M01-F"),("Heb 11:23","M01-B"),("Heb 11:27","M01-B"),("Heb 13:6","M01-B"),
        ("1Jo 4:18","M01-F"),("Rev 1:17","M01-B"),("Rev 2:10","M01-B"),
    ]},
    # --- G5401 fobos (mti=266) — primary A, secondaries B / C / F ---
    266: {ref: sg for ref, sg in [
        # B (acute alarm)
        ("Mat 14:26","M01-B"),("Mat 28:4","M01-B"),("Mat 28:8","M01-B"),("Mar 4:41","M01-B"),
        ("Luk 1:12","M01-B"),("Luk 1:65","M01-B"),("Luk 5:26","M01-B"),("Luk 7:16","M01-B"),
        ("Luk 8:37","M01-B"),("Luk 21:26","M01-B"),("Joh 7:13","M01-B"),("Joh 19:38","M01-B"),
        ("Joh 20:19","M01-B"),("Rev 11:11","M01-B"),("Rev 18:10","M01-B"),("Rev 18:15","M01-B"),
        # C (terror as ordering force)
        ("Rom 13:3","M01-C"),
        # F (anticipatory)
        ("Heb 2:15","M01-F"),("2Cor 7:5","M01-F"),
    ]},
    # --- H3372G ya.re-revere (mti=298) — primary A; AI listed B verses below ---
    298: {ref: "M01-B" for ref in [
        "Gen 3:10","Gen 15:1","Gen 18:15","Gen 19:30","Gen 20:8","Gen 21:17","Gen 26:7","Gen 26:24",
        "Gen 31:31","Gen 32:7","Gen 35:17","Gen 42:35","Gen 43:18","Gen 43:23","Gen 46:3","Gen 50:19",
        "Gen 50:21","Exo 2:14","Exo 14:10","Exo 14:13","Exo 34:30","Num 12:8","Num 14:9","Num 21:34",
        "Deu 1:21","Deu 1:29","Deu 2:4","Deu 3:2","Deu 3:22","Deu 5:5","Deu 7:18","Deu 20:1",
        "Deu 31:6","Deu 31:8","Jos 8:1","Jos 9:24","Jos 10:2","Jos 10:8","Jos 10:25","Jos 11:6",
        "Judg 4:18","Judg 6:23","Judg 6:27","Judg 8:20","Rut 3:11","1Sa 3:15","1Sa 4:7","1Sa 4:20",
        "1Sa 7:7","1Sa 12:20","1Sa 14:26","1Sa 15:24","1Sa 17:11","1Sa 17:24","1Sa 18:12","1Sa 18:29",
        "1Sa 21:12","1Sa 22:23","1Sa 23:17","1Sa 28:5","1Sa 28:13","1Sa 28:20","1Sa 31:4","2Sa 1:14",
        "2Sa 3:11","2Sa 6:9","2Sa 9:7","2Sa 10:19","2Sa 12:18","2Sa 13:28","2Sa 14:15","1Ki 1:50",
        "1Ki 1:51","1Ki 17:13","2Ki 1:15","2Ki 6:16","2Ki 10:4","2Ki 19:6","2Ki 25:24","Neh 2:2",
        "Neh 4:14","Neh 6:9","Neh 6:13","Neh 6:14","Neh 6:19","Job 5:21","Job 5:22","Job 6:21",
        "Job 9:35","Job 11:15","Job 32:6","Psa 3:6","Psa 23:4","Psa 27:3","Psa 46:2","Psa 49:5",
        "Psa 49:16","Psa 56:3","Psa 56:4","Psa 56:11","Psa 64:4","Psa 91:5","Psa 112:7","Psa 112:8",
        "Psa 118:6","Isa 7:4","Isa 8:12","Isa 10:24","Isa 35:4","Isa 37:6","Isa 40:9","Isa 41:5",
        "Isa 41:10","Isa 41:13","Isa 41:14","Isa 43:1","Isa 43:5","Isa 44:2","Isa 51:7","Isa 51:12",
        "Isa 54:4","Isa 54:14","Jer 1:8","Jer 10:5","Jer 23:4","Jer 30:10","Jer 40:9","Jer 41:18",
        "Jer 42:11","Jer 46:27","Jer 46:28","Jer 51:46","Lam 3:57","Eze 2:6","Eze 3:9","Eze 11:8",
        "Dan 10:12","Dan 10:19","Joe 2:21","Joe 2:22","Jon 1:5","Jon 1:10","Hab 1:7","Zep 3:15",
        "Zep 3:16","Hag 2:5","Zec 8:13","Zec 8:15","Zec 9:5","Mal 4:5",
    ]},
    # --- H3373 ya.re-afraid (mti=1681) — primary A; AI listed B verses ---
    1681: {ref: "M01-B" for ref in [
        "Gen 32:11","Deu 7:19","Deu 20:8","Judg 7:3","Judg 7:10","1Sa 23:3","2Ki 17:32","2Ki 17:33",
        "2Ki 17:34","2Ki 17:35","2Ki 17:36","2Ki 17:37","2Ki 17:38","2Ki 17:39","2Ki 17:40","2Ki 17:41",
        "Jer 42:11","Jer 42:16","Dan 1:10","Jon 1:9",
    ]},
    # --- H6343 pa.chad-noun (mti=829) — split primary A/C, secondaries B/F ---
    # A (divine-name / reverential): default primary; explicit cross-listings below
    829: {ref: sg for ref, sg in [
        # C (terror as overwhelming force)
        ("Exo 15:16","M01-C"),("Deu 2:25","M01-C"),("Deu 11:25","M01-C"),("1Sa 11:7","M01-C"),
        ("1Ch 14:17","M01-C"),("2Ch 14:14","M01-C"),("2Ch 17:10","M01-C"),("2Ch 20:29","M01-C"),
        ("Est 8:17","M01-C"),("Est 9:2","M01-C"),("Est 9:3","M01-C"),("Psa 105:38","M01-C"),
        ("Isa 2:10","M01-C"),("Isa 2:19","M01-C"),("Isa 2:21","M01-C"),("Jer 49:5","M01-C"),
        # B (acute alarm)
        ("Psa 14:5","M01-B"),("Psa 53:5","M01-B"),("Psa 31:11","M01-B"),("Job 13:11","M01-B"),
        ("Job 15:21","M01-B"),("Job 22:10","M01-B"),("Job 39:22","M01-B"),("Pro 1:26","M01-B"),
        ("Pro 1:27","M01-B"),("Pro 1:33","M01-B"),("Pro 3:25","M01-B"),("Song 3:8","M01-B"),
        ("Isa 33:14","M01-B"),("Isa 44:8","M01-B"),("Isa 44:11","M01-B"),("Jer 30:5","M01-B"),
        ("Jer 36:16","M01-B"),("Jer 36:24","M01-B"),("Jer 48:43","M01-B"),("Jer 48:44","M01-B"),
        ("Jer 33:9","M01-B"),("Lam 3:47","M01-B"),("Psa 64:1","M01-B"),("Psa 91:5","M01-B"),
        # F (anticipatory)
        ("Deu 28:67","M01-F"),("Job 3:25","M01-F"),("Job 4:14","M01-F"),("Job 23:15","M01-F"),
        ("Pro 3:24","M01-F"),("Isa 24:17","M01-F"),("Isa 24:18","M01-F"),("Isa 51:13","M01-F"),
        ("Psa 78:53","M01-F"),("Isa 60:5","M01-F"),
    ]},
    # --- H6342 pa.chad-verb (mti=291) — primary F, secondaries A / B ---
    291: {ref: sg for ref, sg in [
        # A (reverential)
        ("Psa 119:161","M01-A"),("Pro 28:14","M01-A"),("Isa 33:14","M01-A"),("Hos 3:5","M01-A"),
        # B (acute alarm)
        ("Psa 14:5","M01-B"),("Psa 27:1","M01-B"),("Psa 53:5","M01-B"),("Psa 78:53","M01-B"),
        ("Isa 19:17","M01-B"),("Isa 44:8","M01-B"),("Isa 44:11","M01-B"),("Jer 33:9","M01-B"),
        ("Jer 36:16","M01-B"),("Jer 36:24","M01-B"),("Jer 30:5","M01-B"),("Mic 7:17","M01-B"),
        ("Isa 60:5","M01-B"),
    ]},
    # --- H3374 yir.ah (mti=269) — primary A, secondaries C / F ---
    269: {ref: sg for ref, sg in [
        ("Deu 2:25","M01-C"),("Eze 30:13","M01-C"),
        ("Psa 55:5","M01-F"),("Jon 1:10","M01-F"),("Jon 1:16","M01-F"),
    ]},
    # --- H2729 cha.rad (mti=305) — primary E, secondaries B / D ---
    305: {ref: sg for ref, sg in [
        ("Gen 42:28","M01-B"),("Rut 3:8","M01-B"),("1Sa 13:7","M01-B"),("1Sa 16:4","M01-B"),
        ("1Sa 21:1","M01-B"),("1Sa 28:5","M01-B"),("2Sa 17:2","M01-B"),("1Ki 1:49","M01-B"),
        ("Judg 8:12","M01-D"),("1Sa 14:15","M01-D"),
    ]},
    # --- H0926 ba.hal (mti=92) — primary D, secondary B ---
    92: {ref: "M01-B" for ref in ["Gen 45:3","Exo 15:15","1Sa 28:21"]},
    # --- H2731 cha.ra.dah (mti=309) — primary E, secondaries D / G ---
    309: {ref: sg for ref, sg in [
        ("1Sa 14:15","M01-D"),
        ("Pro 29:25","M01-G"),
    ]},
    # --- H7264 ra.gaz (mti=1554) — primary E, secondaries D / B ---
    1554: {ref: sg for ref, sg in [
        ("1Sa 28:15","M01-D"),("2Sa 18:33","M01-D"),("Psa 4:4","M01-D"),("Isa 14:9","M01-D"),
        ("Isa 14:16","M01-D"),
        ("2Sa 7:10","M01-B"),("1Ch 17:9","M01-B"),
    ]},
    # --- H1481C gur (mti=290) — primary A, secondary B ---
    290: {ref: "M01-B" for ref in [
        "Num 22:3","Deu 1:17","Deu 18:22","Job 19:29","Job 41:25","Hos 10:5",
    ]},
    # --- H0367 e.mah (mti=284) — primary C, secondary B ---
    284: {ref: "M01-B" for ref in ["Gen 15:12","Ezr 3:3"]},
}


def main():
    dry_run = "--dry-run" in sys.argv

    # Backup
    if not dry_run:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP_DIR / f"bible_research_backup_{ts}_DIR-20260516-002.db"
        shutil.copy2(DB, backup_path)
        print(f"[BACKUP] {backup_path.name}")

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    counts = {"cluster_subgroup_inserts": 0, "mti_term_subgroup_inserts": 0,
              "vc_updates_mechanical": 0, "vc_updates_overrides": 0,
              "vc_unrouted_set_aside": 0, "missing_vc_for_override": 0}

    try:
        conn.execute("BEGIN")

        # Pre-conditions
        n_active = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M01' AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        if n_active != 81:
            raise RuntimeError(f"Pre-condition fail: M01 active terms = {n_active}, expected 81")
        n_sg_existing = conn.execute(
            "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M01' AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        if n_sg_existing != 0:
            raise RuntimeError(f"Pre-condition fail: M01 has {n_sg_existing} active sub-groups; expected 0")

        # Op A0 — Rename soft-deleted M01 cluster_subgroup rows to free up canonical codes
        # The UNIQUE constraint on (cluster_code, subgroup_code) applies regardless of delete_flagged.
        # DIR-20260515-002 created M01-A..M01-H + M01-BOUNDARY which were soft-deleted by the reset
        # script. Append a rename suffix so the new design's sub-groups can use the canonical codes.
        rc_rename = conn.execute("""
            UPDATE cluster_subgroup
            SET subgroup_code = subgroup_code || '_reset_v2_0_rerun_20260516',
                last_updated_date=?
            WHERE cluster_code='M01' AND delete_flagged=1
              AND subgroup_code NOT LIKE '%_reset_v2_0_rerun_%'
        """, (now,)).rowcount
        print(f"  [A0] Renamed {rc_rename} soft-deleted M01 sub-group codes to free up canonical codes")

        # Op A — Create cluster_subgroup rows
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

        # Op B — Insert mti_term_subgroup rows
        all_term_placements = []
        for mti, primary, secondaries in TERM_PLACEMENTS:
            all_term_placements.append((mti, primary, "primary"))
            for sec in secondaries:
                all_term_placements.append((mti, sec, "secondary"))

        for mti, sg_code, role in all_term_placements:
            sg_id = sg_id_map[sg_code]
            note = f"{DIRECTIVE} [{role}]: per AI WA-M01-subgroup-design-v1-20260516"
            conn.execute(
                """INSERT INTO mti_term_subgroup
                   (mti_term_id, cluster_subgroup_id, placement_note,
                    delete_flagged, created_at, last_updated_date)
                   VALUES (?, ?, ?, 0, ?, ?)""",
                (mti, sg_id, note, now, now)
            )
            counts["mti_term_subgroup_inserts"] += 1

        # Op C — Update verse_context.cluster_subgroup_id
        term_primary = {mti: primary for mti, primary, _ in TERM_PLACEMENTS}
        active_vc = list(conn.execute("""
            SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id, vc.is_relevant,
                   vr.reference
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code='M01' AND mt.status IN ('extracted','extracted_thin')
              AND COALESCE(mt.delete_flagged,0)=0 AND COALESCE(vc.delete_flagged,0)=0
        """))

        for vc in active_vc:
            mti = vc["mti_term_id"]
            ref = vc["reference"]
            override = CROSS_LISTINGS.get(mti, {}).get(ref)
            target_sg_code = override if override else term_primary.get(mti)
            if not target_sg_code:
                # Unaccounted — should not happen for any M01 active term
                continue
            target_sg_id = sg_id_map[target_sg_code]
            rc = conn.execute(
                """UPDATE verse_context SET cluster_subgroup_id=?
                   WHERE id=? AND COALESCE(delete_flagged,0)=0""",
                (target_sg_id, vc["vc_id"])
            ).rowcount
            if rc == 1:
                if override:
                    counts["vc_updates_overrides"] += 1
                else:
                    counts["vc_updates_mechanical"] += 1

        # Validate: every cross-listing's reference resolved against an actual vc row
        for mti, refs in CROSS_LISTINGS.items():
            for ref, sg in refs.items():
                n = conn.execute("""
                    SELECT COUNT(*) FROM verse_context vc
                    JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                    WHERE vc.mti_term_id=? AND vr.reference=? AND COALESCE(vc.delete_flagged,0)=0
                """, (mti, ref)).fetchone()[0]
                if n == 0:
                    counts["missing_vc_for_override"] += 1
                    print(f"  WARN: cross-listing mti={mti} ref={ref!r} → {sg} found no matching vc row")

        # Post-check: all is_relevant vc routed
        unrouted = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code='M01' AND mt.status IN ('extracted','extracted_thin')
              AND COALESCE(mt.delete_flagged,0)=0 AND vc.is_relevant=1
              AND vc.cluster_subgroup_id IS NULL AND COALESCE(vc.delete_flagged,0)=0
        """).fetchone()[0]
        if unrouted > 0:
            raise RuntimeError(f"Post-check fail: {unrouted} is_relevant vc rows unrouted")

        # H4 check: vc.cluster_subgroup_id set but term has no mti_term_subgroup link
        h4 = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            LEFT JOIN mti_term_subgroup mts
                ON mts.mti_term_id = vc.mti_term_id
                AND mts.cluster_subgroup_id = vc.cluster_subgroup_id
                AND COALESCE(mts.delete_flagged,0)=0
            WHERE mt.cluster_code='M01' AND vc.cluster_subgroup_id IS NOT NULL
              AND COALESCE(vc.delete_flagged,0)=0 AND mts.id IS NULL
        """).fetchone()[0]
        if h4 > 0:
            raise RuntimeError(f"H4 violations after apply: {h4}")

        if dry_run:
            conn.execute("ROLLBACK")
            print("\n[DRY RUN] Rolled back.")
        else:
            conn.execute("COMMIT")
            print("\nCommitted.")
        for k, v in counts.items():
            print(f"  {k}: {v}")

    except Exception as exc:
        conn.execute("ROLLBACK")
        print(f"\nERROR: {exc}\nRolled back.")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
