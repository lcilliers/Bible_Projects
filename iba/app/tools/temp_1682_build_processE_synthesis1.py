# -*- coding: utf-8 -*-
import json

syntheses = []

def add(synthesis_id, statement, status, grounded_in, revisit_note, supersedes=None):
    syntheses.append({
        "synthesis_id": synthesis_id,
        "statement": statement,
        "status": status,
        "supersedes": supersedes,
        "grounded_in": grounded_in,
        "revisit_note": revisit_note
    })

add(
    "status-vs-characteristic-hypothesis",
    "Researcher's working hypothesis (this chat turn, prior to running B_sin/G_transgression): "
    "guilt, and possibly sin and transgression, are not 'real characteristics' of the inner being "
    "but particular STATUSES that result from something else and have a knock-on effect -- a "
    "diagnostic marker downstream of an act, not an autonomous mover. First proposed from H_guilt "
    "alone; the direct instruction to run B_sin and G_transgression next was explicitly to test it "
    "against families predicted to behave similarly, not as a mechanical next-in-sequence choice.",
    "provisional",
    grounded_in=[
        {"family": "H_guilt", "question_code": None, "process": "process-d", "note": "T1.2.1, T2.1.1/1.2, T5.5.1 jointly showed condition/status kind, no faculty-seat, no positive sanctification arc"}
    ],
    revisit_note="This is the seed hypothesis the other syntheses below test directly. Superseded in "
                 "part by 'gradient-of-characteristic-hood' below once B_sin/G_transgression were read."
)

add(
    "gradient-of-characteristic-hood",
    "Across the three families read so far, the hypothesis holds only as a GRADIENT, not a uniform "
    "verdict: H_guilt is the purest fit (pure status, no faculty-seat anywhere in 75 occurrences, no "
    "spiritual-beings involvement); G_transgression sits between the two poles (dominantly a "
    "counted/accruing status -- the Amos 'three...and four' formula, load-imagery -- but with two "
    "isolated faculty-touches: heart at Ps 36:1, mouth at Ps 17:3, and one quasi-agentive moment, "
    "transgression itself 'speaking... deep in his heart'); B_sin is the clearest complication -- "
    "in Romans 5-8 'Sin' is grammatically personified as a near-agent that 'reigns,' 'dwells in,' "
    "'deceives,' and wars against 'the law of my mind' (Rom 7:23), a systemic mind-and-body "
    "engagement no occurrence in H_guilt or G_transgression showed. Sin is doing something "
    "structurally different from its two neighbors even though all three were initially suspected "
    "of the same 'not a real characteristic' status.",
    "provisional",
    grounded_in=[
        {"family": "H_guilt", "question_code": "T2.1.1", "process": "process-d"},
        {"family": "H_guilt", "question_code": "T2.1.2", "process": "process-d"},
        {"family": "G_transgression", "question_code": "T2.1.1", "process": "process-d"},
        {"family": "G_transgression", "question_code": "T2.1.2", "process": "process-d"},
        {"family": "B_sin", "question_code": "T2.1.1", "process": "process-d"},
        {"family": "B_sin", "question_code": "T2.1.2", "process": "process-d"},
        {"family": "B_sin", "question_code": "T1.2.1", "process": "process-d"}
    ],
    revisit_note="Needs at least two or three more families (a clear 'act/behavior' family and a "
                 "clear positive-virtue family, if one exists in this cluster's naming) to know "
                 "whether this is a real three-point gradient or just three data points that happen "
                 "to differ. The next family run should explicitly test where it falls on this "
                 "gradient, not just whether it fits the original binary hypothesis.",
    supersedes="status-vs-characteristic-hypothesis"
)

add(
    "t4-6-three-way-spiritual-beings-pattern",
    "T4.6 (spiritual-beings interface) produced a clean three-way split across the same three "
    "families, independent of the T2 gradient above: H_guilt = confirmed negative on BOTH "
    "adversarial and angelic involvement (no occurrence in 75 names either); B_sin = confirmed "
    "POSITIVE on both -- the devil himself is the acting subject of hamartano ('the devil has been "
    "sinning from the beginning,' 1John 3:8) and fallen angels are named as having sinned (2Pet "
    "2:4); G_transgression = positive angelic but negative adversarial -- angels appear only as "
    "MEDIATORS of the law itself ('the message declared by angels,' Heb 2:2), a foundational/"
    "authority-granting role distinct from B_sin's fallen-angel-as-transgressor case, with no "
    "adversarial-transgressor occurrence found anywhere in the family's 118 occurrences.",
    "corroborated",
    grounded_in=[
        {"family": "H_guilt", "question_code": "T4.6.1", "process": "process-d"},
        {"family": "H_guilt", "question_code": "T4.6.2a", "process": "process-d"},
        {"family": "H_guilt", "question_code": "T4.6.2b", "process": "process-d"},
        {"family": "H_guilt", "question_code": "T4.6.3a", "process": "process-d"},
        {"family": "H_guilt", "question_code": "T4.6.3b", "process": "process-d"},
        {"family": "B_sin", "question_code": "T4.6.1", "process": "process-d"},
        {"family": "B_sin", "question_code": "T4.6.2a", "process": "process-d"},
        {"family": "B_sin", "question_code": "T4.6.2b", "process": "process-d"},
        {"family": "B_sin", "question_code": "T4.6.3a", "process": "process-d"},
        {"family": "B_sin", "question_code": "T4.6.3b", "process": "process-d"},
        {"family": "G_transgression", "question_code": "T4.6.1", "process": "process-d"},
        {"family": "G_transgression", "question_code": "T4.6.2a", "process": "process-d"},
        {"family": "G_transgression", "question_code": "T4.6.2b", "process": "process-d"},
        {"family": "G_transgression", "question_code": "T4.6.3a", "process": "process-d"},
        {"family": "G_transgression", "question_code": "T4.6.3b", "process": "process-d"}
    ],
    revisit_note="'Corroborated' rather than 'provisional' because each of the three positions was "
                 "independently checked (not assumed) by mechanically answering all four T4.6 "
                 "sub-questions per family and finding a real, textually-grounded difference each "
                 "time -- this is the single most load-bearing cross-family finding of round 1. "
                 "Still worth re-testing: does the pattern correlate with the T2 gradient above "
                 "(act/agentive characteristics attract more spiritual-beings involvement than pure "
                 "statuses), or is it independent? Needs more families to separate the two axes."
)

