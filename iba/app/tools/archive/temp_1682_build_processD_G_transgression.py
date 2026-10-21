# -*- coding: utf-8 -*-
import json

with open('_analytics/Clusters/1682-test-m10-process-c-G_transgression-v2-20260911.json', encoding='utf-8') as f:
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
      slant("god-as-lawgiver-not-object", "God is related indirectly, as the LAWGIVER whose law defines the boundary being crossed -- 'where there is no law there is no transgression' (Rom 4:15) makes transgression parasitic on God's law existing, without naming God as its direct object in that verse.",
            strong="G3847", occurrences=occs("G3847",["Rom.4.15"])),
      slant("god-as-forgiver", "God/Christ acts as the one who FORGIVES/removes transgression -- the Lord's Prayer formula, 'blots out your transgressions' (Isa 44:22, 43:25), 'pardoning iniquity and passing over transgression' (Mic 7:18).",
            strong="G3900/H6588", occurrences=occs("H6588",["Mic.7.18","Isa.44.22"])),
      slant("god-as-wronged-object", "God is the direct wronged object in the majority of prophetic occurrences -- 'against God' is one of the three registers this family's own meaning block names explicitly for pesha.",
            strong="H6588", occurrences=occs("H6588",["Isa.59.12"]),
            observation_refs=["H6588 verse-grouping: three registers (individual/nation/God)"]),
      slant("angels-as-law-mediators", "Angels appear as MEDIATORS of the law itself, not as transgressors or as God's object -- 'the message declared by angels proved to be reliable, and every transgression... received a just retribution' (Heb 2:2) -- a distinct third relation: angelic beings stand behind the law's authority that transgression violates.",
            strong="G3847", occurrences=occs("G3847",["Heb.2.2"])),
      slant("not-related-to-God", "Most narrative/political-revolt/proverbial occurrences state no God-relation at all.", strong=None)
    ])

add("T0.1.2a","T0","T0.1","Divine Nature Reflected",
    "Across the characteristic's verses, is the characteristic ever predicated of God himself (not just present in a verse where God is also mentioned)?",
    "Other non-human beings",
    [
      slant("firm-negative", "No -- as with H_guilt and B_sin, transgression is never predicated of God himself anywhere in this family's 118 occurrences. God is lawgiver, wronged party, or forgiver -- never transgressor.", strong=None)
    ])

add("T0.1.2b","T0","T0.1","Divine Nature Reflected",
    "What does the pattern of presence/absence found in T0.1.2a indicate for the characteristic's place in the human person and in the divine image?",
    "Other non-human beings",
    [
      slant("transgression-presupposes-a-standard-outside-the-transgressor", "Transgression's defining logic (Rom 4:15's 'no law, no transgression') indicates it is structurally RELATIONAL to a standard that exists independently of and prior to the person -- unlike guilt (a status one falls into) or sin (a failed aim), transgression's very possibility depends on an external boundary already set by God. This makes it, if anything, the MOST clearly derivative of the three families examined so far: it cannot even be defined without first defining God's law.", strong=None)
    ])

add("T0.2.1","T0","T0.2","Created Purpose",
    "Does this verse state any purpose, role, or effect the characteristic serves in the person — what it leads the person to be, do, or become? Record it if stated; otherwise record none.",
    "Verse-context",
    [
      slant("produces-retribution", "Transgression's stated effect is a 'just retribution' following automatically (Heb 2:2) -- a consequence-mechanism, not an inner formative effect.",
            strong="G3847", occurrences=occs("G3847",["Heb.2.2"])),
      slant("produces-affliction", "At national scale, accumulated transgression is named as the direct CAUSE of affliction and captivity -- 'the Lord has afflicted her for the multitude of her transgressions' (Lam 1:5).",
            strong="H6588", occurrences=occs("H6588",["Lam.1.5"]),
            observation_refs=["H6588 instance-meaning: Lam 1:5 accumulating-load"]),
      slant("no-stated-effect", "Most occurrences (the Amos formula, proverbial statements, narrative confessions) state the transgression without a further stated inner effect.", strong=None)
    ])

add("T0.2.2","T0","T0.2","Created Purpose",
    "Across the evidence, does the characteristic's role read as belonging to created design, to the fallen condition, to both, or as not determinable?",
    "Other non-human beings",
    [
      slant("fallen-condition-with-cosmic-order-contrast", "Fallen condition throughout the human occurrences, but this family uniquely also shows the CREATED-ORDER contrast case directly: the sea 'transgressing' its assigned limit is explicitly NOT what happens, because wisdom fixed that limit at creation (Prov 8:29) -- the cosmos keeps its boundary perfectly where humans do not, making the human failure to keep boundaries a departure FROM a working creational pattern that still holds elsewhere in creation.",
            strong="H5674D", occurrences=occs("H5674D",["Prov.8.29"]),
            observation_refs=["H5674D instance-meaning: no human moral content, cosmic-physical case"])
    ])

add("T0.2.3","T0","T0.2","Created Purpose",
    "Across the evidence, is there any orientation toward a future fullness — something the person moves toward, not only what they currently are? Record it, or record none.",
    "Other non-human beings",
    [
      slant("zion-turning-from-transgression", "Isa 59:20 names a future turning-point: transgression will be turned FROM at Zion's redemption -- an explicit forward-looking resolution distinct from H_guilt's single Servant-Song reference and closer to B_sin's Hebrews trajectory.",
            strong="H6588", occurrences=occs("H6588",["Isa.59.20"]),
            observation_refs=["H6588 instance-meaning: named-individual/nation cases"]),
      slant("no-orientation-elsewhere", "Most occurrences show no future-fullness orientation.", strong=None)
    ])

add("T0.3.1","T0","T0.3","Image-Bearer Expression",
    "From the characteristic's God-relation (T0.1) and its role (T0.2), what aspect of the divine likeness, if any, does it instantiate in the person? Record the aspect, or record none.",
    "Other non-human beings",
    [
      slant("none-the-cosmos-keeps-the-pattern-instead", "None in the person -- but the sea's non-transgression of its limit (Prov 8:29) shows the PATTERN of boundary-keeping itself belongs to wisdom's created design; humans fail to instantiate a pattern the rest of creation keeps without difficulty.",
            strong="H5674D", occurrences=occs("H5674D",["Prov.8.29"]))
    ])

