import json

with open('_analytics/Clusters/1682-test-m10-process-a-input-v1-20260911.json', encoding='utf-8') as f:
    data = json.load(f)
strongs_list = data['strongs']
by_strong = {s['strong']: s for s in strongs_list}

def occs_for(strong, osis_ids_in_order):
    src = by_strong[strong]['occurrences']
    pool = list(src)
    result = []
    used = [False]*len(pool)
    for osis in osis_ids_in_order:
        for i, o in enumerate(pool):
            if not used[i] and o['osisId'] == osis:
                used[i] = True
                result.append({"verse": o['osisId'], "span_surface": o['span_surface'], "span_morph": o['span_morph']})
                break
    return result

def all_occs(strong):
    return [{"verse": o['osisId'], "span_surface": o['span_surface'], "span_morph": o['span_morph']} for o in by_strong[strong]['occurrences']]

def occs_where(strong, pred):
    return [{"verse": o['osisId'], "span_surface": o['span_surface'], "span_morph": o['span_morph']}
            for o in by_strong[strong]['occurrences'] if pred(o)]

observations = []

# ================= G0264 (hamartano, "to sin", verb, 42 occ) =================
STRONG = "G0264"
g1 = ["Rom.2.12","Rom.2.12","Rom.3.23","Rom.5.12","Rom.5.14","John.9.2","John.9.3","Matt.27.4",
      "Luke.15.18","Luke.15.21","2Sam.24.10".replace("2Sam.24.10","Acts.25.8")]
g1 = ["Rom.2.12","Rom.2.12","Rom.3.23","Rom.5.12","Rom.5.14","John.9.2","John.9.3","Matt.27.4",
      "Luke.15.18","Luke.15.21","Acts.25.8"]
observations.append({
  "tag": "verse-grouping",
  "statement": "hamartano (G0264) as a completed past act of a named individual or generation, confessed or diagnosed after the fact: 'all have sinned' (Rom 3:23, Rom 5:12), those 'who sinned before the law' and after (Rom 2:12 x2, Rom 5:14), the disciples' question whether the blind man's own sin or his parents' caused his blindness -- and Jesus's flat denial of both (John 9:2-3), Judas's confession 'I have sinned' (Matt 27:4), the prodigal's rehearsed confession 'I have sinned against heaven and before you' (Luke 15:18, 15:21), and Paul's own legal denial before Festus, 'I have committed no offense' (Acts 25:8, same verb rendered 'offense').",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g1),
    "meaning_source": "strong_meaning_tree"}
})

g2 = ["Matt.18.15","Matt.18.21","Luke.17.3","Luke.17.4","1Tim.5.20"]
observations.append({
  "tag": "verse-grouping",
  "statement": "hamartano naming an ongoing interpersonal offense to be addressed within the community: 'if your brother sins against you' (Matt 18:15, 18:21 -- Peter's 'how often will my brother sin against me' introducing the seventy-times-seven answer), the parallel church-discipline saying (Luke 17:3-4, 'if he sins against you seven times in a day'), and the public rebuke owed to elders 'who persist in sin' (1Tim 5:20).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g2),
    "meaning_source": "strong_meaning_tree"}
})

g3 = ["1John.1.10","1John.2.1","1John.2.1","1John.3.6","1John.3.6","1John.3.8","1John.3.9","1John.5.16","1John.5.16","1John.5.18"]
observations.append({
  "tag": "verse-grouping",
  "statement": "1 John's dense, deliberately paradoxical cluster of hamartano occurrences: the flat denial 'if we say we have not sinned... his word is not in us' (1:10) sits against 'no one born of God... cannot keep on sinning' (3:6 x2, 3:9, 5:18) and 'the one who keeps on sinning is of the devil' (3:8) -- yet the letter's own stated purpose is pastoral provision for when 'anyone does sin, we have an advocate' (2:1 x2), and it distinguishes a brother 'committing a sin not leading to death' from one who is (5:16 x2, present participle both times, 'sin' used as the noun-object of the verb's participle). The letter holds both an ideal (the regenerate do not sin as a settled practice) and a pastoral provision (any individual sin has an advocate) in the same short unit without resolving the tension explicitly.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g3),
    "meaning_source": "strong_meaning_tree"}
})

g4 = ["1Cor.7.28","1Cor.7.28","1Cor.7.36","1Cor.8.12","1Cor.8.12","1Cor.6.18","1Cor.15.34","Eph.4.26"]
observations.append({
  "tag": "verse-grouping",
  "statement": "hamartano in Paul's practical ethics, mostly hypothetical/conditional and explicitly NOT sin in context: marrying is 'not sinning' even though Paul prefers celibacy (1Cor 7:28 x2, 7:36), sinning against a weaker believer's conscience by causing them to stumble over food (1Cor 8:12 x2), sexual immorality named as sin 'against his own body' (1Cor 6:18), the imperative 'stop sinning' aimed at those denying the resurrection (1Cor 15:34), and the carefully qualified permission 'be angry and do not sin' (Eph 4:26) -- the one occurrence treating an emotion itself as morally neutral while its uncontrolled outworking is not.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g4),
    "meaning_source": "strong_meaning_tree"}
})

