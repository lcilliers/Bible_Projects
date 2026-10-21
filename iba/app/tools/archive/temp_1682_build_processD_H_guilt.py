# -*- coding: utf-8 -*-
import json

with open('_analytics/Clusters/1682-test-m10-process-c-H_guilt-v2-20260911.json', encoding='utf-8') as f:
    fam = json.load(f)

with open('_analytics/Clusters/1682-test-m10-process-a-input-v1-20260911.json', encoding='utf-8') as f:
    proc_a = json.load(f)
by_strong = {s['strong']: s for s in proc_a['strongs']}
verse_text_lookup = {}
for st in fam['strongs_in_family']:
    for o in by_strong[st]['occurrences']:
        verse_text_lookup[o['osisId']] = o['verse_text']

def occ(strong, verse, surface=None, morph=None):
    """Build one {verse, span_surface, span_morph, verse_text} evidence entry.
    If surface/morph omitted, look up the first matching occurrence for that verse+strong."""
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
      slant("guilt-against-God", "God (the LORD) is the direct object/wronged party of the guilt named: 'full of guilt against the Holy One of Israel' (Jer 51:5) and 'breaking faith with the LORD' as the stated ground of guilt (Num 5:6). God is the one wronged, not the one bearing or giving guilt.",
            strong="H0817/H0816", occurrences=occs("H0817",["Jer.51.5"])+occs("H0816",["Num.5.6"]),
            observation_refs=["H0817 instance-meaning: 'full of guilt against the Holy One'","H0816 cross-family: Num.5.6 breaking faith"]),
      slant("guilt-remedy-before-God", "God is the recipient/judge before whom the guilt-offering and guilt-bearing remedy is enacted -- Aaron bears guilt 'before the LORD' as standing priestly office, and the Servant's soul becomes a guilt offering to God. God is the one to whom the remedy is directed, not the guilty party.",
            strong="H5375J/H0817", occurrences=occs("H5375J",["Exod.28.38","Exod.28.43"])+occs("H0817",["Isa.53.10"])+occs("H5375J",["Isa.53.12"]),
            observation_refs=["H5375J instance-meaning: institutional priestly bearing","H0817 instance-meaning: Servant Song pivot"]),
      slant("guilt-against-Christ", "1Cor 11:27's cultic-propriety register makes Christ ('the Lord') the direct object of the offense -- guilty concerning his body and blood.",
            strong="G1777", occurrences=occs("G1777",["1Cor.11.27"]),
            observation_refs=["G1777 instance-meaning: sacramental impropriety"]),
      slant("not-related-to-God", "The great majority of this family's occurrences state no God-relation at all in the verse itself: enochos's civil/criminal register (Matt 5:21-22, 26:66, Mark 3:29, Jas 2:10, Heb 2:15), and asham's procedural/national/individual register (2Chr 19:10, Judg 21:22, Ps 34:21-22, Ezek 25:12, Hab 1:11, Zech 11:5, and nasa's punishment-bearing occurrences). Guilt is predicated purely of human relations in these verses.",
            strong=None)
    ])

add("T0.1.2a","T0","T0.1","Divine Nature Reflected",
    "Across the characteristic's verses, is the characteristic ever predicated of God himself (not just present in a verse where God is also mentioned)?",
    "Other non-human beings",
    [
      slant("firm-negative", "No -- across all 75 occurrences, God is never said to BE guilty, liable, or to bear guilt as his own fault. Where God appears he is consistently the wronged party, the judge, or the recipient of a remedy -- never the guilty party.", strong=None),
      slant("substitutionary-exception-noted", "The one occurrence that comes closest -- the Servant 'bearing' others' sin/guilt (Isa 53:12, H5375J) -- is typologically read as Christ, but the text itself frames this as a CHOSEN act of bearing OTHERS' guilt, not God's own guilt. This is the exception that confirms the rule rather than contradicting it: guilt is never intrinsic to the divine nature even in the one verse where a divine figure is most closely associated with it.",
            strong="H5375J", occurrences=occs("H5375J",["Isa.53.12"]),
            observation_refs=["H5375J instance-meaning: nasa applied to the Servant"])
    ])

add("T0.1.2b","T0","T0.1","Divine Nature Reflected",
    "What does the pattern of presence/absence found in T0.1.2a indicate for the characteristic's place in the human person and in the divine image?",
    "Other non-human beings",
    [
      slant("guilt-is-creaturely-not-divine", "Guilt is a specifically human/creaturely condition, definitionally excluded from God's own nature in this vocabulary. This indicates guilt marks a real, non-shared property of the fallen human condition -- not an aspect of the divine image itself, but a departure from it (see T0.3 below).", strong=None)
    ])

add("T0.2.1","T0","T0.2","Created Purpose",
    "Does this verse state any purpose, role, or effect the characteristic serves in the person — what it leads the person to be, do, or become? Record it if stated; otherwise record none.",
    "Verse-context",
    [
      slant("triggers-remedy", "Recognition of guilt is the stated hinge that leads a person to bring the guilt-offering -- the 'realizes his guilt' formula recurs nine times as the trigger-point for the remedy procedure.",
            strong="H0816", occurrences=occs("H0816",["Lev.4.13","Lev.5.4"]),
            observation_refs=["H0816 verse-grouping: the realizes-his-guilt formula"]),
      slant("produces-bondage", "Guilt/liability leads to lifelong slavery to fear of death (Heb 2:15) -- an effect on the person's whole life orientation, not a single act.",
            strong="G1777", occurrences=occs("G1777",["Heb.2.15"]),
            observation_refs=["G1777 instance-meaning: literal held/bound sense"]),
      slant("leads-to-restitution", "Guiltiness leads to a dated moment of realization followed by restitution being supplied (the post-exilic mixed-marriage crisis's guilt-offering supply).",
            strong="H0819", occurrences=occs("H0819",["Lev.6.5","Ezra.10.19"]),
            observation_refs=["H0819 instance-meaning: paired with iniquity, restitution timing"]),
      slant("no-stated-effect", "Most occurrences (2Chr 19:10, Judg 21:22, Ps 34:21-22, Ezek 25:12, Hab 1:11) simply pronounce or describe guilt with no further stated inner effect in that verse.", strong=None)
    ])

add("T0.2.2","T0","T0.2","Created Purpose",
    "Across the evidence, does the characteristic's role read as belonging to created design, to the fallen condition, to both, or as not determinable?",
    "Other non-human beings",
    [
      slant("fallen-condition", "Guilt itself reads uniformly as belonging to the FALLEN condition -- every occurrence presupposes an already-committed offense (an act, a broken command, a betrayal) as its precondition. There is no occurrence where guilt is a neutral or designed capacity.", strong=None),
      slant("remedy-system-is-provision", "The guilt-OFFERING and guilt-BEARING systems (H0817/H0819/H5375J) are God-given remedies FOR the fallen condition -- their existence answers to the fall, giving this family a 'provision' character distinct from the guilt-state itself, worth distinguishing from the guilt-condition proper.",
            strong="H0817/H5375J", occurrences=[],
            observation_refs=["H0817/H5375J procedural and substitutionary observations"])
    ])

