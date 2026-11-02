# Concepts retry from the surface subgroups: plan for approval (#2354, v1, 2026-11-01)

Researcher, chat 2026-11-01, verbatim: "i want to retry the compilation of the concepts from the surface sub groups.    more attention to be given to differentiate : behaviours,  inner being states (such as sin, righteousness) , other beings."

Nothing has been built or written to iba/app/db/iba.db. Counts below were read from the live tables today.

## What I read first (cfg_table.use, cfg_column.use)
- `surface_subgroup` (13,462 rows, all `provisional`): the subgroup each (cluster, strong, surface) pair belongs to; `reason` says why; `two_sense` flags a pair settled later per occurrence. Provisional, never a finding.
- `cluster_subgroup` (572 live and flagged rows): `kind` is group 406, anomaly 81, not_this_sense 80, qualifier 5; `label` and `core_description` define the sense.
- The v1 concepts (iba/docs/concept-mapping-spec-v1-20261031.json, outputs/concept-mapping/concepts-v1-20261031.md) were grouped mainly by subgroup label and description, into 14 domains and 101 concepts. They do not separate what a word is: an act, a state, or a being.

## Understanding
Redo the compilation of concepts, starting from the surface subgroups, and make three kinds explicit so they are never mixed in one concept:
1. **Behaviours**: what the inner being does (acts, responses, speech, choices).
2. **Inner being states**: what it is or is in (sin, righteousness, and similar conditions).
3. **Other beings**: God, angels, Satan and demons, other people, spirits.

This is the first step of #2354; the narrative redraft follows after you approve the concepts.

## Proposed approach (draft; for your decision)
1. **Classify every live group and qualifier subgroup (411) as behaviour, inner-being state, other being, or "none of these" (outward things, for example wealth or kingship).** The call is made from the subgroup's `core_description` and the `surface` and `reason` of its pairs, one reading per subgroup, with the evidence quoted. A subgroup that is two kinds is listed, not forced.
2. **Form concepts inside each kind**, not across them, from the subgroups of that kind. The domains then follow the three kinds, with your story's movements (II behaviours, III beings, IV states) as the frame.
3. **Output as a review file only** (`outputs/concept-mapping/concepts-v2-<date>.md`) with, per concept, its subgroups, its kind, and the open calls. All of it is marked inferential (B:4). Nothing is written to `concept_domain`, `concept` or `concept_subgroup` until you approve the file; the write is then a separate step.
4. Anomaly and not_this_sense subgroups (161) are left out of the first pass and listed with the reason, unless you want them included.

## Decisions I need from you
- **A. Method:** classify all 411 subgroups myself in one pass (recommended; cost: one long run, tokens only), or run the local LLM pilot. The local LLM work is on hold at your instruction, so I take it as not in use.
- **B. Spirit:** the spirit strongs (cluster M47) are not yet placed. Is spirit a being, a state, or both? I will list those subgroups for you rather than choose.
- **C. Existing tables:** replace the current 14 domains and 101 concepts on approval (old rows soft-deleted via `deleted`), or keep them beside the new set until you compare?
- **D. "None of these" subgroups:** keep them as a fourth group, or leave them out of the concepts?

## Not claimed
No concept is a finding. The classification of a subgroup is my reading of recorded text, not a verse-level reading; where the text is thin it is flagged.