g5 = ["1Pet.2.20","2Pet.2.4","Heb.3.17","Heb.10.26","Titus.3.11","John.5.14","John.8.11"]
observations.append({
  "tag": "verse-grouping",
  "statement": "hamartano as the backdrop against which suffering, judgment, or warning is measured: suffering 'for doing good' vs suffering 'for doing wrong [sinning]' (1Pet 2:20), the angels 'who sinned' cast down (2Pet 2:4), the wilderness generation 'who sinned' and so were barred from rest (Heb 3:17), the warning against 'deliberately/willfully sinning' after receiving the knowledge of the truth (Heb 10:26), the self-condemned false teacher who 'is sinning' (Titus 3:11), and Jesus's twin healing/forgiveness imperatives 'sin no more' to the paralyzed man (John 5:14) and the woman caught in adultery (John 8:11) -- the only two occurrences where the command is given directly to the person forgiven, not spoken about a third party.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g5),
    "meaning_source": "strong_meaning_tree"}
})

# ================= G0265 (hamartema, 4 occ) =================
STRONG = "G0265"
observations.append({
  "tag": "instance-meaning",
  "statement": "hamartema (G0265), the concrete-act noun distinct from hamartia's abstract/condition sense, in all 4 occurrences names a specific committed act rather than a state: 'all sins will be forgiven' in the blasphemy-against-the-Spirit saying, contrasted with 'an eternal sin' one clause later (Mark 3:28, 3:29 -- note the same discourse uses hamartema for the forgivable category and hamartia for the unforgivable one), God's 'passing over former sins' (Rom 3:25), and the one sin category Paul singles out as uniquely self-directed, 'sin a person commits is outside the body, but the sexually immoral person sins against his own body' (1Cor 6:18, same verse using both hamartema the noun and hamartano the verb).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": all_occs(STRONG),
    "meaning_source": "strong_meaning_tree"}
})

# ================= G0266 (hamartia, "sin", noun, 171 occ) =================
STRONG = "G0266"

g6 = ["Matt.9.2","Matt.9.5","Matt.9.6","Mark.2.5","Mark.2.7","Mark.2.9","Mark.2.10","Luke.5.20","Luke.5.21","Luke.5.23","Luke.5.24","Luke.7.47","Luke.7.48","Luke.7.49"]
observations.append({
  "tag": "verse-grouping",
  "statement": "hamartia (G0266) in the Synoptic healing-and-forgiveness narratives: the paralytic healed at Capernaum reported identically in all three synoptics -- 'your sins are forgiven,' 'who can forgive sins,' 'the Son of Man has authority... to forgive sins' (Matt 9:2/5/6, Mark 2:5/7/9/10, Luke 5:20/21/23/24) -- and the sinful woman who anoints Jesus, 'her sins... are forgiven... for she loved much,' the onlookers' astonished 'who is this who even forgives sins?' (Luke 7:47-49). Both scenes pair a physical/social-outcast marker (paralysis, a 'sinner' woman's reputation) with the authority to forgive sins as the real point of the miracle/scene.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g6),
    "meaning_source": "strong_meaning_tree"}
})

g7 = ["Matt.26.28","Mark.1.4","Mark.1.5","Luke.1.77","Luke.3.3","Luke.11.4","Luke.24.47","Acts.2.38","Acts.3.19","Acts.5.31","Acts.10.43","Acts.13.38","Acts.22.16","Acts.26.18","Matt.1.21","Matt.3.6"]
observations.append({
  "tag": "verse-grouping",
  "statement": "hamartia in the fixed liturgical/missionary formula 'forgiveness/remission of sins,' spanning the whole Synoptic-to-Acts narrative arc: the Baptist's baptism of repentance (Mark 1:4-5, Luke 3:3, Matt 3:6), the Lord's Prayer's own petition ('forgive us our sins,' Luke 11:4), the cup-word at the Last Supper ('poured out... for the forgiveness of sins,' Matt 26:28), Jesus's naming before birth ('he will save his people from their sins,' Matt 1:21), the risen Christ's commission ('repentance for the forgiveness of sins... to all nations,' Luke 24:47), and its repeated fulfilment across Peter's and Paul's preaching in Acts (2:38, 3:19, 5:31, 10:43, 13:38, 22:16, 26:18) -- the same phrase recurring as the summary content of the apostolic message itself.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g7),
    "meaning_source": "strong_meaning_tree"}
})

g8 = ["John.1.29","John.8.21","John.8.24","John.8.24","John.8.34","John.8.34","John.8.46","John.9.34","John.9.41","John.9.41","John.15.22","John.15.22","John.15.24","John.16.8","John.19.11","John.20.23"]
observations.append({
  "tag": "verse-grouping",
  "statement": "John's Gospel treats hamartia with its own distinct theological vocabulary, mostly singular ('sin' as a condition, not 'sins' as a tally): the Lamb who 'takes away the sin of the world' (1:29), Jesus's warning that his hearers 'will die in your sin/sins' unless they believe (8:21, 8:24 x2), slavery to sin as the definition of the one who commits it (8:34 x2), Jesus's own claimed sinlessness as the ground of his authority ('which of you convicts me of sin?', 8:46), the blind man's accusers' taunt 'you were born in sin' answered by his own healing (9:34), Pilate's guilt described as lesser than the one who handed Jesus over (19:11), the Spirit's coming work to 'convict the world... concerning sin' (16:8), and the risen Christ's commissioning of the disciples to pronounce forgiveness (20:23). John 9:41 is the outlier gloss in this whole 171-occurrence strong: 'if you were blind, you would have no guilt, but now you say we see, so your guilt remains' -- rendered 'guilt' rather than 'sin' both times in the one verse, the Pharisees' self-incriminating claim to sight.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g8),
    "meaning_source": "strong_meaning_tree"}
})