add("T0.2.3","T0","T0.2","Created Purpose",
    "Across the evidence, is there any orientation toward a future fullness — something the person moves toward, not only what they currently are? Record it, or record none.",
    "Other non-human beings",
    [
      slant("servant-song-forward-orientation", "The Servant Song material (Isa 53:10, H0817; Isa 53:12, H5375J) is explicitly forward-oriented: the guilt-offering/bearing achieves a future state ('he shall see his offspring,' many 'made righteous') that the present act only inaugurates.",
            strong="H0817/H5375J", occurrences=occs("H0817",["Isa.53.10"])+occs("H5375J",["Isa.53.12"]),
            observation_refs=["H0817 instance-meaning: Servant Song pivot","H5375J instance-meaning: nasa applied to the Servant"]),
      slant("no-future-orientation-elsewhere", "Elsewhere, no future-fullness orientation is stated; the guilt vocabulary is bound to the immediate past act and its immediate remedy/consequence.", strong=None)
    ])

add("T0.3.1","T0","T0.3","Image-Bearer Expression",
    "From the characteristic's God-relation (T0.1) and its role (T0.2), what aspect of the divine likeness, if any, does it instantiate in the person? Record the aspect, or record none.",
    "Other non-human beings",
    [
      slant("guilt-itself-instantiates-none", "Given T0.1.2a's finding (guilt never predicated of God), guilt itself instantiates NO aspect of divine likeness -- it is precisely the human departure from likeness, a broken relation to God's law/character.", strong=None),
      slant("bearing-for-another-echoes-self-giving", "The guilt-BEARING vocabulary (H5375J), read typologically through the Servant, echoes a divine character trait -- self-sacrificial bearing on behalf of another -- even though guilt as a status does not.",
            strong="H5375J", occurrences=occs("H5375J",["Isa.53.12"]),
            observation_refs=["H5375J instance-meaning: nasa applied to the Servant"])
    ])

add("T0.3.2","T0","T0.3","Image-Bearer Expression",
    "Across the evidence, is the characteristic shared between God and the person, or an exclusively creaturely analogue to something in God?",
    "Other non-human beings",
    [
      slant("exclusively-creaturely", "Guilt (the state) is exclusively creaturely, never shared with God (see T0.1.2a). Guilt-bearing (H5375J's act of carrying another's guilt) has only a partial divine analogue via the Servant/Christ identification -- the text's own human referents (priests, husband, community) bear guilt as creatures acting within a God-instituted system, not as something God himself possesses.", strong=None)
    ])

add("T0.3.3","T0","T0.3","Image-Bearer Expression",
    "Where the characteristic is present or absent in a person, what does that indicate about the condition of the divine image in them — or is no such indication evidenced?",
    "Other non-human beings",
    [
      slant("presence-indicates-damaged-but-functioning-image", "Where guilt is present (the overwhelming majority), it indicates a moral-relational faculty that is FUNCTIONING (capable of recognizing violation -- the 'realizes his guilt' formula presupposes a working conscience) but in a state of violation, not a non-functioning image.",
            strong="H0816", occurrences=occs("H0816",["Lev.4.13"]),
            observation_refs=["H0816 verse-grouping: realizes-his-guilt formula"]),
      slant("absence-case", "Ps 34:21-22's pairing is this family's clearest positive-absence case: 'those who take refuge in him will not be condemned,' implying the image's relational function restored to a non-guilty state through refuge in God rather than self-effort.",
            strong="H0816", occurrences=occs("H0816",["Ps.34.21","Ps.34.22"]),
            observation_refs=["H0816 alternative-meaning: condemned/not-condemned pairing"])
    ])

add("T0.4.1","T0","T0.4","Typological Significance",
    "Does this verse use the characteristic typologically — pointing beyond the immediate to a covenantal, eschatological, or christological reality; if so, which, and in which direction (the divine instance establishing the pattern, or the human pointing toward the divine)? Record the use and direction, or record none.",
    "Verse-context",
    [
      slant("servant-song-christological", "Isa 53:10 (H0817) and 53:12 (H5375J) are explicitly christological -- direction: the human/Servant figure's guilt-offering and guilt-bearing point forward, later read as fulfilled in Christ's atoning work.",
            strong="H0817/H5375J", occurrences=occs("H0817",["Isa.53.10"])+occs("H5375J",["Isa.53.12"]),
            observation_refs=["cross-family: Isaiah 53 convergence"],
            ),
      slant("scapegoat-typological-institution", "Lev 16:22's scapegoat ritual (H5375J) is typological in the classic sense -- a divinely-instituted OT pattern, direction: the divine institution establishing the pattern, later read as fulfilled.",
            strong="H5375J", occurrences=occs("H5375J",["Lev.16.22"]),
            observation_refs=["H5375J instance-meaning: substitutionary transfer"]),
      slant("no-typology-elsewhere", "The vast majority of occurrences show no typological signal in the verse itself -- straightforward legal/narrative/procedural statements.", strong=None)
    ],
    cross_flags=[{"statement":"Isaiah 53 is cited independently by H_guilt (v.10, v.12) and by family G_transgression/D_crime_injustice's own citations of v.5 -- a convergence point across at least three families, not resolved here.","related_family":"G_transgression","related_cluster":None}])

# ================= T1 =================

add("T1.1.1","T1","T1.1","Name and Naming",
    "What is the characteristic called in the programme, and what does the name signal about its essential nature?",
    "Word/term (lexical)",
    [
      slant("guilt-is-consequent-status", "Called 'Guilt' (H_guilt, M10). The name signals a STATUS/CONDITION resulting from wrongdoing -- the state of being answerable for an offense -- rather than the act of wrongdoing itself (sin, family B) or the act of crossing a boundary (transgression, family G). Guilt sits downstream of both, as the consequent liability.", strong=None)
    ])

add("T1.1.2","T1","T1.1","Name and Naming",
    "What do the primary Hebrew and Greek terms show at the definitional level?",
    "Word/term (lexical)",
    [
      slant("asham-unstable-core", "asham (H0816/H0817/H0819) is primarily 'be/become guilty,' but has a documented, live secondary sense 'be desolate/suffer' (Ezek 6:6, Joel 1:18) -- the Hebrew term's own definitional core is not perfectly stable.",
            strong="H0816", occurrences=occs("H0816",["Ezek.6.6","Joel.1.18"]),
            observation_refs=["H0816 alternative-meaning x2: desolate/suffer sense"]),
      slant("enochos-derivative", "enochos (G1777) literally means 'held in/bound by,' specialized here to forensic liability -- guilt as a state of being GRIPPED, not a primitive 'guilt' root.",
            strong="G1777", occurrences=[],
            observation_refs=["G1777 difference-inference: one root image, three registers"]),
      slant("nasa-not-a-guilt-word-at-root", "nasa (H5375J) is not a guilt-word at the root at all -- 'to lift/carry/bear' -- only guilt-marked by its grammatical object ('bear HIS INIQUITY'). The guilt-sense is entirely borrowed from context.", strong="H5375J", occurrences=[]),
      slant("vazar-unattested", "vazar (H2054) has zero occurrences; meaning-block only ('guilty, burdened with guilt, strange') -- no live definitional evidence.", strong="H2054", occurrences=[],
            observation_refs=["H2054 no-human-context"])
    ])

