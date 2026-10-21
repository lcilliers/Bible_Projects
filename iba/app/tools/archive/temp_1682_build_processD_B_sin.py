# -*- coding: utf-8 -*-
import json

with open('_analytics/Clusters/1682-test-m10-process-c-B_sin-v2-20260911.json', encoding='utf-8') as f:
    fam = json.load(f)

with open('_analytics/Clusters/1682-test-m10-process-a-input-v1-20260911.json', encoding='utf-8') as f:
    proc_a = json.load(f)
by_strong = {s['strong']: s for s in proc_a['strongs']}
verse_text_lookup = {}
for st in fam['strongs_in_family']:
    for o in by_strong[st]['occurrences']:
        verse_text_lookup[o['osisId']] = o['verse_text']

def occ(strong, verse, surface=None, morph=None):
    if surface is None or morph is None:
        for o in by_strong[strong]['occurrences']:
            if o['osisId'] == verse:
                surface, morph = o['span_surface'], o['span_morph']
                break
    return {"verse": verse, "span_surface": surface, "span_morph": morph,
            "verse_text": verse_text_lookup.get(verse)}

def occs(strong, verses):
    return [occ(strong, v) for v in verses]

answers = []

def add(question_code, tier, component_code, component_title, question_text, scope,
        slants, needs_adjacent=None, cross_flags=None):
    answers.append({
        "question_code": question_code, "tier": tier,
        "component_code": component_code, "component_title": component_title,
        "question_text": question_text, "catalogue_scope": scope,
        "slants": slants,
        "needs_adjacent_verse_context": needs_adjacent or [],
        "cross_family_or_cluster_flags": cross_flags or []
    })

def slant(label, answer, strong=None, occurrences=None, observation_refs=None):
    return {"slant_label": label, "answer": answer, "strong": strong,
            "basis": {"occurrences": occurrences or [], "observation_refs": observation_refs or []}}

# ================= T0 =================

add("T0.1.1","T0","T0.1","Divine Nature Reflected",
    "In this verse, is the characteristic predicated of God or otherwise related to God; if so, in what relation (God as the one who bears it, acts, gives it, or is its object)? Record the relation, or record that it is not related to God here.",
    "Word/term (lexical)",
    [
      slant("god-explicitly-denied-of-Christ", "Sin is explicitly DENIED of Christ/God -- 'he made him who KNEW NO SIN to be sin' (2Cor 5:21), 'yet without sin' (Heb 4:15), 'which of you convicts me of sin?' (John 8:46) -- a stronger, more textually direct negative than H_guilt's mere absence: sin is not just unpredicated of God, it is actively ruled out by name.",
            strong="G0266", occurrences=occs("G0266",["John.8.46"]),
            observation_refs=["G0266 verse-grouping: Hebrews' sustained argument"]),
      slant("god-as-forgiver-forgiveness-formula", "God/Christ is the one who ACTS on sin -- the fixed 'forgiveness of sins' formula recurring from the Baptist through the apostolic preaching -- God as the one who forgives/removes, never the one who commits.",
            strong="G0266", occurrences=occs("G0266",["Mark.1.4","Acts.2.38"]),
            observation_refs=["G0266 verse-grouping: liturgical/missionary forgiveness formula"]),
      slant("god-as-wronged-party-implicit", "Sin against God as the implicit wronged party runs through the whole family's confession formula ('we have sinned' addressed to the LORD, 1Kgs 8:47, Dan 9:5) -- God is the one sinned against, not the sinner.",
            strong="H2398", occurrences=occs("H2398",["Dan.9.5"]),
            observation_refs=["H2398 verse-grouping: Qal national confession formula"]),
      slant("not-related-to-God", "The great majority of occurrences (interpersonal offense, practical ethics, narrative confession, the 'sinner' social category) state no God-relation at all in the verse itself.", strong=None)
    ])

add("T0.1.2a","T0","T0.1","Divine Nature Reflected",
    "Across the characteristic's verses, is the characteristic ever predicated of God himself (not just present in a verse where God is also mentioned)?",
    "Other non-human beings",
    [
      slant("firm-negative-explicitly-stated", "No -- and unlike H_guilt, this family states the negative explicitly rather than leaving it merely unattested: 2Cor 5:21 and Heb 4:15 both directly assert Christ's sinlessness by name, and John 8:46 poses it as an unanswerable rhetorical challenge. Sin is not merely absent from God's predicate-set; it is affirmatively excluded.", strong=None)
    ])

add("T0.1.2b","T0","T0.1","Divine Nature Reflected",
    "What does the pattern of presence/absence found in T0.1.2a indicate for the characteristic's place in the human person and in the divine image?",
    "Other non-human beings",
    [
      slant("sin-marks-departure-from-image", "Sin's explicit exclusion from Christ, held up as the standard of what a fully image-bearing human looks like, indicates sin is precisely the human departure from the image, not a variant expression of it -- Christ's sinlessness is presented as what humanity was meant to be.", strong=None)
    ])

add("T0.2.1","T0","T0.2","Created Purpose",
    "Does this verse state any purpose, role, or effect the characteristic serves in the person — what it leads the person to be, do, or become? Record it if stated; otherwise record none.",
    "Verse-context",
    [
      slant("produces-death", "Sin's stated effect, repeatedly, is DEATH -- 'sin, when it is full-grown, brings forth death' (Jas 1:15), 'the wages of sin is death' (Rom 6:23), 'sin... producing death in me' (Rom 7:13).",
            strong="G0266", occurrences=occs("G0266",["Jas.1.15","Jas.1.15"]),
            observation_refs=["G0266 verse-grouping: general epistles"]),
      slant("produces-slavery", "Sin produces SLAVERY to itself as a ruling condition -- 'everyone who commits sin is a slave to sin' (John 8:34), 'sold to sin' (Rom 7:14 register).",
            strong="G0266", occurrences=occs("G0266",["John.8.34","John.8.34"])),
      slant("produces-hardening", "Sin's 'deceitfulness' HARDENS the heart over time (Heb 3:13) -- an explicit constitutional effect on a named faculty.",
            strong="G0266", occurrences=occs("G0266",["Heb.3.13"]),
            observation_refs=["G0266 surface-gloss-divergence: Hebrews' sustained argument"]),
      slant("no-stated-effect", "Most narrative/confession/legal occurrences state no further effect -- the act or status is simply named.", strong=None)
    ])

add("T0.2.2","T0","T0.2","Created Purpose",
    "Across the evidence, does the characteristic's role read as belonging to created design, to the fallen condition, to both, or as not determinable?",
    "Other non-human beings",
    [
      slant("fallen-condition-with-cosmic-scope", "Fallen condition, and stated at cosmic scope rather than only individual scale: 'sin came into the world through one man' (Rom 5:12), 'the whole world lies... in the power of the evil one' (implied by 1John's sinning-of-the-devil material) -- sin is presented as an entered, not created, condition of the world itself.",
            strong="G0266", occurrences=occs("G0266",["Rom.5.12"]))
    ])