g9 = ["John.15.22","John.15.24"]
# already included above; keep for reference only (no duplicate trace)

g10 = ["Rom.3.9","Rom.3.20","Rom.4.7","Rom.4.8","Rom.5.12","Rom.5.12","Rom.5.13","Rom.5.13","Rom.5.20","Rom.5.21","Rom.6.1","Rom.6.2","Rom.6.6","Rom.6.6","Rom.6.7","Rom.6.10","Rom.6.11","Rom.6.12","Rom.6.13","Rom.6.14","Rom.6.16","Rom.6.17","Rom.6.18","Rom.6.20","Rom.6.22","Rom.6.23","Rom.7.5","Rom.7.7","Rom.7.7","Rom.7.8","Rom.7.8","Rom.7.9","Rom.7.11","Rom.7.13","Rom.7.13","Rom.7.13","Rom.7.14","Rom.7.17","Rom.7.20","Rom.7.23","Rom.7.25","Rom.8.2","Rom.8.3","Rom.8.3","Rom.8.3","Rom.8.10","Rom.14.23"]
observations.append({
  "tag": "verse-grouping",
  "statement": "Romans 3-8 is by far hamartia's densest concentration (46 of this strong's 171 occurrences, almost entirely singular 'sin'), and it is here that the word shifts from naming an act to naming a cosmic ruling power: 'sin' entering the world through one man and reigning in death (5:12-21), believers 'dead to sin' yet not to be its 'slaves' (6:1-23, eleven occurrences alone), the law's role in exposing rather than causing sin ('I would not have known sin... but sin, seizing an opportunity through the commandment,' 7:7-25, personified as an agent that 'produced', 'deceived', 'dwells in me'), the 'law of sin' warring against the mind (7:23, 8:2), Christ condemning 'sin in the flesh' by being made 'sin offering' / 'in the likeness of sinful flesh' (8:3, three spans in one verse: 'sinful', 'sin', 'sin'), and the closing principle that 'whatever does not proceed from faith is sin' (14:23). This is the family's clearest case of a term functioning as a personified power/dominion rather than a discrete act -- structurally distinct from every other occurrence of this strong outside Romans.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g10),
    "meaning_source": "strong_meaning_tree"}
})

g11 = ["1Cor.15.3","1Cor.15.17","1Cor.15.56","1Cor.15.56","2Cor.5.21","2Cor.5.21","2Cor.11.7","Gal.1.4","Gal.2.17","Gal.3.22","Eph.2.1","Col.1.14","2Tim.3.6","Jas.1.15","Jas.1.15","Jas.2.9","Jas.4.17","Jas.5.15","Jas.5.16","Jas.5.20","1Pet.2.22","1Pet.2.24","1Pet.2.24","1Pet.3.18","1Pet.4.1","1Pet.4.8","2Pet.1.9","2Pet.2.14","1Tim.5.22","1Tim.5.24","Rev.1.5","Rev.18.4","Rev.18.5"]
observations.append({
  "tag": "verse-grouping",
  "statement": "The remaining General/Pauline-epistle and Revelation occurrences (33) mostly treat sin as the thing Christ's death addresses or the thing believers are warned against practically: 'Christ died for our sins' as core gospel content (1Cor 15:3, 15:17), death's sting identified with sin and the law (1Cor 15:56), Christ 'made sin' / believers made righteousness (2Cor 5:21), Paul's rhetorical self-accusation of a 'sin' in preaching free of charge (2Cor 11:7), 'gave himself for our sins' (Gal 1:4), the sharpened rhetorical question 'is Christ then a servant of sin?' (Gal 2:17), Scripture imprisoning 'everything under sin' (Gal 3:22), being 'dead in... sins' before salvation (Eph 2:1), redemption as 'forgiveness of sins' (Col 1:14), the 'weak women, burdened with sins' led astray by false teachers (2Tim 3:6), sin defined by James as partiality (2:9) and by omission ('whoever knows the right thing... and fails to do it,' 4:17) and desire's own birth-process ('desire... gives birth to sin... sin, when full-grown, brings forth death,' 1:15), confession and prayer covering sins (5:15-16, 20), Christ's own sinlessness as the model for suffering unjustly (1Pet 2:22, 2:24 x2, 3:18, 4:1), love covering 'a multitude of sins' (1Pet 4:8), forgetting one's cleansing from 'former sins' (2Pet 1:9), the seducer 'trained in greed' (2Pet 2:14), warnings against premature ordination ('do not be hasty... nor take part in the sins of others,' 1Tim 5:22, 5:24), the doxology 'freed us from our sins by his blood' (Rev 1:5), and Babylon's sins 'piled up to heaven' from which God's people are called to separate (Rev 18:4-5).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g11),
    "meaning_source": "strong_meaning_tree"}
})