add("T1.1.3","T1","T1.1","Name and Naming",
    "What directional, relational, or constitutional implication does the name carry?",
    "Word/term (lexical)",
    [
      slant("held-bound-external", "enochos's 'held/bound' implies something EXTERNAL holds the person (a law, a verdict, a fear) -- guilt as being gripped from outside.", strong="G1777"),
      slant("bear-lift-weight", "nasa's 'bear/lift' implies a WEIGHT carried BY the person, with the possibility of the load moving to another carrier (scapegoat, Servant).", strong="H5375J"),
      slant("become-entered-into", "asham Qal's 'become' implies a state ENTERED INTO by the person's own act -- guilt as something one falls into, not merely imposed.", strong="H0816"),
      slant("no-constitutional-level-in-name", "None of these terms code a specific constitutional level (spirit/soul/heart/mind) into the name itself; that is addressed separately under T2.", strong=None)
    ])

add("T1.2.1","T1","T1.2","Kind",
    "What kind of inner-being phenomenon is the characteristic — an act, a disposition, a condition/status, a quality, or something else?",
    "Characteristic (HIB behaviour)",
    [
      slant("condition-status-dominant", "CONDITION/STATUS is the dominant pattern across all 7 strongs: enochos = liable status, asham = guilty status, ashmah = abstract quality-noun of guiltiness, nasa's 'bear guilt' = the state of carrying a status.", strong=None),
      slant("act-at-origin", "Guilt also names the ACT that produces the status: Ezek 22:4's 'become guilty' names the act-to-status transition explicitly (bloodshed and idolatry producing the guilty condition) in one verse.",
            strong="H0816", occurrences=occs("H0816",["Ezek.22.4"]),
            observation_refs=["H0816 instance-meaning: becoming-guilty paired with defiled"]),
      slant("not-a-disposition", "Guilt is never a standing personality trait in this family -- even Hab 1:11's 'guilty men' describes a settled STATE of a class, not a character disposition.",
            strong="H0816", occurrences=occs("H0816",["Hab.1.11"]))
    ])

add("T1.2.2","T1","T1.2","Kind",
    "Is the characteristic simple in structure, or does it combine constituent elements; if compound, which?",
    "Characteristic (HIB behaviour)",
    [
      slant("simple-at-root", "Mostly simple at the lexical root -- a single status-word.", strong=None),
      slant("compound-formulas", "Several key formulas compound guilt with a second element: H0816's 'realizes his guilt' compounds perception/recognition WITH guilt-status (the status only becomes actionable once recognized); H5375J's causative Hiphil (Lev 22:16) compounds guilt-status with a second party's culpable negligence.",
            strong="H0816/H5375J", occurrences=occs("H0816",["Lev.4.13"])+occs("H5375J",["Lev.22.16"]),
            observation_refs=["H0816 verse-grouping: realizes-his-guilt formula","H5375J instance-meaning: Hiphil causative bearing"])
    ])

add("T1.3.1","T1","T1.3","Boundary",
    "What stands against the characteristic as its structural opposite — the inner-being reality that excludes it?",
    "Characteristic (HIB behaviour)",
    [
      slant("refuge-in-God", "Innocence via refuge in God is this family's own clearest structural-opposite pair: 'the wicked are condemned... but those who take refuge in the LORD will not be condemned' (Ps 34:21-22).",
            strong="H0816", occurrences=occs("H0816",["Ps.34.21","Ps.34.22"]),
            observation_refs=["H0816 alternative-meaning: condemned/not-condemned pairing"])
    ])

add("T1.3.2","T1","T1.3","Boundary",
    "What does the characteristic exclude or resist at its edge?",
    "Characteristic (HIB behaviour)",
    [
      slant("consequence-can-be-withheld", "Guilt's normal consequence (punishment) can be withheld even from the apparently culpable -- Zech 11:5's profiteers 'go unpunished' -- showing the boundary between guilt and its consequence is not automatic, and the text frames the withholding itself as a wrong needing correction.",
            strong="H0816", occurrences=occs("H0816",["Zech.11.5"]),
            observation_refs=["H0816 instance-meaning: negated ironic sense"])
    ],
    needs_adjacent=[{"verse":"Zech.11.5","why":"the shepherd-allegory chapter's surrounding verses are needed to identify who 'those who buy them' and 'their own shepherds' are, to fully ground the ironic unpunished-profiteers reading."}])

add("T1.3.3","T1","T1.3","Boundary",
    "Where does the characteristic end and another thing begin — what is it not?",
    "Characteristic (HIB behaviour)",
    [
      slant("guilt-vs-desolation", "The same word (asham) crosses from moral guilt into non-moral desolation/suffering (Ezek 6:6, Joel 1:18) -- the boundary between the two senses is not carried by the word alone, only by its object/context (altars/idols/sheep vs. a person).",
            strong="H0816", occurrences=occs("H0816",["Ezek.6.6","Joel.1.18"])),
      slant("guilt-vs-sin", "The boundary between this family's guilt-vocabulary and family B's sin-vocabulary (chattah) is not maintained in the English surface even where the underlying Hebrew keeps two distinct roots -- asham renders as 'sin' at Lev 5:7.",
            strong="H0817", occurrences=occs("H0817",["Lev.5.7"]),
            observation_refs=["H0817 surface-gloss-divergence: sin/guilt-offering overlap"])
    ],
    cross_flags=[{"statement":"Guilt-offering vocabulary (H0817/H0819) sits beside and is translated interchangeably with family B's sin-offering vocabulary at Lev 5:7 -- whether the two offering-systems should be read together is unresolved.","related_family":"B_sin","related_cluster":None}])

add("T1.4.1a","T1","T1.4","Modes of Operation",
    "What is the grammatical/stem form of the characteristic's primary term in this verse?",
    "Word/term (lexical)",
    [
      slant("hebrew-stems", "Qal (H0816 majority -- active/simple 'become guilty'); Niphal (H0816 Ezek 6:6/Joel 1:18 -- passive 'be made desolate/suffer'); Hiphil (H0816 Ps 5:10 imperative causative 'bear guilt', H5375J Lev 22:16 causative 'cause to bear'); Qal participle used substantively (H5375J Prov 19:19 'pay').", strong="H0816/H5375J"),
      slant("greek-forms", "Adjective throughout for enochos (A-NSM/A-NPM); noun forms for asham/ashmah (HNcmsa/HNcfsa).", strong="G1777")
    ])

add("T1.4.1b","T1","T1.4","Modes of Operation",
    "In what distinct mode(s) does the characteristic operate within the inner person in this verse — the manner of its functioning?",
    "Verse-context",
    [
      slant("recognition-triggered", "H0816's Lev 4-6 formula: guilt operates by being RECOGNIZED -- recognition is itself the operative moment before which the offering procedure cannot begin.",
            strong="H0816", occurrences=occs("H0816",["Lev.4.13"])),
      slant("imputed-pronounced", "H0816's Judg 21:22, Ps 34:21-22, Hab 1:11: guilt operates as a verdict PRONOUNCED on a person/class, with no recognition-step described.",
            strong="H0816", occurrences=occs("H0816",["Judg.21.22","Hab.1.11"])),
      slant("borne-carried", "H5375J throughout: guilt operates as WEIGHT, something carried (by the guilty party, a priest, an animal, or the Servant) rather than merely declared.", strong="H5375J"),
      slant("held-bound", "G1777: guilt operates as a BINDING/HOLDING relation between a person and a penalty or practice.", strong="G1777")
    ])