add("T0.3.2","T0","T0.3","Image-Bearer Expression",
    "Across the evidence, is the characteristic shared between God and the person, or an exclusively creaturely analogue to something in God?",
    "Other non-human beings",
    [
      slant("exclusively-creaturely", "Exclusively creaturely -- no positive divine analogue exists for transgression anywhere in this family.", strong=None)
    ])

add("T0.3.3","T0","T0.3","Image-Bearer Expression",
    "Where the characteristic is present or absent in a person, what does that indicate about the condition of the divine image in them — or is no such indication evidenced?",
    "Other non-human beings",
    [
      slant("presence-indicates-boundary-blindness", "Where present, it indicates a person who does not (or will not) recognize the LORD's boundary as binding -- Ps 17:3's self-examined 'I will not transgress' (with the mouth) is this family's clearest positive-absence case, framed as a deliberate, examined self-restraint rather than a status simply avoided.",
            strong="H5674D", occurrences=occs("H5674D",["Ps.17.3"]))
    ])

add("T0.4.1","T0","T0.4","Typological Significance",
    "Does this verse use the characteristic typologically — pointing beyond the immediate to a covenantal, eschatological, or christological reality; if so, which, and in which direction (the divine instance establishing the pattern, or the human pointing toward the divine)? Record the use and direction, or record none.",
    "Verse-context",
    [
      slant("adam-typology", "Rom 5:14/Hos 6:7's Adam-paradigm is explicitly typological -- Adam's transgression as the type, later reversed by Christ; Hosea uses the same comparison ('like Adam, they transgressed the covenant').",
            strong="G3847/H5674D", occurrences=occs("G3847",["Rom.5.14"])+occs("H5674D",["Hos.6.7"])),
      slant("isaiah-53-christological", "Isa 53:5's 'pierced for our transgressions' is explicitly christological, the fourth strong across three families to independently cite this one verse.",
            strong="H6588", occurrences=occs("H6588",["Isa.53.5"]),
            observation_refs=["H6588 instance-meaning: Isaiah 53 convergence"]),
      slant("no-typology-elsewhere", "Most occurrences show no typological signal.", strong=None)
    ],
    cross_flags=[{"statement":"Isaiah 53:5 is now cited independently by four strongs across three families (H_guilt's H0817/H5375J, family D's H5771G, and here H6588) -- the single most heavily cross-referenced verse found in M10 so far.","related_family":"H_guilt","related_cluster":None}])

# ================= T1 =================

add("T1.1.1","T1","T1.1","Name and Naming",
    "What is the characteristic called in the programme, and what does the name signal about its essential nature?",
    "Word/term (lexical)",
    [
      slant("transgression-is-boundary-crossing", "Called 'Transgression' (G_transgression, M10). The name signals a spatial/legal metaphor -- STEPPING PAST or CROSSING a fixed line -- more literally boundary-oriented than either guilt (a status) or sin (missing a target); several occurrences show the literal spatial sense surfacing directly in translation ('bounds,' Jer 5:28; 'turned aside,' Acts 1:25).",
            strong="G3845/H5674D", occurrences=occs("H5674D",["Jer.5.28"]))
    ])

add("T1.1.2","T1","T1.1","Name and Naming",
    "What do the primary Hebrew and Greek terms show at the definitional level?",
    "Word/term (lexical)",
    [
      slant("parabaino-step-past", "parabaino/parabasis (Greek) roots literally in 'step beside/past' -- the family's noun form (parabasis) even states its own definitional dependency on law: 'where there is no law there is no transgression' (Rom 4:15).", strong="G3845/G3847"),
      slant("avar-pass-over", "avar (Hebrew, H5674D) is a general 'pass over/through/by' verb with the moral sense as one branch among many -- unlike chata (sin) or asham (guilt), which are dedicated moral roots, avar's moral use borrows a general motion-verb.", strong="H5674D"),
      slant("pasha-fuses-transgress-and-revolt", "pasha (H6586/H6588) fuses 'transgress' and 'rebel/revolt' as a single lexeme -- the same root names religious sin and political insurrection, distinguished only by grammatical tense-environment, not by a different word.",
            strong="H6586", occurrences=[],
            observation_refs=["H6586 difference-inference: political vs religious tense split"])
    ])

add("T1.1.3","T1","T1.1","Name and Naming",
    "What directional, relational, or constitutional implication does the name carry?",
    "Word/term (lexical)",
    [
      slant("crossing-implies-a-fixed-external-line", "'Crossing/passing beyond' implies a FIXED, EXTERNALLY-SET line that exists prior to and independent of the person -- the person moves, the boundary does not. This is the sharpest directional implication of the three families read so far: guilt is entered, sin is missed, transgression is crossed.", strong=None),
      slant("revolt-implies-rejected-authority", "pasha's 'rebel' sense implies REJECTED AUTHORITY -- not just crossing a line but repudiating the ruler who set it, whether a king (political revolt) or God (religious rebellion).", strong="H6586")
    ])

