# #2275 Design (v1): the reading made progressive, per verse

**Date:** 2026-10-25 · **Escalation:** #2275 (from #2268) · **Status:** design for the researcher's review. Nothing has
been built or changed.

Researcher, chat 2026-10-25 (verbatim): *"The base data extract is incomplete, there is nothing about the
verse-lexical data, or the meaning. but I have anothing concern in relation to the timing of the extract, because if
the base data for a verse will only be required to be pulled if the observations are incomplete. So reading and
gathering data must be progressive. a) set scope (collection of verses), check status of base data analysis
(observations), of complete for base data analysis - use observations for the lexical understanding, if not pull base
data, complete observations lexical work first, then check if the observations include characteristic analysis, if
not use lexixal analysis observations to start to read verses for all the characteristics and completion of the
observations for the characteristic analysis, else if already done use the observations, then proceed to the the
claims process"*

What it replaces:
- the scope JSON as it stands (`outputs/escalation/2275-scope-json-contents-v1-20261025.md`);
- the word-based D1 of B3 design v1 (withdrawn);
- the order of Gather and Observe that B1 built (design v6 §4).

Kept from B1 and B2: the observation record (findings and their nodes), the claims step, Narrate and Publish.

---

## 1. The process

Every step is per verse of the scope. Each verse moves on only when its layer is complete.

| Step | For each verse | Reads | Writes | Done when |
|---|---|---|---|---|
| **1. Scope (0.C)** | the scope is set: its verses and its objective; then each verse's layer status is checked from the tables | the verse set; the observations applied to each verse | the scope JSON: the verses, each with its lexical status and its characteristic status (§2) | — |
| **2. Lexical layer** | only for a verse whose lexical status is incomplete: its base data is pulled (§3), and the lexical observations are completed. A verse already complete uses its lexical observations and pulls no base data. | the base data extract, for those verses only | lexical findings (face, term; silence for a word with no inner-being bearing) | every word in focus in the verse has its lexical finding, an open item, or a reason |
| **3. Characteristic layer** | only for a verse whose characteristic status is incomplete: the verse is read in its passage for all its characteristics, from its lexical observations, not the base data (RO6). A verse already complete uses its characteristic observations. | the lexical findings; the verse and its passage; the characteristic observations already there | characteristic findings (qualification, party, statement, link, use) | every M-code word in focus has its characteristic finding, an open item, or a reason |
| **4. Claims** | the claims process, from the observations of both layers (B1's Synergy and Apply, the claims gate) | observations, claims | claims, dispositions | as built (B1) |
| **5. Narrate, publish** | as built (B1) | | | |

Base data is read only at step 2, and only for the verses that need it (RO4).

## 2. A verse's layer status

Taken from the observations applied to the verse (`ib_node.verse_reference`), per word in focus:

| Status | Lexical layer | Characteristic layer |
|---|---|---|
| **complete** | every word in focus has a lexical finding applied to it in this verse | every M-code word in focus has a characteristic finding applied to it in this verse |
| **partial** | some words have one | some words have one |
| **none** | none | none |

The scope JSON gives, for each verse, its two statuses and the words still open in each layer, so the reading takes
up only what is missing.

## 3. The base data extract (step 2), for a verse that needs it

| Part | From |
|---|---|
| Every word of the verse, in order: position, surface, strong (lettered), morph, its clusters and T-code tags, its subgroup | `verse_lexical`, `cluster_strong`, `cluster_subgroup_strong` |
| The span behind each word | `span` |
| Each word's meaning: the head gloss; the meaning-tree senses; for Greek also Mounce and the LSJ text | `strong_sense`, `strong_meaning_tree`, `strong_lexicon` |
| Each word's related words | `strong_related` (on the exact code) |
| The word's surfaces across its other occurrences, with counts (B:110) | `verse_lexical` |
| The verse text and its passage | `verse` |

## 4. Decisions for the researcher

Each is a new decision (B:44). My recommendation is first.

| # | Question | Options | Decision |
|---|---|---|---|
| Q1 | Do the older observations count towards a layer being complete? There are 5,642 live verse-reading observations (the API's lexical stage, per word and verse), 773 strand-reading (the October ledgers) and 885 from the char stages. | (a) no: only findings in the new record count. The older ones are given with the verse as existing analysis, and the reading carries forward what still holds by applying them (a node) or writing them anew. (b) yes, they count as they are. | |
| Q2 | Which words are in focus for the lexical layer? | (a) every content word of the verse, M-coded, T-coded or untagged (RG-22); function words left out by their morph, negators and connectives kept; (b) as now: M-coded words, T2 qualifiers and T5 negators only | |
| Q3 | Where do the existing-analysis gaps go (a verse read only in a study file; a ledger face not in the record; an open item on the verse)? | (a) into the scope JSON, per verse, as inputs to the layer they serve: files and faces to the lexical or characteristic layer, open items read at the characteristic layer and settled at claims; (b) a gathering step of their own before step 2, as B1's Gather is now | |
| Q4 | Is a verse's lexical layer done for good once complete, for every later scope? | (a) yes: a later scope uses those observations and pulls no base data, unless a re-read finds them wrong (RO3, D6); (b) each scope checks them against its own objective | |

Once these are settled, the build replaces B1's Gather and Observe with steps 2 and 3, and B3 retires the API steps.
That design comes to you before anything is built.