add("T1.4.2","T1","T1.4","Modes of Operation",
    "Does the mode of operation vary by context, direction, or constitutional level; if so, how?",
    "Characteristic (HIB behaviour)",
    [
      slant("varies-by-strong-not-level", "Yes, strongly -- the mode of operation tracks WHICH TERM/STRONG is used (recognition for asham's legal-formula use, pronouncement for its declarative use, bearing for nasa, binding for enochos) rather than a single term flexing across constitutional levels. H_guilt is genuinely different modes attached to different roots, not one mode wearing different words.", strong=None)
    ])

add("T1.4.3","T1","T1.4","Modes of Operation",
    "Does the characteristic operate through a communicative or speech-based mode (commanded, addressed, spoken); if so, how? Record it, or record none.",
    "Characteristic (HIB behaviour)",
    [
      slant("codified-law-speech", "H0816's Lev 4-6 formula is codified/commanded speech -- Torah legislation.", strong="H0816", occurrences=occs("H0816",["Lev.4.13"])),
      slant("quoted-self-justification", "Jer 50:7's 'we are not guilty' is spoken self-justification, directly quoted.", strong="H0816", occurrences=occs("H0816",["Jer.50.7"])),
      slant("prophetic-indictment", "Zech 11:5's 'go unpunished' is spoken as prophetic indictment.", strong="H0816", occurrences=occs("H0816",["Zech.11.5"])),
      slant("mostly-not-communicative", "Most occurrences are narrated/legal-code register rather than reported speech.", strong=None)
    ])

add("T1.5.1","T1","T1.5","Immediate Response",
    "What first or most immediate inner-being response does this verse show following the characteristic? Record it, or record none.",
    "Verse-context",
    [
      slant("recognition-to-offering", "Recognition leads immediately to bringing the prescribed offering (H0816 Lev 4-6; H0819 Lev 6:5).",
            strong="H0816/H0819", occurrences=occs("H0816",["Lev.4.13"])+occs("H0819",["Lev.6.5"])),
      slant("fear-bondage", "Fear of death, described as lifelong (G1777 Heb 2:15).", strong="G1777", occurrences=occs("G1777",["Heb.2.15"])),
      slant("self-justifying-denial", "Denial, not acknowledgment (H0816 Jer 50:7).", strong="H0816", occurrences=occs("H0816",["Jer.50.7"])),
      slant("spontaneous-relational-confession", "Spontaneous, unprompted confession among brothers, entirely relational, with no ritual/legal trigger at all (H0818 Gen 42:21).", strong="H0818", occurrences=occs("H0818",["Gen.42.21"])),
      slant("no-response-stated", "Most occurrences state no immediate response -- a legal pronouncement or narrative note with no follow-on reaction recorded.", strong=None)
    ])

add("T1.5.2","T1","T1.5","Immediate Response",
    "Across the verses, is that immediate response consistent or varied?",
    "Characteristic (HIB behaviour)",
    [
      slant("stark-variation", "Varied, and starkly so: response ranges from prescribed cultic action (offering) to psychological bondage (fear) to denial to spontaneous relational confession -- no single 'the' response to guilt exists across this family's evidence.", strong=None)
    ])

add("T1.6.1","T1","T1.6","Sustained Effect",
    "What does the characteristic produce in the inner being over time in this verse — what states, qualities, capacities, or orientations does it establish? Record it, or record none.",
    "Verse-context",
    [
      slant("lifelong-bondage", "Lifelong slavery to fear of death, explicit sustained-effect language ('all their lives') (G1777 Heb 2:15).", strong="G1777", occurrences=occs("G1777",["Heb.2.15"])),
      slant("settled-trait-or-fatal-culmination", "A settled, ongoing characteristic of a class of people (Hab 1:11), or guilt culminating in death (Hos 13:1).", strong="H0816", occurrences=occs("H0816",["Hab.1.11","Hos.13.1"])),
      slant("cumulative-quantity", "Guilt as an accumulating quantity over time -- 'already great,' 'more and more' when unaddressed (2Chr 28:13, 33:23).",
            strong="H0819", occurrences=occs("H0819",["2Chr.28.13","2Chr.33.23"]),
            observation_refs=["H0819 instance-meaning: accumulating quantity"]),
      slant("no-sustained-effect-stated", "Most procedural/legal occurrences state no sustained effect -- the verse only pronounces status, not its trajectory.", strong=None)
    ],
    needs_adjacent=[{"verse":"2Chr.33.23","why":"the contrast drawn ('unlike his father Manasseh, who humbled himself') depends on 2Chr 33's fuller Manasseh narrative, not just this one verse."}])

add("T1.6.3","T1","T1.6","Sustained Effect",
    "How does the sustained effect differ from the immediate response (T1.5)?",
    "Characteristic (HIB behaviour)",
    [
      slant("actions-vs-states", "Immediate responses are ACTIONS/REACTIONS (offering, denial, fear-onset, confession); sustained effects, where recorded at all, are STATES that persist or accumulate (bondage, cumulative guilt-quantity, a settled character trait) -- guilt behaves like compound interest when unaddressed (2Chr's 'more and more') rather than a one-off event whose response happens once and is finished.", strong=None)
    ])

add("T1.7.1","T1","T1.7","Conditions of Reception",
    "Under what inner conditions does the characteristic take hold or operate rightly?",
    "Characteristic (HIB behaviour)",
    [
      slant("recognition-required", "Recognition/self-awareness is the necessary condition for guilt to operate rightly in the legal-cultic system -- the whole 'realizes his guilt' formula presupposes this before remedy can begin.",
            strong="H0816", occurrences=occs("H0816",["Lev.4.13"])),
      slant("triggered-by-memory", "For H0818 (Gen 42:21), the condition is a triggering MEMORY/reflection -- guilt 'takes hold' through recollection of a past failure, not fresh legal violation.",
            strong="H0818", occurrences=occs("H0818",["Gen.42.21"]))
    ])

add("T1.7.2","T1","T1.7","Conditions of Reception",
    "Under what inner conditions is the characteristic blocked, distorted, resisted, or not taken up — including, where the evidence shows it, distortion or interference by another spirit (adversarial or angelic)?",
    "Characteristic (HIB behaviour)",
    [
      slant("resisted-by-rationalization", "Guilt is resisted by the guilty party's own rationalization -- 'we are not guilty, for THEY have sinned,' displacing blame (Jer 50:7).",
            strong="H0816", occurrences=occs("H0816",["Jer.50.7"])),
      slant("consequence-blocked-institutionally", "Guilt's normal consequence is blocked/withheld in the text's own telling (Zech 11:5's profiteers going unpunished), though framed as a wrong needing correction, not a legitimate release.",
            strong="H0816", occurrences=occs("H0816",["Zech.11.5"])),
      slant("no-adversarial-angelic-interference-found", "No occurrence in this family names an adversarial or angelic being as the source of guilt-distortion -- record none for that specific clause (see T4.6 below, which tests this directly and confirms the same negative).", strong=None)
    ],
    needs_adjacent=[{"verse":"Jer.50.7","why":"the surrounding Babylon oracle is needed to confirm the speaker is Babylon (not Israel) voicing this self-justification."}])