add("T1.2.1","T1","T1.2","Kind",
    "What kind of inner-being phenomenon is the characteristic — an act, a disposition, a condition/status, a quality, or something else?",
    "Characteristic (HIB behaviour)",
    [
      slant("dominantly-a-counted-status", "Predominantly a COUNTED STATUS/QUANTITY -- pesha (H6588, the family's largest and most frequent strong by far) is overwhelmingly a noun tallied in Amos's 'three... and four' formula, described as accumulating ('abundance,' 'multitude'), sealed in a bag, borne as a load. This is much closer to H_guilt's status-profile than to B_sin's agentive-power profile.",
            strong="H6588", occurrences=occs("H6588",["Amos.1.3","Lam.1.5"]),
            observation_refs=["H6588 verse-grouping: Amos formula","H6588 verse-grouping: accumulating load"]),
      slant("also-an-identity-noun", "parabates/pasha's participle forms also make it a PERSON-IDENTITY category ('a transgressor,' 'rebels') -- the same participle-as-identity pattern already found in na'aph/bagad/pathah.",
            strong="G3848/H6586", occurrences=occs("H6586",["Isa.1.28"]),
            observation_refs=["H6586 verse-grouping: participle-as-identity pattern"]),
      slant("one-partial-agentive-exception", "One occurrence gives transgression a quasi-agentive voice, echoing (faintly) B_sin's Romans-7 personification: 'Transgression speaks to the wicked deep in his heart' (Ps 36:1) -- transgression here SPEAKS, though as an external voice addressing the heart, not (like sin) an indwelling ruling power.",
            strong="H6588", occurrences=occs("H6588",["Ps.36.1"]),
            observation_refs=["H6588 verse-grouping: general wisdom-proverb statements"])
    ],
    cross_flags=[{"statement":"Ps 36:1's 'transgression speaks... deep in his heart' is worth comparing directly against B_sin's Rom 7 personification -- both give the characteristic a speaking/acting voice, but with different registers (external address vs. indwelling power); a genuine three-way comparison point for guilt/sin/transgression's differing degrees of personification.","related_family":"B_sin","related_cluster":None}])

add("T1.2.2","T1","T1.2","Kind",
    "Is the characteristic simple in structure, or does it combine constituent elements; if compound, which?",
    "Characteristic (HIB behaviour)",
    [
      slant("recognition-accrual-remedy-compound", "This family's own meaning block names a three-part compound structure explicitly: transgression 'as recognised by sinner... as God deals with it... as God forgives' -- a built-in recognition-accrual-remedy sequence, the most explicitly staged compound structure found in any M10 family so far.",
            strong="H6588", occurrences=occs("H6588",["Ps.51.3","Mic.7.18"]),
            observation_refs=["H6588 verse-grouping: recognition-accrual-remedy sequence"])
    ])

add("T1.3.1","T1","T1.3","Boundary",
    "What stands against the characteristic as its structural opposite — the inner-being reality that excludes it?",
    "Characteristic (HIB behaviour)",
    [
      slant("self-examined-restraint", "Deliberate, self-examined restraint -- 'I have kept my ways and have not transgressed' (Ps 17:3 register), the psalmist actively guarding his own mouth as the boundary-opposite.",
            strong="H5674D", occurrences=occs("H5674D",["Ps.17.3"])),
      slant("kept-limit-by-design", "The sea's kept limit (Prov 8:29) is this family's non-human structural opposite -- an ordained boundary actually held, not merely avoided by choice.",
            strong="H5674D", occurrences=occs("H5674D",["Prov.8.29"]))
    ])

add("T1.3.2","T1","T1.3","Boundary",
    "What does the characteristic exclude or resist at its edge?",
    "Characteristic (HIB behaviour)",
    [
      slant("denial-that-an-act-counts", "Prov 28:24's flat denial ('whoever robs his father or mother and says, \"That is no transgression\"') shows the category's edge being actively DISPUTED by the offender himself -- a boundary-policing move from inside, not outside.",
            strong="H6588", occurrences=occs("H6588",["Prov.28.24"]),
            observation_refs=["H6588 verse-grouping: general wisdom-proverb statements"])
    ])

add("T1.3.3","T1","T1.3","Boundary",
    "Where does the characteristic end and another thing begin — what is it not?",
    "Characteristic (HIB behaviour)",
    [
      slant("transgression-vs-fall-in-faith", "paraptoma's own meaning block carries a second sense -- 'a fall in faith' -- attested directly at Rom 11:11-12's description of Israel's 'trespass/stumble,' distinct from a moral crime: the same word spans a specific committed wrong and a corporate faith-stumble.",
            strong="G3900", occurrences=occs("G3900",["Rom.11.11","Rom.11.12"]),
            observation_refs=["G3900 instance-meaning: Rom 11:11-12 fall-in-faith sense"]),
      slant("transgression-vs-revolt", "H6586/pasha's identical form spans religious transgression and political revolt, distinguished only by grammatical tense-environment (waw-consecutive narrative-past for revolt, perfect/infinitive for confession) -- the boundary between a theological category and a purely secular-political one is carried by grammar, not vocabulary.",
            strong="H6586", occurrences=[])
    ])

add("T1.4.1a","T1","T1.4","Modes of Operation",
    "What is the grammatical/stem form of the characteristic's primary term in this verse?",
    "Word/term (lexical)",
    [
      slant("greek-forms", "Verb forms (V-PAI/V-2AAI etc.) for parabaino; noun forms (N-*SF/N-*SN) for parabasis/paraptoma; person-noun (N-*SM) for parabates.", strong="G3845/G3847/G3848/G3900"),
      slant("hebrew-forms", "Qal (H5674D throughout its moral sense; H6586's dominant stem); one Niphal passive (H6586 Prov 18:19, 'a brother offended' -- the sole receiving-end form); construct nouns (HNcmsc/HNcmpc, H6588's dominant morph, marking WHOSE transgression it is grammatically in almost every occurrence).", strong="H5674D/H6586/H6588")
    ])

add("T1.4.1b","T1","T1.4","Modes of Operation",
    "In what distinct mode(s) does the characteristic operate within the inner person in this verse — the manner of its functioning?",
    "Verse-context",
    [
      slant("counted-tallied-mode", "As a TALLIED quantity -- the Amos formula's 'three... and four,' 'abundance,' 'multitude' -- transgression operates by ACCUMULATING as a countable record.",
            strong="H6588", occurrences=occs("H6588",["Amos.1.3"])),
      slant("borne-load-mode", "As a BORNE LOAD -- 'bound into a yoke... set upon my neck' (Lam 1:14), 'sealed up in a bag' (Job 14:17) -- weight-imagery closely paralleling H_guilt's nasa material.",
            strong="H6588", occurrences=occs("H6588",["Lam.1.14","Job.14.17"])),
      slant("spoken-address-mode", "As a SPOKEN address to the heart (Ps 36:1) -- the one quasi-agentive exception noted above.",
            strong="H6588", occurrences=occs("H6588",["Ps.36.1"])),
      slant("crossed-boundary-mode", "As a literal CROSSING -- the root's spatial sense surfacing directly ('turned aside,' 'bounds,' 'goes on ahead').",
            strong="G3845/H5674D", occurrences=occs("G3845",["Acts.1.25"]))
    ])

