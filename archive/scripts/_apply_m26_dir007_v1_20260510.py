"""_apply_m26_dir007_v1_20260510.py — DB-modifying.

Apply DIR-M26-20260510-007 (M26-BOUNDARY → A1/A2/G reallocation).

Operations (single transaction, foreign_keys=ON):

  Phase 1 — Update descriptions on 21 existing vcgs
  Phase 2 — Reassign 108 vc rows from M26-BOUNDARY to destination
            sub-group + vcg (+ clear is_anchor on moved rows)
  Phase 2b — Auto-absorb vcg_term for new cross-term placements
  Phase 3 — Verification

Conflicts in the directive (4 vr_ids listed under 2 destinations);
resolved via first-occurrence-wins:
  25203 → M26-A2-012 (also listed in 950-002)
  95978 → M26-A2-003 (also listed in M26-G special)
  28747 → 950-001    (also listed in M26-A1-007)
  96015 → M26-A2-013 (also listed in M26-A1-004)

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
#  Phase 1 — 21 vcg description updates
# ══════════════════════════════════════════════════════════════════════
DESCRIPTIONS = [
    ("M26-A2-001", (
        "Term names righteousness as a governing quality whose presence "
        "produces measurable outcomes — deliverance from death, "
        "stability of the way, sure reward, honour, enduring legacy, "
        "and ultimately peace, quietness, and trust (Isa 32:17). "
        "Righteousness is not described here as a disposition to be "
        "cultivated but as a quality already operative whose "
        "consequences are stated. Its outcomes extend from the "
        "immediate (life over death, house standing, city rejoicing) "
        "to the eschatological (crown of righteousness awarded by the "
        "righteous judge, 2Ti 4:8). Contrasted consistently with "
        "wickedness whose outcomes are death and captivity."
    )),
    ("M26-A2-002", (
        "Term names righteousness as a dynamic personal standing — "
        "conditional, forfeitable, and non-transferable. In Deuteronomy, "
        "it is promised as the outcome of careful obedience (6:25), "
        "making it explicitly contingent on performance. In Ezekiel, "
        "the standing can be forfeited by turning to injustice, and "
        "none of the prior righteous deeds are then remembered (Eze "
        "33:13); conversely, the wicked who turns receives life. "
        "Righteousness here is non-accumulative — assessed at the "
        "moment of turning, not across a lifetime. Qohelet adds the "
        "sobering observation that even the righteous person may "
        "perish in his righteousness (Ecc 7:15): the standing does not "
        "guarantee protection in the present order. This is the OT's "
        "most developed and unsettling treatment of the inner mechanics "
        "of righteousness."
    )),
    ("M26-A2-003", (
        "Term names the failure, distortion, or counterfeit form of "
        "righteousness across a wide range of expressions: righteous "
        "deeds that are polluted and cannot stand before God (Isa "
        "64:6); swearing in God's name but without righteousness (Isa "
        "48:1); outward seeking without inner reality (Isa 58:2); "
        "righteousness claimed as the basis for divine favour but three "
        "times explicitly denied (Deu 9:4, 5, 6); righteousness "
        "perverted at national scale — justice turned to wormwood, the "
        "fruit of righteousness turned to poison (Amo 5:7, 6:12); "
        "wickedness occupying the institutional place assigned to "
        "righteousness (Ecc 3:16, 5:8); building and ruling by "
        "unrighteousness (Jer 22:13); law-righteousness pursued but "
        "never reached (Rom 9:31); counterfeit servants disguising "
        "themselves as servants of righteousness (2Cor 11:15); "
        "self-assessed righteousness producing contempt (Luk 18:9); "
        "outward appearance concealing inner lawlessness (Mat 23:28). "
        "Together these verses define what genuine righteousness is by "
        "documenting everything it is not."
    )),
    ("M26-A2-004", (
        "Term names the condition of being far from or lacking "
        "righteousness — in the person, the community, and the public "
        "sphere. The distance has inner causes: stubbornness of heart "
        "(Isa 46:12) and the failure of truth in public life (Isa "
        "59:9). The absence is experienced as darkness, as the failure "
        "of justice, as the departure of something that once was "
        "present: righteousness lodged in the faithful city, and now "
        "murderers are there (Isa 1:21). It is turned back from public "
        "squares and cannot enter the gates (Isa 59:14); no one enters "
        "suit justly (Isa 59:4). The condition is both personal and "
        "institutional — the individual who is far from righteousness "
        "and the society from which righteousness has been driven out. "
        "An OT parallel to the NT declaration of universal absence "
        "(Rom 3:10), but expressed as particular conditions rather "
        "than a universal category."
    )),
    ("M26-A2-006", (
        "Term names righteousness as the object of active inner "
        "longing and deliberate pursuit — hungered for, thirsted for, "
        "fled toward (Mat 5:6, 1Ti 6:11, 2Ti 2:22). The righteous "
        "person is defined by the direction of inner desire. The "
        "degree of righteousness matters (exceeding the scribes and "
        "Pharisees, Mat 5:20). Pursuit is commanded, implying the "
        "state is not yet fully arrived at but is the defining goal of "
        "the inner person. Beyond pursuit, righteousness is also a "
        "skill that must be developed: the person who lives on milk is "
        "unskilled in the word of righteousness (Heb 5:13), implying "
        "that maturity and practice produce competence in "
        "righteousness. The state is sought, and it is also formed."
    )),
    ("M26-A2-007", (
        "Term names righteousness as a generative quality — something "
        "sown, grown, harvested, and multiplied. The agricultural "
        "image is most precise: sow for yourselves righteousness and "
        "reap steadfast love (Hos 10:12) — righteousness as seed "
        "produces a different and greater harvest. The fruit of light "
        "is found in all that is good and right and true (Eph 5:9) — "
        "righteousness is what light produces in those who walk in it. "
        "The fruit of righteousness comes through Jesus Christ, to the "
        "glory and praise of God (Phili 1:11), and the harvest of "
        "righteousness increases when God multiplies the sower's seed "
        "(2Cor 9:10). Righteousness is not static possession but "
        "active production."
    )),
    ("M26-A2-008", (
        "Term names righteousness as the defining constitution of the "
        "new self in Christ. The new self is created after the "
        "likeness of God in true righteousness and holiness (Eph "
        "4:24). Righteousness is worn as a breastplate — protective, "
        "constant, part of the person's standing equipment (Eph 6:14). "
        "Most radically: God made Christ to be sin so that in him we "
        "might become the righteousness of God (2Cor 5:21) — the "
        "person is not merely covered by righteousness or credited "
        "with it, but constituted as the righteousness of God in "
        "Christ. These verses describe righteousness not as something "
        "to be pursued but as something already constitutive of the "
        "new identity in Christ, reaching its fullest expression in "
        "the identification of the person with God's own righteous "
        "character."
    )),
    ("M26-A2-009", (
        "Term names righteousness as something worn — it clothes, "
        "covers, and accompanies the person as an enveloping identity. "
        "Job put on righteousness and it clothed him; his justice was "
        "like a robe and turban (Job 29:14) — total coverage from head "
        "to body. Priests are to be clothed with righteousness (Psa "
        "132:9) — those who serve before God are defined by wearing "
        "it. Paul commends the weapons of righteousness for the right "
        "hand and for the left (2Cor 6:7) — righteousness as active "
        "defensive and offensive equipment. Righteousness goes before "
        "the person and the glory of the Lord follows as rear guard "
        "(Isa 58:8) — righteousness as protective escort. The imagery "
        "conveys that righteousness is not one quality among others "
        "but the defining covering of the whole person's presence, "
        "identity, and movement."
    )),
    ("M26-A2-011", (
        "Term names righteousness as a governing inner orientation "
        "expressed through speech and discernment. The interior "
        "dimension is primary: the heart ponders how to answer (Pro "
        "15:28); inner judgment of what is right precedes and governs "
        "speech (Luk 12:57; Joh 7:24 — do not judge by appearances but "
        "with right judgment). From this inner orientation, the mouth "
        "of the righteous produces life and nourishment (Pro 10:11, "
        "10:21), the tongue speaks choice silver and wisdom (Pro "
        "10:20, 10:31), the lips know what is acceptable (Pro 10:32). "
        "All the words of wisdom's mouth are righteous; there is "
        "nothing twisted or crooked in them (Pro 8:8). Truthful speech "
        "gives honest evidence (Pro 12:17); righteous lips are the "
        "delight of the king (Pro 16:13). Falsehood is hated as an "
        "inner aversion (Pro 13:5). The inner person is commanded to "
        "fill the mind with whatever is true, honourable, just, and "
        "pure (Phili 4:8) — establishing the cognitive foundation from "
        "which righteous speech flows."
    )),
    ("M26-A2-012", (
        "Term names righteousness as an inner orientation that extends "
        "outward toward others — in all relationships and at every "
        "scale. It reaches the individual: the righteous person guides "
        "the neighbour (Pro 12:26), gives generously without "
        "withholding (Pro 21:26, Psa 37:21), cares even for animals "
        "(Pro 12:10), returns good for evil (1Sa 24:17), and deals "
        "fairly toward workers — whatever is right I will give you "
        "(Mat 20:4). It reaches the family: children obey parents "
        "because this is right (Eph 6:1); the apostle feels rightly "
        "toward the community (Phili 1:7). It reaches the vulnerable: "
        "do justice and righteousness and deliver from the hand of "
        "the oppressor (Jer 22:3); the king who daily ate, drank, and "
        "did justice and righteousness — it was well with him (Jer "
        "22:15). At its fullest expression, righteousness rolls down "
        "like waters and flows as an ever-flowing stream (Amo 5:24) — "
        "not contained in isolated acts but pervading all relationships "
        "continuously. The righteous person's inner state does not "
        "rest in itself but reaches toward the needs of others at "
        "every level of human life."
    )),
    ("M26-A2-013", (
        "Term names righteousness as a state whose inner foundation "
        "produces lasting stability. The rootedness is deep: the root "
        "of the righteous will never be moved (Pro 12:3), the root "
        "bears fruit (Pro 12:12), and the righteous are established "
        "forever (Pro 10:25, 10:30). The stability is active "
        "protection: righteousness guards him whose way is blameless "
        "(Pro 13:6). When difficulty comes, the righteous falls seven "
        "times and rises again (Pro 24:16); the righteous holds to his "
        "way and grows stronger (Job 17:9); the righteous are bold as "
        "lions (Pro 28:1). Beyond endurance, the stability is divinely "
        "established: in righteousness you shall be established, you "
        "shall be far from oppression (Isa 54:14); God establishes "
        "the righteous through testing — you who test the minds and "
        "hearts (Psa 7:9). What was hidden is vindicated: God will "
        "bring forth your righteousness as the light and your justice "
        "as the noonday (Psa 37:6). The stability is not self-generated "
        "but grounded — in the person's root, in their resilience, and "
        "in God's own establishing act."
    )),
    ("M26-A2-014", (
        "Term names righteousness as a state defined by and constituted "
        "through its orientation toward God. The righteous person "
        "walks with God (Gen 6:9), lives by faith (Hab 2:4), serves "
        "God as the defining mark of their identity (Mal 3:18), keeps "
        "God's statutes faithfully (Eze 18:9), and brings offerings in "
        "righteousness (Mal 3:3). Righteousness qualifies the person "
        "to enter through the gates of the Lord (Psa 118:20) and to "
        "enter the gates of righteousness to give thanks (Psa 118:19). "
        "The covenant oath is sworn in truth, justice, and "
        "righteousness (Jer 4:2). Human righteousness is done in "
        "active response to God's coming righteousness: keep justice "
        "and do righteousness, for my salvation is near (Isa 56:1). "
        "Righteousness flows from God through the new birth: everyone "
        "who practices righteousness has been born of him (1Jo 2:29); "
        "whoever practices righteousness is righteous, as he is "
        "righteous (1Jo 3:7) — the person's righteousness corresponds "
        "to and flows from God's own. The kingdom of God is "
        "righteousness and peace and joy in the Holy Spirit (Rom "
        "14:17). Whether it is right in the sight of God to listen to "
        "you rather than to God — the God-frame is the ultimate test "
        "of what is right (Act 4:19)."
    )),
    ("M26-A2-015", (
        "Term names a recognisable community of righteous persons whose "
        "collective presence carries weight and consequences. The "
        "community is named: a congregation (Psa 1:5), a generation in "
        "whose company God dwells (Psa 14:5), a register in which one "
        "may be enrolled (Psa 69:28), a trusted circle whose rebuke is "
        "welcomed (Psa 141:5). The community carries protective power: "
        "the presence of even fifty righteous can determine the fate "
        "of a city; God will spare the whole place for their sake "
        "(Gen 18:23-26) — even down to ten. At the city level, "
        "righteousness defines communal identity: the faithful city "
        "where righteousness once lodged (Isa 1:21), the city restored "
        "and called city of righteousness (Isa 1:26), the habitation "
        "of righteousness and holy hill (Jer 31:23). The righteous "
        "nation that keeps faith may enter God's gates (Isa 26:2). In "
        "the eschatological vision, the whole people shall be "
        "righteous — they shall possess the land forever (Isa 60:21). "
        "The community of the righteous is not only a present social "
        "reality but has a destiny: from a few protecting a city in "
        "the present, to a whole people inhabiting righteousness "
        "forever."
    )),
    ("M26-A2-016", (
        "Term names the righteous person as a specific target of "
        "hostility — plotted against (Psa 37:12), watched for death "
        "(Psa 37:32), spoken against with contempt (Psa 31:18), sold "
        "for silver (Amo 2:6), afflicted by corrupt leaders (Amo "
        "5:12), deprived of justice by bribes (Isa 5:23, Pro 17:15), "
        "and killed (Lam 4:13, 2Sa 4:11). The opposition is directed "
        "precisely because the person is righteous: the wicked surround "
        "the righteous so that justice goes forth perverted (Hab 1:4); "
        "even false prophecy is used to dishearten the righteous (Eze "
        "13:22). The pattern is named and blessed by Jesus: Blessed "
        "are those who are persecuted for righteousness' sake, for "
        "theirs is the kingdom of heaven (Mat 5:10). The opposition "
        "is not incidental but structural — righteousness provokes "
        "hostility from those whose character is defined against it. "
        "The enemy of the righteous person is characterised as an "
        "enemy of all righteousness (Act 13:10): the opposition is "
        "not personal but comprehensive."
    )),
    ("950-001", (
        "Term names righteousness received through a divine crediting "
        "act — counted, reckoned, and conferred rather than earned or "
        "produced. The foundational OT instance is Abraham: he "
        "believed God, and it was counted to him as righteousness (Gen "
        "15:6), the pattern Paul unfolds in Romans 4 (4:3, 4:5, 4:9, "
        "4:11, 4:13, 4:22). The crediting pattern extends beyond faith "
        "alone: a specific act of justice toward the poor is credited "
        "as righteousness before the Lord (Deu 24:13); an act of zeal "
        "for God's honour is counted as righteousness from generation "
        "to generation forever (Psa 106:31). In the NT, the pattern "
        "reaches its definitive personal expression: not having a "
        "righteousness of my own that comes from the law, but that "
        "which comes through faith in Christ, the righteousness from "
        "God that depends on faith (Phili 3:9). Christ is the telos "
        "of the law for righteousness to everyone who believes (Rom "
        "10:4). The faith-righteousness itself speaks and invites "
        "(Rom 10:6). Righteousness received through faith is the "
        "standing conferred, not attained — granted by God on the "
        "basis of trust, not performance."
    )),
    ("950-002", (
        "Term names righteousness as a practiced, lived orientation — "
        "the daily direction of a person's conduct before God. It is "
        "not a one-time standing but a manner of life expressed in "
        "what the person does with their whole self. The members of "
        "the body are presented as instruments of righteousness (Rom "
        "6:13); the person becomes a slave of righteousness (Rom "
        "6:18) — subjecting the whole self to righteousness as a "
        "governing master — and this slavery produces progressive "
        "sanctification (Rom 6:19). The lived orientation is more "
        "acceptable to God than ritual performance: to do "
        "righteousness and justice is more acceptable to the Lord "
        "than sacrifice (Pro 21:3). It is the pattern of daily "
        "conduct: the king who ate, drank, and did justice and "
        "righteousness — it was well with him (Jer 22:15). It is "
        "formable through scripture and discipline (2Ti 3:16, Heb "
        "12:11) and can grow: Scripture produces training in "
        "righteousness, and discipline yields the peaceful fruit of "
        "righteousness to those who have been trained by it (Heb "
        "12:11). This is righteousness in its daily, bodily, "
        "progressive expression."
    )),
    ("M26-A1-002", (
        "Term names God's righteousness as expressed through his "
        "judicial acts — judgments that conform to what is right "
        "rather than to preference or power. God judges the world "
        "with righteousness (Psa 9:8), his throne gives righteous "
        "judgment (Psa 9:4), the heavens declare it (Psa 50:6), and "
        "his judgments are named just in their most severe "
        "eschatological expressions (Rev 15:3–19:2). Christ's "
        "judgment is just because it aligns with the Father's will "
        "(Joh 5:30). God's righteous rules are expressions of this "
        "judicial character (Psa 119:7, 75, 106). The law is holy "
        "and righteous and good (Rom 7:12); the commandments of God "
        "are so righteous that no other nation has statutes and "
        "rules as righteous (Deu 4:8); his testimonies are righteous "
        "forever and every righteous rule endures (Psa 119:144, "
        "160). His righteous judgment is grounded in complete "
        "knowledge: he is the one who knows the hearts of all (Act "
        "1:24, 15:8) — the judicial righteousness is not formal but "
        "penetrating. Every transgression and disobedience received a "
        "just retribution (Heb 2:2); their condemnation is just "
        "(Rom 3:8)."
    )),
    ("M26-A1-003", (
        "Term names God's righteousness as the quality that makes "
        "him reliable and faithful to his covenant people — keeping "
        "promises (Neh 9:8), betrothing in righteousness and justice "
        "(Hos 2:19), extending his righteousness across generations "
        "to those who fear him (Psa 103:17). His righteous promise "
        "is longed for (Psa 119:123); his testimonies are appointed "
        "in righteousness and faithfulness (Psa 119:138). The "
        "covenant bond itself is characterised by righteousness: 'I "
        "will be their God, in faithfulness and in righteousness' "
        "(Zec 8:8). He practices steadfast love, justice, and "
        "righteousness in the earth (Jer 9:24). In the covenant "
        "convergence, steadfast love and faithfulness meet; "
        "righteousness and peace kiss each other (Psa 85:10) — "
        "righteousness inseparable from covenant peace. The land of "
        "covenant restoration becomes a habitation of righteousness, "
        "a holy hill (Jer 31:23)."
    )),
    ("M26-A1-004", (
        "Term names God's righteousness as the basis on which he "
        "acts to save, deliver, vindicate, and redeem — the quality "
        "that makes him reliably and confidently appealable. The "
        "psalmists invoke it repeatedly as the ground of petition: "
        "'In your righteousness deliver me' (Psa 31:1, 71:2, 143:1, "
        "143:11). God's saving acts are expressions of his "
        "righteousness (1Sa 12:7). Righteousness and salvation "
        "travel inseparably (Isa 45:8, 46:13, 51:5). He vindicates "
        "the righteous by rewarding him according to his "
        "righteousness (1Ki 8:32, 2Ch 6:23); he restores to man his "
        "righteousness (Job 33:26); he brings forth righteousness as "
        "the light and justice as the noonday (Psa 37:6); justice "
        "returns to the righteous (Psa 94:15). The prayer of appeal "
        "is heard: standing before God's house and crying out — God "
        "answers for his name's sake (2Ch 20:9). In the NT, God's "
        "righteousness is the basis on which he forgives (1Jo 1:9), "
        "and the ground of the cross — where he is simultaneously "
        "just and the justifier (Rom 3:26). God gives his "
        "righteousness to his people as gift and vindication (Psa "
        "24:5, Isa 54:17)."
    )),
    ("M26-A1-006", (
        "Term names God's righteousness as the standard that exposes "
        "human unrighteousness by contrast — when God's righteousness "
        "is affirmed, human guilt and shame are simultaneously "
        "revealed. The pattern recurs throughout Scripture: 'you are "
        "righteous; we have acted wickedly' (Neh 9:33), 'you are "
        "just; we are before you in guilt' (Ezr 9:15), 'The Lord is "
        "in the right; I have rebelled against his word' (Lam 1:18), "
        "'to you belongs righteousness, but to us open shame' (Dan "
        "9:7). Human anger cannot produce God's righteousness (Jam "
        "1:20); human self-established righteousness fails to submit "
        "to it (Rom 10:3). The standard does not remain abstract: "
        "when Paul reasoned about righteousness and self-control and "
        "the coming judgment, Felix was alarmed (Act 24:25) — the "
        "standard of God's righteousness invades the conscience of "
        "those who hear it and produces alarm even in those who "
        "resist it."
    )),
    ("M26-A1-007", (
        "Term names righteousness as the defining quality of the "
        "coming Messianic figure — the Righteous One, the righteous "
        "Branch, the righteous Servant. The Servant's righteousness "
        "enables him to make many accounted righteous (Isa 53:11); "
        "the Branch is named 'The Lord is our righteousness' (Jer "
        "23:6, 33:16); the Messianic king is 'righteous and having "
        "salvation' (Zec 9:9); Christ's love of righteousness grounds "
        "his anointing (Psa 45:7, Heb 1:9); he rides out victoriously "
        "for the cause of truth and meekness and righteousness (Psa "
        "45:4). The prayer for the Messianic king's righteousness "
        "(Psa 72:2) is answered in Christ, and through the seventy "
        "weeks God brings in everlasting righteousness (Dan 9:24). "
        "Wisdom who walks in the paths of righteousness (Pro 8:20) "
        "and Melchizedek the king of righteousness (Heb 7:2) are "
        "types of this figure. In the NT, Jesus is identified as the "
        "Holy and Righteous One (Act 3:14), whose coming was "
        "betrayed (Act 7:52), who was appointed to be seen by his "
        "servant (Act 22:14). Even the Roman governor testifies to "
        "his innocence three times — I find no guilt in him (Joh "
        "18:38, 19:4, 19:6; Luk 23:4, 14, 22; Act 13:28) — the "
        "pagan authority bears triple witness to Messianic "
        "righteousness. He died 'the righteous for the unrighteous' "
        "(1Pe 3:18), is called as advocate 'Jesus Christ the "
        "righteous' (1Jo 2:1), and as the source of eternal "
        "salvation to all who obey him (Heb 5:9). He is the telos of "
        "the law for righteousness (Rom 10:4). God's righteousness "
        "does not remain external — it becomes incarnate in the "
        "Messiah and through him is extended to all who believe."
    )),
]


# ══════════════════════════════════════════════════════════════════════
#  Phase 2 — 108 verse moves: (vr_id, dest_subgroup_code, dest_vcg_code)
#  First-occurrence wins for the 4 directive conflicts.
# ══════════════════════════════════════════════════════════════════════
MOVES_RAW = [
    # → M26-A2 / M26-A2-001 (3)
    (169293, "M26-A2", "M26-A2-001"),
    (25173,  "M26-A2", "M26-A2-001"),
    (93725,  "M26-A2", "M26-A2-001"),
    # → M26-A2 / M26-A2-002 (2)
    (169255, "M26-A2", "M26-A2-002"),
    (95980,  "M26-A2", "M26-A2-002"),
    # → M26-A2 / M26-A2-003 (11)
    (169256, "M26-A2", "M26-A2-003"),
    (169257, "M26-A2", "M26-A2-003"),
    (169258, "M26-A2", "M26-A2-003"),
    (169251, "M26-A2", "M26-A2-003"),
    (169252, "M26-A2", "M26-A2-003"),
    (95978,  "M26-A2", "M26-A2-003"),  # also listed under M26-G; first wins
    (95979,  "M26-A2", "M26-A2-003"),
    (28772,  "M26-A2", "M26-A2-003"),
    (28748,  "M26-A2", "M26-A2-003"),
    (28724,  "M26-A2", "M26-A2-003"),
    (28335,  "M26-A2", "M26-A2-003"),
    # → M26-A2 / M26-A2-004 (3)
    (25193,  "M26-A2", "M26-A2-004"),
    (28309,  "M26-A2", "M26-A2-004"),
    (28329,  "M26-A2", "M26-A2-004"),
    # → M26-A2 / M26-A2-006 (1)
    (28742,  "M26-A2", "M26-A2-006"),
    # → M26-A2 / M26-A2-007 (3)
    (25168,  "M26-A2", "M26-A2-007"),
    (28307,  "M26-A2", "M26-A2-007"),
    (28732,  "M26-A2", "M26-A2-007"),
    # → M26-A2 / M26-A2-008 (1)
    (28726,  "M26-A2", "M26-A2-008"),
    # → M26-A2 / M26-A2-009 (3)
    (96005,  "M26-A2", "M26-A2-009"),
    (28357,  "M26-A2", "M26-A2-009"),
    (28328,  "M26-A2", "M26-A2-009"),
    # → M26-A2 / M26-A2-011 (6)
    (93780,  "M26-A2", "M26-A2-011"),
    (93777,  "M26-A2", "M26-A2-011"),
    (95991,  "M26-A2", "M26-A2-011"),
    (95984,  "M26-A2", "M26-A2-011"),
    (95985,  "M26-A2", "M26-A2-011"),
    (93806,  "M26-A2", "M26-A2-011"),
    # → M26-A2 / M26-A2-012 (6)
    (25204,  "M26-A2", "M26-A2-012"),
    (25203,  "M26-A2", "M26-A2-012"),  # also 950-002; first wins
    (93796,  "M26-A2", "M26-A2-012"),
    (93768,  "M26-A2", "M26-A2-012"),
    (93805,  "M26-A2", "M26-A2-012"),
    (169250, "M26-A2", "M26-A2-012"),
    # → M26-A2 / M26-A2-013 (4)
    (169285, "M26-A2", "M26-A2-013"),
    (25188,  "M26-A2", "M26-A2-013"),
    (169505, "M26-A2", "M26-A2-013"),
    (96015,  "M26-A2", "M26-A2-013"),  # also M26-A1-004; first wins
    # → M26-A2 / M26-A2-014 (10)
    (25166,  "M26-A2", "M26-A2-014"),
    (25190,  "M26-A2", "M26-A2-014"),
    (25207,  "M26-A2", "M26-A2-014"),
    (95992,  "M26-A2", "M26-A2-014"),
    (93765,  "M26-A2", "M26-A2-014"),
    (28750,  "M26-A2", "M26-A2-014"),
    (93748,  "M26-A2", "M26-A2-014"),
    (93750,  "M26-A2", "M26-A2-014"),
    (25215,  "M26-A2", "M26-A2-014"),
    (169336, "M26-A2", "M26-A2-014"),
    # → M26-A2 / M26-A2-015 (8)
    (169363, "M26-A2", "M26-A2-015"),
    (169364, "M26-A2", "M26-A2-015"),
    (169365, "M26-A2", "M26-A2-015"),
    (169366, "M26-A2", "M26-A2-015"),
    (169367, "M26-A2", "M26-A2-015"),
    (169376, "M26-A2", "M26-A2-015"),
    (169386, "M26-A2", "M26-A2-015"),
    (28310,  "M26-A2", "M26-A2-015"),
    # → M26-A2 / M26-A2-016 (2)
    (93737,  "M26-A2", "M26-A2-016"),
    (93727,  "M26-A2", "M26-A2-016"),
    # → M26-A2 / 950-001 (6)
    (25165,  "M26-A2", "950-001"),
    (169253, "M26-A2", "950-001"),
    (169298, "M26-A2", "950-001"),
    (93744,  "M26-A2", "950-001"),
    (28749,  "M26-A2", "950-001"),
    (28747,  "M26-A2", "950-001"),  # also M26-A1-007; first wins
    # → M26-A2 / 950-002 (6)  (25203 dropped — already routed above)
    (169292, "M26-A2", "950-002"),
    (28766,  "M26-A2", "950-002"),
    (28767,  "M26-A2", "950-002"),
    (28768,  "M26-A2", "950-002"),
    (28769,  "M26-A2", "950-002"),
    # → M26-A1 / M26-A1-002 (8)
    (93818,  "M26-A1", "M26-A1-002"),
    (93945,  "M26-A1", "M26-A1-002"),
    (93944,  "M26-A1", "M26-A1-002"),
    (9056,   "M26-A1", "M26-A1-002"),
    (9057,   "M26-A1", "M26-A1-002"),
    (169344, "M26-A1", "M26-A1-002"),
    (95998,  "M26-A1", "M26-A1-002"),
    (95999,  "M26-A1", "M26-A1-002"),
    # → M26-A1 / M26-A1-003 (2)
    (96030,  "M26-A1", "M26-A1-003"),
    (28336,  "M26-A1", "M26-A1-003"),
    # → M26-A1 / M26-A1-004 (5; 96015 dropped — already routed above)
    (169241, "M26-A1", "M26-A1-004"),
    (169244, "M26-A1", "M26-A1-004"),
    (25211,  "M26-A1", "M26-A1-004"),
    (96094,  "M26-A1", "M26-A1-004"),
    (146255, "M26-A1", "M26-A1-004"),
    # → M26-A1 / M26-A1-006 (1)
    (93729,  "M26-A1", "M26-A1-006"),
    # → M26-A1 / M26-A1-007 (13; 28747 dropped — already routed above)
    (3124,   "M26-A1", "M26-A1-007"),
    (3125,   "M26-A1", "M26-A1-007"),
    (3126,   "M26-A1", "M26-A1-007"),
    (3128,   "M26-A1", "M26-A1-007"),
    (3139,   "M26-A1", "M26-A1-007"),
    (3140,   "M26-A1", "M26-A1-007"),
    (3141,   "M26-A1", "M26-A1-007"),
    (3143,   "M26-A1", "M26-A1-007"),
    (96019,  "M26-A1", "M26-A1-007"),
    (96029,  "M26-A1", "M26-A1-007"),
    (28306,  "M26-A1", "M26-A1-007"),
    (28743,  "M26-A1", "M26-A1-007"),
    (169294, "M26-A1", "M26-A1-007"),
    # → M26-G / 1225-001 (1; 95978 dropped — first-wins to A2-003)
    (28727,  "M26-G",  "1225-001"),
]

# Dedup with first-occurrence-wins (already filtered above, but double-check)
seen: set = set()
MOVES = []
for vr, sg, vcg in MOVES_RAW:
    if vr in seen:
        continue
    seen.add(vr)
    MOVES.append((vr, sg, vcg))

assert len(MOVES) == 104, f"Expected 104 unique moves, got {len(MOVES)}"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, p)
    return p


def preflight(conn):
    msgs = []
    ok = True

    sg = {r[0]: r[1] for r in conn.execute(
        "SELECT subgroup_code, id FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0"
    )}
    for c in ("M26-A1", "M26-A2", "M26-G", "M26-BOUNDARY"):
        if c not in sg:
            msgs.append(f"[ERR] sub-group {c} missing")
            ok = False

    # Resolve all destination vcg codes
    dest_codes = sorted({code for _, _, code in MOVES})
    ph = ",".join("?" * len(dest_codes))
    vcg_ids = {r[0]: r[1] for r in conn.execute(
        f"SELECT group_code, id FROM verse_context_group "
        f" WHERE group_code IN ({ph}) AND COALESCE(delete_flagged,0)=0",
        dest_codes,
    )}
    missing = [c for c in dest_codes if c not in vcg_ids]
    if missing:
        msgs.append(f"[ERR] destination vcgs missing: {missing}")
        ok = False
    else:
        msgs.append(f"[ok] all {len(dest_codes)} destination vcgs resolved")

    # All description codes must exist
    desc_codes = [c for c, _ in DESCRIPTIONS]
    found_desc = {r[0]: r[1] for r in conn.execute(
        f"SELECT group_code, id FROM verse_context_group "
        f" WHERE group_code IN ({','.join('?' * len(desc_codes))}) "
        f"   AND COALESCE(delete_flagged,0)=0",
        desc_codes,
    )}
    missing_desc = [c for c in desc_codes if c not in found_desc]
    if missing_desc:
        msgs.append(f"[ERR] description-update vcgs missing: {missing_desc}")
        ok = False
    else:
        msgs.append(f"[ok] all {len(desc_codes)} description targets present")

    # Each move's vr_id must be in M26-BOUNDARY currently
    vr_ids = [v for v, _, _ in MOVES]
    ph = ",".join("?" * len(vr_ids))
    cur_state = {
        r[0]: (r[1], r[2]) for r in conn.execute(
            f"SELECT vc.verse_record_id, cs.subgroup_code, vc.id "
            f"  FROM verse_context vc "
            f"  LEFT JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id "
            f" WHERE vc.verse_record_id IN ({ph}) "
            f"   AND COALESCE(vc.delete_flagged,0)=0",
            vr_ids,
        )
    }
    not_in_boundary = []
    missing_vr = []
    for vr in vr_ids:
        if vr not in cur_state:
            missing_vr.append(vr)
        elif cur_state[vr][0] != "M26-BOUNDARY":
            not_in_boundary.append((vr, cur_state[vr][0]))
    if missing_vr:
        msgs.append(f"[ERR] {len(missing_vr)} vr_ids have no active vc "
                    f"row: {missing_vr[:10]}")
        ok = False
    if not_in_boundary:
        msgs.append(f"[WARN] {len(not_in_boundary)} vr_ids NOT in "
                    f"M26-BOUNDARY: {not_in_boundary[:10]}")
        # Don't block — they may have been moved by an earlier directive
    if not missing_vr and not not_in_boundary:
        msgs.append(f"[ok] all {len(vr_ids)} vr_ids in M26-BOUNDARY")

    n_b_pre = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
        (sg.get("M26-BOUNDARY", -1),),
    ).fetchone()[0]
    msgs.append(f"  M26-BOUNDARY active vc rows pre-apply: {n_b_pre}")

    return ok, msgs, sg, vcg_ids, found_desc


def run_apply(conn, sg, vcg_ids, found_desc):
    cur = conn.cursor()
    counts = defaultdict(int)
    ts = now_iso()

    # ─── Phase 1 — Description updates ──────────────────────────────
    print()
    print("Phase 1 — Description updates (21)")
    print("-" * 72)
    for code, desc in DESCRIPTIONS:
        rc = cur.execute(
            "UPDATE verse_context_group SET context_description=? "
            " WHERE id=?",
            (desc, found_desc[code]),
        ).rowcount
        counts["phase1_descriptions"] += rc
    print(f"  vcg descriptions updated: {counts['phase1_descriptions']}")

    # ─── Phase 2 — Verse moves ──────────────────────────────────────
    print()
    print(f"Phase 2 — Verse moves ({len(MOVES)} unique vr_ids)")
    print("-" * 72)
    for vr, dest_sg, dest_vcg in MOVES:
        rc = cur.execute(
            "UPDATE verse_context "
            "   SET cluster_subgroup_id=?, group_id=?, is_anchor=0 "
            " WHERE verse_record_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (sg[dest_sg], vcg_ids[dest_vcg], vr),
        ).rowcount
        counts["phase2_vc_moved"] += rc
    print(f"  vc rows moved: {counts['phase2_vc_moved']} / {len(MOVES)}")

    # ─── Phase 2b — Auto-absorb vcg_term ────────────────────────────
    print()
    print("Phase 2b — Auto-absorb vcg_term for cross-term placements")
    print("-" * 72)
    rc = cur.execute(
        "INSERT OR IGNORE INTO vcg_term "
        "  (vcg_id, mti_term_id, placement_note, delete_flagged, "
        "   created_at, last_updated_date) "
        "SELECT DISTINCT vc.group_id, vc.mti_term_id, "
        "       'DIR-007 absorb cross-term placement', 0, ?, ? "
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
    counts["phase2b_vcg_term_absorbed"] = rc
    print(f"  vcg_term rows absorbed: {rc}")

    return counts


def verify(conn, sg, vcg_ids):
    invariants = {}

    # Sub-group totals
    for code in ("M26-A1", "M26-A2", "M26-BOUNDARY", "M26-G"):
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
            (sg[code],),
        ).fetchone()[0]
        invariants[f"I-1: active vc rows in {code}"] = n

    # Each move's vr_id should now be in its destination
    misplaced = []
    for vr, dest_sg, dest_vcg in MOVES:
        r = conn.execute(
            "SELECT cs.subgroup_code, vcg.group_code "
            "  FROM verse_context vc "
            "  LEFT JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id "
            "  LEFT JOIN verse_context_group vcg ON vcg.id=vc.group_id "
            " WHERE vc.verse_record_id=? "
            "   AND COALESCE(vc.delete_flagged,0)=0",
            (vr,),
        ).fetchone()
        if not r:
            misplaced.append((vr, "missing"))
        elif r[0] != dest_sg or r[1] != dest_vcg:
            misplaced.append((vr, f"{r[0]}/{r[1]} expected {dest_sg}/{dest_vcg}"))
    invariants["I-2: misplaced vc rows post-apply"] = (
        misplaced if misplaced else "(none — all 104 moves landed)"
    )

    # H3 in M26 should still be 0 after auto-absorb
    n_h3 = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
         WHERE mt.cluster_code='M26'
           AND vc.group_id IS NOT NULL
           AND COALESCE(vc.delete_flagged,0)=0
           AND NOT EXISTS (
               SELECT 1 FROM vcg_term vt
                WHERE vt.vcg_id=vc.group_id
                  AND vt.mti_term_id=vc.mti_term_id
                  AND COALESCE(vt.delete_flagged,0)=0
           )
    """).fetchone()[0]
    invariants["I-3: M26 H3 violations post-apply (expect 0)"] = n_h3

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

    print("=" * 72)
    print("DIR-M26-20260510-007 apply (BOUNDARY → A1/A2/G reallocation)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print(f"  Unique moves after dedupe: {len(MOVES)} (raw: "
          f"{len(MOVES_RAW)}; conflicts dropped: 4)")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    print("PRE-FLIGHT")
    print("-" * 72)
    ok, msgs, sg, vcg_ids, found_desc = preflight(conn)
    for m in msgs:
        print(m)
    print()
    if not ok:
        print("Pre-flight failed.")
        return 1

    if args.live:
        b = take_backup("m26_dir007")
        print(f"Backup: {b}\n")

    try:
        conn.execute("BEGIN")
        counts = run_apply(conn, sg, vcg_ids, found_desc)
        print()
        print("FOREIGN-KEY CHECK")
        print("-" * 72)
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {len(fkv)}")
        print("  [ok] zero violations")
        print()
        print("VERIFICATION")
        print("-" * 72)
        invariants = verify(conn, sg, vcg_ids)
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
        print(f"\n[err] rolled back: {e}")
        raise

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:35s} {v}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
