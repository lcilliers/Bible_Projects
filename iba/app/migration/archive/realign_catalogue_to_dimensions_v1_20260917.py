"""Re-align `wa_obs_question_catalogue` to the 12 goal-derived dimensions (escalation #1712,
2026-09-17). Full chain: end goal (programme prose Ch.1's definition) -> 12 independently-derived
dimensions (two blind derivations, converged) -> checked against live data (role-cluster tags,
M47, science-extract files) -> this migration, which is the actual re-grounding the researcher
asked for: "create new questions for every prompt that is missing... revise the text content of
every existing question to align with the dimension object... capture the dimension and the data
mechanism in the table... re-align all the numbering."

Every one of the 92 live questions is reclassified to its primary dimension and given a real
`data_mechanism` value (a role-cluster tag, a specific existing table/cluster, an existing
reading-stage tag, a science-extract file, or "direct LLM reading of base text -- no special tag
needed"), CHECKED against live data (SS6 of iba/docs/1712-catalogue-first-principles-validation-
method-v1-20260917.md), not asserted.

Two categories fall OUTSIDE the 12 substantive dimensions, found while classifying -- kept, not
forced into the 12:
- `M0` Lexical/Textual Evidence -- T1.1 (Name)/T1.2 (Kind)/T1.3 (Boundary)/T1.4.1a (grammatical
  form)/T7.1 (Lexical-Semantic)/T7.2 (Verse-Literary) are evidence-gathering/definitional
  questions that FEED the 12 dimensions rather than being one themselves.
- `X0` Cross-Characteristic Synthesis -- T6 (Relationships: co-occurrence/sequence/causal/
  vocabulary-sharing/distinctions) asks about relationships BETWEEN characteristics, a
  cross-cluster synergy-stage concern, not a per-characteristic dimension.

9 new questions authored for the dimensions found to have ZERO dedicated coverage: D1 Cognitive,
D2 Affective, D9 Physiological/Generational, D12 Social/Behavioural (both D9/D12 now have a real,
checked data mechanism -- the per-cluster science-extract files at
Workflow/Sciences/science_files/wa-m{NN}-*-scienceextract-*.md, confirmed live, structured exactly
for this per the files' own "standing reference for T7.3 prompt responses" framing), D11's
scientific half, and D7's operation-anchored gap (T3/Operations is the densest role signal in the
corpus -- 85.8% of characteristic-verses -- but had no catalogue question anchored to it at all).

T7.3.1-4 (the old generic "which human-science framework" catch-all) are superseded by the new
dedicated D9/D11/D12 questions, which name the actual mechanism instead of asking the LLM to guess
a framework -- marked deleted=1 with a review_note, not silently dropped.

`source_word`/`source_registry_no` dropped (confirmed relics, escalation #1712 chat turn 2026-09-17:
source_word is the literal string "Programme" on all 92 rows, source_registry_no is NULL on all 92).

Renumbering is safe: checked live, the only current-DB tables referencing `question_code` directly
are `ib_observation`/`ib_node`, both 0 rows. The old bible_research.db-side reference tables
(cluster_finding/wa_finding_catalogue_links/wa_flag_type_question_link) reference this table's own
numeric `obs_id`, which is UNCHANGED by this migration, and in any case live in a different
database entirely.

Safe to re-run: guarded by `catalogue_version`; a second run is a no-op if version already applied.

Usage:
    python iba/app/migration/realign_catalogue_to_dimensions_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
CATALOGUE_VERSION = "v2-dimension-realign-20260917"

# (old_code, new_code, new_tier, new_component_code, new_component_title, dimension, data_mechanism)
REMAP: list[tuple[str, str, str, str, str, str, str]] = [
    # D3 Volitional
    ("T1.4.1b", "D3.1.1", "D3", "D3.1", "Modes of Operation", "D3",
     "Direct LLM reading of base verse/lexical text -- no special tag needed."),
    ("T1.4.2", "D3.1.2", "D3", "D3.1", "Modes of Operation", "D3",
     "Direct LLM reading of base verse/lexical text -- no special tag needed."),
    ("T1.4.3", "D3.1.3", "D3", "D3.1", "Modes of Operation", "D3",
     "Direct LLM reading of base verse/lexical text -- no special tag needed."),
    ("T1.7.1", "D3.2.1", "D3", "D3.2", "Conditions of Reception", "D3",
     "Direct LLM reading of base verse/lexical text -- no special tag needed."),
    ("T1.7.2", "D3.2.2", "D3", "D3.2", "Conditions of Reception", "D3",
     "Direct LLM reading; secondary D7 signal where the blocking party is named (role-T4 Adversarial / role-T9 Angelic)."),
    ("T1.7.3", "D3.2.3", "D3", "D3.2", "Conditions of Reception", "D3",
     "Direct LLM reading of base verse/lexical text -- no special tag needed."),

    # D4 Relational (horizontal)
    ("T4.5.1", "D4.1.1", "D4", "D4.1", "Human Interface -- Boundaries and Scope", "D4",
     "role-T8 (Party-Human) co-occurrence in verse; direct LLM reading for the relational judgement."),
    ("T4.5.2", "D4.1.2", "D4", "D4.1", "Human Interface -- Boundaries and Scope", "D4",
     "role-T8 (Party-Human) co-occurrence in verse; direct LLM reading."),
    ("T4.5.3", "D4.1.3", "D4", "D4.1", "Human Interface -- Boundaries and Scope", "D4",
     "role-T8 (Party-Human) co-occurrence in verse; direct LLM reading."),

    # D5 Orientational (Godward / meaning) -- person's OWN stance, not something done to them
    ("T0.1.2a", "D5.1.1", "D5", "D5.1", "God-Relation Pattern", "D5",
     "role-T7 (Party-Divine) co-occurrence across the characteristic's verses (checked live: role-T7 present in 34.9% of M-coded verses)."),
    ("T0.1.2b", "D5.1.2", "D5", "D5.1", "God-Relation Pattern", "D5",
     "Aggregate reading over D5.1.1's per-verse findings."),
    ("T4.2.1", "D5.2.1", "D5", "D5.2", "Human-to-God Movement", "D5",
     "role-T7 (Party-Divine) co-occurrence in verse; direct LLM reading. Reclassified from the old T4 'interface' framing -- this is the person's own outward orientation, not an external cause acting on them (that's D7)."),
    ("T4.2.2", "D5.2.2", "D5", "D5.2", "Human-to-God Movement", "D5",
     "Direct LLM reading of base verse/lexical text."),
    ("T4.2.3", "D5.2.3", "D5", "D5.2", "Human-to-God Movement", "D5",
     "Direct LLM reading of base verse/lexical text."),
    ("T0.3.1", "D5.3.1", "D5", "D5.3", "Divine Image", "D5",
     "Depends on D5.1/D7.6's own findings; direct LLM reading, no new tag."),
    ("T0.3.2", "D5.3.2", "D5", "D5.3", "Divine Image", "D5",
     "Direct LLM reading across the characteristic's verses."),
    ("T0.3.3", "D5.3.3", "D5", "D5.3", "Divine Image", "D5",
     "Direct LLM reading across the characteristic's verses."),

    # F0 Faculty Reflection -- a DELIBERATE consolidation spanning D1/D2/D3/D4, per #1704 SS5
    # Decision 4 and #1701's resolution (T2.11 authored precisely to fold cognitive/affective/
    # volitional/relational into one end-of-read, subgroup-level reflection). Not a gap to split
    # apart -- kept as its own designed category, tagged with every dimension it deliberately spans.
    ("T2.11.1", "F0.1.1", "F0", "F0.1", "Faculty Engagement", "D1+D2+D3+D4",
     "Direct LLM reflection over the completed subgroup read -- deliberately consolidated, not "
     "per-dimension, per #1704 SS5 Decision 4 / #1701's resolution."),
    ("T2.11.2", "F0.1.2", "F0", "F0.1", "Faculty Engagement", "D1+D2+D3+D4",
     "Aggregate reading over F0.1.1's per-verse findings."),

    # D6 Spirit/soul locus
    ("T2.1.1", "D6.1.1", "D6", "D6.1", "Constitutional Level", "D6",
     "M47 cluster (spirit/soul/heart/mind, 38 strongs, checked live) plus direct LLM reading of the verse."),
    ("T2.1.2", "D6.1.2", "D6", "D6.1", "Constitutional Level", "D6",
     "Aggregate reading over D6.1.1's per-verse findings."),
    ("T2.7.1", "D6.2.1", "D6", "D6.2", "Body-Link Direction", "D6",
     "Depends on D6.1.1's audit; secondary D8 (embodied expression) signal. No dedicated body-part role tag needed beyond role-T14 if a named body part is the link."),
    ("T2.10.1", "D6.3.1", "D6", "D6.3", "Constitutional Movement", "D6",
     "M47 + direct LLM reading; secondary D7 signal where the movement's source is external (role-T7/T4/T9)."),

    # D7 Permeability -- the dimension this whole thread was actually circling
    ("T0.1.1", "D7.6.1", "D7", "D7.6", "God-Relation Directionality", "D7",
     "role-T7 (Party-Divine) co-occurrence in verse (34.9% of M-verses, checked live)."),
    ("T4.1.1", "D7.1.1", "D7", "D7.1", "Divine Extension", "D7",
     "role-T7 (Party-Divine) co-occurrence in verse."),
    ("T4.1.2", "D7.1.2", "D7", "D7.1", "Divine Extension", "D7",
     "role-T7 (Party-Divine) co-occurrence in verse; direct LLM reading."),
    ("T4.1.3", "D7.1.3", "D7", "D7.1", "Divine Extension", "D7",
     "role-T7 (Party-Divine) co-occurrence in verse; direct LLM reading."),
    ("T4.3.1", "D7.2.1", "D7", "D7.2", "Interpersonal Extension (Giving)", "D7",
     "role-T8 (Party-Human) co-occurrence in verse (33.8% of M-verses); secondary D4."),
    ("T4.3.2", "D7.2.2", "D7", "D7.2", "Interpersonal Extension (Giving)", "D7",
     "role-T8 (Party-Human) co-occurrence in verse; direct LLM reading."),
    ("T4.3.3", "D7.2.3", "D7", "D7.2", "Interpersonal Extension (Giving)", "D7",
     "role-T8 (Party-Human) co-occurrence in verse; direct LLM reading."),
    ("T4.4.1", "D7.3.1", "D7", "D7.3", "Interpersonal Uptake (Receiving)", "D7",
     "role-T8 (Party-Human) co-occurrence in verse; secondary D4."),
    ("T4.4.2", "D7.3.2", "D7", "D7.3", "Interpersonal Uptake (Receiving)", "D7",
     "role-T8 (Party-Human) co-occurrence in verse; direct LLM reading."),
    ("T4.4.3", "D7.3.3", "D7", "D7.3", "Interpersonal Uptake (Receiving)", "D7",
     "role-T8 (Party-Human) co-occurrence in verse; direct LLM reading."),
    ("T4.6.1", "D7.4.1", "D7", "D7.4", "Adversarial/Angelic Interface", "D7",
     "role-T4 (Adversarial) + role-T9 (Angelic) co-occurrence in verse (checked live: combined 1.9% of M-verses -- small, real)."),
    ("T4.6.2a", "D7.4.2a", "D7", "D7.4", "Adversarial/Angelic Interface", "D7",
     "role-T4 (Adversarial) co-occurrence in verse (7 strongs total, checked live)."),
    ("T4.6.2b", "D7.4.2b", "D7", "D7.4", "Adversarial/Angelic Interface", "D7",
     "Aggregate reading over D7.4.2a's findings."),
    ("T4.6.3a", "D7.4.3a", "D7", "D7.4", "Adversarial/Angelic Interface", "D7",
     "role-T9 (Angelic) co-occurrence in verse (13 strongs total, checked live)."),
    ("T4.6.3b", "D7.4.3b", "D7", "D7.4", "Adversarial/Angelic Interface", "D7",
     "Aggregate reading over D7.4.3a's findings."),
    ("T2.9.1", "D7.5.1", "D7", "D7.5", "Origin and Source", "D7",
     "role-T7/T8/T4/T9 co-occurrence in verse depending on stated source; secondary D9 where 'carried generationally' is the finding."),
    ("T2.9.2", "D7.5.2", "D7", "D7.5", "Origin and Source", "D7",
     "Aggregate reading over D7.5.1's findings."),

    # D10 Developmental/formational
    ("T0.2.1", "D10.1.1", "D10", "D10.1", "Purpose and Trajectory", "D10",
     "Direct LLM reading of base verse/lexical text -- no special tag needed."),
    ("T0.2.3", "D10.1.2", "D10", "D10.1", "Purpose and Trajectory", "D10",
     "Direct LLM reading across the characteristic's verses."),
    ("T1.5.1", "D10.2.1", "D10", "D10.2", "Immediate Response", "D10",
     "Direct LLM reading of base verse/lexical text."),
    ("T1.5.2", "D10.2.2", "D10", "D10.2", "Immediate Response", "D10",
     "Aggregate reading over D10.2.1's findings."),
    ("T1.6.1", "D10.3.1", "D10", "D10.3", "Sustained Effect", "D10",
     "Direct LLM reading of base verse/lexical text."),
    ("T1.6.3", "D10.3.2", "D10", "D10.3", "Sustained Effect", "D10",
     "Depends on D10.2's own findings; direct LLM reading."),
    ("T5.1.1", "D10.4.1", "D10", "D10.4", "Transformation", "D10",
     "Direct LLM reading of base verse/lexical text."),
    ("T5.1.2", "D10.4.2", "D10", "D10.4", "Transformation", "D10",
     "Aggregate reading over D10.4.1's findings."),
    ("T5.2.1", "D10.5.1", "D10", "D10.5", "Sequence of Inner States", "D10",
     "Direct LLM reading of base verse/lexical text."),
    ("T5.3.1", "D10.6.1", "D10", "D10.6", "Mechanism of Change", "D10",
     "Direct LLM reading of base verse/lexical text."),
    ("T5.3.2", "D10.6.2", "D10", "D10.6", "Mechanism of Change", "D10",
     "Aggregate reading over D10.6.1's findings."),

    # D11 Innate vs. acquired
    ("T0.2.2", "D11.1.1", "D11", "D11.1", "Created Design vs. Fallen Condition", "D11",
     "Direct LLM reading across the characteristic's verses -- the theological half of this dimension."),

    # M0 Lexical/Textual Evidence -- feeds the 12 dimensions, isn't one of them
    ("T1.1.1", "M0.1.1", "M0", "M0.1", "Name and Naming", "M0",
     "Direct LLM reading of the term's gloss/name."),
    ("T1.1.2", "M0.1.2", "M0", "M0.1", "Name and Naming", "M0",
     "strong_meaning_tree / strong_lexicon.lsj / strong_lexicon.mounce (the 3 meaning sources)."),
    ("T1.1.3", "M0.1.3", "M0", "M0.1", "Name and Naming", "M0",
     "Direct LLM reading of the term's gloss/name and its verse contexts."),
    ("T1.2.1", "M0.2.1", "M0", "M0.2", "Kind", "M0",
     "Direct LLM reading of the term's grammatical/semantic profile."),
    ("T1.2.2", "M0.2.2", "M0", "M0.2", "Kind", "M0",
     "Direct LLM reading; compound-term detection from the lexicon sources."),
    ("T1.3.1", "M0.3.1", "M0", "M0.3", "Boundary", "M0",
     "strong_meaning_tree / strong_lexicon.lsj / strong_lexicon.mounce -- structural-opposite vocabulary."),
    ("T1.3.2", "M0.3.2", "M0", "M0.3", "Boundary", "M0",
     "Direct LLM reading of the term's semantic edge."),
    ("T1.3.3", "M0.3.3", "M0", "M0.3", "Boundary", "M0",
     "Direct LLM reading of the term's semantic edge."),
    ("T1.4.1a", "M0.4.1", "M0", "M0.4", "Grammatical Form", "M0",
     "span.morph_code (already-parsed morphology) -- no new mechanism needed."),
    ("T7.1.1", "M0.5.1", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "strong_meaning_tree / strong_lexicon.lsj / strong_lexicon.mounce."),
    ("T7.1.2", "M0.5.2", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "span.morph_code + the 3 meaning sources."),
    ("T7.1.3", "M0.5.3", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "The 3 meaning sources, read as complementary evidence (per #1706 SS4A's own governing rule)."),
    ("T7.1.4", "M0.5.4", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "The 3 meaning sources."),
    ("T7.1.5", "M0.5.5", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "The 3 meaning sources."),
    ("T7.1.6", "M0.5.6", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "The 3 meaning sources."),
    ("T7.1.7", "M0.5.7", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "The 3 meaning sources."),
    ("T7.1.8", "M0.5.8", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "The 3 meaning sources, cross-referenced by testament (strong.language)."),
    ("T7.1.9", "M0.5.9", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "The 3 meaning sources, cross-referenced by testament."),
    ("T7.1.10", "M0.5.10", "M0", "M0.5", "Lexical and Semantic Analysis", "M0",
     "Aggregate reading over M0.5.1-9's findings."),
    ("T7.2.1", "M0.6.1", "M0", "M0.6", "Verse and Literary Interpretation", "M0",
     "span.strong_variant ordering (sentence role) + role-T6 (Connective) tag where present."),
    ("T7.2.3", "M0.6.2", "M0", "M0.6", "Verse and Literary Interpretation", "M0",
     "Direct LLM reading of the verse's argument structure."),
    ("T7.2.5", "M0.6.3", "M0", "M0.6", "Verse and Literary Interpretation", "M0",
     "Direct LLM reading across the characteristic's verses."),
    ("T7.2.6", "M0.6.4", "M0", "M0.6", "Verse and Literary Interpretation", "M0",
     "Depends on M0.6.3's own finding; direct LLM reading."),

    # X0 Cross-Characteristic Synthesis -- a synergy-stage concern, not per-characteristic
    ("T6.1.1", "X0.1.1", "X0", "X0.1", "Co-occurrence", "X0",
     "Cross-cluster verse-overlap query at the synergy stage, not per-characteristic base data."),
    ("T6.1.2", "X0.1.2", "X0", "X0.1", "Co-occurrence", "X0",
     "Depends on X0.1.1's own finding; synergy-stage reading."),
    ("T6.2.1", "X0.2.1", "X0", "X0.2", "Sequential Relationships", "X0",
     "Cross-cluster verse-sequence query at the synergy stage."),
    ("T6.2.2", "X0.2.2", "X0", "X0.2", "Sequential Relationships", "X0",
     "Depends on X0.2.1's own finding; synergy-stage reading."),
    ("T6.3.1", "X0.3.1", "X0", "X0.3", "Causal and Constitutive Relationships", "X0",
     "Cross-cluster reading at the synergy stage."),
    ("T6.3.2", "X0.3.2", "X0", "X0.3", "Causal and Constitutive Relationships", "X0",
     "Cross-cluster reading at the synergy stage."),
    ("T6.3.3", "X0.3.3", "X0", "X0.3", "Causal and Constitutive Relationships", "X0",
     "Cross-cluster reading at the synergy stage."),
    ("T6.4.1", "X0.4.1", "X0", "X0.4", "Vocabulary and Root Sharing", "X0",
     "Cross-cluster lexical comparison (the 3 meaning sources, compared across clusters) at the synergy stage."),
    ("T6.4.2", "X0.4.2", "X0", "X0.4", "Vocabulary and Root Sharing", "X0",
     "Cross-cluster lexical comparison at the synergy stage."),
    ("T6.4.3", "X0.4.3", "X0", "X0.4", "Vocabulary and Root Sharing", "X0",
     "Depends on X0.4.1/4.2's own findings; synergy-stage reading."),
    ("T6.5.1", "X0.5.1", "X0", "X0.5", "Distinctions", "X0",
     "Cross-cluster comparative reading at the synergy stage."),
    ("T6.5.2", "X0.5.2", "X0", "X0.5", "Distinctions", "X0",
     "Cross-cluster comparative reading at the synergy stage."),
    ("T6.5.3", "X0.5.3", "X0", "X0.5", "Distinctions", "X0",
     "Depends on X0.5.1/5.2's own findings; synergy-stage reading."),
]

# New questions authored for confirmed zero-coverage dimensions, per #1712 SS6/SS7.
NEW_QUESTIONS: list[dict] = [
    dict(question_code="D1.1.1", tier="D1", component_code="D1.1", component_title="Cognitive Engagement",
         dimension="D1",
         question_text="In this verse, what does the characteristic reveal about the person's "
                        "perception, belief, or judgement -- what do they perceive, believe true, "
                        "or conclude? Record it, or record none.",
         data_mechanism="Direct LLM reading of base verse/lexical text -- no special tag needed."),
    dict(question_code="D1.1.2", tier="D1", component_code="D1.1", component_title="Cognitive Engagement",
         dimension="D1",
         question_text="Across the verses, does the characteristic consistently precede a "
                        "judgement or belief, follow one, or both?",
         data_mechanism="Aggregate reading over D1.1.1's per-verse findings."),
    dict(question_code="D2.1.1", tier="D2", component_code="D2.1", component_title="Affective Quality",
         dimension="D2",
         question_text="In this verse, what is the felt quality of the characteristic -- is it "
                        "shown as a settled disposition or a transient response, and what "
                        "emotion-language or bodily-feeling language, if any, accompanies it? "
                        "Record it, or record none.",
         data_mechanism="Direct LLM reading of base verse/lexical text -- no special tag needed."),
    dict(question_code="D2.1.2", tier="D2", component_code="D2.1", component_title="Affective Quality",
         dimension="D2",
         question_text="Across the verses, is the felt quality consistent, or does it vary by context?",
         data_mechanism="Aggregate reading over D2.1.1's per-verse findings."),
    dict(question_code="D7.7.1", tier="D7", component_code="D7.7", component_title="Operation-Anchored Party Relation",
         dimension="D7",
         question_text="Where an action/operation word (role-T3) appears in this verse alongside "
                        "the characteristic, what is that operation's relation to the parties "
                        "present -- who initiates it and toward whom or what is it directed? "
                        "Record none if no such operation word is present.",
         data_mechanism="role-T3 (Operations) co-occurrence with role-T7/T8/T4/T9 (party tags) in "
                        "verse -- checked live: role-T3 present in 85.8% of M-coded verses, the "
                        "single densest role signal in the corpus, previously anchored to no "
                        "catalogue question at all."),
    dict(question_code="D9.1.1", tier="D9", component_code="D9.1", component_title="Physiological/Neural Substrate",
         dimension="D9",
         question_text="Per the cluster's science extract, what does neuroscience or physiology "
                        "show about the mechanism underlying this characteristic, and does the "
                        "verse evidence engage or diverge from that mechanism?",
         data_mechanism="Workflow/Sciences/science_files/wa-m{NN}-{name}-scienceextract-*.md "
                        "(per-cluster file, checked live: 45 of 85 clusters covered) -- the "
                        "already-designed 'science pass' reference shelf (programme prose Ch.2), "
                        "wired in as this question's data input."),
    dict(question_code="D9.2.1", tier="D9", component_code="D9.2", component_title="Generational Transmission",
         dimension="D9",
         question_text="Per the cluster's science extract, does the scientific literature show "
                        "the characteristic (or its pattern) transmitted generationally, and does "
                        "the verse evidence show anything comparable (covenant, inheritance, "
                        "generational language)?",
         data_mechanism="Per-cluster science-extract file; cross-reference with D7.5 (Origin and Source)."),
    dict(question_code="D11.2.1", tier="D11", component_code="D11.2", component_title="Innate Endowment",
         dimension="D11",
         question_text="Per the cluster's science extract, does genetics/evolutionary biology "
                        "treat this characteristic (or its precursor) as part of innate human "
                        "endowment, and how does that relate to D11.1's created-design/"
                        "fallen-condition finding?",
         data_mechanism="Per-cluster science-extract file; cross-reference with D11.1."),
    dict(question_code="D12.1.1", tier="D12", component_code="D12.1", component_title="Social/Behavioural Manifestation",
         dimension="D12",
         question_text="Per the cluster's science extract, what does behavioural science show "
                        "about how the characteristic expresses socially -- cooperatively or "
                        "competitively -- and does the verse evidence show a comparable social "
                        "pattern?",
         data_mechanism="Per-cluster science-extract file."),
]

# Superseded by the new dedicated D9/D11/D12 questions above -- named a real mechanism instead of
# asking the LLM to guess a framework.
RETIRE_CODES = ["T7.3.1", "T7.3.2", "T7.3.3", "T7.3.4"]
RETIRE_NOTE = ("Superseded 2026-09-17, escalation #1712: replaced by D9.1.1/D9.2.1 (physiological/"
               "generational), D11.2.1 (innate endowment), D12.1.1 (social/behavioural) -- each "
               "naming a real data mechanism (the per-cluster science-extract file) instead of "
               "asking the LLM to pick a framework generically.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        already = cur.execute(
            "SELECT COUNT(*) c FROM wa_obs_question_catalogue WHERE catalogue_version=?",
            (CATALOGUE_VERSION,)).fetchone()["c"]
        if already:
            report.append(f"already applied ({already} rows carry {CATALOGUE_VERSION!r}) -- no-op")
            print("\n".join(report))
            conn.rollback()
            return 0

        cols = {r[1] for r in cur.execute("PRAGMA table_info(wa_obs_question_catalogue)")}
        if "dimension" not in cols:
            cur.execute("ALTER TABLE wa_obs_question_catalogue ADD COLUMN dimension TEXT")
            report.append("column 'dimension' added")
        if "data_mechanism" not in cols:
            cur.execute("ALTER TABLE wa_obs_question_catalogue ADD COLUMN data_mechanism TEXT")
            report.append("column 'data_mechanism' added")

        for old_code, new_code, tier, comp_code, comp_title, dimension, mechanism in REMAP:
            cur.execute(
                "UPDATE wa_obs_question_catalogue SET question_code=?, tier=?, component_code=?, "
                "component_title=?, dimension=?, data_mechanism=?, catalogue_version=? "
                "WHERE question_code=? AND deleted=0",
                (new_code, tier, comp_code, comp_title, dimension, mechanism, CATALOGUE_VERSION,
                 old_code))
            if cur.rowcount != 1:
                raise RuntimeError(f"remap {old_code} -> {new_code}: expected 1 row, got {cur.rowcount}")
        report.append(f"{len(REMAP)} existing questions renumbered + dimension/mechanism captured")

        for q in NEW_QUESTIONS:
            cur.execute(
                "INSERT INTO wa_obs_question_catalogue (question_code, section, question_text, "
                "scope, status, deleted, date_added, catalogue_version, tier, component_code, "
                "component_title, dimension, data_mechanism, source) VALUES "
                "(?,?,?,?,?,0,date('now'),?,?,?,?,?,?,?)",
                (q["question_code"], q["tier"], q["question_text"], "Characteristic (HIB behaviour)",
                 "active", CATALOGUE_VERSION, q["tier"], q["component_code"], q["component_title"],
                 q["dimension"], q["data_mechanism"], "escalation-1712-dimension-realign-20260917"))
        report.append(f"{len(NEW_QUESTIONS)} new questions authored for confirmed zero-coverage dimensions")

        for code in RETIRE_CODES:
            cur.execute(
                "UPDATE wa_obs_question_catalogue SET deleted=1, review_note=?, "
                "catalogue_version=? WHERE question_code=?",
                (RETIRE_NOTE, CATALOGUE_VERSION, code))
            if cur.rowcount != 1:
                raise RuntimeError(f"retire {code}: expected 1 row, got {cur.rowcount}")
        report.append(f"{len(RETIRE_CODES)} questions retired (superseded by dedicated science-dimension questions)")

        for col in ("source_word", "source_registry_no"):
            try:
                cur.execute(f"ALTER TABLE wa_obs_question_catalogue DROP COLUMN {col}")
                report.append(f"column '{col}' dropped")
            except sqlite3.OperationalError as e:
                report.append(f"column '{col}' NOT dropped ({e}) -- SQLite version may not support DROP COLUMN")

        live = cur.execute("SELECT COUNT(*) c FROM wa_obs_question_catalogue WHERE deleted=0").fetchone()["c"]
        undimensioned = cur.execute(
            "SELECT COUNT(*) c FROM wa_obs_question_catalogue WHERE deleted=0 AND (dimension IS NULL OR dimension='')"
        ).fetchone()["c"]
        report.append(f"post-migration: {live} live questions, {undimensioned} without a dimension "
                      f"(expect 0)")
        if undimensioned:
            raise RuntimeError(f"{undimensioned} live questions have no dimension -- migration incomplete")

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
