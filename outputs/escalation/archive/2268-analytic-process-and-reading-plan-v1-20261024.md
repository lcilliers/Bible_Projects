# #2268 The analytic process, adjusted to rulings R1 to R3, and what is read when (v1)

**Date:** 2026-10-24 · **Escalation:** #2268 · **Status:** findings and a proposed process for your check. Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"read my feedback on R1 - R3 in rulings review v1 and take that on board.  this will allow you to make some adjustments in the 2268 files. I will then take on the remainder of the R-decisions,  after you have adjusted the analytic process and the file changes following from that.  You also need to carefully think about the reading process to optimise what is read when, and how many times the same thing is being read."*

Your feedback on R1 to R3 is in `outputs/escalation/2268-rulings-review-v1-20261024.md` and is recorded verbatim on #2268 v13. This file sets out what I take from it (§1), the analytic process it gives (§2 and §3), what is read when and how often (§4 and §5), and what changes in the other #2268 files (§6). Where I am reading your words and may have them wrong, I say so, and the question goes into R3 in the rulings review v3.

## 1. What the feedback settles

**R1: config is the home of the rules.**
- 99% of governing rules live in config.
- No operating rule is hard-coded in a script.
- No choice is left to interpretation where it can be stated as a rule.
- A file stays only where a rule cannot be stated without extended explanation, and that usually means the rule is not yet well thought through.
- A file is the authority only with a config pointer to it. The one such case you know of is the programme and inner-being definitions in the programme prose (`cfg_prose_concept`).

What follows for the #2268 files:
- The role guide, the observation-rules checklist and the three method files go into config (overlay C2, P26).
- `cfg_control_home` study_method changes.
- **A new finding:** rules hard-coded in the reading's own code, listed in §6 as C25.

**R2: B:84 is retired as it stands.**
- It held part of the truth without its context, and as a behaviour rule it must not modify or overrule the configs.
- It is replaced by proper configs. Your example: `whole_cluster_reading_start`, "prepare overview of cluster to allow for segmentation, do not read all the verses in a cluster by default".
- **Backfill** is replaced by **gathering work already done, and not re-doing it unless there is reason to believe it is incomplete or needs revision.**

**R3: repositioned.** You define reading and give the phases. Both are taken as the frame of §2 to §4:
- **Reading is digesting the content and context of data.** It is not only reading the text of a verse.
- **The data is everything the tables hold for a scope,** a scope being a collection of verses: Strong's, span, meaning, verse text, cluster assignment, derived data, and interpreted data such as observations, claims and narrative.
- **Every reading rule answers four questions:** what is read, why, what outcome is expected, and what it relates to.
- **The phases:** 0.B base data, 0.C scope, 0.GAP (before and after claims), D1 to D3 (table data only), D4 (verses in context, from observations to narration).
- You found D4, D5 and OBS misplaced in my process analysis (§2 below places them).

**A factual note (B:24).** The R3 feedback says the characteristic stages do not use the API. The registered steps `cluster.subgroup`, `cluster.reading` and `cluster.answer` do call it (`iba/app/handlers/cluster.py`, lines 224 and 371), as do `lexical.meaning` and `lexical.relational`. Whether D1 to D3, as phases, are read through the API or by Claude in a session is therefore an open point (R3c).

## 2. The analytic process, adjusted

The inventory's earlier stage map (A to G, with GAP and OBS) and the reading process's steps (N0 to N10) are replaced by this map. The changes:
- **OBS is not a stage.** It is the record (`ib_observation`, `ib_node`) that D1 to D4 write and that 0.GAP reads.
- **D5 is not a stage.** The observation enhancer is a tool on that record, and the question catalogue is the question set of D1 and D2.
- **The old E and F are part of D4,** which runs from observations to narration.

| Phase | What it is | Reads | Does not read |
|---|---|---|---|
| **0.B Base data** | outside the analytic rule set; built in the Base_data stage | – | – |
| **0.C Scope** | a collection of verses for a stated purpose; for a cluster, an overview that segments it (R2) rather than a whole-cluster reading | base data (to assess the scope: words, clusters, sizes, what exists) | verse text |
| **0.GAP pre-claims** | across all tables for the scope, at quality depth: what is there, what is expected to be there, its quality; work already done gathered; gaps written and updated in the tables; missing base data routed to its recovery process | base data, `verse_lexical`, `verse_meta`, `ib_observation`, `ib_node`, open items, claims, narrative, file index | verse text |
| **D1 Word level** | Stage 1: each word's meaning and form in its occurrences | `verse_lexical`, `ib_observation` / `ib_node` (word-level), `verse_meta` | base data tables, verse text |
| **D2 Characteristics** | clusters, cluster groups (subgroups), characteristics, open items | D1's results, cluster and subgroup tables, open items | base data tables, verse text |
| **D3 Claims and characteristics** | the claims already resting on the scope, read against the characteristics | claims, their sources, the observations they rest on | base data tables, verse text |
| **D4 Verses in context** | the only phase that reads verse text and passage: observations formed by reading each verse in its passage (the role guide); then synergy into claims; then narration | verse text and passage, with everything 0.GAP gathered and D1 to D3 produced | – |
| **0.GAP post-claims** | inside D4's claim step, from the same read: claims updated, and the gaps they close or open recorded | (the same read as D4's claims) | a second read of verse text |
| **Publish** | the touched chapters published | narrative blocks | – |
| *Across all* | open items and threads; the observation record | – | – |

