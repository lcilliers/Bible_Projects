# M12 Deep-read — U3 Holiness & Consecration (qadosh family + holy-sacred / dedicate)

- **File:** wa-m12-deepread-u3-holiness-consecration-v1-20260623.md · **v1 · 2026-06-23 · Author:** Claude Code.
- **Cluster:** M12 (Purity, Holiness and Consecration) · **Draft unit:** U3 · **Term(s):** qadosh family — H6942G/H/I/J/K (qa.dash "to consecrate/sanctify/dedicate"), H6918H (qa.dosh, the adjective "holy"), G3741 (hosios "holy/devout"), H5144A (na.zar "to separate / abstain").
- **What this file is:** the **self-contained evidence home** that **TESTS** the U3 draft-unit hypothesis against the full per-verse evidence — (A) the grounded general read (computed mechanical signature + the consecrate-ACT vs holy-STATE test + the who-consecrates split + flags), then (B) the per-verse structured evidence (generator output, all co-terms). **Evidence only; no synthesis. Re-assigns NOTHING** (no ownership fixes, no DB writes, no merges) — records what the evidence supports per the Step 5 brief.
- **Inputs:** draft units `wa-m12-draft-units-from-lexical-read-v1-20260623.md` (§2 U3); §10 lens `wa-m10-section10-object-kinds-typology-provisional-v1-20260623.md`; template `wa-m11-unit-01-atonement-v1-20260623.md`. §B generator: `_build_m10_unit_verse_evidence_20260623.py --strongs H6918H,H6942G,H6942H,H6942I,H6942J,H6942K,G3741,H5144A`.

---

## A. General observations

**Draft-unit hypothesis under test (from the lexical read):** *MIXED — consecration = an ACT/CHARACTERISTIC (setting-apart, type=action), holy = a STATE; lev/levav touched. Is consecration done by God, by the person, or both (split by experiencer/divine_involvement, like na.cham was bilateral)? Does "holy" read as a STATE distinct from the consecrating ACT?*

### Computed mechanical signature (165 focus occurrences)

| Field | Distribution |
|---|---|
| **type** | **action 155** · quality 10 |
| **valence** | **commanded 83** · righteous 49 · neutral 22 · (none) 5 · **sinful 5 · forbidden 1** |
| **faculty** | **(none) 162** · affect 3 |
| **experiencer** | other 61 · (none) 47 · other-addressed 38 · self 19 |
| **divine_involvement** | **(none) 104** · **agent 34** · object 21 · possessor 4 · addressee 2 |
| **object_type** | person 52 · thing 43 · (none) 33 · God 18 · abstract 15 · situation 3 · spiritual-being 1 |
| **per-strong** | H6942G 113 · H6942H 22 · H6918H 7 · H6942J 7 · H6942K 7 · H5144A 5 · G3741 3 · H6942I 1 |
| **sense-top** | consecrated 30 · holy 30 · consecrate 26 · Consecrate 11 · sanctifies 7 · dedicate 7 · holiness 7 · dedicates 6 · dedicated 6 · sanctify 4 |

### Test 1 — consecrate-ACT vs holy-STATE: **the hypothesis HOLDS (MIXED), refined to ACT-dominant with a thin, lemma-localised STATE register**

The "ACT mostly + a holy STATE" read is **confirmed, not merely asserted**:

- **type=action 155/165 (94%)** — qadosh is overwhelmingly **an act performed**: consecrate / sanctify / dedicate / set-apart / ordain / prepare. Setting-apart is something *done to* an object (person 52, thing 43, abstract 15, God 18). This is a **CHARACTERISTIC/ACT (§10 kind A — faculty-in-operation as setting-apart)**, not a standing STATE the inner being is in.
- **The holy-STATE is real but the minority register, and it is lemma-localised.** Only **10/165 read type=quality** — and they are **not the verb qadosh at all**; they are the **adjective qa.dosh (H6918H, 7×)** ("holy", "holy ones", "saints", "holy one") and **hosios (G3741, 3×)** ("holy/devout" of persons — 1Ti 2:8 holy hands, Tit 1:8, Heb 7:26 of Christ "holy, innocent"). So the **STATE reads SPLIT out by lemma**: the *verb* family = the ACT; the *adjective* (qadosh / hosios) = the STATE. The 25 "holy"-sense occurrences typed *action* are the verb's resultative ("made it holy", "I am the LORD who makes holy") — still an act, not a standing quality.
- **Verdict:** **HOLDS / SPLITS-by-lemma.** U3 is a **MIXED unit**: a dominant **consecration ACT** (the qadosh verb, 155 action) + a thin **holy STATE** carried by the adjective qa.dosh + hosios (10 quality). The STATE is genuinely distinct from the consecrating act (different lemma, different type), confirming the draft read. ⚖ The STATE is thin enough (10) that it is a *register* of the unit, not a separable second unit — record it as the unit's state-pole, not a split.

### Test 2 — the who-consecrates split: **TRILATERAL (richer than na.cham's bilateral)**

Splitting by `divine_involvement` × `experiencer` gives **three agents of consecration**, not two:

