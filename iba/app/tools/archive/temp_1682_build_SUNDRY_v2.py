import json

with open('_analytics/Clusters/1682-test-m10-process-a-input-v1-20260911.json', encoding='utf-8') as f:
    data = json.load(f)
by_strong = {s['strong']: s for s in data['strongs']}

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

observations = []

observations.append({
  "tag": "no-human-context",
  "statement": "G21497 ('Sin/Shin') has zero occurrences and an empty meaning block -- it is the Greek transliteration entry for the Hebrew letter name, not a word with independent scriptural usage. Earmarked; no further analysis possible or warranted.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"G21497","occurrences": [], "meaning_source": None}
})

observations.append({
  "tag": "instance-meaning",
  "statement": "H5512B ('Sin') is a place name -- the wilderness of Sin between Elim and Sinai, an Exodus itinerary stop. Its own meaning block states this directly: 'a location... Sin = thorn or clay, the tract of wilderness between Elim and Sinai.' All four occurrences are travel-itinerary notices ('the congregation... camped in the wilderness of Sin') with no moral or inner-being content of any kind.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H5512B",
    "occurrences": all_occs("H5512B"), "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "data-error",
  "statement": "H5512B is a homograph collision with the English word 'sin' -- earmarked; no further analysis of it as a family-H10 concept is warranted.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H5512B","occurrences": [], "meaning_source": None}
})

observations.append({
  "tag": "instance-meaning",
  "statement": "G0073 (agon) has real, coherent, human-relevant meaning: a struggle or contest, most often used in the NT as an athletic/perseverance metaphor for faithful endurance -- 'fight the good fight of the faith' (1Tim 6:12), 'I have fought the good fight, I have finished the race' (2Tim 4:7), 'run with endurance the race that is set before us' (Heb 12:1), plus 'conflict'/'struggle' describing external opposition faced in ministry (1Thess 2:2, Phil 1:30, Col 2:1). None of its 6 occurrences describe a moral failure or an inner disposition toward wrongdoing.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"G0073",
    "occurrences": all_occs("G0073"), "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "data-error",
  "statement": "G0073's attested meaning (faithful perseverance, an athletic-contest metaphor) does not touch M10's apparent theme (sin/moral-failure vocabulary) in any of its 6 occurrences. This is not a 'no human context' case -- the word has clear, positive, analysable meaning -- it is a cluster_strong membership question: on the verse evidence, this strong does not belong to M10 at all. Flagged for the cluster-assignment process, not resolved here.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"G0073","occurrences": [], "meaning_source": None}
})

observations.append({
  "tag": "instance-meaning",
  "statement": "H2342J (chul, one sense-split of the root) has real, coherent meaning covering whirling and its natural/violent extensions, all literal: a whirling storm-tempest twice in one verse ('a storm... it will burst,' Jer 23:19, two spans -- 'whirling' and 'burst') and again at Jer 30:23, a spindle/whirl reference within a curse formula ('may he... fall,' 2Sam 3:29), the voice of the Lord in the storm making a deer give birth (Ps 29:9), and a sword raging/whirling against cities (Hos 11:6). None describe moral perversion, despite this root being pulled into a 'twist/perversion' gloss-family.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H2342J",
    "occurrences": all_occs("H2342J"), "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "instance-meaning",
  "statement": "H2342K's occurrences (the same root's 'wait/anticipate' sense) are likewise all literal waiting, none moral: Ps 37:7's counsel to wait patiently, Gen 8:10's dove sent out and waited for, Judg 3:25's servants waiting outside a chamber, Mic 1:12's anxious waiting for good news.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H2342K",
    "occurrences": all_occs("H2342K"), "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "data-error",
  "statement": "H2342J/H2342K were pulled into a 'twist/perversion' gloss-family purely because one of chul's many senses translates as 'twist' -- a homonym match on the English gloss word, not a match on meaning. Neither sub-sense's actual verse usage touches moral perversion. Flagged as a cluster_strong membership question.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H2342J","occurrences": [], "meaning_source": None}
})

observations.append({
  "tag": "instance-meaning",
  "statement": "H7806 (shazar, 'to twist') has real, coherent meaning: a technical textile-craft term. All 19 occurrences are the tabernacle-construction formula 'fine twined linen' (two occurrences render slightly differently -- 'twined linen' at Exod 39:24, 'twined' alone at Exod 39:29), repeated near-verbatim through Exodus 26-39 (curtains, the ephod, the breastpiece, the veil, the screen). No occurrence has moral content.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H7806",
    "occurrences": all_occs("H7806"), "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "data-error",
  "statement": "H7806 is purely technical craft vocabulary (linen-weaving), pulled into a moral-perversion family on the same gloss-word homonym basis as H2342J/K. Flagged as a cluster_strong membership question -- the largest single misassigned strong found in this cluster by occurrence count (19).",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H7806","occurrences": [], "meaning_source": None}
})