add("T0.2.3","T0","T0.2","Created Purpose",
    "Across the evidence, is there any orientation toward a future fullness — something the person moves toward, not only what they currently are? Record it, or record none.",
    "Other non-human beings",
    [
      slant("negative-future-if-persisted", "The only future orientation this family states is negative if sin is not addressed -- ongoing/final death (Jas 1:15, Rom 6:23) -- rather than a future fullness sin itself moves toward.",
            strong="G0266", occurrences=occs("G0266",["Rom.6.23"])),
      slant("remedy-future-orientation", "Where a future fullness IS stated, it belongs to the remedy, not to sin itself: Christ's sacrifice removes sin permanently ('he will remember their sins no more,' Heb 8:12) so that no further offering for sin is needed -- a future-oriented resolution, not an unfolding of sin toward anything.",
            strong="G0266", occurrences=occs("G0266",["Heb.8.12"]))
    ])

add("T0.3.1","T0","T0.3","Image-Bearer Expression",
    "From the characteristic's God-relation (T0.1) and its role (T0.2), what aspect of the divine likeness, if any, does it instantiate in the person? Record the aspect, or record none.",
    "Other non-human beings",
    [
      slant("none-sin-is-the-negation", "None -- sin instantiates no aspect of divine likeness; per T0.1, it is explicitly what God/Christ is not. Its role (T0.2) is uniformly corrosive (death, slavery, hardening), the structural opposite of a likeness-bearing function.", strong=None)
    ])

add("T0.3.2","T0","T0.3","Image-Bearer Expression",
    "Across the evidence, is the characteristic shared between God and the person, or an exclusively creaturely analogue to something in God?",
    "Other non-human beings",
    [
      slant("exclusively-creaturely-not-even-analogue", "Exclusively creaturely, and not even an analogue to anything in God (contrast H_guilt's guilt-bearing, which had a partial typological analogue via the Servant/Christ). Sin has no positive counterpart in the divine nature at all -- it is pure departure, not a creaturely echo of a divine quality.", strong=None)
    ])

add("T0.3.3","T0","T0.3","Image-Bearer Expression",
    "Where the characteristic is present or absent in a person, what does that indicate about the condition of the divine image in them — or is no such indication evidenced?",
    "Other non-human beings",
    [
      slant("presence-indicates-slavery-not-mere-damage", "Where present, sin indicates more than a damaged-but-functioning image (H_guilt's pattern) -- John 8:34's 'slave to sin' language suggests the image's governing capacity (its freedom to choose otherwise) is itself compromised, not just its moral record.",
            strong="G0266", occurrences=occs("G0266",["John.8.34"])),
      slant("absence-indicates-christlikeness", "Absence (Christ's own sinlessness, held up as the standard) indicates the image functioning as intended -- the clearest positive-absence case in this family.",
            strong="G0266", occurrences=occs("G0266",["Heb.4.15"]))
    ])

add("T0.4.1","T0","T0.4","Typological Significance",
    "Does this verse use the characteristic typologically — pointing beyond the immediate to a covenantal, eschatological, or christological reality; if so, which, and in which direction (the divine instance establishing the pattern, or the human pointing toward the divine)? Record the use and direction, or record none.",
    "Verse-context",
    [
      slant("adam-christ-typology", "Rom 5:12-21's 'sin entered through one man' is explicitly typological -- Adam as the type, Christ as the antitype who reverses sin's reign; direction: the human (Adam) establishing the pattern, later answered/reversed by the divine instance (Christ).",
            strong="G0266", occurrences=occs("G0266",["Rom.5.12"]),
            observation_refs=["G0266 verse-grouping: Romans 3-8 cosmic ruling power"]),
      slant("hebrews-sacrificial-typology", "Hebrews' whole sin-offering argument (old sacrifices repeated annually vs. Christ's one sacrifice) is typological -- the old system establishing a pattern later fulfilled.",
            strong="G0266", occurrences=occs("G0266",["Heb.10.4"])),
      slant("no-typology-elsewhere", "Most narrative/legal/confession occurrences show no typological signal.", strong=None)
    ])

# ================= T1 =================

add("T1.1.1","T1","T1.1","Name and Naming",
    "What is the characteristic called in the programme, and what does the name signal about its essential nature?",
    "Word/term (lexical)",
    [
      slant("sin-is-the-primary-act-category", "Called 'Sin' (B_sin, M10). Unlike H_guilt (a consequence-status downstream of an act), the name here signals the ACT/violation itself -- 'to sin' (hamartano/chata) is the base verb form across both languages, making this family's core sense more primary/originating than H_guilt's, which was always secondary to an act already named elsewhere.", strong=None)
    ])

add("T1.1.2","T1","T1.1","Name and Naming",
    "What do the primary Hebrew and Greek terms show at the definitional level?",
    "Word/term (lexical)",
    [
      slant("hamartano-missing-the-mark", "hamartano/hamartia (Greek) roots in 'missing the mark' -- an archery/target metaphor, an act that fails to reach its intended goal rather than a purely legal-liability term.", strong="G0266"),
      slant("chata-multivalent-by-binyan", "chata (Hebrew) is genuinely multivalent by grammatical stem -- Qal 'sin,' Hiphil 'cause to sin,' Piel 'purify from sin' -- the single root spans committing, causing, AND removing sin through grammar alone.",
            strong="H2398", occurrences=[],
            observation_refs=["H2398 difference-inference x2: Hiphil causative, Piel purification"])
    ])

add("T1.1.3","T1","T1.1","Name and Naming",
    "What directional, relational, or constitutional implication does the name carry?",
    "Word/term (lexical)",
    [
      slant("missing-the-mark-implies-failed-aim", "'Missing the mark' implies a FAILED aim at a real target -- sin presupposes a standard/goal that existed and was not reached, not an arbitrary rule violated.", strong="G0266"),
      slant("chata-become-implies-entered-state", "chata's Qal 'become/commit' implies entering a state through one's own act, echoing H_guilt's asham but here naming the originating act itself rather than its consequence.", strong="H2398")
    ])

add("T1.2.1","T1","T1.2","Kind",
    "What kind of inner-being phenomenon is the characteristic — an act, a disposition, a condition/status, a quality, or something else?",
    "Characteristic (HIB behaviour)",
    [
      slant("primarily-an-act", "Primarily an ACT at the verb level (hamartano, chata Qal) -- 'to sin' names a discrete commission, the family's base sense.", strong="G0264/H2398"),
      slant("also-a-ruling-power-condition", "But the abstract noun (hamartia) in Romans 5-8 is treated as far more than a condition/status -- it is PERSONIFIED as a quasi-agent: 'sin reigned' (5:21), 'sin... produced... deceived' (7:8-11), 'sin dwells in me' (7:17), 'the law of sin' warring against the mind (7:23). This goes beyond H_guilt's status-language into something closer to an internal ruling force with its own operative agency -- worth flagging directly against the working hypothesis that this family behaves 'just like guilt.'",
            strong="G0266", occurrences=occs("G0266",["Rom.7.17","Rom.7.23"]),
            observation_refs=["G0266 verse-grouping: Romans 3-8 personified power"]),
      slant("hamartolos-is-a-social-category", "hamartolos names a STANDING SOCIAL/RELATIONAL CATEGORY (a class of person -- 'tax collectors and sinners') rather than an act or a status in the individual's own inner economy -- a third kind this family carries that H_guilt did not.",
            strong="G0268", occurrences=occs("G0268",["Luke.15.1"]))
    ])

