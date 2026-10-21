"""Build cycle-3 passage readings (Pro 2:4 - 2:20) via _pro_read_lib. Each in isolation."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pro_read_lib import Reading, IB, GOD, PER

# P1 2:4
r = Reading(2, "P3725 (Pro 2:4) — seek wisdom like silver, search as for hidden treasure.")
r.ch(267033,"seek (baqash)","seeking — searching for wisdom as for silver/hidden treasure","action","the seeker","seeking wisdom with the intensity of a treasure-hunt","wisdom (implied)","welded to the treasure-image: the search is costly, deliberate, prized",IB,"baqash raises the seeking of 2:2-3 to its peak: wisdom pursued like buried silver — the effort that the whole ch.2 promise turns on.",manner="intense, treasure-seeking")
r.write("p3725-2_4")

# P2 2:5-6
r = Reading(2, "P3726 (Pro 2:5-6) — then you understand the fear of the LORD; the LORD gives wisdom, knowledge, understanding.")
r.ch(267039,"understand (bin)","understanding — grasping the fear of the LORD as the fruit of seeking","cognition","the seeker","coming to understand the fear of the LORD","the fear of the LORD","the payoff of the search: understanding opens onto reverence",IB,"bin here yields not data but the fear of God — understanding terminates in reverence (inverting 1:7: fear begins knowledge, knowledge deepens fear).",target_to=267040)
r.ch(267040,"the fear of the LORD (yirah)","reverent fear of God — what the seeker comes to understand","affect","the seeker","the reverence gained by the one who seeks wisdom","the LORD","paired with the knowledge of God","internal:ib-state","yirah as the SUMMIT of the search (cf 1:7 as its beginning) — God the target, the fear the human interior.")
r.ch(267043,"knowledge of God (daat)","knowledge — the knowing of God found by the seeker","cognition","the seeker","finding the knowledge of God","God","coupled to the fear of the LORD as its twin","internal:ib-state","daat-elohim: knowing God, paired with fearing him — the two faces of the seeker's reward.")
r.ch(267048,"wisdom (chokmah)","wisdom — given by the LORD","disposition","the seeker","wisdom given by God, the source of the seeker's competence","the LORD (its giver/source)","the gift whose source is God's own mouth","internal:ib-state","chokmah's SOURCE named as God — the human good is given, not self-generated (cf the register: God = source D3).")
r.ch(267051,"knowledge (daat)","knowledge — from God's mouth","cognition","the seeker","knowledge coming from the mouth of God","God (its source)","paired with understanding as God-given","internal:ib-state","distinct daat from 267043: here the knowledge that ISSUES from God, a gift, alongside understanding.")
r.ch(267052,"understanding (tebunah)","understanding — from God's mouth","cognition","the seeker","understanding proceeding from God","God (its source)","paired with knowledge as the twin gift","internal:ib-state","tebunah given by God — the discernment the seeker sought (2:3) is finally God's to give.")
r.write("p3726-2_5-6")

# P3 2:7
r = Reading(2, "P3727 (Pro 2:7) — he stores sound wisdom for the upright; a shield to those of integrity.")
r.ch(267054,"sound wisdom (tushiyyah)","sound wisdom — the effectual competence God stores for the upright","disposition","the upright","the practical, sound wisdom God lays up for the upright","the upright who receive it","the reserve God keeps for the upright","internal:ib-state","tushiyyah = success/sound-competence, distinct from chokmah — the effective wisdom that actually works, stored as a treasure for the upright.")
r.ch(267055,"upright (yashar)","uprightness — the straight of heart for whom wisdom is stored","disposition","the upright","the upright for whom sound wisdom is reserved","sound wisdom (stored for them)","paired with integrity in the next line","internal:ib-state","yashar (straight/upright) — the moral condition that qualifies one for the stored wisdom; the character God rewards.")
r.ch(267058,"integrity (tom)","integrity — the wholeness of those God shields","disposition","those who walk in it","walking in integrity, under God's shield","God's shielding (its reward)","welded to the walk it describes","internal:ib-state","tom (completeness/integrity) — the undivided moral wholeness; those who walk in it have God as shield. Distinct from yashar (straightness): tom is wholeness, yashar is straightness.")
r.write("p3727-2_7")

# P4 2:8-9
r = Reading(2, "P3728 (Pro 2:8-9) — God guards justice and his saints; you will understand righteousness, justice, equity. watching-over(God's) qualifies saints.")
r.ch(267061,"justice (mishpat)","justice — the paths God guards","disposition","(the just order God guards)","the just order that God protects","God's guarding","the object of God's guarding","internal:ib-state","mishpat here = the paths of justice God keeps; the moral order upheld from above.")
r.ch(267064,"saints (chasid)","the faithful/pious — those God watches over","disposition","the saints","the devoted faithful whose way God watches over","God's watching-over","welded to God's protective watching","internal:ib-state","chasidim = the covenant-faithful/devout; a char of settled loyalty. God's watching-over (267062) is its qualifier — God-content guarding the pious.",coupling_to=267062)
r.ch(267065,"understand (bin)","understanding — grasping the moral goods","cognition","the seeker","coming to understand righteousness, justice, equity, every good path","righteousness/justice/equity","the discernment that opens the whole moral field","internal:ib-state","bin here yields the ETHICAL triad (cf 1:3) — understanding terminates in moral perception, not just theory.",target_to=267066)
r.ch(267066,"righteousness (tsedeq)","righteousness — first of the moral triad understood","disposition","the seeker","rightness of the person, now understood","justice/equity (the triad)","first of righteousness-justice-equity","internal:ib-state","tsedeq (cf 1:3) recurs as the object of understanding — the moral goods are not just given but grasped.")
r.ch(267067,"justice (mishpat)","justice — right judgement, understood","disposition","the seeker","just judgement grasped by the seeker","righteousness/equity","middle of the moral triad","internal:ib-state","distinct mishpat from 267061 (God's paths): here the justice the seeker comes to understand — the same good, now internalised.")
r.ch(267068,"equity (mesharim)","equity — evenness/straight dealing, understood","disposition","the seeker","even, straight dealing grasped by the seeker","righteousness/justice","closes the triad","internal:ib-state","mesharim (cf 1:3) as the third moral good understood — the level, fair dealing of the discerning.")
r.ch(267070,"good path (tob)","the good — every good course the seeker discerns","disposition","the seeker","discerning every good path","the moral triad it sums","the summation of the moral goods","internal:ib-state","tob ('every good path') gathers up the triad — the whole field of good conduct now open to the one who understands.")
r.write("p3728-2_8-9")

# P5 2:10
r = Reading(2, "P3729 (Pro 2:10) — wisdom enters the heart; knowledge pleasant to the soul.")
r.ch(266940,"wisdom (chokmah)","wisdom — entering the heart","disposition","the seeker","wisdom coming INTO the heart, taking up residence within","the heart it enters","welded to the heart it indwells","internal:ib-state","chokmah pictured as ENTERING (bo) the heart — wisdom is not external instruction but an inward guest that settles in the seat.",target_to=266942)
r.ch(266942,"heart (leb)","the heart — the seat wisdom enters","seat","the seeker","the inner seat that wisdom comes to indwell","wisdom (its guest)","the organ wisdom enters","internal:ib-state","leb as the SEAT that receives wisdom — the destination of the whole search; wisdom lodges in the heart.")
r.ch(266943,"knowledge (daat)","knowledge — pleasant to the soul","cognition","the seeker","knowledge become sweet/pleasant to the inner self","the soul it delights","welded to the soul's pleasure in it","internal:ib-state","daat here not merely possessed but ENJOYED — knowledge becomes pleasant, an affective good, not a burden.",target_to=266945)
r.ch(266944,"pleasant (naem)","pleasantness — knowledge's sweetness to the soul","affect","the seeker","knowledge being pleasant/sweet to the soul","the soul that finds it sweet","the affective bond between knowledge and the self","internal:ib-state","naem (be pleasant/sweet) — the read surfaces that wisdom's goal is not grim duty but DELIGHT: knowledge pleasing the nephesh.")
r.ch(266945,"soul (nephesh)","the soul — the self to which knowledge is sweet","seat","the seeker","the inner self that finds knowledge pleasant","knowledge (its delight)","the seat of the pleasure in knowledge","internal:ib-state","nephesh as the seat of ENJOYMENT here (cf 1:18-19 where it was forfeited) — the self savouring knowledge; the whole inner person delighting.")
r.write("p3729-2_10")

# P6 2:11
r = Reading(2, "P3730 (Pro 2:11) — discretion watches over you; understanding guards. watch-over qualifies discretion.")
r.ch(266946,"discretion (mezimmah)","discretion — shrewd forethought that guards the person","disposition","the one it guards","discretion keeping watch over the person, warding off danger","its watching-over (266947)","welded to its protective watching","internal:ib-state","mezimmah (cf 1:4, positive) now PERSONIFIED as a guardian — the same shrewdness that could scheme here stands sentinel over the one who has it.",coupling_to=266947)
r.ch(266948,"understanding (tebunah)","understanding — that guards the person","disposition","the one it guards","understanding standing guard over the person","its guarding function","paired with discretion as twin protectors","internal:ib-state","tebunah paired with mezimmah as inner GUARDIANS — the moral goods actively defend the one who has taken them in (2:10).")
r.write("p3730-2_11")

# P7 2:12
r = Reading(2, "P3731 (Pro 2:12) — delivering you from the way of evil and perverted speech.")
r.ch(266950,"delivering (natsal)","deliverance — wisdom's rescue from the way of evil","action","wisdom/discretion (delivering); the person delivered","being delivered from the way of evil and perverse men","evil (the danger delivered from)","welded to the evil it rescues from","internal:ib-state","natsal (snatch away/deliver) — the protective goods (2:11) issue in RESCUE: wisdom actively pulls the person out of evil's way.",target_to=266952)
r.ch(266952,"evil (ra)","evil — the way from which one is delivered","disposition","the wicked","the way of evil, the danger wisdom rescues from","the deliverance opposing it","paired with perverted speech as the danger","internal:ib-state","ra (cf 1:16) as the WAY delivered-from — a whole path/manner of life, embodied in 'men of perverted speech'.")
r.ch(266955,"perverted speech (tahpukot)","perversity — the twisted speech of evil men","disposition","the wicked","the perverse, twisted things such men speak","evil (whose way it marks)","welded to the way of evil","internal:ib-state","tahpukot (perversities/things-turned-upside-down) — the crookedness of the wicked's speech; the inner distortion that marks the way of evil.")
r.write("p3731-2_12")

# P8 2:13
r = Reading(2, "P3732 (Pro 2:13) — who forsake the paths of uprightness to walk in ways of darkness.")
r.ch(266959,"uprightness (yosher)","uprightness — the straight paths the wicked forsake","disposition","the wicked (who forsake it)","the upright way abandoned for the ways of darkness","the darkness it is traded for","the good forsaken in the turn to darkness","internal:ib-state","yosher (straightness) as the good ABANDONED — the wicked's descent is an active forsaking of the straight for the dark; uprightness surfaced only as what is left behind.")
r.write("p3732-2_13")

# P9 2:14
r = Reading(2, "P3733 (Pro 2:14) — who rejoice in doing evil and delight in the perverseness of evil. Descent at full weight.")
r.ch(266964,"rejoice (sameach)","rejoicing — gladness perversely taken in doing evil","affect","the wicked","rejoicing in the doing of evil — joy fixed on wrong","evil (the object of the joy)","the perverse coupling: gladness welded to evil-doing","internal:ib-state","sameach (rejoice) at its darkest: the affect of joy turned on EVIL itself — not weakness but delight in wrong. Read at full weight.",target_to=266966)
r.ch(266966,"evil (ra)","evil — the doing in which they rejoice","disposition","the wicked","the evil deeds that are the object of their joy","the rejoicing fixed on it","the object of perverse gladness","internal:ib-state","ra as the object of rejoicing — evil not merely done but ENJOYED.")
r.ch(266967,"delight (gil)","delight — exultation in the perverseness of evil","affect","the wicked","exulting/delighting in evil's perversity","perverseness (the object)","the second perverse affect, paired with rejoicing","internal:ib-state","gil (exult/spin-with-joy) intensifies sameach: not just gladness but exultant delight in perversity — the affect doubled.",target_to=266968)
r.ch(266968,"perverseness (tahpukot)","perversity — the twistedness of evil in which they delight","disposition","the wicked","the perverse crookedness of evil that they exult in","evil (whose perversity it is)","welded to the evil it twists","internal:ib-state","tahpukot (cf 2:12) here the OBJECT of delight — the wicked exult not just in evil but in its very perversity/upside-downness.")
r.ch(266969,"evil (ra)","evil — its perverseness their delight","disposition","the wicked","the evil whose perversity they exult in","the delight fixed on its perversity","the substance of the perversity delighted in","internal:ib-state","distinct third ra of the passage (2:14): the evil whose PERVERSENESS (not just deed) is the object of exultation — the deepest point of the descent.")
r.write("p3733-2_14")

# P10 2:16
r = Reading(2, "P3734 (Pro 2:16) — you will be delivered from the forbidden woman/adulteress with smooth words.")
r.ch(308258,"delivered (natsal)","deliverance — rescue from the forbidden woman","action","the person delivered","being delivered from the adulteress and her smooth words","the seductress delivered from","the rescue wisdom works against seduction","internal:ib-state","natsal (cf 2:12) now aimed at the second great danger — the forbidden woman; wisdom's deliverance extends from the way of evil (men) to seduction (the adulteress).")
r.write("p3734-2_16")

# P11 2:17
r = Reading(2, "P3735 (Pro 2:17) — she forsakes the companion of her youth and forgets the covenant of her God. forgets->covenant qualifier.")
r.ch(266979,"forgets (shakach)","forgetting — the adulteress's forgetting of the covenant of her God","affect","the adulteress","forgetting the covenant of her God — a culpable letting-slip of sacred bond","the covenant (266980)","welded to the covenant it lets fall","internal:ib-state","shakach (forget) here is not mere lapse but MORAL forgetting — the sacred covenant deliberately let slip; the inner root of her betrayal.",target_to=266980)
r.write("p3735-2_17")

# P12 2:20
r = Reading(2, "P3736 (Pro 2:20) — so you will walk in the way of the good and keep to the paths of the righteous.")
r.ch(267006,"the good (tob)","the good — the way the wise walk","disposition","the wise/delivered","walking in the way of good people","the walk it describes","paired with the righteous","internal:ib-state","tob (the good ones/good way) — the positive outcome: deliverance from evil issues in walking WITH the good.")
r.ch(267007,"keep (shamar)","keeping — holding to the paths of the righteous","action","the wise/delivered","keeping/guarding one's steps to the righteous paths","the paths of the righteous","welded to the righteous way it holds to","internal:ib-state","shamar (keep/guard) read as a characteristic — the vigilant holding-to the right way; the active adherence that completes the deliverance (contrast the wicked's forsaking, 2:13).",target_to=267009)
r.ch(267009,"the righteous (tsaddiq)","the righteous — whose paths one keeps to","disposition","the righteous","the righteous whose paths the wise hold to","the keeping fixed on them","the company the wise keep","internal:ib-state","tsaddiq (the righteous) as the goal-company — the delivered walk in and hold to the way of the righteous; the chapter closes on belonging to the good.")
r.write("p3736-2_20")
print("\nCycle 3 built.")