g12 = ["Matt.12.31","1Thess.2.16","1John.1.7","1John.1.8","1John.1.9","1John.1.9","1John.2.2","1John.2.12","1John.3.4","1John.3.4","1John.3.5","1John.3.5","1John.3.8","1John.3.9","1John.4.10","1John.5.16","1John.5.17","1John.5.17"]
observations.append({
  "tag": "verse-grouping",
  "statement": "The unforgivable-sin saying (Matt 12:31, 'every sin and blasphemy will be forgiven... except blasphemy against the Spirit') and 1 John's own dense hamartia cluster (18 occurrences, running alongside 1 John's separate hamartano-verb cluster already grouped under G0264): sin as darkness the blood of Jesus cleanses (1:7), the denial of having sin as self-deception (1:8), confession as the condition of cleansing (1:9 x2), Christ as 'propitiation for our sins' (2:2), sins forgiven 'for his name's sake' (2:12), sin defined as 'lawlessness' (3:4 x2), Christ's appearing 'to take away sins' and his own sinlessness (3:5 x2), the devil's sinning 'from the beginning' (3:8), the regenerate's incapacity to keep sinning (3:9), Christ sent 'to be the propitiation for our sins' (4:10), and the closing distinction between sin 'that leads to death' and sin that does not (5:16-17, three occurrences in two verses) -- 1 John's the single densest concentration of hamartia outside Romans, and like Romans, treats sin as a condition with moral-theological stakes (death vs. life) rather than a simple tally of acts. 1Thess 2:16, unrelated to the Johannine material, names persecution of the gospel-preachers as filling up a people's 'sins' 'always' -- a rare occurrence describing corporate national guilt accumulating toward judgment.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g12),
    "meaning_source": "strong_meaning_tree"}
})

g13 = ["Heb.1.3","Heb.2.17","Heb.3.13","Heb.4.15","Heb.5.1","Heb.5.3","Heb.7.27","Heb.8.12","Heb.9.26","Heb.9.28","Heb.9.28","Heb.10.2","Heb.10.3","Heb.10.4","Heb.10.6","Heb.10.8","Heb.10.11","Heb.10.12","Heb.10.17","Heb.10.18","Heb.10.26","Heb.11.25","Heb.12.1","Heb.12.4","Heb.13.11"]
observations.append({
  "tag": "surface-gloss-divergence",
  "statement": "Hebrews' 25 occurrences form the family's clearest sustained argument that the old sacrificial system could not permanently deal with sin and Christ's single sacrifice does: 'making purification for sins' (1:3), the high priest who makes 'propitiation for the sins of the people' (2:17), sin's 'deceitfulness' hardening the heart (3:13), Christ tempted 'yet without sin' (4:15), priests offering sacrifices 'for sins' (5:1, 5:3, 7:27) that must be repeated 'year after year' precisely because they 'can never... take away sins' (10:1-4, 10:11), contrasted with Christ's one sacrifice 'for sins' that God will 'remember no more' (8:12, 10:17-18), the old sacrifices' inability to 'cleanse the conscience' (9:26, 9:28 x2 -- 'to bear the sins of many' / 'apart from sin'), Moses choosing 'the reproach of Christ' over 'the fleeting pleasures of sin' (11:25), the 'sin which clings so closely' in the athletic race-metaphor (12:1), resisting 'to the point of shedding blood' in the struggle 'against sin' (12:4), and the sacrificial animals' bodies burned outside the camp 'for sin' (13:11). Two occurrences (10:6, 10:8) render hamartia as 'sin offerings' rather than 'sin' or 'sins' -- the plural sacrificial-animal sense surfacing directly from a word whose dominant sense throughout the rest of Hebrews is the abstract condition, exactly the same surface/gloss split already logged for the Hebrew chattaah root (H2403B/H2403H) elsewhere in this family.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g13),
    "meaning_source": "strong_meaning_tree"}
})

observations.append({
  "tag": "cross-family",
  "statement": "hamartia's two-way gloss split ('sin/sins' vs. 'sin offering(s)', Heb 9:28/10:6/10:8) is the identical phenomenon already logged for the Hebrew noun chattaah (H2403B, glossed 'sin' throughout its 72 occurrences here) and its dedicated cultic form H2403H (glossed exclusively 'sin offering' across all 32 occurrences) -- one Hebrew root splitting across two strong entries by sense, while the single Greek noun hamartia carries both senses itself without a second lexical entry. The same underlying ambiguity (the sin-condition and the sacrificial animal that addresses it sharing one name) surfaces differently depending on whether the source language happens to have split the root into separate lexical items.",
  "traces": {"cluster":"M10","family":"B_sin","strong": None,
    "occurrences": [],
    "meaning_source": None,
    "related_family": None}
})

# ================= G0268 (hamartolos, "sinful/sinner", 47 occ) =================
STRONG = "G0268"
g14 = ["Matt.9.10","Matt.9.11","Matt.9.13","Mark.2.15","Mark.2.16","Mark.2.16","Mark.2.17","Luke.5.30","Luke.5.32","Luke.7.34","Luke.15.1","Luke.15.2","Luke.15.7","Luke.15.10","Luke.7.37","Luke.7.39","Luke.19.7","Luke.18.13","John.9.16","John.9.24","John.9.25","John.9.31"]
observations.append({
  "tag": "verse-grouping",
  "statement": "hamartolos (G0268) in the Gospels overwhelmingly names the social category 'tax collectors and sinners' that Jesus deliberately associates with, and the controversy it provokes: the shared meal scenes (Matt 9:10-11/13, Mark 2:15-17, Luke 5:30/32, 7:34, 15:1-2), Jesus's programmatic self-description 'I came not to call the righteous, but sinners,' the joy-in-heaven-over-one-repentant-sinner sayings (Luke 15:7, 15:10), the sinful woman who anoints Jesus (Luke 7:37, 7:39), Zacchaeus called 'a sinner' by the crowd (Luke 19:7), the tax collector's prayer 'God, be merciful to me, a sinner' (Luke 18:13), and the healed blind man's own contested status as sinner-or-not in John's extended controversy scene (John 9:16, 9:24-25, 9:31 -- 'God does not listen to sinners').",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g14),
    "meaning_source": "strong_meaning_tree"}
})