add("T1.4.2","T1","T1.4","Modes of Operation",
    "Does the mode of operation vary by context, direction, or constitutional level; if so, how?",
    "Characteristic (HIB behaviour)",
    [
      slant("varies-by-strong-and-register", "Yes -- tallied/counted, borne/carried, spoken/addressed, and literally-crossed are four distinct modes tracking which strong and literary register is in view (prophetic indictment, wisdom-proverb, narrative, legal-covenant), similar in kind to H_guilt's per-strong variation but with more distinct modes attested.", strong=None)
    ])

add("T1.4.3","T1","T1.4","Modes of Operation",
    "Does the characteristic operate through a communicative or speech-based mode (commanded, addressed, spoken); if so, how? Record it, or record none.",
    "Characteristic (HIB behaviour)",
    [
      slant("confessional-speech", "Confessional speech throughout the recognition-group ('I know my transgressions,' Ps 51:3; Job's plea, Job 13:23/7:21).",
            strong="H6588", occurrences=occs("H6588",["Ps.51.3","Job.7.21"])),
      slant("transgression-itself-speaks", "Uniquely in this family, the characteristic itself is the SPEAKER, not just the topic of speech: 'Transgression speaks to the wicked deep in his heart' (Ps 36:1).",
            strong="H6588", occurrences=occs("H6588",["Ps.36.1"]))
    ])

add("T1.5.1","T1","T1.5","Immediate Response",
    "What first or most immediate inner-being response does this verse show following the characteristic? Record it, or record none.",
    "Verse-context",
    [
      slant("immediate-plea-for-removal", "Immediate plea for removal -- 'blot out my transgressions' (Ps 51:1), 'why do you not pardon my transgression' (Job 7:21).",
            strong="H6588", occurrences=occs("H6588",["Ps.51.1","Job.7.21"])),
      slant("immediate-retribution", "Immediate/automatic retribution follows, with no described inner reaction from the offender at all (Heb 2:2's 'received a just retribution').",
            strong="G3847", occurrences=occs("G3847",["Heb.2.2"])),
      slant("immediate-denial", "Immediate denial that the act even qualifies (Prov 28:24).",
            strong="H6588", occurrences=occs("H6588",["Prov.28.24"]))
    ])

add("T1.5.2","T1","T1.5","Immediate Response",
    "Across the verses, is that immediate response consistent or varied?",
    "Characteristic (HIB behaviour)",
    [
      slant("varied-plea-dominant", "Varied, but plea/confession is the single most frequent response by volume -- more concentrated than H_guilt's scattered set, though not as singularly dominant as B_sin's near-mechanical confession formula.", strong=None)
    ])

add("T1.6.1","T1","T1.6","Sustained Effect",
    "What does the characteristic produce in the inner being over time in this verse — what states, qualities, capacities, or orientations does it establish? Record it, or record none.",
    "Verse-context",
    [
      slant("accumulating-multitude", "An accumulating, nameable quantity over time -- 'abundance of their transgressions' (Ps 5:10), 'multitude of her transgressions' (Lam 1:5) -- the same compound-interest image already found for H0819's guilt.",
            strong="H6588", occurrences=occs("H6588",["Ps.5.10","Lam.1.5"])),
      slant("no-sustained-effect-elsewhere", "Most occurrences state no sustained effect beyond the single named act.", strong=None)
    ])

add("T1.6.3","T1","T1.6","Sustained Effect",
    "How does the sustained effect differ from the immediate response (T1.5)?",
    "Characteristic (HIB behaviour)",
    [
      slant("single-act-to-cumulative-record", "Immediate response is a single spoken plea or an automatic retributive consequence; sustained effect is a CUMULATIVE RECORD (a growing tally, a growing load) that persists independently of any one act -- structurally identical to H_guilt's compound-interest pattern, reinforcing that guilt and transgression share this particular behaviour even where sin (agentive, indwelling) does not.", strong=None)
    ])

add("T1.7.1","T1","T1.7","Conditions of Reception",
    "Under what inner conditions does the characteristic take hold or operate rightly?",
    "Characteristic (HIB behaviour)",
    [
      slant("existence-of-law-is-the-precondition", "The law's very existence is the stated precondition for transgression to be possible at all (Rom 4:15) -- an unusually explicit, almost definitional, condition-of-possibility statement not paralleled this directly in either H_guilt or B_sin.",
            strong="G3847", occurrences=occs("G3847",["Rom.4.15"]))
    ])

add("T1.7.2","T1","T1.7","Conditions of Reception",
    "Under what inner conditions is the characteristic blocked, distorted, resisted, or not taken up — including, where the evidence shows it, distortion or interference by another spirit (adversarial or angelic)?",
    "Characteristic (HIB behaviour)",
    [
      slant("angelic-mediation-of-the-standard-not-distortion", "Angels appear here in a THIRD role distinct from either H_guilt's clean negative or B_sin's adversarial-affiliation positive: angels MEDIATE the very law whose transgression carries penalty (Heb 2:2) -- a positive, non-distorting angelic involvement in the standard itself, not interference with a person's compliance.",
            strong="G3847", occurrences=occs("G3847",["Heb.2.2"])),
      slant("no-adversarial-transgressor-found", "Unlike B_sin (where the devil himself is said to sin), no occurrence in this family names an adversarial being as a transgressor or as distorting a person's keeping of the boundary.", strong=None)
    ],
    cross_flags=[{"statement":"Three-way pattern now visible across H_guilt/B_sin/G_transgression on spiritual-beings involvement: guilt = clean negative both angelic and adversarial; sin = positive both (devil sins, angels sinned); transgression = positive angelic (mediating the law) but negative adversarial (no transgressor-devil case). Worth a dedicated cross-family synthesis once more families are read.","related_family":"H_guilt","related_cluster":None}])

