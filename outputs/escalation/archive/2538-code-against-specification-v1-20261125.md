# #2538 code against the specification (v1, 2026-11-25)

Read by Claude in this session: lib/layerreading.py (load, derive, expected_nodes, wordnet_control, pull, open_step gates),
lib/collectiongroup.py (pull), lib/layerinner.py (function and query list only), the layer.reading config. NOT read or tested: the
record/check validation rules in full, layerinner.derive/pull/record internals, node-column completeness, any test. So this is a
partial audit; "conforms" below means only what was read.

| Spec | Result | Evidence |
|---|---|---|
| B1 S1 pull: surfaces + WordNet groups, no verse-lexical | Conforms | collectiongroup._pull reads surface_network_group and surface_relation by indexed lookup; no verse read |
| B2 missing WordNet item = its own subgroup | Conforms | collectiongroup._seeds (`alone`); output is the subgroup table |
| A4/B3 per-subgroup pull, nothing read whole | **Does not conform** | layerreading.pull calls load() for every pull, even with -Subgroup: ev.build_collection reads the whole collection, and for layer 2 steps and 3.3 ev.build_pairs reads every verse_lexical row of every verse of the whole collection. Only the rows written are filtered to the subgroup. Run once per subgroup per step this is the cause of the slow runs |
| B3 full verse-lexical + verse text + existing observations (nature evidence or null) | **Does not conform** | pull shows at most pull_max_nodes=80 nodes per row, verse text cut to 200 chars, existing observations capped at 12 with text cut to 200, and the existing-observation query filters by stage (not layer-1/2/lexical), not by nature, so an older inner_being observation is included and an older one beyond 12 is not shown |
| B4 2.1 WordNet as control against verse-lexical pairings | Conforms in form | wordnet_control and control_for exist and are attached to the pairing rows of 2.1 |
| B4 "create new observations by verse"; "each subgroup surface its own observation" | **Does not conform / conflict** | config items are one observation per subgroup (qualifier, entity, direction) or per subgroup and partner collection (pairing); a pairing is required only when it spans pair_min_verses=3 verses, a threshold you never gave. The 2026-11-14 text ("each group or word") and the 2026-11-24 text ("by verse", "each subgroup surface") differ; needs your ruling |
| B5/E6 older observations: consumed then deleted, never discarded unverified | **Unverified** | the rule "an older observation is kept only as inner being" (layer.reading older_keep_natures, BUILD 568, #2555) is my reading; I recorded it as your 2026-11-24 ruling but I cannot find those words in your messages. Your 2026-11-22 words say consumed into the new observations, then deleted |
| B6 evidence validation inside the loop; E5 evidence and inner being validated separately | Conforms in form | open_step runs the evidence gate (bv.closing_gate "evidence") before 3.1; 3.3 closing gate runs "both" |
| B7 3.1: evidence observations + verse text of the subgroup | Not verified | layerinner._stage3_of_subgroup and _texts exist; not read in full |
| B9 3.2 pulls all inner-being observations of all subgroups | Not verified | layerinner._stage4_of exists |
| B10 3.3 refuses while a partner collection is open | Conforms in form | layerreading.open_step calls bv.partner_gaps; the "ask me" step is manual |
| S1 word-sense step ("words" reading of each surface, after grouping) | **Not in your 2026-11-24 sequence** | it fits your stage 1 (2026-11-15) and "lexical first" (2026-11-20), but the 2026-11-24 flow does not mention it; needs confirming |
| A8 observations created fresh, no scratch | **Did not hold in the thought run** | 3.1 and 3.2 were rebuilt from the earlier run's withdrawn findings with scratch scripts; the 98 deletions and 168 markers were applied from scratch-built sheets |