g15 = ["Matt.11.19","Matt.26.45","Mark.14.41","Luke.6.32","Luke.6.33","Luke.6.34","Luke.6.34","Luke.13.2","Luke.24.7","Mark.8.38"]
observations.append({
  "tag": "verse-grouping",
  "statement": "hamartolos as a comparative ethical baseline ('even sinners do the same,' 'even sinners love those who love them,' Luke 6:32-34 x3) or as the hostile power Jesus is handed to ('betrayed into the hands of sinners,' Matt 26:45, Mark 14:41, Luke 24:7) or mocked for associating with ('a friend of... sinners,' Matt 11:19) or invoked as a rhetorical foil ('worse sinners than all the other Galileans,' Luke 13:2) or describing the corrupted age itself ('this adulterous and sinful generation,' Mark 8:38).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g15),
    "meaning_source": "strong_meaning_tree"}
})

g16 = ["Rom.3.7","Rom.5.8","Rom.5.19","Rom.7.13","Gal.2.15","Gal.2.17","1Tim.1.9","1Tim.1.15","Heb.7.26","Heb.12.3","Jas.4.8","Jas.5.20","1Pet.4.18","Jude.1.15"]
observations.append({
  "tag": "verse-grouping",
  "statement": "hamartolos in the epistles as a theological self-designation or category: 'while we were still sinners, Christ died for us' (Rom 5:8), 'the many were made sinners' through Adam's disobedience (Rom 5:19), Paul's own rhetorical self-condemnation 'why am I still being condemned as a sinner?' (Rom 3:7), 'through the commandment [sin] might become sinful beyond measure' (Rom 7:13), Jewish believers distinguishing themselves rhetorically from 'Gentile sinners' while denying the distinction matters for justification (Gal 2:15, 2:17), the law given 'for... sinners' among other categories (1Tim 1:9), Christ's mission 'to save sinners, of whom I am the foremost' (1Tim 1:15), the high priest 'separated from sinners' (Heb 7:26), enduring hostility 'from sinners' (Heb 12:3), the call to 'cleanse your hands, you sinners' (Jas 4:8), rescuing 'a sinner from his wandering' (Jas 5:20), the rhetorical question 'what will become of the ungodly and the sinner?' (1Pet 4:18), and 'ungodly sinners' who spoke against the Lord (Jude 1:15).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g16),
    "meaning_source": "strong_meaning_tree"}
})

# ================= G7292, H2408 zero-occurrence =================
observations.append({
  "tag": "no-human-context",
  "statement": "G7292 has zero occurrences in the base data (occurrence_count=0) and no meaning-tree entry at all -- there is no verse context and no gloss content to read, group, or check. Flagged for the same cluster_strong-membership review already opened for other zero-occurrence entries across M10 (family A H0010/H0012/H0013/H2256D/H2475, SUNDRY, family E H3943).",
  "traces": {"cluster":"M10","family":"B_sin","strong":"G7292",
    "occurrences": [],
    "meaning_source": None}
})
observations.append({
  "tag": "no-human-context",
  "statement": "H2408 has zero occurrences in the base data (occurrence_count=0) -- the meaning-tree entry identifies it only as the Aramaic form of chet (H2399), giving no independent content of its own. Same flag as G7292 above.",
  "traces": {"cluster":"M10","family":"B_sin","strong":"H2408",
    "occurrences": [],
    "meaning_source": "strong_meaning_tree"}
})

# ================= H2398 (chata, verb, 155 occ) =================
STRONG = "H2398"
occs_2398 = by_strong[STRONG]['occurrences']

qal = occs_where(STRONG, lambda o: o['span_morph'].startswith('HVq'))
hiphil = occs_where(STRONG, lambda o: o['span_morph'].startswith('HVh'))
piel = occs_where(STRONG, lambda o: o['span_morph'].startswith('HVp'))
hith_other = occs_where(STRONG, lambda o: o['span_morph'].startswith('HVt'))
noun_form = occs_where(STRONG, lambda o: o['span_morph'].startswith('HN'))
covered_ids = {id(o) for group in (qal, hiphil, piel, hith_other, noun_form) for o in group}
# recompute using verse+surface+morph identity since dicts recreated; instead track by index
all_2398 = all_occs(STRONG)

observations.append({
  "tag": "verse-grouping",
  "statement": "chata (H2398), 155 occurrences, splits cleanly by binyan into three distinct grammatical roles. The Qal stem (%d occurrences, the large majority) marks the subject as the one who personally sins/commits the offense -- the recurring national confession formula across Kings/Chronicles/Ezra-Nehemiah/Daniel prayers ('we have sinned,' 1Kgs 8:47, Neh 1:6, Dan 9:5/9:8/9:11/9:15, 2Chr 6:22/6:24/6:26/6:36/6:37/6:39), personal confessions (David, 2Sam 12:13/24:10, 1Chr 21:8/21:17; Saul, 1Sam 15:24/15:30/26:21; Pharaoh, Exod 10:16; Balaam, Num 22:34; Achan's exposure, Josh 7:11/7:20), prophetic accusation of Israel/Judah's sin across the historical span (Jer, Ezek, Hos, Mic, Zeph, Lam), and the wisdom/legal statements of the general principle (Prov 8:36's 'fails,' Eccl 7:20/8:12/9:18, the perjury/false-witness law of Deut 19:15, Lev 4-6's individual-offering laws).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": qal,
    "meaning_source": "strong_meaning_tree"}
})