add("T1.7.3","T1","T1.7","Conditions of Reception",
    "What is the inner-being state of the person in whom the characteristic is present but does not take hold?",
    "The HIB",
    [
      slant("self-denial-of-category", "Prov 28:24's offender: the characteristic is present (by the proverb's own moral judgment) but does not take hold in the person's self-understanding -- their inner state is one of active category-denial, structurally similar to B_sin's/H_guilt's self-justifying deniers (Jer 50:7).",
            strong="H6588", occurrences=occs("H6588",["Prov.28.24"]))
    ])

# ================= T2 =================

add("T2.1.1","T2","T2.1","Spirit-Level Location",
    "At which constitutional level(s) does this verse locate the characteristic — from {spirit, soul, heart, mind, other soul-subset, a named body part} — and how is each engaged? Record every level evidenced, or none.",
    "Verse-context",
    [
      slant("heart-engaged-once", "HEART is explicitly engaged, uniquely in this family among the ones read so far in this specific way: 'Transgression speaks to the wicked deep in his heart' (Ps 36:1) -- the heart as the site addressed by the characteristic, paired with 'no fear of God before his eyes' in the same verse (a second, visual/perceptual faculty in the same breath).",
            strong="H6588", occurrences=occs("H6588",["Ps.36.1"])),
      slant("mouth-as-self-guarded-boundary", "MOUTH is named as a self-guarded boundary -- Ps 17:3's resolve that his mouth 'will not transgress,' a specific bodily/faculty location for the self-imposed limit.",
            strong="H5674D", occurrences=occs("H5674D",["Ps.17.3"])),
      slant("no-level-named-elsewhere", "The overwhelming majority of occurrences (the Amos formula, the load-imagery, the political-revolt uses, the confession formulas) name no constitutional level at all.", strong=None)
    ])

add("T2.1.2","T2","T2.1","Spirit-Level Location",
    "Across the verses, what does the pattern of engaged and absent levels indicate — the characteristic's depth and seat, the levels it never engages, and (for any body link) whether the link is emphatic, functional, expressive, indicative, or mediating?",
    "The HIB",
    [
      slant("intermediate-between-guilt-and-sin", "This family sits BETWEEN H_guilt (no constitutional engagement at all) and B_sin (mind and body directly engaged as an operating site, Rom 7): transgression touches the heart and mouth in isolated, occasional verses (Ps 36:1, Ps 17:3) rather than as a sustained operating description -- present but thin, not absent and not systemic.", strong=None)
    ],
    cross_flags=[{"statement":"A three-family T2 gradient is now visible: guilt (none) < transgression (thin, occasional) < sin (systemic, Romans 7). Worth testing whether this gradient holds or breaks once more families are read -- it would be a significant structural finding for the status-vs-characteristic hypothesis if it holds.","related_family":"H_guilt","related_cluster":None}])

add("T2.10.1","T2","T2.10","Constitutional Movement",
    "Does the characteristic move across constitutional levels (spirit→soul→body), or onto the person from an external source — including another spirit (angelic or adversarial) — or in another direction; and if so in what sequence or pattern? If no movement, record none.",
    "The HIB",
    [
      slant("speaks-inward-to-heart", "Ps 36:1 shows a movement pattern: transgression (as if external) SPEAKS inward, reaching the heart -- an outside-to-inside movement distinct from H_guilt's off-the-guilty-party substitutionary movement and from sin's already-indwelling-power framing.",
            strong="H6588", occurrences=occs("H6588",["Ps.36.1"])),
      slant("no-movement-elsewhere", "Most occurrences show no stated movement across levels.", strong=None)
    ])

add("T2.7.1","T2","T2.7","Body — Direction",
    "Where a body link exists (from the T2.1.1 audit), in which direction does it run — soul/spirit expressing through the body, the body feeding back to the soul, or both — and what follows from that direction? If no body link, record none.",
    "The HIB",
    [
      slant("mouth-as-outward-guard", "The mouth-link (Ps 17:3) runs OUTWARD -- an inner resolve (self-examination) expressing as guarded speech -- the inner state governs the bodily boundary, not the reverse.",
            strong="H5674D", occurrences=occs("H5674D",["Ps.17.3"]))
    ])

add("T2.9.1","T2","T2.9","Origin and Source",
    "Where does this verse say the characteristic originates — generated within the person, received from another person, bestowed by God, carried generationally, introduced by another spirit (angelic or adversarial), or not stated?",
    "Verse-context",
    [
      slant("generated-within", "Generated within, by one's own act -- the dominant pattern (confession formulas, the Amos indictments, political revolts each attributed to the revolting party's own decision).", strong="H6586/H6588"),
      slant("adam-generational-paradigm", "A generational PARADIGM (not an automatic transmission mechanism like B_sin's Rom 5:12, but a repeated pattern/type) -- Adam's transgression cited as the model later generations are compared to and re-enact (Hos 6:7, Rom 5:14) rather than a claim that Adam's specific transgression is inherited wholesale.",
            strong="H5674D/G3847", occurrences=occs("H5674D",["Hos.6.7"])),
      slant("law-mediated-by-angels", "The STANDARD whose crossing constitutes transgression originates in a message mediated by angels (Heb 2:2) -- the boundary's own origin, not the transgressive act's origin, is angelically mediated.",
            strong="G3847", occurrences=occs("G3847",["Heb.2.2"]))
    ])

add("T2.9.2","T2","T2.9","Origin and Source",
    "Across the verses, is the origin single or multiple, and does it change with context?",
    "Characteristic (HIB behaviour)",
    [
      slant("multiple-types-paradigm-not-transmission", "Multiple, but notably this family's 'generational' origin-type is a PARADIGM/TYPOLOGY (later generations re-enacting Adam's pattern) rather than B_sin's stronger claim of an actual transmission mechanism (Rom 5:12's 'entered the world') -- a real, specific difference in how the same Adam-material is used across the two families.", strong=None)
    ])

