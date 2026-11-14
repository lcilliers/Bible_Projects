# #2486 The objectives of the layers, and what a claim is and is not: draft v2 for discussion (2026-11-13)

Status: a draft for the researcher to correct. Not a rule, not built. Replaces v1 (`outputs/escalation/archive/2486-claim-objectives-and-definition-draft-v1-20261113.md`). It is the wording that would go into the rule set and guidance once agreed (B:31). The decisions of `outputs/escalation/2486-claim-collection-design-v2-20261113.md` wait on it.

Researcher, verbatim (2026-11-13), corrections to v1: "§4 what it is not - 'a restatement of an observation'. The issue that we currently have is that some observations have moved too far. the definitive border between an observation and a claim is as follows: an observation is about what the verse say. a claim is what the verse say about how the inner being works. going forward observations must stop short of crossing this border. Where an observation captures the verse and the verse is explicit about what in means for the inner being the claim and the observation covers the same territory. §3 a claim can be on various levels : the surface (word) ; the interaction between words (behaviour + state + entity + qualifyer, or any other combinations; accross behaviours (collections); over or above behaviours (meta). this is covered in §5, but it is not clear in §3. (this conflicts a bit with some of your statements in §4). §6 I agree the current rules are too simplistic. but if it is too convoluted, it will fall apart. the claim must decide its destination in the narrative - but not a chapter numbers, because that will change. I did some work earlier to define the entire book holistically. that is the skeleton. it almost feels as if the skeleton for the narrative must be build like a index so the claim knows exactly where it would fit in the skeleton. §7 - I agree, we should do a end to end trial build."

## 1. The objectives of the layers (unchanged from v1, from the researcher's account)

- **Collections**: the base data for behaviour and inner-being states, pulled together as related and similar words (surfaces). The verse's context tells the story. A verse holds words of different collections, some working together, some independent.
- **Observations and nodes**: the deeper analysis of every element of a verse and its operations, tied together by the nodes.
- **Claims**: look at the observations across the nodes and describe how Scripture portrays the working of the inner being.
- **Narrative**: the claims woven together, for a collection or a group of collections, in a chapter.
- **The link between a claim and its evidence is definitive**: back into the base data (claim, observations, nodes, surface, collection, verse) and forward into the narrative (claim, its place in the skeleton, the block that tells it).

## 2. The border between an observation and a claim (new)

- An **observation** is about **what the verse says**.
- A **claim** is **what the verse says about how the inner being works**.
- Going forward an observation stops short of this border: it does not interpret how the inner being works beyond what the verse says.
- Where the verse is itself explicit about what something means for the inner being, the observation and the claim cover the same territory. That is not a duplicate; each states it at its own layer, and the claim is then founded on that observation.
- Some existing observations have moved too far across the border. The claim-by-claim reading will find them: what such an observation says beyond the verse belongs to a claim, and the observation is cut back to what the verse says (soft delete or restate, with its reason, B:131).

## 3. What a claim is (revised draft test)

A claim:
1. says what the verse (or verses) say about how the inner being works, in its own plain wording;
2. is on one stated level (section 5);
3. is founded: it names the observations it uses and the nodes of those it applies, and no others;
4. makes one point; a compound is split;
5. names its destination in the narrative skeleton (section 6);
6. is held, restated or withdrawn by the researcher's verdict, not by the tool.

A claim may rest on a single observation where that observation already states what the verse says about the working of the inner being. The v1 test that a claim must go beyond any single observation is dropped.

## 4. What a claim is not (revised draft)

- a quotation or a paraphrase of a verse with no statement about how the inner being works;
- a statement of what the verse says only (that is an observation);
- a statement about a word's meaning alone (that is a meaning face or observation); a claim may speak at the level of a surface when it says what the verse shows that word doing in the inner being;
- a word grouping or a collection list;
- the narrator's framing or a chapter's conclusion (the narrative's work);
- a statement its observations do not support (held or withdrawn).

v1 excluded cross-collection and word-level statements by implication; v2 does not.

## 5. Levels of a claim (as the researcher states them)

1. **Surface**: one word (a surface) and what it shows of the working of the inner being.
2. **Interaction between words**: behaviour, state, entity, qualifier or any other combination in the verse.
3. **Across behaviours**: between behaviours, so across collections.
4. **Over or above behaviours (meta)**: how behaviours and states relate or are governed as a whole.

My earlier three (individual, inter, meta) read onto these as: individual is levels 1 and 2, inter is level 3, meta is level 4. To be confirmed. Open: whether the level is stored on the claim or read from its nodes and observations; to be found in the trial (section 7), not decided here.

## 6. The skeleton, and the claim's destination (revised, kept simple)

- The narrative's skeleton is the whole book defined holistically, as an index, so a claim knows exactly where it fits. A claim names its destination as an entry of the skeleton, by a stable key, never a chapter number; chapter numbers are produced from the skeleton and may change.
- One destination per claim as the starting rule; whether a bridging claim ever needs a second is left to the trial.
- The register's `main_chapter_id` and `main_section_id` assume a chapter home and would be replaced by the skeleton key.
- The skeleton is the four-movement story the researcher gave on 2026-11-01 under #2345 (completed, "will be used later on"); confirmed by the researcher in chat 2026-11-13 ("Yes, that one"): I what the study is; II what the inner being does, when and how; III the beings; IV purpose and the states. A draft fit to it, by concepts, which predate the collections, is `_analytics/surfaces/exports/documents/inner-being-story-fit-v2-20261101.md`. It is a story in four movements, not yet an index with keys. #2377 (assemble narration chapter scope, on hold with the researcher) is where the chapter scope and the index would naturally be assembled; I have not touched it.
- The 169 collections do not each become a chapter section (B:127 and B:129 say they do and conflict with this; named, not changed). Groupings of collections are read out of the claims and set into the skeleton, not guessed.

## 7. End-to-end trial build (agreed in principle)

Proposed, to be agreed before anything is made:
1. Choose one small area of the skeleton (a movement or part of one) and the collections that feed it.
2. Take a few verses through every layer on a copy of the database under a named snapshot (B:97), never the live database: collection, observations and nodes (cut back to the border where they cross it), claims with level and skeleton key, the skeleton entry, the block that tells them.
3. Check both directions of the evidence link, and what the skeleton index needs to hold (a key, a place, a parent) for a claim to find its place.
4. Findings go to the researcher; the rule wording, `cfg_*` rows through `apply_logged`, the guidance in `iba/app/GOVERNANCE.md` and `iba/app/USER-GUIDE.md`, the amendments of B:127 and B:129 and the revised design for the 294 claims follow from what the trial shows.