add("T1.7.3","T1","T1.7","Conditions of Reception",
    "What is the inner-being state of the person in whom the characteristic is present but does not take hold?",
    "The HIB",
    [
      slant("self-justifying-blame-displacement", "Jer 50:7's speaker: guilt is present (from the narrator/prophetic framing) but does not take hold in the person's own self-understanding -- their inner state is self-justifying, blame-displacing.",
            strong="H0816", occurrences=occs("H0816",["Jer.50.7"])),
      slant("undisturbed-profiting", "Zech 11:5's profiteers: guilt does not take hold in the sense of producing any behavioral change -- their inner state, as far as evidenced, is untouched, profiting undisturbed.",
            strong="H0816", occurrences=occs("H0816",["Zech.11.5"]))
    ])

# ================= T2 =================

add("T2.1.1","T2","T2.1","Spirit-Level Location",
    "At which constitutional level(s) does this verse locate the characteristic — from {spirit, soul, heart, mind, other soul-subset, a named body part} — and how is each engaged? Record every level evidenced, or none.",
    "Verse-context",
    [
      slant("soul-named-once", "H0818 (Gen 42:21) names 'soul' explicitly -- 'we saw the distress of HIS SOUL... and did not listen' -- though this is Joseph's soul (the victim); the guilt named is the brothers' own for having ignored it.",
            strong="H0818", occurrences=occs("H0818",["Gen.42.21"])),
      slant("body-part-emblematic", "Exod 28:38 names the forehead as the location where Aaron 'bears' guilt from the holy things -- a literal body part, but as a priestly emblem/office marker, not an inner-faculty location claim.",
            strong="H5375J", occurrences=occs("H5375J",["Exod.28.38"])),
      slant("no-level-named-elsewhere", "The remaining occurrences (enochos, most of asham/ashmah, most of nasa) name NO constitutional level -- guilt is predicated of the whole person or a community, not a named inner faculty.", strong=None)
    ])

add("T2.1.2","T2","T2.1","Spirit-Level Location",
    "Across the verses, what does the pattern of engaged and absent levels indicate — the characteristic's depth and seat, the levels it never engages, and (for any body link) whether the link is emphatic, functional, expressive, indicative, or mediating?",
    "The HIB",
    [
      slant("guilt-is-relational-not-faculty-seated", "Guilt's seat, per this family's evidence, is NOT localized to a specific inner faculty -- it is a RELATIONAL/STATUS category attaching to the whole person before God/community/law, unlike characteristics with a heart- or soul-level seat. Heart, mind, and spirit are never engaged by name anywhere in this family's 75 occurrences -- a notable, checked absence.", strong=None),
      slant("body-link-is-emphatic", "The one body-link (Exod 28:38, forehead) is EMPHATIC/expressive -- a visible priestly marker displaying the office -- not functional or mediating; it doesn't mechanically process guilt through the forehead.",
            strong="H5375J", occurrences=occs("H5375J",["Exod.28.38"]))
    ],
    cross_flags=[{"statement":"H_guilt's near-total absence of heart/soul/mind vocabulary is worth comparing directly against other M10 families once their T2 answers exist -- flagged for a cross-family round, not resolved here.","related_family":None,"related_cluster":"M10"}])

add("T2.10.1","T2","T2.10","Constitutional Movement",
    "Does the characteristic move across constitutional levels (spirit→soul→body), or onto the person from an external source — including another spirit (angelic or adversarial) — or in another direction; and if so in what sequence or pattern? If no movement, record none.",
    "The HIB",
    [
      slant("substitutionary-relocation", "The substitutionary-transfer occurrences show explicit movement -- guilt/iniquity moves OFF the guilty party ONTO another carrier (an animal, the Servant) and is carried away (Lev 16:22, Isa 53:12). Guilt is depicted as relocatable between agents, not fixed to one bearer.",
            strong="H5375J", occurrences=occs("H5375J",["Lev.16.22","Isa.53.12"]),
            observation_refs=["H5375J instance-meaning: substitutionary transfer","H5375J instance-meaning: nasa applied to the Servant"]),
      slant("generational-transfer-explicitly-denied", "A different kind of movement is explicitly DENIED: Ezek 18:19-20 rules out automatic generational transfer (father's guilt to son) as a valid mechanism.",
            strong="H5375J", occurrences=occs("H5375J",["Ezek.18.19","Ezek.18.20"]),
            observation_refs=["H5375J difference-inference: Ezekiel 18's opposite-direction statement"]),
      slant("no-adversarial-angelic-origin", "No occurrence attributes guilt's origin or movement to an adversarial or angelic being -- record none for that specific option.", strong=None)
    ])

add("T2.7.1","T2","T2.7","Body — Direction",
    "Where a body link exists (from the T2.1.1 audit), in which direction does it run — soul/spirit expressing through the body, the body feeding back to the soul, or both — and what follows from that direction? If no body link, record none.",
    "The HIB",
    [
      slant("outward-only", "Exod 28:38's forehead-bearing is soul/office EXPRESSING outward through the body (the priestly role displayed on the body); no occurrence shows the reverse direction (bodily state feeding back inward).",
            strong="H5375J", occurrences=occs("H5375J",["Exod.28.38"])),
      slant("no-body-link-elsewhere", "Most occurrences have no body-link at all -- record none.", strong=None)
    ])

add("T2.9.1","T2","T2.9","Origin and Source",
    "Where does this verse say the characteristic originates — generated within the person, received from another person, bestowed by God, carried generationally, introduced by another spirit (angelic or adversarial), or not stated?",
    "Verse-context",
    [
      slant("generated-within-by-own-act", "The dominant pattern: guilt generated within, by one's own violation (H0816's Qal 'become guilty,' Ezek 22:4's bloodshed/idolatry, Judg 21:22's specific act).",
            strong="H0816", occurrences=occs("H0816",["Ezek.22.4","Judg.21.22"])),
      slant("generational-explicitly-denied", "Generational origin (received from father) is explicitly ruled out as valid by Ezek 18:19-20 -- a stated NO, not silence.",
            strong="H5375J", occurrences=occs("H5375J",["Ezek.18.19","Ezek.18.20"])),
      slant("received-via-substitution-reverse", "A carrier RECEIVES guilt that originated with others through a chosen transfer (Lev 16:22, Isa 53:12) -- the reverse of ordinary origin, a designated exception.",
            strong="H5375J", occurrences=occs("H5375J",["Lev.16.22","Isa.53.12"])),
      slant("not-god-bestowed-not-spirit-introduced", "No occurrence attributes guilt's origin to being directly bestowed by God, or introduced by another spirit (angelic/adversarial) -- record none for both.", strong=None)
    ])

add("T2.9.2","T2","T2.9","Origin and Source",
    "Across the verses, is the origin single or multiple, and does it change with context?",
    "Characteristic (HIB behaviour)",
    [
      slant("three-mutually-exclusive-origin-types", "Multiple, and mutually exclusive in a documented way: self-generated-by-one's-own-act (the norm) vs. explicitly-denied-generational-inheritance vs. voluntarily-received-via-substitution (the exception, reserved for a designated remedy) -- three distinct, non-overlapping origin-types, not one shifting continuum.", strong=None)
    ])