add("T1.2.2","T1","T1.2","Kind",
    "Is the characteristic simple in structure, or does it combine constituent elements; if compound, which?",
    "Characteristic (HIB behaviour)",
    [
      slant("compound-desire-to-death-sequence", "James 1:15 states an explicit compound sequence within a single verse: desire conceives, sin is born, sin (once grown) brings forth death -- sin is structurally the middle term of a three-stage process (desire -> sin -> death), not a standalone simple unit.",
            strong="G0266", occurrences=occs("G0266",["Jas.1.15","Jas.1.15"]))
    ])

add("T1.3.1","T1","T1.3","Boundary",
    "What stands against the characteristic as its structural opposite — the inner-being reality that excludes it?",
    "Characteristic (HIB behaviour)",
    [
      slant("righteousness-and-obedience", "Righteousness/obedience is the explicit structural opposite throughout Romans 5-6 ('the many will be made righteous,' 5:19 register; slaves either 'to sin, leading to death, or of obedience, leading to righteousness,' 6:16).",
            strong="G0266", occurrences=occs("G0266",["Rom.6.16"])),
      slant("not-sinning-as-a-settled-state", "1 John frames the opposite as a settled incapacity to sin in the one born of God (3:9) -- a stronger opposite than H_guilt's 'refuge' pairing, framed as a change of nature rather than an avoided event.",
            strong="G0264", occurrences=occs("G0264",["1John.3.9"])),
    ])

add("T1.3.2","T1","T1.3","Boundary",
    "What does the characteristic exclude or resist at its edge?",
    "Characteristic (HIB behaviour)",
    [
      slant("marrying-is-not-sin", "Paul explicitly polices the edge of the category: marrying is 'not sinning' even though he prefers celibacy (1Cor 7:28, 7:36) -- a deliberate boundary-drawing that excludes an act some might have assumed was sinful.",
            strong="G0264", occurrences=occs("G0264",["1Cor.7.28"]),
            observation_refs=["G0264 verse-grouping: practical ethics"]),
      slant("anger-itself-is-not-sin", "'Be angry and do not sin' (Eph 4:26) treats the emotion itself as outside the category, only its uncontrolled outworking falling inside it.",
            strong="G0264", occurrences=occs("G0264",["Eph.4.26"]))
    ])

add("T1.3.3","T1","T1.3","Boundary",
    "Where does the characteristic end and another thing begin — what is it not?",
    "Characteristic (HIB behaviour)",
    [
      slant("sin-vs-sin-offering", "The same word (hamartia, chattaah) crosses from the abstract condition into the concrete sacrificial ANIMAL that addresses it (Heb 10:6/10:8 'sin offerings'; H2403H's 32 occurrences exclusively this cultic sense) -- the boundary between the wrongdoing and its remedy-object is not kept lexically distinct.",
            strong="G0266", occurrences=occs("G0266",["Heb.10.6","Heb.10.8"]),
            observation_refs=["G0266 surface-gloss-divergence: sin/sin-offering split", "cross-family: same phenomenon as H2403B/H2403H"]),
      slant("sin-vs-guilt", "John 9:41 renders hamartia as 'guilt' rather than 'sin' -- the boundary between THIS family and family H_guilt is not maintained in the English surface even within a single strong.",
            strong="G0266", occurrences=occs("G0266",["John.9.41","John.9.41"]))
    ],
    cross_flags=[{"statement":"hamartia's sin/sin-offering split mirrors H2403B/H2403H's split within this same family, and John 9:41's 'guilt' gloss crosses directly into family H_guilt's territory -- both already logged, restated here against the specific boundary question.","related_family":"H_guilt","related_cluster":None}])

add("T1.4.1a","T1","T1.4","Modes of Operation",
    "What is the grammatical/stem form of the characteristic's primary term in this verse?",
    "Word/term (lexical)",
    [
      slant("hebrew-stems", "Qal (H2398 majority -- 'sin' personally); Hiphil (H2398, 23 occ -- causative 'cause to sin,' dominated by the Jeroboam refrain); Piel (H2398, 9 occ -- 'purify from sin'); Hithpael (H2398, 7 occ -- reflexive self-purification).", strong="H2398"),
      slant("greek-forms", "Aorist/present indicative and participle forms throughout for hamartano (verb); noun forms (N-*SF) for hamartia; adjective/substantive forms (A-*) for hamartolos.", strong="G0264/G0266/G0268")
    ])

add("T1.4.1b","T1","T1.4","Modes of Operation",
    "In what distinct mode(s) does the characteristic operate within the inner person in this verse — the manner of its functioning?",
    "Verse-context",
    [
      slant("committed-act-mode", "As a discrete committed act -- the confession formula ('I have sinned') names a completed, punctual event.", strong="H2398/G0264"),
      slant("ruling-power-mode", "As an indwelling ruling power that acts on the person -- 'sin dwells in me,' 'sin, seizing an opportunity through the commandment, deceived me' (Rom 7:11, 7:17) -- sin here functions almost as a second agent operating within the same person.",
            strong="G0266", occurrences=occs("G0266",["Rom.7.11","Rom.7.17"])),
      slant("social-category-mode", "As a standing social label attached to a person by others or self ('tax collectors and sinners') -- an externally/relationally applied mode, not an inner operation at all.",
            strong="G0268", occurrences=occs("G0268",["Luke.15.1"]))
    ])

add("T1.4.2","T1","T1.4","Modes of Operation",
    "Does the mode of operation vary by context, direction, or constitutional level; if so, how?",
    "Characteristic (HIB behaviour)",
    [
      slant("varies-sharply-by-strong-and-book", "Yes, sharply: the same family ranges from a punctual confessed act (Old Testament narrative formula) to a personified ruling power (Romans) to a social category (Synoptic Gospels) to a purification target (Levitical Piel/Hithpael) -- more registers than H_guilt showed, and tracking BOTH strong and literary context/book, not one axis alone.", strong=None)
    ])