# ================= T4 =================

add("T4.1.1","T4","T4.1","Divine Interface — God to Human",
    "In this verse, does the characteristic operate from God toward the human person, and if so how? Record none if it does not.",
    "Word/term (lexical)",
    [
      slant("god-forgives-blots-out", "God acts toward the person by forgiving/blotting out transgression (Isa 44:22, 43:25, Mic 7:18) -- the dominant God-to-human operation in this family, matching H_guilt's remedy-pattern.",
            strong="H6588", occurrences=occs("H6588",["Isa.44.22"])),
      slant("no-operation-in-most", "Most occurrences show no God-to-human operation.", strong=None)
    ])

add("T4.1.2","T4","T4.1","Divine Interface — God to Human",
    "On what basis does God extend the characteristic — conditional, unconditional, covenantal, or responsive — as the evidence shows?",
    "Other non-human beings",
    [
      slant("mercy-based-not-merit-based", "Explicitly on the basis of MERCY, stated directly: 'according to your abundant mercy blot out my transgressions' (Ps 51:1) -- the petitioner names the basis himself as God's character, not any procedure completed.",
            strong="H6588", occurrences=occs("H6588",["Ps.51.1"]))
    ])

add("T4.1.3","T4","T4.1","Divine Interface — God to Human",
    "What does God's extension of the characteristic show about his disposition toward the human person?",
    "Other non-human beings",
    [
      slant("disposition-toward-mercy-over-tally", "Mic 7:18's rhetorical question ('who is a God like you, pardoning iniquity and passing over transgression?') frames mercy as God's own distinguishing characteristic against a backdrop where the default expectation would be tallying/retribution (Heb 2:2's 'just retribution') -- disposition toward mercy is presented as remarkable precisely because strict accounting is the norm this family otherwise assumes.",
            strong="H6588", occurrences=occs("H6588",["Mic.7.18"]))
    ])

add("T4.2.1","T4","T4.2","Divine Interface — Human to God",
    "In this verse, does the characteristic operate in the person's movement toward God — seeking, supplication, worship, covenant — and if so how? Record none if it does not.",
    "Word/term (lexical)",
    [
      slant("plea-as-movement-toward-God", "The recognition-group's pleas ('blot out,' 'pardon my transgression') are direct petitionary movement toward God.",
            strong="H6588", occurrences=occs("H6588",["Ps.51.1","Job.7.21"]))
    ])

add("T4.2.2","T4","T4.2","Divine Interface — Human to God",
    "What inner posture does this movement require, as the evidence shows?",
    "Other non-human beings",
    [
      slant("acknowledgment-plus-appeal-to-mercy", "Acknowledgment of the specific transgression PLUS an explicit appeal to God's character (mercy) rather than to a completed legal procedure -- a more personal, less procedural posture than H_guilt's cultic-recognition formula.",
            strong="H6588", occurrences=occs("H6588",["Ps.51.1"]))
    ])

add("T4.2.3","T4","T4.2","Divine Interface — Human to God",
    "What does the human-to-God direction of the characteristic show about the person's relationship with God?",
    "Other non-human beings",
    [
      slant("relationship-personal-not-only-procedural", "The relationship is personal and appeal-based (mercy invoked directly) at least as much as procedural -- closer to B_sin's confession-and-grace pattern than to H_guilt's more ritual-bound one.", strong=None)
    ])

add("T4.3.1","T4","T4.3","Human Interface — Giving",
    "In this verse, is the characteristic extended by one person toward another, and if so how does it operate in that extension? Record none if it is not.",
    "Word/term (lexical)",
    [
      slant("individual-offense-against-another", "Jacob's demand of Laban 'what is my transgression?' (Gen 31:36) treats transgression as a specific wrong one person could have committed against another -- the individual-against-individual register this family's own meaning block names.",
            strong="H6588", occurrences=occs("H6588",["Gen.31.36"]),
            observation_refs=["H6588 verse-grouping: three registers"]),
      slant("political-revolt-as-collective-extension", "At national scale, one people's revolt against another's rule (Moab, Edom, Israel against the house of David) is a collective, political form of the same person-to-person-scaled extension.",
            strong="H6586", occurrences=occs("H6586",["2Kgs.1.1","1Kgs.12.19"]))
    ])

add("T4.3.2","T4","T4.3","Human Interface — Giving",
    "What inner conditions or orientations in the giver accompany genuine extension of the characteristic?",
    "Characteristic relational",
    [
      slant("no-positive-case-again", "As with H_guilt and B_sin, no occurrence shows a virtuous inner condition accompanying an extension of transgression toward another -- every case (offense, revolt) is adversarial by definition.", strong=None)
    ])

add("T4.3.3","T4","T4.3","Human Interface — Giving",
    "What does the evidence show a person must have received or become before they extend the characteristic?",
    "Characteristic relational",
    [
      slant("prior-rejection-of-authority", "For the revolt-cases specifically, the giver must first have decided to reject an established authority's rule -- a specific prior orientation (rejection of legitimate rule) this family names more explicitly than H_guilt or B_sin did for their own person-to-person cases.",
            strong="H6586", occurrences=occs("H6586",["2Kgs.8.22"]))
    ])

add("T4.4.1","T4","T4.4","Human Interface — Receiving",
    "In this verse, is the characteristic taken up by a person from another, and if so how does it operate in that uptake? Record none if it is not.",
    "Word/term (lexical)",
    [
      slant("no-clear-receiving-case", "No occurrence clearly shows one person's transgression being 'taken up' from another the way H_guilt's Num 30:15 or B_sin's 2Tim 3:6 did -- this family's person-to-person cases (offense, revolt) are given/committed, not passed on or absorbed by another.", strong=None)
    ])

add("T4.4.2","T4","T4.4","Human Interface — Receiving",
    "What inner conditions accompany or block uptake of the characteristic from another person?",
    "Characteristic relational",
    [
      slant("not-evidenced", "Not evidenced in this family -- consistent with T4.4.1's finding of no clear receiving-case at all.", strong=None)
    ])