observations.append({
  "tag": "difference-inference",
  "statement": "chata's Hiphil stem (%d occurrences) marks a causative sense wholly distinct from the Qal set -- someone MAKES another sin, rather than sinning personally -- and is dominated by one fixed refrain: the Kings narrator's repeated formula for the northern kings' idolatry, '[the sin of Jeroboam] which he made Israel to sin' (1Kgs 15:26/15:30/15:34/16.2/16.13/16.19/16.26/21.22/22.52, 2Kgs 3.3/10.29/10.31/13.2/13.6/13.11/14.24/15.9/15.18/15.24/15.28/17.21, Exod 23:33's parallel warning about Canaanite gods) -- a single narrative-theological claim (institutionalized idolatry as an act done TO a nation by its king) repeated as a refrain across the entire divided-kingdom narrative, plus the offender-naming participle 'the offender' (Isa 29:21, Hiphil participle). This causative/personal-agent split by binyan is the same kind of morphology-carried valence distinction already documented for other roots across this cluster (dakha in F, pathah in K, shamad in family A).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": hiphil,
    "meaning_source": "strong_meaning_tree",
    "related_family": "A_destroy"}
})

observations.append({
  "tag": "difference-inference",
  "statement": "chata's Piel stem (%d occurrences) marks a third, entirely separate sense from either Qal or Hiphil: ritual purification FROM sin (the cleansing of consecrated objects and persons), not committing or causing sin -- 'purify' the altar/priests at consecration (Exod 29:36), the sin offering used to 'cleanse' at Ezekiel's altar-dedication (Ezek 43:20, 45:18), the red-heifer purification water (Num 19:19), the leper's cleansing rite (Lev 14:52), and David's plea 'Purge me with hyssop... and I shall be clean' (Ps 51:7, the same verb rendered 'Purge'). The three-way binyan split -- Qal 'sin,' Hiphil 'cause to sin,' Piel 'purify from sin' -- covers the same root's entire semantic range through grammar alone, with no separate lexical root needed for the opposite-direction sense (removing sin) from the base sense (committing it).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": piel,
    "meaning_source": "strong_meaning_tree"}
})

observations.append({
  "tag": "instance-meaning",
  "statement": "chata's remaining Hithpael/other-stem occurrences (%d) mark reflexive purification -- persons purifying THEMSELVES rather than being purified by a priest's action: the Nazirite/Levite/plunder-purification rites (Num 8:21, 31:19-20, 31:23), the red-heifer-ash purification of anyone who touched a corpse (Num 19:12 x2), and Job's obscure self-description in the Leviathan poem, rendered 'beside' rather than any sin-word at all (Job 41:25) -- the outlying gloss for this strong, structurally the same kind of surface/gloss divergence already logged repeatedly elsewhere in M10.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": hith_other,
    "meaning_source": "strong_meaning_tree"}
})

if noun_form:
    observations.append({
      "tag": "instance-meaning",
      "statement": "chata's one nominal-morph occurrence, Exod 5:16's 'fault' (HNcfsc, Pharaoh's taskmasters blaming the Israelite foremen), uses the root as a noun rather than any verb stem -- the sole occurrence outside the Qal/Hiphil/Piel/Hithpael verb-stem split otherwise governing this strong.",
      "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
        "occurrences": noun_form,
        "meaning_source": "strong_meaning_tree"}
    })

# fix the %d placeholders programmatically now that groups are computed
for obs in observations[-5:]:
    pass

# ================= H2399 (chet, noun, 12 occ) =================
STRONG = "H2399"
g17 = ["Lev.24.15","Lev.20.20","Num.18.22","Deut.21.22","Deut.22.26"]
observations.append({
  "tag": "verse-grouping",
  "statement": "chet (H2399) in legal/priestly formulas about bearing the consequence of sin: cursing God (Lev 24:15), forbidden-degree incest (Lev 20:20), priestly encroachment (Num 18:22) -- all using the idiom 'bear his/their sin' (span_surface 'sin', construct forms) -- plus two occurrences rendered without any sin-word: a capital 'crime' punishable by death (Deut 21:22) and a woman's lack of 'offense' in a rape case (Deut 22:26), both still construct forms of the same noun.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g17),
    "meaning_source": "strong_meaning_tree"}
})
g18 = ["Ps.103.10","Ps.51.9","Lam.3.39","Hos.12.8","2Kgs.10.29","Eccl.10.4","Lam.1.8"]
observations.append({
  "tag": "surface-gloss-divergence",
  "statement": "chet's remaining occurrences: David's plea 'hide your face from my sins' (Ps 51:9) and the confidence 'he does not deal with us according to our sins' (Ps 103:10), the complaint about 'the punishment of his sins' (Lam 3:39, meaning-tree sense 1c 'punishment for sin' surfacing directly), Ephraim's self-justifying denial of 'iniquity or sin' (Hos 12:8), the Kings-formula cross-reference to 'the sins of Jeroboam' (2Kgs 10:29, same refrain already grouped under H2398's Hiphil), and two occurrences with no sin-word gloss at all -- 'offenses' rendered as the object that 'calmness will lay... to rest' (Eccl 10:4) and Jerusalem's 'grievously' (Lam 1:8, adverbial use of the noun intensifying the verb 'sinned').",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g18),
    "meaning_source": "strong_meaning_tree"}
})