add("T1.4.3","T1","T1.4","Modes of Operation",
    "Does the characteristic operate through a communicative or speech-based mode (commanded, addressed, spoken); if so, how? Record it, or record none.",
    "Characteristic (HIB behaviour)",
    [
      slant("confessional-speech", "Extensively communicative: the recurring first-person confession formula ('I/we have sinned') IS spoken/prayed speech across dozens of occurrences (Dan 9, Neh 1, 2Chr 6, David, Saul, Pharaoh) -- far more pervasively speech-based than H_guilt's occasional quoted denial.",
            strong="H2398", occurrences=occs("H2398",["Dan.9.5","2Sam.12.13"])),
      slant("commanded-cessation", "Also directly commanded: 'sin no more' (John 5:14, 8:11), 'stop sinning' (1Cor 15:34) -- imperative speech addressed directly to the person.",
            strong="G0264", occurrences=occs("G0264",["John.8.11","1Cor.15.34"]))
    ])

add("T1.5.1","T1","T1.5","Immediate Response",
    "What first or most immediate inner-being response does this verse show following the characteristic? Record it, or record none.",
    "Verse-context",
    [
      slant("immediate-confession", "Immediate spoken confession/acknowledgment ('I have sinned') -- the dominant, near-mechanical response across the Qal-formula occurrences.", strong="H2398", occurrences=occs("H2398",["2Sam.12.13"])),
      slant("immediate-suicide-Judas", "Judas's confession is followed immediately by despair and suicide (Matt 27:4-5 context) -- the family's most extreme immediate-response case.",
            strong="G0264", occurrences=occs("G0264",["Matt.27.4"])),
      slant("immediate-forgiveness-pronounced", "In the Synoptic healing scenes, the immediate response recorded is not the sinner's own reaction at all but Christ's PRONOUNCEMENT of forgiveness -- the narrative moves straight to the remedy.",
            strong="G0266", occurrences=occs("G0266",["Mark.2.5"]))
    ])

add("T1.5.2","T1","T1.5","Immediate Response",
    "Across the verses, is that immediate response consistent or varied?",
    "Characteristic (HIB behaviour)",
    [
      slant("varied-but-confession-dominant", "Varied, but far more dominated by ONE response (spoken confession) than H_guilt was -- the sheer repetition of the 'I have sinned' formula across so many independent narratives suggests this is closer to a fixed cultural/liturgical script than guilt's genuinely scattered response set.", strong=None)
    ])

add("T1.6.1","T1","T1.6","Sustained Effect",
    "What does the characteristic produce in the inner being over time in this verse — what states, qualities, capacities, or orientations does it establish? Record it, or record none.",
    "Verse-context",
    [
      slant("slavery-as-sustained-state", "Slavery to sin as an ongoing, self-perpetuating state (John 8:34, Rom 6:16-20) -- once entered, it is described as governing further action, not just a past mark.",
            strong="G0266", occurrences=occs("G0266",["Rom.6.20"])),
      slant("hardening-over-time", "Hardening of the heart through sin's repeated 'deceitfulness' (Heb 3:13) -- an explicit accumulation-over-time claim, paralleling H0819's cumulative-guilt finding but naming a specific faculty (the heart) that H_guilt never did.",
            strong="G0266", occurrences=occs("G0266",["Heb.3.13"])),
      slant("no-sustained-effect-stated", "Most confession/narrative occurrences state no sustained effect beyond the single act.", strong=None)
    ])

add("T1.6.3","T1","T1.6","Sustained Effect",
    "How does the sustained effect differ from the immediate response (T1.5)?",
    "Characteristic (HIB behaviour)",
    [
      slant("act-to-governing-condition", "Immediate response is a single spoken/enacted event (confession, a command to stop); sustained effect is a GOVERNING CONDITION (slavery, hardening) that outlasts and can outweigh any single act -- sin's sustained effect looks less like accumulated status (H_guilt's compound-interest image) and more like an entrenched RULE taking over the person's operation.", strong=None)
    ])

add("T1.7.1","T1","T1.7","Conditions of Reception",
    "Under what inner conditions does the characteristic take hold or operate rightly?",
    "Characteristic (HIB behaviour)",
    [
      slant("desire-is-the-entry-point", "Desire is named as the specific entry point through which sin takes hold -- 'each person is tempted when he is lured and enticed by his own desire; then desire... gives birth to sin' (Jas 1:15) -- a precise inner mechanism H_guilt never stated for its own onset.",
            strong="G0266", occurrences=occs("G0266",["Jas.1.15"])),
      slant("law-provides-the-opportunity", "The commandment itself, not sin's own initiative, provides the 'opportunity' Paul says sin exploits (Rom 7:8, 7:11) -- a paradoxical condition where the very prohibition becomes sin's occasion.",
            strong="G0266", occurrences=occs("G0266",["Rom.7.8","Rom.7.11"]))
    ])

add("T1.7.2","T1","T1.7","Conditions of Reception",
    "Under what inner conditions is the characteristic blocked, distorted, resisted, or not taken up — including, where the evidence shows it, distortion or interference by another spirit (adversarial or angelic)?",
    "Characteristic (HIB behaviour)",
    [
      slant("adversarial-interference-explicit", "Unlike H_guilt's clean negative, this family DOES show adversarial involvement directly: 'the devil has been sinning from the beginning... whoever keeps on sinning is of the devil' (1John 3:8) -- ongoing sin is explicitly tied to demonic origin/affiliation, and 'the angels who sinned' (2Pet 2:4) shows the category applied to spiritual beings themselves, not just humans.",
            strong="G0264", occurrences=occs("G0264",["1John.3.8","2Pet.2.4"]),
            observation_refs=["G0264 verse-grouping: 1 John's paradoxical cluster","G0264 verse-grouping: suffering/judgment backdrop"]),
      slant("regenerate-incapacity-blocks-it", "In the same letter, being 'born of God' is stated to BLOCK ongoing sinning as a settled practice (1John 3:9, 5:18) -- a stated inner condition (new birth) that resists it, structurally opposite to the devil's affiliation-condition above.",
            strong="G0264", occurrences=occs("G0264",["1John.3.9","1John.5.18"]))
    ],
    cross_flags=[{"statement":"1 John's tying of persistent sin to the devil directly answers H_guilt's T4.6 confirmed-negative finding -- worth a direct side-by-side once other families' T4.6 answers exist, to see whether adversarial involvement clusters around act-vocabulary (sin) rather than status-vocabulary (guilt).","related_family":"H_guilt","related_cluster":None}])

add("T1.7.3","T1","T1.7","Conditions of Reception",
    "What is the inner-being state of the person in whom the characteristic is present but does not take hold?",
    "The HIB",
    [
      slant("regenerate-resistance-state", "1 John's regenerate person: sin is present as a possibility (2:1's pastoral provision assumes it can still happen) but does not take hold as settled practice -- the inner state is one of God's 'seed' abiding in them (3:9's stated ground).",
            strong="G0264", occurrences=occs("G0264",["1John.3.9","1John.2.1"]))
    ])

# ================= T2 =================