add("T4.4.3","T4","T4.4","Human Interface — Receiving",
    "What is the inner-being state of the person who meets the characteristic from another but does not take it up?",
    "Characteristic relational",
    [
      slant("prov-18-19-passive-recipient", "Prov 18:19's Niphal 'a brother offended' is the closest case -- naming the person on the RECEIVING end of another's offense, though the verse describes the relational damage that follows, not an inner state of refusing uptake.",
            strong="H6586", occurrences=occs("H6586",["Prov.18.19"]),
            observation_refs=["H6586 difference-inference: the one Niphal form"])
    ])

add("T4.5.1","T4","T4.5","Human Interface — Boundaries",
    "Does the evidence show the characteristic operating differently within existing relational bonds versus across relational distance or difference; if so, how?",
    "Characteristic relational",
    [
      slant("within-bond-covenant-breach", "Within a bond, it operates as covenant-breach with a named party (Israel's covenant, Judg 2:20; the everlasting covenant, Isa 24:5) -- a violation of an existing relationship's terms.",
            strong="H5674D", occurrences=occs("H5674D",["Judg.2.20","Isa.24.5"])),
      slant("across-distance-political-revolt", "Across political/national distance, it operates as outright REVOLT against an imposed rule with no prior personal bond assumed (Moab, Edom against Judah/Israel) -- a rejection of external authority rather than a breach of a covenant one had entered voluntarily.",
            strong="H6586", occurrences=occs("H6586",["2Kgs.3.7","2Kgs.8.22"]))
    ])

add("T4.5.2","T4","T4.5","Human Interface — Boundaries",
    "Does the characteristic operate within covenantal contexts only, or does it cross covenantal boundaries, as the evidence shows?",
    "Characteristic relational",
    [
      slant("both-covenantal-and-purely-political", "Both: it operates within covenant (Israel's covenant with God) AND in purely political, non-covenantal contexts (one kingdom revolting against another's secular rule) -- this family shows the widest range of the three read so far, spanning theological covenant-breach to secular political insurrection under the very same lexeme.",
            strong="H5674D/H6586", occurrences=occs("H6586",["1Kgs.12.19"]))
    ])

add("T4.5.3","T4","T4.5","Human Interface — Boundaries",
    "What does the evidence show about the relational scope of the characteristic — who is included and who is not?",
    "Characteristic relational",
    [
      slant("individuals-nations-and-the-cosmos-itself", "Included: individuals (Jacob/Laban), nations against nations (the Amos formula's seven-plus-two peoples), Israel against God (the majority prophetic register), and even the cosmos as a limiting case that could in principle transgress but does not (the sea, Prov 8:29). Excluded: God himself (T0.1.2a).", strong=None)
    ])

add("T4.6.1","T4","T4.6","Spiritual Beings Interface",
    "In this verse, does the characteristic operate in relation to other spiritual beings — angelic or adversarial — and if so how? Record none if it does not.",
    "Word/term (lexical)",
    [
      slant("angels-mediate-the-law", "Yes, positively for angels: 'the message declared by angels' (Heb 2:2) stands behind the law whose transgression is then punished -- angels are the channel through which the very standard transgression violates was given.",
            strong="G3847", occurrences=occs("G3847",["Heb.2.2"])),
      slant("no-adversarial-case", "No occurrence names an adversarial being as a transgressor or as inducing transgression.", strong=None)
    ])

add("T4.6.2a","T4","T4.6","Spiritual Beings Interface",
    "Does an adversarial-being code ever appear as an acting party in a verse carrying this characteristic?",
    "Word/term (lexical)",
    [slant("no", "No -- none found across this family's 118 occurrences.", strong=None)])

add("T4.6.2b","T4","T4.6","Spiritual Beings Interface",
    "What does that pattern show about the characteristic being a site of adversarial activity?",
    "Other non-human beings",
    [slant("not-a-site-of-adversarial-activity", "Transgression, like guilt and unlike sin, shows no confirmed adversarial-activity pattern in this cluster's own textual evidence -- a genuine point of alignment with H_guilt against B_sin's positive finding.", strong=None)])

add("T4.6.3a","T4","T4.6","Spiritual Beings Interface",
    "Does an angelic-being code ever appear as an acting party in a verse carrying this characteristic?",
    "Word/term (lexical)",
    [slant("yes-mediating-role", "Yes -- angels are the acting party who declared the law (Heb 2:2), though in a mediating/instrumental role, not as transgressors themselves.",
           strong="G3847", occurrences=occs("G3847",["Heb.2.2"]))])

add("T4.6.3b","T4","T4.6","Spiritual Beings Interface",
    "What does that pattern show about the characteristic being communicated, strengthened, or mediated through angelic ministry?",
    "Other non-human beings",
    [slant("angelic-mediation-of-the-standard-itself", "This is the clearest positive angelic-mediation finding across the three families read so far: the STANDARD whose transgression carries penalty was itself given through angelic ministry -- angels are constitutive of the boundary's authority, a distinct and more foundational role than any 'strengthening' or 'communicating' of the characteristic to a person.",
           strong="G3847", occurrences=occs("G3847",["Heb.2.2"]))],
    cross_flags=[{"statement":"This is the only confirmed positive angelic-involvement case (as opposed to adversarial) found across H_guilt (negative), B_sin (adversarial positive, angelic positive only via fallen angels), and G_transgression (angelic positive, in a mediating/authority-granting role distinct from B_sin's fallen-angel case) -- a genuinely distinct third pattern worth holding separately in any synthesis.","related_family":"B_sin","related_cluster":None}])

# ================= T5 =================

add("T5.1.1","T5","T5.1","Nature of Transformation",
    "In this verse, does the characteristic produce transformation in the person, and if so does it change the person's condition, their orientation to their condition, or both? Record none if no transformation is shown.",
    "Verse-context",
    [
      slant("condition-change-via-retribution", "Produces a condition change via automatic retribution (Heb 2:2) -- the person's condition changes (penalty incurred) independent of any change in their orientation.",
            strong="G3847", occurrences=occs("G3847",["Heb.2.2"])),
      slant("orientation-change-via-confession", "The recognition-group occurrences (Ps 51, Job 7:21) produce an orientation change -- turning to plead for removal -- without the verse itself narrating the underlying record's actual erasure.",
            strong="H6588", occurrences=occs("H6588",["Ps.51.1"]))
    ])

