# #2367 draft glossary entries for the surface-cycle terms

Drafted 2026-11-06 from the recorded meaning in `cfg_table.use` and the active prompts `base.word` v2 and `group.word` v3 (`cfg_ai_prompt`). Nothing is applied. Correct the text below (or tell me what to change); then the patch is applied with `Prose.ps1 -Step ApplyPatch` (dry run first).

Patch: `archive/patches/wa-prose-glossary-surface-terms-v1-20261106.json`

## base

[DEFINITION] A base is the English word a surface text is an inflected or derived form of, when the two share the same root meaning (sought: seek; wonderful: wonder). It is itself a surface text: a base is a row of the same table as the surface that points to it, and a word with no base is its own base. A base is where surfaces of one root meaning are gathered before they are placed in collections.

[BACKGROUND] Named 'base form' in the AI question. Held in surface_term (base_id), with the evidence in surface_derivation. Everything a model decided about a base is inferential until its state is confirmed.

Your correction: 

## inflection

[DEFINITION] The relation of a surface to its base when only the grammatical ending changes: tense, plural, participle, comparative, including irregular forms (wept: weep; grew: grow).

[BACKGROUND] One of three allowed base relations (inflection, derivation, none). The relation 'none' is used when the word has no base, is only an opposite or look-alike of a candidate base, or its meaning has moved away from it.

Your correction: 

## derivation

[DEFINITION] The relation of a surface to its base when a different word form is made with a suffix or prefix, such as a noun from a verb or an adjective, and the core meaning stays the same (wonderful: wonder; strife: strive).

[BACKGROUND] Contrast inflection, where only the grammatical ending changes. A derived form with a changed meaning is not a derivation here (undoing is not undo).

Your correction: 

## surface group

[DEFINITION] The first sorting of a surface text by what it names, as the ESV uses it: behaviour (something a person does or undergoes, an act, feeling, thought, speech or choice), inner_being_state (a standing condition or characteristic of a person or of the inner being: righteous, proud, humble, weak), being (a thing that exists: a human, a plant or animal, God in all forms, an unseen power, or a part of any of these), or other (everything else, and any word that definitely belongs in none of the other three).

[BACKGROUND] Held in surface_term.surface_group and judged by a model, so it is inferential until confirmed. A word that says what an entity does, is like or has undergone is not a being, even when it describes one. The surface group is not the cluster or the concept.

Your correction: 

## subgroup

[DEFINITION] A subdivision of an M-code cluster that carries a label and a core description of which sense of the cluster theme it covers (for example M01-A). A (Strong's code, surface) pair is allocated to a subgroup at the clustering stage; the allocation is provisional, never a finding, and a pair with two senses is settled per occurrence in the claims step.

[BACKGROUND] Held in cluster_subgroup; the allocation of a pair is surface_subgroup. Each live subgroup belongs to exactly one live concept (concept_subgroup).

Your correction: 

## collection

[DEFINITION] A set of bases of like meaning gathered round one core word and named for it. Each member is placed by a tier: core (the seed), synonym, or opposite (confirmed by two judges); a possible opposite and an associated word are listed apart for the researcher and are not members, and a word the model listed but the judge would not bind is set aside.

[BACKGROUND] Held in collection and collection_link. A collection is the finer step before a concept: it is rolled up into a concept later. Provisional and inferential until its status is confirmed.

Your correction: 

## concept

[DEFINITION] A sub-chapter of a concept domain, named for what its subgroups share. The concept holds subgroups of clusters, and a live subgroup is in exactly one live concept; it is the link from the base data to the narrative.

[BACKGROUND] Held in concept and concept_subgroup. The collections of bases will be rolled up into concepts (collection.concept_id), which will replace the subgroup membership. A first grouping, not a finding.

Your correction: 

## concept domain

[DEFINITION] A domain of the concept grouping, the basis the researcher ruled for the narrative: domains are chapters and concepts are sub-chapters (chat 2026-10-31).

[BACKGROUND] Held in concept_domain. Loaded from the v1 specification iba/docs/concept-mapping-spec-v1-20261031.json by grouping the existing subgroups; a first grouping, not a finding.

Your correction: 

## Points for your ruling

1. **Group name mismatch.** The active prompt `group.word` v3 names the third group `entity`; the allowed values (`cfg_enum surface_term.surface_group`) and the 716 stored rows say `being`, and no row holds `entity`. I wrote the entry with `being`. The mismatch is raised as its own item.
2. **`role`** stays in the contentious glossary, awaiting you; not touched.
3. All eight entries are `draft`, like the 78 other draft entries; none is approved.