add("T2.1.1","T2","T2.1","Spirit-Level Location",
    "At which constitutional level(s) does this verse locate the characteristic — from {spirit, soul, heart, mind, other soul-subset, a named body part} — and how is each engaged? Record every level evidenced, or none.",
    "Verse-context",
    [
      slant("mind-explicitly-engaged", "MIND is explicitly named and engaged: 'the law of sin' wars against 'the law of my mind' (Rom 7:23) -- a direct constitutional-level claim H_guilt's family never made anywhere in its 75 occurrences.",
            strong="G0266", occurrences=occs("G0266",["Rom.7.23"]),
            observation_refs=["G0266 verse-grouping: Romans 3-8 personified power"]),
      slant("heart-engaged-via-hardening", "HEART is engaged via sin's 'deceitfulness' hardening it over time (Heb 3:13).",
            strong="G0266", occurrences=occs("G0266",["Heb.3.13"])),
      slant("body-engaged-as-members", "The BODY is engaged as the site where sin's law operates ('the members of my body,' Rom 7:23 register; 'sin that dwells in me... in my flesh,' 7:17-18) -- a functional, not merely emblematic, body-link, unlike H_guilt's one purely emblematic case (Aaron's forehead).",
            strong="G0266", occurrences=occs("G0266",["Rom.7.17"])),
      slant("no-level-named-elsewhere", "Most narrative/legal/confession occurrences name no constitutional level -- guilt-like in this respect.", strong=None)
    ])

add("T2.1.2","T2","T2.1","Spirit-Level Location",
    "Across the verses, what does the pattern of engaged and absent levels indicate — the characteristic's depth and seat, the levels it never engages, and (for any body link) whether the link is emphatic, functional, expressive, indicative, or mediating?",
    "The HIB",
    [
      slant("sin-is-faculty-seated-where-guilt-was-not", "Sin (at least in Paul's psychological register) IS faculty-seated -- mind and body are both named as the sites of its operation -- a direct contrast to H_guilt's near-total absence of such language. This is the clearest evidence yet that sin and guilt, despite superficial similarity, occupy structurally different positions relative to the inner being: guilt is a relational/legal status with no seat; sin (at least as Paul develops it) is an operative condition WITH a seat.",
            strong="G0266", occurrences=occs("G0266",["Rom.7.23"])),
      slant("body-link-is-functional", "The body-link here is FUNCTIONAL, not merely emphatic (contrast H_guilt's Exod 28:38) -- sin is described as actually operating THROUGH the members/flesh, not just displayed on a body part.",
            strong="G0266", occurrences=occs("G0266",["Rom.7.17"]))
    ],
    cross_flags=[{"statement":"This is the single clearest point of divergence from H_guilt found so far in the T0-T5 pass -- worth flagging prominently for the researcher's status-vs-characteristic hypothesis: sin engages mind/body directly where guilt engaged neither.","related_family":"H_guilt","related_cluster":None}])

add("T2.10.1","T2","T2.10","Constitutional Movement",
    "Does the characteristic move across constitutional levels (spirit→soul→body), or onto the person from an external source — including another spirit (angelic or adversarial) — or in another direction; and if so in what sequence or pattern? If no movement, record none.",
    "The HIB",
    [
      slant("desire-to-act-to-body-sequence", "James 1:15 states a movement sequence: desire (an inner state) conceives -> sin is born (an act) -> death (a bodily/final consequence) -- movement from inner disposition outward to act to consequence.",
            strong="G0266", occurrences=occs("G0266",["Jas.1.15"])),
      slant("world-to-person-entry", "Rom 5:12's 'sin entered the world through one man' names a movement ONTO humanity from a single origin point, then spreading -- an external-entry-then-universal-diffusion pattern distinct from H_guilt's individual-origin norm.",
            strong="G0266", occurrences=occs("G0266",["Rom.5.12"])),
      slant("devil-affiliation-as-external-source", "1John 3:8's 'of the devil' framing names an external, adversarial source for ongoing sinning -- a movement-onto-the-person pattern H_guilt confirmed as absent for itself.",
            strong="G0264", occurrences=occs("G0264",["1John.3.8"]))
    ])

add("T2.7.1","T2","T2.7","Body — Direction",
    "Where a body link exists (from the T2.1.1 audit), in which direction does it run — soul/spirit expressing through the body, the body feeding back to the soul, or both — and what follows from that direction? If no body link, record none.",
    "The HIB",
    [
      slant("both-directions-shown", "Both directions appear: sin operating 'in my members' suggests an inward rule expressing through bodily action (Rom 7 register), while the whole 'body of death' language (7:24 context) suggests the body also feeding back as the site FROM WHICH deliverance is sought -- a two-way relationship, unlike H_guilt's one-directional-only body link.",
            strong="G0266", occurrences=occs("G0266",["Rom.7.17"]))
    ])

add("T2.9.1","T2","T2.9","Origin and Source",
    "Where does this verse say the characteristic originates — generated within the person, received from another person, bestowed by God, carried generationally, introduced by another spirit (angelic or adversarial), or not stated?",
    "Verse-context",
    [
      slant("generated-within-dominant", "Generated within, by one's own act -- the dominant pattern across the confession-formula occurrences.", strong="H2398"),
      slant("generational-entry-point", "Carried generationally/at a species level from a single origin -- 'sin entered the world through one man, and death through sin' (Rom 5:12) -- a stated generational-diffusion claim that H_guilt's family explicitly DENIED for itself (Ezek 18:19-20). Sin and guilt take opposite positions on generational transmission within the same overall cluster.",
            strong="G0266", occurrences=occs("G0266",["Rom.5.12"])),
      slant("adversarial-origin-for-persistence", "Introduced/sustained by an adversarial spirit for its ongoing form -- 1John 3:8's devil-affiliation for the one who 'keeps on sinning.'",
            strong="G0264", occurrences=occs("G0264",["1John.3.8"]))
    ],
    cross_flags=[{"statement":"Sin's Romans 5:12 generational-diffusion claim directly contradicts H_guilt's Ezekiel 18:19-20 generational-denial -- the same cluster holds both positions depending on which family/strong is read, worth a dedicated cross-family reconciliation round.","related_family":"H_guilt","related_cluster":None}])

add("T2.9.2","T2","T2.9","Origin and Source",
    "Across the verses, is the origin single or multiple, and does it change with context?",
    "Characteristic (HIB behaviour)",
    [
      slant("multiple-and-more-varied-than-guilt", "Multiple, and more varied than H_guilt's three clean types: self-generated (the norm), single-origin-then-universal-diffusion (Rom 5:12, a claim about the whole species, not just individuals), and adversarial-affiliation (1John 3:8) for the sustained/settled form specifically. Origin appears to correlate with WHICH aspect of sin is being discussed (the act vs. the condition vs. the practice), not just which strong.", strong=None)
    ])

# ================= T4 =================