# ================= T4 =================

add("T4.1.1","T4","T4.1","Divine Interface — God to Human",
    "In this verse, does the characteristic operate from God toward the human person, and if so how? Record none if it does not.",
    "Word/term (lexical)",
    [
      slant("god-provides-remedy-not-guilt", "God is never the source of guilt itself (see T0.1), but IS the source of the guilt-offering law's REMEDY system (Lev 4-6) -- presented as God's own instituted provision, a God-to-human operation via a legal/covenantal channel rather than by directly imposing guilt.",
            strong="H0816/H0817", occurrences=occs("H0816",["Lev.4.13"])),
      slant("no-operation-in-most", "Most occurrences show no God-to-human operation -- record none; this is the majority pattern for this family.", strong=None)
    ])

add("T4.1.2","T4","T4.1","Divine Interface — God to Human",
    "On what basis does God extend the characteristic — conditional, unconditional, covenantal, or responsive — as the evidence shows?",
    "Other non-human beings",
    [
      slant("covenantal-conditional", "The guilt-offering provision (Lev 4-6) is covenantal AND conditional -- it applies within Israel's covenant law, conditioned on recognition ('when he realizes his guilt').",
            strong="H0816", occurrences=occs("H0816",["Lev.4.13"])),
      slant("responsive-divine-initiative", "Isa 53:10's Servant-as-guilt-offering is presented as God's own responsive/purposive act ('it was the will of the LORD to crush him') -- a different basis, divine initiative rather than conditional legal provision.",
            strong="H0817", occurrences=occs("H0817",["Isa.53.10"]))
    ])

add("T4.1.3","T4","T4.1","Divine Interface — God to Human",
    "What does God's extension of the characteristic show about his disposition toward the human person?",
    "Other non-human beings",
    [
      slant("disposition-toward-remedy", "The guilt-offering provision's mere existence shows a disposition toward REMEDY rather than only punishment -- God provides a way to resolve guilt rather than leaving it unaddressed. The Servant Song intensifies this into God himself providing/willing the ultimate remedy.",
            strong="H0817", occurrences=occs("H0817",["Isa.53.10"]))
    ])

add("T4.2.1","T4","T4.2","Divine Interface — Human to God",
    "In this verse, does the characteristic operate in the person's movement toward God — seeking, supplication, worship, covenant — and if so how? Record none if it does not.",
    "Word/term (lexical)",
    [
      slant("offering-as-movement-toward-God", "H0816's Lev 4-6 procedure IS a human-to-God movement -- bringing an offering, a covenantally-defined approach to God following recognition of guilt.",
            strong="H0816", occurrences=occs("H0816",["Lev.4.13"])),
      slant("denial-as-failed-movement", "Jer 50:7's denial ('we are not guilty') is the negative case -- guilt-recognition explicitly FAILING to produce any movement toward God, self-justification instead.",
            strong="H0816", occurrences=occs("H0816",["Jer.50.7"])),
      slant("no-movement-elsewhere", "Most narrative/pronouncement occurrences show no human-to-God movement -- record none.", strong=None)
    ])

add("T4.2.2","T4","T4.2","Divine Interface — Human to God",
    "What inner posture does this movement require, as the evidence shows?",
    "Other non-human beings",
    [
      slant("recognition-required", "Recognition/acknowledgment ('realizes his guilt') is the required posture across H0816/H0819's cultic-law occurrences -- movement toward God cannot begin without it.", strong="H0816/H0819"),
      slant("trust-dependence-alternative", "Ps 34's 'taking refuge in the LORD' implies a posture of trust/dependence as the alternative-track posture to the offering-based path.",
            strong="H0816", occurrences=occs("H0816",["Ps.34.22"]))
    ])

add("T4.2.3","T4","T4.2","Divine Interface — Human to God",
    "What does the human-to-God direction of the characteristic show about the person's relationship with God?",
    "Other non-human beings",
    [
      slant("legally-mediated-relationship", "The relationship is legally/covenantally MEDIATED -- guilt is resolved through a prescribed procedure (offering), not unstructured personal appeal, in the majority of this family's occurrences. This contrasts with families built more directly around confession/petition language.", strong=None)
    ])

add("T4.3.1","T4","T4.3","Human Interface — Giving",
    "In this verse, is the characteristic extended by one person toward another, and if so how does it operate in that extension? Record none if it is not.",
    "Word/term (lexical)",
    [
      slant("causative-negligence", "A priest/authority figure CAUSES another to bear guilt through negligent oversight (Lev 22:16, Hiphil) -- a person-to-person extension, but culpable/negative, not a positive giving.",
            strong="H5375J", occurrences=occs("H5375J",["Lev.22.16"])),
      slant("absorption-through-silence", "A husband's procedural silence causes him to bear his wife's guilt (Num 30:15) -- here the guilt moves TOWARD the 'giver' rather than away from him.",
            strong="H5375J", occurrences=occs("H5375J",["Num.30.15"])),
      slant("no-positive-giving-case", "No occurrence shows one person positively 'extending' (offering, granting) guilt to another in a constructive sense -- every person-to-person case in this family is culpable causation or absorption, not a gift.", strong=None)
    ],
    needs_adjacent=[{"verse":"Num.30.15","why":"the vow-law chapter's fuller context is needed to establish the precise husband/wife procedural dynamic (silence at the time of hearing, then later invalidation)."}])

add("T4.3.2","T4","T4.3","Human Interface — Giving",
    "What inner conditions or orientations in the giver accompany genuine extension of the characteristic?",
    "Characteristic relational",
    [
      slant("not-applicable-no-positive-case", "No positive-extension case is evidenced in this family (see T4.3.1). The closest analogue -- negligent oversight (Lev 22:16) -- is characterized by inattention/permissiveness, not a virtuous inner condition.",
            strong="H5375J", occurrences=occs("H5375J",["Lev.22.16"]))
    ])

add("T4.3.3","T4","T4.3","Human Interface — Giving",
    "What does the evidence show a person must have received or become before they extend the characteristic?",
    "Characteristic relational",
    [
      slant("prior-authority-or-prior-silence", "Not evidenced for a positive case. For the negative cases: the figure in Lev 22:16 must first hold a position of authority/oversight that they then fail to exercise; the husband in Num 30:15 must first have failed to speak up at the proper time.",
            strong="H5375J", occurrences=occs("H5375J",["Lev.22.16","Num.30.15"]))
    ])

add("T4.4.1","T4","T4.4","Human Interface — Receiving",
    "In this verse, is the characteristic taken up by a person from another, and if so how does it operate in that uptake? Record none if it is not.",
    "Word/term (lexical)",
    [
      slant("receiving-through-passivity", "Num 30:15 -- the husband RECEIVES/takes on his wife's guilt as a consequence of his own prior silence.", strong="H5375J", occurrences=occs("H5375J",["Num.30.15"])),
      slant("receiving-through-designation", "Lev 16:22/Isa 53:12 -- the scapegoat/Servant RECEIVES the community's/many's guilt by substitutionary designation, a wholly different mechanism from passive absorption.",
            strong="H5375J", occurrences=occs("H5375J",["Lev.16.22","Isa.53.12"]))
    ])

