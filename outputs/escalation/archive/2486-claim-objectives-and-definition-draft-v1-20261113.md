# #2486 The objectives of the layers, and what a claim is and is not: draft v1 for discussion (2026-11-13)

Status: a draft for the researcher to correct. Not a rule, not built. It is the wording that would go into the rule set and guidance once agreed (B:31). It sits beside `outputs/escalation/2486-claim-collection-design-v2-20261113.md`, whose node-level and ordering decisions wait on it.

Researcher, verbatim (2026-11-13): "chapter 10 is going to have 169 sub chapters. That is enormous. in itself we already know that there are a high level of interrelatedness between the collections and there is a high possibility that the collections will at some point group together ... these groups are unknown, and I am not sure that we are ready to guess them. this grouping and inter relatedness will flow out of the claims - when we observe how the inner being works. we therefore need to allow claims to bridge the gap without forcing claims down a collection route with the occasional cross collection elements. it is a feature, that need teasing out and exploration. the claims need to be able to differentiate between individual behaviour, inter behaviour, and meta (related behaviour) level. I also do not think we have clearly defined what a claim should be, and should not be."

## 1. The objectives of the layers (draft wording, from the researcher's account of 2026-11-13)

- **Collections**: the base data for behaviour and inner-being states, pulled together as related and similar words (surfaces). The verse's context tells the story. A verse holds words of different collections, some working together, some independent.
- **Observations and nodes**: the deeper analysis of every element of a verse and its operations, tied together by the nodes.
- **Claims**: look at the observations across the nodes and describe how Scripture portrays the working of the inner being.
- **Narrative**: the claims woven together, for a collection or a group of collections, in a chapter.
- **The link between a claim and its evidence is definitive**: back into the base data (claim, observations, nodes, surface, collection, verse) and forward into the narrative (claim, block, chapter).

## 2. A claim is not tied to a collection (new, to be confirmed)

A claim's collections are those of the nodes it applies, found by query. It is not placed in a collection. A claim may stay within one collection, or bridge several; bridging is a feature to be explored, not an exception to be forced down one collection. The groupings of collections that the narrative needs are not decided in advance: they are to be read out of the claims, from the collections the claims bridge.

## 3. What a claim is (draft test, for correction)

A claim:
1. says how the inner being works (what moves, what it acts on, what follows), in the claim's own plain wording;
2. goes beyond any single observation: a pattern, mechanism, sequence, contrast or relation across observations, nodes or verses; otherwise it is that observation;
3. is founded: it names the observations it uses and the nodes of those it applies, and no others;
4. makes one point; a compound is split;
5. is held, restated or withdrawn by the researcher's verdict, not by the tool.

## 4. What a claim is not (draft)

- a quotation or paraphrase of a verse;
- a restatement of one observation (the observation goes forward by itself);
- a statement about a word's meaning (that is a face or observation of meaning);
- a collection or a word grouping;
- a chapter's conclusion or the narrator's framing (the narrative's work);
- a statement its observations do not support (held or withdrawn).

## 5. Levels (proposed, to explore)

A claim differs by what it speaks of:
- **Individual**: one behaviour or inner-being state in one person or occurrence.
- **Inter**: behaviour or states between parties (the app already has party and link findings with a route; they are the nearest evidence).
- **Meta**: how behaviours or states relate: one leads to another, one governs or restrains another, a pattern across occurrences. Meta claims are where collections group.

Open: whether a level is stored on the claim or read from its observations (kind, route) and nodes. Not decided; it should be found in the trial below before any column is made.

## 6. Conflicts with the rules as they stand (named, not changed)

- B:127 (the narrative's chapter 10 is built by collection) and B:129 (each collection becomes a chapter, so the collection must make a coherent story) assume one chapter section per collection. The researcher's account above says the groupings are not yet known and should come from the claims. These two rules conflict with that and would need amending when the researcher confirms it.
- `cfg_table` text for `narrative_claim` ("a statement derived from sources that goes beyond their mere text") is the only current definition; the tests in section 3 would replace or extend it.
- The register's `main_chapter_id` and `main_section_id` on a claim assume one home in the narrative; with bridging claims this may need review.

## 7. Discovery proposed (read and trial, nothing written)

1. Read-only: for the claims that name observations, which collections their nodes reach and which collections come up together across claims (candidate groupings, shown to the researcher as findings, none assumed).
2. Hand trial with the researcher: three or four claims from one collection area, taken through the whole chain (observations, nodes, claim, block), tested against sections 3 to 5, to find what holds and what a level really is.
3. Then, and only then: the rule wording (a new behaviour rule for the definition and objectives, amendments to B:127 and B:129 as the researcher decides), `cfg_*` rows through `apply_logged`, guidance in `iba/app/GOVERNANCE.md` and `iba/app/USER-GUIDE.md`, and the v2 design for the 294 claims revised to match.