add("T4.1.1","T4","T4.1","Divine Interface — God to Human",
    "In this verse, does the characteristic operate from God toward the human person, and if so how? Record none if it does not.",
    "Word/term (lexical)",
    [
      slant("god-removes-sin", "God/Christ operates toward the person by REMOVING sin -- 'the Lamb of God, who takes away the sin of the world' (John 1:29), the whole forgiveness-of-sins formula.",
            strong="G0266", occurrences=occs("G0266",["John.1.29"])),
      slant("god-convicts-of-sin", "The Spirit operates toward the person by CONVICTING of sin (John 16:8) -- a distinct mode (exposure) from the remedy-mode above.",
            strong="G0266", occurrences=occs("G0266",["John.16.8"])),
      slant("no-operation-in-most", "Most occurrences show no God-to-human operation.", strong=None)
    ])

add("T4.1.2","T4","T4.1","Divine Interface — God to Human",
    "On what basis does God extend the characteristic — conditional, unconditional, covenantal, or responsive — as the evidence shows?",
    "Other non-human beings",
    [
      slant("unconditional-once-for-all", "Christ's removal of sin is presented as UNCONDITIONAL and final in Hebrews' argument -- 'once for all,' no further offering needed (Heb 10:12, 8:12's 'remember no more') -- a stronger basis than H_guilt's conditional/recognition-gated remedy.",
            strong="G0266", occurrences=occs("G0266",["Heb.10.12","Heb.8.12"]))
    ])

add("T4.1.3","T4","T4.1","Divine Interface — God to Human",
    "What does God's extension of the characteristic show about his disposition toward the human person?",
    "Other non-human beings",
    [
      slant("disposition-toward-decisive-removal", "God's disposition is toward decisively REMOVING sin's power and record, not merely managing it case by case -- the sustained Hebrews argument frames this as qualitatively different from (and superior to) the old system's repeated, incomplete remedy.",
            strong="G0266", occurrences=occs("G0266",["Heb.10.4"]))
    ])

add("T4.2.1","T4","T4.2","Divine Interface — Human to God",
    "In this verse, does the characteristic operate in the person's movement toward God — seeking, supplication, worship, covenant — and if so how? Record none if it does not.",
    "Word/term (lexical)",
    [
      slant("confession-as-movement-toward-God", "The recurring confession formula ('I have sinned... against you') IS a human-to-God movement -- far more pervasively documented in this family than in H_guilt.",
            strong="H2398", occurrences=occs("H2398",["2Sam.12.13"])),
      slant("prayer-for-forgiveness", "The Lord's Prayer's own petition ('forgive us our sins,' Luke 11:4) and confession/prayer 'covering' sins (Jas 5:15-16) name this movement explicitly as ongoing communal/personal practice.",
            strong="G0266", occurrences=occs("G0266",["Luke.11.4"]))
    ])

add("T4.2.2","T4","T4.2","Divine Interface — Human to God",
    "What inner posture does this movement require, as the evidence shows?",
    "Other non-human beings",
    [
      slant("acknowledgment-and-turning", "Acknowledgment/confession is the required posture, paired in Acts's preaching formula with REPENTANCE ('repentance for the forgiveness of sins,' Luke 24:47) -- a more developed posture-requirement than H_guilt's mere 'recognition.'",
            strong="G0266", occurrences=occs("G0266",["Luke.24.47"]))
    ])

add("T4.2.3","T4","T4.2","Divine Interface — Human to God",
    "What does the human-to-God direction of the characteristic show about the person's relationship with God?",
    "Other non-human beings",
    [
      slant("relationship-mediated-by-confession-and-grace", "The relationship is mediated by confession met with grace/forgiveness rather than by ritual procedure alone (contrast H_guilt's more procedurally-bound pattern) -- 1 John explicitly frames this as an ongoing, expected feature of the relationship ('if we confess... he will forgive,' 1:9 register), not an exceptional legal event.",
            strong="G0264", occurrences=occs("G0264",["1John.2.1"]))
    ])

add("T4.3.1","T4","T4.3","Human Interface — Giving",
    "In this verse, is the characteristic extended by one person toward another, and if so how does it operate in that extension? Record none if it is not.",
    "Word/term (lexical)",
    [
      slant("interpersonal-offense", "Sin operates directly person-to-person as an OFFENSE given: 'if your brother sins against you' (Matt 18:15, Luke 17:3-4) -- a genuine positive-extension case (one person wrongs another) that H_guilt's family lacked entirely.",
            strong="G0264", occurrences=occs("G0264",["Matt.18.15","Luke.17.3"]),
            observation_refs=["G0264 verse-grouping: interpersonal offense"]),
      slant("misleading-others-into-sin", "False teachers 'leading astray' weak women 'burdened with sins' (2Tim 3:6) is a genuine causing-another-to-sin case, structurally parallel to H_guilt's negligence cases but here an active, not merely negligent, extension.",
            strong="G0266", occurrences=occs("G0266",["2Tim.3.6"]))
    ])

add("T4.3.2","T4","T4.3","Human Interface — Giving",
    "What inner conditions or orientations in the giver accompany genuine extension of the characteristic?",
    "Characteristic relational",
    [
      slant("hostility-or-manipulation", "Where sin is actively given to another, the giver's orientation is hostile (offense against a brother) or manipulative/self-serving (false teachers exploiting the vulnerable, 2Tim 3:6) -- always a negative orientation, never a virtuous one, matching H_guilt's pattern that no positive 'giving' case exists in either family.",
            strong="G0266", occurrences=occs("G0266",["2Tim.3.6"]))
    ])

add("T4.3.3","T4","T4.3","Human Interface — Giving",
    "What does the evidence show a person must have received or become before they extend the characteristic?",
    "Characteristic relational",
    [
      slant("already-sinning-or-deceiving", "The false teachers of 2Tim 3 are themselves already characterized as deceivers; the sinning brother of Matt 18 needs no prior state at all, just committing the offense -- unlike H_guilt, no prior 'authority position' is required here; sin can simply be committed against anyone at any time.", strong="G0264/G0266")
    ])

add("T4.4.1","T4","T4.4","Human Interface — Receiving",
    "In this verse, is the characteristic taken up by a person from another, and if so how does it operate in that uptake? Record none if it is not.",
    "Word/term (lexical)",
    [
      slant("led-astray", "The weak women 'led astray' (2Tim 3:6) and the general pattern of 'bad company' corrupting (a cross-family echo of A_destroy's phtheiro material) show sin being taken up FROM another's influence.",
            strong="G0266", occurrences=occs("G0266",["2Tim.3.6"]))
    ],
    cross_flags=[{"statement":"2Tim 3:6's 'led astray' pattern echoes A_destroy's G5351 (phtheiro, 'bad company ruins good morals') material -- worth a direct comparison.","related_family":"A_destroy","related_cluster":None}])

add("T4.4.2","T4","T4.4","Human Interface — Receiving",
    "What inner conditions accompany or block uptake of the characteristic from another person?",
    "Characteristic relational",
    [
      slant("weakness-enables-uptake", "2Tim 3:6 explicitly names the receiving condition: being 'weak,' 'burdened with sins,' and 'led astray by various passions' -- a compound vulnerability profile, more explicit than anything in H_guilt's receiving cases.",
            strong="G0266", occurrences=occs("G0266",["2Tim.3.6"]))
    ])