add("T4.4.2","T4","T4.4","Human Interface — Receiving",
    "What inner conditions accompany or block uptake of the characteristic from another person?",
    "Characteristic relational",
    [
      slant("willing-vs-passive-uptake", "The scapegoat/Servant case shows willing/designated bearing (the Servant 'poured out his soul,' read typologically as voluntary); the husband's case shows uptake through passivity/failure to act at the proper time, not willingness -- two structurally opposite conditions of uptake within the same strong.",
            strong="H5375J", occurrences=occs("H5375J",["Isa.53.12","Num.30.15"]))
    ])

add("T4.4.3","T4","T4.4","Human Interface — Receiving",
    "What is the inner-being state of the person who meets the characteristic from another but does not take it up?",
    "Characteristic relational",
    [
      slant("evidentiary-gap", "Not directly evidenced in this family -- no occurrence shows a person explicitly refusing to take up guilt offered/imposed by another and describes the resulting inner state. Record none; flagged as a genuine evidentiary gap specific to this family, not a reading failure.", strong=None)
    ])

add("T4.5.1","T4","T4.5","Human Interface — Boundaries",
    "Does the evidence show the characteristic operating differently within existing relational bonds versus across relational distance or difference; if so, how?",
    "Characteristic relational",
    [
      slant("within-a-bond", "Within an established bond (household, priestly office, national covenant) -- Num 30:15 (husband/wife), Exod 28:38 (priest/nation), Num 5:6 (Israelite/the LORD) -- guilt-bearing/incurring operates within a structure with defined roles.",
            strong="H5375J/H0816", occurrences=occs("H5375J",["Num.30.15","Exod.28.38"])+occs("H0816",["Num.5.6"])),
      slant("across-hostile-distance", "Between hostile/foreign parties with no covenant bond -- Ezek 25:12 (Edom's guilt against Judah), Jer 50:7 (Babylon's self-justifying denial against Israel) -- framed as accountability to God's justice rather than to a relational structure.",
            strong="H0816", occurrences=occs("H0816",["Ezek.25.12","Jer.50.7"]))
    ])

add("T4.5.2","T4","T4.5","Human Interface — Boundaries",
    "Does the characteristic operate within covenantal contexts only, or does it cross covenantal boundaries, as the evidence shows?",
    "Characteristic relational",
    [
      slant("crosses-covenantal-boundaries", "Crosses: the cultic/legal asham-vocabulary is covenant-internal (Israel's law), but the same guilt-concept is applied to explicitly non-covenant nations (Edom, Babylon, and implicitly 'the inhabitants of the earth' at Isa 24:6) -- guilt is treated as a universal moral category God holds even non-covenant peoples to.",
            strong="H0816", occurrences=occs("H0816",["Ezek.25.12","Jer.50.7","Isa.24.6"]))
    ])

add("T4.5.3","T4","T4.5","Human Interface — Boundaries",
    "What does the evidence show about the relational scope of the characteristic — who is included and who is not?",
    "Characteristic relational",
    [
      slant("included-and-excluded", "Included: individuals (self), a specific class (priests, judges, a nation's inhabitants), and explicitly foreign nations. Excluded/denied: generational transfer to an innocent descendant (Ezek 18:19-20 explicitly excludes the son from the father's guilt) -- this family's clearest stated exclusion boundary.",
            strong="H5375J", occurrences=occs("H5375J",["Ezek.18.19","Ezek.18.20"]))
    ])

add("T4.6.1","T4","T4.6","Spiritual Beings Interface",
    "In this verse, does the characteristic operate in relation to other spiritual beings — angelic or adversarial — and if so how? Record none if it does not.",
    "Word/term (lexical)",
    [
      slant("confirmed-negative", "No occurrence in H_guilt's 75 occurrences names an angelic or adversarial being as a party. Record none -- a clean, confirmed negative across the whole family, not a gap in reading.", strong=None)
    ])

add("T4.6.2a","T4","T4.6","Spiritual Beings Interface",
    "Does an adversarial-being code ever appear as an acting party in a verse carrying this characteristic?",
    "Word/term (lexical)",
    [slant("no", "No -- none found across all 75 occurrences.", strong=None)])

add("T4.6.2b","T4","T4.6","Spiritual Beings Interface",
    "What does that pattern show about the characteristic being a site of adversarial activity?",
    "Other non-human beings",
    [slant("not-a-site-of-adversarial-activity", "Since T4.6.2a is negative, guilt in this family's vocabulary is never depicted as originating from or exploited by an adversarial being -- worth noting as a real, checked finding rather than an oversight.", strong=None,
           observation_refs=[])],
    cross_flags=[{"statement":"Contrast with deception-vocabulary families elsewhere in M10 (e.g. family K, error/deception) which may show adversarial involvement more directly -- worth a direct cross-family comparison once K's T4 answers exist.","related_family":"K_error_deception","related_cluster":None}])

add("T4.6.3a","T4","T4.6","Spiritual Beings Interface",
    "Does an angelic-being code ever appear as an acting party in a verse carrying this characteristic?",
    "Word/term (lexical)",
    [slant("no", "No -- none found across all 75 occurrences.", strong=None)])

add("T4.6.3b","T4","T4.6","Spiritual Beings Interface",
    "What does that pattern show about the characteristic being communicated, strengthened, or mediated through angelic ministry?",
    "Other non-human beings",
    [slant("no-angelic-mediation", "No angelic-mediation pattern exists in this family -- confirmed negative.", strong=None)])

# ================= T5 =================

add("T5.1.1","T5","T5.1","Nature of Transformation",
    "In this verse, does the characteristic produce transformation in the person, and if so does it change the person's condition, their orientation to their condition, or both? Record none if no transformation is shown.",
    "Verse-context",
    [
      slant("orientation-change", "H0816's recognition-formula produces a change in ORIENTATION -- once 'realized,' the person is oriented toward remedy -- more than a change in underlying condition (recognition alone doesn't remove the guilt; the offering does).",
            strong="H0816", occurrences=occs("H0816",["Lev.4.13"])),
      slant("condition-change", "The guilt-offering/scapegoat/Servant mechanism produces a change in CONDITION itself -- guilt is actually removed/transferred, not merely reoriented toward.",
            strong="H0817/H5375J", occurrences=occs("H5375J",["Lev.16.22"])),
      slant("produced-condition-no-exit-shown", "G1777's fear-bondage (Heb 2:15) is a produced CONDITION with no described exit within this family's own verse.",
            strong="G1777", occurrences=occs("G1777",["Heb.2.15"]))
    ])

add("T5.1.2","T5","T5.1","Nature of Transformation",
    "Is the transformation reversible or irreversible in the evidence?",
    "Characteristic (HIB behaviour)",
    [
      slant("reversible-via-remedy", "Reversible via the prescribed remedy -- the entire guilt-offering/bearing system exists because guilt, in this family's own framing, is addressable/removable (recognition -> offering -> resolved).",
            strong="H0816/H0817", occurrences=occs("H0816",["Lev.4.13"])),
      slant("irreversible-in-narrated-death", "Irreversible in specific narrated cases -- Hos 13:1's 'incurred guilt through Baal and died' shows guilt culminating in death with no remedy narrated in that verse; death forecloses reversal.",
            strong="H0816", occurrences=occs("H0816",["Hos.13.1"]))
    ])