add("T5.1.2","T5","T5.1","Nature of Transformation",
    "Is the transformation reversible or irreversible in the evidence?",
    "Characteristic (HIB behaviour)",
    [
      slant("reversible-via-mercy", "Reversible via God's mercy -- 'blots out,' 'passes over' -- stated as a genuine erasure, not a mere covering-over.",
            strong="H6588", occurrences=occs("H6588",["Isa.44.22"])),
      slant("irreversible-in-retribution-case", "Irreversible where automatic retribution is described (Heb 2:2) -- no remedy is named in that verse itself.",
            strong="G3847", occurrences=occs("G3847",["Heb.2.2"]))
    ])

add("T5.2.1","T5","T5.2","Sequence of Inner States",
    "Does this verse describe a sequence of inner states the characteristic moves the person through — a before, during, and after — and what are those states? Record none if no sequence is shown.",
    "Verse-context",
    [
      slant("recognition-accrual-remedy-again", "The same three-stage sequence already named at T1.2.2 -- committed-and-accruing (before/during) -> recognized/confessed (turning point) -> forgiven/blotted out (after) -- this family's clearest and most explicitly self-named sequence of any read so far.",
            strong="H6588", occurrences=occs("H6588",["Ps.51.3","Mic.7.18"]))
    ])

add("T5.3.1","T5","T5.3","Mechanism of Change",
    "In this verse, by what mechanism does the characteristic produce change — discipline, encounter, gradual formation, sudden transformation, or other? Record none if no mechanism is shown.",
    "Verse-context",
    [
      slant("mercy-based-declarative-mechanism", "A declarative act of divine mercy (blotting out, passing over) is the mechanism -- sudden and unilateral, resembling B_sin's declarative-forgiveness mechanism more than H_guilt's ritual-procedural one.",
            strong="H6588", occurrences=occs("H6588",["Mic.7.18"])),
      slant("automatic-retribution-mechanism", "Automatic retribution (Heb 2:2) is a distinct, disciplinary mechanism with no described process at all -- consequence simply follows.",
            strong="G3847", occurrences=occs("G3847",["Heb.2.2"]))
    ])

add("T5.3.2","T5","T5.3","Mechanism of Change",
    "Does the mechanism differ across contexts in the evidence; if so, how?",
    "Characteristic (HIB behaviour)",
    [
      slant("two-mechanisms-mercy-vs-automatic", "Yes -- mercy-based declarative removal and automatic retribution are the two poles, with the choice between them turning on whether the party is described as pleading/recognized or simply named as an offender under the law's operation.", strong=None)
    ])

add("T5.4.1","T5","T5.4","Suffering and Affliction",
    "In this verse, does the characteristic operate in relation to suffering or affliction — as a response to it, a product of it, or a context for it? Record none if no such relation is shown.",
    "Verse-context",
    [
      slant("transgression-as-cause-of-affliction", "Transgression is named as the direct CAUSE of national affliction -- 'the Lord has afflicted her for the multitude of her transgressions' (Lam 1:5).",
            strong="H6588", occurrences=occs("H6588",["Lam.1.5"]))
    ])

add("T5.4.2","T5","T5.4","Suffering and Affliction",
    "What does the evidence show suffering doing to the characteristic in the person — and record no such effect if none is shown.",
    "Characteristic (HIB behaviour)",
    [
      slant("no-effect-shown-suffering-is-consequence-not-remedy", "No occurrence shows suffering reducing or discharging transgression the way H_guilt's punishment-bearing did -- here suffering is transgression's CONSEQUENCE, not its resolution mechanism (resolution belongs to mercy/forgiveness instead, per T5.3.1).", strong=None)
    ])

add("T5.5.1","T5","T5.5","Formation and Sanctification",
    "In this verse, does the characteristic participate in the longer arc of character formation and sanctification — shaping the person over time — and what does the evidence show of its role in that arc? Record none if no such participation is shown.",
    "Verse-context",
    [
      slant("negative-formation-only-again", "As with H_guilt and B_sin, only a negative-formation arc is shown -- transgression accumulates (T1.6.1) rather than forms virtue; no occurrence gives it a positive sanctifying role.", strong=None)
    ])

add("T5.6.1","T5","T5.6","Eschatological Trajectory",
    "In this verse, is the characteristic oriented toward an eschatological fullness — a future state toward which its present operation points — and what does its present experience anticipate of that fullness? Record none if no such orientation is shown.",
    "Verse-context",
    [
      slant("zion-redemption-trajectory", "Isa 59:20's turning-from-transgression at Zion's redemption is an explicit eschatological trajectory, and Isa 53:5's christological convergence-verse reinforces it.",
            strong="H6588", occurrences=occs("H6588",["Isa.59.20","Isa.53.5"])),
      slant("no-orientation-elsewhere", "Most occurrences show no eschatological orientation.", strong=None)
    ])

assert len(answers) == 64, f"expected 64 questions answered, got {len(answers)}"

out = {
  "cluster_code": "M10",
  "family_id": "G_transgression",
  "process": "1682-cluster-reading-process-d",
  "spec_round": 1,
  "catalogue_scope": "T0-T5",
  "questions_answered": len(answers),
  "answers": answers
}

with open('_analytics/Clusters/1682-test-m10-process-d-G_transgression-v1-20260911.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("written, questions:", len(answers))
total_slants = sum(len(a['slants']) for a in answers)
print("total slants:", total_slants)
total_adjacent_flags = sum(len(a['needs_adjacent_verse_context']) for a in answers)
print("adjacent-context flags:", total_adjacent_flags)
total_cross_flags = sum(len(a['cross_family_or_cluster_flags']) for a in answers)
print("cross-family/cluster flags:", total_cross_flags)