add("T4.4.3","T4","T4.4","Human Interface — Receiving",
    "What is the inner-being state of the person who meets the characteristic from another but does not take it up?",
    "Characteristic relational",
    [
      slant("evidentiary-gap-again", "As with H_guilt, no occurrence directly shows a person refusing an attempted inducement to sin and describes their resulting inner state -- an evidentiary gap shared by both families so far.", strong=None)
    ])

add("T4.5.1","T4","T4.5","Human Interface — Boundaries",
    "Does the evidence show the characteristic operating differently within existing relational bonds versus across relational distance or difference; if so, how?",
    "Characteristic relational",
    [
      slant("within-community-discipline", "Within the believing community, sin triggers a defined discipline/restoration process (Matt 18, 1Tim 5:20's public rebuke, Jas 5:19-20's bringing back a wanderer).",
            strong="G0264/G0268", occurrences=occs("G0264",["Matt.18.15"])),
      slant("across-social-distance-labeling", "Across social distance, it operates as a LABEL applied to an entire outsider class ('tax collectors and sinners') that the label-user typically avoids -- a distancing function H_guilt did not show at all (guilt's cross-boundary case, Edom/Judah, was national-political, not a social-purity label).",
            strong="G0268", occurrences=occs("G0268",["Luke.15.1"]))
    ])

add("T4.5.2","T4","T4.5","Human Interface — Boundaries",
    "Does the characteristic operate within covenantal contexts only, or does it cross covenantal boundaries, as the evidence shows?",
    "Characteristic relational",
    [
      slant("crosses-boundaries-universally", "Crosses boundaries universally and explicitly -- 'all have sinned' (Rom 3:23), 'the whole world' under sin's power (Rom 3:9 register) -- stated at a more absolute, unqualified universal scope than H_guilt's cross-national but still bounded cases.",
            strong="G0264/G0266", occurrences=occs("G0264",["Rom.3.23"]))
    ])

add("T4.5.3","T4","T4.5","Human Interface — Boundaries",
    "What does the evidence show about the relational scope of the characteristic — who is included and who is not?",
    "Characteristic relational",
    [
      slant("all-included-Christ-excluded", "Included: universally, 'all have sinned' -- Jew and Gentile alike (Rom 3:9, 3:23), even the devil and fallen angels (1John 3:8, 2Pet 2:4). Excluded: Christ alone, explicitly and by name (2Cor 5:21, Heb 4:15) -- the widest inclusion-scope and the narrowest, most explicit exclusion found in either family so far.",
            strong="G0266", occurrences=occs("G0266",["Rom.3.23"]))
    ])

add("T4.6.1","T4","T4.6","Spiritual Beings Interface",
    "In this verse, does the characteristic operate in relation to other spiritual beings — angelic or adversarial — and if so how? Record none if it does not.",
    "Word/term (lexical)",
    [
      slant("devil-sins-and-fallen-angels-sinned", "Yes, directly and repeatedly, unlike H_guilt's clean negative: 'the devil has been sinning from the beginning' (1John 3:8) and 'the angels who sinned' and were cast into hell (2Pet 2:4) -- the characteristic is predicated of adversarial/angelic beings themselves, not merely connected to them.",
            strong="G0264", occurrences=occs("G0264",["1John.3.8","2Pet.2.4"]))
    ])

add("T4.6.2a","T4","T4.6","Spiritual Beings Interface",
    "Does an adversarial-being code ever appear as an acting party in a verse carrying this characteristic?",
    "Word/term (lexical)",
    [slant("yes", "Yes -- the devil is explicitly the acting subject of hamartano at 1John 3:8 ('the devil has been sinning from the beginning'), and the affiliation clause ('whoever keeps on sinning is of the devil') ties ongoing human sinning to that same adversarial party.",
           strong="G0264", occurrences=occs("G0264",["1John.3.8"]))])

add("T4.6.2b","T4","T4.6","Spiritual Beings Interface",
    "What does that pattern show about the characteristic being a site of adversarial activity?",
    "Other non-human beings",
    [slant("sin-is-a-confirmed-site-of-adversarial-activity", "Sin (unlike guilt) is a CONFIRMED site of adversarial activity in this cluster's own textual evidence -- the devil is not merely tempting toward sin from outside, he is himself said to sin, and the practice of sinning is used as a marker of spiritual paternity ('of the devil' vs. 'of God,' the same contrast 3:9-10 draws). This directly answers H_guilt's negative and gives the researcher's status-hypothesis its sharpest complication: sin has a genuine adversarial/spiritual-warfare dimension that guilt (a downstream legal status) apparently does not.",
           strong="G0264", occurrences=occs("G0264",["1John.3.8"]))],
    cross_flags=[{"statement":"Direct, confirmed contrast with H_guilt's T4.6.2b negative -- the clearest cross-family finding of this whole round; worth prioritizing in any cross-family synthesis.","related_family":"H_guilt","related_cluster":None}])

add("T4.6.3a","T4","T4.6","Spiritual Beings Interface",
    "Does an angelic-being code ever appear as an acting party in a verse carrying this characteristic?",
    "Word/term (lexical)",
    [slant("yes-fallen-angels", "Yes -- 'the angels who sinned' (2Pet 2:4) are the acting subject, though these are angels in their fallen/judged state, not angels in good standing acting rightly.",
           strong="G0264", occurrences=occs("G0264",["2Pet.2.4"]))])

add("T4.6.3b","T4","T4.6","Spiritual Beings Interface",
    "What does that pattern show about the characteristic being communicated, strengthened, or mediated through angelic ministry?",
    "Other non-human beings",
    [slant("not-mediation-but-shared-liability", "This is not angelic MEDIATION of sin to humans -- it shows sin as a category that also applies to (fallen) angels themselves, i.e. a shared moral-legal category across orders of created being, not a channel through which angels transmit sin to humans.",
           strong="G0264", occurrences=occs("G0264",["2Pet.2.4"]))])

# ================= T5 =================

add("T5.1.1","T5","T5.1","Nature of Transformation",
    "In this verse, does the characteristic produce transformation in the person, and if so does it change the person's condition, their orientation to their condition, or both? Record none if no transformation is shown.",
    "Verse-context",
    [
      slant("condition-change-slavery", "Produces a CONDITION change -- 'a slave to sin' (John 8:34) describes an actual change of governing status, not merely a changed orientation.",
            strong="G0266", occurrences=occs("G0266",["John.8.34"])),
      slant("orientation-change-confession", "The confession-formula occurrences produce an ORIENTATION change -- turning to acknowledge and seek remedy -- without necessarily narrating the underlying condition's removal in that verse.",
            strong="H2398", occurrences=occs("H2398",["2Sam.12.13"]))
    ])

