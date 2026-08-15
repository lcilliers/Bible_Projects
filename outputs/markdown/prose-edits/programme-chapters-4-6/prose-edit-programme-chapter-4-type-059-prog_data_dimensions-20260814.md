# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 28 -->
<!-- PROSE_SECTION_TYPE: prog_data_dimensions -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Dimensions — the analytical grouping mechanism -->
<!-- PROSE_SORT_ORDER: 28 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch4-obslog-v1_0-20260423.md -->

## Dimensions — the analytical grouping mechanism

Dimensions are the programme's analytical grouping mechanism. A dimension is a named inner-being characteristic that a group of verses engages; it is assigned to a `verse_context_group` as the outcome of the Dimension Review analytical pass. Groups with the same dimension engage the same kind of inner-being content across different terms and different registries; dimensions are the axis along which the programme's analytical structure is organised.

The governing principle of the dimensional work is that dimensions always follow the verse. A group is read for what its anchor verses and context description reveal. A dimension is assigned only when it genuinely describes what the group shows. Where no existing dimension in the working vocabulary captures the group, the group does not receive an ill-fitting label; the mismatch is recorded as a finding, and the vocabulary is extended — by researcher decision — to account for what the data shows. Dimensions are not applied to the data. They emerge from it.

`wa_dimension_index` holds the dimensional record — three thousand five hundred rows, one per (group × owning registry). Each row carries the group it indexes (`verse_context_group_id`), the registry that owns the group's term (`owning_registry_no`), the dimension assigned (`dimension`), the primary subject of the characteristic (`dominant_subject`), counts of anchor, related, and set-aside verses in the group (`anchor_count`, `related_count`, `set_aside_count`, `total_verse_count`), the confidence level of the current assignment (`dimension_confidence`), a manual-override flag for researcher-confirmed assignments (`manual_override`), and the administrative tranche within which the registry was processed (`cluster_assignment`). The notes field carries the analytical reasoning that attaches to the assignment; `last_modified` tracks when it was last changed; `delete_flagged` carries the soft-delete state.

The working dimension vocabulary is eleven labels, derived from the data across the programme's Dimension Review passes: Emotion — Positive; Emotion — Negative; Cognition; Volition; Moral Character; Relational Disposition; Vitality / Existence; Transformation; Agency / Power; Dependence / Creatureliness; Divine-Human Correspondence. The list is the current working set, not a final taxonomy: the eleventh dimension was added from C18 data when a group appeared whose characteristic crossed the boundary between divine and human inner-being content that no earlier dimension adequately captured. The vocabulary is canonical in `wa_vocab_set.DIMENSION_LABEL` and its allowed values in `wa_vocab_member`; the applicator validator rejects any dimension patch whose label is not in the canonical list. Extension of the vocabulary is a researcher decision implemented through a vocabulary migration.

`dominant_subject` names the primary bearer of the characteristic in the group's verses. The controlled vocabulary is five values: `GOD`, `HUMAN`, `OTHER_HUMAN`, `UNSEEN`, and `NONE` (for groups that are purely circumstantial or where no dominant subject is identifiable). NULL is not valid for a group after Dimension Review is complete; the field is a required output of the dimensional pass.

`dimension_confidence` carries the refinement stage of the assignment. Automated keyword matching produces an initial hypothesis (`KEYWORD_WEAK` or `KEYWORD_STRONG`). The Claude AI reviewer reads the group and its anchor verses, confirms or revises the assignment, and moves the row to `CLAUDE_AI` confidence. Researcher review moves a confirmed assignment to `RESEARCHER_CONFIRMED` and sets `manual_override = 1`, which locks the assignment against automated overwrite on re-runs.

`wa_dim_review_cluster_log` carries the completion record for the Dimension Review at the cluster level — five rows at present, one per cluster that has completed the pass. Each row records the instruction version under which the review ran, the registry count, the group count, the anchored count, and the completion date.

Dimensions are distinct from the C01–C22 values in the registry's `cluster_assignment` field described in the sub-section on the registry. The C-values are the run-batch tranches the programme uses to schedule Verse Context processing; they are administrative and carry no analytical claim about the words they group. Dimensions are analytical: groups that share a dimension engage the same inner-being characteristic in the evidence, and two words whose groups sit under the same dimension are analytically related by what the verses show. The programme's answer to "what inner-being characteristics does Scripture's vocabulary engage" is carried in the dimensional record, not in the cluster assignments.

A per-word summary of dimensional profile is held separately in `wa_session_b_dimensions`, produced as a Session B output. Each row carries four dimension pairs for a registry — relational environment, spirit/soul/body, inner operations, and being — with a value and a note against each. This is the distilled dimensional summary of a word, produced once the per-group dimensional work has completed; it is the per-word form of the dimensional record that the group-level index holds in detail.

The quality of the dimensional record depends on the quality of the layers above it. Sound anchor verses are the evidence against which dimensions are read; accurate group descriptions are the analytical statements the dimensions confirm or refine. Where anchor or group quality is deficient, the dimensional pass stops and issues a return instruction to the Verse Context pipeline rather than assigning a dimension to a group it cannot read with confidence. The analytical grouping this architecture produces is the foundation for the synthesis work described in the final two sub-sections.

---