add(
    "isaiah-53-five-convergence",
    "Isaiah 53:5 (and the surrounding Servant Song, vv.10/12) is independently cited by observations "
    "in at least three separately-catalogued M10 families -- H_guilt (H0817 v.10 'offering for "
    "guilt', H5375J v.12 'bore the sin of many'), D_crime_injustice (H5771G, logged independently "
    "before this comparison began), and G_transgression (H6588 v.5 'pierced for our "
    "transgressions') -- four strongs across three families all landing on the same handful of "
    "verses without being asked to. This is the cluster's single most cross-referenced textual "
    "location found so far, and it happened without any deliberate cross-family search -- each "
    "family's own process-(c) reading surfaced it independently.",
    "corroborated",
    grounded_in=[
        {"family": "H_guilt", "question_code": None, "process": "process-c", "note": "H0817 instance-meaning Isa.53.10; H5375J instance-meaning Isa.53.12; cross-family observation citing G_transgression"},
        {"family": "G_transgression", "question_code": None, "process": "process-c", "note": "H6588 instance-meaning Isa.53.5, citing H_guilt and D_crime_injustice"},
        {"family": "H_guilt", "question_code": "T0.4.1", "process": "process-d"},
        {"family": "G_transgression", "question_code": "T0.4.1", "process": "process-d"}
    ],
    revisit_note="Worth a dedicated single-verse-cluster deep read once enough families are done to "
                 "know if any more strongs converge on the same three verses -- this could become "
                 "its own standing cross-cluster reference point (a 'convergence verse' category) "
                 "rather than a one-off curiosity."
)

add(
    "guilt-and-transgression-one-structure-two-names",
    "family G_transgression's own process-(c) reading independently concluded (not prompted by this "
    "comparison) that its overlap with H_guilt 'looks less like two related-but-distinct concepts "
    "and more like two English-gloss windows onto one shared underlying structure' -- grounded in "
    "three specific parallels: G3848's Jas 2:9/11 whole-law-is-one-unit argument mirrors G1777's "
    "identical argument in H_guilt (same author, same argument, two different M10 families); "
    "G3900's forgiveness-defined identity mirrors H0817's guilt-offering identity; and both "
    "families show the same recognition-accrual-remedy sequence and the same against-man/against-"
    "God/against-nation three-register split. This is a real structural claim about how the M10 "
    "family-grouping itself should be read, not just a shared-vocabulary coincidence.",
    "provisional",
    grounded_in=[
        {"family": "G_transgression", "question_code": None, "process": "process-c", "note": "cross-family observation, 'this family reinforces a pattern...'"},
        {"family": "H_guilt", "question_code": None, "process": "process-c", "note": "cross-family observation citing B_sin's Lev 5:7 overlap and F_violence_wound's 'filled with X' construction"}
    ],
    revisit_note="If corroborated further, this has a direct implication for the eventual "
                 "findings-table/characteristic work: guilt and transgression might need to be "
                 "modeled as one node with two lexical faces, not two nodes -- a genuine design "
                 "decision for whoever does that modeling, not something to resolve by fiat here. "
                 "Should be tested against B_sin too: does sin show the same three-register split "
                 "and recognition-accrual-remedy sequence, or is that specifically a "
                 "guilt/transgression feature that sin's agentive character breaks?"
)

out = {
  "cluster_code": "M10",
  "process": "1682-cluster-reading-process-e",
  "spec_round": 1,
  "families_compared": ["H_guilt", "B_sin", "G_transgression"],
  "syntheses": syntheses
}

with open('_analytics/Clusters/1682-test-m10-process-e-synthesis-round1-v1-20260911.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("written, syntheses:", len(syntheses))