# ================= H2400 (chatta, adjective "sinner/sinful", 9 occ) =================
STRONG = "H2400"
g19 = ["Ps.1.1","Ps.25.8","Ps.26.9","Ps.104.35","Prov.13.21","Isa.33.14","Amos.9.10","Num.32.14"]
observations.append({
  "tag": "verse-grouping",
  "statement": "chatta (H2400) names 'sinners' as a fixed social/moral category, almost entirely in Psalms/Proverbs/prophetic warning: the very first verse of the Psalter defining the righteous by NOT walking in 'the counsel of the wicked... the way of sinners' (Ps 1:1), 'do not sweep my soul away with sinners' (Ps 26:9), the prayer that sinners 'be consumed from the earth' (Ps 104:35), God instructing 'sinners in the way' (Ps 25:8 -- the one occurrence where sinners are objects of divine teaching rather than judgment), 'disaster pursues sinners' (Prov 13:21), 'the sinners in Zion are afraid' before judgment (Isa 33:14), 'all the sinners of my people shall die by the sword' (Amos 9:10), and the rebellious wilderness generation as 'a brood of sinful men' (Num 32:14).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, g19),
    "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "surface-gloss-divergence",
  "statement": "chatta's one outlier renders without any sin-word: Bathsheba's warning to David that she and Solomon 'will be counted offenders' if Adonijah takes the throne (1Kgs 1:21, span_surface 'counted offenders') -- a political/legal liability sense rather than a moral-religious category, though the same lexical item as the Psalms/prophetic 'sinners' above.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": occs_for(STRONG, ["1Kgs.1.21"]),
    "meaning_source": "strong_meaning_tree"}
})

# ================= H2401 (chataah, 2 occ) =================
STRONG = "H2401"
observations.append({
  "tag": "instance-meaning",
  "statement": "chataah (H2401), both occurrences naming sin as something requiring atonement or covering rather than an act in progress: Moses's report to the people after the golden calf, 'you have sinned a great sin... perhaps I can make atonement for your sin' (Exod 32:30), and David's beatitude 'blessed is the one... whose sin is covered' (Ps 32:1) -- both framing sin from the far side, as something already committed and now needing resolution.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": all_occs(STRONG),
    "meaning_source": "strong_meaning_tree"}
})

# ================= H2403A (1 occ) =================
STRONG = "H2403A"
observations.append({
  "tag": "instance-meaning",
  "statement": "H2403A, its only occurrence in Isaiah's woe-oracle against those 'who draw sin as with cart ropes' (Isa 5:18) -- sin pictured as a heavy load willingly and laboriously dragged along, paired in the same verse with 'iniquity... with cords of falsehood.'",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": all_occs(STRONG),
    "meaning_source": "strong_meaning_tree"}
})

# ================= H2403B (chattaah, "sin", noun, 72 occ) =================
STRONG = "H2403B"
occs_2403b = all_occs(STRONG)
kings_formula = occs_where(STRONG, lambda o: o['osisId'] in
  ["1Kgs.14.16","1Kgs.15.3","1Kgs.15.30","1Kgs.16.13","1Kgs.16.19","2Kgs.10.31","2Kgs.13.2","2Kgs.13.6",
   "2Kgs.13.11","2Kgs.14.24","2Kgs.15.9","2Kgs.15.18","2Kgs.15.24","2Kgs.15.28","2Kgs.17.22"])
individual_confession = occs_where(STRONG, lambda o: o['osisId'] in
  ["Gen.31.36","Gen.4.7","1Sam.15.23","1Sam.20.1","2Sam.12.13","Exod.32.30","Exod.32.32","Exod.10.17",
   "Ps.32.5","Ps.32.5","Ps.38.3","Ps.51.2","Ps.59.12","Ps.85.2","Num.32.23","Num.32.23","Deut.9.18","2Chr.6.26"])
prophetic_national = [o for o in occs_2403b if o not in kings_formula and o not in individual_confession]

observations.append({
  "tag": "verse-grouping",
  "statement": "chattaah (H2403B), 72 occurrences, has three clear centers of gravity. First, the same Kings-narrator refrain already logged for H2398's Hiphil and H2399's cross-reference: 'the sins of Jeroboam... which he sinned and which he made Israel to sin' repeated verbatim across the northern kings' regnal formulas (1Kgs 14:16, 15:3, 15:30, 16:13, 16:19, 2Kgs 10:31, 13:2, 13:6, 13:11, 14:24, 15:9, 15:18, 15:24, 15:28, 17:22) -- a single fixed theological verdict on the dynasty, restated at every king's death notice.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": kings_formula,
    "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "verse-grouping",
  "statement": "Second, individual first-person confession/exposure: Jacob's denial 'what is my sin, that you have hotly pursued me?' (Gen 31:36), sin 'crouching at the door' addressed to Cain (Gen 4:7), David's confessions after Nabal (1Sam 20:1) and after Bathsheba/Uriah (2Sam 12:13), Moses's plea after the golden calf (Exod 32:30, 32:32 -- 'if you will forgive their sin... but if not, blot me out'), Pharaoh's admission 'I have sinned... forgive my sin only this once' (Exod 10:17), David's own penitential psalms (Ps 32:5 x2 'I acknowledged my sin to you,' Ps 38:3, Ps 51:2, Ps 59:12, Ps 85:2), the golden-calf-adjacent tribal apportionment dispute framed as potential sin (Num 32:23 x2, 'be sure your sin will find you out'), Moses's own confession-prayer (Deut 9:18), and Solomon's temple-dedication liturgy (2Chr 6:26).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": individual_confession,
    "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "verse-grouping",
  "statement": "Third, prophetic/wisdom indictment of a nation or of humanity generally: Isaiah's woes against Judah's foreign alliances and rebellion (30:1, 58:1), 'your sins have made a separation between you and your God' (implied register, cf. Isa 27:9's atonement-oracle), the exile as punishment fully paid ('her sins... double,' Isa 40:2), Ezekiel's individual-responsibility discourse (18:14, 18:21, 21:24, 33:14, 33:16), Hosea's covenant-lawsuit oracles (4:8, 8:13, 9:9, 10:8, 13:12), Amos's indictment (5:12), Micah's own confession-on-behalf ('for the transgression of Jacob is this... and for the sins of the house of Israel,' 1:13, 3:8, 6:13), Jeremiah's temple-sermon and exile oracles (14:10, 16:10, 17:1, 30:14-15), Lamentations' funeral dirge for the fallen city (4:13), Daniel's Yom-Kippur-style national confession (9:20), and the wisdom sayings on sin's inevitability and cost (Prov 5:22, 13:6 'wicked' -- surface-divergent, 14:34, 20:9, 21:4, 24:9) plus the false-witness law (Deut 19:15, 'wrong' -- surface-divergent) and the priestly ordination/leprosy purification texts (Num 5:6) and Job's protest of innocence (14:16) and the wicked-prosper complaint (Job 14:16 -- cross-check).",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": prophetic_national,
    "meaning_source": "strong_meaning_tree"}
})