1. **Human / priestly consecration (the cultic default) — divine_involvement=(none) 104/165 (63%).** The dominant case: the priest/people/individual sets a person or thing apart (Exo 19:10 "consecrate them today"; 1Ki/2Ch temple/vessel consecrations; Job 1:5 Job consecrates his children — lev-seated). valence=commanded dominates here (the prescribed cultic act).
2. **GOD consecrates — divine_involvement=agent 34/165 (21%).** God is the consecrator: Gen 2:3 / Exo 20:11 (the Sabbath made holy), Exo 28:41 / 29:* (God ordains/consecrates the priests and altar), and the great Leviticus refrain **"I am the LORD who sanctifies you"** (Lev 20:8; 21:8,15,23; 22:9,16,32; Eze 20:12; 37:28 — `H6942G`, di=agent, "sanctifies", obj=person). Here consecration is a **divine ACT upon the person** — the inner being is the *site/recipient*, not the agent (cf. M11 #1 atonement's "site/beneficiary" logic).
3. **Divine SELF-sanctification — experiencer=self + di=agent/possessor (Ezekiel cluster).** A distinct third agent: God **vindicates / shows Himself holy** — Eze 20:41; 28:22,25; 36:23; 38:23; 39:27 (`H6942K`, "holiness", exp=self, di=agent/possessor: "I will manifest my holiness… vindicate my holiness"). This is **God consecrating God** (the holiness-of-God axis), distinct from God consecrating the creature. *(Note: the raw `experiencer=self` count of 19 conflates this divine self-sanctification with genuine human self-consecration — e.g. Num 8:17 Levites; 2Ch 7:16,20 the temple "I have consecrated"; these are God's, not the creature's. True creature self-consecration is rarer than the count suggests.)*

- **Verdict:** **HOLDS and exceeds the hypothesis.** Consecration is done **by God, by the person/priest, AND by God of Himself** — trilateral. The na.cham bilateral parallel is the right instinct (a characteristic borne by both God and creature, per the §10 BILATERAL refinement), but qadosh adds the **God-of-God self-sanctification** register that na.cham lacked. Split by `divine_involvement` (agent = God-on-creature) + `experiencer` (self vs other) + the Ezekiel "my holiness" cluster.

### Test 3 — lev/levav touched? **YES but THIN — heart-consecration, not a faculty-seat**

- faculty is **(none) 162/165** on the lemma itself — qadosh is term-intrinsically **faculty-less** (like an act/state, not a faculty-in-operation seated in an organ).
- The **lev/levav touch is real but confined to ~6 co-seated verses**: Exo 28:3 (skill of *heart* to make consecrating garments), 1Ki 9:3 (God's *heart* on the consecrated house), Job 1:5 + Isa 30:29 (gladness of *heart* / holy feast), Lev 11:44 + Num 16:38 (ne.phesh). These are **the heart as participant/locus of the consecrating act**, not qadosh seated *in* the heart as its faculty. So "lev/levav touched" = **a real but peripheral co-seating**, not a faculty signature. The draft note ("lev/levav touched") is confirmed as *touched*, not *seated*.

### Inverse-pole / cross-cluster links (recorded, NOT acted on)

- **↔ the set-apart vs profane axis (the unit's own pole):** the §3 screening read U3 as "the set-apart vs profane axis." The evidence confirms it: consecration carves the **holy** out from the **common/defiled** — its contrast pole is the M12 **negation-pole** (tum.ah/miainō/anosios, the defilement vocabulary owned in M12 as the contrast pole, per the draft §G) and M10c defilement. The **forbidden/sinful-valence cases prove the pole**: Isa 65:5 ("I am too holy for you" — false/self-righteous holiness, val=sinful), Isa 66:17 (sanctify-self to eat pig's flesh, val=sinful), Judg 17:3 (idolatrous dedication, val=sinful), Lev 27:26 (may NOT dedicate the firstborn, val=forbidden), Eze 14:7 / Hos 9:10 (na.zar — "separates himself" *to idols*, val=sinful). **Holiness has a counterfeit**: separation toward the wrong object inverts the valence. This is the unit's own internal pole, worth a flag.
- **↔ M22 holiness/glory:** doxa (M22) co-occurs at the seam (cf. U6 Rom 2:7); the holiness-of-God self-sanctification (Eze "vindicate my holiness") is the M12↔M22 bond — God's holiness as both the *source* of consecration and the *glory* it vindicates. Recorded for synthesis.
- **↔ M11 #1 (Atonement):** qadosh is a standing partner of kip.per/ka.phar in the ordination rites (Exo 29:33 — consecration + atonement together); the priest is *atoned* and *consecrated* in one rite. The M11 atonement file already names this seam (its §B Exo 29:33 carries qa.dash as partner).
- **↔ M38 / M45:** the NT trajectory (sanctification as God's transforming work, the saints = hagioi STATE) sits with salvation/Spirit clusters — surfaced, not assembled.

### §10 object-kind classification (grounded)

- **Primary: CHARACTERISTIC / ACT (§10 kind A)** — setting-apart as a faculty-in-operation (the consecrating act), **BILATERAL/trilateral** per the §10 refinement (God-borne + human + God-of-God). type=action 94%, the act *does something to* an object.
- **Secondary register: positive STATE (§10 kind B / the candidate 9th "outcome-state")** — the **holy** quality (qa.dosh adjective, hosios), the standing set-apart condition that the act *produces*. Thin (10), lemma-localised.
- This makes U3 the clearest M12 instance of **§10 H1** (the characteristic generates the state): the consecrating ACT produces the holy STATE.

### Flags (surfaced, NOT resolved)

- **⚖ BORDER — ACT vs STATE within one unit:** U3 is genuinely MIXED. The verb (act) and the adjective (state) are different lemmas with different types. Keep as **one unit with two registers** (act-dominant + thin state-pole), not two units — the state is too thin (10) and too lemma-bound to stand alone. Record for the status-treatment step (step 6).
- **⚑ SYNTH — trilateral consecrator (God / creature / God-of-God):** the Ezekiel "I will vindicate my holiness" self-sanctification is a distinct register the na.cham bilateral model did not have; route to the §10 BILATERAL-characteristic refinement (a characteristic that is *also God-of-God-reflexive*). Surfaced, not resolved.
- **⚑ SYNTH — the counterfeit-holiness pole:** Isa 65:5 / 66:17 / Judg 17:3 / Eze 14:7 / Hos 9:10 (val=sinful/forbidden) show consecration *toward the wrong object* inverts valence — holiness has a counterfeit (self-righteous / idolatrous separation). A genuine analytical finding for the holy-vs-profane axis; surfaced for synthesis.
- **↔ BOND (cross-cluster):** M22 (Glory/holiness-of-God) · M11 #1 (Atonement — joint ordination rite) · M10c (the defilement contrast-pole) · M38/M45 (NT sanctification/saints) · M13/M26 (the holy↔profane / righteous pole-pair). Recorded, not routed.
- **⚠ HYGIENE — `experiencer=self` conflates two things:** the raw self=19 mixes **God's self-sanctification** (Ezekiel, God's own holiness) with **creature self-consecration** (Levites, temple). Read `divine_involvement` alongside `experiencer` — do not count "self" as human-only.
- **⚠ HYGIENE — na.zar (H5144A, 5 occ) is heterogeneous:** "keep/abstain" (Lev 15:31; 22:2; Zec 7:3 cultic abstention) vs "separates to idols" (Eze 14:7; Hos 9:10, sinful). Small and split; it belongs to the separation-sense of the unit but its idolatrous half is the counterfeit pole.
- **⚠ HYGIENE — qadosh is faculty-less (162/165 none):** the lev/levav co-seating (~6) is *participation/locus*, not a faculty seat. Do not over-read a heart-faculty signature.

---

## B. Per-verse structured evidence

_Per-verse structured evidence — 164 verses; Strong's ['G3741', 'H5144A', 'H6918H', 'H6942G', 'H6942H', 'H6942I', 'H6942J', 'H6942K']. From the corpus; evidence only._

#### Gen 2:3
> Gen 2:3 So God blessed the seventh day and made it holy , because on it God rested from all his work that he had done in creation .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpw3ms · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=all · object_type=thing · cause=God's rest from all his work of creation on the seventh day · cause_clause=rested all work that he done creation · experiencer=other · divine_involvement=agent · intensity=all (all) · valence=righteous
  - compound: et "[Obj.]" — qualifier; ba.rakh "to bless" — partner
- **ba.rakh (H1288)** — to bless  [Hebrew · M39]  morph=HVpw3ms · stem=Piel · target=“blessed”
  - sense=blessed · lemma_meaning=to bless, kneel · type=action · object=day · object_type=thing · cause=God's rest from all his work of creation on the seventh day · cause_clause=rested all work that he done creation · experiencer=other · divine_involvement=agent · valence=righteous
  - compound: et "[Obj.]" — qualifier; qa.dash "to consecrate: consecate" — partner

#### Exo 13:2
> Exo 13:2 “ Consecrate to me all the firstborn . Whatever is the first to open the womb among the people of Israel , both of man and of beast , is mine .”
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVpv2ms · stem=Piel · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · object=all · object_type=person · experiencer=other (addressed) · divine_involvement=agent · intensity=['all (all)', 'all (Whatever)'] · valence=commanded

#### Exo 19:10
> Exo 19:10 the Lord said to Moses , “ Go to the people and consecrate them today and tomorrow , and let them wash their garments
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=today · object_type=person · experiencer=other (addressed) · divine_involvement=agent · valence=commanded · immediate_response=wash garments

#### Exo 19:14
> Exo 19:14 So Moses went down from the mountain to the people and consecrated the people ; and they washed their garments .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpw3ms · stem=Piel · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=people · object_type=person · experiencer=other · valence=commanded

#### Exo 19:22
> Exo 19:22 Also let the priests who come near to the Lord consecrate themselves, lest the Lord break out against them.”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVti3mp · stem=Hithpael · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=Lord · object_type=God · experiencer=other · valence=commanded

#### Exo 19:23
> Exo 19:23 And Moses said to the Lord , “The people cannot come up to Mount Sinai , for you yourself warned us, saying , ‘Set limits around the mountain and consecrate it .’”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=it · object_type=person · cause=God's warning to set limits around the mountain · cause_clause=you warned saying limits mountain consecrate it · experiencer=other (addressed) · valence=commanded

#### Exo 20:8
> Exo 20:8 “ Remember the Sabbath day , to keep it holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · valence=commanded
  - compound: za.khar "to remember" — partner
- **za.khar (H2142)** — to remember  [Hebrew · M41]  morph=HVqaa · stem=Qal · target=“Remember”
  - sense=Remember · lemma_meaning=to remember, recall, call to mind · type=action · faculty=['cognition', 'memory'] · object=Sabbath · object_type=thing · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### Exo 20:11
> Exo 20:11 For in six days the Lord made the heavens and the earth , the sea , and all that is in them, and rested on the seventh day . Therefore the Lord blessed the Sabbath day and made it holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpw3ms · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · cause=God's rest on the seventh day · cause_clause=days Lord made heavens earth sea all that · experiencer=other · divine_involvement=agent · valence=righteous
  - compound: nu.ach "to rest" — partner
- **nu.ach (H5117)** — to rest  [Hebrew · M33]  morph=HVqw3ms · stem=Qal · target=“rested”
  - sense=rested · lemma_meaning=to rest · type=action · object=day · object_type=situation · cause=God completing creation in six days · cause_clause=days Lord made heavens earth sea all that · experiencer=other · intensity=all (all) · valence=righteous
  - compound: qa.dash "to consecrate: consecate" — partner

#### Exo 28:3
> Exo 28:3 You shall speak to all the skillful , whom I have filled with a spirit of skill , that they make Aaron’s garments to consecrate him for my priesthood .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · valence=commanded · relational=my
  - compound: cha.kham "wise" — partner; lev "heart" — co-seated
- **lev (H3820A)** — heart  [Hebrew · M47]  morph=HNcmsa · target=“whom”
  - sense=whom · lemma_meaning=inner man, mind, will, heart, understanding · type=UNRESOLVED · faculty=['cognition', 'perception', 'volition', 'conscience'] · how=filled (H4390) · intensity=all (all) · valence=righteous
  - compound: cha.kham "wise" — partner; qa.dash "to consecrate: consecate" — partner
- **cha.kham (H2450)** — wise  [Hebrew · M15]  morph=HAampc · target=“skillful”
  - sense=skillful · lemma_meaning=wise, wise (man) · type=quality · faculty=cognition · how=filled (H4390) · intensity=all (all) · valence=righteous
  - compound: lev "heart" — co-seated; qa.dash "to consecrate: consecate" — partner

#### Exo 28:38
> Exo 28:38 It shall be on Aaron’s forehead , and Aaron shall bear any guilt from the holy things that the people of Israel consecrate as their holy gifts . It shall regularly be on his forehead , that they may be accepted before the Lord .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhi3mp · stem=Hiphil · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=holy · object_type=thing · experiencer=other · intensity=all (gifts) · valence=commanded
  - compound: ra.tson "acceptance" — partner; a.von "iniquity: guilt" — partner
- **ra.tson (H7522)** — acceptance  [Hebrew · M29]  morph=HNcmsa · target=“accepted”
  - sense=accepted · lemma_meaning=pleasure, delight, favour, goodwill, acceptance, will · type=status · faculty=['affect', 'volition'] · how=be (H1961) · object=forehead · object_type=abstract · experiencer=other · divine_involvement=object · valence=righteous
  - compound: a.von "iniquity: guilt" — partner; qa.dash "to consecrate: consecate" — partner
- **a.von (H5771H)** — iniquity: guilt  [Hebrew · M10]  morph=HNcmsc · target=“guilt”
  - sense=guilt · lemma_meaning=crime · type=status · how=bear (H5375) · object=holy things · object_type=abstract · experiencer=other · valence=sinful
  - compound: ra.tson "acceptance" — partner; qa.dash "to consecrate: consecate" — partner

#### Exo 28:41
> Exo 28:41 And you shall put them on Aaron your brother , and on his sons with him, and shall anoint them and ordain them and consecrate them, that they may serve me as priests .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“ordain”
  - sense=ordain · lemma_meaning=consecate/sanctify · type=action · experiencer=other (addressed) · divine_involvement=agent · valence=commanded

#### Exo 29:1
> Exo 29:1 “Now this is what you shall do to them to consecrate them, that they may serve me as priests . Take one bull of the herd and two rams without blemish ,
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · divine_involvement=agent · valence=commanded
  - compound: ta.mim "unblemished" — partner

#### Exo 29:21
> Exo 29:21 Then you shall take part of the blood that is on the altar , and of the anointing oil , and sprinkle it on Aaron and his garments , and on his sons and his sons ’ garments with him . He and his garments shall be holy , and his sons and his sons ’ garments with him .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVqq3ms · stem=Qal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=sons · object_type=person · experiencer=other · divine_involvement=agent · valence=commanded

#### Exo 29:27
> Exo 29:27 And you shall consecrate the breast of the wave offering that is waved and the thigh of the priests’ portion that is contributed from the ram of ordination , from what was Aaron’s and his sons ’.
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=breast · object_type=thing · experiencer=other (addressed) · valence=commanded
  - compound: rum "to exalt" — partner

#### Exo 29:33
> Exo 29:33 They shall eat those things with which atonement was made at their ordination and consecration , but an outsider shall not eat of them, because they are holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“consecration”
  - sense=consecration · lemma_meaning=consecate/sanctify · type=action · cause=ordination and consecration rites · cause_clause=they holy · valence=commanded
  - compound: kip.per "to atone" — partner; ka.phar "to cover" — partner
- **kip.per (H3722A)** — to atone  [Hebrew · M11]  morph=HVPp3ms · stem=Pual · target=“atonement”
  - sense=atonement · lemma_meaning=to cover, purge, make an atonement, make reconciliation · type=action · cause=ordination and consecration rites · cause_clause=they holy · experiencer=other · valence=commanded
  - compound: ka.phar "to cover" — partner; qa.dash "to consecrate: consecate" — partner
- **ka.phar (H3722B)** — to cover  [Hebrew · M38]  morph=HVPp3ms · stem=Pual · target=“atonement”
  - sense=atonement · lemma_meaning=to cover, purge, make an atonement, make reconciliation · type=action · cause=ordination and consecration rites · cause_clause=they holy · experiencer=other · valence=commanded
  - compound: kip.per "to atone" — partner; qa.dash "to consecrate: consecate" — partner

#### Exo 29:36
> Exo 29:36 and every day you shall offer a bull as a sin offering for atonement . Also you shall purify the altar , when you make atonement for it, and shall anoint it to consecrate it .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=it · object_type=person · divine_involvement=agent · valence=commanded
  - compound: cha.ta "to sin" — partner; chat.tat "sin: sin offering" — partner; kip.pu.rim "atonement" — partner; ka.phar "to cover" — partner
- **cha.ta (H2398)** — to sin  [Hebrew · M10]  morph=HVpq2ms · stem=Piel · target=“purify”
  - sense=purify · lemma_meaning=to sin, miss, miss the way, go wrong, incur guilt, forfeit, purify fro · type=action · faculty=moral_evaluation · object=altar · object_type=thing · experiencer=other (addressed) · valence=sinful
  - compound: chat.tat "sin: sin offering" — partner; kip.pu.rim "atonement" — partner; ka.phar "to cover" — partner; qa.dash "to consecrate: consecate" — partner
- **chat.tat (H2403H)** — sin: sin offering  [Hebrew · M10]  morph=HNcfsa · target=“sin offering”
  - sense=sin offering · lemma_meaning=sin, sinful thing · type=status · how=offer (H6213) · valence=sinful
  - compound: cha.ta "to sin" — partner; kip.pu.rim "atonement" — partner; ka.phar "to cover" — partner; qa.dash "to consecrate: consecate" — partner
- **kip.pu.rim (H3725)** — atonement  [Hebrew · M10]  morph=HNcmpa · target=“atonement”
  - sense=atonement · lemma_meaning=atonement · type=status · how=purify (H2398) · valence=commanded
  - compound: cha.ta "to sin" — partner; chat.tat "sin: sin offering" — partner; ka.phar "to cover" — partner; qa.dash "to consecrate: consecate" — partner

#### Exo 29:37
> Exo 29:37 Seven days you shall make atonement for the altar and consecrate it, and the altar shall be most holy . Whatever touches the altar shall become holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=altar · object_type=thing · experiencer=other (addressed) · divine_involvement=agent · valence=commanded
  - compound: ka.phar "to cover" — partner

#### Exo 29:43
> Exo 29:43 There I will meet with the people of Israel , and it shall be sanctified by my glory .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVNq3ms · stem=Niphal · target=“sanctified”
  - sense=sanctified · lemma_meaning=consecate/sanctify · type=action · object=my · object_type=person · experiencer=other · divine_involvement=agent · valence=commanded
  - compound: ka.vod "glory" — partner
- **ka.vod (H3519)** — glory  [Hebrew · M22]  morph=HNcbsc · target=“glory”
  - sense=glory · lemma_meaning=glory, honour, glorious, abundance · type=status · faculty=affect · how=sanctified (H6942) · object=my · object_type=person · experiencer=self · divine_involvement=agent
  - compound: qa.dash "to consecrate: consecate" — partner

#### Exo 29:44
> Exo 29:44 I will consecrate the tent of meeting and the altar . Aaron also and his sons I will consecrate to serve me as priests .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq1cs · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=tent · object_type=thing · experiencer=self · valence=commanded · immediate_response=consecrate

#### Exo 30:29
> Exo 30:29 You shall consecrate them, that they may be most holy . Whatever touches them will become holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=most · object_type=thing · experiencer=other (addressed) · divine_involvement=agent · valence=commanded

#### Exo 30:30
> Exo 30:30 You shall anoint Aaron and his sons , and consecrate them, that they may serve me as priests .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · experiencer=other (addressed) · valence=commanded · relational=me

#### Exo 31:13
> Exo 31:13 “ You are to speak to the people of Israel and say , ‘Above all you shall keep my Sabbaths , for this is a sign between me and you throughout your generations , that you may know that I , the Lord , sanctify you .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVprmsc · stem=Piel · target=“sanctify”
  - sense=sanctify · lemma_meaning=consecate/sanctify · type=action · object=you · object_type=person · cause=the Lord sanctifying the people · cause_clause=sign between you generations know that I Lord · divine_involvement=agent · valence=righteous
  - compound: sha.mar "to keep: obey" — partner
- **sha.mar (H8104G)** — to keep: obey  [Hebrew · M30]  morph=HVqi2mp · stem=Qal · target=“keep”
  - sense=keep · lemma_meaning=obey/observe · type=action · faculty=['perception', 'volition'] · object=Sabbaths · object_type=abstract · cause_clause=sign between you generations know that I Lord · experiencer=other (addressed) · valence=commanded · immediate_response=sanctify
  - compound: qa.dash "to consecrate: consecate" — partner

#### Exo 40:9
> Exo 40:9 “Then you shall take the anointing oil and anoint the tabernacle and all that is in it, and consecrate it and all its furniture , so that it may become holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=all · object_type=thing · experiencer=other (addressed) · intensity=['all (all)', 'all (all)'] · valence=commanded · immediate_response=become holy

#### Exo 40:10
> Exo 40:10 You shall also anoint the altar of burnt offering and all its utensils , and consecrate the altar , so that the altar may become most holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=altar · object_type=thing · experiencer=other (addressed) · intensity=all (all) · valence=commanded

#### Exo 40:11
> Exo 40:11 You shall also anoint the basin and its stand , and consecrate it .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · experiencer=other (addressed) · valence=commanded

#### Exo 40:13
> Exo 40:13 and put on Aaron the holy garments . And you shall anoint him and consecrate him, that he may serve me as priest .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · experiencer=other (addressed) · valence=commanded · relational=me

#### Lev 6:18
> Lev 6:18 Every male among the children of Aaron may eat of it, as decreed forever throughout your generations , from the Lord’s food offerings . Whatever touches them shall become holy .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVqi3ms · stem=Qal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · experiencer=other · intensity=all (touches) · valence=righteous

#### Lev 6:27
> Lev 6:27 Whatever touches its flesh shall be holy , and when any of its blood is splashed on a garment , you shall wash that on which it was splashed in a holy place .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVqi3ms · stem=Qal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · location=flesh · object=any · object_type=thing · experiencer=other · intensity=all (any) · valence=righteous

#### Lev 8:10
> Lev 8:10 Then Moses took the anointing oil and anointed the tabernacle and all that was in it, and consecrated them .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpw3ms · stem=Piel · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · experiencer=other · intensity=all (all) · valence=commanded

#### Lev 8:11
> Lev 8:11 And he sprinkled some of it on the altar seven times , and anointed the altar and all its utensils and the basin and its stand , to consecrate them .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=them · object_type=person · valence=commanded

#### Lev 8:12
> Lev 8:12 And he poured some of the anointing oil on Aaron’s head and anointed him to consecrate him .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=him · object_type=person · valence=commanded

#### Lev 8:15
> Lev 8:15 And he killed it, and Moses took the blood , and with his finger put it on the horns of the altar around it and purified the altar and poured out the blood at the base of the altar and consecrated it to make atonement for it .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpw3ms · stem=Piel · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=it · object_type=person · experiencer=other · valence=commanded
  - compound: cha.ta "to sin" — partner; ka.phar "to cover" — partner
- **cha.ta (H2398)** — to sin  [Hebrew · M10]  morph=HVpw3ms · stem=Piel · target=“purified”
  - sense=purified · lemma_meaning=to sin, miss, miss the way, go wrong, incur guilt, forfeit, purify fro · type=action · faculty=moral_evaluation · object=altar · object_type=thing · experiencer=other · valence=sinful
  - compound: qa.dash "to consecrate: consecate" — partner; ka.phar "to cover" — partner

#### Lev 8:30
> Lev 8:30 Then Moses took some of the anointing oil and of the blood that was on the altar and sprinkled it on Aaron and his garments , and also on his sons and his sons ’ garments . So he consecrated Aaron and his garments , and his sons and his sons ’ garments with him .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpw3ms · stem=Piel · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=Aaron · object_type=person · experiencer=other · valence=commanded

#### Lev 10:3
> Lev 10:3 Then Moses said to Aaron , “This is what the Lord has said : ‘ Among those who are near me I will be sanctified , and before all the people I will be glorified .’” And Aaron held his peace .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVNi1cs · stem=Niphal · target=“sanctified”
  - sense=sanctified · lemma_meaning=consecate/sanctify · type=action · object=before · object_type=God · experiencer=self · intensity=all (all) · valence=commanded · immediate_response=glorified Aaron
  - compound: da.mam "to silence: silent" — partner
- **da.mam (H1826H)** — to silence: silent  [Hebrew · M33]  morph=HVqw3ms · stem=Qal · target=“peace”
  - sense=peace · lemma_meaning=stationary · type=action · experiencer=other · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner

#### Lev 11:44
> Lev 11:44 For I am the Lord your God . Consecrate yourselves therefore, and be holy , for I am holy . You shall not defile yourselves with any swarming thing that crawls on the ground .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtq2mp · stem=Hithpael · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · location=soul · cause_clause=God Consecrate be holy holy not defile yourselves · experiencer=other (addressed) · valence=commanded
  - compound: qa.dosh "holy" — partner; ne.phesh "soul: myself" — co-seated; ta.me "to defile" — partner
- **qa.dosh (H6918G)** — holy  [Hebrew · M22]  morph=HAampa · target=“holy”
  - sense=holy · lemma_meaning=holy · type=quality · location=soul · how=be (H1961) · cause_clause=God Consecrate be holy holy not defile yourselves · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner; ne.phesh "soul: myself" — co-seated; ta.me "to defile" — partner
- **ta.me (H2930A)** — to defile  [Hebrew · M10]  morph=HVpi2mp · stem=Piel · target=“defile”
  - sense=defile · lemma_meaning=to be unclean, become unclean, become impure · type=action · location=soul · object=yourselves · object_type=person · cause=contact with swarming things that crawl on the ground · cause_clause=God Consecrate be holy holy not defile yourselves · experiencer=other (addressed) · intensity=all (any) · valence=forbidden
  - compound: qa.dash "to consecrate: consecate" — partner; qa.dosh "holy" — partner; ne.phesh "soul: myself" — co-seated
- **ne.phesh (H5315I)** — soul: myself  [Hebrew · M47]  morph=HNcfpc · target=“yourselves”
  - sense=yourselves · lemma_meaning=soul, self, life, creature, person, appetite, mind, living being, desi · type=status · faculty=['affect', 'volition'] · location=soul · how=defile (H2930) · object=any · object_type=God · cause_clause=God Consecrate be holy holy not defile yourselves · intensity=all (any) · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner; qa.dosh "holy" — partner; ta.me "to defile" — partner

#### Lev 15:31
> Lev 15:31 “Thus you shall keep the people of Israel separate from their uncleanness , lest they die in their uncleanness by defiling my tabernacle that is in their midst .”
- **na.zar (H5144A)** — to dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhq2mp · stem=Hiphil · target=“keep”
  - sense=keep · lemma_meaning=to dedicate, consecrate, separate · type=action · object=people · object_type=person · experiencer=other (addressed) · valence=commanded
  - compound: ta.me "to defile" — partner; tum.ah "uncleanness" — partner
- **ta.me (H2930A)** — to defile  [Hebrew · M10]  morph=HVpcc · stem=Piel · target=“defiling”
  - sense=defiling · lemma_meaning=to be unclean, become unclean, become impure · type=action · object=tabernacle · object_type=thing · valence=forbidden
  - compound: na.zar "to dedicate" — partner; tum.ah "uncleanness" — partner
- **tum.ah (H2932)** — uncleanness  [Hebrew · M12]  morph=HNcfsc · target=“uncleanness”
  - sense=uncleanness · lemma_meaning=uncleanness · type=status · how=die (H4191) · experiencer=other · valence=forbidden · immediate_response=defiling tabernacle
  - compound: na.zar "to dedicate" — partner; ta.me "to defile" — partner

#### Lev 16:19
> Lev 16:19 And he shall sprinkle some of the blood on it with his finger seven times , and cleanse it and consecrate it from the uncleannesses of the people of Israel .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq3ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=uncleannesses · object_type=thing · experiencer=other · valence=commanded
  - compound: tum.ah "uncleanness" — partner; ta.her "be pure" — partner
- **tum.ah (H2932)** — uncleanness  [Hebrew · M12]  morph=HNcfpc · target=“uncleannesses”
  - sense=uncleannesses · lemma_meaning=uncleanness · type=status · how=consecrate (H6942) · object=people · object_type=abstract · experiencer=other · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner; ta.her "be pure" — partner
- **ta.her (H2891)** — be pure  [Hebrew · M12]  morph=HVpq3ms · stem=Piel · target=“cleanse”
  - sense=cleanse · lemma_meaning=to be clean, be pure · type=action · object=uncleannesses · object_type=thing · experiencer=other · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner; tum.ah "uncleanness" — partner

#### Lev 20:7
> Lev 20:7 Consecrate yourselves, therefore, and be holy , for I am the Lord your God .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtq2mp · stem=Hithpael · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · cause_clause=God · experiencer=other (addressed) · valence=commanded
  - compound: qa.dosh "holy" — partner
- **qa.dosh (H6918G)** — holy  [Hebrew · M22]  morph=HAampa · target=“holy”
  - sense=holy · lemma_meaning=holy · type=quality · how=be (H1961) · cause_clause=God · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### Lev 20:8
> Lev 20:8 Keep my statutes and do them; I am the Lord who sanctifies you .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVprmsc · stem=Piel · target=“sanctifies”
  - sense=sanctifies · lemma_meaning=consecate/sanctify · type=action · object=you · object_type=person · divine_involvement=agent · valence=commanded
  - compound: sha.mar "to keep: obey" — partner
- **sha.mar (H8104G)** — to keep: obey  [Hebrew · M30]  morph=HVqq2mp · stem=Qal · target=“Keep”
  - sense=Keep · lemma_meaning=obey/observe · type=action · faculty=['perception', 'volition'] · object=statutes · object_type=abstract · experiencer=other (addressed) · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### Lev 21:8
> Lev 21:8 You shall sanctify him , for he offers the bread of your God . He shall be holy to you, for I , the Lord , who sanctify you , am holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2ms · stem=Piel · target=“sanctify”
  - sense=sanctify · lemma_meaning=consecate/sanctify · type=action · object=bread · object_type=person · cause=offering the bread of God · cause_clause=God holy I Lord sanctify you am holy · experiencer=other (addressed) · divine_involvement=object · valence=commanded
  - compound: qa.dosh "holy" — partner
- **qa.dosh (H6918G)** — holy  [Hebrew · M22]  morph=HAamsa · target=“holy”
  - sense=holy · lemma_meaning=holy · type=quality · cause_clause=God holy I Lord sanctify you am holy · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### Lev 21:15
> Lev 21:15 that he may not profane his offspring among his people , for I am the Lord who sanctifies him .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVprmsc · stem=Piel · target=“sanctifies”
  - sense=sanctifies · lemma_meaning=consecate/sanctify · type=action · object=him · object_type=person · cause_clause=sanctifies him · divine_involvement=agent · valence=commanded

#### Lev 21:23
> Lev 21:23 but he shall not go through the veil or approach the altar , because he has a blemish , that he may not profane my sanctuaries , for I am the Lord who sanctifies them .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVprmsc · stem=Piel · target=“sanctifies”
  - sense=sanctifies · lemma_meaning=consecate/sanctify · type=action · object=them · object_type=person · cause_clause=not profane sanctuaries I Lord sanctifies them · divine_involvement=agent · valence=commanded

#### Lev 22:2
> Lev 22:2 “ Speak to Aaron and his sons so that they abstain from the holy things of the people of Israel , which they dedicate to me, so that they do not profane my holy name : I am the Lord .
- **na.zar (H5144A)** — to dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVNu3mp · stem=Niphal · target=“abstain”
  - sense=abstain · lemma_meaning=to dedicate, consecrate, separate · type=action · object=holy things · object_type=thing · experiencer=other · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhrmpa · stem=Hiphil · target=“dedicate”
  - sense=dedicate · lemma_meaning=consecate/sanctify · type=action · object=holy · object_type=abstract · valence=commanded
  - compound: na.zar "to dedicate" — partner

#### Lev 22:3
> Lev 22:3 Say to them, ‘If any one of all your offspring throughout your generations approaches the holy things that the people of Israel dedicate to the Lord , while he has an uncleanness , that person shall be cut off from my presence : I am the Lord .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhi3mp · stem=Hiphil · target=“dedicate”
  - sense=dedicate · lemma_meaning=consecate/sanctify · type=action · location=soul · object=Lord · object_type=God · experiencer=other · divine_involvement=object · valence=commanded · immediate_response=cut off presence
  - compound: tum.ah "uncleanness" — partner
- **tum.ah (H2932)** — uncleanness  [Hebrew · M12]  morph=HNcfsc · target=“uncleanness”
  - sense=uncleanness · lemma_meaning=uncleanness · type=status · location=soul · how=cut off (H3772) · object=presence · object_type=situation · experiencer=other · valence=sinful
  - compound: qa.dash "to consecrate: consecate" — partner

#### Lev 22:9
> Lev 22:9 They shall therefore keep my charge , lest they bear sin for it and die thereby when they profane it: I am the Lord who sanctifies them .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVprmsc · stem=Piel · target=“sanctifies”
  - sense=sanctifies · lemma_meaning=consecate/sanctify · type=action · object=them · object_type=person · cause_clause=I Lord sanctifies them · divine_involvement=agent · valence=commanded
  - compound: chet "sin" — partner; sha.mar "to keep: obey" — partner
- **chet (H2399)** — sin  [Hebrew · M10]  morph=HNcmsa · target=“sin”
  - sense=sin · lemma_meaning=sin · type=status · how=bear (H5375) · cause=profaning the holy charge by not keeping it · cause_clause=I Lord sanctifies them · experiencer=other · valence=sinful
  - compound: qa.dash "to consecrate: consecate" — partner; sha.mar "to keep: obey" — partner
- **sha.mar (H8104G)** — to keep: obey  [Hebrew · M30]  morph=HVqq3cp · stem=Qal · target=“keep”
  - sense=keep · lemma_meaning=obey/observe · type=action · faculty=['perception', 'volition'] · object=charge · object_type=thing · cause_clause=I Lord sanctifies them · experiencer=other · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner; chet "sin" — partner

#### Lev 22:16
> Lev 22:16 and so cause them to bear iniquity and guilt , by eating their holy things : for I am the Lord who sanctifies them .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVprmsc · stem=Piel · target=“sanctifies”
  - sense=sanctifies · lemma_meaning=consecate/sanctify · type=action · object=them · object_type=person · cause_clause=sanctifies them · divine_involvement=agent · valence=commanded
  - compound: ash.mah "guiltiness" — partner; a.von "iniquity: crime" — partner
- **ash.mah (H0819)** — guiltiness  [Hebrew · M10]  morph=HNcfsa · target=“guilt”
  - sense=guilt · lemma_meaning=guiltiness, guilt, offense, sin, wrong-doing · type=status · how=bear (H5375) · cause=eating holy things in an unauthorized manner · cause_clause=sanctifies them · experiencer=other · valence=sinful
  - compound: qa.dash "to consecrate: consecate" — partner; a.von "iniquity: crime" — partner
- **a.von (H5771G)** — iniquity: crime  [Hebrew · M10]  morph=HNcmsc · target=“iniquity”
  - sense=iniquity · lemma_meaning=crime · type=status · how=bear (H5375) · object=guilt · object_type=abstract · cause=eating holy things in an unauthorized manner · cause_clause=sanctifies them · experiencer=other · valence=sinful
  - compound: qa.dash "to consecrate: consecate" — partner; ash.mah "guiltiness" — partner

#### Lev 22:32
> Lev 22:32 And you shall not profane my holy name , that I may be sanctified among the people of Israel . I am the Lord who sanctifies you ,
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVNq1cs · stem=Niphal · target=“sanctified”
  - sense=sanctified · lemma_meaning=consecate/sanctify · type=action · object=among · object_type=abstract · experiencer=self · divine_involvement=agent · valence=commanded

#### Lev 25:10
> Lev 25:10 And you shall consecrate the fiftieth year , and proclaim liberty throughout the land to all its inhabitants . It shall be a jubilee for you, when each of you shall return to his property and each of you shall return to his clan .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2mp · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=year · object_type=abstract · experiencer=other (addressed) · valence=commanded
  - compound: qa.ra "to call: call out" — partner
- **qa.ra (H7121I)** — to call: call out  [Hebrew · M37]  morph=HVqq2mp · stem=Qal · target=“proclaim”
  - sense=proclaim · lemma_meaning=call to/invite/entreat · type=action · faculty=volition · object=liberty · object_type=abstract · experiencer=other (addressed) · intensity=all (all) · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### Lev 27:14
> Lev 27:14 “When a man dedicates his house as a holy gift to the Lord , the priest shall value it as either good or bad ; as the priest values it, so it shall stand .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhi3ms · stem=Hiphil · target=“dedicates”
  - sense=dedicates · lemma_meaning=consecate/sanctify · type=action · object=house · object_type=thing · cause=man dedicating his house as a holy gift · cause_clause=house holy Lord priest value either good bad · experiencer=other · valence=neutral
  - compound: tov "pleasant" — partner

#### Lev 27:15
> Lev 27:15 And if the donor wishes to redeem his house , he shall add a fifth to the valuation price , and it shall be his .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhrmsa · stem=Hiphil · target=“donor”
  - sense=donor · lemma_meaning=consecate/sanctify · type=action · object=house · object_type=thing · valence=neutral

#### Lev 27:16
> Lev 27:16 “If a man dedicates to the Lord part of the land that is his possession , then the valuation shall be in proportion to its seed . A homer of barley seed shall be valued at fifty shekels of silver .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhi3ms · stem=Hiphil · target=“dedicates”
  - sense=dedicates · lemma_meaning=consecate/sanctify · type=action · object=Lord · object_type=God · experiencer=other · divine_involvement=object · valence=neutral

#### Lev 27:17
> Lev 27:17 If he dedicates his field from the year of jubilee , the valuation shall stand ,
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhi3ms · stem=Hiphil · target=“dedicates”
  - sense=dedicates · lemma_meaning=consecate/sanctify · type=action · object=field · object_type=thing · experiencer=other · valence=neutral

#### Lev 27:18
> Lev 27:18 but if he dedicates his field after the jubilee , then the priest shall calculate the price according to the years that remain until the year of jubilee , and a deduction shall be made from the valuation .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhi3ms · stem=Hiphil · target=“dedicates”
  - sense=dedicates · lemma_meaning=consecate/sanctify · type=action · object=field · object_type=thing · experiencer=other · valence=neutral · immediate_response=calculate price
  - compound: cha.shav "to devise: count" — partner

#### Lev 27:19
> Lev 27:19 And if he who dedicates the field wishes to redeem it, then he shall add a fifth to its valuation price , and it shall remain his .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhrmsa · stem=Hiphil · target=“dedicates”
  - sense=dedicates · lemma_meaning=consecate/sanctify · type=action · object=field · object_type=thing · valence=neutral

#### Lev 27:22
> Lev 27:22 If he dedicates to the Lord a field that he has bought , which is not a part of his possession ,
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhi3ms · stem=Hiphil · target=“dedicates”
  - sense=dedicates · lemma_meaning=consecate/sanctify · type=action · object=Lord · object_type=God · experiencer=other · divine_involvement=object · valence=righteous

#### Lev 27:26
> Lev 27:26 “ But a firstborn of animals , which as a firstborn belongs to the Lord , no man may dedicate ; whether ox or sheep , it is the Lord’s .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhi3ms · stem=Hiphil · target=“dedicate”
  - sense=dedicate · lemma_meaning=consecate/sanctify · type=action · object=ox · object_type=thing · experiencer=other · valence=forbidden

#### Num 3:13
> Num 3:13 for all the firstborn are mine. On the day that I struck down all the firstborn in the land of Egypt , I consecrated for my own all the firstborn in Israel , both of man and of beast . They shall be mine: I am the Lord .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp1cs · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=all · object_type=person · cause=striking down firstborn in Egypt · cause_clause=firstborn On day struck all firstborn land Egypt · experiencer=self · divine_involvement=agent · intensity=all (all) · valence=righteous
  - compound: a.ni "I" — qualifier

#### Num 6:11
> Num 6:11 and the priest shall offer one for a sin offering and the other for a burnt offering , and make atonement for him, because he sinned by reason of the dead body . And he shall consecrate his head that same day
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq3ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · location=soul · object=head · object_type=thing · experiencer=other · valence=commanded
  - compound: cha.ta "to sin" — partner; chat.tat "sin: sin offering" — partner; kip.per "to atone" — partner; ka.phar "to cover" — partner
- **cha.ta (H2398)** — to sin  [Hebrew · M10]  morph=HVqp3ms · stem=Qal · target=“sinned”
  - sense=sinned · lemma_meaning=to sin, miss, miss the way, go wrong, incur guilt, forfeit, purify fro · type=action · faculty=moral_evaluation · location=soul · object=dead body · object_type=abstract · experiencer=other · valence=sinful · relational=['because', 'reason of']
  - compound: qa.dash "to consecrate: consecate" — partner; chat.tat "sin: sin offering" — partner; kip.per "to atone" — partner; ka.phar "to cover" — partner
- **chat.tat (H2403H)** — sin: sin offering  [Hebrew · M10]  morph=HNcfsa · target=“sin offering”
  - sense=sin offering · lemma_meaning=sin, sinful thing · type=status · location=soul · how=offer (H6213) · experiencer=other · valence=neutral · immediate_response=atonement
  - compound: qa.dash "to consecrate: consecate" — partner; cha.ta "to sin" — partner; kip.per "to atone" — partner; ka.phar "to cover" — partner
- **kip.per (H3722A)** — to atone  [Hebrew · M11]  morph=HVpq3ms · stem=Piel · target=“atonement”
  - sense=atonement · lemma_meaning=to cover, purge, make an atonement, make reconciliation · type=action · location=soul · experiencer=other · valence=commanded · relational=for
  - compound: qa.dash "to consecrate: consecate" — partner; cha.ta "to sin" — partner; chat.tat "sin: sin offering" — partner; ka.phar "to cover" — partner
- **ka.phar (H3722B)** — to cover  [Hebrew · M38]  morph=HVpq3ms · stem=Piel · target=“atonement”
  - sense=atonement · lemma_meaning=to cover, purge, make an atonement, make reconciliation · type=action · location=soul · experiencer=other · valence=commanded · relational=for
  - compound: qa.dash "to consecrate: consecate" — partner; cha.ta "to sin" — partner; chat.tat "sin: sin offering" — partner; kip.per "to atone" — partner

#### Num 7:1
> Num 7:1 On the day when Moses had finished setting up the tabernacle and had anointed and consecrated it with all its furnishings and had anointed and consecrated the altar with all its utensils ,
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpw3ms · stem=Piel · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=all · object_type=thing · experiencer=other · intensity=all (all) · valence=commanded · immediate_response=anointed altar

#### Num 8:17
> Num 8:17 For all the firstborn among the people of Israel are mine, both of man and of beast . On the day that I struck down all the firstborn in the land of Egypt I consecrated them for myself ,
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp1cs · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · cause=striking down firstborn in Egypt · cause_clause=all firstborn people Israel man beast day struck down · experiencer=self · valence=righteous

#### Num 11:18
> Num 11:18 And say to the people , ‘ Consecrate yourselves for tomorrow , and you shall eat meat , for you have wept in the hearing of the Lord , saying , “ Who will give us meat to eat ? For it was better for us in Egypt .” Therefore the Lord will give you meat , and you shall eat .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtv2mp · stem=Hithpael · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · object=tomorrow · object_type=person · cause=preparation before receiving meat from the Lord · cause_clause=wept hearing Lord saying Who meat eat For · experiencer=other (addressed) · valence=commanded
  - compound: tov "be pleasing" — partner; mi "who?" — qualifier; ba.khah "to weep" — partner
- **ba.khah (H1058)** — to weep  [Hebrew · M03]  morph=HVqp2mp · stem=Qal · target=“wept”
  - sense=wept · lemma_meaning=to weep, bewail, cry, shed tears · type=action · faculty=affect · object=hearing · object_type=situation · cause=desire for meat and dissatisfaction with conditions · cause_clause=wept hearing Lord saying Who meat eat For · experiencer=other (addressed) · divine_involvement=addressee · valence=sinful
  - compound: tov "be pleasing" — partner; qa.dash "to consecrate: consecate" — partner; mi "who?" — qualifier

#### Num 16:7
> Num 16:7 put fire in them and put incense on them before the Lord tomorrow , and the man whom the Lord chooses shall be the holy one. You have gone too far , sons of Levi !”
- **qa.dosh (H6918H)** — holy: saint  [Hebrew · M12 · **FOCUS**]  morph=HAamsa · target=“holy”
  - sense=holy · lemma_meaning=holy · type=quality · how=chooses (H0977) · divine_involvement=agent · intensity=many (far) · valence=righteous
  - compound: ba.char "to choose" — partner
- **ba.char (H0977)** — to choose  [Hebrew · M37]  morph=HVqi3ms · stem=Qal · target=“chooses”
  - sense=chooses · lemma_meaning=to choose, elect, decide for · type=action · faculty=volition · object=sons · object_type=person · experiencer=other · divine_involvement=agent · intensity=many (far) · valence=neutral
  - compound: qa.dosh "holy: saint" — partner

#### Num 16:37
> Num 16:37 “ Tell Eleazar the son of Aaron the priest to take up the censers out of the blaze . Then scatter the fire far and wide , for they have become holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVqp3cp · stem=Qal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · cause=being offered before the Lord · cause_clause=holy · experiencer=other · valence=neutral
  - compound: rum "to exalt" — partner

#### Num 16:38
> Num 16:38 As for the censers of these men who have sinned at the cost of their lives , let them be made into hammered plates as a covering for the altar , for they offered them before the Lord , and they became holy . Thus they shall be a sign to the people of Israel .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVqw3mp · stem=Qal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · location=soul · object=sign · object_type=thing · cause=being offered before the Lord · cause_clause=before Lord holy be sign people Israel · experiencer=other · valence=neutral
  - compound: ne.phesh "soul: life" — co-seated; chat.ta "sinner" — partner
- **chat.ta (H2400)** — sinner  [Hebrew · M10]  morph=HAampa · target=“sinned”
  - sense=sinned · lemma_meaning=sinners · type=quality · faculty=moral_evaluation · location=soul · how=made (H6213) · cause=offering censers before the Lord at cost of their lives · cause_clause=before Lord holy be sign people Israel · valence=sinful
  - compound: qa.dash "to consecrate: consecate" — partner; ne.phesh "soul: life" — co-seated
- **ne.phesh (H5315H)** — soul: life  [Hebrew · M25]  morph=HNcfpc · target=“lives”
  - sense=lives · lemma_meaning=soul, self, life, creature, person, appetite, mind, living being, desi · type=status · faculty=['affect', 'volition'] · location=soul · how=made (H6213) · cause=sinning by offering unauthorized fire before the Lord · cause_clause=before Lord holy be sign people Israel · experiencer=other · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner; chat.ta "sinner" — partner

#### Num 20:12
> Num 20:12 And the Lord said to Moses and Aaron , “ Because you did not believe in me, to uphold me as holy in the eyes of the people of Israel , therefore you shall not bring this assembly into the land that I have given them .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhcc · stem=Hiphil · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=eyes · object_type=God · divine_involvement=object · relational=to
  - compound: a.man "be faithful" — partner; na.tan "to give: give" — partner
- **a.man (H0539)** — be faithful  [Hebrew · M13]  morph=HVhp2mp · stem=Hiphil · target=“believe”
  - sense=believe · lemma_meaning=to support, confirm, be faithful · type=action · object=eyes · object_type=God · experiencer=other (addressed) · divine_involvement=object · relational=to
  - compound: qa.dash "to consecrate: consecate" — partner; na.tan "to give: give" — partner
- **na.tan (H5414G)** — to give: give  [Hebrew · M12]  morph=HVqp1cs · stem=Qal · target=“given”
  - sense=given · lemma_meaning=give/deliver/send/produce · type=action · experiencer=self · divine_involvement=giver · relational=them
  - compound: qa.dash "to consecrate: consecate" — partner; a.man "be faithful" — partner

#### Num 20:13
> Num 20:13 These are the waters of Meribah , where the people of Israel quarreled with the Lord , and through them he showed himself holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVNw3ms · stem=Niphal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · experiencer=other · divine_involvement=agent · relational=them
  - compound: riv "to contend" — partner
- **riv (H7378)** — to contend  [Hebrew · M44]  morph=HVqp3cp · stem=Qal · target=“quarreled”
  - sense=quarreled · lemma_meaning=to strive, contend · type=action · object=Lord · object_type=God · experiencer=other · divine_involvement=addressee · relational=with
  - compound: qa.dash "to consecrate: consecate" — partner

#### Num 27:14
> Num 27:14 because you rebelled against my word in the wilderness of Zin when the congregation quarreled , failing to uphold me as holy at the waters before their eyes .” ( These are the waters of Meribah of Kadesh in the wilderness of Zin .)
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhcc · stem=Hiphil · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=waters · object_type=God · divine_involvement=object · valence=commanded · relational=to
  - compound: me.ri.vah "provocation" — partner
- **me.ri.vah (H4808)** — provocation  [Hebrew · M02]  morph=HNcfsc · target=“quarreled”
  - sense=quarreled · lemma_meaning=strife, contention · type=status · valence=sinful · relational=to
  - compound: qa.dash "to consecrate: consecate" — partner

#### Deu 5:12
> Deu 5:12 “‘ Observe the Sabbath day , to keep it holy , as the Lord your God commanded you.
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=Lord · object_type=God · valence=commanded
  - compound: sha.mar "to keep: obey" — partner
- **sha.mar (H8104G)** — to keep: obey  [Hebrew · M30]  morph=HVqaa · stem=Qal · target=“Observe”
  - sense=Observe · lemma_meaning=obey/observe · type=action · faculty=['perception', 'volition'] · object=Sabbath · object_type=abstract · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### Deu 15:19
> Deu 15:19 “ All the firstborn males that are born of your herd and flock you shall dedicate to the Lord your God . You shall do no work with the firstborn of your herd , nor shear the firstborn of your flock .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhi2ms · stem=Hiphil · target=“dedicate”
  - sense=dedicate · lemma_meaning=consecate/sanctify · type=action · object=Lord · object_type=God · experiencer=other (addressed) · divine_involvement=object · valence=commanded

#### Deu 22:9
> Deu 22:9 “You shall not sow your vineyard with two kinds of seed , lest the whole yield be forfeited , the crop that you have sown and the yield of the vineyard .
- **qa.dash (H6942I)** — to consecrate: forfeit  [Hebrew · M12 · **FOCUS**]  morph=HVqi3fs · stem=Qal · target=“forfeited”
  - sense=forfeited · lemma_meaning=consecate/sanctify · type=action · object=crop · object_type=thing · experiencer=other · valence=neutral

#### Deu 32:51
> Deu 32:51 because you broke faith with me in the midst of the people of Israel at the waters of Meribah-kadesh , in the wilderness of Zin , and because you did not treat me as holy in the midst of the people of Israel .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpp2mp · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=midst · object_type=God · experiencer=other (addressed) · divine_involvement=object · valence=commanded
  - compound: ma.al "be unfaithful" — partner
- **ma.al (H4603)** — be unfaithful  [Hebrew · M10]  morph=HVqp2mp · stem=Qal · target=“broke faith”
  - sense=broke faith · lemma_meaning=to act unfaithfully, act treacherously, transgress, commit a trespass · type=action · object=midst · object_type=God · experiencer=other (addressed) · divine_involvement=object · valence=sinful · relational=because
  - compound: qa.dash "to consecrate: consecate" — partner

#### Deu 33:3
> Deu 33:3 Yes , he loved his people , all his holy ones were in his hand ; so they followed in your steps , receiving direction from you,
- **qa.dosh (H6918H)** — holy: saint  [Hebrew · M12 · **FOCUS**]  morph=HAampc · target=“holy ones”
  - sense=holy ones · lemma_meaning=holy · type=quality · how=followed (H8497) · experiencer=other · intensity=all (all) · valence=righteous · immediate_response=receiving direction

#### Jos 3:5
> Jos 3:5 Then Joshua said to the people , “ Consecrate yourselves, for tomorrow the Lord will do wonders among you.”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtv2mp · stem=Hithpael · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · object=tomorrow · object_type=person · cause_clause=Lord do wonders among · experiencer=other (addressed) · valence=commanded
  - compound: pa.la "to wonder" — partner
- **pa.la (H6381)** — to wonder  [Hebrew · M04]  morph=HVNrfpa · stem=Niphal · target=“wonders”
  - sense=wonders · lemma_meaning=to be marvellous, be wonderful, be surpassing, be extraordinary, separ · type=action · faculty=['affect', 'cognition'] · object=among · object_type=situation · cause=the Lord doing wonders among the people · cause_clause=Lord do wonders among · divine_involvement=agent · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner

#### Jos 7:13
> Jos 7:13 Get up ! Consecrate the people and say , ‘ Consecrate yourselves for tomorrow ; for thus says the Lord , God of Israel , “There are devoted things in your midst , O Israel . You cannot stand before your enemies until you take away the devoted things from among you.”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpv2ms · stem=Piel · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · object=people · object_type=person · cause=God's command through Joshua before the battle · cause_clause=Lord God Israel devoted things midst Israel cannot stand · experiencer=other (addressed) · valence=commanded
  - compound: sur "to turn aside: remove" — partner
- **sur (H5493G)** — to turn aside: remove  [Hebrew · M30]  morph=HVhcc · stem=Hiphil · target=“away”
  - sense=away · lemma_meaning=remove · type=action · object=devoted things · object_type=thing · cause=presence of devoted things in the camp · cause_clause=Lord God Israel devoted things midst Israel cannot stand · valence=commanded · relational=until
  - compound: qa.dash "to consecrate: consecate" — partner

#### Jos 20:7
> Jos 20:7 So they set apart Kedesh in Galilee in the hill country of Naphtali , and Shechem in the hill country of Ephraim , and Kiriath-arba (that is, Hebron ) in the hill country of Judah .
- **qa.dash (H6942J)** — to consecrate: prepare  [Hebrew · M12 · **FOCUS**]  morph=HVhw3mp · stem=Hiphil · target=“set apart”
  - sense=set apart · lemma_meaning=consecate/sanctify · type=action · object=Kedesh · object_type=thing · experiencer=other · valence=commanded

#### 1Sa 7:1
> 1Sa 7:1 And the men of Kiriath-jearim came and took up the ark of the Lord and brought it to the house of Abinadab on the hill . And they consecrated his son Eleazar to have charge of the ark of the Lord .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpp3cp · stem=Piel · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=son · object_type=person · experiencer=other · divine_involvement=object · valence=righteous · immediate_response=charge ark

#### 1Sa 16:5
> 1Sa 16:5 And he said , “ Peaceably ; I have come to sacrifice to the Lord . Consecrate yourselves, and come with me to the sacrifice .” And he consecrated Jesse and his sons and invited them to the sacrifice .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtv2mp · stem=Hithpael · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · object=sacrifice · object_type=person · experiencer=other (addressed) · valence=neutral
  - compound: sha.lom "peace" — partner; qa.ra "to call: call to" — partner
- **qa.ra (H7121G)** — to call: call to  [Hebrew · M37]  morph=HVqw3ms · stem=Qal · target=“invited”
  - sense=invited · lemma_meaning=call to/invite/entreat · type=action · faculty=volition · object=sacrifice · object_type=person · experiencer=other · valence=neutral
  - compound: sha.lom "peace" — partner; qa.dash "to consecrate: consecate" — partner

#### 1Sa 21:5
> 1Sa 21:5 And David answered the priest , “ Truly women have been kept from us as always when I go on an expedition. The vessels of the young men are holy even when it is an ordinary journey . How much more today will their vessels be holy ?”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVqi3ms · stem=Qal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · cause=going on a military expedition · cause_clause=today vessels holy · experiencer=other · valence=righteous
  - compound: a.tsar "to restrain" — partner
- **a.tsar (H6113)** — to restrain  [Hebrew · M30]  morph=HVqsfsa · stem=Qal · target=“kept”
  - sense=kept · lemma_meaning=to restrain, retain, close up, shut, withhold, refrain, stay, detain · type=action · object=always · object_type=person · cause=going on a military expedition · cause_clause=today vessels holy · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Sa 8:11
> 2Sa 8:11 These also King David dedicated to the Lord , together with the silver and gold that he dedicated from all the nations he subdued ,
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhp3ms · stem=Hiphil · target=“dedicated”
  - sense=dedicated · lemma_meaning=consecate/sanctify · type=action · object=Lord · object_type=God · experiencer=other · divine_involvement=object · valence=righteous · immediate_response=dedicated all

#### 2Sa 11:4
> 2Sa 11:4 So David sent messengers and took her, and she came to him, and he lay with her. ( Now she had been purifying herself from her uncleanness .) Then she returned to her house .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtrfsa · stem=Hithpael · target=“purifying”
  - sense=purifying · lemma_meaning=consecate/sanctify · type=action · object=uncleanness · object_type=person · valence=neutral
  - compound: tum.ah "uncleanness" — partner
- **tum.ah (H2932)** — uncleanness  [Hebrew · M12]  morph=HNcfsc · target=“uncleanness”
  - sense=uncleanness · lemma_meaning=uncleanness · type=status · how=returned (H7725) · object=her · object_type=person · experiencer=other · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner

#### 1Ki 8:64
> 1Ki 8:64 The same day the king consecrated the middle of the court that was before the house of the Lord , for there he offered the burnt offering and the grain offering and the fat pieces of the peace offerings , because the bronze altar that was before the Lord was too small to receive the burnt offering and the grain offering and the fat pieces of the peace offerings .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpp3ms · stem=Piel · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=middle · object_type=thing · cause=The bronze altar being too small for all the offerings · cause_clause=burnt offering grain offering fat peace offerings bronze altar that before · experiencer=other · valence=righteous

#### 1Ki 9:3
> 1Ki 9:3 And the Lord said to him, “I have heard your prayer and your plea , which you have made before me. I have consecrated this house that you have built , by putting my name there forever . My eyes and my heart will be there for all time .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp1cs · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · location=heart · object=house · object_type=thing · experiencer=self · divine_involvement=agent · valence=righteous
  - compound: lev "heart" — co-seated; cha.nan "be gracious" — partner; te.chin.nah "supplication" — partner
- **cha.nan (H2603A)** — be gracious  [Hebrew · M39]  morph=HVtp2ms · stem=Hithpael · target=“made”
  - sense=made · lemma_meaning=to be gracious, show favour, pity · type=action · faculty=['affect', 'cognition', 'perception'] · location=heart · object=before · object_type=person · experiencer=other (addressed) · divine_involvement=addressee · valence=righteous
  - compound: lev "heart" — co-seated; te.chin.nah "supplication" — partner; qa.dash "to consecrate: consecate" — partner
- **te.chin.nah (H8467)** — supplication  [Hebrew · M21]  morph=HNcfsc · target=“plea”
  - sense=plea · lemma_meaning=favour, supplication, supplication for favour · type=status · location=heart · how=said (H0559) · experiencer=other (addressed) · divine_involvement=addressee · valence=righteous
  - compound: lev "heart" — co-seated; cha.nan "be gracious" — partner; qa.dash "to consecrate: consecate" — partner
- **lev (H3820A)** — heart  [Hebrew · M47]  morph=HNcmsc · target=“heart”
  - sense=heart · lemma_meaning=inner man, mind, will, heart, understanding · type=status · faculty=['cognition', 'perception', 'volition', 'conscience'] · location=heart · object=all · object_type=God · experiencer=self · divine_involvement=possessor · intensity=all (all) · valence=righteous
  - compound: cha.nan "be gracious" — partner; te.chin.nah "supplication" — partner; qa.dash "to consecrate: consecate" — partner

#### 1Ki 9:7
> 1Ki 9:7 then I will cut off Israel from the land that I have given them, and the house that I have consecrated for my name I will cast out of my sight , and Israel will become a proverb and a byword among all peoples .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp1cs · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=name · object_type=thing · experiencer=self · valence=righteous
- **na.tan (H5414G)** — to give: give  [Hebrew · M12]  morph=HVqp1cs · stem=Qal · target=“given”
  - sense=given · lemma_meaning=give/deliver/send/produce · type=action · object=house · object_type=thing/abstract · experiencer=self · divine_involvement=UNRESOLVED · immediate_response=consecrated name
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Ki 4:9
> 2Ki 4:9 And she said to her husband , “ Behold now , I know that this is a holy man of God who is continually passing our way .
- **qa.dosh (H6918H)** — holy: saint  [Hebrew · M12 · **FOCUS**]  morph=HAamsa · target=“holy”
  - sense=holy · lemma_meaning=holy · type=quality · how=know (H3045) · cause=the man of God continually passing by her home · cause_clause=holy man God continually passing way · valence=righteous

#### 2Ki 10:20
> 2Ki 10:20 And Jehu ordered , “ Sanctify a solemn assembly for Baal .” So they proclaimed it.
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpv2mp · stem=Piel · target=“Sanctify”
  - sense=Sanctify · lemma_meaning=consecate/sanctify · type=action · object=solemn assembly · object_type=situation · experiencer=other (addressed) · valence=neutral
  - compound: qa.ra "to call: call out" — partner; a.tsa.rah "assembly" — partner
- **qa.ra (H7121I)** — to call: call out  [Hebrew · M37]  morph=HVqw3mp · stem=Qal · target=“proclaimed”
  - sense=proclaimed · lemma_meaning=call to/invite/entreat · type=action · faculty=volition · experiencer=other · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner; a.tsa.rah "assembly" — partner
- **a.tsa.rah (H6116)** — assembly  [Hebrew · M05]  morph=HNcfsa · target=“solemn assembly”
  - sense=solemn assembly · lemma_meaning=assembly, solemn assembly · type=status · how=ordered (H0559) · experiencer=other · valence=neutral
  - compound: qa.ra "to call: call out" — partner; qa.dash "to consecrate: consecate" — partner

#### 2Ki 12:18
> 2Ki 12:18 Jehoash king of Judah took all the sacred gifts that Jehoshaphat and Jehoram and Ahaziah his fathers , the kings of Judah , had dedicated , and his own sacred gifts , and all the gold that was found in the treasuries of the house of the Lord and of the king’s house , and sent these to Hazael king of Syria . Then Hazael went away from Jerusalem .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhp3cp · stem=Hiphil · target=“dedicated”
  - sense=dedicated · lemma_meaning=consecate/sanctify · type=action · object=sacred gifts · object_type=thing · experiencer=other · intensity=all (all) · valence=neutral · immediate_response=found treasuries

#### 1Ch 15:12
> 1Ch 15:12 and said to them, “ You are the heads of the fathers’ houses of the Levites . Consecrate yourselves , you and your brothers , so that you may bring up the ark of the Lord , the God of Israel , to the place that I have prepared for it .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtv2mp · stem=Hithpael · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · object=brothers · object_type=person · experiencer=other (addressed) · divine_involvement=object · valence=commanded · immediate_response=bring up ark

#### 1Ch 15:14
> 1Ch 15:14 So the priests and the Levites consecrated themselves to bring up the ark of the Lord , the God of Israel .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtw3mp · stem=Hithpael · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=ark · object_type=person · experiencer=other · divine_involvement=object · valence=commanded

#### 1Ch 18:11
> 1Ch 18:11 These also King David dedicated to the Lord , together with the silver and gold that he had carried off from all the nations , from Edom , Moab , the Ammonites , the Philistines , and Amalek .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhp3ms · stem=Hiphil · target=“dedicated”
  - sense=dedicated · lemma_meaning=consecate/sanctify · type=action · object=Lord · object_type=God · experiencer=other · divine_involvement=object · valence=righteous · immediate_response=carried off all

#### 1Ch 23:13
> 1Ch 23:13 The sons of Amram : Aaron and Moses . Aaron was set apart to dedicate the most holy things , that he and his sons forever should make offerings before the Lord and minister to him and pronounce blessings in his name forever .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhcc · stem=Hiphil · target=“dedicate”
  - sense=dedicate · lemma_meaning=consecate/sanctify · type=action · object=most · object_type=abstract · valence=commanded · immediate_response=offerings before

#### 1Ch 26:26
> 1Ch 26:26 This Shelomoth and his brothers were in charge of all the treasuries of the dedicated gifts that David the king and the heads of the fathers’ houses and the officers of the thousands and the hundreds and the commanders of the army had dedicated .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhp3ms · stem=Hiphil · target=“dedicated”
  - sense=dedicated · lemma_meaning=consecate/sanctify · type=action · experiencer=other · valence=righteous

#### 1Ch 26:27
> 1Ch 26:27 From spoil won in battles they dedicated gifts for the maintenance of the house of the Lord .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhp3cp · stem=Hiphil · target=“dedicated gifts”
  - sense=dedicated gifts · lemma_meaning=consecate/sanctify · type=action · origin=received-from-outside · object=house · object_type=thing · experiencer=other · valence=righteous

#### 1Ch 26:28
> 1Ch 26:28 Also all that Samuel the seer and Saul the son of Kish and Abner the son of Ner and Joab the son of Zeruiah had dedicated — all dedicated gifts were in the care of Shelomoth and his brothers .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhp3ms · stem=Hiphil · target=“dedicated”
  - sense=dedicated · lemma_meaning=consecate/sanctify · type=action · object=all · object_type=thing · experiencer=other · intensity=all (all) · valence=righteous

#### 2Ch 2:4
> 2Ch 2:4 Behold , I am about to build a house for the name of the Lord my God and dedicate it to him for the burning of incense of sweet spices before him, and for the regular arrangement of the showbread , and for burnt offerings morning and evening , on the Sabbaths and the new moons and the appointed feasts of the Lord our God , as ordained forever for Israel .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhcc · stem=Hiphil · target=“dedicate”
  - sense=dedicate · lemma_meaning=consecate/sanctify · type=action · object=incense · object_type=thing · divine_involvement=addressee · valence=commanded

#### 2Ch 5:11
> 2Ch 5:11 And when the priests came out of the Holy Place ( for all the priests who were present had consecrated themselves, without regard to their divisions ,
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtp3cp · stem=Hithpael · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=without · object_type=person · cause_clause=all priests present consecrated without regard divisions · experiencer=other · intensity=all (all) · valence=commanded
  - compound: sha.mar "to keep: careful" — partner
- **sha.mar (H8104J)** — to keep: careful  [Hebrew · M30]  morph=HVqcc · stem=Qal · target=“regard”
  - sense=regard · lemma_meaning=obey/observe · type=action · faculty=['perception', 'volition'] · object=divisions · object_type=abstract · cause_clause=all priests present consecrated without regard divisions · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Ch 7:7
> 2Ch 7:7 And Solomon consecrated the middle of the court that was before the house of the Lord , for there he offered the burnt offering and the fat of the peace offerings , because the bronze altar Solomon had made could not hold the burnt offering and the grain offering and the fat .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpw3ms · stem=Piel · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=middle · object_type=thing · cause_clause=there offered burnt offering fat peace offerings because bronze altar · experiencer=other · valence=righteous

#### 2Ch 7:16
> 2Ch 7:16 For now I have chosen and consecrated this house that my name may be there forever . My eyes and my heart will be there for all time .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp1cs · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · location=heart · object=house · object_type=thing · experiencer=self · valence=righteous
  - compound: ba.char "to choose" — partner
- **ba.char (H0977)** — to choose  [Hebrew · M37]  morph=HVqp1cs · stem=Qal · target=“chosen”
  - sense=chosen · lemma_meaning=to choose, elect, decide for · type=action · faculty=volition · location=heart · object=house · object_type=thing · experiencer=self · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner
- **lev (H3820A)** — heart  [Hebrew · M47]  morph=HNcmsc · target=“heart”
  - sense=heart · lemma_meaning=inner man, mind, will, heart, understanding · type=status · faculty=['cognition', 'perception', 'volition', 'conscience'] · location=heart · experiencer=self · divine_involvement=UNRESOLVED · intensity=all (all)
  - compound: ba.char "to choose" — partner; qa.dash "to consecrate: consecate" — partner

#### 2Ch 7:20
> 2Ch 7:20 then I will pluck you up from my land that I have given you, and this house that I have consecrated for my name , I will cast out of my sight , and I will make it a proverb and a byword among all peoples .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp1cs · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=name · object_type=thing · experiencer=self · valence=neutral
- **na.tan (H5414G)** — to give: give  [Hebrew · M12]  morph=HVqp1cs · stem=Qal · target=“given”
  - sense=given · lemma_meaning=give/deliver/send/produce · type=action · object=house · object_type=thing/abstract · experiencer=self · divine_involvement=UNRESOLVED · immediate_response=consecrated name
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Ch 26:18
> 2Ch 26:18 and they withstood King Uzziah and said to him, “It is not for you, Uzziah , to burn incense to the Lord , but for the priests , the sons of Aaron , who are consecrated to burn incense . Go out of the sanctuary , for you have done wrong , and it will bring you no honor from the Lord God .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVPsmpa · stem=Pual · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · cause_clause=sons Aaron consecrated burn incense Go out of sanctuary done wrong · divine_involvement=agent · valence=commanded
  - compound: ma.al "be unfaithful" — partner; ka.vod "glory" — partner
- **ma.al (H4603)** — be unfaithful  [Hebrew · M10]  morph=HVqp2ms · stem=Qal · target=“done wrong”
  - sense=done wrong · lemma_meaning=to act unfaithfully, act treacherously, transgress, commit a trespass · type=action · origin=received-from-outside · object=honor · object_type=God · cause=unlawfully burning incense in the sanctuary · cause_clause=sons Aaron consecrated burn incense Go out of sanctuary done wrong · experiencer=other (addressed) · valence=sinful
  - compound: ka.vod "glory" — partner; qa.dash "to consecrate: consecate" — partner
- **ka.vod (H3519)** — glory  [Hebrew · M22]  morph=HNcmsa · target=“honor”
  - sense=honor · lemma_meaning=glory, honour, glorious, abundance · type=status · faculty=affect · how=done wrong (H4603) · cause_clause=sons Aaron consecrated burn incense Go out of sanctuary done wrong · experiencer=other (addressed) · valence=neutral
  - compound: ma.al "be unfaithful" — partner; qa.dash "to consecrate: consecate" — partner

#### 2Ch 29:5
> 2Ch 29:5 and said to them, “ Hear me, Levites ! Now consecrate yourselves, and consecrate the house of the Lord , the God of your fathers , and carry out the filth from the Holy Place .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtv2mp · stem=Hithpael · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=house · object_type=person · experiencer=other (addressed) · divine_involvement=object · valence=commanded
  - compound: nid.dah "impurity" — partner
- **nid.dah (H5079)** — impurity  [Hebrew · M10]  morph=HNcfsa · target=“filth”
  - sense=filth · lemma_meaning=impurity, filthiness, menstruous, set apart · type=status · origin=received-from-outside · how=carry out (H3318) · experiencer=other (addressed) · valence=sinful · relational=from
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Ch 29:15
> 2Ch 29:15 They gathered their brothers and consecrated themselves and went in as the king had commanded , by the words of the Lord , to cleanse the house of the Lord .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtw3mp · stem=Hithpael · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=king · object_type=person · experiencer=other · valence=commanded
  - compound: ta.her "be pure" — partner
- **ta.her (H2891)** — be pure  [Hebrew · M12]  morph=HVpcc · stem=Piel · target=“cleanse”
  - sense=cleanse · lemma_meaning=to be clean, be pure · type=action · object=house · object_type=thing · valence=commanded · relational=to
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Ch 29:17
> 2Ch 29:17 They began to consecrate on the first day of the first month , and on the eighth day of the month they came to the vestibule of the Lord . Then for eight days they consecrated the house of the Lord , and on the sixteenth day of the first month they finished .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=first · object_type=thing · valence=commanded · immediate_response=came vestibule · relational=on

#### 2Ch 29:19
> 2Ch 29:19 All the utensils that King Ahaz discarded in his reign when he was faithless , we have made ready and consecrated , and behold , they are before the altar of the Lord .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp1cp · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=before · object_type=thing · experiencer=self · valence=commanded
  - compound: ma.al "unfaithfulness" — partner
- **ma.al (H4604)** — unfaithfulness  [Hebrew · M10]  morph=HNcmsc · target=“faithless”
  - sense=faithless · lemma_meaning=unfaithful or treacherous act, trespass · type=status · how=discarded (H2186) · object=reign · object_type=God · experiencer=other · valence=sinful
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Ch 29:34
> 2Ch 29:34 But the priests were too few and could not flay all the burnt offerings , so until other priests had consecrated themselves, their brothers the Levites helped them, until the work was finished — for the Levites were more upright in heart than the priests in consecrating themselves.
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVti3mp · stem=Hithpael · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · location=heart · object=brothers · object_type=person · cause_clause=more upright heart priests consecrating · experiencer=other · intensity=all (all) · valence=commanded
  - compound: ya.shar "upright:right" — partner
- **ya.shar (H3477G)** — upright:right  [Hebrew · M13]  morph=HAampc · target=“more upright”
  - sense=more upright · lemma_meaning=straight, upright, correct, right · type=quality · faculty=moral_evaluation · location=heart · how=helped (H2388) · cause_clause=more upright heart priests consecrating · valence=righteous
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Ch 30:3
> 2Ch 30:3 for they could not keep it at that time because the priests had not consecrated themselves in sufficient number , nor had the people assembled in Jerusalem —
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtp3cp · stem=Hithpael · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=sufficient number · object_type=person · cause_clause=could not keep at time because priests not · experiencer=other · valence=commanded · immediate_response=assembled Jerusalem

#### 2Ch 30:8
> 2Ch 30:8 Do not now be stiff-necked as your fathers were, but yield yourselves to the Lord and come to his sanctuary , which he has consecrated forever , and serve the Lord your God , that his fierce anger may turn away from you.
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp3ms · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=forever · object_type=thing · experiencer=other · divine_involvement=agent · valence=commanded
  - compound: cha.ron "burning anger" — partner; a.vad "to serve: minister" — partner
- **cha.ron (H2740)** — burning anger  [Hebrew · M02]  morph=HNcmsc · target=“fierce”
  - sense=fierce · lemma_meaning=anger, heat, burning (of anger) · type=status · faculty=affect · how=turn away (H7725) · object=anger · object_type=God · experiencer=other (addressed) · divine_involvement=possessor · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner; a.vad "to serve: minister" — partner
- **a.vad (H5647H)** — to serve: minister  [Hebrew · M36]  morph=HVqv2mp · stem=Qal · target=“serve”
  - sense=serve · lemma_meaning=serve[someone] · type=action · object=Lord · object_type=God · experiencer=other (addressed) · divine_involvement=addressee · valence=commanded
  - compound: cha.ron "burning anger" — partner; qa.dash "to consecrate: consecate" — partner
- **na.tan (H5414G)** — to give: give  [Hebrew · M12]  morph=HVqv2mp · stem=Qal · target=“yield”
  - sense=yield · lemma_meaning=give/deliver/send/produce · type=action · object=yourselves · object_type=thing/abstract · experiencer=other (addressed) · divine_involvement=UNRESOLVED · valence=forbidden
  - compound: cha.ron "burning anger" — partner; qa.dash "to consecrate: consecate" — partner; a.vad "to serve: minister" — partner

#### 2Ch 30:15
> 2Ch 30:15 And they slaughtered the Passover lamb on the fourteenth day of the second month . And the priests and the Levites were ashamed , so that they consecrated themselves and brought burnt offerings into the house of the Lord .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtw3mp · stem=Hithpael · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=burnt offerings · object_type=person · experiencer=other · valence=commanded
  - compound: ka.lam "be humiliated" — partner
- **ka.lam (H3637)** — be humiliated  [Hebrew · M07]  morph=HVNp3cp · stem=Niphal · target=“ashamed”
  - sense=ashamed · lemma_meaning=to insult, shame, humiliate, blush, be ashamed, be put to shame, be re · type=action · faculty=affect · object=burnt offerings · object_type=person · experiencer=other · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Ch 30:17
> 2Ch 30:17 For there were many in the assembly who had not consecrated themselves. Therefore the Levites had to slaughter the Passover lamb for everyone who was not clean , to consecrate it to the Lord .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtp3cp · stem=Hithpael · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=Levites · object_type=person · cause=assembly members being unclean · cause_clause=assembly who not consecrated Levites slaughter Passover lamb everyone · experiencer=other · valence=commanded · immediate_response=consecrate Lord
  - compound: ta.hor "pure" — partner
- **ta.hor (H2889)** — pure  [Hebrew · M12]  morph=HAamsa · target=“clean”
  - sense=clean · lemma_meaning=pure, clean · type=quality · cause_clause=assembly who not consecrated Levites slaughter Passover lamb everyone · intensity=all (everyone) · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### 2Ch 30:24
> 2Ch 30:24 For Hezekiah king of Judah gave the assembly 1,000 bulls and 7,000 sheep for offerings, and the princes gave the assembly 1,000 bulls and 10,000 sheep . And the priests consecrated themselves in great numbers .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtw3mp · stem=Hithpael · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=great numbers · object_type=person · cause=Hezekiah and princes giving abundant offerings · cause_clause=king Judah gave assembly 1,000 bulls 7,000 sheep · experiencer=other · valence=righteous
  - compound: rum "to exalt" — partner

#### 2Ch 31:6
> 2Ch 31:6 And the people of Israel and Judah who lived in the cities of Judah also brought in the tithe of cattle and sheep , and the tithe of the dedicated things that had been dedicated to the Lord their God , and laid them in heaps .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVPsmpa · stem=Pual · target=“dedicated”
  - sense=dedicated · lemma_meaning=consecate/sanctify · type=action · object=Lord · object_type=God · divine_involvement=object · valence=righteous

#### 2Ch 31:18
> 2Ch 31:18 They were enrolled with all their little children , their wives , their sons , and their daughters , the whole assembly , for they were faithful in keeping themselves holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVti3mp · stem=Hithpael · target=“keeping”
  - sense=keeping · lemma_meaning=consecate/sanctify · type=action · object=holy · object_type=person · cause=faithful keeping of holiness · cause_clause=faithful keeping holy · experiencer=other · valence=righteous
  - compound: e.mu.nah "faithfulness" — partner; qo.desh "holiness" — partner
- **e.mu.nah (H0530)** — faithfulness  [Hebrew · M13]  morph=HNcfsc · target=“faithful”
  - sense=faithful · lemma_meaning=firmness, fidelity, steadfastness, steadiness · type=status · how=keeping (H6942) · cause_clause=faithful keeping holy · experiencer=other · intensity=all (whole) · valence=righteous
  - compound: qa.dash "to consecrate: consecate" — partner; qo.desh "holiness" — partner
- **qo.desh (H6944G)** — holiness  [Hebrew · M22]  morph=HNcmsa · target=“holy”
  - sense=holy · lemma_meaning=apartness, holiness, sacredness, separateness · type=status · how=keeping (H6942) · cause_clause=faithful keeping holy · experiencer=other · valence=righteous
  - compound: e.mu.nah "faithfulness" — partner; qa.dash "to consecrate: consecate" — partner

#### 2Ch 35:6
> 2Ch 35:6 And slaughter the Passover lamb , and consecrate yourselves, and prepare for your brothers , to do according to the word of the Lord by Moses .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtv2mp · stem=Hithpael · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=brothers · object_type=abstract · experiencer=other (addressed) · valence=commanded

#### 2Ch 36:14
> 2Ch 36:14 All the officers of the priests and the people likewise were exceedingly unfaithful , following all the abominations of the nations . And they polluted the house of the Lord that he had made holy in Jerusalem .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp3ms · stem=Hiphil · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=Jerusalem · object_type=thing · experiencer=other · divine_involvement=object · valence=righteous
  - compound: to.e.vah "abomination" — partner; ra.vah "to multiply" — partner; ma.al "be unfaithful" — partner; ma.al "unfaithfulness" — partner; ta.me "to defile" — partner
- **ma.al (H4604)** — unfaithfulness  [Hebrew · M10]  morph=HNcmsa · target=“exceedingly”
  - sense=exceedingly · lemma_meaning=unfaithful or treacherous act, trespass · type=status · intensity=all (all) · valence=sinful
  - compound: to.e.vah "abomination" — partner; ra.vah "to multiply" — partner; ma.al "be unfaithful" — partner; qa.dash "to consecrate: consecate" — partner; ta.me "to defile" — partner
- **ma.al (H4603)** — be unfaithful  [Hebrew · M10]  morph=HVqcc · stem=Qal · target=“unfaithful”
  - sense=unfaithful · lemma_meaning=to act unfaithfully, act treacherously, transgress, commit a trespass · type=action · object=all · object_type=God · divine_involvement=object · intensity=all (all) · valence=sinful
  - compound: to.e.vah "abomination" — partner; ra.vah "to multiply" — partner; ma.al "unfaithfulness" — partner; qa.dash "to consecrate: consecate" — partner; ta.me "to defile" — partner
- **ta.me (H2930A)** — to defile  [Hebrew · M10]  morph=HVpw3mp · stem=Piel · target=“polluted”
  - sense=polluted · lemma_meaning=to be unclean, become unclean, become impure · type=action · object=house · object_type=thing · experiencer=other · divine_involvement=object · intensity=all (all) · valence=sinful
  - compound: to.e.vah "abomination" — partner; ra.vah "to multiply" — partner; ma.al "be unfaithful" — partner; ma.al "unfaithfulness" — partner; qa.dash "to consecrate: consecate" — partner
- **ra.vah (H7235A)** — to multiply  [Hebrew · M23]  morph=HVhp3cp · stem=Hiphil · target=“exceedingly”
  - sense=exceedingly · lemma_meaning=be or become great, be or become many, be or become much, be or become · type=status · intensity=all (all) · valence=sinful
  - compound: to.e.vah "abomination" — partner; ma.al "be unfaithful" — partner; ma.al "unfaithfulness" — partner; qa.dash "to consecrate: consecate" — partner; ta.me "to defile" — partner
- **to.e.vah (H8441)** — abomination  [Hebrew · M10]  morph=HNcfpc · target=“abominations”
  - sense=abominations · lemma_meaning=a disgusting thing, abomination, abominable · type=status · faculty=moral_evaluation · how=polluted (H2930) · object=house · object_type=abstract · experiencer=other · intensity=all (all) · valence=sinful
  - compound: ra.vah "to multiply" — partner; ma.al "be unfaithful" — partner; ma.al "unfaithfulness" — partner; qa.dash "to consecrate: consecate" — partner; ta.me "to defile" — partner

#### Ezr 3:5
> Ezr 3:5 and after that the regular burnt offerings, the offerings at the new moon and at all the appointed feasts of the Lord , and the offerings of everyone who made a freewill offering to the Lord .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVPsmpa · stem=Pual · target=“appointed”
  - sense=appointed · lemma_meaning=consecate/sanctify · type=action · object=feasts · object_type=thing · intensity=['all (all)', 'all (everyone)'] · valence=commanded · immediate_response=made freewill offering
  - compound: na.dav "be willing" — partner
- **na.dav (H5068)** — be willing  [Hebrew · M29]  morph=HVtrmsa · stem=Hithpael · target=“made”
  - sense=made · lemma_meaning=to incite, impel, make willing · type=action · faculty=volition · object=freewill offering · object_type=thing · intensity=all (everyone) · valence=righteous
  - compound: qa.dash "to consecrate: consecate" — partner

#### Neh 3:1
> Neh 3:1 Then Eliashib the high priest rose up with his brothers the priests , and they built the Sheep Gate . They consecrated it and set its doors . They consecrated it as far as the Tower of the Hundred , as far as the Tower of Hananel .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpp3cp · stem=Piel · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=doors · object_type=thing · experiencer=other · valence=commanded
  - compound: et "[Obj.]" — qualifier

#### Neh 12:47
> Neh 12:47 And all Israel in the days of Zerubbabel and in the days of Nehemiah gave the daily portions for the singers and the gatekeepers ; and they set apart that which was for the Levites ; and the Levites set apart that which was for the sons of Aaron .
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhrmpa · stem=Hiphil · target=“set apart”
  - sense=set apart · lemma_meaning=consecate/sanctify · type=action · object=Levites · object_type=thing · valence=righteous · immediate_response=set apart sons

#### Neh 13:22
> Neh 13:22 Then I commanded the Levites that they should purify themselves and come and guard the gates , to keep the Sabbath day holy . Remember this also in my favor, O my God , and spare me according to the greatness of your steadfast love .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · valence=commanded
  - compound: che.sed "kindness" — partner; rov "abundance" — partner; za.khar "to remember" — partner; gam "also" — qualifier; che.sed "shame" — partner; chus "to pity" — partner; ta.her "be pure" — partner
- **chus (H2347)** — to pity  [Hebrew · M05]  morph=HVqv2ms · stem=Qal · target=“spare”
  - sense=spare · lemma_meaning=(Qal) to pity, have compassion, spare, look upon with compassion · type=action · faculty=affect · object=greatness · object_type=person · experiencer=other (addressed) · valence=righteous · relational=me
  - compound: che.sed "kindness" — partner; qa.dash "to consecrate: consecate" — partner; rov "abundance" — partner; za.khar "to remember" — partner; gam "also" — qualifier; che.sed "shame" — partner; ta.her "be pure" — partner
- **che.sed (H2617B)** — shame  [Hebrew · M05]  morph=HNcmsc · target=“steadfast love”
  - sense=steadfast love · lemma_meaning=goodness, kindness, faithfulness · type=status · faculty=affect · how=spare (H2347) · experiencer=other (addressed) · valence=righteous
  - compound: che.sed "kindness" — partner; qa.dash "to consecrate: consecate" — partner; rov "abundance" — partner; za.khar "to remember" — partner; gam "also" — qualifier; chus "to pity" — partner; ta.her "be pure" — partner
- **che.sed (H2617A)** — kindness  [Hebrew · M05]  morph=HNcmsc · target=“steadfast love”
  - sense=steadfast love · lemma_meaning=goodness, kindness, faithfulness · type=status · how=spare (H2347) · experiencer=other (addressed) · divine_involvement=possessor · valence=righteous
  - compound: qa.dash "to consecrate: consecate" — partner; rov "abundance" — partner; za.khar "to remember" — partner; gam "also" — qualifier; che.sed "shame" — partner; chus "to pity" — partner; ta.her "be pure" — partner
- **za.khar (H2142)** — to remember  [Hebrew · M41]  morph=HVqv2ms · stem=Qal · target=“Remember”
  - sense=Remember · lemma_meaning=to remember, recall, call to mind · type=action · faculty=['cognition', 'memory'] · object=God · object_type=God · experiencer=other (addressed) · divine_involvement=addressee · valence=righteous
  - compound: che.sed "kindness" — partner; qa.dash "to consecrate: consecate" — partner; rov "abundance" — partner; gam "also" — qualifier; che.sed "shame" — partner; chus "to pity" — partner; ta.her "be pure" — partner
- **ta.her (H2891)** — be pure  [Hebrew · M12]  morph=HVtrmpa · stem=Hithpael · target=“purify themselves”
  - sense=purify themselves · lemma_meaning=to be clean, be pure · type=action · object=gates · object_type=person · valence=commanded
  - compound: che.sed "kindness" — partner; qa.dash "to consecrate: consecate" — partner; rov "abundance" — partner; za.khar "to remember" — partner; gam "also" — qualifier; che.sed "shame" — partner; chus "to pity" — partner
- **rov (H7230)** — abundance  [Hebrew · M46]  morph=HNcmsc · target=“greatness”
  - sense=greatness · lemma_meaning=multitude, abundance, greatness · type=status · how=spare (H2347) · experiencer=self · valence=righteous · relational=me
  - compound: che.sed "kindness" — partner; qa.dash "to consecrate: consecate" — partner; za.khar "to remember" — partner; gam "also" — qualifier; che.sed "shame" — partner; chus "to pity" — partner; ta.her "be pure" — partner
- **che.sed (H2617B)** — shame  [Hebrew · M05]  morph=HNcmsc · target=“steadfast love”
  - sense=steadfast love · lemma_meaning=goodness, kindness, faithfulness · type=status · faculty=affect · how=spare (H2347) · experiencer=other (addressed) · valence=righteous
  - compound: che.sed "kindness" — partner; qa.dash "to consecrate: consecate" — partner; rov "abundance" — partner; za.khar "to remember" — partner; gam "also" — qualifier; chus "to pity" — partner; ta.her "be pure" — partner

#### Job 1:5
> Job 1:5 And when the days of the feast had run their course , Job would send and consecrate them, and he would rise early in the morning and offer burnt offerings according to the number of them all . For Job said , “It may be that my children have sinned , and cursed God in their hearts .” Thus Job did continually .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpw3ms · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · location=heart · object=morning · object_type=person · cause=possibility that his children sinned · cause_clause=days feast course Job send consecrate rise morning · experiencer=other · valence=righteous
  - compound: le.vav "heart" — co-seated; kol "all" — qualifier; ba.rakh "to bless" — partner; cha.ta "to sin" — partner
- **kol (H3605)** — all  [Hebrew · T2]  morph=HNcmsc · target=“all”
  - sense=all · lemma_meaning=all, the whole · type=status · location=heart · how=offer (H5927) · object=burnt offerings · object_type=thing/abstract · cause=pending-read · cause_clause=days feast course Job send consecrate rise morning · experiencer=other · divine_involvement=UNRESOLVED · intensity=all (all)
  - compound: le.vav "heart" — co-seated; qa.dash "to consecrate: consecate" — partner; ba.rakh "to bless" — partner; cha.ta "to sin" — partner
- **cha.ta (H2398)** — to sin  [Hebrew · M10]  morph=HVqp3cp · stem=Qal · target=“sinned”
  - sense=sinned · lemma_meaning=to sin, miss, miss the way, go wrong, incur guilt, forfeit, purify fro · type=action · faculty=moral_evaluation · location=heart · object=God · object_type=God · cause_clause=days feast course Job send consecrate rise morning · experiencer=other · valence=sinful
  - compound: le.vav "heart" — co-seated; qa.dash "to consecrate: consecate" — partner; kol "all" — qualifier; ba.rakh "to bless" — partner
- **le.vav (H3824)** — heart  [Hebrew · M47]  morph=HNcmsc · target=“hearts”
  - sense=hearts · lemma_meaning=inner man, mind, will, heart, soul, understanding · type=status · faculty=['cognition', 'perception', 'volition', 'conscience'] · location=heart · how=did (H6213) · object=continually · object_type=abstract · cause_clause=days feast course Job send consecrate rise morning · experiencer=other · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner; kol "all" — qualifier; ba.rakh "to bless" — partner; cha.ta "to sin" — partner
- **ba.rakh (H1288)** — to bless  [Hebrew · M39]  morph=HVpq3cp · stem=Piel · target=“cursed”
  - sense=cursed · lemma_meaning=to bless, kneel · type=action · location=heart · object=God · object_type=God · cause_clause=days feast course Job send consecrate rise morning · experiencer=other · divine_involvement=object · valence=sinful
  - compound: le.vav "heart" — co-seated; qa.dash "to consecrate: consecate" — partner; kol "all" — qualifier; cha.ta "to sin" — partner

#### Psa 16:3
> Psa 16:3 As for the saints in the land , they are the excellent ones , in whom is all my delight .
- **qa.dosh (H6918H)** — holy: saint  [Hebrew · M12 · **FOCUS**]  morph=HAampa · target=“saints”
  - sense=saints · lemma_meaning=holy · type=quality · valence=righteous · relational=As
  - compound: che.phets "pleasure" — partner
- **che.phets (H2656)** — pleasure  [Hebrew · M04]  morph=HNcmsc · target=“delight”
  - sense=delight · lemma_meaning=delight, pleasure · type=status · faculty=affect · experiencer=self · intensity=all (all)
  - compound: qa.dosh "holy: saint" — partner

#### Psa 34:9
> Psa 34:9 Oh, fear the Lord , you his saints , for those who fear him have no lack !
- **qa.dosh (H6918H)** — holy: saint  [Hebrew · M12 · **FOCUS**]  morph=HAampc · target=“saints”
  - sense=saints · lemma_meaning=holy · type=quality · how=fear (H3372) · cause_clause=fear no lack · experiencer=other · valence=righteous
  - compound: ya.re "to fear: revere" — partner; ya.re "afraid" — partner
- **ya.re (H3372H)** — to fear: revere  [Hebrew · M01]  morph=HVqv2mp · stem=Qal · target=“fear”
  - sense=fear · lemma_meaning=frightening(DANGER) · type=action · faculty=affect · object=Lord · object_type=God · cause_clause=fear no lack · experiencer=other (addressed) · divine_involvement=object · valence=commanded
  - compound: ya.re "afraid" — partner; qa.dosh "holy: saint" — partner
- **ya.re (H3373)** — afraid  [Hebrew · M01]  morph=HAampc · target=“fear”
  - sense=fear · lemma_meaning=fearing, reverent, afraid · type=quality · faculty=affect · how=fear (H3372) · cause_clause=fear no lack · experiencer=other · divine_involvement=object · valence=righteous
  - compound: ya.re "to fear: revere" — partner; qa.dosh "holy: saint" — partner

#### Psa 106:16
> Psa 106:16 When men in the camp were jealous of Moses and Aaron , the holy one of the Lord ,
- **qa.dosh (H6918H)** — holy: saint  [Hebrew · M12 · **FOCUS**]  morph=HAamsc · target=“holy one”
  - sense=holy one · lemma_meaning=holy · type=quality · how=jealous (H7065) · divine_involvement=object · valence=neutral
  - compound: qa.na "be jealous" — partner
- **qa.na (H7065)** — be jealous  [Hebrew · M02]  morph=HVpw3mp · stem=Piel · target=“jealous”
  - sense=jealous · lemma_meaning=to envy, be jealous, be envious, be zealous · type=action · faculty=affect · object=Moses · object_type=person · experiencer=other · valence=sinful
  - compound: qa.dosh "holy: saint" — partner

#### Isa 5:16
> Isa 5:16 But the Lord of hosts is exalted in justice , and the Holy God shows himself holy in righteousness .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVNrmsa · stem=Niphal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=righteousness · object_type=God · divine_involvement=agent · valence=righteous
  - compound: ga.vah "to exult" — partner; tse.da.qah "righteousness" — partner; el "God" — qualifier; mish.pat "justice" — partner
- **mish.pat (H4941H)** — justice  [Hebrew · M26]  morph=HNcmsa · target=“justice”
  - sense=justice · lemma_meaning=judgement/punishment · type=status · faculty=moral_evaluation · how=exalted (H1361) · experiencer=other · divine_involvement=agent · valence=righteous · immediate_response=holy righteousness
  - compound: ga.vah "to exult" — partner; qa.dash "to consecrate: consecate" — partner; tse.da.qah "righteousness" — partner; el "God" — qualifier
- **tse.da.qah (H6666)** — righteousness  [Hebrew · M26]  morph=HNcfsa · target=“righteousness”
  - sense=righteousness · lemma_meaning=justice, righteousness · type=status · faculty=moral_evaluation · divine_involvement=agent · valence=righteous
  - compound: ga.vah "to exult" — partner; qa.dash "to consecrate: consecate" — partner; el "God" — qualifier; mish.pat "justice" — partner
- **el (H0410G)** — God  [Hebrew · T2]  morph=HNcmsa · target=“God”
  - sense=God · lemma_meaning=The Deity · type=status · faculty=moral_evaluation · how=exalted (H1361) · object=justice · object_type=thing/abstract · experiencer=other · divine_involvement=UNRESOLVED
  - compound: ga.vah "to exult" — partner; qa.dash "to consecrate: consecate" — partner; tse.da.qah "righteousness" — partner; mish.pat "justice" — partner

#### Isa 8:13
> Isa 8:13 But the Lord of hosts , him you shall honor as holy . Let him be your fear , and let him be your dread .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhi2mp · stem=Hiphil · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=fear · object_type=God · experiencer=other (addressed) · divine_involvement=object · valence=commanded · immediate_response=dread
  - compound: mo.rah "fear" — partner; a.rats "to tremble" — partner; et "[Obj.]" — qualifier; mo.rah "fear" — partner
- **mo.rah (H4172A)** — fear  [Hebrew · M01]  morph=HNcmsc · target=“fear”
  - sense=fear · lemma_meaning=fear, reverence, terror · type=status · faculty=affect · how=holy (H6942) · object=him · object_type=person · divine_involvement=object · valence=commanded
  - compound: a.rats "to tremble" — partner; et "[Obj.]" — qualifier; qa.dash "to consecrate: consecate" — partner; mo.rah "fear" — partner
- **mo.ra (H4172B)** — fear  [Hebrew · M01]  morph=HNcmsc · target=“fear”
  - sense=fear · lemma_meaning=fear, reverence, terror · type=status · faculty=affect · how=holy (H6942) · object=him · object_type=person · divine_involvement=object · valence=commanded
  - compound: mo.rah "fear" — partner; a.rats "to tremble" — partner; et "[Obj.]" — qualifier; qa.dash "to consecrate: consecate" — partner
- **a.rats (H6206)** — to tremble  [Hebrew · M01]  morph=HVhrmsc · stem=Hiphil · target=“dread”
  - sense=dread · lemma_meaning=to tremble, dread, fear, oppress, prevail, break, be terrified, cause  · type=action · faculty=affect · divine_involvement=object · valence=commanded
  - compound: mo.rah "fear" — partner; et "[Obj.]" — qualifier; qa.dash "to consecrate: consecate" — partner; mo.rah "fear" — partner

#### Isa 13:3
> Isa 13:3 I myself have commanded my consecrated ones , and have summoned my mighty men to execute my anger , my proudly exulting ones .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVPsmpc · stem=Pual · target=“consecrated ones”
  - sense=consecrated ones · lemma_meaning=consecate/sanctify · type=action · object=mighty men · object_type=person · valence=righteous
  - compound: ga.a.vah "pride" — partner; qa.ra "to call: call to" — partner; a.ni "I" — qualifier
- **qa.ra (H7121G)** — to call: call to  [Hebrew · M37]  morph=HVqp1cs · stem=Qal · target=“summoned”
  - sense=summoned · lemma_meaning=call to/invite/entreat · type=action · faculty=volition · object=mighty men · object_type=person · experiencer=self · divine_involvement=agent · valence=neutral
  - compound: ga.a.vah "pride" — partner; qa.dash "to consecrate: consecate" — partner; a.ni "I" — qualifier

#### Isa 29:23
> Isa 29:23 For when he sees his children , the work of my hands , in his midst , they will sanctify my name ; they will sanctify the Holy One of Jacob and will stand in awe of the God of Israel .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhi3mp · stem=Hiphil · target=“sanctify”
  - sense=sanctify · lemma_meaning=consecate/sanctify · type=action · object=name · object_type=God · cause=seeing the work of God's hands among his children · cause_clause=sees children work hands midst they sanctify name · experiencer=other · divine_involvement=object · valence=righteous
  - compound: a.rats "to tremble" — partner; ra.ah "to see: see" — qualifier; qa.dosh "holy" — partner
- **ra.ah (H7200G)** — to see: see  [Hebrew · T2]  morph=HVqcc · stem=Qal · target=“sees”
  - sense=sees · lemma_meaning=see/show · type=action · faculty=['cognition', 'perception', 'volition'] · location=UNRESOLVED · object=children · object_type=thing/abstract · cause=pending-read · cause_clause=sees children work hands midst they sanctify name · divine_involvement=UNRESOLVED
  - compound: a.rats "to tremble" — partner; qa.dash "to consecrate: consecate" — partner; qa.dosh "holy" — partner
- **a.rats (H6206)** — to tremble  [Hebrew · M01]  morph=HVhi3mp · stem=Hiphil · target=“awe”
  - sense=awe · lemma_meaning=to tremble, dread, fear, oppress, prevail, break, be terrified, cause  · type=action · faculty=affect · object=God · object_type=God · cause=seeing children as work of God's hands · cause_clause=sees children work hands midst they sanctify name · experiencer=other · divine_involvement=object · valence=righteous
  - compound: qa.dash "to consecrate: consecate" — partner; ra.ah "to see: see" — qualifier; qa.dosh "holy" — partner
- **qa.dosh (H6918G)** — holy  [Hebrew · M22]  morph=HAamsc · target=“Holy One”
  - sense=Holy One · lemma_meaning=holy · type=quality · how=sanctify (H6942) · cause_clause=sees children work hands midst they sanctify name · experiencer=self · divine_involvement=object · valence=righteous
  - compound: a.rats "to tremble" — partner; qa.dash "to consecrate: consecate" — partner; ra.ah "to see: see" — qualifier

#### Isa 30:29
> Isa 30:29 You shall have a song as in the night when a holy feast is kept, and gladness of heart , as when one sets out to the sound of the flute to go to the mountain of the Lord , to the Rock of Israel .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtcc · stem=Hithpael · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · location=heart · object=feast · object_type=situation · divine_involvement=object · valence=righteous · immediate_response=sets out flute
  - compound: le.vav "heart" — co-seated; sim.chah "joy" — partner; el "to[wards]" — qualifier
- **sim.chah (H8057)** — joy  [Hebrew · M04]  morph=HNcfsc · target=“gladness”
  - sense=gladness · lemma_meaning=joy, mirth, gladness · type=status · faculty=affect · location=heart · object=heart · object_type=situation · valence=righteous
  - compound: le.vav "heart" — co-seated; el "to[wards]" — qualifier; qa.dash "to consecrate: consecate" — partner
- **le.vav (H3824)** — heart  [Hebrew · M47]  morph=HNcmsa · target=“heart”
  - sense=heart · lemma_meaning=inner man, mind, will, heart, soul, understanding · type=status · faculty=['cognition', 'perception', 'volition', 'conscience'] · location=heart · valence=righteous · relational=as
  - compound: sim.chah "joy" — partner; el "to[wards]" — qualifier; qa.dash "to consecrate: consecate" — partner

#### Isa 65:5
> Isa 65:5 who say , “ Keep to yourself, do not come near me, for I am too holy for you.” These are a smoke in my nostrils , a fire that burns all the day .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVqp1cs · stem=Qal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=smoke · object_type=person · cause_clause=holy These smoke nostrils fire burns all day · experiencer=self · valence=sinful

#### Isa 66:17
> Isa 66:17 “Those who sanctify and purify themselves to go into the gardens , following one in the midst , eating pig’s flesh and the abomination and mice , shall come to an end together , declares the Lord .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVtrmpa · stem=Hithpael · target=“sanctify”
  - sense=sanctify · lemma_meaning=consecate/sanctify · type=action · location=flesh · object=gardens · object_type=person · valence=sinful
  - compound: she.qets "detestation" — partner; ta.her "be pure" — partner
- **she.qets (H8263)** — detestation  [Hebrew · M06]  morph=HNcmsa · target=“abomination”
  - sense=abomination · lemma_meaning=detestable thing or idol, an unclean thing, an abomination, detestatio · type=status · location=flesh · how=end (H5486) · valence=sinful
  - compound: qa.dash "to consecrate: consecate" — partner; ta.her "be pure" — partner
- **ta.her (H2891)** — be pure  [Hebrew · M12]  morph=HVtrmpa · stem=Hithpael · target=“purify themselves”
  - sense=purify themselves · lemma_meaning=to be clean, be pure · type=action · location=flesh · object=gardens · object_type=person · valence=sinful · relational=to
  - compound: she.qets "detestation" — partner; qa.dash "to consecrate: consecate" — partner

#### Jer 1:5
> Jer 1:5 “ Before I formed you in the womb I knew you, and before you were born I consecrated you; I appointed you a prophet to the nations .”
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhp1cs · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=you · object_type=person · experiencer=self · divine_involvement=agent · valence=righteous

#### Jer 6:4
> Jer 6:4 “ Prepare war against her; arise , and let us attack at noon ! Woe to us, for the day declines , for the shadows of evening lengthen !
- **qa.dash (H6942J)** — to consecrate: prepare  [Hebrew · M12 · **FOCUS**]  morph=HVpv2mp · stem=Piel · target=“Prepare”
  - sense=Prepare · lemma_meaning=consecate/sanctify · type=action · object=war · object_type=situation · cause_clause=day declines for shadows evening lengthen · experiencer=other (addressed)

#### Jer 12:3
> Jer 12:3 But you , O Lord , know me; you see me, and test my heart toward you. Pull them out like sheep for the slaughter , and set them apart for the day of slaughter .
- **qa.dash (H6942J)** — to consecrate: prepare  [Hebrew · M12 · **FOCUS**]  morph=HVhv2ms · stem=Hiphil · target=“apart”
  - sense=apart · lemma_meaning=consecate/sanctify · type=action · location=heart · object=day · object_type=person · experiencer=other (addressed) · divine_involvement=agent · valence=neutral
  - compound: lev "heart" — co-seated
- **lev (H3820A)** — heart  [Hebrew · M47]  morph=HNcmsc · target=“heart”
  - sense=heart · lemma_meaning=inner man, mind, will, heart, understanding · type=status · faculty=['cognition', 'perception', 'volition', 'conscience'] · location=heart · how=test (H0974) · experiencer=self · divine_involvement=agent · valence=neutral
  - compound: qa.dash "to consecrate: prepare" — partner
- **lev (H3820A)** — heart  [Hebrew · M47]  morph=HNcmsc · target=“heart”
  - sense=heart · lemma_meaning=inner man, mind, will, heart, understanding · type=status · faculty=['cognition', 'perception', 'volition', 'conscience'] · location=heart · how=test (H0974) · experiencer=self · divine_involvement=agent · valence=neutral
  - compound: qa.dash "to consecrate: prepare" — partner

#### Jer 17:22
> Jer 17:22 And do not carry a burden out of your houses on the Sabbath or do any work , but keep the Sabbath day holy , as I commanded your fathers .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpq2mp · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=your · object_type=person · experiencer=other (addressed) · valence=commanded

#### Jer 17:24
> Jer 17:24 “‘But if you listen to me, declares the Lord , and bring in no burden by the gates of this city on the Sabbath day , but keep the Sabbath day holy and do no work on it,
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“keep”
  - sense=keep · lemma_meaning=consecate/sanctify · type=action · object=Sabbath · object_type=thing · valence=commanded

#### Jer 17:27
> Jer 17:27 But if you do not listen to me, to keep the Sabbath day holy , and not to bear a burden and enter by the gates of Jerusalem on the Sabbath day , then I will kindle a fire in its gates , and it shall devour the palaces of Jerusalem and shall not be quenched .’”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpcc · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=not · object_type=thing · valence=commanded
  - compound: sha.ma "to hear: obey" — partner
- **sha.ma (H8085H)** — to hear: obey  [Hebrew · M41]  morph=HVqi2mp · stem=Qal · target=“listen”
  - sense=listen · lemma_meaning=hear · type=action · faculty=['cognition', 'perception', 'volition'] · object=Sabbath · object_type=God · experiencer=other (addressed) · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner

#### Jer 22:7
> Jer 22:7 I will prepare destroyers against you, each with his weapons , and they shall cut down your choicest cedars and cast them into the fire .
- **qa.dash (H6942J)** — to consecrate: prepare  [Hebrew · M12 · **FOCUS**]  morph=HVpq1cs · stem=Piel · target=“prepare”
  - sense=prepare · lemma_meaning=consecate/sanctify · type=action · object=destroyers · object_type=person · experiencer=self · divine_involvement=agent · valence=neutral · immediate_response=cut down choicest
  - compound: sha.chat "to ruin" — partner
- **sha.chat (H7843)** — to ruin  [Hebrew · M27]  morph=HNcmpa · target=“destroyers”
  - sense=destroyers · lemma_meaning=to destroy, corrupt, go to ruin, decay · type=status · how=cut down (H3772) · object=choicest · object_type=thing · experiencer=other (addressed) · valence=neutral · immediate_response=cast fire · relational=against
  - compound: qa.dash "to consecrate: prepare" — partner

#### Jer 51:27
> Jer 51:27 “Set up a standard on the earth ; blow the trumpet among the nations ; prepare the nations for war against her; summon against her the kingdoms , Ararat , Minni , and Ashkenaz ; appoint a marshal against her; bring up horses like bristling locusts .
- **qa.dash (H6942J)** — to consecrate: prepare  [Hebrew · M12 · **FOCUS**]  morph=HVpv2mp · stem=Piel · target=“prepare”
  - sense=prepare · lemma_meaning=consecate/sanctify · type=action · object=nations · object_type=person · experiencer=other (addressed) · immediate_response=appoint marshal
  - compound: sha.ma "to hear: proclaim" — partner

#### Jer 51:28
> Jer 51:28 Prepare the nations for war against her, the kings of the Medes , with their governors and deputies , and every land under their dominion .
- **qa.dash (H6942J)** — to consecrate: prepare  [Hebrew · M12 · **FOCUS**]  morph=HVpv2mp · stem=Piel · target=“Prepare”
  - sense=Prepare · lemma_meaning=consecate/sanctify · type=action · object=nations · object_type=person · experiencer=other (addressed)

#### Eze 14:7
> Eze 14:7 For any one of the house of Israel , or of the strangers who sojourn in Israel , who separates himself from me , taking his idols into his heart and putting the stumbling block of his iniquity before his face , and yet comes to a prophet to consult me through him, I the Lord will answer him myself .
- **na.zar (H5144A)** — to dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVNu3ms · stem=Niphal · target=“separates”
  - sense=separates · lemma_meaning=to dedicate, consecrate, separate · type=action · location=heart · cause=taking idols into heart · cause_clause=any one of house Israel of strangers who · experiencer=other · valence=sinful · relational=from
  - compound: a.von "iniquity: crime" — partner; da.rash "to seek" — partner; no.khach "before" — qualifier
- **a.von (H5771G)** — iniquity: crime  [Hebrew · M10]  morph=HNcmsc · target=“iniquity”
  - sense=iniquity · lemma_meaning=crime · type=status · location=heart · how=putting (H7760) · object=stumbling block · object_type=abstract · cause=placing stumbling block before face · cause_clause=any one of house Israel of strangers who · experiencer=other · valence=sinful
  - compound: na.zar "to dedicate" — partner; da.rash "to seek" — partner; no.khach "before" — qualifier
- **da.rash (H1875)** — to seek  [Hebrew · M41]  morph=HVqcc · stem=Qal · target=“consult”
  - sense=consult · lemma_meaning=to resort to, seek, seek with care, enquire, require · type=action · faculty=perception · location=heart · object=Lord · object_type=God · cause_clause=any one of house Israel of strangers who · divine_involvement=object · valence=sinful
  - compound: a.von "iniquity: crime" — partner; na.zar "to dedicate" — partner; no.khach "before" — qualifier
- **lev (H3820A)** — heart  [Hebrew · M47]  morph=HNcmsc · target=“heart”
  - sense=heart · lemma_meaning=inner man, mind, will, heart, understanding · type=status · faculty=['cognition', 'perception', 'volition', 'conscience'] · location=heart · how=putting (H7760) · object=stumbling block · object_type=thing/abstract · cause=pending-read · cause_clause=any one of house Israel of strangers who · experiencer=other · divine_involvement=UNRESOLVED · immediate_response=comes prophet
  - compound: a.von "iniquity: crime" — partner; na.zar "to dedicate" — partner; da.rash "to seek" — partner; no.khach "before" — qualifier

#### Eze 20:12
> Eze 20:12 Moreover , I gave them my Sabbaths , as a sign between me and them , that they might know that I am the Lord who sanctifies them .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVprmsc · stem=Piel · target=“sanctifies”
  - sense=sanctifies · lemma_meaning=consecate/sanctify · type=action · object=them · object_type=person · cause_clause=I Lord sanctifies them · divine_involvement=agent · valence=righteous
- **na.tan (H5414G)** — to give: give  [Hebrew · M12]  morph=HVqp1cs · stem=Qal · target=“gave”
  - sense=gave · lemma_meaning=give/deliver/send/produce · type=action · object=Sabbaths · object_type=thing/abstract · cause=pending-read · cause_clause=I Lord sanctifies them · experiencer=self · divine_involvement=UNRESOLVED · immediate_response=sanctifies
  - compound: qa.dash "to consecrate: consecate" — partner

#### Eze 20:20
> Eze 20:20 and keep my Sabbaths holy that they may be a sign between me and you , that you may know that I am the Lord your God .'
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpv2mp · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=sign · object_type=thing · cause_clause=I Lord God · experiencer=other (addressed) · valence=commanded

#### Eze 20:41
> Eze 20:41 As a pleasing aroma I will accept you, when I bring you out from the peoples and gather you out of the countries where you have been scattered . And I will manifest my holiness among you in the sight of the nations .
- **qa.dash (H6942K)** — to consecrate: holiness  [Hebrew · M12 · **FOCUS**]  morph=HVNq1cs · stem=Niphal · target=“holiness”
  - sense=holiness · lemma_meaning=consecate/sanctify · type=action · object=sight · object_type=abstract · experiencer=self · divine_involvement=agent · valence=righteous
  - compound: ni.cho.ach "soothing" — partner; ra.tsah "to accept" — partner
- **ra.tsah (H7521)** — to accept  [Hebrew · M39]  morph=HVqi1cs · stem=Qal · target=“accept”
  - sense=accept · lemma_meaning=to be pleased with, be favourable to, accept favourably · type=action · faculty=['perception', 'volition'] · origin=received-from-outside · object=peoples · object_type=person · experiencer=self · valence=righteous
  - compound: ni.cho.ach "soothing" — partner; qa.dash "to consecrate: holiness" — partner
- **ni.cho.ach (H5207)** — soothing  [Hebrew · M04]  morph=HNcmsa · target=“pleasing”
  - sense=pleasing · lemma_meaning=soothing, quieting, tranquillising · type=status · how=accept (H7521) · valence=righteous
  - compound: ra.tsah "to accept" — partner; qa.dash "to consecrate: holiness" — partner

#### Eze 28:22
> Eze 28:22 and say , Thus says the Lord God : “ Behold , I am against you, O Sidon , and I will manifest my glory in your midst . And they shall know that I am the Lord when I execute judgments in her and manifest my holiness in her ;
- **qa.dash (H6942K)** — to consecrate: holiness  [Hebrew · M12 · **FOCUS**]  morph=HVNq1cs · stem=Niphal · target=“holiness”
  - sense=holiness · lemma_meaning=consecate/sanctify · type=action · cause=executing judgments in Sidon · cause_clause=when execute judgments holiness her · experiencer=self · divine_involvement=agent · valence=righteous · relational=her

#### Eze 28:25
> Eze 28:25 “ Thus says the Lord God : When I gather the house of Israel from the peoples among whom they are scattered , and manifest my holiness in them in the sight of the nations , then they shall dwell in their own land that I gave to my servant Jacob .
- **qa.dash (H6942K)** — to consecrate: holiness  [Hebrew · M12 · **FOCUS**]  morph=HVNq1cs · stem=Niphal · target=“holiness”
  - sense=holiness · lemma_meaning=consecate/sanctify · type=action · object=sight · object_type=God · experiencer=self · divine_involvement=agent · valence=righteous
- **na.tan (H5414G)** — to give: give  [Hebrew · M12]  morph=HVqp1cs · stem=Qal · target=“gave”
  - sense=gave · lemma_meaning=give/deliver/send/produce · type=action · object=servant · object_type=thing/abstract · experiencer=self · divine_involvement=UNRESOLVED
  - compound: qa.dash "to consecrate: holiness" — partner

#### Eze 36:23
> Eze 36:23 And I will vindicate the holiness of my great name , which has been profaned among the nations , and which you have profaned among them. And the nations will know that I am the Lord , declares the Lord God , when through you I vindicate my holiness before their eyes .
- **qa.dash (H6942K)** — to consecrate: holiness  [Hebrew · M12 · **FOCUS**]  morph=HVpq1cs · stem=Piel · target=“holiness”
  - sense=holiness · lemma_meaning=consecate/sanctify · type=action · object=name · object_type=abstract · cause=Israel profaning God's name among the nations · cause_clause=I Lord declares Lord God holiness their eyes · experiencer=self · divine_involvement=possessor · intensity=great (great) · valence=righteous

#### Eze 37:28
> Eze 37:28 Then the nations will know that I am the Lord who sanctifies Israel , when my sanctuary is in their midst forevermore .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVprmsa · stem=Piel · target=“sanctifies”
  - sense=sanctifies · lemma_meaning=consecate/sanctify · type=action · object=Israel · object_type=person · cause=God's sanctuary being in Israel's midst · cause_clause=I Lord sanctifies Israel sanctuary midst forevermore · divine_involvement=agent · valence=righteous

#### Eze 38:16
> Eze 38:16 You will come up against my people Israel , like a cloud covering the land . In the latter days I will bring you against my land , that the nations may know me, when through you, O Gog , I vindicate my holiness before their eyes .
- **qa.dash (H6942K)** — to consecrate: holiness  [Hebrew · M12 · **FOCUS**]  morph=HVNcc · stem=Niphal · target=“holiness”
  - sense=holiness · lemma_meaning=consecate/sanctify · type=action · object=eyes · object_type=abstract · divine_involvement=possessor · valence=righteous

#### Eze 38:23
> Eze 38:23 So I will show my greatness and my holiness and make myself known in the eyes of many nations . Then they will know that I am the Lord .
- **qa.dash (H6942K)** — to consecrate: holiness  [Hebrew · M12 · **FOCUS**]  morph=HVtq1cs · stem=Hithpael · target=“holiness”
  - sense=holiness · lemma_meaning=consecate/sanctify · type=action · object=eyes · object_type=abstract · cause_clause=I Lord · experiencer=self · divine_involvement=possessor · intensity=many (many) · valence=righteous
  - compound: ga.dal "to magnify" — partner
- **ga.dal (H1431)** — to magnify  [Hebrew · M22]  morph=HVtq1cs · stem=Hithpael · target=“greatness”
  - sense=greatness · lemma_meaning=to grow, become great or important, promote, make powerful, praise, ma · type=action · object=eyes · object_type=abstract · cause_clause=I Lord · experiencer=self · divine_involvement=agent · valence=righteous
  - compound: qa.dash "to consecrate: holiness" — partner

#### Eze 39:27
> Eze 39:27 when I have brought them back from the peoples and gathered them from their enemies ’ lands , and through them have vindicated my holiness in the sight of many nations .
- **qa.dash (H6942K)** — to consecrate: holiness  [Hebrew · M12 · **FOCUS**]  morph=HVNq1cs · stem=Niphal · target=“holiness”
  - sense=holiness · lemma_meaning=consecate/sanctify · type=action · object=sight · object_type=abstract · experiencer=self · divine_involvement=possessor · intensity=many (many) · valence=righteous

#### Eze 44:24
> Eze 44:24 In a dispute , they shall act as judges , and they shall judge it according to my judgments . They shall keep my laws and my statutes in all my appointed feasts , and they shall keep my Sabbaths holy .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpi3mp · stem=Piel · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · experiencer=other · divine_involvement=addressee · intensity=all (all) · valence=commanded
  - compound: sha.mar "to keep: obey" — partner; riv "strife" — partner
- **sha.mar (H8104G)** — to keep: obey  [Hebrew · M30]  morph=HVqi3mp · stem=Qal · target=“keep”
  - sense=keep · lemma_meaning=obey/observe · type=action · faculty=['perception', 'volition'] · object=laws · object_type=abstract · experiencer=other · divine_involvement=addressee · intensity=all (all) · valence=commanded · immediate_response=holy
  - compound: qa.dash "to consecrate: consecate" — partner; riv "strife" — partner

#### Eze 48:11
> Eze 48:11 This shall be for the consecrated priests , the sons of Zadok , who kept my charge , who did not go astray when the people of Israel went astray , as the Levites did .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVPsmsa · stem=Pual · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=priests · object_type=person · valence=righteous
  - compound: sha.mar "to keep: obey" — partner
- **sha.mar (H8104G)** — to keep: obey  [Hebrew · M30]  morph=HVqp3cp · stem=Qal · target=“kept”
  - sense=kept · lemma_meaning=obey/observe · type=action · faculty=['perception', 'volition'] · object=charge · object_type=abstract · experiencer=other · valence=righteous
  - compound: qa.dash "to consecrate: consecate" — partner

#### Dan 8:24
> Dan 8:24 His power shall be great — but not by his own power ; and he shall cause fearful destruction and shall succeed in what he does , and destroy mighty men and the people who are the saints .
- **qa.dosh (H6918H)** — holy: saint  [Hebrew · M12 · **FOCUS**]  morph=HAampa · target=“saints”
  - sense=saints · lemma_meaning=holy · type=quality · how=men and (H7843) · valence=righteous
  - compound: pa.la "to wonder" — partner; sha.chat "to ruin" — partner; ko.ach "strength" — partner
- **sha.chat (H7843)** — to ruin  [Hebrew · M27]  morph=HVhi3ms · stem=Hiphil · target=“and destroy”
  - sense=and destroy · lemma_meaning=to destroy, corrupt, go to ruin, decay · type=action · object=people · object_type=person · experiencer=other · valence=sinful
  - compound: pa.la "to wonder" — partner; qa.dosh "holy: saint" — partner; ko.ach "strength" — partner
- **pa.la (H6381)** — to wonder  [Hebrew · M04]  morph=HVNrfpa · stem=Niphal · target=“destruction”
  - sense=destruction · lemma_meaning=to be marvellous, be wonderful, be surpassing, be extraordinary, separ · type=action · faculty=['affect', 'cognition'] · valence=neutral
  - compound: qa.dosh "holy: saint" — partner; sha.chat "to ruin" — partner; ko.ach "strength" — partner
- **ko.ach (H3581B)** — strength  [Hebrew · M23]  morph=HNcmsc · target=“power”
  - sense=power · lemma_meaning=a small reptile, probably a kind of lizard, which is unclean · type=status · how=great (H6105) · object=power · object_type=abstract · experiencer=other · valence=neutral · immediate_response=destruction
  - compound: pa.la "to wonder" — partner; qa.dosh "holy: saint" — partner; sha.chat "to ruin" — partner

#### Hos 9:10
> Hos 9:10 Like grapes in the wilderness , I found Israel . Like the first fruit on the fig tree in its first season , I saw your fathers . But they came to Baal-peor and consecrated themselves to the thing of shame , and became detestable like the thing they loved .
- **na.zar (H5144A)** — to dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVNw3mp · stem=Niphal · target=“consecrated”
  - sense=consecrated · lemma_meaning=to dedicate, consecrate, separate · type=action · object=shame · object_type=spiritual-being · experiencer=other · valence=sinful
  - compound: shiq.quts "abomination" — partner; bo.shet "shame" — partner; ra.ah "to see: see" — qualifier
- **shiq.quts (H8251)** — abomination  [Hebrew · M10]  morph=HNcmpa · target=“became detestable”
  - sense=became detestable · lemma_meaning=detestable thing or idol, abominable thing, abomination, idol, deteste · type=status · how=consecrated (H5144) · object=shame · object_type=thing · experiencer=other · valence=sinful
  - compound: bo.shet "shame" — partner; ra.ah "to see: see" — qualifier; na.zar "to dedicate" — partner
- **ra.ah (H7200G)** — to see: see  [Hebrew · T2]  morph=HVqp1cs · stem=Qal · target=“saw”
  - sense=saw · lemma_meaning=see/show · type=action · faculty=['cognition', 'perception', 'volition'] · object=fathers · object_type=thing/abstract · experiencer=self · divine_involvement=UNRESOLVED
  - compound: shiq.quts "abomination" — partner; bo.shet "shame" — partner; na.zar "to dedicate" — partner
- **bo.shet (H1322)** — shame  [Hebrew · M07]  morph=HNcfsa · target=“shame”
  - sense=shame · lemma_meaning=shame · type=status · faculty=affect · how=consecrated (H5144) · valence=sinful
  - compound: shiq.quts "abomination" — partner; ra.ah "to see: see" — qualifier; na.zar "to dedicate" — partner

#### Joe 1:14
> Joe 1:14 Consecrate a fast ; call a solemn assembly . Gather the elders and all the inhabitants of the land to the house of the Lord your God , and cry out to the Lord .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpv2mp · stem=Piel · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · object=fast · object_type=abstract · experiencer=other (addressed) · valence=commanded
  - compound: qa.ra "to call: call to" — partner; za.aq "to cry out" — partner; a.tsa.rah "assembly" — partner
- **qa.ra (H7121G)** — to call: call to  [Hebrew · M37]  morph=HVqv2mp · stem=Qal · target=“call”
  - sense=call · lemma_meaning=call to/invite/entreat · type=action · faculty=volition · object=solemn assembly · object_type=person · experiencer=other (addressed) · divine_involvement=addressee · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner; za.aq "to cry out" — partner; a.tsa.rah "assembly" — partner
- **za.aq (H2199)** — to cry out  [Hebrew · M42]  morph=HVqv2mp · stem=Qal · target=“cry”
  - sense=cry · lemma_meaning=to cry, cry out, call, call for help · type=action · object=Lord · object_type=God · experiencer=other (addressed) · divine_involvement=addressee · valence=commanded · relational=to
  - compound: qa.ra "to call: call to" — partner; qa.dash "to consecrate: consecate" — partner; a.tsa.rah "assembly" — partner
- **a.tsa.rah (H6116)** — assembly  [Hebrew · M05]  morph=HNcfsa · target=“solemn assembly”
  - sense=solemn assembly · lemma_meaning=assembly, solemn assembly · type=status · how=call (H7121) · intensity=all (all) · valence=commanded
  - compound: qa.ra "to call: call to" — partner; qa.dash "to consecrate: consecate" — partner; za.aq "to cry out" — partner

#### Joe 2:15
> Joe 2:15 Blow the trumpet in Zion ; consecrate a fast ; call a solemn assembly ;
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpv2mp · stem=Piel · target=“consecrate”
  - sense=consecrate · lemma_meaning=consecate/sanctify · type=action · object=fast · object_type=abstract · experiencer=other (addressed) · valence=commanded
  - compound: qa.ra "to call: call to" — partner; a.tsa.rah "assembly" — partner
- **qa.ra (H7121G)** — to call: call to  [Hebrew · M37]  morph=HVqv2mp · stem=Qal · target=“call”
  - sense=call · lemma_meaning=call to/invite/entreat · type=action · faculty=volition · object=solemn assembly · object_type=person · experiencer=other (addressed) · valence=commanded
  - compound: qa.dash "to consecrate: consecate" — partner; a.tsa.rah "assembly" — partner
- **a.tsa.rah (H6116)** — assembly  [Hebrew · M05]  morph=HNcfsa · target=“solemn assembly”
  - sense=solemn assembly · lemma_meaning=assembly, solemn assembly · type=status · how=call (H7121) · valence=commanded
  - compound: qa.ra "to call: call to" — partner; qa.dash "to consecrate: consecate" — partner

#### Joe 2:16
> Joe 2:16 gather the people . Consecrate the congregation ; assemble the elders ; gather the children , even nursing infants. Let the bridegroom leave his room , and the bride her chamber .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpv2mp · stem=Piel · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · object=congregation · object_type=person · experiencer=other (addressed) · valence=commanded

#### Joe 3:9
> Joe 3:9 Proclaim this among the nations : Consecrate for war ; stir up the mighty men. Let all the men of war draw near ; let them come up .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVpv2mp · stem=Piel · target=“Consecrate”
  - sense=Consecrate · lemma_meaning=consecate/sanctify · type=action · object=war · object_type=abstract · experiencer=other (addressed) · valence=neutral
  - compound: qa.ra "to call: call out" — partner
- **qa.ra (H7121I)** — to call: call out  [Hebrew · M37]  morph=HVqv2mp · stem=Qal · target=“Proclaim”
  - sense=Proclaim · lemma_meaning=call to/invite/entreat · type=action · faculty=volition · object=among the nations · object_type=person · experiencer=other (addressed) · valence=neutral
  - compound: qa.dash "to consecrate: consecate" — partner

#### Mic 3:5
> Mic 3:5 Thus says the Lord concerning the prophets who lead my people astray , who cry “ Peace ” when they have something to eat , but declare war against him who puts nothing into their mouths .
- **qa.dash (H6942J)** — to consecrate: prepare  [Hebrew · M12 · **FOCUS**]  morph=HVpq3cp · stem=Piel · target=“declare”
  - sense=declare · lemma_meaning=consecate/sanctify · type=action · object=war · object_type=abstract · experiencer=other · valence=neutral
  - compound: sha.lom "peace" — partner; qa.ra "to call: call out" — partner
- **qa.ra (H7121I)** — to call: call out  [Hebrew · M37]  morph=HVqq3cp · stem=Qal · target=“cry”
  - sense=cry · lemma_meaning=call to/invite/entreat · type=action · faculty=volition · object=Peace · object_type=abstract · experiencer=other · valence=neutral
  - compound: sha.lom "peace" — partner; qa.dash "to consecrate: prepare" — partner
- **sha.lom (H7965G)** — peace  [Hebrew · M33]  morph=HNcmsa · target=“Peace”
  - sense=Peace · lemma_meaning=peace · type=status · how=who puts (H5414) · object=mouths · object_type=abstract · experiencer=other · valence=neutral
  - compound: qa.ra "to call: call out" — partner; qa.dash "to consecrate: prepare" — partner

#### Zep 1:7
> Zep 1:7 Be silent before the Lord God ! For the day of the Lord is near ; the Lord has prepared a sacrifice and consecrated his guests .
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVhp3ms · stem=Hiphil · target=“consecrated”
  - sense=consecrated · lemma_meaning=consecate/sanctify · type=action · object=his · object_type=person · cause_clause=Lord prepared sacrifice consecrated his guests · experiencer=other · divine_involvement=agent · valence=neutral
  - compound: has "to silence" — partner; qa.ra "to call: call to" — partner
- **qa.ra (H7121G)** — to call: call to  [Hebrew · M37]  morph=HVqsmpc · stem=Qal · target=“guests”
  - sense=guests · lemma_meaning=call to/invite/entreat · type=action · faculty=volition · cause_clause=Lord prepared sacrifice consecrated his guests · valence=neutral
  - compound: has "to silence" — partner; qa.dash "to consecrate: consecate" — partner
- **has (H2013)** — to silence  [Hebrew · M33]  morph=HVpv2ms · stem=Piel · target=“silent”
  - sense=silent · lemma_meaning=interj · type=action · object=before · object_type=person · cause=nearness of the day of the Lord · cause_clause=Lord prepared sacrifice consecrated his guests · experiencer=other (addressed) · divine_involvement=addressee · valence=commanded
  - compound: qa.ra "to call: call to" — partner; qa.dash "to consecrate: consecate" — partner

#### Hag 2:12
> Hag 2:12 ‘ If someone carries holy meat in the fold of his garment and touches with his fold bread or stew or wine or oil or any kind of food , does it become holy ?’” The priests answered and said , “ No .”
- **qa.dash (H6942G)** — to consecrate: consecate  [Hebrew · M12 · **FOCUS**]  morph=HVqi3ms · stem=Qal · target=“holy”
  - sense=holy · lemma_meaning=consecate/sanctify · type=action · object=priests · object_type=thing · experiencer=other · intensity=all (any) · valence=neutral

#### Zec 7:3
> Zec 7:3 saying to the priests of the house of the Lord of hosts and the prophets , “Should I weep and abstain in the fifth month , as I have done for so many years ?”
- **na.zar (H5144A)** — to dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVNcc · stem=Niphal · target=“abstain”
  - sense=abstain · lemma_meaning=to dedicate, consecrate, separate · type=action · object=month · object_type=abstract · valence=neutral
  - compound: ba.khah "to weep" — partner
- **ba.khah (H1058)** — to weep  [Hebrew · M03]  morph=HVqi1cs · stem=Qal · target=“weep”
  - sense=weep · lemma_meaning=to weep, bewail, cry, shed tears · type=action · faculty=affect · object=month · object_type=abstract · experiencer=self · valence=neutral
  - compound: na.zar "to dedicate" — partner

#### 1Ti 2:8
> 1Ti 2:8 I desire then that in every place the men should pray , lifting holy hands without anger or quarreling ;
- **hosios (G3741)** — sacred  [Greek · M12 · **FOCUS**]  morph=A-APF · target=“holy”
  - sense=holy · lemma_meaning=holy, pious, devout · type=quality · faculty=affect · valence=commanded
  - compound: boulomai "to plan" — partner; orgē "wrath" — partner; proseuchomai "to pray" — partner; dialogismos "reasoning" — partner
- **boulomai (G1014)** — to plan  [Greek · M15]  morph=V-PNI-1S · target=“desire”
  - sense=desire · lemma_meaning=to wish, will, desire · type=action · faculty=['affect', 'volition'] · experiencer=self · valence=commanded · immediate_response=pray
  - compound: orgē "wrath" — partner; hosios "sacred" — partner; proseuchomai "to pray" — partner; dialogismos "reasoning" — partner
- **dialogismos (G1261)** — reasoning  [Greek · M15]  morph=N-GSM · target=“quarreling”
  - sense=quarreling · lemma_meaning=thought, doubt · type=status · faculty=cognition · valence=forbidden
  - compound: boulomai "to plan" — partner; orgē "wrath" — partner; hosios "sacred" — partner; proseuchomai "to pray" — partner
- **proseuchomai (G4336)** — to pray  [Greek · M21]  morph=V-PNN · target=“pray”
  - sense=pray · lemma_meaning=to pray, offer prayer, Mt. 5:44 · type=action · object=lifting · valence=commanded
  - compound: boulomai "to plan" — partner; orgē "wrath" — partner; hosios "sacred" — partner; dialogismos "reasoning" — partner
- **orgē (G3709)** — wrath  [Greek · M02]  morph=N-GSF · target=“anger”
  - sense=anger · lemma_meaning=wrath, anger, the feeling and expression of strong displeasure and hos · type=status · faculty=['affect', 'moral_evaluation'] · valence=forbidden · relational=without
  - compound: boulomai "to plan" — partner; hosios "sacred" — partner; proseuchomai "to pray" — partner; dialogismos "reasoning" — partner

#### Tit 1:8
> Tit 1:8 but hospitable , a lover of good , self-controlled , upright , holy , and disciplined .
- **hosios (G3741)** — sacred  [Greek · M12 · **FOCUS**]  morph=A-ASM · target=“holy”
  - sense=holy · lemma_meaning=holy, pious, devout · type=quality · faculty=affect · valence=righteous
  - compound: filagathos "lover of good" — partner; dikaios "just" — partner; sōfrōn "self-controlled" — partner; filoxenos "hospitable" — partner; enkratēs "self-controlled" — partner
- **filoxenos (G5382)** — hospitable  [Greek · M05]  morph=A-ASM · target=“hospitable”
  - sense=hospitable · lemma_meaning=kind to strangers, hospitable, 1Tim. 3:2 · type=quality · valence=righteous
  - compound: filagathos "lover of good" — partner; dikaios "just" — partner; sōfrōn "self-controlled" — partner; hosios "sacred" — partner; enkratēs "self-controlled" — partner
- **dikaios (G1342)** — just  [Greek · M26]  morph=A-ASM · target=“upright”
  - sense=upright · lemma_meaning=right, righteous, upright · type=quality · faculty=['moral_evaluation', 'conscience'] · valence=righteous
  - compound: filagathos "lover of good" — partner; sōfrōn "self-controlled" — partner; filoxenos "hospitable" — partner; hosios "sacred" — partner; enkratēs "self-controlled" — partner
- **filagathos (G5358)** — lover of good  [Greek · M05]  morph=A-ASM · target=“good”
  - sense=good · lemma_meaning=loving what islover of good · type=quality · faculty=affect · valence=righteous
  - compound: dikaios "just" — partner; sōfrōn "self-controlled" — partner; filoxenos "hospitable" — partner; hosios "sacred" — partner; enkratēs "self-controlled" — partner
- **sōfrōn (G4998)** — self-controlled  [Greek · M19]  morph=A-ASM · target=“self-controlled”
  - sense=self-controlled · lemma_meaning=self-controlled, implied to be wise and prudent in nature · type=quality · faculty=cognition · valence=righteous
  - compound: filagathos "lover of good" — partner; dikaios "just" — partner; filoxenos "hospitable" — partner; hosios "sacred" — partner; enkratēs "self-controlled" — partner
- **enkratēs (G1468)** — self-controlled  [Greek · M19]  morph=A-ASM · target=“disciplined”
  - sense=disciplined · lemma_meaning=disciplined, self-controlled · type=quality · valence=righteous
  - compound: filagathos "lover of good" — partner; dikaios "just" — partner; sōfrōn "self-controlled" — partner; filoxenos "hospitable" — partner; hosios "sacred" — partner

#### Heb 7:26
> Heb 7:26 For it was indeed fitting that we should have such a high priest , holy , innocent , unstained , separated from sinners , and exalted above the heavens .
- **hosios (G3741)** — sacred  [Greek · M12 · **FOCUS**]  morph=A-NSM · target=“holy”
  - sense=holy · lemma_meaning=holy, pious, devout · type=quality · faculty=affect · how=fitting (G4241) · cause_clause=indeed fitting we such high priest holy innocent unstained · experiencer=other · valence=righteous
  - compound: hamartōlos "sinful" — partner; hupsēlos "high" — partner; akakos "innocent" — partner
- **akakos (G0172)** — innocent  [Greek · M12]  morph=A-NSM · target=“innocent”
  - sense=innocent · lemma_meaning=free from evil, innocent, blameless · type=quality · faculty=conscience · cause_clause=indeed fitting we such high priest holy innocent unstained · valence=righteous
  - compound: hamartōlos "sinful" — partner; hupsēlos "high" — partner; hosios "sacred" — partner
- **hamartōlos (G0268)** — sinful  [Greek · M10]  morph=A-GPM · target=“sinners”
  - sense=sinners · lemma_meaning=(a.) sinful, as an absolute moral failure · type=quality · faculty=volition · origin=received-from-outside · cause_clause=indeed fitting we such high priest holy innocent unstained · valence=sinful · immediate_response=exalted heavens · relational=from
  - compound: hupsēlos "high" — partner; akakos "innocent" — partner; hosios "sacred" — partner

#### Judg 17:3
> Judg 17:3 And he restored the 1,100 pieces of silver to his mother . And his mother said , “I dedicate the silver to the Lord from my hand for my son , to make a carved image and a metal image . Now therefore I will restore it to you .”
- **qa.dash (H6942H)** — to consecrate: dedicate  [Hebrew · M12 · **FOCUS**]  morph=HVhaa · stem=Hiphil · target=“dedicate”
  - sense=dedicate · lemma_meaning=consecate/sanctify · type=action · object=silver · object_type=God · divine_involvement=object · valence=sinful


---

*Deep-read U3 (Step 5) — TESTS the draft unit against the full per-verse evidence; re-assigns nothing. Verdict: MIXED HOLDS — consecration ACT (qadosh verb, 155/165 action) dominant + thin holy STATE (qa.dosh adjective + hosios, 10 quality); who-consecrates is TRILATERAL (God 34 / human-priestly 104 / God-of-God Ezekiel self-sanctification); lev/levav touched-not-seated (~6); counterfeit-holiness pole (sinful/forbidden 6). §B = generator output, all co-terms.*
