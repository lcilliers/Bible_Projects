# #2275 Design (v2): the reading made progressive, per verse

**Date:** 2026-10-25 · **Escalation:** #2275 (from #2268) · **Status:** design for the researcher's approval. Nothing
has been built or changed.

Researcher, chat 2026-10-25 (verbatim, #2275 v11): *"… So reading and gathering data must be progressive. a) set scope
(collection of verses), check status of base data analysis (observations), of complete for base data analysis - use
observations for the lexical understanding, if not pull base data, complete observations lexical work first, then
check if the observations include characteristic analysis, if not use lexixal analysis observations to start to read
verses for all the characteristics and completion of the observations for the characteristic analysis, else if
already done use the observations, then proceed to the the claims process"*

Researcher, chat 2026-10-25 (verbatim, #2275 v13): *"q1 - if the older data is correct then use it, I hate that we
continue to start over. note that if the older data is analysed, and not in ib_observations, then the analysis done
must be added to ib_observations. q2. this question should be answered by the rules for this process, which are well
established. I am not re-inventing the wheel. (in esssence, this is where role comes in) Q3 - the previous documents
are digested, and then should go into the json, so it can be captured in the tables. Q4 - absolutely, that is why we
do not want to redo work alraedy done."*

v1 is in `outputs/escalation/archive/`. This version builds in the four rulings (§2) and adds the build (§5).

---

## 1. The process

Per verse of the scope; a verse moves on only when its layer is complete.

| Step | For each verse | Reads | Writes | Done when |
|---|---|---|---|---|
| **1. Scope (0.C)** | the verses and the objective are set; each verse's two statuses are checked from the tables | the verse set; everything already analysed about each verse (§3) | the scope JSON: the verses, each with its status in both layers and its existing analysis | — |
| **2. Lexical layer** | only where the verse's lexical layer is incomplete: its base data is pulled (§4), and the lexical work completed. Where it is complete, its observations are the lexical understanding; no base data is pulled. | the base data extract, for those verses only; the verse's existing lexical analysis | lexical findings (face, term; silence where a word carries nothing); older analysis confirmed or carried in (§2 R1) | every word in focus has its lexical finding, an open item, or a reason |
| **3. Characteristic layer** | only where the characteristic layer is incomplete: the verse is read in its passage for all its characteristics, from its lexical observations (RO6). Where it is complete, its observations are used. | the verse's lexical findings; the verse and its passage; its existing characteristic analysis | characteristic findings (qualification, party, statement, link, use); older analysis confirmed or carried in | every word in focus has its characteristic finding where it has one, an open item, or a reason |
| **4. Claims** | as built (B1: Synergy, Apply, the claims gate) | | | |
| **5. Narrate, publish** | as built (B1) | | | |

## 2. The rulings, built in

| # | Ruling | What it means for the build |
|---|---|---|
| R1 (Q1) | Older data that is correct is used; analysis done but not in ib_observation is added to it | **What the verse already has is the starting point.** The older observations on a verse (any stage) are given with it, each with its nodes. A reading that finds one correct applies it to the word, with the word's role (a node on the existing observation, `existing`), and does not write it again. One that is wrong is withdrawn with its reason (RW-01). Analysis held only in documents (§3) is written into ib_observation as findings. |
| R2 (Q2) | The words in focus come from the established rules; role is the point | The rules decide which words are read and how. RG-03: every M-coded word, and every T-code word found relevant, gets its role. RG-07: operations, movement, negators, connectives, body parts, places, objects and nature are read, and every row with them. RG-22: content words are read even without an M-code; function words get no observation of their own, except negators and connectives. RG-23 and RG-24 settle qualifiers. `cfg_setting reading.focus_words` (set in B1) is restated to these rules: every content word of the verse, M- or T-coded, with function words left out by their morph, and negators and connectives kept. Every strong has a cluster (spine check SC2, strong -> cluster), so every word in focus can carry a node. |
| R3 (Q3) | The previous documents are digested into the JSON, to be captured in the tables | Per verse, the scope JSON carries what the documents say of it: the study-file lines that name it (`reading_ref`: 51,765 lines in 235 files) and its ledger faces (`reading_strand_hit`: 4,480 hits, 4,239 with a face). The reading digests them at the layer they serve and writes them as findings. B1's separate Gather step goes. |
| R4 (Q4) | A completed layer holds for every later scope | A verse whose lexical or characteristic layer is complete is not read again at that layer, by any later scope, unless a re-read finds it wrong (RO3; B2 D6). |

## 3. A verse's status, and what it already has

**When a word counts as done.** It has a node applied by a reading (`ib_node.reading_id` set), with its role, on a live
finding of that layer's kinds:
- **lexical layer:** face, term, silence;
- **characteristic layer:** qualification, party, statement, link, use.

An older observation counts once a reading has confirmed it by such a node (R1).

**The statuses.** Per layer, a verse is:
- **complete:** every word in focus is done;
- **partial:** some are;
- **none:** none are.

The scope JSON lists the words still open in each layer.

**What the verse already has.** Given with each verse, as existing analysis:
- **every live observation on it, of any stage, with its nodes:**
  - verse-reading: the API's lexical work, 5,642 live;
  - strand-reading: the October ledgers, 773;
  - char-subgroup, char-reading and char-answers: 885;
  - the findings of earlier readings;
- **its ledger faces** (strand hits);
- **the study-file lines that name it;**
- **the claims resting on it,** and the blocks citing it;
- **the open items matching it.**

This takes in build B4 (#2276), the collation reading every observation.

## 4. The base data extract (step 2), only for verses whose lexical layer is incomplete

| Part | From |
|---|---|
| Every word of the verse in order: position, surface, lettered strong, morph, its M- and T-codes, its subgroup | `verse_lexical`, `cluster_strong`, `cluster_subgroup_strong` |
| The span behind each word | `span` |
| Each word's meaning: head gloss, meaning-tree senses, and for Greek, Mounce and the LSJ text | `strong_sense`, `strong_meaning_tree`, `strong_lexicon` |
| Each word's related words | `strong_related` (on the exact code) |
| Each word's surfaces across its other occurrences, with counts (B:110) | `verse_lexical` |
| The verse text and its passage | `verse` |

---

## 5. The build

| Part | Change |
|---|---|
| Steps | Open (0.C and the scope JSON); **Lexical** (the lexical JSON, for the verses incomplete in that layer); Record; Check (lexical gate); **Characteristic** (the characteristic JSON, for the verses incomplete there); Record; Check (characteristic gate); then Synergy, Apply, Check, Narrate, Check, Publish, Account as built. B1's Gather and Observe are replaced by Lexical and Characteristic; Record serves both. |
| States | open -> lexical -> observed -> synergised -> narrated -> published (`gathered` retired) |
| Gap types | the pre gap types become inputs in the scope JSON (R3). `term_reading_missing` and `not_read` become each layer's open words. Open items are read at the characteristic layer and settled at claims, as now. |
| Scope JSON | replaces the collation: §3 per verse, with the two statuses and the open words; built by `versecollate.collate`, extended (B4 taken in) |
| Words in focus | `reading.focus_words` restated to RG-03, RG-07, RG-22 (R2) |
| Layer of each kind | `cfg_setting reading.layer_kinds`: lexical (face, term, silence), characteristic (qualification, party, statement, link, use) |
| Method rules | already on `reading.observe`; split by layer: the base-data rules (RG-08, RG-14, RG-21, RW-05, RW-11) on `reading.lexical`, the rest on `reading.characteristic` |
| The API steps (B3) | retired as in the withdrawn B3 design §5: the five steps, their scripts, libraries and settings; what they wrote is kept, and is now given to every reading as existing analysis (R1) |
| RC-01 to RC-07 | RC-07 (every occurrence cited) is the lexical gate itself, made active on `reading.lexical`. RC-01 to RC-06 (subgrouping a cluster) have no per-verse place; they stay inactive, and subgroups stay as they are (D1 below). |

## 6. Test, on a copy (B:97)

1. The migration from the pre-run snapshot, and a re-run that writes nothing.
2. A trial scope of three verses:
   - one with older observations: confirmed by a node, not written again;
   - one with ledger faces and file lines only: written as findings;
   - one with nothing: base data pulled.
3. Only the incomplete verse gets base data; a complete verse pulls none (R4).
4. The lexical gate refuses while a word in focus has no lexical finding, item or reason. The characteristic gate does
   the same.
5. A word without an M-code but with a T-code (an operation, a connective) is in focus and takes a node (R2).
6. The claims, narrate and publish steps unchanged (the #2273 cases re-run).
7. The API steps retired; the kept lexical and cluster steps still dispatch; validate clean.

## 7. Decision for the researcher

| # | Question | Options | Decision |
|---|---|---|---|
| D1 | Subgrouping a cluster (RC-01 to RC-06) is cluster-wide and has no place in the per-verse process. Where does it go? | (a) left out of this build: RC-01 to RC-06 stay inactive, the 13 subgroups stay, and subgrouping is raised as its own item for later; (b) a cluster-scope reading writes subgroups after its characteristic layer | |

On approval of the design and D1, the build is made and tested on a copy, and the results recorded on #2275.
