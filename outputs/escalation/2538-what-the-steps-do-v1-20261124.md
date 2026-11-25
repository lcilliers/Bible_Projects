# What each step of the collection build does (v1, 2026-11-24)

One document for reading the build as it is now. It is written from the config (`cfg_setting layer.reading`, the method rules) and from the code (`iba/app/lib/layerreading.py`, `layerinner.py`, `buildvalidate.py`), not from the older design notes. A line that I did not verify in the code says so.

## 1. The shape of the work

A collection is read in four stages. Each stage is one or more **steps**; each step has **rows** (the aspects the data demands, kept in the ledger `collection_layer_item`); each row is answered by me with **observations** and **nodes** (a node ties an observation to one word occurrence in one verse). A step **closes** only when every row is answered and validated; the next step does not open before. For each row the routine is the same four verbs:

| Verb | What happens |
|---|---|
| `LayerOpen` | checks the gates, then derives the rows the data demands |
| `LayerPull` | writes a working file: the rows with the data I read for them |
| `LayerRecord` | I fill the file; the whole file is checked, then written in one transaction, or refused with every problem listed and nothing written |
| `LayerCheck` | re-derives from the tables what each answered row demands and marks it validated |

The validation (what used to run afterwards) is inside the record and the check: the marker, the node columns, the answer to each older observation, the text clash, and the gates (section 4).

## 2. The steps

| Stage | Step | One row is | What it asks me | Data I am given | Marker | Closes when |
|---|---|---|---|---|---|---|
| 1 words | S1 | a word (surface and lettered Strong's code) | what the word means in each verse of the collection where it stands, one observation per sense, naming the verses; a departing sense is its own observation (kind face) | every occurrence with its verse text, morph, unit and structure facts from `verse_lexical`; the dictionary entries for the code from the three meaning sources; the prompts; the older observations already on those occurrences | evidence | every word answered and validated |
| 2 grouping | (not a step of the ledger) | a surface | which subgroup of the collection it belongs to; subgroups are made by meaning | `GroupPull`: each surface with its word family, codes, a spread of its verses | n/a | every surface placed or isolated with its reason, every subgroup holding a surface |
| 3 verse-lexical | 1.1 groups | a subgroup | what the surfaces of the subgroup mean together, as the dictionary gives it | the subgroup's occurrences with verse text, the codes, older observations | evidence | every subgroup answered and validated |
| 3 | 1.2 strong-enrichment | a subgroup | what the Strong's codes of the subgroup say; checks the grouping against them | the same occurrences with a count of the codes (the text is checked against the lexicon entries of the codes; whether the pull itself shows me those entries I did not verify) | evidence | as above |
| 3 | 2.1 pairings | a subgroup with a partner collection, or a subgroup alone | the words that stand with the subgroup in its verses (partner words with side and distance, qualifiers and negators, entities, direction, relation to another subgroup, double meanings); may be recorded as none with a reason | the member occurrences and the partner words of the row with their verse text; the rows themselves come from the typed pairings of the verses that hold a member occurrence (stored position and type, nothing evaluated) | evidence | every row answered or none, validated |
| 4 inner being | 3.1 elements | a subgroup | from the stage 3 observations of the subgroup: what is done, its mode, what it is directed at, the other party, the circumstance, the chain of operations; each finding rests on named observations | the stage 3 observations of the subgroup, the earlier observations with their flags, the verses read back where needed | inner_being | every stage 3 observation of the subgroup is rested on or declared not used with its reason |
| 4 | 3.2 behaviours | the collection | which behaviours the collection shows, discovered from the 3.1 findings, each a flag finding that gathers its elements | the 3.1 observations | inner_being | every 3.1 observation gathered into a behaviour or declared not gathered; at least one behaviour or none with a reason |
| 4 | 3.3 across collections | a subgroup and a partner collection that share verses | how they work together in the shared verses; may be none | the shared verses and both sides' observations | inner_being | every row answered or none, validated; **and the whole validation of the collection passes** |

Row counts are set by the data. For thought: S1 177 word rows, 1.1 and 1.2 seven subgroups each, 2.1 132 rows, 3.1 seven, 3.2 one, 3.3 87.

Stage 5, the claims, has no step and is not decided.

## 3. The unit of the analysis: the surface, and why a collection comes first

(The researcher's framing, 2026-11-24, in chat.) The collection approach is a surface approach. A collection is a group of like surfaces; the verses are looked at for those surfaces, and the reading of a verse is focused on the selected surface and what binds with it. Other surfaces in the verse matter only where they enhance the focused surface. A verse approach would look very different: a verse holds several surfaces belonging to several collections, the surface group is immaterial, and every inner-being surface carries equal weight. The build is not that.

Consequences the researcher stated:

- A verse is not an entry point to the build, neither feasible nor correct.
- The smallest unit of entry is a **surface**, and only in a collection that has already gone through the surface subgroup creation process.
- So the first run of a collection must be the collection, because only a collection leads to the surface groups.

How the data is to be pulled for step 1 (S1) is the researcher's to formulate; it is open (section 6).

## 4. The validation inside the build

At `LayerRecord` (nothing is written if any of it fails):

1. The marker (`ib_observation.nature`) is set from the item answered (the table above), never by me.
2. Each word node carries strong, verse reference, surface, morph, role, occurrence, collection and (from step 1.1 on) subgroup. A column the data cannot give (an empty morph in the source, a surface with no subgroup placement) is left empty and the reason is written on the node; any other missing column refuses the file.
3. Every older live observation with a node on an occurrence of the row gets one answer from me in `fill.older`: keep, restate, merge, consume, delete as neither, or defer to a named collection. An unanswered one refuses the file.
4. A new observation with the same text as a live observation of the collection is refused, the other named.

At `LayerCheck`: the same tests are re-derived from the tables, so a row stays validated only while they hold.

Gates: step 3.1 opens only when the evidence layer of the collection's validation passes; step 3.3 closes only when both layers pass (evidence, then inner being). The end state of a collection: every observation in its scope is marked and fixed or deleted, every word node complete or with its reason, and every deferral owned by a named collection.

`ValidatePull`, `ValidateRecord`, `ValidateCheck` remain as the audit that must find nothing, and for a collection built before these changes.

## 5. Where the build stands (2026-11-24)

| Part | State |
|---|---|
| The marker and node columns at creation | built, applied live |
| The validation inside the build, the scan guard and four indexes | built and tested on a copy; **not applied live** |
| The read of the base data (no scan of `verse_lexical`; the layered reading reads only links, member terms and occurrences) | built; `load` takes 0.04 s where it took 3.5 s |
| A run limited to verses | built and then taken out again at the researcher's instruction; not in the code |
| The pull of the data for each step | as it was; to be formulated for S1 by the researcher |
| Live app | the working-tree code needs config that is not applied, so live `LayerRecord` and `LayerCheck` would refuse until it is |

## 6. What is open

1. **The data pull for step 1 (S1):** the researcher will formulate it. Nothing is built for it until then.
2. **Applying the config of the validation-in-build migration live,** and a review of the whole diff first. Live is out of step with the working-tree code.
3. **The thought rerun,** once the above is settled.