add("T5.2.1","T5","T5.2","Sequence of Inner States",
    "Does this verse describe a sequence of inner states the characteristic moves the person through — a before, during, and after — and what are those states? Record none if no sequence is shown.",
    "Verse-context",
    [
      slant("recognition-sequence", "H0816's Lev 4-6 formula states a sequence: unwitting violation (before, unaware) -> realization/recognition (during, the hinge point the verb itself names) -> offering (after, implied by the wider legal unit).",
            strong="H0816", occurrences=occs("H0816",["Lev.4.13"])),
      slant("no-sequence-elsewhere", "Most narrative/pronouncement occurrences show only a single state, no sequence -- record none.", strong=None)
    ])

add("T5.3.1","T5","T5.3","Mechanism of Change",
    "In this verse, by what mechanism does the characteristic produce change — discipline, encounter, gradual formation, sudden transformation, or other? Record none if no mechanism is shown.",
    "Verse-context",
    [
      slant("ritual-legal-mechanism", "Prescribed ritual/legal mechanism -- the guilt-offering procedure (H0816/H0817/H0819) changes the person's status through a defined ritual act.",
            strong="H0816/H0817/H0819", occurrences=occs("H0816",["Lev.4.13"])),
      slant("substitutionary-mechanism", "Substitutionary transfer -- scapegoat/Servant physically/typologically removing the guilt via a designated carrier.",
            strong="H5375J", occurrences=occs("H5375J",["Lev.16.22","Isa.53.12"])),
      slant("disciplinary-punitive-mechanism", "Discipline/punishment -- bearing punishment (days/years as enacted judgment, Ezek 4:5-6, Num 14:34, Ezek 23:49) is itself the mechanism, distinct from the cultic-ritual one.",
            strong="H5375J", occurrences=occs("H5375J",["Ezek.4.5","Ezek.4.6","Num.14.34","Ezek.23.49"])),
      slant("not-gradual-formation-or-encounter", "No occurrence shows 'gradual formation' or 'sudden encounter' (in the discipleship/sanctification sense) as the mechanism -- those categories are not represented in this family; record none for both.", strong=None)
    ])

add("T5.3.2","T5","T5.3","Mechanism of Change",
    "Does the mechanism differ across contexts in the evidence; if so, how?",
    "Characteristic (HIB behaviour)",
    [
      slant("three-genuinely-distinct-mechanisms", "Yes -- ritual/legal, substitutionary-transfer, and disciplinary/punitive are three genuinely distinct mechanisms attached to different strongs/contexts within the same family, not one mechanism varying superficially.", strong=None)
    ])

add("T5.4.1","T5","T5.4","Suffering and Affliction",
    "In this verse, does the characteristic operate in relation to suffering or affliction — as a response to it, a product of it, or a context for it? Record none if no such relation is shown.",
    "Verse-context",
    [
      slant("guilt-as-cause-of-imposed-suffering", "Bearing punishment (days lying down, forty years wandering) IS the suffering, directly produced by/as the consequence of guilt (Ezek 4:5-6, Num 14:34, Ezek 23:49, Ezek 14:10).",
            strong="H5375J", occurrences=occs("H5375J",["Ezek.4.5","Ezek.4.6","Num.14.34","Ezek.23.49","Ezek.14.10"])),
      slant("unrelated-suffering-context", "Joel 1:18's flocks 'suffer' (H0816's alternate desolate-sense) for lack of pasture -- a suffering context unrelated to moral guilt at all (the non-moral sense already flagged elsewhere).",
            strong="H0816", occurrences=occs("H0816",["Joel.1.18"])),
      slant("no-relation-elsewhere", "Most occurrences state no suffering/affliction relation.", strong=None)
    ])

add("T5.4.2","T5","T5.4","Suffering and Affliction",
    "What does the evidence show suffering doing to the characteristic in the person — and record no such effect if none is shown.",
    "Characteristic (HIB behaviour)",
    [
      slant("suffering-as-temporal-discharge", "Where punishment-bearing is the mechanism, suffering appears to be the vehicle through which guilt is WORKED OFF/discharged over a fixed period (days-for-years symbolic enactments) -- suffering functions as guilt's temporal payment. No occurrence shows suffering intensifying or reducing guilt as an inner quality.",
            strong="H5375J", occurrences=occs("H5375J",["Ezek.4.5","Ezek.4.6"]))
    ])

add("T5.5.1","T5","T5.5","Formation and Sanctification",
    "In this verse, does the characteristic participate in the longer arc of character formation and sanctification — shaping the person over time — and what does the evidence show of its role in that arc? Record none if no such participation is shown.",
    "Verse-context",
    [
      slant("negative-formation-arc-only", "Not directly evidenced as a positive, ongoing sanctification arc anywhere in this family. The closest analogue -- 2Chr 28:13/33:23's cumulative-guilt pattern -- is the INVERSE of sanctification: guilt compounding through unrepented conduct, rather than a virtue compounding through faithful practice.",
            strong="H0819", occurrences=occs("H0819",["2Chr.28.13","2Chr.33.23"])),
      slant("family-fit-flag", "H_guilt shows a negative-formation arc rather than the positive sanctification arc this component's question is primarily aimed at -- worth flagging as a genuine asymmetry: H_guilt may simply not be the right family to answer this component's positive sense at all.", strong=None)
    ])

add("T5.6.1","T5","T5.6","Eschatological Trajectory",
    "In this verse, is the characteristic oriented toward an eschatological fullness — a future state toward which its present operation points — and what does its present experience anticipate of that fullness? Record none if no such orientation is shown.",
    "Verse-context",
    [
      slant("servant-song-eschatological", "Isa 53:10/53:12 (Servant Song) is the family's one clear eschatological orientation -- the guilt-offering/bearing achieves a future state (justification, 'many made righteous') that the present sacrificial system only anticipates.",
            strong="H0817/H5375J", occurrences=occs("H0817",["Isa.53.10"])+occs("H5375J",["Isa.53.12"])),
      slant("no-eschatological-orientation-elsewhere", "Most occurrences show no eschatological orientation -- the ordinary cultic-law and narrative occurrences are all bounded to their immediate historical/legal situation.", strong=None)
    ])

assert len(answers) == 64, f"expected 64 questions answered, got {len(answers)}"

out = {
  "cluster_code": "M10",
  "family_id": "H_guilt",
  "process": "1682-cluster-reading-process-d",
  "spec_round": 1,
  "catalogue_scope": "T0-T5",
  "questions_answered": len(answers),
  "answers": answers
}

with open('_analytics/Clusters/1682-test-m10-process-d-H_guilt-v1-20260911.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("written, questions:", len(answers))
total_slants = sum(len(a['slants']) for a in answers)
print("total slants:", total_slants)
total_adjacent_flags = sum(len(a['needs_adjacent_verse_context']) for a in answers)
print("adjacent-context flags:", total_adjacent_flags)
total_cross_flags = sum(len(a['cross_family_or_cluster_flags']) for a in answers)
print("cross-family/cluster flags:", total_cross_flags)