**Where I may be reading you wrong:**
- **(a) The order of D1 to D3.** I have them running before D4, as table readings that prepare it.
- **(b) The scope of D3.** I read your words as "the claims and characteristics already recorded for the scope", not the retired passage method.
- **(c) Who performs D1 to D3.** Today D1 and D2 run through the API (above).

All three go to R3 in the rulings review v3.

## 3. Each phase's reading, by the four questions

| Phase | What is read | Why | Expected outcome | Related to |
|---|---|---|---|---|
| 0.C | the scope's words (`verse_lexical`, `cluster_strong`), clusters and sizes; for a cluster, its subgroups and the spread of its verses | to set a scope that can be read for its purpose without quality loss | a scope with its purpose; a cluster segmented, not read whole | the anchoring escalation; open items on the scope |
| 0.GAP pre | for each verse and word in scope: base data present (span, Strong's, meaning in three sources); `verse_lexical` complete; observations and nodes present **and up to the rules**; `verse_meta`; open items; claims and their tellings; file readings not yet in the tables | to know what is there, what should be there, and its quality; and to gather work already done | gap items written or updated, of every kind, base-data gaps routed to recovery; the gathered set (the collation) that D1 to D4 read | the gap register (R13); the spine; the recovery steps |
| D1 | each word's occurrences: meaning in three sources, surface, morph; existing word-level observations | to settle each word's meaning and form in its occurrences once, so D4 does not re-derive it | word-level observations (new, or gathered as already done) | the question catalogue (R17) |
| D2 | the scope's clusters and subgroups, characteristics, open items, D1's results | to see the characteristics the scope bears on, and how its words group | characteristic-level observations; open items matched | the clusters (anchors, not goals) |
| D3 | current claims resting on the scope, their sources and observations | to know what is already claimed, so D4 tests it rather than re-claims it | the claims D4 must confirm, adjust or withdraw | the narrative (B:77) |
| D4 observe | each verse in its passage: all its M-coded words' roles, the main operation, parties, route, faces, significances (the role guide) | the reading proper: what the inner being is doing in the verse | observations to the rules, per verse, with every significance recorded | D1 to D3's outcomes; open items |
| D4 claims (with 0.GAP post) | the scope's observations and claims (tables), in one read | to carry each observation by a claim or dispose of it, and to record what that closes or opens | claims and dispositions; gaps closed or opened | the narrative |
| D4 narrate | claims and the blocks that tell them | to tell the story from the claims | blocks rewritten | publishing |

## 4. What is read when, and how often

**Each kind of data is read in one phase for one purpose. A later phase reads what the earlier one wrote, not the source again.**

| Data | 0.C | 0.GAP pre | D1 | D2 | D3 | D4 | 0.GAP post |
|---|---|---|---|---|---|---|---|
| base data (verse, span, strong, meaning tables) | assess | quality | – | – | – | – | – |
| `verse_lexical`, cluster assignment | assess | quality | **read** | via D1 | – | via gathered set | – |
| `verse_meta` | – | quality | read | – | – | – | update |
| observations, nodes | – | quality, gather | **read, write** | **read, write** | read | **write** | read (same read as claims) |
| open items | match | quality | – | read | – | settle | update |
| claims, tellings | – | quality | – | – | **read** | **write** | read (same read) |
| narrative blocks | – | coverage | – | – | – | **write** | – |
| verse text and passage | – | – | – | – | – | **read once** | – |

**Rules this gives (candidate config rows; each follows from your feedback):**

| # | Rule | From |
|---|---|---|
| RO1 | Verse text and passage are read only in D4, once per verse per reading. | your 0.GAP and 0.D1 to D3 notes |
| RO2 | When a verse is read in D4, every M-coded word in it is given its role, and every significance is recorded with where it bears, not only those the reading's purpose asks for. A later reading with another purpose reads that record. It reads the verse again only when the record lacks what the new purpose needs. | role guide §4.0, §4.2; your "not re-doing work" |
| RO3 | Work already done is gathered, not redone, unless 0.GAP finds it incomplete or in need of revision. A re-read or re-run happens only for a recorded gap. | R2 |
| RO4 | Base data is read only in 0.C and 0.GAP pre. Missing or poor base data becomes a gap routed to its recovery process, never worked round or silently ignored. | your 0.B note |
| RO5 | 0.GAP pre reads each table once for the scope and writes the gathered set. D1 to D4 read the gathered set, not the tables again. | your 0.GAP note |
| RO6 | D1 to D3 read table data only. | your 0.D1 to D3 note |
| RO7 | 0.GAP post is done inside D4's claim step, from the same read. | your 0.GAP note |
| RO8 | A cluster is not read whole by default. 0.C prepares an overview that segments it. | R2 (`whole_cluster_reading_start`) |
| RO9 | Narration reads claims and observations from the tables. It quotes verse text from the `verse` table (quote-checked) and does not re-read the verse in context. | RO1 |

**How often the same thing is read today (measured, iba.db, 2026-10-24):**
- **Verses with several M-codes.** 24,227 verses carry M-coded words. 15,761 of them (65%) carry two or more M-clusters, and 8,579 (35%) carry three or more. Reading by cluster or strand means at least 54,025 verse readings. Reading once per verse with every word's role (RO2) means 24,227.
- **Stage 1.** It reached 718 verses, and 350 of them (49%) were read by more than one cluster run. Its re-runs left 4,953 withdrawn observations (B:68's correction by rerun).
- **Several stages on one verse.** 384 of the 3,091 verses with any observation were observed by two or more stages.
- **The reading process.** It reads verse text once, at gate 1, and its gate 2 reads the tables. That already matches RO1 and RO7. But it reads only the selected verses (no passage, overlay C3), it does not record every word's role (so RO2 cannot work), and its collation is not the full gathered set (overlay P7, C4).

## 5. What the current reading process would change to

| Today (`Reading.ps1`) | Under the adjusted process |
|---|---|
| Open: scope, collation (presence), gap JSON | 0.C (scope with purpose, segmentation) and 0.GAP pre (quality, gather, gap items in tables) |
| – | D1 to D3: table readings before any verse is read (who performs them: R3c) |
| Record (gate 1): observations in the ledger shape; strand faces; item responses | D4 observe: per verse in its passage, every word's role and every significance (RO2), to the observation rules (R15) |
| Check gate 1: an id or a 10-character reason | D4 observe's quality check (role guide §7) |
| Synergy and Apply (gate 2) | D4 claims with 0.GAP post in the same read (RO7), then D4 narrate |
| Publish (gate 3) | Publish |

## 6. What changes in the other #2268 files

- **Inventory v3:** the stage map becomes the phases of §2. D5 and OBS are folded as above, and 0.GAP is split into pre and post. B:84 is marked for retirement and replacement (R2). The rows themselves do not change.
- **Overlay v3:**
  - The N0 to N10 steps are mapped onto the phases.
  - New conflict **C25:** rules hard-coded in the reading's code, against R1 ("no operating rule should be hard coded in scripts"):
    - the gap kinds (`versecollate.py:24`, beside `reading.gap_types`);
    - `draft` as the only observation status that counts as read (`versecollate.py:82`);
    - M-codes only, `cluster_code LIKE 'M%'` (`versecollate.py:70`), which keeps the T-codes from a reading;
    - Mounce checked for Greek only (`reading.py:198`, `versecollate.py:182`);
    - the 10-character minimum for a reason or a response (`reading.py:292`, `307`);
    - the settle kinds and the read-in-part mark (`reading.py:53`, `54`);
    - the reading's stage and tag (`recordingpass.py:571`).
  - New conflict **C26:** the reading process reads verse text before any table phase (D1 to D3), against the phase order.
  - New gap **P32:** no config for the phases, their order, or what each reads (§4).
  - C1 is settled by R2. C2 is settled by R1.
- **Guide plotting v3:** each statement's step is restated as a phase.
- **Rulings review v3:**
  - R1 and R2 are recorded as decided, in your words.
  - R3 is rephrased as the questions above: (a) the phase order; (b) the scope of D3; (c) who performs D1 to D3, and whether the existing D1 and D2 outputs are gathered as done (RO3); (d) RO1 to RO9 as the reading rules.
  - R4 to R17 are restated where the phases change them: R5 and R14 (dispositions in D4 claims), R6 (B:68 under RO3), R13 (0.GAP pre and post), R15 (D1 to D4 writes) and R17 (the catalogue in D1 and D2).