observations.append({
  "tag": "instance-meaning",
  "statement": "H3725 (atonement) has real, central theological meaning -- its one occurrence names the Day of Atonement itself ('a Day of Atonement, to make atonement for you before the Lord your God').",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H3725",
    "occurrences": all_occs("H3725"), "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "difference-inference",
  "statement": "Unlike the other SUNDRY strongs, H3725 is not off-topic -- it is the *remedy* for this cluster's theme rather than an instance of it, and it sits conceptually beside family H_guilt's own guilt-offering vocabulary (H0817, H0819) and the atonement language already appearing inside that family's Lev 14:21 occurrence. This is a fit question, not a homonym or membership error: does 'atonement' belong in a sin/moral-failure cluster at all, or does it belong with the guilt-offering system specifically?",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H3725",
    "occurrences": all_occs("H3725"), "meaning_source": None,
    "related_family": "H_guilt"}
})

observations.append({
  "tag": "no-human-context",
  "statement": "H6330 (staggering) has zero occurrences in the live span/verse data -- no verse evidence exists to read. Meaning block only: 'tottering, staggering, stumbling; of qualm of conscience (fig.).' Earmarked; no further analysis possible without verse context.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H6330",
    "occurrences": [], "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "difference-inference",
  "statement": "H6330's own meaning block carries a figurative sense -- 'qualm of conscience' -- that would fit the guilt/inner-disposition theme well, unlike the other strongs in this SUNDRY bucket. Its complete absence of verse evidence (0 occurrences) is what earns it a SUNDRY placement here, not a lack of thematic fit -- this is a data-completeness gap, not a homonym or a membership error, and should be distinguished from G0073/chul/shazar's genuine off-topic status.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H6330",
    "occurrences": [], "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "data-error",
  "statement": "H6330 is included in cluster_strong for M10 but has no live span occurrences anywhere in the base data. Flagged for the spine/integrity process (same category as H2054 in family H_guilt), not resolved here.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H6330","occurrences": [], "meaning_source": None}
})

observations.append({
  "tag": "instance-meaning",
  "statement": "H4560's one occurrence ('a thousand from each tribe... provided/mustered for war,' Num 31:5, span_surface 'provided', HVNw3mp -- Niphal, passive: the men ARE mustered/provided, not an active moral act) is a military-levy term -- its own meaning block gives 'to set apart, deliver up, offer,' with no sense resembling 'commit [a sin]' at all. The stepGloss 'to commit' appears to be a mismatch against the strong's actual attested meaning and usage.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H4560",
    "occurrences": all_occs("H4560"), "meaning_source": "strong_meaning_tree"}
})
observations.append({
  "tag": "data-error",
  "statement": "H4560's stepGloss ('to commit') does not match its meaning-tree definition ('to set apart, deliver up, offer') or its one occurrence's actual sense (military mustering). Either the stepGloss is wrong, or it reflects a different, unattested sub-sense not represented in the live verse data. Flagged for gloss/data review, separate from cluster-membership questions.",
  "traces": {"cluster":"M10","family":"SUNDRY","strong":"H4560","occurrences": [], "meaning_source": None}
})

observations.append({
  "tag": "cross-family",
  "statement": "This SUNDRY bucket separates into four genuinely different reasons for non-placement, worth keeping distinct rather than treating 'sundry' as one undifferentiated leftover bin: (1) true homonym/name collisions with no inner-being content (G21497, H5512B); (2) real, coherent, human-relevant meaning that is simply off-topic for this cluster -- a cluster_strong membership question (G0073, H2342J, H2342K, H7806); (3) genuine candidates for the cluster's theme that lack the verse evidence to confirm it (H6330), or a specific data/gloss mismatch worth checking (H4560); and (4) a conceptually adjacent but distinct role -- the cluster's remedy rather than its subject (H3725, close to family H_guilt).",
  "traces": {"cluster":"M10","family":"SUNDRY","strong": None,
    "occurrences": [], "meaning_source": None}
})

out = {
  "cluster_code": "M10",
  "family_id": "SUNDRY",
  "process": "1682-cluster-reading-process-c",
  "spec_round": 2,
  "strongs_in_family": ["G21497","H5512B","G0073","H2342J","H2342K","H7806","H3725","H6330","H4560"],
  "observations": observations,
  "strong_checks": []
}

with open('_analytics/Clusters/1682-test-m10-process-c-SUNDRY-v2-20260911.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("written, total observations:", len(observations))
