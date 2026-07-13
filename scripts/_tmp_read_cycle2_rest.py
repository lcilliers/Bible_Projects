"""Build the remaining cycle-2 passage readings (Pro 1:24 - 2:3) via _pro_read_lib.
Each passage authored in isolation; writes one JSON per passage. Emergent chars noted."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pro_read_lib import Reading, IB, GOD, PER

# ---- P3 Pro 1:24 — Wisdom called; they refused, none heeded ----
r = Reading(1, "P3715 (Pro 1:24) — the ground of judgement: Wisdom called, they refused to listen, none heeded.")
r.ch(264754,"called (qara)","calling — Wisdom's persistent public appeal","action","Wisdom","calling out and being rejected","those who refused","welded to their refusal to listen",IB,"qara again (cf 1:21): the appeal that judgement will answer; here stated as spurned.")
r.ch(264755,"refused (maen)","to refuse — the will's outright rejection of the call","volition","those addressed","refusing to listen to Wisdom's call","Wisdom's call","the human counter to the calling — will set against appeal",IB,"maen = flat refusal of the will; the decisive act that grounds 1:26's judgement. Read at full weight.",coupling_to=264754)
r.ch(264760,"heeded (qashab)","to heed/pay-attention — here NONE heeded","action","no one","the attentive heeding that was wholly absent","Wisdom's outstretched hand","paired with the refusal; attention withheld",IB,"qashab (attend) negated: not merely refusing words but ignoring the outstretched hand. Non-attention as culpable posture.")
r.write("p3715-1_24")

# ---- P4 Pro 1:25 — ignored counsel, would have none of reproof ----
r = Reading(1, "P3716 (Pro 1:25) — 'you have ignored all my counsel and would have none of my reproof.' avah(will) refuses; counsel is its object (qualifier).")
r.ch(264764,"would have none / be willing (avah)","the will — here refusing all of Wisdom's counsel","volition","those addressed","the will setting itself against counsel and reproof, wanting none of it","Wisdom's counsel (etsah)","the will's refusal binds to the counsel it spurns",IB,"avah (the will) recurs (cf 1:10 'do not consent'): here the will actively wants NONE of wisdom's counsel. counsel(264763) is its rejected object.",target_to=264763)
r.write("p3716-1_25")

# ---- P5 Pro 1:26-27 — Wisdom's answering mockery; terror/distress/anguish ----
r = Reading(1, "P3717 (Pro 1:26-27) — Wisdom's retributive laughter/mockery; the dread that overtakes. distress(tsarah) EMERGENT.")
r.ch(264771,"mock (laag)","to mock/deride — Wisdom's answering derision at their calamity","affect","Wisdom","mocking when their dreaded terror strikes","those who refused","the just recoil of their scorn: Wisdom laughs as they once scoffed",IB,"laag pairs with 'I will laugh': Wisdom's mockery is the measured answer to the scoffers' delight (1:22) — scorn returned for scorn.")
r.ch(264772,"terror (pachad)","dread/terror — the sudden fear that overtakes them","affect","those who refused","the terror that strikes them in their calamity","their calamity","welded to the calamity/storm that triggers it",IB,"pachad = the seizing dread; first of two occurrences in 1:27.")
r.ch(264774,"terror (pachad)","dread/terror — likened to a storm sweeping in","affect","those who refused","terror bearing down like a storm","the whirlwind of calamity","coupled to the storm-image intensifying it",IB,"distinct second pachad (1:27b): the dread now given its simile (storm/whirlwind) — the same fear, its violence stressed.",manner="storm-like, overwhelming")
r.ch(264780,"distress (tsarah)","distress — the straitness/anguish that comes upon them","affect","those who refused","distress coming upon the one who spurned wisdom","anguish (tsuqah)","paired with anguish as the twin closing terror",IB,"EMERGENT (seed-missed): tsarah = constriction/distress, paired with tsuqah; the inner narrowing that judgement brings.")
r.ch(264781,"anguish (tsuqah)","anguish — crushing pressure of the inner life","affect","those who refused","anguish overtaking them alongside distress","distress (tsarah)","the twin of distress; the pair names the whole weight",IB,"tsuqah (pressure/anguish) closes the terror-sequence; distinct from tsarah though paired — the crushing that follows the constriction.",coupling_to=264780)
r.write("p3717-1_26-27")

# ---- P6 Pro 1:28 — too-late calling and seeking ----
r = Reading(1, "P3718 (Pro 1:28) — the reversal: now THEY call and seek, too late.")
r.ch(264784,"call (qara)","calling — the desperate, too-late appeal to Wisdom","action","those who refused","calling upon Wisdom when it is too late for answer","Wisdom (who will not answer)","the mirror of 1:24: the appeal now runs the other way, unanswered",IB,"qara reversed: those who spurned Wisdom's call now call her — but 'I will not answer'. The calling is real but forfeited.")
r.ch(264787,"seek diligently (shachar)","to seek earnestly/at dawn — the frantic late search","action","those who refused","seeking Wisdom diligently yet not finding","Wisdom (who will not be found)","welded to the futility: earnest search, no finding",IB,"shachar (seek early/earnestly) — the intensity of the too-late search underscores that the door has closed; earnestness cannot undo the prior refusal.")
r.write("p3718-1_28")

# ---- P7 Pro 1:29 — hated knowledge, did not choose the fear ----
r = Reading(1, "P3719 (Pro 1:29) — the root cause named: hated knowledge, did not choose the fear of the LORD.")
r.ch(264792,"hated (sane)","to hate — their aversion to knowledge","affect","those who refused","hating knowledge, the settled aversion behind the refusal","knowledge (daat)","the fool's defining hatred (cf 1:22)",IB,"sane recurs (1:22): here given as the ROOT reason for the coming judgement — knowledge was not missed but hated.",target_to=264793)
r.ch(264793,"knowledge (daat)","knowledge — the good they hated","cognition","those who refused","knowledge as the hated object","","the target of their hatred",IB,"daat, the fruit of the fear of God (1:7), was the very thing they hated. Two-axes with hate's target.")
r.ch(264795,"choose (bachar)","to choose/elect — here NOT chosen","volition","those who refused","the will declining to choose the fear of the LORD","the fear of the LORD","the will's refusal parallel to the hatred: they would not elect reverence",IB,"bachar (elect) negated: the fear of God was set before them and NOT chosen — reverence is here a matter of the will's election, refused.",target_to=264796)
r.ch(264796,"the fear of the LORD (yirah)","reverent fear of God — what they refused to choose","affect","those who refused","the reverence they declined to elect","the LORD","paired with knowledge: the twin goods refused",IB,"yirah (cf 1:7) here as the object NOT chosen — the beginning of knowledge, deliberately passed over. God the target; the fear the human interior.")
r.write("p3719-1_29")

# ---- P8 Pro 1:30 — none of counsel, despised reproof ----
r = Reading(1, "P3720 (Pro 1:30) — 'would have none of my counsel and despised all my reproof.'")
r.ch(264805,"would / be willing (avah)","the will — refusing all counsel","volition","those who refused","the will wanting none of Wisdom's counsel","counsel (etsah)","the will bound against the counsel it spurns",IB,"avah recurs (cf 1:25): the refusing will, now paired with active contempt for reproof.",target_to=264807)
r.ch(264808,"despised (naats)","to spurn/despise — active contempt for reproof","affect","those who refused","despising all of Wisdom's reproof","Wisdom's reproof","the contempt that hardens the refusal",IB,"naats (spurn) is heavier than avah's refusal: not just declining counsel but DESPISING correction — the scoffer's posture (cf buz 1:7).")
r.write("p3720-1_30")

# ---- P9 Pro 1:31 — sated with their own devices ----
r = Reading(1, "P3721 (Pro 1:31) — the retribution: they eat the fruit of their way, sated with their own devices.")
r.ch(264816,"have their fill (saba)","satiation — glutted, ironically, on the fruit of their own way","state","those who refused","being filled to satiety with the results of their own schemes","their own devices (moetsah)","the ironic coupling: appetite met by consequence",IB,"saba (be sated) turned to judgement: the fullness they get is the harvest of their devices — desire answered by its own fruit.",target_to=264817)
r.write("p3721-1_31")

# ---- P10 Pro 1:32 — simple killed by turning; complacency of fools ----
r = Reading(1, "P3722 (Pro 1:32) — the simple's turning-away kills them; the complacency of fools destroys. complacency(shalvah) EMERGENT.")
r.ch(308243,"simple (peti)","the simple — killed by their own turning away","state","the simple","the naive whose backsliding is fatal to them","their turning away (meshubah)","the simple-state welded to the apostasy that kills it",IB,"peti (cf 1:22) now under judgement: the naivety that is loved (1:22) here kills, via its turning.")
r.ch(308245,"turning away (meshubah)","apostasy/backsliding — the turn that kills the simple","disposition","the simple","the turning-away from wisdom that brings death","the simple it destroys","the fatal movement of the naive heart away from wisdom",IB,"meshubah (turning-back/apostasy) is the DRIVER of the simple's death — a settled turning, not a slip. (This is H4878, onboarded Stage 2.)")
r.ch(308246,"complacency (shalvah)","complacency/false ease — the security that destroys fools","state","fools (kesil)","the careless ease of fools that destroys them","the fools it destroys","the fool's false security welded to his destruction",IB,"EMERGENT (seed-missed): shalvah = careless ease/complacency — the fool's fatal calm, set opposite the true security of 1:33 (betach). A key contrast the read surfaces.")
r.ch(308247,"fools (kesil)","fools — destroyed by their complacency","disposition","the fool","the fool whose complacency is his ruin","complacency (shalvah)","welded to the complacency that destroys him",IB,"kesil (cf 1:22): here defined by a fatal ease — the fool is undone not by storm but by his own untroubled carelessness.")
r.write("p3722-1_32")

# ---- P11 Pro 1:33 — whoever listens: secure, at ease, no dread ----
r = Reading(1, "P3723 (Pro 1:33) — the promise to the listener: dwell secure, at ease, without dread. True security vs the fool's complacency.")
r.ch(264818,"listens (shama)","listening — the receptive attention that inherits safety","action","whoever listens","heeding Wisdom and thereby dwelling secure","Wisdom's call","the positive counterpart to 1:24's refusal: listening yields security",IB,"shama here the SAVING posture, opposite the refusal/non-heeding of 1:24-25 — the one act that changes the outcome.")
r.ch(264820,"secure (betach)","security — safe, trustful dwelling","state","whoever listens","dwelling in safety as the fruit of listening","","the reward of heeding; genuine security",IB,"betach = grounded safety/trust — the TRUE security set against the fool's shalvah (1:32): one saves, the other destroys.")
r.ch(264821,"at ease (shaan)","ease/untroubledness — quiet rest of the inner life","state","whoever listens","being at ease, undisturbed","dread of disaster (absent)","paired with security; the settled calm of the wise",IB,"shaan (be at ease/quiet) — the inner tranquillity of the one who heeds; distinct from complacency in that it rests on having listened, not on carelessness.")
r.ch(264823,"dread (pachad)","dread — here ABSENT: without dread of disaster","affect","whoever listens","the fear of calamity that the listener does NOT feel","disaster (ra)","the dread negated; its object (disaster) held off",IB,"pachad (cf 1:26-27, where it seizes the refuser) here NEGATED for the listener: the same terror that overtakes the fool is absent from the one who heeded. The contrast is exact.",target_to=264824)
r.write("p3723-1_33")

# ---- P12 Pro 2:2-3 — bending ear/heart, calling out for insight ----
r = Reading(2, "P3724 (Pro 2:2-3) — the conditions of gaining wisdom: attentive ear, inclined heart, voice raised for insight/understanding.")
r.ch(266998,"attentive (qashab)","attentiveness — making the ear strain toward wisdom","action","the seeker","bending the ear attentively toward wisdom","wisdom (chokmah)","the deliberate turning of attention that seeking requires",IB,"qashab (make attentive) is the first CONDITION-operation: wisdom is not received passively but by an ear made to strain — the effortful attention the whole ch.2 protasis builds on.",target_to=266999)
r.ch(266999,"wisdom (chokmah)","wisdom — what the attentive ear is bent toward","disposition","the seeker","wisdom as the object the ear strains after","","the goal of the bent ear",IB,"chokmah as the target of active listening (qashab); the seeking of wisdom requires the ear's deliberate turn.")
r.ch(267001,"heart (leb)","the heart — the inner faculty inclined toward understanding","seat","the seeker","inclining/stretching the heart toward understanding","understanding (tebunah)","the heart as the organ that must be bent, not just the ear",IB,"leb here is the SEAT actively 'inclined' (natah) — wisdom is sought not only by the ear (attention) but by turning the whole inner faculty. A rare explicit seat-as-actor.",target_to=267002)
r.ch(267002,"understanding (tebunah)","understanding — toward which the heart inclines","cognition","the seeker","understanding as the heart's aim","","the object of the inclined heart",IB,"tebunah (discernment) as the heart's target; first of two occurrences in 2:2-3.")
r.ch(267025,"call out (qara)","calling out — crying aloud for insight","action","the seeker","raising the voice, calling out for insight as for a treasure","insight (binah)","the vocal, urgent seeking that matches the bent ear and heart",IB,"qara here is the seeker's cry (contrast Wisdom's qara, 1:20-24): the search for understanding becomes a loud, urgent calling-out — desire made vocal.",target_to=267026)
r.ch(267026,"insight (binah)","insight — cried out for aloud","cognition","the seeker","insight sought by raising the voice, called for like a treasure","","the object of the vocal seeking",IB,"binah as the thing 'called out for' — the search for understanding is vocal, urgent, like crying for help (2:3).")
r.ch(267031,"understanding (tebunah)","understanding — for which the voice is raised","cognition","the seeker","understanding sought by lifting the voice","","the aim of the raised voice",IB,"distinct second tebunah (2:3): understanding now the object of the raised voice — the seeking intensifies from bent ear to lifted cry.")
r.write("p3724-2_2-3")
print("\nAll remaining cycle-2 passages built.")
