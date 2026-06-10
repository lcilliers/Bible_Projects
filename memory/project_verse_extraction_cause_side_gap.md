---
name: project_verse_extraction_cause_side_gap
description: FINDING (2026-06-10) prep for catalogue session — the verse read captures the EFFECT side but not the CAUSE side. Missing structured fields = eliciting_cause (why), object/target (at/of what), valence (righteous vs sinful = the exception axis), experiencer_type (who), and a TYPED inter-characteristic relationship A-rel[effect]->B (the synergy substrate; co-occurrence alone is only a candidate-finder). Most are Type B = already in the meaning prose (M02: cause 39% / object 48% / inter-term 15%), 0% structured -> recoverable by a cheap extraction pass over the 8367 existing meanings, no Bible re-read. Type A residue (scenario_type, intensity, implicit links) needs an augmented read. Doc wa-verse-extraction-gaps-v1-20260610.
metadata:
  type: project
---

**Governing principle (researcher, 2026-06-10):** evidence not captured at the verse cannot be recovered in
analysis — "it'll be dealt with in synthesis" is empty if the data was never teased out. The synergy phase
will use the tier signals as INDICATORS but must read the meaning (and sometimes the surrounding context) to
answer why-did-it-happen / how-does-it-differ / what-are-the-exceptions.

**What IS captured (solid, validated by VE-by-cluster):** identity/constitution/faculty + the EFFECT
(`produces_effect` ~90-100%). Faculty cleanly separates clusters (Wisdom 94% cognition · Fear 91% affect ·
Anger 74% affect+63% moral-eval). See [[project_cc_generation_mode]] for the VE field set / v_l2_tier.

**The systematic blind spot = CAUSATION + DIFFERENTIATION.** Add as new Layer-A fields (extending the
restructured catalogue VE-15/16/17): `eliciting_cause` · `object`(+type) · `valence`(righteous/sinful/commanded/
forbidden) · `experiencer_type` · `typed_relationship`(causes/produces/intensifies/opposes/accompanies/
responds-to/precedes/constitutes + effect). These feed SYNTH T5.3/T6.2/T6.3/T0.2.2/T1.7/T4.x. Connects to
[[feedback_ontology_typed_relationships]] (the typed A->B with differential effect is the prize) and
[[project_cross_cluster_three_link_classes]].

**Recommended sequence:** (1) structured extraction pass over existing 8367 meanings to backfill the Type-B
fields (cheap, no re-read); (2) augment the live verse read going forward for the Type-A residue. Decide in the
catalogue session (the [[feedback_catalogue_refit_four_principles]] D-decisions). We are largely on the right
track — this is an additive fix, not a redo.