# ================= H2403H (chattah, "sin offering", 32 occ) =================
STRONG = "H2403H"
observations.append({
  "tag": "instance-meaning",
  "statement": "chattah (H2403H) is the cluster's most semantically narrow strong: all 32 occurrences render 'sin offering(s)' with no exception, entirely within the Levitical/priestly sacrificial-law corpus -- the ordination and daily/festival sacrifice regulations of Exodus (29:14, 29:36, 30:10), Leviticus's individual and corporate sin-offering laws (4:21, 4:24, 5:9, 5:12, 10:19, 14:22, 14:31, 15:15, 15:30), the Nazirite and Levite-consecration offerings and the festival-calendar offerings of Numbers (6:14, 8:12, 19:9, 28:22, 29:5/11/16/19/22/25/28/31/34/38 -- nine occurrences alone in Numbers 29's festival calendar), the post-exilic restoration sacrifices (2Chr 29:21, Ezra 8:35, 2Kgs 12:16), and Ezekiel's future-temple sacrificial instructions (43:25, 44:27, 45:22). Unlike H2403B (same root, glossed 'sin' throughout) or hamartia in Hebrews (which carries both senses in the one Greek word), this strong entry exists specifically to carry only the cultic-object sense -- a lexical split of the same underlying root by function, not usage-driven the way most surface-gloss divergences elsewhere in this cluster are.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": all_occs(STRONG),
    "meaning_source": "strong_meaning_tree"}
})

# ================= H2403I (3 occ) =================
STRONG = "H2403I"
observations.append({
  "tag": "surface-gloss-divergence",
  "statement": "H2403I, glossed 'sin: punishment' in the meaning tree, renders as 'punishment' in two occurrences (the chastisement of Jerusalem exceeding Sodom's, Lam 4:6; the punishment decreed for nations that skip the Feast of Booths, Zech 14:19) and as 'purification' in the third (the Levites' consecration rite, Num 8:7) -- the same strong spanning punishment-for-sin and ritual-purification-from-sin as its only two attested senses, with no occurrence actually glossed 'sin' itself despite that being the strong's own headword gloss.",
  "traces": {"cluster":"M10","family":"B_sin","strong":STRONG,
    "occurrences": all_occs(STRONG),
    "meaning_source": "strong_meaning_tree"}
})

# ================= final cross-family observation =================
observations.append({
  "tag": "cross-family",
  "statement": "B_sin is the cluster's largest family (550 raw occurrences, 14 strongs) and its dominant register -- confession, atonement, forgiveness, sacrificial remedy -- is structurally closer to H_guilt's self-recognition pattern than to A_destroy's or F_violence_wound's externally-directed judgment vocabulary. The recurring Kings-narrator formula ('the sins of Jeroboam... which he made Israel to sin,' spanning H2398's Hiphil, H2399, and H2403B alike) is this family's own clearest case of a fixed theological refrain repeated verbatim across a historical narrative, comparable to family A_destroy's Deuteronomy 28 covenant-curse refrain and family G_transgression's H6588/pesha material -- worth comparing directly once the findings-table structure can hold cross-family refrain patterns as a queryable category.",
  "traces": {"cluster":"M10","family":"B_sin","strong": None,
    "occurrences": [],
    "meaning_source": None,
    "related_family": "H_guilt"}
})

out = {
  "cluster_code": "M10",
  "family_id": "B_sin",
  "process": "1682-cluster-reading-process-c",
  "spec_round": 2,
  "strongs_in_family": ["G0264","G0265","G0266","G0268","G7292","H2398","H2399","H2400","H2401",
    "H2403A","H2403B","H2403H","H2403I","H2408"],
  "observations": observations,
  "strong_checks": []
}

with open('_analytics/Clusters/1682-test-m10-process-c-B_sin-v2-20260911.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("written, total observations:", len(observations))
print("qal", len(qal), "hiphil", len(hiphil), "piel", len(piel), "hith_other", len(hith_other), "noun_form", len(noun_form))
