"""One-shot builder for M11's unified VCG creation JSON.

Reads the 5 per-sub-group meanings reports, the VCG assignments hardcoded here
(matching the design markdown files), and writes the unified JSON for Phase C.4.

This is intentionally a one-shot per-cluster script — under v3_0 a parametric
builder would generalise, but for the M11 test the explicit assignment table
is the cleanest validation.
"""
from __future__ import annotations
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "Sessions" / "Session_Clusters" / "M11" / "WA-M11-vcg-creation-v1-20260527.json"

# Format: {subgroup_code: {provisional_code: {description, verses, anchor_vc_id}}}
DATA = {
    "M11-A": {
        "M11-A-VCG-01": {
            "description": "Day of Atonement core ritual — annual high-priest atonement for self, household, sanctuary, and people in concentric circles. Includes Lev 6:30 (DoA-class sanctuary-blood atonement) and Lev 23:28 (work-cease discipline).",
            "verses": [29526, 29527, 29528, 29529, 29530, 29531, 29532, 29533, 29534, 29537, 29511],
            "anchor_vc_id": 29532,
        },
        "M11-A-VCG-02": {
            "description": "Standard Levitical sin/guilt offering → forgiveness mechanism. The canonical kip.per produces sa.lach as declared outcome. Includes hand-laying identification (Lev 1:4), blood-as-life theology (Lev 17:11), iniquity-bearing role of sin offering (Lev 10:17), and unintentional-sin sub-pattern.",
            "verses": [29501, 29493, 29502, 29503, 29504, 29505, 29506, 29507, 29508, 29509, 29510, 29512, 29513, 29515, 29492, 29536, 29538, 29543, 29544],
            "anchor_vc_id": 29493,
        },
        "M11-A-VCG-03": {
            "description": "Cleansing-atonement (ritual defilement removed) — childbirth, skin disease, bodily discharges, corpse contact. Distinct from VCG-02 because the precondition is defilement rather than transgression. M10c cross-register.",
            "verses": [29516, 29517, 29518, 29519, 29520, 29521, 29522, 29523, 29524, 29525, 29539],
            "anchor_vc_id": 29520,
        },
        "M11-A-VCG-04": {
            "description": "Priestly preparation / self-atonement / ordination — the mediator must first be cleansed before cleansing others. Includes half-shekel ransom (Exo 30:15/16) and Levite-as-protective-barrier role.",
            "verses": [29498, 29499, 29500, 29514, 29540, 29541, 29542],
            "anchor_vc_id": 29514,
        },
        "M11-A-VCG-05": {
            "description": "Crisis / intercessory / wrath-averting atonement — Moses post-golden-calf, Aaron's incense in plague, Phinehas's zeal, warriors' offering. Urgent mediation interposing between active wrath and its outworking.",
            "verses": [29571, 29545, 29546, 29547, 29572],
            "anchor_vc_id": 29545,
        },
        "M11-A-VCG-06": {
            "description": "National / institutional / annual atonement — Chronicles' corporate reformations, Hezekiah's restoration, second Passover, Deuteronomic land-cleansing, Ezekielian temple economics, Nehemiah's covenant offerings, festival-cycle sin offerings. Lev 16:34 (annual statute) framing.",
            "verses": [29551, 29552, 29570, 29497, 29564, 29535, 29553, 29554, 29555, 29548, 29549, 29550],
            "anchor_vc_id": 29552,
        },
        "M11-A-VCG-07": {
            "description": "Divine self-atonement (God as agent) — Psalms' divine covering, Isaianic seraph touch, eschatological cleansing, Eze 16:63 shame-producing atonement-reception. Where human resources are exhausted, God acts directly.",
            "verses": [29495, 29557, 29556, 29565, 29562, 29494, 29563],
            "anchor_vc_id": 29562,
        },
        "M11-A-VCG-08": {
            "description": "Atonement denied / impossible / false-covering — the negative pole. Refused (1Sa 3:14, Isa 22:14, Jer 18:23), unable (Isa 47:11), self-deception exposed (Isa 28:18).",
            "verses": [29559, 29560, 29569, 29561, 29568],
            "anchor_vc_id": 29560,
        },
        "M11-A-VCG-09": {
            "description": "Inner moral disposition / interpersonal appeasement — atonement outside the priestly frame. Pro 16:6 inner-character mechanism, Pro 16:14 wisdom-defusing-wrath, Gen 32:20 calculated gift, 2Sa 21:3 bloodguilt reparations.",
            "verses": [29567, 29496, 29566, 29558],
            "anchor_vc_id": 29558,
        },
        "M11-A-VCG-10": {
            "description": "Christic atoning surrender — Jesus voluntarily releases his spirit (Mat 27:50) and grants disciples free passage in self-substitution (Joh 18:8). G0863I afiēmi-permit verses routed to M11-A by atonement-register content per B.2 §3.3.",
            "verses": [17641, 17636],
            "anchor_vc_id": 17641,
        },
    },
    "M11-B": {
        "M11-B-VCG-01": {
            "description": "NT direct declarations of forgiveness on faith — Jesus pronounces sins forgiven into the inner person, paralytic + sinful woman corpus, Son-of-Man authority demonstrated against scribal challenges, Joh 20:23 delegation.",
            "verses": [17589, 17590, 17591, 17592, 17595, 17596, 17597, 17598, 17601, 17602, 17603, 17604, 17605, 17606, 17609],
            "anchor_vc_id": 17605,
        },
        "M11-B-VCG-02": {
            "description": "Reciprocal / conditional forgiveness — forgive-as-forgiven Lord's-Prayer pattern, unforgiving-servant parable, Luk 17 repeated repentance/forgiveness instruction.",
            "verses": [17615, 17616, 17617, 17618, 17619, 17620, 17621, 17622, 17623, 17624, 17625],
            "anchor_vc_id": 17616,
        },
        "M11-B-VCG-03": {
            "description": "Repentance / turning unlocks divine pardon — Mar 4:12, Jer 36:3, Isa 55:7, 2Ch 7:14, Act 8:22.",
            "verses": [17600, 17610, 17672, 17675, 17689],
            "anchor_vc_id": 17689,
        },
        "M11-B-VCG-04": {
            "description": "Forgiveness foreclosed / unforgivable / withheld — blasphemy against the Spirit, national-scale unforgiveness (2Ki 24:4, Deu 29:20, Jer 5:1/7, Lam 3:42).",
            "verses": [17593, 17594, 17607, 17668, 17670, 17673, 17674, 17676],
            "anchor_vc_id": 17593,
        },
        "M11-B-VCG-05": {
            "description": "Levitical atonement → forgiveness arc (sa.lach as kip.per outcome) — Lev 4–7, 19:22, Num 15. M11-A-VCG-02 ↔ M11-B-VCG-05 same verses from outcome side.",
            "verses": [17648, 17649, 17650, 17651, 17652, 17653, 17654, 17655, 17656, 17657, 17658, 17659, 17660],
            "anchor_vc_id": 17648,
        },
        "M11-B-VCG-06": {
            "description": "Solomon's temple-prayer corpus — canonical OT corporate forgiveness petition (1Ki 8 + 2Ch 6).",
            "verses": [17679, 17680, 17681, 17682, 17683, 17684, 17685, 17686, 17687, 17688],
            "anchor_vc_id": 17679,
        },
        "M11-B-VCG-07": {
            "description": "Intercession-driven forgiveness — Moses, prophets, apostolic, christic. Includes 2Ki 5:18 preemptive Naaman pardon and confession-driving variants (1Jo 1:9, Jam 5:15).",
            "verses": [17608, 17612, 17613, 17661, 17662, 17663, 17664, 17669, 17677, 17691],
            "anchor_vc_id": 17662,
        },
        "M11-B-VCG-08": {
            "description": "Forgiveness as divine character attribute — God IS forgiving (Psa 86:5, Neh 9:17, Dan 9:9, Psa 130:4, Psa 103:3, Psa 25:11).",
            "verses": [17671, 17690, 17693, 17694, 17695, 17696],
            "anchor_vc_id": 17693,
        },
        "M11-B-VCG-09": {
            "description": "New covenant / total pardon / abundance — sin remembered no more (Jer 31:34), guilt unfindable (Jer 50:20), already-forgiven assurance (1Jo 2:12), blessedness of forgiven (Rom 4:7), all sins forgivable (Mar 3:28).",
            "verses": [17599, 17611, 17614, 17678, 17692],
            "anchor_vc_id": 17678,
        },
        "M11-B-VCG-10": {
            "description": "Vow nullification forgiveness — Num 30:5/8/12. Father/husband nullifies vow → God forgives the binding-obligation guilt.",
            "verses": [17665, 17666, 17667],
            "anchor_vc_id": 17665,
        },
    },
    "M11-C": {
        "M11-C-VCG-01": {
            "description": "NT divine release-of-sin proclamation — afesis as central forgiveness-of-sins noun in NT proclamation, plus exaleifō sin-erasure (Act 3:19, Col 2:14) and Luk 4:18 captivity-liberation.",
            "verses": [17507, 17508, 17509, 17510, 17511, 17512, 17513, 17514, 17515, 17516, 17517, 17518, 17519, 17521, 17522, 2266, 2268],
            "anchor_vc_id": 17508,
        },
        "M11-C-VCG-02": {
            "description": "Release foreclosed — Mar 3:29 blasphemy against the Spirit. Parallels M11-B-VCG-04 and M11-A-VCG-08 in content.",
            "verses": [17520],
            "anchor_vc_id": 17520,
        },
        "M11-C-VCG-03": {
            "description": "Discipleship-call leaving — G0863G volitional detachment for following. Non-M11-primary register (M30/M29) per Phase 3; co-located in M11-C by term-lexical association.",
            "verses": [17523, 17524, 17525, 17526, 17527, 17528, 17529, 17530, 17531, 17532, 17533, 17534, 17535],
            "anchor_vc_id": 17529,
        },
        "M11-C-VCG-04": {
            "description": "Reconciliation-prioritizing release / bond maintained — M11-primary G0863G. Mat 5:24 leave-gift-to-reconcile, 1Cor 7:11–13 do-not-abandon-spouse, Heb 6:1 leave-rudimentary-to-advance, Joh 8:29 Father-has-not-left-Son.",
            "verses": [17542, 17543, 17544, 17545, 17548, 17549],
            "anchor_vc_id": 17545,
        },
        "M11-C-VCG-05": {
            "description": "Loyalty failure / abandonment of bond — disciples flee (Mar 14:50, Mat 26:56), hired hand abandons sheep (Joh 10:12), religious leaders abandon command (Mar 7:8), weightier matters neglected (Mat 23:23), first love abandoned (Rev 2:4).",
            "verses": [17536, 17537, 17538, 17539, 17540, 17541],
            "anchor_vc_id": 17536,
        },
        "M11-C-VCG-06": {
            "description": "Eschatological separation — one-taken-one-left (Mat 24:40/41, Luk 17:34/35), house-forsaken (Luk 13:35). M38 cross-register per Phase 3.",
            "verses": [17550, 17551, 17552, 17553, 17554],
            "anchor_vc_id": 17550,
        },
        "M11-C-VCG-07": {
            "description": "Volitional release for care / mission priority — leave blind guides (Mat 15:14), leave ninety-nine for one (Mat 18:12).",
            "verses": [17546, 17547],
            "anchor_vc_id": 17547,
        },
        "M11-C-VCG-08": {
            "description": "Permission granted / welcoming openness — children permitted (Mat 19:14, Mar 10:14, Luk 18:16), permission for righteousness (Mat 3:15), non-resistance generosity (Mat 5:40), Gamaliel non-interference (Act 5:38).",
            "verses": [17626, 17627, 17628, 17630, 17635, 17637],
            "anchor_vc_id": 17626,
        },
        "M11-C-VCG-09": {
            "description": "Permission withheld / blocking / authority restraining — kingdom blocked (Mat 23:13), temple guarded (Mar 11:16), demons silenced (Mar 1:34), companionship withheld (Mar 5:19), tradition-blocks-duty (Mar 7:12), priority sequencing (Mar 7:27), ironic permission (Luk 6:42, Mat 7:4), burial refused (Rev 11:9), nature abandoned (Rom 1:27).",
            "verses": [17629, 17631, 17632, 17633, 17634, 17638, 17639, 17640, 17642, 17643],
            "anchor_vc_id": 17638,
        },
        "M11-C-VCG-10": {
            "description": "Eschatological tear-wiping — exaleifō downstream restoration outcome (Rev 7:17, Rev 21:4). M03/M04 cross-register per Phase 3.",
            "verses": [2267, 2269],
            "anchor_vc_id": 2267,
        },
    },
    "M11-D": {
        "M11-D-VCG-01": {
            "description": "Divine relenting in response to intercession — Moses at Sinai (Exo 32:12/14), Amos's prophetic intercession (Amo 7:3/6).",
            "verses": [30737, 30744, 30765, 30766],
            "anchor_vc_id": 30737,
        },
        "M11-D-VCG-02": {
            "description": "Divine relenting triggered by human turning — Jonah/Nineveh, Jeremianic conditional mercy, David's census, Joel's character-grounded relenting, Jer 42:10.",
            "verses": [30738, 30749, 30750, 30756, 30758, 30759, 30760, 30761, 30763, 30764, 30767, 30768],
            "anchor_vc_id": 30738,
        },
        "M11-D-VCG-03": {
            "description": "Divine refusal to relent / judgment fixed — 1Sa 15:29 Glory-of-Israel constancy, Num 23:19 parallel, Psa 110:4 oath, Eze 24:14, Jer 4:28, Jer 15:6 (exhausted), Isa 57:6, Zec 8:14.",
            "verses": [30745, 30747, 30752, 30753, 30754, 30755, 30762, 30769],
            "anchor_vc_id": 30747,
        },
        "M11-D-VCG-04": {
            "description": "Divine grief / sorrow over human failure — Gen 6:6/7 grief over creation, 1Sa 15:11/35 grief over Saul. M03 cross-register per Phase 3.",
            "verses": [30742, 30743, 30746, 30748],
            "anchor_vc_id": 30742,
        },
        "M11-D-VCG-05": {
            "description": "Conditional relenting / covenant memory — Jer 18:10 (good withheld for disobedience), Psa 106:45 (covenant remembered drives relenting).",
            "verses": [30751, 30757],
            "anchor_vc_id": 30751,
        },
        "M11-D-VCG-06": {
            "description": "Human contrition / self-reproach — Job 42:6 dust-and-ashes, Jer 31:19 Ephraim post-turning shame.",
            "verses": [30736, 30741],
            "anchor_vc_id": 30736,
        },
        "M11-D-VCG-07": {
            "description": "Negative human relenting — inappropriate (Exo 13:17 resolve-collapse, M20 cross-register) or absent (Jer 8:6 no one relents).",
            "verses": [30739, 30740],
            "anchor_vc_id": 30740,
        },
        "M11-D-VCG-08": {
            "description": "Inner heart-turning and memory-recall (shuv repentance) — Solomon exile-prayer, Deuteronomic recall, Isaianic transgressor address, Lam 3:21 recall-to-hope pivot.",
            "verses": [35024, 35025, 35026, 35027, 35028, 35029, 35030],
            "anchor_vc_id": 35027,
        },
        "M11-D-VCG-09": {
            "description": "Marginal: faithfulness-under-pressure (ud Psa 119:61) — structural-opposite STAYS verdict per Phase 3 §6.3.2; flagged for Phase D T6 awareness.",
            "verses": [40564],
            "anchor_vc_id": 40564,
        },
    },
    "M11-E": {
        "M11-E-VCG-01": {
            "description": "Cosmic / theological reconciliation through Christ's death — Col 1:20 cosmic restoration, Col 1:22 blameless purpose, Eph 2:16 enmity killed, Rom 5:10 enmity-while-still-enemies.",
            "verses": [37232, 62945, 62946, 62947],
            "anchor_vc_id": 62946,
        },
        "M11-E-VCG-02": {
            "description": "Ministry-of-reconciliation appeal — 2Cor 5:18 divine initiative + ministry entrusted; 5:19 not counting trespasses; 5:20 ambassadorial appeal.",
            "verses": [37234, 37235, 37236],
            "anchor_vc_id": 37234,
        },
        "M11-E-VCG-03": {
            "description": "Interpersonal marital reconciliation — 1Cor 7:11 separated spouse's proper aim. M44 cross-register per Phase 3.",
            "verses": [37233],
            "anchor_vc_id": 37233,
        },
        "M11-E-VCG-04": {
            "description": "Israel-rejection paradox — Rom 11:15 (apobolē): loss as mechanism by which reconciliation extends to the world. M10 cross-register per Phase 3.",
            "verses": [35726],
            "anchor_vc_id": 35726,
        },
    },
}


def main() -> int:
    # Sanity: count
    total = 0
    for sg, vcgs in DATA.items():
        sg_total = sum(len(v["verses"]) for v in vcgs.values())
        print(f"  {sg}: {len(vcgs)} VCGs, {sg_total} verses")
        total += sg_total
    print(f"Total across cluster: {total} verses")

    OUT.write_text(json.dumps(DATA, indent=2), encoding="utf-8")
    print(f"\nWrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