add("T5.1.2","T5","T5.1","Nature of Transformation",
    "Is the transformation reversible or irreversible in the evidence?",
    "Characteristic (HIB behaviour)",
    [
      slant("reversible-via-Christ", "Reversible, and more emphatically/permanently so than H_guilt's remedy: Hebrews argues Christ's sacrifice removes sin decisively ('no longer any offering for sin,' 10:18) rather than merely making it addressable case by case.",
            strong="G0266", occurrences=occs("G0266",["Heb.10.18"])),
      slant("irreversible-in-Judas-case", "Irreversible in Judas's narrated case -- confession followed by no recorded remedy, ending in death.",
            strong="G0264", occurrences=occs("G0264",["Matt.27.4"]))
    ])

add("T5.2.1","T5","T5.2","Sequence of Inner States",
    "Does this verse describe a sequence of inner states the characteristic moves the person through — a before, during, and after — and what are those states? Record none if no sequence is shown.",
    "Verse-context",
    [
      slant("desire-sin-death-sequence", "James 1:15's full sequence: desire (before) -> conception/birth of sin (during) -> death when full-grown (after) -- the family's most explicit, self-contained sequence statement.",
            strong="G0266", occurrences=occs("G0266",["Jas.1.15","Jas.1.15"]))
    ])

add("T5.3.1","T5","T5.3","Mechanism of Change",
    "In this verse, by what mechanism does the characteristic produce change — discipline, encounter, gradual formation, sudden transformation, or other? Record none if no mechanism is shown.",
    "Verse-context",
    [
      slant("gradual-deceit-mechanism", "GRADUAL formation via deceit -- sin's 'deceitfulness' hardening the heart over repeated exposure (Heb 3:13) -- a mechanism category (gradual, deception-driven) that H_guilt's family did not name at all.",
            strong="G0266", occurrences=occs("G0266",["Heb.3.13"])),
      slant("sudden-encounter-mechanism", "SUDDEN transformation via direct encounter with Christ -- the healing/forgiveness pronouncements (Mark 2:5 etc.) change the person's status in a single declarative moment.",
            strong="G0266", occurrences=occs("G0266",["Mark.2.5"])),
      slant("ritual-mechanism", "Ritual/legal mechanism -- the Piel purification occurrences (H2398) change status through a priestly act, matching H_guilt's dominant mechanism.",
            strong="H2398", occurrences=occs("H2398",["Exod.29.36"]))
    ])

add("T5.3.2","T5","T5.3","Mechanism of Change",
    "Does the mechanism differ across contexts in the evidence; if so, how?",
    "Characteristic (HIB behaviour)",
    [
      slant("more-mechanisms-than-guilt", "Yes, and this family shows MORE distinct mechanisms than H_guilt did: ritual/legal, sudden-declarative (a Christ-encounter), and gradual-deceptive (Hebrews) are three genuinely different change-mechanisms, where H_guilt had ritual/legal, substitutionary, and disciplinary/punitive. The two families' mechanism-sets barely overlap (only 'ritual/legal' is shared), suggesting sin and guilt are not just different in seat (T2) but in how they are actually changed.", strong=None)
    ])

add("T5.4.1","T5","T5.4","Suffering and Affliction",
    "In this verse, does the characteristic operate in relation to suffering or affliction — as a response to it, a product of it, or a context for it? Record none if no such relation is shown.",
    "Verse-context",
    [
      slant("suffering-for-sin-vs-for-good", "1Pet 2:20 explicitly contrasts suffering 'for doing good' against suffering 'for doing wrong [sinning]' -- sin is the explanation FOR deserved suffering, in deliberate contrast to Christ's undeserved suffering (2:22-24 context).",
            strong="G0264/G0266", occurrences=occs("G0264",["1Pet.2.20"]))
    ])

add("T5.4.2","T5","T5.4","Suffering and Affliction",
    "What does the evidence show suffering doing to the characteristic in the person — and record no such effect if none is shown.",
    "Characteristic (HIB behaviour)",
    [
      slant("no-direct-effect-shown", "No occurrence shows suffering itself discharging or reducing sin the way H_guilt's punishment-bearing vocabulary did (Ezek 4's days-for-years) -- suffering here is more often the CONSEQUENCE or CONTRAST-POINT of sin than its resolution mechanism.", strong=None)
    ])

add("T5.5.1","T5","T5.5","Formation and Sanctification",
    "In this verse, does the characteristic participate in the longer arc of character formation and sanctification — shaping the person over time — and what does the evidence show of its role in that arc? Record none if no such participation is shown.",
    "Verse-context",
    [
      slant("negative-formation-hardening", "As with H_guilt, only a NEGATIVE formation arc is shown -- sin's deceitfulness hardening the heart over time (Heb 3:13) is the inverse of sanctification, not a positive contribution to it.",
            strong="G0266", occurrences=occs("G0266",["Heb.3.13"])),
      slant("resistance-as-implied-positive-arc", "Heb 12:1-4's athletic metaphor ('the sin which clings so closely,' 'struggle against sin,' resisting 'to the point of shedding blood') implies sin's role in a POSITIVE arc only as the thing actively resisted/thrown off during sanctification -- sin itself still doesn't form virtue, but the resistance to it is framed as part of the race.",
            strong="G0266", occurrences=occs("G0266",["Heb.12.1","Heb.12.4"]))
    ])

add("T5.6.1","T5","T5.6","Eschatological Trajectory",
    "In this verse, is the characteristic oriented toward an eschatological fullness — a future state toward which its present operation points — and what does its present experience anticipate of that fullness? Record none if no such orientation is shown.",
    "Verse-context",
    [
      slant("final-removal-anticipated", "Hebrews' whole argument anticipates a final state where sin's remembrance and effect are permanently gone ('remember their sins no more,' 8:12) -- an eschatological trajectory toward sin's total absence, more explicitly developed than H_guilt's single Servant-Song reference.",
            strong="G0266", occurrences=occs("G0266",["Heb.8.12"])),
      slant("judgment-trajectory-for-the-unrepentant", "For the impenitent, the trajectory runs the other way -- persecutors 'always' filling up their sins toward a wrath that 'has come upon them at last' (1Thess 2:16) -- an eschatological trajectory of accumulating judgment, the negative mirror of the removal-trajectory above.",
            strong="G0266", occurrences=occs("G0266",["1Thess.2.16"]))
    ])

assert len(answers) == 64, f"expected 64 questions answered, got {len(answers)}"

out = {
  "cluster_code": "M10",
  "family_id": "B_sin",
  "process": "1682-cluster-reading-process-d",
  "spec_round": 1,
  "catalogue_scope": "T0-T5",
  "questions_answered": len(answers),
  "answers": answers
}

with open('_analytics/Clusters/1682-test-m10-process-d-B_sin-v1-20260911.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("written, questions:", len(answers))
total_slants = sum(len(a['slants']) for a in answers)
print("total slants:", total_slants)
total_adjacent_flags = sum(len(a['needs_adjacent_verse_context']) for a in answers)
print("adjacent-context flags:", total_adjacent_flags)
total_cross_flags = sum(len(a['cross_family_or_cluster_flags']) for a in answers)
print("cross-family/cluster flags:", total_cross_flags)
