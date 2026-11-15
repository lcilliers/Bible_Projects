# #2463 Readiness audit: can the layered reading produce observations for every aspect of layer 1 and layer 2? (v1, 2026-11-15)

Status: read-only audit, Developer Mode session 58e035fd. Nothing was written to config, tables or code. Statements marked (inferential) are my reading (B:4). Sources are named per finding (B:34).

The outcome asked for: an observation in the database for every aspect of layer 1 (step 1 groups, step 2 Strong's enrichment) and layer 2 (step 1 pairings, qualifiers, entities, direction, interchangeability, double meaning) of a collection. The researcher's definition of the layers is #2463 comment v16, verbatim, with the answers in v18 to v22.

## 1. Verdict

Not everything is in place. The data foundation and the writing tools exist; the rules, the layer routine, the observation kinds and stage, the completeness check, and the layer 1 grouping itself do not.

## 2. In place (checked)

| # | Item | Evidence |
|---|---|---|
| P1 | Evidence report with layer 1 and layer 2 material for `thought`: sections 2.1, 2.2, 3, 3a; sheets Links, Members, Strongs codes, Meaning trees, Occurrences, Verse view, Pairings, Pairing summary, Verse observations | `_analytics/surfaces/exports/collection-evidence-thought-v3-20261114.md` and `.xlsx` exist; `cfg_step collection.evidence`; `cfg_setting collection.evidence_pairs`; BUILD 528 (19 test cases) |
| P2 | Index of surfaces and subgroups: `collection_subgroup`, `collection_subgroup_surface`, steps `collection.index`, `collection.subgroup`, `collection.index_check`, enums, write grants | `cfg_step` ordinals 11 to 13; live rows: 3,437 index rows over 169 collections; BUILD 529 (16 test cases) |
| P3 | Node rules (B:130) and observation rules (B:131): a node per occurrence with `verse_lexical_id`, surface, Strong's, role, collection | `cfg_behaviour_rule` 130, 131 (active) |
| P4 | A loader that writes observations with nodes in one checked transaction, whole-or-none, with a change log | `Draft-Apply.ps1` Check and Apply, rules DA-01 to DA-04 (`cfg_method_rule` 233 to 236) |
| P5 | Node roles: characteristic, qualifier (relevant); object, relational_target, enactment (bears on); standalone (recognised) | `cfg_setting reading.node_roles` |

## 3. Gaps

| # | Gap | Evidence | What it blocks |
|---|---|---|---|
| G1 | **The layers are in no rule or setting.** Layer 1 step 1, step 2 and layer 2 step 1, with their outputs, exist only as #2463 comments and working papers. A search of every `cfg_*` table for "layer 1" and "layer 2" finds only the old verse_lexical layers (`lexical.enrich`, method rules 52, 55, 64, 69, `report.lexical_exceptions`) and the new index tables. No behaviour rule after id 131; B:127 to B:131 do not name them. The capture of the answers as rules (B:31) has not started. | `cfg_behaviour_rule` newest id 131; comparison v4 section 6 item 5 | "What is expected" is not defined where the app can enforce it; breaches `governance.rules_must_be_config_driven`. |
| G2 | **B:119 and B:120 still active and wrong for collections**: both name the subgroup and cluster as the unit; the researcher said clusters and subgroups are no longer the starting point or a readying unit. Replacement wording (draft v2) is not written to config; the lexical-and-claims-separate rule and the blur allowance have no home; RG-09's last sentence ("claims work") and RW-02 (lists subgroup and cluster among node contents) contradict the new split and B:130. | `2463-scope-rules-b119-b120-draft-v2-20261114.md` sections 5 and 6; four decisions open | Scope of a layer reading is still defined by subgroup in config and in `versescope.py`. |
| G3 | **No routine writes layer observations.** `collection.subgroup` places surfaces and writes a `surface_event` only; no step turns a group, a Strong's enrichment or a pairing finding into an `ib_observation` with nodes. Existing writers: `Engagement.ps1` (per-verse role assessment, stage `engagement`, not a group or pairing) and `Draft-Apply.ps1` (could load them, see G4). `Reading.ps1 Open` still takes a subgroup (USER-GUIDE line 440), and #2448 (reading by collections) is on hold. | `cfg_step` list for work package `collection-build`; Engagement.ps1 header; Draft-Apply.ps1 header | Layer observations cannot be produced by a defined, repeatable procedure. |
| G4 | **Kinds and stage do not fit.** The eight finding kinds (face, qualification, party, statement, link, use, term, silence) have none for a group of surfaces, a Strong's definition or enrichment, or a pairing. `ib_observation.stage` has no layer value. Draft-Apply writes new observations as stage `prior-reread`, status `draft` (DA-04), so a layer observation would be filed as a prior re-read; its `enrich` action changes text only (DA-01). Whether Draft-Apply validates a kind against the eight is not verified. | `cfg_setting reading.observation_parts`, `reading.observation_items`; `cfg_enum ib_observation.stage`; `draftapply.py:31,194` | No way to tell a layer 1 group observation from a re-read, so coverage cannot be counted by stage or kind. |
| G5 | **No completeness check for the outcome.** IndexCheck tests index integrity; Node-Check tests nodes against B:130; `reading.surface_requirements` tests per-surface coverage. Nothing tests: every non-isolated subgroup has a definition observation; every group has a Strong's enrichment observation whose nodes carry its codes; every pairing type, qualifier, entity and group-to-group relation in the Pairings sheet has an observation; every isolated word has its recorded reason. | `cfg_step collection.index_check` description; `reading.surface_requirements` | "Every aspect has an observation" cannot be proved, which B:2 requires. |
| G6 | **Layer 1 step 1 is not done for any collection.** `thought` has 0 subgroups and its 33 surfaces are all `unplaced`; no collection has a subgroup. So layer 1 step 2 and the group-level part of layer 2 have nothing to run on. | `collection_subgroup` count 0; `collection_subgroup_surface` for collection 56: 33 unplaced | Everything downstream of the grouping. |
| G7 | **Layer 2 data lacks fields the researcher listed.** The Pairings sheet gives side (before or after), distance, band and type; there is no direction-of-travel field, no group-to-group interchangeability measure and no double-meaning marker beyond the empty `reading` column (inferential: these are reading judgements, but the report has nowhere prepared to hold them). Pairing summary at subgroup level is empty until G6 is done. | `collection.evidence_pairs` setting; USER-GUIDE line 1012 | Direction-of-travel and interchangeability observations have no prepared base data. |
| G8 | **The group reaches the node by join only.** The researcher wanted the groups on the nodes so they are discoverable (v18 point d); the design added no node column and reaches a subgroup by `collection_id`, surface and Strong's code. It works only once the surface is placed, and the join key for a split surface is the Strong's code. The researcher approved "the group on the node by join" in #2503 v1; whether that meets point d once layer observations exist is for the researcher to confirm. | `USER-GUIDE.md` line 1013; #2503 v1 | Discovery of a group's observations through its nodes. |
| G9 | **The lexical precondition is not checked.** The researcher says lexical observations must be complete before a collection's layer work and the two must not run together. No check or gate states that a collection's lexical observations are complete; `Lexical-Readiness.ps1` covers the verse_lexical build, not observations. Today `thought` has 514 live nodes on four stages (observations: engagement 13, prior-capture 169, strand-reading 35, verse-reading 3) and 106 of those nodes have no role. The figure of 258 of 394 occurrences without a live node (2026-11-13) was not re-measured. | `ib_node` and `ib_observation` for collection 56; `cfg_method_rule` 69 | Starting layers on an incomplete lexical base, the failure the researcher named. |
| G10 | **Concept level undecided.** `concept` rows were left alone; `collection.concept_id` is empty on 169 collections; the researcher's groups are held only in the new index. Analysis at concept level depends on the groups (G6). | #2463 v33 to v41 | Analysis above the group. |
| G11 | **Housekeeping.** 274 member links carry a stale `shared` flag (IndexCheck). The escalation context check lists `outputs/escalation/2463-concept-rows-destroy-and-reform-plan-v1-20261114.md` as missing; it is not in the folder (a dangling reference after the researcher's change of decision). | `collection-index-check-v1-20261114.md`; context check for #2463 | Noise in coverage reports. |

## 4. What each layer step needs before it can yield its observations

| Layer step | Needs | Gaps open |
|---|---|---|
| 1.1 groups as observations, surfaces as nodes | groups made and surfaces placed; a kind and stage for it; a writer; a rule that each group and each isolated word has one | G1, G3, G4, G5, G6 |
| 1.2 Strong's enrichment as observations, codes as nodes | 1.1 done; a kind for definition; nodes on the occurrences carrying the group's codes | G1, G3, G4, G5, G6, G8 |
| 2.1 pairings, qualifiers, entities, direction as observations | 1.1 done; report fields for direction and group relations; a kind for a pairing; the lexical base complete | G1, G3, G4, G5, G7, G9 |

## 5. For the researcher's decision (B:105: nothing designed here)

1. Which of G1 to G5 to take first. Recommendation (inferential): G1 and G2 first, as one config change with B:31, because the routine and the check (G3, G5) are written against them.
2. G6 is the researcher's work (the groups), done with `Collection-Build.ps1 -Action Subgroup`.
3. G4, G5 and G7 each need a design that goes to the researcher as decision_required before any build.

## 6. Not checked

Whether `draftapply.py` accepts a kind outside the eight; the content of `Reading.ps1` steps beyond the USER-GUIDE description; the text of #2448 (on hold, not opened); today's count of `thought` occurrences without a node.
